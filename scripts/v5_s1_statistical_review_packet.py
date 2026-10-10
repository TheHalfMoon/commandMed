#!/usr/bin/env python3
"""Prepare a source-bound V5 development-only reviewer packet, never a power result."""
from __future__ import annotations

import argparse
import json
import math
import statistics
from pathlib import Path
from typing import Any

import v5_manuscript_development_evidence_audit as bound

INTERVENTIONS = {"B1_TYPED_V1": "B1", "C1_CRDI_V1": "C1", "C2_CRDI_RETAIN_V1": "C2"}
SEEDS = (11, 29, 47)
SPLITS = ("S1_DEV_EVAL", "S1_CAL_EVAL")
METRICS = ("canonical_accuracy", "canonical_nll", "canonical_brier", "semantic_js")


class ReviewerPacketError(ValueError):
    """Source snapshots are incomplete, inconsistent or scientifically promoted."""


def require(ok: bool, code: str) -> None:
    if not ok:
        raise ReviewerPacketError(code)


def exact_float(a: Any, b: Any) -> bool:
    return (type(a) in (int, float) and type(b) in (int, float)
            and math.isfinite(a) and math.isfinite(b)
            and math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12))


def create_packet(sd: dict[str, Any], icc: dict[str, Any]) -> dict[str, Any]:
    """Connect separately frozen development diagnostics without fitting inference."""
    require(sd.get("primary_non_target_family_size") is None
            and sd.get("training_seed_uncertainty_not_included_in_paired_item_sd") is True
            and sd.get("confirmatory") is False and sd.get("reserve") is False,
            "SOURCE_SD_SCIENCE_AUTHORITY_DRIFT")
    bounds = icc.get("boundaries", {})
    for name in ("confirmatory_authorized", "final_90_percent_power_qualified",
                 "source_case_seed_crossed_variance_qualified",
                 "primary_holm_family_independently_reviewed"):
        require(bounds.get(name) is False, "ICC_SCIENCE_AUTHORITY_DRIFT:" + name)
    require(bounds.get("source_cases_per_split") == 3840
            and bounds.get("frozen_confirmatory_source_case_count") == 4096
            and icc.get("reference_sd_sha256") == bound.LOCKED_SOURCES["sd_inventory"][1],
            "SOURCE_SCOPE_OR_HASH_DRIFT")
    results = sd.get("intervention_results", {})
    expected_conditions = {f"{prefix}_{seed}" for prefix in INTERVENTIONS.values() for seed in SEEDS}
    require(isinstance(results, dict) and set(results) == expected_conditions,
            "MISSING_OR_EXTRA_SOURCE_CONDITIONS")
    rows = icc.get("all_development_cells", [])
    require(isinstance(rows, list) and len(rows) == 72, "ICC_CELL_SET_DRIFT")
    indexed: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    for row in rows:
        require(isinstance(row, dict), "INVALID_ICC_CELL")
        key = (row.get("intervention"), row.get("split"), row.get("metric"), row.get("seed"))
        require(key[0] in INTERVENTIONS and key[1] in SPLITS and key[2] in METRICS
                and type(key[3]) is int and key[3] in SEEDS
                and key not in indexed, "DUPLICATE_OR_UNKNOWN_ICC_CELL")
        require(row.get("condition") == f"{INTERVENTIONS[key[0]]}_{key[3]}"
                and row.get("calculator_count") == 64
                and row.get("source_cases_per_calculator") == 60,
                "SOURCE_CASE_OR_CONDITION_DRIFT")
        # Recalculate the ANOVA moment ICC independently of the saved rho
        # field; retaining negative sampling estimates is intentional.
        between_ms, within_ms = row.get("between_calculator_ms"), row.get("within_calculator_ms")
        require(type(between_ms) is float and math.isfinite(between_ms) and between_ms >= 0
                and type(within_ms) is float and math.isfinite(within_ms) and within_ms >= 0,
                "INVALID_ANOVA_COMPONENTS")
        denominator = between_ms + (60 - 1) * within_ms
        require(math.isfinite(denominator) and denominator > 0, "INVALID_ANOVA_COMPONENTS")
        rho = row.get("anovamom_rho_unclipped")
        require(type(rho) is float and math.isfinite(rho), "INVALID_ICC_VALUE")
        require(exact_float((between_ms - within_ms) / denominator, rho),
                "ICC_MOMENT_RECONSTRUCTION_DRIFT")
        require(row.get("rho_status") == (
                "NEGATIVE_FINITE_SAMPLE_ESTIMATE" if rho < 0
                else "DESCRIPTIVE_NONNEGATIVE_ESTIMATE"), "ICC_SIGN_STATUS_DRIFT")
        indexed[key] = row
    require(len(indexed) == 72, "INCOMPLETE_ICC_MAPPING")
    spreads = icc.get("three_seed_between_effect_spreads", [])
    require(isinstance(spreads, list) and len(spreads) == 24, "SEED_SPREAD_GROUP_COUNT_DRIFT")
    groups: dict[tuple[str, str, str], dict[str, Any]] = {}
    for spread in spreads:
        require(isinstance(spread, dict), "INVALID_SEED_SPREAD")
        key = (spread.get("intervention"), spread.get("split"), spread.get("metric"))
        require(key[0] in INTERVENTIONS and key[1] in SPLITS and key[2] in METRICS
                and key not in groups, "SEED_SPREAD_GROUP_DRIFT")
        require(spread.get("training_seed_count") == 3
                and spread.get("uncertainty_qualified") is False,
                "SEED_UNCERTAINTY_PROMOTED")
        means = spread.get("seed_level_mean_delta_by_seed")
        require(isinstance(means, dict) and set(means) == {str(x) for x in SEEDS},
                "SEED_MEMBERSHIP_DRIFT")
        sample_sd = statistics.stdev(means.values())
        require(exact_float(sample_sd, spread.get("three_seed_sample_sd_of_overall_effects")),
                "BETWEEN_SEED_SD_DRIFT")
        examples = []
        for seed in SEEDS:
            source = results[f"{INTERVENTIONS[key[0]]}_{seed}"]
            require(source.get("intervention") == key[0] and source.get("seed") == seed,
                    "SOURCE_CONDITION_DRIFT")
            cell = source["splits"][key[1]][key[2]]
            icc_row = indexed[(key[0], key[1], key[2], seed)]
            require(cell.get("task_count") == 3840
                    and exact_float(cell.get("mean_delta_raw_orientation"), means[str(seed)])
                    and exact_float(cell.get("mean_delta_raw_orientation"), icc_row.get("paired_delta_mean")),
                    "SEED_EFFECT_MISMATCH")
            require(type(cell.get("paired_source_task_sample_sd")) is float
                    and math.isfinite(cell["paired_source_task_sample_sd"])
                    and cell["paired_source_task_sample_sd"] >= 0,
                    "INVALID_PAIRED_SD")
            # Independent sample-SD reconstruction from the original K=64,
            # m=60 ANOVA mean-square components; source cases remain the unit.
            between_ms = icc_row["between_calculator_ms"]
            within_ms = icc_row["within_calculator_ms"]
            sample_variance = ((64 - 1) * between_ms + 64 * (60 - 1) * within_ms) / (3840 - 1)
            require(math.isfinite(sample_variance) and sample_variance >= 0
                    and exact_float(math.sqrt(sample_variance),
                                    cell["paired_source_task_sample_sd"]),
                    "ANOVA_SOURCE_CASE_SD_RECONSTRUCTION_DRIFT")
            examples.append({
                "seed": seed,
                "paired_delta_mean_raw_metric_orientation": cell["mean_delta_raw_orientation"],
                "paired_source_case_sample_sd": cell["paired_source_task_sample_sd"],
                "calculator_anova_icc_unclipped": icc_row["anovamom_rho_unclipped"],
                "negative_icc_sample_estimate": icc_row["anovamom_rho_unclipped"] < 0,
            })
        require(exact_float(statistics.stdev([x["paired_delta_mean_raw_metric_orientation"]
                                               for x in examples]), sample_sd),
                "SEED_SPREAD_RECONSTRUCTION_MISMATCH")
        groups[key] = {
            "intervention": key[0], "split": key[1], "metric": key[2],
            "training_seed_count": 3,
            "seed_level_development_evidence": examples,
            "descriptive_sd_of_three_seed_effect_means": sample_sd,
            "paired_sd_min_across_three_seed_snapshots": min(x["paired_source_case_sample_sd"] for x in examples),
            "paired_sd_max_across_three_seed_snapshots": max(x["paired_source_case_sample_sd"] for x in examples),
            "negative_sample_icc_cells": sum(x["negative_icc_sample_estimate"] for x in examples),
            "crossed_source_case_calculator_seed_nuisance_qualified": False,
        }
    require(len(groups) == 24, "GROUP_COVERAGE_DRIFT")
    require(sum(x["negative_sample_icc_cells"] for x in groups.values()) == 12,
            "NEGATIVE_ICC_ESTIMATES_ERASED")
    return {
        "schema": "commandmed.v5.descriptive-statistical-review-packet.v1",
        "status": "SOURCE_BOUND_DESCRIPTIVE_REVIEW_PACKET_NOT_POWER",
        "source_sha256": {
            "development_paired_sd": bound.LOCKED_SOURCES["sd_inventory"][1],
            "development_calculator_icc": bound.LOCKED_SOURCES["icc_inventory"][1],
        },
        "source_cases_per_development_split": 3840,
        "calculators_per_development_split": 64,
        "cases_per_calculator": 60,
        "planned_confirmatory_source_cases_unmaterialized": 4096,
        "seed_ids": list(SEEDS),
        "descriptive_condition_seed_metric_split_cells": 72,
        "descriptive_intervention_metric_split_groups": 24,
        "observed_negative_unclipped_icc_estimates": 12,
        "groups": [groups[key] for key in sorted(groups)],
        "prospective_primary_non_target_hypothesis_family": None,
        "primary_non_target_family_size": None,
        "source_case_calculator_seed_crossed_covariance_model": None,
        "confirmatory_90_percent_power_qualified": False,
        "confirmatory_authorized": False,
        "independent_statistical_review_completed": False,
        "publication_or_clinical_authorized": False,
        "review_decisions_required": [
            "Declare full non-target Holm family before estimating final power",
            "Choose conditional-on-selected-calculators versus transport estimand",
            "Prespecify crossed source-case/calculator/training-seed dependence and missingness",
            "Prespecify per-cell orientation, native-unit margins, coupling and fixed-policy rules",
            "Verify each-primary-effect 90% power at actual family size or apply power-failure rule",
            "Obtain independent statistical/code/provenance review and founder execution authority",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    # Read immutable evidence and all 307 original scientific bindings first.
    bound.audit()
    source = json.loads((bound.ROOT / bound.LOCKED_SOURCES["sd_inventory"][0]).read_text())
    icc = json.loads((bound.ROOT / bound.LOCKED_SOURCES["icc_inventory"][0]).read_text())
    payload = json.dumps(create_packet(source, icc), sort_keys=True, indent=2, allow_nan=False) + "\n"
    if args.verify is not None:
        require(args.verify.is_file() and args.verify.read_bytes() == payload.encode("utf-8"),
                "COMMITTED_REVIEW_PACKET_REPLAY_DRIFT")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as f:
            f.write(payload)
    print(json.dumps({"status": "PASS_SOURCE_BOUND_DESCRIPTIVE_REVIEW_PACKET_REPLAY",
                      "groups": 24, "cells": 72, "statistical_power_qualified": False},
                     sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
