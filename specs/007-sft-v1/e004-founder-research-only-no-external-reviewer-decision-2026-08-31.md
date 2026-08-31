# E004 Founder Research-Only No-External-Reviewer Decision — 2026-08-31

**Spec:** 007 SFT V1  
**Canonical base:** `4f428dc2c6b7282cdfa5b158d3834625686a8ff0`  
**Artifact class:** Founder policy decision and bounded scientific-governance amendment  
**Decision owner:** Founder  
**Decision state:** SELECTED_PENDING_CANONICAL_MERGE  
**Decision ID:** `FD-007-RESEARCH-ONLY-NO-EXTERNAL-REVIEWER`  
**Authority effect before canonical merge:** NONE  
**External reviewer outreach performed:** NO  
**Scientific review performed:** NO  
**Model/benchmark/device execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Founder direction and provenance

This decision records the Founder's explicit post-canonical direction in the trusted first-party ChatGPT project conversation on 2026-08-31:

```text
FOUNDER_DIRECTION_CONTENT=i do not want and need revewr , where we at in the project ?
FOUNDER_CONTINUATION_CONTENT=go ahead do not stop until finish the project , you have all approvals fro me
FOUNDER_DIRECTION_SOURCE=TRUSTED_FIRST_PARTY_CHATGPT_PROJECT_CONVERSATION
FOUNDER_DIRECTION_CAPTURE_TIME=2026-08-31T08:28:00+03:00
FOUNDER_DIRECTION_ORDERING=AFTER_PR139_AND_PR140_CANONICAL_MERGES
```

The direction is interpreted narrowly and prospectively:

```text
FOUNDER_REVIEWER_POLICY=NO_EXTERNAL_CLINICAL_OR_STATISTICAL_REVIEWER_PATH_FOR_CURRENT_RESEARCH_PROGRAM
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
EXTERNAL_REVIEWER_ENGAGEMENT_EXECUTION=PROHIBITED
```

This is not `E004_OUTREACH_DECISION_B`. PR #117 remains controlling for outreach prohibition. The PR #139 decision surface remains historical evidence and is not used to infer contact authority.

## 2. Current rule being amended

The current Spec 002 / Spec 005 / E004 path requires population-level clinical/statistical thresholds to remain non-passable until identity-bound clinical/statistical evidence and the required review authority exist. The current A2 governance profile further requires distinct clinical-domain review, statistical-method review, and canonical governance adoption before such a numeric policy may be frozen and represented as scientifically accepted.

Those rules remain valid for any clinical qualification, patient-facing claim, release claim, or population-level threshold PASS.

The present project path, however, makes those external-review dispositions a prerequisite to any later research adaptation. That conflicts with the Founder's explicit decision not to use external reviewers for the current research program.

## 3. Replacement: bounded research-only adaptation lane

After this decision is canonically merged, Spec 007 SHALL distinguish two evidence lanes.

### 3.1 Research-only adaptation lane

The current program selects the following lane:

```text
CURRENT_SPEC007_EVIDENCE_LANE=RESEARCH_ONLY_ADAPTATION
EXTERNAL_CLINICAL_REVIEW_REQUIRED_FOR_THIS_LANE=NO
EXTERNAL_STATISTICAL_REVIEW_REQUIRED_FOR_THIS_LANE=NO
POPULATION_CLINICAL_THRESHOLD_PASS_REQUIRED_FOR_THIS_LANE=NO
CLINICAL_VALIDATION_CLAIMS_AUTHORIZED=NO
PATIENT_BENEFIT_CLAIMS_AUTHORIZED=NO
CLINICAL_SUPERIORITY_CLAIMS_AUTHORIZED=NO
CLINICAL_GRADE_CLAIMS_AUTHORIZED=NO
DEPLOYMENT_READINESS_CLAIMS_AUTHORIZED=NO
RELEASE_READINESS_CLAIMS_AUTHORIZED=NO
```

Research-only adaptation may become eligible only after all separately required non-reviewer prerequisites are proven, including at minimum:

```text
FROZEN_EVALUATION_PROTOCOL_BEFORE_OPTIMIZATION=REQUIRED
IDENTITY_BOUND_POLICY_AND_SENTINEL_HARD_GATES=REQUIRED_PASS
ANY_OBSERVED_APPLICABLE_SAFETY_FAIL=DISQUALIFY
PROVENANCE_LICENSE_AND_CONTENT_IDENTITY=REQUIRED
HOLDOUT_AND_PRIVATE_GOLD_QUARANTINE=REQUIRED
CONTAMINATION_CONTROL=REQUIRED
CAPABILITY_PRESERVATION_PROTOCOL=REQUIRED
EXACT_MODEL_DATA_CONFIG_ENVIRONMENT_BINDING=REQUIRED
RESOURCE_ACCESS_AND_FINANCE_PREFLIGHT=REQUIRED
SEPARATE_MODEL_EXECUTION_AUTHORITY=REQUIRED
SEPARATE_TRAINING_AUTHORITY=REQUIRED
```

No unresolved population-level clinical threshold is converted into PASS. For this lane only, a `PENDING_CLINICAL_EVIDENCE` or `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE` population threshold remains explicitly unresolved and is excluded from the **research-only adaptation eligibility decision**, while every applicable frozen policy/sentinel hard gate remains mandatory and noncompensable.

```text
PENDING_POPULATION_CLINICAL_THRESHOLDS_RECLASSIFIED_AS_PASS=NO
PENDING_POPULATION_CLINICAL_THRESHOLDS_STATUS=INSUFFICIENT_EVIDENCE_FOR_CLINICAL_QUALIFICATION
PENDING_POPULATION_CLINICAL_THRESHOLDS_USED_TO_CLAIM_SAFETY=NO
PENDING_POPULATION_CLINICAL_THRESHOLDS_USED_TO_CLAIM_CLINICAL_SUPERIORITY=NO
FROZEN_SENTINEL_ZERO_VIOLATION_GATES_WAIVED=NO
DETERMINISTIC_SAFETY_GATES_WAIVED=NO
```

This replacement narrows what a successful research run means. It does not weaken the pass conditions for a clinical qualification.

### 3.2 Clinical-qualification lane

The existing human clinical/statistical evidence architecture remains available only as a separate future lane:

```text
CLINICAL_QUALIFICATION_LANE_CURRENTLY_SELECTED=NO
CLINICAL_QUALIFICATION_REVIEW_REQUIREMENTS_PRESERVED=YES
SPEC002_PENDING_CLINICAL_THRESHOLD_SEMANTICS_PRESERVED=YES
SPEC005_Q4_CLINICAL_STATISTICAL_REVIEW_ARCHITECTURE_PRESERVED_FOR_CLINICAL_QUALIFICATION=YES
E004_A2_REVIEW_PROFILE_PRESERVED_FOR_CLINICAL_QUALIFICATION=YES
```

If a later specification or release seeks population-level clinical threshold PASS, patient-facing benefit, clinical-grade, clinical superiority, deployment readiness, or equivalent claims, the clinical-qualification evidence path must be reopened or replaced by a separately justified and canonically reviewed scientific method before those claims become eligible.

## 4. Safety semantics remain fail closed

This decision does not permit averages to compensate for critical failures and does not redefine deterministic safety truth.

For the research-only lane:

1. every applicable frozen `FROZEN_POLICY_ZERO_TOLERANCE` gate remains mandatory;
2. every applicable frozen `FROZEN_SENTINEL_ZERO_VIOLATIONS` gate remains mandatory;
3. any observed applicable safety `FAIL` disqualifies the exact candidate/run;
4. unresolved or malformed sentinel/policy evidence blocks the research-only eligibility decision;
5. population clinical rates without justified thresholds remain descriptive/unqualified evidence only and cannot be represented as clinical PASS;
6. public benchmark performance cannot compensate for a safety failure or create a clinical claim.

The research-only lane is therefore not a shortcut from missing clinical evidence to clinical safety. It is a narrower research claim class.

## 5. Evaluation-before-optimization remains unchanged

No training run may define its own success criteria.

Before any separately authorized research-only optimization run, the exact evaluation protocol must be frozen and identity-bound. It must state which metrics are:

- mandatory research hard gates;
- frozen sentinel/policy gates;
- descriptive development metrics;
- unresolved population clinical metrics that are prohibited from clinical PASS interpretation;
- protected final evidence excluded from optimization and model/checkpoint selection.

