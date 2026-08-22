from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.lineage import (
    compute_lineage_contract_sha256,
    compute_lineage_record_sha256,
    evaluate_lineage_admission,
    validate_lineage_contract,
    validate_lineage_record,
    validate_lineage_registry,
)


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = json.loads((ROOT / "data/lineage/lineage_contract.json").read_text(encoding="utf-8"))


def base_record(**overrides):
    record = {
        "asset_id": "fixture-asset-001",
        "asset_class": "DATASET_OR_CORPUS",
        "canonical_name": "Fixture Dataset",
        "record_version": "1",
        "source_identifier": "github:org/repo",
        "source_uri": "https://github.com/org/repo",
        "source_revision": "a" * 40,
        "source_verification_status": "VERIFIED",
        "source_evidence_uri": "https://github.com/org/repo/tree/" + "a" * 40,
        "declared_use": "TRAINING_OR_ADAPTATION",
        "access_class": "PUBLIC",
        "rights_state": "SUPPORTED",
        "rights_evidence_uri": "https://github.com/org/repo/blob/" + "a" * 40 + "/LICENSE",
        "artifact_binding_state": "IMMUTABLE_REVISION_LOCATOR",
        "artifact_locator": "data/train.jsonl",
        "phi_privacy_state": "NO_PHI_KNOWN",
        "purpose": "TRAIN",
        "quarantine_state": "NOT_QUARANTINED",
        "contamination_state": "ASSESSED_CLEAN",
    }
    record.update(overrides)
    return record


class TestLineageContract(unittest.TestCase):
    def test_canonical_contract_is_valid(self):
        self.assertEqual(validate_lineage_contract(CONTRACT), [])

    def test_contract_hash_is_representation_order_stable(self):
        reordered = copy.deepcopy(CONTRACT)
        reordered["asset_classes"] = list(reversed(reordered["asset_classes"]))
        reordered["invariants"] = list(reversed(reordered["invariants"]))
        self.assertEqual(
            compute_lineage_contract_sha256(CONTRACT),
            compute_lineage_contract_sha256(reordered),
        )

    def test_invalid_contract_cannot_authorize(self):
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"]
            if item["invariant_id"] != "ADMISSION_IS_COMPUTED"
        ]
        result = evaluate_lineage_admission(base_record(), weakened)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["INVALID_CONTRACT"])
        self.assertIsNone(result["contract_sha256"])
        self.assertIsNone(result["record_sha256"])

    def test_contract_rejects_duplicate_closed_vocabulary_value(self):
        bad = copy.deepcopy(CONTRACT)
        bad["admission_states"].append("ELIGIBLE")
        errors = validate_lineage_contract(bad)
        self.assertTrue(any("duplicate" in error.lower() for error in errors))

    def test_contract_rejects_unknown_admission_state(self):
        bad = copy.deepcopy(CONTRACT)
        bad["admission_states"].append("MAYBE")
        errors = validate_lineage_contract(bad)
        self.assertTrue(any("unknown values" in error for error in errors))

    def test_contract_rejects_unknown_contract_id_and_schema_version(self):
        bad = copy.deepcopy(CONTRACT)
        bad["contract_id"] = "other-contract"
        bad["schema_version"] = "2.0"
        errors = validate_lineage_contract(bad)
        self.assertTrue(any("unsupported contract_id" in error for error in errors))
        self.assertTrue(any("unsupported schema_version" in error for error in errors))


class TestLineageRecordValidation(unittest.TestCase):
    def test_valid_immutable_revision_locator_record(self):
        self.assertEqual(validate_lineage_record(base_record(), CONTRACT), [])

    def test_valid_direct_digest_record(self):
        record = base_record(
            artifact_binding_state="DIRECT_DIGEST",
            content_sha256="b" * 64,
            source_revision="UNBOUND",
        )
        record.pop("artifact_locator")
        self.assertEqual(validate_lineage_record(record, CONTRACT), [])

    def test_mutable_revision_cannot_masquerade_as_immutable_binding(self):
        record = base_record(source_revision="latest")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("40- or 64-hex" in error for error in errors))

    def test_named_version_cannot_masquerade_as_immutable_binding(self):
        record = base_record(source_revision="v1.0")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("40- or 64-hex" in error for error in errors))

    def test_direct_digest_rejects_malformed_sha256(self):
        record = base_record(
            artifact_binding_state="DIRECT_DIGEST",
            content_sha256="abc",
        )
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("64 hex" in error for error in errors))

    def test_self_asserted_admission_is_rejected(self):
        record = base_record(admission_state="ELIGIBLE")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("computed output field 'admission_state'" in error for error in errors))

    def test_self_asserted_record_identity_is_rejected(self):
        record = base_record(record_sha256="f" * 64)
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("computed output field 'record_sha256'" in error for error in errors))

    def test_payload_marker_is_rejected(self):
        record = base_record(case_text="not real PHI, still prohibited payload key")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("Prohibited payload key" in error for error in errors))

    def test_optional_controlled_fields_are_fail_closed_when_supplied(self):
        record = base_record(contamination_state="MAGICALLY_CLEAN")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("invalid contamination_state" in error for error in errors))

    def test_spdx_metadata_rejects_control_characters(self):
        record = base_record(spdx_license_expression="MIT\nOR Apache-2.0")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("unsafe/control content" in error for error in errors))

    def test_registry_rejects_duplicate_asset_id(self):
        valid, errors = validate_lineage_registry([base_record(), base_record()], CONTRACT)
        self.assertFalse(valid)
        self.assertTrue(any("duplicate asset_id" in error for error in errors))

    def test_malformed_list_does_not_raise(self):
        record = base_record(
            asset_class="MODEL_GENERATED_OR_SYNTHETIC_ASSET",
            parent_asset_ids=[{"not": "a string"}],
            origin_type="SYNTHETIC",
            generator_identity="provider:model@rev",
            generation_config_id="cfg-001",
            output_use_evidence_uri="https://example.test/terms",
            purpose=None,
            quarantine_state=None,
        )
        record.pop("purpose")
        record.pop("quarantine_state")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(errors)


