from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.eval_contract.model import GateEvaluationState
from src.commandmed.eval_contract.safety import (
    evaluate_safety_sentinel,
    evaluate_truth_boundary_fixture,
    resolve_gate_applicability,
    validate_evaluation_scope,
    validate_safety_policy,
)
from src.commandmed.eval_contract.validate import evaluate_hard_gates

POLICY_PATH = Path(__file__).parents[2] / "data" / "eval" / "safety_policy.json"
METRICS_PATH = Path(__file__).parents[2] / "data" / "eval" / "metrics.json"


def policy() -> dict:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def system_scope() -> dict:
    return {
        "scope_id": "system-text-safety-v1",
        "scope_kind": "SYSTEM_QUALIFICATION",
        "claimed_capabilities": ["ARABIC_CLINICAL", "PATIENT_CAREGIVER_SAFETY", "EVIDENCE_GROUNDED_CLINICAL"],
        "out_of_scope_capabilities": ["LAB_DOCUMENT"],
    }


def component_scope() -> dict:
    return {
        "scope_id": "component-evidence-v1",
        "scope_kind": "COMPONENT_QUALIFICATION",
        "claimed_capabilities": ["EVIDENCE_GROUNDED_CLINICAL"],
        "out_of_scope_capabilities": ["ARABIC_CLINICAL", "PATIENT_CAREGIVER_SAFETY", "LAB_DOCUMENT"],
    }


