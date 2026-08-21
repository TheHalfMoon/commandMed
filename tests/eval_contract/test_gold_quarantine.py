"""Tests for private Gold protocol metadata and data quarantine rules."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.model import GoldFamilyId, Purpose
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

    def test_contamination_records_validate(self) -> None:
        """FR-007: Contamination metadata records validate cleanly."""
        records = self.quarantine_data["contamination_records"]
        is_valid, errors = validate_contamination_records(records)
        self.assertTrue(is_valid, f"contamination_records failed validation: {errors}")
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
