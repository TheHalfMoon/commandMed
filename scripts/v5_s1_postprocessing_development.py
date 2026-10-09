#!/usr/bin/env python3
"""Prospectively frozen V5 S1 development-only post-processing analysis.

Reads only durable development/calibration decision matrices. No model weights,
network access, confirmatory/reserve identities, training, or threshold/bin
optimization outside the frozen rules in the adjacent conventions record.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from statistics import fmean
from typing import Any, Callable, Iterable, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.commandmed.reliability_v5.diagnostics import (
    reliability_bins,
    weighted_calibration_gap,
)
from src.commandmed.reliability_v5.probability import (
    multiclass_brier,
    negative_log_likelihood,
    softmax,
)
from src.commandmed.reliability_v5.selection_bias import (
    align_display_to_semantic,
    debias_display_distribution,
    estimate_display_slot_prior,
)

SPLIT_COUNTS = {
    "S1_TRAIN": 256,
    "S1_DEV_EVAL": 3840,
    "S1_CAL_TUNE": 256,
    "S1_CAL_EVAL": 3840,
}
EVAL_SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")
VARIANTS = ("canonical", "transformed")
LOG_T_MIN = -6.0
LOG_T_MAX = 6.0
LOG_T_STEP = 0.005
LOG_T_COUNT = 2401
D1_RISK_TARGET = 0.05
CALIBRATION_BINS = (10, 15, 20)
PRIMARY_CALIBRATION_BINS = 15


class PostprocessingError(RuntimeError):
    """Fail-closed development post-processing error."""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _finite_pair(values: Any, field: str) -> tuple[float, float]:
    if not isinstance(values, list) or len(values) != 2:
        raise PostprocessingError(f"{field}: expected two logits")
    pair = tuple(float(value) for value in values)
    if any(not math.isfinite(value) for value in pair):
        raise PostprocessingError(f"{field}: nonfinite value")
    return pair  # type: ignore[return-value]


def _semantic_permutation(option_a_semantic: str) -> tuple[int, int]:
    if option_a_semantic == "MATCH":
        return (0, 1)
    if option_a_semantic == "MISMATCH":
        return (1, 0)
    raise PostprocessingError("option_a_semantic: expected MATCH or MISMATCH")


def _semantic_target(row: dict[str, Any]) -> int:
    target = row.get("target_index")
    if target not in (0, 1):
        raise PostprocessingError("target_index: expected 0 or 1")
    mapping = _semantic_permutation(str(row.get("option_a_semantic")))
    return mapping[target]


def _display_probabilities(row: dict[str, Any]) -> tuple[float, float]:
    return softmax(_finite_pair(row.get("logits"), "logits"))  # type: ignore[return-value]


def _semantic_probabilities(display: Sequence[float], row: dict[str, Any]) -> tuple[float, float]:
    return align_display_to_semantic(display, _semantic_permutation(str(row.get("option_a_semantic"))))  # type: ignore[return-value]


def _js(left: Sequence[float], right: Sequence[float]) -> float:
    if len(left) != 2 or len(right) != 2:
        raise PostprocessingError("semantic JS expects two-class probabilities")
    mean = ((left[0] + right[0]) / 2.0, (left[1] + right[1]) / 2.0)
    total = 0.0
    for p, q, m in zip(left, right, mean):
        if p > 0.0:
            total += 0.5 * p * math.log(p / m)
        if q > 0.0:
            total += 0.5 * q * math.log(q / m)
    if not math.isfinite(total) or total < -1e-15:
        raise PostprocessingError("nonfinite or negative semantic JS")
    return max(0.0, total)


def validate_complete_matrix(payload: dict[str, Any]) -> list[dict[str, Any]]:
    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 16384:
        raise PostprocessingError("expected exactly 16384 decision rows")
    seen: set[tuple[str, str]] = set()
    counts: dict[tuple[str, str], int] = {}
    tasks: dict[str, set[str]] = {}
    for position, row in enumerate(rows):
        if not isinstance(row, dict):
            raise PostprocessingError(f"row {position}: expected object")
        task_id = row.get("task_id")
        split = row.get("split")
        variant = row.get("variant")
        if not isinstance(task_id, str) or len(task_id) != 64:
            raise PostprocessingError(f"row {position}: invalid task_id")
        if split not in SPLIT_COUNTS or variant not in VARIANTS:
            raise PostprocessingError(f"row {position}: invalid split/variant")
        key = (task_id, variant)
        if key in seen:
            raise PostprocessingError(f"duplicate task/variant:{task_id}:{variant}")
        seen.add(key)
        counts[(split, variant)] = counts.get((split, variant), 0) + 1
        tasks.setdefault(task_id, set()).add(variant)
        _finite_pair(row.get("logits"), f"row {position} logits")
        _semantic_target(row)
    expected = {(split, variant): count for split, count in SPLIT_COUNTS.items() for variant in VARIANTS}
    if counts != expected:
        raise PostprocessingError(f"split counts mismatch:{counts}")
    if len(tasks) != 8192 or any(variants != set(VARIANTS) for variants in tasks.values()):
        raise PostprocessingError("expected 8192 paired canonical/transformed tasks")
    return rows


def _rows(rows: Iterable[dict[str, Any]], split: str, variant: str | None = None) -> list[dict[str, Any]]:
    return [
        row
        for row in rows
        if row["split"] == split and (variant is None or row["variant"] == variant)
    ]


def _temperature_grid() -> tuple[float, ...]:
    values = tuple(LOG_T_MIN + index * LOG_T_STEP for index in range(LOG_T_COUNT))
    if abs(values[-1] - LOG_T_MAX) > 1e-12:
        raise PostprocessingError("temperature grid endpoint mismatch")
    return values


def fit_temperature(
    rows: Sequence[dict[str, Any]],
    probability_fn: Callable[[dict[str, Any], float], Sequence[float]],
) -> dict[str, Any]:
    if len(rows) != 256 or any(row["split"] != "S1_CAL_TUNE" or row["variant"] != "canonical" for row in rows):
        raise PostprocessingError("temperature fit requires 256 canonical S1_CAL_TUNE rows")
    candidates = []
    for log_t in _temperature_grid():
        temperature = math.exp(log_t)
        losses = []
        for row in rows:
            probabilities = tuple(probability_fn(row, temperature))
            losses.append(negative_log_likelihood(probabilities, int(row["target_index"])))
        nll = fmean(losses)
        if not math.isfinite(nll):
            raise PostprocessingError("nonfinite temperature-fit NLL")
        candidates.append((nll, abs(log_t), log_t, temperature))
    best = min(candidates, key=lambda item: (item[0], item[1], item[2]))
    return {
        "temperature": best[3],
        "log_temperature": best[2],
        "tuning_mean_nll": best[0],
        "grid_log_temperature_min": LOG_T_MIN,
        "grid_log_temperature_max": LOG_T_MAX,
        "grid_step": LOG_T_STEP,
        "grid_count": LOG_T_COUNT,
        "boundary_selected": best[2] in (LOG_T_MIN, LOG_T_MAX),
    }


def _a1_display(row: dict[str, Any], temperature: float) -> tuple[float, float]:
    logits = _finite_pair(row["logits"], "logits")
    return softmax((logits[0] / temperature, logits[1] / temperature))  # type: ignore[return-value]


def _fit_a2_prior(
    rows: Sequence[dict[str, Any]],
    transform: Callable[[dict[str, Any]], Sequence[float]],
) -> tuple[float, float]:
    tune = _rows(rows, "S1_CAL_TUNE")
    if len(tune) != 512:
        raise PostprocessingError("A2 fit requires all 512 S1_CAL_TUNE rows")
    prior = estimate_display_slot_prior((transform(row) for row in tune), epsilon=1e-12)
    if len(prior) != 2:
        raise PostprocessingError("A2 prior must have two slots")
    return prior  # type: ignore[return-value]


def _condition_metrics(
    rows: Sequence[dict[str, Any]],
    transform: Callable[[dict[str, Any]], Sequence[float]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for split in EVAL_SPLITS:
        split_result: dict[str, Any] = {}
        by_task: dict[str, dict[str, Any]] = {}
        for variant in VARIANTS:
            chosen = _rows(rows, split, variant)
            if len(chosen) != SPLIT_COUNTS[split]:
                raise PostprocessingError(f"{split}/{variant}: row count mismatch")
            accuracies = []
            nlls = []
            briers = []
            match_probabilities = []
            match_outcomes = []
            for row in chosen:
                display = tuple(float(value) for value in transform(row))
                semantic = _semantic_probabilities(display, row)
                semantic_target = _semantic_target(row)
                predicted = 0 if semantic[0] >= semantic[1] else 1
                accuracy = 1.0 if predicted == semantic_target else 0.0
                target_display = int(row["target_index"])
                accuracies.append(accuracy)
                nlls.append(negative_log_likelihood(display, target_display))
                briers.append(multiclass_brier(display, target_display))
                match_probabilities.append(semantic[0])
                match_outcomes.append(1 if semantic_target == 0 else 0)
                task = by_task.setdefault(row["task_id"], {})
                task[variant] = {
                    "semantic_probabilities": list(semantic),
                    "accuracy": accuracy,
                    "nll": nlls[-1],
                    "brier": briers[-1],
                }
            calibration = {}
            for bins in CALIBRATION_BINS:
                edges = tuple(index / bins for index in range(bins + 1))
                table = reliability_bins(match_probabilities, match_outcomes, bin_edges=edges)
                calibration[str(bins)] = {
                    "weighted_absolute_gap": weighted_calibration_gap(table),
                    "bins": [
                        {
                            "lower": cell.lower,
                            "upper": cell.upper,
                            "count": cell.count,
                            "mean_probability_match": cell.mean_confidence,
                            "empirical_match_rate": cell.event_rate,
                            "absolute_gap": cell.absolute_gap,
                        }
                        for cell in table
                    ],
                }
            split_result[variant] = {
                "count": len(chosen),
                "accuracy": fmean(accuracies),
                "nll": fmean(nlls),
                "brier": fmean(briers),
                "calibration_primary_bins": PRIMARY_CALIBRATION_BINS,
                "calibration": calibration,
            }
        js_values = []
        for task_id, pair in by_task.items():
            if set(pair) != set(VARIANTS):
                raise PostprocessingError(f"missing variant pair:{task_id}")
            js_values.append(_js(pair["canonical"]["semantic_probabilities"], pair["transformed"]["semantic_probabilities"]))
        split_result["semantic_js"] = {
            "count": len(js_values),
            "mean": fmean(js_values),
            "max": max(js_values),
        }
        result[split] = split_result
    return result


def _baseline_transform(row: dict[str, Any]) -> tuple[float, float]:
    return _display_probabilities(row)


def tune_d1(rows: Sequence[dict[str, Any]]) -> dict[str, Any]:
    tune = _rows(rows, "S1_CAL_TUNE", "canonical")
    if len(tune) != 256:
        raise PostprocessingError("D1 tuning requires 256 canonical S1_CAL_TUNE rows")
    records = []
    for row in tune:
        semantic = _semantic_probabilities(_baseline_transform(row), row)
        score = max(semantic)
        prediction = 0 if semantic[0] >= semantic[1] else 1
        loss = 0.0 if prediction == _semantic_target(row) else 1.0
        records.append((score, loss))
    feasible = []
    for threshold in sorted({score for score, _ in records}, reverse=True):
        accepted = [loss for score, loss in records if score >= threshold]
        if not accepted:
            continue
        risk = fmean(accepted)
        coverage = len(accepted) / len(records)
        if risk <= D1_RISK_TARGET:
            feasible.append((coverage, threshold, risk, len(accepted)))
    if not feasible:
        return {
            "status": "NO_FEASIBLE_NONZERO_COVERAGE",
            "risk_target": D1_RISK_TARGET,
            "threshold": None,
            "tuning_risk": None,
            "tuning_coverage": 0.0,
            "accepted": 0,
            "total": len(records),
        }
    coverage, threshold, risk, accepted = max(feasible, key=lambda item: (item[0], item[1]))
    return {
        "status": "FEASIBLE",
        "risk_target": D1_RISK_TARGET,
        "threshold": threshold,
        "tuning_risk": risk,
        "tuning_coverage": coverage,
        "accepted": accepted,
        "total": len(records),
    }


def _aurc_tie_block(scores: Sequence[float], losses: Sequence[float]) -> dict[str, Any]:
    if len(scores) != len(losses) or not scores:
        raise PostprocessingError("AURC requires equal non-empty score/loss sequences")
    groups: dict[float, list[float]] = {}
    for score, loss in zip(scores, losses):
        if not math.isfinite(score) or not math.isfinite(loss):
            raise PostprocessingError("AURC received nonfinite score/loss")
        groups.setdefault(score, []).append(loss)
    total = len(scores)
    accepted = 0
    error_sum = 0.0
    previous_coverage = 0.0
    area = 0.0
    curve = []
    for score in sorted(groups, reverse=True):
        block = groups[score]
        accepted += len(block)
        error_sum += math.fsum(block)
        coverage = accepted / total
        risk = error_sum / accepted
        area += (coverage - previous_coverage) * risk
        previous_coverage = coverage
        curve.append(
            {
                "threshold_score": score,
                "coverage": coverage,
                "risk": risk,
                "accepted": accepted,
                "total": total,
                "tie_block_count": len(block),
            }
        )
    return {"aurc_step_tie_block": area, "curve": curve}


def evaluate_d1(rows: Sequence[dict[str, Any]], tuning: dict[str, Any]) -> dict[str, Any]:
    result = {"tuning": tuning, "evaluation": {}}
    for split in EVAL_SPLITS:
        split_result = {}
        for variant in VARIANTS:
            chosen = _rows(rows, split, variant)
            scores = []
            losses = []
            for row in chosen:
                semantic = _semantic_probabilities(_baseline_transform(row), row)
                score = max(semantic)
                prediction = 0 if semantic[0] >= semantic[1] else 1
                loss = 0.0 if prediction == _semantic_target(row) else 1.0
                scores.append(score)
                losses.append(loss)
            curve = _aurc_tie_block(scores, losses)
            threshold = tuning["threshold"]
            if threshold is None:
                policy = {"coverage": 0.0, "risk": None, "accepted": 0, "total": len(chosen)}
            else:
                accepted_losses = [loss for score, loss in zip(scores, losses) if score >= threshold]
                policy = {
                    "coverage": len(accepted_losses) / len(chosen),
                    "risk": fmean(accepted_losses) if accepted_losses else None,
                    "accepted": len(accepted_losses),
                    "total": len(chosen),
                }
            split_result[variant] = {**policy, **curve}
        result["evaluation"][split] = split_result
    return result


def _reviewed_c1_folders(repo: Path) -> dict[int, Path]:
    root = repo / "artifacts/v5/development/s1-kaggle-adapters"
    result = {}
    for seed in (11, 29, 47):
        candidates = list(root.glob(f"c1-seed-{seed}-v*-*"))
        valid = []
        for folder in candidates:
            receipt = folder / "export-verification-receipt.json"
            review = folder / "validation-and-review.json"
            matrix = folder / "evidence" / "adapter-decision-matrix.json"
            if not receipt.is_file() or not review.is_file() or not matrix.is_file():
                continue
            r = json.loads(receipt.read_text(encoding="utf-8"))
            v = json.loads(review.read_text(encoding="utf-8"))
            if (
                r.get("status") == "PASS_MODEL_FREE_EXPORT_VERIFICATION"
                and r.get("seed") == seed
                and r.get("intervention") == "C1_CRDI_V1"
                and r.get("durable_export_verified") is True
                and v.get("spend_usd") == 0
                and str(v.get("host_review", "")).startswith("NO_MATERIAL_BLOCKER")
            ):
                valid.append(folder)
        if len(valid) != 1:
            raise PostprocessingError(f"expected one reviewed C1 folder for seed {seed}, got {len(valid)}")
        result[seed] = valid[0]
    return result


def analyze(repo: Path) -> dict[str, Any]:
    baseline_path = repo / "artifacts/v5/development/s1-colab-resource-qualification/b1-complete-2026-10-04/baseline-decision-matrix.json"
    if not baseline_path.is_file():
        raise PostprocessingError("durable baseline matrix missing")
    baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline_rows = validate_complete_matrix(baseline_payload)

    cal_canonical = _rows(baseline_rows, "S1_CAL_TUNE", "canonical")
    a1_fit = fit_temperature(cal_canonical, lambda row, t: _a1_display(row, t))
    a1 = lambda row: _a1_display(row, a1_fit["temperature"])

    a2_prior = _fit_a2_prior(baseline_rows, _baseline_transform)
    a2 = lambda row: debias_display_distribution(_baseline_transform(row), a2_prior, epsilon=1e-12)

    a1_then_a2_prior = _fit_a2_prior(baseline_rows, a1)
    a1_then_a2 = lambda row: debias_display_distribution(a1(row), a1_then_a2_prior, epsilon=1e-12)

    a2_cal_canonical = _rows(baseline_rows, "S1_CAL_TUNE", "canonical")
    def a2_log_probability_scaled(row: dict[str, Any], temperature: float) -> tuple[float, float]:
        corrected = a2(row)
        logs = tuple(math.log(value) for value in corrected)
        return softmax((logs[0] / temperature, logs[1] / temperature))  # type: ignore[return-value]
    a2_then_a1_fit = fit_temperature(a2_cal_canonical, a2_log_probability_scaled)
    a2_then_a1 = lambda row: a2_log_probability_scaled(row, a2_then_a1_fit["temperature"])

    result: dict[str, Any] = {
        "schema": "commandmed.v5.s1-postprocessing-development.v1",
        "scope": "DEVELOPMENT_CALIBRATION_ONLY",
        "confirmatory": False,
        "reserve": False,
        "claim_promotion": False,
        "baseline_matrix_sha256": sha256_file(baseline_path),
        "conventions": {
            "calibration_event": "SEMANTIC_MATCH",
            "calibration_primary_bins": PRIMARY_CALIBRATION_BINS,
            "calibration_sensitivity_bins": list(CALIBRATION_BINS),
            "temperature_log_grid": {
                "min": LOG_T_MIN,
                "max": LOG_T_MAX,
                "step": LOG_T_STEP,
                "count": LOG_T_COUNT,
            },
            "d1_risk_target": D1_RISK_TARGET,
            "d1_score": "MAX_SEMANTIC_PROBABILITY",
            "d1_loss": "TOP1_SEMANTIC_0_1_ERROR",
            "aurc": "RIGHT_CONTINUOUS_TIE_BLOCK_STEP_AREA",
        },
        "tuning": {
            "A1_TS_V1": a1_fit,
            "A2_SELBIAS_V1": {"display_slot_prior": list(a2_prior), "epsilon": 1e-12},
            "A1_THEN_A2": {
                "temperature": a1_fit,
                "display_slot_prior_after_a1": list(a1_then_a2_prior),
                "epsilon": 1e-12,
            },
            "A2_THEN_A1": {
                "display_slot_prior": list(a2_prior),
                "temperature_after_a2": a2_then_a1_fit,
                "epsilon": 1e-12,
            },
        },
        "results": {
            "BASELINE_V1": _condition_metrics(baseline_rows, _baseline_transform),
            "A1_TS_V1": _condition_metrics(baseline_rows, a1),
            "A2_SELBIAS_V1": _condition_metrics(baseline_rows, a2),
            "A1_THEN_A2": _condition_metrics(baseline_rows, a1_then_a2),
            "A2_THEN_A1": _condition_metrics(baseline_rows, a2_then_a1),
        },
    }

    d1_tuning = tune_d1(baseline_rows)
    result["tuning"]["D1_DEFER_V1"] = d1_tuning
    result["results"]["D1_DEFER_V1"] = evaluate_d1(baseline_rows, d1_tuning)

    c1_compositions = {}
    for seed, folder in _reviewed_c1_folders(repo).items():
        matrix_path = folder / "evidence" / "adapter-decision-matrix.json"
        payload = json.loads(matrix_path.read_text(encoding="utf-8"))
        rows = validate_complete_matrix(payload)
        cal = _rows(rows, "S1_CAL_TUNE", "canonical")
        fit = fit_temperature(cal, lambda row, t: _a1_display(row, t))
        transform = lambda row, temperature=fit["temperature"]: _a1_display(row, temperature)
        c1_compositions[str(seed)] = {
            "matrix_sha256": sha256_file(matrix_path),
            "temperature_fit": fit,
            "results": _condition_metrics(rows, transform),
        }
    result["results"]["C1_THEN_A1_BY_SEED"] = c1_compositions

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = analyze(args.repo.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status":"PASS_POSTPROCESSING_DEVELOPMENT","output":str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
