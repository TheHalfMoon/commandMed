#!/usr/bin/env python3
"""Rebuild frozen development source-case identities; reject pseudoreplication.

Requires the separately verified pinned *public* RiskCalcs JSON source file.
No model, training, API, confirmatory/reserve identity, or GPU is used.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.commandmed.reliability_v5.rule_dataset import (
    RuleVerificationExample,
    bind_selected_rules,
    materialize_development_examples,
)

SOURCE_SHA = "00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9"
PACKET = Path("docs/research/paper-rebuild-v2-2026-10-02")
MANIFEST_PATH = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
MANIFEST_SHA = "445e37ee7b3a2bb56c21d04a6236e16a929f6207c74351c0143fe436c61abd9c"
RULE_DATASET_PATH = Path("src/commandmed/reliability_v5/rule_dataset.py")
RULE_DATASET_SHA = "bb062209196b045295a65403fd72e132ef01c6bc556a79048ba6284d905a3433"
CASE_GENERATOR_PATH = Path("src/commandmed/reliability_v5/case_generator.py")
CASE_GENERATOR_SHA = "1a79f6336a2f31440609b6d1af57984765b360cd09404bd7c817d61724cb73f0"
PREP_PATH = Path("artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json")
RUN_PATHS = {
    1: (
        Path("artifacts/v5/development/s1-kaggle-repeatability-runs/repeat-1-v1-2026-10-09/evidence/repeatability-decision-matrix.json"),
        "600dbd236098b967558e96d5ddf7d4144903fad96b172ad2871ec02fb0f30a44",
    ),
    2: (
        Path("artifacts/v5/development/s1-kaggle-repeatability-runs/repeat-2-v1-2026-10-09/evidence/repeatability-decision-matrix.json"),
        "37a78d4d067d00a486e2c63fc72662ecb2cee4d54c522ac8e05048e432eec902",
    ),
}
SPLIT_COUNTS = {"S1_TRAIN": 256, "S1_DEV_EVAL": 3840, "S1_CAL_TUNE": 256, "S1_CAL_EVAL": 3840}
PER_CALCULATOR_COUNTS = {"S1_TRAIN": 4, "S1_DEV_EVAL": 60, "S1_CAL_TUNE": 4, "S1_CAL_EVAL": 60}
TASK_SEQUENCE_SHA = "36c86610e2a762cb57ab61a8dff6a829e7196a638178dc612b5d1d3d5bdd5e0c"


class SourceCaseAuditError(ValueError):
    """Model-free case-to-task identity or hash mismatch."""


def _require(ok: bool, reason: str) -> None:
    if not ok:
        raise SourceCaseAuditError(reason)


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _locked_bytes(root: Path, rel: Path, expected_sha: str) -> bytes:
    path = (root / rel).resolve()
    _require(path.is_relative_to(root.resolve()), "SOURCE_PATH_ESCAPES_REPO")
    _require(path.is_file(), "MISSING_LOCKED_FILE:" + str(rel))
    data = path.read_bytes()
    _require(_sha(data) == expected_sha, "LOCKED_SOURCE_HASH_MISMATCH:" + str(rel))
    return data


def verify_unique_case_unit(examples: Sequence[RuleVerificationExample]) -> dict[str, Any]:
    """One intrinsic generated medical case, one task_id, across both splits."""
    _require(len(examples) == 8192, "SOURCE_CASE_COUNT_INCORRECT")
    case_ids = [x.case_id for x in examples]
    task_ids = [x.task_id for x in examples]
    state_keys = [(x.calculator_id, x.state_index) for x in examples]
    _require(len(set(case_ids)) == len(examples), "SOURCE_CASE_ID_REUSED")
    _require(len(set(task_ids)) == len(examples), "TASK_ID_REUSED")
    _require(len(set(state_keys)) == len(examples), "CALCULATOR_STATE_REUSED")
    _require(all(x.case_id and x.task_id and x.calculator_id for x in examples), "EMPTY_CASE_OR_TASK_ID")
    split_counts = dict(Counter(x.split for x in examples))
    _require(split_counts == SPLIT_COUNTS, "SOURCE_CASE_SPLITS_CHANGED")
    calculators = {x.calculator_id for x in examples}
    _require(len(calculators) == 64, "CALCULATOR_COUNT_CHANGED")
    per_calc = Counter((x.calculator_id, x.split) for x in examples)
    for calc in calculators:
        _require(all(per_calc[(calc, split)] == count for split, count in PER_CALCULATOR_COUNTS.items()), "CALCULATOR_SPLIT_DISTRIBUTION_CHANGED")
    _require(_sha("".join(task_ids).encode("ascii")) == TASK_SEQUENCE_SHA, "FROZEN_TASK_SEQUENCE_CHANGED")
    return {
        "source_case_count": len(examples),
        "unique_intrinsic_case_ids": len(set(case_ids)),
        "unique_task_ids": len(set(task_ids)),
        "unique_calculator_state_pairs": len(set(state_keys)),
        "selected_calculators": len(calculators),
        "split_counts": split_counts,
        "frozen_task_sequence_sha256": TASK_SEQUENCE_SHA,
        "case_to_task_binding_sha256": _sha(
            "".join(f"{x.case_id}|{x.task_id}|{x.split}\n" for x in examples).encode("ascii")
        ),
    }


def verify_model_output_pairing(
    examples: Sequence[RuleVerificationExample],
    rows: Sequence[dict[str, Any]],
) -> None:
    _require(len(rows) == 2 * len(examples), "PROMPT_VARIANT_COUNT_MISMATCH")
    for index, case in enumerate(examples):
        canonical, transformed = rows[2 * index:2 * index + 2]
        for variant, row, prompt in (
            ("canonical", canonical, case.canonical_prompt),
            ("transformed", transformed, case.transformed_prompt),
        ):
            expected = {
                "task_id": case.task_id,
                "calculator_id": case.calculator_id,
                "split": case.split,
                "variant": variant,
                "target_index": 0 if case.target_label == "A" else 1,
                "option_a_semantic": case.option_a_semantic,
                "prompt_sha256": _sha(prompt.encode("utf-8")),
            }
            _require(all(row.get(key) == val and type(row.get(key)) == type(val)
                         for key, val in expected.items()), "SOURCE_TO_PROMPT_BINDING_MISMATCH")


def audit(source: Path, *, root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    _require(source.is_file(), "PINNED_PUBLIC_SOURCE_REQUIRED")
    source_bytes = source.read_bytes()
    _require(_sha(source_bytes) == SOURCE_SHA, "PINNED_SOURCE_SHA_MISMATCH")
    _locked_bytes(root, RULE_DATASET_PATH, RULE_DATASET_SHA)
    _locked_bytes(root, CASE_GENERATOR_PATH, CASE_GENERATOR_SHA)
    manifest = json.loads(_locked_bytes(root, MANIFEST_PATH, MANIFEST_SHA))
    prep = json.loads((root / PREP_PATH).read_text(encoding="utf-8"))
    _require(prep.get("status") == "PASS_PRE_MODEL_INTERFACE" and
             prep.get("task_id_sequence_sha256") == TASK_SEQUENCE_SHA and
             prep.get("prompt_identity_count") == 16384, "FROZEN_PREPARATION_IDENTITY_MISMATCH")
    rules = bind_selected_rules(source_bytes=source_bytes, selection_manifest=manifest)
    _require(len(rules) == 64, "SELECTED_RULES_CHANGED")
    examples = materialize_development_examples(rules)
    output = verify_unique_case_unit(examples)
    for repeat, (rel, digest) in RUN_PATHS.items():
        payload = json.loads(_locked_bytes(root, rel, digest))
        _require(payload.get("complete") is True and payload.get("intervention") == "BASELINE_V1"
                 and type(payload.get("repeat")) is int and payload.get("repeat") == repeat,
                 "REPEAT_LABEL_OR_SCOPE_MISMATCH")
        verify_model_output_pairing(examples, payload["rows"])
    return {
        "schema": "commandmed.v5.s1.source-case-pseudoreplication-audit.v1",
        "status": "PASS_SOURCE_CASE_TO_TASK_ONE_TO_ONE_DEVELOPMENT_ONLY",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "riskcalcs_sha256": SOURCE_SHA,
        "selected_manifest_sha256": MANIFEST_SHA,
        "rule_dataset_sha256": RULE_DATASET_SHA,
        "case_generator_sha256": CASE_GENERATOR_SHA,
        "full_r1_r2_source_to_prompt_replay": True,
        "repeatabilities": [1, 2],
        "original_decision_matrix_shas": {str(k): digest for k, (_, digest) in RUN_PATHS.items()},
        "two_prompt_variants_independent": False,
        "source_case_unit": "case_id, one-to-one with development task_id",
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "training": False,
        "clinical_validity": False,
        "final_statistical_power_qualified": False,
        **output,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--riskcalcs-source", type=Path, required=True,
                        help="Local copy of fixed public RiskCalcs blob, SHA-256 checked before use")
    args = parser.parse_args()
    print(json.dumps(audit(args.riskcalcs_source), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
