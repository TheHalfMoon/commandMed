#!/usr/bin/env python3
"""Fail-closed V5 S1 artifact binding and local resource qualification.

This script is development-only. It never materializes confirmatory/reserve
identities and never executes paid/provider resources.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import threading
import time
import urllib.request
from dataclasses import asdict
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from commandmed.reliability_v5.preflight import (
    DevelopmentAuthority,
    DevelopmentRunManifest,
    evaluate_development_preflight,
)
from commandmed.reliability_v5.rule_dataset import (
    FROZEN_SOURCE_SHA256,
    bind_selected_rules,
    materialize_development_examples,
    split_counts,
)

MODEL_REPO = "Qwen/Qwen3.5-0.8B-Base"
MODEL_REVISION = "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"
AUTHORITY_ID = "V5_FOUNDER_AUTHORIZATION_2026-10-03"
SOURCE_URL = (
    "https://raw.githubusercontent.com/ncbi-nlp/Clinical-Tool-Learning/"
    "d474a95128e128623933c9be0d389ff7d82ef782/"
    "riskqa_evaluation/tools/riskcalcs.json"
)
SELECTION_MANIFEST = REPO / "docs/research/paper-rebuild-v2-2026-10-02/riskcalcs-rule-oracle-final-candidate-v5.json"
OUTPUT_REL = Path("artifacts/v5/development/s1-resource-qualification")
OUTPUT = REPO / OUTPUT_REL
RUNTIME_DTYPE = "bfloat16"
CPU_THREADS = 8
CPU_INTEROP_THREADS = 1
GIB = 1024 ** 3
MIN_DISK_HEADROOM = 2 * GIB
MIN_MEMORY_HEADROOM = int(1.5 * GIB)
MAX_BENCHMARK_SECONDS = 180.0
MAX_PROJECTED_SEED_SECONDS = 12 * 60 * 60


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode("utf-8")


def write_json(path: Path, value: Any) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n"
    path.write_text(payload, encoding="utf-8", newline="\n")
    return sha256_bytes(payload.encode("utf-8"))


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(REPO), *args], text=True).strip()


def require_clean_head() -> str:
    status = git_text("status", "--porcelain", "--untracked-files=all")
    unexpected: list[str] = []
    evidence_prefix = OUTPUT_REL.as_posix().rstrip("/") + "/"
    for line in status.splitlines():
        path = line[3:].strip().replace("\\", "/")
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if path.startswith(evidence_prefix):
            continue
        unexpected.append(line)
    if unexpected:
        raise RuntimeError("working tree has non-evidence changes before V5 model execution: " + " | ".join(unexpected))
    head = git_text("rev-parse", "HEAD")
    if len(head) != 40:
        raise RuntimeError("unexpected Git HEAD identity")
    return head


def package_version(name: str) -> str:
    return importlib.metadata.version(name)


def environment_record() -> dict[str, Any]:
    import psutil
    import torch

    return {
        "schema": "commandmed.v5.environment.v1",
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python": sys.version,
        "python_executable": sys.executable,
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "cpu_count_physical": psutil.cpu_count(logical=False),
        "torch_threads": CPU_THREADS,
        "torch_interop_threads": CPU_INTEROP_THREADS,
        "runtime_dtype": RUNTIME_DTYPE,
        "cuda_available": bool(torch.cuda.is_available()),
        "packages": {
            name: package_version(name)
            for name in (
                "torch",
                "torchvision",
                "transformers",
                "peft",
                "datasets",
                "numpy",
                "huggingface-hub",
                "safetensors",
                "psutil",
            )
        },
    }


def bind_artifact(model_dir: Path) -> tuple[dict[str, Any], str]:
    rows: list[dict[str, Any]] = []
    for path in sorted(model_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(model_dir).as_posix()
        if rel.startswith(".cache/"):
            continue
        rows.append({"path": rel, "size": path.stat().st_size, "sha256": sha256_file(path)})
    if not rows or not any(row["path"].endswith(".safetensors") for row in rows):
        raise RuntimeError("model artifact binding found no safetensors weights")
    bundle_sha = sha256_bytes(canonical_json(rows))
    record = {
        "schema": "commandmed.v5.model-artifact.v1",
        "repo": MODEL_REPO,
        "revision": MODEL_REVISION,
        "file_count": len(rows),
        "files": rows,
        "bundle_sha256": bundle_sha,
    }
    return record, bundle_sha


def authority() -> DevelopmentAuthority:
    return DevelopmentAuthority(
        approved=True,
        authority_id=AUTHORITY_ID,
        paid_compute=False,
        paid_api=False,
        spend_usd=0.0,
        phi_allowed=False,
        gated_data_allowed=False,
        confirmatory_allowed=False,
        reserve_allowed=False,
    )


def preflight(*, action: str, intervention: str, roles: tuple[str, ...], code_sha: str, artifact_sha: str, env_sha: str) -> dict[str, Any]:
    manifest = DevelopmentRunManifest(
        action=action,
        model_repo=MODEL_REPO,
        model_revision=MODEL_REVISION,
        model_artifact_sha256=artifact_sha,
        intervention_id=intervention,
        data_roles=roles,
        code_sha=code_sha,
        environment_id=f"sha256:{env_sha}",
        output_destination=OUTPUT_REL.as_posix() + "/",
        confirmatory_materialized=False,
        reserve_materialized=False,
        contains_phi=False,
        uses_gated_data=False,
        paid_resource=False,
        expected_spend_usd=0.0,
    )
    decision = evaluate_development_preflight(manifest, authority())
    record = {"manifest": asdict(manifest), "authority": asdict(authority()), "decision": asdict(decision)}
    if not decision.allowed:
        raise RuntimeError(f"preflight blocked: {decision.reason_codes}")
    return record


class MemorySampler:
    def __init__(self) -> None:
        self._stop = threading.Event()
        self.peak_rss = 0
        self.min_available = 2**63 - 1
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        import psutil

        process = psutil.Process(os.getpid())

        def sample() -> None:
            while not self._stop.is_set():
                self.peak_rss = max(self.peak_rss, process.memory_info().rss)
                self.min_available = min(self.min_available, psutil.virtual_memory().available)
                self._stop.wait(0.05)

        self._thread = threading.Thread(target=sample, daemon=True)
        self._thread.start()

    def stop(self) -> dict[str, int]:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=2)
        return {"peak_rss_bytes": self.peak_rss, "min_system_available_bytes": self.min_available}


def acquire_model(model_dir: Path) -> dict[str, Any]:
    from huggingface_hub import HfApi, snapshot_download

    api = HfApi()
    info = api.model_info(MODEL_REPO, revision=MODEL_REVISION)
    if info.sha != MODEL_REVISION:
        raise RuntimeError(f"resolved model SHA mismatch: {info.sha}")
    model_dir.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=MODEL_REPO, revision=MODEL_REVISION, local_dir=str(model_dir))
    return {"resolved_sha": info.sha, "private": bool(info.private), "gated": bool(info.gated)}


def acquire_source(source_path: Path) -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "CommandMed-V5-development"})
    with urllib.request.urlopen(req, timeout=60) as response:
        payload = response.read()
    if sha256_bytes(payload) != FROZEN_SOURCE_SHA256:
        raise RuntimeError("RiskCalcs source hash mismatch")
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_bytes(payload)
    return payload


def token_suffix_id(tokenizer: Any, prompt: str, label: str) -> int:
    base = tokenizer.encode(prompt, add_special_tokens=False)
    extended = tokenizer.encode(prompt + label, add_special_tokens=False)
    if len(extended) != len(base) + 1 or extended[: len(base)] != base:
        raise RuntimeError(f"label {label!r} is not exactly one next token under frozen answer prefix")
    return int(extended[-1])


def dataset_interface_record(tokenizer: Any, source_bytes: bytes) -> tuple[dict[str, Any], tuple[Any, ...]]:
    selection = json.loads(SELECTION_MANIFEST.read_text(encoding="utf-8"))
    rules = bind_selected_rules(source_bytes=source_bytes, selection_manifest=selection)
    examples = materialize_development_examples(rules)
    lengths = [len(tokenizer.encode(example.canonical_prompt, add_special_tokens=False)) for example in examples]
    transformed_lengths = [len(tokenizer.encode(example.transformed_prompt, add_special_tokens=False)) for example in examples]
    maximum = max(lengths + transformed_lengths)
    if maximum > 768:
        raise RuntimeError(f"medical prompt length exceeds frozen 768-token bound: {maximum}")
    representative = examples[0].canonical_prompt
    a_id = token_suffix_id(tokenizer, representative, "A")
    b_id = token_suffix_id(tokenizer, representative, "B")
    if a_id == b_id:
        raise RuntimeError("A/B candidate token IDs are not distinct")
    record = {
        "calculator_count": len(rules),
        "example_count": len(examples),
        "split_counts": split_counts(examples),
        "max_canonical_tokens": max(lengths),
        "max_transformed_tokens": max(transformed_lengths),
        "candidate_token_ids": {"A": a_id, "B": b_id},
        "task_ids_sha256": sha256_bytes(canonical_json([example.task_id for example in examples])),
        "confirmatory_materialized": False,
        "reserve_materialized": False,
    }
    return record, examples


def candidate_probabilities(model: Any, torch: Any, encoded: dict[str, Any], a_id: int, b_id: int) -> Any:
    outputs = model(**encoded, use_cache=False)
    logits = outputs.logits[:, -1, [a_id, b_id]].float()
    return torch.softmax(logits, dim=-1)


def smoke_inference(model: Any, tokenizer: Any, torch: Any, a_id: int, b_id: int) -> dict[str, Any]:
    prompt = "TASK: Mechanical label check.\nA = MATCH\nB = MISMATCH\nReturn only A or B.\nANSWER:\n"
    if token_suffix_id(tokenizer, prompt, "A") != a_id or token_suffix_id(tokenizer, prompt, "B") != b_id:
        raise RuntimeError("candidate token identity changed across frozen answer prefix")
    encoded = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    with torch.no_grad():
        probs = candidate_probabilities(model, torch, encoded, a_id, b_id)[0].tolist()
    return {"prompt_sha256": sha256_bytes(prompt.encode("utf-8")), "candidate_probabilities": {"A": probs[0], "B": probs[1]}}


def final_block_linear_names(model: Any, torch: Any) -> list[str]:
    if not hasattr(model, "model") or not hasattr(model.model, "layers"):
        raise RuntimeError("exact final text block cannot be isolated")
    layers = model.model.layers
    if len(layers) != 24:
        raise RuntimeError(f"unexpected text layer count: {len(layers)}")
    prefix = "model.layers.23."
    names = [name for name, module in model.named_modules() if name.startswith(prefix) and isinstance(module, torch.nn.Linear)]
    if not names:
        raise RuntimeError("no final-block Linear modules found")
    return sorted(names)


def js_divergence(torch: Any, p: Any, q: Any) -> Any:
    midpoint = 0.5 * (p + q)
    return 0.5 * torch.sum(p * (torch.log(p) - torch.log(midpoint))) + 0.5 * torch.sum(q * (torch.log(q) - torch.log(midpoint)))


def lora_resource_benchmark(model: Any, tokenizer: Any, torch: Any, a_id: int, b_id: int) -> dict[str, Any]:
    from peft import LoraConfig, TaskType, get_peft_model

    targets = final_block_linear_names(model, torch)
    config = LoraConfig(
        r=4,
        lora_alpha=8,
        target_modules=targets,
        lora_dropout=0.0,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    adapted = get_peft_model(model, config)
    trainable = [(name, param.numel()) for name, param in adapted.named_parameters() if param.requires_grad]
    if not trainable or any("lora_" not in name or "layers.23." not in name for name, _ in trainable):
        raise RuntimeError("trainable parameter set escaped frozen final-block LoRA scope")

    unit = tokenizer.encode(" mechanical", add_special_tokens=False)
    if not unit:
        raise RuntimeError("synthetic benchmark tokenization failed")
    ids = (unit * ((256 // len(unit)) + 1))[:256]
    input_ids = torch.tensor([ids], dtype=torch.long)
    attention_mask = torch.ones_like(input_ids)
    optimizer = torch.optim.AdamW(
        (param for _, param in adapted.named_parameters() if param.requires_grad),
        lr=5e-4,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=0.0,
    )

    def step() -> float:
        optimizer.zero_grad(set_to_none=True)
        out1 = adapted(input_ids=input_ids, attention_mask=attention_mask, use_cache=False).logits[:, -1, [a_id, b_id]].float()
        out2 = adapted(input_ids=input_ids, attention_mask=attention_mask, use_cache=False).logits[:, -1, [a_id, b_id]].float()
        target = torch.tensor([0], dtype=torch.long)
        medical_nll = torch.nn.functional.cross_entropy(out1, target)
        p = torch.softmax(out1, dim=-1)[0].clamp_min(1e-12)
        q = torch.softmax(out2, dim=-1)[0].clamp_min(1e-12)
        loss = medical_nll + 0.1 * js_divergence(torch, p, q)
        loss.backward()
        torch.nn.utils.clip_grad_norm_((param for _, param in adapted.named_parameters() if param.requires_grad), 1.0)
        optimizer.step()
        return float(loss.detach().cpu())

    warmup_loss = step()
    sampler = MemorySampler()
    sampler.start()
    started = time.perf_counter()
    timed_loss = step()
    elapsed = time.perf_counter() - started
    memory = sampler.stop()
    projected_seed_seconds = elapsed * 256
    return {
        "target_modules": targets,
        "trainable_parameters": sum(count for _, count in trainable),
        "trainable_parameter_names": [name for name, _ in trainable],
        "sequence_tokens": 256,
        "warmup_loss": warmup_loss,
        "timed_loss": timed_loss,
        "timed_forward_backward_seconds": elapsed,
        "projected_256_example_seed_seconds": projected_seed_seconds,
        **memory,
    }


def qualify(model_dir: Path, source_path: Path) -> dict[str, Any]:
    import psutil
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    torch.set_num_threads(CPU_THREADS)
    torch.set_num_interop_threads(CPU_INTEROP_THREADS)
    if torch.cuda.is_available():
        raise RuntimeError("S1 local qualification is CPU-only; unexpected CUDA availability")

    code_sha = require_clean_head()
    artifact, artifact_sha = bind_artifact(model_dir)
    artifact_record_sha = write_json(OUTPUT / "model-artifact-manifest.json", artifact)
    env = environment_record()
    env_sha = sha256_bytes(canonical_json(env))
    write_json(OUTPUT / "environment-manifest.json", {**env, "environment_sha256": env_sha})

    free_disk = psutil.disk_usage(str(model_dir.drive + "\\")).free
    if free_disk < MIN_DISK_HEADROOM:
        raise RuntimeError(f"resource blocker: disk headroom below 2 GiB ({free_disk})")

    source_bytes = source_path.read_bytes()
    if sha256_bytes(source_bytes) != FROZEN_SOURCE_SHA256:
        raise RuntimeError("local RiskCalcs source hash mismatch")

    load_preflight = preflight(action="MODEL_LOAD", intervention="BASELINE_V1", roles=("SYNTHETIC_MECHANICAL",), code_sha=code_sha, artifact_sha=artifact_sha, env_sha=env_sha)
    write_json(OUTPUT / "preflight-model-load.json", load_preflight)

    load_sampler = MemorySampler()
    load_sampler.start()
    load_started = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        local_files_only=True,
        dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
    )
    model.eval()
    load_seconds = time.perf_counter() - load_started
    load_memory = load_sampler.stop()
    if load_memory["min_system_available_bytes"] < MIN_MEMORY_HEADROOM:
        raise RuntimeError("resource blocker: model load leaves less than 1.5 GiB system headroom")

    interface, _ = dataset_interface_record(tokenizer, source_bytes)
    write_json(OUTPUT / "dataset-interface.json", interface)
    a_id = int(interface["candidate_token_ids"]["A"])
    b_id = int(interface["candidate_token_ids"]["B"])

    inference_preflight = preflight(action="INFERENCE", intervention="BASELINE_V1", roles=("SYNTHETIC_MECHANICAL",), code_sha=code_sha, artifact_sha=artifact_sha, env_sha=env_sha)
    write_json(OUTPUT / "preflight-inference.json", inference_preflight)
    smoke = smoke_inference(model, tokenizer, torch, a_id, b_id)
    smoke_sha = write_json(OUTPUT / "smoke-inference.json", smoke)

    training_preflight = preflight(action="TRAINING", intervention="C1_CRDI_V1", roles=("SYNTHETIC_MECHANICAL",), code_sha=code_sha, artifact_sha=artifact_sha, env_sha=env_sha)
    write_json(OUTPUT / "preflight-training.json", training_preflight)
    benchmark = lora_resource_benchmark(model, tokenizer, torch, a_id, b_id)

    blockers: list[str] = []
    if benchmark["timed_forward_backward_seconds"] > MAX_BENCHMARK_SECONDS:
        blockers.append("SYNTHETIC_LORA_STEP_EXCEEDS_180_SECONDS")
    if benchmark["projected_256_example_seed_seconds"] > MAX_PROJECTED_SEED_SECONDS:
        blockers.append("PROJECTED_C1_C2_SEED_EXCEEDS_12_HOURS")
    if benchmark["min_system_available_bytes"] < MIN_MEMORY_HEADROOM:
        blockers.append("MEMORY_HEADROOM_BELOW_1_5_GIB")

    result = {
        "schema": "commandmed.v5.s1-resource-qualification.v1",
        "status": "RESOURCE_BLOCKED" if blockers else "RESOURCE_QUALIFIED",
        "blockers": blockers,
        "code_sha": code_sha,
        "model_repo": MODEL_REPO,
        "model_revision": MODEL_REVISION,
        "model_artifact_sha256": artifact_sha,
        "model_artifact_manifest_sha256": artifact_record_sha,
        "environment_sha256": env_sha,
        "load_seconds": load_seconds,
        "load_memory": load_memory,
        "dataset_interface_sha256": sha256_file(OUTPUT / "dataset-interface.json"),
        "smoke_output_sha256": smoke_sha,
        "benchmark": benchmark,
        "paid_api": False,
        "paid_compute": False,
        "spend_usd": 0.0,
        "phi": False,
        "gated_data": False,
        "confirmatory_materialized": False,
        "reserve_materialized": False,
    }
    result_sha = write_json(OUTPUT / "resource-qualification.json", result)
    write_json(OUTPUT / "run-attestation.json", {"result_sha256": result_sha, "completed": True, "status": result["status"]})
    return result


def self_test() -> None:
    payload = {"b": 2, "a": 1}
    assert sha256_bytes(canonical_json(payload)) == sha256_bytes(b'{"a":1,"b":2}')
    decision = evaluate_development_preflight(
        DevelopmentRunManifest(
            action="MODEL_LOAD",
            model_repo=MODEL_REPO,
            model_revision=MODEL_REVISION,
            model_artifact_sha256="0" * 64,
            intervention_id="BASELINE_V1",
            data_roles=("SYNTHETIC_MECHANICAL",),
            code_sha="0" * 40,
            environment_id="sha256:" + "0" * 64,
            output_destination=OUTPUT_REL.as_posix() + "/",
        ),
        authority(),
    )
    assert decision.allowed
    print("SELF_TEST=PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime-root", type=Path, default=Path(r"D:\CommandMed-V5-runtime"))
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--acquire", action="store_true")
    parser.add_argument("--qualify", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    model_dir = args.runtime_root / "model" / MODEL_REVISION
    source_path = args.runtime_root / "source" / "riskcalcs.json"
    OUTPUT.mkdir(parents=True, exist_ok=True)
    if args.acquire:
        acquisition = acquire_model(model_dir)
        source_bytes = acquire_source(source_path)
        artifact, artifact_sha = bind_artifact(model_dir)
        acquisition.update(
            {
                "model_artifact_sha256": artifact_sha,
                "model_files": len(artifact["files"]),
                "source_sha256": sha256_bytes(source_bytes),
                "runtime_drive_free_bytes": __import__("shutil").disk_usage(args.runtime_root).free,
                "paid_api": False,
                "paid_compute": False,
                "spend_usd": 0.0,
            }
        )
        write_json(OUTPUT / "acquisition.json", acquisition)
        print(json.dumps(acquisition, sort_keys=True))
    if args.qualify:
        result = qualify(model_dir, source_path)
        print(json.dumps(result, sort_keys=True))
        return 2 if result["status"] == "RESOURCE_BLOCKED" else 0
    if not args.acquire and not args.qualify:
        parser.error("select --self-test, --acquire, and/or --qualify")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
