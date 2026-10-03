#!/usr/bin/env python3
"""Fail-closed local smoke runner for the authorized CommandMed V5 S1 grain."""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib.metadata
import json
import os
import platform
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.preflight import (  # noqa: E402
    DevelopmentAuthority,
    DevelopmentRunManifest,
    evaluate_development_preflight,
)

MODEL_REPO = "Qwen/Qwen3.5-0.8B-Base"
MODEL_REVISION = "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"
AUTH_PATH = ROOT / "docs/research/paper-rebuild-v2-2026-10-02/V5_DEVELOPMENT_EXECUTION_AUTHORIZATION_2026-10-03.md"
OUTPUT_REL = "artifacts/v5/development/s1_runtime_smoke/"
REQUIRED_MODEL_FILES = (
    "config.json",
    "merges.txt",
    "model.safetensors-00001-of-00001.safetensors",
    "model.safetensors.index.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "vocab.json",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def write_json(path: Path, value: object) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return sha256_file(path)


def model_artifact_manifest(model_dir: Path) -> dict[str, object]:
    if not model_dir.is_dir():
        raise SystemExit("MODEL_ARTIFACT_DIR_MISSING")
    rows: list[dict[str, object]] = []
    for name in REQUIRED_MODEL_FILES:
        path = model_dir / name
        if not path.is_file():
            raise SystemExit(f"MODEL_ARTIFACT_FILE_MISSING={name}")
        rows.append({"path": name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    payload: dict[str, object] = {
        "schema": "commandmed.v5.s1.model-artifact.v1",
        "model_repo": MODEL_REPO,
        "model_revision": MODEL_REVISION,
        "files": rows,
    }
    payload["bundle_sha256"] = canonical_sha256(payload)
    return payload


def windows_memory() -> dict[str, int]:
    if os.name != "nt":
        return {}

    class MemoryStatus(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
        ]

    status = MemoryStatus()
    status.dwLength = ctypes.sizeof(MemoryStatus)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        raise OSError("GlobalMemoryStatusEx failed")
    return {
        "total_physical_bytes": int(status.ullTotalPhys),
        "available_physical_bytes": int(status.ullAvailPhys),
        "memory_load_percent": int(status.dwMemoryLoad),
    }


def environment_manifest() -> dict[str, object]:
    packages = {
        name: importlib.metadata.version(name)
        for name in ("numpy", "safetensors", "tokenizers", "torch", "transformers")
    }
    disk = shutil.disk_usage(ROOT.drive + "\\")
    payload: dict[str, object] = {
        "schema": "commandmed.v5.s1.environment.v1",
        "python": sys.version,
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "logical_cpu_count": os.cpu_count(),
        "memory": windows_memory(),
        "disk": {"total_bytes": disk.total, "free_bytes": disk.free},
        "packages": packages,
        "paid_resource": False,
        "expected_spend_usd": 0.0,
    }
    payload["environment_sha256"] = canonical_sha256(payload)
    return payload


def authority() -> DevelopmentAuthority:
    if not AUTH_PATH.is_file():
        raise SystemExit("AUTHORIZATION_RECORD_MISSING")
    return DevelopmentAuthority(
        approved=True,
        authority_id=f"{AUTH_PATH.relative_to(ROOT).as_posix()}@sha256:{sha256_file(AUTH_PATH)}",
        paid_compute=False,
        paid_api=False,
        spend_usd=0.0,
        phi_allowed=False,
        gated_data_allowed=False,
        confirmatory_allowed=False,
        reserve_allowed=False,
    )


def preflight(*, code_sha: str, action: str, artifact_sha: str, environment_sha: str) -> dict[str, object]:
    manifest = DevelopmentRunManifest(
        action=action,
        model_repo=MODEL_REPO,
        model_revision=MODEL_REVISION,
        model_artifact_sha256=artifact_sha,
        intervention_id="BASELINE_V1",
        data_roles=("SYNTHETIC_MECHANICAL",),
        code_sha=code_sha,
        environment_id=f"sha256:{environment_sha}",
        output_destination=OUTPUT_REL,
        confirmatory_materialized=False,
        reserve_materialized=False,
        contains_phi=False,
        uses_gated_data=False,
        paid_resource=False,
        expected_spend_usd=0.0,
    )
    founder = authority()
    decision = evaluate_development_preflight(manifest, founder)
    return {
        "action": action,
        "manifest": {
            "model_repo": manifest.model_repo,
            "model_revision": manifest.model_revision,
            "model_artifact_sha256": manifest.model_artifact_sha256,
            "intervention_id": manifest.intervention_id,
            "data_roles": list(manifest.data_roles),
            "code_sha": manifest.code_sha,
            "environment_id": manifest.environment_id,
            "output_destination": manifest.output_destination,
            "confirmatory_materialized": manifest.confirmatory_materialized,
            "reserve_materialized": manifest.reserve_materialized,
            "contains_phi": manifest.contains_phi,
            "uses_gated_data": manifest.uses_gated_data,
            "paid_resource": manifest.paid_resource,
            "expected_spend_usd": manifest.expected_spend_usd,
        },
        "authority_id": founder.authority_id,
        "decision": {
            "allowed": decision.allowed,
            "state": decision.state,
            "reason_codes": list(decision.reason_codes),
        },
    }


def candidate_suffix_id(tokenizer, prefix: str, label: str) -> int:
    prefix_ids = tokenizer(prefix, add_special_tokens=False)["input_ids"]
    full_ids = tokenizer(prefix + label, add_special_tokens=False)["input_ids"]
    common = 0
    while common < min(len(prefix_ids), len(full_ids)) and prefix_ids[common] == full_ids[common]:
        common += 1
    suffix = full_ids[common:]
    if common != len(prefix_ids) or len(suffix) != 1:
        raise SystemExit(f"CANDIDATE_TOKEN_NOT_SINGLE={label}:{suffix}")
    return int(suffix[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--code-sha", required=True)
    args = parser.parse_args()
    code_sha = args.code_sha.strip().lower()
    if len(code_sha) != 40 or any(ch not in "0123456789abcdef" for ch in code_sha):
        raise SystemExit("CODE_SHA_INVALID")

    output_dir = ROOT / OUTPUT_REL
    artifact = model_artifact_manifest(args.model_dir)
    environment = environment_manifest()
    write_json(output_dir / "model-artifact-manifest.json", artifact)
    write_json(output_dir / "environment-manifest.json", environment)

    load_preflight = preflight(
        code_sha=code_sha,
        action="MODEL_LOAD",
        artifact_sha=str(artifact["bundle_sha256"]),
        environment_sha=str(environment["environment_sha256"]),
    )
    write_json(output_dir / "preflight-model-load.json", load_preflight)
    if load_preflight["decision"]["state"] != "PREFLIGHT_PASS":
        print(json.dumps(load_preflight["decision"], sort_keys=True))
        return 2

    import torch
    from transformers import AutoModelForMultimodalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    prefix = "TASK: Return only A.\nANSWER: "
    token_a = candidate_suffix_id(tokenizer, prefix, "A")
    token_b = candidate_suffix_id(tokenizer, prefix, "B")

    started = time.perf_counter()
    model = AutoModelForMultimodalLM.from_pretrained(
        args.model_dir,
        local_files_only=True,
        dtype=torch.float32,
    )
    model.eval()
    load_seconds = time.perf_counter() - started

    post_load_memory = windows_memory()
    if post_load_memory and post_load_memory["available_physical_bytes"] < int(1.5 * 1024**3):
        result = {
            "state": "RESOURCE_BLOCKED_AFTER_LOAD",
            "reason": "AVAILABLE_PHYSICAL_MEMORY_BELOW_1_5_GIB",
            "load_seconds": load_seconds,
            "memory": post_load_memory,
        }
        write_json(output_dir / "smoke-result.json", result)
        print(json.dumps(result, sort_keys=True))
        return 3

    inference_preflight = preflight(
        code_sha=code_sha,
        action="INFERENCE",
        artifact_sha=str(artifact["bundle_sha256"]),
        environment_sha=str(environment["environment_sha256"]),
    )
    write_json(output_dir / "preflight-inference.json", inference_preflight)
    if inference_preflight["decision"]["state"] != "PREFLIGHT_PASS":
        print(json.dumps(inference_preflight["decision"], sort_keys=True))
        return 4

    inputs = tokenizer(prefix, return_tensors="pt", add_special_tokens=False)
    infer_started = time.perf_counter()
    with torch.no_grad():
        outputs = model(**inputs)
    infer_seconds = time.perf_counter() - infer_started
    logits = outputs.logits[0, -1]
    values = [float(logits[token_a].item()), float(logits[token_b].item())]
    result = {
        "state": "S1_SMOKE_PASS",
        "model_repo": MODEL_REPO,
        "model_revision": MODEL_REVISION,
        "code_sha": code_sha,
        "artifact_bundle_sha256": artifact["bundle_sha256"],
        "environment_sha256": environment["environment_sha256"],
        "candidate_token_ids": {"A": token_a, "B": token_b},
        "candidate_logits": {"A": values[0], "B": values[1]},
        "candidate_logits_sha256": canonical_sha256(values),
        "load_seconds": load_seconds,
        "inference_seconds": infer_seconds,
        "parameter_count": sum(parameter.numel() for parameter in model.parameters()),
        "trainable_parameter_count": sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad),
        "memory_after_inference": windows_memory(),
        "paid_api": False,
        "paid_compute": False,
        "phi": False,
        "confirmatory_materialized": False,
        "reserve_materialized": False,
    }
    result_sha = write_json(output_dir / "smoke-result.json", result)
    print("PREFLIGHT_MODEL_LOAD=PREFLIGHT_PASS")
    print("PREFLIGHT_INFERENCE=PREFLIGHT_PASS")
    print("SMOKE_STATE=S1_SMOKE_PASS")
    print(f"RESULT_SHA256={result_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
