# E004 FD-004 Over-Triage Founder Decision — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Decision owner:** Founder  
**Decision register item:** `FD-004 — Acceptable over-triage policy`  
**Decision request:** `specs/007-sft-v1/e004-fd004-over-triage-founder-decision-request-2026-08-28.md`  
**Decision request canonical merge:** `45ae41b384f90f2da21c4bce557472f2c68869a9`  
**Decision request blob:** `d1395996041d9b64ac093bc29df0ac510b7ce600`  
**Founder selection date:** 2026-08-28  
**Founder selection:** `FD004_DECISION_B`  
**Artifact class:** Founder decision capture only  
**Numeric threshold freeze effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**External reviewer outreach authority:** NONE  
**Credential/gated/private asset authority:** NONE  
**Current authorized spend:** USD 0

## Founder selection binding

The exact three-class FD-004 decision surface was presented to the Founder before the valid response. The Founder then supplied the unambiguous selection:

```text
FD004_DECISION=FD004_DECISION_B
```

This captures only the product/ethics posture defined by Decision B. It does not infer any separate gated authority from the Founder's general continuation authorization.

## Locked product posture

```text
FD004_CURRENT_STATE=LOCKED_TO_SELECTED_PRODUCT_POSTURE
FOUNDER_POLICY_DECISION_CAPTURED=YES
FD004_DECISION=FD004_DECISION_B
FOUNDER_POLICY_POSTURE=BALANCED_BURDEN_WITH_NONCOMPENSABLE_SAFETY
PRODUCT_PRIORITY=REDUCE_UNNECESSARY_ESCALATION_SUBJECT_TO_NONCOMPENSABLE_SAFETY_GATES
BENIGN_OVER_TRIAGE_BURDEN=MUST_BE_MEASURED_AND_BOUNDED
NUMERIC_OVER_TRIAGE_CEILING=REQUIRES_CLINICAL_STATISTICAL_EVIDENCE
SAFETY_GATE_RELAXATION=PROHIBITED
```

Interpretation: commandMed should reduce unnecessary escalation only after frozen safety hard gates are satisfied. Convenience, engagement, average utility, or a lower benign over-triage burden may not compensate for a safety-gate failure. Qualified clinical/statistical governance must still establish any numeric ceiling, uncertainty method, intended-use framing, and sample-size/power design.

## Preserved clinical/statistical boundary

This Founder decision resolves an owner/product posture only. It does not establish or freeze a clinical or statistical value.

```text
BENIGN_CASE_OVER_TRIAGE_NUMERIC_THRESHOLD=NEEDS_CLINICAL_STATISTICAL_EVIDENCE
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO_UNLESS_ALL_OTHER_PREREQUISITES_PASS
T1_A2=INCOMPLETE_UNTIL_REAL_EVIDENCE_AND_QUALIFIED_REVIEW_PASS
QUALIFIED_CLINICAL_REVIEW=REQUIRED
QUALIFIED_STATISTICAL_REVIEW=REQUIRED
NUMERIC_THRESHOLD_SELECTED=NO
A2_PASS_DISPOSITION_CREATED=NO
```

The constitution's safety-hard-gate rule remains controlling. No safety-critical threshold may be inferred from this product decision.

## Preserved E004/E005 lifecycle state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_TOURNAMENT_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

FD-004 selection does not complete the frozen model tournament, create a winner, or advance E005.

## No downstream authority expansion

This decision does not authorize or perform any of the following:

- model/source-weight acquisition beyond existing E002 authority;
- persistent conversion workspace provisioning;
- converter or quantizer build reruns;
- model conversion or quantization;
- model loading or inference;
- benchmark payload access or tournament execution;
- device qualification;
- contamination assessment;
- A15 construction or activation;
- external scientific/governance reviewer outreach;
- personnel appointment or engagement;
- credentials, gated assets, PHI, or Private Gold;
- provider generation;
- training, adaptation, distillation, DPO, RL, GRPO, or QAT;
- procurement, payment, or spend.

The resulting authority state remains:

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Canonicalization requirements

This decision becomes canonical only after exact-head independent repository review reports no material blocker, a guarded merge lands on canonical `main`, and post-merge `main` is re-verified.

Until then:

```text
FD004_DECISION_CAPTURE_BRANCH_STATE=PROPOSED_FOR_CANONICALIZATION
CANONICAL_FD004_STATE=FOUNDER_REQUIRED_UNTIL_MERGE
```
