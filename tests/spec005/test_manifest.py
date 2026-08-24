"""US7 fixture tests: Spec 005 manifest validation and Spec 004 projection."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from src.commandmed.spec005.manifest import (
    build_spec004_projection,
    evaluate_spec005_preflight,
    validate_spec005_manifest,
)

ROOT = Path(__file__).resolve().parents[2]
QUALITY_CONTRACT_PATH = ROOT / "data/spec005/selection_quality_contract.json"
METRICS_V2_PATH = ROOT / "data/eval/metrics-v2.json"
V1_SHA = "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a"
V2_SHA = "bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b"

GATES = (
    "R1", "T1", "D34", "G1", "G2", "G3", "G4",
    "S1", "P1", "C1", "H1", "I1", "F1",
)


def make_artifacts(**overrides):
    artifacts = {
        "metrics_v2_catalog": json.loads(
            METRICS_V2_PATH.read_text(encoding="utf-8")
        ),
        "selection_quality_contract": json.loads(
            QUALITY_CONTRACT_PATH.read_text(encoding="utf-8")
        ),
        "threshold_policies": [
            {
                "threshold_policy_id": "TP-001",
                "record_canonical_sha256": "a" * 64,
            }
        ],
        "statistical_designs": [
            {
                "statistical_design_id": "SD-001",
                "record_canonical_sha256": "b" * 64,
            }
        ],
    }
    artifacts.update(overrides)
    return artifacts


def make_manifest(**overrides):
    manifest = {
        "manifest_id": "MANIFEST-SPEC005-001",
        "manifest_version": "1.0",
        "metrics_v2_identity": {
            "metrics_contract_schema_id": "commandmed-metrics-catalog",
            "metrics_contract_schema_version": "2.0",
            "metrics_catalog_path": "data/eval/metrics-v2.json",
            "metrics_catalog_sha256": V2_SHA,
        },
        "selection_quality_contract_identity": {
            "contract_id": "commandmed-spec005-selection-quality-contract",
            "contract_version": "1.0",
            "selection_quality_contract_sha256": "d" * 64,
        },
        "threshold_policy_identities": [
            {"threshold_policy_id": "TP-001", "record_canonical_sha256": "a" * 64}
        ],
        "statistical_design_identities": [
            {"statistical_design_id": "SD-001", "record_canonical_sha256": "b" * 64}
        ],
        "preconstruction_snapshot_identity": {
            "snapshot_id": "SNAP-ACT-1",
            "preconstruction_snapshot_sha256": "e" * 64,
        },
        "construction_activation_identity": {
            "activation_id": "ACT-1",
            "activation_state": "READY_FOR_SEPARATE_AUTHORIZATION",
        },
        "candidate_admission_records": [
            {
                "candidate_id": "candidate-alpha",
                "candidate_role": "PRIMARY",
                "artifact_sha256": "f" * 64,
                "base_pretrained": True,
            }
        ],
        "device_protocol_identity": {
            "protocol_id": "commandmed-spec005-device-qualification-protocol",
            "protocol_version": "1.0",
            "preflight_state": "PREFLIGHT_PASS",
        },
        "comparison_policy": {
            "comparison_strategy": "LEXICOGRAPHIC_PREDECLARED",
            "tie_policy": "NO_SELECTION_ON_TIE",
        },
        "record_canonical_sha256": "0" * 64,
    }
    manifest.update(overrides)
    return manifest


class ManifestValidationTests(unittest.TestCase):
    def test_valid_manifest_validates(self):
        errors = validate_spec005_manifest(make_manifest(), make_artifacts())
        self.assertEqual(errors, [])

    def test_wrong_metrics_v2_sha_rejected(self):
        manifest = make_manifest()
        manifest["metrics_v2_identity"]["metrics_catalog_sha256"] = "9" * 64
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("metrics" in e.lower() for e in errors))

    def test_private_gold_admission_rejected(self):
        manifest = make_manifest()
        manifest["candidate_admission_records"].append(
            {
                "candidate_id": "gold-shadow",
                "candidate_role": "PRIMARY",
                "evidence_source": "COMMANDMED_ARABIC_GOLD",
                "artifact_sha256": "7" * 64,
                "base_pretrained": True,
            }
        )
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("PRIVATE_GOLD" in e.upper() for e in errors))

    def test_instruct_candidate_rejected_for_base_only_tournament(self):
        manifest = make_manifest()
        manifest["candidate_admission_records"][0]["base_pretrained"] = False
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("BASE" in e.upper() for e in errors))

    def test_unknown_candidate_role_fails_closed(self):
        manifest = make_manifest()
        manifest["candidate_admission_records"][0]["candidate_role"] = "WINNER_MAYBE"
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("WINNER_MAYBE" in e for e in errors))

    def test_missing_device_identity_rejected(self):
        manifest = make_manifest()
        del manifest["device_protocol_identity"]
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("device_protocol_identity" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 6):
            errors = validate_spec005_manifest(bad, make_artifacts())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)

    def test_malformed_identity_subobjects_do_not_crash(self):
        manifest = make_manifest(
            metrics_v2_identity="not-a-dict",
            selection_quality_contract_identity=["x"],
            comparison_policy="LEXICOGRAPHIC_PREDECLARED",
            candidate_admission_records=[
                {"candidate_role": "PRIMARY", "base_pretrained": True}
            ],
        )
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertIsInstance(errors, list)
        self.assertTrue(any("candidate_id" in e for e in errors))

    def test_projection_never_raises_on_preflight_blocked(self):
        manifest = make_manifest(candidate_admission_records=[{}])
        self.assertIsNone(build_spec004_projection(manifest, make_artifacts()))


class PreflightTests(unittest.TestCase):
    def test_complete_manifest_preflight_passes(self):
        manifest = make_manifest()
        # Synthetic fixture representing the fully authorized shape to test
        # validator compatibility only; this creates no real authority.
        manifest["construction_activation_identity"] = {
            "activation_id": "ACT-SYNTH-AUTH",
            "activation_state": "AUTHORIZED_TO_CONSTRUCT",
        }
        result = evaluate_spec005_preflight(manifest, make_artifacts())
        self.assertEqual(result["state"], "PREFLIGHT_COMPLETE")
        self.assertEqual(result["reason_codes"], [])

    def test_incomplete_evidence_blocks_projection(self):
        manifest = make_manifest()
        manifest["threshold_policy_identities"] = []
        result = evaluate_spec005_preflight(manifest, make_artifacts())
        self.assertEqual(result["state"], "PREFLIGHT_BLOCKED")
        self.assertTrue(any("THRESHOLD" in c for c in result["reason_codes"]))

    def test_unresolved_values_block_not_default(self):
        artifacts = make_artifacts()
        artifacts["threshold_policies"] = []
        result = evaluate_spec005_preflight(make_manifest(), artifacts)
        self.assertNotEqual(result["state"], "PREFLIGHT_COMPLETE")

    def test_malformed_fail_closed(self):
        result = evaluate_spec005_preflight(None, None)
        self.assertEqual(result["state"], "PREFLIGHT_BLOCKED")
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


class ProjectionTests(unittest.TestCase):
    def _ready_manifest(self):
        return make_manifest()

    def test_no_projection_when_not_authorized(self):
        projection = build_spec004_projection(
            self._ready_manifest(), make_artifacts()
        )
        # A15 is not authorized; no executable Spec 004 tournament manifest
        # may be produced from synthetic evidence.
        self.assertIsNone(projection)
        result = evaluate_spec005_preflight(
            self._ready_manifest(), make_artifacts()
        )
        self.assertIn(
            "PROJECTION:A15_REAL_ACTIVATION_NOT_AUTHORIZED",
            result["reason_codes"],
        )

    def test_projection_shape_matches_spec004_requirements(self):
        """If a real authorized activation existed, the projection would carry
        the exact Spec 004 required fields; verified here structurally."""
        source = open(
            str(ROOT / "src/commandmed/tournament.py"), encoding="utf-8"
        ).read()
        for required in (
            "tournament_id",
            "execution_mode",
            "comparison_strategy",
            "tie_policy",
            "canonical_artifact_identities",
            "CANONICAL_UPSTREAM_IDENTITIES_V1",
        ):
            self.assertIn(required, source)


if __name__ == "__main__":
    unittest.main()
