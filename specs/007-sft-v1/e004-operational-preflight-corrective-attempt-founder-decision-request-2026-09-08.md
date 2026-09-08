# E004 Operational Preflight Corrective Attempt Founder Decision Request — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Decision owner:** Founder
**Canonical prerequisite repair merge:** `264e1f4056d7fdf96696c5296edc9ab3f42df291`
**Failed V1 evidence run:** `34171361117`
**Failed V1 evidence job:** `101892133669`
**V1 failure reconciliation:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v1-failure-reconciliation-2026-09-08.md`
**Current-state overlay:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v50-2026-09-08.md`
**Artifact class:** Founder decision request only
**Authority effect before exact post-canonical selection:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Request a new, explicit Founder decision after the single V1 operational-preflight evidence allowance was consumed by terminal run `34171361117` and after the fail-closed ancestry-guard defect was repaired and canonically merged.

This request does not reopen, rerun, retry, replay, or reinterpret the consumed V1 run. It creates no new execution authority by itself.

## 2. Canonical evidence requiring a new decision

The prior exact Founder Decision B authorized exactly one post-merge operational-preflight evidence run with no automatic retry:

```text
MAX_AUTHORIZED_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

That allowance is now consumed:

```text
V1_EVIDENCE_RUN_ID=34171361117
V1_EVIDENCE_RUN_ATTEMPT=1
V1_EVIDENCE_RUN_CONCLUSION=failure
V1_EVIDENCE_RUN_HEAD=af6472d4df3218bdf3a39dbe24ea405178f3424a
V1_AUTHORIZED_RUNS_EXECUTED=1
V1_AUTHORIZED_RUNS_REMAINING=0
V1_RERUN_AUTHORITY=NONE
```

The failure occurred in the first marker/canonical-authority guard before runtime provisioning. No model, evaluation, tournament, A15, training, protected-data, credentialed custom-step, procurement, payment, or spend action occurred.

The repair is now canonical at:

```text
V1_GUARD_REPAIR_PR=307
V1_GUARD_REPAIR_QUALIFIED_HEAD=b57dbcbac207573dd92b2b93cfbde37fbf79c099
V1_GUARD_REPAIR_STATIC_RUN=34171734731
V1_GUARD_REPAIR_STATIC_JOB=101893184515
V1_GUARD_REPAIR_SPEC007=390_PASS_50_SUBTESTS_PASS
V1_GUARD_REPAIR_FULL_REPOSITORY=1039_PASS_178_SUBTESTS_PASS
V1_GUARD_REPAIR_DIFF_CHECK=PASS
V1_GUARD_REPAIR_EMPIRICAL_JOB=SKIPPED
V1_GUARD_REPAIR_CANONICAL_MERGE=264e1f4056d7fdf96696c5296edc9ab3f42df291
```

The repair changes ancestry visibility from shallow depth 2 to full history and does not itself authorize another empirical run.

## 3. Decision A — remain blocked

Exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_A
```

Decision A means:

```text
CORRECTIVE_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No new operational-preflight attempt is prepared or executed.

## 4. Decision B — authorize one new versioned corrective attempt

Recommended exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_B
```

Only after this exact token is supplied **after this decision request is canonically merged** and then separately captured canonically, Decision B authorizes the following bounded sequence:

1. prepare a new review-first V2 operational-preflight implementation from the then-current canonical `main`;
2. preserve the V1 failure and exhausted V1 allowance unchanged;
3. use a new versioned workflow surface and new versioned evidence branch/marker rather than rerunning/reusing V1;
4. statically qualify the exact V2 implementation head without executing the empirical lane;
5. guarded-merge the qualified V2 implementation canonically;
6. create exactly one marker-only direct-child commit on the exact V2 evidence branch from the exact V2 implementation merge;
7. execute exactly one new V2 operational-preflight evidence run, attempt 1 only;
8. reconcile its observed result append-only as PASS, INCOMPLETE, or FAIL;
9. do not retry, rerun, replay, or create a second V2 attempt absent a later separate authority.

