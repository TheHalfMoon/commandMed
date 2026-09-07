# E004 Operational Preflight Evidence Run V1 Failure Reconciliation — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Authority:** `specs/007-sft-v1/e004-operational-preflight-evidence-founder-decision-2026-09-08.md`
**Implementation merge:** `758a2097e8446c4cf6eaf5abcfc1b0d3a24a3094`
**Evidence trigger commit:** `af6472d4df3218bdf3a39dbe24ea405178f3424a`
**Workflow run:** `34171361117`
**Evidence job:** `101892133669`
**Artifact class:** observed terminal failure reconciliation
**Authority effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Record the exact terminal outcome of the single operational-preflight evidence run authorized by Founder Decision B. The run failed closed in the first repository/authority guard step before credential/access checks, runtime provisioning, host/resource capture, network-isolated runtime validation, or any model-adjacent operation began.

This record does not reopen the exhausted one-run allowance and does not create retry, rerun, model, tournament, A15, training, credential, protected-data, paid-compute, procurement, payment, or spend authority.

## 2. Exact run identity

```text
WORKFLOW_NAME=E004 operational preflight evidence V1
WORKFLOW_RUN_ID=34171361117
EVENT=push
RUN_NUMBER=3
RUN_ATTEMPT=1
RUN_HEAD_BRANCH=evidence/e004-operational-preflight-run-v1
RUN_HEAD_SHA=af6472d4df3218bdf3a39dbe24ea405178f3424a
RUN_STATUS=completed
RUN_CONCLUSION=failure
EVIDENCE_JOB_ID=101892133669
EVIDENCE_JOB_CONCLUSION=failure
STATIC_QUALIFICATION_PUSH_JOB=skipped
WORKFLOW_ARTIFACT_COUNT=0
```

The trigger commit is a direct child of the exact implementation merge and changed only:

```text
.github/e004-operational-preflight-run-v1.txt
```

The marker binds:

```text
E004_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN=V1
IMPLEMENTATION_CANONICAL_MERGE=758a2097e8446c4cf6eaf5abcfc1b0d3a24a3094
FOUNDER_DECISION_TOKEN_SHA256=b085f4766959f011551cc29faf2dabfed5b89e40762918f6f15f16d9f4b71858
```

GitHub canonical commit metadata independently confirms that `758a2097...` is the marker's sole parent and that the marker commit contains only the three-line marker file.

## 3. Observed step sequence

The evidence job observed:

```text
RUNNER_IMAGE=ubuntu-24.04
RUNNER_IMAGE_VERSION=20260831.293.1
RUNNER_OS=Ubuntu_24.04.4_LTS
WORKFLOW_TOKEN_CONTENTS_PERMISSION=read
WORKFLOW_TOKEN_METADATA_PERMISSION=read
CHECKOUT_PERSIST_CREDENTIALS=false
CHECKOUT_FETCH_DEPTH=2

CHECKOUT_EXACT_EVIDENCE_HEAD=PASS
ONE_RUN_MARKER_AND_CANONICAL_AUTHORITY_GUARD=FAIL
CREDENTIAL_AND_PUBLIC_ACCESS_BOUNDARY_STEP=skipped
RUNNER_HOST_AND_RESOURCE_CAPTURE_STEP=skipped
LLAMA_RUNTIME_RECONSTRUCTION_STEP=skipped
TRANSFORMERS_TORCH_RUNTIME_RECONSTRUCTION_STEP=skipped
DEFAULT_DENY_NETWORK_VALIDATION_STEP=skipped
RETENTION_CLEANUP_STEP=PASS
SUCCESS_DISPOSITION_STEP=skipped
```

The cleanup step emitted:

```text
RETENTION_CLEANUP_STATE=PASS
RETENTION_SENTINEL_ABSENT_AFTER_CLEANUP=YES
RUNTIME_STAGING_ABSENT_AFTER_CLEANUP=YES
GITHUB_ACTIONS_CACHE_UPLOAD=NO
WORKFLOW_ARTIFACT_UPLOAD=NO
RELEASE_ASSET_UPLOAD=NO
PACKAGE_REGISTRY_UPLOAD=NO
```

No retained workflow artifact exists for the run.

## 4. Fail-closed evidence boundary

Because the first guard failed, no later operational-preflight field may be promoted to PASS from this run except the directly observed runner/check-out/cleanup facts above.