class SafetyPolicyValidationTests(unittest.TestCase):
    def test_canonical_policy_valid(self):
        self.assertEqual(validate_safety_policy(policy()), [])

    def test_non_object_policy_fails_cleanly(self):
        self.assertTrue(validate_safety_policy(None)); self.assertTrue(validate_safety_policy([]))

    def test_unknown_behavior_state_fails(self):
        p = policy(); p["behavior_states"][0] = "GUESS"; self.assertTrue(validate_safety_policy(p))

    def test_duplicate_rule_id_fails(self):
        p = policy(); p["precedence_rules"][1]["rule_id"] = p["precedence_rules"][0]["rule_id"]
        self.assertTrue(validate_safety_policy(p))

    def test_missing_trigger_class_fails(self):
        p = policy(); p["precedence_rules"] = p["precedence_rules"][:-1]
        self.assertTrue(any("missing canonical trigger" in e for e in validate_safety_policy(p)))

    def test_forced_emergency_must_prohibit_all_non_emergency_states(self):
        p = policy(); p["precedence_rules"][0]["prohibited_lower_states"].remove("ANSWER")
        self.assertTrue(any("must prohibit every non-EMERGENCY state" in e for e in validate_safety_policy(p)))

    def test_truth_boundary_cannot_allow_generative_substitution(self):
        p = policy(); p["truth_boundaries"][0]["generative_substitution"] = "ALLOWED"
        self.assertTrue(validate_safety_policy(p))

    def test_missing_truth_boundary_task_class_fails(self):
        p = policy(); p["truth_boundaries"] = p["truth_boundaries"][:-1]
        self.assertTrue(any("missing canonical task classes" in e for e in validate_safety_policy(p)))

    def test_duplicate_truth_boundary_task_class_fails(self):
        p = policy(); p["truth_boundaries"][1]["task_class"] = p["truth_boundaries"][0]["task_class"]
        self.assertTrue(any("duplicate canonical task class" in e for e in validate_safety_policy(p)))

    def test_unavailable_truth_boundary_cannot_fallback_to_answer(self):
        p = policy(); p["truth_boundaries"][0]["allowed_unavailable_fallback_states"].append("ANSWER")
        self.assertTrue(validate_safety_policy(p))

    def test_all_spec001_hard_gates_must_be_mapped(self):
        p = policy(); p["gate_contracts"] = p["gate_contracts"][:-1]
        self.assertTrue(any("missing hard-gate mappings" in e for e in validate_safety_policy(p)))

    def test_hard_gate_capability_mapping_cannot_be_relabelled(self):
        p = policy(); gate = next(g for g in p["gate_contracts"] if g["metric_id"] == "arabic_clinical_parity_gap")
        gate["capability_claim_id"] = "LAB_DOCUMENT"
        self.assertTrue(any("must map to 'ARABIC_CLINICAL'" in e for e in validate_safety_policy(p)))

    def test_hard_gate_policy_class_cannot_be_weakened(self):
        p = policy(); gate = next(g for g in p["gate_contracts"] if g["metric_id"] == "emergency_miss_rate")
        gate["threshold_class"] = "PENDING_CLINICAL_EVIDENCE"
        self.assertTrue(any("must use canonical policy class" in e for e in validate_safety_policy(p)))

    def test_every_hard_gate_must_apply_to_system_qualification(self):
        p = policy(); p["gate_contracts"][0]["required_scope_kinds"] = ["COMPONENT_QUALIFICATION"]
        self.assertTrue(any("must apply to SYSTEM_QUALIFICATION" in e for e in validate_safety_policy(p)))

    def test_pending_gate_contract_is_fully_fail_closed(self):
        p = policy(); gate = next(g for g in p["gate_contracts"] if g["metric_id"] == "selective_risk_at_target_coverage")
        gate["fail_condition"] = "IGNORE_PENDING"
        self.assertTrue(any("NO_PASS_UNTIL_FROZEN/PENDING_OR_UNSUPPORTED" in e for e in validate_safety_policy(p)))

    def test_gate_evidence_kind_matches_threshold_class(self):
        p = policy(); gate = next(g for g in p["gate_contracts"] if g["metric_id"] == "emergency_miss_rate")
        gate["required_evidence_kind"] = "IDENTITY_BOUND_CLINICAL_EVIDENCE"
        self.assertTrue(any("requires IDENTITY_BOUND_SENTINEL_EVIDENCE" in e for e in validate_safety_policy(p)))

    def test_pending_threshold_cannot_be_passable(self):
        p = policy(); p["statistical_threshold_requirements"][0]["pass_allowed"] = True
        self.assertTrue(validate_safety_policy(p))

    def test_pending_threshold_cannot_smuggle_numeric_value(self):
        p = policy(); p["statistical_threshold_requirements"][0]["threshold_value"] = 0.01
        self.assertTrue(any("must not contain a frozen numeric/operator value" in e for e in validate_safety_policy(p)))

    def test_pending_threshold_requires_core_provenance(self):
        p = policy(); p["statistical_threshold_requirements"][0]["required_before_freeze"].remove("CLINICAL_REVIEW_AUTHORITY")
        self.assertTrue(any("missing core prerequisites" in e for e in validate_safety_policy(p)))

    def test_all_required_statistical_threshold_records_must_exist(self):
        p = policy(); p["statistical_threshold_requirements"] = p["statistical_threshold_requirements"][:-1]
        self.assertTrue(any("missing required metrics" in e for e in validate_safety_policy(p)))

    def test_unknown_statistical_metric_fails(self):
        p = policy(); extra = copy.deepcopy(p["statistical_threshold_requirements"][0]); extra["metric_id"] = "made_up_safety_metric"
        p["statistical_threshold_requirements"].append(extra); self.assertTrue(validate_safety_policy(p))

    def test_benign_overtriage_must_remain_bound_to_fd004(self):
        p = policy(); req = next(r for r in p["statistical_threshold_requirements"] if r["metric_id"] == "benign_case_over_triage_rate")
        req["founder_decision_id"] = "FD-999"
        self.assertTrue(any("must remain bound to FD-004" in e for e in validate_safety_policy(p)))

    def test_malformed_scalar_tokens_and_freeze_lists_fail_without_exception(self):
        mutations = []
        for label, section, field, bad in (
            ("trigger", "precedence_rules", "trigger_class", []),
            ("required_state", "precedence_rules", "required_state", {}),
            ("rule_evidence", "precedence_rules", "evidence_requirement", 7),
            ("task_class", "truth_boundaries", "task_class", []),
            ("mechanism_class", "truth_boundaries", "mechanism_class", {}),
            ("metric_id", "gate_contracts", "metric_id", []),
            ("threshold_class", "gate_contracts", "threshold_class", {}),
            ("capability_claim", "gate_contracts", "capability_claim_id", []),
            ("gate_evidence", "gate_contracts", "required_evidence_kind", {}),
            ("threshold_state", "statistical_threshold_requirements", "state", []),
        ):
            mutations.append((label, section, field, bad))
        for label, section, field, bad in mutations:
            with self.subTest(label=label):
                p = policy(); p[section][0][field] = bad
                self.assertTrue(validate_safety_policy(p))
        p = policy(); p["statistical_threshold_requirements"][0]["required_before_freeze"] = [{}]
        self.assertTrue(validate_safety_policy(p))


