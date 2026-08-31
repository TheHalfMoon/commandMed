# E004 Founder Research-Only No-External-Reviewer Decision — 2026-08-31

**Spec:** 007 SFT V1  
**Canonical base:** `4f428dc2c6b7282cdfa5b158d3834625686a8ff0`  
**Artifact class:** Founder policy decision and successor-governance direction  
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

## 2. Current rule remains operative until a successor is canonical

Canonical Spec 002 currently applies its fail-closed safety policy before a candidate model can be promoted, selected for a later stage, adapted, or released. Every applicable `NO_PASS_UNTIL_FROZEN` gate remains `INSUFFICIENT_EVIDENCE` until its threshold is validly frozen, and only an all-required-gates PASS set qualifies the exact declared scope.

Spec 005 Session 9 Q4 and the current E004 A2 governance profile require clinical-domain review, statistical-method review, and canonical governance adoption before population-level clinical/statistical thresholds can be represented as scientifically accepted.

The Founder has selected a no-external-reviewer direction for the current research program. That direction does **not** by itself waive or supersede the current Spec 002 adaptation gate.

```text
CURRENT_SPEC002_ADAPTATION_GATE_SUPERSEDED_BY_THIS_DECISION=NO
PENDING_POPULATION_CLINICAL_GATES_RECLASSIFIED_AS_PASS=NO
PENDING_POPULATION_CLINICAL_GATES_EXCLUDED_FROM_CURRENT_AGGREGATION=NO
CURRENT_RESEARCH_ADAPTATION_ELIGIBLE_FROM_THIS_DECISION=NO
```

Until a separately justified successor safety-policy contract is canonically reviewed and merged, existing Spec 002 semantics continue to block adaptation when an applicable pending clinical gate is `INSUFFICIENT_EVIDENCE`.

## 3. Selected direction: bounded research-only successor lane

After this decision is canonically merged, the repository SHALL specify a successor safety-policy lane for research-only model development that does not depend on external clinical/statistical reviewers and does not manufacture clinical qualification.

The selected target direction is:

```text
TARGET_SPEC007_EVIDENCE_LANE=RESEARCH_ONLY_ADAPTATION
EXTERNAL_CLINICAL_REVIEW_TARGET_REQUIREMENT=NO
EXTERNAL_STATISTICAL_REVIEW_TARGET_REQUIREMENT=NO
CLINICAL_VALIDATION_CLAIMS_AUTHORIZED=NO
PATIENT_BENEFIT_CLAIMS_AUTHORIZED=NO
CLINICAL_SUPERIORITY_CLAIMS_AUTHORIZED=NO
CLINICAL_GRADE_CLAIMS_AUTHORIZED=NO
DEPLOYMENT_READINESS_CLAIMS_AUTHORIZED=NO
RELEASE_READINESS_CLAIMS_AUTHORIZED=NO
SUCCESSOR_POLICY_REQUIRED_BEFORE_RESEARCH_ADAPTATION=YES
```

This target direction is not executable authority. The successor policy must be a separate identity-bound, canonically reviewed governance unit before it can change any evaluator, threshold applicability, E004 prerequisite, or adaptation eligibility result.

## 4. Mandatory successor-policy constraints

The successor policy must remain consistent with the constitution and must not use scope relabeling to hide a claimed capability.

It SHALL explicitly define a narrower non-clinical research scope and prove which capabilities are genuinely outside that exact scope before any corresponding population clinical gate can become non-applicable to that scope.

At minimum, the successor specification must preserve:

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

It must also preserve the following fail-closed boundaries:

```text
PENDING_POPULATION_CLINICAL_THRESHOLDS_RECLASSIFIED_AS_PASS=NO
PENDING_POPULATION_CLINICAL_THRESHOLDS_USED_TO_CLAIM_SAFETY=NO
PENDING_POPULATION_CLINICAL_THRESHOLDS_USED_TO_CLAIM_CLINICAL_SUPERIORITY=NO
FROZEN_SENTINEL_ZERO_VIOLATION_GATES_WAIVED=NO
DETERMINISTIC_SAFETY_GATES_WAIVED=NO
CLAIMED_CAPABILITY_HIDDEN_BY_SCOPE_RELABELING=PROHIBITED
PATIENT_OR_CAREGIVER_SAFETY_GATE_SUPPRESSION=PROHIBITED
SYSTEM_LEVEL_PASS_FROM_COMPONENT_SCOPE=PROHIBITED
```

If the successor cannot define a truthful narrower scope without suppressing a claimed capability, the affected pending clinical gate remains applicable and adaptation remains blocked.

## 5. Clinical-qualification lane remains unchanged

The existing human clinical/statistical evidence architecture remains controlling for any clinical qualification:

```text
CLINICAL_QUALIFICATION_LANE_CURRENTLY_SELECTED=NO
CLINICAL_QUALIFICATION_REVIEW_REQUIREMENTS_PRESERVED=YES
SPEC002_PENDING_CLINICAL_THRESHOLD_SEMANTICS_PRESERVED=YES
SPEC005_Q4_CLINICAL_STATISTICAL_REVIEW_ARCHITECTURE_PRESERVED_FOR_CLINICAL_QUALIFICATION=YES
E004_A2_REVIEW_PROFILE_PRESERVED_FOR_CLINICAL_QUALIFICATION=YES
```

