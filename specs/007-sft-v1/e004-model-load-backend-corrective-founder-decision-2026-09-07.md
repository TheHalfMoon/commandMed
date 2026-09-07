# E004 Model-Load Backend Corrective Founder Decision — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical backend-corrective decision request:** `specs/007-sft-v1/e004-model-load-backend-corrective-founder-decision-request-2026-09-07.md`
**Backend-corrective decision-request PR:** #289
**Backend-corrective decision-request canonical merge:** `6ed44a1ad675dccd0a7c3351de01d2e32a405312`
**Canonical predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v44-2026-09-07.md`
**Canonical predecessor main:** `721114a332af994201f2a7d3be268765e9c9ddcc`
**Artifact class:** Founder decision capture
**Decision owner:** Founder
**Decision state before canonical merge:** CAPTURED_PENDING_CANONICAL_MERGE
**Current authorized spend:** USD 0

## 1. Exact post-canonical Founder token

After the backend-corrective decision request became canonical through merge `6ed44a1ad675dccd0a7c3351de01d2e32a405312`, and after V44 became the canonical current frontier, the Founder separately supplied exactly:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B
```

Exact token SHA-256:

```text
FOUNDER_BACKEND_CORRECTIVE_DECISION_TOKEN_SHA256=cec425a5904823c7edaaff25ce8633c64e7a40930721679da204382cc62191ae
```

This is the operative post-canonical Decision B token required by the canonical backend-corrective decision surface. It is not inferred from broad continuation, ordinary authorization, prior decision tokens, or any earlier approval.

## 2. Decision effect after canonical merge

Only after this decision record is canonically merged, and only while every exact constraint in the canonical backend-corrective decision request remains satisfied:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B
BACKEND_CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST
BACKEND_REGISTRATION_STATIC_PROBE_AUTHORITY=AUTHORIZED_EXACT_FROZEN_RUNTIME_NO_MODEL_BYTES_ONLY
BACKEND_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=AUTHORIZED_EXACT_TWO_PUBLIC_UNGATED_CANONICAL_GGUF_BUNDLES_ONLY_POST_MERGE_EVIDENCE_RUN
BACKEND_CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY_POST_MERGE
BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW_AUTHORITY=AUTHORIZED_ONE_NEW_SUCCESSOR_WORKFLOW_RUN
PRIOR_CORRECTIVE_RUN_RERUN_AUTHORITY=NONE
PRIOR_CORRECTIVE_RUN_RETRY_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B creates one new prospective successor lane. It does not reopen, rerun, retry, mutate, or replace either consumed workflow run `34063020745` or `34150708258`.

## 3. Frozen successor subject

The authorized successor subject is exactly:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

Parent identities remain frozen:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

No candidate, revision, artifact, bundle, tokenizer/config identity, role, runtime route, or parent identity may be substituted. The two historical Transformers PASS candidates remain outside this authority and may not be rerun.

## 4. Frozen llama.cpp runtime identity

No runtime substitution is permitted:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

A mismatch fails closed and does not authorize another archive, a rebuilt runtime, a system-installed backend, a package-manager backend, another source revision, or any ambient backend path.

## 5. Review-first implementation boundary

After canonical merge of this decision record, the review-first implementation may only:

1. preserve the exact two frozen GGUF candidates and exact parent bundle/protocol identities;
2. preserve the exact frozen llama.cpp source/archive/runtime identities;
3. deterministically derive the exact runtime library directory from the verified frozen runtime archive;
4. bind exact dynamic-backend library filenames, byte counts, and SHA-256 values from that same archive before merge;
5. modify the existing load-only helper only enough to register dynamic backends from the verified runtime library directory using `ggml_backend_load_all_from_path` before model construction;
6. fail closed before model load when `ggml_backend_reg_count()` is zero;
7. optionally perform a no-model backend-registration static probe using the exact frozen runtime only, without candidate/model bytes and without calling `llama_model_load_from_file`;
8. add or strengthen static policy tests for the bounded helper and workflow;
9. add exactly one new versioned post-merge-only evidence workflow mechanically limited to the two frozen GGUF candidates.

Allowed helper/runtime API surface:

```text
llama_backend_init
ggml_backend_load_all_from_path
ggml_backend_reg_count
llama_model_default_params
llama_model_load_from_file
llama_model_free
llama_backend_free
```

Prohibited helper/runtime behavior:

```text
CONTEXT_CREATION=PROHIBITED
TOKENIZATION=PROHIBITED
DECODE=PROHIBITED
ENCODE=PROHIBITED
BATCH_EXECUTION=PROHIBITED
SAMPLER_CREATION_OR_USE=PROHIBITED
PROMPT_PROCESSING=PROHIBITED
FORWARD_PASS=PROHIBITED
LOGITS_COMPUTATION=PROHIBITED
INFERENCE=PROHIBITED
GENERATION=PROHIBITED
PERPLEXITY=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
WINNER_SELECTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
```

## 6. PR qualification boundary

Before any successor evidence run:

