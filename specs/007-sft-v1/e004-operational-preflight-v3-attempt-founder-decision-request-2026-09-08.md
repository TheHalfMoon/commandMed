# E004 Operational Preflight V3 Attempt Founder Decision Request — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical prerequisite main:** `89f3bd245905f016c7c133c84dd47b65c62a8a2f`
**V2 evidence run:** `34176481565`
**V2 evidence job:** `101906795703`
**V2 evidence head:** `225d0ebe280a4ae2305dcc84dd5795ba90d198d0`
**V2 failure reconciliation:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v2-failure-reconciliation-2026-09-08.md`
**Current-state overlay:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md`
**Decision owner:** Founder
**Artifact class:** Founder decision request only
**Authority effect before exact post-canonical selection:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Request a new explicit Founder decision after the single authorized V2 operational-preflight evidence attempt terminated in a fail-closed dependency-set drift state and its one-shot allowance was consumed and canonically reconciled.

This request preserves V1 and V2 as immutable historical evidence. It does not rerun, retry, replay, amend, reinterpret, or reclassify either consumed attempt. It creates no V3 implementation, static-qualification, runtime-provisioning, empirical-run, model, evaluation, tournament, A15, training, credential, procurement, payment, or spend authority by itself.

## 2. Canonical evidence requiring a new decision

The V2 corrective Founder decision authorized exactly one new V2 empirical attempt after review-first static qualification and guarded canonical merge. That allowance is now consumed:

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
V2_REPLAY_AUTHORITY=NONE
V2_SECOND_MARKER_AUTHORITY=NONE
```

The exact Transformers/Torch dependency reconstruction frontier was:

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
EXPECTED_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAILED_BEFORE_VENV_INSTALL
```

The exact failing shell gate was:

```bash
test "$(wc -l < "$manifest" | tr -d ' ')" = "$DEPENDENCY_ARTIFACT_COUNT"
```

The run terminated at that equality check before the dependency-set manifest digest comparison, virtual-environment creation, offline dependency installation, installed-environment digest validation, Python-runtime digest validation, offline Transformers/Torch static imports, and post-staging default-deny network proof.

The captured evidence proves only dependency-set drift relative to the frozen 27-artifact contract. It does not establish a package-level root cause.

```text
PACKAGE_LEVEL_ROOT_CAUSE=NOT_PROVEN
DOWNLOAD_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
PACKAGE_SET_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
FILENAME_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
WHEEL_PLATFORM_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
PYTHON_RUNTIME_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
UPSTREAM_ARTIFACT_DRIFT_SPECIFIC_CAUSE=NOT_PROVEN
```

The V2 run separately established partial bounded evidence for the one-shot authority guard, public/ungated access boundary, runner/resource observations, exact llama.cpp reconstruction, and cleanup. Those partial PASS observations do not make the complete operational preflight PASS.

## 3. Decision A — remain blocked

Exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_A
```

Decision A means:

```text
NEW_V3_IMPLEMENTATION_AUTHORITY=NONE
NEW_V3_STATIC_QUALIFICATION_AUTHORITY=NONE
NEW_V3_RUNTIME_PROVISIONING_AUTHORITY=NONE
NEW_V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No V3 implementation or empirical attempt is prepared or executed.

## 4. Decision B — authorize one separately versioned V3 attempt

Recommended exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
```

Only after this exact token is supplied **after this decision request is canonically merged** and then separately captured canonically, Decision B authorizes the following bounded sequence:

1. prepare a new review-first V3 operational-preflight implementation from the then-current canonical `main`;
2. preserve V1 and V2 evidence and consumed allowances unchanged;
3. use new V3 workflow, evidence branch, and marker surfaces rather than rerunning or reusing V1 or V2;
4. explicitly version and review the prospective V3 dependency-artifact contract before any empirical run;
5. statically qualify the exact V3 implementation head without executing the empirical lane;
6. guarded-merge the qualified V3 implementation canonically;
7. create exactly one marker-only direct-child commit on the exact V3 evidence branch from the exact V3 implementation merge;
8. execute exactly one new V3 operational-preflight evidence run at attempt 1 only;
9. treat the first V3 run as consuming the complete V3 allowance regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure;
10. reconcile the observed V3 result append-only as PASS, INCOMPLETE, or FAIL;
11. do not retry, rerun, replay, or create a second V3 attempt absent a later separate canonical authority.

Reserved V3 surfaces:

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

## 5. Required prospective V3 dependency-evidence design

V3 must address the observed V2 dependency-set drift prospectively. V3 must not silently replace the frozen V2 dependency contract with whatever the current resolver returns.

Before any future V3 empirical trigger becomes eligible, the review-first V3 implementation must define an explicit, versioned, bounded dependency-artifact contract and static policy tests for that contract. The contract must be based only on separately justified evidence available at implementation time; this decision request does not declare what the future artifact count, filenames, sizes, or digests are.

The V3 empirical lane must use diagnostic-first fail-closed ordering so that an identity mismatch remains a failure while still preserving enough bounded evidence to reconcile the exact drift without a second empirical run. Where directly observable and authorized, the lane must emit or derive before the first terminating identity comparison:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT
OBSERVED_DEPENDENCY_ARTIFACT_FILENAMES
OBSERVED_DEPENDENCY_ARTIFACT_SIZES
OBSERVED_DEPENDENCY_ARTIFACT_SHA256_VALUES
OBSERVED_DEPENDENCY_SET_MANIFEST_SHA256
OBSERVED_PROVISIONING_HOSTS
```

