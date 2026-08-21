"""Tests for benchmark registry validation and required initial families."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.model import AccessClass, VerificationStatus
from src.commandmed.eval_contract.validate import (
    check_no_payload_markers,
    validate_benchmark,
    validate_benchmark_registry,
)


class TestBenchmarkRegistry(unittest.TestCase):
    """Tests for the benchmark registry contract."""

    def setUp(self) -> None:
        self.data_dir = Path(__file__).resolve().parents[2] / "data" / "eval"
        self.benchmarks_file = self.data_dir / "benchmarks.json"

    def test_canonical_benchmarks_file_exists_and_validates(self) -> None:
        """Canonical data/eval/benchmarks.json must exist and validate cleanly."""
        self.assertTrue(self.benchmarks_file.is_file(), "benchmarks.json must exist")
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        is_valid, errors = validate_benchmark_registry(data)
        self.assertTrue(is_valid, f"benchmarks.json failed validation: {errors}")
        self.assertEqual(len(errors), 0)

    def test_all_fr002_required_benchmark_families_present(self) -> None:
        """FR-002: Ensure all required initial benchmark families are present in registry."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        ids = {b["benchmark_id"] for b in data}

        required_ids = {
            "medhelm",
            "healthbench_core",
            "healthbench_hard",
            "healthbench_consensus",
            "healthbench_professional",
            "medxpertqa",
            "medqa_usmle",
            "medmcqa",
            "pubmedqa",
            "medqabstain",
            "medabstain",
        }
        for req_id in required_ids:
            self.assertIn(req_id, ids, f"Missing required benchmark family: {req_id}")

    def test_all_benchmarks_have_verified_sources_and_dates(self) -> None:
        """Ensure every entry in initial registry has verified source metadata."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        for b in data:
            self.assertEqual(
                b["verification_status"],
                VerificationStatus.VERIFIED.value,
                f"Benchmark {b['benchmark_id']} not verified",
            )
            self.assertTrue(len(b["primary_source"]) > 0)
            self.assertNotEqual(b["primary_source"], "UNRESOLVED")
            self.assertTrue(len(b["verification_date"]) == 10)

    def test_missing_required_field_rejection(self) -> None:
        """Validation fails if any required field is missing or null."""
        sample = {
            "benchmark_id": "test_missing",
            "canonical_name": "Test Benchmark",
            # primary_source missing
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "MIT",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",
            "verification_status": "VERIFIED",
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(any("Missing required field 'primary_source'" in e for e in errors))

    def test_duplicate_benchmark_id_rejection(self) -> None:
        """Validation fails if duplicate benchmark IDs are detected."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        duplicated_data = data + [data[0]]
        is_valid, errors = validate_benchmark_registry(duplicated_data)
        self.assertFalse(is_valid)
        self.assertTrue(any("Duplicate benchmark_id" in e for e in errors))

    def test_invalid_enum_rejection(self) -> None:
        """Validation fails if invalid enum value is used."""
        sample = {
            "benchmark_id": "test_invalid_enum",
            "canonical_name": "Test Invalid Enum",
            "primary_source": "Source Reference",
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "INVALID_ACCESS_CLASS",
            "license_status": "MIT",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",
            "verification_status": "VERIFIED",
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(any("Invalid access_class" in e for e in errors))

    def test_no_prohibited_payload_markers_in_registry(self) -> None:
        """Ensure no patient or case payloads exist in the registry data."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        payload_errors = check_no_payload_markers(data)
        self.assertEqual(len(payload_errors), 0, f"Payload markers found: {payload_errors}")

    def test_payload_marker_rejection(self) -> None:
        """Ensure check_no_payload_markers detects prohibited keys."""
        dirty_data = {
            "benchmark_id": "dirty_bench",
            "case_payload": "Patient presented with acute chest pain...",
        }
        errors = check_no_payload_markers(dirty_data)
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any("case_payload" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
