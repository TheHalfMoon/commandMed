"""FD-009 non-human T1/A2 evidence-policy tests.

Synthetic fixtures only. Numeric values exercise structure and fail-closed
behavior; they are not commandMed scientific threshold recommendations.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec005.fd009 import (
    FD009_CLINICAL_POLICY_AUTHORITY,
    FD009_POLICY_ID,
    FD009_STATISTICAL_POLICY_AUTHORITY,
    evaluate_fd009_scientific_selection_readiness,
    validate_fd009_threshold_policy,
)

ROOT = Path(__file__).resolve().parents[2]
QUALITY_CONTRACT_PATH = ROOT / "data/spec005/selection_quality_contract.json"
METRICS_V2_PATH = ROOT / "data/eval/metrics-v2.json"

SEVEN_LANES = [
    "A_MEDICAL_KNOWLEDGE_BIOMEDICAL_REASONING",
    "B_PATIENT_CAREGIVER_CLINICAL_SAFETY",
    "C_UNCERTAINTY_ABSTENTION_INFORMATION_SEEKING",
    "D_EVIDENCE_GROUNDED_CLINICAL",
    "E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
    "F_CLINICAL_PROFESSIONAL_REASONING_WORKFLOW",
    "G_LAB_DOCUMENT_STRUCTURED_QUALIFICATION",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def make_quality_contract():
    return load_json(QUALITY_CONTRACT_PATH)


def make_metrics_v2():
    return load_json(METRICS_V2_PATH)


def first_selection_metric(metrics_v2):
    for metric in metrics_v2["metrics"]:
        for requirement in metric.get("evidence_requirements", []):
            if requirement.get("evidence_role") in {"SELECTION_DEV", "QUALIFICATION_ONLY"}:
                return metric["metric_id"], requirement["evidence_role"]
    raise AssertionError("no selection-eligible metric found")


def make_threshold(metrics_v2, lane=SEVEN_LANES[0], policy_id="TP-001", **overrides):
    metric_id, role = first_selection_metric(metrics_v2)
    record = {
        "threshold_policy_id": policy_id,
        "threshold_policy_version": "1.0",
        "metric_id": metric_id,
        "metric_evidence_role": role,
        "lane_id": lane,
        "required_stratum_or_scope": "SYNTHETIC_TEST_SCOPE",
        "estimand_id": "EST-SYNTHETIC",
        "metric_direction": "HIGHER_BETTER",
        "decision_role": "HARD_GATE",
        "threshold_kind": "ABSOLUTE_THRESHOLD",
        "threshold_value_or_margin": 0.5,
        "unit_or_scale": "SYNTHETIC_SCALE",
        "clinical_meaningfulness_evidence_ids": ["EVIDENCE-CLINICAL-001"],
        "statistical_justification_evidence_ids": ["EVIDENCE-STATISTICAL-001"],
        "clinical_review_authority_reference": FD009_CLINICAL_POLICY_AUTHORITY,
        "statistical_review_authority_reference": FD009_STATISTICAL_POLICY_AUTHORITY,
        "conflict_disposition_record_ids": [],
        "pre_result_freeze": True,
        "record_canonical_sha256": "a" * 64,
    }
    record.update(overrides)
    return record


def make_design(lane, threshold_id, design_id):
    return {
        "statistical_design_id": design_id,
        "design_version": "1.0",
        "quality_lane": lane,
        "metric_id_or_metric_mapping_id": "MM-SYNTHETIC",
        "required_stratum_or_scope": "SYNTHETIC_TEST_SCOPE",
        "estimand": "SYNTHETIC_ESTIMAND",
        "unit_of_analysis": "SYNTHETIC_UNIT",
        "decision_role": "HARD_GATE",
        "threshold_policy_id_or_explicit_not_applicable": threshold_id,
        "precision_or_power_objective": {"synthetic": True},
        "confidence_or_error_rate_parameters": {"synthetic": True},
        "anticipated_rate_variance_or_other_nuisance_inputs": {"synthetic": True},
        "source_and_provenance_for_planning_inputs": ["PROV-SYNTHETIC"],
        "pairing_or_cluster_dependency_model": "PAIRED_ROOT_CASE_DEPENDENCY",
        "multiplicity_structure": {"declaration": "SYNTHETIC"},
        "planned_numeric_n": 10,
        "coverage_allocation_design": {"synthetic": 10},
        "rounding_or_allocation_rule": "SYNTHETIC_RULE",
        "software_formula_or_method_identity": "SYNTHETIC_METHOD_V1",
        "sensitivity_analysis_identity_or_explicit_not_required": "EXPLICIT_NOT_REQUIRED",
        "candidate_neutral": True,
        "pre_result_freeze": True,
        "record_canonical_sha256": "b" * 64,
    }


def make_ready_records(metrics_v2):
    metric_id, role = first_selection_metric(metrics_v2)
    thresholds = [
        make_threshold(metrics_v2, lane=lane, policy_id=f"TP-{index}")
        for index, lane in enumerate(SEVEN_LANES)
    ]
    designs = [
        make_design(lane, f"TP-{index}", f"SD-{index}")
        for index, lane in enumerate(SEVEN_LANES)
    ]
    mappings = [
        {
            "lane_id": lane,
            "metric_id": metric_id,
            "metric_evidence_role": role,
            "metric_direction": "HIGHER_BETTER",
        }
        for lane in SEVEN_LANES
    ]
    return {
        "lane_metric_mappings": mappings,
        "threshold_policies": thresholds,
        "statistical_designs": designs,
    }


class FD009ThresholdPolicyTests(unittest.TestCase):
    def setUp(self):
        self.metrics = make_metrics_v2()
        self.quality = make_quality_contract()

    def test_exact_non_human_policy_authorities_validate(self):
        errors = validate_fd009_threshold_policy(
            make_threshold(self.metrics), self.quality, self.metrics
        )
        self.assertEqual(errors, [])

    def test_legacy_reviewer_like_authority_does_not_substitute(self):
        record = make_threshold(
            self.metrics,
            clinical_review_authority_reference="REV-AUTH-1",
            statistical_review_authority_reference="REV-AUTH-2",
        )
        errors = validate_fd009_threshold_policy(record, self.quality, self.metrics)
        self.assertTrue(any("FD009_NON_HUMAN_POLICY" in error for error in errors))

    def test_missing_clinical_evidence_fails_closed(self):
        record = make_threshold(self.metrics, clinical_meaningfulness_evidence_ids=[])
        errors = validate_fd009_threshold_policy(record, self.quality, self.metrics)
        self.assertTrue(any("clinical_meaningfulness_evidence_ids" in e for e in errors))

    def test_missing_statistical_evidence_fails_closed(self):
        record = make_threshold(self.metrics, statistical_justification_evidence_ids=[])
        errors = validate_fd009_threshold_policy(record, self.quality, self.metrics)
        self.assertTrue(any("statistical_justification_evidence_ids" in e for e in errors))

    def test_threshold_value_remains_mandatory(self):
        record = make_threshold(self.metrics)
        del record["threshold_value_or_margin"]
        errors = validate_fd009_threshold_policy(record, self.quality, self.metrics)
        self.assertTrue(any("MISSING_THRESHOLD_VALUE_OR_MARGIN" in e for e in errors))

    def test_pre_result_freeze_remains_mandatory(self):
        record = make_threshold(self.metrics, pre_result_freeze=False)
        errors = validate_fd009_threshold_policy(record, self.quality, self.metrics)
        self.assertTrue(any("pre_result_freeze" in e for e in errors))


class FD009ReadinessTests(unittest.TestCase):
    def test_ready_records_require_fd009_policy(self):
        metrics = make_metrics_v2()
        result = evaluate_fd009_scientific_selection_readiness(
            make_ready_records(metrics), make_quality_contract(), metrics
        )
        self.assertEqual(result["policy_id"], FD009_POLICY_ID)
        self.assertEqual(result["state"], "READY_FOR_PRECONSTRUCTION")
        self.assertEqual(result["reason_codes"], [])

    def test_one_legacy_authority_blocks_global_readiness(self):
        metrics = make_metrics_v2()
        records = make_ready_records(metrics)
        records["threshold_policies"][3]["clinical_review_authority_reference"] = (
            "HUMAN-REVIEWER-PLACEHOLDER"
        )
        result = evaluate_fd009_scientific_selection_readiness(
            records, make_quality_contract(), metrics
        )
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(any("FD009_NON_HUMAN_POLICY" in c for c in result["reason_codes"]))

    def test_incomplete_evidence_still_blocks_global_readiness(self):
        metrics = make_metrics_v2()
        records = make_ready_records(metrics)
        records["threshold_policies"][0]["statistical_justification_evidence_ids"] = []
        result = evaluate_fd009_scientific_selection_readiness(
            records, make_quality_contract(), metrics
        )
        self.assertEqual(result["state"], "INCOMPLETE")
        self.assertTrue(result["reason_codes"])


if __name__ == "__main__":
    unittest.main()
