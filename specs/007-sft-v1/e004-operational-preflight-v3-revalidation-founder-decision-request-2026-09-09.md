# E004 Operational Preflight V3 Revalidation Founder Decision Request — 2026-09-09

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Corrected evidence:** `specs/007-sft-v1/e004-operational-preflight-v2-evidence-correction-2026-09-09.md`
**Current-state overlay:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v52-2026-09-09.md`
**Previous V3 decision capture:** `specs/007-sft-v1/e004-operational-preflight-v3-attempt-founder-decision-2026-09-09.md`
**Decision owner:** Founder
**Artifact class:** corrected Founder authority revalidation request only
**Authority effect before exact post-canonical selection:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Request an exact corrected Founder decision after direct immutable GitHub Actions evidence disproved the material 28-versus-27 premise used by the earlier V3 decision request and Decision B capture.

The earlier Decision B remains part of immutable repository history but is suspended for future V3 implementation/execution because its own canonical effect is conditional on the decision-request constraints remaining satisfied.

This request creates no V3 implementation, static qualification, runtime provisioning, marker, empirical attempt, model, evaluation, benchmark, tournament, A15, training, credential, procurement, payment, or spend authority by itself.

## 2. Correct evidence basis

The single consumed V2 run remains:

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
```

Correct terminal observation:

```text
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAME_COUNT=27
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAMES_MATCH_HISTORICAL_27_SET=YES
V2_UNEXPECTED_PROVISIONING_HOST=download-r2.pytorch.org
V2_TERMINAL_FAILURE_GATE=TRANSFORMERS_PROVISIONING_HOST_POLICY
DEPENDENCY_ARTIFACT_COUNT_GATE=NOT_EXECUTED
DEPENDENCY_SET_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
```

The earlier successful runtime-binding evidence independently proves the exact prospective dependency identity:

```text
HISTORICAL_DEPENDENCY_ARTIFACT_COUNT=27
HISTORICAL_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
```

The earlier metadata-only V4 diagnostic independently proves the required compatible public Torch route:

```text
PROVEN_REQUIRED_TORCH_PUBLIC_ROUTE_HOST=download-r2.pytorch.org
PROVEN_REQUIRED_TORCH_PUBLIC_ROUTE_PORT=443
```

## 3. Decision A — remain blocked

Exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_REVALIDATION_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_REVALIDATION_DECISION_A
```

Token SHA-256:

```text
b9ecd9cac24c44baba538101cdee7d316b602ee4bc83102edba6940afdee7342
```

Decision A means:

```text
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

## 4. Decision B — revalidate one corrected separately versioned V3 attempt

Recommended exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_REVALIDATION_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_REVALIDATION_DECISION_B
```

Token SHA-256:

```text
23909829cd962f2cbbca1048a1f0ae0f247199b01f1b81487fbd68d4791bf041
```

Only after this exact token is supplied **after this revalidation request is canonically merged** and then separately captured canonically, Decision B reauthorizes the bounded sequence below.

```text
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_V3_CORRECTED_EVIDENCE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=AUTHORIZED_NO_MODEL_NO_EVALUATION_PAYLOAD
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=AUTHORIZED_BOUNDED_PUBLIC_RUNTIME_RECONSTRUCTION_ONLY
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=AUTHORIZED_EXACTLY_ONE_NEW_V3_POST_MERGE_RUN
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 5. Required corrected V3 implementation design

If Decision B later becomes canonical, the implementation must preserve the existing reserved V3 surfaces:

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
```

The corrected implementation must not use an unconstrained resolver as the identity authority. It must define and statically test a versioned dependency-artifact contract containing the exact 27 historical filenames, sizes, and SHA-256 values recovered from the successful canonical runtime-binding evidence.

The exact contract aggregate must remain:

```text
V3_EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
V3_EXPECTED_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
```

The prospective provisioning host set may include only explicitly reviewed public hosts required by the exact frozen artifacts. For Torch, the corrected evidence justifies:

```text
V3_ALLOWED_TORCH_ARTIFACT_HOST=download-r2.pytorch.org
V3_ALLOWED_TORCH_ARTIFACT_PORT=443
```

This is a narrow exact-artifact public route authorization. It is not arbitrary web access and does not authorize model-provider endpoints, model assets, evaluation data endpoints, private credentials, or gated resources.

Before the first terminating identity comparison, the single empirical lane must emit or derive:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT
OBSERVED_DEPENDENCY_ARTIFACT_FILENAMES
OBSERVED_DEPENDENCY_ARTIFACT_SIZES
OBSERVED_DEPENDENCY_ARTIFACT_SHA256_VALUES
OBSERVED_DEPENDENCY_SET_MANIFEST_SHA256
OBSERVED_PROVISIONING_HOSTS
```

The lane must then fail closed against the frozen contract.

## 6. Required review-first and one-shot order

If Decision B is later selected and canonically captured:

```text
CORRECTED_DECISION_CAPTURE
→ V3_IMPLEMENTATION
→ STATIC_TESTS
→ REVIEW_PR
→ EXACT_HEAD_QUALIFICATION
→ GUARDED_CANONICAL_IMPLEMENTATION_MERGE
→ REVERIFY_EXACT_CANONICAL_MERGE
→ CREATE_ONE_MARKER_ONLY_DIRECT_CHILD_COMMIT
→ EXACTLY_ONE_V3_EMPIRICAL_ATTEMPT
→ EVIDENCE_RECONCILIATION
```

The first V3 empirical run at attempt 1 consumes the complete V3 allowance regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure.

```text
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

## 7. Required trigger and ancestry controls

```text
ANCESTRY_GUARD_CHECKOUT_FETCH_DEPTH=0
EVIDENCE_MARKER_DIRECT_CHILD_OF_EXACT_CANONICAL_IMPLEMENTATION_MERGE=REQUIRED
EVIDENCE_MARKER_ONLY_CHANGED_PATH=REQUIRED
IMPLEMENTATION_PARENT_MUST_BE_MERGE_COMMIT=REQUIRED
CORRECTED_FOUNDER_REVALIDATION_TOKEN_SHA256_BINDING=REQUIRED
PULL_REQUEST_EMPIRICAL_JOB=SKIPPED
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
```

V1 and V2 workflows, markers, branches, terminal runs, and evidence remain immutable and consumed.

## 8. Safety and spend boundary

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

A future V3 PASS, if actually observed, proves only what that run directly establishes. It does not activate A15, create a live A1-A14 PASS snapshot by declaration, authorize tournament execution, select a winner, authorize training, or declare project completion.

## 9. Exact post-canonical selection rule

At authoring time:

```text
POST_CANONICAL_EXACT_V3_REVALIDATION_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_REVALIDATION_DECISION=ABSENT
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `continue`, `all permissions`, `finish the project`, the earlier stale V3 Decision B token, or any V1/V2 decision does not match either corrected revalidation token and cannot create corrected V3 authority.

## 10. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_V3_REVALIDATION_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_PROVISIONING_HOST_POLICY_MISMATCH
V3_PREVIOUS_DECISION_B=CANONICAL_BUT_MATERIALLY_STALE
POST_CANONICAL_V3_REVALIDATION_DECISION=ABSENT
V3_IMPLEMENTATION_AUTHORITY=NONE
V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
LIVE_A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
