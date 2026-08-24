"""US2 fixture tests: scientific selection quality, thresholds, A3+A4 design.

Synthetic, non-medical fixtures only. No threshold/N values are asserted as
scientifically correct; only structural/fail-closed contract behavior.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec005.science import (
    evaluate_scientific_selection_readiness,
    validate_selection_quality_contract,
    validate_statistical_design,
    validate_threshold_policy,
)

ROOT = Path(__file__).resolve().parents[2]
QUALITY_CONTRACT_PATH = ROOT / "data/spec005/selection_quality_contract.json"
METRICS_V2_PATH = ROOT / "data/eval/metrics-v2.json"
V1_SHA = "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a"

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


def make_quality_contract(**overrides):
    contract = load_json(QUALITY_CONTRACT_PATH)
    contract.update(overrides)
    return contract


def make_metrics_v2():
    return load_json(METRICS_V2_PATH)


def first_metric_id(metrics_v2):
    return metrics_v2["metrics"][0]["metric_id"]


def metric_with_role(metrics_v2, role):
    for metric in metrics_v2["metrics"]:
        roles = {
            entry["evidence_role"]
            for entry in metric.get("evidence_requirements", [])
        }
        if role in roles:
            return metric["metric_id"]
    raise AssertionError(f"no metric with role {role}")


def make_lane_mapping(metrics_v2, lane, role="SELECTION_DEV"):
    return {
        "lane_id": lane,
        "metric_id": metric_with_role(metrics_v2, role),
        "metric_evidence_role": role,
        "metric_direction": "HIGHER_BETTER",
    }


def make_threshold_record(metrics_v2, **overrides):
    record = {
        "threshold_policy_id": "TP-001",
        "threshold_policy_version": "1.0",
        "metric_id": first_metric_id(metrics_v2),
        "metric_evidence_role": "SELECTION_DEV",
        "lane_id": SEVEN_LANES[0],
        "required_stratum_or_scope": "OVERALL",
        "estimand_id": "EST-001",
        "metric_direction": "HIGHER_BETTER",
        "decision_role": "RANKING",
        "threshold_kind": "ABSOLUTE_THRESHOLD",
        "threshold_value_or_margin": 0.65,
        "unit_or_scale": "SCORE_0_1",
        "clinical_meaningfulness_evidence_ids": ["EV-CLIN-1"],
        "statistical_justification_evidence_ids": ["EV-STAT-1"],
        "clinical_review_authority_reference": "REV-AUTH-1",
        "statistical_review_authority_reference": "REV-AUTH-2",
        "conflict_disposition_record_ids": [],
        "pre_result_freeze": True,
        "record_canonical_sha256": "a" * 64,
    }
    record.update(overrides)
    return record


def make_statistical_design(**overrides):
    design = {
        "statistical_design_id": "SD-001",
        "design_version": "1.0",
        "quality_lane": SEVEN_LANES[4],
        "metric_id_or_metric_mapping_id": "MM-001",
        "required_stratum_or_scope": "ALL_ANCHORS_PAIRED",
        "estimand": "MEAN_PAIRED_DIFFERENCE",
        "unit_of_analysis": "PAIRED_ROOT_CASE",
        "decision_role": "RANKING",
        "threshold_policy_id_or_explicit_not_applicable": "TP-001",
        "precision_or_power_objective": {"target_power": 0.8},
        "confidence_or_error_rate_parameters": {"alpha": 0.05},
        "anticipated_rate_variance_or_other_nuisance_inputs": {
            "nuisance_source_ids": ["NUIS-1"]
        },
        "source_and_provenance_for_planning_inputs": ["PROV-1"],
        "pairing_or_cluster_dependency_model": "PAIRED_ROOT_CASE_DEPENDENCY",
        "multiplicity_structure": {"declaration": "HOLM_ACROSS_LANES"},
        "planned_numeric_n": 240,
        "coverage_allocation_design": {"per_anchor_pairs": 48},
        "rounding_or_allocation_rule": "CEILING_PER_STRATUM",
        "software_formula_or_method_identity": "FORMULA-IDENTITY-1",
        "sensitivity_analysis_identity_or_explicit_not_required": "SENS-1",
        "candidate_neutral": True,
        "pre_result_freeze": True,
        "record_canonical_sha256": "b" * 64,
    }
    design.update(overrides)
    return design


class SelectionQualityContractTests(unittest.TestCase):
    def test_canonical_contract_validates(self):
        errors = validate_selection_quality_contract(
            make_quality_contract(), make_metrics_v2()
        )
        self.assertEqual(errors, [])

    def test_missing_required_lane_fails(self):
        contract = make_quality_contract()
        contract["required_quality_lanes"] = SEVEN_LANES[:-1]
        errors = validate_selection_quality_contract(contract, make_metrics_v2())
        self.assertTrue(any("lane" in e.lower() for e in errors))

    def test_unknown_lane_fails_closed(self):
        contract = make_quality_contract()
        contract["required_quality_lanes"] = SEVEN_LANES + ["Z_UNKNOWN_LANE"]
        errors = validate_selection_quality_contract(contract, make_metrics_v2())
        self.assertTrue(any("Z_UNKNOWN_LANE" in e for e in errors))

    def test_duplicate_lane_rejected(self):
        contract = make_quality_contract(
            required_quality_lanes=SEVEN_LANES + [SEVEN_LANES[0]]
        )
        errors = validate_selection_quality_contract(contract, make_metrics_v2())
        self.assertTrue(any("DUPLICATE" in e.upper() for e in errors))

    def test_non_arabic_language_scope_fails(self):
        contract = make_quality_contract()
        contract["required_language_scope"] = ["en"]
        errors = validate_selection_quality_contract(contract, make_metrics_v2())
        self.assertTrue(any("LANGUAGE_SCOPE" in e for e in errors))

    def test_missing_coverage_anchor_fails(self):
        contract = make_quality_contract()
        contract["required_arabic_coverage_anchors"] = contract[
            "required_arabic_coverage_anchors"
        ][:4]
        errors = validate_selection_quality_contract(contract, make_metrics_v2())
        self.assertTrue(any("anchor" in e.lower() for e in errors))

    def test_private_gold_role_cannot_map_lanes(self):
        contract = make_quality_contract()
        contract["metric_mapping_requirements"]["allowed_evidence_roles_for_lane_mapping"].append(
            "PRIVATE_GOLD_FINAL_AUDIT"
        )
        errors = validate_selection_quality_contract(
            contract, make_metrics_v2()
        )
        self.assertTrue(any("PRIVATE_GOLD" in e for e in errors))


class ThresholdPolicyTests(unittest.TestCase):
    def test_complete_threshold_record_validates(self):
        errors = validate_threshold_policy(
            make_threshold_record(make_metrics_v2()),
            make_quality_contract(),
            make_metrics_v2(),
        )
        self.assertEqual(errors, [])

    def test_missing_threshold_value_blocks(self):
        record = make_threshold_record(make_metrics_v2())
        del record["threshold_value_or_margin"]
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("INCOMPLETE" in e or "BLOCKED" in e for e in errors))

    def test_unknown_metric_blocked(self):
        record = make_threshold_record(make_metrics_v2(), metric_id="NO_SUCH_METRIC")
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("NO_SUCH_METRIC" in e for e in errors))

    def test_unknown_lane_blocked(self):
        record = make_threshold_record(make_metrics_v2(), lane_id="X_NOPE")
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("X_NOPE" in e for e in errors))

    def test_private_gold_metric_role_rejected(self):
        record = make_threshold_record(
            make_metrics_v2(), metric_evidence_role="PRIVATE_GOLD_FINAL_AUDIT"
        )
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("PRIVATE_GOLD" in e for e in errors))

    def test_post_result_freeze_false_rejected(self):
        record = make_threshold_record(make_metrics_v2(), pre_result_freeze=False)
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("pre_result_freeze" in e for e in errors))

    def test_missing_review_authority_blocks(self):
        record = make_threshold_record(make_metrics_v2())
        record["clinical_review_authority_reference"] = ""
        errors = validate_threshold_policy(
            record, make_quality_contract(), make_metrics_v2()
        )
        self.assertTrue(any("review" in e.lower() for e in errors))

    def test_malformed_input_does_not_raise(self):
        for bad in (None, [], "x", 42):
            errors = validate_threshold_policy(
                bad, make_quality_contract(), make_metrics_v2()
            )
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class StatisticalDesignTests(unittest.TestCase):
    def setUp(self):
        self.quality = make_quality_contract()
        self.metrics_v2 = make_metrics_v2()
        self.thresholds = [make_threshold_record(self.metrics_v2)]

    def test_complete_design_validates(self):
        errors = validate_statistical_design(
            make_statistical_design(), self.thresholds, self.quality
        )
        self.assertEqual(errors, [])

    def test_missing_n_blocks(self):
        design = make_statistical_design()
        del design["planned_numeric_n"]
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("planned_numeric_n" in e for e in errors))

    def test_missing_allocation_blocks(self):
        design = make_statistical_design()
        del design["coverage_allocation_design"]
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("coverage_allocation_design" in e for e in errors))

    def test_unpaired_arabic_shortcut_rejected(self):
        design = make_statistical_design(
            pairing_or_cluster_dependency_model="INDEPENDENT_TWO_SAMPLE_UNPAIRED"
        )
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(
            any("paired" in e.lower() or "unpaired" in e.lower() for e in errors)
        )

    def test_candidate_neutrality_required(self):
        design = make_statistical_design(candidate_neutral=False)
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("candidate_neutral" in e for e in errors))

    def test_post_result_freeze_false_rejected(self):
        design = make_statistical_design(pre_result_freeze=False)
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("pre_result_freeze" in e for e in errors))

    def test_unknown_lane_rejected(self):
        design = make_statistical_design(quality_lane="Q_UNKNOWN")
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("Q_UNKNOWN" in e for e in errors))

    def test_multiplicity_declaration_required(self):
        design = make_statistical_design()
        del design["multiplicity_structure"]
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        self.assertTrue(any("multiplicity" in e.lower() for e in errors))

    def test_malformed_input_does_not_raise(self):
        for bad in (None, "x", 7, []):
            errors = validate_statistical_design(bad, self.thresholds, self.quality)
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)

    def test_caller_pass_claim_not_trusted(self):
        design = make_statistical_design(design_state="PASS", powered=True)
        errors = validate_statistical_design(design, self.thresholds, self.quality)
        # Extra claim fields are ignored; validation outcome is evidence-based.
        self.assertEqual(errors, [])


class ScientificReadinessTests(unittest.TestCase):
    def test_ready_when_all_records_present_and_valid(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        mappings = [
            make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES
        ]
        records = {
            "lane_metric_mappings": mappings,
            "threshold_policies": [
                make_threshold_record(metrics_v2, lane_id=lane,
                                      threshold_policy_id=f"TP-{lane}")
                for lane in SEVEN_LANES
            ],
            "statistical_designs": [
                make_statistical_design(
                    quality_lane=lane,
                    statistical_design_id=f"SD-{lane}",
                    threshold_policy_id_or_explicit_not_applicable=f"TP-{lane}",
                )
                for lane in SEVEN_LANES
            ],
        }
        result = evaluate_scientific_selection_readiness(
            records, quality, metrics_v2
        )
        self.assertEqual(result["state"], "READY_FOR_PRECONSTRUCTION")
        self.assertEqual(result["reason_codes"], [])

    def test_incomplete_mapping_yields_incomplete(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        records = {
            "lane_metric_mappings": [
                make_lane_mapping(metrics_v2, SEVEN_LANES[0])
            ],
            "threshold_policies": [],
            "statistical_designs": [],
        }
        result = evaluate_scientific_selection_readiness(
            records, quality, metrics_v2
        )
        self.assertIn(
            result["state"], {"INCOMPLETE", "BLOCKED"}
        )
        self.assertTrue(result["reason_codes"])

    def test_failed_lane_is_not_compensated_by_others(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        mappings = [
            make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES
        ]
        broken = dict(mappings[1])
        broken["metric_id"] = "NO_SUCH_METRIC"
        mappings[1] = broken
        records = {
            "lane_metric_mappings": mappings,
            "threshold_policies": [make_threshold_record(metrics_v2)],
            "statistical_designs": [make_statistical_design()],
        }
        result = evaluate_scientific_selection_readiness(
            records, quality, metrics_v2
        )
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")

    def test_malformed_records_fail_closed(self):
        result = evaluate_scientific_selection_readiness(
            None, make_quality_contract(), make_metrics_v2()
        )
        self.assertIn(result["state"], {"INCOMPLETE", "BLOCKED"})
        self.assertTrue(result["reason_codes"])

    def test_per_lane_threshold_and_design_coverage_required(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        mappings = [make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES]
        thresholds = [
            make_threshold_record(metrics_v2, lane_id=lane) for lane in SEVEN_LANES
        ]
        designs = [
            make_statistical_design(
                quality_lane=lane,
                statistical_design_id=f"SD-{lane}",
                threshold_policy_id_or_explicit_not_applicable=f"TP-{lane}",
            )
            for lane in SEVEN_LANES
        ]
        full = {
            "lane_metric_mappings": mappings,
            "threshold_policies": thresholds,
            "statistical_designs": designs,
        }
        result = evaluate_scientific_selection_readiness(full, quality, metrics_v2)
        self.assertEqual(result["state"], "READY_FOR_PRECONSTRUCTION")

        partial = dict(full)
        partial["threshold_policies"] = thresholds[:6]
        result = evaluate_scientific_selection_readiness(partial, quality, metrics_v2)
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")

        partial = dict(full)
        partial["statistical_designs"] = designs[:6]
        result = evaluate_scientific_selection_readiness(partial, quality, metrics_v2)
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")

    def test_duplicate_lane_records_rejected(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        mappings = [make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES]
        thresholds = [
            make_threshold_record(
                metrics_v2, lane_id=lane, threshold_policy_id=f"TP-{lane}"
            )
            for lane in SEVEN_LANES
        ]
        thresholds.append(
            make_threshold_record(
                metrics_v2,
                lane_id=SEVEN_LANES[0],
                threshold_policy_id="TP-DUP",
            )
        )
        designs = [
            make_statistical_design(
                quality_lane=lane,
                statistical_design_id=f"SD-{lane}",
                threshold_policy_id_or_explicit_not_applicable=f"TP-{lane}",
            )
            for lane in SEVEN_LANES
        ]
        records = {
            "lane_metric_mappings": mappings,
            "threshold_policies": thresholds,
            "statistical_designs": designs,
        }
        result = evaluate_scientific_selection_readiness(records, quality, metrics_v2)
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")
        self.assertTrue(
            any("DUPLICATE" in c.upper() and "LANE" in c.upper()
                for c in result["reason_codes"])
        )

    def test_design_threshold_binding_validated(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        mappings = [make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES]
        thresholds = [
            make_threshold_record(
                metrics_v2, lane_id=lane, threshold_policy_id=f"TP-{lane}"
            )
            for lane in SEVEN_LANES
        ]
        designs = [
            make_statistical_design(
                quality_lane=lane,
                statistical_design_id=f"SD-{lane}",
                threshold_policy_id_or_explicit_not_applicable="TP-UNKNOWN",
            )
            for lane in SEVEN_LANES
        ]
        records = {
            "lane_metric_mappings": mappings,
            "threshold_policies": thresholds,
            "statistical_designs": designs,
        }
        result = evaluate_scientific_selection_readiness(records, quality, metrics_v2)
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")
        self.assertTrue(
            any("THRESHOLD_POLICY_ID_OR_EXPLICIT_NOT_APPLICABLE" in c
                for c in result["reason_codes"])
        )

    def test_malformed_inputs_fail_closed_not_crash(self):
        for bad in ([], "x", 42):
            result = evaluate_scientific_selection_readiness({}, bad, make_metrics_v2())
            self.assertIn(result["state"], {"INCOMPLETE", "BLOCKED"})
            result = evaluate_scientific_selection_readiness(
                {}, make_quality_contract(), bad
            )
            self.assertIn(result["state"], {"INCOMPLETE", "BLOCKED"})

    def test_design_and_threshold_lane_bindings_validated(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        records = {
            "lane_metric_mappings": [
                make_lane_mapping(metrics_v2, lane) for lane in SEVEN_LANES
            ],
            "threshold_policies": [
                make_threshold_record(metrics_v2, lane_id="Q_UNKNOWN_LANE")
            ],
            "statistical_designs": [],
        }
        result = evaluate_scientific_selection_readiness(records, quality, metrics_v2)
        self.assertNotEqual(result["state"], "READY_FOR_PRECONSTRUCTION")

    def test_reason_codes_sorted_deterministic(self):
        metrics_v2 = make_metrics_v2()
        quality = make_quality_contract()
        result = evaluate_scientific_selection_readiness(
            {}, quality, metrics_v2
        )
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


if __name__ == "__main__":
    unittest.main()
