from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
CORRECTIVE_WORKFLOW = ROOT / ".github/workflows/e004-model-load-compatibility-corrective-evidence-v1.yml"
STATIC_WORKFLOW = ROOT / ".github/workflows/e004-model-load-compatibility-corrective-static-ci-v1.yml"
HELPER = ROOT / "tools/e004_model_load_probe.cpp"
DECISION = ROOT / "specs/007-sft-v1/e004-model-load-compatibility-corrective-founder-decision-2026-09-07.md"
IMPLEMENTATION = ROOT / "specs/007-sft-v1/e004-model-load-compatibility-corrective-implementation-v1-2026-09-07.md"
TRIGGER_MARKER = ROOT / ".github/e004-model-load-compatibility-corrective-run-v1.txt"


class TestE004ModelLoadCompatibilityCorrectivePolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = CORRECTIVE_WORKFLOW.read_text(encoding="utf-8")
        cls.static_workflow = STATIC_WORKFLOW.read_text(encoding="utf-8")
        cls.helper = HELPER.read_text(encoding="utf-8")
        cls.decision = DECISION.read_text(encoding="utf-8")
        cls.implementation = IMPLEMENTATION.read_text(encoding="utf-8")

    def test_corrective_evidence_workflow_is_post_merge_push_only(self) -> None:
        self.assertIn("evidence/e004-model-load-compatibility-corrective-run-v1", self.workflow)
        self.assertIn(".github/e004-model-load-compatibility-corrective-run-v1.txt", self.workflow)
        self.assertNotIn("pull_request:", self.workflow)
        self.assertNotIn("workflow_dispatch:", self.workflow)
        self.assertIn("github.run_attempt == 1", self.workflow)
        self.assertIn("fetch-depth: 2", self.workflow)
        self.assertIn("persist-credentials: false", self.workflow)
        self.assertFalse(TRIGGER_MARKER.exists())

    def test_exact_two_gguf_candidate_matrix_is_frozen(self) -> None:
        expected = {
            "Qwen/Qwen3-0.6B-Base": "da87bfb608c14b7cf20ba1ce41287e8de496c0cd",
            "Qwen/Qwen3.5-0.8B-Base": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
        }
        self.assertEqual(self.workflow.count("          - candidate_id:"), 2)
        for candidate_id, revision in expected.items():
            self.assertEqual(self.workflow.count(f"candidate_id: {candidate_id}"), 1)
            self.assertEqual(self.workflow.count(f"revision: {revision}"), 1)
        self.assertEqual(self.workflow.count("route: LLAMA_CPP_GGUF"), 2)
        self.assertNotIn("TRANSFORMERS_TORCH_CPU", self.workflow)
        self.assertNotIn("ibm-granite/granite-4.0-350m-base", self.workflow)
        self.assertNotIn("Qwen/Qwen3-4B-Base", self.workflow)
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
            self.assertIn(token, self.decision)
            self.assertIn(token, self.workflow)

    def test_original_evidence_run_is_not_reused(self) -> None:
        self.assertIn('ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID: "34063020745"', self.workflow)
        self.assertIn("AUTOMATIC_RERUN_AUTHORITY=NONE", self.decision)
        self.assertIn("FAILED_RUN_RETRY_AUTHORITY=NONE", self.decision)
        self.assertIn("SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE", self.decision)
        self.assertNotIn("evidence/e004-model-load-compatibility-run-v1", self.workflow)
        self.assertNotIn(".github/e004-model-load-compatibility-run-v1.txt", self.workflow)

    def test_exact_missing_header_is_staged_from_frozen_runtime_revision(self) -> None:
        self.assertIn(
            "fetch_header ggml/include/ggml-alloc.h ggml/include/ggml-alloc.h",
            self.workflow,
        )
        self.assertIn(
            "fetch_header ggml/include/ggml-alloc.h ggml/include/ggml-alloc.h",
            self.static_workflow,
        )
        self.assertIn("CORRECTIVE_HEADER_CLOSURE=PASS_GGML_ALLOC_INCLUDED", self.workflow)
        self.assertIn("CORRECTIVE_HEADER_CLOSURE=PASS_GGML_ALLOC_INCLUDED", self.static_workflow)
        self.assertIn(
            "fatal error: ggml-alloc.h: No such file or directory",
            self.implementation,
        )

    def test_static_pr_qualification_cannot_load_a_model(self) -> None:
        self.assertIn("pull_request:", self.static_workflow)
        self.assertIn("MODEL_BYTES_ACQUIRED=NO", self.static_workflow)
        self.assertIn("MODEL_LOAD_PERFORMED=NO", self.static_workflow)
        self.assertNotIn("huggingface.co/", self.static_workflow)
        self.assertNotIn("MODEL_WEIGHT", self.static_workflow)
        self.assertNotIn("unshare -n -- \"$ROOT/e004_model_load_probe\"", self.static_workflow)
        self.assertNotIn("workflow_dispatch:", self.static_workflow)

    def test_reason_codes_are_frozen_before_corrective_run(self) -> None:
        for token in (
            "PASS_EXACT_MODEL_LOAD_COMPLETED",
            "FAIL_MODEL_LOAD_ERROR",
            "FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD",
            "INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION",
            "INCOMPLETE_MODEL_LOAD_NOT_REACHED_PRELOAD_PREREQUISITE_FAILED",
        ):
            self.assertIn(token, self.workflow)

    def test_llama_helper_remains_model_load_only(self) -> None:
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

    def test_evidence_workflow_has_no_evaluation_or_training_invocation(self) -> None:
        prohibited = (
            "llama-perplexity",
            "--multiple-choice",
            "research_tournament.py --",
            ".generate(",
            "Trainer(",
            ".backward(",
            "optimizer.step(",
        )
        for token in prohibited:
            self.assertNotIn(token, self.workflow)


if __name__ == "__main__":
    unittest.main()
