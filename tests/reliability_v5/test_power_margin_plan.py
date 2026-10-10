from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_power_margin_plan as plan


def _spec() -> dict:
    return {
        "scope": "DEVELOPMENT_ONLY_POWER_PLANNING",
        "confirmatory": False,
        "reserve": False,
        "family_alpha": 0.05,
        "multiplicity": "HOLM",
        "primary_non_target_family_size": 4,
        "desired_power": 0.90,
        "planned_clusters": 4096,
        "margin_rule": "MAX_DOMAIN_FLOOR_2X_REPEATABILITY95",
        "metrics": {
            "canonical_nll": {
                "domain_floor": 0.01,
                "repeatability95": 0.002,
                "paired_sd": 0.20,
                "domain_floor_justification_sha256": "a" * 64,
                "repeatability_evidence_sha256": "b" * 64,
                "paired_sd_evidence_sha256": "c" * 64,
            },
            "semantic_js": {
                "domain_floor": 0.001,
                "repeatability95": 0.001,
                "paired_sd": 0.02,
                "domain_floor_justification_sha256": "d" * 64,
                "repeatability_evidence_sha256": "e" * 64,
                "paired_sd_evidence_sha256": "f" * 64,
            },
        },
    }


def test_holm_planning_alpha_is_conservative_first_step() -> None:
    assert plan.conservative_holm_planning_alpha(0.05, 4) == pytest.approx(0.0125)


def test_build_plan_applies_frozen_margin_rule_and_power() -> None:
    result = plan.build_plan(_spec())
    assert result["conservative_holm_planning_alpha"] == pytest.approx(0.0125)
    assert result["metrics"]["canonical_nll"]["meaningful_margin"] == pytest.approx(0.01)
    assert result["metrics"]["semantic_js"]["meaningful_margin"] == pytest.approx(0.002)
    assert result["metrics"]["canonical_nll"]["normal_approx_required_clusters_at_margin"] >= 2
    assert isinstance(result["all_metrics_meet_normal_approx_target"], bool)
    assert result["confirmatory"] is False
    assert result["reserve"] is False
    assert result["family_membership_frozen_and_independently_reviewed"] is False
    assert result["source_case_seed_nuisance_qualified"] is False
    assert result["final_90_percent_power_qualified"] is False
    assert result["confirmatory_execution_authorized"] is False


def test_zero_paired_sd_is_handled_without_fake_positive_noise() -> None:
    spec = _spec()
    spec["metrics"]["canonical_nll"]["paired_sd"] = 0.0
    result = plan.build_plan(spec)
    row = result["metrics"]["canonical_nll"]
    assert row["normal_approx_mde_at_planned_clusters"] == 0.0
    assert row["normal_approx_required_clusters_at_margin"] == 2
    assert row["planned_clusters_meet_normal_approx_target"] is True


@pytest.mark.parametrize(
    "mutator,match",
    [
        (lambda s: s.update(scope="WRONG"), "scope"),
        (lambda s: s.update(confirmatory=True), "confirmatory/reserve"),
        (lambda s: s.update(multiplicity="BONFERRONI"), "multiplicity"),
        (lambda s: s.update(primary_non_target_family_size=0), "family_size"),
        (lambda s: s["metrics"]["canonical_nll"].update(domain_floor=0.0), "domain_floor"),
        (lambda s: s["metrics"]["canonical_nll"].update(repeatability95=-0.1), "repeatability95"),
        (
            lambda s: s["metrics"]["canonical_nll"].update(
                domain_floor_justification_sha256="TBD"
            ),
            "frozen justification",
        ),
        (
            lambda s: s["metrics"]["canonical_nll"].update(
                repeatability_evidence_sha256=""
            ),
            "repeatability evidence",
        ),
        (
            lambda s: s["metrics"]["canonical_nll"].update(
                paired_sd_evidence_sha256=None
            ),
            "nuisance evidence",
        ),
    ],
)
def test_plan_fails_closed_on_unfrozen_or_invalid_inputs(mutator, match) -> None:
    spec = copy.deepcopy(_spec())
    mutator(spec)
    with pytest.raises(plan.PowerPlanContractError, match=match):
        plan.build_plan(spec)

@pytest.mark.parametrize(
    "mutator,match",
    [
        (lambda s: s.update(family_alpha=0.20), "frozen V5 family-wise alpha"),
        (lambda s: s.update(family_alpha=0.01), "frozen V5 family-wise alpha"),
        (lambda s: s.update(desired_power=0.51), "frozen V5 target"),
        (lambda s: s.update(desired_power=0.95), "frozen V5 target"),
        (lambda s: s.update(planned_clusters=2), "frozen V5 plan"),
        (lambda s: s.update(planned_clusters=8192), "frozen V5 plan"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd=False), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd=True), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd="0.001"), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd=10 ** 1000), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(domain_floor=True), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(repeatability95="0"), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(domain_floor_justification_sha256="x"), "SHA-256"),
        (lambda s: s["metrics"]["canonical_nll"].update(repeatability_evidence_sha256="g" * 64), "SHA-256"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd_evidence_sha256="0" * 63), "SHA-256"),
        (lambda s: s["metrics"]["canonical_nll"].update(paired_sd_evidence_sha256="A" * 64), "SHA-256"),
    ],
)
def test_reject_unreviewed_power_relaxation_or_forged_hash(mutator, match) -> None:
    spec = copy.deepcopy(_spec())
    mutator(spec)
    with pytest.raises(plan.PowerPlanContractError, match=match):
        plan.build_plan(spec)
