from __future__ import annotations

import math
import unittest

from src.commandmed.reliability_v5.statistics import (
    StatisticsContractError,
    holm_adjusted_p_values,
    normal_approx_paired_mde,
    normal_approx_required_clusters,
    paired_cluster_bootstrap_effect,
    paired_mean_effect,
)


class PairedStatisticsTests(unittest.TestCase):
    def test_paired_mean_effect_orientation(self):
        self.assertAlmostEqual(0.5, paired_mean_effect([1, 2, 3], [1.5, 2.5, 3.5]))

    def test_paired_vectors_must_align(self):
        with self.assertRaises(StatisticsContractError):
            paired_mean_effect([1.0], [1.0, 2.0])
        with self.assertRaises(StatisticsContractError):
            paired_mean_effect([], [])

    def test_bootstrap_is_seed_deterministic_and_cluster_paired(self):
        base = [0.0, 1.0, 2.0, 3.0]
        treated = [1.0, 2.0, 3.0, 4.0]
        first = paired_cluster_bootstrap_effect(base, treated, resamples=400, seed=11)
        second = paired_cluster_bootstrap_effect(base, treated, resamples=400, seed=11)
        self.assertEqual(first, second)
        self.assertEqual(1.0, first.estimate)
        self.assertEqual(1.0, first.lower)
        self.assertEqual(1.0, first.upper)

    def test_bootstrap_rejects_invalid_contract(self):
        with self.assertRaises(StatisticsContractError):
            paired_cluster_bootstrap_effect([0.0], [0.0], resamples=99, seed=1)
        with self.assertRaises(StatisticsContractError):
            paired_cluster_bootstrap_effect([0.0], [0.0], resamples=100, seed=1, confidence=1.0)


class MultiplicityTests(unittest.TestCase):
    def test_holm_known_example(self):
        adjusted = holm_adjusted_p_values([0.01, 0.04, 0.03])
        self.assertEqual((0.03, 0.06, 0.06), adjusted)

    def test_holm_preserves_bounds_and_rejects_bad_values(self):
        self.assertEqual((0.0, 1.0), holm_adjusted_p_values([0.0, 1.0]))
        with self.assertRaises(StatisticsContractError):
            holm_adjusted_p_values([0.1, math.nan])
        with self.assertRaises(StatisticsContractError):
            holm_adjusted_p_values([1.1])


class PowerPlanningTests(unittest.TestCase):
    def test_mde_matches_normal_formula(self):
        value = normal_approx_paired_mde(1.0, 100, alpha=0.05, power=0.90)
        self.assertAlmostEqual(0.32415, value, places=4)

    def test_required_clusters_inverts_planning_formula(self):
        required = normal_approx_required_clusters(1.0, 0.2, alpha=0.05, power=0.90)
        self.assertGreaterEqual(required, 2)
        achieved = normal_approx_paired_mde(1.0, required, alpha=0.05, power=0.90)
        self.assertLessEqual(achieved, 0.2)
        if required > 2:
            previous = normal_approx_paired_mde(1.0, required - 1, alpha=0.05, power=0.90)
            self.assertGreater(previous, 0.2)

    def test_power_planning_rejects_invalid_inputs(self):
        with self.assertRaises(StatisticsContractError):
            normal_approx_paired_mde(0.0, 100)
        with self.assertRaises(StatisticsContractError):
            normal_approx_required_clusters(1.0, 0.0)
        with self.assertRaises(StatisticsContractError):
            normal_approx_paired_mde(1.0, 1)


if __name__ == "__main__":
    unittest.main()
