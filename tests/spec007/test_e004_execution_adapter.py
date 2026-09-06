from __future__ import annotations

import copy
import json
import struct
import unittest
from pathlib import Path

from src.commandmed.spec007.e004_execution_adapter import (
    FROZEN_EVALUATION_ASSETS,
    LLAMA_CLI_EXECUTABLE_SHA256,
    LLAMA_MULTIPLE_CHOICE_INPUT_FORMAT,
    LLAMA_PERPLEXITY_EXECUTABLE_SHA256,
    MULTIPLE_CHOICE_ASSET_KIND,
    RESOURCE_ASSET_KIND,
    build_e004_llama_adapter_manifest,
    build_llama_multiple_choice_argv,
    build_llama_resource_invocations,
    compute_llama_multiple_choice_payload_sha256,
    serialize_llama_multiple_choice_asset,
    validate_e004_llama_adapter_manifest,
)
from src.commandmed.spec007.research_tournament import PRIMARY_CANDIDATES


ASSET_SET = json.loads(
    Path(
        "specs/007-sft-v1/e004-research-component-tournament-evaluation-assets-v1.json"
    ).read_text(encoding="utf-8")
)
ASSETS = {record["asset_id"]: record for record in ASSET_SET["asset_records"]}


def _read_u32(raw: bytes, offset: int) -> tuple[int, int]:
    return struct.unpack_from("<I", raw, offset)[0], offset + 4


def _read_i32(raw: bytes, offset: int) -> tuple[int, int]:
    return struct.unpack_from("<i", raw, offset)[0], offset + 4


def _read_string(raw: bytes, offset: int) -> tuple[str, int]:
    size, offset = _read_u32(raw, offset)
    end = offset + size
    return raw[offset:end].decode("utf-8"), end


