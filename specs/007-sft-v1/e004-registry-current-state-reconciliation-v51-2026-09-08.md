# E004 Registry Current-State Reconciliation V51 — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v50-2026-09-08.md`
**V2 corrective decision:** `specs/007-sft-v1/e004-operational-preflight-corrective-attempt-founder-decision-2026-09-08.md`
**V2 evidence result:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v2-failure-reconciliation-2026-09-08.md`
**Artifact class:** append-only current-state / dependency-frontier overlay
**Authority effect:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Advance the E004 current-state overlay through the canonical corrective Decision B, the qualified V2 implementation, and the terminal result of the single authorized V2 empirical attempt.

V51 preserves both V1 and V2 as immutable historical evidence. It does not reinterpret either failed run as PASS and does not create another empirical allowance.

## 2. Canonical V2 decision and implementation

The exact post-canonical corrective Founder decision was captured and canonically merged:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_B
FOUNDER_E004_OPERATIONAL_PREFLIGHT_CORRECTIVE_ATTEMPT_DECISION_TOKEN_SHA256=774f35983f70ba560b2e0bd9174a7f2f76c92c1617e76851e1123dcc7d39780e
CORRECTIVE_DECISION_CAPTURE_PR=309
CORRECTIVE_DECISION_CAPTURE_CANONICAL_MERGE=846807332c69c64ace242a492e900491a58f020a
```

The V2 implementation then received exact-head static qualification and canonical merge:

```text
V2_IMPLEMENTATION_PR=310
V2_IMPLEMENTATION_QUALIFIED_HEAD=584ee75eaa36cb9dd995d76eacca9205d33ca918
V2_IMPLEMENTATION_STATIC_RUN=34176403881
V2_IMPLEMENTATION_STATIC_JOB=101906571803
V2_IMPLEMENTATION_STATIC_QUALIFICATION=PASS
V2_IMPLEMENTATION_EMPIRICAL_JOB_ON_PR=skipped
V2_IMPLEMENTATION_CANONICAL_MERGE=a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0
```

The first PR head failed only the diff-whitespace gate and was repaired prospectively before merge. That PR static failure did not consume empirical V2 authority because the empirical job remained skipped.

## 3. V2 empirical run identity and terminal result

Exactly one post-merge V2 evidence marker was created as the direct child of the exact canonical implementation merge:

```text
V2_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v2
V2_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v2.txt
V2_EVIDENCE_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_EVIDENCE_WORKFLOW_RUN_ID=34176481565
V2_EVIDENCE_WORKFLOW_RUN_NUMBER=3
V2_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_JOB_CONCLUSION=failure
WORKFLOW_ARTIFACT_COUNT=0
```

The terminal evidence disposition is:

```text
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_DEPENDENCY_SET_DRIFT
```

## 4. Progress proven by V2

Unlike V1, V2 passed the corrected ancestry guard and reached bounded runtime reconstruction.

```text
ONE_RUN_MARKER_AND_CANONICAL_AUTHORITY_GUARD=PASS
CREDENTIAL_AND_PUBLIC_UNGATED_ACCESS_BOUNDARY=PASS
HOST_RESOURCE_CAPTURE=PASS
LLAMA_RUNTIME_RECONSTRUCTION=PASS
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAIL
POST_STAGING_DEFAULT_DENY_NETWORK_PROOF=NOT_EXECUTED
RETENTION_CLEANUP_STATE=PASS
```

The live runner observations and exact successful llama.cpp reconstruction are preserved in the V2 failure-reconciliation record. They are partial evidence only and do not make the complete operational preflight PASS.

## 5. Exact V2 failure frontier

The frozen V2 dependency contract expected 27 artifacts. The live resolver produced 28.

```text
EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
EXPECTED_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAILED_BEFORE_VENV_INSTALL
```

The exact failing gate was the artifact-count equality test. The run stopped before the dependency manifest hash comparison, offline install, installed-environment hash, Python-runtime hash, offline Transformers/Torch static import, and post-staging default-deny network proof.

The captured evidence proves dependency-set drift relative to the frozen contract; it does not prove a package-level root cause.

