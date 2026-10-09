from __future__ import annotations

import math
import unittest

from src.commandmed.reliability_v5.probability import (
    ProbabilityContractError,
    multiclass_brier,
    negative_log_likelihood,
    normalize_probabilities,
    softmax,
    temperature_scale_logits,
)


class ProbabilityContractTests(unittest.TestCase):
    def test_normalize_probabilities_preserves_ratios(self):
        result = normalize_probabilities([2.0, 3.0, 5.0])
        self.assertAlmostEqual(1.0, sum(result))
        self.assertEqual((0.2, 0.3, 0.5), result)

    def test_invalid_probability_vectors_fail_closed(self):
        for value in ([], [0.0, 0.0], [-0.1, 1.1], [math.nan, 1.0], "0.5,0.5"):
            with self.subTest(value=value):
                with self.assertRaises((ProbabilityContractError, ValueError)):
                    normalize_probabilities(value)

    def test_softmax_is_stable_for_large_logits(self):
        result = softmax([1000.0, 1001.0, 1002.0])
        self.assertAlmostEqual(1.0, sum(result))
        self.assertGreater(result[2], result[1])
        self.assertGreater(result[1], result[0])

    def test_temperature_one_matches_softmax(self):
        logits = [1.0, 2.0, -1.0]
        self.assertEqual(softmax(logits), temperature_scale_logits(logits, 1.0))

    def test_lower_temperature_sharpens_distribution(self):
        logits = [0.0, 1.0]
        cold = temperature_scale_logits(logits, 0.5)
        warm = temperature_scale_logits(logits, 2.0)
        self.assertGreater(cold[1], warm[1])

    def test_invalid_temperature_rejected(self):
        for value in (0.0, -1.0, math.inf, math.nan, "bad"):
            with self.subTest(value=value):
                with self.assertRaises(ProbabilityContractError):
                    temperature_scale_logits([0.0, 1.0], value)

    def test_nll_and_brier_are_exact_on_simple_fixture(self):
        probabilities = [0.25, 0.75]
        self.assertAlmostEqual(-math.log(0.75), negative_log_likelihood(probabilities, 1))
        self.assertAlmostEqual(0.125, multiclass_brier(probabilities, 1))

    def test_target_index_must_be_valid_integer(self):
        for target in (-1, 2, True, 0.5):
            with self.subTest(target=target):
                with self.assertRaises(ProbabilityContractError):
                    negative_log_likelihood([0.5, 0.5], target)


if __name__ == "__main__":
    unittest.main()
