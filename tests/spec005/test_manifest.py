"""Corrective-maintenance tests for Spec 005 manifest pre-execution binding."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec005.device import build_device_execution_readiness_record
from src.commandmed.spec005.manifest import (
    build_spec004_projection,
    evaluate_spec005_preflight,
    validate_spec005_manifest,
)

ROOT = Path(__file__).resolve().parents[2]
QUALITY_CONTRACT_PATH = ROOT / "data/spec005/selection_quality_contract.json"
METRICS_V2_PATH = ROOT / "data/eval/metrics-v2.json"
DEVICE_CONTRACT_PATH = ROOT / "data/spec005/device_qualification_contract.json"
V1_SHA = "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a"
V2_SHA = "bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b"

GATES = (
    "R1",
    "T1",
    "D34",
    "G1",
    "G2",
    "G3",
    "G4",
    "S1",
    "P1",
    "C1",
    "H1",
    "I1",
    "F1",
)

CONTRACT_CANONICAL_HASH = "c0ffee" + "0" * 58


def make_device_contract():
    contract = json.loads(DEVICE_CONTRACT_PATH.read_text(encoding="utf-8"))
    contract["performance_threshold_policy"] = {
        "state": "FROZEN",
        "record_id": "PERF-THRESHOLD-SYNTHETIC-001",
        "record_canonical_sha256": "9" * 64,
        "resolution_rule": "MUST_BE_FROZEN_BEFORE_REAL_DEVICE_EXECUTION",
    }
    return contract


def make_device_records(contract=None):
    contract = contract or make_device_contract()
    records = []
    for target in contract["targets"]:
        target_id = target["target_id"]
        records.append(
            {
                "target_id": target_id,
                "candidate_id": "candidate-alpha",
                "candidate_role": "PRIMARY",
                "model_artifact_sha256": "f" * 64,
                "complete_bundle_sha256": "1" * 64,
                "complete_bundle_bytes": 563_035_840,
                "gguf_quantization": "Q4_0",
                "llama_cpp_core_revision": "2" * 40,
                "build_toolchain_identity": f"TOOLCHAIN_{target_id}",
                "runtime_artifact_sha256": "3" * 64,
                "wrapper_identity": f"WRAPPER_{target_id}",
                "memory_measurement_identity": f"MEMORY_{target_id}",
                "thermal_signal_identity": f"THERMAL_{target_id}",
                "energy_signal_identity": f"ENERGY_{target_id}",
                "execution_plan_sha256": "4" * 64,
            }
        )
    return records


def make_device_binding():
    contract = make_device_contract()
    records = make_device_records(contract)
    readiness = build_device_execution_readiness_record(records, contract)
    assert readiness["state"] == "PRE_EXECUTION_READY"
    return contract, records, compute_canonical_sha256(readiness)


def make_artifacts(**overrides):
    quality_contract = json.loads(
        QUALITY_CONTRACT_PATH.read_text(encoding="utf-8")
    )
    quality_contract["canonical_sha256"] = CONTRACT_CANONICAL_HASH
    device_contract, device_records, _ = make_device_binding()
    artifacts = {
        "metrics_v2_catalog": json.loads(METRICS_V2_PATH.read_text(encoding="utf-8")),
        "selection_quality_contract": quality_contract,
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
        "device_qualification_contract": device_contract,
        "device_execution_readiness_records": device_records,
    }
    artifacts.update(overrides)
    return artifacts


def make_manifest(**overrides):
    _, _, readiness_sha = make_device_binding()
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
            "selection_quality_contract_sha256": CONTRACT_CANONICAL_HASH,
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
            "protocol_version": "1.1",
            "execution_readiness_state": "PRE_EXECUTION_READY",
            "execution_readiness_record_sha256": readiness_sha,
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

    def test_device_ready_state_is_recomputed_not_caller_owned(self):
        artifacts = make_artifacts()
        artifacts["device_execution_readiness_records"] = artifacts[
            "device_execution_readiness_records"
        ][:-1]
        errors = validate_spec005_manifest(make_manifest(), artifacts)
        self.assertTrue(any("COMPUTED_DEVICE_EXECUTION_READINESS" in e for e in errors))

    def test_device_readiness_sha_is_exactly_bound(self):
        manifest = make_manifest()
        manifest["device_protocol_identity"]["execution_readiness_record_sha256"] = (
            "8" * 64
        )
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("READINESS_SHA_MISMATCH" in e for e in errors))

    def test_legacy_measured_preflight_state_cannot_satisfy_pre_execution_gate(self):
        manifest = make_manifest()
        manifest["device_protocol_identity"] = {
            "protocol_id": "commandmed-spec005-device-qualification-protocol",
            "protocol_version": "1.1",
            "preflight_state": "PREFLIGHT_PASS",
        }
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("LEGACY_DEVICE_PREFLIGHT" in e for e in errors))
        self.assertTrue(any("PRE_EXECUTION_READY" in e for e in errors))

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

    def test_declared_artifact_hashes_are_bound(self):
        artifacts = make_artifacts()
        artifacts["threshold_policies"][0]["record_canonical_sha256"] = "8" * 64
        errors = validate_spec005_manifest(make_manifest(), artifacts)
        self.assertTrue(any("THRESHOLD" in e.upper() and "SHA" in e.upper() for e in errors))

        errors = validate_spec005_manifest(make_manifest(), make_artifacts())
        self.assertEqual(errors, [])

    def test_design_hashes_are_bound(self):
        artifacts = make_artifacts()
        artifacts["statistical_designs"][0]["record_canonical_sha256"] = "7" * 64
        errors = validate_spec005_manifest(make_manifest(), artifacts)
        self.assertTrue(any("STATISTICAL" in e.upper() and "SHA" in e.upper() for e in errors))

    def test_quality_contract_hash_is_verified_when_supplied(self):
        manifest = make_manifest()
        manifest["selection_quality_contract_identity"][
            "selection_quality_contract_sha256"
        ] = "d" * 64
        errors = validate_spec005_manifest(manifest, make_artifacts())
        self.assertTrue(any("SELECTION_QUALITY_CONTRACT_SHA" in e for e in errors))

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

    def test_malformed_or_duplicate_id_sha_entries_rejected(self):
        artifacts = make_artifacts(
            threshold_policies=[
                {"threshold_policy_id": "TP-001", "record_canonical_sha256": "bad"},
            ]
        )
        errors = validate_spec005_manifest(make_manifest(), artifacts)
        self.assertTrue(
            any(
                "TP-001" in e and ("SHA" in e.upper() or "FORMAT" in e.upper())
                for e in errors
            )
        )
        artifacts = make_artifacts(
            threshold_policies=[
                {"threshold_policy_id": "TP-001", "record_canonical_sha256": "a" * 64},
                {"threshold_policy_id": "TP-001", "record_canonical_sha256": "b" * 64},
            ]
        )
        errors = validate_spec005_manifest(make_manifest(), artifacts)
        self.assertTrue(any("DUPLICATE" in e.upper() for e in errors))

    def test_activation_identity_required_for_projection_preflight(self):
        manifest = make_manifest()
        manifest["construction_activation_identity"] = {
            "activation_state": "AUTHORIZED_TO_CONSTRUCT"
        }
        result = evaluate_spec005_preflight(manifest, make_artifacts())
        self.assertNotEqual(result["state"], "PREFLIGHT_COMPLETE")

    def test_malformed_artifact_collections_do_not_crash(self):
        for bad in (None, "x", 42, {"a": 1}):
            artifacts = make_artifacts(
                threshold_policies=bad, statistical_designs=bad
            )
            errors = validate_spec005_manifest(make_manifest(), artifacts)
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)

    def test_projection_never_raises_on_preflight_blocked(self):
        manifest = make_manifest(candidate_admission_records=[{}])
        self.assertIsNone(build_spec004_projection(manifest, make_artifacts()))


class PreflightTests(unittest.TestCase):
    def test_complete_manifest_preflight_passes_with_synthetic_authorized_shape(self):
        manifest = make_manifest()
        manifest["construction_activation_identity"] = {
            "activation_id": "ACT-SYNTH-AUTH",
            "activation_record_canonical_sha256": "6" * 64,
            "preconstruction_snapshot_id": manifest[
                "preconstruction_snapshot_identity"
            ]["snapshot_id"],
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
        projection = build_spec004_projection(self._ready_manifest(), make_artifacts())
        self.assertIsNone(projection)
        result = evaluate_spec005_preflight(self._ready_manifest(), make_artifacts())
        self.assertTrue(
            any("A15" in c or "ACTIVATION_BINDING" in c for c in result["reason_codes"]),
            result["reason_codes"],
        )

    def test_projection_shape_matches_spec004_requirements(self):
        source = open(str(ROOT / "src/commandmed/tournament.py"), encoding="utf-8").read()
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
