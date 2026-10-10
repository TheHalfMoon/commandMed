from __future__ import annotations

import copy
import json
import subprocess
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
        "primary_non_target_hypotheses": [
            {
                "hypothesis_id": f"SYNTH-HYP-{i:02d}",
                "intervention": intervention,
                "target_property": "canonical_accuracy",
                "non_target_metric": metric,
                "coupling_tag": "SHARED_INPUT",
                "inferential_unit": "SOURCE_CASE",
                "primary": True,
            }
            for i, (intervention, metric) in enumerate((
                ("B1", "canonical_nll"),
                ("B1", "semantic_js"),
                ("C1", "canonical_nll"),
                ("C1", "semantic_js"),
            ))
        ],
        "desired_power": 0.90,
        "planned_clusters": 4096,
        "margin_rule": "MAX_DOMAIN_FLOOR_2X_REPEATABILITY95",
        "metrics": {
            "canonical_nll": {
                "domain_floor": 0.01,
                "repeatability95": 0.002,
                "domain_floor_justification_sha256": "a" * 64,
                "repeatability_evidence_sha256": "b" * 64,
            },
            "semantic_js": {
                "domain_floor": 0.001,
                "repeatability95": 0.001,
                "domain_floor_justification_sha256": "d" * 64,
                "repeatability_evidence_sha256": "e" * 64,
            },
        },
        "paired_nuisance_by_hypothesis": {
            f"SYNTH-HYP-{i:02d}": {
                "paired_sd": 0.20 if i % 2 == 0 else 0.02,
                "paired_sd_evidence_sha256": "c" * 64 if i % 2 == 0 else "f" * 64,
                "nuisance_scope": "UNQUALIFIED_DEVELOPMENT_DESCRIPTIVE",
            }
            for i in range(4)
        },
    }


def test_holm_planning_alpha_is_conservative_first_step() -> None:
    assert plan.conservative_holm_planning_alpha(0.05, 4) == pytest.approx(0.0125)


def test_build_plan_applies_frozen_margin_rule_and_power() -> None:
    result = plan.build_plan(_spec())
    assert result["schema"] == "commandmed.v5.power-margin-plan.v2"
    assert result["conservative_holm_planning_alpha"] == pytest.approx(0.0125)
    assert result["family_size_matches_unreviewed_declared_hypotheses"] is True
    assert len(result["unreviewed_family_declaration_sha256"]) == 64
    assert result["metrics"]["canonical_nll"]["meaningful_margin"] == pytest.approx(0.01)
    assert result["metrics"]["semantic_js"]["meaningful_margin"] == pytest.approx(0.002)
    assert result["hypothesis_plans"]["SYNTH-HYP-00"]["normal_approx_required_clusters_at_margin"] >= 2
    assert isinstance(result["all_declared_hypotheses_meet_illustrative_normal_approx_target"], bool)
    assert "paired_sd" not in result["metrics"]["canonical_nll"]
    assert result["confirmatory"] is False
    assert result["reserve"] is False
    assert result["family_membership_frozen_and_independently_reviewed"] is False
    assert result["source_case_seed_nuisance_qualified"] is False
    assert result["final_90_percent_power_qualified"] is False
    assert result["confirmatory_execution_authorized"] is False


def test_zero_paired_sd_is_handled_without_fake_positive_noise() -> None:
    spec = _spec()
    spec["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"]["paired_sd"] = 0.0
    result = plan.build_plan(spec)
    row = result["hypothesis_plans"]["SYNTH-HYP-00"]
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
            lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(
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
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd=False), "JSON number"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd=True), "JSON number"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd="0.001"), "JSON number"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd=10 ** 1000), "JSON number"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd=1e308), "unrepresentable"),
        (lambda s: s["metrics"]["canonical_nll"].update(domain_floor=True), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(repeatability95="0"), "JSON number"),
        (lambda s: s["metrics"]["canonical_nll"].update(domain_floor_justification_sha256="x"), "SHA-256"),
        (lambda s: s["metrics"]["canonical_nll"].update(repeatability_evidence_sha256="g" * 64), "SHA-256"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd_evidence_sha256="0" * 63), "SHA-256"),
        (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd_evidence_sha256="A" * 64), "SHA-256"),
    ],
)
def test_reject_unreviewed_power_relaxation_or_forged_hash(mutator, match) -> None:
    spec = copy.deepcopy(_spec())
    mutator(spec)
    with pytest.raises(plan.PowerPlanContractError, match=match):
        plan.build_plan(spec)


