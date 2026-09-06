from __future__ import annotations

import copy
import inspect
import json
import unittest
from pathlib import Path

from src.commandmed.spec007 import e004_execution_plan as execution_plan
from src.commandmed.spec007.e004_execution_plan import (
    FROZEN_CANDIDATES,
    ORCHESTRATOR_ENTRYPOINT,
    ORCHESTRATOR_IMPLEMENTATION_STATE,
    RUNTIME_FORMAT_COMPATIBILITY_STATE,
    build_e004_candidate_execution_plan,
    build_e004_four_candidate_execution_plan_set,
    validate_e004_candidate_execution_plan,
    validate_e004_four_candidate_execution_plan_set,
)
from src.commandmed.spec007.research_tournament import CONTROL_CANDIDATE, PRIMARY_CANDIDATES


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


class TestE004ExecutionPlan(unittest.TestCase):
    def _build(self, pair: tuple[str, str]) -> dict:
        return build_e004_candidate_execution_plan(
            ASSET_SET,
            BUNDLE_SET,
            candidate_id=pair[0],
            upstream_revision=pair[1],
        )

    def test_all_four_candidate_plans_are_deterministic_and_valid(self) -> None:
        for pair in FROZEN_CANDIDATES:
            first = self._build(pair)
            second = self._build(pair)
            self.assertEqual(first, second)
            self.assertEqual(
                validate_e004_candidate_execution_plan(first, ASSET_SET, BUNDLE_SET),
                [],
            )
            self.assertEqual(len(first["execution_plan_sha256"]), 64)
            self.assertFalse(first["execution_performed"])
            self.assertEqual(first["authorized_spend_usd"], 0)

    def test_route_composition_is_exact(self) -> None:
        for pair in PRIMARY_CANDIDATES[:2]:
            plan = self._build(pair)
            self.assertEqual(plan["artifact_format"], "GGUF")
            self.assertEqual(plan["backend_family"], "LLAMA_CPP_GGUF")
            self.assertEqual(
                plan["backend_runtime_identity"]["runtime_family"],
                "LLAMA_CPP_GGUF",
            )
            self.assertEqual(
                [
                    item["entrypoint"]
                    for item in plan["backend_runtime_identity"]["entrypoint_executables"]
                ],
                ["llama-perplexity", "llama-cli"],
            )

        for pair in (PRIMARY_CANDIDATES[2], CONTROL_CANDIDATE):
            plan = self._build(pair)
            self.assertEqual(plan["artifact_format"], "SAFETENSORS")
            self.assertEqual(plan["backend_family"], "TRANSFORMERS_TORCH_CPU")
            self.assertEqual(
                plan["backend_runtime_identity"]["runtime_family"],
                "TRANSFORMERS_TORCH_CPU",
            )
            self.assertEqual(
                plan["backend_runtime_identity"]["entrypoint_executables"][0][
                    "entrypoint"
                ],
                "python3.12",
            )

    def test_top_level_runtime_argv_is_exact_per_candidate(self) -> None:
        observed = set()
        for pair in FROZEN_CANDIDATES:
            plan = self._build(pair)
            argv = plan["runtime_argv"]
            self.assertEqual(plan["runtime_entrypoint"], ORCHESTRATOR_ENTRYPOINT)
            self.assertEqual(argv[0], ORCHESTRATOR_ENTRYPOINT)
            self.assertIn("--execution-plan-id", argv)
            self.assertIn("--candidate-id", argv)
            self.assertIn(pair[0], argv)
            self.assertIn("--candidate-revision", argv)
            self.assertIn(pair[1], argv)
            self.assertIn("--adapter-sha256", argv)
            self.assertIn(plan["adapter_sha256"], argv)
            self.assertEqual(argv[-4:], ["--network-mode", "offline", "--authorized-spend-usd", "0"])
            observed.add(tuple(argv))
        self.assertEqual(len(observed), 4)

    def test_plan_preserves_exact_bundle_and_tokenizer_identities(self) -> None:
        by_pair = {
            (item["candidate_id"], item["upstream_revision"]): item
            for item in BUNDLE_SET["candidate_bundles"]
        }
        for pair in FROZEN_CANDIDATES:
            plan = self._build(pair)
            bundle = by_pair[pair]
            for field in (
                "model_artifact_sha256",
                "model_artifact_bytes",
                "complete_bundle_sha256",
                "complete_bundle_bytes",
                "tokenizer_config_sha256",
            ):
                self.assertEqual(plan[field], bundle[field])

    def test_plan_set_binds_exact_dependency_ordered_four_candidate_set(self) -> None:
        first = build_e004_four_candidate_execution_plan_set(ASSET_SET, BUNDLE_SET)
        second = build_e004_four_candidate_execution_plan_set(ASSET_SET, BUNDLE_SET)
        self.assertEqual(first, second)
        self.assertEqual(
            validate_e004_four_candidate_execution_plan_set(first, ASSET_SET, BUNDLE_SET),
            [],
        )
        self.assertEqual(
            [
                (plan["candidate_id"], plan["upstream_revision"])
                for plan in first["execution_plans"]
            ],
            list(FROZEN_CANDIDATES),
        )
        self.assertEqual(len({plan["execution_plan_sha256"] for plan in first["execution_plans"]}), 4)
        self.assertFalse(first["execution_performed"])
        self.assertEqual(first["authorized_spend_usd"], 0)

    def test_empirical_compatibility_and_future_executor_remain_unbound(self) -> None:
        for pair in FROZEN_CANDIDATES:
            plan = self._build(pair)
            self.assertEqual(
                plan["runtime_format_compatibility_state"],
                RUNTIME_FORMAT_COMPATIBILITY_STATE,
            )
            self.assertEqual(
                plan["orchestrator_implementation_state"],
                ORCHESTRATOR_IMPLEMENTATION_STATE,
            )
            self.assertEqual(plan["future_execution_environment_state"], "INCOMPLETE")

    def test_candidate_plan_tampering_fails_closed(self) -> None:
        plan = self._build(PRIMARY_CANDIDATES[0])
        plan["runtime_argv"][-1] = "1"
        errors = validate_e004_candidate_execution_plan(plan, ASSET_SET, BUNDLE_SET)
        self.assertIn("E004CandidateExecutionPlan: runtime_argv mismatch", errors)
        self.assertIn("E004CandidateExecutionPlan: execution_plan_sha256 mismatch", errors)

    def test_plan_set_tampering_fails_closed(self) -> None:
        plan_set = build_e004_four_candidate_execution_plan_set(ASSET_SET, BUNDLE_SET)
        plan_set["execution_plans"] = list(reversed(plan_set["execution_plans"]))
        errors = validate_e004_four_candidate_execution_plan_set(
            plan_set, ASSET_SET, BUNDLE_SET
        )
        self.assertTrue(any("dependency-ordered frozen candidate set" in error for error in errors))
        self.assertIn("E004FourCandidateExecutionPlanSet: plan_set_sha256 mismatch", errors)

    def test_bundle_tamper_is_rejected(self) -> None:
        tampered = copy.deepcopy(BUNDLE_SET)
        tampered["candidate_bundles"][0]["complete_bundle_bytes"] += 1
        with self.assertRaisesRegex(ValueError, "not canonically valid"):
            build_e004_four_candidate_execution_plan_set(ASSET_SET, tampered)

    def test_module_contains_no_model_process_or_network_execution_imports(self) -> None:
        source = inspect.getsource(execution_plan)
        prohibited = (
            "from transformers",
            "import transformers",
            "import torch",
            "from torch",
            "import subprocess",
            "from subprocess",
            "import socket",
            "import requests",
            "import urllib",
            "os.system(",
        )
        for marker in prohibited:
            self.assertNotIn(marker, source)


if __name__ == "__main__":
    unittest.main()
