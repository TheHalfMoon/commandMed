from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from src.commandmed.reliability_v5.case_generator import cases_from_state_indices
from src.commandmed.reliability_v5.contracts import ReliabilityContractError
from src.commandmed.reliability_v5.quarantine import (
    CALIBRATION_COUNT,
    CONFIRMATORY_COUNT,
    DEVELOPMENT_COUNT,
    RESERVE_COUNT,
    assignment_commitment,
    confirmatory_reserve_state_partition,
    derive_partition_seed,
    prefreeze_state_partition,
)


class QuarantineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator_id = "pmid:toy"
        self.total = 2048
        self.commit = "a" * 40
        self.beacon = "ab" * 64
        self.seed = derive_partition_seed(
            freeze_commit=self.commit,
            beacon_output_hex=self.beacon,
        )

    def test_prefreeze_partition_is_disjoint_and_small(self):
        partition = prefreeze_state_partition(self.calculator_id, self.total)
        self.assertEqual(len(partition["development"]), DEVELOPMENT_COUNT)
        self.assertEqual(len(partition["calibration"]), CALIBRATION_COUNT)
        self.assertTrue(set(partition["development"]).isdisjoint(partition["calibration"]))
        self.assertLess(
            len(partition["development"]) + len(partition["calibration"]),
            self.total,
        )

    def test_prefreeze_partition_is_deterministic(self):
        first = prefreeze_state_partition(self.calculator_id, self.total)
        second = prefreeze_state_partition(self.calculator_id, self.total)
        self.assertEqual(first, second)

    def test_future_partition_is_disjoint_from_prefreeze(self):
        fixed = prefreeze_state_partition(self.calculator_id, self.total)
        excluded = fixed["development"] + fixed["calibration"]
        future = confirmatory_reserve_state_partition(
            self.calculator_id, self.total, excluded, self.seed
        )
        self.assertEqual(len(future["confirmatory"]), CONFIRMATORY_COUNT)
        self.assertEqual(len(future["reserve"]), RESERVE_COUNT)
        selected = set(future["confirmatory"] + future["reserve"])
        self.assertEqual(len(selected), CONFIRMATORY_COUNT + RESERVE_COUNT)
        self.assertTrue(selected.isdisjoint(excluded))

    def test_future_randomness_changes_confirmatory_assignment(self):
        fixed = prefreeze_state_partition(self.calculator_id, self.total)
        excluded = fixed["development"] + fixed["calibration"]
        alternate = derive_partition_seed(
            freeze_commit=self.commit,
            beacon_output_hex="cd" * 64,
        )
        first = confirmatory_reserve_state_partition(
            self.calculator_id, self.total, excluded, self.seed
        )
        second = confirmatory_reserve_state_partition(
            self.calculator_id, self.total, excluded, alternate
        )
        self.assertNotEqual(first["confirmatory"], second["confirmatory"])

    def test_commitment_is_stable(self):
        partition = prefreeze_state_partition(self.calculator_id, self.total)
        self.assertEqual(assignment_commitment(partition), assignment_commitment(partition))

    def test_small_candidate_space_fails_closed(self):
        with self.assertRaises(ReliabilityContractError):
            prefreeze_state_partition(self.calculator_id, 512)

    def test_bad_beacon_length_fails_closed(self):
        with self.assertRaises(ReliabilityContractError):
            derive_partition_seed(freeze_commit=self.commit, beacon_output_hex="ab")

    def test_bad_commit_fails_closed(self):
        with self.assertRaises(ReliabilityContractError):
            derive_partition_seed(freeze_commit="z" * 40, beacon_output_hex=self.beacon)


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "docs/research/paper-rebuild-v2-2026-10-02"
MANIFEST = PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json"
COMMITMENTS = PACKET / "quarantine-commitments-v5.json"
BINDINGS = PACKET / "scientific-freeze-bindings-v5.json"
SOURCE_AUDIT = PACKET / "clinical-source-audit-v5.json"