If a later specification or release seeks population-level clinical threshold PASS, patient-facing benefit, clinical-grade, clinical superiority, deployment readiness, or equivalent claims, the clinical-qualification evidence path must be reopened or replaced by a separately justified and canonically reviewed scientific method before those claims become eligible.

## 6. Safety semantics remain fail closed

This decision does not permit averages to compensate for critical failures and does not redefine deterministic safety truth.

Under the current policy and any future compliant successor:

1. every applicable frozen `FROZEN_POLICY_ZERO_TOLERANCE` gate remains mandatory;
2. every applicable frozen `FROZEN_SENTINEL_ZERO_VIOLATIONS` gate remains mandatory;
3. any observed applicable safety `FAIL` disqualifies the exact candidate/run;
4. unresolved or malformed mandatory safety evidence cannot produce research eligibility;
5. population clinical rates without justified thresholds cannot be represented as clinical PASS;
6. public benchmark performance cannot compensate for a safety failure or create a clinical claim.

The target research-only lane is not a shortcut from missing clinical evidence to clinical safety. It is a narrower future research claim class whose exact scope and evaluator semantics must be specified and independently reviewed before use.

## 7. Evaluation-before-optimization remains unchanged

No training run may define its own success criteria.

Before any separately authorized research-only optimization run, the exact evaluation protocol must be frozen and identity-bound. A future successor must state which metrics are:

- mandatory research hard gates;
- frozen sentinel/policy gates;
- descriptive development metrics;
- unresolved population clinical metrics that remain prohibited from clinical PASS interpretation;
- protected final evidence excluded from optimization and model/checkpoint selection.

A post-result reclassification from descriptive/unresolved to PASS is prohibited.

## 8. Scope and claim boundary

A candidate eventually produced under a compliant research-only successor may be called only a research candidate or research-adapted candidate unless later evidence supports a stronger term.

The following representations remain prohibited from this decision and from the target research-only lane alone:

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

## 9. Authority boundaries unchanged

This decision selects governance direction only. It does not authorize any model/data/runtime execution.

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

## 10. Effect on E004 and E005

Canonical merge of this decision records that external-reviewer outreach is not the chosen remediation path. It does **not** remove any current Spec 002 gate from E004 and does not close E004.

```text
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
CURRENT_E004_PREREQUISITE_MATRIX_CHANGED_BY_THIS_DECISION=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

E005 may not begin until a compliant successor policy is canonical, the E004 prerequisite matrix is separately reconciled to that successor, and all remaining mandatory prerequisites are actually PASS.

## 11. Prior evidence and comparability

Historical evidence remains immutable.

```text
PR116_HISTORICAL_PRESCREEN_RECORD_RETAINED=YES
PR117_NO_OUTREACH_RECORD_RETAINED=YES
PR139_OUTREACH_DECISION_SURFACE_RETAINED=YES
PR140_V7_RECONCILIATION_RETAINED=YES
PRIOR_A2_REVIEW_GOVERNANCE_RECORD_RETAINED=YES
PRIOR_RESULTS_RECLASSIFIED=NO
```

Any future research-only results collected under a successor policy are not automatically comparable to a clinically qualified lane because the qualification claim class differs. The successor must state comparability rules explicitly before any result is generated.

## 12. Independent review repair history

The first PR #141 candidate, exact head `0d1b7db57e1bb8e6c5f7e3d14b690b4de4520ed2`, was independently reviewed by CodeRabbit and rejected with:

```text
MATERIAL_BLOCKER=YES
FINDING=PROPOSED_RESEARCH_ONLY_ADAPTATION_ELIGIBILITY_CONFLICTED_WITH_CURRENT_SPEC002_FAIL_CLOSED_AGGREGATION
```

That finding is accepted. This repaired version removes the parallel adaptation-eligibility path. Current Spec 002 remains fully operative until a separately justified successor is canonical.

## 13. Required canonical follow-up

After this record becomes canonical, the next bounded repository unit SHALL specify the successor research-only safety-policy contract. That successor must:

1. identify the exact non-clinical research scope;
2. identify every capability claimed by that scope;
3. map every Spec 002 gate to applicable or genuinely non-applicable with rationale;
4. preserve every applicable frozen policy/sentinel hard gate;
5. leave unresolved population clinical thresholds non-passable for clinical qualification;
6. define research-only eligibility without suppressing gates for claimed capabilities;
7. preserve no-outreach and zero-spend boundaries;
8. create no execution/training authority by specification alone;
9. undergo fresh independent repository review before canonical merge.

Only after that successor is canonical may a separate E004 reconciliation change the prerequisite matrix.

## Exit evidence for this decision record

This decision record is ready for canonical merge only if fresh exact-head independent repository review confirms that it:

1. faithfully captures the Founder's explicit no-external-reviewer direction;
2. preserves PR #117's no-outreach boundary;
3. preserves current Spec 002 adaptation blocking until a successor is canonical;
4. creates no clinical/statistical review evidence or PASS by assertion;
5. preserves frozen deterministic/sentinel safety hard gates;
6. preserves evaluation-before-optimization, provenance, quarantine, contamination, reproducibility, and capability-preservation requirements;
7. narrows the future target claim class to research-only rather than weakening current clinical qualification;
8. creates no model, benchmark, conversion, training, credential, protected-data, procurement, payment, or spend authority;
9. leaves E004 incomplete and E005 not reached pending a separately reviewed successor and later prerequisite reconciliation.
