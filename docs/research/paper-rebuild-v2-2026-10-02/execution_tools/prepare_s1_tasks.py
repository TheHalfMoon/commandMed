#!/usr/bin/env python3
"""Prepare and attest only pre-frozen V5 S1 development/calibration tasks."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.rule_dataset import (  # noqa: E402
    bind_selected_rules,
    materialize_development_examples,
    split_counts,
)

PACKET = ROOT / "docs/research/paper-rebuild-v2-2026-10-02"
MANIFEST_PATH = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
OUT_DIR = ROOT / "artifacts/v5/development/s1_task_preparation"
EXPECTED_SPLITS = {
    "S1_TRAIN": 256,
    "S1_DEV_EVAL": 3840,
    "S1_CAL_TUNE": 256,
    "S1_CAL_EVAL": 3840,
}
MAX_TOKENS = 768


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def write_json(path: Path, value: object) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return sha256_file(path)


def candidate_token_check(tokenizer, prefix: str, label: str) -> dict[str, object]:
    prefix_ids = tokenizer(prefix, add_special_tokens=False)["input_ids"]
    full_ids = tokenizer(prefix + label, add_special_tokens=False)["input_ids"]
    common = 0
    while common < min(len(prefix_ids), len(full_ids)) and prefix_ids[common] == full_ids[common]:
        common += 1
    suffix = full_ids[common:]
    return {
        "prefix_ids": prefix_ids,
        "full_ids": full_ids,
        "common_prefix_length": common,
        "suffix_ids": suffix,
        "prefix_preserved": common == len(prefix_ids),
        "valid": common == len(prefix_ids) and len(suffix) == 1,
    }


def candidate_suffix_id(tokenizer, prefix: str, label: str) -> int:
    check = candidate_token_check(tokenizer, prefix, label)
    if not check["valid"]:
        raise SystemExit(f"CANDIDATE_TOKEN_NOT_SINGLE={label}:{check['suffix_ids']}")
    return int(check["suffix_ids"][0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--riskcalcs-source", type=Path, required=True)
    parser.add_argument("--model-dir", type=Path, required=True)
    args = parser.parse_args()

    source_bytes = args.riskcalcs_source.read_bytes()
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    rules = bind_selected_rules(source_bytes=source_bytes, selection_manifest=manifest)
    examples = materialize_development_examples(rules)
    counts = split_counts(examples)
    if counts != dict(sorted(EXPECTED_SPLITS.items())):
        raise SystemExit(f"SPLIT_COUNT_MISMATCH={json.dumps(counts, sort_keys=True)}")

    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    answer_prefix = "ANSWER:\n"
    token_checks = {
        label: candidate_token_check(tokenizer, answer_prefix, label) for label in ("A", "B")
    }
    candidate_failures = [label for label, check in token_checks.items() if not check["valid"]]
    candidate_ids = {
        label: int(check["suffix_ids"][0]) if check["valid"] else None
        for label, check in token_checks.items()
    }

    max_lengths: dict[str, int] = {name: 0 for name in EXPECTED_SPLITS}
    overlength: list[str] = []
    target_counts: dict[str, dict[str, int]] = {
        split: {"A": 0, "B": 0, "MATCH": 0, "MISMATCH": 0} for split in EXPECTED_SPLITS
    }
    transformed_identity_failures = 0
    ordered_task_ids: list[str] = []
    prompt_identities: list[dict[str, object]] = []
    full_prompt_candidate_failures: list[dict[str, str]] = []
    overlength_records: list[dict[str, object]] = []

    for example in examples:
        ordered_task_ids.append(example.task_id)
        for variant, prompt in (("canonical", example.canonical_prompt), ("transformed", example.transformed_prompt)):
            length = len(tokenizer(prompt, add_special_tokens=False)["input_ids"])
            prompt_identities.append({
                "task_id": example.task_id,
                "variant": variant,
                "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                "tokens": length,
            })
            for label in ("A", "B"):
                check = candidate_token_check(tokenizer, prompt, label)
                if not check["valid"] or check["suffix_ids"] != [candidate_ids[label]]:
                    full_prompt_candidate_failures.append({
                        "task_id": example.task_id, "variant": variant, "label": label,
                    })
            max_lengths[example.split] = max(max_lengths[example.split], length)
            if length > MAX_TOKENS:
                overlength.append(example.task_id)
                overlength_records.append({
                    "task_id": example.task_id,
                    "pmid": example.pmid,
                    "split": example.split,
                    "variant": variant,
                    "tokens": length,
                })
        if example.canonical_prompt == example.transformed_prompt:
            transformed_identity_failures += 1
        target_counts[example.split][example.target_label] += 1
        target_counts[example.split]["MATCH" if example.proposal_matches else "MISMATCH"] += 1

    evidence: dict[str, object] = {
        "schema": "commandmed.v5.s1.task-preparation.v1",
        "status": "FAILED_PRE_MODEL_INTERFACE" if candidate_failures or full_prompt_candidate_failures or overlength or transformed_identity_failures else "PASS_PRE_MODEL_INTERFACE",
        "code_sha": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "preparation_implementation_sha256": sha256_file(Path(__file__)),
        "renderer_implementation_sha256": sha256_file(ROOT / "src/commandmed/reliability_v5/rule_dataset.py"),
        "prompt_identity_count": len(prompt_identities),
        "prompt_content_sequence_sha256": canonical_sha256(prompt_identities),
        "full_prompt_candidate_check_count": len(prompt_identities) * 2,
        "full_prompt_candidate_failures": full_prompt_candidate_failures,
        "model_repo": "Qwen/Qwen3.5-0.8B-Base",
        "model_revision": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
        "tokenizer_files": {
            name: sha256_file(args.model_dir / name)
            for name in ("tokenizer.json", "tokenizer_config.json", "vocab.json", "merges.txt")
        },
        "tokenizer_packages": {
            name: importlib.metadata.version(name) for name in ("transformers", "tokenizers")
        },
        "riskcalcs_source_sha256": sha256_file(args.riskcalcs_source),
        "selection_manifest_sha256": sha256_file(MANIFEST_PATH),
        "calculator_count": len(rules),
        "example_count": len(examples),
        "split_counts": counts,
        "task_id_sequence_sha256": hashlib.sha256("".join(ordered_task_ids).encode("ascii")).hexdigest(),
        "answer_prefix": answer_prefix,
        "tokenizer_candidate_ids": candidate_ids,
        "tokenizer_candidate_checks": token_checks,
        "candidate_token_failures": candidate_failures,
        "max_prompt_tokens_by_split": dict(sorted(max_lengths.items())),
        "max_tokens_contract": MAX_TOKENS,
        "overlength_count": len(overlength),
        "overlength_task_ids_sha256": canonical_sha256(sorted(overlength)),
        "overlength_records": overlength_records,
        "transformed_identity_failures": transformed_identity_failures,
        "target_counts": target_counts,
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "phi": False,
        "gated_data": False,
        "model_loaded": False,
        "model_inference": False,
        "training": False,
    }
    evidence_sha = write_json(OUT_DIR / "task-preparation-evidence.json", evidence)
    print(f"BOUND_RULES={len(rules)}")
    print(f"EXAMPLES={len(examples)}")
    print(f"SPLITS={json.dumps(counts, sort_keys=True)}")
    print(f"MAX_PROMPT_TOKENS={max(max_lengths.values())}")
    print(f"OVERLENGTH={len(overlength)}")
    print(f"CANDIDATE_TOKEN_FAILURES={json.dumps(candidate_failures)}")
    print(f"EVIDENCE_SHA256={evidence_sha}")
    if candidate_failures or full_prompt_candidate_failures or overlength or transformed_identity_failures:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
