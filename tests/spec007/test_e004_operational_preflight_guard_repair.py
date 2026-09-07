from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/e004-operational-preflight-evidence-v1.yml"
FAILURE = ROOT / "specs/007-sft-v1/e004-operational-preflight-evidence-run-v1-failure-reconciliation-2026-09-08.md"
FRONTIER = ROOT / "specs/007-sft-v1/e004-registry-current-state-reconciliation-v50-2026-09-08.md"


class TestE004OperationalPreflightGuardRepair(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.failure = FAILURE.read_text(encoding="utf-8")
        cls.frontier = FRONTIER.read_text(encoding="utf-8")

    def test_every_checkout_uses_full_history_after_ancestry_guard_failure(self) -> None:
        self.assertNotIn("fetch-depth: 2", self.workflow)
        self.assertEqual(self.workflow.count("fetch-depth: 0"), 2)
        self.assertIn("git rev-list --parents -n 1 \"$parent\"", self.workflow)
        self.assertIn("git rev-list --count \"$parent\"..HEAD", self.workflow)

    def test_repair_does_not_claim_new_empirical_authority(self) -> None:
        self.assertIn("The V1 empirical allowance has been consumed", self.workflow)
        for token in (
            "AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS_REMAINING=0",
            "OPERATIONAL_PREFLIGHT_EVIDENCE_RERUN_AUTHORIZED_NOW=NO",
            "SECOND_MARKER_RUN_AUTHORITY=NONE",
            "NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE",
        ):
            self.assertIn(token, self.failure + "\n" + self.frontier)

    def test_failed_run_remains_fail_closed(self) -> None:
        for token in (
            "OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_PRE_PROVISIONING_GUARD",
            "RUNTIME_DEPENDENCY_PROVISIONING_PERFORMED=NO",
            "MODEL_LOAD_PERFORMED=NO",
            "EVALUATION_PAYLOAD_EXECUTION_PERFORMED=NO",
            "TOURNAMENT_EXECUTION_PERFORMED=NO",
            "TRAINING_PERFORMED=NO",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
        ):
            self.assertIn(token, self.failure)

    def test_frontier_stays_blocked_pending_separate_new_attempt_authority(self) -> None:
        for token in (
            "NEW_EMPIRICAL_RUN_AUTHORITY=NONE",
            "CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE",
            "SUCCESSOR_PASS_PREFLIGHT=NO",
            "A15_ACTIVATION=ABSENT_NOT_AUTHORIZED",
            "TRAINING_AUTHORITY=NONE",
            "PROJECT_FINISHED=NO",
        ):
            self.assertIn(token, self.frontier)


if __name__ == "__main__":
    unittest.main()
