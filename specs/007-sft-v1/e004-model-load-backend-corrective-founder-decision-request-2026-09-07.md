# E004 Model-Load Backend Corrective Founder Decision Request — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md`
**Canonical predecessor merge:** `7e490d0c174e7c96854ee196a9e2ca401da5d2d9`
**Repository-only diagnosis:** `specs/007-sft-v1/e004-model-load-backend-registration-diagnosis-2026-09-07.md`
**Artifact class:** Founder decision request only
**Authority effect before exact post-canonical Founder token:** NONE
**Current authorized spend:** USD 0

## 1. Decision question

The original four-candidate model-load compatibility run and the later two-GGUF corrective run are both consumed.

The corrective run fixed the prior missing-header prerequisite, reached `llama_model_load_from_file` for both frozen GGUF candidates, and produced empirical `FAIL_MODEL_LOAD_ERROR` for both because the exact frozen llama.cpp runtime had no registered backend at model-load time.

Repository-only frozen-source diagnosis establishes that this llama.cpp revision exposes dynamic backend-registration APIs and that its own simple example loads dynamic backends before model loading.

The Founder must choose whether to preserve the current `2 PASS / 2 FAIL` compatibility state or authorize one new, independently bounded successor corrective lane that registers only backends from the exact already-frozen runtime before repeating load-only compatibility for exactly the same two frozen GGUF candidates.

## 2. Current canonical evidence state

```text
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
ORIGINAL_EVIDENCE_RUN=CONSUMED_NO_RERUN_AUTHORITY
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
CORRECTIVE_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_GGUF_EMPIRICAL_FAIL
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_PASS_ALL_FOUR
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
```

Current GGUF outcomes:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd=FAIL_MODEL_LOAD_ERROR_EXIT_2_NO_BACKENDS_LOADED
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68=FAIL_MODEL_LOAD_ERROR_EXIT_2_NO_BACKENDS_LOADED
```

The original Transformers PASS outcomes remain historical evidence and may not be rerun by this decision surface.

## 3. Frozen successor corrective subject

Any Decision-B successor lane is limited to exactly:

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

No candidate, revision, artifact, bundle, tokenizer/config identity, role, or runtime route may be substituted.

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

Any mismatch fails closed and does not authorize a newer release, another archive, a system-installed backend, a package-manager backend, a rebuilt runtime, or another source revision.

## 5. Frozen-source basis for the successor correction

At the exact frozen source revision:

```text
ggml/include/ggml-backend.h
```

declares:

```text
ggml_backend_reg_count
ggml_backend_load
ggml_backend_load_all
ggml_backend_load_all_from_path
```

and:

```text
ggml/src/ggml-backend-reg.cpp
```

establishes that `ggml_backend_load_all_from_path(dir_path)` searches only the caller-supplied directory for dynamic backends and attempts CPU backend discovery.

The exact frozen upstream example:

```text
examples/simple/simple.cpp
```

calls `ggml_backend_load_all()` before `llama_model_load_from_file`.

The bounded diagnosis therefore supports a path-bound registration correction using the already-verified frozen runtime library directory.

## 6. Founder decision classes

### `E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_A` — preserve the current failed compatibility gate

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_A
```

Effect after canonical capture:

```text
BACKEND_CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
BACKEND_REGISTRATION_STATIC_PROBE_AUTHORITY=NONE
BACKEND_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
BACKEND_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW_AUTHORITY=NONE
```

The exact compatibility state remains `PARTIAL_2_PASS_2_FAIL` and E004 remains blocked.

### `E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B` — authorize one new exact two-GGUF successor corrective lane

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B
```

Effect only after this request is canonical and the exact token is separately captured in a canonical Founder decision record:

```text
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

Decision B creates new prospective successor authority; it does not reopen or mutate run `34150708258` and does not authorize GitHub's rerun/retry action on any consumed workflow run.

## 7. Exact implementation boundary under Decision B

After canonical Decision-B capture, a review-first implementation may only:

