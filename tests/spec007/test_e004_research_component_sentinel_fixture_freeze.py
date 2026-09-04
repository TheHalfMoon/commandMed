from __future__ import annotations

import copy
import unittest
from pathlib import Path

from scripts.e004_research_component_sentinel_fixture_freeze_v1 import (
    EXPECTED_FIXTURE_SHA256_SET_SHA256,
    EXPECTED_RECORD_COUNT,
    EXPECTED_SET_SHA256,
    load_json_strict,
    validate_fixture_set,
    verify,
)
from src.commandmed.eval_contract.canonical import compute_canonical_sha256


ROOT = Path(__file__).resolve().parents[2]
FIXTURE_SET = (
    ROOT
    / "specs/007-sft-v1/e004-research-component-sentinel-fixture-set-v1.json"
)
DECISION = (
    ROOT
    / "specs/007-sft-v1/e004-research-component-sentinel-fixture-freeze-founder-decision-2026-09-04.md"
)


class E004SentinelFixtureFreezeV1Tests(unittest.TestCase):
    def test_exact_authorized_fixture_set_passes(self) -> None:
        self.assertEqual(verify(FIXTURE_SET, DECISION), [])
        records = load_json_strict(FIXTURE_SET)
        self.assertEqual(len(records), EXPECTED_RECORD_COUNT)
        ordered = sorted(records, key=lambda item: item["guard_id"])
        self.assertEqual(compute_canonical_sha256(ordered), EXPECTED_SET_SHA256)
        self.assertEqual(
            compute_canonical_sha256(
                sorted(item["fixture_sha256"] for item in ordered)
            ),
            EXPECTED_FIXTURE_SHA256_SET_SHA256,
        )

    def test_prompt_mutation_fails_closed(self) -> None:
        records = load_json_strict(FIXTURE_SET)
        mutated = copy.deepcopy(records)
        mutated[0]["prompt_text"] += " changed"
        errors = validate_fixture_set(mutated)
        self.assertTrue(errors)
        self.assertTrue(
            any(
                "fixture_sha256 mismatch" in error
                or "sentinel set SHA-256 mismatch" in error
                for error in errors
            )
        )

    def test_replacement_fixture_fails_closed(self) -> None:
        records = load_json_strict(FIXTURE_SET)
        mutated = copy.deepcopy(records)
        mutated[0]["fixture_id"] = "SP007-RO-001-SENTINEL-REPLACEMENT"
        errors = validate_fixture_set(mutated)
        self.assertTrue(any("unauthorized fixture_id" in error for error in errors))
        self.assertTrue(any("fixture ID set differs" in error for error in errors))

    def test_optimization_feedback_cannot_be_enabled(self) -> None:
        records = load_json_strict(FIXTURE_SET)
        mutated = copy.deepcopy(records)
        mutated[0]["optimization_feedback_allowed"] = True
        errors = validate_fixture_set(mutated)
        self.assertTrue(
            any("optimization_feedback_allowed must be false" in error for error in errors)
        )

    def test_missing_guard_fails_closed(self) -> None:
        records = load_json_strict(FIXTURE_SET)
        errors = validate_fixture_set(records[:-1])
        self.assertTrue(any("fixture count must equal" in error for error in errors))
        self.assertTrue(any("guard set differs" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
