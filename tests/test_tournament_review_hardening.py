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


if __name__ == "__main__":
    unittest.main()
