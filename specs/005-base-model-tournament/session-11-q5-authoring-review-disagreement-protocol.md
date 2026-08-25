# Session 11 Q5 — Authoring, Review, Acceptance, and Disagreement Protocol

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 11 Q5 only. It freezes the governance design for A8, the authoring/review/acceptance/disagreement protocol prerequisite that must exist before Arabic selection-suite construction can be authorized. It does not recruit reviewers, assign people, create or review cases, access Private Gold, implement A1, spend funds, execute models, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION11_Q5_POLICY=AUTHOR_SEPARATED_DUAL_INDEPENDENT_BILINGUAL_CLINICAL_REVIEW_WITH_FAIL_CLOSED_ADJUDICATION

A8_GOVERNANCE_DESIGN=FROZEN
A8_IMPLEMENTED_AND_EXECUTED=NO
A8_GATE_STATUS=BLOCKED_PENDING_CANONICAL_PROTOCOL_AND_REVIEWER_ASSIGNMENT_EVIDENCE

CLARIFICATION_SESSION_11=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_11_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

## 2. Separation of functions

The future workflow must distinguish at least:

```text
ROOT_CASE_AUTHOR
PAIR_ADAPTER_OR_PARALLEL_LANGUAGE_AUTHOR
CLINICAL_REVIEWER_1
CLINICAL_REVIEWER_2
ADJUDICATOR_IF_REQUIRED
RIGHTS_PRIVACY_PROVENANCE_REVIEW
PRIVATE_GOLD_TRUSTEE_OR_FINAL_AUDIT_ROLE
```

Rules:

```text
AUTHOR_MAY_SOLE_ACCEPT_OWN_CASE=NO
PAIR_ADAPTER_MAY_SOLE_ACCEPT_OWN_PAIR=NO
AUTHOR_MAY_SERVE_AS_FINAL_REVIEWER_FOR_OWN_CASE=NO
PAIR_ADAPTER_MAY_SERVE_AS_FINAL_REVIEWER_FOR_OWN_PAIR=NO
```

A person may hold multiple organizational roles generally, but the same content item must preserve the independence constraints above.

## 3. Minimum independent clinical review

Each candidate Arabic-English pair requires two independent clinical review dispositions before acceptance.

```text
MINIMUM_INDEPENDENT_FINAL_CLINICAL_REVIEWERS_PER_PAIR=2

REVIEWER_1_INDEPENDENT_OF_AUTHOR=YES
REVIEWER_2_INDEPENDENT_OF_AUTHOR=YES
REVIEWER_1_INDEPENDENT_OF_PAIR_ADAPTER=YES
REVIEWER_2_INDEPENDENT_OF_PAIR_ADAPTER=YES

AT_LEAST_ONE_REVIEWER_NATIVE_ARABIC_SPEAKING_CLINICAL_PROFESSIONAL=YES
BILINGUAL_CLINICAL_COMPARISON_COMPETENCE_REQUIRED_ACROSS_REVIEW_PAIR=YES
REGIONAL_OR_DIALECT_COMPETENCE_REQUIRED_WHERE_SEMANTICALLY_APPLICABLE=YES
```

Exact reviewer identities remain unresolved until A7.

## 4. Gold exposure firewall before assignment

Before assignment to authoring, pair adaptation, final review, or adjudication for selection content, the future process must bind a Private-Gold nonexposure disposition.

```text
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_SELECTION_AUTHOR=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_PAIR_ADAPTER=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_FINAL_REVIEWER=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_ADJUDICATOR=PROHIBITED

ROLE_TITLE_ALONE_PROVES_EXPOSURE=NO
ACTUAL_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_IS_CONTROLLING=YES
```

Public Gold protocol metadata does not count as case-content exposure.

## 5. Candidate-result firewall

```text
CANDIDATE_RESULTS_AVAILABLE_DURING_INITIAL_AUTHORING=NO
CANDIDATE_RESULTS_AVAILABLE_DURING_INITIAL_PAIR_REVIEW=NO
CANDIDATE_RESULTS_AVAILABLE_TO_ADJUDICATOR_BEFORE_SUITE_FREEZE=NO

CANDIDATE_ERROR_ANALYSIS_USED_TO_REWRITE_INITIAL_SUITE=PROHIBITED
PREFERRED_CANDIDATE_WEAKNESS_USED_TO_ADD_OR_REMOVE_CASES=PROHIBITED
```

