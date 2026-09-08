# E004 Registry Current-State Reconciliation V52 — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md`
**Decision request:** `specs/007-sft-v1/e004-operational-preflight-v3-founder-decision-request-2026-09-08.md`
**Artifact class:** append-only current-state / dependency-frontier overlay
**Authority effect:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Bind the post-V2 E004 frontier to the new V3 Founder decision surface without granting any V3 implementation, dependency-resolution, or empirical authority.

V52 preserves the terminal V1 and V2 evidence and requires a new exact post-canonical Founder selection before any V3 preparation begins.

## 2. Historical one-shot state

```text
V1_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_DEPENDENCY_SET_DRIFT
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
```

No historical run is reopened or reclassified.

## 3. V3 decision surface

The companion decision request exposes exactly two choices:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_DECISION_A
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_DECISION_B
```

Recommended Decision B exact token SHA-256:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION_TOKEN_SHA256=ed76f9a9259201bfd84a66f33a41b2e4e7f02a2f101b2bd2582e054a7c8bc0e7
```

At authoring time neither token is active.

## 4. V3 Decision B prospective design only

If and only if exact Decision B is supplied after the decision request is canonical and is then separately captured canonically, the next bounded work may prepare a new V3 review-first lane with an exact committed dependency lock qualified before any empirical run.

The reserved future surfaces are:

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_DEPENDENCY_LOCK_PATH=specs/007-sft-v1/e004-operational-preflight-v3-dependency-set-v1.tsv
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
```

These names are reservations only. Their existence or execution is not authorized by V52.

## 5. Current authority state

```text
POST_CANONICAL_EXACT_V3_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=ABSENT
V3_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
V3_DEPENDENCY_SET_PREPARATION_AUTHORITY=NONE
V3_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_EMPIRICAL_EVIDENCE_RUN_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `all permissions`, earlier Founder directives, and the consumed V1/V2 decisions do not create V3 authority.

## 6. Stable downstream state

```text
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=PASS
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PASS_4_OF_4
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE
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

## 7. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v52-2026-09-08.md
CURRENT_DECISION_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_V3_OPERATIONAL_PREFLIGHT_DECISION
V3_DECISION_REQUEST=READY_FOR_CANONICALIZATION
POST_CANONICAL_EXACT_V3_FOUNDER_DECISION_TOKEN=ABSENT
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED_PENDING_EXACT_POST_CANONICAL_V3_FOUNDER_DECISION
PROJECT_FINISHED=NO
```