1. preserve the exact frozen two-GGUF candidate subject and parent bundle/protocol identities;
2. preserve the exact frozen llama.cpp source, archive, runtime manifest, and `libllama` identities;
3. inspect the verified extracted frozen runtime archive to locate the exact directory containing its dynamic backend libraries;
4. deterministically bind the exact backend-library filenames, byte counts, and SHA-256 values from that already-frozen archive before merge;
5. modify the load-only helper only enough to register dynamic backends from that exact verified directory before `llama_model_load_from_file`;
6. use `ggml_backend_load_all_from_path` rather than ambient or system search paths;
7. fail closed before model load if zero backends are registered;
8. optionally execute a no-model static backend-registration probe during PR qualification using only the exact frozen runtime archive and no candidate/model bytes;
9. add static policy tests that prohibit any broader helper/runtime behavior;
10. add one new post-merge-only evidence workflow mechanically limited to exactly the two frozen GGUF candidates.

The implementation may not use backend libraries from any source outside the exact verified frozen runtime archive.

## 8. Helper semantic boundary

Decision B would add only dynamic backend registration and registration-count verification before the already-reviewed load-only model operation.

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

Prohibited helper/runtime operations include:

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

## 9. Review-first static qualification boundary

Before a post-merge evidence trigger exists, the implementation PR must genuinely establish:

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

The no-model static backend-registration probe, if used, must not acquire candidate/model bytes and must not call `llama_model_load_from_file`.

Independent repository review remains optional by default under FD-007 unless later bounded governance explicitly requires it.

## 10. One-new-run boundary under Decision B

The prior corrective run remains immutable and consumed.

Any Decision-B evidence must use a new versioned workflow/marker surface and exactly one new workflow run:

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

Ordinary transport retries remain limited to the same exact public source URL/revision/path before the canonical SHA-256 gate and do not authorize source substitution.

## 11. Empirical disposition boundary

Before model load, exact reason codes must distinguish backend-registration failure from model-load failure.

```text
BACKEND_REGISTRATION_ZERO_OR_UNAVAILABLE=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY
BACKEND_LIBRARY_IDENTITY_MISMATCH=INCOMPLETE_RUNTIME_IDENTITY_GATE
MODEL_LOAD_EXIT_0=PASS_EXACT_MODEL_LOAD_COMPLETED
MODEL_LOAD_EXIT_137_OR_143=INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
MODEL_LOAD_EXIT_134_OR_139=FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
OTHER_NONZERO_MODEL_LOAD_EXIT=FAIL_MODEL_LOAD_ERROR
```

An inability to register a verified backend before `llama_model_load_from_file` must not be mislabeled as empirical model-load FAIL because model load would not have been reached.

Static reasoning or a no-model backend-registration probe may never be promoted to empirical model-load PASS.

## 12. Acquisition, network, credential, retention, resource, and finance boundary

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

If either candidate cannot complete model loading inside this exact runtime/resource envelope, the single successor run must fail closed. No resource escalation or another workflow run is implied.

## 13. Non-expansion statement

Even if both future successor GGUF probes later PASS, this decision would not establish or activate:

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

## 14. Exact post-canonical selection requirement

This request creates no implementation or execution authority by itself.

After this request is canonically merged, the Founder must supply exactly one of:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_A
```

or:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B
```

The selected token must be supplied after canonical merge and captured in a separate canonical Founder decision record before any Decision-B implementation preparation or no-model backend-registration probe is treated as authorized.

A broad continuation statement, generic approval, ordinary authorization, or previously supplied token for a different decision surface does not substitute for either exact token above.

## 15. Current disposition before selection

```text
BACKEND_CORRECTIVE_DECISION_SURFACE=NOT_YET_CANONICAL
POST_CANONICAL_EXACT_BACKEND_CORRECTIVE_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=ABSENT
BACKEND_CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
BACKEND_REGISTRATION_STATIC_PROBE_AUTHORITY=NONE
BACKEND_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
BACKEND_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW_AUTHORITY=NONE
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
