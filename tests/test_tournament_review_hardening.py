from __future__ import annotations

import copy
import unittest

from src.commandmed.tournament import (
    compute_tournament_report_sha256,
    evaluate_tournament,
    validate_tournament_manifest,
)
from tests.test_tournament import canonical_artifacts, candidate_result, manifest


class TournamentReviewHardeningTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = canonical_artifacts()
        self.manifest = manifest()

    def result(self, candidate_id: str, info: float, calibration: float) -> dict:
        return candidate_result(
            candidate_id,
            self.manifest,
            info_score=info,
            calibration_score=calibration,
        )

    def test_prohibited_key_normalization_rejects_internal_whitespace_and_separators(self):
        for hidden_key in ("api\tkey", "api\u200bkey", "provider.endpoint"):
            candidate_manifest = copy.deepcopy(self.manifest)
            candidate_manifest["safety_scope"][hidden_key] = "fixture-secret"
            errors = validate_tournament_manifest(candidate_manifest, self.artifacts)
            self.assertTrue(
                any("prohibited execution/payload key" in error for error in errors),
                msg=f"expected prohibited-key rejection for {hidden_key!r}: {errors}",
            )

    def test_report_hash_binds_lexicographic_comparison_vector_order(self):
        report = evaluate_tournament(
            self.manifest,
            [
                self.result("fixture-model-a", 2.0, 0.2),
                self.result("fixture-model-b", 1.0, 0.3),
            ],
            self.artifacts,
        )
        self.assertEqual(report["tournament_state"], "SELECTED")
        candidate = next(
            item for item in report["candidate_reports"] if item["candidate_id"] == "fixture-model-a"
        )
        self.assertGreaterEqual(len(candidate["comparison_vector"]), 2)

        mutated = copy.deepcopy(report)
        mutated_candidate = next(
            item
            for item in mutated["candidate_reports"]
            if item["candidate_id"] == "fixture-model-a"
        )
        mutated_candidate["comparison_vector"] = list(
            reversed(mutated_candidate["comparison_vector"])
        )

        self.assertNotEqual(
            compute_tournament_report_sha256(mutated),
            report["report_sha256"],
        )

    def test_non_list_candidate_results_fail_closed_for_every_declared_candidate(self):
        report = evaluate_tournament(self.manifest, {"candidate_id": "fixture-model-a"}, self.artifacts)

        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
        self.assertEqual(len(report["candidate_reports"]), len(self.manifest["candidate_ids"]))
        for candidate in report["candidate_reports"]:
            self.assertEqual(candidate["state"], "INCOMPLETE")
            self.assertIn("MISSING_CANDIDATE_RESULT", candidate["reason_codes"])

    def test_non_object_candidate_result_entry_invalidates_result_set(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        report = evaluate_tournament(self.manifest, [a, "not-an-envelope", b], self.artifacts)

        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
        self.assertTrue(
            any("non-object result envelope" in error for error in report["result_set_errors"])
        )

    def test_missing_or_unresolved_candidate_id_invalidates_result_set(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        for invalid_id in (None, "", "   ", "UNRESOLVED"):
            malformed = copy.deepcopy(a)
            if invalid_id is None:
                malformed.pop("candidate_id")
            else:
                malformed["candidate_id"] = invalid_id
            report = evaluate_tournament(self.manifest, [a, malformed, b], self.artifacts)
            self.assertEqual(report["tournament_state"], "NO_SELECTION")
            self.assertEqual(report["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
            self.assertTrue(
                any("unresolved candidate_id" in error for error in report["result_set_errors"]),
                msg=f"expected unresolved candidate_id error for {invalid_id!r}: {report}",
            )

    def test_mixed_type_manifest_keys_fail_closed_without_hash_exception(self):
        malformed = copy.deepcopy(self.manifest)
        malformed[7] = "unexpected"

        report = evaluate_tournament(malformed, [], self.artifacts)

        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "INVALID_MANIFEST_OR_PROTOCOL")
        self.assertIsNone(report["tournament_manifest_sha256"])
        self.assertTrue(
            any("object key" in error and "string" in error for error in report["result_set_errors"]),
            msg=f"expected mixed-key validation error: {report}",
        )

    def test_mixed_type_candidate_keys_fail_closed_as_incomplete(self):
        malformed = self.result("fixture-model-a", 2.0, 0.2)
        malformed[7] = "unexpected"
        valid = self.result("fixture-model-b", 1.0, 0.3)

        report = evaluate_tournament(self.manifest, [malformed, valid], self.artifacts)

        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        candidate = by_id["fixture-model-a"]
        self.assertEqual(candidate["state"], "INCOMPLETE")
        self.assertIn("MALFORMED_CANDIDATE_RESULT", candidate["reason_codes"])
        self.assertTrue(
            any("object key" in error and "string" in error for error in candidate["validation_errors"]),
            msg=f"expected mixed-key candidate validation error: {candidate}",
        )


if __name__ == "__main__":
    unittest.main()
