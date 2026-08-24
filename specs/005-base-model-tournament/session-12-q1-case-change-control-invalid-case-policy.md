# Session 12 Q1 — Case Change-Control and Invalid-Case Disposition Policy

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 12 Q1 only. It freezes the governance design for A12, the case change-control and invalid-case disposition prerequisite that must exist before Arabic selection-suite construction can be authorized. It does **not** create, edit, review, access, score, replace, or execute any case; implement A1; access Private Gold; access benchmark payloads; execute models; spend funds; or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION12_Q1_POLICY=PREDECLARED_IDENTITY_BOUND_RESULT_BLINDED_CASE_CHANGE_CONTROL_AND_INVALIDITY_DISPOSITION

A12_GOVERNANCE_DESIGN=FROZEN
A12_IMPLEMENTED_AND_EXECUTED=NO
A12_GATE_STATUS=BLOCKED_PENDING_CANONICAL_CHANGE_CONTROL_PROTOCOL_AND_AUDIT_SCHEMA

CLARIFICATION_SESSION_12=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_12_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

## 2. Governing distinction: invalid case versus candidate performance

A case may be invalid only because the case/evidence contract itself is objectively defective or no longer admissible under the frozen governance rules. Candidate behavior is not evidence that the case is invalid.

```text
CANDIDATE_WRONG_ANSWER_IMPLIES_CASE_INVALID=NO
CANDIDATE_LOW_SCORE_IMPLIES_CASE_INVALID=NO
CANDIDATE_REFUSAL_IMPLIES_CASE_INVALID=NO
CANDIDATE_TIMEOUT_IMPLIES_CASE_INVALID=NO
CANDIDATE_MALFORMED_OUTPUT_IMPLIES_CASE_INVALID=NO
MULTIPLE_CANDIDATES_FAILING_CASE_IMPLIES_CASE_INVALID=NO
PREFERRED_CANDIDATE_FAILURE_IMPLIES_CASE_INVALID=NO
```

Consistent with Session 9 Q3:

```text
CANDIDATE_OUTPUT_FAILURE_COUNTS_AS_STATISTICAL_ATTRITION=NO
CANDIDATE_OUTPUT_FAILURE_AUTHORIZES_CASE_REPLACEMENT=NO
CANDIDATE_SPECIFIC_SAMPLE_REPLENISHMENT=PROHIBITED
```

A case-invalidity decision must be based on the case content, provenance, rights/privacy state, scoring specification, pair validity, or predeclared design contract—not on whether a candidate performed well or poorly.

## 3. Closed invalidity-reason classes

The future A12 protocol must use a controlled invalidity taxonomy. At minimum it must represent:

```text
CLINICAL_FACTUAL_DEFECT
CLINICAL_AMBIGUITY_OR_MULTIPLE_DEFENSIBLE_ANSWERS
SCORING_OR_EXPECTED_BEHAVIOR_SPECIFICATION_DEFECT
ARABIC_ENGLISH_PAIR_SEMANTIC_EQUIVALENCE_FAILURE
ROLE_OR_USE_CONTEXT_MISMATCH
COVERAGE_ANCHOR_MISASSIGNMENT
DUPLICATE_OR_NONINDEPENDENT_ROOT_IDENTITY_DEFECT
RIGHTS_OR_LICENSE_BLOCK
PRIVACY_OR_PHI_BLOCK
PROVENANCE_OR_ARTIFACT_BINDING_BLOCK
PRIVATE_GOLD_OR_PROHIBITED_SOURCE_DERIVATION
CONTAMINATION_BLOCK_WHERE_APPLICABLE
CORRUPT_OR_MALFORMED_CASE_ARTIFACT
PREDECLARED_SCHEMA_OR_FORMAT_CONTRACT_VIOLATION
```

Unknown or convenience reason codes may not silently enter the protocol.

