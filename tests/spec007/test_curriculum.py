"""I005-I007 RED tests for curriculum, provenance, and duplicate contracts."""

from __future__ import annotations

import copy
import unittest

from src.commandmed.spec007.curriculum import (
    compute_curriculum_record_sha256,
    validate_curriculum_record,
    validate_duplicate_contamination_report,
    validate_knowledge_placement,
)


def valid_curriculum_record() -> dict:
    record = {
        "schema_version": "1",
        "record_id": "synthetic-record-001",
        "record_canonical_sha256": "0" * 64,
        "content_sha256": "1" * 64,
        "source_authority_id": "synthetic-authority",
        "source_license_id": "synthetic-license",
        "source_verification_status": "VERIFIED",
        "split_id": "VERIFIED_SFT_CURRICULUM_DATA",
        "contamination_status": "ASSESSED_CLEAN",
        "review_state": "PASS",
        "role_class": "PATIENT_CAREGIVER",
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
    }
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
    return record


class TestCurriculumRecord(unittest.TestCase):
    def test_valid_synthetic_record_passes(self):
        self.assertEqual([], validate_curriculum_record(valid_curriculum_record()))

    def test_record_identity_mismatch_fails(self):
        record = valid_curriculum_record()
        record["record_canonical_sha256"] = "f" * 64
        self.assertTrue(any("record_canonical_sha256 mismatch" in e for e in validate_curriculum_record(record)))

    def test_provenance_must_be_verified_and_clean(self):
        for field, value in (("source_verification_status", "UNRESOLVED"), ("contamination_status", "NOT_ASSESSED"), ("review_state", "PENDING")):
            record = valid_curriculum_record()
            record[field] = value
            record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
            self.assertTrue(validate_curriculum_record(record), field)

    def test_rendering_bundle_is_all_or_none(self):
        record = valid_curriculum_record()
        record["rendering_policy_id"] = "render-v1"
        record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
        errors = validate_curriculum_record(record)
        self.assertTrue(any("rendering fields must be all present or all absent" in e for e in errors))

    def test_supervised_tokens_cannot_exceed_rendered_tokens(self):
        record = valid_curriculum_record()
        record.update({
            "rendering_policy_id": "render-v1",
            "rendered_input_sha256": "2" * 64,
            "rendered_token_count": 10,
            "supervised_token_count": 11,
            "loss_mask_policy_id": "mask-v1",
        })
        record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
        self.assertTrue(any("supervised_token_count" in e for e in validate_curriculum_record(record)))

    def test_language_profile_requires_explicit_nullable_normalization_id(self):
        record = valid_curriculum_record()
        del record["language_profile"]["terminology_normalization_id"]
        record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
        self.assertTrue(any("terminology_normalization_id" in e for e in validate_curriculum_record(record)))

    def test_duplicate_strata_and_invalid_knowledge_placement_fail(self):
        record = valid_curriculum_record()
        record["curriculum_strata"] = ["safety", "safety"]
        record["knowledge_placement"] = "MEMORIZE_CURRENT_GUIDELINES"
        record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
        errors = validate_curriculum_record(record)
        self.assertTrue(any("curriculum_strata" in e for e in errors))
        self.assertTrue(any("knowledge_placement" in e for e in errors))

    def test_knowledge_placement_vocabulary_is_closed(self):
        self.assertEqual([], validate_knowledge_placement("DETERMINISTIC_TOOL_REQUIRED"))
        self.assertTrue(validate_knowledge_placement("TOOL_OPTIONAL"))


class TestDuplicateContaminationReport(unittest.TestCase):
    def test_empty_synthetic_report_can_pass(self):
        report = {
            "report_id": "dup-report-001",
            "input_snapshot_candidate_id": "candidate-001",
            "exact_duplicate_groups": [],
            "near_duplicate_groups": [],
            "benchmark_overlap_findings": [],
            "quarantine_overlap_findings": [],
            "source_concentration_findings": [],
            "post_render_overlap_findings": None,
            "disposition": "PASS",
        }
        self.assertEqual([], validate_duplicate_contamination_report(report))

    def test_pass_disposition_rejected_when_prohibited_overlap_exists(self):
        report = {
            "report_id": "dup-report-002",
            "input_snapshot_candidate_id": "candidate-002",
            "exact_duplicate_groups": [["a", "b"]],
            "near_duplicate_groups": [],
            "benchmark_overlap_findings": [],
            "quarantine_overlap_findings": [],
            "source_concentration_findings": [],
            "post_render_overlap_findings": None,
            "disposition": "PASS",
        }
        self.assertTrue(any("disposition PASS" in e for e in validate_duplicate_contamination_report(report)))


if __name__ == "__main__":
    unittest.main()
