"""Regression tests for fail-closed governance validation."""
from __future__ import annotations

import unittest

from src.commandmed.eval_contract.model import GateEvaluationState
from src.commandmed.eval_contract.validate import (
    evaluate_hard_gates,
    validate_benchmark,
    validate_benchmark_registry,
    validate_contamination_records,
    validate_gold_protocols,
    validate_metrics_catalog,
    validate_quarantine_rules,
)


def valid_benchmark() -> dict:
    return {
        "benchmark_id": "fixture",
        "canonical_name": "Fixture",
        "primary_source": "Canonical source",
        "source_uri": "https://example.com/source",
        "source_identifier": "fixture:v1",
        "source_revision": "abc123",
        "verification_date": "2026-08-22",
        "artifact_version": "fixture.json",
        "access_class": "PUBLIC",
        "license_status": "MIT",
        "license_source_uri": "https://example.com/license",
        "languages": ["en"],
        "roles": ["CLINICAL_PROFESSIONAL"],
        "modalities": ["TEXT"],
        "capability_domains": ["SAFETY"],
        "contamination_sensitivity": "HIGH",
        "intended_use": "DEVELOPMENT",
        "verification_status": "VERIFIED",
        "notes": "Synthetic fixture only",
    }


def hard_gate(metric_id: str = "gate") -> dict:
    return {
        "metric_id": metric_id,
        "name": "Gate",
        "category": "SAFETY",
        "description": "Synthetic gate",
        "direction": "LOWER_BETTER",
        "unit": "ratio",
        "is_hard_gate": True,
        "threshold_state": "FROZEN",
        "applicable_roles": ["CLINICAL_PROFESSIONAL"],
        "applicable_modalities": ["TEXT"],
        "applicable_languages": ["en"],
        "required_evidence": "Synthetic evidence",
    }


def canonical_quarantine_rules() -> list[dict]:
    gold = [
        "COMMANDMED_ARABIC_GOLD",
        "COMMANDMED_CLINICAL_GOLD",
        "COMMANDMED_MULTIMODAL_GOLD",
    ]
    return [
        {
            "purpose": "CALIBRATION",
            "allowed_sources": ["CALIBRATION_HOLD_OUT_SPLIT"],
            "prohibited_sources": gold,
            "can_train": False,
            "can_select_model": True,
        },
        {
            "purpose": "CHECKPOINT_SELECTION",
            "allowed_sources": ["MODEL_SELECTION_DEV_SET", "PUBLIC_BENCHMARK_DEV_SPLITS"],
            "prohibited_sources": gold,
            "can_train": False,
            "can_select_model": True,
        },
        {
            "purpose": "DEV",
            "allowed_sources": ["HELD_OUT_SYNTHETIC_PILOT_CASES", "VERIFIED_DEV_SPLIT"],
            "prohibited_sources": gold,
            "can_train": False,
            "can_select_model": True,
        },
        {
            "purpose": "PRIVATE_GOLD",
            "allowed_sources": gold,
            "prohibited_sources": ["DEVELOPMENT_SPLITS", "PUBLIC_SCRAPED_DATA", "TRAINING_CORPORA"],
            "can_train": False,
            "can_select_model": False,
        },
        {
            "purpose": "PUBLIC_EXTERNAL_EVAL",
            "allowed_sources": ["PUBLIC_BENCHMARK_CANONICAL_TEST_SPLITS"],
            "prohibited_sources": gold,
            "can_train": False,
            "can_select_model": False,
        },
        {
            "purpose": "TRAIN",
            "allowed_sources": [
                "VERIFIED_PERMISSIVE_PRETRAINING_CORPUS",
                "VERIFIED_SFT_CURRICULUM_DATA",
                "VERIFIED_SYNTHETIC_DERIVED_EXAMPLES",
            ],
            "prohibited_sources": gold + ["PUBLIC_EXTERNAL_EVAL"],
            "can_train": True,
            "can_select_model": False,
        },
    ]


