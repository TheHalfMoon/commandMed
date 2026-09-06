from __future__ import annotations

import copy
import inspect
import json
import unittest
from pathlib import Path

from src.commandmed.spec007 import e004_transformers_adapter as adapter
from src.commandmed.spec007.e004_transformers_adapter import (
    CONTROL_CANDIDATE,
    GRANITE_CANDIDATE,
    LOADER_POLICY,
    PYTHON_RUNTIME_SHA256,
    RESOURCE_GENERATION_CONTRACT,
    SCORING_CONTRACT,
    TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
    TRANSFORMERS_SOURCE_REVISION,
    build_e004_transformers_adapter_manifest,
    normalized_log_likelihood_argmax,
    validate_e004_transformers_adapter_manifest,
)


ASSET_SET = json.loads(
    Path(
        "specs/007-sft-v1/e004-research-component-tournament-evaluation-assets-v1.json"
    ).read_text(encoding="utf-8")
)
BUNDLE_SET = json.loads(
    Path(
        "specs/007-sft-v1/e004-successor-candidate-artifact-bundle-set-v1.json"
    ).read_text(encoding="utf-8")
)


class TestE004TransformersAdapter(unittest.TestCase):
    def _build(self, pair: tuple[str, str]) -> dict:
        return build_e004_transformers_adapter_manifest(
            ASSET_SET,
            BUNDLE_SET,
            candidate_id=pair[0],
            upstream_revision=pair[1],
        )

    def test_granite_and_control_manifests_are_deterministic_and_valid(self) -> None:
        for pair in (GRANITE_CANDIDATE, CONTROL_CANDIDATE):
            first = self._build(pair)
            second = self._build(pair)
            self.assertEqual(first, second)
            self.assertEqual(
                validate_e004_transformers_adapter_manifest(first, ASSET_SET, BUNDLE_SET),
                [],
            )
            self.assertFalse(first["execution_performed"])
            self.assertEqual(first["authorized_spend_usd"], 0)
            self.assertEqual(
                first["runtime_format_compatibility_state"],
                "NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE",
            )
            self.assertEqual(first["artifact_format"], "SAFETENSORS")

    def test_candidate_roles_and_bundle_identities_are_exact(self) -> None:
        granite = self._build(GRANITE_CANDIDATE)
        control = self._build(CONTROL_CANDIDATE)
        self.assertEqual(granite["candidate_role"], "PRIMARY")
        self.assertTrue(granite["winner_eligible"])
        self.assertEqual(granite["model_artifact_bytes"], 704786224)
        self.assertEqual(granite["complete_bundle_bytes"], 714515562)
        self.assertEqual(control["candidate_role"], "CONTROL")
        self.assertFalse(control["winner_eligible"])
        self.assertEqual(control["model_artifact_bytes"], 8044982000)
        self.assertEqual(control["complete_bundle_bytes"], 8056508630)

    def test_runtime_dependency_identities_are_exact(self) -> None:
        manifest = self._build(GRANITE_CANDIDATE)
        self.assertEqual(manifest["transformers_source_revision"], TRANSFORMERS_SOURCE_REVISION)
        self.assertEqual(manifest["python_runtime_sha256"], PYTHON_RUNTIME_SHA256)
        self.assertEqual(
            manifest["installed_environment_manifest_sha256"],
            TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
        )
        self.assertEqual(manifest["loader_policy"], LOADER_POLICY)
        self.assertTrue(manifest["loader_policy"]["local_files_only"])
        self.assertFalse(manifest["loader_policy"]["trust_remote_code"])
        self.assertFalse(manifest["loader_policy"]["network_allowed"])

    def test_scoring_contract_matches_frozen_normalization_semantics(self) -> None:
        manifest = self._build(GRANITE_CANDIDATE)
        self.assertEqual(manifest["scoring_contract"], SCORING_CONTRACT)
        self.assertEqual(
            manifest["scoring_contract"]["scoring_method"],
            "NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX",
        )
        self.assertEqual(
            manifest["scoring_contract"]["tie_policy"],
            "FIRST_IN_FROZEN_CHOICE_ORDER",
        )
        self.assertEqual(manifest["scoring_contract"]["choice_order"], ["A", "B", "C", "D"])

    def test_normalized_log_likelihood_argmax_uses_mean_and_first_tie(self) -> None:
        self.assertEqual(
            normalized_log_likelihood_argmax(
                [-10.0, -8.0, -12.0, -9.0],
                [5, 2, 3, 3],
            ),
            2,
        )
        self.assertEqual(
            normalized_log_likelihood_argmax(
                [-2.0, -4.0, -3.0, -5.0],
                [2, 4, 3, 5],
            ),
            0,
        )
        with self.assertRaises(ValueError):
            normalized_log_likelihood_argmax([-1.0] * 4, [1, 1, 0, 1])
        with self.assertRaises(ValueError):
            normalized_log_likelihood_argmax([-1.0] * 3, [1, 1, 1])

    def test_operations_cover_six_scoring_assets_and_resource_asset(self) -> None:
        manifest = self._build(GRANITE_CANDIDATE)
        operations = manifest["operations"]
        scoring = [item for item in operations if item["operation_kind"] == "MULTIPLE_CHOICE_SCORE"]
        resource = [item for item in operations if item["operation_kind"] == "RESOURCE_MEASUREMENT"]
        self.assertEqual(len(scoring), 6)
        self.assertEqual(len(resource), 1)
        for operation in scoring:
            self.assertEqual(operation["scoring_method"], "NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX")
            self.assertEqual(len(operation["invocations"]), 1)
            invocation = operation["invocations"][0]
            self.assertEqual(invocation["run_class"], "SCORING")
            self.assertEqual(invocation["max_new_tokens"], 0)
        self.assertEqual(len(resource[0]["invocations"]), 32)

    def test_resource_schedule_is_exact_and_measurement_bound(self) -> None:
        manifest = self._build(CONTROL_CANDIDATE)
        resource = next(
            item for item in manifest["operations"] if item["operation_kind"] == "RESOURCE_MEASUREMENT"
        )
        invocations = resource["invocations"]
        self.assertEqual(len(invocations), 32)
        self.assertEqual(sum(item["run_class"] == "WARMUP" for item in invocations), 8)
        self.assertEqual(sum(item["run_class"] == "MEASURED" for item in invocations), 24)
        self.assertEqual(len({item["invocation_id"] for item in invocations}), 32)
        self.assertEqual(
            manifest["resource_generation_contract"], RESOURCE_GENERATION_CONTRACT
        )
        self.assertFalse(manifest["resource_generation_contract"]["do_sample"])
        self.assertEqual(manifest["resource_generation_contract"]["max_new_tokens"], 8)
        self.assertEqual(
            manifest["resource_generation_contract"]["required_measurements"],
            [
                "MODEL_ARTIFACT_BYTES",
                "PEAK_RSS_BYTES",
                "TIME_TO_FIRST_TOKEN_MS",
                "DECODE_TOKENS_PER_SECOND",
                "WALL_CLOCK_MS",
            ],
        )

    def test_manifest_tampering_fails_closed(self) -> None:
        manifest = self._build(GRANITE_CANDIDATE)
        manifest["python_runtime_sha256"] = "0" * 64
        errors = validate_e004_transformers_adapter_manifest(
            manifest, ASSET_SET, BUNDLE_SET
        )
        self.assertIn("E004TransformersAdapterManifest: python_runtime_sha256 mismatch", errors)
        self.assertIn("E004TransformersAdapterManifest: adapter_sha256 mismatch", errors)

    def test_operation_tampering_fails_closed(self) -> None:
        manifest = self._build(CONTROL_CANDIDATE)
        resource = next(
            item for item in manifest["operations"] if item["operation_kind"] == "RESOURCE_MEASUREMENT"
        )
        resource["invocations"][0]["run_class"] = "MEASURED"
        errors = validate_e004_transformers_adapter_manifest(
            manifest, ASSET_SET, BUNDLE_SET
        )
        self.assertTrue(
            any("exact warmup/measured invocation set required" in error for error in errors)
        )
        self.assertIn("E004TransformersAdapterManifest: adapter_sha256 mismatch", errors)

    def test_candidate_outside_transformers_route_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "not assigned"):
            build_e004_transformers_adapter_manifest(
                ASSET_SET,
                BUNDLE_SET,
                candidate_id="Qwen/Qwen3-0.6B-Base",
                upstream_revision="da87bfb608c14b7cf20ba1ce41287e8de496c0cd",
            )

    def test_bundle_tamper_is_rejected_before_manifest_construction(self) -> None:
        tampered = copy.deepcopy(BUNDLE_SET)
        granite = next(
            item
            for item in tampered["candidate_bundles"]
            if item["candidate_id"] == GRANITE_CANDIDATE[0]
        )
        granite["model_artifact_bytes"] += 1
        with self.assertRaisesRegex(ValueError, "not canonically valid"):
            build_e004_transformers_adapter_manifest(
                ASSET_SET,
                tampered,
                candidate_id=GRANITE_CANDIDATE[0],
                upstream_revision=GRANITE_CANDIDATE[1],
            )

    def test_module_contains_no_runtime_or_process_execution_imports(self) -> None:
        source = inspect.getsource(adapter)
        prohibited = (
            "from transformers",
            "import transformers",
            "import torch",
            "from torch",
            "import subprocess",
            "from subprocess",
        )
        for marker in prohibited:
            self.assertNotIn(marker, source)


if __name__ == "__main__":
    unittest.main()
