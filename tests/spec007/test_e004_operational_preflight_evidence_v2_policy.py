from __future__ import annotations

import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/e004-operational-preflight-evidence-v2.yml"
DECISION = ROOT / "specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-2026-09-08.md"
REQUEST = ROOT / "specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-request-2026-09-08.md"
IMPLEMENTATION = ROOT / "specs/007-sft-v1/e004-operational-preflight-evidence-implementation-v2-2026-09-08.md"
BUNDLE_SET = ROOT / "specs/007-sft-v1/e004-successor-candidate-artifact-bundle-set-v1.json"


class TestE004OperationalPreflightEvidenceV2Policy(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")
        cls.decision = DECISION.read_text(encoding="utf-8")
        cls.request = REQUEST.read_text(encoding="utf-8")
        cls.implementation = IMPLEMENTATION.read_text(encoding="utf-8")
        cls.bundle_set = BUNDLE_SET.read_text(encoding="utf-8")

    def test_exact_corrective_decision_b_is_canonical_and_bounded(self) -> None:
        for token in (
            "FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_B",
            "FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_TOKEN_SHA256=774f35983f70ba560b2e0bd9174a7f2f76c92c1617e76851e1123dcc7d39780e",
            "CORRECTIVE_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_V2",
            "CORRECTIVE_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=AUTHORIZED_NO_MODEL_NO_EVALUATION_PAYLOAD",
            "CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=AUTHORIZED_EXACTLY_ONE_NEW_V2_POST_MERGE_RUN",
            "MAX_AUTHORIZED_CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1",
            "CORRECTIVE_RUN_ATTEMPT_REQUIRED=1",
            "CORRECTIVE_RERUN_AUTHORITY=NONE_BY_DEFAULT",
            "CORRECTIVE_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
        ):
            self.assertIn(token, self.decision)

    def test_request_reserves_exact_v2_surface(self) -> None:
        for token in (
            "CORRECTIVE_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v2.yml",
            "CORRECTIVE_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v2",
            "CORRECTIVE_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v2.txt",
            "ANCESTRY_GUARD_CHECKOUT_FETCH_DEPTH=0",
        ):
            self.assertIn(token, self.request)

    def test_empirical_lane_has_only_exact_v2_marker_push_trigger(self) -> None:
        self.assertIn("pull_request:\n", self.workflow)
        self.assertIn("push:\n", self.workflow)
        self.assertIn("evidence/e004-operational-preflight-run-v2", self.workflow)
        self.assertIn(".github/e004-operational-preflight-run-v2.txt", self.workflow)
        self.assertNotIn("workflow_dispatch:", self.workflow)
        self.assertNotIn("repository_dispatch:", self.workflow)
        self.assertNotIn("schedule:", self.workflow)
        self.assertIn("github.run_attempt == 1", self.workflow)

    def test_marker_is_direct_child_of_merge_and_only_changed_path(self) -> None:
        for token in (
            'parent="$(git rev-parse HEAD^)"',
            'marker_parent="$(awk -F= \'$1=="IMPLEMENTATION_CANONICAL_MERGE" {print $2}\' "$EVIDENCE_MARKER")"',
            'test "$marker_parent" = "$parent"',
            'git rev-list --parents -n 1 "$parent"',
            'test "$(git rev-list --count "$parent"..HEAD)" = \'1\'',
            'test "$(git diff --name-only "$parent" HEAD)" = "$EVIDENCE_MARKER"',
            'git cat-file -e "$parent:.github/workflows/e004-operational-preflight-evidence-v2.yml"',
            "E004_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN=V2",
            "774f35983f70ba560b2e0bd9174a7f2f76c92c1617e76851e1123dcc7d39780e",
        ):
            self.assertIn(token, self.workflow)

    def test_full_history_is_required_for_both_checkouts(self) -> None:
        self.assertNotIn("fetch-depth: 2", self.workflow)
        self.assertEqual(self.workflow.count("fetch-depth: 0"), 2)

    def test_v1_is_not_reused_as_v2_execution_surface(self) -> None:
        self.assertNotIn("E004_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN=V1", self.workflow)
        self.assertNotIn("evidence/e004-operational-preflight-run-v1", self.workflow)
        self.assertNotIn(".github/e004-operational-preflight-run-v1.txt", self.workflow)
        self.assertIn("V1_RERUN=PROHIBITED", self.decision)
        self.assertIn("V1_FAILED_JOB_RERUN=PROHIBITED", self.decision)
        self.assertIn("V1_REPLAY=PROHIBITED", self.decision)

    def test_no_model_or_evaluation_execution_surface_exists(self) -> None:
        for prohibited in (
            "from_pretrained",
            "llama_model_load_from_file",
            "AutoModel",
            "pipeline(",
            "generate(",
            "evaluate.load",
            "datasets.load_dataset",
            "huggingface.co",
        ):
            self.assertNotIn(prohibited, self.workflow)
        for token in (
            "MODEL_OBJECT_INSTANTIATED=NO",
            "MODEL_WEIGHT_FILE_OPENED=NO",
            "MODEL_LOAD_PERFORMED=NO",
            "MODEL_INFERENCE_PERFORMED=NO",
            "EVALUATION_PAYLOAD_ACCESS_PERFORMED=NO",
            "TOURNAMENT_EXECUTION_PERFORMED=NO",
            "TRAINING_PERFORMED=NO",
        ):
            self.assertIn(token, self.workflow)

    def test_exact_previously_bound_runtime_identities_are_frozen(self) -> None:
        for token in (
            "c1d0e7a004015f23bc0233470b747b596f29b264",
            "2255f4747492109298a5c997f374d49c2af3113d",
            "91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583",
            "4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711",
            "f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7",
            "TRANSFORMERS_VERSION: 4.57.6",
            "753d61104116eefc8ffc977327b441ee0c8d599f",
            "TORCH_RUNTIME_TARGET: 2.11.0+cpu",
            "DEPENDENCY_ARTIFACT_COUNT: \"27\"",
            "bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05",
            "a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223",
            "54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384",
        ):
            self.assertIn(token, self.workflow)

    def test_network_boundary_is_bounded_then_default_deny(self) -> None:
        for host in (
            "github.com",
            "release-assets.githubusercontent.com",
            "objects.githubusercontent.com",
            "pypi.org",
            "files.pythonhosted.org",
            "download.pytorch.org",
        ):
            self.assertIn(host, self.workflow)
        self.assertIn("sudo -n unshare -n", self.workflow)
        self.assertIn("NETWORK_DISABLE_MECHANISM_STATE=PASS_UNSHARE_NET_NAMESPACE_NO_DEFAULT_ROUTE", self.workflow)
        self.assertIn("POST_STAGING_RUNTIME_VALIDATION_NETWORK=DEFAULT_DENY", self.workflow)

    def test_credentials_and_access_are_fail_closed(self) -> None:
        self.assertIn("persist-credentials: false", self.workflow)
        self.assertIn("permissions:\n  contents: read", self.workflow)
        for token in (
            "unset HF_TOKEN HUGGING_FACE_HUB_TOKEN GH_TOKEN GITHUB_TOKEN",
            "CREDENTIAL_BOUNDARY_STATE=PASS_NO_CUSTOM_STEP_CREDENTIALS",
            "CREDENTIALS_REQUIRED_FOR_EXECUTION=NO",
            "PRIVATE_OR_GATED_ASSET_ACCESS=NO",
            "PHI_ACCESS=NO",
        ):
            self.assertIn(token, self.workflow)
        self.assertEqual(self.bundle_set.count('"artifact_access_state":"PUBLIC_UNGATED_EXACT_IDENTITY"'), 4)

    def test_runner_resource_identity_zero_spend_and_retention_are_bounded(self) -> None:
        for token in (
            "RUNNER_LABEL=ubuntu-24.04",
            "RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER",
            "IMAGE_VERSION=",
            "HOST_OS_RELEASE_SHA256=",
            "KERNEL_IDENTITY=",
            "LIBC_IDENTITY=",
            "CPU_MODEL_IDENTITY=",
            "LOGICAL_CPU_COUNT=",
            "TOTAL_MEMORY_BYTES=",
            "RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AFTER_RUNTIME_STAGING=",
            "EXPECTED_MAX_WALLCLOCK_SECONDS=3600",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
            "synthetic-retention-sentinel-v2",
            "RETENTION_CLEANUP_STATE=PASS",
            "RUNTIME_STAGING_ABSENT_AFTER_CLEANUP=YES",
        ):
            self.assertIn(token, self.workflow)
        self.assertNotIn("actions/upload-artifact", self.workflow)
        self.assertNotIn("actions/cache", self.workflow)
        self.assertNotIn("gh release", self.workflow)

    def test_static_qualification_runs_required_regressions_and_diff_check(self) -> None:
        for token in (
            "tests.spec007.test_e004_operational_preflight_evidence_v2_policy",
            "python3 -m pytest -q tests/spec007",
            "python3 -m pytest -q",
            "git diff --check",
            "EMPIRICAL_OPERATIONAL_EVIDENCE_EXECUTED=NO",
        ):
            self.assertIn(token, self.workflow)

    def test_implementation_record_preserves_non_expansion(self) -> None:
        for token in (
            "IMPLEMENTATION_STATE=REVIEW_FIRST_NOT_CANONICAL",
            "OPERATIONAL_PREFLIGHT_EVIDENCE_V2=NOT_RUN_BY_IMPLEMENTATION_PR",
            "V1_EVIDENCE_AUTHORITY=CONSUMED_UNCHANGED",
            "MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE",
            "TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE",
            "A15_AUTHORITY_EXPANSION=NONE",
            "TRAINING_AUTHORITY=NONE",
            "CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE",
            "SUCCESSOR_PASS_PREFLIGHT=NO",
            "CURRENT_AUTHORIZED_SPEND_USD=0",
            "PROJECT_FINISHED=NO",
        ):
            self.assertIn(token, self.implementation)


if __name__ == "__main__":
    unittest.main()
