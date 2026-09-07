# E004 Operational Preflight Evidence Design — 2026-09-07

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical design base:** `f1ac05218f4b2483bd782e59d64bf5e476cef01a`  
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v47-2026-09-07.md`  
**Artifact class:** repository-only pre-execution evidence design  
**Authority effect:** NONE  
**Model execution effect:** NONE  
**Tournament execution effect:** NONE  
**A15 effect:** NONE  
**Training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Design the narrowest fail-closed evidence mechanism needed to resolve the V47 operational preflight frontier without using historical mutable GitHub-hosted runner observations as if they were the exact future tournament environment.

V47 currently requires real evidence for:

```text
ORCHESTRATOR_IMPLEMENTATION_BINDING
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT
EXACT_COMPUTE_RESOURCE_IDENTITY
RESOURCE_AUTHORIZATION_BASIS
EXPECTED_CPU_RAM_DISK_ENVELOPE
EXPECTED_MAX_WALLCLOCK
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT
EXACT_CREDENTIAL_STATE_BINDING
NETWORK_DURING_TOURNAMENT_EXECUTION_BINDING
RETENTION_BINDING_FOR_TOURNAMENT
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING
```

This design deliberately does not make any of those fields PASS.

## 2. Why historical runtime evidence is insufficient

The canonical successor runtime-binding evidence run established exact software/runtime identities on one historical GitHub-hosted runner image. That record correctly states that future runner-image or package drift requires fresh reconciliation.

Therefore:

```text
HISTORICAL_RUNNER_IMAGE_EQUALS_FUTURE_EXECUTION_ENVIRONMENT=NO
HISTORICAL_RESOURCE_CAPACITY_EQUALS_FUTURE_RESOURCE_BINDING=NO
HISTORICAL_CREDENTIAL_STATE_EQUALS_FUTURE_CREDENTIAL_BINDING=NO
HISTORICAL_NETWORK_NAMESPACE_CAPABILITY_EQUALS_FUTURE_NETWORK_BINDING=NO
```

The active execution path must fail closed on mutable-host drift rather than infer compatibility.

## 3. Circularity that must be avoided

The already-canonical Founder successor Decision B authorizes model/tournament execution only after exact PASS preflight.

It therefore cannot be used circularly to run a model, benchmark, or tournament in order to create the missing preflight evidence that is required before that execution becomes startable.

```text
MODEL_EXECUTION_TO_PROVE_PREFLIGHT=PROHIBITED
TOURNAMENT_EXECUTION_TO_PROVE_PREFLIGHT=PROHIBITED
BENCHMARK_PAYLOAD_EXECUTION_TO_PROVE_PREFLIGHT=PROHIBITED
```

A separate bounded non-model operational evidence lane is required if real runner evidence is to be collected.

## 4. Selected evidence architecture

The narrowest defensible architecture is:

```text
PHASE_1=REVIEW_FIRST_STATIC_IMPLEMENTATION
PHASE_2=EXACTLY_ONE_POST_MERGE_NO_MODEL_OPERATIONAL_EVIDENCE_RUN
PHASE_3=APPEND_ONLY_EVIDENCE_RECONCILIATION
PHASE_4=ORCHESTRATOR_AND_EXACT_SUBJECT_BINDING_ONLY_IF_EVIDENCE_PASSES
```

The evidence lane must not load model weights, execute inference, access evaluation payloads, run benchmarks, select a winner, activate A15, or train.

## 5. Runner identity model

The intended zero-spend resource class remains the standard public-repository GitHub-hosted runner:

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
```

Because the underlying VM image is mutable, the operational evidence run must capture the exact observed image identity and the later tournament must fail before any candidate/model byte acquisition if that image identity no longer matches the bound subject.

At minimum, capture:

```text
RUNNER_OS
RUNNER_ARCH
ImageOS
ImageVersion
HOST_OS_RELEASE_SHA256
KERNEL_IDENTITY
LIBC_IDENTITY
CPU_MODEL_IDENTITY
LOGICAL_CPU_COUNT
TOTAL_MEMORY_BYTES
ROOT_FILESYSTEM_TOTAL_BYTES
ROOT_FILESYSTEM_FREE_BYTES_AT_PREFLIGHT
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AT_PREFLIGHT
```

No mutable branch or generic `ubuntu-24.04` label alone is sufficient as the final exact execution-environment identity.

## 6. Same-host tournament rule

To avoid cross-candidate hardware drift, the future tournament implementation should execute all four candidates sequentially inside one job on one runner allocation, with cleanup between candidates.

```text
ONE_TOURNAMENT_JOB=REQUIRED
FOUR_CANDIDATES_SEQUENTIAL=REQUIRED
CANDIDATE_PARALLEL_JOBS=PROHIBITED
HOST_CHANGE_BETWEEN_CANDIDATES=PROHIBITED
```

This is a future implementation constraint only; no tournament workflow is authorized by this design.

## 7. Sequential workspace rule

