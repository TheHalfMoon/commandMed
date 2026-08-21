"""Tests for private Gold protocol metadata and data quarantine rules."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.model import ExactMatchStatus, GoldFamilyId, Purpose, SemanticOverlapStatus
from src.commandmed.eval_contract.validate import (
    check_no_payload_markers,
    validate_contamination_records,
    validate_gold_protocol,
    validate_gold_protocols,
    validate_quarantine_rules,
)


class TestGoldAndQuarantine(unittest.TestCase):
    """Tests for Gold protocols, quarantine rules, and anti-contamination contracts."""

    def setUp(self) -> None:
        self.data_dir = Path(__file__).resolve().parents[2] / "data" / "eval"
        self.gold_file = self.data_dir / "gold_protocols.json"
        self.quarantine_file = self.data_dir / "quarantine.json"

        self.gold_data = json.loads(self.gold_file.read_text(encoding="utf-8"))
        self.quarantine_data = json.loads(self.quarantine_file.read_text(encoding="utf-8"))

    def test_canonical_gold_protocols_validate(self) -> None:
        """Canonical data/eval/gold_protocols.json must validate cleanly."""
        is_valid, errors = validate_gold_protocols(self.gold_data)
        self.assertTrue(is_valid, f"gold_protocols.json failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_all_three_canonical_gold_families_present(self) -> None:
        """FR-005: All 3 canonical Gold families must exist in protocols."""
        present_families = {g["family_id"] for g in self.gold_data}
        expected = {
            GoldFamilyId.COMMANDMED_CLINICAL_GOLD.value,
            GoldFamilyId.COMMANDMED_ARABIC_GOLD.value,
            GoldFamilyId.COMMANDMED_MULTIMODAL_GOLD.value,
        }
        self.assertEqual(present_families, expected)

    def test_gold_selection_stage_contradiction_fails(self) -> None:
        """Finding 3: Gold protocol cannot specify candidate selection scoring stages."""
        bad_gold = dict(self.gold_data[0])
        bad_gold["permitted_scoring_stages"] = [
            "FINAL_BACKBONE_SELECTION_GATE",  # Contradiction with non-selection policy!
            "PRE_RELEASE_SAFETY_AUDIT",
        ]
        errors = validate_gold_protocol(bad_gold)
        self.assertTrue(any("Private Gold cannot perform candidate selection" in e for e in errors))

    def test_gold_adapter_gate_contradiction_fails(self) -> None:
        """Finding 3: Gold protocol cannot specify ADAPTER_GATE candidate selection."""
        bad_gold = dict(self.gold_data[2])
        bad_gold["permitted_scoring_stages"] = [
            "MULTIMODAL_ADAPTER_GATE",  # Contradiction!
            "PRE_RELEASE_SAFETY_AUDIT",
        ]
        errors = validate_gold_protocol(bad_gold)
        self.assertTrue(any("Private Gold cannot perform candidate selection" in e for e in errors))

    def test_gold_protocol_requires_power_analysis(self) -> None:
        """Gold protocols MUST require power analysis; failing to require it fails validation."""
        bad_gold = dict(self.gold_data[0])
        bad_gold["power_analysis_required"] = False
        errors = validate_gold_protocol(bad_gold)
        self.assertTrue(any("power_analysis_required" in e for e in errors))

    def test_gold_protocol_mandatory_prohibitions_enforced(self) -> None:
        """Gold protocols MUST explicitly prohibit training, distillation, selection, etc."""
        bad_gold = dict(self.gold_data[0])
        bad_gold["prohibited_optimization_uses"] = ["TRAIN"]  # Missing CPT, SFT, DISTILLATION, etc.
        errors = validate_gold_protocol(bad_gold)
        self.assertTrue(any("missing mandatory prohibitions" in e for e in errors))

    def test_gold_protocols_contain_zero_payload_or_phi(self) -> None:
        """FR-005 / US3: Ensure zero case content or PHI payload is in gold protocols."""
        errors = check_no_payload_markers(self.gold_data)
        self.assertEqual(len(errors), 0)

    def test_canonical_quarantine_rules_validate(self) -> None:
        """Canonical data/eval/quarantine.json must validate cleanly."""
        rules = self.quarantine_data["quarantine_rules"]
        is_valid, errors = validate_quarantine_rules(rules)
        self.assertTrue(is_valid, f"quarantine_rules failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_public_external_eval_cannot_select_model(self) -> None:
        """Finding 5: PUBLIC_EXTERNAL_EVAL must have can_select_model=False to prevent test leakage."""
        rules = self.quarantine_data["quarantine_rules"]
        public_rule = next(r for r in rules if r["purpose"] == Purpose.PUBLIC_EXTERNAL_EVAL.value)
        self.assertFalse(public_rule["can_train"])
        self.assertFalse(public_rule["can_select_model"])

    def test_public_external_eval_with_selection_fails(self) -> None:
        """Finding 5: Attempting to set can_select_model=True on PUBLIC_EXTERNAL_EVAL fails validation."""
        illegal_rules = [
            {
                "purpose": Purpose.PUBLIC_EXTERNAL_EVAL.value,
                "allowed_sources": ["PUBLIC_BENCHMARK_CANONICAL_TEST_SPLITS"],
                "prohibited_sources": ["PRIVATE_GOLD"],
                "can_train": False,
                "can_select_model": True,  # Illegal!
            }
        ]
        is_valid, errors = validate_quarantine_rules(illegal_rules)
        self.assertFalse(is_valid)
        self.assertTrue(any("purpose 'PUBLIC_EXTERNAL_EVAL' must have can_select_model=False" in e for e in errors))

    def test_private_gold_cannot_train_or_select_model(self) -> None:
        """FR-006: Quarantine rule for PRIVATE_GOLD must have can_train=False and can_select_model=False."""
        rules = self.quarantine_data["quarantine_rules"]
        gold_rule = next(r for r in rules if r["purpose"] == Purpose.PRIVATE_GOLD.value)
        self.assertFalse(gold_rule["can_train"])
        self.assertFalse(gold_rule["can_select_model"])

    def test_quarantine_violation_rejection(self) -> None:
        """Attempting to allow training on PRIVATE_GOLD fails validation."""
        illegal_rules = [
            {
                "purpose": Purpose.PRIVATE_GOLD.value,
                "allowed_sources": ["ANY"],
                "prohibited_sources": [],
                "can_train": True,  # Illegal!
                "can_select_model": False,
            }
        ]
        is_valid, errors = validate_quarantine_rules(illegal_rules)
        self.assertFalse(is_valid)
        self.assertTrue(any("Quarantine violation" in e for e in errors))

    def test_canonical_contamination_records_validate(self) -> None:
        """Finding 4: Canonical contamination metadata records validate cleanly with NOT_ASSESSED state."""
        records = self.quarantine_data["contamination_records"]
        is_valid, errors = validate_contamination_records(records)
        self.assertTrue(is_valid, f"contamination_records failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_checked_clean_without_evidence_fails(self) -> None:
        """Finding 4: Claiming CHECKED_CLEAN with evidence_artifact_id='NONE' fails validation."""
        bad_records = [
            {
                "asset_id": "test_asset",
                "exact_match_status": ExactMatchStatus.CHECKED_CLEAN.value,
                "semantic_overlap_status": SemanticOverlapStatus.NOT_ASSESSED.value,
                "evidence_artifact_id": "NONE",  # Unsubstantiated claim!
                "methodology_interface": "13-gram hash",
                "notes": "Notes",
            }
        ]
        is_valid, errors = validate_contamination_records(bad_records)
        self.assertFalse(is_valid)
        self.assertTrue(any("exact_match_status='CHECKED_CLEAN' requires a resolved evidence_artifact_id" in e for e in errors))

    def test_assessed_low_risk_without_evidence_fails(self) -> None:
        """Finding 4: Claiming ASSESSED_LOW_RISK with evidence_artifact_id='NONE' fails validation."""
        bad_records = [
            {
                "asset_id": "test_asset",
                "exact_match_status": ExactMatchStatus.NOT_ASSESSED.value,
                "semantic_overlap_status": SemanticOverlapStatus.ASSESSED_LOW_RISK.value,
                "evidence_artifact_id": "NONE",  # Unsubstantiated claim!
                "methodology_interface": "Embedding search",
                "notes": "Notes",
            }
        ]
        is_valid, errors = validate_contamination_records(bad_records)
        self.assertFalse(is_valid)
        self.assertTrue(any("semantic_overlap_status='ASSESSED_LOW_RISK' requires a resolved evidence_artifact_id" in e for e in errors))

    def test_overlap_found_without_evidence_fails(self) -> None:
        """Finding 6: Substantive assessment OVERLAP_FOUND without evidence ID must fail (evidence symmetry)."""
        bad_records = [
            {
                "asset_id": "test_asset",
                "exact_match_status": ExactMatchStatus.OVERLAP_FOUND.value,
                "semantic_overlap_status": SemanticOverlapStatus.NOT_ASSESSED.value,
                "evidence_artifact_id": "NONE",  # Unsubstantiated claim!
                "methodology_interface": "13-gram hash",
                "notes": "Notes",
            }
        ]
        is_valid, errors = validate_contamination_records(bad_records)
        self.assertFalse(is_valid)
        self.assertTrue(any("exact_match_status='OVERLAP_FOUND' requires a resolved evidence_artifact_id" in e for e in errors))

    def test_assessed_high_risk_without_evidence_fails(self) -> None:
        """Finding 6: Substantive assessment ASSESSED_HIGH_RISK without evidence ID must fail (evidence symmetry)."""
        bad_records = [
            {
                "asset_id": "test_asset",
                "exact_match_status": ExactMatchStatus.NOT_ASSESSED.value,
                "semantic_overlap_status": SemanticOverlapStatus.ASSESSED_HIGH_RISK.value,
                "evidence_artifact_id": "NONE",  # Unsubstantiated claim!
                "methodology_interface": "Embedding search",
                "notes": "Notes",
            }
        ]
        is_valid, errors = validate_contamination_records(bad_records)
        self.assertFalse(is_valid)
        self.assertTrue(any("semantic_overlap_status='ASSESSED_HIGH_RISK' requires a resolved evidence_artifact_id" in e for e in errors))

    def test_blocked_assessment_without_evidence_fails(self) -> None:
        """Finding 6: BLOCKED caused by an actual assessment must also be evidence-bound."""
        bad_records = [
            {
                "asset_id": "test_asset",
                "exact_match_status": ExactMatchStatus.BLOCKED.value,
                "semantic_overlap_status": SemanticOverlapStatus.BLOCKED.value,
                "evidence_artifact_id": "NONE",  # Unsubstantiated claim!
                "methodology_interface": "13-gram hash",
                "notes": "Notes",
            }
        ]
        is_valid, errors = validate_contamination_records(bad_records)
        self.assertFalse(is_valid)
        self.assertTrue(any("exact_match_status='BLOCKED' requires a resolved evidence_artifact_id" in e for e in errors))
        self.assertTrue(any("semantic_overlap_status='BLOCKED' requires a resolved evidence_artifact_id" in e for e in errors))

    def test_substantive_assessment_with_evidence_passes(self) -> None:
        """Finding 6: Substantive contamination assessments with a resolved evidence ID validate cleanly."""
        good_records = [
            {
                "asset_id": "test_asset_clean",
                "exact_match_status": ExactMatchStatus.CHECKED_CLEAN.value,
                "semantic_overlap_status": SemanticOverlapStatus.ASSESSED_LOW_RISK.value,
                "evidence_artifact_id": "evidence:decontam-report-2026-08-22-sha256-abc123",
                "methodology_interface": "13-gram hash + embedding search",
                "notes": "Evidence-bound assessment",
            },
            {
                "asset_id": "test_asset_overlap",
                "exact_match_status": ExactMatchStatus.OVERLAP_FOUND.value,
                "semantic_overlap_status": SemanticOverlapStatus.ASSESSED_HIGH_RISK.value,
                "evidence_artifact_id": "evidence:decontam-report-2026-08-22-sha256-def456",
                "methodology_interface": "13-gram hash + embedding search",
                "notes": "Evidence-bound assessment",
            },
        ]
        is_valid, errors = validate_contamination_records(good_records)
        self.assertTrue(is_valid, f"evidence-bound records failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_not_assessed_and_pending_remain_valid_without_evidence(self) -> None:
        """Finding 6: NOT_ASSESSED and PENDING remain valid evidence-free states."""
        baseline_records = [
            {
                "asset_id": "test_asset_baseline",
                "exact_match_status": ExactMatchStatus.NOT_ASSESSED.value,
                "semantic_overlap_status": SemanticOverlapStatus.PENDING.value,
                "evidence_artifact_id": "NONE",
                "methodology_interface": "Interface specification",
                "notes": "Pre-experimental baseline",
            }
        ]
        is_valid, errors = validate_contamination_records(baseline_records)
        self.assertTrue(is_valid, f"baseline records failed validation: {errors}")
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
