from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/e004-model-load-compatibility-evidence-v1.yml"
CORRECTIVE_WORKFLOW = ROOT / ".github/workflows/e004-model-load-compatibility-corrective-evidence-v1.yml"
HELPER = ROOT / "tools/e004_model_load_probe.cpp"


class TestE004ModelLoadCompatibilityPolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.helper = HELPER.read_text(encoding="utf-8")

    def test_evidence_workflow_is_post_merge_push_only(self) -> None:
        self.assertIn("evidence/e004-model-load-compatibility-run-v1", self.workflow)
        self.assertIn(".github/e004-model-load-compatibility-run-v1.txt", self.workflow)
        self.assertNotIn("pull_request:", self.workflow)
        self.assertNotIn("workflow_dispatch:", self.workflow)
        self.assertIn("github.run_attempt == 1", self.workflow)
        self.assertIn("fetch-depth: 2", self.workflow)
        self.assertIn("persist-credentials: false", self.workflow)

    def test_exact_four_candidate_matrix_is_frozen(self) -> None:
        expected = {
            "Qwen/Qwen3-0.6B-Base": "da87bfb608c14b7cf20ba1ce41287e8de496c0cd",
            "Qwen/Qwen3.5-0.8B-Base": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
            "ibm-granite/granite-4.0-350m-base": "a50b46cef21c8a86b15f0496cb794487a78a910b",
            "Qwen/Qwen3-4B-Base": "906bfd4b4dc7f14ee4320094d8b41684abff8539",
        }
        self.assertEqual(self.workflow.count("          - candidate_id:"), 4)
        for candidate_id, revision in expected.items():
            self.assertEqual(self.workflow.count(f"candidate_id: {candidate_id}"), 1)
            self.assertEqual(self.workflow.count(f"revision: {revision}"), 1)
        self.assertEqual(self.workflow.count("route: LLAMA_CPP_GGUF"), 2)
        self.assertEqual(self.workflow.count("route: TRANSFORMERS_TORCH_CPU"), 2)
        self.assertIn("max-parallel: 1", self.workflow)
        self.assertIn("fail-fast: false", self.workflow)

    def test_standard_runner_and_zero_retention_only(self) -> None:
        self.assertEqual(self.workflow.count("runs-on: ubuntu-24.04"), 1)
        self.assertNotIn("upload-artifact", self.workflow)
        self.assertNotIn("actions/cache", self.workflow)
        self.assertNotIn("larger", self.workflow.lower())
        self.assertIn("CURRENT_AUTHORIZED_SPEND_USD=0", self.workflow)
        self.assertIn("Remove all candidate and runtime bytes", self.workflow)
        self.assertIn("MODEL_BYTE_PERSISTENCE_AFTER_JOB=NO", self.workflow)

    def test_network_is_disabled_during_model_load(self) -> None:
        self.assertIn("Execute exact load-only compatibility probe with network disabled", self.workflow)
        self.assertGreaterEqual(self.workflow.count("unshare -n --"), 3)
        self.assertIn("HF_HUB_OFFLINE=1", self.workflow)
        self.assertIn("TRANSFORMERS_OFFLINE=1", self.workflow)
        self.assertIn("local_files_only=True", self.workflow)
        self.assertIn("trust_remote_code=False", self.workflow)

    def test_workflow_has_no_evaluation_or_training_invocation(self) -> None:
        prohibited = (
            "llama-perplexity",
            "--multiple-choice",
            "benchmark/evaluation payload path",
            "research_tournament.py --",
            ".generate(",
            "Trainer(",
            ".backward(",
            "optimizer.step(",
        )
        for token in prohibited:
            self.assertNotIn(token, self.workflow)

    def test_llama_helper_is_model_load_only(self) -> None:
        self.assertIn("llama_backend_init()", self.helper)
        self.assertIn("llama_model_default_params()", self.helper)
        self.assertIn("llama_model_load_from_file", self.helper)
        self.assertIn("llama_model_free", self.helper)
        self.assertIn("llama_backend_free", self.helper)
        for prohibited in (
            "llama_init_from_model",
            "llama_new_context_with_model",
            "llama_decode",
            "llama_encode",
            "llama_batch",
            "llama_sampler",
            "prompt",
            "generate",
            "perplexity",
        ):
            self.assertNotIn(prohibited, self.helper)

    def test_authority_and_reason_codes_are_frozen_before_run(self) -> None:
        for token in (
            "FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_B",
            "MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_SP007_RO_001_FOUR_CANDIDATE_LOAD_ONLY",
            "MODEL_FORWARD_PASS_AUTHORITY=NONE",
            "MODEL_INFERENCE_AUTHORITY=NONE",
            "GENERATION_AUTHORITY=NONE",
            "A15_ACTIVATION_AUTHORITY=NONE",
            "TRAINING_AUTHORITY=NONE",
            "PASS_EXACT_MODEL_LOAD_COMPLETED",
            "FAIL_MODEL_LOAD_ERROR",
            "FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD",
            "INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION",
        ):
            self.assertIn(token, self.workflow)