class TestAdmission(unittest.TestCase):
    def test_eligible_record(self):
        result = evaluate_lineage_admission(base_record(), CONTRACT)
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])
        self.assertRegex(result["contract_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(result["record_sha256"], r"^[0-9a-f]{64}$")

    def test_unbound_exact_use_degrades_to_reference_only(self):
        record = base_record(
            artifact_binding_state="UNBOUND",
            source_revision="UNBOUND",
        )
        record.pop("artifact_locator")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "REFERENCE_ONLY")
        self.assertEqual(result["reason_codes"], ["ARTIFACT_UNBOUND"])

    def test_unresolved_rights_block_even_if_source_verified(self):
        record = base_record(
            rights_state="UNRESOLVED",
            rights_evidence_uri="UNRESOLVED",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("RIGHTS_UNRESOLVED", result["reason_codes"])

    def test_incompatible_rights_are_prohibited(self):
        record = base_record(rights_state="INCOMPATIBLE")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertEqual(result["reason_codes"], ["RIGHTS_INCOMPATIBLE"])

    def test_unknown_privacy_blocks_training(self):
        record = base_record(phi_privacy_state="UNRESOLVED")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("PRIVACY_UNRESOLVED", result["reason_codes"])

    def test_phi_is_prohibited_for_training(self):
        record = base_record(phi_privacy_state="RESTRICTED_OR_PHI")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("RESTRICTED_OR_PHI", result["reason_codes"])

    def test_private_gold_training_is_prohibited(self):
        record = base_record(
            asset_class="PRIVATE_GOLD_METADATA",
            purpose="PRIVATE_GOLD",
            quarantine_state="PRIVATE_GOLD",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PRIVATE_GOLD_PROHIBITED_USE", result["reason_codes"])

    def test_unresolved_contamination_blocks_training(self):
        record = base_record(contamination_state="PENDING")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("CONTAMINATION_UNRESOLVED", result["reason_codes"])

    def test_high_risk_overlap_prohibits_training(self):
        record = base_record(contamination_state="OVERLAP_OR_HIGH_RISK")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("CONTAMINATION_HIGH_RISK", result["reason_codes"])

    def test_reference_only_access_degrades_executable_use(self):
        record = base_record(access_class="REFERENCE_ONLY")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "REFERENCE_ONLY")
        self.assertEqual(result["reason_codes"], ["ACCESS_REFERENCE_ONLY"])

    def test_source_verification_does_not_bind_artifact(self):
        record = base_record(
            artifact_binding_state="UNBOUND",
            source_revision="UNBOUND",
            source_verification_status="VERIFIED",
        )
        record.pop("artifact_locator")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "REFERENCE_ONLY")
        self.assertIn("ARTIFACT_UNBOUND", result["reason_codes"])

    def test_source_unresolved_blocks(self):
        record = base_record(source_verification_status="UNRESOLVED")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("SOURCE_UNVERIFIED", result["reason_codes"])


class TestSyntheticAndIdentity(unittest.TestCase):
    def synthetic_record(self, **overrides):
        record = base_record(
            asset_class="MODEL_GENERATED_OR_SYNTHETIC_ASSET",
            origin_type="MODEL_GENERATED",
            parent_asset_ids=["parent-b", "parent-a"],
            generator_identity="provider:model@" + "c" * 40,
            generation_config_id="cfg-001",
            output_use_evidence_uri="https://provider.example/terms/revision/1",
        )
        record.pop("purpose")
        record.pop("quarantine_state")
        record.update(overrides)
        return record

    def test_generated_training_requires_parent_generator_and_output_evidence(self):
        record = self.synthetic_record()
        record.pop("parent_asset_ids")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("parent_asset_ids" in error for error in errors))
        self.assertEqual(evaluate_lineage_admission(record, CONTRACT)["state"], "BLOCKED")

    def test_generated_training_requires_output_use_evidence(self):
        record = self.synthetic_record()
        record.pop("output_use_evidence_uri")
        errors = validate_lineage_record(record, CONTRACT)
        self.assertTrue(any("output_use_evidence_uri" in error for error in errors))

    def test_parent_order_does_not_change_scientific_identity(self):
        first = self.synthetic_record()
        second = copy.deepcopy(first)
        second["parent_asset_ids"] = list(reversed(second["parent_asset_ids"]))
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_audit_timestamp_and_local_path_do_not_change_identity(self):
        first = base_record()
        second = copy.deepcopy(first)
        second["retrieval_timestamp"] = "2026-08-22T23:00:00+03:00"
        second["local_path"] = "C:/tmp/asset"
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_identity_bearing_source_revision_changes_identity(self):
        first = base_record()
        second = copy.deepcopy(first)
        second["source_revision"] = "b" * 40
        self.assertNotEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_hex_case_is_representation_only_for_identity(self):
        first = base_record(source_revision="A" * 40)
        second = base_record(source_revision="a" * 40)
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_reason_codes_are_deterministic_sorted(self):
        record = base_record(
            rights_state="UNRESOLVED",
            rights_evidence_uri="UNRESOLVED",
            phi_privacy_state="UNRESOLVED",
            contamination_state="PENDING",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["reason_codes"], sorted(result["reason_codes"]))


