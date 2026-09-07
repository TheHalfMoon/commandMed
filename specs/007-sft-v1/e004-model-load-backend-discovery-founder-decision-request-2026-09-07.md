# E004 Model-Load Backend-Discovery Founder Decision Request — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md`
**Canonical predecessor merge:** `7e490d0c174e7c96854ee196a9e2ca401da5d2d9`
**Canonical predecessor tree:** `48b31bde037a81c82986ea82676b72dba1c5e08b`
**Artifact class:** Founder decision request only
**Authority effect before exact post-canonical Founder token:** NONE
**Current authorized spend:** USD 0

## 1. Decision question

The single corrective model-load compatibility evidence run is consumed. It corrected the prior missing-header prerequisite defect, reached the exact load-only model call for both frozen GGUF candidates, and produced empirical `FAIL_MODEL_LOAD_ERROR` for both because the frozen llama.cpp runtime reported that no backend was loaded.

The Founder must now choose whether to preserve that empirical failure state or authorize one new review-first, post-merge, zero-spend backend-discovery corrective lane limited to the same exact two frozen GGUF candidates.

No current rerun, retry, or further model-load authority exists.

## 2. Current canonical empirical state

```text
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_GGUF_EMPIRICAL_FAIL
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
TRANSFORMERS_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS_FOR_BOTH_FROZEN_TRANSFORMERS_CANDIDATES_FROM_ORIGINAL_CONSUMED_RUN
LLAMA_CPP_GGUF_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL_FOR_BOTH_FROZEN_GGUF_CANDIDATES_MODEL_LOAD_ERROR_NO_BACKENDS_LOADED
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

The observed llama.cpp diagnostic for both frozen GGUF candidates was:

```text
llama_model_load_from_file_impl: no backends are loaded. hint: use ggml_backend_load() or ggml_backend_load_all() to load a backend before calling this function
```

## 3. Repository-only diagnosis of the backend-discovery failure

The reviewed helper remains load-only and already calls:

```cpp
llama_backend_init();
```

At the exact frozen llama.cpp source revision `c1d0e7a004015f23bc0233470b747b596f29b264`, `llama_backend_init()` calls `ggml_backend_load_all()` when no backend registry is populated.

At that same exact source revision, `ggml_backend_load_all()` uses the default dynamic-backend search path when no explicit path is supplied. The default search path is:

```text
1. executable directory
2. current working directory
```

The loader searches for dynamic backend libraries matching `libggml-<backend>-*.so` and then `libggml-<backend>.so`, including the CPU backend.

The corrective evidence workflow compiled the helper at a temporary root path while the verified frozen runtime libraries remained under the extracted runtime directory. The helper was then executed from the repository working directory. Therefore neither default backend-discovery location was bound to the frozen runtime library directory.

This diagnosis is consistent with all observed evidence:

```text
CANDIDATE_BYTE_INTEGRITY=PASS
CORRECTIVE_HEADER_CLOSURE_GGML_ALLOC=PASS
LLAMA_RUNTIME_REBIND=PASS
MODEL_LOAD_STEP=EXECUTED
LLAMA_CPP_BACKEND_LOAD_STATE_AT_MODEL_LOAD=NO_BACKENDS_LOADED
```

No model execution or new model load was performed to reach this diagnosis.

## 4. Frozen subject remains unchanged

Any future backend-discovery corrective lane, if explicitly selected and canonically captured, is limited to exactly:

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

The already-PASS Transformers candidates may not be rerun.

## 5. Frozen llama.cpp runtime identity remains unchanged

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

Runtime substitution is not part of either decision below.

## 6. Founder decision classes

### `E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_A` — preserve current empirical failure state

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_A
```

Effect after canonical capture:

```text
BACKEND_DISCOVERY_CORRECTIVE_IMPLEMENTATION_AUTHORITY=NONE
BACKEND_DISCOVERY_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
BACKEND_DISCOVERY_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
ADDITIONAL_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUN_AUTHORITY=NONE
```

The two GGUF candidates remain empirical `FAIL_MODEL_LOAD_ERROR` and the four-candidate model-load compatibility gate remains failed.

