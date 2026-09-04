from __future__ import annotations

import unittest

from scripts.e004_aya_43_curriculum_construction_v1 import (
    AUTHORITY_ID,
    build_curriculum_record,
    build_scope_verification,
    curriculum_strata,
    expected_capabilities,
)
from src.commandmed.spec007.curriculum import validate_curriculum_record
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_SCOPE_ID,
    validate_research_component_content_scope_verification,
)


class Aya43CurriculumConstructionTests(unittest.TestCase):
    def _candidate(
        self,
        *,
        candidate_id: str = "a" * 64,
        language_code: str = "eng",
        task_family: str = "REWRITE_EDIT",
    ) -> dict[str, object]:
        return {
            "candidate_record_id": candidate_id,
            "content_sha256": "b" * 64,
            "language_code": language_code,
            "task_family": task_family,
            "verified_target_capability_ids": expected_capabilities(
                language_code,
                task_family,
            ),
        }

    def test_english_capabilities_are_exact(self) -> None:
        self.assertEqual(
            expected_capabilities("eng", "REWRITE_EDIT"),
            ["GENERAL_ENGLISH_LANGUAGE", "GENERAL_INSTRUCTION_FOLLOWING"],
        )

    def test_arabic_formatting_adds_research_formatting_capability(self) -> None:
        self.assertEqual(
            expected_capabilities("arb", "SUMMARIZATION"),
            [
                "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL",
                "GENERAL_INSTRUCTION_FOLLOWING",
                "NON_CLINICAL_RESEARCH_LEARNING_FORMATTING",
            ],
        )

    def test_unknown_capability_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "UNKNOWN_CAPABILITY"):
            curriculum_strata(["GENERAL_INSTRUCTION_FOLLOWING", "UNKNOWN"])

    def test_curriculum_record_is_contract_valid_and_hash_bound(self) -> None:
        record = build_curriculum_record(self._candidate(), "b" * 64)
        self.assertEqual(record["source_authority_id"], AUTHORITY_ID)
        self.assertEqual(record["role_class"], "LEARNER_RESEARCHER")
        self.assertEqual(record["knowledge_placement"], "DURABLE_WEIGHT_ELIGIBLE")
        self.assertEqual(record["split_id"], "VERIFIED_SFT_CURRICULUM_DATA")
        self.assertEqual(record["quarantine_disposition"], "PASS")
        self.assertEqual(record["language_profile"]["code_switch_state"], "NOT_CLASSIFIED")
        self.assertEqual(validate_curriculum_record(record), [])

    def test_scope_verification_is_contract_valid_and_linked(self) -> None:
        candidate = self._candidate(task_family="FORMATTING_ORGANIZATION")
        record = build_curriculum_record(candidate, "b" * 64)
        verification = build_scope_verification(candidate, record)
        self.assertEqual(verification["scope_id"], RESEARCH_COMPONENT_SCOPE_ID)
        self.assertEqual(verification["record_canonical_sha256"], record["record_canonical_sha256"])
        self.assertEqual(verification["record_content_sha256"], record["content_sha256"])
        self.assertEqual(verification["excluded_capability_hits"], [])
        self.assertEqual(
            validate_research_component_content_scope_verification(
                verification,
                record,
            ),
            [],
        )

    def test_candidate_capability_drift_fails_closed(self) -> None:
        candidate = self._candidate()
        candidate["verified_target_capability_ids"] = ["GENERAL_INSTRUCTION_FOLLOWING"]
        with self.assertRaisesRegex(ValueError, "CANDIDATE_CAPABILITY_MISMATCH"):
            build_curriculum_record(candidate, "b" * 64)


if __name__ == "__main__":
    unittest.main()
