# E004 GitHub Actions Authority-Safe Successor Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Predecessor recapture:** PR #95  
**Abandoned promotion:** PR #96 / CLOSED_UNMERGED  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority class:** successor exact-subject recapture after workflow-validation and root-purpose defects  
**Runtime/model authority expansion:** NONE  
**Live workflow on canonical main:** NO  
**Build execution occurred:** NO  
**Build pass:** NO  
**Current authorized spend:** USD 0

## 1. Incident that invalidated PR #96

PR #96 promoted the then-qualified non-live subject to:

```text
.github/workflows/e004-llama-quantize-build-evidence.yml
```

It was never merged. GitHub nevertheless created provider run `33153171634` on exact PR #96 head `3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2`.

```text
RUN_ID=33153171634
RUN_EVENT=push
RUN_STATUS=completed
RUN_CONCLUSION=failure
RUN_ATTEMPT=1
RUN_JOBS=0
PR96_MERGED=NO
WORKFLOW_JOB_EXECUTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
```

The earlier PR #96 claim that no workflow run existed is therefore false and is superseded by this record. The zero-job provider record is not build evidence and does not create runtime, model, benchmark, training, procurement, or spend authority.

## 2. Defect A — invalid workflow-level `runner` context

The PR #95 subject referenced `${{ runner.temp }}` in workflow-level `env`. GitHub Actions context-availability rules do not permit the `runner` context there; they do permit it at `jobs.<job_id>.steps.env`.

Primary source:

```text
https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability
```

The successor subject removes all workflow-level `runner` references and binds the same runner-derived paths only in step-level `env`.

```text
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
RUNNER_TEMP_REFERENCES_OUTSIDE_STEP_ENV=0
```

The PR #96 zero-job failed `push` run is consistent with pre-job workflow validation failure. No more specific provider error is fabricated because no job or job log exists.

## 3. Defect B — unauthorized root preflight

The predecessor candidate also contained:

```text
sudo -n true
```

Canonical exact authority states:

```text
ROOT_PRIVILEGE_PURPOSE=NETWORK_NAMESPACE_CREATION_ONLY
```

and requires configure/build to be unprivileged after the namespace is created. Even though `sudo -n true` was only a passwordless-sudo probe, it still created root execution outside the sole permitted root purpose.

The successor subject therefore removes that probe. Passwordless sudo and namespace capability are tested only by the authorized operation itself:

```text
sudo -n unshare --net -- ...
```

If that operation is unavailable, the job fails closed before configure/build. No replacement privileged probe is added.

```text
SUDO_TRUE_PREFLIGHT_PRESENT=NO
ROOT_EXECUTION_OUTSIDE_NAMESPACE_CREATION=NO_BY_SUBJECT
ROOT_PRIVILEGE_PURPOSE=NETWORK_NAMESPACE_CREATION_ONLY
```

