#!/usr/bin/env python3
"""Source-bound calculator-level paired-effect ICC diagnostics; DEVELOPMENT ONLY.

This one-way descriptive ANOVA is NOT a mixed model, a population-calculator
inference, a crossed training-seed variance estimator, or a valid power certificate.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import statistics
from typing import Any, Sequence

import v5_s1_development_paired_sd_inventory as source
from v5_s1_repeatability_analysis import PRIMARY_METRICS

CALCULATORS_PER_SPLIT = 64
EVAL_TASKS_PER_CALCULATOR = 60
SEEDS = frozenset((11, 29, 47))
FROZEN_REFERENCE_SHA256 = "b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd"
# Exact SHA-256 for each previously source-bound original development matrix.
EXPECTED_INPUT_SHA256 = {
    'B1_11': '24f6be4368723f403bcb5c017ea79934a17986d517c57411df2012ca6826baf0',
    'B1_29': '37d9604165562bda296fba163ea0e4bc152663baadcfdbccecdd4e9cdb35faaa',
    'B1_47': '9cacfb2e46cc4db7c628b40fc7e857e31635c40150e87ec71dcfdb8e00a73ee0',
    'BASELINE': '4308392b831da1ac7d60f5f75e5eec6a011a685ccbd8c9252f77d593d0bf5dc9',
    'C1_11': 'dd8daa62900043ea8aee1e3f26543d6c70632c1f4d54016675cb2954a62d4769',
    'C1_29': '37c022d535fffed59215a32eb25da0ffd85faa3d0d34b084a4c9173eb4053f28',
    'C1_47': '565b83b42e4476f458466a1b6e7193891ee6b38e81823538383a7a028739a8a8',
    'C2_11': '9b320389a9aa16b22f8e8fc5e4699a20975deaebd7d3e1deab6372db4b163970',
    'C2_29': '33633cd0542863e913f38da0d6b1443f589da0433d95db330872c54aa2e9ebeb',
    'C2_47': '51f74581c0e31252948d8f0c467fbf725a71c1618d0cc8b3190518c3f7b3b6f1',
    'R1': '600dbd236098b967558e96d5ddf7d4144903fad96b172ad2871ec02fb0f30a44',
}
REFERENCE_PATH = source.DEVELOPMENT / "s1-paired-sd-inventory-2026-10-09/development-paired-sd.json"


class CalculatorICCContractError(ValueError):
    """An input or independently checkable descriptive invariant was violated."""


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def calculator_anova_components(pairs: Sequence[tuple[str, float]]) -> dict[str, Any]:
    """Compute unclipped method-of-moments ICC on 64 × 60 paired case effects."""
    groups: dict[str, list[float]] = defaultdict(list)
    for calculator, value in pairs:
        if not isinstance(calculator, str) or not calculator:
            raise CalculatorICCContractError("INVALID_CALCULATOR_ID")
        if type(value) not in (int, float) or not math.isfinite(value):
            raise CalculatorICCContractError("INVALID_FINITE_PAIRED_DELTA")
        groups[calculator].append(value)
    k, m = CALCULATORS_PER_SPLIT, EVAL_TASKS_PER_CALCULATOR
    if len(groups) != k or any(len(group) != m for group in groups.values()):
        raise CalculatorICCContractError("UNBALANCED_OR_MISSING_CALCULATOR_TASKS")
    grand = statistics.fmean(v for group in groups.values() for v in group)
    means = {cal: statistics.fmean(group) for cal, group in groups.items()}
    ms_between = m * math.fsum((mean - grand) ** 2 for mean in means.values()) / (k - 1)
    ms_within = math.fsum(
        math.fsum((v - means[cal]) ** 2 for v in group)
        for cal, group in groups.items()
    ) / (k * (m - 1))
    denominator = ms_between + (m - 1) * ms_within
    rho = (ms_between - ms_within) / denominator if denominator > 0 else None
    if rho is not None and not (-1 / (m - 1) - 1e-8 <= rho <= 1 + 1e-8):
        raise CalculatorICCContractError("ICC_ESTIMATE_OUT_OF_THEORETICAL_BOUNDS")
    return {
        "calculator_count": k,
        "source_cases_per_calculator": m,
        "paired_delta_mean": grand,
        "within_calculator_ms": ms_within,
        "between_calculator_ms": ms_between,
        "anovamom_rho_unclipped": rho,
        "rho_status": "UNDEFINED_ZERO_TOTAL_VARIANCE" if rho is None else (
            "NEGATIVE_FINITE_SAMPLE_ESTIMATE" if rho < 0 else "DESCRIPTIVE_NONNEGATIVE_ESTIMATE"
        ),
        "illustrative_deff": 1 + (m - 1) * rho if rho is not None and rho >= 0 else None,
        "illustrative_effective_cases": k * m / (1 + (m - 1) * rho) if rho is not None and rho >= 0 else None,
        "calculator_mean_min": min(means.values()),
        "calculator_mean_max": max(means.values()),
    }


def _reference_cell(reference: dict[str, Any], name: str, split: str, metric: str) -> float:
    try:
        sd = reference["intervention_results"][name]["splits"][split][metric]["paired_source_task_sample_sd"]
    except (KeyError, TypeError) as exc:
        raise CalculatorICCContractError("MISSING_SOURCE_BOUND_REFERENCE_SD_CELL") from exc
    if type(sd) not in (int, float) or not math.isfinite(sd) or sd < 0:
        raise CalculatorICCContractError("INVALID_SOURCE_BOUND_REFERENCE_SD")
    return sd


def build_inventory() -> dict[str, Any]:
    if _sha(REFERENCE_PATH) != FROZEN_REFERENCE_SHA256:
        raise CalculatorICCContractError("ORIGINAL_DESCRIPTIVE_SD_REFERENCE_SHA_MISMATCH")
    reference = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))
    baseline_path = source.DEVELOPMENT / source.BASELINE_PATH
    r1_path = source.DEVELOPMENT / source.REPEAT_R1_PATH
    baseline = source._load(baseline_path, "BASELINE_V1")
    r1 = source._load(r1_path, "BASELINE_V1")
    if r1.get("repeat") != 1 or any(
        any(a.get(field) != b.get(field) for field in source.IDENTITY_FIELDS + ("logits",))
        for a, b in zip(baseline["rows"], r1["rows"])
    ):
        raise CalculatorICCContractError("BASELINE_R1_SOURCE_OR_LOGITS_MISMATCH")
    base_index = source._validate_and_index(baseline["rows"])
    rows = []
    hashes = {"BASELINE": _sha(baseline_path), "R1": _sha(r1_path)}
    seed_mean_map: dict[tuple[str, str, str], dict[int, float]] = defaultdict(dict)
    maximum_sd_reconstruction_error = 0.0
    for name, (relative, intervention, seed) in sorted(source.CANDIDATES.items()):
        path = source.DEVELOPMENT / relative
        candidate = source._load(path, intervention, seed)
        candidate_index = source._validate_and_index(candidate["rows"])
        if tuple(base_index) != tuple(candidate_index):
            raise CalculatorICCContractError("ORDERED_SOURCE_TASK_SET_CHANGED")
        hashes[name] = _sha(path)
        paired = {(split, metric): [] for split in source.EVAL_SPLITS for metric in PRIMARY_METRICS}
        for task_id, (base_metrics, bc, bt) in base_index.items():
            candidate_metrics, cc, ct = candidate_index[task_id]
            for b, c in ((bc, cc), (bt, ct)):
                if any(b.get(f) != c.get(f) for f in source.IDENTITY_FIELDS):
                    raise CalculatorICCContractError("SOURCE_TASK_OR_PROMPT_IDENTITY_CHANGED")
            if type(bc["calculator_id"]) is not str or not bc["calculator_id"]:
                raise CalculatorICCContractError("INVALID_CALCULATOR_ID")
            for metric in PRIMARY_METRICS:
                diff = candidate_metrics[metric] - base_metrics[metric]
                if not math.isfinite(diff):
                    raise CalculatorICCContractError("NONFINITE_PAIRED_DELTA")
                paired[(bc["split"], metric)].append((bc["calculator_id"], diff))
        for (split, metric), pairs in sorted(paired.items()):
            if len(pairs) != source.EVAL_PER_SPLIT:
                raise CalculatorICCContractError("INCOMPLETE_DEVELOPMENT_EVAL_SPLIT")
            result = calculator_anova_components(pairs)
            k, m = CALCULATORS_PER_SPLIT, EVAL_TASKS_PER_CALCULATOR
            sd_from_components = math.sqrt(
                ((k - 1) * result["between_calculator_ms"] +
                 k * (m - 1) * result["within_calculator_ms"]) / (k * m - 1)
            )
            saved_sd = _reference_cell(reference, name, split, metric)
            err = abs(sd_from_components - saved_sd)
            if not math.isclose(sd_from_components, saved_sd, rel_tol=1e-11, abs_tol=1e-11):
                raise CalculatorICCContractError("SOURCE_BOUND_SD_ANOVA_DECOMPOSITION_MISMATCH")
            maximum_sd_reconstruction_error = max(maximum_sd_reconstruction_error, err)
            result.update({
                "condition": name, "intervention": intervention,
                "seed": seed, "split": split, "metric": metric,
            })
            rows.append(result)
            seed_mean_map[(intervention, split, metric)][seed] = result["paired_delta_mean"]
    if hashes != EXPECTED_INPUT_SHA256:
        raise CalculatorICCContractError("ORIGINAL_DEVELOPMENT_INPUT_SHA_MISMATCH")
    if len(rows) != 72 or len(seed_mean_map) != 24:
        raise CalculatorICCContractError("UNEXPECTED_DEVELOPMENT_CELL_COUNT")
    seed_spread = []
    for (intervention, split, metric), means in sorted(seed_mean_map.items()):
        if set(means) != SEEDS:
            raise CalculatorICCContractError("MISSING_OR_DUPLICATE_TRAINING_SEED")
        seed_spread.append({
            "intervention": intervention, "split": split, "metric": metric,
            "seed_level_mean_delta_by_seed": {str(k): v for k, v in sorted(means.items())},
            "three_seed_sample_sd_of_overall_effects": statistics.stdev(means.values()),
            "training_seed_count": 3, "uncertainty_qualified": False,
        })
    valid_rho = [row["anovamom_rho_unclipped"] for row in rows
                 if row["anovamom_rho_unclipped"] is not None]
    return {
        "status": "DEVELOPMENT_ONLY_CALCULATOR_ANOVAMOM_SENSITIVITY_NOT_POWER",
        "source": "ORIGINAL_PINNED_DEVELOPMENT_MATRIX_SHA256",
        "input_hashes": hashes,
        "reference_sd_sha256": FROZEN_REFERENCE_SHA256,
        "reference_sd_cells_reproduced": 72,
        "reference_sd_reconstruction_max_abs_error": maximum_sd_reconstruction_error,
        "rows": len(rows), "n_missing_icc": 72-len(valid_rho),
        "n_negative_icc": sum(x < 0 for x in valid_rho),
        "n_nonnegative_icc": sum(x >= 0 for x in valid_rho),
        "rho_min": min(valid_rho) if valid_rho else None,
        "rho_median": statistics.median(valid_rho) if valid_rho else None,
        "rho_max": max(valid_rho) if valid_rho else None,
        "highest_positive_icc_cells": sorted(
            (row for row in rows if row["anovamom_rho_unclipped"] is not None),
            key=lambda row: row["anovamom_rho_unclipped"], reverse=True
        )[:12],
        "all_development_cells": rows,
        "three_seed_between_effect_spreads": seed_spread,
        "boundaries": {
            "primary_holm_family_independently_reviewed": False,
            "calculator_sampling_generalization_qualified": False,
            "calculator_effect_icc_confirmatory_qualified": False,
            "source_case_seed_crossed_variance_qualified": False,
            "final_90_percent_power_qualified": False,
            "confirmatory_authorized": False,
            "source_cases_per_split": 3840,
            "frozen_confirmatory_source_case_count": 4096,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_inventory()
    text = json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Existing scientific records and symlink targets are never overwritten.
    with args.output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)
    print(json.dumps({
        "status": result["status"], "cells": result["rows"],
        "reference_sd_cells_reproduced": result["reference_sd_cells_reproduced"],
        "output_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
