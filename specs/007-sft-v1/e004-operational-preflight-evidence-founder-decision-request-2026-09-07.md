# E004 Operational Preflight Evidence — Founder Decision Request — 2026-09-07

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical design record:** `specs/007-sft-v1/e004-operational-preflight-evidence-design-2026-09-07.md`  
**Artifact class:** Founder decision request / authority proposal only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Model execution performed:** NO  
**Tournament execution performed:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Why a new decision is required

Canonical V47 requires real operational evidence before the exact successor subject can be bound.

The already-selected successor execution Decision B authorizes model/tournament execution only after exact PASS preflight. It cannot be used circularly to execute a model or tournament in order to create missing preflight evidence.

The next bounded evidence need is therefore a no-model, no-benchmark operational environment/resource/access/credential/network/retention evidence lane.

This request creates no authority until one exact option below is selected by the Founder **after this request is canonical** and that exact token is separately captured in a canonical Founder decision record.

## 2. Decision A — keep the current blocker

Exact token:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_EVIDENCE_DECISION=E004_OPERATIONAL_PREFLIGHT_EVIDENCE_DECISION_A
```

Effect:

```text
OPERATIONAL_PREFLIGHT_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No empirical operational evidence may be collected under Decision A.

## 3. Decision B — authorize one bounded no-model operational evidence lane

Exact token:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_EVIDENCE_DECISION=E004_OPERATIONAL_PREFLIGHT_EVIDENCE_DECISION_B
```

If and only if this exact token is supplied after this request is canonical and is separately captured canonically, Decision B authorizes:

```text
OPERATIONAL_PREFLIGHT_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST
OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=AUTHORIZED_NO_MODEL_NO_EVALUATION_PAYLOAD
OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=AUTHORIZED_EXACT_PREVIOUSLY_BOUND_PUBLIC_RUNTIME_DEPENDENCIES_ONLY
OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=AUTHORIZED_EXACTLY_ONE_NEW_POST_MERGE_RUN
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B does not make any operational gate PASS by declaration. It only permits implementation, static qualification, and one evidence-producing run inside the exact boundaries below.

## 4. Exact provider/resource boundary

```text
PROVIDER=GitHub_Actions
REPOSITORY_VISIBILITY=PUBLIC
RUNNER_LABEL=ubuntu-24.04
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

If the standard runner is unavailable or insufficient, the workflow must fail closed. Decision B creates no substitution authority.

## 5. Exact run purpose

The one authorized run may only resolve and bind the following operational preflight evidence:

```text
EXACT_RUNNER_IMAGE_IDENTITY
EXACT_HOST_OS_KERNEL_LIBC_IDENTITY
EXACT_CPU_AND_MEMORY_RESOURCE_OBSERVATION
EXACT_FILESYSTEM_CAPACITY_OBSERVATION
EXACT_PREVIOUSLY_BOUND_LLAMA_RUNTIME_RECONSTRUCTION_STATE
EXACT_PREVIOUSLY_BOUND_TRANSFORMERS_RUNTIME_RECONSTRUCTION_STATE
EXACT_PUBLIC_UNGATED_ACCESS_CLASS
EXACT_CREDENTIAL_BOUNDARY_STATE
EXACT_NETWORK_DISABLE_MECHANISM_STATE
EXACT_EPHEMERAL_RETENTION_CLEANUP_STATE
EXACT_ZERO_SPEND_RESOURCE_CLASS_STATE
```

The run may not establish model performance, tournament performance, or winner evidence.

## 6. Permitted implementation preparation

After canonical Decision B capture, one review-first implementation PR may add only the smallest required evidence lane and deterministic validation/qualification surface.

Permitted repository changes include:

```text
ONE_NEW_VERSIONED_OPERATIONAL_EVIDENCE_WORKFLOW=YES
ONE_NEW_EVIDENCE_MARKER_PATH=YES
FOCUSED_OFFLINE_POLICY_TESTS=YES
DETERMINISTIC_EVIDENCE_RECORD_VALIDATOR=YES_IF_NEEDED
DOCUMENTATION_AND_REASON_CODES=YES
```

The implementation PR itself must not acquire candidate weights, load a model, execute inference, execute an evaluation payload, execute a tournament, activate A15, select a winner, or train.

## 7. Permitted no-model runtime provisioning in the one evidence run

Only previously canonical public runtime/dependency identities may be provisioned.

### llama.cpp

```text
EXACT_LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
EXACT_LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
EXACT_LLAMA_CPP_TAG=b10621
EXACT_LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
MODEL_FILE_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
```

### Transformers/PyTorch

The implementation must statically bind the exact dependency artifact identities already established by canonical runtime evidence before merge.

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
CANONICAL_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
CANONICAL_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
MODEL_OBJECT_INSTANTIATION=PROHIBITED
MODEL_WEIGHT_FILE_ACQUISITION=PROHIBITED
MODEL_WEIGHT_FILE_OPEN=PROHIBITED
```

