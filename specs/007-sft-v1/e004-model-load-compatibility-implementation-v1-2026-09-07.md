# E004 Model-Load Compatibility Implementation V1 — 2026-09-07

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Authority:** `FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_B`
**Authority record:** `specs/007-sft-v1/e004-model-load-compatibility-founder-decision-2026-09-07.md`
**Authority frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v40-2026-09-07.md`
**Implementation state:** REVIEW_FIRST_NOT_YET_CANONICAL
**Model load performed by this record:** NO
**Current authorized spend:** USD 0

## 1. Purpose

Bind the exact review-first implementation for the single Decision-B model-load compatibility evidence run. This implementation exists only to answer whether each exact frozen `SP007-RO-001` candidate can be loaded by its exact frozen runtime route without any forward pass, inference, generation, benchmark/evaluation payload, tournament, winner selection, A15 activation, training, protected-data access, credential use, paid compute, procurement, payment, or spend.

This record does not itself execute the evidence run and does not expand Decision B.

## 2. Exact implementation surfaces

```text
EVIDENCE_WORKFLOW=.github/workflows/e004-model-load-compatibility-evidence-v1.yml
LLAMA_LOAD_ONLY_HELPER=tools/e004_model_load_probe.cpp
STATIC_POLICY_TEST=tests/spec007/test_e004_model_load_compatibility_policy.py
STATIC_QUALIFICATION_WORKFLOW=.github/workflows/e004-research-component-tournament-control-plane-v1.yml
```

The dedicated evidence workflow intentionally has no `pull_request` or `workflow_dispatch` trigger. Pull-request qualification is static-only through the existing E004 control-plane workflow.

## 3. Frozen four-candidate subject

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

The evidence workflow contains exactly four matrix records, in frozen order:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b | TRANSFORMERS_TORCH_CPU | PRIMARY
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539 | TRANSFORMERS_TORCH_CPU | CONTROL_WINNER_INELIGIBLE
```

Candidate acquisition metadata is derived from and validated against the canonical bundle-set JSON rather than caller input.

## 4. Exact post-merge trigger contract

The only model-load trigger is:

```text
EVENT=push
BRANCH=evidence/e004-model-load-compatibility-run-v1
MARKER=.github/e004-model-load-compatibility-run-v1.txt
MAX_AUTHORIZED_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CANDIDATE_PROBES_PER_WORKFLOW=4_EXACTLY_ONE_PER_FROZEN_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
```

The future marker commit must be the direct child of the canonical implementation merge and must contain exactly the canonical merge bindings required by the workflow:

```text
E004_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=AUTHORIZED_SINGLE_RUN
IMPLEMENTATION_CANONICAL_MERGE=<canonical implementation merge sha>
DECISION_CANONICAL_MERGE=e34bc6eafd92a3dbbc4c9cfa99701a1241efac29
AUTHORITY_FRONTIER_CANONICAL_MERGE=a805381020405ad0d1bb0038dc68994c6c316ce1
```

Every candidate job requires `github.run_attempt == 1`. A later rerun attempt therefore executes no model-load job and cannot be represented as authorized evidence.

## 5. Candidate-byte acquisition and integrity gate

Before runtime use, each job:

1. validates the canonical four-candidate bundle set with `validate_candidate_artifact_bundle_set`;
2. selects exactly one matrix-bound candidate/revision;
3. derives every file path, byte count, SHA-256, source repository, and immutable source revision from the canonical bundle record;
4. acquires only those exact public/ungated files;
5. verifies every exact byte count and SHA-256 before moving a temporary download into the local source directory;
6. rejects symbolic links and file-count drift.

Ordinary transport retries are restricted to the same exact public source URL/revision/path and occur only before the SHA-256 gate.

```text
CANDIDATE_SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_ONLY
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
```

## 6. llama.cpp load-only route

