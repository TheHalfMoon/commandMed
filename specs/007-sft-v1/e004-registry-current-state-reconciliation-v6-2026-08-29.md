# E004 Registry Current-State Reconciliation V6 — 2026-08-29

**Spec:** 007 SFT V1  
**Artifact class:** append-only current-state reconciliation  
**Canonical base:** `6aa5e7a210452fd367e41343f08abee252ef7ad9`  
**Authority effect:** NONE  
**Runtime-evidence execution effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## Purpose

Record the exact live E004 frontier after canonical admission of the one-shot connected-executor dispatch bootstrap through PR #136 and the bootstrap's terminal failure before any target runtime-evidence `workflow_dispatch` was created.

This record supersedes only stale V5 interpretation that a fresh-dispatch remediation mechanism remained available. It preserves all historical E002/build evidence and every scientific, governance, conversion, contamination, A15, training, access, and spend boundary.

## Canonical bootstrap admission

PR #136 admitted exactly the reviewed transient bootstrap workflow and its bounded authority record from exact head:

```text
PR136_EXACT_HEAD=3e47d41c6d6cdc88375c1cbacbab9412d64061a0
PR136_MERGE=6aa5e7a210452fd367e41343f08abee252ef7ad9
PR136_BASE=f34c294458af877a89c832cfa08d9867b28aab25
PR136_CHANGED_FILES=2
BOOTSTRAP_PATH=.github/workflows/e004-runtime-evidence-dispatch-bootstrap.yml
BOOTSTRAP_AUTHORITY_RECORD=specs/007-sft-v1/e004-connected-executor-dispatch-bootstrap-authority-2026-08-29.md
TARGET_WORKFLOW_MODIFIED_BY_PR136=NO
```

The exact target workflow remained unchanged after merge:

```text
TARGET_WORKFLOW=.github/workflows/e004-conversion-runtime-evidence.yml
TARGET_WORKFLOW_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
TARGET_TRIGGER=workflow_dispatch_only
```

## One-shot bootstrap terminal result

The merge push created exactly one bootstrap workflow run:

```text
BOOTSTRAP_RUN_ID=33256775421
BOOTSTRAP_JOB_ID=99111782850
BOOTSTRAP_RUN_HEAD_SHA=6aa5e7a210452fd367e41343f08abee252ef7ad9
BOOTSTRAP_RUN_HEAD_BRANCH=main
BOOTSTRAP_RUN_EVENT=push
BOOTSTRAP_RUN_PATH=.github/workflows/e004-runtime-evidence-dispatch-bootstrap.yml
BOOTSTRAP_RUN_ATTEMPT=1
BOOTSTRAP_RUN_STATUS=completed
BOOTSTRAP_RUN_CONCLUSION=failure
BOOTSTRAP_JOB_NAME=dispatch
BOOTSTRAP_JOB_STATUS=completed
BOOTSTRAP_JOB_CONCLUSION=failure
BOOTSTRAP_REEXECUTION_AUTHORIZED=NO
```

The connected GitHub job-step read returned an empty step list. The decoded job-log read returned `BlobNotFound`, and the check run reports one annotation whose body is not exposed by the currently connected read surface. Therefore the exact platform-level failure reason is not inferred or fabricated:

```text
BOOTSTRAP_EXACT_FAILURE_REASON=NEEDS_EVIDENCE
BOOTSTRAP_JOB_STEPS_OBSERVED=0
BOOTSTRAP_JOB_LOG_BODY_AVAILABLE_TO_CONNECTED_EXECUTOR=NO
BOOTSTRAP_CHECK_ANNOTATION_COUNT=1
BOOTSTRAP_CHECK_ANNOTATION_BODY_AVAILABLE_TO_CONNECTED_EXECUTOR=NO
FAILURE_REASON_INFERRED_FROM_TIMING_OR_ABSENCE_OF_STEPS=NO
```

The bounded authority explicitly permits only one bootstrap run and states that after terminal failure no second bootstrap execution is authorized. This terminal result therefore consumes the bootstrap-remediation attempt regardless of the unresolved platform annotation text.

```text
MAX_AUTHORIZED_BOOTSTRAP_RUNS=1
AUTHORIZED_BOOTSTRAP_RUNS_EXECUTED=1
AUTHORIZED_BOOTSTRAP_RUNS_REMAINING=0
BOOTSTRAP_FAILURE_DISPOSITION=FAIL_CLOSED
BOOTSTRAP_RERUN_AUTHORIZED=NO
FAILED_JOB_RERUN_AUTHORIZED=NO
SECOND_BOOTSTRAP_WORKFLOW_AUTHORIZED=NO
ALTERNATE_TRIGGER_WORKAROUND_AUTHORIZED=NO
```

## Target runtime-evidence dispatch did not occur

Post-failure repository-wide `workflow_dispatch` history contains only historical build-evidence run `33187438094` for `.github/workflows/e004-llama-quantize-build-evidence.yml`. No `workflow_dispatch` exists for the E004 conversion-runtime target workflow.

No branch matching the authorized binding prefix exists after the failed bootstrap.

```text
HISTORICAL_BUILD_EVIDENCE_RUN=33187438094
HISTORICAL_BUILD_EVIDENCE_COUNTS_AS_RUNTIME_EVIDENCE_RUN=NO
TARGET_RUNTIME_EVIDENCE_WORKFLOW_DISPATCH_RUN_COUNT=0
TARGET_RUNTIME_EVIDENCE_EXECUTION_OCCURRED=NO
TARGET_RUNTIME_EVIDENCE_RESULT=NOT_STARTED
TARGET_SHA_NAMED_BINDING_REF_CREATED=NO_OBSERVED
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_EXECUTED=0
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_REMAINING=1
```

