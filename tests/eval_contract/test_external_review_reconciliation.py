"""Regression tests for final external-review governance findings."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.validate import (
    validate_benchmark,
    validate_gold_protocol,
)


class TestExternalReviewReconciliation(unittest.TestCase):
    """Fail-closed regressions discovered by independent review."""

    @classmethod
    def setUpClass(cls) -> None:
        data_dir = Path(__file__).resolve().parents[2] / "data" / "eval"
        cls.benchmarks = json.loads((data_dir / "benchmarks.json").read_text(encoding="utf-8"))
        cls.gold = json.loads((data_dir / "gold_protocols.json").read_text(encoding="utf-8"))

    def _development_record(self) -> dict[str, object]:
        return deepcopy(next(x for x in self.benchmarks if x["intended_use"] == "DEVELOPMENT"))

    def test_executable_unbound_artifact_is_rejected(self) -> None:
        record = self._development_record()
        record["artifact_version"] = "UNBOUND"
        errors = validate_benchmark(record)
        self.assertTrue(any("concrete artifact_version" in e for e in errors))

    def test_executable_unresolved_revision_is_rejected(self) -> None:
        record = self._development_record()
        record["source_revision"] = "UNRESOLVED"
        errors = validate_benchmark(record)
        self.assertTrue(any("immutable source_revision" in e for e in errors))

    def test_whitespace_padded_unresolved_source_is_rejected(self) -> None:
        record = self._development_record()
        record["source_uri"] = "  UNRESOLVED  "
        errors = validate_benchmark(record)
        self.assertTrue(any("resolved source_uri" in e for e in errors))

    def test_unknown_gold_scoring_stage_is_rejected(self) -> None:
        record = deepcopy(self.gold[0])
        record["permitted_scoring_stages"] = ["UNREGISTERED_SAFETY_AUDIT"]
        errors = validate_gold_protocol(record)
        self.assertTrue(any("Unknown permitted_scoring_stage" in e for e in errors))

    def test_canonical_gold_stages_validate(self) -> None:
        for record in self.gold:
            errors = validate_gold_protocol(record)
            self.assertEqual(errors, [], f"{record['family_id']}: {errors}")

    def test_medhelm_license_evidence_is_immutable(self) -> None:
        record = next(x for x in self.benchmarks if x["benchmark_id"] == "medhelm")
        uri = record["license_source_uri"]
        self.assertIn("89001e71b45ff860572bca9fd3f8e28fd1b1c118", uri)
        self.assertNotIn("/blob/main/", uri)
        self.assertEqual(record["intended_use"], "REFERENCE_ONLY")
        self.assertEqual(record["license_status"], "COMPONENT_SPECIFIC")


if __name__ == "__main__":
    unittest.main()
