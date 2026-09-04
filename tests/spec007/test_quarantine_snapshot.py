"""I008-I010 RED tests for quarantine binding, snapshots, and coverage."""

from __future__ import annotations

import copy
import unittest

from src.commandmed.spec007.curriculum import compute_curriculum_record_sha256
from src.commandmed.spec007.quarantine import (
    canonical_quarantine_matrix_sha256,
    evaluate_quarantine_source,
    validate_quarantine_binding,
)
from src.commandmed.spec007.snapshot import (
    build_curriculum_coverage_report,
    build_dataset_snapshot,
    validate_dataset_snapshot,
)


def rendered_record(
    record_id: str,
    role: str = "PATIENT_CAREGIVER",
    *,
    source_authority_id: str = "VERIFIED_SFT_CURRICULUM_DATA",
    split_id: str = "VERIFIED_SFT_CURRICULUM_DATA",
) -> dict:
    record = {
        "schema_version": "1",
        "record_id": record_id,
        "record_canonical_sha256": "0" * 64,
        "content_sha256": "1" * 64,
        "source_authority_id": source_authority_id,
        "source_license_id": "synthetic-license",
        "source_verification_status": "VERIFIED",
        "split_id": split_id,
        "contamination_status": "ASSESSED_CLEAN",
        "review_state": "PASS",
        "role_class": role,
        "curriculum_strata": ["medical_fundamentals", "safety"],
        "language_profile": {
            "primary_language": "en",
            "authored_language": "en",
            "translation_state": "ORIGINAL",
            "dialect_or_register": "GENERAL",
            "code_switch_state": "NONE",
            "transliteration_state": "NONE",
            "terminology_normalization_id": None,
            "qualified_review_state": "PASS",
        },
        "conversation_structure_id": "single-turn-v1",
        "knowledge_placement": "DURABLE_WEIGHT_ELIGIBLE",
        "quarantine_disposition": "PASS",
        "rendering_policy_id": "render-v1",
        "rendered_input_sha256": "2" * 64,
        "rendered_token_count": 20,
        "supervised_token_count": 10,
        "loss_mask_policy_id": "mask-v1",
    }
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
    return record


class TestCanonicalQuarantineBinding(unittest.TestCase):
    def test_canonical_matrix_has_stable_sha256_identity(self):
        digest = canonical_quarantine_matrix_sha256()
        self.assertEqual(64, len(digest))
        self.assertEqual(digest, digest.lower())

    def test_verified_sft_curriculum_is_allowed_for_train(self):
        decision = evaluate_quarantine_source("VERIFIED_SFT_CURRICULUM_DATA", "TRAIN")
        self.assertTrue(decision["allowed"])
        self.assertTrue(decision["can_train"])

    def test_gold_and_holdout_sources_are_not_training_sources(self):
        for source_id in (
            "COMMANDMED_CLINICAL_GOLD",
            "COMMANDMED_ARABIC_GOLD",
            "COMMANDMED_MULTIMODAL_GOLD",
            "CALIBRATION_HOLD_OUT_SPLIT",
            "MODEL_SELECTION_DEV_SET",
            "PUBLIC_BENCHMARK_DEV_SPLITS",
            "HELD_OUT_SYNTHETIC_PILOT_CASES",
            "VERIFIED_DEV_SPLIT",
        ):
            with self.subTest(source_id=source_id):
                self.assertFalse(evaluate_quarantine_source(source_id, "TRAIN")["allowed"])

    def test_noncanonical_monitoring_recipe_and_model_selection_purposes_fail_closed(self):
        for purpose in ("MONITORING", "RECIPE_SELECTION", "MODEL_SELECTION"):
            decision = evaluate_quarantine_source("VERIFIED_DEV_SPLIT", purpose)
            self.assertFalse(decision["allowed"])
            self.assertEqual("UNKNOWN_PURPOSE", decision["reason_code"])

    def test_calibration_holdout_is_calibration_only(self):
        self.assertTrue(evaluate_quarantine_source("CALIBRATION_HOLD_OUT_SPLIT", "CALIBRATION")["allowed"])
        self.assertFalse(evaluate_quarantine_source("CALIBRATION_HOLD_OUT_SPLIT", "DEV")["allowed"])

    def test_binding_must_match_canonical_matrix_identity_and_decision(self):
        decision = evaluate_quarantine_source("VERIFIED_SFT_CURRICULUM_DATA", "TRAIN")
        binding = {
            "binding_id": "quarantine-binding-001",
            "quarantine_matrix_sha256": decision["quarantine_matrix_sha256"],
            "purpose": "TRAIN",
            "source_id": "VERIFIED_SFT_CURRICULUM_DATA",
            "allowed": True,
            "can_train": True,
            "can_select_model": False,
        }
        self.assertEqual([], validate_quarantine_binding(binding))
        bad = copy.deepcopy(binding)
        bad["quarantine_matrix_sha256"] = "f" * 64
        self.assertTrue(any("quarantine_matrix_sha256 mismatch" in e for e in validate_quarantine_binding(bad)))


