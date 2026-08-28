# E004 A2 Review-Governance Direct-Main Qualification Record — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** non-destructive qualification/corrective record  
**Direct-main commit under review:** `c7e4990db9cba99a0c6f86936f5c21c15cb73045`  
**Direct-main parent:** `271712bbea9ef631510c8892ca9ce33ab21d054d`  
**Direct-main tree:** `bedd36392b9d3d26ba5a8a25b8edd376aa2ca72c`  
**Affected path:** `specs/007-sft-v1/e004-a2-review-governance-profile-2026-08-28.md`  
**Authority effect:** NONE until fresh exact-head qualification  
**Execution effect:** NONE  
**Spend:** USD 0

## Purpose

The review-governance profile was written directly to the default branch because the repository write omitted an explicit feature-branch argument. This was a repository-process error. Shared history is preserved: no reset, force-push, rebase, or destructive rewrite is permitted or attempted.

The direct-main commit must not be treated as qualified scientific-governance evidence merely because it is reachable from `main`.

```text
DIRECT_MAIN_WRITE_OCCURRED=YES
DIRECT_MAIN_COMMIT=c7e4990db9cba99a0c6f86936f5c21c15cb73045
DIRECT_MAIN_COMMIT_QUALIFICATION=UNQUALIFIED_PENDING_CORRECTIVE_EXACT_HEAD_REVIEW
HISTORY_REWRITE_PERFORMED=NO
FORCE_PUSH_PERFORMED=NO
REBASE_PERFORMED=NO
RAW_ACTIONS_RUNS_ON_DIRECT_MAIN_HEAD=0
```

## Qualification subject

The substantive subject is exactly:

```text
specs/007-sft-v1/e004-a2-review-governance-profile-2026-08-28.md
```

Its bounded purpose is procedural only: freeze the still-unresolved A2 reviewer-governance mechanics identified by canonical Session 9 Q4 and the qualified-review request brief, while leaving all actual scientific evidence and human review unresolved.

The profile proposes:

```text
THRESHOLD_AUTHORITY_FUNCTION_1=CLINICAL_DOMAIN_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_2=STATISTICAL_METHOD_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_3=CANONICAL_GOVERNANCE_ADOPTION

MINIMUM_DISTINCT_CLINICAL_REVIEWERS=1
MINIMUM_DISTINCT_STATISTICAL_REVIEWERS=1
MINIMUM_DISTINCT_GOVERNANCE_ADOPTERS=1
MINIMUM_DISTINCT_PEOPLE_PER_METRIC_POLICY=3

REVIEW_DISPOSITIONS=ACCEPT,REVISE,REJECT,BLOCKED
QUORUM=ALL_REQUIRED_SCIENTIFIC_REVIEWERS_ACCEPT_THEN_DISTINCT_GOVERNANCE_ADOPTION
MATERIAL_DISSENT=FAIL_CLOSED
FOUNDER_TIE_BREAK=PROHIBITED
AI_OR_CODE_REVIEW_EQUALS_SCIENTIFIC_REVIEW=NO
```

Fresh independent review must determine whether those choices are consistent with the controlling frozen governance rather than treating them as valid because the direct-main commit exists.

## Controlling sources for exact-head review

Review must re-read at least:

```text
.specify/memory/constitution.md
AGENTS.md
specs/005-base-model-tournament/session-9-q3-statistical-rationale-sample-size-power-architecture.md
specs/005-base-model-tournament/session-9-q4-clinical-review-threshold-margin-governance.md
specs/005-base-model-tournament/session-9-q5-per-metric-threshold-freeze-readiness-matrix.md
specs/007-sft-v1/e004-a2-public-threshold-evidence-discovery-2026-08-27.md
specs/007-sft-v1/e004-a2-evidence-package-workbench-2026-08-27.md
specs/007-sft-v1/e004-a2-statistical-method-candidate-packet-2026-08-27.md
specs/007-sft-v1/e004-a2-qualified-review-request-brief-2026-08-27.md
specs/007-sft-v1/e004-a2-review-governance-profile-2026-08-28.md
```

## Required review questions

Fresh exact-head review must verify all of the following:

1. Procedural governance can be frozen without impersonating clinical-domain review, statistical-method review, or numeric threshold evidence.
2. The three required authority functions remain separate and the Founder/governance owner cannot replace either scientific function.
3. The minimum distinct-person rule is compatible with Session 9 Q4 and does not weaken any stronger metric-specific requirement.
4. The broad qualification descriptions do not fabricate reviewer identities or credentials and remain auditable/fail closed.
5. Reuse of `ACCEPT`, `REVISE`, `REJECT`, and `BLOCKED` does not conflict with controlling threshold-review governance.
6. The proposed quorum does not permit majority override, silence-as-approval, or selective discard of dissent.
7. Material policy changes force fresh review and new policy identity.
8. Candidate-result and Private-Gold firewalls remain intact.
9. The profile creates no reviewer appointment/engagement/payment authority and no spend.
10. `T1_A2` remains incomplete; `D34` remains blocked by T1; E004 remains `BLOCKED_PREFLIGHT`; E005 remains `NOT_REACHED`.
11. No model conversion, contamination assessment, training, credential, PHI, Private Gold, or spend authority is created.

## Effectiveness rule

```text
DIRECT_MAIN_PROFILE_EFFECTIVE_AS_QUALIFIED_PROCEDURAL_GOVERNANCE=NO_PENDING_CORRECTIVE_PR
```

Only if the corrective PR receives fresh exact-head independent review with no material blocker and is then merged with exact-head/post-merge evidence may the profile be treated as qualified procedural governance.

Even after such qualification, the following remain absent:

```text
EXACT_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
COMMANDMED_SPECIFIC_NUMERIC_THRESHOLD_OR_MARGIN_POLICY=ABSENT
NUMERIC_CONFIDENCE_OR_ERROR_RATE_POLICY=ABSENT
NUMERIC_SAMPLE_SIZE_OR_POWER_DESIGN=ABSENT
CANONICAL_THRESHOLD_POLICY_ADOPTION=ABSENT
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## Exclusions

This corrective record performs no scientific review, reviewer outreach or engagement, reviewer appointment, payment, threshold/margin selection, benchmark/model/device execution, model conversion, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, or spend.