The remaining target-run allowance does not reopen the consumed bootstrap mechanism. A future target dispatch would require a separately valid connected execution path consistent with canonical authority; no rerun or alternate trigger may be substituted.

## Live repository visibility contradiction

Post-merge live repository metadata reports:

```text
LIVE_REPOSITORY_PRIVATE=true
LIVE_REPOSITORY_VISIBILITY=private
```

This contradicts the earlier current-state/runtime authority assumption that described a standard GitHub-hosted **public-repository** runner class. The contradiction does not prove that the bootstrap failure was caused by repository visibility or billing, and it does not prove that any incremental charge occurred. It does invalidate treating the public-repository runner/cost assumption as established evidence.

Current GitHub Actions billing documentation distinguishes these cases explicitly:

- standard GitHub-hosted runners are free for public repositories;
- private repositories consume plan-included GitHub Actions minutes and may incur billing after the included quota is exhausted;
- `ubuntu-24.04` is a standard GitHub-hosted private-repository runner label.

Authoritative references checked on 2026-08-29:

- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)

These product rules still do not reveal this repository owner's current included-minute balance, metered usage, payment state, or the exact reason run `33256775421` failed. Those are real account/runtime facts and remain unresolved.

```text
PREVIOUS_PUBLIC_REPOSITORY_RUNNER_ASSUMPTION=INVALIDATED_BY_LIVE_REPOSITORY_METADATA
PRIVATE_REPOSITORY_STANDARD_RUNNER_ZERO_INCREMENTAL_SPEND=NOT_PROVEN
PRIVATE_REPOSITORY_INCLUDED_MINUTES_AVAILABLE=NEEDS_EVIDENCE
PRIVATE_REPOSITORY_CURRENT_METERED_USAGE=NEEDS_EVIDENCE
ACTUAL_INCREMENTAL_SPEND_USD_FOR_BOOTSTRAP=NEEDS_EVIDENCE
CURRENT_AUTHORIZED_SPEND_USD=0
SPEND_AUTHORITY_EXPANDED=NO
FAILURE_CAUSE_ATTRIBUTED_TO_BILLING_WITHOUT_EVIDENCE=NO
```

No future GitHub-hosted execution may infer zero incremental spend from the superseded public-repository assumption. Real finance/runtime evidence remains required before relying on a private-repository hosted-runner execution under a USD 0 authorization boundary.

## Cleanup disposition

The transient bootstrap has served its sole authorized one-shot purpose and failed terminally without creating a target run or binding ref. Its authority record requires ordinary reviewed cleanup and prohibits another bootstrap execution.

The cleanup transition therefore removes only:

```text
.github/workflows/e004-runtime-evidence-dispatch-bootstrap.yml
```

No binding branch exists to delete. The target runtime-evidence workflow must remain byte-identical and `workflow_dispatch`-only. The historical authority record and this reconciliation remain canonical audit evidence.

```text
BOOTSTRAP_WORKFLOW_CLEANUP_REQUIRED=YES
TARGET_BINDING_BRANCH_CLEANUP_REQUIRED=NO_NOT_CREATED
TARGET_WORKFLOW_CLEANUP_OR_MUTATION_AUTHORIZED=NO
HISTORY_REWRITE_AUTHORIZED=NO
```

## Scientific and governance frontier

Nothing about PR #136, the failed bootstrap, or cleanup satisfies any scientific or downstream execution gate:

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

## Exact next state

After reviewed cleanup is canonical, the connected executor has no authorized bootstrap retry path. The runtime-evidence allowance remains unconsumed but is not executable through the exhausted remediation mechanism.

```text
E004_RUNTIME_EVIDENCE_TARGET_ALLOWANCE_REMAINS=1
E004_BOOTSTRAP_REMEDIATION_ALLOWANCE_REMAINS=0
CONNECTED_AUTHORIZED_FRESH_DISPATCH_PATH=ABSENT_AFTER_FAILED_ONE_SHOT
REQUIRED_BEFORE_ANY_FUTURE_TARGET_EXECUTION=SEPARATELY_VALID_EXECUTION_PATH_PLUS_REAL_RUNTIME_FINANCE_EVIDENCE
NO_RERUN_OR_TRIGGER_WORKAROUND=YES
```

This is a genuine external/runtime/finance execution blocker, not an E004 PASS or FAIL result and not authorization for E005 or later work.

## Exit evidence

This V6 reconciliation is repository-level complete only after exact-head review confirms:

```text
PR136_MERGED_FROM_EXPECTED_HEAD=YES
BOOTSTRAP_RUN_33256775421_TERMINAL_FAILURE=YES
BOOTSTRAP_RUN_ALLOWANCE_REMAINING=0
TARGET_RUNTIME_WORKFLOW_DISPATCH_COUNT=0
TARGET_RUNTIME_RUN_ALLOWANCE_REMAINING=1
BINDING_REF_CREATED=NO
EXACT_FAILURE_CAUSE_NOT_FABRICATED=YES
LIVE_REPOSITORY_VISIBILITY_PRIVATE_RECORDED=YES
PUBLIC_RUNNER_ASSUMPTION_NOT_REUSED=YES
ZERO_INCREMENTAL_SPEND_NOT_INFERRED=YES
TRANSIENT_BOOTSTRAP_REMOVED=YES
TARGET_WORKFLOW_UNCHANGED=YES
MODEL_CONVERSION_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
E004_REMAINS_BLOCKED_PREFLIGHT=YES
E005_REMAINS_NOT_REACHED=YES
```