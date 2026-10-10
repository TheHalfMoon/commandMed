#!/usr/bin/env python3
"""Descriptive S1 intervention-paired source-task variance inventory.

Development/calibration only. Does not freeze an endpoint family, nuisance bound,
confirmatory power, meaningful margins, or clinical-performance claims.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from pathlib import Path
from typing import Any

from v5_s1_repeatability_analysis import PRIMARY_METRICS, _row_metrics

REPO = Path(__file__).resolve().parents[1]
DEVELOPMENT = REPO / "artifacts/v5/development"
EVAL_SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")
EVAL_PER_SPLIT = 3840
ORDERED_VARIANTS = ("canonical", "transformed")
IDENTITY_FIELDS = (
    "task_id", "calculator_id", "split", "variant", "target_index",
    "option_a_semantic", "prompt_sha256",
)
BASELINE_PATH = Path("s1-colab-resource-qualification/b1-complete-2026-10-04/baseline-decision-matrix.json")
REPEAT_R1_PATH = Path(
    "s1-kaggle-repeatability-runs/repeat-1-v1-2026-10-09/evidence/repeatability-decision-matrix.json"
)
CANDIDATES = {
    **{
        f"B1_{seed}": (
            Path(f"s1-colab-resource-qualification/b1-complete-2026-10-04/b1-seed-{seed}-decision-matrix.json"),
            "B1_TYPED_V1", seed,
        )
        for seed in (11, 29, 47)
    },
    **{
        f"C1_{seed}": (
            Path(f"s1-kaggle-adapters/c1-seed-{seed}-v{version}-2026-10-08/evidence/adapter-decision-matrix.json"),
            "C1_CRDI_V1", seed,
        )
        for seed, version in ((11, 4), (29, 1), (47, 1))
    },
    **{
        f"C2_{seed}": (
            Path(f"s1-kaggle-c2-adapters/c2-seed-{seed}-v{version}-2026-10-09/evidence/adapter-decision-matrix.json"),
            "C2_CRDI_RETAIN_V1", seed,
        )
        for seed, version in ((11, 2), (29, 1), (47, 1))
    },
}


class DescriptiveInventoryContractError(ValueError):
    """Bad or unmatched development evidence; never impute missing cases."""


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path, intervention: str, seed: int | None = None) -> dict[str, Any]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("complete") is not True or obj.get("intervention") != intervention:
        raise DescriptiveInventoryContractError("WRONG_OR_INCOMPLETE_INTERVENTION")
    if seed is not None and (type(obj.get("seed")) is not int or obj["seed"] != seed):
        raise DescriptiveInventoryContractError("SEED_IDENTITY_MISMATCH")
    rows = obj.get("rows")
    if not isinstance(rows, list) or len(rows) != 16384:
        raise DescriptiveInventoryContractError("INCOMPLETE_16384_ROW_DEVELOPMENT_MATRIX")
    return obj


def _validate_and_index(rows: list[dict[str, Any]]) -> dict[str, tuple[dict[str, float], dict, dict]]:
    if len(rows) != 16384:
        raise DescriptiveInventoryContractError("INCOMPLETE_16384_ROW_DEVELOPMENT_MATRIX")
    index = {}
    for position in range(0, len(rows), 2):
        canonical, transformed = rows[position : position + 2]
        if (canonical.get("variant"), transformed.get("variant")) != ORDERED_VARIANTS:
            raise DescriptiveInventoryContractError("CANONICAL_TRANSFORMED_PAIR_ORDER_MISMATCH")
        if any(canonical.get(field) != transformed.get(field) for field in (
            "task_id", "calculator_id", "split", "target_index", "option_a_semantic",
        )):
            raise DescriptiveInventoryContractError("SOURCE_TASK_PAIR_MISMATCH")
        for row in (canonical, transformed):
            logits = row.get("logits")
            if (not isinstance(logits, list) or len(logits) != 2
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in logits)):
                raise DescriptiveInventoryContractError("INVALID_FINITE_LOGITS")
            if any(field not in row for field in IDENTITY_FIELDS):
                raise DescriptiveInventoryContractError("MISSING_IDENTITY_FIELD")
        task_id = canonical["task_id"]
        if not isinstance(task_id, str) or not task_id or task_id in index:
            raise DescriptiveInventoryContractError("DUPLICATE_OR_INVALID_SOURCE_TASK")
        if canonical["split"] in EVAL_SPLITS:
            index[task_id] = (_row_metrics(canonical, transformed), canonical, transformed)
    counts = {split: sum(row["split"] == split for _, row, _ in index.values()) for split in EVAL_SPLITS}
    if any(counts[split] != EVAL_PER_SPLIT for split in EVAL_SPLITS):
        raise DescriptiveInventoryContractError("INCOMPLETE_DEVELOPMENT_EVALUATION_SPLITS")
    return index


def _compute_pair(
    baseline: dict[str, tuple[dict[str, float], dict, dict]],
    candidate: dict[str, tuple[dict[str, float], dict, dict]],
) -> dict[str, dict[str, Any]]:
    if tuple(baseline) != tuple(candidate):
        raise DescriptiveInventoryContractError("ORDERED_SOURCE_TASK_SET_CHANGED")
    differences = {split: {metric: [] for metric in PRIMARY_METRICS} for split in EVAL_SPLITS}
    for task_id in baseline:
        b_metrics, b_c, b_t = baseline[task_id]
        c_metrics, c_c, c_t = candidate[task_id]
        for b, c in ((b_c, c_c), (b_t, c_t)):
            if any(b.get(field) != c.get(field) for field in IDENTITY_FIELDS):
                raise DescriptiveInventoryContractError("INTERVENTION_CHANGED_SOURCE_OR_PROMPT_IDENTITY")
        split = b_c["split"]
        for metric in PRIMARY_METRICS:
            differences[split][metric].append(c_metrics[metric] - b_metrics[metric])
    result = {}
    for split, metrics in differences.items():
        result[split] = {}
        for metric, values in metrics.items():
            if len(values) != EVAL_PER_SPLIT or not all(math.isfinite(value) for value in values):
                raise DescriptiveInventoryContractError("MISSING_OR_NONFINITE_PAIRED_DELTA")
            result[split][metric] = {
                "task_count": len(values),
                "mean_delta_raw_orientation": statistics.fmean(values),
                "paired_source_task_sample_sd": statistics.stdev(values),
                "min_delta": min(values),
                "max_delta": max(values),
            }
    return result


def build_inventory() -> dict[str, Any]:
    baseline_path = DEVELOPMENT / BASELINE_PATH
    r1_path = DEVELOPMENT / REPEAT_R1_PATH
    baseline = _load(baseline_path, "BASELINE_V1")
    r1 = _load(r1_path, "BASELINE_V1")
    if r1.get("repeat") != 1 or any(
        any(a.get(field) != b.get(field) for field in IDENTITY_FIELDS + ("logits",))
        for a, b in zip(baseline["rows"], r1["rows"])
    ):
        raise DescriptiveInventoryContractError("BASELINE_R1_SOURCE_OR_LOGITS_MISMATCH")
    base_index = _validate_and_index(baseline["rows"])
    results = {}
    for name, (relative, intervention, seed) in sorted(CANDIDATES.items()):
        path = DEVELOPMENT / relative
        payload = _load(path, intervention, seed)
        candidate = _validate_and_index(payload["rows"])
        results[name] = {
            "artifact_path": (Path("artifacts/v5/development") / relative).as_posix(),
            "artifact_sha256": _sha(path),
            "intervention": intervention,
            "seed": seed,
            "splits": _compute_pair(base_index, candidate),
        }
    return {
        "schema": "commandmed.v5.descriptive-development-paired-sd-inventory.v1",
        "status": "EXPLORATORY_NUISANCE_NOT_FROZEN_POWER_INPUT",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "confirmatory": False,
        "reserve": False,
        "source_task_cluster": "task_id",
        "variance_estimator": "sample_stddev_ddof_1_within_each_split_and_intervention_seed",
        "delta_orientation": "candidate_metric_minus_unchanged_baseline_metric",
        "primary_metrics": list(PRIMARY_METRICS),
        "baseline_sha256": _sha(baseline_path),
        "verified_r1_reference_sha256": _sha(r1_path),
        "calibration_and_training_excluded_from_sd": True,
        "training_seed_uncertainty_not_included_in_paired_item_sd": True,
        "primary_non_target_family_size": None,
        "confirmatory_power_claim": False,
        "intervention_results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_inventory()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"status": result["status"], "intervention_count": len(result["intervention_results"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