```text
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_PRE_PROVISIONING_GUARD
EXACT_PUBLIC_UNGATED_ACCESS_RUNTIME_CHECK=NOT_EXECUTED
EXACT_CREDENTIAL_BOUNDARY_RUNTIME_CHECK=NOT_EXECUTED
EXACT_HOST_RESOURCE_OBSERVATION=NOT_EXECUTED
EXACT_LLAMA_RUNTIME_RECONSTRUCTION=NOT_EXECUTED
EXACT_TRANSFORMERS_RUNTIME_RECONSTRUCTION=NOT_EXECUTED
EXACT_NETWORK_DISABLE_MECHANISM_RUNTIME_CHECK=NOT_EXECUTED
EXACT_ZERO_SPEND_RESOURCE_CLASS_RUNTIME_CHECK=NOT_EXECUTED
SUCCESSOR_PASS_PREFLIGHT=NO
```

## 5. Static guard diagnosis

The executed workflow checked out the evidence branch with `fetch-depth: 2`, then required the local checkout to prove that the marker parent was itself a merge commit by evaluating the parent's visible parent list.

Canonical GitHub history independently proves:

```text
MARKER_PARENT=758a2097e8446c4cf6eaf5abcfc1b0d3a24a3094
MARKER_PARENT_IS_MERGE_COMMIT=YES
MARKER_PARENT_PARENT_1=b9eb2c8b1b4bebfd4ddc63600d1cf07ba9a2bbea
MARKER_PARENT_PARENT_2=43b92c3b30478eb3563bb4c7201ea7dabed26d0c
MARKER_COMMIT_CHANGED_FILE_COUNT=1
MARKER_COMMIT_CHANGED_FILE=.github/e004-operational-preflight-run-v1.txt
```

The job log does not emit the value of each silent shell `test`, so this reconciliation does not fabricate an exact historical shell-failure line. However, a material static implementation defect is present: a depth-2 shallow checkout is not a sufficient evidence source for a guard that requires visibility of the marker parent's parents. The repository's comparable review-first workflows use full-history checkout when ancestry must be inspected.

```text
EXACT_FAILED_SHELL_TEST_RECOVERED_FROM_LOG=NO
STATIC_GUARD_IMPLEMENTATION_DEFECT=YES_INSUFFICIENT_HISTORY_FOR_REQUIRED_ANCESTRY_PROOF
MINIMUM_REPAIR_CLASS=FULL_HISTORY_CHECKOUT_FOR_ANCESTRY_GUARD
HISTORICAL_RUN_REINTERPRETED_AS_PASS=NO
```

## 6. One-run authority is consumed

Founder Decision B authorizes exactly one new post-merge run and explicitly grants no rerun or failed-run automatic retry authority.

```text
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS_EXECUTED=1
AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS_REMAINING=0
OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY_STATE=CONSUMED_EXACTLY_ONCE
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
OPERATIONAL_PREFLIGHT_EVIDENCE_RERUN_AUTHORIZED_NOW=NO
SECOND_MARKER_RUN_AUTHORITY=NONE
```

The failed run must not be rerun, replayed, retried, or replaced under the consumed Decision B allowance.

## 7. Explicit non-actions

```text
RUNTIME_DEPENDENCY_PROVISIONING_PERFORMED=NO
CANDIDATE_MODEL_WEIGHT_ACQUISITION_PERFORMED=NO
MODEL_OBJECT_INSTANTIATED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
EVALUATION_PAYLOAD_ACCESS_PERFORMED=NO
EVALUATION_PAYLOAD_EXECUTION_PERFORMED=NO
BENCHMARK_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
A15_ACTIVATION_PERFORMED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
GATED_ASSET_ACCESSED=NO
CUSTOM_STEP_CREDENTIAL_USE_PERFORMED=NO
PROCUREMENT_PERFORMED=NO
PAYMENT_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Dependency-safe next unit

The existing implementation-preparation authority may support a review-first static repair of the ancestry guard, but the consumed empirical run authority may not be reopened by implementation work.

The dependency-safe sequence is:

1. qualify and canonically merge a no-execution guard repair using full repository history for ancestry checks;
2. canonically bind the repaired workflow identity;
3. create a separate post-repair Founder decision surface for any new empirical operational-preflight attempt;
4. do not create a new evidence branch/marker/run unless that later decision becomes canonical;
5. if a later authorized run succeeds, reconcile only its directly observed evidence;
6. A1-A14 snapshot construction, A15, tournament execution, winner selection, and training remain downstream and separately gated.

```text
NEXT_E004_TRANSITION=REVIEW_FIRST_STATIC_GUARD_REPAIR
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```
