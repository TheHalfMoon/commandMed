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

    def test_healthbench_family_multilingual_language_truth(self) -> None:
        """Third reconciliation Finding 1: HealthBench records must not make unsupported English-only claims."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        by_id = {b["benchmark_id"]: b for b in data}

        for hb_id in ["healthbench_core", "healthbench_consensus", "healthbench_hard", "healthbench_professional"]:
            rec = by_id[hb_id]
            self.assertEqual(
                rec["languages"],
                ["MULTILINGUAL"],
                f"{hb_id} must record the MULTILINGUAL sentinel, not an unsupported English-only claim",
            )
            # Sentinel semantics must be documented in the record notes.
            self.assertIn("MULTILINGUAL", rec["notes"])

    def test_healthbench_role_scope_truth(self) -> None:
        """Third reconciliation Finding 1: Consensus/Hard (and full-set Core) must not make clinician-only or guessed-role claims."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        by_id = {b["benchmark_id"]: b for b in data}

        for hb_id in ["healthbench_core", "healthbench_consensus", "healthbench_hard"]:
            self.assertEqual(
                by_id[hb_id]["roles"],
                ["MULTI_ROLE"],
                f"{hb_id} must use the broad MULTI_ROLE representation (subset role composition not proven without case inspection)",
            )

        # HealthBench Professional clinician-only role IS proven by its primary source
        # (every example is a physician-authored conversation with ChatGPT for Clinicians).
        self.assertEqual(by_id["healthbench_professional"]["roles"], ["CLINICAL_PROFESSIONAL"])

    def test_verified_benchmark_with_fake_license_status_fails(self) -> None:
        """Third reconciliation Finding 2: VERIFIED benchmark with an uncontrolled license string must FAIL validation."""
        sample = {
            "benchmark_id": "test_fake_license",
            "canonical_name": "Fake License Test",
            "primary_source": "Canonical Paper 2026",
            "source_uri": "https://example.com/source",
            "source_identifier": "arXiv:2601.00000",
            "source_revision": "v1.0",
            "verification_date": "2026-08-22",
            "artifact_version": "v1.0",
            "access_class": "PUBLIC",
            "license_status": "NOT_A_REAL_LICENSE",  # Outside controlled vocabulary!
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
        self.assertTrue(
            any("Invalid license_status 'NOT_A_REAL_LICENSE'" in e for e in errors),
            f"Uncontrolled license string must fail; got errors: {errors}",
        )

    def test_all_canonical_license_statuses_within_controlled_vocabulary(self) -> None:
        """Third reconciliation Finding 2: every license status in the canonical registry must be within the controlled vocabulary."""
        from src.commandmed.eval_contract.model import LicenseStatus

        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        vocabulary = {e.value for e in LicenseStatus}
        canonical_statuses = {b["license_status"] for b in data}
        self.assertTrue(
            canonical_statuses.issubset(vocabulary),
            f"Canonical registry contains license statuses outside the controlled vocabulary: {canonical_statuses - vocabulary}",
        )
        # Every canonical status also passes full benchmark validation via the registry-level test.

    def test_medhelm_bound_to_versioned_uri_not_latest(self) -> None:
        """Third reconciliation Finding 3: MedHELM v2.0.0 must be pinned to the versioned identity URI, not /latest/."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        medhelm = next(b for b in data if b["benchmark_id"] == "medhelm")
        self.assertEqual(medhelm["source_uri"], "https://crfm.stanford.edu/helm/medhelm/v2.0.0/")
        self.assertNotIn("/latest/", medhelm["source_uri"])
        self.assertNotIn("/latest/", medhelm["primary_source"])
        # The /latest/ URL may appear only in notes as a convenience reference.
        self.assertIn("v2.0.0", medhelm["notes"])

    def test_medmcqa_provenance_truth(self) -> None:
        """Final reconciliation Finding 1: MedMCQA canonical paper is arXiv:2203.14371 (not 2203.14381) and license is MIT."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "medmcqa")
        self.assertEqual(rec["source_identifier"], "arXiv:2203.14371")
        # The incorrect legacy ID must not survive in any identity-bearing field
        # (notes may document the correction for governance evidence).
        for field in ["source_identifier", "primary_source", "source_uri", "source_revision"]:
            self.assertNotIn("2203.14381", rec[field])
        self.assertEqual(rec["license_status"], "MIT")
        self.assertIn("c59ef14ca1990266c4107c7864b45a20fd93e5e0", rec["license_source_uri"])
        self.assertEqual(rec["source_revision"], "c59ef14ca1990266c4107c7864b45a20fd93e5e0")
        # MIXED access represents public train/dev data plus non-public official test ground truth.
        self.assertEqual(rec["access_class"], "MIXED")
        self.assertIn("Google Drive", rec["notes"])
        self.assertIn("withheld", rec["notes"])

    def test_medmcqa_not_executable_until_artifact_identity_resolved(self) -> None:
        """Final reconciliation Finding 1: MedMCQA is not executable until its data artifact identity is resolved."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "medmcqa")
        self.assertEqual(rec["verification_status"], "VERIFIED")
        self.assertEqual(rec["intended_use"], "REFERENCE_ONLY")
        self.assertEqual(rec["artifact_version"], "UNBOUND")

    def test_medqa_variant_label_not_source_revision(self) -> None:
        """Final reconciliation Finding 2: MedQA '4-option' is a variant label, never a source revision; record stays REFERENCE_ONLY."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "medqa_usmle")
        self.assertEqual(rec["source_revision"], "27b02f66aac217933c9648a06f82e9f720377925")
        self.assertNotEqual(rec["source_revision"], "4-option-usmle")
        # Variant information preserved as artifact metadata, not revision.
        self.assertIn("4-option", rec["artifact_version"])
        self.assertIn("UNBOUND", rec["artifact_version"])
        self.assertEqual(rec["intended_use"], "REFERENCE_ONLY")
        self.assertEqual(rec["verification_status"], "VERIFIED")
        self.assertIn("not yet identity-bound", rec["notes"])

    def test_pubmedqa_pinned_to_commit_and_pqal_blob(self) -> None:
        """Final reconciliation Finding 3: PubMedQA is pinned to repository commit + PQA-L git blob identity and stays executable DEVELOPMENT."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "pubmedqa")
        self.assertEqual(rec["source_revision"], "1cbae8e92f72f20c8d3747cbb3bf5bc53554d997")
        self.assertEqual(rec["artifact_version"], "data/ori_pqal.json")
        self.assertIn("38db7750761c78950ed32303e7545bdaa513390c", rec["notes"])
        self.assertEqual(rec["intended_use"], "DEVELOPMENT")
        self.assertEqual(rec["license_status"], "MIT")
        # Revision-pinned evidence URIs, not mutable master links.
        self.assertNotIn("/master/", rec["license_source_uri"])
        self.assertNotIn("/master/", rec["source_uri"])
        self.assertIn("/1cbae8e92f72f20c8d3747cbb3bf5bc53554d997/", rec["license_source_uri"])

    def test_medxpertqa_pinned_to_hf_dataset_revision(self) -> None:
        """Final reconciliation Finding 4: MedXpertQA is pinned to the official HF dataset revision, not the GitHub code repo."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "medxpertqa")
        self.assertEqual(rec["source_identifier"], "huggingface:datasets/TsinghuaC3I/MedXpertQA")
        self.assertEqual(rec["source_revision"], "7e7c465a68eb2b866926bfa59c8c9d17a8daba65")
        self.assertEqual(
            rec["source_uri"],
            "https://huggingface.co/datasets/TsinghuaC3I/MedXpertQA/tree/7e7c465a68eb2b866926bfa59c8c9d17a8daba65",
        )
        self.assertIn("/7e7c465a68eb2b866926bfa59c8c9d17a8daba65/", rec["license_source_uri"])
        self.assertNotEqual(rec["source_revision"], "v1.0")
        self.assertEqual(rec["intended_use"], "DEVELOPMENT")
        self.assertEqual(rec["license_status"], "MIT")
        # Split artifacts and quarantine boundary documented.
        self.assertIn("Text/dev.jsonl", rec["artifact_version"])
        self.assertIn("MM/test.jsonl", rec["artifact_version"])
        self.assertIn("can_select_model=false", rec["notes"])

    def test_medabstain_family_component_specific_boundary(self) -> None:
        """Final reconciliation Finding 5: MedAbstain family is COMPONENT_SPECIFIC + MIXED + REFERENCE_ONLY with both license facts in notes."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))
        rec = next(b for b in data if b["benchmark_id"] == "medabstain")
        self.assertEqual(rec["access_class"], "MIXED")
        self.assertEqual(rec["license_status"], "COMPONENT_SPECIFIC")
        self.assertEqual(rec["intended_use"], "REFERENCE_ONLY")
        self.assertEqual(rec["verification_status"], "VERIFIED")
        self.assertEqual(rec["source_revision"], "091e5c22111fffeb51c0c2e69b65d0a21a1e4164")
        # BOTH license facts preserved.
        self.assertIn("CC-BY-NC-4.0", rec["notes"])
        self.assertIn("registered separately", rec["notes"])

    def test_source_verified_does_not_imply_development_authority(self) -> None:
        """Final reconciliation Finding 6: family-level VERIFIED does not imply DEVELOPMENT; only artifact-bound assets are executable."""
        data = json.loads(self.benchmarks_file.read_text(encoding="utf-8"))

        reference_only = {b["benchmark_id"] for b in data if b["intended_use"] == "REFERENCE_ONLY"}
        self.assertEqual(
            reference_only,
            {"medabstain", "medhelm", "medmcqa", "medqa_usmle", "medqabstain"},
            "REFERENCE_ONLY set must exactly match the reconciled registry state",
        )

        # VERIFIED + REFERENCE_ONLY is a valid family state (source truth known, executable identity intentionally gated).
        for bid in ["medabstain", "medhelm", "medmcqa", "medqa_usmle"]:
            rec = next(b for b in data if b["benchmark_id"] == bid)
            self.assertEqual(rec["verification_status"], "VERIFIED", f"{bid} family source truth is verified")

        # Every executable DEVELOPMENT asset must carry a concrete (non-UNBOUND) artifact identity.
        for rec in data:
            if rec["intended_use"] == "DEVELOPMENT":
                self.assertNotIn(
                    "UNBOUND",
                    rec["artifact_version"],
                    f"Executable DEVELOPMENT asset {rec['benchmark_id']} must be artifact-identity-bound",
                )

        # Whole registry still validates.
        is_valid, errors = validate_benchmark_registry(data)
        self.assertTrue(is_valid, f"canonical registry failed validation: {errors}")


if __name__ == "__main__":
    unittest.main()