class TestFailClosedRepair(unittest.TestCase):
    def test_01_empty_hard_gate_catalog_is_not_pass(self):
        state, breakdown = evaluate_hard_gates([], {})
        self.assertEqual(state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)
        self.assertTrue(breakdown)

    def test_02_zero_hard_gate_catalog_is_not_pass(self):
        metric = hard_gate()
        metric["is_hard_gate"] = False
        state, _ = evaluate_hard_gates([metric], {})
        self.assertEqual(state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)

    def test_03_all_hard_gates_pass(self):
        state, _ = evaluate_hard_gates([hard_gate()], {"gate": {"status": "PASS", "score": 0.0}})
        self.assertEqual(state, "PASS")

    def test_04_failed_hard_gate_dominates(self):
        state, _ = evaluate_hard_gates([hard_gate()], {"gate": {"status": "FAIL", "score": 1.0}})
        self.assertEqual(state, "FAIL")

    def test_05_missing_hard_gate_evidence_is_insufficient(self):
        state, _ = evaluate_hard_gates([hard_gate()], {})
        self.assertEqual(state, "INSUFFICIENT_EVIDENCE")

    def test_06_canonical_quarantine_matrix_validates(self):
        ok, errors = validate_quarantine_rules(canonical_quarantine_rules())
        self.assertTrue(ok, errors)

    def test_07_unknown_quarantine_source_rejected(self):
        rules = canonical_quarantine_rules()
        rules[0]["allowed_sources"] = ["UNKNOWN_SOURCE"]
        ok, errors = validate_quarantine_rules(rules)
        self.assertFalse(ok)
        self.assertTrue(any("Invalid quarantine source token" in e for e in errors))

    def test_08_quarantine_overlap_rejected(self):
        rules = canonical_quarantine_rules()
        rules[0]["prohibited_sources"].append("CALIBRATION_HOLD_OUT_SPLIT")
        ok, errors = validate_quarantine_rules(rules)
        self.assertFalse(ok)
        self.assertTrue(any("both allowed_sources and prohibited_sources" in e for e in errors))

    def test_09_train_gold_source_rejected(self):
        rules = canonical_quarantine_rules()
        train = next(r for r in rules if r["purpose"] == "TRAIN")
        train["allowed_sources"].append("COMMANDMED_CLINICAL_GOLD")
        ok, _ = validate_quarantine_rules(rules)
        self.assertFalse(ok)

    def test_10_private_gold_training_source_rejected(self):
        rules = canonical_quarantine_rules()
        private = next(r for r in rules if r["purpose"] == "PRIVATE_GOLD")
        private["allowed_sources"].append("TRAINING_CORPORA")
        ok, _ = validate_quarantine_rules(rules)
        self.assertFalse(ok)

    def test_11_public_eval_selection_rejected(self):
        rules = canonical_quarantine_rules()
        public = next(r for r in rules if r["purpose"] == "PUBLIC_EXTERNAL_EVAL")
        public["can_select_model"] = True
        ok, errors = validate_quarantine_rules(rules)
        self.assertFalse(ok)
        self.assertTrue(any("can_select_model=False" in e for e in errors))

    def test_12_valid_calendar_date_accepted(self):
        self.assertEqual(validate_benchmark(valid_benchmark()), [])

    def test_13_valid_non_leap_date_accepted(self):
        record = valid_benchmark(); record["verification_date"] = "2026-02-28"
        self.assertEqual(validate_benchmark(record), [])

    def test_14_february_30_rejected(self):
        record = valid_benchmark(); record["verification_date"] = "2026-02-30"
        self.assertTrue(any("real calendar date" in e for e in validate_benchmark(record)))

    def test_15_month_13_rejected(self):
        record = valid_benchmark(); record["verification_date"] = "2026-13-01"
        self.assertTrue(validate_benchmark(record))

    def test_16_month_zero_rejected(self):
        record = valid_benchmark(); record["verification_date"] = "2026-00-10"
        self.assertTrue(validate_benchmark(record))

    def test_17_non_date_rejected(self):
        record = valid_benchmark(); record["verification_date"] = "not-a-date"
        self.assertTrue(validate_benchmark(record))

    def test_18_registry_none_member_fails_without_exception(self):
        ok, errors = validate_benchmark_registry([None])
        self.assertFalse(ok); self.assertTrue(errors)

    def test_19_registry_string_member_fails_without_exception(self):
        ok, errors = validate_benchmark_registry(["bad"])
        self.assertFalse(ok); self.assertTrue(errors)

    def test_20_registry_number_member_fails_without_exception(self):
        ok, errors = validate_benchmark_registry([123])
        self.assertFalse(ok); self.assertTrue(errors)

    def test_21_numeric_primary_source_fails_without_exception(self):
        record = valid_benchmark(); record["primary_source"] = 123
        self.assertTrue(validate_benchmark(record))

    def test_22_list_source_uri_fails_without_exception(self):
        record = valid_benchmark(); record["source_uri"] = []
        self.assertTrue(validate_benchmark(record))

    def test_23_object_language_fails_without_exception(self):
        record = valid_benchmark(); record["languages"] = [{"bad": "object"}]
        self.assertTrue(validate_benchmark(record))

    def test_24_metric_none_member_fails_without_exception(self):
        ok, errors = validate_metrics_catalog([None])
        self.assertFalse(ok); self.assertTrue(errors)

    def test_25_gold_non_dict_member_fails_without_exception(self):
        ok, errors = validate_gold_protocols([[]])
        self.assertFalse(ok); self.assertTrue(errors)

    def test_26_quarantine_object_source_fails_without_exception(self):
        rules = canonical_quarantine_rules(); rules[0]["allowed_sources"] = [{}]
        ok, errors = validate_quarantine_rules(rules)
        self.assertFalse(ok); self.assertTrue(errors)

    def test_27_quarantine_nested_source_fails_without_exception(self):
        rules = canonical_quarantine_rules(); rules[0]["allowed_sources"] = [["nested"]]
        ok, errors = validate_quarantine_rules(rules)
        self.assertFalse(ok); self.assertTrue(errors)

    def test_28_numeric_contamination_evidence_fails_without_exception(self):
        records = [{
            "asset_id": "asset",
            "exact_match_status": "NOT_ASSESSED",
            "semantic_overlap_status": "NOT_ASSESSED",
            "evidence_artifact_id": 123,
            "methodology_interface": "fixture",
            "notes": "fixture",
        }]
        ok, errors = validate_contamination_records(records)
        self.assertFalse(ok); self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
