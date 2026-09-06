from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/e004-model-load-compatibility-evidence-v1.yml"
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


if __name__ == "__main__":
    unittest.main()