The two GGUF candidates use the already-bound llama.cpp identity:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
```

The reviewed helper performs only:

```text
llama_backend_init
llama_model_default_params
llama_model_load_from_file
llama_model_free
llama_backend_free
```

It sets CPU-only model parameters and contains no context creation, `llama_decode`, `llama_encode`, batch construction, sampler, prompt, generation, perplexity, benchmark, evaluation, or training operation. The helper is compiled against the exact rebound `libllama` after exact source headers are staged from the frozen llama.cpp revision.

## 7. Transformers/PyTorch CPU load-only route

The two Safetensors candidates use the already-bound runtime identities:

```text
TRANSFORMERS_SOURCE_REVISION=753d61104116eefc8ffc977327b441ee0c8d599f
TRANSFORMERS_VERSION=4.57.6
TORCH_VERSION=2.11.0+cpu
PYTHON_RUNTIME_VERSION=3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
```

The exact previously-evidenced dependency closure is restaged and must reproduce the frozen dependency-set and installed-environment hashes before model loading. Installation and runtime checks occur offline after staging.

The load operation is limited to local `AutoConfig.from_pretrained` plus local `AutoModelForCausalLM.from_pretrained` with:

```text
local_files_only=True
trust_remote_code=False
use_safetensors=True
HF_HUB_OFFLINE=1
TRANSFORMERS_OFFLINE=1
CUDA_VISIBLE_DEVICES=<empty>
```

No tokenizer construction is required for the compatibility question, although all tokenizer/config bytes in the canonical candidate bundle remain subject to the acquisition-integrity gate.

## 8. Network and credential boundary during model loading

Every actual model-load process runs in a separate Linux network namespace using `unshare -n`. Credential variables are unset before load and no repository/user/founder credential is passed into the namespace.

```text
NETWORK_DURING_MODEL_LOAD=PROHIBITED_ENFORCED_UNSHARE_N
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```

## 9. Frozen empirical disposition contract

A zero exit status after all identity/integrity gates yields:

```text
EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS
EMPIRICAL_MODEL_LOAD_REASON_CODE=PASS_EXACT_MODEL_LOAD_COMPLETED
```

Non-zero load outcomes are classified before the run as follows:

```text
EXIT_137_OR_143=INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
EXIT_134_OR_139=FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
OTHER_NONZERO_LOAD_EXIT=FAIL_MODEL_LOAD_ERROR
```

A runtime, authority, marker, source-integrity, dependency-identity, workflow-infrastructure, or policy preflight failure fails the job closed and is not converted into empirical PASS.

Static support, previous import evidence, executable identity, or deterministic argv is never promoted to empirical model-load PASS.

## 10. Resource, retention, and finance boundary

```text
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
RESOURCE_ESCALATION_AUTHORITY=NONE
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

Every candidate job has an unconditional cleanup step that removes its candidate bytes, runtime bytes, wheelhouse, virtual environment, and local manifests from the ephemeral runner. No upload/cache action is present.

## 11. Review-first qualification boundary

Before any evidence trigger is created, the implementation PR must genuinely satisfy:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
EXACT_HEAD_STATIC_QUALIFICATION=PASS_REQUIRED
AUTHORITY_TOKEN_BINDING=PASS_REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=PASS_REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=PASS_REQUIRED
```

The static policy suite verifies the dedicated workflow trigger, exact candidate matrix, runner class, one-attempt guard, no artifact/cache path, offline model-load namespace, frozen reason codes, and the absence of forward/generation/evaluation/training operations from the reviewed helper/workflow.

Independent repository review remains optional by default under FD-007; no skipped status may be represented as substantive review evidence.

## 12. Evidence effect and non-closure

The single authorized run may close only exact per-candidate empirical model-load/runtime-format compatibility facts directly observed in its logs. It does not by itself close future tournament execution environment/resource/access/finance bindings, the A1-A14 snapshot, A15, tournament execution, winner selection, E005, or training.

```text
MODEL_EXECUTION_AUTHORIZED_NOW=NO
TOURNAMENT_EXECUTION_AUTHORIZED_NOW=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```