### `E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_B` — authorize one exact backend-discovery corrective lane

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_B
```

Effect only after this request is canonical and the exact token is separately captured in a canonical Founder decision record:

```text
BACKEND_DISCOVERY_CORRECTIVE_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_STATIC_ONLY
BACKEND_DISCOVERY_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
BACKEND_DISCOVERY_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=AUTHORIZED_EXACT_TWO_PUBLIC_UNGATED_CANONICAL_GGUF_BUNDLES_ONLY
BACKEND_DISCOVERY_CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
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

## 7. Exact implementation boundary under Decision B

Decision B would authorize preparation of a review-first implementation only after the exact token is canonically captured.

The implementation may only:

1. verify the exact frozen runtime archive and canonical runtime-file manifest;
2. statically identify the CPU backend dynamic library within that already-frozen runtime package;
3. preserve `tools/e004_model_load_probe.cpp` semantics unchanged;
4. bind the helper's execution-time backend discovery to the verified frozen runtime library directory by staging the helper beside that directory or setting that exact directory as the process working directory before the existing `llama_backend_init()` call runs;
5. add or strengthen static policy tests for this exact backend-discovery correction;
6. create a dedicated post-merge-only evidence workflow limited mechanically to the same two frozen GGUF candidates;
7. perform exactly one newly authorized post-merge backend-discovery corrective evidence workflow run only after exact-head qualification, guarded merge, and post-merge canonical reverification.

The implementation must fail closed before any model load if the frozen runtime package does not contain a discoverable CPU backend library consistent with the exact frozen archive and runtime-file manifest.

The implementation may not add context creation, decode, encode, sampler, prompt, forward pass, logits computation, token generation, perplexity, benchmark, evaluation payload, tournament, winner selection, A15 activation, or training behavior.

## 8. Exact one-run boundary under Decision B

```text
MAX_AUTHORIZED_BACKEND_DISCOVERY_CORRECTIVE_WORKFLOW_RUNS=1
AUTHORIZED_BACKEND_DISCOVERY_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_BACKEND_DISCOVERY_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

The original run `34063020745` and first corrective run `34150708258` remain consumed and must not be rerun, retried, or mutated.

## 9. Acquisition, network, credentials, retention, resource, and finance boundary

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_ONLY
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

## 10. Review-first and post-merge boundary

Before any future backend-discovery corrective evidence trigger exists:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
PULL_REQUEST_MODEL_BYTE_ACQUISITION=PROHIBITED
REVIEW_FIRST_WORKFLOW_PREPARATION=REQUIRED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
BACKEND_DISCOVERY_PATH_BINDING=REQUIRED
CORRECTIVE_AUTHORITY_TOKEN_BINDING=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

Independent repository review remains optional by default under FD-007. A skipped, quota-limited, or unavailable automated review must not be represented as substantive independent review evidence.

## 11. Non-expansion statement

Even if a future separately authorized backend-discovery corrective run produced GGUF model-load PASS, it would not establish or activate:

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

No tournament, winner, A15, E005, training-readiness, or project-completion claim may be inferred.

## 12. Exact post-canonical selection requirement

This request creates no backend-discovery corrective execution authority by itself.

After this request is canonically merged, the Founder must supply exactly one of:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_A
```

or:

```text
FOUNDER_E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION_B
```

The selected token must be captured in a separate canonical Founder decision record before any backend-discovery corrective implementation is treated as execution-authorized.

Broad continuation, ordinary approval, or any earlier Founder token does not substitute for this new exact decision.

## 13. Current disposition before canonical merge

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md
BACKEND_DISCOVERY_DECISION_SURFACE=NOT_YET_CANONICAL
POST_CANONICAL_EXACT_BACKEND_DISCOVERY_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_MODEL_LOAD_BACKEND_DISCOVERY_CORRECTIVE_DECISION=ABSENT
BACKEND_DISCOVERY_CORRECTIVE_IMPLEMENTATION_AUTHORITY=NONE
BACKEND_DISCOVERY_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
BACKEND_DISCOVERY_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