The canonical candidate bundle set contains a large control bundle, so staging all four candidate bundles simultaneously is unnecessary and increases disk-pressure risk.

The future execution route must use:

```text
ONE_CANDIDATE_BUNDLE_STAGED_AT_A_TIME=REQUIRED
PREVIOUS_CANDIDATE_CLEANUP_BEFORE_NEXT_ACQUISITION=REQUIRED
NO_CROSS_CANDIDATE_WEIGHT_CACHE=REQUIRED
NO_GITHUB_ACTIONS_CACHE=REQUIRED
NO_WORKFLOW_ARTIFACT_UPLOAD=REQUIRED
```

The operational evidence run itself must not acquire any candidate bytes.

## 8. Runtime reconstruction evidence

The no-model evidence lane may verify that the exact previously bound software/runtime identities can be reconstructed on the exact observed runner image.

Permitted no-model runtime checks are limited to:

### llama.cpp route

```text
ACQUIRE_EXACT_FROZEN_LLAMA_RUNTIME_ARCHIVE=YES
VERIFY_ARCHIVE_SHA256=YES
VERIFY_RUNTIME_FILE_MANIFEST_SHA256=YES
VERIFY_EXACT_LLAMA_LIBRARY_IDENTITIES=YES
VERIFY_EXACT_BACKEND_LIBRARY_IDENTITIES=YES
NO_MODEL_FILE=YES
NO_LLAMA_MODEL_LOAD=YES
```

### Transformers/PyTorch route

```text
ACQUIRE_EXACT_PREVIOUSLY_BOUND_DEPENDENCY_ARTIFACT_SET=YES
VERIFY_EVERY_DEPENDENCY_ARTIFACT_SHA256=YES
INSTALL_FROM_LOCAL_HASHED_WHEELHOUSE_ONLY=YES
VERIFY_PYTHON_RUNTIME_SHA256=YES
VERIFY_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=YES
VERIFY_TRANSFORMERS_MODULE_SHA256=YES
VERIFY_TORCH_MODULE_SHA256=YES
STATIC_IMPORT_ONLY=YES
MODEL_OBJECT_INSTANTIATED=NO
MODEL_WEIGHT_FILE_OPENED=NO
```

No resolver-selected replacement, package-version drift, external runtime substitution, or convenience dependency may be silently accepted.

## 9. Resource evidence

The evidence run must record actual capacity before any optional runtime staging and after runtime staging.

Required observations:

```text
LOGICAL_CPU_COUNT
TOTAL_MEMORY_BYTES
AVAILABLE_MEMORY_BYTES_AT_START
ROOT_FILESYSTEM_TOTAL_BYTES
ROOT_FILESYSTEM_FREE_BYTES_AT_START
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AT_START
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AFTER_RUNTIME_STAGING
```

The resulting resource record may establish the exact observed envelope only. It must not fabricate benchmark performance, model peak memory, throughput, latency, or inference capacity.

```text
MODEL_PEAK_MEMORY_MEASURED=NO
MODEL_LATENCY_MEASURED=NO
MODEL_THROUGHPUT_MEASURED=NO
RESOURCE_EVIDENCE_EQUALS_MODEL_PERFORMANCE_EVIDENCE=NO
```

## 10. Credential and access boundary

The evidence workflow must use the minimum repository permission required to check out the canonical repository and must persist no checkout credential.

Required policy:

```text
WORKFLOW_PERMISSIONS=CONTENTS_READ_ONLY
CHECKOUT_PERSIST_CREDENTIALS=false
HF_TOKEN_USE=PROHIBITED
HUGGING_FACE_HUB_TOKEN_USE=PROHIBITED
GH_TOKEN_USE_BY_CUSTOM_STEPS=PROHIBITED
CLOUD_CREDENTIAL_USE=PROHIBITED
PACKAGE_REGISTRY_CREDENTIAL_USE=PROHIBITED
PRIVATE_OR_GATED_ASSET_ACCESS=PROHIBITED
```

The workflow may test only that known credential variables are absent/unset from custom execution steps. It must not print secret values or enumerate protected secret stores.

The final evidence record may bind only:

```text
EXECUTION_SUBJECT_ACCESS_CLASS=PUBLIC_UNGATED_ONLY
CREDENTIALS_REQUIRED_FOR_EXECUTION=NO
PRIVATE_GOLD_ACCESS=NO
PHI_ACCESS=NO
GATED_ASSET_ACCESS=NO
```

## 11. Network boundary

Network is permitted only during explicit public runtime/dependency provisioning needed for the no-model reconstruction evidence.

Allowed destination families must be statically bounded in the future reviewed workflow to the exact sources required by canonical runtime identities.

After staging, runtime validation must occur with outbound network disabled using the already-reviewed unprivileged network-namespace pattern when available.

The evidence run must also prove the network-disable mechanism itself without accessing candidate or evaluation payloads.

