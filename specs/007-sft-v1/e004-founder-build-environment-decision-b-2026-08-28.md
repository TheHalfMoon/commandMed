# E004 Founder Build Environment Decision B — 2026-08-28

**Spec:** 007 SFT V1  
**Branch base:** `47a68359ff51e4438704147bddeade2900ed4adb`  
**Decision owner:** Founder  
**Decision class:** `BUILD_ENVIRONMENT_DECISION_B`  
**Decision state:** RECORDED_FOR_REVIEW  
**Authority effect:** AUTHORIZE EXACT GITHUB-HOSTED ENVIRONMENT CLASS AND EXACT AUTHORITY-CAPTURE PREPARATION ONLY  
**Workflow promotion authority:** NONE  
**Workflow execution authority:** NONE  
**Build execution authority:** NONE UNTIL EXACT SUBJECT AUTHORITY IS CAPTURED AND REVIEWED  
**Model conversion authority:** NONE  
**Model execution authority:** NONE  
**Benchmark execution authority:** NONE  
**Training authority:** NONE  
**Spend authority:** USD 0

## 1. Decision capture

The immediately preceding canonical decision surface and assistant presentation narrowed the recommended next class to:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
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

The Founder then responded directly:

```text
FOUNDER_RESPONSE=go ahead
```

This response immediately followed the presentation of the exact build-environment gate and the explicit recommendation of Decision B. Canonical repository precedent already records the same response form as a valid bounded Founder decision when it immediately follows an exact decision class, scope, purpose, and exclusions.

Therefore this record captures selection of `BUILD_ENVIRONMENT_DECISION_B` only for the bounded environment class above. It does not reuse any earlier generic continuation instruction and does not expand scope beyond the immediately preceding exact decision surface.

## 2. Exact environment class now selected

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=AUTHORIZED_GITHUB_ACTIONS_CLASS_ONLY
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
CURRENT_AUTHORIZED_SPEND_USD=0
```

The selected environment class permits preparation of one exact execution-authority record and one exact live-workflow promotion subject for review. Selection of the environment class alone does not authorize promotion or execution.

## 3. Canonical non-executable subject candidate

The already-reviewed canonical candidate prepared by PR #91 remains:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
CANDIDATE_SHA256=3731d1383e41c5a0cc3f1af1efaebe6bbe45b6fc610a0f529bc2053676206053
CANDIDATE_GIT_BLOB_SHA1=050b53d5ca03ed37d40cd20d5d76066852e92bd9
LIVE_WORKFLOW_CREATED=NO
LIVE_TRIGGER_CREATED=NO
```

This decision does not automatically promote that file. A fresh promoted subject must be created from canonical main only after exact authority capture binds its path, byte identity, trigger, run count, source identities, network boundary, credential boundary, retention policy, and failure disposition.

## 4. Exact source/build boundary preserved

```text
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
OUTPUT_AUTHORITY=BUILD_EVIDENCE_ONLY
```

No branch, tag, alternate commit, alternate tree, target, or converter is authorized by this decision.

## 5. Credential boundary

GitHub may create a job-scoped platform token for the future job. The selected environment class permits only the presence exception already defined by the canonical decision surface:

```text
PLATFORM_MAY_CREATE_JOB_SCOPED_GITHUB_TOKEN=YES
WORKFLOW_PERMISSIONS={}
GITHUB_TOKEN_ACCESS_BY_WORKFLOW_STEPS=PROHIBITED
GITHUB_TOKEN_USE_BY_WORKFLOW_STEPS=PROHIBITED
OTHER_SECRET_ACCESS=PROHIBITED
TOKEN_PRESENCE_IS_EXPLICIT_EXCEPTION_TO_PRIOR_CREDENTIALS_NONE_EXPECTATION=YES
TOKEN_USE_AUTHORITY_CREATED=NO
```

No repository, organization, environment, package, cloud, SSH, PAT, model-provider, or other secret/credential access is authorized.

## 6. What this decision permits now

Repository-only preparation may now:

