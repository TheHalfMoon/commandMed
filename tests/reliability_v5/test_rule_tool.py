from __future__ import annotations

import unittest

from src.commandmed.reliability_v5.contracts import ReliabilityContractError
from src.commandmed.reliability_v5.rule_tool import execute_rule_tool


CALC_SHA = "a" * 64


def toy_risk_rule(*, age: float, high_risk: bool) -> int:
    score = 0
    if age >= 65:
        score += 1
    if high_risk:
        score += 2
    return score


def toy_action(score: int) -> str:
    return "ESCALATE" if score >= 2 else "ANSWER"


class RuleToolTests(unittest.TestCase):
    def test_toy_rule_is_identity_bound_and_deterministic(self):
        first = execute_rule_tool(
            tool_id="toy-risk-v1",
            calculator_sha256=CALC_SHA,
            inputs={"high_risk": True, "age": 70},
            calculator=toy_risk_rule,
            action_mapper=toy_action,
        )
        second = execute_rule_tool(
            tool_id="toy-risk-v1",
            calculator_sha256=CALC_SHA,
            inputs={"age": 70, "high_risk": True},
            calculator=toy_risk_rule,
            action_mapper=toy_action,
        )
        self.assertEqual(first, second)
        self.assertEqual(first.raw_output, 3)
        self.assertEqual(first.action, "ESCALATE")
        self.assertEqual(len(first.input_sha256), 64)
        self.assertEqual(len(first.output_sha256), 64)

    def test_input_change_changes_bound_input_identity(self):
        low = execute_rule_tool(
            tool_id="toy-risk-v1",
            calculator_sha256=CALC_SHA,
            inputs={"age": 40, "high_risk": False},
            calculator=toy_risk_rule,
            action_mapper=toy_action,
        )
        high = execute_rule_tool(
            tool_id="toy-risk-v1",
            calculator_sha256=CALC_SHA,
            inputs={"age": 70, "high_risk": True},
            calculator=toy_risk_rule,
            action_mapper=toy_action,
        )
        self.assertNotEqual(low.input_sha256, high.input_sha256)
        self.assertEqual(low.action, "ANSWER")
        self.assertEqual(high.action, "ESCALATE")

    def test_contract_rejects_unbound_or_unsafe_inputs(self):
        with self.assertRaises(ReliabilityContractError):
            execute_rule_tool(
                tool_id="toy-risk-v1",
                calculator_sha256="not-a-sha",
                inputs={"age": 70, "high_risk": True},
                calculator=toy_risk_rule,
                action_mapper=toy_action,
            )
        with self.assertRaises(ReliabilityContractError):
            execute_rule_tool(
                tool_id="toy-risk-v1",
                calculator_sha256=CALC_SHA,
                inputs={"age": float("nan"), "high_risk": True},
                calculator=toy_risk_rule,
                action_mapper=toy_action,
            )
        with self.assertRaises(ReliabilityContractError):
            execute_rule_tool(
                tool_id="toy-risk-v1",
                calculator_sha256=CALC_SHA,
                inputs={"age": 70, "note": "free text"},
                calculator=lambda **_: 0,
                action_mapper=toy_action,
            )


if __name__ == "__main__":
    unittest.main()
