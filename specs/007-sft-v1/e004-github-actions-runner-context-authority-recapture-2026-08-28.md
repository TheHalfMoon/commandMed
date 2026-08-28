# E004 GitHub Actions Runner-Context Authority Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Predecessor exact-subject recapture:** `specs/007-sft-v1/e004-github-actions-location-neutral-authority-recapture-2026-08-28.md` / PR #95  
**Abandoned promotion:** PR #96 / CLOSED_UNMERGED  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority class:** successor exact-subject recapture after workflow-validation defect  
**Runtime/model authority expansion:** NONE  
**Live workflow on canonical main:** NO  
**Build execution occurred:** NO  
**Build pass:** NO  
**Current authorized spend:** USD 0

## 1. Why a successor capture is required

PR #95 canonically qualified location-neutral candidate bytes. PR #96 then attempted exact-byte promotion of that subject to:

```text
.github/workflows/e004-llama-quantize-build-evidence.yml
```

PR #96 was not merged. GitHub nevertheless created workflow run `33153171634` on exact promotion head `3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2` when the live-path file was pushed.

Exact provider evidence:

```text
RUN_ID=33153171634
RUN_HEAD_SHA=3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2
RUN_EVENT=push
RUN_STATUS=completed
RUN_CONCLUSION=failure
RUN_ATTEMPT=1
RUN_JOBS=0
PR96_MERGED=NO
```

This invalidates PR #96's earlier `WORKFLOW_RUN_EXECUTED=NO` claim. The provider created a run record, but no job was scheduled, no workflow step executed, no build occurred, and no build evidence was produced:

```text
WORKFLOW_RUN_RECORD_CREATED=YES
WORKFLOW_JOB_EXECUTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
```

No PR #96 provider record is treated as evidence of toolchain readiness, runtime qualification, model authority, benchmark authority, or spend.

## 2. Evidence-bound root cause

The PR #95 subject used `runner.temp` inside workflow-level `env`:

```yaml
env:
  SOURCE_DIR: ${{ runner.temp }}/e004-llama.cpp
  BUILD_DIR: ${{ runner.temp }}/e004-llama.cpp-build
  E004_HOME: ${{ runner.temp }}/e004-home
  SECURITY_EVIDENCE: ${{ runner.temp }}/e004-security-boundary.txt
```

GitHub Actions context-availability documentation permits only these contexts at workflow-level `env`:

```text
github
secrets
inputs
vars
```

The same documentation permits the `runner` context at `jobs.<job_id>.steps.env`.

Primary source:

```text
https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability
```

The zero-job failed push run is consistent with workflow validation failing before job scheduling. No more specific provider error string is fabricated because no job/log exists.

## 3. Corrected exact subject