@pytest.mark.parametrize("mutator,match", [
    (lambda s: s.pop("primary_non_target_hypotheses"), "explicit list"),
    (lambda s: s.update(primary_non_target_hypotheses=[]), "explicit list"),
    (lambda s: s.update(primary_non_target_family_size=1), "must equal declared"),
    (lambda s: s.update(primary_non_target_family_size=True), "must equal declared"),
    (lambda s: s["primary_non_target_hypotheses"][1].update(hypothesis_id="SYNTH-HYP-00"), "duplicate hypothesis_id"),
    (lambda s: s["primary_non_target_hypotheses"][1].update(intervention="B1", non_target_metric="canonical_nll"), "duplicate primary"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(non_target_metric="unknown"), "lacks planning metric"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(target_property="canonical_nll"), "non-target cannot equal target"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(inferential_unit="PROMPT_VARIANT"), "source medical case"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(primary=False), "primary hard-gate"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(coupling_tag="NOT_REVIEWED"), "coupling_tag"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(coupling_tag=[]), "coupling_tag"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(hypothesis_id="x"), "stable uppercase"),
    (lambda s: s["primary_non_target_hypotheses"][0].update(extra_field="hidden"), "exact hypothesis fields"),
])
def test_unreviewed_family_declaration_rejects_count_or_membership_drift(mutator, match) -> None:
    spec = copy.deepcopy(_spec())
    mutator(spec)
    with pytest.raises(plan.PowerPlanContractError, match=match):
        plan.build_plan(spec)


def test_unreviewed_family_digest_binds_order_and_member_content() -> None:
    original = plan.build_plan(_spec())
    spec = _spec()
    spec["primary_non_target_hypotheses"].reverse()
    reordered = plan.build_plan(spec)
    assert reordered["primary_non_target_family_size"] == original["primary_non_target_family_size"]
    assert reordered["unreviewed_family_declaration_sha256"] != original["unreviewed_family_declaration_sha256"]
    assert reordered["family_membership_frozen_and_independently_reviewed"] is False
    spec = _spec()
    spec["primary_non_target_hypotheses"][0]["coupling_tag"] = "STRUCTURALLY_DISTINCT"
    changed = plan.build_plan(spec)
    assert changed["unreviewed_family_declaration_sha256"] != original["unreviewed_family_declaration_sha256"]
    assert changed["final_90_percent_power_qualified"] is False


@pytest.mark.parametrize("mutator,reason", [
    (lambda s: s.pop("paired_nuisance_by_hypothesis"), "one hypothesis-specific"),
    (lambda s: s["paired_nuisance_by_hypothesis"].pop("SYNTH-HYP-00"), "one hypothesis-specific"),
    (lambda s: s["paired_nuisance_by_hypothesis"].update(GHOST={}), "one hypothesis-specific"),
    (lambda s: s["metrics"]["canonical_nll"].update(paired_sd=0.001), "must not supply metric-level paired_sd"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(nuisance_scope="QUALIFIED"), "unqualified development scope"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(nuisance_scope=[]), "unqualified development scope"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(hidden=True), "exact nuisance fields"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].pop("paired_sd"), "exact nuisance fields"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd=False), "JSON number"),
    (lambda s: s["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"].update(paired_sd_evidence_sha256="G" * 64), "SHA-256"),
])
def test_hypothesis_specific_nuisance_fails_closed_on_missing_or_invalid_cell(mutator, reason):
    spec = copy.deepcopy(_spec())
    mutator(spec)
    with pytest.raises(plan.PowerPlanContractError, match=reason):
        plan.build_plan(spec)


def test_intervention_specific_nuisance_cannot_be_masked_by_same_metric_good_cell():
    spec = _spec()
    # Two declared interventions on canonical NLL, wildly different source-case SDs.
    spec["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"]["paired_sd"] = 0.001
    spec["paired_nuisance_by_hypothesis"]["SYNTH-HYP-02"]["paired_sd"] = 5.0
    result = plan.build_plan(spec)
    assert result["hypothesis_plans"]["SYNTH-HYP-00"]["non_target_metric"] == "canonical_nll"
    assert result["hypothesis_plans"]["SYNTH-HYP-02"]["non_target_metric"] == "canonical_nll"
    assert result["hypothesis_plans"]["SYNTH-HYP-00"]["planned_clusters_meet_normal_approx_target"] is True
    assert result["hypothesis_plans"]["SYNTH-HYP-02"]["planned_clusters_meet_normal_approx_target"] is False
    assert result["hypothesis_plans"]["SYNTH-HYP-02"]["normal_approx_required_clusters_at_margin"] > 4096
    assert result["all_declared_hypotheses_meet_illustrative_normal_approx_target"] is False
    assert "all_metrics_meet_normal_approx_target" not in result
    assert result["final_90_percent_power_qualified"] is False
    assert result["confirmatory_execution_authorized"] is False

