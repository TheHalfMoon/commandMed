# E004 Build Environment Authority Decision Request — 2026-08-28

**Spec:** 007 SFT V1  
**Parent build authority:** `e004-conversion-toolchain-build-authority-2026-08-28.md`  
**Failed-preflight subject:** PR #88 / exact head `36941015659adb58051bf5258e7244f2fd119632`  
**Artifact class:** non-authorizing Founder decision request  
**Authority effect:** NONE  
**External execution authorized by this record:** NO  
**Credential access authorized by this record:** NO  
**Spend authorized by this record:** USD 0  
**Model conversion authority:** NONE  
**Training authority:** NONE

This request narrows the next build-evidence environment decision after the currently available isolated execution environment failed closed before exact `llama.cpp` source materialization. It does not reinterpret the general instruction to continue repository work as authority for a materially different external execution/provider boundary.

The current build authority remains bounded to:

```text
TOOL_SOURCE=ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264
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

## 1. Why a separate environment decision is required

The current local preflight establishes, subject to exact-head independent review and canonical merge of PR #88:

```text
EXACT_SOURCE_BYTES_MATERIALIZED=NO
BUILD_CONFIGURATION_EXECUTED=NO
LLAMA_QUANTIZE_BUILD_EXECUTED=NO
LLAMA_QUANTIZE_EXECUTABLE_PRODUCED=NO
BUILD_PASS=NO
```

A materially different hosted execution environment is not automatically covered merely because the technical build purpose is already authorized.

Canonical A14 intake explicitly preserves:

```text
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
ZERO_DOLLAR_EXTERNAL_SERVICE_IMPLIES_AUTHORITY=NO
UNPAID_EXTERNAL_WORK_IMPLIES_AUTHORITY=NO
```

The current build authority also requires:

```text
CREDENTIALS=NONE
SPEND_USD=0
```

Therefore any hosted provider path must separately resolve both the external-service boundary and any platform credential/token semantics before execution.

## 2. Public platform facts relevant to one candidate path

Current GitHub documentation states that standard GitHub-hosted runners are free for public repositories. It also states that each GitHub-hosted job receives a fresh runner instance for standard VM-backed labels and that GitHub automatically creates a job-scoped `GITHUB_TOKEN` when a workflow job starts.

These public platform facts are decision inputs only. They do not satisfy commandMed governance by themselves.

Reference sources:

- GitHub Actions billing and usage documentation: standard GitHub-hosted runners are free for public repositories.
- GitHub workflow syntax / hosted-runner documentation: standard public-repository runner labels include fixed labels such as `ubuntu-24.04`.
- GitHub `GITHUB_TOKEN` documentation: GitHub automatically creates a job-scoped token for workflow jobs.
- GitHub workflow-permission documentation: workflow YAML may reduce token permissions, including making unspecified permissions `none`.

```text
PUBLIC_REPOSITORY_STANDARD_RUNNER_MONETARY_USAGE_EXPECTED_USD=0
ZERO_MONETARY_USAGE_EQUALS_A14_AUTHORITY=NO
GITHUB_TOKEN_PLATFORM_CREATION_EXPECTED=YES
TOKEN_NOT_REFERENCED_EQUALS_TOKEN_NOT_CREATED=NO
TOKEN_PERMISSIONS_CAN_BE_RESTRICTED=YES
RESTRICTED_TOKEN_EQUALS_CREDENTIALS_NONE=NO
```

## 3. Decision classes

Exactly one future Founder decision may be bound. Until then:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=ABSENT
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=NONE
GITHUB_ACTIONS_BUILD_EXECUTION_AUTHORITY=NONE
SELF_HOSTED_BUILD_EXECUTION_AUTHORITY_EXPANSION=NONE
CREDENTIAL_BOUNDARY_EXPANSION=NONE
```

### `BUILD_ENVIRONMENT_DECISION_A` — preserve current environment only

