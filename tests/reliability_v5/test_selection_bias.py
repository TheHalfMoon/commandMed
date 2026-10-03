from __future__ import annotations

import unittest

from src.commandmed.reliability_v5.probability import ProbabilityContractError
from src.commandmed.reliability_v5.selection_bias import (
    align_display_to_semantic,
    debias_and_align,
    debias_display_distribution,
    estimate_display_slot_prior,
    mean_semantic_distribution,
)


class SelectionBiasContractTests(unittest.TestCase):
    def assertVectorAlmostEqual(self, left, right, places=12):
        self.assertEqual(len(left), len(right))
        for observed, expected in zip(left, right):
            self.assertAlmostEqual(expected, observed, places=places)

    def test_display_to_semantic_mapping_convention_is_explicit(self):
        # display slot 0 contains semantic candidate 2, slot 1 -> 0, slot 2 -> 1.
        result = align_display_to_semantic([0.6, 0.3, 0.1], [2, 0, 1])
        self.assertVectorAlmostEqual(result, [0.3, 0.1, 0.6])

    def test_semantic_mean_is_permutation_equivariant(self):
        rows = ([0.7, 0.2, 0.1], [0.1, 0.7, 0.2], [0.2, 0.1, 0.7])
        permutations = ([0, 1, 2], [2, 0, 1], [1, 2, 0])
        result = mean_semantic_distribution(rows, permutations)
        self.assertVectorAlmostEqual(result, [0.7, 0.2, 0.1])

    def test_uniform_rows_produce_uniform_slot_prior(self):
        prior = estimate_display_slot_prior([[0.25] * 4, [1.0, 1.0, 1.0, 1.0]])
        self.assertVectorAlmostEqual(prior, [0.25] * 4)

    def test_slot_prior_tracks_repeated_display_bias(self):
        prior = estimate_display_slot_prior([[0.7, 0.2, 0.1], [0.6, 0.3, 0.1]])
        self.assertGreater(prior[0], prior[1])
        self.assertGreater(prior[1], prior[2])
        self.assertAlmostEqual(1.0, sum(prior))

    def test_debias_equal_observation_and_prior_becomes_uniform(self):
        corrected = debias_display_distribution([0.6, 0.3, 0.1], [0.6, 0.3, 0.1])
        self.assertVectorAlmostEqual(corrected, [1 / 3, 1 / 3, 1 / 3], places=10)

    def test_uniform_prior_preserves_observed_distribution(self):
        corrected = debias_display_distribution([0.6, 0.3, 0.1], [1.0, 1.0, 1.0])
        self.assertVectorAlmostEqual(corrected, [0.6, 0.3, 0.1], places=10)

    def test_debias_then_align_returns_semantic_order(self):
        result = debias_and_align([0.6, 0.3, 0.1], [1.0, 1.0, 1.0], [2, 0, 1])
        self.assertVectorAlmostEqual(result, [0.3, 0.1, 0.6], places=10)

    def test_invalid_permutations_fail_closed(self):
        for permutation in ([0, 0, 1], [0, 1], [0, 1, 3], [0, True, 2]):
            with self.subTest(permutation=permutation):
                with self.assertRaises(ProbabilityContractError):
                    align_display_to_semantic([0.2, 0.3, 0.5], permutation)

    def test_row_count_and_width_mismatches_fail_closed(self):
        with self.assertRaises(ProbabilityContractError):
            mean_semantic_distribution([[0.5, 0.5]], [])
        with self.assertRaises(ProbabilityContractError):
            estimate_display_slot_prior([[0.5, 0.5], [0.2, 0.3, 0.5]])
        with self.assertRaises(ProbabilityContractError):
            debias_display_distribution([0.5, 0.5], [0.2, 0.3, 0.5])


if __name__ == "__main__":
    unittest.main()
