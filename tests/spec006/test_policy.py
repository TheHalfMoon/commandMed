"""US2/T013 fixture tests: Spec 006 safety policy precedence + fail-closed."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.spec006 import policy as policy_mod
from src.commandmed.spec006.policy import (
    evaluate_precedence,
    validate_policy_bundle,
    validate_safety_rule,
)

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "data/spec006/safety_policy.json"


def load_policy():
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def minimal_rule(**overrides):
    rule = {
        "rule_id": "R-TEST",
        "rule_version": "1.0.0",
        "source_policy_sha256": "0" * 64,
        "trigger_condition": {"kind": "lexical", "ref": "token"},
        "required_state": "ESCALATE",
        "precedence": 3,
        "threshold_policy_class": "FROZEN_POLICY_ZERO_TOLERANCE",
        "applicable_scope": "COMPONENT_QUALIFICATION",
        "revoked": False,
    }
    rule.update(overrides)
    return rule


class TestSafetyRuleContract(unittest.TestCase):
    def test_canonical_bundle_is_valid(self):
        self.assertEqual([], validate_policy_bundle(load_policy()))

    def test_undeclared_field_rejected(self):
        rule = minimal_rule(extra="nope")
        errors = validate_safety_rule(rule)
        self.assertTrue(any("undeclared" in error and "extra" in error for error in errors))

    def test_unknown_behavioral_state_rejected(self):
        errors = validate_safety_rule(minimal_rule(required_state="BLOCKED"))
        self.assertTrue(any("required_state" in error for error in errors))

    def test_unknown_trigger_kind_rejected(self):
        rule = minimal_rule(trigger_condition={"kind": "vibes", "ref": "x"})
        errors = validate_safety_rule(rule)
        self.assertTrue(any("kind" in error for error in errors))

    def test_precedence_bounds(self):
        self.assertTrue(validate_safety_rule(minimal_rule(precedence=0)))
        self.assertTrue(validate_safety_rule(minimal_rule(precedence=101)))
        self.assertTrue(validate_safety_rule(minimal_rule(precedence="high")))
        self.assertEqual([], validate_safety_rule(minimal_rule(precedence=100)))


class TestPolicyBundle(unittest.TestCase):
    def setUp(self):
        self.policy = load_policy()

    def test_duplicate_rule_id_rejected(self):
        bundle = copy.deepcopy(self.policy)
        bundle["rules"].append(copy.deepcopy(bundle["rules"][0]))
        errors = validate_policy_bundle(bundle)
        self.assertTrue(any("duplicate rule_id" in error for error in errors))

    def test_duplicate_precedence_tie_is_validation_error(self):
        bundle = copy.deepcopy(self.policy)
        extra = copy.deepcopy(bundle["rules"][1])
        extra["rule_id"] = extra["rule_id"] + "-CLONE"
        bundle["rules"].append(extra)
        errors = validate_policy_bundle(bundle)
        self.assertTrue(any("duplicate precedence" in error for error in errors))

    def test_min_items_one_enforced(self):
        bundle = copy.deepcopy(self.policy)
        bundle["rules"] = []
        errors = validate_policy_bundle(bundle)
        self.assertTrue(any("minItems 1" in error or "minItems" in error for error in errors))

    def test_policy_sha256_projection_mismatch_rejected(self):
        bundle = copy.deepcopy(self.policy)
        bundle["policy_sha256"] = "1" * 64
        errors = validate_policy_bundle(bundle)
        self.assertTrue(any("policy_sha256" in error and "mismatch" in error for error in errors))

    def test_revoked_rule_present_in_bundle_still_validates_but_fails_closed_on_fire(self):
        bundle = copy.deepcopy(self.policy)
        revoked = copy.deepcopy(bundle["rules"][0])
        revoked["rule_id"] += "-REVOKED"
        revoked["revoked"] = True
        # A revoked clone shares precedence; remove the original to keep ties clean.
        bundle["rules"] = [r for r in bundle["rules"] if r["rule_id"] != bundle["rules"][0]["rule_id"]]
        bundle["rules"].append(revoked)
        self.assertEqual(
            [],
            [
                error
                for error in validate_policy_bundle(bundle)
                if "policy_sha256" not in error
            ],
        )
        resolution = evaluate_precedence([revoked])
        self.assertEqual("ABSTAIN", resolution["state_after"])
        self.assertIn("BLOCKED_SAFETY_STATE", resolution["reason_codes"])

    def test_malformed_fired_rule_blocks_entire_evaluation(self):
        malformed = {"rule_id": "R-BAD", "precedence": 1, "required_state": "ANSWER"}
        resolution = evaluate_precedence([malformed])
        self.assertEqual("ABSTAIN", resolution["state_after"])
        self.assertIn("BLOCKED_SAFETY_STATE", resolution["reason_codes"])


class TestPrecedenceEvaluation(unittest.TestCase):
    """SP-001..SP-006 operationalization per research.md §5."""

    def test_no_fired_rules_answers(self):
        resolution = evaluate_precedence([])
        self.assertEqual("ANSWER", resolution["state_after"])
        self.assertEqual([], resolution["trigger_record_ids"])

    def test_emergency_exact_equality_dominates_everything(self):
        emergency = minimal_rule(rule_id="R-EM", required_state="EMERGENCY", precedence=2)
        escalate = minimal_rule(rule_id="R-ES", required_state="ESCALATE", precedence=3)
        ask_more = minimal_rule(
            rule_id="R-MISS", required_state="ASK_MORE", precedence=4,
            threshold_policy_class="FROZEN_SENTINEL_ZERO_VIOLATIONS",
        )
        resolution = evaluate_precedence([ask_more, escalate, emergency])
        self.assertEqual("EMERGENCY", resolution["state_after"])
        self.assertEqual(["R-EM"], resolution["trigger_record_ids"])

    def test_escalate_beats_lower_layers(self):
        escalate = minimal_rule(rule_id="R-ES", required_state="ESCALATE", precedence=3)
        use_tool = {
            "rule_id": "SCAFFOLD::TOOL_LAYER",
            "precedence": 6,
            "required_state": "USE_TOOL",
        }
        resolution = evaluate_precedence([use_tool, escalate])
        self.assertEqual("ESCALATE", resolution["state_after"])

    def test_conflicting_equal_precedence_never_averaged_abstains(self):
        first = minimal_rule(rule_id="R-A", required_state="USE_TOOL", precedence=5)
        second = minimal_rule(
            rule_id="R-B", required_state="RETRIEVE_EVIDENCE", precedence=5
        )
        resolution = evaluate_precedence([first, second])
        self.assertEqual("ABSTAIN", resolution["state_after"])
        self.assertIn("CONFLICTING_SAFETY_OUTCOMES", resolution["reason_codes"])

    def test_conflicting_equal_precedence_involving_escalation_fails_toward_escalate(self):
        first = minimal_rule(rule_id="R-A", required_state="ESCALATE", precedence=4)
        second = minimal_rule(
            rule_id="R-B", required_state="ASK_MORE", precedence=4,
            threshold_policy_class="FROZEN_SENTINEL_ZERO_VIOLATIONS",
        )
        resolution = evaluate_precedence([first, second])
        self.assertEqual("ESCALATE", resolution["state_after"])
        self.assertIn("CONFLICTING_SAFETY_OUTCOMES", resolution["reason_codes"])

    def test_tool_layer_pseudo_rule_accepted_when_minimal_and_typed(self):
        pseudo = {
            "rule_id": "SCAFFOLD::TOOL_LAYER",
            "precedence": 6,
            "required_state": "RETRIEVE_EVIDENCE",
        }
        resolution = evaluate_precedence([pseudo])
        self.assertEqual("RETRIEVE_EVIDENCE", resolution["state_after"])

    def test_tool_layer_pseudo_rule_with_extra_fields_blocked(self):
        pseudo = {
            "rule_id": "SCAFFOLD::TOOL_LAYER",
            "precedence": 6,
            "required_state": "USE_TOOL",
            "smuggled": "generative override",
        }
        resolution = evaluate_precedence([pseudo])
        self.assertEqual("ABSTAIN", resolution["state_after"])
        self.assertIn("BLOCKED_SAFETY_STATE", resolution["reason_codes"])

    def test_non_list_input_blocked(self):
        resolution = evaluate_precedence("EMERGENCY")
        self.assertEqual("ABSTAIN", resolution["state_after"])
        self.assertIn("BLOCKED_SAFETY_STATE", resolution["reason_codes"])

    def test_emergency_reason_code_emitted_for_emergency_winner(self):
        emergency = minimal_rule(rule_id="R-EM", required_state="EMERGENCY", precedence=2)
        resolution = evaluate_precedence([emergency])
        self.assertIn("FROZEN_POLICY_EMERGENCY", resolution["reason_codes"])


if __name__ == "__main__":
    unittest.main()


class TestCanonicalVocabulary(unittest.TestCase):
    """Finding repair: one canonical behavioral-state definition."""

    def test_policy_vocabulary_is_the_spec002_canonical_set(self):
        from src.commandmed.eval_contract.safety import BEHAVIOR_STATES

        self.assertIs(BEHAVIOR_STATES, policy_mod.BEHAVIORAL_STATES)

    def test_trace_module_reuses_canonical_vocabulary(self):
        from src.commandmed.spec006 import trace

        self.assertIs(policy_mod.BEHAVIORAL_STATES, trace.BEHAVIORAL_STATES)


class TestTriggerBindingStrictness(unittest.TestCase):
    """Finding repairs 4+6: required trigger bindings + regex compile check."""

    def test_lexical_rule_without_ref_rejected(self):
        rule = minimal_rule(
            trigger_condition={"kind": "lexical"}
        )
        errors = validate_safety_rule(rule)
        self.assertTrue(any("ref" in error for error in errors))

    def test_semantic_pattern_without_ref_rejected(self):
        rule = minimal_rule(trigger_condition={"kind": "semantic_pattern"})
        errors = validate_safety_rule(rule)
        self.assertTrue(any("ref" in error for error in errors))

    def test_tool_result_flag_without_ref_rejected(self):
        rule = minimal_rule(trigger_condition={"kind": "tool_result_flag"})
        errors = validate_safety_rule(rule)
        self.assertTrue(any("ref" in error for error in errors))

    def test_missing_slot_without_threshold_rejected(self):
        rule = minimal_rule(trigger_condition={"kind": "missing_slot", "ref": "slot_a|slot_b"})
        errors = validate_safety_rule(rule)
        self.assertTrue(any("threshold" in error for error in errors))

    def test_malformed_regex_rejected_at_validation_time(self):
        rule = minimal_rule(trigger_condition={"kind": "semantic_pattern", "ref": "(unclosed["})
        errors = validate_safety_rule(rule)
        self.assertTrue(any("malformed frozen pattern" in error for error in errors))

    def test_valid_regex_accepted(self):
        rule = minimal_rule(trigger_condition={"kind": "semantic_pattern", "ref": "worst .*pain"})
        self.assertEqual([], validate_safety_rule(rule))
