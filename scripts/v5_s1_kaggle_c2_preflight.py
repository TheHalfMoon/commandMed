#!/usr/bin/env python3
"""Private Kaggle C2 pre-model qualification; no model load or inference."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import shutil
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import v5_s1_kaggle_preflight as c1_metadata
import v5_s1_colab_qualification as existing

base = existing.base
PACKET = existing.PACKET
OUTPUT_REL = Path("artifacts/v5/development/s1-kaggle-c2-preflight")
AMENDMENT = "V5_S1_KAGGLE_RUNTIME_AMENDMENT_2026-10-08.md"
SEEDS = (11, 29, 47)
INTERVENTION = "C2_CRDI_RETAIN_V1"
RETENTION_REPO = "rajpurkar/squad"
RETENTION_REVISION = "7b6d24c440a36b6815f21b70d25016731768db1f"
RETENTION_FILE = "plain_text/validation-00000-of-00001.parquet"
RETENTION_SHA256 = "8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7"


def c2_kernel(seed):
    if type(seed) is not int or seed not in SEEDS:
        raise RuntimeError("KAGGLE_UNFROZEN_C2_SEED")
    return f"abdulazizshehri/commandmed-v5-c2-seed-{seed}-atomic"


def _verify_committed_seed(folder: Path, seed: int, intervention: str) -> dict:
    receipt_path = folder / "export-verification-receipt.json"
    review_path = folder / "validation-and-review.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    required = {
        "seed": seed,
        "intervention": intervention,
        "durable_export_verified": True,
        "ordered_medical_rows_verified": 16384,
        "model_weights_loaded": False,
        "clinical_validity": False,
        "confirmatory": False,
        "reserve": False,
        "spend_usd": 0,
    }
    if any(receipt.get(k) != v for k, v in required.items()):
        raise RuntimeError("KAGGLE_PRIOR_SEED_RECEIPT_INVALID")
    if intervention == INTERVENTION:
        if receipt.get("retention_evaluated") is not True or receipt.get("retention_rows_verified") != 256:
            raise RuntimeError("KAGGLE_PRIOR_C2_RETENTION_RECEIPT_INVALID")
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if (
        review["v5_tests"]["exit_code"] != 0
        or review["full_repository_tests"]["exit_code"] != 0
        or review["compile_exit_code"] != 0
        or review["diff_check_exit_code"] != 0
        or review["spend_usd"] != 0
        or not review["host_review"].startswith("NO_MATERIAL_BLOCKER")
    ):
        raise RuntimeError("KAGGLE_PRIOR_SEED_REVIEW_MISSING_OR_FAILED")
    archive = folder / "original-export.zip"
    runtime = folder / "commandmed-atomic-kernel-result.json"
    hardware = folder / "commandmed-physical-hardware.json"
    if base.sha256_file(archive) != receipt["archive_sha256"]:
        raise RuntimeError("KAGGLE_PRIOR_SEED_ARCHIVE_CHANGED")
    if (
        base.sha256_file(runtime) != receipt["allowlisted_runtime_sha256"]
        or base.sha256_file(hardware) != receipt["physical_hardware_sha256"]
    ):
        raise RuntimeError("KAGGLE_PRIOR_SEED_RUNTIME_RECORD_CHANGED")
    files = [receipt_path, review_path, archive, runtime, hardware]
    for row in receipt["files"]:
        member = Path(row["path"])
        if member.is_absolute() or ".." in member.parts or "\\" in row["path"] or ":" in row["path"]:
            raise RuntimeError("KAGGLE_PRIOR_SEED_UNSAFE_RECEIPT_PATH")
        evidence = folder / "evidence" / member
        if evidence.stat().st_size != row["bytes"] or base.sha256_file(evidence) != row["sha256"]:
            raise RuntimeError("KAGGLE_PRIOR_SEED_EVIDENCE_CHANGED")
        files.append(evidence)
    for evidence in files:
        relative = evidence.relative_to(base.REPO).as_posix()
        committed = subprocess.check_output(["git", "-C", str(base.REPO), "show", "HEAD:" + relative])
        if base.sha256_bytes(committed) != base.sha256_file(evidence):
            raise RuntimeError("KAGGLE_PRIOR_SEED_NOT_COMMITTED")
    return {
        "seed": seed,
        "receipt": receipt_path.relative_to(base.REPO).as_posix(),
        "receipt_sha256": base.sha256_file(receipt_path),
        "archive_sha256": receipt["archive_sha256"],
    }


def require_complete_c1_evidence() -> list[dict]:
    root = base.REPO / "artifacts/v5/development/s1-kaggle-adapters"
    chain = []
    for seed in SEEDS:
        candidates = list(root.glob(f"c1-seed-{seed}-v*-*/export-verification-receipt.json"))
        passed = []
        for path in candidates:
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("status") == "PASS_MODEL_FREE_EXPORT_VERIFICATION":
                passed.append(path.parent)
        if len(passed) != 1:
            raise RuntimeError("KAGGLE_COMPLETE_C1_CHAIN_NOT_CANONICAL")
        chain.append(_verify_committed_seed(passed[0], seed, "C1_CRDI_V1"))
    return chain


def require_prior_c2_evidence(seed: int) -> list[dict]:
    c2_kernel(seed)
    root = base.REPO / "artifacts/v5/development/s1-kaggle-c2-adapters"
    chain = []
    for previous in SEEDS:
        candidates = []
        for path in root.glob(f"c2-seed-{previous}-v*-*/export-verification-receipt.json"):
            record = json.loads(path.read_text(encoding="utf-8"))
            if record.get("status") == "PASS_MODEL_FREE_C2_EXPORT_VERIFICATION":
                candidates.append(path.parent)
        if previous == seed:
            if candidates:
                raise RuntimeError("KAGGLE_COMPLETED_C2_SEED_RERUN_FORBIDDEN")
            break
        if len(candidates) != 1:
            raise RuntimeError("KAGGLE_PRIOR_C2_SEED_NOT_CANONICALLY_VERIFIED")
        chain.append(_verify_committed_seed(candidates[0], previous, INTERVENTION))
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
        "resume": False,
        "retention_repo": RETENTION_REPO,
        "retention_revision": RETENTION_REVISION,
        "retention_file": RETENTION_FILE,
        "retention_source_sha256": RETENTION_SHA256,
    }
    if any(record.get(key) != value for key, value in required.items()):
        raise RuntimeError("KAGGLE_C2_COST_PRIVACY_GPU_OR_RETENTION_ADMISSION_BLOCKED")
    seed = record.get("seed")
    if type(seed) is not int or seed not in SEEDS:
        raise RuntimeError("KAGGLE_UNFROZEN_C2_SEED")
    if record.get("kernel_ref") != c2_kernel(seed):
        raise RuntimeError("KAGGLE_C2_KERNEL_IDENTITY_MISMATCH")
    now = time.time() if now is None else now
    observed = record.get("quota_observed_unix")
    quota = record.get("free_gpu_seconds_available")
    timeout = record.get("requested_session_timeout_seconds")
    numbers = (observed, quota, timeout, now)
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) for x in numbers):
        raise RuntimeError("KAGGLE_C2_QUOTA_OR_WINDOW_OBSERVATION_MISSING")
    age = now - observed
    if age < 0 or age > 600 or quota <= 0 or not 0 < timeout <= 43200:
        raise RuntimeError("KAGGLE_C2_QUOTA_OR_WINDOW_OBSERVATION_STALE_OR_INVALID")
    remaining = min(quota, timeout) - age
    if remaining <= 600:
        raise RuntimeError("KAGGLE_C2_ATOMIC_WINDOW_UNAVAILABLE")
    return remaining


def verify_frozen_bindings() -> dict:
    return c1_metadata.verify_frozen_bindings()


def verify_gpu_binding(torch) -> list[dict]:
    return c1_metadata.verify_gpu_binding(torch)


def acquire_retention_source(target: Path) -> dict:
    from huggingface_hub import hf_hub_download
    resolved = Path(
        hf_hub_download(
            repo_id=RETENTION_REPO,
            repo_type="dataset",
            revision=RETENTION_REVISION,
            filename=RETENTION_FILE,
        )
    )
    if base.sha256_file(resolved) != RETENTION_SHA256:
        raise RuntimeError("KAGGLE_C2_RETENTION_SOURCE_HASH_MISMATCH")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(resolved, target)
    if base.sha256_file(target) != RETENTION_SHA256:
        raise RuntimeError("KAGGLE_C2_RETENTION_SOURCE_COPY_MISMATCH")
    return {
        "repo": RETENTION_REPO,
        "revision": RETENTION_REVISION,
        "file": RETENTION_FILE,
        "sha256": RETENTION_SHA256,
        "source_payload_exported": False,
    }


def qualify(args) -> tuple[dict, Path]:
    admission = json.loads(args.admission.read_text())
    seed = admission.get("seed")
    output = base.REPO / OUTPUT_REL / f"seed-{seed}"
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "IN_PROGRESS",
        "model_loaded": False,
        "model_inference": False,
        "training": False,
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "phi": False,
        "spend_usd": 0,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
        "durable_export_verified": False,
        "intervention": INTERVENTION,
        "seed": seed,
    }

    def persist(name, value):
        base.write_json(output / name, value)

    try:
        head = base.git_text("rev-parse", "HEAD")
        if head != args.expected_head or base.git_text("status", "--porcelain", "--untracked-files=no"):
            raise RuntimeError("KAGGLE_C2_EXACT_CLEAN_HEAD_MISMATCH")
        remote = base.git_text("ls-remote", "origin", "refs/heads/research/commandmed-paper-first-principles")
        if remote.split()[0] != head:
            raise RuntimeError("KAGGLE_C2_LIVE_REMOTE_HEAD_MISMATCH")
        result.update(code_sha=head, git_tree=base.git_text("show", "-s", "--format=%T", "HEAD"))
        admission = json.loads(args.admission.read_text())
        validate_admission(admission)
        c1_chain = require_complete_c1_evidence()
        c2_chain = require_prior_c2_evidence(seed)
        frozen = verify_frozen_bindings()
        persist("frozen-bindings.json", frozen)

        import psutil
        import torch

        hardware = verify_gpu_binding(torch)
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
        torch.random.default_generator.manual_seed(11)
        torch.cuda.manual_seed(11)
        packages = {
            name: importlib.metadata.version(name)
            for name in (
                "torch",
                "transformers",
                "tokenizers",
                "peft",
                "numpy",
                "huggingface-hub",
                "safetensors",
                "psutil",
                "pyarrow",
            )
        }
        environment = {
            "python": sys.version,
            "platform": platform.platform(),
            "packages": packages,
            "cuda": torch.version.cuda,
            "runtime_dtype": "bfloat16",
            "visible_gpus": hardware,
            "scientific_gpu_count": 1,
            "scientific_device": "cuda:0",
            "native_bfloat16_support": torch.cuda.is_bf16_supported(including_emulation=False),
            "bfloat16_support": torch.cuda.is_bf16_supported(),
            "cpu_count": psutil.cpu_count(),
            "ram_total_bytes": psutil.virtual_memory().total,
            "admission": admission,
            "frozen_bindings": frozen,
            "runner_sha256": base.sha256_file(Path(__file__)),
            "complete_c1_evidence": c1_chain,
            "prior_c2_evidence": c2_chain,
        }
        persist("environment-before-imports.json", environment)

        from peft import LoraConfig, TaskType, get_peft_model  # noqa: F401
        from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: F401
        import pyarrow.parquet as parquet  # noqa: F401
        import v5_s1_retention_preparation as retention_preparation

        environment["required_imports"] = "PASS"
        environment["memory_before_load"] = existing.memory(torch)
        existing.require_headroom(environment["memory_before_load"])

        acquired = base.acquire_model(args.model_dir)
        if acquired["resolved_sha"] != base.MODEL_REVISION or acquired["private"] or acquired["gated"]:
            raise RuntimeError("KAGGLE_C2_EXACT_PUBLIC_MODEL_REVISION_MISMATCH")
        artifact, _bundle = base.bind_artifact(args.model_dir)
        artifact["files"] = existing.reproduce_frozen_file_order(artifact["files"])
        artifact["bundle_sha256"] = base.sha256_bytes(base.canonical_json(artifact["files"]))
        if artifact["bundle_sha256"] != existing.EXPECTED_BUNDLE:
            raise RuntimeError("KAGGLE_C2_MODEL_ARTIFACT_MISMATCH")
        persist("model-artifact-manifest.json", artifact)

        base.acquire_source(args.source)
        retention_binding = acquire_retention_source(args.retention_source)
        if shutil.disk_usage(args.model_dir).free < base.MIN_DISK_HEADROOM:
            raise RuntimeError("KAGGLE_C2_DISK_HEADROOM_BELOW_2_GIB")
        prep = existing.verify_preparation(args.model_dir, args.source, output)
        if (
            prep["example_count"] != 8192
            or prep["full_prompt_candidate_check_count"] != 32768
            or prep["tokenizer_candidate_ids"] != {"A": 32, "B": 33}
            or prep["answer_prefix"] != "ANSWER:\n"
            or max(prep["max_prompt_tokens_by_split"].values()) > 768
            or prep["overlength_count"]
        ):
            raise RuntimeError("KAGGLE_C2_FULL_INTERFACE_QUALIFICATION_MISMATCH")

        qa = retention_preparation.prepare(args.retention_source, args.model_dir)
        if (
            qa.get("status") != "PASS_RETENTION_METADATA_ONLY"
            or qa.get("source_repo") != RETENTION_REPO
            or qa.get("source_revision") != RETENTION_REVISION
            or qa.get("source_file") != RETENTION_FILE
            or qa.get("source_file_sha256") != RETENTION_SHA256
            or qa.get("source_count") != 10570
            or len(qa.get("roles", {}).get("S1_C2_MAINTENANCE", [])) != 64
            or len(qa.get("roles", {}).get("S1_RETENTION_EVAL", [])) != 256
            or qa.get("source_payload_exported") is not False
            or qa.get("model_loaded") is not False
            or qa.get("model_inference") is not False
            or qa.get("training") is not False
        ):
            raise RuntimeError("KAGGLE_C2_RETENTION_METADATA_QUALIFICATION_MISMATCH")
        persist("retention-preparation-preload.json", qa)
        remaining = validate_admission(admission)
        environment.update(
            model_revision=base.MODEL_REVISION,
            artifact_bundle_sha256=artifact["bundle_sha256"],
            tokenizer_files=prep["tokenizer_files"],
            preparation_sha256=base.sha256_file(output / "preparation/task-preparation-evidence.json"),
            retention_source=retention_binding,
            retention_metadata_sha256=base.sha256_bytes(base.canonical_json(qa)),
            retention_maintenance_ids_sha256=hashlib.sha256(
                base.canonical_json([r["source_id"] for r in qa["roles"]["S1_C2_MAINTENANCE"]])
            ).hexdigest(),
            retention_eval_ids_sha256=hashlib.sha256(
                base.canonical_json([r["source_id"] for r in qa["roles"]["S1_RETENTION_EVAL"]])
            ).hexdigest(),
            remaining_window_and_quota_seconds=remaining,
        )
        env_sha = base.sha256_bytes(base.canonical_json(environment))
        persist("environment-manifest.json", {**environment, "environment_sha256": env_sha})
        authority = base.DevelopmentAuthority(
            approved=True,
            authority_id="KAGGLE_AUTHORITY_SHA256:" + frozen["amendment_sha256"],
        )
        manifest = base.DevelopmentRunManifest(
            action="MODEL_LOAD",
            model_repo=base.MODEL_REPO,
            model_revision=base.MODEL_REVISION,
            model_artifact_sha256=existing.EXPECTED_BUNDLE,
            intervention_id=INTERVENTION,
            data_roles=("RULE_ORACLE_DEVELOPMENT", "RULE_ORACLE_CALIBRATION", "SQUAD_RETENTION"),
            code_sha=head,
            environment_id="sha256:" + env_sha,
            output_destination=output.relative_to(base.REPO).as_posix() + "/",
        )
        decision = base.evaluate_development_preflight(manifest, authority)
        persist(
            "preflight-model-load.json",
            {"authority": asdict(authority), "manifest": asdict(manifest), "decision": asdict(decision)},
        )
        if not decision.allowed or decision.state != "PREFLIGHT_PASS":
            raise RuntimeError("KAGGLE_C2_EXACT_RUN_PREFLIGHT_BLOCKED")
        result.update(
            status="KAGGLE_C2_PREFLIGHT_PASS",
            model_load_executed=False,
            duration_admission="NOT_REACHED_NO_MODEL_RESOURCE_MEASUREMENT",
            remaining_seconds=remaining,
            finished_at=datetime.now(timezone.utc).isoformat(),
        )
    except (Exception, SystemExit) as exc:
        result.update(status="KAGGLE_C2_PREFLIGHT_BLOCKED", exception_type=type(exc).__name__, reason=str(exc))
    persist("kaggle-preflight-result.json", result)
    return result, output


def main():
    parser = argparse.ArgumentParser()
    for name in ("model-dir", "source", "retention-source", "admission"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    args = parser.parse_args()
    result, output = qualify(args)
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
    return 0 if result["status"] == "KAGGLE_C2_PREFLIGHT_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
