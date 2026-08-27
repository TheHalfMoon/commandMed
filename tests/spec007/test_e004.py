"""Synthetic tests for the E004 execution request envelope."""

from __future__ import annotations

import unittest
from pathlib import Path

from src.commandmed.spec007.e004 import (
    build_e004_execution_request,
    validate_e004_execution_plan,
)

ROOT = Path(__file__).resolve().parents[2]


def make_plan(**overrides):
    plan = {
        "plan_id": "E004-SYNTHETIC-PLAN-001",
        "plan_version": "1.0",
        "candidate_id": "Qwen/Qwen3.5-0.8B-Base",
        "candidate_revision": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
        "e001_manifest_sha256": "9" * 64,
        "e002_authorization_git_blob": "a25fb2bdbe62f2d59f6624d6aa60b020e09dcbaf",
        "e003_authorization_git_blob": "52b557b54a152204f4451ec9c497f43dbd6f0058",
        "model_artifact_access_authority": "AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY",
        "e003_execution_authority": "AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY",
        "benchmark_payload_execution_authority": "AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY",
        "a15_activation_id": "A15-SYNTHETIC-ACTIVATION-001",
        "a15_activation_record_sha256": "1" * 64,
        "preconstruction_snapshot_sha256": "2" * 64,
        "spec005_preflight_state": "PREFLIGHT_COMPLETE",
        "device_execution_readiness_sha256": "3" * 64,
        "device_execution_readiness_state": "PRE_EXECUTION_READY",
        "model_artifact_sha256": "4" * 64,
        "evaluation_artifact_sha256": "5" * 64,
        "evaluation_input_class": "PUBLIC_UNGATED",
        "evaluation_purpose": "CHECKPOINT_SELECTION",
        "lineage_record_sha256": "6" * 64,
        "lineage_state": "ELIGIBLE",
        "contamination_evidence_sha256": "7" * 64,
        "contamination_state": "ASSESSED_CLEAN",
        "runtime_entrypoint": "llama-cli",
        "runtime_executable_sha256": "8" * 64,
        "llama_cpp_core_revision": "c" * 40,
        "tokenizer_config_sha256": "a" * 64,
        "environment_manifest_sha256": "b" * 64,
        "argv": [
            "llama-cli",
            "--model-id",
            "Qwen/Qwen3.5-0.8B-Base",
            "--evaluation-manifest",
            "EVAL-SYNTHETIC-001",
        ],
        "expected_raw_output_artifact_id": "E004-RAW-SYNTHETIC-001",
        "no_spend_assertion": True,
        "no_credentials_assertion": True,
    }
    plan.update(overrides)
    return plan


class E004PlanValidationTests(unittest.TestCase):
    def test_valid_synthetic_plan_validates(self):
        self.assertEqual(validate_e004_execution_plan(make_plan()), [])

    def test_unresolved_contamination_blocks(self):
        errors = validate_e004_execution_plan(
            make_plan(contamination_state="NOT_ASSESSED")
        )
        self.assertTrue(any("contamination_state" in error for error in errors))

    def test_e003_authority_cannot_be_self_widened(self):
        errors = validate_e004_execution_plan(
            make_plan(e003_execution_authority="AUTHORIZED_ANY_MODEL")
        )
        self.assertTrue(any("e003_execution_authority" in error for error in errors))

    def test_device_readiness_must_be_pre_execution_ready(self):
        errors = validate_e004_execution_plan(
            make_plan(device_execution_readiness_state="INCOMPLETE")
        )
        self.assertTrue(any("device_execution_readiness_state" in error for error in errors))

    def test_credential_flags_are_prohibited(self):
        errors = validate_e004_execution_plan(
            make_plan(argv=["llama-cli", "--api-key", "secret-value"])
        )
        self.assertTrue(any("CREDENTIAL_OR_SECRET" in error for error in errors))

    def test_shell_entrypoints_are_prohibited(self):
        errors = validate_e004_execution_plan(
            make_plan(runtime_entrypoint="bash", argv=["bash", "-c", "echo unsafe"])
        )
        self.assertTrue(any("SHELL_ENTRYPOINT" in error for error in errors))

    def test_private_gold_marker_is_prohibited(self):
        errors = validate_e004_execution_plan(
            make_plan(expected_raw_output_artifact_id="PRIVATE_GOLD_OUTPUT")
        )
        self.assertTrue(any("PROHIBITED_PAYLOAD" in error for error in errors))

    def test_unknown_field_fails_closed(self):
        plan = make_plan()
        plan["execute_now"] = True
        errors = validate_e004_execution_plan(plan)
        self.assertTrue(any("undeclared fields" in error for error in errors))

    def test_malformed_plan_fails_closed(self):
        for bad in (None, [], "x", 7):
            errors = validate_e004_execution_plan(bad)
            self.assertTrue(errors)


class E004RequestTests(unittest.TestCase):
    def test_valid_plan_builds_identity_bound_request_without_execution(self):
        result = build_e004_execution_request(make_plan())
        self.assertEqual(result["state"], "READY_FOR_EXTERNAL_EXECUTOR")
        self.assertIs(result["execution_performed"], False)
        self.assertEqual(len(result["request_canonical_sha256"]), 64)
        self.assertIsNotNone(result["request"])

    def test_invalid_plan_never_builds_request(self):
        result = build_e004_execution_request(
            make_plan(spec005_preflight_state="PREFLIGHT_BLOCKED")
        )
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIs(result["execution_performed"], False)
        self.assertIsNone(result["request"])

    def test_request_identity_is_deterministic(self):
        left = build_e004_execution_request(make_plan())
        right = build_e004_execution_request(make_plan())
        self.assertEqual(
            left["request_canonical_sha256"], right["request_canonical_sha256"]
        )

    def test_module_has_no_external_execution_import(self):
        source = (ROOT / "src/commandmed/spec007/e004.py").read_text(encoding="utf-8")
        for banned in (
            "import subprocess",
            "from subprocess",
            "import socket",
            "import requests",
            "import urllib",
            "os.system(",
        ):
            self.assertNotIn(banned, source)


if __name__ == "__main__":
    unittest.main()