- create an exact authority-capture record bound to Decision B;
- bind the canonical candidate SHA-256 and Git blob identity;
- bind the intended live workflow path and prove no other workflow path is authorized;
- bind the exact runner class/label, trigger, timeout, maximum run count, and zero-spend condition;
- bind exact source repository/commit/tree and build target;
- bind the public-network source boundary and prohibit model/provider/credential endpoints;
- bind token-presence, token-access, token-use, secret, storage, cache, artifact, and retention policies;
- bind fail-closed conditions and evidence requirements;
- prepare the exact promoted workflow subject from canonical main after authority capture;
- obtain fresh exact-head review before any live workflow promotion or run.

## 7. What this decision does not permit

```text
WORKFLOW_PROMOTION_AUTHORITY=NONE
WORKFLOW_EXECUTION_AUTHORITY=NONE
BUILD_EXECUTION_AUTHORITY=NONE_UNTIL_EXACT_SUBJECT_AUTHORITY_CAPTURE_AND_REVIEW
ARBITRARY_GITHUB_ACTIONS_USE=NONE
AUTOMATIC_TRIGGER_AUTHORITY=NONE
MULTI_RUN_AUTHORITY=NONE
PAID_OR_LARGER_RUNNER_AUTHORITY=NONE
ACTIONS_CHECKOUT_AUTHORITY=NONE
THIRD_PARTY_ACTION_AUTHORITY=NONE
REUSABLE_WORKFLOW_AUTHORITY=NONE
CACHE_AUTHORITY=NONE
ARTIFACT_UPLOAD_AUTHORITY=NONE
RELEASE_OR_PACKAGE_PERSISTENCE_AUTHORITY=NONE
GITHUB_TOKEN_USE_AUTHORITY=NONE
OTHER_SECRET_OR_CREDENTIAL_AUTHORITY=NONE
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
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Mandatory next sequence

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION_B_CAPTURED_AND_REVIEWED
-> EXACT_AUTHORITY_CAPTURE
-> FRESH_PROMOTION_SUBJECT_CREATED_FROM_CANONICAL_MAIN
-> VERIFY_PROMOTED_YAML_BYTE_IDENTITY_AND_SCOPE
-> FRESH_EXACT_HEAD_REVIEW
-> LIVE_WORKFLOW_PROMOTION_ONLY_IF_EXACT_AUTHORITY_RECORD_PERMITS
-> AT_MOST_ONE_MANUAL_RUN_ONLY_IF_EXACT_AUTHORITY_RECORD_PERMITS
-> CAPTURE_REAL_BUILD_EVIDENCE_OR_FAIL_CLOSED
```

No arrow may be skipped. No repository merge automatically satisfies the next arrow.

## 9. Current lifecycle effect

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
EXTERNAL_BUILD_ENVIRONMENT_AUTHORITY=AUTHORIZED_GITHUB_ACTIONS_CLASS_ONLY
EXACT_AUTHORITY_CAPTURE=NOT_YET_CANONICAL
WORKFLOW_PROMOTION_AUTHORITY=NONE
WORKFLOW_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This record performs no GitHub Actions workflow promotion or run, source download, package installation, build, model/source-weight acquisition, conversion, quantization, model loading, inference, benchmark access/execution, device qualification, contamination assessment, selection-suite construction, Private Gold/PHI/gated access, credential or secret access, provider generation, training, procurement, personnel engagement, payment, or spend.

## Exit Evidence

Repository-level completion of this decision record requires fresh exact-head review confirming:

```text
FOUNDER_RESPONSE_BOUND_TO_IMMEDIATELY_PRECEDING_EXACT_DECISION_SURFACE=YES
DECISION_CLASS=BUILD_ENVIRONMENT_DECISION_B
PROVIDER_AND_RUNNER_SCOPE_EXACT=YES
ONE_RUN_CLASS_ONLY=YES
PREPARATION_AND_ENVIRONMENT_CLASS_AUTHORITY_ONLY=YES
WORKFLOW_PROMOTION_AUTHORITY=NONE
WORKFLOW_EXECUTION_AUTHORITY=NONE
NO_MODEL_OR_DOWNSTREAM_AUTHORITY_EXPANSION=YES
CURRENT_AUTHORIZED_SPEND_USD=0
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Canonical merge of this record captures only the bounded Founder environment decision and authorizes the next exact authority-capture preparation step. It does not itself authorize a live workflow or build execution.