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

    @staticmethod
    def _pass(score: float, evidence_id: str) -> dict[str, object]:
        return {
            "status": GateEvaluationState.PASS.value,
            "score": score,
            "evidence_artifact_id": evidence_id,
        }

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
        """A critical hard-gate failure dominates otherwise excellent results."""
        mock_eval_results = {
            "emergency_miss_rate": {
                "status": GateEvaluationState.FAIL.value,
                "score": 0.08,
                "reason": "Missed acute aortic dissection presentation in triage simulation",
            },
            "medication_critical_error_rate": self._pass(0.0, "fixture:medication-review"),
            "selective_risk_at_target_coverage": self._pass(0.02, "fixture:abstention-curve"),
            "citation_entailment_fidelity": self._pass(0.98, "fixture:citation-adjudication"),
            "arabic_clinical_parity_gap": self._pass(0.03, "fixture:arabic-parity"),
            "lab_report_field_extraction_accuracy": self._pass(0.99, "fixture:lab-extraction"),
            "medqa_usmle_accuracy": self._pass(0.94, "fixture:medqa"),
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_eval_results
        )

        self.assertEqual(overall_state, GateEvaluationState.FAIL.value)
        failed_gates = [g for g in gate_breakdown if g["status"] == GateEvaluationState.FAIL.value]
        self.assertEqual(len(failed_gates), 1)
        self.assertEqual(failed_gates[0]["metric_id"], "emergency_miss_rate")

    def test_all_hard_gates_pass_yields_overall_pass(self) -> None:
        """All hard gates need both a score and resolved evidence to PASS."""
        mock_eval_results = {
            "emergency_miss_rate": self._pass(0.0, "fixture:emergency"),
            "medication_critical_error_rate": self._pass(0.0, "fixture:medication"),
            "selective_risk_at_target_coverage": self._pass(0.01, "fixture:selective-risk"),
            "citation_entailment_fidelity": self._pass(0.99, "fixture:citation"),
            "arabic_clinical_parity_gap": self._pass(0.02, "fixture:arabic"),
            "lab_report_field_extraction_accuracy": self._pass(0.99, "fixture:lab"),
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_eval_results
        )

        self.assertEqual(overall_state, GateEvaluationState.PASS.value)
        self.assertTrue(all(g["status"] == GateEvaluationState.PASS.value for g in gate_breakdown))

    def test_unevaluated_hard_gate_cannot_silently_pass(self) -> None:
        """A missing hard gate yields INSUFFICIENT_EVIDENCE, never PASS."""
        mock_partial_results = {
            "emergency_miss_rate": self._pass(0.0, "fixture:emergency"),
        }

        overall_state, gate_breakdown = evaluate_hard_gates(
            self.metrics_catalog, mock_partial_results
        )

        self.assertEqual(overall_state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)
        unevaluated = [g for g in gate_breakdown if g["status"] == GateEvaluationState.NOT_EVALUATED.value]
        self.assertTrue(len(unevaluated) > 0)

    def test_status_only_pass_is_insufficient(self) -> None:
        """A self-reported PASS without score/evidence must fail closed."""
        results = {
            metric["metric_id"]: {"status": GateEvaluationState.PASS.value}
            for metric in self.metrics_catalog
            if metric["is_hard_gate"]
        }
        overall_state, breakdown = evaluate_hard_gates(self.metrics_catalog, results)
        self.assertEqual(overall_state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)
        self.assertTrue(
            all(g["status"] == GateEvaluationState.INSUFFICIENT_EVIDENCE.value for g in breakdown)
        )

    def test_malformed_hard_gate_record_is_insufficient(self) -> None:
        """An incomplete hard-gate metric cannot become enforceable merely by ID."""
        state, _ = evaluate_hard_gates(
            [{"metric_id": "gate", "is_hard_gate": True}],
            {"gate": self._pass(0.0, "fixture:fake")},
        )
        self.assertEqual(state, GateEvaluationState.INSUFFICIENT_EVIDENCE.value)

    def test_fail_precedes_missing_evidence_in_mixed_required_gates(self) -> None:
        """An observed hard-gate FAIL dominates a different missing required gate."""
        mixed = {
            "emergency_miss_rate": {
                "status": GateEvaluationState.FAIL.value,
                "score": 1.0,
                "reason": "Synthetic safety failure",
                "evidence_artifact_id": "fixture:mixed-failure",
            },
        }
        overall, breakdown = evaluate_hard_gates(self.metrics_catalog, mixed)
        self.assertEqual(overall, GateEvaluationState.FAIL.value)
        self.assertTrue(any(g["status"] == GateEvaluationState.FAIL.value for g in breakdown))
        self.assertTrue(any(g["status"] == GateEvaluationState.NOT_EVALUATED.value for g in breakdown))

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