```text
DECISION=BUILD_ENVIRONMENT_DECISION_A
EFFECT=NO_NEW_AUTHORITY
EXTERNAL_SERVICE_USE=NO
CREDENTIAL_BOUNDARY_CHANGE=NO
```

Meaning:

- keep the existing build-evidence authority unchanged;
- resume only if a user-controlled/currently-authorized environment can materialize the exact source and dependencies;
- do not use GitHub-hosted or other external runners;
- retain the failed-preflight evidence from PR #88 without promoting it to PASS.

### `BUILD_ENVIRONMENT_DECISION_B` — authorize one bounded GitHub-hosted build-evidence job

```text
DECISION=BUILD_ENVIRONMENT_DECISION_B
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
REPOSITORY_CHECKOUT_REQUIRED=NO
WORKFLOW_TOKEN_REFERENCE=PROHIBITED
WORKFLOW_PERMISSIONS=EMPTY_OR_EQUIVALENT_FAIL_CLOSED_MINIMUM
USER_OR_ORG_SECRETS=PROHIBITED
MODEL_SOURCE_WEIGHTS=PROHIBITED
MODEL_TRANSFORMATION=PROHIBITED
MODEL_LOADING=PROHIBITED
INFERENCE=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
TRAINING=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

This class would authorize only one build-evidence job after a separately reviewable, non-auto-triggering workflow subject is frozen.

The workflow subject would be required to:

1. use only `workflow_dispatch`;
2. use `ubuntu-24.04`, not a mutable `ubuntu-latest` alias;
3. set workflow/job permissions to the minimum fail-closed setting and never reference `github.token`, `secrets.GITHUB_TOKEN`, repository secrets, organization secrets, environment secrets, PATs, SSH keys, cloud credentials, or model-provider credentials;
4. avoid `actions/checkout` because commandMed source is not required for this tool build;
5. acquire only `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264` from public GitHub source endpoints;
6. verify the exact upstream commit/tree/archive identity before configure/build;
7. build only `llama-quantize`;
8. install no model/runtime dependencies beyond what is required for the authorized tool build evidence;
9. perform no model/source-weight acquisition, conversion, inference, benchmark/device, contamination, or training work;
10. print/hash the complete build-evidence manifest and executable identity to the workflow log;
11. upload no executable, source archive, cache, or workflow artifact unless separately authorized;
12. use no paid/larger/GPU runner and create no billable storage artifact;
13. fail closed if the exact source revision, runner identity, network boundary, or zero-spend conditions cannot be established.

Important credential boundary:

```text
GITHUB_JOB_MAY_HAVE_PLATFORM_CREATED_GITHUB_TOKEN=YES
AUTHORIZED_TO_REFERENCE_OR_USE_GITHUB_TOKEN=NO
AUTHORIZED_TO_REFERENCE_OR_USE_OTHER_SECRET=NO
TOKEN_PRESENCE_IS_EXPLICITLY_NOT_CREDENTIALS_NONE=YES
```

Therefore selecting Decision B would be an explicit, narrow exception to the prior `CREDENTIALS=NONE` environment expectation only for unavoidable platform creation/presence of the job token. It would **not** authorize token access or use by the workflow steps.

Decision B would still not authorize creating or executing the workflow until the exact workflow YAML is separately prepared and exact-head reviewed against this scope.

### `BUILD_ENVIRONMENT_DECISION_C` — authorize a user-controlled/self-hosted environment

```text
DECISION=BUILD_ENVIRONMENT_DECISION_C
PROVIDER=USER_CONTROLLED_OR_SELF_HOSTED
EXACT_MACHINE_OR_RUNNER_IDENTITY=REQUIRED_BEFORE_EXECUTION
NETWORK_BOUNDARY=REQUIRED_BEFORE_EXECUTION
CREDENTIAL_STATE=REQUIRED_BEFORE_EXECUTION_EXPECTED_NONE
SPEND_USD=0_REQUIRED
```

Meaning:

- permit the existing build-evidence lane on a separately bound user-controlled/self-hosted environment that can materialize the exact source;
- require exact machine/OS/toolchain/network identity before use;
- require no credentials and no new paid/unpaid external engagement;
- require a separately reviewed execution subject before build.

This class is not satisfied merely by naming an owned laptop, VM, or self-hosted runner. The exact resource must be bound before execution.

### `BUILD_ENVIRONMENT_DECISION_D` — another environment/provider

```text
DECISION=BUILD_ENVIRONMENT_DECISION_D
EFFECT=NEW_EXACT_DECISION_SURFACE_REQUIRED
EXECUTION_AUTHORITY_CREATED_BY_THIS_CLASS=NO
```

Any other cloud, CI, hosted, remote, or delegated environment must be proposed separately with exact provider, resource, credential, network, storage, retention, spend, and execution boundaries.

## 4. ChatGPT recommendation

```text
CHATGPT_BUILD_ENVIRONMENT_POSITION=RECOMMEND_BUILD_ENVIRONMENT_DECISION_B
RECOMMENDED_SCOPE=ONE_STANDARD_UBUNTU_24_04_PUBLIC_REPOSITORY_JOB_BUILD_EVIDENCE_ONLY
RECOMMENDED_RUN_COUNT=1
RECOMMENDED_TOKEN_USAGE=PROHIBITED
RECOMMENDED_ARTIFACT_UPLOAD=PROHIBITED
RECOMMENDED_SPEND_USD=0
```

Rationale:

- the current local environment has repeatedly failed before source bytes can be materialized;
- the exact source is public and ungated;
- a standard public-repository GitHub-hosted runner has a documented zero-monetary-usage path;
- one fresh, bounded runner can produce independent source/build/toolchain identities without touching model bytes;
- a fixed `ubuntu-24.04` label is less ambiguous than `ubuntu-latest`;
- avoiding checkout, token references, secrets, caches, and artifact uploads minimizes credential/storage expansion;
- the single-run cap prevents an open-ended external execution lane.

This is a recommendation only until the Founder explicitly selects the class.

## 5. Authority that would remain prohibited under every class

No environment decision in this request may itself authorize:

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

## 6. Required capture after a Founder decision

A later canonical authority record must bind at minimum:

```text
founder_decision_class
founder_decision_source_reference
provider_or_environment_identity
runner_or_machine_identity_binding_policy
maximum_execution_count
allowed_trigger
network_source_allowlist_or_exact_public_source_boundary
credential_presence_policy
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

