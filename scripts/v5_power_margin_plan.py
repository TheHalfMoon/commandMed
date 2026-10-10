#!/usr/bin/env python3
"""Fail-closed V5 meaningful-margin and conservative Holm power planning.

This utility consumes only prospectively frozen development-only inputs. It does
not choose a domain floor, repeatability estimator, paired SD, endpoint family,
or confirmatory identity. Its only role is to apply already-frozen mechanics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path
import sys
from typing import Any

# Direct CLI execution must find the repository module from outside scripts/.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

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


FAMILY_TAGS = frozenset(("STRUCTURALLY_DISTINCT", "SHARED_INPUT", "MATHEMATICALLY_COUPLED"))
HYPOTHESIS_ID_PATTERN = re.compile(r"[A-Z][A-Z0-9_-]{3,63}\Z")


def _unreviewed_family_bindings(spec: dict[str, Any], metric_names: set[str]) -> tuple[int, str]:
    """Check manifest completeness, not the scientific validity of its members.

    This manifest is entirely caller-provided and remains *unreviewed*.
    No input field can change the hard-coded review/confirmatory=false outputs.
    """
    hypotheses = spec.get("primary_non_target_hypotheses")
    if not isinstance(hypotheses, list) or not hypotheses:
        raise PowerPlanContractError("primary_non_target_hypotheses: nonempty explicit list required")
    declared_size = spec.get("primary_non_target_family_size")
    if type(declared_size) is not int or declared_size != len(hypotheses):
        raise PowerPlanContractError("primary_non_target_family_size: must equal declared hypothesis list length")
    ids: set[str] = set()
    cells: set[tuple[str, str, str]] = set()
    required_fields = frozenset((
        "hypothesis_id", "intervention", "target_property",
        "non_target_metric", "coupling_tag", "inferential_unit", "primary",
    ))
    for idx, row in enumerate(hypotheses):
        prefix = f"primary_non_target_hypotheses[{idx}]"
        if not isinstance(row, dict) or set(row) != required_fields:
            raise PowerPlanContractError(prefix + ": exact hypothesis fields required")
        identifier = row["hypothesis_id"]
        if not isinstance(identifier, str) or HYPOTHESIS_ID_PATTERN.fullmatch(identifier) is None:
            raise PowerPlanContractError(prefix + ": stable uppercase hypothesis ID required")
        if identifier in ids:
            raise PowerPlanContractError(prefix + ": duplicate hypothesis_id")
        ids.add(identifier)
        for key in ("intervention", "target_property", "non_target_metric"):
            val = row[key]
            if not isinstance(val, str) or not val.strip() or val != val.strip():
                raise PowerPlanContractError(prefix + ": invalid " + key)
        if row["non_target_metric"] not in metric_names:
            raise PowerPlanContractError(prefix + ": non_target_metric lacks planning metric")
        if row["target_property"] == row["non_target_metric"]:
            raise PowerPlanContractError(prefix + ": non-target cannot equal target")
        if not isinstance(row["coupling_tag"], str) or row["coupling_tag"] not in FAMILY_TAGS:
            raise PowerPlanContractError(prefix + ": coupling_tag must be declared")
        if row["inferential_unit"] != "SOURCE_CASE":
            raise PowerPlanContractError(prefix + ": source medical case is required inferential unit")
        if row["primary"] is not True:
            raise PowerPlanContractError(prefix + ": primary hard-gate membership required")
        cell = (row["intervention"], row["target_property"], row["non_target_metric"])
        if cell in cells:
            raise PowerPlanContractError(prefix + ": duplicate primary intervention-target-non-target cell")
        cells.add(cell)
    digest = hashlib.sha256(
        json.dumps(hypotheses, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    ).hexdigest()
    return len(hypotheses), digest


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
    metrics = spec.get("metrics")
    if not isinstance(metrics, dict) or not metrics:
        raise PowerPlanContractError("metrics: expected a non-empty object")
    if any(not isinstance(name, str) or not name.strip() for name in metrics):
        raise PowerPlanContractError("metrics: invalid metric name")
    family_size, unreviewed_family_sha = _unreviewed_family_bindings(spec, set(metrics))
    planning_alpha = conservative_holm_planning_alpha(family_alpha, family_size)
    desired_power = _finite_positive(spec.get("desired_power"), "desired_power")
    if desired_power != 0.90:
        raise PowerPlanContractError("desired_power: frozen V5 target 0.90 required")
    planned_clusters = spec.get("planned_clusters")
    if type(planned_clusters) is not int or planned_clusters != 4096:
        raise PowerPlanContractError("planned_clusters: current frozen V5 plan is exactly 4096")

    # Metric-level margins are shared, but training-run/source-case variance
    # is intervention/hypothesis-specific. Never infer cell power from an
    # arbitrary pooled or favorable metric-level paired_sd.
    result_metrics: dict[str, Any] = {}
    expected_metric_fields = {
        "domain_floor", "repeatability95",
        "domain_floor_justification_sha256", "repeatability_evidence_sha256",
    }
    for name in sorted(metrics):
        row = metrics[name]
        if not isinstance(name, str) or not name.strip() or not isinstance(row, dict):
            raise PowerPlanContractError("metrics: invalid metric entry")
        if set(row) != expected_metric_fields:
            raise PowerPlanContractError(
                f"metrics.{name}: margins must not supply metric-level paired_sd"
            )
        floor = _finite_positive(row["domain_floor"], f"metrics.{name}.domain_floor")
        repeat = _finite_nonnegative(row["repeatability95"], f"metrics.{name}.repeatability95")
        _require_sha256(row["domain_floor_justification_sha256"],
                        f"metrics.{name}.domain_floor_justification_sha256: frozen justification")
        _require_sha256(row["repeatability_evidence_sha256"],
                        f"metrics.{name}.repeatability_evidence_sha256: repeatability evidence")
        result_metrics[name] = {
            "domain_floor": floor,
            "repeatability95": repeat,
            "meaningful_margin": max(floor, 2.0 * repeat),
            "domain_floor_justification_sha256": row["domain_floor_justification_sha256"],
            "repeatability_evidence_sha256": row["repeatability_evidence_sha256"],
        }

    nuisance = spec.get("paired_nuisance_by_hypothesis")
    ids = {row["hypothesis_id"] for row in spec["primary_non_target_hypotheses"]}
    if not isinstance(nuisance, dict) or set(nuisance) != ids:
        raise PowerPlanContractError(
            "paired_nuisance_by_hypothesis: one hypothesis-specific "
            "descriptive nuisance record required for every declared "
            "hypothesis, with no extras"
        )
    result_hypotheses: dict[str, Any] = {}
    for row in spec["primary_non_target_hypotheses"]:
        hypothesis_id = row["hypothesis_id"]
        metric_name = row["non_target_metric"]
        metric = metrics[metric_name]
        record = nuisance[hypothesis_id]
        if not isinstance(record, dict) or set(record) != {
            "paired_sd", "paired_sd_evidence_sha256", "nuisance_scope"
        }:
            raise PowerPlanContractError(
                f"paired_nuisance_by_hypothesis.{hypothesis_id}: exact nuisance fields required"
            )
        if record["nuisance_scope"] != "UNQUALIFIED_DEVELOPMENT_DESCRIPTIVE":
            raise PowerPlanContractError(
                f"paired_nuisance_by_hypothesis.{hypothesis_id}: unqualified development scope required"
            )
        _require_sha256(
            record["paired_sd_evidence_sha256"],
            f"paired_nuisance_by_hypothesis.{hypothesis_id}.paired_sd_evidence_sha256: nuisance evidence",
        )
        result_hypotheses[hypothesis_id] = {
            "intervention": row["intervention"],
            "target_property": row["target_property"],
            "non_target_metric": metric_name,
            "coupling_tag": row["coupling_tag"],
            "inferential_unit": row["inferential_unit"],
            "nuisance_scope": "UNQUALIFIED_DEVELOPMENT_DESCRIPTIVE",
            **_plan_metric(
                domain_floor=metric["domain_floor"],
                repeatability95=metric["repeatability95"],
                paired_sd=record["paired_sd"],
                planned_clusters=planned_clusters,
                planning_alpha=planning_alpha,
                desired_power=desired_power,
            ),
            "paired_sd_evidence_sha256": record["paired_sd_evidence_sha256"],
        }

    return {
        "schema": "commandmed.v5.power-margin-plan.v2",
        "scope": "DEVELOPMENT_ONLY_POWER_PLANNING",
        "confirmatory": False,
        "reserve": False,
        "family_alpha": family_alpha,
        "multiplicity": "HOLM",
        "primary_non_target_family_size": family_size,
        "unreviewed_family_declaration_sha256": unreviewed_family_sha,
        "family_size_matches_unreviewed_declared_hypotheses": True,
        "conservative_holm_planning_alpha": planning_alpha,
        "desired_power": desired_power,
        "planned_clusters": planned_clusters,
        "margin_rule": "MAX_DOMAIN_FLOOR_2X_REPEATABILITY95",
        "metrics": result_metrics,
        "hypothesis_plans": result_hypotheses,
        "all_declared_hypotheses_meet_illustrative_normal_approx_target": all(
            row["planned_clusters_meet_normal_approx_target"]
            for row in result_hypotheses.values()
        ),
        "family_membership_frozen_and_independently_reviewed": False,
        "source_case_seed_nuisance_qualified": False,
        "final_90_percent_power_qualified": False,
        "confirmatory_execution_authorized": False,
        "interpretation_boundary": (
            "Normal-approximation development planning only. Family membership "
            "and multiplicity count derive from a caller-supplied, unreviewed "
            "hypothesis list, not independently qualified prospective science. "
            "Each declared hypothesis has its own unqualified descriptive paired "
            "SD; a shared metric SD cannot stand in for an intervention cell. "
            "Holm uses first-step alpha/family_size. This is not final power "
            "or authorization for confirmatory access."
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
    print(json.dumps({
        "status": "PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT",
        "final_90_percent_power_qualified": False,
        "output": str(args.output),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