class TestDatasetSnapshotAndCoverage(unittest.TestCase):
    def test_snapshot_generation_and_validation(self):
        records = [rendered_record("r1"), rendered_record("r2", "CLINICAL_PROFESSIONAL")]
        snapshot = build_dataset_snapshot(
            records,
            snapshot_id="snapshot-001",
            canonical_order_identity="record-id-ascending-v1",
            duplicate_report_id="dup-001",
            contamination_report_id="contam-001",
            quarantine_verification_id="quarantine-001",
        )
        self.assertEqual([], validate_dataset_snapshot(snapshot))
        self.assertEqual(2, snapshot["record_count"])
        self.assertEqual(40, snapshot["rendered_token_count"])
        self.assertEqual(20, snapshot["supervised_token_count"])

    def test_snapshot_treats_source_authority_as_provenance_not_quarantine_source(self):
        record = rendered_record(
            "r-founder-authority",
            source_authority_id="E004_FINAL_CURRICULUM_ADMISSION_DECISION_B",
            split_id="VERIFIED_SFT_CURRICULUM_DATA",
        )
        snapshot = build_dataset_snapshot(
            [record],
            snapshot_id="snapshot-founder-authority",
            canonical_order_identity="record-id-ascending-v1",
            duplicate_report_id="dup-founder-authority",
            contamination_report_id="contam-founder-authority",
            quarantine_verification_id="quarantine-founder-authority",
        )
        self.assertEqual([], validate_dataset_snapshot(snapshot))
        self.assertEqual(
            {"E004_FINAL_CURRICULUM_ADMISSION_DECISION_B": 1},
            snapshot["source_summary"],
        )

    def test_snapshot_still_rejects_prohibited_train_split(self):
        record = rendered_record(
            "r-prohibited-split",
            source_authority_id="E004_FINAL_CURRICULUM_ADMISSION_DECISION_B",
            split_id="MODEL_SELECTION_DEV_SET",
        )
        with self.assertRaisesRegex(ValueError, "split_id not authorized for TRAIN"):
            build_dataset_snapshot(
                [record],
                snapshot_id="snapshot-prohibited-split",
                canonical_order_identity="record-id-ascending-v1",
                duplicate_report_id="dup-prohibited-split",
                contamination_report_id="contam-prohibited-split",
                quarantine_verification_id="quarantine-prohibited-split",
            )

    def test_record_count_and_token_accounting_fail_closed(self):
        snapshot = build_dataset_snapshot(
            [rendered_record("r1")],
            snapshot_id="snapshot-002",
            canonical_order_identity="record-id-ascending-v1",
            duplicate_report_id="dup-002",
            contamination_report_id="contam-002",
            quarantine_verification_id="quarantine-002",
        )
        bad_count = copy.deepcopy(snapshot)
        bad_count["record_count"] = 2
        self.assertTrue(any("record_count" in e for e in validate_dataset_snapshot(bad_count)))
        bad_tokens = copy.deepcopy(snapshot)
        bad_tokens["supervised_token_count"] = bad_tokens["rendered_token_count"] + 1
        self.assertTrue(any("supervised_token_count" in e for e in validate_dataset_snapshot(bad_tokens)))

    def test_coverage_report_surfaces_uncovered_required_strata(self):
        report = build_curriculum_coverage_report(
            [rendered_record("r1")],
            required_strata=("medical_fundamentals", "safety", "tool_use"),
        )
        self.assertEqual(["tool_use"], report["uncovered_required_strata"])
        self.assertEqual(1, report["role_coverage"]["PATIENT_CAREGIVER"])
        self.assertEqual(1, report["knowledge_placement_distribution"]["DURABLE_WEIGHT_ELIGIBLE"])


if __name__ == "__main__":
    unittest.main()