def test_direct_cli_reports_only_dev_contract_status_without_pythonpath(tmp_path: Path) -> None:
    spec = tmp_path / "input.json"
    target = tmp_path / "output.json"
    spec.write_text(json.dumps(_spec()), encoding="utf-8")
    script = Path(__file__).resolve().parents[2] / "scripts" / "v5_power_margin_plan.py"
    completed = subprocess.run(
        [sys.executable, str(script), "--spec", str(spec), "--output", str(target)],
        cwd=tmp_path, capture_output=True, text=True, check=True,
        env={"PATH": "/usr/bin:/bin"},
    )
    receipt = json.loads(completed.stdout)
    result = json.loads(target.read_text(encoding="utf-8"))
    assert receipt["status"] == "PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT"
    assert receipt["final_90_percent_power_qualified"] is False
    assert result["schema"] == "commandmed.v5.power-margin-plan.v2"
    assert result["confirmatory_execution_authorized"] is False


def test_direct_cli_rejects_fake_family_nuisance_without_output(tmp_path: Path) -> None:
    data = _spec()
    data["paired_nuisance_by_hypothesis"].pop("SYNTH-HYP-02")
    src = tmp_path / "invalid.json"
    out = tmp_path / "should-not-exist.json"
    src.write_text(json.dumps(data), encoding="utf-8")
    script = Path(__file__).resolve().parents[2] / "scripts" / "v5_power_margin_plan.py"
    completed = subprocess.run(
        [sys.executable, str(script), "--spec", str(src), "--output", str(out)],
        cwd=tmp_path, capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"},
    )
    assert completed.returncode != 0
    assert "one hypothesis-specific" in completed.stderr
    assert not out.exists()

def test_large_finite_nuisance_exposes_contract_error_not_overflow() -> None:
    spec = _spec()
    spec["paired_nuisance_by_hypothesis"]["SYNTH-HYP-00"]["paired_sd"] = 1e308
    with pytest.raises(plan.PowerPlanContractError, match="unrepresentable"):
        plan.build_plan(spec)