def _sha256_ids(values: list[str] | tuple[str, ...]) -> str:
    payload = json.dumps(list(values), separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class FrozenQuarantineArtifactTests(unittest.TestCase):
    def test_commitment_artifact_matches_manifest_without_future_test_materialization(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        artifact = json.loads(COMMITMENTS.read_text(encoding="utf-8"))
        by_pmid = {str(row["pmid"]): row for row in artifact["rows"]}
        self.assertEqual(len(manifest["selected"]), 64)
        self.assertEqual(len(by_pmid), 64)
        development_ids: list[str] = []
        calibration_ids: list[str] = []
        for calculator in manifest["selected"]:
            pmid = str(calculator["pmid"])
            calculator_id = f"pmid:{pmid}"
            total = int(calculator["prospective_case_space"])
            partition = prefreeze_state_partition(calculator_id, total)
            dev_cases = cases_from_state_indices(
                calculator_id, calculator["domain_constants"], partition["development"]
            )
            cal_cases = cases_from_state_indices(
                calculator_id, calculator["domain_constants"], partition["calibration"]
            )
            dev_ids = [str(case["case_id"]) for case in dev_cases]
            cal_ids = [str(case["case_id"]) for case in cal_cases]
            row = by_pmid[pmid]
            self.assertEqual(row["development_case_ids_sha256"], _sha256_ids(dev_ids))
            self.assertEqual(row["calibration_case_ids_sha256"], _sha256_ids(cal_ids))
            self.assertEqual(row["development_state_indices_sha256"], _sha256_ids(partition["development"]))
            self.assertEqual(row["calibration_state_indices_sha256"], _sha256_ids(partition["calibration"]))
            self.assertEqual(row["candidate_state_space"], total)
            development_ids.extend(dev_ids)
            calibration_ids.extend(cal_ids)

        self.assertEqual(artifact["development_case_ids_sha256"], _sha256_ids(development_ids))
        self.assertEqual(artifact["calibration_case_ids_sha256"], _sha256_ids(calibration_ids))
        self.assertFalse(artifact["confirmatory_assignment_materialized"])
        self.assertFalse(artifact["reserve_assignment_materialized"])
        self.assertNotIn("holdout_ids_sha256", artifact)
        self.assertEqual(len(development_ids), 4096)
        self.assertEqual(len(calibration_ids), 4096)

    def test_freeze_bindings_match_current_manifest(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        commitments = json.loads(COMMITMENTS.read_text(encoding="utf-8"))
        bindings = json.loads(BINDINGS.read_text(encoding="utf-8"))
        oracle = bindings["rule_oracle"]
        spaces = [int(row["prospective_case_space"]) for row in manifest["selected"]]
        self.assertEqual(oracle["static_eligible_count"], manifest["static_eligible_count"])
        self.assertEqual(oracle["eligible_selection_stratum_count"], manifest["eligible_selection_stratum_count"])
        self.assertEqual(oracle["calculator_count"], manifest["selected_count"])
        self.assertEqual(oracle["minimum_candidate_state_space"], commitments["minimum_candidate_state_space"])
        self.assertEqual(oracle["selected_candidate_state_space_min"], min(spaces))
        self.assertEqual(oracle["selected_candidate_state_space_total"], sum(spaces))
        self.assertFalse(oracle["confirmatory_assignment_materialized"])
        self.assertFalse(oracle["reserve_assignment_materialized"])

    def test_source_audit_does_not_persist_abstract_bodies(self):
        audit = json.loads(SOURCE_AUDIT.read_text(encoding="utf-8"))
        self.assertEqual(audit["selected_count"], 64)
        for row in audit["rows"]:
            self.assertNotIn("abstract", row)
            self.assertIn("abstract_present", row)
            self.assertIn("abstract_sha256", row)


if __name__ == "__main__":
    unittest.main()