```text
INVALIDITY_REASON_OTHER_WITHOUT_RECORDED_JUSTIFICATION=PROHIBITED
INVALIDITY_REASON_MODEL_FOUND_IT_HARD=PROHIBITED
INVALIDITY_REASON_PREFERRED_CANDIDATE_FAILED=PROHIBITED
INVALIDITY_REASON_SCORE_WAS_SURPRISING=PROHIBITED
```

## 4. Case lifecycle states

The future governed workflow must distinguish case state from reviewer disposition.

Minimum lifecycle states:

```text
DRAFT
UNDER_REVIEW
ACCEPTED_UNFROZEN
FROZEN_ACTIVE
BLOCKED_INVALID
SUPERSEDED
RETIRED_WITHOUT_REPLACEMENT
```

Rules:

```text
DRAFT_OR_UNDER_REVIEW_MAY_ENTER_SELECTION_SCORING=NO
BLOCKED_INVALID_MAY_ENTER_SELECTION_SCORING=NO
SUPERSEDED_MAY_ENTER_NEW_SELECTION_SCORING=NO
RETIRED_WITHOUT_REPLACEMENT_MAY_ENTER_SELECTION_SCORING=NO

FROZEN_ACTIVE_REQUIRES_ALL_PREDECLARED_ACCEPTANCE_GATES=YES
```

This Q1 does not create the executable state machine; it freezes the required semantics only.

## 5. Material versus non-material change

A change is material if it may affect any scientific, clinical, scoring, provenance, or governance meaning, including:

```text
clinical facts
clinical plausibility
safety meaning
correct answer
expected behavior
scoring rule
rubric or adjudication criterion
Arabic-English semantic equivalence
language register or clinically relevant terminology
role or use-context interpretation
primary coverage anchor
statistical stratum assignment
root-task or pair relationship
rights state
privacy state
provenance or parentage
contamination disposition
```

For every material change:

```text
NEW_CONTENT_ARTIFACT_IDENTITY_REQUIRED=YES
NEW_CASE_OR_PAIR_VERSION_REQUIRED=YES
PRIOR_FINAL_REVIEW_ACCEPTANCE_AUTO_TRANSFER=NO
FRESH_REQUIRED_REVIEW_ON_NEW_IDENTITY=YES
PROVENANCE_CHANGE_RECORD_REQUIRED=YES
```

A change may be classified as non-material only when it is produced by a separately canonical deterministic normalization rule that is proven not to alter semantic content.

Examples may include predeclared whitespace or canonical serialization normalization. Human judgment that a textual edit is merely cosmetic is not sufficient to preserve identity unless the canonical rule explicitly permits it.

```text
FREE_TEXT_EDIT_PRESERVES_CONTENT_IDENTITY_BY_DEFAULT=NO
TRANSLATION_EDIT_PRESERVES_PAIR_IDENTITY_BY_DEFAULT=NO
PUNCTUATION_CHANGE_ALWAYS_NONMATERIAL=NO
```

## 6. Pre-freeze correction rule

Before a suite artifact is frozen and before candidate-result exposure, a draft or accepted-unfrozen case may be repaired through the governed authoring/review process.

```text
PRE_FREEZE_MATERIAL_REPAIR_ALLOWED_IN_PRINCIPLE=YES
PRE_FREEZE_MATERIAL_REPAIR_REQUIRES_NEW_CONTENT_IDENTITY=YES
PRE_FREEZE_MATERIAL_REPAIR_REQUIRES_FRESH_REQUIRED_REVIEW=YES
PRE_FREEZE_MATERIAL_REPAIR_MAY_BYPASS_RIGHTS_PRIVACY_PROVENANCE_RECHECK=NO
```

A blocked or rejected case may not be silently edited into an accepted case under the old identity.

## 7. Post-freeze, pre-result invalidity rule

If an objective defect is discovered after the suite is frozen but before any candidate result is exposed:

