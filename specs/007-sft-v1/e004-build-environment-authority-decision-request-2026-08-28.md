# E004 Build Environment Authority Decision Request — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `5da5949ee9c3cc08f94d2f3f0993097cc30c060d`  
**Canonical failed-preflight record:** PR #88 / merge `5da5949ee9c3cc08f94d2f3f0993097cc30c060d`  
**Parent build authority:** `e004-conversion-toolchain-build-authority-2026-08-28.md`  
**Artifact class:** non-authorizing Founder decision request  
**Authority effect:** NONE  
**External execution authorized by this record:** NO  
**Credential access authorized by this record:** NO  
**Spend authorized by this record:** USD 0  
**Model conversion authority:** NONE  
**Training authority:** NONE

This request narrows the next build-evidence environment decision after the canonical failed execution preflight proved that the currently available isolated environment cannot materialize the exact authorized `llama.cpp` source bytes. It prepares decision classes only. It does not turn a generic continuation instruction into a new external-service, credential, or execution authority.

## 1. Current canonical build boundary

The existing Founder-authorized build-evidence lane remains:

```text
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
OUTPUT_AUTHORITY=BUILD_EVIDENCE_ONLY
MODEL_CONVERSION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_QUALIFICATION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The exact upstream commit is publicly verifiable and signed; the Git tree identity above is the exact tree referenced by that commit.

Canonical PR #88 records:

```text
BUILD_PREFLIGHT_EXECUTED=YES
EXACT_SOURCE_BYTES_MATERIALIZED=NO
BUILD_CONFIGURATION_EXECUTED=NO
LLAMA_QUANTIZE_BUILD_EXECUTED=NO
LLAMA_QUANTIZE_EXECUTABLE_PRODUCED=NO
BUILD_PASS=NO
```

No later step in this request may reinterpret that failed preflight as build evidence PASS.

## 2. Why another environment requires a separate decision

Canonical A14 intake preserves:

```text
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
ZERO_DOLLAR_EXTERNAL_SERVICE_IMPLIES_AUTHORITY=NO
UNPAID_EXTERNAL_WORK_IMPLIES_AUTHORITY=NO
```

The current build authority also preserves:

```text
CREDENTIALS=NONE
SPEND_USD=0
```

A hosted runner is therefore not automatically interchangeable with the failed local execution environment. A different external provider boundary and any platform-created credential/token must be explicitly resolved before execution.

## 3. Public GitHub Actions facts used only as decision inputs

Current GitHub documentation states that:

- standard GitHub-hosted runners are free for public repositories;
- fixed public-repository labels include `ubuntu-24.04`;
- a GitHub-hosted job receives a platform-created job-scoped `GITHUB_TOKEN`;
- `permissions: {}` disables all available permissions for that token.

These facts do not themselves grant commandMed authority.

```text
PUBLIC_REPOSITORY_STANDARD_RUNNER_MONETARY_USAGE_EXPECTED_USD=0
ZERO_MONETARY_USAGE_EQUALS_A14_AUTHORITY=NO
GITHUB_TOKEN_PLATFORM_CREATION_EXPECTED=YES
WORKFLOW_PERMISSIONS_EMPTY_MAP_SUPPORTED=YES
WORKFLOW_PERMISSIONS_EMPTY_MAP_EFFECT=ALL_AVAILABLE_GITHUB_TOKEN_PERMISSIONS_NONE
TOKEN_WITH_ALL_PERMISSIONS_NONE_EQUALS_TOKEN_NOT_CREATED=NO
TOKEN_PRESENCE_EQUALS_CREDENTIALS_NONE=NO
```

## 4. Current decision state

Until one exact class is separately selected by the Founder:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=ABSENT
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=NONE
GITHUB_ACTIONS_BUILD_EXECUTION_AUTHORITY=NONE
SELF_HOSTED_BUILD_EXECUTION_AUTHORITY_EXPANSION=NONE
CREDENTIAL_BOUNDARY_EXPANSION=NONE
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 5. Decision classes

### `BUILD_ENVIRONMENT_DECISION_A` — preserve current/user-controlled environment only

```text
DECISION=BUILD_ENVIRONMENT_DECISION_A
EFFECT=NO_NEW_AUTHORITY
EXTERNAL_SERVICE_USE=NO
CREDENTIAL_BOUNDARY_CHANGE=NO
```

This keeps the current build authority unchanged. The build lane may resume only in an already-authorized/user-controlled environment that can materialize the exact source and dependencies without introducing a new external-service or credential boundary.

### `BUILD_ENVIRONMENT_DECISION_B` — one bounded GitHub-hosted build-evidence job

```text
DECISION=BUILD_ENVIRONMENT_DECISION_B
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
REPOSITORY_CHECKOUT=PROHIBITED_NOT_REQUIRED
GITHUB_TOKEN_REFERENCE_OR_USE=PROHIBITED
OTHER_SECRET_OR_CREDENTIAL_REFERENCE_OR_USE=PROHIBITED
CACHE_USE=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_TRANSFORMATION=PROHIBITED
MODEL_LOADING=PROHIBITED
INFERENCE=PROHIBITED
BENCHMARK_ACCESS_OR_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
TRAINING=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

