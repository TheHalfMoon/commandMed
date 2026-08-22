"""Regression tests for reference-teacher laundering through derived artifacts."""

from __future__ import annotations

from src.commandmed.eval_contract.lineage import (
    evaluate_lineage_admission,
    validate_lineage_record,
)
from tests.eval_contract.test_lineage import CONTRACT, base_record


def derived_training_record(**overrides):
    """Build a derived training artifact with exact-use provenance metadata."""
    record = base_record(
        asset_id="derived-child-001",
        asset_class="DERIVED_RESEARCH_ARTIFACT",
        origin_type="DERIVED",
        parent_asset_ids=["parent-001"],
        generator_identity="deterministic:transform-v1",
        output_use_evidence_uri="https://example.test/derived-use-evidence",
    )
    record.pop("purpose")
    record.pop("quarantine_state")
    record.update(overrides)
    return record


def parent_record(**overrides):
    """Build a clean training parent for derived-artifact admission tests."""
    return base_record(asset_id="parent-001", **overrides)


class TestDerivedTeacherLaundering:
    """Fail-closed tests for derived artifacts entering training lineage."""

    def test_training_derived_artifact_requires_generator_provenance(self):
        """A derived training artifact cannot omit generator/producer identity."""
        child = derived_training_record()
        child.pop("generator_identity")
        errors = validate_lineage_record(child, CONTRACT)
        assert any("generator_identity" in error for error in errors)
        result = evaluate_lineage_admission(child, CONTRACT, [parent_record(), child])
        assert result["state"] == "BLOCKED"
        assert result["reason_codes"] == ["INVALID_RECORD"]

    def test_medgemma_derived_artifact_cannot_train(self):
        """Changing MedGemma output to DERIVED_RESEARCH_ARTIFACT does not bypass policy."""
        parent = parent_record()
        child = derived_training_record(
            generator_identity="google/medgemma-4b-it@" + "d" * 40,
        )
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        assert result["state"] == "PROHIBITED"
        assert "GENERATOR_TRAINING_PROHIBITED" in result["reason_codes"]

    def test_haidef_derived_artifact_cannot_train(self):
        """Changing HAI-DEF output to DERIVED_RESEARCH_ARTIFACT does not bypass policy."""
        parent = parent_record()
        child = derived_training_record(
            generator_identity="google/hai-def/reference@" + "e" * 40,
        )
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        assert result["state"] == "PROHIBITED"
        assert "GENERATOR_TRAINING_PROHIBITED" in result["reason_codes"]

    def test_non_model_derived_artifact_can_train_when_all_gates_pass(self):
        """A deterministic non-prohibited derivation remains eligible with complete evidence."""
        parent = parent_record()
        child = derived_training_record(generator_identity="deterministic:transform-v1")
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        assert result["state"] == "ELIGIBLE"
        assert result["reason_codes"] == []
