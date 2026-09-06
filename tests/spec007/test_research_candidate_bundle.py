"""Tests for deterministic non-executing Spec 007 candidate-artifact bundles."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import unittest

from src.commandmed.spec007.research_candidate_bundle import (
    CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
    COMPLETE_BUNDLE_SEMANTICS,
    MULTI_FILE_MODEL_ARTIFACT_SEMANTICS,
    compute_candidate_artifact_bundle_set_sha256,
    compute_candidate_artifact_bundle_sha256,
    compute_multi_file_model_artifact_sha256,
    validate_candidate_artifact_bundle_set,
)
from src.commandmed.spec007.research_execution import PRIMARY_PACKAGE_HARD_CAP_BYTES


MANIFEST_PATH = Path(
    "specs/007-sft-v1/e004-successor-candidate-artifact-bundle-set-v1.json"
)


def _load() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def _rehash_bundle(bundle: dict) -> None:
    bundle["complete_bundle_sha256"] = compute_candidate_artifact_bundle_sha256(bundle)


def _rehash_set(bundle_set: dict) -> None:
    bundle_set["bundle_set_sha256"] = compute_candidate_artifact_bundle_set_sha256(
        bundle_set
    )


class TestCandidateArtifactBundleSet(unittest.TestCase):
    def test_canonical_manifest_validates(self) -> None:
        manifest = _load()
        self.assertEqual(validate_candidate_artifact_bundle_set(manifest), [])
        self.assertEqual(
            compute_candidate_artifact_bundle_set_sha256(manifest),
            CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        )

    def test_exact_bundle_identities_and_primary_margins(self) -> None:
        manifest = _load()
        observed = {
            bundle["candidate_id"]: (
                bundle["complete_bundle_bytes"],
                bundle["complete_bundle_sha256"],
            )
            for bundle in manifest["candidate_bundles"]
        }
        self.assertEqual(
            observed["Qwen/Qwen3-0.6B-Base"],
            (
                408_195_248,
                "8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415",
            ),
        )
        self.assertEqual(
            observed["Qwen/Qwen3.5-0.8B-Base"],
            (
                585_938_673,
                "682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592",
            ),
        )
        self.assertEqual(
            observed["ibm-granite/granite-4.0-350m-base"],
            (
                714_515_562,
                "90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db",
            ),
        )
        self.assertEqual(
            observed["Qwen/Qwen3-4B-Base"],
            (
                8_056_508_630,
                "9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9",
            ),
        )
        self.assertEqual(PRIMARY_PACKAGE_HARD_CAP_BYTES, 734_003_200)
        self.assertEqual(PRIMARY_PACKAGE_HARD_CAP_BYTES - 408_195_248, 325_807_952)
        self.assertEqual(PRIMARY_PACKAGE_HARD_CAP_BYTES - 585_938_673, 148_064_527)
        self.assertEqual(PRIMARY_PACKAGE_HARD_CAP_BYTES - 714_515_562, 19_487_638)

    def test_control_model_artifact_is_exact_weight_shard_manifest(self) -> None:
        control = _load()["candidate_bundles"][3]
        self.assertEqual(
            control["model_artifact_identity_kind"],
            MULTI_FILE_MODEL_ARTIFACT_SEMANTICS,
        )
        self.assertEqual(control["model_artifact_bytes"], 8_044_982_000)
        self.assertEqual(
            control["model_artifact_sha256"],
            "d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397",
        )
        self.assertEqual(
            compute_multi_file_model_artifact_sha256(control["files"]),
            control["model_artifact_sha256"],
        )

    def test_complete_bundle_semantics_are_manifest_not_archive_digest(self) -> None:
        manifest = _load()
        for bundle in manifest["candidate_bundles"]:
            self.assertEqual(
                bundle["complete_bundle_semantics"], COMPLETE_BUNDLE_SEMANTICS
            )
            self.assertEqual(
                compute_candidate_artifact_bundle_sha256(bundle),
                bundle["complete_bundle_sha256"],
            )

    def test_unknown_runtime_field_is_rejected(self) -> None:
        manifest = _load()
        manifest["candidate_bundles"][0]["runtime_argv"] = ["llama-cli"]
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(any("undeclared fields" in error for error in errors), errors)

    def test_bundle_byte_sum_tamper_is_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        bundle["complete_bundle_bytes"] += 1
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("complete_bundle_bytes mismatch" in error for error in errors), errors
        )

    def test_tokenizer_config_digest_must_match_exact_file(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][1]
        bundle["tokenizer_config_sha256"] = "0" * 64
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("tokenizer_config_sha256 mismatch" in error for error in errors), errors
        )

    def test_single_file_model_identity_must_match_weight_file(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][2]
        bundle["model_artifact_sha256"] = "0" * 64
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("model_artifact_sha256 mismatch" in error for error in errors), errors
        )

    def test_multi_file_model_identity_must_match_weight_shards(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][3]
        bundle["model_artifact_sha256"] = "0" * 64
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("model_artifact_sha256 mismatch" in error for error in errors), errors
        )

    def test_duplicate_file_path_is_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        duplicate = copy.deepcopy(bundle["files"][0])
        bundle["files"].append(duplicate)
        bundle["files"].sort(key=lambda item: item["path"])
        bundle["complete_bundle_bytes"] = sum(item["bytes"] for item in bundle["files"])
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(any("file paths must be unique" in error for error in errors), errors)

    def test_unsorted_file_paths_are_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        bundle["files"][0], bundle["files"][1] = bundle["files"][1], bundle["files"][0]
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(any("files must be sorted by path" in error for error in errors), errors)

    def test_candidate_order_is_frozen(self) -> None:
        manifest = _load()
        manifest["candidate_bundles"][0], manifest["candidate_bundles"][1] = (
            manifest["candidate_bundles"][1],
            manifest["candidate_bundles"][0],
        )
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any(
                "candidate_bundles must use frozen deterministic order" in error
                for error in errors
            ),
            errors,
        )

    def test_wrong_role_is_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        bundle["candidate_role"] = "CONTROL"
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(any("candidate_role mismatch" in error for error in errors), errors)

    def test_bool_bytes_are_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        bundle["files"][0]["bytes"] = True
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("bytes must be a positive integer" in error for error in errors), errors
        )

    def test_path_traversal_is_rejected(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        bundle["files"][0]["path"] = "../config.json"
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any("safe POSIX relative path" in error for error in errors), errors
        )

    def test_primary_hard_cap_is_noncompensable(self) -> None:
        manifest = _load()
        bundle = manifest["candidate_bundles"][0]
        excess = PRIMARY_PACKAGE_HARD_CAP_BYTES - bundle["complete_bundle_bytes"] + 1
        target = next(
            item for item in bundle["files"] if item["purpose"] == "TOKENIZER_ASSET"
        )
        target["bytes"] += excess
        bundle["complete_bundle_bytes"] = sum(item["bytes"] for item in bundle["files"])
        _rehash_bundle(bundle)
        _rehash_set(manifest)
        errors = validate_candidate_artifact_bundle_set(manifest)
        self.assertTrue(
            any(
                "primary complete bundle exceeds frozen 700 MiB hard cap" in error
                for error in errors
            ),
            errors,
        )

    def test_control_is_not_subject_to_primary_hard_cap(self) -> None:
        manifest = _load()
        control = manifest["candidate_bundles"][3]
        self.assertGreater(control["complete_bundle_bytes"], PRIMARY_PACKAGE_HARD_CAP_BYTES)
        self.assertEqual(validate_candidate_artifact_bundle_set(manifest), [])


if __name__ == "__main__":
    unittest.main()
