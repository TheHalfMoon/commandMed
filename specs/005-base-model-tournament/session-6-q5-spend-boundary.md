# Spec 005 — Session 6 Q5 Compute/Spend Boundary

**Lifecycle:** CLARIFY ONLY
**Accepted question:** Session 6 — Q5
**Exact predecessor head:** `15fb48a4cef3c985d4d6bd9482923edd572be194`
**Purpose:** freeze the pre-execution compute/spend authority boundary without granting execution authority.

> This artifact records only the accepted Session 6 Q5 clarification. It does not authorize `PLAN`, model access, model-weight retrieval, model conversion, benchmark-payload access or execution, device execution, provider/API generation, Private Gold access, PHI/restricted-data access, gated-term acceptance, gated-asset access, training, or tournament execution.

## Accepted policy

`ZERO_SPEND_PREEXECUTION_SEPARATE_ACTIVATION_REQUIRED` freezes the current financial and compute authority boundary:

```text
TOURNAMENT_COMPUTE_SPEND_POLICY=ZERO_SPEND_PREEXECUTION_SEPARATE_ACTIVATION_REQUIRED

PREEXECUTION_PROVIDER_SPEND_CAP_USD=0
PREEXECUTION_PAID_COMPUTE_PROVISIONING=PROHIBITED
PREEXECUTION_PAID_API_USAGE=PROHIBITED

READ_ONLY_PUBLIC_METADATA_RESEARCH=ALLOWED
EXISTING_REPOSITORY_ANALYSIS=ALLOWED
DOCUMENTATION_ONLY_GOVERNANCE_WORK=ALLOWED

MODEL_WEIGHT_ACCESS=NOT_AUTHORIZED
MODEL_EXECUTION=NOT_AUTHORIZED
MODEL_CONVERSION=NOT_AUTHORIZED
BENCHMARK_PAYLOAD_ACCESS=NOT_AUTHORIZED
BENCHMARK_PAYLOAD_EXECUTION=NOT_AUTHORIZED
DEVICE_EXECUTION=NOT_AUTHORIZED

FUTURE_EXECUTION_BUDGET_REQUIRES_SEPARATE_CANONICAL_AUTHORIZATION=YES
FUTURE_BUDGET_MUST_BIND_MAX_USD=YES
FUTURE_BUDGET_MUST_BIND_COMPUTE_RESOURCES=YES
FUTURE_BUDGET_MUST_BIND_ALLOWED_PROVIDERS_OR_LOCAL_RESOURCES=YES
FUTURE_BUDGET_MUST_BIND_STOP_CONDITIONS=YES

UNDECLARED_SPEND=PROHIBITED
POST_RESULT_BUDGET_EXPANSION=PROHIBITED
CANDIDATE_SPECIFIC_SPEND_EXCEPTION=PROHIBITED

CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
```

## Semantics

- Current authorized tournament/provider spend is exactly `USD 0`.
- Paid compute provisioning and paid provider/API use are prohibited before a separate canonical execution-budget activation.
- Read-only public metadata research, non-executing analysis of the existing repository, and documentation/governance work remain allowed only within all previously frozen access and execution boundaries.
- Zero paid spend does not create local execution authority. Model weights, model execution, model conversion, benchmark payloads, device execution, provider generation, Private Gold, PHI/restricted data, and gated assets remain separately unauthorized.
- Any future execution budget must be separately authorized before candidate results and must bind an exact maximum USD amount, concrete compute-resource identities/classes, allowed providers and/or local resources, and stop conditions.
- Undeclared spend, candidate-specific spend exceptions, and post-result budget expansion are prohibited.
- This policy selects no provider, cloud, device, local runtime, model, benchmark, or candidate.

## Session 6 closeout

Acceptance of Q5 completes the bounded five-question Session 6 only:

```text
CLARIFICATION_SESSION_6=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_6_STATUS=COMPLETE_BOUNDED_SESSION

TOURNAMENT_COMPUTE_SPEND_POLICY=ZERO_SPEND_PREEXECUTION_SEPARATE_ACTIVATION_REQUIRED
CURRENT_AUTHORIZED_SPEND_USD=0

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

Completion of bounded Session 6 does **not** complete the overall clarification lifecycle and does **not** authorize transition to `PLAN`.

## Canonical progress-marker reconciliation rule

At the exact predecessor head, `spec.md` still recorded Session 6 as `4/5 IN_PROGRESS`. Because a prior full-file replacement attempt during Q4 produced a transient truncation that had to be repaired additively, this Q5 acceptance is recorded in this dedicated append-only clarification artifact rather than risking another whole-file replacement.

At any exact head containing this artifact, the Session 6 progress markers above supersede **only** the older `4/5 IN_PROGRESS` Session 6 progress markers in `spec.md`. They do not supersede, weaken, or rewrite any other policy, authority boundary, unresolved evidence requirement, candidate status, or fail-closed rule in `spec.md`.

A future canonical reconciliation may fold this closeout into `spec.md` only through a separately reviewed, exact-diff-safe documentation change. Until then, this artifact is the exact-head Session 6 Q5 closeout record.

## Remaining clarification scope

Q5 resolves the current pre-execution compute/spend boundary. It does not resolve remaining clarification work, including exact candidate/slice contamination dispositions, primary-selection benchmark slice and purpose mappings, benchmark access routes/authority, clinical/statistical thresholds, component rights/privacy/license evidence, exact runtime/build/tokenizer/instrumentation identities, numeric performance values, thermal/energy/failure-signal details, secondary ranking order, exact-head independent review, or final clarification lifecycle closure.
