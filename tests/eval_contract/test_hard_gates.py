"""Tests for metrics catalog validation and hard safety gate semantics."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.model import GateEvaluationState
from src.commandmed.eval_contract.validate import (
    evaluate_hard_gates,
    validate_metric,
    validate_metrics_catalog,
)


class TestHardGatesAndMetrics(unittest.TestCase):
    """Tests for metric validation and hard-gate dominance."""

    def setUp(self) -> None:
        self.data_dir = Path(__file__).resolve().parents[2] / "data" / "eval"
        self.metrics_file = self.data_dir / "metrics.json"
        self.metrics_catalog = json.loads(self.metrics_file.read_text(encoding="utf-8"))

    def test_canonical_metrics_catalog_validates(self) -> None:
        """Canonical data/eval/metrics.json must validate cleanly."""
        is_valid, errors = validate_metrics_catalog(self.metrics_catalog)
        self.assertTrue(is_valid, f"metrics.json failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_hard_gates_are_present_in_catalog(self) -> None:
        """Ensure critical safety metrics are marked as hard gates."""
        hard_gate_ids = {m["metric_id"] for m in self.metrics_catalog if m["is_hard_gate"]}
        expected_hard_gates = {
            "emergency_miss_rate",
            "medication_critical_error_rate",
            "selective_risk_at_target_coverage",
            "citation_entailment_fidelity",
            "arabic_clinical_parity_gap",
            "lab_report_field_extraction_accuracy",
        }
        for ehg in expected_hard_gates:
            self.assertIn(ehg, hard_gate_ids, f"Expected hard gate missing: {ehg}")

    def test_hard_gate_dominance_over_high_aggregate_score(self) -> None:
        """
        US2 / FR-004: High aggregate performance cannot compensate for a failed hard gate.
        A run with 99.5% accuracy across benchmarks but failing emergency_miss_rate MUST yield FAIL.
        """
        # Synthetic run: Excellent aggregate performance across all metrics except 1 critical failure
        mock_eval_results = {
            "emergency_miss_rate": {
                "status": GateEvaluationState.FAIL.value,
                "score": 0.08,
                "reason": "Missed acute aortic dissection presentation in triage simulation",
            },
            "medication_critical_error_rate": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.0,
                "reason": "Zero drug interaction errors detected",
            },
            "selective_risk_at_target_coverage": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.02,
                "reason": "Risk below threshold at 80% coverage",
            },
            "citation_entailment_fidelity": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.98,
                "reason": "98% entailment verified",
            },
            "arabic_clinical_parity_gap": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.03,
                "reason": "Arabic-English gap is 3%",
            },
            "lab_report_field_extraction_accuracy": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.99,
                "reason": "99% F1 extraction accuracy",
            },
            "medqa_usmle_accuracy": {
                "status": GateEvaluationState.PASS.value,
                "score": 0.94,
                "reason": "94% USMLE accuracy",
            },
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_eval_results
        )

        self.assertEqual(
            overall_state,
            GateEvaluationState.FAIL.value,
            "Overall outcome must be FAIL when any hard gate fails, despite high mean performance",
        )

        failed_gates = [g for g in gate_breakdown if g["status"] == GateEvaluationState.FAIL.value]
        self.assertEqual(len(failed_gates), 1)
        self.assertEqual(failed_gates[0]["metric_id"], "emergency_miss_rate")

    def test_all_hard_gates_pass_yields_overall_pass(self) -> None:
        """When all evaluated hard gates pass, overall state is PASS."""
        mock_eval_results = {
            "emergency_miss_rate": {"status": GateEvaluationState.PASS.value, "score": 0.0},
            "medication_critical_error_rate": {"status": GateEvaluationState.PASS.value, "score": 0.0},
            "selective_risk_at_target_coverage": {"status": GateEvaluationState.PASS.value, "score": 0.01},
            "citation_entailment_fidelity": {"status": GateEvaluationState.PASS.value, "score": 0.99},
            "arabic_clinical_parity_gap": {"status": GateEvaluationState.PASS.value, "score": 0.02},
            "lab_report_field_extraction_accuracy": {"status": GateEvaluationState.PASS.value, "score": 0.99},
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_eval_results
        )

        self.assertEqual(overall_state, GateEvaluationState.PASS.value)
        self.assertTrue(all(g["status"] == GateEvaluationState.PASS.value for g in gate_breakdown))

    def test_unevaluated_hard_gate_cannot_silently_pass(self) -> None:
        """FR-004: A missing or unevaluated hard gate must yield INSUFFICIENT_EVIDENCE, never PASS."""
        mock_partial_results = {
            "emergency_miss_rate": {"status": GateEvaluationState.PASS.value, "score": 0.0},
            # Other hard gates omitted
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_partial_results
        )

        self.assertEqual(overall_state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)
        unevaluated = [g for g in gate_breakdown if g["status"] == GateEvaluationState.NOT_EVALUATED.value]
        self.assertTrue(len(unevaluated) > 0)

    def test_invalid_metric_direction_rejection(self) -> None:
        """Validation fails if metric direction is invalid."""
        invalid_metric = {
            "metric_id": "test_invalid_metric",
            "name": "Test Invalid",
            "category": "SAFETY",
            "description": "Desc",
            "direction": "INVALID_DIRECTION",
            "unit": "ratio",
            "is_hard_gate": False,
            "threshold_state": "DEFINED_NOT_YET_THRESHOLD_FROZEN",
            "applicable_roles": ["CLINICAL_PROFESSIONAL"],
            "applicable_modalities": ["TEXT"],
            "applicable_languages": ["en"],
            "required_evidence": "Review",
        }
        errors = validate_metric(invalid_metric)
        self.assertTrue(any("Invalid direction" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
