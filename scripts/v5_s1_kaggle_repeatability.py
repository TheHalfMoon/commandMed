"""Private Kaggle base-only unchanged-base repeatability execution."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import math
import shutil
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

import v5_s1_b1_development as b1
import v5_s1_colab_qualification as existing
import v5_s1_kaggle_c2_preflight as c2
import v5_s1_kaggle_preflight as common

base = existing.base
OUTPUT_REL = Path("artifacts/v5/development/s1-kaggle-repeatability-runtime")
INTERVENTION = "BASELINE_V1"
REPEATS = (1, 2)
AUTH_DOC = "V5_S1_KAGGLE_REPEATABILITY_RUNTIME_AUTHORIZATION_2026-10-09.md"
METHOD_DOC = "V5_S1_REPEATABILITY_METHOD_FREEZE_2026-10-09.md"


def kernel_ref(repeat: int) -> str:
    if type(repeat) is not int or repeat not in REPEATS:
        raise RuntimeError("KAGGLE_UNFROZEN_REPEATABILITY_REPEAT")
    return f"abdulazizshehri/commandmed-v5-base-repeatability-r{repeat}"


def _single_passed_folder(root: Path, pattern: str, status: str) -> Path:
    folders = []
    for path in root.glob(pattern):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("status") == status:
            folders.append(path.parent)
    if len(folders) != 1:
        raise RuntimeError(f"EXPECTED_ONE_DURABLE_EVIDENCE_FOLDER:{pattern}:{len(folders)}")
    return folders[0]


def require_complete_c2_evidence() -> list[dict]:
    root = base.REPO / "artifacts/v5/development/s1-kaggle-c2-adapters"
    chain = []
    for seed in (11, 29, 47):
        folder = _single_passed_folder(
            root,
            f"c2-seed-{seed}-v*-*/export-verification-receipt.json",
            "PASS_MODEL_FREE_C2_EXPORT_VERIFICATION",
        )
        chain.append(c2._verify_committed_seed(folder, seed, "C2_CRDI_RETAIN_V1"))
    return chain


def _verify_committed_repeat(folder: Path, repeat: int) -> dict:
    receipt_path = folder / "export-verification-receipt.json"
    review_path = folder / "validation-and-review.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    required = {
        "status": "PASS_MODEL_FREE_REPEATABILITY_EXPORT_VERIFICATION",
        "repeat": repeat,
        "intervention": INTERVENTION,
        "durable_export_verified": True,
        "ordered_rows_verified": 16384,
        "model_weights_loaded": False,
        "confirmatory": False,
        "reserve": False,
        "spend_usd": 0,
    }
    if any(receipt.get(key) != value for key, value in required.items()):
        raise RuntimeError("PRIOR_REPEATABILITY_RECEIPT_INVALID")
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if (
        review["v5_tests"]["exit_code"] != 0
        or review["full_repository_tests"]["exit_code"] != 0
        or review["compile_exit_code"] != 0
        or review["diff_check_exit_code"] != 0
        or review["spend_usd"] != 0
        or not review["host_review"].startswith("NO_MATERIAL_BLOCKER")
    ):
        raise RuntimeError("PRIOR_REPEATABILITY_REVIEW_INVALID")
    archive = folder / "original-export.zip"
    runtime = folder / "commandmed-atomic-kernel-result.json"
    hardware = folder / "commandmed-physical-hardware.json"
    if base.sha256_file(archive) != receipt["archive_sha256"]:
        raise RuntimeError("PRIOR_REPEATABILITY_ARCHIVE_CHANGED")
    if (
        base.sha256_file(runtime) != receipt["allowlisted_runtime_sha256"]
        or base.sha256_file(hardware) != receipt["physical_hardware_sha256"]
    ):
        raise RuntimeError("PRIOR_REPEATABILITY_RUNTIME_CHANGED")
    files = [receipt_path, review_path, archive, runtime, hardware]
    for row in receipt["files"]:
        member = Path(row["path"])
        if member.is_absolute() or ".." in member.parts or "\\" in row["path"] or ":" in row["path"]:
            raise RuntimeError("PRIOR_REPEATABILITY_UNSAFE_RECEIPT_PATH")
        evidence = folder / "evidence" / member
        if evidence.stat().st_size != row["bytes"] or base.sha256_file(evidence) != row["sha256"]:
            raise RuntimeError("PRIOR_REPEATABILITY_EVIDENCE_CHANGED")
        files.append(evidence)
    for evidence in files:
        relative = evidence.relative_to(base.REPO).as_posix()
        committed = subprocess.check_output(["git", "-C", str(base.REPO), "show", "HEAD:" + relative])
        if base.sha256_bytes(committed) != base.sha256_file(evidence):
            raise RuntimeError("PRIOR_REPEATABILITY_NOT_COMMITTED")
    return {
        "repeat": repeat,
        "receipt": receipt_path.relative_to(base.REPO).as_posix(),
        "receipt_sha256": base.sha256_file(receipt_path),
        "archive_sha256": receipt["archive_sha256"],
    }


def require_prior_repeatability_evidence(repeat: int) -> list[dict]:
    kernel_ref(repeat)
    root = base.REPO / "artifacts/v5/development/s1-kaggle-repeatability-runs"
    chain = []
    for previous in REPEATS:
        candidates = []
        for path in root.glob(f"repeat-{previous}-v*-*/export-verification-receipt.json"):
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("status") == "PASS_MODEL_FREE_REPEATABILITY_EXPORT_VERIFICATION":
                candidates.append(path.parent)
        if previous == repeat:
            if candidates:
                raise RuntimeError("COMPLETED_REPEATABILITY_RERUN_FORBIDDEN")
            break
        if len(candidates) != 1:
            raise RuntimeError("PRIOR_REPEATABILITY_NOT_CANONICALLY_VERIFIED")
        chain.append(_verify_committed_repeat(candidates[0], previous))
    return chain


def validate_admission(record: dict, now: float | None = None) -> float:
    required = {
        "cost_basis": "KAGGLE_ZERO_COST_RUNTIME",
        "username": "abdulazizshehri",
        "private": True,
        "expected_incremental_spend_usd": 0,
        "new_purchase": False,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "phi": False,
        "intervention": INTERVENTION,
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "resume": False,
    }
    if any(record.get(key) != value for key, value in required.items()):
        raise RuntimeError("REPEATABILITY_COST_PRIVACY_GPU_OR_SCOPE_ADMISSION_BLOCKED")
    repeat = record.get("repeat")
    if type(repeat) is not int or repeat not in REPEATS:
        raise RuntimeError("KAGGLE_UNFROZEN_REPEATABILITY_REPEAT")
    if record.get("kernel_ref") != kernel_ref(repeat):
        raise RuntimeError("REPEATABILITY_KERNEL_IDENTITY_MISMATCH")
    now = time.time() if now is None else now
    values = (
        record.get("quota_observed_unix"),
        record.get("free_gpu_seconds_available"),
        record.get("requested_session_timeout_seconds"),
        now,
    )
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise RuntimeError("REPEATABILITY_QUOTA_OR_WINDOW_OBSERVATION_MISSING")
    observed, quota, timeout, current = values
    age = current - observed
    if age < 0 or age > 600 or quota <= 0 or not 0 < timeout <= 43200:
        raise RuntimeError("REPEATABILITY_QUOTA_OR_WINDOW_OBSERVATION_STALE_OR_INVALID")
    remaining = min(quota, timeout) - age
    if remaining <= 600:
        raise RuntimeError("REPEATABILITY_ATOMIC_WINDOW_UNAVAILABLE")
    return remaining


def _authority_bindings() -> dict[str, str]:
    packet = existing.PACKET
    files = [AUTH_DOC, METHOD_DOC, "V5_DEVELOPMENT_EXECUTION_AUTHORIZATION_2026-10-03.md"]
    result = {}
    for name in files:
        path = packet / name
        if not path.is_file():
            raise RuntimeError("REPEATABILITY_AUTHORITY_OR_METHOD_FILE_MISSING:" + name)
        result[name] = base.sha256_file(path)
    return result


def run(args):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    started = time.perf_counter()
    admission = json.loads(args.admission.read_text(encoding="utf-8"))
    repeat = admission.get("repeat")
    validate_admission(admission)
    output = base.REPO / OUTPUT_REL / f"repeat-{repeat}"
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "REPEATABILITY_IN_PROGRESS",
        "code_sha": args.expected_head,
        "intervention": INTERVENTION,
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "repeat": repeat,
        "complete_matrix": False,
        "prompt_count": 0,
        "training": False,
        "optimizer_steps": 0,
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "phi": False,
        "spend_usd": 0,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
        "durable_export_verified": False,
    }

    def persist(name, value):
        return base.write_json(output / name, value)

    try:
        head = base.git_text("rev-parse", "HEAD")
        if head != args.expected_head or base.git_text("status", "--porcelain", "--untracked-files=no"):
            raise RuntimeError("REPEATABILITY_EXACT_CLEAN_HEAD_MISMATCH")
        remote = base.git_text("ls-remote", "origin", "refs/heads/research/commandmed-paper-first-principles")
        if remote.split()[0] != head:
            raise RuntimeError("REPEATABILITY_LIVE_REMOTE_HEAD_MISMATCH")
        result["git_tree"] = base.git_text("show", "-s", "--format=%T", "HEAD")
        c2_chain = require_complete_c2_evidence()
        prior_repeats = require_prior_repeatability_evidence(repeat)
        frozen = common.verify_frozen_bindings()
        authority_bindings = _authority_bindings()
        persist("frozen-bindings.json", frozen)

        if torch.cuda.device_count() != 1 or torch.cuda.current_device() != 0:
            raise RuntimeError("REPEATABILITY_SCIENTIFIC_GPU_ISOLATION_FAILED")
        hardware = common.verify_gpu_binding(torch)
        persist(
            "hardware-manifest.json",
            {
                "visible_gpus": hardware,
                "cuda_device_count": len(hardware),
                "scientific_gpu_count": 1,
                "scientific_device": "cuda:0",
            },
        )
        torch.set_num_threads(base.CPU_THREADS)
        torch.set_num_interop_threads(base.CPU_INTEROP_THREADS)
        torch.random.default_generator.manual_seed(991)
        torch.cuda.manual_seed(991)

        packages = {
            name: importlib.metadata.version(name)
            for name in (
                "torch",
                "transformers",
                "tokenizers",
                "numpy",
                "huggingface-hub",
                "safetensors",
                "psutil",
            )
        }
        environment = {
            "python": sys.version,
            "packages": packages,
            "cuda": torch.version.cuda,
            "runtime_dtype": "bfloat16",
            "scientific_gpu_count": 1,
            "scientific_device": "cuda:0",
            "repeat_rng_seed": 991,
            "admission": admission,
            "frozen_bindings": frozen,
            "authority_sha256": authority_bindings,
            "complete_c2_evidence": c2_chain,
            "prior_repeatability_evidence": prior_repeats,
            "runner_sha256": base.sha256_file(Path(__file__)),
        }
        persist("environment-before-load.json", environment)

        acquired = base.acquire_model(args.model_dir)
        if acquired["resolved_sha"] != base.MODEL_REVISION or acquired["private"] or acquired["gated"]:
            raise RuntimeError("REPEATABILITY_EXACT_PUBLIC_MODEL_REVISION_MISMATCH")
        artifact, _ = base.bind_artifact(args.model_dir)
        artifact["files"] = existing.reproduce_frozen_file_order(artifact["files"])
        artifact["bundle_sha256"] = base.sha256_bytes(base.canonical_json(artifact["files"]))
        if artifact["bundle_sha256"] != existing.EXPECTED_BUNDLE:
            raise RuntimeError("REPEATABILITY_MODEL_ARTIFACT_MISMATCH")
        persist("model-artifact-manifest.json", artifact)
        base.acquire_source(args.source)
        prep = existing.verify_preparation(args.model_dir, args.source, output)
        if (
            prep["example_count"] != 8192
            or prep["full_prompt_candidate_check_count"] != 32768
            or prep["tokenizer_candidate_ids"] != {"A": 32, "B": 33}
            or prep["answer_prefix"] != "ANSWER:\n"
            or max(prep["max_prompt_tokens_by_split"].values()) > 768
            or prep["overlength_count"]
        ):
            raise RuntimeError("REPEATABILITY_FULL_INTERFACE_QUALIFICATION_MISMATCH")

        environment.update(
            model_revision=base.MODEL_REVISION,
            artifact_bundle_sha256=artifact["bundle_sha256"],
            tokenizer_files=prep["tokenizer_files"],
            preparation_sha256=base.sha256_file(output / "preparation/task-preparation-evidence.json"),
        )
        env_sha = base.sha256_bytes(base.canonical_json(environment))
        persist("environment-manifest.json", {**environment, "environment_sha256": env_sha})
        authority = base.DevelopmentAuthority(
            approved=True,
            authority_id="KAGGLE_REPEATABILITY_AUTHORITY_SHA256:" + authority_bindings[AUTH_DOC],
        )
        counter = 0

        def preflight(action: str, label: str):
            nonlocal counter
            if base.git_text("rev-parse", "HEAD") != args.expected_head:
                raise RuntimeError("REPEATABILITY_HEAD_CHANGED_DURING_RUN")
            manifest = base.DevelopmentRunManifest(
                action=action,
                model_repo=base.MODEL_REPO,
                model_revision=base.MODEL_REVISION,
                model_artifact_sha256=existing.EXPECTED_BUNDLE,
                intervention_id=INTERVENTION,
                data_roles=("RULE_ORACLE_DEVELOPMENT", "RULE_ORACLE_CALIBRATION"),
                code_sha=args.expected_head,
                environment_id="sha256:" + env_sha,
                output_destination=output.relative_to(base.REPO).as_posix() + "/",
            )
            decision = base.evaluate_development_preflight(manifest, authority)
            counter += 1
            persist(
                f"preflight-{counter:02d}-{label}.json",
                {"manifest": asdict(manifest), "authority": asdict(authority), "decision": asdict(decision)},
            )
            if not decision.allowed or decision.state != "PREFLIGHT_PASS":
                raise RuntimeError("REPEATABILITY_ACTION_PREFLIGHT_BLOCKED")

        preflight("MODEL_LOAD", "load")
        load_started = time.perf_counter()
        sampler = base.MemorySampler()
        sampler.start()
        try:
            model = AutoModelForCausalLM.from_pretrained(
                args.model_dir,
                local_files_only=True,
                dtype=torch.bfloat16,
                low_cpu_mem_usage=True,
            ).to("cuda:0").eval()
            torch.cuda.synchronize()
        finally:
            load_memory = sampler.stop()
            persist("load-observation.json", {"wall_seconds": time.perf_counter() - load_started, **load_memory, **existing.memory(torch)})
        if load_memory["min_system_available_bytes"] < base.MIN_MEMORY_HEADROOM:
            raise RuntimeError("REPEATABILITY_MODEL_LOAD_SYSTEM_HEADROOM_BLOCKER")
        if any(p.dtype != torch.bfloat16 or p.device != torch.device("cuda:0") for p in model.parameters()):
            raise RuntimeError("REPEATABILITY_MODEL_DTYPE_OR_DEVICE_MISMATCH")
        for parameter in model.parameters():
            parameter.requires_grad_(False)
        base_identity_before = b1.parameter_identity(model, torch)
        tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
        candidates = [prep["tokenizer_candidate_ids"]["A"], prep["tokenizer_candidate_ids"]["B"]]
        rules = base.bind_selected_rules(
            source_bytes=args.source.read_bytes(),
            selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text()),
        )
        examples = base.materialize_development_examples(rules)

        preflight("INFERENCE", "resource-timing")
        sample = examples[:16]
        timings = []
        with torch.no_grad():
            for example in sample:
                for prompt in (example.canonical_prompt, example.transformed_prompt):
                    encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda:0")
                    torch.cuda.synchronize()
                    tick = time.perf_counter()
                    logits = model(**encoded, use_cache=False).logits[0, -1, candidates]
                    torch.cuda.synchronize()
                    if not bool(torch.isfinite(logits).all()):
                        raise RuntimeError("REPEATABILITY_NONFINITE_RESOURCE_LOGITS")
                    timings.append(time.perf_counter() - tick)
        mean_forward = sum(timings) / len(timings)
        projection = mean_forward * 16384 * 1.25 + 600.0
        remaining = validate_admission(admission)
        persist(
            "duration-admission.json",
            {
                "sample_prompt_count": len(timings),
                "mean_forward_seconds": mean_forward,
                "projected_full_matrix_seconds_with_buffer": projection,
                "remaining_window_and_quota_seconds": remaining,
                "full_prompt_count": 16384,
                "buffer_multiplier": 1.25,
                "completion_export_buffer_seconds": 600,
            },
        )
        if not math.isfinite(projection) or projection >= remaining:
            raise RuntimeError("REPEATABILITY_ATOMIC_DURATION_NOT_ADMITTED")

        preflight("INFERENCE", "complete-matrix")
        rows = []
        inference_started = time.perf_counter()
        with torch.no_grad():
            for example in examples:
                for variant, prompt in (
                    ("canonical", example.canonical_prompt),
                    ("transformed", example.transformed_prompt),
                ):
                    encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to("cuda:0")
                    if encoded.input_ids.shape[1] > 768:
                        raise RuntimeError("REPEATABILITY_SEQUENCE_OVER_768_NO_TRUNCATION")
                    logits = model(**encoded, use_cache=False).logits[0, -1, candidates].float()
                    if not bool(torch.isfinite(logits).all()):
                        raise RuntimeError("REPEATABILITY_NONFINITE_MEDICAL_LOGITS")
                    rows.append(
                        {
                            "task_id": example.task_id,
                            "calculator_id": example.calculator_id,
                            "split": example.split,
                            "variant": variant,
                            "target_index": 0 if example.target_label == "A" else 1,
                            "option_a_semantic": example.option_a_semantic,
                            "prompt_sha256": base.sha256_bytes(prompt.encode()),
                            "logits": logits.cpu().tolist(),
                        }
                    )
                    if len(rows) % 128 == 0:
                        print(
                            f"REPEATABILITY_MATRIX_PROGRESS={len(rows)}/16384; "
                            f"WALL_SECONDS={time.perf_counter()-inference_started:.3f}",
                            flush=True,
                        )
        if len(rows) != 16384:
            raise RuntimeError("REPEATABILITY_INCOMPLETE_MATRIX")
        base_identity_after = b1.parameter_identity(model, torch)
        if base_identity_after != base_identity_before:
            raise RuntimeError("REPEATABILITY_BASE_PARAMETER_IDENTITY_CHANGED")
        raw_sha = persist(
            "repeatability-decision-matrix.json",
            {"complete": True, "intervention": INTERVENTION, "repeat": repeat, "rows": rows},
        )
        analysis_sha = persist("repeatability-analysis.json", b1.analyze_rows(rows))
        result.update(
            status="BASELINE_REPEAT_COMPLETE_DEVELOPMENT",
            complete_matrix=True,
            prompt_count=16384,
            raw_output_sha256=raw_sha,
            analysis_sha256=analysis_sha,
            base_parameter_identity=base_identity_before,
            wall_seconds=time.perf_counter() - started,
        )
    except (Exception, SystemExit) as exc:
        result.update(status="BASELINE_REPEATABILITY_BLOCKED", reason=str(exc), exception_type=type(exc).__name__)
    persist("repeatability-result.json", result)
    return result, output


def main() -> int:
    parser = argparse.ArgumentParser()
    for name in ("model-dir", "source", "admission"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    args = parser.parse_args()
    result, output = run(args)
    archive = Path(shutil.make_archive(str(output), "zip", output))
    print(
        json.dumps(
            {
                "result": result,
                "evidence_zip": str(archive),
                "evidence_zip_sha256": base.sha256_file(archive),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return 0 if result["status"] == "BASELINE_REPEAT_COMPLETE_DEVELOPMENT" else 2


if __name__ == "__main__":
    raise SystemExit(main())
