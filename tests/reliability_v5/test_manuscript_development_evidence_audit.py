"""Regression controls for the immutable development-only manuscript claim gate."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_manuscript_development_evidence_audit as audit


def _records() -> dict:
    return {
        name: json.loads((audit.ROOT / path).read_text(encoding="utf-8"))
        for name, (path, _) in audit.LOCKED_SOURCES.items()
        if name != "crosswalk"
    }


def test_real_immutable_evidence_and_all_307_frozen_entries() -> None:
    result = audit.audit()
    assert result["status"] == "PASS_DEVELOPMENT_ONLY_EVIDENCE_ADMISSION"
    assert result["descriptive_sd_cells"] == 72
    assert result["frozen_source_files_verified"] == 307
    assert result["confirmatory"] is False
    assert result["independent_peer_review"] is False


def test_scope_escalation_rejected_for_repeat_and_margins() -> None:
    for section, key in (("r1_receipt", "confirmatory"), ("r2_receipt", "reserve"),
                         ("margins", "publication_authorized"), ("sd_inventory", "confirmatory_power_claim")):
        records = _records()
        records[section][key] = True
        with pytest.raises(audit.ManuscriptEvidenceAuditError):
            audit.assert_development_semantics(records)


def test_fake_power_family_or_shrunk_margin_rejected() -> None:
    records = _records()
    records["sd_inventory"]["primary_non_target_family_size"] = 1
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="POSTHOC_FAMILY_SIZE"):
        audit.assert_development_semantics(records)
    records = _records()
    records["margins"]["metrics"]["canonical_accuracy"]["meaningful_margin"] = 0.001
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="MARGIN_POSTHOC_DRIFT"):
        audit.assert_development_semantics(records)


def test_missing_or_invalid_source_is_fail_closed(tmp_path: Path) -> None:
    path, sha = audit.LOCKED_SOURCES["crosswalk"]
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="MISSING_LOCKED_SOURCE"):
        audit._locked_file(tmp_path, path, sha)
    full = tmp_path / path
    full.parent.mkdir(parents=True)
    full.write_text("forged development outcome\n", encoding="utf-8")
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="SOURCE_SHA256_MISMATCH"):
        audit._locked_file(tmp_path, path, sha)


def test_nonfinite_sd_and_changed_repeatability_rejected() -> None:
    records = _records()
    records["sd_inventory"]["intervention_results"]["B1_11"]["splits"]["S1_DEV_EVAL"]["canonical_accuracy"]["paired_source_task_sample_sd"] = float("nan")
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="INVALID_SD_CELL"):
        audit.assert_development_semantics(records)
    records = _records()
    records["paired"]["metrics"]["canonical_accuracy"]["repeatability95"] = 0.001
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="PAIRED_REPEATABILITY_CHANGED"):
        audit.assert_development_semantics(records)


def test_frozen_307_entry_manifest_is_itself_cryptographically_pinned(tmp_path: Path) -> None:
    manifest = audit.ROOT / audit.FROZEN_BINDINGS_RELATIVE
    assert audit._digest(manifest) == audit.FROZEN_BINDINGS_SHA256
    path = tmp_path / audit.FROZEN_BINDINGS_RELATIVE
    path.parent.mkdir(parents=True)
    original = json.loads(manifest.read_text(encoding="utf-8"))
    assert len(original["unchanged_entry_files"]) == 307
    path.write_text(json.dumps(original) + "\n", encoding="utf-8")
    with pytest.raises(audit.ManuscriptEvidenceAuditError, match="SOURCE_SHA256_MISMATCH"):
        audit._locked_file(tmp_path, audit.FROZEN_BINDINGS_RELATIVE, audit.FROZEN_BINDINGS_SHA256)
