from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.reliability_v5.case_generator import (
    case_space_size,
    deterministic_cases,
    expanded_domains,
)
from src.commandmed.reliability_v5.contracts import ReliabilityContractError

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/research/paper-rebuild-v2-2026-10-02/riskcalcs-rule-oracle-final-candidate-v5.json"


class CaseGeneratorTests(unittest.TestCase):
    def test_boolean_numeric_expansion_is_deterministic(self):
        domains = {"flag": [True], "age": [65]}
        self.assertEqual(case_space_size(domains), 10)
        self.assertEqual(expanded_domains(domains), expanded_domains({"age": [65], "flag": [False]}))

    def test_generation_is_unique_and_mapping_order_invariant(self):
        a = {"x": [10], "flag": [True], "y": [20], "z": [30]}
        b = {"z": [30], "y": [20], "x": [10], "flag": [False]}
        first = deterministic_cases("toy", a, count=64)
        second = deterministic_cases("toy", b, count=64)
        self.assertEqual(first, second)
        self.assertEqual(len({row["case_id"] for row in first}), 64)
        self.assertEqual(len({row["state_index"] for row in first}), 64)

    def test_insufficient_space_fails_closed(self):
        with self.assertRaises(ReliabilityContractError):
            deterministic_cases("tiny", {"flag": [True]}, count=64)

    def test_invalid_domain_value_fails_closed(self):
        with self.assertRaises(ReliabilityContractError):
            expanded_domains({"category": ["high"]})

    def test_frozen_manifest_supports_64_cases_per_calculator(self):
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        selected = payload["selected"]
        self.assertEqual(len(selected), 64)
        for calculator in selected:
            with self.subTest(pmid=calculator["pmid"]):
                self.assertGreaterEqual(calculator["prospective_case_space"], 64)
                cases = deterministic_cases(
                    f"pmid:{calculator['pmid']}",
                    calculator["domain_constants"],
                    count=64,
                )
                self.assertEqual(len(cases), 64)
                self.assertEqual(len({row["case_id"] for row in cases}), 64)


if __name__ == "__main__":
    unittest.main()
