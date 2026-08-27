"""I009 negative fixtures for every prohibited Spec 007 optimization surface."""

from __future__ import annotations

import unittest

from src.commandmed.spec007.quarantine import evaluate_quarantine_source


class TestProhibitedPurposeSurfaces(unittest.TestCase):
    def test_training_rejects_gold_source(self):
        self.assertFalse(
            evaluate_quarantine_source("COMMANDMED_CLINICAL_GOLD", "TRAIN")["allowed"]
        )

    def test_monitoring_is_not_a_canonical_quarantine_purpose(self):
        decision = evaluate_quarantine_source("VERIFIED_DEV_SPLIT", "MONITORING")
        self.assertFalse(decision["allowed"])
        self.assertEqual("UNKNOWN_PURPOSE", decision["reason_code"])

    def test_recipe_selection_is_not_a_canonical_quarantine_purpose(self):
        decision = evaluate_quarantine_source("VERIFIED_DEV_SPLIT", "RECIPE_SELECTION")
        self.assertFalse(decision["allowed"])
        self.assertEqual("UNKNOWN_PURPOSE", decision["reason_code"])

    def test_checkpoint_selection_rejects_gold_source(self):
        self.assertFalse(
            evaluate_quarantine_source(
                "COMMANDMED_ARABIC_GOLD", "CHECKPOINT_SELECTION"
            )["allowed"]
        )

    def test_model_selection_is_not_a_canonical_quarantine_purpose(self):
        decision = evaluate_quarantine_source("MODEL_SELECTION_DEV_SET", "MODEL_SELECTION")
        self.assertFalse(decision["allowed"])
        self.assertEqual("UNKNOWN_PURPOSE", decision["reason_code"])


if __name__ == "__main__":
    unittest.main()