## 6. One-shot authority state after V2

The first empirical V2 run at attempt 1 consumes the entire corrective allowance regardless of conclusion.

```text
MAX_AUTHORIZED_CORRECTIVE_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY_STATE=CONSUMED_EXACTLY_ONCE
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
V2_REPLAY_AUTHORITY=NONE
V2_SECOND_MARKER_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
```

No rerun of workflow run `34176481565`, no failed-job rerun, no replacement V2 marker, no alternate V2 branch, and no new empirical attempt is authorized by the consumed Decision B.

## 7. Stable scientific and execution state

The pre-existing four-candidate model-load compatibility result remains distinct from operational preflight. V2 itself performed no model execution.

```text
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=PASS
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PASS_4_OF_4
MODEL_WEIGHT_ACQUISITION_PERFORMED_BY_V2=NO
MODEL_LOAD_PERFORMED_BY_V2=NO
MODEL_INFERENCE_PERFORMED_BY_V2=NO
EVALUATION_PAYLOAD_EXECUTION_PERFORMED_BY_V2=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
LIVE_A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 8. Remaining preflight gap

The V2 run materially narrowed the operational uncertainty, but the exact Transformers/Torch runtime identity and the later network proof remain incomplete.

```text
EXACT_RUNNER_RESOURCE_OBSERVATION=PARTIAL_PASS_FROM_V2
EXACT_PUBLIC_UNGATED_ACCESS_CLASS=PASS_FROM_V2
EXACT_CREDENTIAL_BOUNDARY_STATE=PASS_FROM_V2
EXACT_LLAMA_RUNTIME_RECONSTRUCTION_STATE=PASS_FROM_V2
EXACT_TRANSFORMERS_RUNTIME_RECONSTRUCTION_STATE=FAIL_DEPENDENCY_SET_DRIFT
POST_STAGING_NETWORK_DISABLE_MECHANISM_STATE=NOT_EXECUTED
EXACT_EPHEMERAL_RETENTION_CLEANUP_STATE=PASS_FROM_V2
EXACT_ZERO_SPEND_RESOURCE_CLASS_STATE=PASS_FROM_V2_OBSERVATION
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE
```

A later attempt must not silently replace the frozen dependency evidence with current resolver output. Any prospective dependency-set update must be explicitly reviewed, versioned, and bounded before a new empirical attempt is authorized.

## 9. Dependency-safe next transition

The consumed V2 authority permits reconciliation of the observed result but does not authorize another empirical attempt.

The next dependency-safe repository transition is a new Founder decision request that exposes whether to remain blocked or authorize a separately versioned review-first V3 preparation and exactly one future V3 attempt after its own static qualification and canonical merge.

```text
NEXT_E004_TRANSITION=NEW_FOUNDER_DECISION_SURFACE_FOR_SEPARATELY_VERSIONED_V3_ATTEMPT
V2_STATIC_OR_EMPIRICAL_RETRY=PROHIBITED
NEW_V3_IMPLEMENTATION_AUTHORITY=NONE
NEW_V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
```

Any future V3 proposal must preserve the no-model, no-evaluation-payload, zero-spend boundary and must address the observed dependency-set drift prospectively rather than changing V2 historical evidence.

## 10. Explicit non-actions

```text
V2_RERUN_PERFORMED=NO
V2_FAILED_JOB_RERUN_PERFORMED=NO
SECOND_V2_MARKER_CREATED=NO
MODEL_WEIGHT_ACQUISITION_PERFORMED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
EVALUATION_PAYLOAD_ACCESS_PERFORMED=NO
EVALUATION_PAYLOAD_EXECUTION_PERFORMED=NO
BENCHMARK_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
GATED_ASSET_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 11. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md
V1_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_DECISION_B=CANONICAL_CONSUMED_SINGLE_RUN
V2_OPERATIONAL_PREFLIGHT_IMPLEMENTATION=CANONICAL_QUALIFIED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN=TERMINAL_FAILURE_TRANSFORMERS_DEPENDENCY_SET_DRIFT
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED_PENDING_SEPARATE_NEW_ATTEMPT_DECISION
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
