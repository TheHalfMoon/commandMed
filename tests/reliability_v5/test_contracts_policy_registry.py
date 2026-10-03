from __future__ import annotations

import math
import unittest

from src.commandmed.reliability_v5.contracts import (
    EffectInterval,
    ReliabilityContractError,
    classify_effect,
    hard_gate_noninferiority_pass,
    order_gap,
    ordered_interaction,
)
from src.commandmed.reliability_v5.policy import fixed_defer_policy
from src.commandmed.reliability_v5.probability import ProbabilityContractError
from src.commandmed.reliability_v5.registry import (
    IMPLEMENTED,
    OBJECTIVE_MECHANICS_IMPLEMENTED,
    INTERVENTIONS,
    ORDERED_INTERACTION_CANDIDATES,
    get_intervention,
)


class EffectContractTests(unittest.TestCase):
    def test_effect_interval_validates_order_and_finiteness(self):
        with self.assertRaises(ReliabilityContractError):
            EffectInterval(0.0, 1.0, -1.0)
        with self.assertRaises(ReliabilityContractError):
            EffectInterval(0.0, -1.0, math.inf)
        with self.assertRaises(ReliabilityContractError):
            EffectInterval(2.0, -1.0, 1.0)

    def test_effect_classes_are_non_overlapping(self):
        margin = 0.05
        self.assertEqual("IMPROVE", classify_effect(EffectInterval(0.10, 0.06, 0.14), margin))
        self.assertEqual("HARM", classify_effect(EffectInterval(-0.10, -0.14, -0.06), margin))
        self.assertEqual("EQUIVALENT", classify_effect(EffectInterval(0.0, -0.04, 0.04), margin))
        self.assertEqual("INCONCLUSIVE", classify_effect(EffectInterval(0.04, -0.01, 0.08), margin))

    def test_hard_gate_uses_lower_confidence_bound(self):
        margin = 0.05
        self.assertTrue(hard_gate_noninferiority_pass(EffectInterval(0.0, -0.05, 0.03), margin))
        self.assertFalse(hard_gate_noninferiority_pass(EffectInterval(-0.04, -0.051, 0.01), margin))

    def test_ordered_interaction_and_order_gap(self):
        gamma_ab = ordered_interaction(base=0.50, intervention_a=0.60, intervention_b=0.55, a_after_b=0.70)
        gamma_ba = ordered_interaction(base=0.50, intervention_a=0.60, intervention_b=0.55, a_after_b=0.64)
        self.assertAlmostEqual(0.05, gamma_ab)
        self.assertAlmostEqual(-0.01, gamma_ba)
        self.assertAlmostEqual(0.06, order_gap(gamma_ab, gamma_ba))

    def test_invalid_margin_rejected(self):
        with self.assertRaises(ReliabilityContractError):
            classify_effect(EffectInterval(0.0, -0.1, 0.1), 0.0)


class FixedPolicyTests(unittest.TestCase):
    def test_policy_acts_at_or_above_threshold(self):
        decision = fixed_defer_policy([0.2, 0.8], 0.8, action_labels=["NO", "YES"])
        self.assertEqual("YES", decision.action)
        self.assertEqual(1, decision.semantic_index)
        self.assertFalse(decision.deferred)

    def test_policy_defers_below_threshold(self):
        decision = fixed_defer_policy([0.49, 0.51], 0.8, action_labels=["NO", "YES"])
        self.assertEqual("DEFER", decision.action)
        self.assertIsNone(decision.semantic_index)
        self.assertTrue(decision.deferred)

    def test_tie_rule_is_lowest_semantic_index(self):
        decision = fixed_defer_policy([0.5, 0.5], 0.4, action_labels=["A", "B"])
        self.assertEqual("A", decision.action)
        self.assertEqual(0, decision.semantic_index)

    def test_policy_contract_rejects_bad_threshold_or_labels(self):
        with self.assertRaises(ProbabilityContractError):
            fixed_defer_policy([0.5, 0.5], 1.1)
        with self.assertRaises(ProbabilityContractError):
            fixed_defer_policy([0.5, 0.5], 0.5, action_labels=["A"])
        with self.assertRaises(ProbabilityContractError):
            fixed_defer_policy([0.5, 0.5], 0.5, action_labels=["DEFER", "B"])


class InterventionRegistryTests(unittest.TestCase):
    def test_registry_has_exact_v5_candidate_ids(self):
        self.assertEqual(
            {
                "A1_TS_V1",
                "A2_SELBIAS_V1",
                "B1_TYPED_V1",
                "C1_CRDI_V1",
                "C2_CRDI_RETAIN_V1",
                "D1_DEFER_V1",
                "D2_RULETOOL_V1",
            },
            set(INTERVENTIONS),
        )

    def test_no_registry_entry_grants_execution_authority(self):
        self.assertTrue(all(spec.execution_authority == "NO" for spec in INTERVENTIONS.values()))

    def test_registry_distinguishes_mechanical_and_objective_mechanics(self):
        self.assertEqual(IMPLEMENTED, get_intervention("A1_TS_V1").implementation_status)
        self.assertEqual(IMPLEMENTED, get_intervention("A2_SELBIAS_V1").implementation_status)
        self.assertEqual(IMPLEMENTED, get_intervention("D1_DEFER_V1").implementation_status)
        self.assertEqual(OBJECTIVE_MECHANICS_IMPLEMENTED, get_intervention("B1_TYPED_V1").implementation_status)
        self.assertEqual(OBJECTIVE_MECHANICS_IMPLEMENTED, get_intervention("C1_CRDI_V1").implementation_status)
        self.assertEqual(OBJECTIVE_MECHANICS_IMPLEMENTED, get_intervention("C2_CRDI_RETAIN_V1").implementation_status)
        self.assertEqual(IMPLEMENTED, get_intervention("D2_RULETOOL_V1").implementation_status)

    def test_ordered_interaction_registry_is_exact(self):
        self.assertEqual(
            (
                ("A1_TS_V1", "A2_SELBIAS_V1"),
                ("A2_SELBIAS_V1", "A1_TS_V1"),
                ("A1_TS_V1", "C1_CRDI_V1"),
                ("C1_CRDI_V1", "A1_TS_V1"),
            ),
            ORDERED_INTERACTION_CANDIDATES,
        )

    def test_unknown_intervention_fails_closed(self):
        with self.assertRaises(KeyError):
            get_intervention("LATEST")


if __name__ == "__main__":
    unittest.main()
