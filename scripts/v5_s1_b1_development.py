#!/usr/bin/env python3
"""Complete bounded baseline/B1 development stage in one interactive Colab run.

No checkpoint/resume. A complete 8192-task paired matrix is required; resource
samples never qualify as scientific matrices. No SQuAD/model-retention call.
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import shutil
import time
from dataclasses import asdict
from pathlib import Path

import v5_s1_colab_qualification as colab

base = colab.base
SEEDS = (11, 29, 47)
EPOCHS = 40
BATCH_SIZE = 32


def choose_epoch(history: list[float]) -> int:
    if not history or any(not math.isfinite(value) for value in history):
        raise ValueError("B1_NONFINITE_OR_MISSING_CAL_TUNE_NLL")
    return min(range(len(history)), key=lambda index: (history[index], index)) + 1


def require_duration(projected: float, available: float) -> None:
    if not math.isfinite(projected) or projected <= 0 or not math.isfinite(available) or projected + 300 > available:
        raise RuntimeError("COLAB_RUNTIME_DURATION_BLOCKER")


def tensor_sha(tensor, torch) -> str:
    return base.sha256_bytes(tensor.detach().contiguous().cpu().view(torch.uint8).numpy().tobytes())


def parameter_identity(module, torch) -> str:
    return base.sha256_bytes(base.canonical_json([
        {"name": name, "shape": list(param.shape), "dtype": str(param.dtype), "sha256": tensor_sha(param, torch)}
        for name, param in module.named_parameters()
    ]))


def nll(torch, logits, targets):
    probabilities = torch.softmax(logits.float(), dim=-1)
    return -torch.log(probabilities.gather(1, targets[:, None]).clamp_min(1e-15)).mean()


def fit_head(torch, features, targets, calibration_features, calibration_targets, seed: int):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    head = torch.nn.Linear(features.shape[1], 2, bias=True, dtype=torch.bfloat16, device="cuda")
    optimizer = torch.optim.AdamW(head.parameters(), lr=1e-2, weight_decay=1e-4)
    generator = torch.Generator().manual_seed(seed)
    history, best_state, best_nll = [], None, math.inf
    started = time.perf_counter()
    for epoch in range(1, EPOCHS + 1):
        head.train()
        permutation = torch.randperm(len(features), generator=generator)
        for offset in range(0, len(features), BATCH_SIZE):
            positions = permutation[offset:offset+BATCH_SIZE]
            optimizer.zero_grad(set_to_none=True)
            logits = head(features[positions].to("cuda"))
            loss = nll(torch, logits, targets[positions].to("cuda"))
            if not bool(torch.isfinite(loss)):
                raise RuntimeError("B1_NONFINITE_TRAINING_LOSS")
            loss.backward()
            if any(p.grad is None or p.grad.dtype != torch.bfloat16 or not bool(torch.isfinite(p.grad).all()) for p in head.parameters()):
                raise RuntimeError("B1_GRADIENT_CONTRACT_FAILURE")
            optimizer.step()
            if any(p.dtype != torch.bfloat16 or not bool(torch.isfinite(p).all()) for p in head.parameters()):
                raise RuntimeError("B1_PARAMETER_CONTRACT_FAILURE")
        head.eval()
        with torch.no_grad():
            value = float(nll(torch, head(calibration_features.to("cuda")), calibration_targets.to("cuda")).cpu())
        if not math.isfinite(value):
            raise RuntimeError("B1_NONFINITE_CAL_TUNE_NLL")
        history.append(value)
        if value < best_nll:
            best_nll = value
            best_state = {name: tensor.detach().clone() for name, tensor in head.state_dict().items()}
        colab.require_headroom(colab.memory(torch))
    selected = choose_epoch(history)
    if best_state is None or history[selected-1] != best_nll:
        raise RuntimeError("B1_CHECKPOINT_SELECTION_CONTRACT_FAILURE")
    head.load_state_dict(best_state)
    torch.cuda.synchronize()
    record = {
        "seed": seed, "epochs": EPOCHS, "optimizer_steps": EPOCHS * (len(features)//BATCH_SIZE),
        "selected_epoch": selected, "cal_tune_nll_by_epoch": history,
        "selection_rule": "LOWEST_CANONICAL_CAL_TUNE_NLL; EARLIEST_EXACT_TIE",
        "trainable_parameters": sum(p.numel() for p in head.parameters()), "dtype": "bfloat16",
        "linear_bias": True, "classes": ["A", "B"], "head_parameter_sha256": parameter_identity(head, torch),
        "training_feature_sha256": tensor_sha(features, torch), "training_target_sha256": tensor_sha(targets, torch),
        "cal_tune_feature_sha256": tensor_sha(calibration_features, torch), "cal_tune_target_sha256": tensor_sha(calibration_targets, torch),
        "wall_seconds": time.perf_counter()-started,
        "optimizer": {"name": "AdamW", "lr": 1e-2, "weight_decay": 1e-4, "batch_size": 32, "betas": optimizer.defaults["betas"], "eps": optimizer.defaults["eps"]},
    }
    return head, record


def analyze_rows(rows: list[dict]) -> dict:
    from commandmed.reliability_v5.objectives import jensen_shannon_divergence
    from commandmed.reliability_v5.probability import softmax, negative_log_likelihood, multiclass_brier
    from statistics import fmean
    partitions = {}
    for split in sorted({row["split"] for row in rows}):
        for variant in ("canonical", "transformed"):
            selected = [row for row in rows if row["split"] == split and row["variant"] == variant]
            if not selected:
                raise RuntimeError("INCOMPLETE_MEDICAL_MATRIX")
            probabilities = [softmax(row["logits"]) for row in selected]
            partitions[split+"/"+variant] = {
                "count": len(selected),
                "accuracy": fmean(float(max(range(2), key=lambda i:p[i]) == row["target_index"]) for row, p in zip(selected, probabilities)),
                "nll": fmean(negative_log_likelihood(p, row["target_index"]) for row, p in zip(selected, probabilities)),
                "brier": fmean(multiclass_brier(p, row["target_index"]) for row, p in zip(selected, probabilities)),
            }
    by_id = {}
    for row in rows:
        by_id.setdefault(row["task_id"], {})[row["variant"]] = row
    if len(by_id) != 8192 or len(rows) != 16384 or any(set(pair) != {"canonical", "transformed"} for pair in by_id.values()):
        raise RuntimeError("INCOMPLETE_MEDICAL_MATRIX")
    js_by_split = {}
    for pair in by_id.values():
        left, right = pair["canonical"], pair["transformed"]
        p, q = softmax(left["logits"]), softmax(right["logits"])
        # The identical A/B semantic mapping within a pair makes JS invariant
        # to exchanging both components; explicitly bind that mapping in rows.
        js_by_split.setdefault(left["split"], []).append(jensen_shannon_divergence(p, q))
    return {"scope": "DEVELOPMENT_CALIBRATION_ONLY", "partitions": partitions,
            "mean_semantic_js_by_split": {split: fmean(values) for split, values in js_by_split.items()},
            "not_confirmatory": True, "clinical_validity": False}


def run(args):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    started = time.perf_counter()
    admission = json.loads(args.admission.read_text())
    colab.validate_admission(admission)
    # Repeat all exact artifact/interface, smoke, LoRA and resource gates at
    # this new reviewed head before the separately admitted complete B1 stage.
    resource, output = colab.qualify(args)
    if resource["status"] != "RESOURCE_QUALIFICATION_MEASURED":
        return resource, output
    gc.collect()
    torch.cuda.empty_cache()
    scientific = {"status": "IN_PROGRESS", "code_sha": args.expected_head, "complete_matrix": False,
                  "medical_training": False, "retention_execution": False, "durable_export_verified": False}
    base.write_json(output / "b1-progress.json", scientific)
    raw_rows = []
    stage_sampler = base.MemorySampler()
    stage_sampler.start()
    try:
        previous_env = json.loads((output / "environment-manifest.json").read_text())
        environment = {"resource_environment_sha256": previous_env["environment_sha256"],
                       "runner_sha256": base.sha256_file(Path(__file__)), "config": {"seeds": SEEDS, "epochs": EPOCHS, "batch_size": BATCH_SIZE},
                       "admission": admission}
        env_sha = base.sha256_bytes(base.canonical_json(environment))
        base.write_json(output / "b1-environment.json", {**environment, "environment_sha256": env_sha})
        counter = 0

        def preflight(action, intervention, label):
            nonlocal counter
            colab.verify_head(args.expected_head)
            authority = base.DevelopmentAuthority(approved=True, authority_id="COLAB_AUTHORITY_SHA256:"+base.sha256_bytes(base.canonical_json(previous_env["authority_sha256"])))
            manifest = base.DevelopmentRunManifest(action=action, model_repo=base.MODEL_REPO, model_revision=base.MODEL_REVISION,
                model_artifact_sha256=colab.EXPECTED_BUNDLE, intervention_id=intervention,
                data_roles=("SYNTHETIC_MECHANICAL",) if label.startswith("resource") else ("RULE_ORACLE_DEVELOPMENT", "RULE_ORACLE_CALIBRATION"),
                code_sha=args.expected_head, environment_id="sha256:"+env_sha, output_destination=output.relative_to(base.REPO).as_posix()+"/")
            decision = base.evaluate_development_preflight(manifest, authority)
            counter += 1
            base.write_json(output / f"b1-preflight-{counter:02d}-{label}.json", {"manifest": asdict(manifest), "authority": asdict(authority), "decision": asdict(decision)})
            if not decision.allowed or decision.state != "PREFLIGHT_PASS":
                raise RuntimeError("B1_EXACT_RUN_PREFLIGHT_BLOCKED")
            print(label+"=PREFLIGHT_PASS", flush=True)

        preflight("MODEL_LOAD", "BASELINE_V1", "load")
        sampler = base.MemorySampler()
        sampler.start()
        load_started = time.perf_counter()
        try:
            model = AutoModelForCausalLM.from_pretrained(args.model_dir, local_files_only=True, dtype=torch.bfloat16, low_cpu_mem_usage=True).to("cuda").eval()
            torch.cuda.synchronize()
        finally:
            load_memory = sampler.stop()
            base.write_json(output / "b1-load-observation.json", {"wall_seconds": time.perf_counter()-load_started, **load_memory, **colab.memory(torch)})
        if load_memory["min_system_available_bytes"] < base.MIN_MEMORY_HEADROOM:
            raise RuntimeError("B1_MODEL_LOAD_SYSTEM_HEADROOM_BLOCKER")
        for param in model.parameters():
            if param.dtype != torch.bfloat16:
                raise RuntimeError("B1_BASE_DTYPE_MISMATCH")
            param.requires_grad_(False)
        base_identity = parameter_identity(model, torch)
        tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
        prep = json.loads((output / "preparation/task-preparation-evidence.json").read_text())
        candidates = [prep["tokenizer_candidate_ids"][label] for label in ("A", "B")]
        rules = base.bind_selected_rules(source_bytes=args.source.read_bytes(), selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text()))
        examples = base.materialize_development_examples(rules)
        trainable_backbone_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
        if trainable_backbone_count != 0:
            raise RuntimeError("B1_BACKBONE_NOT_FROZEN")
        preflight("INFERENCE", "BASELINE_V1", "resource-representation")
        mechanical = tokenizer("TASK: Mechanical label check.\nA = MATCH\nB = MISMATCH\nReturn only A or B.\nANSWER:\n", return_tensors="pt", add_special_tokens=False).to("cuda")
        with torch.no_grad():
            mechanical_output = model(**mechanical, use_cache=False, output_hidden_states=True)
            mechanical_hidden = mechanical_output.hidden_states[-1][0, -1, :]
            if mechanical_hidden.dtype != torch.bfloat16 or not bool(torch.isfinite(mechanical_hidden).all()):
                raise RuntimeError("B1_MECHANICAL_REPRESENTATION_CONTRACT_FAILURE")
            hidden_width = mechanical_hidden.numel()
            base.write_json(output / "b1-mechanical-representation.json", {"hidden_width": hidden_width, "dtype": str(mechanical_hidden.dtype), "sha256": tensor_sha(mechanical_hidden, torch), "scope": "SYNTHETIC_MECHANICAL_ONLY"})
        del mechanical, mechanical_output, mechanical_hidden
        preflight("TRAINING", "B1_TYPED_V1", "resource-head")
        fixture = torch.randn((256, hidden_width), dtype=torch.bfloat16, device="cpu", generator=torch.Generator().manual_seed(11))
        fixture_targets = torch.arange(256, dtype=torch.long) % 2
        resource_head, head_timing = fit_head(torch, fixture, fixture_targets, fixture, fixture_targets, 11)
        del resource_head, fixture, fixture_targets
        base.write_json(output / "b1-head-resource-timing.json", {"scope": "SYNTHETIC_MECHANICAL_RESOURCE_ONLY", **head_timing})
        projection = json.loads((output / "workload-projection.json").read_text())
        available = admission["observed_remaining_runtime_seconds"] - (time.perf_counter()-started)
        projected_stage = projection["b1_feature_extraction_length_sensitivity_seconds"] + 3*head_timing["wall_seconds"]*1.25 + 300
        base.write_json(output / "b1-stage-duration-admission.json", {"projected_seconds": projected_stage, "available_seconds": available, "all_8192_tasks": True, "seeds": SEEDS, "resume": False})
        require_duration(projected_stage, available)
        preflight("INFERENCE", "BASELINE_V1", "complete-base-matrix")
        features, row_index = [], {}
        inference_started = time.perf_counter()
        with torch.no_grad():
            for example in examples:
                for variant, prompt in (("canonical", example.canonical_prompt), ("transformed", example.transformed_prompt)):
                    encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")
                    if encoded.input_ids.shape[1] > 768:
                        raise RuntimeError("B1_MEDICAL_SEQUENCE_OVER_768_NO_TRUNCATION")
                    result = model(**encoded, use_cache=False, output_hidden_states=True)
                    logits = result.logits[0, -1, candidates]
                    hidden = result.hidden_states[-1][0, -1, :].detach().cpu()
                    if hidden.dtype != torch.bfloat16 or not bool(torch.isfinite(hidden).all()) or not bool(torch.isfinite(logits).all()):
                        raise RuntimeError("B1_NONFINITE_OR_DTYPE_FEATURE_FAILURE")
                    row_index[(example.task_id, variant)] = len(features)
                    features.append(hidden)
                    raw_rows.append({"task_id": example.task_id, "calculator_id": example.calculator_id, "split": example.split, "variant": variant,
                        "target_index": 0 if example.target_label == "A" else 1, "option_a_semantic": example.option_a_semantic,
                        "prompt_sha256": base.sha256_bytes(prompt.encode()), "feature_sha256": tensor_sha(hidden, torch), "logits": logits.float().cpu().tolist()})
                    del result, hidden, logits, encoded
                    colab.require_headroom(colab.memory(torch))
                    if len(raw_rows) % 128 == 0:
                        elapsed = time.perf_counter()-inference_started
                        print(f"COMPLETE_BASE_MATRIX_PROGRESS={len(raw_rows)}/16384; WALL_SECONDS={elapsed:.3f}", flush=True)
                        remaining = admission["observed_remaining_runtime_seconds"]-(time.perf_counter()-started)
                        if len(raw_rows) < 16384:
                            require_duration((16384-len(raw_rows))*elapsed/len(raw_rows)*1.25 + 3*head_timing["wall_seconds"]*1.25, remaining)
        feature_matrix = torch.stack(features)
        del features
        base.write_json(output / "baseline-decision-matrix.json", {"complete": True, "intervention": "BASELINE_V1", "rows": raw_rows})
        base.write_json(output / "baseline-analysis.json", analyze_rows(raw_rows))
        by_split = {split: [row_index[(example.task_id, "canonical")] for example in examples if example.split == split] for split in ("S1_TRAIN", "S1_CAL_TUNE")}
        if len(by_split["S1_TRAIN"]) != 256 or len(by_split["S1_CAL_TUNE"]) != 256:
            raise RuntimeError("B1_TRAIN_OR_CAL_IDENTITY_COUNT_MISMATCH")
        targets = torch.tensor([row["target_index"] for row in raw_rows], dtype=torch.long)
        fitting = []
        for seed in SEEDS:
            preflight("TRAINING", "B1_TYPED_V1", "fit-seed-"+str(seed))
            scientific["medical_training"] = True
            base.write_json(output / "b1-progress.json", scientific)
            head, record = fit_head(torch, feature_matrix[by_split["S1_TRAIN"]], targets[by_split["S1_TRAIN"]],
                                    feature_matrix[by_split["S1_CAL_TUNE"]], targets[by_split["S1_CAL_TUNE"]], seed)
            base.write_json(output / f"b1-fit-seed-{seed}.json", record)
            fitting.append(record)
            preflight("INFERENCE", "B1_TYPED_V1", "complete-head-matrix-seed-"+str(seed))
            rows = []
            with torch.no_grad():
                for offset in range(0, len(feature_matrix), BATCH_SIZE):
                    logits = head(feature_matrix[offset:offset+BATCH_SIZE].to("cuda"))
                    if logits.dtype != torch.bfloat16 or not bool(torch.isfinite(logits).all()):
                        raise RuntimeError("B1_HEAD_INFERENCE_CONTRACT_FAILURE")
                    for parent, values in zip(raw_rows[offset:offset+BATCH_SIZE], logits.float().cpu().tolist()):
                        rows.append({**parent, "logits": values})
            base.write_json(output / f"b1-seed-{seed}-decision-matrix.json", {"complete": True, "intervention": "B1_TYPED_V1", "seed": seed, "rows": rows})
            base.write_json(output / f"b1-seed-{seed}-analysis.json", analyze_rows(rows))
            del head, rows
            print(f"B1_SEED_COMPLETE={seed}", flush=True)
        after_identity = parameter_identity(model, torch)
        if after_identity != base_identity or any(p.requires_grad for p in model.parameters()):
            raise RuntimeError("B1_BASE_BACKBONE_CHANGED")
        scientific.update(status="B1_COMPLETE_DEVELOPMENT", complete_matrix=True, baseline_prompt_count=len(raw_rows),
            seed_count=len(fitting), seeds=SEEDS, base_parameter_identity_before=base_identity,
            base_parameter_identity_after=after_identity, raw_feature_matrix_sha256=tensor_sha(feature_matrix, torch),
            stage_wall_seconds=time.perf_counter()-started, memory=colab.memory(torch),
            c1_c2_executed=False, confirmatory=False, reserve=False, spend_usd=0)
    except KeyboardInterrupt:
        scientific.update(status="RUNTIME_INTERRUPTION", reason="INTERACTIVE_EXECUTION_INTERRUPTED")
    except (Exception, SystemExit) as exc:
        scientific.update(status="B1_STAGE_BLOCKED", reason=str(exc), exception_type=type(exc).__name__)
    finally:
        sampled_memory = stage_sampler.stop()
        scientific["stage_memory_sampling"] = sampled_memory
        if sampled_memory["min_system_available_bytes"] < base.MIN_MEMORY_HEADROOM:
            scientific.update(status="B1_STAGE_BLOCKED", reason="SYSTEM_HEADROOM_BELOW_1_5_GIB")
    if scientific["status"] != "B1_COMPLETE_DEVELOPMENT" and raw_rows:
        base.write_json(output / "incomplete-baseline-decision-matrix.json", {"complete": False, "rows": raw_rows})
    base.write_json(output / "b1-progress.json", scientific)
    base.write_json(output / "b1-stage-result.json", scientific)
    return scientific, output


def main():
    parser = argparse.ArgumentParser()
    for name in ("model-dir", "source", "admission"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    args = parser.parse_args()
    result, output = run(args)
    archive = shutil.make_archive(str(output), "zip", output)
    print(json.dumps({"result": result, "evidence_zip": archive, "evidence_zip_sha256": base.sha256_file(Path(archive))}, sort_keys=True), flush=True)
    return 0 if result["status"] == "B1_COMPLETE_DEVELOPMENT" else 2


if __name__ == "__main__":
    raise SystemExit(main())
