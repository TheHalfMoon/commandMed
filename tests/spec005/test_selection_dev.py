"""Synthetic tests for the Spec 005 selection-dev manifest contract."""

from __future__ import annotations

import unittest

from src.commandmed.spec005.selection_dev import (
    EXPLICIT_NONE,
    METRICS_CATALOG_PATH,
    METRICS_CONTRACT_SCHEMA_ID,
    METRICS_CONTRACT_SCHEMA_VERSION,
    METRICS_V2_SHA256,
    compute_selection_dev_manifest_sha256,
    validate_selection_dev_manifest,
)


def make_case(
    case_id: str,
    *,
    lane: str = "B_PATIENT_CAREGIVER_CLINICAL_SAFETY",
    language: str = "en",
    role: str = "PATIENT_CAREGIVER",
    purpose: str = "DEV",
    root_id: str = EXPLICIT_NONE,
    pair_id: str = EXPLICIT_NONE,
    contamination: str = "CONTAM-EVIDENCE-001",
):
    return {
        "case_id": case_id,
        "root_case_id_or_explicit_none": root_id,
        "quality_lane": lane,
        "role": role,
        "language_or_explicit_not_applicable": language,
        "use_context_or_task_stratum": "SYNTHETIC_TEST_STRATUM",
        "source_component_id": "SYNTHETIC_COMPONENT",
        "quarantine_purpose": purpose,
        "metric_id_or_metric_mapping_id": "SYNTHETIC_METRIC_MAPPING",
        "pair_id_or_explicit_none": pair_id,
        "fold_id_or_explicit_none": EXPLICIT_NONE,
        "artifact_identity": "SYNTHETIC_ARTIFACT-001",
        "source_revision": "SYNTHETIC_REVISION-001",
        "contamination_evidence_identity_or_unresolved_state": contamination,
    }


def make_manifest(cases=None):
    if cases is None:
        cases = [make_case("CASE-001")]
    manifest = {
        "manifest_id": "SPEC005-SELECTION-DEV-SYNTHETIC-V1",
        "schema_version": "1.0",
        "metrics_contract_schema_id": METRICS_CONTRACT_SCHEMA_ID,
        "metrics_contract_schema_version": METRICS_CONTRACT_SCHEMA_VERSION,
        "metrics_catalog_path": METRICS_CATALOG_PATH,
        "metrics_catalog_sha256": METRICS_V2_SHA256,
        "candidate_neutral": True,
        "pre_result_freeze": True,
        "case_records": cases,
        "manifest_canonical_sha256": "0" * 64,
    }
    manifest["manifest_canonical_sha256"] = compute_selection_dev_manifest_sha256(
        manifest
    )
    return manifest


class SelectionDevManifestTests(unittest.TestCase):
    def test_valid_synthetic_manifest(self):
        self.assertEqual(validate_selection_dev_manifest(make_manifest()), [])

    def test_execution_ready_requires_resolved_contamination(self):
        manifest = make_manifest(
            [make_case("CASE-001", contamination="UNRESOLVED")]
        )
        self.assertEqual(validate_selection_dev_manifest(manifest), [])
        errors = validate_selection_dev_manifest(manifest, execution_ready=True)
        self.assertTrue(any("contamination" in error for error in errors))

    def test_private_gold_is_prohibited_for_selection_dev_manifest(self):
        manifest = make_manifest([make_case("CASE-001", purpose="PRIVATE_GOLD")])
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("quarantine_purpose" in error for error in errors))

    def test_train_is_prohibited_for_selection_dev_manifest(self):
        manifest = make_manifest([make_case("CASE-001", purpose="TRAIN")])
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("quarantine_purpose" in error for error in errors))

    def test_duplicate_case_identity_fails(self):
        manifest = make_manifest([make_case("CASE-001"), make_case("CASE-001")])
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("duplicate 'CASE-001'" in error for error in errors))

    def test_lane_e_requires_complete_matched_pair(self):
        arabic = make_case(
            "PAIR-1-AR",
            lane="E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
            language="ar",
            role="CLINICAL_PROFESSIONAL",
            purpose="CHECKPOINT_SELECTION",
            root_id="ROOT-PAIR-1",
            pair_id="PAIR-1",
        )
        manifest = make_manifest([arabic])
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("exactly one ar and one en" in error for error in errors))

    def test_lane_e_valid_pair_requires_shared_root(self):
        arabic = make_case(
            "PAIR-1-AR",
            lane="E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
            language="ar",
            role="CLINICAL_PROFESSIONAL",
            purpose="CHECKPOINT_SELECTION",
            root_id="ROOT-PAIR-1",
            pair_id="PAIR-1",
        )
        english = make_case(
            "PAIR-1-EN",
            lane="E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
            language="en",
            role="CLINICAL_PROFESSIONAL",
            purpose="CHECKPOINT_SELECTION",
            root_id="ROOT-PAIR-1",
            pair_id="PAIR-1",
        )
        self.assertEqual(validate_selection_dev_manifest(make_manifest([arabic, english])), [])

    def test_lane_e_mismatched_root_fails(self):
        arabic = make_case(
            "PAIR-1-AR",
            lane="E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
            language="ar",
            purpose="CHECKPOINT_SELECTION",
            root_id="ROOT-A",
            pair_id="PAIR-1",
        )
        english = make_case(
            "PAIR-1-EN",
            lane="E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
            language="en",
            purpose="CHECKPOINT_SELECTION",
            root_id="ROOT-B",
            pair_id="PAIR-1",
        )
        errors = validate_selection_dev_manifest(make_manifest([arabic, english]))
        self.assertTrue(any("share one resolved root_case_id" in error for error in errors))

    def test_manifest_hash_is_case_order_invariant(self):
        first = make_manifest([make_case("CASE-002"), make_case("CASE-001")])
        second = make_manifest([make_case("CASE-001"), make_case("CASE-002")])
        self.assertEqual(
            first["manifest_canonical_sha256"],
            second["manifest_canonical_sha256"],
        )

    def test_manifest_hash_mismatch_fails(self):
        manifest = make_manifest()
        manifest["candidate_neutral"] = False
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("candidate_neutral" in error for error in errors))
        self.assertTrue(any("canonical SHA mismatch" in error for error in errors))

    def test_metrics_v2_binding_is_exact(self):
        manifest = make_manifest()
        manifest["metrics_catalog_sha256"] = "f" * 64
        manifest["manifest_canonical_sha256"] = compute_selection_dev_manifest_sha256(
            manifest
        )
        errors = validate_selection_dev_manifest(manifest)
        self.assertTrue(any("metrics-v2 SHA" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