No compatible-version resolver substitution may be accepted as equivalent to the exact previously bound dependency artifact set.

## 8. Network boundary

Network use is permitted only during explicit provisioning of the exact public runtime/dependency artifacts required by Section 7.

The future reviewed workflow must statically bind allowed destination families and commands before merge.

After staging, runtime/static validation must run with outbound network disabled using the reviewed network-namespace mechanism.

```text
MODEL_PROVIDER_ENDPOINT_ACCESS=PROHIBITED
HUGGING_FACE_MODEL_ENDPOINT_ACCESS=PROHIBITED
EVALUATION_DATA_ENDPOINT_ACCESS=PROHIBITED
ARBITRARY_WEB_ACCESS=PROHIBITED
EXTERNAL_API_GENERATION=PROHIBITED
```

## 9. Credential and protected-access boundary

```text
WORKFLOW_REPOSITORY_PERMISSION=CONTENTS_READ_ONLY
CHECKOUT_PERSIST_CREDENTIALS=false
HF_TOKEN_USE=PROHIBITED
HUGGING_FACE_HUB_TOKEN_USE=PROHIBITED
GH_TOKEN_USE_BY_CUSTOM_STEPS=PROHIBITED
CLOUD_CREDENTIAL_USE=PROHIBITED
PACKAGE_REGISTRY_CREDENTIAL_USE=PROHIBITED
PRIVATE_OR_GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
```

No credential may be invented, requested, printed, persisted, or inferred from platform bootstrap behavior.

## 10. Retention boundary

The evidence run must use only ephemeral runner storage and must prove cleanup with synthetic sentinels.

```text
GITHUB_ACTIONS_CACHE_UPLOAD=PROHIBITED
WORKFLOW_ARTIFACT_UPLOAD=PROHIBITED
RELEASE_ASSET_UPLOAD=PROHIBITED
PACKAGE_REGISTRY_UPLOAD=PROHIBITED
REPOSITORY_BINARY_COMMIT=PROHIBITED
SYNTHETIC_RETENTION_SENTINEL_ALLOWED=YES
RUNTIME_STAGING_CLEANUP_REQUIRED=YES
CLEANUP_VERIFICATION_REQUIRED=YES
```

Candidate/model bytes are prohibited, so this run cannot retroactively repair or repeat any historical model-weight cleanup event.

## 11. Explicitly prohibited actions

Decision B does **not** authorize:

```text
CANDIDATE_MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
WINNER_SELECTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
MODEL_CONVERSION=PROHIBITED
QUANTIZATION_OR_REQUANTIZATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PHI=PROHIBITED
GATED_ASSETS=PROHIBITED
PAID_COMPUTE=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 12. Trigger and single-run rule

The evidence workflow must not expose an ordinary manual or PR execution surface.

Required trigger shape:

```text
pull_request=NONE_FOR_EVIDENCE_EXECUTION
workflow_dispatch=NONE
repository_dispatch=NONE
schedule=NONE
push=EXACT_VERSIONED_EVIDENCE_BRANCH_AND_MARKER_ONLY
```

The marker commit must be a direct child of the exact canonical implementation merge and contain only the marker path.

```text
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
RUN_ATTEMPT_REQUIRED=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
RETRY_AUTHORITY=NONE_BY_DEFAULT
```

## 13. Required static qualification before merge

Before the evidence workflow implementation may merge, exact-head qualification must prove at least:

```text
AUTHORITY_PREFLIGHT_TESTS=PASS
NO_MODEL_NO_EVALUATION_PAYLOAD_POLICY_TESTS=PASS
EXACT_RUNTIME_IDENTITY_BINDING_TESTS=PASS
NETWORK_BOUNDARY_POLICY_TESTS=PASS
CREDENTIAL_BOUNDARY_POLICY_TESTS=PASS
RETENTION_CLEANUP_POLICY_TESTS=PASS
TRIGGER_SINGLE_RUN_POLICY_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
```

No green CI result may be represented as operational evidence because the implementation PR is forbidden from running the empirical evidence lane.

## 14. Post-run reconciliation rule

After the one run finishes, the observed evidence must be reconciled append-only.

Possible disposition includes:

```text
OPERATIONAL_PREFLIGHT_EVIDENCE=PASS
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE
OPERATIONAL_PREFLIGHT_EVIDENCE=FAIL
```

Only actual observed values may be promoted.

A PASS operational evidence record still does not automatically authorize A15, bind the live preexecution subject, execute the tournament, select a winner, or train.

## 15. Existing authority remains unchanged until exact selection

Until an exact post-canonical Founder token is supplied and captured:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_EVIDENCE_DECISION=ABSENT
OPERATIONAL_PREFLIGHT_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
```

Generic continuation language, `go ahead`, `all permissions`, ordinary project approval, or any earlier Founder token does not equal either exact decision token in this request.