def _run_unambiguous_input_cli(
    tmp_path: Path, raw_json: str
) -> tuple[subprocess.CompletedProcess[str], Path]:
    spec = tmp_path / "submitted-input.json"
    output = tmp_path / "unqualified-plan.json"
    spec.write_text(raw_json, encoding="utf-8")
    script = Path(__file__).resolve().parents[2] / "scripts" / "v5_power_margin_plan.py"
    completed = subprocess.run(
        [sys.executable, str(script), "--spec", str(spec), "--output", str(output)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin"},
    )
    return completed, output


@pytest.mark.parametrize(
    "mutator,reason",
    [
        (
            lambda raw: raw[:-1] + ', "primary_non_target_family_size": 1, "primary_non_target_family_size": 4}',
            "AMBIGUOUS_JSON_DUPLICATE_KEY",
        ),
        (
            lambda raw: raw.replace(
                '"paired_sd": 0.2', '"paired_sd": 0.1, "paired_sd": 0.2', 1
            ),
            "AMBIGUOUS_JSON_DUPLICATE_KEY",
        ),
        (
            lambda raw: raw.replace(
                '"hypothesis_id": "SYNTH-HYP-00"',
                '"hypothesis_id": "SYNTH-HYP-01", "hypothesis_id": "SYNTH-HYP-00"',
                1,
            ),
            "AMBIGUOUS_JSON_DUPLICATE_KEY",
        ),
        (
            lambda raw: raw.replace(
                '"paired_sd": 0.2',
                '"paired_sd": 0.1, "paired_\\u0073d": 0.2',
                1,
            ),
            "AMBIGUOUS_JSON_DUPLICATE_KEY",
        ),
        (
            lambda raw: raw.replace('"paired_sd": 0.2', '"paired_sd": NaN', 1),
            "NONSTANDARD_JSON_CONSTANT",
        ),
        (
            lambda raw: raw.replace('"paired_sd": 0.2', '"paired_sd": Infinity', 1),
            "NONSTANDARD_JSON_CONSTANT",
        ),
    ],
)
def test_direct_cli_rejects_ambiguous_or_nonstandard_json_at_all_depths(
    tmp_path: Path, mutator, reason: str
) -> None:
    original = json.dumps(_spec(), sort_keys=True)
    submitted = mutator(original)
    assert submitted != original
    completed, output = _run_unambiguous_input_cli(tmp_path, submitted)
    assert completed.returncode != 0
    assert reason in completed.stderr
    assert not output.exists()


def test_direct_cli_accepts_single_key_equivalent_unicode_json(
    tmp_path: Path,
) -> None:
    original = json.dumps(_spec(), sort_keys=True)
    completed, output = _run_unambiguous_input_cli(tmp_path, original)
    assert completed.returncode == 0, completed.stderr
    receipt = json.loads(completed.stdout)
    assert receipt["status"] == "PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT"
    assert receipt["final_90_percent_power_qualified"] is False
    result = json.loads(output.read_text(encoding="utf-8"))
    assert result["family_membership_frozen_and_independently_reviewed"] is False
    assert result["confirmatory_execution_authorized"] is False


def test_reject_json_array_root_and_invalid_syntax(tmp_path: Path) -> None:
    for idx, (raw, reason) in enumerate((
        ("[]", "POWER_PLAN_ROOT_MUST_BE_OBJECT"),
        ('{"scope": "DEVELOPMENT_ONLY_POWER_PLANNING"', "INVALID_POWER_PLAN_JSON"),
    )):
        case = tmp_path / str(idx)
        case.mkdir()
        completed, output = _run_unambiguous_input_cli(case, raw)
        assert completed.returncode != 0
        assert reason in completed.stderr
        assert not output.exists()



def test_direct_cli_does_not_overwrite_its_input(tmp_path: Path) -> None:
    source = tmp_path / "source-plan.json"
    original = json.dumps(_spec(), sort_keys=True)
    source.write_text(original, encoding="utf-8")
    script = Path(__file__).resolve().parents[2] / "scripts" / "v5_power_margin_plan.py"
    result = subprocess.run(
        [sys.executable, str(script), "--spec", str(source), "--output", str(source)],
        cwd=tmp_path, capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"},
    )
    assert result.returncode != 0
    assert "OUTPUT_ALREADY_EXISTS" in result.stderr
    assert source.read_text(encoding="utf-8") == original
    assert "PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT" not in result.stdout


def test_direct_cli_does_not_overwrite_existing_evidence(tmp_path: Path) -> None:
    destination = tmp_path / "unqualified-plan.json"
    original = b"ORIGINAL_IMMUTABLE_EVIDENCE_2026-10-10\n"
    destination.write_bytes(original)
    result, output = _run_unambiguous_input_cli(tmp_path, json.dumps(_spec()))
    assert output == destination
    assert result.returncode != 0
    assert "OUTPUT_ALREADY_EXISTS" in result.stderr
    assert output.read_bytes() == original
    assert "PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT" not in result.stdout


def test_direct_cli_refuses_existing_evidence_symlink(tmp_path: Path) -> None:
    target = tmp_path / "untouchable-source-evidence.txt"
    target.write_text("EVIDENCE_MUST_BE_PRESERVED", encoding="utf-8")
    destination = tmp_path / "unqualified-plan.json"
    destination.symlink_to(target)
    result, output = _run_unambiguous_input_cli(tmp_path, json.dumps(_spec()))
    assert result.returncode != 0
    assert "OUTPUT_ALREADY_EXISTS" in result.stderr
    assert output.is_symlink()
    assert target.read_text(encoding="utf-8") == "EVIDENCE_MUST_BE_PRESERVED"


def test_repeated_identical_cli_invocation_never_rewrites_first_receipt(
    tmp_path: Path,
) -> None:
    spec = json.dumps(_spec())
    first, output = _run_unambiguous_input_cli(tmp_path, spec)
    assert first.returncode == 0, first.stderr
    first_bytes = output.read_bytes()
    second, output2 = _run_unambiguous_input_cli(tmp_path, spec)
    assert second.returncode != 0
    assert "OUTPUT_ALREADY_EXISTS" in second.stderr
    assert output2.read_bytes() == first_bytes
