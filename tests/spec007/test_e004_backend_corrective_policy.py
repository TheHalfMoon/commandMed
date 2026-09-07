from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
STATIC_WORKFLOW = ROOT / ".github/workflows/e004-backend-corrective-static-qualification-v1.yml"
EVIDENCE_WORKFLOW = ROOT / ".github/workflows/e004-model-load-backend-corrective-evidence-v1.yml"
MODEL_HELPER = ROOT / "tools/e004_model_load_probe.cpp"
BACKEND_HELPER = ROOT / "tools/e004_backend_registration_probe.cpp"
DECISION = ROOT / "specs/007-sft-v1/e004-model-load-backend-corrective-founder-decision-2026-09-07.md"


class TestE004BackendCorrectivePolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.static = STATIC_WORKFLOW.read_text(encoding="utf-8")
        cls.evidence = EVIDENCE_WORKFLOW.read_text(encoding="utf-8")
        cls.model_helper = MODEL_HELPER.read_text(encoding="utf-8")
        cls.backend_helper = BACKEND_HELPER.read_text(encoding="utf-8")
        cls.decision = DECISION.read_text(encoding="utf-8")

    def test_decision_b_is_exact_and_non_expanding(self) -> None:
        for token in (
            "FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B",
            "BACKEND_CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST",
            "BACKEND_REGISTRATION_STATIC_PROBE_AUTHORITY=AUTHORIZED_EXACT_FROZEN_RUNTIME_NO_MODEL_BYTES_ONLY",
            "BACKEND_CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY_POST_MERGE",
            "BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW_AUTHORITY=AUTHORIZED_ONE_NEW_SUCCESSOR_WORKFLOW_RUN",
            "TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE",
            "MODEL_FORWARD_PASS_AUTHORITY=NONE",
            "MODEL_INFERENCE_AUTHORITY=NONE",
            "GENERATION_AUTHORITY=NONE",
            "TOURNAMENT_EXECUTION_AUTHORITY=NONE",
            "WINNER_SELECTION_AUTHORITY=NONE",
            "A15_ACTIVATION_AUTHORITY=NONE",
            "TRAINING_AUTHORITY=NONE",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
        ):
            self.assertIn(token, self.decision)

    def test_static_qualification_is_exact_runtime_no_model_only(self) -> None:
        self.assertIn("pull_request:", self.static)
        self.assertNotIn("workflow_dispatch:", self.static)
        self.assertNotIn("repository_dispatch:", self.static)
        self.assertNotIn("huggingface.co", self.static)
        self.assertNotIn("MODEL_WEIGHT", self.static)
        self.assertNotIn("llama_model_load_from_file", self.static)
        self.assertIn("tools/e004_backend_registration_probe.cpp", self.static)
        self.assertIn("MODEL_BYTES_ACQUIRED=NO", self.static)
        self.assertIn("MODEL_LOAD_PERFORMED=NO", self.static)

    def test_exact_backend_manifest_is_bound(self) -> None:
        expected = {
            "libggml-base.so": "ebbcda9795124309a9fa492e3a7be49dbbc6b8fd7d95cde1524838f88057fcc3",
            "libggml-cpu-alderlake.so": "f1e420c6069bb3d6f310069bb3164b8a2e3895227183dc095f2d521f5d54a7e7",
            "libggml-cpu-cannonlake.so": "d7c129e27327bdbe7fe5884aa60e4a5dec9eddbf5adadd3d72f73905ab5f17ab",
            "libggml-cpu-cascadelake.so": "4e2ee9f47758426548403f75c6031baa3fc1b6c3c5d209354d947b9cf35c8c20",
            "libggml-cpu-cooperlake.so": "c706d1d1ba8804deb457f0cde14fb1cffa3f7a8e465bac0169a2c957a3f3fb4f",
            "libggml-cpu-haswell.so": "f8620357aea4dce39ccc3326626573a71c783f5dd11e49f52addb21006adbc67",
            "libggml-cpu-icelake.so": "ef2ec9d39c701e5ab9062fe5aad49d55d0a4c63b1e0eb46fbbfb5d437b6b56b8",
            "libggml-cpu-ivybridge.so": "547c9295f247cb2ba4947af75a04a5279f40479af85eadc4876282a681c3c6fd",
            "libggml-cpu-piledriver.so": "4bdbbeca90cc5b2acb32284b09b6def78546a7d897b8fead87d38a39a52035b1",
            "libggml-cpu-sandybridge.so": "9ba32dcb20048f67dc5816646edd64799048bbe2c40deaf7c2cd46a726a99e04",
            "libggml-cpu-sapphirerapids.so": "6221b414b195d1d075eb575debb93e24daf26afec7352b136146e650595d3617",
            "libggml-cpu-skylakex.so": "211269ef5a067b400c19fb10472e4f4bcecd58b724760d9e4cfa968f4c9a8cdc",
            "libggml-cpu-sse42.so": "94ee365a747ce6b81d81e32981f8c1ffa05942f39c245f3e33c05300208d7355",
            "libggml-cpu-x64.so": "a31a3e374f01e90ef60dbc8b654be972029107ed5f0c670bb211ed6d6821d490",
            "libggml-cpu-zen4.so": "17dde3b34a68055c2c5f9c6d63a6ca6a9f1b470fdf8869113495af6eaad24f87",
            "libggml-rpc.so": "aff4f89035be449fdc46d56a7e493e9eab4b7dbf09b35b170bf7d36be3709f55",
        }
        for name, sha256 in expected.items():
            self.assertIn(name, self.static)
            self.assertIn(name, self.evidence)
            self.assertIn(sha256, self.static)
            self.assertIn(sha256, self.evidence)
        for token in (
            "BACKEND_LIBRARY_DIRECTORY_RELATIVE: llama-b10621",
            'BACKEND_LIBRARY_COUNT: "16"',
            "3875fabcb38e9bb09acb0e08f6a0ffc3f97ac4acb1434c83f5ad8b656e86ab79",
        ):
            self.assertIn(token, self.static)
            self.assertIn(token, self.evidence)

    def test_model_helper_adds_only_path_bound_backend_registration_before_load(self) -> None:
        self.assertIn("ggml_backend_load_all_from_path(argv[2])", self.model_helper)
        self.assertIn("ggml_backend_reg_count()", self.model_helper)
        self.assertIn("BACKEND_REGISTRATION=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY", self.model_helper)
        self.assertIn("MODEL_LOAD_REACHED=YES", self.model_helper)
        self.assertIn("llama_model_load_from_file(argv[1], params)", self.model_helper)
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
            self.assertNotIn(prohibited, self.model_helper)

    def test_backend_registration_helper_cannot_load_a_model(self) -> None:
        self.assertIn("ggml_backend_load_all_from_path(argv[1])", self.backend_helper)
        self.assertIn("ggml_backend_reg_count()", self.backend_helper)
        self.assertNotIn("llama_model_load_from_file", self.backend_helper)
        self.assertIn("MODEL_BYTES_ACQUIRED=NO", self.backend_helper)
        self.assertIn("MODEL_LOAD_PERFORMED=NO", self.backend_helper)

    def test_successor_evidence_is_new_post_merge_single_run_two_gguf_only(self) -> None:
        self.assertIn("evidence/e004-model-load-backend-corrective-run-v1", self.evidence)
        self.assertIn(".github/e004-model-load-backend-corrective-run-v1.txt", self.evidence)
        self.assertNotIn("pull_request:", self.evidence)
        self.assertNotIn("workflow_dispatch:", self.evidence)
        self.assertNotIn("repository_dispatch:", self.evidence)
        self.assertIn("github.run_attempt == 1", self.evidence)
        self.assertEqual(self.evidence.count("          - candidate_id:"), 2)
        for candidate, revision in (
            ("Qwen/Qwen3-0.6B-Base", "da87bfb608c14b7cf20ba1ce41287e8de496c0cd"),
            ("Qwen/Qwen3.5-0.8B-Base", "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68"),
        ):
            self.assertEqual(self.evidence.count(f"candidate_id: {candidate}"), 1)
            self.assertEqual(self.evidence.count(f"revision: {revision}"), 1)
        self.assertNotIn("ibm-granite/granite-4.0-350m-base", self.evidence)
        self.assertNotIn("Qwen/Qwen3-4B-Base", self.evidence)
        self.assertNotIn("TRANSFORMERS_TORCH_CPU", self.evidence)

    def test_successor_reason_codes_and_network_boundary_are_frozen(self) -> None:
        for token in (
            "INCOMPLETE_BACKEND_REGISTRATION_NOT_READY",
            "INCOMPLETE_RUNTIME_IDENTITY_GATE",
            "PASS_EXACT_MODEL_LOAD_COMPLETED",
            "INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION",
            "FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD",
            "FAIL_MODEL_LOAD_ERROR",
            "sudo unshare -n -- env LD_LIBRARY_PATH=",
            "MODEL_FORWARD_PASS_PERFORMED=NO",
            "MODEL_INFERENCE_PERFORMED=NO",
            "GENERATION_PERFORMED=NO",
            "TOURNAMENT_EXECUTION_PERFORMED=NO",
            "TRAINING_PERFORMED=NO",
        ):
            self.assertIn(token, self.evidence)

    def test_no_retention_or_paid_compute_path_exists(self) -> None:
        for workflow in (self.static, self.evidence):
            self.assertEqual(workflow.count("runs-on: ubuntu-24.04"), 1)
            self.assertNotIn("upload-artifact", workflow)
            self.assertNotIn("actions/cache", workflow)
        self.assertIn("MODEL_BYTE_PERSISTENCE_AFTER_JOB=NO", self.evidence)
        self.assertIn("RAW_MODEL_BYTE_ARTIFACT_UPLOAD=NO", self.evidence)
        self.assertIn("ACTIONS_CACHE_FOR_MODEL_BYTES=NO", self.evidence)


if __name__ == "__main__":
    unittest.main()