```text
PROVISIONING_NETWORK=BOUNDED_PUBLIC_RUNTIME_DEPENDENCIES_ONLY
MODEL_PROVIDER_NETWORK=PROHIBITED
HUGGING_FACE_MODEL_ENDPOINT=PROHIBITED
EVALUATION_DATA_ENDPOINT=PROHIBITED
POST_STAGING_RUNTIME_VALIDATION_NETWORK=DEFAULT_DENY
```

## 12. Retention boundary

The operational run must prove cleanup mechanics using only non-sensitive synthetic sentinels and runtime staging files.

Required behavior:

```text
EPHEMERAL_WORKSPACE_ONLY=YES
SYNTHETIC_RETENTION_SENTINEL_CREATED=YES
WORKSPACE_REMOVED_AT_END=YES
RETENTION_SENTINEL_ABSENT_AFTER_CLEANUP=YES_REQUIRED_FOR_PASS
RUNTIME_STAGING_ABSENT_AFTER_CLEANUP=YES_REQUIRED_FOR_PASS
CACHE_UPLOAD=NO
ARTIFACT_UPLOAD=NO
RELEASE_ASSET_UPLOAD=NO
REPOSITORY_BINARY_COMMIT=NO
```

This proves the cleanup mechanism on the exact runner image. It does not rewrite the historical Transformers cleanup limitation.

## 13. Zero-spend boundary

The operational evidence lane is limited to the existing standard public-repository GitHub-hosted runner class and must not create procurement or payment authority.

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PAID_COMPUTE=PROHIBITED
LARGER_RUNNER=PROHIBITED
EXTERNAL_PAID_API=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
```

If the standard runner cannot satisfy the evidence lane, the run must fail closed. No automatic upgrade to another resource class is permitted.

## 14. Evidence output

Evidence must be emitted to job logs only and then reconciled into a reviewed repository record.

No workflow artifact is required.

The evidence record must include at least:

```text
WORKFLOW_RUN_ID
RUN_NUMBER
RUN_ATTEMPT
RUN_HEAD_SHA
IMPLEMENTATION_CANONICAL_MERGE
RUNNER_LABEL
RUNNER_OS
RUNNER_ARCH
IMAGE_OS
IMAGE_VERSION
HOST_OS_RELEASE_SHA256
KERNEL_IDENTITY
LIBC_IDENTITY
CPU_MODEL_IDENTITY
LOGICAL_CPU_COUNT
TOTAL_MEMORY_BYTES
AVAILABLE_MEMORY_BYTES_AT_START
ROOT_FILESYSTEM_TOTAL_BYTES
ROOT_FILESYSTEM_FREE_BYTES_AT_START
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AT_START
RUNNER_TEMP_FILESYSTEM_FREE_BYTES_AFTER_RUNTIME_STAGING
LLAMA_RUNTIME_IDENTITY_STATE
TRANSFORMERS_RUNTIME_IDENTITY_STATE
NETWORK_DISABLE_MECHANISM_STATE
CREDENTIAL_BOUNDARY_STATE
RETENTION_CLEANUP_STATE
ACCESS_CLASS
SPEND_USD
```

## 15. Pass/fail semantics

A successful workflow conclusion is necessary but not sufficient. Canonical reconciliation must classify each field.

The operational evidence lane may become PASS only when all required exact observations exist and every identity/boundary check passes.

Examples:

```text
RUNNER_IMAGE_IDENTITY_MISSING=INCOMPLETE
RUNTIME_IDENTITY_MISMATCH=FAIL
DEPENDENCY_ARTIFACT_IDENTITY_MISMATCH=FAIL
NETWORK_DISABLE_MECHANISM_UNAVAILABLE=INCOMPLETE
CREDENTIAL_BOUNDARY_VIOLATION=FAIL
RETENTION_CLEANUP_FAILURE=FAIL
RESOURCE_OBSERVATION_MISSING=INCOMPLETE
PAID_OR_SUBSTITUTED_RESOURCE_CLASS=FAIL
```

No model-level result can be inferred from this lane.

## 16. Single-run discipline

If separately authorized, the evidence lane must use exactly one new post-merge run.

```text
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
SECOND_MARKER_RUN_AUTHORITY=NONE
```

A failed/incomplete run is evidence. It is not an invitation to retry.

## 17. Required authority transition

The current canonical authority does not permit using model/tournament execution to create its own prerequisites. A new exact Founder decision surface is therefore required before implementation of a live evidence workflow or any empirical operational evidence run.

The paired decision request is:

`specs/007-sft-v1/e004-operational-preflight-evidence-founder-decision-request-2026-09-07.md`

Until an exact post-canonical Founder token is supplied and separately captured:

```text
OPERATIONAL_PREFLIGHT_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
```

## 18. Non-expansion boundary

```text
MODEL_WEIGHT_ACQUISITION_AUTHORITY_EXPANSION=NONE
MODEL_LOAD_AUTHORITY_EXPANSION=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
WINNER_SELECTION_AUTHORITY_EXPANSION=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
GATED_ASSET_AUTHORITY=NONE
CREDENTIAL_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
