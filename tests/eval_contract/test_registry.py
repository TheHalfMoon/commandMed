"""Tests for benchmark registry validation and required initial families."""

import json
from pathlib import Path
import unittest

from src.commandmed.eval_contract.model import AccessClass, IntendedUse, VerificationStatus
from src.commandmed.eval_contract.validate import (
    check_no_payload_markers,
    validate_benchmark,
    validate_benchmark_registry,
)


class TestBenchmarkRegistry(unittest.TestCase):
    """Tests for the benchmark registry contract and evidence-bound rules."""

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

    def test_all_fr002_required_benchmark_families_accounted_for(self) -> None:
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

        # Check breakdown: 10 verified, 1 explicitly unresolved
        verified = [b for b in data if b["verification_status"] == VerificationStatus.VERIFIED.value]
        unresolved = [b for b in data if b["verification_status"] == VerificationStatus.UNRESOLVED.value]
        self.assertEqual(len(verified), 10)
        self.assertEqual(len(unresolved), 1)
        self.assertEqual(unresolved[0]["benchmark_id"], "medqabstain")
        self.assertEqual(unresolved[0]["intended_use"], IntendedUse.REFERENCE_ONLY.value)

    def test_verified_benchmark_with_unresolved_license_fails(self) -> None:
        """Finding 2: VERIFIED benchmark cannot have license_status='UNRESOLVED'."""
        sample = {
            "benchmark_id": "test_unresolved_license",
            "canonical_name": "Test Benchmark",
            "primary_source": "Canonical Paper 2026",
            "source_uri": "https://example.com/source",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v1.0",
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "UNRESOLVED",  # Unresolved license!
            "license_source_uri": "UNRESOLVED",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",
            "verification_status": "VERIFIED",  # Contradiction!
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(any("license_status='UNRESOLVED' cannot have verification_status='VERIFIED'" in e for e in errors))

    def test_verified_benchmark_with_unresolved_source_fails(self) -> None:
        """Finding 2: VERIFIED benchmark cannot have unresolved source_uri or primary_source."""
        sample = {
            "benchmark_id": "test_unresolved_source",
            "canonical_name": "Test Benchmark",
            "primary_source": "Canonical Paper 2026",
            "source_uri": "UNRESOLVED",  # Unresolved source URI!
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v1.0",
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "MIT",
            "license_source_uri": "https://example.com/LICENSE",
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
        self.assertTrue(any("resolved source_uri" in e for e in errors))

    def test_unresolved_benchmark_with_development_use_fails(self) -> None:
        """Finding 2: UNRESOLVED benchmark cannot have intended_use='DEVELOPMENT' or 'POSSIBLE_RELEASE_GATE'."""
        sample = {
            "benchmark_id": "test_unresolved_dev_use",
            "canonical_name": "Test Benchmark",
            "primary_source": "Paper 2026",
            "source_uri": "https://example.com",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "UNRESOLVED",
            "verification_date": "2026-08-21",
            "artifact_version": "UNRESOLVED",
            "access_class": "PUBLIC",
            "license_status": "UNRESOLVED",
            "license_source_uri": "UNRESOLVED",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",  # Prohibited for UNRESOLVED benchmark!
            "verification_status": "UNRESOLVED",
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(any("UNRESOLVED benchmark cannot have executable intended_use 'DEVELOPMENT'" in e for e in errors))

    def test_unresolved_benchmark_with_reference_only_use_passes(self) -> None:
        """UNRESOLVED benchmark with REFERENCE_ONLY is valid fail-closed behavior."""
        sample = {
            "benchmark_id": "test_unresolved_ref_use",
            "canonical_name": "Test Benchmark",
            "primary_source": "Paper 2026",
            "source_uri": "https://example.com",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "UNRESOLVED",
            "verification_date": "2026-08-21",
            "artifact_version": "UNRESOLVED",
            "access_class": "PUBLIC",
            "license_status": "UNRESOLVED",
            "license_source_uri": "UNRESOLVED",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "REFERENCE_ONLY",
            "verification_status": "UNRESOLVED",
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertEqual(len(errors), 0)

    def test_missing_required_field_rejection(self) -> None:
        """Validation fails if any required field is missing or null."""
        sample = {
            "benchmark_id": "test_missing",
            "canonical_name": "Test Benchmark",
            # primary_source missing
            "source_uri": "https://example.com",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v1.0",
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "MIT",
            "license_source_uri": "https://example.com/LICENSE",
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
            "source_uri": "https://example.com",
            "source_identifier": "ID",
            "source_revision": "v1.0",
            "verification_date": "2026-08-21",
            "artifact_version": "v1.0",
            "access_class": "INVALID_ACCESS_CLASS",
            "license_status": "MIT",
            "license_source_uri": "https://example.com/LICENSE",
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

    def test_component_specific_license_with_development_use_fails(self) -> None:
        """Finding 3: A mixed-family record with COMPONENT_SPECIFIC license cannot silently become executable DEVELOPMENT."""
        sample = {
            "benchmark_id": "test_mixed_family",
            "canonical_name": "Mixed Framework Family",
            "primary_source": "Framework Reference",
            "source_uri": "https://example.com/framework",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v2.0.0",
            "verification_date": "2026-08-22",
            "artifact_version": "v2.0.0",
            "access_class": "MIXED",
            "license_status": "COMPONENT_SPECIFIC",
            "license_source_uri": "https://example.com/framework/LICENSE",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",
            "verification_status": "VERIFIED",
            "notes": "Framework-only license must not authorize component data execution.",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(
            any("license_status='COMPONENT_SPECIFIC' cannot have executable intended_use 'DEVELOPMENT'" in e for e in errors)
        )

    def test_component_specific_license_with_reference_only_use_passes(self) -> None:
        """Finding 3: COMPONENT_SPECIFIC license state validates only with REFERENCE_ONLY family use."""
        sample = {
            "benchmark_id": "test_mixed_family_ref",
            "canonical_name": "Mixed Framework Family",
            "primary_source": "Framework Reference",
            "source_uri": "https://example.com/framework",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v2.0.0",
            "verification_date": "2026-08-22",
            "artifact_version": "v2.0.0",
            "access_class": "MIXED",
            "license_status": "COMPONENT_SPECIFIC",
            "license_source_uri": "https://example.com/framework/LICENSE",
            "languages": ["en"],
            "roles": ["CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "REFERENCE_ONLY",
            "verification_status": "VERIFIED",
            "notes": "Family record is reference-only; components registered individually before execution.",
        }
        errors = validate_benchmark(sample)
        self.assertEqual(len(errors), 0)

    def test_duplicate_set_like_metadata_values_fail(self) -> None:
        """Hardening: duplicate values in set-like fields (languages, roles, modalities) must fail, not be silently deduplicated."""
        sample = {
            "benchmark_id": "test_duplicate_sets",
            "canonical_name": "Duplicate Set Test",
            "primary_source": "Source Reference",
            "source_uri": "https://example.com",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v1.0",
            "verification_date": "2026-08-22",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "MIT",
            "license_source_uri": "https://example.com/LICENSE",
            "languages": ["en", "en"],
            "roles": ["CLINICAL_PROFESSIONAL", "CLINICAL_PROFESSIONAL"],
            "modalities": ["TEXT", "TEXT"],
            "capability_domains": ["KNOWLEDGE"],
            "contamination_sensitivity": "HIGH",
            "intended_use": "DEVELOPMENT",
            "verification_status": "VERIFIED",
            "notes": "Test notes",
        }
        errors = validate_benchmark(sample)
        self.assertTrue(any("Duplicate values found in set-like field 'languages'" in e for e in errors))
        self.assertTrue(any("Duplicate values found in set-like field 'roles'" in e for e in errors))
        self.assertTrue(any("Duplicate values found in set-like field 'modalities'" in e for e in errors))

    def test_corrected_canonical_benchmark_source_identities(self) -> None:
        """Finding 1/2: corrected canonical registry binds HealthBench to official HF datasets and MedHELM to arXiv:2505.23802 v2.0.0."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        by_id = {b["benchmark_id"]: b for b in data}

        for hb_id, artifact in [
            ("healthbench_core", "2025-05-07-06-14-12_oss_eval.jsonl"),
            ("healthbench_consensus", "consensus_2025-05-09-20-00-46.jsonl"),
            ("healthbench_hard", "hard_2025-05-08-21-00-10.jsonl"),
        ]:
            rec = by_id[hb_id]
            self.assertEqual(rec["source_uri"], "https://huggingface.co/datasets/openai/healthbench")
            self.assertEqual(rec["source_identifier"], "huggingface:datasets/openai/healthbench")
            self.assertEqual(rec["source_revision"], "40ee1968852fc57f625934251ac22be47077a8fb")
            self.assertEqual(rec["artifact_version"], artifact)
            self.assertEqual(rec["license_status"], "MIT")
            self.assertIn("huggingface.co/datasets/openai/healthbench", rec["license_source_uri"])

        pro = by_id["healthbench_professional"]
        self.assertEqual(pro["source_uri"], "https://huggingface.co/datasets/openai/healthbench-professional")
        self.assertEqual(pro["source_identifier"], "huggingface:datasets/openai/healthbench-professional")
        self.assertEqual(pro["source_revision"], "349962fd46dd02343a0d8a606491baf59154ea1a")
        self.assertEqual(pro["artifact_version"], "healthbench_professional_eval.jsonl")
        self.assertEqual(pro["license_status"], "MIT")
        self.assertIn("arXiv:2604.27470", pro["primary_source"])

        medhelm = by_id["medhelm"]
        self.assertEqual(medhelm["source_identifier"], "arXiv:2505.23802")
        self.assertEqual(medhelm["source_revision"], "v2.0.0")
        self.assertEqual(medhelm["artifact_version"], "v2.0.0")
        self.assertEqual(medhelm["access_class"], "MIXED")
        self.assertEqual(medhelm["license_status"], "COMPONENT_SPECIFIC")
        self.assertEqual(medhelm["intended_use"], "REFERENCE_ONLY")
        self.assertEqual(medhelm["verification_status"], "VERIFIED")
        self.assertNotIn("arXiv:2408.01242", medhelm["source_identifier"])


if __name__ == "__main__":
    unittest.main()
