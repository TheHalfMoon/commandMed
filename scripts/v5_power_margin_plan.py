#!/usr/bin/env python3
"""Fail-closed V5 meaningful-margin and conservative Holm power planning.

This utility consumes only prospectively frozen development-only inputs. It does
not choose a domain floor, repeatability estimator, paired SD, endpoint family,
or confirmatory identity. Its only role is to apply already-frozen mechanics.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

from src.commandmed.reliability_v5.statistics import (
    StatisticsContractError,
    normal_approx_paired_mde,
    normal_approx_required_clusters,
)


class PowerPlanContractError(ValueError):
    """Raised when a prospective power-plan input is incomplete or malformed."""


SHA256_PATTERN = re.compile(r"[0-9a-f]{64}\Z")


def _require_sha256(value: Any, field: str) -> str:
    """Require actual SHA-256 syntax, not a placeholder or arbitrary nonempty text."""
    if not isinstance(value, str) or SHA256_PATTERN.fullmatch(value) is None:
        raise PowerPlanContractError(f"{field}: frozen 64-character lowercase SHA-256 required")
    return value


def _finite_nonnegative(value: Any, field: str) -> float:
    # JSON booleans and numeric strings must not silently become real variance.
    if type(value) not in (int, float):
        raise PowerPlanContractError(f"{field}: expected a finite nonnegative JSON number")
    try:
        number = float(value)
    except OverflowError as exc:
        raise PowerPlanContractError(f"{field}: expected a finite nonnegative JSON number") from exc
    if not math.isfinite(number) or number < 0.0:
        raise PowerPlanContractError(f"{field}: expected a finite nonnegative number")
    return number


def _finite_positive(value: Any, field: str) -> float:
    number = _finite_nonnegative(value, field)
    if number <= 0.0:
        raise PowerPlanContractError(f"{field}: expected a finite positive number")
    return number


def conservative_holm_planning_alpha(family_alpha: float, family_size: int) -> float:
    """Return the Holm first-step alpha used for conservative per-cell planning."""
    alpha = _finite_positive(family_alpha, "family_alpha")
    if alpha >= 1.0:
        raise PowerPlanContractError("family_alpha: expected a value in (0, 1)")
    if type(family_size) is not int or family_size < 1:
        raise PowerPlanContractError("family_size: expected an integer >= 1")
    return alpha / family_size


def _plan_metric(
    *,
    domain_floor: float,
    repeatability95: float,
    paired_sd: float,
    planned_clusters: int,
    planning_alpha: float,
    desired_power: float,
) -> dict[str, Any]:
    floor = _finite_positive(domain_floor, "domain_floor")
    repeat = _finite_nonnegative(repeatability95, "repeatability95")
    sd = _finite_nonnegative(paired_sd, "paired_sd")
    margin = max(floor, 2.0 * repeat)
    if type(planned_clusters) is not int or planned_clusters < 2:
        raise PowerPlanContractError("planned_clusters: expected an integer >= 2")
    power = _finite_positive(desired_power, "desired_power")
    if not 0.5 < power < 1.0:
        raise PowerPlanContractError("desired_power: expected a value in (0.5, 1)")

    if sd == 0.0:
        mde = 0.0
        required = 2
    else:
        try:
            mde = normal_approx_paired_mde(
                sd,
                planned_clusters,
                alpha=planning_alpha,
                power=power,
            )
            required = normal_approx_required_clusters(
                sd,
                margin,
                alpha=planning_alpha,
                power=power,
            )
        except StatisticsContractError as exc:
            raise PowerPlanContractError(str(exc)) from exc

    return {
        "domain_floor": floor,
        "repeatability95": repeat,
        "repeatability_component": 2.0 * repeat,
        "meaningful_margin": margin,
        "paired_sd": sd,
        "planned_clusters": planned_clusters,
        "conservative_holm_planning_alpha": planning_alpha,
        "desired_power": power,
        "normal_approx_mde_at_planned_clusters": mde,
        "normal_approx_required_clusters_at_margin": required,
        "planned_clusters_meet_normal_approx_target": planned_clusters >= required,
    }


def build_plan(spec: dict[str, Any]) -> dict[str, Any]:
    if spec.get("scope") != "DEVELOPMENT_ONLY_POWER_PLANNING":
        raise PowerPlanContractError("scope: DEVELOPMENT_ONLY_POWER_PLANNING required")
    if spec.get("confirmatory") is not False or spec.get("reserve") is not False:
        raise PowerPlanContractError("confirmatory/reserve: must both be false")
    if spec.get("margin_rule") != "MAX_DOMAIN_FLOOR_2X_REPEATABILITY95":
        raise PowerPlanContractError("margin_rule: frozen V5 rule required")
    if spec.get("multiplicity") != "HOLM":
        raise PowerPlanContractError("multiplicity: HOLM required")

    family_alpha = _finite_positive(spec.get("family_alpha"), "family_alpha")
    if family_alpha != 0.05:
        raise PowerPlanContractError("family_alpha: frozen V5 family-wise alpha 0.05 required")
    family_size = spec.get("primary_non_target_family_size")
    planning_alpha = conservative_holm_planning_alpha(family_alpha, family_size)
    desired_power = _finite_positive(spec.get("desired_power"), "desired_power")
    if desired_power != 0.90:
        raise PowerPlanContractError("desired_power: frozen V5 target 0.90 required")
    planned_clusters = spec.get("planned_clusters")
    if type(planned_clusters) is not int or planned_clusters != 4096:
        raise PowerPlanContractError("planned_clusters: current frozen V5 plan is exactly 4096")

    metrics = spec.get("metrics")
    if not isinstance(metrics, dict) or not metrics:
        raise PowerPlanContractError("metrics: expected a non-empty object")
    result_metrics: dict[str, Any] = {}
    for name in sorted(metrics):
        row = metrics[name]
        if not isinstance(name, str) or not name.strip() or not isinstance(row, dict):
            raise PowerPlanContractError("metrics: invalid metric entry")
        _require_sha256(row.get("domain_floor_justification_sha256"),
                        f"metrics.{name}.domain_floor_justification_sha256: frozen justification")
        _require_sha256(row.get("repeatability_evidence_sha256"),
                        f"metrics.{name}.repeatability_evidence_sha256: repeatability evidence")
        _require_sha256(row.get("paired_sd_evidence_sha256"),
                        f"metrics.{name}.paired_sd_evidence_sha256: nuisance evidence")
        result_metrics[name] = {
            **_plan_metric(
                domain_floor=row.get("domain_floor"),
                repeatability95=row.get("repeatability95"),
                paired_sd=row.get("paired_sd"),
                planned_clusters=planned_clusters,
                planning_alpha=planning_alpha,
                desired_power=desired_power,
            ),
            "domain_floor_justification_sha256": row["domain_floor_justification_sha256"],
            "repeatability_evidence_sha256": row["repeatability_evidence_sha256"],
            "paired_sd_evidence_sha256": row["paired_sd_evidence_sha256"],
        }

    return {
        "schema": "commandmed.v5.power-margin-plan.v1",
        "scope": "DEVELOPMENT_ONLY_POWER_PLANNING",
        "confirmatory": False,
        "reserve": False,
        "family_alpha": family_alpha,
        "multiplicity": "HOLM",
        "primary_non_target_family_size": family_size,
        "conservative_holm_planning_alpha": planning_alpha,
        "desired_power": desired_power,
        "planned_clusters": planned_clusters,
        "margin_rule": "MAX_DOMAIN_FLOOR_2X_REPEATABILITY95",
        "metrics": result_metrics,
        "all_metrics_meet_normal_approx_target": all(
            row["planned_clusters_meet_normal_approx_target"]
            for row in result_metrics.values()
        ),
        "family_membership_frozen_and_independently_reviewed": False,
        "source_case_seed_nuisance_qualified": False,
        "final_90_percent_power_qualified": False,
        "confirmatory_execution_authorized": False,
        "interpretation_boundary": (
            "Normal-approximation development planning only. Holm is handled "
            "conservatively using the first-step alpha/family_size threshold. "
            "This output is not final inference and cannot authorize confirmatory access."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    payload = build_plan(spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"status": "PASS_POWER_MARGIN_PLAN", "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
