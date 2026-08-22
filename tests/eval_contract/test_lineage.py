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
    """Build a fully resolved synthetic training record with no external payload."""
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
        "origin_type": "ORIGINAL",
    }
    record.update(overrides)
    return record


def synthetic_record(**overrides):
    """Build a generated child whose training lineage references one parent."""
    record = base_record(
        asset_id="synthetic-child-001",
        asset_class="MODEL_GENERATED_OR_SYNTHETIC_ASSET",
        origin_type="MODEL_GENERATED",
        parent_asset_ids=["parent-001"],
        generator_identity="provider:model@" + "c" * 40,
        generation_config_id="cfg-001",
        output_use_evidence_uri="https://provider.example/terms/revision/1",
    )
    record.pop("purpose")
    record.pop("quarantine_state")
    record.update(overrides)
    return record


class TestLineageContract(unittest.TestCase):
    """Contract immutability and fail-closed policy tests."""

    def test_canonical_contract_is_valid(self):
        """The checked-in Spec 003 contract validates cleanly."""
        self.assertEqual(validate_lineage_contract(CONTRACT), [])

    def test_contract_hash_is_representation_order_stable(self):
        """Set-like contract ordering does not change canonical identity."""
        reordered = copy.deepcopy(CONTRACT)
        reordered["asset_classes"] = list(reversed(reordered["asset_classes"]))
        reordered["invariants"] = list(reversed(reordered["invariants"]))
        reordered["training_prohibited_generator_markers"] = list(
            reversed(reordered["training_prohibited_generator_markers"])
        )
        reordered["purpose_allowed_declared_uses"] = dict(
            reversed(list(reordered["purpose_allowed_declared_uses"].items()))
        )
        for purpose in reordered["purpose_allowed_declared_uses"]:
            reordered["purpose_allowed_declared_uses"][purpose] = list(
                reversed(reordered["purpose_allowed_declared_uses"][purpose])
            )
        self.assertEqual(
            compute_lineage_contract_sha256(CONTRACT),
            compute_lineage_contract_sha256(reordered),
        )

    def test_invalid_contract_cannot_authorize(self):
        """A contract missing a required invariant cannot govern admission."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"] if item["invariant_id"] != "ADMISSION_IS_COMPUTED"
        ]
        result = evaluate_lineage_admission(base_record(), weakened)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["INVALID_CONTRACT"])

    def test_contract_requires_purpose_use_invariant(self):
        """Removing Purpose/use enforcement invalidates the contract."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"]
            if item["invariant_id"] != "PURPOSE_USE_COMPATIBILITY_ENFORCED"
        ]
        errors = validate_lineage_contract(weakened)
        self.assertTrue(any("PURPOSE_USE_COMPATIBILITY_ENFORCED" in error for error in errors))

    def test_contract_requires_parent_propagation_invariant(self):
        """Removing parent restriction propagation invalidates the contract."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"]
            if item["invariant_id"] != "PARENT_RESTRICTIONS_PROPAGATE"
        ]
        errors = validate_lineage_contract(weakened)
        self.assertTrue(any("PARENT_RESTRICTIONS_PROPAGATE" in error for error in errors))

    def test_contract_requires_reference_teacher_invariant(self):
        """Removing reference-teacher training prohibition invalidates V1."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["invariants"] = [
            item for item in weakened["invariants"]
            if item["invariant_id"] != "REFERENCE_TEACHER_OUTPUTS_NOT_TRAINING_LINEAGE"
        ]
        errors = validate_lineage_contract(weakened)
        self.assertTrue(
            any("REFERENCE_TEACHER_OUTPUTS_NOT_TRAINING_LINEAGE" in error for error in errors)
        )

    def test_contract_rejects_weakened_purpose_matrix(self):
        """Adding training permission to public evaluation invalidates V1."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["purpose_allowed_declared_uses"]["PUBLIC_EXTERNAL_EVAL"].append(
            "TRAINING_OR_ADAPTATION"
        )
        errors = validate_lineage_contract(weakened)
        self.assertTrue(any("purpose matrix 'PUBLIC_EXTERNAL_EVAL'" in error for error in errors))

    def test_contract_rejects_weakened_teacher_markers(self):
        """Removing MedGemma from the prohibited teacher markers invalidates V1."""
        weakened = copy.deepcopy(CONTRACT)
        weakened["training_prohibited_generator_markers"].remove("medgemma")
        errors = validate_lineage_contract(weakened)
        self.assertTrue(any("training_prohibited_generator_markers" in error for error in errors))

    def test_contract_rejects_duplicate_closed_vocabulary(self):
        """Duplicate closed-vocabulary values fail closed."""
        bad = copy.deepcopy(CONTRACT)
        bad["admission_states"].append("ELIGIBLE")
        self.assertTrue(any("duplicate" in e.lower() for e in validate_lineage_contract(bad)))

    def test_contract_rejects_unknown_admission_state(self):
        """Unknown admission states cannot extend the V1 contract."""
        bad = copy.deepcopy(CONTRACT)
        bad["admission_states"].append("MAYBE")
        self.assertTrue(any("unknown values" in e for e in validate_lineage_contract(bad)))

    def test_contract_rejects_unknown_id_and_schema(self):
        """Only the exact V1 contract/schema IDs are accepted."""
        bad = copy.deepcopy(CONTRACT)
        bad["contract_id"] = "other-contract"
        bad["schema_version"] = "2.0"
        errors = validate_lineage_contract(bad)
        self.assertTrue(any("unsupported contract_id" in e for e in errors))
        self.assertTrue(any("unsupported schema_version" in e for e in errors))


class TestRecordValidation(unittest.TestCase):
    """Evidence-record structural and exact-binding validation tests."""

    def test_valid_immutable_revision_locator_record(self):
        """A 40-hex revision plus exact locator is accepted."""
        self.assertEqual(validate_lineage_record(base_record(), CONTRACT), [])

    def test_valid_direct_digest_record(self):
        """A direct SHA-256 can independently bind exact payload bytes."""
        record = base_record(
            artifact_binding_state="DIRECT_DIGEST",
            content_sha256="b" * 64,
            source_revision="UNBOUND",
        )
        record.pop("artifact_locator")
        self.assertEqual(validate_lineage_record(record, CONTRACT), [])

    def test_mutable_revision_cannot_bind(self):
        """The mutable label latest cannot masquerade as immutable identity."""
        errors = validate_lineage_record(base_record(source_revision="latest"), CONTRACT)
        self.assertTrue(any("40- or 64-hex" in e for e in errors))

    def test_named_version_cannot_bind(self):
        """A named release like v1.0 alone cannot prove exact content."""
        errors = validate_lineage_record(base_record(source_revision="v1.0"), CONTRACT)
        self.assertTrue(any("40- or 64-hex" in e for e in errors))

    def test_direct_digest_rejects_malformed_sha(self):
        """Malformed content digests fail closed."""
        record = base_record(artifact_binding_state="DIRECT_DIGEST", content_sha256="abc")
        self.assertTrue(any("64 hex" in e for e in validate_lineage_record(record, CONTRACT)))

    def test_self_asserted_admission_is_rejected(self):
        """Callers cannot inject computed admission state."""
        errors = validate_lineage_record(base_record(admission_state="ELIGIBLE"), CONTRACT)
        self.assertTrue(any("computed output field 'admission_state'" in e for e in errors))

    def test_self_asserted_identity_is_rejected(self):
        """Callers cannot inject scientific record identity."""
        errors = validate_lineage_record(base_record(record_sha256="f" * 64), CONTRACT)
        self.assertTrue(any("computed output field 'record_sha256'" in e for e in errors))

    def test_payload_marker_is_rejected(self):
        """Payload-like fixture keys remain prohibited."""
        errors = validate_lineage_record(base_record(case_text="fixture text"), CONTRACT)
        self.assertTrue(any("Prohibited payload key" in e for e in errors))

    def test_optional_controlled_field_is_fail_closed(self):
        """Unknown optional contamination state is rejected when supplied."""
        errors = validate_lineage_record(base_record(contamination_state="MAGICALLY_CLEAN"), CONTRACT)
        self.assertTrue(any("invalid contamination_state" in e for e in errors))

    def test_spdx_metadata_rejects_control_chars(self):
        """Unsafe control content is not accepted as SPDX evidence metadata."""
        errors = validate_lineage_record(
            base_record(spdx_license_expression="MIT\nOR Apache-2.0"), CONTRACT
        )
        self.assertTrue(any("unsafe/control content" in e for e in errors))

    def test_duplicate_asset_id_registry_fails(self):
        """Registry stable IDs are globally unique."""
        valid, errors = validate_lineage_registry([base_record(), base_record()], CONTRACT)
        self.assertFalse(valid)
        self.assertTrue(any("duplicate asset_id" in e for e in errors))

    def test_malformed_parent_list_does_not_raise(self):
        """Malformed parent values return errors instead of exceptions."""
        record = synthetic_record(parent_asset_ids=[{"not": "a string"}])
        self.assertTrue(validate_lineage_record(record, CONTRACT))

    def test_private_gold_requires_private_gold_quarantine(self):
        """PRIVATE_GOLD purpose cannot claim ordinary quarantine state."""
        record = base_record(
            asset_class="PRIVATE_GOLD_METADATA",
            declared_use="PRIVATE_RELEASE_EVALUATION",
            purpose="PRIVATE_GOLD",
            quarantine_state="NOT_QUARANTINED",
        )
        self.assertTrue(
            any("requires quarantine_state='PRIVATE_GOLD'" in e for e in validate_lineage_record(record, CONTRACT))
        )

    def test_private_gold_quarantine_requires_private_gold_purpose(self):
        """PRIVATE_GOLD quarantine cannot be attached to another purpose."""
        record = base_record(purpose="TRAIN", quarantine_state="PRIVATE_GOLD")
        self.assertTrue(
            any("requires purpose='PRIVATE_GOLD'" in e for e in validate_lineage_record(record, CONTRACT))
        )


class TestAdmission(unittest.TestCase):
    """Exact-use admission and canonical Purpose authorization tests."""

    def test_eligible_training_record(self):
        """A fully resolved TRAIN-purpose training record is eligible."""
        result = evaluate_lineage_admission(base_record(), CONTRACT)
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])
        self.assertRegex(result["contract_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(result["record_sha256"], r"^[0-9a-f]{64}$")

    def test_unbound_exact_use_is_reference_only(self):
        """Verified source evidence does not bind an unbound artifact."""
        record = base_record(artifact_binding_state="UNBOUND", source_revision="UNBOUND")
        record.pop("artifact_locator")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "REFERENCE_ONLY")
        self.assertEqual(result["reason_codes"], ["ARTIFACT_UNBOUND"])

    def test_unresolved_rights_block(self):
        """Unresolved exact-use rights block eligibility."""
        result = evaluate_lineage_admission(
            base_record(rights_state="UNRESOLVED", rights_evidence_uri="UNRESOLVED"), CONTRACT
        )
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("RIGHTS_UNRESOLVED", result["reason_codes"])

    def test_incompatible_rights_prohibit(self):
        """Known incompatible rights prohibit the exact declared use."""
        result = evaluate_lineage_admission(base_record(rights_state="INCOMPATIBLE"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("RIGHTS_INCOMPATIBLE", result["reason_codes"])

    def test_unknown_privacy_blocks_training(self):
        """Unresolved privacy state blocks training admission."""
        result = evaluate_lineage_admission(base_record(phi_privacy_state="UNRESOLVED"), CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("PRIVACY_UNRESOLVED", result["reason_codes"])

    def test_phi_prohibits_training(self):
        """Restricted/PHI classification prohibits V1 training use."""
        result = evaluate_lineage_admission(base_record(phi_privacy_state="RESTRICTED_OR_PHI"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("RESTRICTED_OR_PHI", result["reason_codes"])

    def test_unresolved_contamination_blocks_training(self):
        """Pending contamination assessment blocks training use."""
        result = evaluate_lineage_admission(base_record(contamination_state="PENDING"), CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("CONTAMINATION_UNRESOLVED", result["reason_codes"])

    def test_high_risk_overlap_prohibits_training(self):
        """Known high-risk overlap prohibits clean training lineage."""
        result = evaluate_lineage_admission(
            base_record(contamination_state="OVERLAP_OR_HIGH_RISK"), CONTRACT
        )
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("CONTAMINATION_HIGH_RISK", result["reason_codes"])

    def test_reference_only_access_degrades_exact_use(self):
        """Reference-only access cannot become executable training admission."""
        result = evaluate_lineage_admission(base_record(access_class="REFERENCE_ONLY"), CONTRACT)
        self.assertEqual(result["state"], "REFERENCE_ONLY")
        self.assertIn("ACCESS_REFERENCE_ONLY", result["reason_codes"])

    def test_source_unresolved_blocks(self):
        """Source verification uncertainty blocks admission."""
        result = evaluate_lineage_admission(
            base_record(source_verification_status="UNRESOLVED"), CONTRACT
        )
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("SOURCE_UNVERIFIED", result["reason_codes"])

    def test_public_external_eval_cannot_train(self):
        """Canonical public evaluation purpose cannot enter training."""
        result = evaluate_lineage_admission(base_record(purpose="PUBLIC_EXTERNAL_EVAL"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PURPOSE_USE_INCOMPATIBLE", result["reason_codes"])

    def test_checkpoint_selection_cannot_train(self):
        """Checkpoint-selection purpose cannot enter training."""
        result = evaluate_lineage_admission(base_record(purpose="CHECKPOINT_SELECTION"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PURPOSE_USE_INCOMPATIBLE", result["reason_codes"])

    def test_dev_cannot_train(self):
        """Development purpose cannot enter training."""
        result = evaluate_lineage_admission(base_record(purpose="DEV"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PURPOSE_USE_INCOMPATIBLE", result["reason_codes"])

    def test_train_cannot_masquerade_as_development_evaluation(self):
        """TRAIN purpose cannot be relabeled as development evaluation."""
        record = base_record(declared_use="DEVELOPMENT_EVALUATION", purpose="TRAIN")
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PURPOSE_USE_INCOMPATIBLE", result["reason_codes"])

    def test_public_external_eval_allows_development_evaluation(self):
        """Canonical public benchmark development evaluation remains eligible."""
        record = base_record(
            declared_use="DEVELOPMENT_EVALUATION",
            purpose="PUBLIC_EXTERNAL_EVAL",
            contamination_state="NOT_APPLICABLE",
        )
        self.assertEqual(evaluate_lineage_admission(record, CONTRACT)["state"], "ELIGIBLE")

    def test_private_gold_allows_private_release_evaluation(self):
        """Private Gold remains usable only for its bounded release evaluation."""
        record = base_record(
            asset_class="PRIVATE_GOLD_METADATA",
            declared_use="PRIVATE_RELEASE_EVALUATION",
            purpose="PRIVATE_GOLD",
            quarantine_state="PRIVATE_GOLD",
            contamination_state="NOT_APPLICABLE",
        )
        self.assertEqual(evaluate_lineage_admission(record, CONTRACT)["state"], "ELIGIBLE")

    def test_generic_quarantine_blocks_non_reference_use(self):
        """An explicitly quarantined record cannot become eligible for execution."""
        result = evaluate_lineage_admission(base_record(quarantine_state="QUARANTINED"), CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("QUARANTINE_CONFLICT", result["reason_codes"])

    def test_public_external_eval_cannot_redistribute(self):
        """Purpose matrix is exact: evaluation purpose cannot imply redistribution."""
        record = base_record(
            declared_use="REDISTRIBUTION",
            purpose="PUBLIC_EXTERNAL_EVAL",
            contamination_state="NOT_APPLICABLE",
        )
        result = evaluate_lineage_admission(record, CONTRACT)
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("PURPOSE_USE_INCOMPATIBLE", result["reason_codes"])


class TestParentPropagation(unittest.TestCase):
    """Derived/synthetic parent resolution and restriction propagation tests."""

    def parent(self, **overrides):
        """Build a resolved parent record scoped to training/adaptation."""
        return base_record(asset_id="parent-001", **overrides)

    def test_generated_child_without_registry_blocks(self):
        """Parent IDs cannot be trusted without a resolver/registry."""
        result = evaluate_lineage_admission(synthetic_record(), CONTRACT)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["PARENT_REGISTRY_REQUIRED"])

    def test_unresolved_parent_reference_invalidates_registry(self):
        """Every referenced parent ID must resolve in the supplied registry."""
        child = synthetic_record(parent_asset_ids=["missing-parent"])
        valid, errors = validate_lineage_registry([child], CONTRACT)
        self.assertFalse(valid)
        self.assertTrue(any("is unresolved" in e for e in errors))

    def test_self_parent_invalidates_registry(self):
        """A record cannot name itself as a parent."""
        child = synthetic_record(parent_asset_ids=["synthetic-child-001"])
        valid, errors = validate_lineage_registry([child], CONTRACT)
        self.assertFalse(valid)
        self.assertTrue(any("cannot be its own parent" in e for e in errors))

    def test_parent_cycle_invalidates_registry(self):
        """Cycles cannot satisfy a provenance ancestry chain."""
        first = synthetic_record(asset_id="child-a", parent_asset_ids=["child-b"])
        second = synthetic_record(asset_id="child-b", parent_asset_ids=["child-a"])
        valid, errors = validate_lineage_registry([first, second], CONTRACT)
        self.assertFalse(valid)
        self.assertTrue(any("cycle detected" in e for e in errors))

    def test_parent_exact_use_evidence_mismatch_blocks(self):
        """Parent rights recorded for another use cannot authorize the child use."""
        parent = self.parent(
            declared_use="DEVELOPMENT_EVALUATION",
            purpose="PUBLIC_EXTERNAL_EVAL",
            contamination_state="NOT_APPLICABLE",
        )
        child = synthetic_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["PARENT_USE_EVIDENCE_MISMATCH"])

    def test_public_eval_parent_prohibits_training_child(self):
        """A public-evaluation parent scoped to training is still prohibited by purpose."""
        parent = self.parent(purpose="PUBLIC_EXTERNAL_EVAL")
        child = synthetic_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertEqual(result["reason_codes"], ["PARENT_PROHIBITED"])

    def test_unresolved_rights_parent_blocks_child(self):
        """A parent's unresolved rights propagate as a child block."""
        parent = self.parent(rights_state="UNRESOLVED", rights_evidence_uri="UNRESOLVED")
        child = synthetic_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["PARENT_BLOCKED"])

    def test_reference_only_parent_blocks_child(self):
        """Reference-only parent evidence cannot authorize a training child."""
        parent = self.parent(access_class="REFERENCE_ONLY")
        child = synthetic_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], ["PARENT_REFERENCE_ONLY"])

    def test_clean_training_parent_allows_child(self):
        """A fully eligible exact-use parent permits a clean derived child."""
        parent = self.parent()
        child = synthetic_record()
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])

    def test_medgemma_output_cannot_be_training_lineage(self):
        """MedGemma output stays reference/evaluation-only despite clean evidence."""
        parent = self.parent()
        child = synthetic_record(generator_identity="google/medgemma-4b-it@" + "d" * 40)
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])

    def test_haidef_output_cannot_be_training_lineage(self):
        """HAI-DEF-labelled output stays prohibited for commandMed training lineage."""
        parent = self.parent()
        child = synthetic_record(generator_identity="google/hai-def/reference@" + "d" * 40)
        result = evaluate_lineage_admission(child, CONTRACT, [parent, child])
        self.assertEqual(result["state"], "PROHIBITED")
        self.assertIn("GENERATOR_TRAINING_PROHIBITED", result["reason_codes"])


