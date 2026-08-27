# E004 Preconstruction Governance Foundation Candidate Pack — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `89c6e177c77806529401a0e788991e5443b68bbd`  
**Related Spec 005 DAG nodes:** `G1/A5`, `G2/A6`, `G3/A8`, `G4/A12`  
**Artifact class:** operational-policy candidate extraction from already-frozen architecture  
**Authority effect:** NONE  
**Validator input:** NO  
**Case/content construction:** NO  
**Personnel assignment:** NO  
**Acceptance/signature evidence:** NO

This packet performs only the parallel governance work that the current E004 frontier permits without case construction or external execution. It extracts reviewable operational candidate text from the already-frozen Spec 005 Session 11/12 governance decisions. It does **not** mutate closed Spec 005 code/data/contracts, create a new schema, execute an agreement, appoint a contributor/reviewer, authorize construction, or claim that any A5/A6/A8/A12 gate has passed.

```text
G1_A5_CONTROL_PLANE=AVAILABLE
G1_A5_FROZEN_DESIGN=AVAILABLE
G1_A5_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G1_A5_REAL_GATE_PASS=NO

G2_A6_CONTROL_PLANE=AVAILABLE
G2_A6_FROZEN_DESIGN=AVAILABLE
G2_A6_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G2_A6_REAL_GATE_PASS=NO

G3_A8_CONTROL_PLANE=AVAILABLE
G3_A8_FROZEN_DESIGN=AVAILABLE
G3_A8_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G3_A8_REAL_GATE_PASS=NO

G4_A12_CONTROL_PLANE=AVAILABLE
G4_A12_FROZEN_DESIGN=AVAILABLE
G4_A12_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G4_A12_REAL_GATE_PASS=NO

ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_CASE_CONSTRUCTION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
PAID_CONTRIBUTOR_OR_REVIEWER_ENGAGEMENT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=BLOCKED_PREFLIGHT_UNDER_E003
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Why this packet exists

The frozen preconstruction DAG allows `G1`, `G2`, `G3`, and `G4` to be clarified in parallel with the A2 scientific path. Historical clarification records deliberately stopped at design and state that exact operational artifacts/acceptance evidence remain unresolved.

This packet reduces that gap only by preparing bounded candidate operational wording for later independent governance/legal/clinical review. It does not claim:

```text
EXACT_CANONICAL_INSTRUMENT_TEXT_ADOPTED=NO
EXACT_CANONICAL_POLICY_SHA256_BOUND=NO
CONTRIBUTOR_ACCEPTANCE_EVIDENCE_EXISTS=NO
AUTHOR_PRIVACY_ATTESTATION_EXISTS=NO
REVIEWER_ASSIGNMENT_EVIDENCE_EXISTS=NO
CASE_CHANGE_CONTROL_RECORD_EXISTS=NO
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=NO
```

A code-review bot or repository agent cannot satisfy those real-world or governance facts.

## 2. Source decisions preserved

This packet is subordinate to and must not reinterpret:

```text
A5_DESIGN=
  specs/005-base-model-tournament/session-11-q3-contributor-content-rights-instrument-design.md

A6_DESIGN=
  specs/005-base-model-tournament/session-11-q4-non-phi-authoring-policy-attestation.md

A8_DESIGN=
  specs/005-base-model-tournament/session-11-q5-authoring-review-disagreement-protocol.md

A12_DESIGN=
  specs/005-base-model-tournament/session-12-q1-case-change-control-invalid-case-policy.md

PRECONSTRUCTION_DAG=
  data/spec005/preconstruction_contract.json

VALIDATION_SURFACE=
  src/commandmed/spec005/preconstruction.py
