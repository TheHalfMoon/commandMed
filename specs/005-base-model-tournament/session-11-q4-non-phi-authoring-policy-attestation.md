# Session 11 Q4 — Non-PHI Authoring Policy and Attestation

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 11 Q4 only. It freezes the governance design for A6, the non-PHI authoring policy and attestation prerequisite that must exist before Arabic selection-suite construction can be authorized. It does not authorize authoring, create cases, access patient data, access Private Gold, implement A1, spend funds, execute models, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION11_Q4_POLICY=FICTIONAL_OR_NON_PATIENT_IDENTIFYING_AUTHORING_WITH_FAIL_CLOSED_PRIVACY_ATTESTATION

A6_GOVERNANCE_DESIGN=FROZEN
A6_IMPLEMENTED_AND_EXECUTED=NO
A6_GATE_STATUS=BLOCKED_PENDING_CANONICAL_POLICY_AND_ATTESTATION_MECHANISM

ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

## 2. Default authoring boundary

Initial selection-suite authoring must use content that is not derived from identifiable real-patient records.

```text
DEFAULT_ROOT_CASE_ORIGIN=ORIGINAL_HUMAN_AUTHORED_NON_PHI
REAL_PATIENT_RECORD_COPYING=PROHIBITED
REAL_PATIENT_NOTE_TRANSCRIPTION=PROHIBITED
REAL_PATIENT_SCREENSHOT_OR_DOCUMENT_IMPORT=PROHIBITED
REAL_PATIENT_AUDIO_OR_IMAGE_IMPORT=PROHIBITED
RESTRICTED_CLINICAL_DATA_IMPORT=PROHIBITED
```

Clinical realism may be achieved through professional knowledge and independently authored fictional scenarios, not by copying a real patient's record.

## 3. Privacy-state requirement

The existing lineage contract distinguishes privacy states including `NO_PHI_KNOWN`, `DEIDENTIFIED`, `RESTRICTED_OR_PHI`, and `UNRESOLVED`.

For initial selection-suite construction:

```text
REQUIRED_PRIVACY_STATE=NO_PHI_KNOWN
DEIDENTIFIED_REAL_PATIENT_SOURCE_AUTO_ELIGIBLE=NO
RESTRICTED_OR_PHI=PROHIBITED
UNRESOLVED=BLOCKED
NOT_APPLICABLE_ALLOWED_FOR_CASE_CONTENT=NO
```

A future separate authorization may define a governed path for legitimately deidentified real-patient-derived evidence; Q4 does not authorize or design that path.

## 4. Author attestation requirements

Before an authored root task or language variant may enter the governed selection authoring workspace, the author must attest that, to the best of their knowledge:

```text
NO_REAL_PATIENT_IDENTIFIER_INCLUDED=YES
NO_REAL_PATIENT_RECORD_WAS_COPIED_OR_TRANSCRIBED=YES
NO_RESTRICTED_CLINICAL_DATA_WAS_USED=YES
NO_CONFIDENTIAL_EMPLOYER_OR_CLIENT_RECORD_WAS_USED=YES
NO_PRIVATE_GOLD_CASE_CONTENT_WAS_USED=YES
NO_PROHIBITED_PUBLIC_TEST_CASE_WAS_USED=YES
THIRD_PARTY_SOURCE_MATERIAL_DISCLOSED=YES_IF_PRESENT
```

Missing, ambiguous, or conflicting attestation fails closed.

## 5. Prohibited identifier and payload classes

The future policy must prohibit inclusion of direct or reasonably identifying patient information, including at minimum:

```text
patient_name
medical_record_number_or_equivalent
phone_or_email
street_address_or_precise_location
patient_specific_account_or_record_identifier
full_face_or_identifying_image
patient_specific_document_or_report_image
unique_record_locator
raw_phi
```

The policy must also prohibit copying a supposedly anonymous clinical narrative when its origin/rights/privacy status is unresolved.

```text
ABSENCE_OF_NAME_ALONE_PROVES_NON_PHI=NO
PUBLICLY_VISIBLE_CLINICAL_STORY_AUTO_SAFE=NO
```

## 6. Clinical realism without patient copying

Permitted design methods, once construction is separately authorized, may include:

```text
ORIGINAL_FICTIONAL_SCENARIO_FROM_GENERAL_CLINICAL_KNOWLEDGE
INDEPENDENTLY_AUTHORED_COMPOSITE_SCENARIO_WITH_NO_PATIENT_TRACEABILITY
ABSTRACTED_CLINICAL_PATTERN_WITHOUT_SOURCE_PATIENT_DETAILS
PUBLIC_NON_CASE_CLINICAL_STANDARD_OR_GUIDELINE_FACTS_WITH_RIGHTS_PROVENANCE
```