The successor candidate remains non-live:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
PREDECESSOR_CANDIDATE_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
PREDECESSOR_CANDIDATE_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
NEW_CANDIDATE_GIT_BLOB_SHA1=c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7
NEW_CANDIDATE_SHA256=55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a
DIGEST_BINDING_EVIDENCE=LOCAL_BYTE_LEVEL_CROSSCHECK_MATCHED_GITHUB_GIT_BLOB
INDEPENDENT_DIGEST_RECOMPUTE=PENDING_EXACT_HEAD_REVIEW
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
```

The correction removes all `runner.temp` expressions from workflow-level `env` and binds the same derived paths only in step-level `env`, where GitHub permits `runner`.

Static workflow-level values remain:

```text
TOOL_REPOSITORY_URL
TOOL_COMMIT
TOOL_TREE
GIT_TERMINAL_PROMPT
GIT_CONFIG_NOSYSTEM
GIT_ASKPASS
SSH_ASKPASS
```

Runner-derived path values are step-scoped only:

```text
SOURCE_DIR
BUILD_DIR
E004_HOME
SECURITY_EVIDENCE
HOME
```

A local byte-level reconstruction produced Git blob SHA-1 `c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7`, matching GitHub exactly, and SHA-256 `55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a`. Fresh independent exact-head review must recompute and confirm the digest.

## 4. Pinned-source compile-command check

During PR #98 self-audit, a temporary candidate revision added `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` out of concern that required `compile_commands.json` evidence might otherwise be absent.

Exact review of the pinned source disproved that concern. At frozen llama.cpp commit:

```text
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
```

root `CMakeLists.txt` already contains:

```cmake
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
```

Therefore the temporary command-line override was redundant and was removed before qualification. The final candidate is again exactly Git blob `c5bc77cc...` / SHA-256 `55d28ec4...`.

```text
TEMPORARY_COMPILE_COMMAND_OVERRIDE_IN_FINAL_SUBJECT=NO
PINNED_SOURCE_ALREADY_EXPORTS_COMPILE_COMMANDS=YES
COMPILE_COMMAND_EVIDENCE_REQUIREMENT_CHANGED=NO
```

This preserves pinned-source truth rather than creating an unnecessary configuration delta.

## 5. Runtime/security invariants preserved

No runtime purpose, source identity, build target, security boundary, persistence policy, downstream authority, or spend changes:

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
TIMEOUT_MINUTES=30
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

The candidate retains:

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

Static pre-review checks against exact candidate bytes recorded:

```text
RUAMEL_YAML_SAFE_PARSE=PASS
TOP_LEVEL_ON_WORKFLOW_DISPATCH_PARSE=PASS
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
RUNNER_TEMP_REFERENCES_OUTSIDE_STEP_ENV=0
STEP_RUN_BLOCK_COUNT=4
BASH_N_STEP_1=PASS
BASH_N_STEP_2=PASS
BASH_N_STEP_3=PASS
BASH_N_STEP_4=PASS
BASH_N_INNER_NETWORK_ISOLATED_SCRIPT=PASS
```

These checks are not runtime PASS evidence and do not replace independent exact-head review.

## 6. Unexpected-run allowance disposition boundary

The observed PR #96 run was not the authorized future manual build-evidence run:

```text
EXPECTED_AUTHORIZED_TRIGGER=workflow_dispatch
OBSERVED_TRIGGER=push
OBSERVED_JOBS=0
OBSERVED_BUILD_EXECUTION=NO
```

Canonical predecessor authority states:

```text
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
```

and describes the executable allowance as the "at-most-one manual build-evidence run" after canonical promotion and pre-run verification. It separately classifies `AUTOMATIC_OR_UNEXPECTED_TRIGGER` as fail-closed.

This record does not self-approve the final disposition. Independent exact-head review must bind whether the zero-job non-manual validation run consumes the bounded manual allowance:

```text
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
UNEXPECTED_ZERO_JOB_RUN_OBSERVED=YES
UNEXPECTED_ZERO_JOB_RUN_ID=33153171634
AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION=NEEDS_EXACT_REVIEW
FUTURE_MANUAL_DISPATCH_EXERCISABLE=NO
```

## 7. Successor promotion sequence

No live workflow may be created from these corrected bytes until this recapture becomes canonical after fresh exact-head review.

```text
THIS_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> THIS_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_GIT_BLOB_EQUALS_NEW_QUALIFIED_CANDIDATE_BLOB=YES
-> PROMOTED_WORKFLOW_SHA256_EQUALS_NEW_QUALIFIED_CANDIDATE_SHA256=YES
-> PROMOTION_PUSH_CREATES_UNEXPECTED_WORKFLOW_RUN=NO
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
-> ALL_PRE_RUN_CONDITIONS_STILL_PASS
-> AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION_IS_EXPLICIT
-> AT_MOST_ONE_AUTHORIZED_MANUAL_RUN_IF_STILL_AVAILABLE
```

Any further candidate-byte change requires another exact authority capture.

## 8. Current branch state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
SUCCESSOR_EXACT_AUTHORITY_RECAPTURE=PENDING_FINAL_EXACT_HEAD_REVIEW
NEW_CANDIDATE_GIT_BLOB_SHA1=c5bc77cce1cdf23cb4fe5c4adc4f12713072eca7
NEW_CANDIDATE_SHA256=55d28ec4e9c6319482bf0b3147797ace6b525c3cbd5e85f43f8741819cdb663a
INDEPENDENT_DIGEST_RECOMPUTE=PENDING_EXACT_HEAD_REVIEW
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

Raw GitHub Actions API must report zero workflow runs for the final exact PR head before merge.

## Exit evidence required

Fresh exact-head review must independently confirm:

```text
PR96_INCIDENT_EVIDENCE_BOUND=YES
ROOT_CAUSE_RUNNER_CONTEXT_AVAILABILITY_DEFECT_CONFIRMED=YES
WORKFLOW_LEVEL_RUNNER_CONTEXT_REFERENCES=0
ALL_RUNNER_CONTEXT_REFERENCES_ARE_IN_ALLOWED_STEP_SCOPE=YES
PINNED_SOURCE_COMPILE_COMMAND_SETTING_CONFIRMED=YES
TEMPORARY_REDUNDANT_COMPILE_OVERRIDE_ABSENT_FROM_FINAL_SUBJECT=YES
NEW_CANDIDATE_GIT_BLOB_MATCHES=YES
NEW_CANDIDATE_SHA256_RECOMPUTED_AND_BOUND=YES
FINAL_CANDIDATE_DELTA_IS_RUNNER_CONTEXT_SCOPE_ONLY=YES
PREDECESSOR_RUNTIME_SECURITY_LIMITS_UNCHANGED=YES
NO_LIVE_WORKFLOW_CREATED_BY_THIS_RECAPTURE=YES
NO_WORKFLOW_RUN_CREATED_BY_THIS_RECAPTURE=YES
UNEXPECTED_RUN_ALLOWANCE_DISPOSITION_IS_EXPLICIT=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.