class TestSpec001Compatibility(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmarks = json.loads(
            (ROOT / "data/eval/benchmarks.json").read_text(encoding="utf-8")
        )

    def by_id(self, benchmark_id):
        return next(item for item in self.benchmarks if item["benchmark_id"] == benchmark_id)

    def test_canonical_healthbench_revision_and_artifact_map_to_immutable_binding(self):
        benchmark = self.by_id("healthbench_consensus")
        record = {
            "asset_id": "benchmark:" + benchmark["benchmark_id"],
            "asset_class": "BENCHMARK_OR_EVALUATION_ASSET",
            "canonical_name": benchmark["canonical_name"],
            "record_version": "1",
            "source_identifier": benchmark["source_identifier"],
            "source_uri": benchmark["source_uri"],
            "source_revision": benchmark["source_revision"],
            "source_verification_status": benchmark["verification_status"],
            "source_evidence_uri": benchmark["source_uri"] + "/tree/" + benchmark["source_revision"],
            "declared_use": "DEVELOPMENT_EVALUATION",
            "access_class": benchmark["access_class"],
            "rights_state": "SUPPORTED",
            "rights_evidence_uri": benchmark["license_source_uri"],
            "artifact_binding_state": "IMMUTABLE_REVISION_LOCATOR",
            "artifact_locator": benchmark["artifact_version"],
            "phi_privacy_state": "NOT_APPLICABLE",
            "purpose": "PUBLIC_EXTERNAL_EVAL",
            "quarantine_state": "NOT_QUARANTINED",
        }
        self.assertEqual(validate_lineage_record(record, CONTRACT), [])
        self.assertEqual(evaluate_lineage_admission(record, CONTRACT)["state"], "ELIGIBLE")

    def test_canonical_reference_only_component_specific_family_does_not_broaden(self):
        benchmark = self.by_id("medabstain")
        self.assertEqual(benchmark["artifact_version"], "UNBOUND")
        self.assertEqual(benchmark["license_status"], "COMPONENT_SPECIFIC")
        record = {
            "asset_id": "benchmark:" + benchmark["benchmark_id"],
            "asset_class": "BENCHMARK_OR_EVALUATION_ASSET",
            "canonical_name": benchmark["canonical_name"],
            "record_version": "1",
            "source_identifier": benchmark["source_identifier"],
            "source_uri": benchmark["source_uri"],
            "source_revision": benchmark["source_revision"],
            "source_verification_status": benchmark["verification_status"],
            "source_evidence_uri": benchmark["source_uri"],
            "declared_use": "DEVELOPMENT_EVALUATION",
            "access_class": benchmark["access_class"],
            "rights_state": "CONDITIONAL",
            "rights_evidence_uri": benchmark["license_source_uri"],
            "artifact_binding_state": "UNBOUND",
            "phi_privacy_state": "NOT_APPLICABLE",
            "purpose": "PUBLIC_EXTERNAL_EVAL",
            "quarantine_state": "NOT_QUARANTINED",
        }
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertNotEqual(result["state"], "ELIGIBLE")
        self.assertIn("RIGHTS_UNRESOLVED", result["reason_codes"])


if __name__ == "__main__":
    unittest.main()