The implementation must then compare those observations against the separately reviewed and frozen V3 contract and fail closed on any mismatch.

This diagnostic ordering is an implementation requirement only. It is not current runtime evidence and does not establish a new dependency identity in this request.

## 6. V3 one-shot and trigger controls

If Decision B later becomes canonical, V3 must preserve or strengthen the existing fail-closed controls:

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
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

V1 and V2 workflows, markers, branches, terminal runs, and reconciliation records remain immutable historical evidence.

## 7. Runtime and provider boundary

Decision B, if later selected and canonically captured, may authorize only the public, no-model, no-evaluation-payload operational-preflight runtime reconstruction necessary to produce the bounded evidence explicitly defined by the future V3 implementation record.

Any future V3 runtime identity, dependency contract, provider binding, host/resource observation, network boundary, retention binding, or zero-spend binding must be explicit and fail closed. Compatible substitution, unreviewed dependency drift, credential ambiguity, gated/private access, or spend ambiguity is not accepted.

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

## 8. Explicit non-expansion

Neither this request nor a future Decision B selection authorizes any V1 or V2 rerun, retry, replay, failed-job rerun, replacement marker, branch reset, or historical evidence rewrite.

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
HISTORICAL_V2_EVIDENCE_REINTERPRETATION=PROHIBITED
```

A future V3 operational-preflight PASS, if actually observed, would establish only the fields it directly proves. It would not itself activate A15, create a live A1-A14 snapshot by declaration, bind a tournament execution subject, authorize tournament execution, select a winner, or authorize training.

## 9. Exact post-canonical selection rule

At authoring time no selection in this request is active.

```text
POST_CANONICAL_EXACT_V3_ATTEMPT_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=ABSENT
NEW_V3_IMPLEMENTATION_AUTHORITY=NONE
NEW_V3_STATIC_QUALIFICATION_AUTHORITY=NONE
NEW_V3_RUNTIME_PROVISIONING_AUTHORITY=NONE
NEW_V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `continue`, `all permissions`, `finish the project`, prior Founder directives, and the consumed V1/V2 decisions do not match either exact V3 token and cannot create V3 authority.

The recommended Decision B token is deliberately not self-executing. It must be supplied by the Founder in a later message after this decision request is canonical.

For later exact identity capture, the recommended Decision B token has:

```text
V3_DECISION_B_TOKEN_SHA256=e21b6faea3700c716d702ff80b13269721083f9e0ea06b33e215d289f0930fdf
```

## 10. Decision criteria

Decision B is appropriate only if the Founder accepts all of the following:

- V1 and V2 allowances remain permanently consumed;
- both V1 and V2 terminal failures remain canonical evidence and are not rewritten as PASS;
- V3 is a new versioned one-shot attempt, not a V2 retry;
- the package-level cause of the V2 28-versus-27 drift remains unproven by current evidence;
- the V3 dependency contract must be prospective, explicit, versioned, and reviewed rather than silently adopting current resolver output;
- V3 must capture bounded diagnostic dependency identity before a terminating equality/hash mismatch where technically and policy-wise available;
- V3 remains no-model, no-evaluation-payload, no-private-credential, and zero-spend;
- exact-head static qualification and guarded canonical merge occur before the V3 marker exists;
- one V3 run attempt consumes the complete V3 allowance regardless of conclusion;
- no automatic retry follows a V3 failure;
- live A1-A14, A15, tournament, winner-selection, and training gates remain separate downstream gates.

## 11. Current disposition

Until an exact post-canonical selection is supplied and separately captured:

```text
CURRENT_GLOBAL_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_V3_OPERATIONAL_PREFLIGHT_ATTEMPT_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_DEPENDENCY_SET_DRIFT
PACKAGE_LEVEL_ROOT_CAUSE=NOT_PROVEN
V3_DECISION_SURFACE=READY_FOR_CANONICALIZATION
POST_CANONICAL_V3_DECISION=ABSENT
NEW_V3_IMPLEMENTATION_AUTHORITY=NONE
NEW_V3_STATIC_QUALIFICATION_AUTHORITY=NONE
NEW_V3_RUNTIME_PROVISIONING_AUTHORITY=NONE
NEW_V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
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