class TestE004CorrectiveModelLoadCompatibilityPolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = CORRECTIVE_WORKFLOW.read_text(encoding="utf-8")
        cls.helper = HELPER.read_text(encoding="utf-8")

    def test_corrective_workflow_is_post_merge_marker_push_only(self) -> None:
        self.assertIn(
            "evidence/e004-model-load-compatibility-corrective-run-v1",
            self.workflow,
        )
        self.assertIn(
            ".github/e004-model-load-compatibility-corrective-run-v1.txt",
            self.workflow,
        )
        self.assertNotIn("pull_request:", self.workflow)
        self.assertNotIn("workflow_dispatch:", self.workflow)
        self.assertIn("github.run_attempt == 1", self.workflow)
        self.assertIn("fetch-depth: 2", self.workflow)
        self.assertIn("persist-credentials: false", self.workflow)
        self.assertIn('test "$(git diff --name-only HEAD^ HEAD)" = "$MARKER"', self.workflow)

    def test_corrective_matrix_is_exactly_the_two_frozen_gguf_candidates(self) -> None:
        expected = {
            "Qwen/Qwen3-0.6B-Base": "da87bfb608c14b7cf20ba1ce41287e8de496c0cd",
            "Qwen/Qwen3.5-0.8B-Base": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
        }
        self.assertEqual(self.workflow.count("          - candidate_id:"), 2)
        for candidate_id, revision in expected.items():
            self.assertEqual(self.workflow.count(f"candidate_id: {candidate_id}"), 1)
            self.assertEqual(self.workflow.count(f"revision: {revision}"), 1)
        for prohibited_candidate in (
            "ibm-granite/granite-4.0-350m-base",
            "Qwen/Qwen3-4B-Base",
        ):
            self.assertNotIn(prohibited_candidate, self.workflow)
        self.assertNotIn("TRANSFORMERS_TORCH_CPU", self.workflow)
        self.assertIn("RUNTIME_ROUTE=LLAMA_CPP_GGUF", self.workflow)
        self.assertIn("max-parallel: 1", self.workflow)
        self.assertIn("fail-fast: false", self.workflow)

    def test_corrective_authority_is_bound_and_non_expanding(self) -> None:
        for token in (
            "FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B",
            "CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY",
            "CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY",
            "TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE",
            "MODEL_FORWARD_PASS_AUTHORITY=NONE",
            "MODEL_INFERENCE_AUTHORITY=NONE",
            "GENERATION_AUTHORITY=NONE",
            "BENCHMARK_EXECUTION_AUTHORITY=NONE",
            "EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE",
            "TOURNAMENT_EXECUTION_AUTHORITY=NONE",
            "WINNER_SELECTION_AUTHORITY=NONE",
            "A15_ACTIVATION_AUTHORITY=NONE",
            "TRAINING_AUTHORITY=NONE",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
        ):
            self.assertIn(token, self.workflow)

    def test_original_run_is_consumed_and_corrective_run_is_single_attempt(self) -> None:
        for token in (
            'ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID: "34063020745"',
            "EVIDENCE_WORKFLOW_RUN_ID=34063020745",
            "MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY",
            "MAX_AUTHORIZED_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1",
            "FAILED_RUN_RETRY_AUTHORITY=NONE",
            "SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE",
        ):
            self.assertIn(token, self.workflow)
        self.assertNotIn("rerun", self.workflow.lower())

    def test_corrective_runtime_identity_is_frozen(self) -> None:
        for token in (
            "c1d0e7a004015f23bc0233470b747b596f29b264",
            "2255f4747492109298a5c997f374d49c2af3113d",
            "b10621",
            "91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583",
            "4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711",
            "89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448",
        ):
            self.assertIn(token, self.workflow)

    def test_corrective_header_closure_fixes_observed_preload_failure(self) -> None:
        required_headers = (
            "fetch_header include/llama.h include/llama.h",
            "fetch_header ggml/include/ggml.h ggml/include/ggml.h",
            "fetch_header ggml/include/ggml-cpu.h ggml/include/ggml-cpu.h",
            "fetch_header ggml/include/ggml-backend.h ggml/include/ggml-backend.h",
            "fetch_header ggml/include/ggml-alloc.h ggml/include/ggml-alloc.h",
            "fetch_header ggml/include/ggml-opt.h ggml/include/ggml-opt.h",
            "fetch_header ggml/include/gguf.h ggml/include/gguf.h",
        )
        for token in required_headers:
            self.assertEqual(self.workflow.count(token), 1)
        self.assertIn(
            'grep -Fq \'#include "ggml-alloc.h"\' "$headers/ggml/include/ggml-backend.h"',
            self.workflow,
        )
        self.assertIn("CORRECTIVE_HEADER_CLOSURE_GGML_ALLOC=PASS", self.workflow)

    def test_corrective_probe_is_network_disabled_and_model_load_only(self) -> None:
        self.assertIn(
            "Execute exact corrective GGUF load-only probe with network disabled",
            self.workflow,
        )
        self.assertEqual(self.workflow.count("sudo unshare -n --"), 1)
        self.assertIn("llama_model_load_from_file", self.helper)
        for prohibited in (
            "llama_init_from_model",
            "llama_new_context_with_model",
            "llama_decode",
            "llama_encode",
            "llama_batch",
            "llama_sampler",
            "prompt",
            "generate",
            "perplexity",
        ):
            self.assertNotIn(prohibited, self.helper)

    def test_corrective_workflow_has_no_evaluation_training_or_retention_path(self) -> None:
        for prohibited in (
            "llama-perplexity",
            "--multiple-choice",
            "research_tournament.py --",
            ".generate(",
            "Trainer(",
            ".backward(",
            "optimizer.step(",
            "upload-artifact",
            "actions/cache",
        ):
            self.assertNotIn(prohibited, self.workflow)
        self.assertEqual(self.workflow.count("runs-on: ubuntu-24.04"), 1)
        self.assertIn("Remove all corrective candidate and runtime bytes", self.workflow)
        self.assertIn("MODEL_BYTE_PERSISTENCE_AFTER_JOB=NO", self.workflow)
        self.assertIn("RAW_MODEL_BYTE_ARTIFACT_UPLOAD=NO", self.workflow)
        self.assertIn("ACTIONS_CACHE_FOR_MODEL_BYTES=NO", self.workflow)

    def test_corrective_reason_codes_are_frozen(self) -> None:
        for token in (
            "PASS_EXACT_MODEL_LOAD_COMPLETED",
            "INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION",
            "FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD",
            "FAIL_MODEL_LOAD_ERROR",
        ):
            self.assertIn(token, self.workflow)


if __name__ == "__main__":
    unittest.main()
