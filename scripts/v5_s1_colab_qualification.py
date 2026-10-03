#!/usr/bin/env python3
"""Interactive Colab S1 resource qualification; no medical training or resume.

Run from a normal notebook cell. All model actions require fresh repository
preflight and the exact, clean reviewed checkout. Evidence is not accepted as
durable until its exported bytes are independently checked outside the VM.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import shutil
import sys
import time
import uuid
from dataclasses import asdict
from pathlib import Path

import v5_s1_resource_qualification as base

REPO = base.REPO
PACKET = REPO / "docs/research/paper-rebuild-v2-2026-10-02"
OUTPUT_REL = Path("artifacts/v5/development/s1-colab-resource-qualification")
EXPECTED_BUNDLE = "b2b4de85ad1149ad987d01e5226c83389fa974fac8d2698bac0e4bdc7e682477"
AUTHORITY_FILES = (
    "V5_DEVELOPMENT_EXECUTION_AUTHORIZATION_2026-10-03.md",
    "V5_S1_RULE_ORACLE_EXECUTION_COVERAGE_AMENDMENT_2026-10-03.md",
    "V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md",
    "V5_S1_COLAB_FREE_RUNTIME_AUTHORIZATION_SOURCE_2026-10-04.md",
    "V5_S1_EXISTING_COLAB_PRO_AUTHORIZATION_2026-10-04.md",
    "V5_S1_FREE_COLAB_SELECTION_2026-10-04.md",
    "V5_S1_DEVELOPMENT_EXECUTION_PROTOCOL_2026-10-03.md",
)


def verify_head(expected: str) -> str:
    head = base.git_text("rev-parse", "HEAD")
    if head != expected or len(expected) != 40:
        raise RuntimeError("EXACT_REVIEWED_HEAD_MISMATCH")
    changes = base.git_text("status", "--porcelain", "--untracked-files=all")
    if any(not line[3:].startswith(OUTPUT_REL.as_posix() + "/") for line in changes.splitlines()):
        raise RuntimeError("NON_EVIDENCE_CHECKOUT_CHANGE")
    return head


def validate_admission(record: dict) -> None:
    required = {
        "cost_basis": "COLAB_FREE_EXPOSED_RESOURCES",
        "ui_subscription": "NOT_SUBSCRIBED",
        "compute_unit_balance": 0,
        "expected_incremental_spend_usd": 0,
        "new_purchase": False,
        "normal_interactive_notebook": True,
    }
    if any(record.get(key) != value for key, value in required.items()):
        raise RuntimeError("COLAB_COST_OR_INTERFACE_ADMISSION_BLOCKED")
    if not isinstance(record.get("notebook_id"), str) or not record["notebook_id"]:
        raise RuntimeError("NOTEBOOK_IDENTITY_MISSING")
    lifetime = record.get("observed_remaining_runtime_seconds")
    if not isinstance(lifetime, (int, float)) or not math.isfinite(lifetime) or lifetime <= 0:
        raise RuntimeError("RUNTIME_LIFETIME_OBSERVATION_MISSING")


def reproduce_frozen_file_order(rows: list[dict]) -> list[dict]:
    """Require all exact files, then use the already-bound manifest's order.

    pathlib sorts Windows paths without case sensitivity but POSIX paths with
    case sensitivity. The historical bundle bound the Windows order. Reordering
    identical records preserves that identity; no file mismatch is admitted.
    """
    reference_path = REPO / "artifacts/v5/development/s1-resource-qualification/model-artifact-manifest.json"
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    expected_rows = reference["files"]
    if reference["bundle_sha256"] != EXPECTED_BUNDLE or base.sha256_bytes(base.canonical_json(expected_rows)) != EXPECTED_BUNDLE:
        raise RuntimeError("FROZEN_ARTIFACT_REFERENCE_MISMATCH")
    actual_map = {row["path"]: row for row in rows}
    expected_map = {row["path"]: row for row in expected_rows}
    if len(rows) != 12 or len(actual_map) != 12 or actual_map != expected_map:
        raise RuntimeError("EXACT_MODEL_FILE_CONTENT_OR_INVENTORY_MISMATCH")
    return [actual_map[row["path"]] for row in expected_rows]


def verify_preparation(model_dir: Path, source: Path, output: Path) -> dict:
    path = PACKET / "execution_tools/prepare_s1_tasks.py"
    spec = importlib.util.spec_from_file_location("colab_task_preparation", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT_DIR = output / "preparation"
    saved = sys.argv
    try:
        sys.argv = [str(path), "--model-dir", str(model_dir), "--riskcalcs-source", str(source)]
        if module.main() != 0:
            raise RuntimeError("COLAB_PREPARATION_FAILED")
    finally:
        sys.argv = saved
    actual = json.loads((module.OUT_DIR / "task-preparation-evidence.json").read_text(encoding="utf-8"))
    frozen = json.loads((REPO / "artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json").read_text(encoding="utf-8"))
    # Only generation HEAD can differ. Tokenizer packages and every scientific
    # field must reproduce, including labels, task/prompt identities and length.
    differences = [key for key in sorted(set(actual) | set(frozen)) if key != "code_sha" and actual.get(key) != frozen.get(key)]
    if differences or actual["status"] != "PASS_PRE_MODEL_INTERFACE":
        base.write_json(output / "preparation-mismatch.json", {"different_fields": differences})
        raise RuntimeError("COLAB_FROZEN_PREPARATION_MISMATCH:" + ",".join(differences))
    return actual


def memory(torch) -> dict:
    import psutil
    free, total = torch.cuda.mem_get_info()
    return {
        "ram_available_bytes": psutil.virtual_memory().available,
        "process_rss_bytes": psutil.Process().memory_info().rss,
        "gpu_free_bytes": free,
        "gpu_total_bytes": total,
        "gpu_allocated_bytes": torch.cuda.memory_allocated(),
        "gpu_reserved_bytes": torch.cuda.memory_reserved(),
        "gpu_peak_allocated_bytes": torch.cuda.max_memory_allocated(),
        "gpu_peak_reserved_bytes": torch.cuda.max_memory_reserved(),
    }


def require_headroom(observation: dict) -> None:
    if observation["ram_available_bytes"] < base.MIN_MEMORY_HEADROOM:
        raise RuntimeError("SYSTEM_MEMORY_HEADROOM_BELOW_1_5_GIB")
    if observation["gpu_free_bytes"] < base.MIN_MEMORY_HEADROOM:
        raise RuntimeError("GPU_MEMORY_HEADROOM_BELOW_1_5_GIB")


def primitive_probe(torch) -> dict:
    x = torch.ones((32, 32), dtype=torch.bfloat16, device="cuda", requires_grad=True)
    weight = torch.ones_like(x, requires_grad=True)
    out = torch.nn.functional.linear(x, weight)
    out.mean().backward()
    torch.cuda.synchronize()
    tensors = (out, x.grad, weight.grad)
    if any(tensor.dtype != torch.bfloat16 or not bool(torch.isfinite(tensor).all()) for tensor in tensors):
        raise RuntimeError("BFLOAT16_PRIMITIVE_BLOCKER")
    return {"status": "PASS_PRIMITIVE_ONLY", "dtypes": [str(t.dtype) for t in tensors], "autocast": False}


def project_workload(step_seconds: float, maximum_tokens: int, medical_forward_seconds: float | None = None) -> dict:
    # Retain the original 256-step training projection. Also expose a conservative
    # sequence-length sensitivity estimate; this is not a measured full workload.
    scale = max(1.0, (maximum_tokens / 256) ** 2)
    training_per_seed = step_seconds * 256
    # The timed synthetic step contains two forwards plus backward/optimizer.
    # Half that elapsed time is a conservative per-forward estimate at 256 tokens.
    decision_matrix_per_variant = step_seconds / 2 * 16384 * scale if medical_forward_seconds is None else medical_forward_seconds * 16384 * 1.25
    return {
        "original_256_example_seed_seconds": training_per_seed,
        "length_sensitivity_factor": scale,
        "c1_training_length_sensitivity_seconds": training_per_seed * scale,
        "c2_training_length_sensitivity_seconds": training_per_seed * scale * 2,
        "b1_feature_extraction_length_sensitivity_seconds": decision_matrix_per_variant,
        "c1_or_c2_decision_matrix_length_sensitivity_seconds": decision_matrix_per_variant,
        "medical_forward_mean_seconds": medical_forward_seconds,
        "medical_matrix_estimate_method": "HASH_SELECTED_PAIRED_PROMPT_MEAN_WITH_25_PERCENT_RESOURCE_BUFFER" if medical_forward_seconds is not None else "SYNTHETIC_LENGTH_SENSITIVITY_ONLY",
        "method": "256_TIMED_STEPS; HALF_PAIR_STEP_PER_FORWARD; QUADRATIC_LENGTH_SENSITIVITY; C2_TWO_TIMES_C1_TRAINING",
        "limitations": "B1 head fitting and SQuAD retention decoding not timed; full development remains separately gated.",
    }


def qualify(args) -> tuple[dict, Path]:
    import importlib.metadata
    import platform
    import psutil
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    head = verify_head(args.expected_head)
    admission = json.loads(args.admission.read_text(encoding="utf-8"))
    validate_admission(admission)
    output = REPO / OUTPUT_REL / str(uuid.uuid4())
    output.mkdir(parents=True)
    state = {"status": "IN_PROGRESS", "code_sha": head, "git_tree": base.git_text("rev-parse", "HEAD^{tree}"), "model_loaded": False, "model_inference": False, "optimization_executed": False, "durable_export_verified": False}
    base.write_json(output / "progress.json", state)

    def persist(name, payload):
        return base.write_json(output / name, payload)

    try:
        if not torch.cuda.is_available():
            raise RuntimeError("ASSIGNED_CUDA_ACCELERATOR_UNAVAILABLE")
        torch.set_num_threads(base.CPU_THREADS)
        torch.set_num_interop_threads(base.CPU_INTEROP_THREADS)
        torch.manual_seed(11)
        torch.cuda.manual_seed_all(11)
        torch.cuda.reset_peak_memory_stats()
        artifact, bundle = base.bind_artifact(args.model_dir)
        persist("artifact-native-order-observation.json", artifact)
        artifact["files"] = reproduce_frozen_file_order(artifact["files"])
        bundle = base.sha256_bytes(base.canonical_json(artifact["files"]))
        artifact["bundle_sha256"] = bundle
        if bundle != EXPECTED_BUNDLE or artifact["file_count"] != 12:
            raise RuntimeError("EXACT_12_FILE_BUNDLE_MISMATCH")
        persist("model-artifact-manifest.json", artifact)
        if base.sha256_file(args.source) != base.FROZEN_SOURCE_SHA256:
            raise RuntimeError("RISKCALCS_SOURCE_MISMATCH")
        if shutil.disk_usage(args.model_dir).free < base.MIN_DISK_HEADROOM:
            raise RuntimeError("DISK_HEADROOM_BELOW_2_GIB")
        authority_bindings = {name: base.sha256_file(PACKET / name) for name in AUTHORITY_FILES}
        prep = verify_preparation(args.model_dir, args.source, output)
        props = torch.cuda.get_device_properties(0)
        environment = {
            "python": sys.version, "platform": platform.platform(), "cpu": platform.processor(),
            "cpu_count": psutil.cpu_count(), "ram_total_bytes": psutil.virtual_memory().total,
            "gpu_name": props.name, "gpu_compute_capability": list(torch.cuda.get_device_capability()),
            "native_bfloat16_support": torch.cuda.is_bf16_supported(including_emulation=False),
            "bfloat16_support_including_emulation": torch.cuda.is_bf16_supported(),
            "cuda_version": torch.version.cuda, "runtime_dtype": "bfloat16",
            "torch_threads": torch.get_num_threads(), "torch_interop_threads": torch.get_num_interop_threads(),
            "packages": {name: importlib.metadata.version(name) for name in ("torch", "transformers", "tokenizers", "peft", "numpy", "huggingface-hub", "safetensors", "psutil")},
            "authority_sha256": authority_bindings, "admission": admission,
            "artifact_bundle_sha256": bundle, "tokenizer_files": prep["tokenizer_files"],
            "preparation_sha256": base.sha256_file(output / "preparation/task-preparation-evidence.json"),
            "runner_sha256": base.sha256_file(Path(__file__)),
            "memory_before_load": memory(torch), "bfloat16_primitive_probe": primitive_probe(torch),
        }
        env_sha = base.sha256_bytes(base.canonical_json(environment))
        persist("environment-manifest.json", {**environment, "environment_sha256": env_sha})
        require_headroom(environment["memory_before_load"])

        def preflight(action, intervention="BASELINE_V1", roles=("SYNTHETIC_MECHANICAL",), label=None):
            verify_head(head)
            founder = base.DevelopmentAuthority(approved=True, authority_id="COLAB_AUTHORITY_SHA256:" + base.sha256_bytes(base.canonical_json(authority_bindings)))
            manifest = base.DevelopmentRunManifest(action=action, model_repo=base.MODEL_REPO, model_revision=base.MODEL_REVISION, model_artifact_sha256=bundle, intervention_id=intervention, data_roles=roles, code_sha=head, environment_id="sha256:" + env_sha, output_destination=output.relative_to(REPO).as_posix() + "/")
            decision = base.evaluate_development_preflight(manifest, founder)
            persist("preflight-" + (label or action.lower()) + ".json", {"manifest": asdict(manifest), "authority": asdict(founder), "decision": asdict(decision)})
            if not decision.allowed or decision.state != "PREFLIGHT_PASS":
                raise RuntimeError("EXACT_RUN_PREFLIGHT_BLOCKED")
            print(action + "=PREFLIGHT_PASS", flush=True)

        preflight("MODEL_LOAD")
        started = time.perf_counter()
        sampler = base.MemorySampler()
        sampler.start()
        try:
            model = AutoModelForCausalLM.from_pretrained(args.model_dir, local_files_only=True, dtype=torch.bfloat16, low_cpu_mem_usage=True)
            state["model_loaded"] = True
            model.to("cuda").eval()
            torch.cuda.synchronize()
        finally:
            load_memory = sampler.stop()
            persist("load-observation.json", {"load_seconds": time.perf_counter() - started, **load_memory, **memory(torch), "model_loaded": state["model_loaded"]})
        if load_memory["min_system_available_bytes"] < base.MIN_MEMORY_HEADROOM:
            raise RuntimeError("MODEL_LOAD_SYSTEM_HEADROOM_BLOCKER")
        require_headroom(memory(torch))
        dtype_counts = {}
        for parameter in model.parameters():
            dtype_counts[str(parameter.dtype)] = dtype_counts.get(str(parameter.dtype), 0) + parameter.numel()
        persist("model-observation.json", {"class": type(model).__name__, "parameter_dtype_counts": dtype_counts, "parameter_count": sum(dtype_counts.values()), "device": str(next(model.parameters()).device)})
        if set(dtype_counts) != {"torch.bfloat16"}:
            raise RuntimeError("MODEL_DTYPE_CONTRACT_MISMATCH")
        tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
        a, b = prep["tokenizer_candidate_ids"]["A"], prep["tokenizer_candidate_ids"]["B"]
        preflight("INFERENCE")
        encoded = tokenizer("TASK: Mechanical label check.\nA = MATCH\nB = MISMATCH\nReturn only A or B.\nANSWER:\n", return_tensors="pt", add_special_tokens=False).to("cuda")
        started = time.perf_counter()
        with torch.no_grad():
            state["model_inference"] = True
            logits = model(**encoded, use_cache=False).logits[0, -1, [a, b]]
        torch.cuda.synchronize()
        smoke_seconds = time.perf_counter() - started
        if not bool(torch.isfinite(logits).all()):
            raise RuntimeError("NONFINITE_SMOKE_LOGITS")
        persist("smoke-inference.json", {"candidate_logits": logits.float().cpu().tolist(), "wall_seconds": smoke_seconds, "logits_dtype": str(logits.dtype), "memory": memory(torch)})
        targets = base.final_block_linear_names(model, torch)
        from peft import LoraConfig, TaskType, get_peft_model
        adapted = get_peft_model(model, LoraConfig(r=4, lora_alpha=8, lora_dropout=0.0, bias="none", target_modules=targets, task_type=TaskType.CAUSAL_LM), autocast_adapter_dtype=False)
        trainable = [(name, p) for name, p in adapted.named_parameters() if p.requires_grad]
        if not trainable or any("lora_" not in name or "layers.23." not in name or p.dtype != torch.bfloat16 for name, p in trainable):
            raise RuntimeError("FINAL_BLOCK_LORA_SCOPE_OR_DTYPE_MISMATCH")
        persist("trainable-parameters.json", {"target_modules": targets, "parameters": [{"name": name, "count": p.numel(), "dtype": str(p.dtype)} for name, p in trainable], "total": sum(p.numel() for _, p in trainable)})
        preflight("TRAINING", "C1_CRDI_V1")
        unit = tokenizer.encode(" mechanical", add_special_tokens=False)
        ids = torch.tensor([(unit * (256 // len(unit) + 1))[:256]], dtype=torch.long, device="cuda")
        optimizer = torch.optim.AdamW([p for _, p in trainable], lr=5e-4, betas=(0.9, 0.999), eps=1e-8, weight_decay=0.0)

        def step(label):
            optimizer.zero_grad(set_to_none=True)
            pair = [adapted(input_ids=ids, attention_mask=torch.ones_like(ids), use_cache=False).logits[:, -1, [a, b]].float() for _ in range(2)]
            probabilities = [torch.softmax(item, dim=-1)[0].clamp_min(1e-12) for item in pair]
            loss = torch.nn.functional.cross_entropy(pair[0], torch.tensor([0], device="cuda")) + 0.1 * base.js_divergence(torch, *probabilities)
            if not bool(torch.isfinite(loss)):
                raise RuntimeError("NONFINITE_SYNTHETIC_LOSS")
            loss.backward()
            if any(p.grad is None or not bool(torch.isfinite(p.grad).all()) for _, p in trainable):
                raise RuntimeError("NONFINITE_OR_MISSING_LORA_GRADIENT")
            torch.nn.utils.clip_grad_norm_([p for _, p in trainable], 1.0)
            optimizer.step()
            state["optimization_executed"] = True
            if any(not bool(torch.isfinite(p).all()) for _, p in trainable):
                raise RuntimeError("NONFINITE_LORA_PARAMETER_AFTER_STEP")
            torch.cuda.synchronize()
            persist(label + "-step.json", {"loss": float(loss.detach().cpu()), "memory": memory(torch), "synthetic_tokens": 256})
            require_headroom(memory(torch))

        step("warmup")
        torch.cuda.reset_peak_memory_stats()
        sampler = base.MemorySampler()
        sampler.start()
        started = time.perf_counter()
        try:
            step("timed")
        finally:
            timing = {"wall_seconds": time.perf_counter() - started, **sampler.stop(), **memory(torch)}
            persist("benchmark-timing.json", timing)
        # Protocol section 3 admits model-output-independent hash samples solely
        # for resource qualification. Measure real paired-prompt dispatch costs
        # instead of treating a quadratic sensitivity bound as measured runtime.
        rules = base.bind_selected_rules(source_bytes=args.source.read_bytes(), selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text(encoding="utf-8")))
        examples = base.materialize_development_examples(rules)
        domain = "|CommandMed-V5-S1-COLAB-RESOURCE-TIMING-v1"
        sample = sorted(examples, key=lambda example: base.sha256_bytes((example.task_id + domain).encode("ascii")))[:16]
        preflight("INFERENCE", roles=("RULE_ORACLE_DEVELOPMENT", "RULE_ORACLE_CALIBRATION"), label="medical-resource-timing")
        resource_times = []
        with adapted.disable_adapter(), torch.no_grad():
            for example in sample:
                for variant, prompt in (("canonical", example.canonical_prompt), ("transformed", example.transformed_prompt)):
                    encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda")
                    torch.cuda.synchronize()
                    started = time.perf_counter()
                    logits = adapted(**encoded, use_cache=False).logits[0, -1, [a, b]]
                    torch.cuda.synchronize()
                    if not bool(torch.isfinite(logits).all()):
                        raise RuntimeError("NONFINITE_RESOURCE_ONLY_MEDICAL_LOGITS")
                    resource_times.append({"task_id": example.task_id, "variant": variant, "tokens": encoded.input_ids.shape[1], "wall_seconds": time.perf_counter() - started, "logits_sha256": base.sha256_bytes(base.canonical_json(logits.float().cpu().tolist()))})
                    require_headroom(memory(torch))
        mean_forward = sum(row["wall_seconds"] for row in resource_times) / len(resource_times)
        persist("medical-resource-timing.json", {"scope": "RESOURCE_QUALIFICATION_ONLY; NO_SCIENTIFIC_METRIC", "selection": "FIRST_16_SHA256_TASK_ID_PLUS_DOMAIN", "domain": domain, "adapter_disabled": True, "sample": resource_times, "mean_forward_seconds": mean_forward})
        projection = project_workload(timing["wall_seconds"], max(prep["max_prompt_tokens_by_split"].values()), mean_forward)
        persist("workload-projection.json", projection)
        blockers = []
        if timing["wall_seconds"] > 180:
            blockers.append("SYNTHETIC_LORA_STEP_EXCEEDS_180_SECONDS")
        if max(projection["original_256_example_seed_seconds"], projection["c2_training_length_sensitivity_seconds"]) > 43200:
            blockers.append("PROJECTED_C1_C2_SEED_EXCEEDS_12_HOURS")
        if timing["min_system_available_bytes"] < base.MIN_MEMORY_HEADROOM:
            blockers.append("SYSTEM_HEADROOM_BELOW_1_5_GIB")
        atomic_projection = projection["c2_training_length_sensitivity_seconds"] + projection["c1_or_c2_decision_matrix_length_sensitivity_seconds"]
        if atomic_projection > admission["observed_remaining_runtime_seconds"]:
            blockers.append("COLAB_RUNTIME_DURATION_BLOCKER")
        state.update(status="RESOURCE_BLOCKED" if blockers else "RESOURCE_QUALIFICATION_MEASURED", blockers=blockers, full_development_qualified=False, full_development_gap=projection["limitations"])
    except KeyboardInterrupt:
        state.update(status="RUNTIME_INTERRUPTION", reason="INTERACTIVE_EXECUTION_INTERRUPTED")
    except (Exception, SystemExit) as exc:
        state.update(status="RESOURCE_BLOCKED", exception_type=type(exc).__name__, reason=str(exc))
    persist("progress.json", state)
    persist("resource-qualification.json", state)
    return state, output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--admission", type=Path, required=True)
    args = parser.parse_args()
    result, output = qualify(args)
    archive = shutil.make_archive(str(output), "zip", output)
    print(json.dumps({"result": result, "evidence_zip": archive, "evidence_zip_sha256": base.sha256_file(Path(archive))}, sort_keys=True), flush=True)
    return 0 if result["status"] == "RESOURCE_QUALIFICATION_MEASURED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