class SafetyScopeTests(unittest.TestCase):
    def test_system_scope_valid_with_lab_explicitly_out_of_scope(self):
        self.assertEqual(validate_evaluation_scope(policy(), system_scope()), [])

    def test_system_scope_cannot_waive_arabic(self):
        scope = system_scope(); scope["claimed_capabilities"].remove("ARABIC_CLINICAL"); scope["out_of_scope_capabilities"].append("ARABIC_CLINICAL")
        self.assertTrue(any("SYSTEM_QUALIFICATION must claim" in e for e in validate_evaluation_scope(policy(), scope)))

    def test_component_scope_can_mark_unclaimed_capability_na(self):
        state, errors = resolve_gate_applicability(policy(), "arabic-clinical-parity-statistical-gate-v1", component_scope())
        self.assertEqual(errors, []); self.assertEqual(state, "NOT_APPLICABLE_TO_DECLARED_SCOPE")

    def test_claimed_component_gate_is_applicable(self):
        state, errors = resolve_gate_applicability(policy(), "citation-evidence-sentinel-gate-v1", component_scope())
        self.assertEqual(errors, []); self.assertEqual(state, "APPLICABLE")

    def test_scope_must_explicitly_classify_every_known_capability(self):
        scope = component_scope(); scope["out_of_scope_capabilities"].remove("LAB_DOCUMENT")
        self.assertTrue(any("every capability" in e for e in validate_evaluation_scope(policy(), scope)))

    def test_scope_cannot_claim_and_exclude_same_capability(self):
        scope = component_scope(); scope["claimed_capabilities"].append("LAB_DOCUMENT")
        self.assertTrue(any("both claimed and out-of-scope" in e for e in validate_evaluation_scope(policy(), scope)))

    def test_malformed_claimed_capability_collection_fails_without_exception(self):
        scope = component_scope(); scope["claimed_capabilities"] = [{}]
        errors = validate_evaluation_scope(policy(), scope)
        self.assertTrue(errors); self.assertTrue(any("claimed_capabilities[0]" in e for e in errors))

    def test_malformed_excluded_capability_collection_fails_without_exception(self):
        scope = component_scope(); scope["out_of_scope_capabilities"] = [["LAB_DOCUMENT"]]
        errors = validate_evaluation_scope(policy(), scope)
        self.assertTrue(errors); self.assertTrue(any("out_of_scope_capabilities[0]" in e for e in errors))

    def test_malformed_scope_kind_fails_without_exception(self):
        scope = component_scope(); scope["scope_kind"] = []
        self.assertTrue(validate_evaluation_scope(policy(), scope))


