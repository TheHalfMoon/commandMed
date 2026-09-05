"""Permanent evidence checks for the bounded SP007-RO-001 nonce repair."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec007.research_tournament import (
    compute_research_component_tournament_protocol_sha256,
)
from src.commandmed.spec007.research_tournament_assets import (
    compute_research_component_evaluation_asset_set_sha256,
    compute_research_component_evaluation_asset_sha256,
    evaluate_research_component_asset_admission,
)

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "specs" / "007-sft-v1"


def load_json(name: str):
    return json.loads((SPEC / name).read_text(encoding="utf-8"))


EVIDENCE = load_json("e004-research-component-evaluation-nonce-repair-evidence-v1.json")
ASSET_SET = load_json("e004-research-component-tournament-evaluation-assets-v1.json")
PROTOCOL = load_json("e004-research-component-tournament-protocol-v1.json")
LINEAGE = json.loads(
    (ROOT / "data" / "lineage" / "lineage_contract.json").read_text(encoding="utf-8")
)

EXPECTED_DECISION = (
    "FOUNDER_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION="
    "E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_DECISION_B"
)
EXPECTED_ASSET_SET_SHA256 = "709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454"
EXPECTED_PROTOCOL_SHA256 = "1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8"


class ResearchComponentNonceRepairEvidenceTests(unittest.TestCase):
    def test_repair_evidence_is_exactly_bounded(self):
        self.assertEqual(EVIDENCE["schema_version"], "1")
        self.assertEqual(
            EVIDENCE["evidence_id"],
            "E004_RESEARCH_COMPONENT_EVAL_NONCE_REPAIR_EVIDENCE_V1",
        )
        self.assertEqual(EVIDENCE["founder_decision_token"], EXPECTED_DECISION)
        self.assertEqual(
            EVIDENCE["repair_formula"],
            'SHA256(f"{fixture_namespace_seed}|{metric_family}|{index}")[:16]',
        )
        self.assertEqual(EVIDENCE["repair_indexing"], "ONE_BASED_DECIMAL_UNPADDED")
        self.assertEqual(
            EVIDENCE["repair_embedding_rule"],
            "FIRST_EXACT_FULL_NONCE_OCCURRENCE_ONLY",
        )
        self.assertEqual(
            EVIDENCE["validator_repair"],
            "ALLOW_EXACT_NON_CLINICAL_NEGATIVE_DESCRIPTOR_ONLY",
        )
        self.assertEqual(EVIDENCE["nonce_record_count"], 80)
        self.assertFalse(EVIDENCE["semantic_payload_change"])
        self.assertEqual(EVIDENCE["semantic_projection_proof"], "PASS")
        self.assertFalse(EVIDENCE["caller_controlled_eligible_state"])
        self.assertEqual(EVIDENCE["authorized_spend_usd"], 0)
        self.assertFalse(EVIDENCE["model_execution_performed"])
        self.assertFalse(EVIDENCE["tournament_execution_performed"])
        self.assertFalse(EVIDENCE["winner_selected"])
        self.assertFalse(EVIDENCE["training_performed"])
        self.assertFalse(EVIDENCE["private_gold_accessed"])
        self.assertFalse(EVIDENCE["phi_accessed"])

    def test_evidence_binds_current_asset_set_and_protocol(self):
        self.assertEqual(EVIDENCE["repaired_asset_set_sha256"], EXPECTED_ASSET_SET_SHA256)
        self.assertEqual(ASSET_SET["asset_set_sha256"], EXPECTED_ASSET_SET_SHA256)
        self.assertEqual(
            compute_research_component_evaluation_asset_set_sha256(ASSET_SET),
            EXPECTED_ASSET_SET_SHA256,
        )
        self.assertEqual(EVIDENCE["protocol_sha256_rebinding"]["new"], EXPECTED_PROTOCOL_SHA256)
        self.assertEqual(PROTOCOL["protocol_sha256"], EXPECTED_PROTOCOL_SHA256)
        self.assertEqual(
            compute_research_component_tournament_protocol_sha256(PROTOCOL),
            EXPECTED_PROTOCOL_SHA256,
        )

    def test_all_seven_asset_hash_rebindings_match_current_subject(self):
        assets = {asset["asset_id"]: asset for asset in ASSET_SET["asset_records"]}
        rebindings = EVIDENCE["asset_hash_rebindings"]
        self.assertEqual(len(assets), 7)
        self.assertEqual(len(rebindings), 7)
        self.assertEqual({item["asset_id"] for item in rebindings}, set(assets))
        for binding in rebindings:
            asset = assets[binding["asset_id"]]
            with self.subTest(asset_id=binding["asset_id"]):
                self.assertEqual(asset["asset_sha256"], binding["new_asset_sha256"])
                self.assertEqual(
                    compute_research_component_evaluation_asset_sha256(asset),
                    binding["new_asset_sha256"],
                )

    def test_all_seven_spec003_admissions_recompute_eligible(self):
        recorded = {item["asset_id"]: item for item in EVIDENCE["spec003_admissions"]}
        self.assertEqual(len(recorded), 7)
        for asset in ASSET_SET["asset_records"]:
            result = evaluate_research_component_asset_admission(asset, LINEAGE)
            with self.subTest(asset_id=asset["asset_id"]):
                self.assertEqual(recorded[asset["asset_id"]]["state"], "ELIGIBLE")
                self.assertEqual(recorded[asset["asset_id"]]["reason_codes"], [])
                self.assertEqual(result["state"], "ELIGIBLE")
                self.assertEqual(result["reason_codes"], [])

    def test_nonce_edit_log_is_complete_unique_and_replaced(self):
        edits = EVIDENCE["nonce_edits"]
        self.assertEqual(len(edits), 80)
        self.assertEqual(len({item["record_id"] for item in edits}), 80)
        self.assertTrue(all(len(item["old_nonce"]) == 16 for item in edits))
        self.assertTrue(all(len(item["new_nonce"]) == 16 for item in edits))
        self.assertTrue(all(item["old_nonce"] != item["new_nonce"] for item in edits))


if __name__ == "__main__":
    unittest.main()
