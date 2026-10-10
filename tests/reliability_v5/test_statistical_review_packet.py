"""Model-free, nonselective bridge across pinned descriptive nuisance diagnostics."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_manuscript_development_evidence_audit as source_audit
import v5_s1_statistical_review_packet as packet


def originals():
    sd = json.loads((source_audit.ROOT / source_audit.LOCKED_SOURCES["sd_inventory"][0]).read_text())
    icc = json.loads((source_audit.ROOT / source_audit.LOCKED_SOURCES["icc_inventory"][0]).read_text())
    return sd, icc


def test_real_24_group_72_cell_unqualified_review_packet() -> None:
    assert source_audit.audit()["frozen_source_files_verified"] == 307
    sd, icc = originals()
    x = packet.create_packet(sd, icc)
    assert x["descriptive_intervention_metric_split_groups"] == len(x["groups"]) == 24
    assert x["descriptive_condition_seed_metric_split_cells"] == 72
    assert sum(g["negative_sample_icc_cells"] for g in x["groups"]) == 12
    assert {tuple((g["intervention"],g["split"],g["metric"])) for g in x["groups"]} == {
        (name, split, metric) for name in packet.INTERVENTIONS
        for split in packet.SPLITS for metric in packet.METRICS
    }
    for g in x["groups"]:
        assert [e["seed"] for e in g["seed_level_development_evidence"]] == [11,29,47]
        assert g["crossed_source_case_calculator_seed_nuisance_qualified"] is False
    assert x["primary_non_target_family_size"] is None
    assert x["prospective_primary_non_target_hypothesis_family"] is None
    assert x["source_case_calculator_seed_crossed_covariance_model"] is None
    assert x["confirmatory_90_percent_power_qualified"] is False
    assert x["confirmatory_authorized"] is False
    assert x["independent_statistical_review_completed"] is False
    assert x["publication_or_clinical_authorized"] is False


def test_saved_packet_is_exact_fresh_deterministic_replay(tmp_path: Path) -> None:
    committed = source_audit.ROOT / (
        "artifacts/v5/development/s1-statistical-review-packet-2026-10-10/reviewer-packet.json"
    )
    saved = committed.read_bytes()
    assert saved == (json.dumps(packet.create_packet(*originals()),
                                sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    cmd = [sys.executable, str(source_audit.ROOT / "scripts/v5_s1_statistical_review_packet.py")]
    verified = subprocess.run(cmd + ["--verify", str(committed)], cwd=tmp_path,
                              capture_output=True, text=True)
    assert verified.returncode == 0, verified.stderr
    fresh = tmp_path / "fresh-review-packet.json"
    created = subprocess.run(cmd + ["--output", str(fresh)], cwd=tmp_path,
                             capture_output=True, text=True)
    assert created.returncode == 0, created.stderr
    assert fresh.read_bytes() == saved
    second = subprocess.run(cmd + ["--output", str(fresh)], cwd=tmp_path,
                            capture_output=True, text=True)
    assert second.returncode != 0
    assert fresh.read_bytes() == saved
    falsified = tmp_path / "falsified.json"
    falsified.write_bytes(saved + b"\n")
    mismatch = subprocess.run(cmd + ["--verify", str(falsified)], cwd=tmp_path,
                              capture_output=True, text=True)
    assert mismatch.returncode != 0
    assert "COMMITTED_REVIEW_PACKET_REPLAY_DRIFT" in mismatch.stderr
    assert falsified.read_bytes() == saved + b"\n"


@pytest.mark.parametrize("mutate,expected", [
    (lambda sd,icc: sd.update(primary_non_target_family_size=1), "SOURCE_SD_SCIENCE_AUTHORITY_DRIFT"),
    (lambda sd,icc: icc["boundaries"].update(final_90_percent_power_qualified=True),
     "ICC_SCIENCE_AUTHORITY_DRIFT"),
    (lambda sd,icc: icc["all_development_cells"][0].update(seed=29,condition="B1_29"), "DUPLICATE_OR_UNKNOWN_ICC_CELL"),
    (lambda sd,icc: icc["all_development_cells"][0].update(calculator_count=63),
     "SOURCE_CASE_OR_CONDITION_DRIFT"),
    (lambda sd,icc: icc["all_development_cells"][0].update(anovamom_rho_unclipped=0.2),
     "ICC_SIGN_STATUS_DRIFT"),
    (lambda sd,icc: icc["three_seed_between_effect_spreads"][0].update(uncertainty_qualified=True),
     "SEED_UNCERTAINTY_PROMOTED"),
    (lambda sd,icc: icc["three_seed_between_effect_spreads"][0]["seed_level_mean_delta_by_seed"].update({"29":0.0005}),
     "BETWEEN_SEED_SD_DRIFT"),
    (lambda sd,icc: sd["intervention_results"]["B1_11"]["splits"]["S1_CAL_EVAL"]["canonical_accuracy"].update(mean_delta_raw_orientation=0.03),
     "SEED_EFFECT_MISMATCH"),
    (lambda sd,icc: sd["intervention_results"]["B1_11"]["splits"]["S1_CAL_EVAL"]["canonical_accuracy"].update(paired_source_task_sample_sd=-0.1),
     "INVALID_PAIRED_SD"),
])
def test_fail_closed_on_missing_science_provenance_or_seed_alignment(mutate,expected) -> None:
    sd,icc=originals()
    mutate(sd,icc)
    with pytest.raises(packet.ReviewerPacketError,match=expected):
        packet.create_packet(sd,icc)