class TestIdentity(unittest.TestCase):
    """Scientific identity projection tests."""

    def test_parent_order_does_not_change_identity(self):
        """Parent IDs are a set-like lineage relation for identity."""
        first = synthetic_record(parent_asset_ids=["parent-b", "parent-a"])
        second = copy.deepcopy(first)
        second["parent_asset_ids"] = list(reversed(second["parent_asset_ids"]))
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_audit_metadata_does_not_change_identity(self):
        """Audit timestamp/local path remain outside scientific identity."""
        first = base_record()
        second = copy.deepcopy(first)
        second["retrieval_timestamp"] = "2026-08-22T23:00:00+03:00"
        second["local_path"] = "C:/tmp/asset"
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_source_revision_changes_identity(self):
        """An immutable source revision mutation changes scientific identity."""
        first = base_record()
        second = copy.deepcopy(first)
        second["source_revision"] = "b" * 40
        self.assertNotEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))

    def test_hex_case_is_representation_only(self):
        """Hexadecimal case does not create scientific identity drift."""
        first = base_record(source_revision="A" * 40)
        second = base_record(source_revision="a" * 40)
        self.assertEqual(compute_lineage_record_sha256(first), compute_lineage_record_sha256(second))


class TestSpec001Compatibility(unittest.TestCase):
    """Compatibility proof against canonical Spec 001 benchmark records."""

    @classmethod
    def setUpClass(cls):
        """Load canonical metadata only; no benchmark payload is accessed."""
        cls.benchmarks = json.loads((ROOT / "data/eval/benchmarks.json").read_text(encoding="utf-8"))

    def by_id(self, benchmark_id):
        """Return one canonical benchmark metadata record by stable ID."""
        return next(item for item in self.benchmarks if item["benchmark_id"] == benchmark_id)

    def test_healthbench_maps_to_immutable_binding(self):
        """Canonical HealthBench remains eligible for development evaluation."""
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

    def test_medabstain_family_does_not_broaden(self):
        """Canonical component-specific reference family remains non-executable."""
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