class SafetySentinelTests(unittest.TestCase):
    def fixture(self, rule_id: str, observed_state: str) -> dict:
        return {"fixture_id":"sentinel-001","rule_id":rule_id,"observed_state":observed_state,"evidence_artifact_id":"sha256:sentinel-evidence-001"}

    def test_required_emergency_exact_state_passes_with_zero_violations(self):
        result = evaluate_safety_sentinel(policy(), self.fixture("forced-emergency-non-override-v1", "EMERGENCY"))
        self.assertEqual(result["status"], GateEvaluationState.PASS.value); self.assertEqual(result["score"], 0); self.assertTrue(result["evidence_artifact_id"])

    def test_required_emergency_answer_fails(self):
        result = evaluate_safety_sentinel(policy(), self.fixture("forced-emergency-non-override-v1", "ANSWER"))
        self.assertEqual(result["status"], GateEvaluationState.FAIL.value); self.assertEqual(result["score"], 1)

    def test_required_escalate_emergency_is_not_silently_counted_as_exact_pass(self):
        result = evaluate_safety_sentinel(policy(), self.fixture("forced-escalation-non-override-v1", "EMERGENCY"))
        self.assertEqual(result["status"], GateEvaluationState.FAIL.value); self.assertEqual(result["score"], 1)

    def test_missing_critical_information_answer_fails(self):
        result = evaluate_safety_sentinel(policy(), self.fixture("missing-critical-information-blocks-answer-v1", "ANSWER"))
        self.assertEqual(result["status"], GateEvaluationState.FAIL.value)

    def test_missing_evidence_cannot_pass(self):
        fixture = self.fixture("forced-emergency-non-override-v1", "EMERGENCY"); fixture["evidence_artifact_id"] = "UNRESOLVED"
        result = evaluate_safety_sentinel(policy(), fixture)
        self.assertEqual(result["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value); self.assertIsNone(result["score"])

    def test_unknown_rule_cannot_pass(self):
        result = evaluate_safety_sentinel(policy(), self.fixture("unknown-rule", "EMERGENCY"))
        self.assertEqual(result["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value)

    def test_malformed_observed_state_fails_without_exception(self):
        fixture = self.fixture("forced-emergency-non-override-v1", "EMERGENCY"); fixture["observed_state"] = []
        self.assertEqual(evaluate_safety_sentinel(policy(), fixture)["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value)


class TruthBoundaryFixtureTests(unittest.TestCase):
    def base_fixture(self) -> dict:
        return {
            "fixture_id":"truth-fixture-001","boundary_id":"arithmetic-truth-boundary-v1","evidence_artifact_id":"sha256:truth-evidence-001",
            "mechanism_available":True,"used_generative_substitution":False,"observed_state":"ANSWER",
            "result_identity":{"mechanism_id":"stdlib-decimal","mechanism_revision":"py311-v1","result_digest":"sha256:typed-result-001"},
            "authoritative_result":{"value":"2.0","unit":"mg"},"reported_result":{"value":"2.0","unit":"mg"},
        }

    def test_identity_bound_result_preserved_passes(self):
        result = evaluate_truth_boundary_fixture(policy(), self.base_fixture())
        self.assertEqual(result["status"], GateEvaluationState.PASS.value); self.assertEqual(result["score"], 0)

    def test_generative_substitution_fails(self):
        fixture = self.base_fixture(); fixture["used_generative_substitution"] = True
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.FAIL.value)

    def test_altered_deterministic_result_fails(self):
        fixture = self.base_fixture(); fixture["reported_result"] = {"value":"20.0","unit":"mg"}
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.FAIL.value)

    def test_altered_unit_fails(self):
        fixture = self.base_fixture(); fixture["reported_result"] = {"value":"2.0","unit":"g"}
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.FAIL.value)

    def test_missing_result_identity_is_insufficient_evidence(self):
        fixture = self.base_fixture(); del fixture["result_identity"]["result_digest"]
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value)

    def test_unavailable_mechanism_with_safe_fallback_passes_contract_fixture(self):
        fixture = self.base_fixture(); fixture["mechanism_available"] = False; fixture["observed_state"] = "ABSTAIN"
        fixture.pop("result_identity"); fixture.pop("authoritative_result"); fixture.pop("reported_result")
        result = evaluate_truth_boundary_fixture(policy(), fixture)
        self.assertEqual(result["status"], GateEvaluationState.PASS.value); self.assertEqual(result["score"], 0)

    def test_unavailable_mechanism_with_answer_fails(self):
        fixture = self.base_fixture(); fixture["mechanism_available"] = False; fixture["observed_state"] = "ANSWER"
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.FAIL.value)

    def test_missing_or_unresolved_fixture_identity_is_insufficient_evidence(self):
        for marker in (None, "UNRESOLVED"):
            with self.subTest(marker=marker):
                fixture = self.base_fixture()
                if marker is None:
                    fixture.pop("fixture_id")
                else:
                    fixture["fixture_id"] = marker
                result = evaluate_truth_boundary_fixture(policy(), fixture)
                self.assertEqual(result["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value)
                self.assertIsNone(result["score"])

    def test_malformed_observed_state_fails_without_exception(self):
        fixture = self.base_fixture(); fixture["observed_state"] = {}
        self.assertEqual(evaluate_truth_boundary_fixture(policy(), fixture)["status"], GateEvaluationState.INSUFFICIENT_EVIDENCE.value)


class SafetyHardGateIntegrationTests(unittest.TestCase):
    def test_sentinel_failure_routes_through_existing_hard_gate_evaluator(self):
        metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
        results = {
            metric["metric_id"]: {
                "status": GateEvaluationState.PASS.value,
                "score": 0.0,
                "evidence_artifact_id": f"fixture:{metric['metric_id']}",
            }
            for metric in metrics
            if metric.get("is_hard_gate") is True
        }
        results["emergency_miss_rate"] = evaluate_safety_sentinel(
            policy(),
            {
                "fixture_id": "sentinel-integration-001",
                "rule_id": "forced-emergency-non-override-v1",
                "observed_state": "ANSWER",
                "evidence_artifact_id": "fixture:sentinel-integration-001",
            },
        )
        overall, breakdown = evaluate_hard_gates(metrics, results)
        self.assertEqual(overall, GateEvaluationState.FAIL.value)
        self.assertTrue(any(g["metric_id"] == "emergency_miss_rate" and g["status"] == GateEvaluationState.FAIL.value for g in breakdown))


class SafetyPolicyCanonicalIdentityTests(unittest.TestCase):
    def test_representation_only_reordering_preserves_policy_digest(self):
        original = policy(); reordered = copy.deepcopy(original)
        for key in ("behavior_states","scope_kinds","precedence_rules","truth_boundaries","gate_contracts","statistical_threshold_requirements"): reordered[key].reverse()
        reordered["truth_boundaries"][0]["applicable_roles"].reverse()
        self.assertEqual(compute_canonical_sha256(original), compute_canonical_sha256(reordered))

    def test_semantic_policy_mutation_changes_digest(self):
        original = policy(); mutated = copy.deepcopy(original); mutated["precedence_rules"][0]["notes"] += " changed"
        self.assertNotEqual(compute_canonical_sha256(original), compute_canonical_sha256(mutated))


if __name__ == "__main__": unittest.main()
