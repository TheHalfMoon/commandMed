from __future__ import annotations

import math
import unittest

from src.commandmed.reliability_v5.contracts import ReliabilityContractError
from src.commandmed.reliability_v5.objectives import (
    capability_retention_penalty,
    contract_consistency_penalty,
    contract_regularized_objective,
    negative_log_likelihood_for_target,
    retention_regularized_objective,
    typed_readout_logits,
    typed_readout_probabilities,
)


class ObjectiveMechanicsTests(unittest.TestCase):
    def test_typed_readout_linear_map_is_exact(self):
        logits = typed_readout_logits([2.0, -1.0], [[1.0, 0.5], [-2.0, 1.0]], [0.25, 1.0])
        self.assertEqual((1.75, -4.0), logits)
        probabilities = typed_readout_probabilities([2.0, -1.0], [[1.0, 0.5], [-2.0, 1.0]], [0.25, 1.0])
        self.assertAlmostEqual(1.0, sum(probabilities))
        self.assertGreater(probabilities[0], probabilities[1])

    def test_typed_readout_shape_and_target_validation_fail_closed(self):
        with self.assertRaises(ReliabilityContractError):
            typed_readout_logits(["bad"], [[1.0]], [0.0])
        with self.assertRaises(ReliabilityContractError):
            typed_readout_logits([1.0], [[float("nan")]], [0.0])
        with self.assertRaises(ReliabilityContractError):
            typed_readout_logits([1.0, 2.0], [[1.0]], [0.0])
        with self.assertRaises(ReliabilityContractError):
            typed_readout_logits([1.0], [[1.0], [2.0]], [0.0])
        with self.assertRaises(ReliabilityContractError):
            negative_log_likelihood_for_target([0.5, 0.5], True)
        with self.assertRaises(ReliabilityContractError):
            negative_log_likelihood_for_target([-0.1, 1.1], 1)

    def test_objective_probability_floor_is_finite_and_deterministic(self):
        value = negative_log_likelihood_for_target([0.0, 1.0], 0)
        self.assertAlmostEqual(-math.log(1e-15), value)

    def test_contract_penalty_is_zero_for_identical_distribution(self):
        p = [0.1, 0.2, 0.7]
        self.assertAlmostEqual(0.0, contract_consistency_penalty(p, p))
        self.assertGreater(contract_consistency_penalty(p, [0.7, 0.2, 0.1]), 0.0)

    def test_c1_composite_objective_adds_weighted_contract_penalty(self):
        penalty = contract_consistency_penalty([0.8, 0.2], [0.6, 0.4])
        value = contract_regularized_objective(
            task_loss=1.25,
            original=[0.8, 0.2],
            transformed=[0.6, 0.4],
            contract_weight=2.0,
        )
        self.assertAlmostEqual(1.25 + 2.0 * penalty, value)

    def test_c2_adds_directional_retention_anchor(self):
        reference = [0.9, 0.1]
        candidate = [0.7, 0.3]
        retention = capability_retention_penalty(reference, candidate)
        value = retention_regularized_objective(
            task_loss=0.5,
            original=[0.8, 0.2],
            transformed=[0.75, 0.25],
            contract_weight=1.0,
            retention_reference=reference,
            retention_candidate=candidate,
            retention_weight=3.0,
        )
        base = contract_regularized_objective(
            task_loss=0.5,
            original=[0.8, 0.2],
            transformed=[0.75, 0.25],
            contract_weight=1.0,
        )
        self.assertAlmostEqual(base + 3.0 * retention, value)

    def test_negative_or_nonfinite_weights_are_rejected(self):
        bad_values = (-1.0, math.inf, math.nan, "bad")
        for bad in bad_values:
            with self.subTest(bad=bad):
                with self.assertRaises(ReliabilityContractError):
                    contract_regularized_objective(
                        task_loss=0.1,
                        original=[0.5, 0.5],
                        transformed=[0.5, 0.5],
                        contract_weight=bad,
                    )


if __name__ == "__main__":
    unittest.main()