```text
PULL_REQUEST_CANDIDATE_OR_MODEL_BYTES=PROHIBITED
PULL_REQUEST_MODEL_LOAD=PROHIBITED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
EXACT_FROZEN_RUNTIME_ARCHIVE_REVERIFICATION=REQUIRED
EXACT_RUNTIME_FILE_MANIFEST_REVERIFICATION=REQUIRED
EXACT_BACKEND_LIBRARY_DIRECTORY_BINDING=REQUIRED
EXACT_BACKEND_LIBRARY_FILE_IDENTITY_BINDING=REQUIRED
PATH_BOUND_BACKEND_DISCOVERY=REQUIRED
ZERO_REGISTERED_BACKENDS_FAIL_CLOSED=REQUIRED
NO_MODEL_STATIC_BACKEND_REGISTRATION_PROBE=PASS_REQUIRED_IF_IMPLEMENTED
LOAD_ONLY_HELPER_POLICY=REQUIRED
EXACT_TWO_GGUF_MATRIX_BINDING=REQUIRED
TRANSFORMERS_RERUN_EXCLUSION=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

Independent repository review remains optional by default under FD-007 unless later bounded governance explicitly requires it. Automated review that is absent, unavailable, or skipped must not be represented as substantive independent review evidence.

## 7. Exactly-one successor workflow-run boundary

```text
MAX_AUTHORIZED_BACKEND_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_BACKEND_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_BACKEND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

Any successor evidence must use a new versioned workflow and marker surface. GitHub rerun/retry actions on consumed runs remain unauthorized.

## 8. Empirical disposition boundary

```text
BACKEND_REGISTRATION_ZERO_OR_UNAVAILABLE=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY
BACKEND_LIBRARY_IDENTITY_MISMATCH=INCOMPLETE_RUNTIME_IDENTITY_GATE
MODEL_LOAD_EXIT_0=PASS_EXACT_MODEL_LOAD_COMPLETED
MODEL_LOAD_EXIT_137_OR_143=INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
MODEL_LOAD_EXIT_134_OR_139=FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
OTHER_NONZERO_MODEL_LOAD_EXIT=FAIL_MODEL_LOAD_ERROR
```

If backend registration fails before `llama_model_load_from_file`, model load has not been reached and the result must not be mislabeled as empirical model-load FAIL. Static reasoning and the optional no-model backend probe may never be promoted to empirical model-load PASS.

## 9. Acquisition, network, credential, retention, resource, and finance boundary

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_AND_EXACT_FROZEN_LLAMA_RUNTIME_ONLY
NETWORK_DURING_BYTE_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_PUBLIC_SOURCE_BYTES
NETWORK_DURING_MODEL_LOAD=PROHIBITED
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

If either candidate cannot complete load-only model construction in this exact resource/runtime envelope, the single successor run fails closed. No resource escalation or second workflow run is implied.

## 10. Non-expansion statement

Even a future successful two-GGUF successor result does not itself establish or authorize:

```text
RETROACTIVE_TRANSFORMERS_CLEANUP_PASS=NOT_ESTABLISHED
ORCHESTRATOR_IMPLEMENTATION_STATE=NOT_ESTABLISHED
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=NOT_ESTABLISHED
EXACT_COMPUTE_RESOURCE_IDENTITY=NOT_ESTABLISHED
RESOURCE_AUTHORIZATION_BASIS=NOT_ESTABLISHED
EXPECTED_CPU_RAM_DISK_ENVELOPE=NOT_ESTABLISHED
EXPECTED_MAX_WALLCLOCK=NOT_ESTABLISHED
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=NOT_ESTABLISHED
EXACT_CREDENTIAL_STATE_BINDING=NOT_ESTABLISHED
NETWORK_DURING_TOURNAMENT_EXECUTION_BINDING=NOT_ESTABLISHED
RETENTION_BINDING_FOR_TOURNAMENT=NOT_ESTABLISHED
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=NOT_ESTABLISHED
A1_A14_APPLICABLE_PASS_SNAPSHOT=NOT_ESTABLISHED
A15_ACTIVATION=NOT_ESTABLISHED
TOURNAMENT_EXECUTION_AUTHORIZED_NOW=NO
WINNER_SELECTION_AUTHORIZED_NOW=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
```

No tournament, winner, A15, E005, training-readiness, or project-completion claim may be inferred from this decision or from a future load-only PASS.

## 11. Current disposition before canonical merge

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v44-2026-09-07.md
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B
POST_CANONICAL_EXACT_BACKEND_CORRECTIVE_FOUNDER_DECISION_TOKEN=CAPTURED_PENDING_CANONICAL_MERGE
BACKEND_CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=PENDING_CANONICAL_DECISION_CAPTURE
BACKEND_REGISTRATION_STATIC_PROBE_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
BACKEND_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
BACKEND_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
PRIOR_CORRECTIVE_RUN_RERUN_AUTHORITY=NONE
PRIOR_CORRECTIVE_RUN_RETRY_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

After canonical merge, live repository truth and exact authority must be reverified before any implementation preparation, static backend-registration probe, candidate byte acquisition, model load, or evidence workflow execution is treated as authorized.