Selecting Decision B would authorize only the external environment class above. It would not by itself authorize an arbitrary workflow or a build run.

Before any run, a separately reviewable workflow subject must be frozen. It must satisfy all of the following:

1. `on: workflow_dispatch` only; no `push`, `pull_request`, schedule, repository-dispatch, workflow-run, or other automatic trigger.
2. `runs-on: ubuntu-24.04`; mutable `ubuntu-latest` is prohibited.
3. top-level `permissions: {}`.
4. no `actions/checkout`, no third-party action, no reusable workflow, and no step that references `github.token`, `secrets.GITHUB_TOKEN`, any repository/organization/environment secret, PAT, SSH key, cloud credential, package credential, or model-provider credential.
5. materialize the source through unauthenticated public Git transport only.
6. fetch exactly commit `c1d0e7a004015f23bc0233470b747b596f29b264` and fail closed unless both:

```text
git rev-parse HEAD == c1d0e7a004015f23bc0233470b747b596f29b264
git rev-parse HEAD^{tree} == 2255f4747492109298a5c997f374d49c2af3113d
```

7. no mutable branch/tag may substitute for those identities.
8. configure/build only the already-authorized `llama-quantize` target.
9. perform no model/source-weight download, conversion, quantization of model weights, loading, inference, benchmark/device execution, contamination assessment, or training.
10. capture runner-image, kernel, libc, Python, CMake, compiler, build-system, source, configure argv, build argv, output-path, executable SHA-256, build-log, network-boundary, and zero-spend evidence.
11. emit evidence to the job log only; no Actions artifact, cache, release asset, package, or other persisted build output is authorized.
12. fail closed on source-identity mismatch, unexpected credential requirement, paid-runner selection, missing zero-spend condition, unexpected network dependency, or any prohibited operation.

Credential exception boundary for Decision B:

```text
PLATFORM_MAY_CREATE_JOB_SCOPED_GITHUB_TOKEN=YES
WORKFLOW_PERMISSIONS={}
GITHUB_TOKEN_ACCESS_BY_WORKFLOW_STEPS=PROHIBITED
GITHUB_TOKEN_USE_BY_WORKFLOW_STEPS=PROHIBITED
OTHER_SECRET_ACCESS=PROHIBITED
TOKEN_PRESENCE_IS_EXPLICIT_EXCEPTION_TO_PRIOR_CREDENTIALS_NONE_EXPECTATION=YES
TOKEN_USE_AUTHORITY_CREATED=NO
```

The exception is presence-only: it acknowledges unavoidable platform token creation while forbidding workflow access/use and setting all available token permissions to `none`.

### `BUILD_ENVIRONMENT_DECISION_C` — exact user-controlled/self-hosted environment

```text
DECISION=BUILD_ENVIRONMENT_DECISION_C
PROVIDER=USER_CONTROLLED_OR_SELF_HOSTED
EXACT_MACHINE_OR_RUNNER_IDENTITY=REQUIRED_BEFORE_EXECUTION
NETWORK_BOUNDARY=REQUIRED_BEFORE_EXECUTION
CREDENTIAL_STATE=REQUIRED_BEFORE_EXECUTION_EXPECTED_NONE
NEW_EXTERNAL_ENGAGEMENT=PROHIBITED
SPEND_USD=0_REQUIRED
```

This permits preparation of a separate exact execution subject for a user-controlled resource only after its exact machine/OS/toolchain/network/credential/resource identities are bound. An owned laptop, VM, or self-hosted runner name alone is not sufficient evidence.

### `BUILD_ENVIRONMENT_DECISION_D` — any other environment/provider

```text
DECISION=BUILD_ENVIRONMENT_DECISION_D
EFFECT=NEW_EXACT_DECISION_SURFACE_REQUIRED
EXECUTION_AUTHORITY_CREATED_BY_THIS_CLASS=NO
```

Any other cloud, CI, remote, delegated, paid, or unpaid service must receive its own exact provider/resource/network/credential/storage/retention/spend boundary before a future authority decision.