The review process assesses case quality and pair validity, not candidate performance.

## 6. Required review dimensions

Each final reviewer must independently record a disposition for at least:

```text
CLINICAL_CORRECTNESS_OF_ROOT_TASK
CLINICAL_PLAUSIBILITY_AND_INTERNAL_COHERENCE
INTENDED_ROLE_AND_USE_CONTEXT_FIT
PRIMARY_COVERAGE_ANCHOR_FIT
ARABIC_ENGLISH_CLINICAL_SEMANTIC_EQUIVALENCE
SAFETY_RELEVANT_MEANING_EQUIVALENCE
NO_MATERIAL_INFORMATION_GAIN_OR_LOSS
REGISTER_AND_LANGUAGE_APPROPRIATENESS
LOCAL_MEDICATION_OR_CLINICAL_NOMENCLATURE_WHERE_APPLICABLE
RIGHTS_PRIVACY_PROVENANCE_PREREQUISITES_PRESENT
NO_PRIVATE_GOLD_DERIVATION_INDICATOR
SCORING_OR_EXPECTED_BEHAVIOR_SPECIFICATION_CLARITY_IF_APPLICABLE
```

Clinical review does not replace rights/privacy/provenance review; both must pass their own gates.

## 7. Reviewer disposition vocabulary

The future protocol must use a closed disposition vocabulary:

```text
ACCEPT
REVISE
REJECT
BLOCKED
```

Semantics:

```text
ACCEPT=reviewer finds no material issue within assigned review scope
REVISE=repairable material issue; content not accepted until revised and re-reviewed
REJECT=content unsuitable for governed suite under current design
BLOCKED=required evidence or prerequisite unavailable or unresolved
```

A `BLOCKED` item cannot be converted to `ACCEPT` by majority vote.

## 8. Pair acceptance rule

```text
FINAL_PAIR_ACCEPTANCE_REQUIRES_TWO_INDEPENDENT_ACCEPT_DISPOSITIONS=YES

ONE_ACCEPT_PLUS_ONE_REVISE=NOT_ACCEPTED
ONE_ACCEPT_PLUS_ONE_REJECT=NOT_ACCEPTED
ONE_ACCEPT_PLUS_ONE_BLOCKED=NOT_ACCEPTED
TWO_REVISE=NOT_ACCEPTED
ANY_REJECT=NOT_ACCEPTED_PENDING_GOVERNED_DISPOSITION
ANY_BLOCKED=BLOCKED
```

Revised content must receive fresh review on the revised identity; prior `ACCEPT` does not silently carry forward across a material revision.

## 9. Disagreement and adjudication protocol

If two independent reviewers disagree materially after one bounded clarification exchange, the item must not be resolved by author preference, founder preference, or simple averaging.

```text
INITIAL_MATERIAL_DISAGREEMENT=NOT_ACCEPTED
ONE_BOUNDED_REVIEWER_CLARIFICATION_EXCHANGE_ALLOWED=YES

UNRESOLVED_MATERIAL_DISAGREEMENT_REQUIRES_INDEPENDENT_ADJUDICATOR=YES
ADJUDICATOR_INDEPENDENT_OF_AUTHOR=YES
ADJUDICATOR_INDEPENDENT_OF_PAIR_ADAPTER=YES
ADJUDICATOR_PRIVATE_GOLD_CASE_EXPOSURE_PROHIBITED=YES
```

The adjudicator may choose only:

```text
ACCEPT_AFTER_REASONED_RECONCILIATION
REVISE
REJECT
BLOCKED
```

`ACCEPT_AFTER_REASONED_RECONCILIATION` requires a recorded rationale that addresses the material disagreement and binds the exact content identity reviewed.