```

If candidate wording below conflicts with those frozen sources, the frozen source wins and this candidate must be repaired rather than silently changing semantics.

## 3. Identity discipline

Candidate IDs below are review handles only.

```text
CANDIDATE_ID_IS_CANONICAL_POLICY_ID=NO
CANDIDATE_ID_IS_CANONICAL_SHA256=NO
GIT_COMMIT_OR_BLOB_SHA_AUTOMATICALLY_EQUALS_POLICY_CANONICAL_SHA256=NO
MUTABLE_LATEST_BINDING=PROHIBITED
```

No SHA-256 self-identity scheme is invented by this packet. A future canonicalization step must use an already-governed identity mechanism or separately authorize one.

---

# Part A — G1 / A5 Contributor and Content Rights Instrument Candidate

## 4. Candidate handle and scope

```text
A5_CANDIDATE_HANDLE=commandmed-selection-contributor-rights-candidate-v0
A5_DECLARED_USE=DEVELOPMENT_EVALUATION
A5_PURPOSE=CHECKPOINT_SELECTION_SUPPORTING_CONTENT_GOVERNANCE
A5_OWNERSHIP_TRANSFER_REQUIRED=NO
A5_NONEXCLUSIVE_GRANT_MODEL=CANDIDATE
```

This candidate is intended only for future selection-development contribution/adaptation governance. It grants nothing merely by existing in the repository.

## 5. Candidate contributor terms

A future executed instrument should state, in substance:

1. **Contributor authority.** The contributor represents, to the best of their knowledge, that they have authority to submit the material and to grant the rights expressly listed in the instrument.
2. **Ownership.** The contributor is not required by default to transfer ownership. Any project rights are nonexclusive unless a separately reviewed future instrument explicitly says otherwise.
3. **Storage and internal review.** The contributor permits commandMed to store the submitted material in the governed selection-development workspace and provide access to authorized internal reviewers/adjudicators for the declared evaluation purpose.
4. **Development evaluation use.** The contributor permits the submitted material to be used for commandMed development evaluation and checkpoint-selection evidence only within the separately authorized lifecycle.
5. **Arabic/English paired adaptation.** The contributor permits creation of Arabic/English paired translations or adaptations when that right is actually within the contributor's authority and when the parent/source lineage remains bound.
6. **Non-semantic corrections.** The project may apply deterministic formatting/normalization or other separately governed non-semantic corrections that do not alter clinical or scientific meaning.
7. **Identity-bound derived selection artifacts.** The project may create lineage-bound derivative selection artifacts only within the expressly granted development-evaluation scope.
8. **No silent broader rights.** Selection-development permission does not automatically grant training, teacher-generation, model-synthesis, public redistribution, commercial deployment, or unrelated research rights.

## 6. Candidate mandatory contributor representations

A future contributor acceptance mechanism should require explicit representations equivalent to:

```text
CONTRIBUTOR_HAS_AUTHORITY_TO_SUBMIT=YES
CONTENT_IS_NOT_COPIED_FROM_PRIVATE_GOLD=YES
CONTENT_IS_NOT_DERIVED_FROM_PRIVATE_GOLD_CASE_CONTENT=YES
CONTENT_IS_NOT_COPIED_FROM_PROHIBITED_PUBLIC_TEST_SPLIT=YES
CONTENT_DOES_NOT_CONTAIN_REAL_PATIENT_PHI_OR_RESTRICTED_CLINICAL_DATA=YES
CONTENT_DOES_NOT_CONTAIN_CONFIDENTIAL_EMPLOYER_OR_CLIENT_INFORMATION=YES
THIRD_PARTY_MATERIAL_DISCLOSED=YES_IF_PRESENT
THIRD_PARTY_RIGHTS_BOUND=YES_IF_PRESENT
```

Missing, ambiguous, conflicting, or materially false evidence must fail closed.

## 7. Third-party / derivative rule

```text
UNDECLARED_THIRD_PARTY_MATERIAL=PROHIBITED
UNRESOLVED_THIRD_PARTY_RIGHTS=BLOCKED
INCOMPATIBLE_THIRD_PARTY_RIGHTS=PROHIBITED
TRANSLATION_OR_PARAPHRASE_CREATES_NEW_RIGHTS=NO
DERIVATIVE_RETAINS_PARENT_RIGHTS_RESTRICTIONS=YES
PRIVATE_GOLD_PARENT_OR_SOURCE=PROHIBITED
```

Public visibility, repository availability, employment status, volunteer status, or verbal permission alone is not sufficient rights evidence.

## 8. Candidate acceptance-evidence metadata

A future auditable acceptance record should be able to bind at least:

```text
instrument_id
instrument_version
instrument_canonical_sha256
contributor_or_participant_reference
acceptance_evidence_id
acceptance_timestamp_or_equivalent_audit_sequence
accepted_declared_use
rights_scope_codes
privacy_attestation_state
private_gold_nonuse_attestation_state
third_party_material_disclosure_state
review_status
```

The open repository need not contain a personal signature document. It may contain only a minimal protected-system audit pointer when that is sufficient and governed.

## 9. A5 candidate exit gap

This candidate does not satisfy A5. Still required:

```text
EXACT_INSTRUMENT_TEXT_CANONICAL=NEEDS_GOVERNANCE_ADOPTION
EXACT_INSTRUMENT_VERSION_AND_CANONICAL_SHA256=NEEDS_EVIDENCE
INDEPENDENT_GOVERNANCE_OR_LEGAL_REVIEW=NEEDS_EVIDENCE
REAL_CONTRIBUTOR_ACCEPTANCE_MECHANISM=NEEDS_EVIDENCE
REAL_CONTRIBUTOR_ACCEPTANCE_RECORDS=NEEDS_EVIDENCE
```

---

# Part B — G2 / A6 Non-PHI Authoring Policy Candidate

## 10. Candidate handle and default boundary

```text
A6_CANDIDATE_HANDLE=commandmed-selection-non-phi-authoring-policy-candidate-v0
REQUIRED_PRIVACY_STATE=NO_PHI_KNOWN
DEFAULT_ROOT_CASE_ORIGIN=ORIGINAL_HUMAN_AUTHORED_NON_PHI
DEIDENTIFIED_REAL_PATIENT_SOURCE_AUTO_ELIGIBLE=NO
RESTRICTED_OR_PHI=PROHIBITED
UNRESOLVED_PRIVACY=BLOCKED
```

The preferred future construction route remains fictional/non-patient-identifying clinical scenarios authored from general professional knowledge, not copied real-patient records.

## 11. Prohibited source/content classes

A future operational policy should prohibit, at minimum:

```text
REAL_PATIENT_RECORD_COPYING
REAL_PATIENT_NOTE_TRANSCRIPTION
REAL_PATIENT_SCREENSHOT_OR_DOCUMENT_IMPORT
REAL_PATIENT_AUDIO_OR_IMAGE_IMPORT
RESTRICTED_CLINICAL_DATA_IMPORT
PATIENT_NAME
MEDICAL_RECORD_NUMBER_OR_EQUIVALENT
PHONE_OR_EMAIL
STREET_ADDRESS_OR_PRECISE_LOCATION
PATIENT_SPECIFIC_ACCOUNT_OR_RECORD_IDENTIFIER
FULL_FACE_OR_IDENTIFYING_IMAGE
PATIENT_SPECIFIC_DOCUMENT_OR_REPORT_IMAGE
UNIQUE_RECORD_LOCATOR
RAW_PHI
```

Absence of a name alone does not prove non-PHI, and public visibility of a clinical story does not make its privacy/provenance safe.

## 12. Candidate author attestation

Before any future authored root or language variant enters a governed construction workspace, the author should be required to attest, to the best of their knowledge:

```text
NO_REAL_PATIENT_IDENTIFIER_INCLUDED=YES
NO_REAL_PATIENT_RECORD_COPIED_OR_TRANSCRIBED=YES
NO_RESTRICTED_CLINICAL_DATA_USED=YES
NO_CONFIDENTIAL_EMPLOYER_OR_CLIENT_RECORD_USED=YES
NO_PRIVATE_GOLD_CASE_CONTENT_USED=YES
NO_PROHIBITED_PUBLIC_TEST_CASE_USED=YES
THIRD_PARTY_SOURCE_MATERIAL_DISCLOSED=YES_IF_PRESENT
```

## 13. Pair-level privacy candidate rule

```text
ROOT_TASK_PRIVACY_ATTESTATION_REQUIRED=YES
ARABIC_VARIANT_PRIVACY_CHECK_REQUIRED=YES
ENGLISH_VARIANT_PRIVACY_CHECK_REQUIRED=YES
PAIR_ACCEPTANCE_REQUIRES_BOTH_VARIANTS_PRIVACY_CLEAR=YES
```

A clean English variant cannot compensate for an unsafe Arabic variant, or vice versa. Translation/adaptation can introduce identifying detail and therefore requires its own check.

## 14. Clinical realism boundary

Permitted future authoring approaches, once construction is separately authorized, may include:

```text
ORIGINAL_FICTIONAL_SCENARIO_FROM_GENERAL_CLINICAL_KNOWLEDGE
INDEPENDENTLY_AUTHORED_COMPOSITE_WITH_NO_PATIENT_TRACEABILITY
ABSTRACTED_CLINICAL_PATTERN_WITHOUT_SOURCE_PATIENT_DETAILS
PUBLIC_NON_CASE_CLINICAL_STANDARD_OR_GUIDELINE_FACTS_WITH_RIGHTS_PROVENANCE
```

```text
PSEUDONYMIZATION_OF_ONE_REAL_PATIENT_EQUALS_ORIGINAL_FICTIONAL_CASE=NO
MINOR_DETAIL_PERTURBATION_OF_REAL_CASE_ALLOWED=NO
```

## 15. Incident / discovery candidate rule

If suspected PHI/restricted provenance is discovered:

```text
STOP_USE_OF_AFFECTED_CONTENT=REQUIRED
AFFECTED_CONTENT_STATUS=BLOCKED
NO_SCORING_OR_SELECTION_USE=REQUIRED
NO_FURTHER_PROPAGATION=REQUIRED
INCIDENT_METADATA_MUST_NOT_REPEAT_PHI=YES
GOVERNED_PRIVACY_REVIEW_REQUIRED=YES
```

If correction/removal materially changes a frozen suite, silent patching is prohibited; new suite identity and affected review/evaluation rebinding are required.

## 16. Candidate privacy-attestation metadata

A future auditable record should support at least:

```text
policy_id
policy_version
policy_canonical_sha256
author_or_participant_reference
root_task_or_content_reference
attestation_evidence_id
attestation_state
privacy_state
third_party_material_disclosure_state
private_gold_nonuse_state
review_status
```

## 17. A6 candidate exit gap

```text
EXACT_NON_PHI_POLICY_CANONICAL=NEEDS_GOVERNANCE_ADOPTION
POLICY_VERSION_AND_CANONICAL_SHA256=NEEDS_EVIDENCE
AUTHOR_ATTESTATION_MECHANISM_IMPLEMENTED=NEEDS_EVIDENCE
PAIR_LEVEL_PRIVACY_REVIEW_OPERATIONAL=NEEDS_EVIDENCE
INDEPENDENT_GOVERNANCE_OR_PRIVACY_REVIEW=NEEDS_EVIDENCE
REAL_ATTESTATION_RECORDS=NEEDS_EVIDENCE
```

---

# Part C — G3 / A8 Authoring, Review, Acceptance and Disagreement Protocol Candidate

## 18. Candidate handle and role separation

```text
A8_CANDIDATE_HANDLE=commandmed-selection-pair-review-protocol-candidate-v0
```

Future governed work should distinguish at least:

```text
ROOT_CASE_AUTHOR
PAIR_ADAPTER_OR_PARALLEL_LANGUAGE_AUTHOR
CLINICAL_REVIEWER_1
CLINICAL_REVIEWER_2
ADJUDICATOR_IF_REQUIRED
RIGHTS_PRIVACY_PROVENANCE_REVIEW
PRIVATE_GOLD_TRUSTEE_OR_FINAL_AUDIT_ROLE
```

For the same content identity:

```text
AUTHOR_MAY_SOLE_ACCEPT_OWN_CASE=NO
PAIR_ADAPTER_MAY_SOLE_ACCEPT_OWN_PAIR=NO
AUTHOR_MAY_SERVE_AS_FINAL_REVIEWER_FOR_OWN_CASE=NO
PAIR_ADAPTER_MAY_SERVE_AS_FINAL_REVIEWER_FOR_OWN_PAIR=NO
```

## 19. Candidate minimum clinical-review structure

Each future Arabic-English pair requires two independent clinical review dispositions before acceptance.

```text
MINIMUM_INDEPENDENT_FINAL_CLINICAL_REVIEWERS_PER_PAIR=2
REVIEWER_1_INDEPENDENT_OF_AUTHOR=YES
REVIEWER_2_INDEPENDENT_OF_AUTHOR=YES
REVIEWER_1_INDEPENDENT_OF_PAIR_ADAPTER=YES
REVIEWER_2_INDEPENDENT_OF_PAIR_ADAPTER=YES
AT_LEAST_ONE_REVIEWER_NATIVE_ARABIC_SPEAKING_CLINICAL_PROFESSIONAL=YES
BILINGUAL_CLINICAL_COMPARISON_COMPETENCE_REQUIRED_ACROSS_REVIEW_PAIR=YES
REGIONAL_OR_DIALECT_COMPETENCE_REQUIRED_WHERE_APPLICABLE=YES
```

Exact identities and any additional credential requirements remain unresolved and cannot be invented here.

## 20. Gold / candidate-result firewall

Before assignment to authoring/adaptation/final review/adjudication:

```text
ACTUAL_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_IS_CONTROLLING=YES
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_SELECTION_AUTHOR=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_PAIR_ADAPTER=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_FINAL_REVIEWER=PROHIBITED
PRIOR_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE_FOR_ADJUDICATOR=PROHIBITED
```

And before suite freeze:

```text
CANDIDATE_RESULTS_AVAILABLE_DURING_INITIAL_AUTHORING=NO
CANDIDATE_RESULTS_AVAILABLE_DURING_INITIAL_PAIR_REVIEW=NO
CANDIDATE_RESULTS_AVAILABLE_TO_ADJUDICATOR_BEFORE_SUITE_FREEZE=NO
CANDIDATE_ERROR_ANALYSIS_USED_TO_REWRITE_INITIAL_SUITE=PROHIBITED
```

## 21. Candidate individual-review dimensions

Each final reviewer should independently address at least:

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

Clinical review does not replace rights/privacy/provenance review.

## 22. Distinguish individual dispositions from final binding vocabulary

The frozen Session 11 individual reviewer vocabulary is:

```text
INDIVIDUAL_REVIEW_DISPOSITIONS=ACCEPT,REVISE,REJECT,BLOCKED
```

The existing `preconstruction.py` final `ReviewBinding` validator separately accepts:

```text
FINAL_REVIEW_BINDING_DISPOSITIONS=ACCEPTED,REJECTED,ESCALATED_FOR_ADJUDICATION
```

This packet treats those as **different layers**, not conflicting synonyms:

- individual reviewers record their own review findings/dispositions;
- the future final review-binding record reflects the governed aggregate/adjudication state accepted by the existing validator.

This packet does not modify either vocabulary.

## 23. Candidate pair-acceptance rule

```text
TWO_INDEPENDENT_INDIVIDUAL_ACCEPT_DISPOSITIONS_REQUIRED_BEFORE_NORMAL_ACCEPTANCE=YES
ONE_ACCEPT_PLUS_ONE_REVISE=NOT_ACCEPTED
ONE_ACCEPT_PLUS_ONE_REJECT=NOT_ACCEPTED
ONE_ACCEPT_PLUS_ONE_BLOCKED=NOT_ACCEPTED
TWO_REVISE=NOT_ACCEPTED
ANY_BLOCKED=BLOCKED
```

A revised material content identity requires fresh required review; prior acceptance does not silently transfer.

## 24. Candidate disagreement/adjudication rule

After one bounded reviewer clarification exchange, unresolved material disagreement must not be resolved by author preference, founder preference, or simple averaging.

```text
UNRESOLVED_MATERIAL_DISAGREEMENT_REQUIRES_INDEPENDENT_ADJUDICATOR=YES
ADJUDICATOR_INDEPENDENT_OF_AUTHOR=YES
ADJUDICATOR_INDEPENDENT_OF_PAIR_ADAPTER=YES
ADJUDICATOR_PRIVATE_GOLD_CASE_EXPOSURE_PROHIBITED=YES
```

The adjudicator may produce a reasoned outcome equivalent to:

```text
ACCEPT_AFTER_REASONED_RECONCILIATION
REVISE
REJECT
BLOCKED
```

A future mapping from this adjudication outcome to the existing final `ReviewBinding` disposition must be explicitly governed; this packet does not silently define it.

## 25. Candidate review-record metadata

Future records should support at least:

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

Adjudication should support:

```text
adjudication_record_id
adjudicator_reference
adjudicated_content_artifact_sha256
reviewer_disagreement_references
adjudication_disposition
reasoned_reconciliation
```

## 26. A8 candidate exit gap

```text
EXACT_REVIEW_PROTOCOL_CANONICAL=NEEDS_GOVERNANCE_ADOPTION
PROTOCOL_VERSION_AND_CANONICAL_SHA256=NEEDS_EVIDENCE
EXACT_REVIEWER_ELIGIBILITY_CRITERIA_BEYOND_FROZEN_MINIMUM=UNRESOLVED_IF_REQUIRED
REAL_REVIEWER_ASSIGNMENT_EVIDENCE=NEEDS_EVIDENCE
REAL_GOLD_NONEXPOSURE_EVIDENCE=NEEDS_EVIDENCE
REAL_REVIEW_EXECUTION=NOT_AUTHORIZED_AND_NOT_PERFORMED
INDEPENDENT_GOVERNANCE_REVIEW=NEEDS_EVIDENCE
```

---

# Part D — G4 / A12 Change Control and Invalid-Case Disposition Candidate

## 27. Candidate handle and objective-invalidity rule

```text
A12_CANDIDATE_HANDLE=commandmed-selection-case-change-control-candidate-v0
```

Candidate performance is never sufficient evidence that a case is invalid.

```text
CANDIDATE_WRONG_ANSWER_IMPLIES_CASE_INVALID=NO
CANDIDATE_LOW_SCORE_IMPLIES_CASE_INVALID=NO
CANDIDATE_REFUSAL_IMPLIES_CASE_INVALID=NO
CANDIDATE_TIMEOUT_IMPLIES_CASE_INVALID=NO
CANDIDATE_MALFORMED_OUTPUT_IMPLIES_CASE_INVALID=NO
MULTIPLE_CANDIDATES_FAILING_CASE_IMPLIES_CASE_INVALID=NO
PREFERRED_CANDIDATE_FAILURE_IMPLIES_CASE_INVALID=NO
CANDIDATE_OUTPUT_FAILURE_AUTHORIZES_CASE_REPLACEMENT=NO
CANDIDATE_SPECIFIC_SAMPLE_REPLENISHMENT=PROHIBITED
```

## 28. Candidate invalidity taxonomy

A future protocol should use a closed taxonomy including at least:

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

```text
MODEL_FOUND_IT_HARD_AS_INVALIDITY_REASON=PROHIBITED
PREFERRED_CANDIDATE_FAILED_AS_INVALIDITY_REASON=PROHIBITED
SURPRISING_SCORE_AS_INVALIDITY_REASON=PROHIBITED
```

## 29. Candidate lifecycle states

```text
DRAFT
UNDER_REVIEW
ACCEPTED_UNFROZEN
FROZEN_ACTIVE
BLOCKED_INVALID
SUPERSEDED
RETIRED_WITHOUT_REPLACEMENT
```

Only an identity satisfying all predeclared acceptance gates may become `FROZEN_ACTIVE`.

## 30. Material-change rule

A material change includes any change that may affect clinical/safety/scoring/language/provenance/governance/statistical meaning.

For every material change:

```text
NEW_CONTENT_ARTIFACT_IDENTITY_REQUIRED=YES
NEW_CASE_OR_PAIR_VERSION_REQUIRED=YES
PRIOR_FINAL_REVIEW_ACCEPTANCE_AUTO_TRANSFER=NO
FRESH_REQUIRED_REVIEW_ON_NEW_IDENTITY=YES
PROVENANCE_CHANGE_RECORD_REQUIRED=YES
```

A change may preserve identity only if produced by a separately canonical deterministic normalization rule proven not to alter semantic content.

## 31. Pre-freeze and post-freeze rules

Before freeze and before candidate-result exposure, a material repair may occur only through governed new-identity review.

After suite freeze but before candidate results:

```text
SILENT_IN_PLACE_PATCH=PROHIBITED
SILENT_CASE_REMOVAL=PROHIBITED
SILENT_REPLACEMENT=PROHIBITED
AFFECTED_CASE_STATUS=BLOCKED_INVALID
INVALIDITY_RECORD_REQUIRED=YES
```

Possible governed future dispositions include:

```text
REPAIR_AS_NEW_IDENTITY
REPLACE_WITH_PREDECLARED_SLOT_COMPATIBLE_NEW_CASE
REVISE_STATISTICAL_ALLOCATION_OR_DESIGN_THROUGH_GOVERNED_REDESIGN
RETIRE_WITHOUT_REPLACEMENT_ONLY_IF_PREDECLARED_STATISTICAL_REQUIREMENTS_REMAIN_SATISFIED_AND_RECONFIRMED
```

Every material content-set change creates a new suite identity and requires statistical/coverage recheck.

## 32. Replacement rule

A replacement must satisfy the same predeclared statistical/coverage/role/use-context slot and all rights/privacy/provenance/review gates.

```text
CANDIDATE_SPECIFIC_REPLACEMENT=PROHIBITED
REPLACEMENT_CHOSEN_TO_HELP_PREFERRED_CANDIDATE=PROHIBITED
REPLACEMENT_CHOSEN_TO_REDUCE_OBSERVED_FAILURE_RATE=PROHIBITED
REPLACEMENT_CHOSEN_AFTER_COMPARING_CANDIDATE_RESULTS=PROHIBITED
```

If no valid replacement preserves the frozen design, the process stops for governed redesign rather than silently reducing `N` or reallocating coverage.

## 33. Post-result invalidity rule

If genuine objective invalidity is discovered after any candidate-result exposure:

```text
POST_RESULT_SILENT_REMOVAL=PROHIBITED
POST_RESULT_SILENT_REPAIR=PROHIBITED
POST_RESULT_CANDIDATE_SPECIFIC_EXCLUSION=PROHIBITED
POST_RESULT_RESULT_AWARE_REPLACEMENT=PROHIBITED
OLD_FROZEN_SUITE_IDENTITY_REMAINS_HISTORICAL_AND_REPRODUCIBLE=YES
NEW_CORRECTED_SUITE_IDENTITY_REQUIRED=YES
OLD_RESULTS_AUTO_TRANSFER_TO_NEW_SUITE=NO
FRESH_ALL_CANDIDATE_EVALUATION_ON_CORRECTED_SUITE_REQUIRED_FOR_COMPARATIVE_SELECTION_EVIDENCE=YES
```

This is a future scientific consequence only; no model/benchmark execution is authorized by this packet.

## 34. Candidate change-control metadata

A future material change/invalidity record should support at least:

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

Candidate-result exposure state should distinguish at least:

```text
NO_CANDIDATE_RESULTS_EXIST_OR_EXPOSED
CANDIDATE_RESULTS_EXIST_BUT_INVALIDITY_REVIEW_FIREWALLED
COMPARATIVE_CANDIDATE_RESULTS_EXPOSED
```

## 35. A12 candidate exit gap

```text
EXACT_CHANGE_CONTROL_PROTOCOL_CANONICAL=NEEDS_GOVERNANCE_ADOPTION
PROTOCOL_VERSION_AND_CANONICAL_SHA256=NEEDS_EVIDENCE
EXACT_OPERATIONAL_AUDIT_STORAGE_BINDING=NEEDS_EVIDENCE
REAL_SUITE_IDENTITY=ABSENT
REAL_CHANGE_RECORDS=NOT_APPLICABLE_BEFORE_CONSTRUCTION
INDEPENDENT_GOVERNANCE_REVIEW=NEEDS_EVIDENCE
```

---

# Part E — Cross-foundation review and next dependencies

## 36. No gate PASS from this packet

This packet must not be cited as proof that A5/A6/A8/A12 passed.

```text
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
```

It provides candidate operational wording only.

## 37. Required future independent governance review questions

A future qualified governance/legal/privacy/clinical review, as applicable, should determine:

1. Whether the A5 rights grant is legally/operationally sufficient for the exact selection-development lifecycle without silently granting training/redistribution rights.
2. Whether the A5 contributor representations and withdrawal/dispute handling are sufficient for the intended jurisdictions/operating model.
3. Whether A6's `NO_PHI_KNOWN` policy and attestation language is operationally sufficient and whether any additional privacy/security review is required.
4. Whether A8 correctly separates individual reviewer dispositions from the existing final `ReviewBinding` disposition vocabulary.
5. Whether A8's minimum two-reviewer/native-Arabic/bilingual/regional competence rules need additional exact eligibility criteria before assignment.
6. Whether the A8 disagreement/adjudication flow maps safely into the existing final binding validator without mutating closed Spec 005 semantics.
7. Whether A12's invalidity taxonomy and identity-change rules are complete enough for operational use.
8. Whether any material conflict exists among A5/A6/A8/A12 that blocks A10 source-route finalization or A9 provenance binding.

No answer is fabricated here.

## 38. DAG consequences

Even after these candidates exist:

```text
G1_REAL_PASS_REQUIRES=CANONICAL_INSTRUMENT+GOVERNANCE_REVIEW+REAL_ACCEPTANCE_MECHANISM/EVIDENCE
G2_REAL_PASS_REQUIRES=CANONICAL_POLICY+GOVERNANCE/PRIVACY_REVIEW+REAL_ATTESTATION_MECHANISM/EVIDENCE
G3_REAL_PASS_REQUIRES=CANONICAL_PROTOCOL+GOVERNANCE_REVIEW+REAL_PERSONNEL_ASSIGNMENT/NONEXPOSURE/REVIEW_BINDINGS
G4_REAL_PASS_REQUIRES=CANONICAL_PROTOCOL+GOVERNANCE_REVIEW+LATER_REAL_SUITE_BINDING
```

Therefore:

```text
S1_A10_EXACT_SOURCE_ROUTE=STILL_NOT_REAL_PASS
P1_A9_PROVENANCE_BINDINGS=STILL_NOT_REAL_PASS
C1_A11_CONTAMINATION_PLAN_BINDING=STILL_NOT_REAL_PASS
H1_A7_PERSONNEL=STILL_NOT_REAL_PASS
I1_A13_ACCESS_FIREWALL=STILL_NOT_REAL_PASS
F1_A14_SPEND_ENGAGEMENT=STILL_NOT_REAL_PASS
J1=NOT_REACHED
ACT_A15=ABSENT
```

## 39. Current E004 state

```text
T1_A2=INCOMPLETE_REAL_QUALIFIED_SCIENTIFIC_REVIEW_AND_NUMERIC_POLICY
D34_A3_A4=BLOCKED_BY_T1
G1_G2_G3_G4_OPERATIONAL_CANDIDATE_TEXT=PREPARED_FOR_REVIEW_ONLY
REAL_A2_TO_A14_SNAPSHOT=ABSENT
REAL_A15_ACTIVATION=ABSENT
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next safe transition for these governance candidates is independent governance review/canonical adoption where required, not simulated acceptances, invented reviewer identities, or case construction.