A post-result reclassification from descriptive/unresolved to PASS is prohibited.

## 6. Scope and claim boundary

A candidate produced under this lane may be called only a research candidate or research-adapted candidate unless later evidence supports a stronger term.

The following representations are prohibited from this lane alone:

```text
SAFE_FOR_PATIENT_USE
CLINICALLY_VALIDATED
CLINICAL_GRADE
CLINICALLY_SUPERIOR
DEPLOYMENT_READY
RELEASE_READY
REAL_WORLD_PATIENT_BENEFIT_PROVEN
POPULATION_ERROR_RATE_ACCEPTABLE
HUMAN_AI_BENEFIT_PROVEN
```

Spec 015 Human Evaluation and Spec 017 Release Review & Paper are not satisfied or bypassed by this decision.

## 7. Authority boundaries unchanged

This decision changes the reviewer dependency and claim class only. It does not itself authorize any execution.

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_INFERENCE_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=UNCHANGED_SEPARATELY_GATED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The existing E004 runtime-evidence target allowance and its connected-transport blocker are unchanged. This decision does not authorize reruns, alternate triggers, local substitutes, or any workflow-dispatch workaround.

## 8. Effect on E004 and E005

Canonical merge of this decision removes only this prerequisite from the current research-only lane:

```text
E004_RESEARCH_ONLY_LANE_REQUIRES_EXTERNAL_CLINICAL_REVIEW=NO
E004_RESEARCH_ONLY_LANE_REQUIRES_EXTERNAL_STATISTICAL_REVIEW=NO
```

It does not close E004. All other real E004 blockers remain blockers until separately proven or canonically changed.

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

E005 may not begin until the revised research-only E004 prerequisite matrix is canonically reconciled and all remaining mandatory research-only prerequisites are actually PASS.

## 9. Prior evidence and comparability

Historical evidence remains immutable.

```text
PR116_HISTORICAL_PRESCREEN_RECORD_RETAINED=YES
PR117_NO_OUTREACH_RECORD_RETAINED=YES
PR139_OUTREACH_DECISION_SURFACE_RETAINED=YES
PR140_V7_RECONCILIATION_RETAINED=YES
PRIOR_A2_REVIEW_GOVERNANCE_RECORD_RETAINED=YES
PRIOR_RESULTS_RECLASSIFIED=NO
```

Research-only results collected under this policy are not automatically comparable to a future clinically qualified lane because the qualification claim class differs. Any later clinical-qualification transition must bind the exact prior result identities and state explicitly which results remain scientifically comparable.

## 10. Required canonical follow-up

After this record becomes canonical, the next bounded repository unit SHALL reconcile the E004 prerequisite matrix, task ledger, and Spec registry to the research-only lane without marking any unresolved execution/scientific/resource gate PASS.

That reconciliation must preserve:

```text
NO_EXTERNAL_REVIEWER_OUTREACH=YES
NO_CLINICAL_PASS_FROM_MISSING_REVIEW=YES
NO_TRAINING_AUTHORITY_FROM_THIS_DECISION=YES
NO_EXECUTION_AUTHORITY_FROM_THIS_DECISION=YES
NO_SPEND_AUTHORITY_FROM_THIS_DECISION=YES
NO_PRIVATE_GOLD_OR_PHI_AUTHORITY=YES
NO_FALSE_E004_CLOSE=YES
NO_FALSE_E005_ENTRY=YES
```

## Exit evidence for this decision record

This decision record is ready for canonical merge only if independent repository review confirms that it:

1. faithfully captures the Founder's explicit no-external-reviewer direction;
2. preserves PR #117's no-outreach boundary;
3. creates no clinical/statistical review evidence or PASS by assertion;
4. preserves frozen deterministic/sentinel safety hard gates;
5. preserves evaluation-before-optimization, provenance, quarantine, contamination, reproducibility, and capability-preservation requirements;
6. narrows claims to research-only rather than weakening clinical qualification;
7. creates no model, benchmark, conversion, training, credential, protected-data, procurement, payment, or spend authority;
8. leaves E004 incomplete and E005 not reached pending a separate canonical prerequisite reconciliation.