class TestE004LlamaExecutionAdapter(unittest.TestCase):
    def test_frozen_asset_registry_matches_asset_set(self) -> None:
        self.assertEqual(set(ASSETS), set(FROZEN_EVALUATION_ASSETS))
        for asset_id, (expected_sha, expected_kind, expected_scoring) in (
            FROZEN_EVALUATION_ASSETS.items()
        ):
            asset = ASSETS[asset_id]
            self.assertEqual(asset["asset_sha256"], expected_sha)
            self.assertEqual(asset["asset_kind"], expected_kind)
            self.assertEqual(asset["scoring_method"], expected_scoring)

    def test_multiple_choice_serializer_matches_llama_native_layout(self) -> None:
        mc_assets = [
            asset
            for asset in ASSETS.values()
            if asset["asset_kind"] == MULTIPLE_CHOICE_ASSET_KIND
        ]
        self.assertEqual(len(mc_assets), 6)
        for asset in mc_assets:
            raw = serialize_llama_multiple_choice_asset(asset)
            self.assertEqual(raw, serialize_llama_multiple_choice_asset(asset))
            self.assertEqual(
                compute_llama_multiple_choice_payload_sha256(asset),
                __import__("hashlib").sha256(raw).hexdigest(),
            )

            task_count, offset = _read_u32(raw, 0)
            self.assertEqual(task_count, 12)
            task_offsets: list[int] = []
            for _ in range(task_count):
                task_offset, offset = _read_u32(raw, offset)
                task_offsets.append(task_offset)
            self.assertEqual(task_offsets, sorted(task_offsets))
            self.assertGreaterEqual(task_offsets[0], 4 + task_count * 4)

            first_case = asset["cases"][0]
            cursor = task_offsets[0]
            question, cursor = _read_string(raw, cursor)
            self.assertEqual(question, first_case["prompt"])
            answer_count, cursor = _read_u32(raw, cursor)
            self.assertEqual(answer_count, 4)
            answers: list[str] = []
            for _ in range(answer_count):
                answer, cursor = _read_string(raw, cursor)
                answers.append(answer)
            self.assertEqual(answers, [choice["text"] for choice in first_case["choices"]])
            labels: list[int] = []
            for _ in range(answer_count):
                label, cursor = _read_i32(raw, cursor)
                labels.append(label)
            self.assertEqual(sum(labels), 1)
            correct_index = [
                choice["choice_id"] for choice in first_case["choices"]
            ].index(first_case["correct_choice_id"])
            self.assertEqual(labels[correct_index], 1)
            mc2_count, _ = _read_u32(raw, cursor)
            self.assertEqual(mc2_count, 0)

    def test_resource_asset_is_not_multiple_choice_serializable(self) -> None:
        resource_asset = next(
            asset
            for asset in ASSETS.values()
            if asset["asset_kind"] == RESOURCE_ASSET_KIND
        )
        with self.assertRaisesRegex(ValueError, "resource-measurement"):
            serialize_llama_multiple_choice_asset(resource_asset)

    def test_frozen_asset_identity_tamper_fails_closed(self) -> None:
        asset = copy.deepcopy(ASSETS["SP007-RO-001-EVAL-INSTRUCTION-V1"])
        asset["asset_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "canonically valid"):
            serialize_llama_multiple_choice_asset(asset)

    def test_llama_multiple_choice_argv_is_exact_and_offline(self) -> None:
        argv = build_llama_multiple_choice_argv(
            model_path="runtime/candidate.gguf",
            payload_path="evaluation/instruction.mcbin",
        )
        self.assertEqual(argv[0], "llama-perplexity")
        self.assertIn("--multiple-choice", argv)
        self.assertEqual(argv[argv.index("--multiple-choice-tasks") + 1], "12")
        self.assertEqual(argv[argv.index("--ctx-size") + 1], "512")
        self.assertIn("--offline", argv)
        with self.assertRaises(ValueError):
            build_llama_multiple_choice_argv(
                model_path="runtime/candidate.gguf\n--token=secret",
                payload_path="evaluation/instruction.mcbin",
            )

    def test_resource_projection_expands_all_frozen_runs(self) -> None:
        resource_asset = next(
            asset
            for asset in ASSETS.values()
            if asset["asset_kind"] == RESOURCE_ASSET_KIND
        )
        invocations = build_llama_resource_invocations(
            resource_asset, model_path="runtime/candidate.gguf"
        )
        self.assertEqual(len(invocations), 32)
        self.assertEqual(
            sum(item["run_class"] == "WARMUP" for item in invocations), 8
        )
        self.assertEqual(
            sum(item["run_class"] == "MEASURED" for item in invocations), 24
        )
        self.assertEqual(len({item["invocation_id"] for item in invocations}), 32)
        for invocation in invocations:
            self.assertEqual(invocation["runtime_entrypoint"], "llama-cli")
            self.assertEqual(
                invocation["runtime_executable_sha256"], LLAMA_CLI_EXECUTABLE_SHA256
            )
            argv = invocation["argv"]
            self.assertEqual(len(argv), 16)
            self.assertEqual(argv[0], "llama-cli")
            self.assertEqual(argv[argv.index("--n-predict") + 1], "8")
            self.assertEqual(argv[argv.index("--temp") + 1], "0")
            self.assertEqual(argv[argv.index("--seed") + 1], "1")
            self.assertIn("--offline", argv)
            self.assertIn("--no-conversation", argv)
            self.assertIn("--no-display-prompt", argv)

    def test_complete_llama_adapter_manifest_is_deterministic_and_nonexecuting(self) -> None:
        for candidate_id, revision in PRIMARY_CANDIDATES[:2]:
            first = build_e004_llama_adapter_manifest(
                ASSET_SET,
                candidate_id=candidate_id,
                upstream_revision=revision,
                model_path="runtime/candidate.gguf",
                payload_directory="evaluation/generated",
            )
            second = build_e004_llama_adapter_manifest(
                ASSET_SET,
                candidate_id=candidate_id,
                upstream_revision=revision,
                model_path="runtime/candidate.gguf",
                payload_directory="evaluation/generated",
            )
            self.assertEqual(first, second)
            self.assertEqual(validate_e004_llama_adapter_manifest(first, ASSET_SET), [])
            self.assertFalse(first["execution_performed"])
            self.assertEqual(first["authorized_spend_usd"], 0)
            self.assertEqual(len(first["operations"]), 7)

            mc_ops = [
                operation
                for operation in first["operations"]
                if operation["operation_kind"] == "MULTIPLE_CHOICE_SCORE"
            ]
            resource_ops = [
                operation
                for operation in first["operations"]
                if operation["operation_kind"] == "RESOURCE_MEASUREMENT"
            ]
            self.assertEqual(len(mc_ops), 6)
            self.assertEqual(len(resource_ops), 1)
            for operation in mc_ops:
                self.assertEqual(operation["input_format"], LLAMA_MULTIPLE_CHOICE_INPUT_FORMAT)
                invocation = operation["invocations"][0]
                self.assertEqual(invocation["runtime_entrypoint"], "llama-perplexity")
                self.assertEqual(
                    invocation["runtime_executable_sha256"],
                    LLAMA_PERPLEXITY_EXECUTABLE_SHA256,
                )
            self.assertEqual(len(resource_ops[0]["invocations"]), 32)

    def test_manifest_tamper_fails_self_hash(self) -> None:
        candidate_id, revision = PRIMARY_CANDIDATES[0]
        manifest = build_e004_llama_adapter_manifest(
            ASSET_SET,
            candidate_id=candidate_id,
            upstream_revision=revision,
            model_path="runtime/candidate.gguf",
            payload_directory="evaluation/generated",
        )
        manifest["operations"][0]["invocations"][0]["argv"].append("--unexpected")
        self.assertIn(
            "E004LlamaAdapterManifest: adapter_sha256 mismatch",
            validate_e004_llama_adapter_manifest(manifest, ASSET_SET),
        )

    def test_non_llama_candidate_route_fails_closed(self) -> None:
        candidate_id, revision = PRIMARY_CANDIDATES[2]
        with self.assertRaisesRegex(ValueError, "not assigned"):
            build_e004_llama_adapter_manifest(
                ASSET_SET,
                candidate_id=candidate_id,
                upstream_revision=revision,
                model_path="runtime/candidate.safetensors",
                payload_directory="evaluation/generated",
            )


if __name__ == "__main__":
    unittest.main()