## 4. Final successor candidate identity

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
PREDECESSOR_PR95_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
PREDECESSOR_PR95_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
RUNNER_CONTEXT_ONLY_INTERMEDIATE_GIT_BLOB_SHA1=c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7
RUNNER_CONTEXT_ONLY_INTERMEDIATE_SHA256=55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a
FINAL_SUCCESSOR_GIT_BLOB_SHA1=e8f1a069f88037d2ba139c697bbdffaf6b43ef2a
FINAL_SUCCESSOR_SHA256=NEEDS_FRESH_INDEPENDENT_EXACT_HEAD_HASH
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
```

The final successor differs from the PR #95 subject only by:

1. moving runner-derived paths from invalid workflow-level `env` into allowed step-level `env`; and
2. deleting `sudo -n true` so root execution is limited to network namespace creation.

Any further candidate-byte change invalidates this recapture and requires another exact-subject review.

## 5. Pinned-source checks

Frozen llama.cpp identity remains:

```text
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
```

Exact source review confirms:

- root `CMakeLists.txt` already contains `set(CMAKE_EXPORT_COMPILE_COMMANDS ON)`;
- `tools/quantize/CMakeLists.txt` defines executable target `llama-quantize`.

A temporary PR #98 revision that added `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` was therefore redundant and is not part of the final subject.

```text
PINNED_SOURCE_ALREADY_EXPORTS_COMPILE_COMMANDS=YES
LLAMA_QUANTIZE_TARGET_PRESENT_AT_PINNED_COMMIT=YES
TEMPORARY_COMPILE_COMMAND_OVERRIDE_IN_FINAL_SUBJECT=NO
```

## 6. Runtime and security invariants preserved

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
BUILD_TARGET=llama-quantize
TIMEOUT_MINUTES=30
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The successor retains all predecessor prohibitions and fail-closed controls:

```text
PUBLIC_SOURCE_FETCH_ONLY
NO_PACKAGE_INSTALLATION
CONFIGURE_BUILD_NETWORK_NAMESPACE_ISOLATION
ROOT_PRIVILEGE_FOR_NAMESPACE_CREATION_ONLY
NONROOT_CONFIGURE_BUILD
SUPPLEMENTARY_GROUPS_CLEARED
LINUX_CAPABILITIES_DROPPED
NO_NEW_PRIVS_REQUIRED
INHERITED_ENVIRONMENT_RESET
SENSITIVE_PLATFORM_ENVIRONMENT_REJECTED
NO_ACTIONS_CACHE
NO_ARTIFACT_UPLOAD
NO_RELEASE_OR_PACKAGE_PUBLICATION
NO_MODEL_OPERATION
NO_BENCHMARK_OR_DEVICE_OPERATION
NO_CONTAMINATION_ASSESSMENT
NO_SELECTION_SUITE_CONSTRUCTION
NO_TRAINING
NO_PROCUREMENT
```

No candidate statement is treated as evidence that a hosted runner will actually satisfy the tool, sudo, namespace, compiler, or build requirements. Those remain runtime evidence requirements.

## 7. PR #96 run-allowance disposition

Canonical exact authority binds:

```text
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
```

It describes the executable allowance as an "at-most-one manual build-evidence run" that becomes exercisable only after canonical workflow promotion, post-merge byte verification, and all pre-run conditions remain satisfied. It separately lists `AUTOMATIC_OR_UNEXPECTED_TRIGGER` as fail-closed.

PR #96 run `33153171634` occurred:

- before any canonical workflow promotion;
- with event `push`, not `workflow_dispatch`;
- with zero jobs and no build execution.

Therefore the evidence-bound disposition is:

```text
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
UNEXPECTED_ZERO_JOB_RUN_OBSERVED=YES
AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION=DOES_NOT_CONSUM_AUTHORIZED_MANUAL_ALLOWANCE
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1_CONDITIONAL_NOT_YET_EXERCISABLE
FUTURE_MANUAL_DISPATCH_EXERCISABLE=NO
```

This is interpretation of already-canonical run semantics, not creation of a second run or new authority. Fresh independent exact-head review must verify this disposition before merge.

## 8. Promotion sequence after this recapture

```text
FINAL_SUCCESSOR_SHA256_INDEPENDENTLY_RECOMPUTED_AND_BOUND
-> THIS_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> THIS_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_BYTES_EQUAL_QUALIFIED_SUCCESSOR_BYTES=YES
-> PROMOTION_PUSH_CREATES_UNEXPECTED_WORKFLOW_RUN=NO
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
-> ALL_PRE_RUN_CONDITIONS_STILL_PASS
-> AT_MOST_ONE_AUTHORIZED_MANUAL_WORKFLOW_DISPATCH_RUN
```

The connected GitHub action surface still does not expose a `workflow_dispatch` initiation action. Tooling absence is not execution evidence and does not revoke the conditional authority.

## 9. Current branch state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
SUCCESSOR_EXACT_AUTHORITY_RECAPTURE=PENDING_FINAL_SHA256_AND_EXACT_HEAD_REVIEW
FINAL_SUCCESSOR_GIT_BLOB_SHA1=e8f1a069f88037d2ba139c697bbdffaf6b43ef2a
FINAL_SUCCESSOR_SHA256=NEEDS_FRESH_INDEPENDENT_EXACT_HEAD_HASH
LIVE_WORKFLOW_ON_CANONICAL_MAIN=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Raw GitHub Actions API must report zero runs for the final exact PR head before canonical merge.

## Exit evidence required

Fresh exact-head review must independently confirm:

```text
PR96_INCIDENT_EVIDENCE_BOUND=YES
RUNNER_CONTEXT_DEFECT_REPAIRED=YES
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
ALL_RUNNER_CONTEXT_REFERENCES_ARE_IN_ALLOWED_STEP_SCOPE=YES
UNAUTHORIZED_SUDO_TRUE_PREFLIGHT_REMOVED=YES
ROOT_PRIVILEGE_PURPOSE_MATCHES_CANONICAL_AUTHORITY=YES
FINAL_SUCCESSOR_GIT_BLOB_MATCHES=YES
FINAL_SUCCESSOR_SHA256_RECOMPUTED_AND_BOUND=YES
PINNED_SOURCE_COMPILE_COMMAND_SETTING_CONFIRMED=YES
LLAMA_QUANTIZE_TARGET_PRESENT_AT_PINNED_COMMIT=YES
NO_LIVE_WORKFLOW_CREATED_BY_THIS_RECAPTURE=YES
NO_WORKFLOW_RUN_CREATED_BY_THIS_RECAPTURE=YES
RUN_ALLOWANCE_DISPOSITION_VERIFIED=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.