```text
SILENT_IN_PLACE_PATCH=PROHIBITED
SILENT_CASE_REMOVAL=PROHIBITED
SILENT_REPLACEMENT=PROHIBITED

AFFECTED_CASE_STATUS=BLOCKED_INVALID
INVALIDITY_RECORD_REQUIRED=YES
```

The process must then choose a governed disposition before any candidate evaluation begins:

```text
DISPOSITION_1=REPAIR_AS_NEW_IDENTITY
DISPOSITION_2=REPLACE_WITH_PREDECLARED_SLOT_COMPATIBLE_NEW_CASE
DISPOSITION_3=REVISE_STATISTICAL_ALLOCATION_OR_DESIGN_THROUGH_GOVERNED_REDESIGN
DISPOSITION_4=RETIRE_WITHOUT_REPLACEMENT_ONLY_IF_PREDECLARED_STATISTICAL_REQUIREMENTS_REMAIN_SATISFIED_AND_FORMALLY_RECONFIRMED
```

Every material disposition creates a new suite artifact identity.

```text
POST_FREEZE_CONTENT_SET_CHANGE_REQUIRES_NEW_SUITE_IDENTITY=YES
POST_FREEZE_STATISTICAL_RECHECK_REQUIRED=YES
POST_FREEZE_COVERAGE_RECHECK_REQUIRED=YES
```

## 8. Replacement rule

Replacement exists to preserve a scientifically predeclared design after an objectively invalid case is removed; it is not a mechanism to improve candidate results.

A replacement case must:

```text
SATISFY_SAME_PREDECLARED_STATISTICAL_STRATUM_SLOT=YES
SATISFY_SAME_REQUIRED_PRIMARY_COVERAGE_ANCHOR_SLOT=YES
SATISFY_PREDECLARED_ROLE_AND_USE_CONTEXT_REQUIREMENTS=YES
SATISFY_FULL_RIGHTS_PRIVACY_PROVENANCE_GATES=YES
SATISFY_FULL_AUTHORING_AND_REVIEW_GATES=YES
RECEIVE_NEW_CONTENT_AND_SUITE_IDENTITIES=YES
```

Replacement must not be chosen using candidate performance.

```text
CANDIDATE_SPECIFIC_REPLACEMENT=PROHIBITED
REPLACEMENT_CHOSEN_TO_HELP_PREFERRED_CANDIDATE=PROHIBITED
REPLACEMENT_CHOSEN_TO_REDUCE_OBSERVED_FAILURE_RATE=PROHIBITED
REPLACEMENT_CHOSEN_AFTER_COMPARING_CANDIDATE_RESULTS=PROHIBITED
```

If no replacement can satisfy the frozen slot without changing the statistical design, the process must stop for governed redesign rather than reducing or reallocating the requirement for convenience.

## 9. Post-result invalidity discovery

Discovery of a genuine case defect after any candidate-result exposure is a high-risk event because removal or repair can change comparative conclusions.

```text
POST_RESULT_INVALIDITY_DISCOVERY_MAY_BE_IGNORED=NO
POST_RESULT_SILENT_CASE_REMOVAL=PROHIBITED
POST_RESULT_SILENT_CASE_REPAIR=PROHIBITED
POST_RESULT_CANDIDATE_SPECIFIC_EXCLUSION=PROHIBITED
POST_RESULT_RESULT_AWARE_REPLACEMENT=PROHIBITED
```

The initial invalidity assessment must be isolated from comparative candidate performance as far as practicable and must adjudicate the case contract itself.

```text
POST_RESULT_INVALIDITY_REVIEW_MUST_USE_CASE_CONTRACT_EVIDENCE=YES
PREFERRED_CANDIDATE_IDENTITY_MAY_JUSTIFY_INVALIDITY=NO
CANDIDATE_SCORE_DIRECTION_MAY_JUSTIFY_INVALIDITY=NO
```

If objective invalidity is confirmed after results exist:

