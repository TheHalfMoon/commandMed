"""Frozen development-only unchanged-base repeatability analysis.

No model/network access. The estimator is frozen in
V5_S1_REPEATABILITY_METHOD_FREEZE_2026-10-09.md.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from commandmed.reliability_v5.probability import (
    multiclass_brier,
    negative_log_likelihood,
    softmax,
)

EVAL_SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")
PRIMARY_METRICS = (
    "canonical_accuracy",
    "canonical_nll",
    "canonical_brier",
    "semantic_js",
)
SECONDARY_METRICS = (
    "transformed_accuracy",
    "transformed_nll",
    "transformed_brier",
)


class RepeatabilityContractError(ValueError):
    """Raised when a repeatability artifact violates the frozen contract."""


def _semantic(probabilities: tuple[float, float], option_a_semantic: str) -> tuple[float, float]:
    if option_a_semantic == "MATCH":
        return probabilities
    if option_a_semantic == "MISMATCH":
        return probabilities[1], probabilities[0]
    raise RepeatabilityContractError("INVALID_OPTION_A_SEMANTIC")


def _js(left: tuple[float, float], right: tuple[float, float]) -> float:
    midpoint = tuple((a + b) / 2.0 for a, b in zip(left, right))
    total = 0.0
    for distribution in (left, right):
        for value, middle in zip(distribution, midpoint):
            if value > 0.0:
                total += 0.5 * value * math.log(value / middle)
    if not math.isfinite(total) or total < -1e-15:
        raise RepeatabilityContractError("INVALID_SEMANTIC_JS")
    return max(0.0, total)


def _row_metrics(canonical: dict[str, Any], transformed: dict[str, Any]) -> dict[str, float]:
    target = canonical["target_index"]
    if transformed["target_index"] != target:
        raise RepeatabilityContractError("TARGET_CHANGED_BETWEEN_VARIANTS")
    if canonical["option_a_semantic"] != transformed["option_a_semantic"]:
        raise RepeatabilityContractError("SEMANTIC_LEGEND_CHANGED_BETWEEN_VARIANTS")
    c_prob = softmax(canonical["logits"])
    t_prob = softmax(transformed["logits"])
    c_sem = _semantic(c_prob, canonical["option_a_semantic"])
    t_sem = _semantic(t_prob, transformed["option_a_semantic"])
    return {
        "canonical_accuracy": float(max(range(2), key=c_prob.__getitem__) == target),
        "canonical_nll": min(
            negative_log_likelihood(c_prob, target),
            -math.log(1e-15),
        ),
        "canonical_brier": multiclass_brier(c_prob, target),
        "transformed_accuracy": float(max(range(2), key=t_prob.__getitem__) == target),
        "transformed_nll": min(
            negative_log_likelihood(t_prob, target),
            -math.log(1e-15),
        ),
        "transformed_brier": multiclass_brier(t_prob, target),
        "semantic_js": _js(c_sem, t_sem),
    }


def _index_rows(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if payload.get("complete") is not True or payload.get("intervention") != "BASELINE_V1":
        raise RepeatabilityContractError("INCOMPLETE_OR_WRONG_INTERVENTION")
    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 16384:
        raise RepeatabilityContractError("REPEATABILITY_MATRIX_MUST_HAVE_16384_ROWS")
    index: dict[str, dict[str, Any]] = {}
    last_task = None
    expected_variant = "canonical"
    for position, row in enumerate(rows):
        required = (
            "task_id",
            "calculator_id",
            "split",
            "variant",
            "target_index",
            "option_a_semantic",
            "prompt_sha256",
            "logits",
        )
        if any(key not in row for key in required):
            raise RepeatabilityContractError(f"MISSING_ROW_FIELD:{position}")
        variant = row["variant"]
        if variant not in ("canonical", "transformed"):
            raise RepeatabilityContractError("INVALID_VARIANT")
        if variant != expected_variant:
            raise RepeatabilityContractError("CANONICAL_TRANSFORMED_ORDER_MISMATCH")
        if variant == "canonical":
            last_task = row["task_id"]
            expected_variant = "transformed"
        else:
            if row["task_id"] != last_task:
                raise RepeatabilityContractError("TASK_PAIR_ORDER_MISMATCH")
            expected_variant = "canonical"
        logits = row["logits"]
        if (
            not isinstance(logits, list)
            or len(logits) != 2
            or any(not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) for v in logits)
        ):
            raise RepeatabilityContractError("INVALID_LOGITS")
        key = f"{row['task_id']}|{variant}"
        if key in index:
            raise RepeatabilityContractError("DUPLICATE_TASK_VARIANT")
        index[key] = row
    if expected_variant != "canonical":
        raise RepeatabilityContractError("INCOMPLETE_FINAL_PAIR")
    if len({row["task_id"] for row in rows}) != 8192:
        raise RepeatabilityContractError("EXPECTED_8192_SOURCE_TASKS")
    return index


def _nearest_rank_95(values: list[float]) -> float:
    if not values:
        raise RepeatabilityContractError("EMPTY_REPEATABILITY_VECTOR")
    if any(not math.isfinite(value) or value < 0.0 for value in values):
        raise RepeatabilityContractError("INVALID_REPEATABILITY_VALUE")
    ordered = sorted(values)
    return ordered[math.ceil(0.95 * len(ordered)) - 1]


def compare(payload_r1: dict[str, Any], payload_r2: dict[str, Any]) -> dict[str, Any]:
    # Enforce the prospectively frozen R1 -> R2 pairing before computing any metric.
    # Without this guard, passing R1 twice falsely yields zero repeatability.
    if (
        type(payload_r1.get("repeat")) is not int
        or payload_r1["repeat"] != 1
        or type(payload_r2.get("repeat")) is not int
        or payload_r2["repeat"] != 2
    ):
        raise RepeatabilityContractError("DISTINCT_ORDERED_REPEAT_IDENTITIES_REQUIRED")
    r1 = _index_rows(payload_r1)
    r2 = _index_rows(payload_r2)
    if tuple(r1) != tuple(r2):
        raise RepeatabilityContractError("ORDERED_IDENTITY_SET_MISMATCH")
    by_split: dict[str, dict[str, list[float]]] = {
        split: {metric: [] for metric in PRIMARY_METRICS + SECONDARY_METRICS}
        for split in EVAL_SPLITS
    }
    task_ids = []
    for key in r1:
        if not key.endswith("|canonical"):
            continue
        task_id = key[:-10]
        c1, t1 = r1[key], r1[f"{task_id}|transformed"]
        c2, t2 = r2[key], r2[f"{task_id}|transformed"]
        identity_fields = (
            "task_id",
            "calculator_id",
            "split",
            "variant",
            "target_index",
            "option_a_semantic",
            "prompt_sha256",
        )
        for a, b in ((c1, c2), (t1, t2)):
            if any(a[field] != b[field] for field in identity_fields):
                raise RepeatabilityContractError("CROSS_RUN_IDENTITY_MISMATCH")
        m1 = _row_metrics(c1, t1)
        m2 = _row_metrics(c2, t2)
        split = c1["split"]
        if split in by_split:
            task_ids.append(task_id)
            for metric in PRIMARY_METRICS + SECONDARY_METRICS:
                by_split[split][metric].append(abs(m2[metric] - m1[metric]))
    counts = {split: len(by_split[split]["canonical_nll"]) for split in EVAL_SPLITS}
    if counts != {"S1_DEV_EVAL": 3840, "S1_CAL_EVAL": 3840}:
        raise RepeatabilityContractError(f"EVAL_COUNTS_MISMATCH:{counts}")
    summary: dict[str, Any] = {}
    for metric in PRIMARY_METRICS + SECONDARY_METRICS:
        split_rows = {}
        for split in EVAL_SPLITS:
            values = by_split[split][metric]
            split_rows[split] = {
                "count": len(values),
                "mean_absolute_difference": math.fsum(values) / len(values),
                "max_absolute_difference": max(values),
                "q95_nearest_rank": _nearest_rank_95(values),
            }
        summary[metric] = {
            "splits": split_rows,
            "repeatability95": max(
                split_rows["S1_DEV_EVAL"]["q95_nearest_rank"],
                split_rows["S1_CAL_EVAL"]["q95_nearest_rank"],
            ),
            "primary": metric in PRIMARY_METRICS,
        }
    return {
        "schema": "commandmed.v5.s1-unchanged-base-repeatability.v1",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "confirmatory": False,
        "reserve": False,
        "source_task_cluster": "task_id",
        "repeat_count": 2,
        "eval_task_count": len(task_ids),
        "percentile": "NEAREST_RANK_95_NO_INTERPOLATION",
        "primary_metrics": list(PRIMARY_METRICS),
        "secondary_metrics": list(SECONDARY_METRICS),
        "metrics": summary,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeat-1", type=Path, required=True)
    parser.add_argument("--repeat-2", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    first = json.loads(args.repeat_1.read_text(encoding="utf-8"))
    second = json.loads(args.repeat_2.read_text(encoding="utf-8"))
    result = compare(first, second)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "PASS_REPEATABILITY_ANALYSIS", "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