The exact new versioned surfaces are reserved as:

```text
CORRECTIVE_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v2.yml
CORRECTIVE_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v2
CORRECTIVE_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v2.txt
MAX_AUTHORIZED_CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
CORRECTIVE_RUN_ATTEMPT_REQUIRED=1
CORRECTIVE_RERUN_AUTHORITY=NONE_BY_DEFAULT
CORRECTIVE_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

## 5. V2 implementation constraints

If Decision B becomes canonical, the V2 implementation must preserve or strengthen all V1 fail-closed controls and specifically require:

```text
ANCESTRY_GUARD_CHECKOUT_FETCH_DEPTH=0
EVIDENCE_MARKER_DIRECT_CHILD_OF_EXACT_CANONICAL_IMPLEMENTATION_MERGE=REQUIRED
EVIDENCE_MARKER_ONLY_CHANGED_PATH=REQUIRED
IMPLEMENTATION_PARENT_MUST_BE_MERGE_COMMIT=REQUIRED
FOUNDER_DECISION_TOKEN_SHA256_BINDING=REQUIRED
PULL_REQUEST_EMPIRICAL_JOB=SKIPPED
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
```

V2 may reconstruct only the exact previously bound public runtime dependencies needed for operational evidence. Dependency drift, runner-policy drift, identity mismatch, access ambiguity, credential ambiguity, network-boundary ambiguity, retention ambiguity, or zero-spend ambiguity must fail closed.

## 6. Non-expansion boundary

Decision B, if later selected and canonically captured, does **not** authorize any of the following:

```text
V1_RERUN=PROHIBITED
V1_FAILED_JOB_RERUN=PROHIBITED
V1_REPLAY=PROHIBITED
MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
MODEL_CONVERSION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_CREDENTIAL_USE=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
SPEND=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

A successful V2 operational-preflight result would be evidence only for the fields it directly observes. It would not itself activate A15, bind a tournament subject, authorize tournament execution, select a winner, or authorize training.

## 7. Exact post-canonical selection rule

At authoring time no selection in this request is active.

```text
POST_CANONICAL_EXACT_CORRECTIVE_ATTEMPT_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION=ABSENT
CORRECTIVE_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
CORRECTIVE_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `all permissions`, prior Founder directives, and the already-consumed V1 Decision B do not match either exact corrective-attempt token and cannot create post-repair V2 authority.

The recommended token is deliberately not self-executing. It must be supplied by the Founder in a later message after this decision request is canonical.

For later exact identity capture, the recommended Decision B token has:

```text
CORRECTIVE_DECISION_B_TOKEN_SHA256=774f35983f70ba560b2e0bd9174a7f2f76c92c1617e76851e1123dcc7d39780e
```

## 8. Decision criteria

Decision B is appropriate only if the Founder accepts all of the following:

- the V1 allowance remains permanently consumed;
- the V1 terminal failure remains canonical evidence and is not rewritten as PASS;
- the repair is a prospective technical correction, not a retroactive reinterpretation;
- V2 is a new versioned one-shot attempt;
- V2 remains no-model/no-evaluation-payload and zero-spend;
- exact-head static qualification and guarded canonical merge occur before the V2 marker exists;
- one V2 run attempt consumes the new allowance regardless of conclusion;
- no automatic retry follows a V2 failure;
- downstream A1-A14, A15, tournament, winner-selection, and training gates remain separate.

## 9. Current disposition

Until an exact post-canonical selection is supplied and separately captured:

```text
CURRENT_GLOBAL_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_CORRECTIVE_OPERATIONAL_PREFLIGHT_ATTEMPT_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V1_STATIC_GUARD_REPAIR=CANONICAL_QUALIFIED
CORRECTIVE_DECISION_SURFACE=READY_FOR_CANONICALIZATION
POST_CANONICAL_CORRECTIVE_DECISION=ABSENT
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