```text
AFFECTED_FROZEN_SUITE_IDENTITY_REMAINS_HISTORICAL_AND_REPRODUCIBLE=YES
NEW_CORRECTED_SUITE_IDENTITY_REQUIRED=YES
OLD_RESULTS_AUTOMATICALLY_TRANSFER_TO_NEW_SUITE=NO
```

For any selection evidence intended to support comparison on the corrected suite:

```text
FRESH_ALL_CANDIDATE_EVALUATION_ON_NEW_SUITE_REQUIRED=YES
SELECTIVE_RERUN_OF_ONLY_AFFECTED_OR_PREFERRED_CANDIDATE=PROHIBITED
```

No model or benchmark execution is authorized by this rule; it states the future scientific consequence only.

## 10. Candidate output failure is not an invalid-case event

When a candidate produces no valid output, refuses, times out, or produces a malformed response on an otherwise valid case:

```text
CASE_STATUS_REMAINS_VALID_UNLESS_SEPARATE_OBJECTIVE_CASE_DEFECT_PROVEN=YES
NO_REPLACEMENT_CASE_AUTHORIZED=YES
NO_SAMPLE_REPLENISHMENT_AUTHORIZED=YES
```

The metric-specific consequence for the candidate must be predeclared separately; it must not be converted into case attrition.

## 11. Duplicate and dependency discoveries

If two purported independent root tasks are later found to duplicate or materially derive from one root source:

```text
RAW_CASE_COUNT_MAY_NOT_CONTINUE_AS_IF_INDEPENDENT=YES
ROOT_IDENTITY_DEFECT_REQUIRES_STATISTICAL_RECHECK=YES
SILENT_RELABELLING_TO_PRESERVE_N=PROHIBITED
```

A corrected dependency representation may require a new suite identity even when the surface text is unchanged, because independence structure is part of the statistical evidence contract.

## 12. Rights, privacy, provenance, and contamination changes

A case that loses an admissible rights/privacy/provenance/contamination state must fail closed even if its clinical content is otherwise excellent.

```text
RIGHTS_STATE_BECOMES_CONDITIONAL_OR_UNRESOLVED=BLOCKED_PENDING_RESOLUTION
RIGHTS_STATE_BECOMES_INCOMPATIBLE=PROHIBITED_FOR_SELECTION_USE
PRIVACY_STATE_BECOMES_UNRESOLVED=BLOCKED
PRIVACY_STATE_BECOMES_RESTRICTED_OR_PHI=PROHIBITED_FOR_CURRENT_SELECTION_ROUTE
PROVENANCE_OR_BINDING_BECOMES_UNRESOLVED=BLOCKED
PRIVATE_GOLD_DERIVATION_DISCOVERED=PROHIBITED
CONTAMINATION_BLOCK_DISCOVERED=BLOCKED
```

No downstream success, reviewer preference, or candidate result can waive those blockers.

## 13. Change-control record identity

Every material repair, invalidity finding, supersession, retirement, or replacement must create an auditable change-control record binding the exact affected identities.

Minimum fields:

```text
change_control_protocol_id
change_control_protocol_version
change_control_protocol_canonical_sha256
change_record_id
change_type
invalidity_reason_code_or_explicit_not_applicable
old_content_or_pair_id
old_content_artifact_sha256
new_content_or_pair_id_or_explicit_none
new_content_artifact_sha256_or_explicit_none
old_suite_artifact_sha256_if_frozen
new_suite_artifact_sha256_or_explicit_none
statistical_slot_identity
coverage_anchor_identity
change_rationale
case_invalidity_review_evidence_id
rights_privacy_provenance_recheck_ids
clinical_review_recheck_ids
candidate_result_exposure_state
final_disposition
```

The record must not embed Private Gold content, PHI, candidate output payloads, or unnecessary personal reviewer information.

## 14. Candidate-result exposure state

The change record must distinguish at minimum:

