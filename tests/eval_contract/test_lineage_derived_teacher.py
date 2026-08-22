"""Regression tests for reference-teacher laundering across asset classes."""

from __future__ import annotations

import copy
import unittest

from src.commandmed.eval_contract.lineage import (
    evaluate_lineage_admission,
    validate_lineage_contract,
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


def generated_dataset_record(**overrides):
    """Build model-generated training data while retaining the generic dataset class."""
    record = base_record(
        asset_id="dataset-child-001",
        asset_class="DATASET_OR_CORPUS",
        origin_type="MODEL_GENERATED",
        parent_asset_ids=["parent-001"],
        generator_identity="provider:model@" + "c" * 40,
        generation_config_id="cfg-dataset-001",
        output_use_evidence_uri="https://provider.example/terms/revision/1",
    )
    record.update(overrides)
    return record


def parent_record(**overrides):
    """Build a clean original training parent for provenance propagation tests."""
    return base_record(asset_id="parent-001", **overrides)


class TestDerivedTeacherLaundering(unittest.TestCase):
    """Fail-closed tests for generated or derived content entering training lineage."""

    def test_contract_requires_training_origin_provenance_invariant(self):
        """The contract cannot remove the class-independent training-origin gate."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"]
            if item["invariant_id"] != "TRAINING_ORIGIN_PROVENANCE_REQUIRED"
        ]
        errors = validate_lineage_contract(weakened)
        self.assertTrue(
            any("TRAINING_ORIGIN_PROVENANCE_REQUIRED" in error for error in errors)
        )

    def test_training_record_requires_origin_type(self):
        """A training record cannot rely on an implicit original-origin assumption."""
        record = base_record()
        record.pop("origin_type")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("training/adaptation requires valid 'origin_type'" in e for e in errors))
        self.assertEqual(
            evaluate_lineage_admission(record, CONTRACT)["reason_codes"],
            ["INVALID_RECORD"],
        )

    def test_non_original_dataset_requires_complete_provenance(self):
        """Relabeling generated output as DATASET_OR_CORPUS cannot omit its producer chain."""
        record = base_record(origin_type="MODEL_GENERATED")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("parent_asset_ids" in error for error in errors))
        self.assertTrue(any("generator_identity" in error for error in errors))
        self.assertTrue(any("generation_config_id" in error for error in errors))
        self.assertTrue(any("output_use_evidence_uri" in error for error in errors))

    def test_training_derived_artifact_requires_generator_provenance(self):
        """A derived training artifact cannot omit generator/producer identity."""
        child = derived_training_record()
        child.pop("generator_identity")
        errors = validate_lineage_record(child, CONTRACT)
        self.assertTrue(any("generator_identity" in error for error in errors))
        result = evaluate_lineage_admission(child, CONTRACT, [parent_record(), child])
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["INVALID_RECORD"])

    def test_medgemma_derived_artifact_cannot_train(self):
        """Changing MedGemma output to DERIVED_RESEARCH_ARTIFACT does not bypass policy."""
        parent = parent_record()
        child = derived_training_record(
            generator_identity="google/medgemma-4b-it@" + "d" * 40,
        )
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])

    def test_haidef_derived_artifact_cannot_train(self):
        """Changing HAI-DEF output to DERIVED_RESEARCH_ARTIFACT does not bypass policy."""
        parent = parent_record()
        child = derived_training_record(
            generator_identity="google/hai-def/reference@" + "e" * 40,
        )
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])

    def test_medgemma_dataset_relabel_cannot_train(self):
        """MedGemma output cannot evade policy by claiming DATASET_OR_CORPUS and ORIGINAL."""
        record = base_record(
            asset_class="DATASET_OR_CORPUS",
            origin_type="ORIGINAL",
            canonical_name="MedGemma generated responses",
            source_identifier="huggingface:google/medgemma-4b-it",
            source_uri="https://huggingface.co/google/medgemma-4b-it",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])

    def test_haidef_dataset_relabel_cannot_train(self):
        """HAI-DEF output cannot evade policy by claiming a generic dataset class."""
        record = base_record(
            asset_class="DATASET_OR_CORPUS",
            origin_type="ORIGINAL",
            canonical_name="HAI-DEF reference teacher output",
            source_identifier="google:health-ai-developer-foundations/output",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])

    def test_original_origin_cannot_carry_generator_identity(self):
        """Contradictory original-origin claims fail validation instead of broadening lineage."""
        record = base_record(
            origin_type="ORIGINAL",
            generator_identity="provider:model@" + "f" * 40,
        )
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("origin_type='ORIGINAL'" in error for error in errors))

    def test_non_model_derived_artifact_can_train_when_all_gates_pass(self):
        """A deterministic non-prohibited derivation remains eligible with complete evidence."""
        parent = parent_record()
        child = derived_training_record(generator_identity="deterministic:transform-v1")
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])

    def test_non_prohibited_generated_dataset_can_train_with_complete_provenance(self):
        """Class-independent provenance does not prohibit a fully evidenced allowed generator."""
        parent = parent_record()
        child = generated_dataset_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])


if __name__ == "__main__":
    unittest.main()