# E004 FD-004 Over-Triage Founder Decision Request — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Canonical base:** `c21230338d3295932f11e4d9f331cef907ce2eae`  
**Canonical base tree:** `8d3b4b132df774654a0225863b8aa48e4afb31fd`  
**Decision owner:** Founder  
**Decision register item:** `FD-004 — Acceptable over-triage policy`  
**Artifact class:** Founder decision request only  
**Founder decision captured by this document:** NO  
**Authority effect:** NONE  
**Numeric threshold freeze effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**Training authority:** NONE  
**External reviewer outreach authority:** NONE  
**Current authorized spend:** USD 0

## Purpose

Prepare the exact Founder decision surface for the product/ethics posture governing `benign_case_over_triage_rate` without inventing a clinical or statistical threshold.

The canonical safety policy classifies this metric as `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE`. The frozen Spec 005 threshold-readiness matrix additionally requires `FD-004` before the metric-specific threshold can ever become ready to freeze.

This request resolves only the irreducible owner/product posture. It does not replace clinical review, statistical review, intended-use definition, identity-bound evaluation evidence, uncertainty design, sample-size/power rationale, or canonical numeric threshold adoption.

```text
FD004_CURRENT_STATE=FOUNDER_REQUIRED
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO
FOUNDER_POLICY_DECISION_CAPTURED=NO
NUMERIC_THRESHOLD_SELECTED=NO
T1_A2=INCOMPLETE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## Controlling safety boundary

No option below may weaken the already-frozen noncompensable safety semantics.

```text
EMERGENCY_SAFETY_HARD_GATES_REMAIN_NONCOMPENSABLE=YES
MEDICATION_SAFETY_HARD_GATES_REMAIN_NONCOMPENSABLE=YES
MISSING_CRITICAL_INFORMATION_FAIL_CLOSED_BEHAVIOR_REMAINS_REQUIRED=YES
DETERMINISTIC_AND_AUTHORITATIVE_TOOL_BOUNDARIES_REMAIN_REQUIRED=YES
HIGH_AVERAGE_UTILITY_MAY_COMPENSATE_FOR_SAFETY_FAILURE=NO
```

`benign_case_over_triage_rate` measures burden from unnecessary escalation on clearly benign cases. It must not be optimized by silently accepting more dangerous misses or by weakening emergency/escalation policy.

## What the Founder is deciding

The Founder is choosing the product posture to be used later by qualified clinical/statistical governance when proposing an evidence-backed numeric ceiling or disposition.

The Founder is **not** choosing:

- a percentage, ratio, confidence bound, margin, sample size, or power target;
- a clinical standard of care;
- an emergency sensitivity or miss-rate threshold;
- an evaluation-suite identity;
- a reviewer identity;
- an A2 PASS disposition;
- an E004 tournament result.

## Decision classes

### `FD004_DECISION_A` — `CONSERVATIVE_SAFETY_BIAS`

```text
FOUNDER_POLICY_POSTURE=CONSERVATIVE_SAFETY_BIAS
PRODUCT_PRIORITY=MINIMIZE_DANGEROUS_UNDER_ESCALATION_WITHIN_FROZEN_SAFETY_POLICY
BENIGN_OVER_TRIAGE_BURDEN=ACCEPT_HIGHER_BURDEN_IF_REQUIRED_BY_EVIDENCE_BACKED_SAFETY_POLICY
NUMERIC_OVER_TRIAGE_CEILING=REQUIRES_CLINICAL_STATISTICAL_EVIDENCE
SAFETY_GATE_RELAXATION=PROHIBITED
```

Interpretation: commandMed should prefer a conservative escalation posture when evidence leaves a genuine safety-versus-burden tradeoff, accepting a higher benign escalation burden if required to preserve the frozen safety contract. Qualified reviewers must still establish a defensible numeric ceiling and intended-use context.

### `FD004_DECISION_B` — `BALANCED_BURDEN_WITH_NONCOMPENSABLE_SAFETY`

```text
FOUNDER_POLICY_POSTURE=BALANCED_BURDEN_WITH_NONCOMPENSABLE_SAFETY
PRODUCT_PRIORITY=REDUCE_UNNECESSARY_ESCALATION_SUBJECT_TO_NONCOMPENSABLE_SAFETY_GATES
BENIGN_OVER_TRIAGE_BURDEN=MUST_BE_MEASURED_AND_BOUNDED
NUMERIC_OVER_TRIAGE_CEILING=REQUIRES_CLINICAL_STATISTICAL_EVIDENCE
SAFETY_GATE_RELAXATION=PROHIBITED
```

Interpretation: commandMed should minimize unnecessary escalation burden, but only after the frozen safety gates are satisfied. No gain in convenience, engagement, average utility, or lower over-triage may compensate for a safety-gate failure. Qualified reviewers must still establish the numeric ceiling and uncertainty/sample-size design.

### `FD004_DECISION_C` — `NARROW_PATIENT_SCOPE_IF_BURDEN_UNRESOLVED`

```text
FOUNDER_POLICY_POSTURE=NARROW_PATIENT_SCOPE_IF_BURDEN_UNRESOLVED
PRODUCT_PRIORITY=PRESERVE_SAFETY_AND_NARROW_CLAIMS_OR_MODE_SCOPE_IF_ACCEPTABLE_BURDEN_CANNOT_BE_JUSTIFIED
BENIGN_OVER_TRIAGE_BURDEN=NO_UNSUPPORTED_ACCEPTANCE
NUMERIC_OVER_TRIAGE_CEILING=REQUIRES_CLINICAL_STATISTICAL_EVIDENCE
SAFETY_GATE_RELAXATION=PROHIBITED
```

Interpretation: if qualified evidence cannot establish an acceptable benign over-triage burden without compromising frozen safety requirements, commandMed should narrow or disable the affected patient-facing scope instead of weakening safety policy.

## ChatGPT recommendation for Founder review

```text
CHATGPT_FD004_RECOMMENDATION=FD004_DECISION_B
CHATGPT_REASON_1=IT_PRESERVES_NONCOMPENSABLE_EMERGENCY_AND_OTHER_SAFETY_GATES
CHATGPT_REASON_2=IT_TREATS_UNNECESSARY_ESCALATION_AS_A_REAL_PATIENT_AND_SYSTEM_BURDEN_THAT_MUST_BE_MEASURED
CHATGPT_REASON_3=IT_DOES_NOT_PREJUDGE_THE_NUMERIC_THRESHOLD_BEFORE_QUALIFIED_CLINICAL_AND_STATISTICAL_EVIDENCE
CHATGPT_REASON_4=IF_EVIDENCE_LATER_CANNOT_SUPPORT_A_SAFE_BALANCE_SCOPE_NARROWING_REMAINS_AVAILABLE_UNDER_THE_SEPARATE_RELEASE_AND_SCOPE_GOVERNANCE
```

The recommendation is not a Founder decision and has no authority effect.

## Required Founder response binding

A Founder decision may be captured only after this exact decision surface is presented immediately before the response.

A valid response must unambiguously select one decision class, for example:

```text
FD004_DECISION=FD004_DECISION_A
```

or

```text
FD004_DECISION=FD004_DECISION_B
```

or

```text
FD004_DECISION=FD004_DECISION_C
```

A generic continuation instruction such as `go ahead`, standing alone without an immediately preceding exact decision surface, must not be retroactively interpreted as an FD-004 choice.

## Effect of a future valid Founder selection

A later canonical decision-capture record may change only:

```text
FD004_CURRENT_STATE=LOCKED_TO_SELECTED_PRODUCT_POSTURE
FOUNDER_POLICY_DECISION_CAPTURED=YES
```

It must continue to preserve:

```text
BENIGN_CASE_OVER_TRIAGE_NUMERIC_THRESHOLD=NEEDS_CLINICAL_STATISTICAL_EVIDENCE
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO_UNLESS_ALL_OTHER_PREREQUISITES_PASS
T1_A2=INCOMPLETE_UNTIL_REAL_EVIDENCE_AND_QUALIFIED_REVIEW_PASS
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## No downstream authority expansion