```text
NO_CANDIDATE_RESULTS_EXIST_OR_EXPOSED
CANDIDATE_RESULTS_EXIST_BUT_INVALIDITY_REVIEW_FIREWALLED
COMPARATIVE_CANDIDATE_RESULTS_EXPOSED
```

This distinction is required because post-result change control has stronger anti-bias consequences than pre-result repair.

## 15. Suite identity and reproducibility

```text
FROZEN_SUITE_IS_IMMUTABLE_BY_IDENTITY=YES
MATERIAL_CASE_SET_CHANGE_CREATES_NEW_SUITE_IDENTITY=YES
MATERIAL_CASE_CONTENT_CHANGE_CREATES_NEW_SUITE_IDENTITY=YES
MATERIAL_STRATUM_OR_COVERAGE_CHANGE_CREATES_NEW_SUITE_IDENTITY=YES
MATERIAL_SCORING_CHANGE_CREATES_NEW_SUITE_IDENTITY=YES

HISTORICAL_SUITE_IDENTITY_MUST_REMAIN_REPRODUCIBLE=YES
HISTORICAL_RESULTS_MUST_REMAIN_BOUND_TO_HISTORICAL_SUITE_IDENTITY=YES
```

A corrected suite supersedes rather than rewrites the historical suite.

## 16. No optional stopping or result-conditioned case set

A12 must preserve Session 9 Q3 optional-stopping and candidate-neutrality rules.

```text
POST_RESULT_ADD_CASES_TO_RESCUE_CANDIDATE=PROHIBITED
POST_RESULT_DROP_CASES_TO_RESCUE_CANDIDATE=PROHIBITED
POST_RESULT_REWEIGHT_CASES_TO_RESCUE_CANDIDATE=PROHIBITED
POST_RESULT_EARLY_STOP_BECAUSE_PREFERRED_CANDIDATE_IS_AHEAD=PROHIBITED

FINAL_CASE_SET_MAY_DEPEND_ON_CANDIDATE_RESULTS=NO
```

## 17. A12 exit evidence required before construction readiness

A12 may become `PASS` only after a future canonical artifact proves:

```text
EXACT_CHANGE_CONTROL_PROTOCOL_CANONICAL=YES
PROTOCOL_VERSION_AND_SHA_BOUND=YES
CLOSED_INVALIDITY_REASON_VOCABULARY_DEFINED=YES
CASE_LIFECYCLE_STATE_SEMANTICS_DEFINED=YES
MATERIAL_CHANGE_IDENTITY_RULE_DEFINED=YES
PRE_FREEZE_REPAIR_RULE_DEFINED=YES
POST_FREEZE_PRE_RESULT_RULE_DEFINED=YES
POST_RESULT_INVALIDITY_RULE_DEFINED=YES
CANDIDATE_OUTPUT_FAILURE_NOT_ATTRITION_RULE_DEFINED=YES
REPLACEMENT_SLOT_COMPATIBILITY_RULE_DEFINED=YES
STATISTICAL_AND_COVERAGE_RECHECK_RULE_DEFINED=YES
CHANGE_CONTROL_RECORD_SCHEMA_DEFINED=YES
HISTORICAL_REPRODUCIBILITY_RULE_DEFINED=YES
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Q1 freezes the design only; it does not implement or execute the protocol.

## 18. Resulting DAG state

Q1 removes ambiguity about A12's design but does not make A12 operationally complete.

```text
A1_STATUS=BLOCKED_NOT_IMPLEMENTED
A2_STATUS=BLOCKED
A3_A4_ATOMIC_STATUS=BLOCKED
A5_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A6_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A7_STATUS=BLOCKED
A8_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A9_STATUS=BLOCKED
A10_STATUS=PARTIAL_ARCHITECTURE_ONLY
A11_STATUS=BLOCKED
A12_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A13_STATUS=BLOCKED
A14_STATUS=BLOCKED
A15_STATUS=BLOCKED

ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

## 19. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE
A12_PROTOCOL_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