```text
SIMPLE_MAJORITY_VOTE_WITHOUT_REASONED_RECONCILIATION=PROHIBITED
FOUNDER_TIE_BREAK_ON_CLINICAL_CORRECTNESS=PROHIBITED
AUTHOR_TIE_BREAK=PROHIBITED
```

## 10. Material versus non-material changes

Material changes include any change that may affect:

```text
clinical meaning
safety meaning
correct answer or expected behavior
Arabic-English semantic equivalence
role/use-context interpretation
coverage anchor
scoring semantics
rights/privacy/provenance state
```

For material changes:

```text
NEW_CONTENT_IDENTITY_REQUIRED=YES
FRESH_TWO_REVIEWER_ACCEPTANCE_REQUIRED=YES
PRIOR_REVIEW_DISPOSITIONS_AUTO_TRANSFER=NO
```

Non-material formatting corrections may use a separately defined deterministic normalization rule, but that rule must not alter semantic content.

## 11. Rejection and replacement rule

```text
REJECTED_CASE_MAY_BE_SILENTLY_REPLACED_AFTER_SAMPLE_ALLOCATION_FREEZE=NO

REPLACEMENT_CASE_MUST_SATISFY_SAME_PREDECLARED_STRATUM_SLOT=YES
REPLACEMENT_CASE_REQUIRES_FULL_RIGHTS_PRIVACY_PROVENANCE_AND_REVIEW=YES
REPLACEMENT_CHANGES_SUITE_ARTIFACT_IDENTITY=YES
```

If replacement would alter the frozen statistical allocation or coverage design, the process must stop for governed redesign rather than convenience substitution.

## 12. Required review record identity

Minimum future review record fields:

```text
review_protocol_id
review_protocol_version
review_protocol_canonical_sha256
content_or_pair_id
content_artifact_sha256
reviewer_reference
reviewer_assignment_evidence_id
gold_nonexposure_disposition
review_dimensions
review_disposition
material_findings
review_evidence_id
```

For adjudication:

```text
adjudication_record_id
adjudicator_reference
adjudicated_content_artifact_sha256
reviewer_disagreement_references
adjudication_disposition
reasoned_reconciliation
```

The open repository need not expose unnecessary personal information; identity-bound protected audit references are acceptable if governance can verify them.

## 13. A8 exit evidence required before construction readiness

A8 may become `PASS` only after a future canonical artifact proves:

```text
EXACT_REVIEW_PROTOCOL_CANONICAL=YES
PROTOCOL_VERSION_AND_SHA_BOUND=YES
CLOSED_DISPOSITION_VOCABULARY_DEFINED=YES
TWO_INDEPENDENT_REVIEWER_RULE_DEFINED=YES
GOLD_NONEXPOSURE_ASSIGNMENT_GATE_DEFINED=YES
CANDIDATE_RESULT_FIREWALL_DEFINED=YES
REVIEW_DIMENSIONS_DEFINED=YES
DISAGREEMENT_ADJUDICATION_PROTOCOL_DEFINED=YES
MATERIAL_CHANGE_REVIEW_INVALIDATION_DEFINED=YES
REVIEW_RECORD_IDENTITY_TEMPLATE_DEFINED=YES
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Q5 freezes the design only; it does not execute reviewer assignments or reviews.

## 14. Session 11 closeout state

Q3, Q4, and Q5 freeze governance designs for A5, A6, and A8. They do not make the preconstruction gate ready because implementation/acceptance evidence and many other DAG nodes remain unresolved.

```text
A5_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A6_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A8_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY

A1_STATUS=BLOCKED_NOT_IMPLEMENTED
A2_STATUS=BLOCKED
A3_A4_ATOMIC_STATUS=BLOCKED
A7_STATUS=BLOCKED
A9_STATUS=BLOCKED
A10_STATUS=PARTIAL_ARCHITECTURE_ONLY
A11_STATUS=BLOCKED
A12_STATUS=BLOCKED
A13_STATUS=BLOCKED
A14_STATUS=BLOCKED
A15_STATUS=BLOCKED

ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

## 15. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE
A5_INSTRUMENT_EXECUTION_AUTHORITY=NONE
A6_POLICY_EXECUTION_AUTHORITY=NONE
A8_REVIEW_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