## 6. ChatGPT recommendation

```text
CHATGPT_BUILD_ENVIRONMENT_POSITION=RECOMMEND_BUILD_ENVIRONMENT_DECISION_B
RECOMMENDED_SCOPE=ONE_STANDARD_UBUNTU_24_04_PUBLIC_REPOSITORY_JOB_BUILD_EVIDENCE_ONLY
RECOMMENDED_RUN_COUNT=1
RECOMMENDED_WORKFLOW_PERMISSIONS={}
RECOMMENDED_TOKEN_USE=PROHIBITED
RECOMMENDED_ARTIFACT_UPLOAD=PROHIBITED
RECOMMENDED_CACHE_USE=PROHIBITED
RECOMMENDED_SPEND_USD=0
```

Rationale:

- the canonical local preflight is blocked before source bytes;
- the exact build source is public and ungated;
- standard public-repository GitHub-hosted runners have a documented zero-monetary-usage path;
- `ubuntu-24.04` avoids a mutable runner label;
- `permissions: {}` plus no actions/checkout/secret/token references materially narrows the credential surface;
- exact commit **and tree** verification protects source identity;
- one-run authorization prevents an open-ended external execution lane;
- no artifact/cache persistence avoids silently creating a storage/retention lane.

This recommendation is not authority.

## 7. Authority that remains prohibited under every decision class

No class in this request grants:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_EXPANSION=NONE
MODEL_WEIGHT_LOADING=NONE
MODEL_CONVERSION=NONE
MODEL_WEIGHT_QUANTIZATION=NONE
MODEL_INFERENCE=NONE
BENCHMARK_PAYLOAD_ACCESS=NONE
BENCHMARK_EXECUTION=NONE
DEVICE_QUALIFICATION_EXPANSION=NONE
CONTAMINATION_ASSESSMENT=NONE
SELECTION_SUITE_CONSTRUCTION=NONE
PRIVATE_GOLD=NONE
PHI=NONE
GATED_ASSETS=NONE
PROVIDER_GENERATION=NONE
TRAINING=NONE
PROCUREMENT=NONE
BACKBONE_WINNER_SELECTION=NONE
```

## 8. Required authority capture after a Founder decision

A later authority record must bind at minimum:

```text
founder_decision_class
founder_decision_source_reference
provider_or_environment_identity
runner_or_machine_identity_binding_policy
maximum_execution_count
allowed_trigger
exact_source_commit
exact_source_tree
network_source_boundary
credential_presence_policy
credential_access_policy
credential_use_policy
secret_policy
storage_and_retention_policy
artifact_upload_policy
cache_policy
workflow_or_execution_subject_identity
zero_spend_evidence_policy
failure_disposition
all_explicit_prohibitions
```

A generic continuation instruction must not be reused as this decision unless it is given directly against a presented exact decision class with unambiguous scope.

## 9. Current lifecycle state

```text
PR88_FAILED_PREFLIGHT=CANONICAL
BUILD_EVIDENCE_LANE=AUTHORIZED_BUT_CURRENT_ENVIRONMENT_BLOCKED
FOUNDER_BUILD_ENVIRONMENT_DECISION=ABSENT
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=NONE
GITHUB_ACTIONS_BUILD_EXECUTION_AUTHORITY=NONE
CREDENTIAL_BOUNDARY_EXPANSION=NONE
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This request performs no hosted/self-hosted execution, source/model download, build, conversion, quantization, model loading, inference, benchmark access/execution, device qualification, contamination assessment, selection-suite construction, Private Gold/PHI/gated access, credential/secret access, provider generation, training, procurement, personnel engagement, payment, or spend.

## Exit Evidence

Repository-level completion of this decision request requires:

```text
CANONICAL_BASE_IS_POST_PR88_MAIN=YES
EXACT_UPSTREAM_COMMIT_AND_TREE_BOUND=YES
DECISION_CLASSES_REVIEWED_WITHOUT_MATERIAL_BOUNDARY_DEFECT=YES
EXTERNAL_SERVICE_ZERO_COST_NOT_MISTAKEN_FOR_AUTHORITY=YES
PLATFORM_TOKEN_PRESENCE_NOT_MISTAKEN_FOR_CREDENTIALS_NONE=YES
NO_EXECUTION_AUTHORITY_CREATED_BY_REQUEST=YES
NO_DOWNSTREAM_AUTHORITY_CREATED=YES
```

Canonical merge of this request would create only the reviewed decision surface. It would not select a decision class, authorize a hosted/self-hosted execution subject, or execute a build.