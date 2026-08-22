from __future__ import annotations

import copy
import unittest

from src.commandmed.tournament import (
    CANONICAL_UPSTREAM_IDENTITIES_V1,
    compute_tournament_report_sha256,
    evaluate_tournament,
)
from tests.test_tournament import canonical_artifacts, candidate_result, manifest


class TournamentReportContractHardeningTests(unittest.TestCase):
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

    def test_report_carries_exact_canonical_artifact_identities(self):
        report = evaluate_tournament(
            self.manifest,
            [
                self.result("fixture-model-a", 2.0, 0.2),
                self.result("fixture-model-b", 1.0, 0.3),
            ],
            self.artifacts,
        )
        self.assertEqual(
            report["canonical_artifact_identities"],
            CANONICAL_UPSTREAM_IDENTITIES_V1,
        )

    def test_canonical_identity_mutation_changes_report_identity(self):
        report = evaluate_tournament(
            self.manifest,
            [
                self.result("fixture-model-a", 2.0, 0.2),
                self.result("fixture-model-b", 1.0, 0.3),
            ],
            self.artifacts,
        )
        mutated = copy.deepcopy(report)
        mutated["canonical_artifact_identities"]["metrics_sha256"] = "0" * 64
        self.assertNotEqual(
            compute_tournament_report_sha256(mutated),
            report["report_sha256"],
        )

    def test_unknown_candidate_input_order_does_not_change_invalid_report_identity(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        extra_one = copy.deepcopy(a)
        extra_one["candidate_id"] = "fixture-extra-one"
        extra_two = copy.deepcopy(a)
        extra_two["candidate_id"] = "fixture-extra-two"

        first = evaluate_tournament(
            self.manifest,
            [extra_one, a, extra_two, b],
            self.artifacts,
        )
        second = evaluate_tournament(
            self.manifest,
            [b, extra_two, a, extra_one],
            self.artifacts,
        )

        self.assertEqual(first, second)
        self.assertEqual(first["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
        self.assertEqual(first["report_sha256"], second["report_sha256"])

    def test_malformed_result_input_order_does_not_change_invalid_report_identity(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)

        first = evaluate_tournament(
            self.manifest,
            ["malformed-one", a, None, b],
            self.artifacts,
        )
        second = evaluate_tournament(
            self.manifest,
            [b, None, a, "malformed-one"],
            self.artifacts,
        )

        self.assertEqual(first, second)
        self.assertEqual(first["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
        self.assertEqual(first["report_sha256"], second["report_sha256"])


if __name__ == "__main__":
    unittest.main()
