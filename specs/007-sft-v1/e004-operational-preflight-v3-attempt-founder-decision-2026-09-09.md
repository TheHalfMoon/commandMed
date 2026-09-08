# E004 Operational Preflight V3 Attempt Founder Decision — 2026-09-09

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical decision request:** `specs/007-sft-v1/e004-operational-preflight-v3-attempt-founder-decision-request-2026-09-08.md`
**Canonical decision-request merge:** `e7682a16876e542f82a16045c8fbd66ea2651edf`
**Artifact class:** Founder decision capture
**Decision owner:** Founder
**Decision state before canonical merge:** CAPTURED_PENDING_CANONICAL_MERGE
**Current authorized spend:** USD 0

## 1. Exact post-canonical Founder token

After the V3 decision request became canonical, the Founder separately supplied exactly:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
```

Exact token SHA-256:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_TOKEN_SHA256=e21b6faea3700c716d702ff80b13269721083f9e0ea06b33e215d289f0930fdf
```

This token is not inferred from generic continuation language, ordinary approvals, prior Founder directives, or the consumed V1/V2 decisions.

## 2. Decision effect after canonical merge

Only after this decision capture is canonically merged, and only while the canonical V3 decision-request constraints remain satisfied:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_V3
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=AUTHORIZED_NO_MODEL_NO_EVALUATION_PAYLOAD
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=AUTHORIZED_BOUNDED_PUBLIC_RUNTIME_RECONSTRUCTION_ONLY
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=AUTHORIZED_EXACTLY_ONE_NEW_V3_POST_MERGE_RUN
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B does not make operational preflight or any downstream gate PASS by declaration.

## 3. Reserved V3 surfaces

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
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

V1 and V2 workflows, branches, markers, runs, and reconciliation records remain immutable historical evidence.

## 4. Required prospective V3 dependency contract

The V3 implementation must address the observed V2 dependency-set drift prospectively and must not silently promote the V2 observed count of 28 or current resolver output into a new expected contract.

Before a V3 empirical marker becomes eligible, the review-first V3 implementation must define an explicit, versioned, bounded dependency-artifact contract and static policy tests for it.

The V3 empirical lane must capture bounded diagnostic dependency identity before the first terminating expected-count or expected-digest equality comparison, including where directly observable and authorized:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT
OBSERVED_DEPENDENCY_ARTIFACT_FILENAMES
OBSERVED_DEPENDENCY_ARTIFACT_SIZES
OBSERVED_DEPENDENCY_ARTIFACT_SHA256_VALUES
OBSERVED_DEPENDENCY_SET_MANIFEST_SHA256
OBSERVED_PROVISIONING_HOSTS
```

The lane must then fail closed on any mismatch against the separately reviewed and frozen V3 contract.

## 5. Runtime and access boundary

Any V3 implementation and later single empirical attempt remain public, no-model, no-evaluation-payload, no-private-credential, and zero-spend.

```text
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

## 6. Explicit non-expansion

```text
V1_RERUN=PROHIBITED
V1_RETRY=PROHIBITED
V1_REPLAY=PROHIBITED
V2_RERUN=PROHIBITED
V2_RETRY=PROHIBITED
V2_REPLAY=PROHIBITED
V2_FAILED_JOB_RERUN=PROHIBITED
V2_SECOND_MARKER=PROHIBITED
V2_BRANCH_RESET_FOR_NEW_RUN=PROHIBITED
HISTORICAL_V1_V2_EVIDENCE_REINTERPRETATION=PROHIBITED
```

A future V3 operational-preflight PASS, if actually observed, establishes only the fields directly proven by that run. It does not activate A15, create a live A1-A14 PASS snapshot by declaration, bind tournament execution authority, select a model winner, or authorize training.

## 7. One-shot consumption rule

The V3 implementation must first receive exact-head static qualification and guarded canonical merge. Only then may one marker-only direct-child commit be created on the exact V3 evidence branch.

The first V3 empirical workflow run at attempt 1 consumes the complete V3 allowance regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure.

```text
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

## 8. Current disposition before canonical merge

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
POST_CANONICAL_EXACT_V3_ATTEMPT_FOUNDER_DECISION_TOKEN=CAPTURED_PENDING_CANONICAL_MERGE
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=PENDING_CANONICAL_DECISION_CAPTURE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
SUCCESSOR_PASS_PREFLIGHT=NO
LIVE_A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
