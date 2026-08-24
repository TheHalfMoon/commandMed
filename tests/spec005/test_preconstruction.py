"""US3 fixture tests: preconstruction evidence and source governance.

Synthetic, non-medical fixtures only; no case payload, Gold payload, or PHI.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec005.preconstruction import (
    evaluate_preconstruction_snapshot,
    validate_contamination_plan,
    validate_pair_metadata,
    validate_preconstruction_contract,
    validate_review_binding,
    validate_root_task_metadata,
    validate_source_route,
)

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "data/spec005/preconstruction_contract.json"


def load_contract():
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def make_source_route(**overrides):
    record = {
        "source_route_record_id": "SR-001",
        "route_class": "ORIGINAL_HUMAN_AUTHORED_NON_PHI",
        "origin_type": "HUMAN_AUTHORED",
        "lineage_record_id": "LIN-001",
        "lineage_record_sha256": "a" * 64,
        "parent_asset_ids": [],
        "rights_evidence_id": "RIGHTS-1",
        "privacy_evidence_id": "PRIV-1",
        "declared_use": "DEVELOPMENT_EVALUATION",
        "purpose": "CHECKPOINT_SELECTION",
        "record_canonical_sha256": "b" * 64,
    }
    record.update(overrides)
    return record


def make_root_task(**overrides):
    record = {
        "root_task_id": "RT-001",
        "root_task_record_version": "1.0",
        "root_task_state": "DRAFT_UNFROZEN",
        "root_content_artifact_sha256": "c" * 64,
        "source_route_record_id": "SR-001",
        "source_route_record_sha256": "d" * 64,
        "lineage_record_id": "LIN-001",
        "lineage_record_sha256": "e" * 64,
        "primary_coverage_anchor_id": "MODERN_STANDARD_ARABIC_CLINICAL",
        "secondary_coverage_tags": [],
        "role_id": "PATIENT_CAREGIVER",
        "use_context_id": "UC-001",
        "statistical_stratum_id": "STRAT-1",
        "statistical_slot_id": "SLOT-1",
        "rights_instrument_evidence_id": "RIGHTS-1",
        "privacy_attestation_evidence_id": "PRIV-1",
        "gold_nonexposure_attestation_reference": "GOLD-ATTEST-1",
        "content_authoring_record_id": "AUTH-001",
        "record_canonical_sha256": "f" * 64,
    }
    record.update(overrides)
    return record


def make_pair(**overrides):
    pair = {
        "pair_id": "PAIR-001",
        "pair_record_version": "1.0",
        "pair_state": "DRAFT_UNFROZEN",
        "root_task_id": "RT-001",
        "arabic_variant_id": "VAR-AR-1",
        "english_variant_id": "VAR-EN-1",
        "primary_coverage_anchor_id": "MODERN_STANDARD_ARABIC_CLINICAL",
        "role_id": "PATIENT_CAREGIVER",
        "use_context_id": "UC-001",
        "statistical_stratum_id": "STRAT-1",
        "statistical_slot_id": "SLOT-1",
        "pair_review_binding_id": "REVB-001",
        "pair_content_identity_sha256": "0" * 64,
        "record_canonical_sha256": "1" * 64,
    }
    pair.update(overrides)
    return pair


def make_review_binding(**overrides):
    binding = {
        "review_binding_id": "REVB-001",
        "review_binding_version": "1.0",
        "pair_id": "PAIR-001",
        "review_protocol_id": "PROTO-A8",
        "review_protocol_version": "2.0",
        "review_protocol_canonical_sha256": "2" * 64,
        "reviewer_references": ["P-REV-1"],
        "author_references": ["P-AUTH-1"],
        "adjudicator_reference_or_none": None,
        "final_review_disposition": "ACCEPTED",
        "reviewed_pair_content_identity_sha256": "0" * 64,
        "record_canonical_sha256": "3" * 64,
    }
    binding.update(overrides)
    return binding


def make_contamination_plan(**overrides):
    plan = {
        "contamination_plan_id": "CONTAM-001",
        "selection_content_universe_policy": "SELECTION_SUITE_ONLY",
        "exact_method_id": "EXACT-METHOD-1",
        "exact_method_version": "1.0",
        "semantic_method_id": "SEM-METHOD-1",
        "semantic_method_version": "1.0",
        "semantic_threshold_policy_id": "THRESH-POL-1",
        "candidate_corpus_binding_policy": "EXACT_CANDIDATE_CORPUS_IDENTITY",
        "parent_aware": True,
        "cross_lingual_semantic_assessment_required": True,
        "record_canonical_sha256": "4" * 64,
    }
    plan.update(overrides)
    return plan


class ContractTests(unittest.TestCase):
    def test_canonical_contract_validates(self):
        self.assertEqual(validate_preconstruction_contract(load_contract()), [])

    def test_missing_dependency_dag_fails(self):
        contract = load_contract()
        del contract["preconstruction_dependency_dag"]
        errors = validate_preconstruction_contract(contract)
        self.assertTrue(any("DEPENDENCY_DAG" in e for e in errors))

    def test_prohibited_activation_state_rejected(self):
        contract = load_contract()
        contract["snapshot_readiness_states"].append("AUTHORIZED_TO_CONSTRUCT")
        errors = validate_preconstruction_contract(contract)
        self.assertTrue(any("AUTHORIZED_TO_CONSTRUCT" in e for e in errors))

    def test_malformed_contract_does_not_raise(self):
        for bad in (None, [], 5):
            errors = validate_preconstruction_contract(bad)
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)

    def test_malformed_contract_fails_closed_in_record_validators(self):
        for bad in (None, "x", 42):
            for validator in (
                validate_source_route,
                validate_root_task_metadata,
                validate_pair_metadata,
                validate_review_binding,
                validate_contamination_plan,
            ):
                record = {
                    validate_source_route: make_source_route(),
                    validate_root_task_metadata: make_root_task(),
                    validate_pair_metadata: make_pair(),
                    validate_review_binding: make_review_binding(),
                    validate_contamination_plan: make_contamination_plan(),
                }[validator]
                errors = validator(record, bad)
                self.assertIsInstance(errors, list)
                self.assertTrue(errors)


class SourceRouteTests(unittest.TestCase):
    def test_valid_original_route_validates(self):
        self.assertEqual(validate_source_route(make_source_route(), load_contract()), [])

    def test_provider_generated_blocked_for_selection(self):
        errors = validate_source_route(
            make_source_route(route_class="MODEL_OR_PROVIDER_GENERATED"),
            load_contract(),
        )
        self.assertTrue(any("PROHIBITED" in e.upper() for e in errors))

    def test_wrong_declared_use_rejected(self):
        errors = validate_source_route(
            make_source_route(declared_use="TRAINING"), load_contract()
        )
        self.assertTrue(errors)

    def test_derived_route_requires_parents(self):
        errors = validate_source_route(
            make_source_route(
                route_class="PUBLIC_DEV_DERIVED", parent_asset_ids=[]
            ),
            load_contract(),
        )
        self.assertTrue(any("PARENT" in e.upper() for e in errors))

    def test_missing_rights_or_privacy_blocks(self):
        for field in ("rights_evidence_id", "privacy_evidence_id"):
            record = make_source_route()
            del record[field]
            errors = validate_source_route(record, load_contract())
            self.assertTrue(any(field in e for e in errors))

    def test_missing_parent_asset_ids_does_not_raise(self):
        record = make_source_route()
        del record["parent_asset_ids"]
        errors = validate_source_route(record, load_contract())
        self.assertIsInstance(errors, list)
        self.assertTrue(any("parent_asset_ids" in e for e in errors))

    def test_gold_hidden_in_nested_parent_structure_detected(self):
        errors = validate_source_route(
            make_source_route(parent_asset_ids={"nested": ["COMMANDMED_ARABIC_GOLD"]}),
            load_contract(),
        )
        self.assertTrue(any("PRIVATE_GOLD" in e.upper() for e in errors))
        errors = validate_source_route(
            make_source_route(parent_asset_ids="COMMANDMED_ARABIC_GOLD"),
            load_contract(),
        )
        self.assertTrue(any("PRIVATE_GOLD" in e.upper() or "LIST" in e.upper() for e in errors))

    def test_gold_as_parent_never_allowed(self):
        errors = validate_source_route(
            make_source_route(parent_asset_ids=["COMMANDMED_ARABIC_GOLD"]),
            load_contract(),
        )
        self.assertTrue(any("PRIVATE_GOLD" in e.upper() for e in errors))

    def test_malformed_input_does_not_raise(self):
        for bad in (None, [], 9):
            errors = validate_source_route(bad, load_contract())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class RootTaskMetadataTests(unittest.TestCase):
    def test_valid_root_task_validates(self):
        self.assertEqual(
            validate_root_task_metadata(make_root_task(), load_contract()), []
        )

    def test_unknown_coverage_anchor_fails_closed(self):
        errors = validate_root_task_metadata(
            make_root_task(primary_coverage_anchor_id="NOT_AN_ANCHOR"),
            load_contract(),
        )
        self.assertTrue(any("NOT_AN_ANCHOR" in e for e in errors))

    def test_two_primary_anchors_rejected(self):
        errors = validate_root_task_metadata(
            make_root_task(
                primary_coverage_anchor_id="MODERN_STANDARD_ARABIC_CLINICAL",
                secondary_coverage_tags=["SAUDI_GULF_COLLOQUIAL_PATIENT"],
            ),
            load_contract(),
        )
        # Secondary tags are allowed as tags; a second *primary* is structural.
        self.assertEqual(errors, [])
        errors = validate_root_task_metadata(
            make_root_task(
                primary_coverage_anchor_id=[
                    "MODERN_STANDARD_ARABIC_CLINICAL",
                    "LOCAL_MEDICATION_NOMENCLATURE",
                ]
            ),
            load_contract(),
        )
        self.assertTrue(any("PRIMARY" in e.upper() for e in errors))

    def test_payload_text_field_rejected(self):
        record = make_root_task(embedded_case_text="patient has chest pain")
        errors = validate_root_task_metadata(record, load_contract())
        self.assertTrue(any("PAYLOAD" in e.upper() for e in errors))

    def test_malformed_input_does_not_raise(self):
        for bad in (None, "x", []):
            errors = validate_root_task_metadata(bad, load_contract())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class PairMetadataTests(unittest.TestCase):
    def test_valid_pair_validates(self):
        self.assertEqual(validate_pair_metadata(make_pair(), load_contract()), [])

    def test_both_languages_required_distinct(self):
        errors = validate_pair_metadata(
            make_pair(arabic_variant_id="V1", english_variant_id="V1"),
            load_contract(),
        )
        self.assertTrue(any("DISTINCT" in e.upper() for e in errors))

    def test_unit_count_is_one(self):
        errors = validate_pair_metadata(
            make_pair(statistical_unit_count=2), load_contract()
        )
        self.assertTrue(any("UNIT_COUNT" in e.upper() for e in errors))

    def test_malformed_input_does_not_raise(self):
        for bad in (None, 3, []):
            errors = validate_pair_metadata(bad, load_contract())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class ReviewBindingTests(unittest.TestCase):
    def test_valid_binding_validates(self):
        self.assertEqual(
            validate_review_binding(make_review_binding(), load_contract()), []
        )

    def test_unhashable_reference_elements_do_not_crash(self):
        errors = validate_review_binding(
            make_review_binding(
                author_references=[{"nested": 1}],
                reviewer_references=[["x"]],
            ),
            load_contract(),
        )
        self.assertIsInstance(errors, list)
        self.assertTrue(any("STRING" in e.upper() for e in errors))

    def test_scalar_reason_codes_fail_closed(self):
        snapshot = {
            "snapshot_id": "SNAP-007",
            "snapshot_version": "1.0",
            "requirements": {},
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), {"state": "INCOMPLETE", "reason_codes": 42}
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")

    def test_missing_author_or_reviewer_rejected(self):
        errors = validate_review_binding(
            make_review_binding(reviewer_references=[]), load_contract()
        )
        self.assertTrue(any("reviewer" in e.lower() for e in errors))
        errors = validate_review_binding(
            make_review_binding(author_references=[]), load_contract()
        )
        self.assertTrue(any("author" in e.lower() for e in errors))

    def test_author_cannot_review_own_pair(self):
        binding = make_review_binding(
            reviewer_references=["P-AUTH-1"], author_references=["P-AUTH-1"]
        )
        errors = validate_review_binding(binding, load_contract())
        self.assertTrue(any("SELF_REVIEW" in e.upper() for e in errors))

    def test_stale_content_identity_rejected(self):
        binding = make_review_binding(reviewed_pair_content_identity_sha256="9" * 64)
        binding["current_pair_content_identity_sha256"] = "8" * 64
        errors = validate_review_binding(binding, load_contract())
        self.assertTrue(any("CONTENT_IDENTITY" in e.upper() for e in errors))

    def test_unknown_disposition_fails_closed(self):
        errors = validate_review_binding(
            make_review_binding(final_review_disposition="MAYBE_FINE"),
            load_contract(),
        )
        self.assertTrue(any("MAYBE_FINE" in e for e in errors))


class ContaminationPlanTests(unittest.TestCase):
    def test_valid_plan_validates(self):
        self.assertEqual(
            validate_contamination_plan(make_contamination_plan(), load_contract()),
            [],
        )

    def test_parent_aware_false_rejected(self):
        errors = validate_contamination_plan(
            make_contamination_plan(parent_aware=False), load_contract()
        )
        self.assertTrue(any("parent_aware" in e for e in errors))

    def test_cross_lingual_false_rejected(self):
        errors = validate_contamination_plan(
            make_contamination_plan(
                cross_lingual_semantic_assessment_required=False
            ),
            load_contract(),
        )
        self.assertTrue(
            any("cross_lingual" in e.lower() for e in errors)
        )

    def test_mutable_latest_policy_reference_rejected(self):
        errors = validate_contamination_plan(
            make_contamination_plan(semantic_threshold_policy_id="latest"),
            load_contract(),
        )
        self.assertTrue(any("LATEST" in e.upper() for e in errors))


class SnapshotTests(unittest.TestCase):
    def _scientific_ready(self):
        return {"state": "READY_FOR_PRECONSTRUCTION", "reason_codes": []}

    def test_complete_gate_set_yields_not_ready_to_construct(self):
        snapshot = {
            "snapshot_id": "SNAP-001",
            "snapshot_version": "1.0",
            "requirements": {
                gate: {
                    "state": "PASS",
                    "record_id": f"REC-{gate}",
                    "record_canonical_sha256": "a" * 64,
                    "stale": False,
                }
                for gate in (
                    "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                    "S1", "P1", "C1", "H1", "I1", "F1",
                )
            },
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED")

    def test_missing_gate_blocks(self):
        snapshot = {
            "snapshot_id": "SNAP-002",
            "snapshot_version": "1.0",
            "requirements": {},
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")

    def test_scientific_readiness_cannot_be_bypassed(self):
        snapshot = {
            "snapshot_id": "SNAP-003",
            "snapshot_version": "1.0",
            "requirements": {
                gate: {
                    "state": "PASS",
                    "record_id": f"REC-{gate}",
                    "record_canonical_sha256": "a" * 64,
                    "stale": False,
                }
                for gate in ("T1", "D34")
            },
        }
        result = evaluate_preconstruction_snapshot(
            snapshot,
            load_contract(),
            {"state": "INCOMPLETE", "reason_codes": ["X"]},
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")
        self.assertTrue(any("SCIENTIFIC" in r.upper() for r in result["reason_codes"]))

    def test_caller_ready_claim_not_trusted(self):
        snapshot = {
            "snapshot_id": "SNAP-004",
            "snapshot_version": "1.0",
            "computed_readiness": "READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED",
            "ready": True,
            "requirements": {},
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")

    def test_pass_gate_without_bound_record_blocked(self):
        snapshot = {
            "snapshot_id": "SNAP-006",
            "snapshot_version": "1.0",
            "requirements": {
                gate: (
                    {"state": "PASS", "record_id": "", "record_canonical_sha256": ""}
                    if gate == "G2"
                    else {
                        "state": "PASS",
                        "record_id": f"REC-{gate}",
                        "record_canonical_sha256": "a" * 64,
                        "stale": False,
                    }
                )
                for gate in (
                    "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                    "S1", "P1", "C1", "H1", "I1", "F1",
                )
            },
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")
        self.assertTrue(any("G2" in c and ("RECORD_ID" in c or "SHA" in c) for c in result["reason_codes"]))

    def test_stale_gate_blocks(self):
        snapshot = {
            "snapshot_id": "SNAP-005",
            "snapshot_version": "1.0",
            "requirements": {
                gate: {
                    "state": "PASS",
                    "record_id": f"REC-{gate}",
                    "record_canonical_sha256": "a" * 64,
                    "stale": gate == "G1",
                }
                for gate in (
                    "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                    "S1", "P1", "C1", "H1", "I1", "F1",
                )
            },
        }
        result = evaluate_preconstruction_snapshot(
            snapshot, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")

    def test_malformed_snapshot_fail_closed(self):
        result = evaluate_preconstruction_snapshot(
            None, load_contract(), self._scientific_ready()
        )
        self.assertEqual(result["state"], "NOT_READY_TO_CONSTRUCT")
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


if __name__ == "__main__":
    unittest.main()