## 7. Current state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=ABSENT
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=NONE
GITHUB_ACTIONS_BUILD_EXECUTION_AUTHORITY=NONE
CREDENTIAL_BOUNDARY_EXPANSION=NONE
BUILD_EVIDENCE_LANE=AUTHORIZED_BUT_CURRENT_ENVIRONMENT_BLOCKED
PR88_CANONICAL_MERGE=NOT_YET_PROVEN
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

This request performs no hosted workflow execution, self-hosted execution, source/model download, build, model conversion, quantization, model loading, inference, benchmark access/execution, device qualification, contamination assessment, selection-suite construction, Private Gold/PHI/gated access, secret/credential access, training, procurement, personnel engagement, payment, or spend.

## Exit Evidence

Repository-level completion of this decision-request artifact requires:

```text
PR88_FAILED_PREFLIGHT_CANONICAL_OR_EXPLICITLY_SUPERSEDED=YES
DECISION_CLASSES_REVIEWED_WITHOUT_MATERIAL_BOUNDARY_DEFECT=YES
EXTERNAL_SERVICE_ZERO_COST_NOT_MISTAKEN_FOR_AUTHORITY=YES
PLATFORM_TOKEN_PRESENCE_NOT_MISTAKEN_FOR_CREDENTIALS_NONE=YES
NO_EXECUTION_AUTHORITY_CREATED_BY_REQUEST=YES
NO_DOWNSTREAM_AUTHORITY_CREATED=YES
```

Canonical merge of this request would only create a decision surface. It would not grant any decision class or execute any build.