The author must not reconstruct a memorable real patient by changing only names, ages, dates, or a few surface details.

```text
PSEUDONYMIZATION_OF_ONE_REAL_PATIENT_EQUALS_ORIGINAL_FICTIONAL_CASE=NO
MINOR_DETAIL_PERTURBATION_OF_REAL_CASE_ALLOWED=NO
```

## 7. Arabic/English pair privacy rule

Privacy clearance applies to the root semantic specification and to both language realizations.

```text
ROOT_TASK_PRIVACY_ATTESTATION_REQUIRED=YES
ARABIC_VARIANT_PRIVACY_CHECK_REQUIRED=YES
ENGLISH_VARIANT_PRIVACY_CHECK_REQUIRED=YES

TRANSLATION_MAY_REINTRODUCE_IDENTIFYING_DETAIL=YES_POSSIBLE_AND_MUST_BE_REVIEWED
PAIR_ACCEPTANCE_REQUIRES_BOTH_VARIANTS_PRIVACY_CLEAR=YES
```

A clean English variant cannot compensate for an unsafe Arabic variant, or vice versa.

## 8. Incident / discovery rule

If suspected PHI, restricted data, or patient-identifying provenance is discovered before or after acceptance:

```text
STOP_USE_OF_AFFECTED_CONTENT=REQUIRED
AFFECTED_CONTENT_STATUS=BLOCKED
NO_SCORING_OR_SELECTION_USE=REQUIRED
NO_FURTHER_PROPAGATION=REQUIRED
INCIDENT_METADATA_MUST_NOT_REPEAT_THE_PHI=YES
GOVERNED_PRIVACY_REVIEW_REQUIRED=YES
```

If removal or replacement changes a frozen suite materially:

```text
SILENT_PATCH=PROHIBITED
NEW_SUITE_ARTIFACT_IDENTITY_REQUIRED=YES
AFFECTED_REVIEW_BINDINGS_MUST_BE_RECOMPUTED=YES
FRESH_ALL_CANDIDATE_EVALUATION_REQUIRED_IF_SELECTION_EVIDENCE_ALREADY_EXISTS=YES
```

Q4 does not authorize any real incident handling action because no case construction is currently authorized.

## 9. Gold firewall

```text
PRIVATE_GOLD_CASE_CONTENT_AS_AUTHORING_SOURCE=PROHIBITED
PRIVATE_GOLD_CASE_CONTENT_AS_PRIVACY_CLEARED_SOURCE=PROHIBITED
PRIVATE_GOLD_TRANSLATION_OR_PARAPHRASE_AS_SELECTION_CASE=PROHIBITED

PUBLIC_GOLD_PROTOCOL_METADATA_MAY_DEFINE_COVERAGE_ANCHORS=YES
```

No privacy attestation can convert Private Gold into selection material.

## 10. Provider and model boundary

```text
EXTERNAL_MODEL_OR_PROVIDER_CASE_AUTHORING=NOT_AUTHORIZED
EXTERNAL_MODEL_OR_PROVIDER_PHI_SCREENING=NOT_AUTHORIZED
MODEL_OUTPUT_AS_AUTHORING_SOURCE=NOT_AUTHORIZED

PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
```

A future automated privacy checker would require separate authority and must not become the sole basis for clinical/privacy eligibility.

## 11. Required attestation identity

The future authoring system must bind each accepted content item to an auditable privacy attestation without publishing unnecessary contributor personal information.

Minimum fields:

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

```text
PUBLIC_REPOSITORY_MUST_STORE_PERSONAL_SIGNATURE_DOCUMENT=NO
AUDITABLE_ATTESTATION_EVIDENCE_REQUIRED=YES
```

## 12. A6 exit evidence required before construction readiness

A6 may become `PASS` only after a future canonical artifact proves:

```text
EXACT_NON_PHI_POLICY_CANONICAL=YES
POLICY_VERSION_AND_SHA_BOUND=YES
REQUIRED_PRIVACY_STATE_DEFINED=YES
PROHIBITED_REAL_PATIENT_SOURCE_RULES_DEFINED=YES
AUTHOR_ATTESTATION_MECHANISM_DEFINED=YES
PAIR_LEVEL_PRIVACY_REVIEW_DEFINED=YES
INCIDENT_FAIL_CLOSED_RULE_DEFINED=YES
GOLD_NONUSE_RULE_DEFINED=YES
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Q4 itself does not satisfy these implementation facts.

## 13. Authority boundary

```text
PLAN_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A6_POLICY_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
RESTRICTED_CLINICAL_DATA_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