Neither this request nor a future FD-004 posture selection authorizes:

- model/source-weight acquisition beyond existing E002 authority;
- persistent conversion workspace provisioning;
- converter build reruns;
- model conversion or quantization;
- model loading or inference;
- benchmark payload access or tournament execution;
- device qualification;
- contamination assessment;
- A15 construction or activation;
- external reviewer outreach;
- personnel appointment or engagement;
- credentials, gated assets, PHI, or Private Gold;
- provider generation;
- training, adaptation, distillation, RL, or QAT;
- procurement, payment, or spend.

## Repository-level exit evidence for this request

This decision-request artifact is repository-level complete only when one exact head demonstrates:

```text
CHANGED_PATH_COUNT=1
DOCUMENTATION_ONLY=YES
FD004_OWNER_DECISION_SEPARATED_FROM_NUMERIC_THRESHOLD=YES
THREE_DECISION_CLASSES_PRESENTED=YES
ALL_OPTIONS_PRESERVE_NONCOMPENSABLE_SAFETY_GATES=YES
NO_CLINICAL_OR_STATISTICAL_VALUE_INVENTED=YES
NO_FOUNDER_DECISION_SELF_CAPTURED=YES
NO_EXECUTION_OR_ACCESS_AUTHORITY_CREATED=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
FRESH_EXACT_HEAD_REVIEW=MATERIAL_BLOCKER_NO
GUARDED_CANONICAL_MERGE=YES
POST_MERGE_MAIN_VERIFIED=YES
```

Canonical merge closes this **decision request only**. It does not select A/B/C and does not create a numeric threshold or any execution authority.