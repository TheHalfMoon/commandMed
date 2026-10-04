#!/usr/bin/env python3
"""Metadata-only pinned SQuAD preparation; never loads or executes model weights."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
from pathlib import Path

import v5_s1_colab_qualification as colab
from commandmed.reliability_v5 import retention_dataset as retention


def prepare(source: Path, model_dir: Path) -> dict:
    import pyarrow.parquet as parquet
    from transformers import AutoTokenizer
    if colab.base.sha256_file(source) != retention.SOURCE_FILE_SHA256:
        raise ValueError("SQUAD_EXACT_PUBLIC_SOURCE_FILE_MISMATCH")
    frozen = json.loads((colab.REPO / "artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json").read_text())
    for name, digest in frozen["tokenizer_files"].items():
        if colab.base.sha256_file(model_dir / name) != digest:
            raise ValueError("SQUAD_EXACT_TOKENIZER_FILE_MISMATCH")
    packages = {name: importlib.metadata.version(name) for name in ("transformers", "tokenizers")}
    if packages != frozen["tokenizer_packages"]:
        raise ValueError("SQUAD_EXACT_TOKENIZER_PACKAGE_MISMATCH")
    config = json.loads((model_dir / "config.json").read_text())
    context_bound = config["text_config"]["max_position_embeddings"]
    if not isinstance(context_bound, int) or context_bound <= 0:
        raise ValueError("SQUAD_EXACT_MODEL_CONTEXT_IDENTITY_MISSING")
    rows = parquet.read_table(source).to_pylist()
    maintenance, evaluation = retention.select_roles(rows)
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    records = {}
    for role, pool in (("S1_C2_MAINTENANCE", maintenance), ("S1_RETENTION_EVAL", evaluation)):
        records[role] = [retention.prepare_row(row, tokenizer, maintenance=role == "S1_C2_MAINTENANCE", context_bound=context_bound) for row in pool]
    return {
        "schema": "commandmed.v5.s1.retention-preparation.v1", "status": "PASS_RETENTION_METADATA_ONLY",
        "code_sha": colab.base.git_text("rev-parse", "HEAD"),
        "source_repo": retention.SOURCE_REPO, "source_revision": retention.SOURCE_REVISION,
        "source_file": retention.SOURCE_FILE, "source_file_sha256": retention.SOURCE_FILE_SHA256,
        "source_count": len(rows), "namespace": retention.SOURCE_NAMESPACE,
        "rank_preimage": "UPSTREAM_ID_UTF8_ONLY; SHA256; ID_TIEBREAK", "roles": records,
        "prompt_template_sha256": colab.base.sha256_bytes(retention.QA_PROMPT_TEMPLATE.encode()),
        "retention_implementation_sha256": colab.base.sha256_file(Path(retention.__file__)),
        "preparation_implementation_sha256": colab.base.sha256_file(Path(__file__)),
        "tokenizer_files": frozen["tokenizer_files"], "tokenizer_packages": packages,
        "pyarrow_version": importlib.metadata.version("pyarrow"),
        "max_prompt_tokens": max(item["prompt_tokens"] for pool in records.values() for item in pool),
        "maximum_answer_tokens": retention.MAX_ANSWER_TOKENS,
        "maintenance_first_gold_annotation_max_tokens": retention.MAINTENANCE_GOLD_TOKENS,
        "exact_model_context_bound": context_bound, "medical_maximum_unchanged": 768,
        "truncation": False, "source_payload_exported": False,
        "model_loaded": False, "model_inference": False, "training": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    args = parser.parse_args()
    colab.verify_head(args.expected_head)
    if not args.output.resolve().is_relative_to((colab.REPO / "artifacts/v5/development").resolve()):
        raise ValueError("RETENTION_METADATA_OUTPUT_OUTSIDE_DEVELOPMENT")
    try:
        result = prepare(args.source, args.model_dir)
    except Exception as exc:
        result = {"status": "FAILED_RETENTION_METADATA_ONLY", "reason": str(exc), "model_loaded": False, "model_inference": False}
    digest = colab.base.write_json(args.output, result)
    print(json.dumps({"status": result["status"], "sha256": digest, "max_prompt_tokens": result.get("max_prompt_tokens"), "reason": result.get("reason")}), flush=True)
    return 0 if result["status"] == "PASS_RETENTION_METADATA_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
