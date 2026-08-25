# Session 11 Q3 — Contributor and Content Rights Instrument Design

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 11 Q3 only. It freezes the governance design for A5, the contributor/content-rights prerequisite that must exist before Arabic selection-suite construction can be authorized. It does not create the instrument as an executed legal agreement, obtain any contributor acceptance, authorize authoring, access data, access Private Gold, spend funds, execute models, implement A1, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION11_Q3_POLICY=IDENTITY_BOUND_CONTRIBUTOR_RIGHTS_INSTRUMENT_BEFORE_ANY_SELECTION_CASE_AUTHORING

A5_GOVERNANCE_DESIGN=FROZEN
A5_IMPLEMENTED_AND_EXECUTED=NO
A5_GATE_STATUS=BLOCKED_PENDING_CANONICAL_INSTRUMENT_AND_ACCEPTANCE_EVIDENCE

CONSTRUCTION_AUTHORITY=NONE
```

## 2. Purpose

The future instrument exists to prove that commandMed has sufficient rights for the exact intended selection-development lifecycle without overclaiming ownership or public redistribution rights.

The instrument must separately cover:

```text
AUTHOR_OR_CONTRIBUTOR_AUTHORITY_TO_SUBMIT
PROJECT_RIGHT_TO_STORE_AND_REVIEW
PROJECT_RIGHT_TO_USE_FOR_DEVELOPMENT_EVALUATION
PROJECT_RIGHT_TO_CREATE_ARABIC_ENGLISH_PAIRED_ADAPTATIONS
PROJECT_RIGHT_TO_MAKE_NON_SEMANTIC_CORRECTIONS_AND_FORMAT_NORMALIZATION
PROJECT_RIGHT_TO_CREATE_IDENTITY_BOUND_DERIVED_SELECTION_ARTIFACTS
AUTHORIZED_INTERNAL_REVIEWER_ACCESS
```

No right is inferred from public availability, employment status, repository access, or contribution alone.

## 3. Ownership and grant semantics

Default policy:

```text
CONTRIBUTOR_OWNERSHIP_TRANSFER_REQUIRED=NO
NONEXCLUSIVE_GRANT_ACCEPTABLE=YES

RIGHTS_SCOPE_MUST_COVER_EXACT_DECLARED_USE=DEVELOPMENT_EVALUATION
RIGHTS_SCOPE_MUST_COVER_PAIR_TRANSLATION_OR_ADAPTATION=YES
RIGHTS_SCOPE_MUST_COVER_INTERNAL_REVIEW_AND_ADJUDICATION=YES

PUBLIC_REDISTRIBUTION_RIGHT_AUTO_GRANTED=NO
TRAINING_OR_ADAPTATION_RIGHT_AUTO_GRANTED=NO
TEACHER_OR_SYNTHETIC_GENERATION_RIGHT_AUTO_GRANTED=NO
COMMERCIAL_DEPLOYMENT_RIGHT_AUTO_GRANTED=NO
```

If later lifecycle stages require broader rights, they require separate evidence and authorization. A selection-development grant must not silently become a training, redistribution, or deployment grant.

## 4. Required contributor representations

Before any contributed content may enter an authoring workspace intended for the selection suite, the future executed instrument must require the contributor to attest that, to the best of their knowledge:

```text
CONTRIBUTOR_HAS_AUTHORITY_TO_SUBMIT=YES
CONTENT_IS_NOT_COPIED_FROM_PRIVATE_GOLD=YES
CONTENT_IS_NOT_DERIVED_FROM_PRIVATE_GOLD_CASE_CONTENT=YES
CONTENT_IS_NOT_COPIED_FROM_A_PROHIBITED_PUBLIC_TEST_SPLIT=YES
CONTENT_DOES_NOT_CONTAIN_REAL_PATIENT_PHI_OR_RESTRICTED_CLINICAL_DATA=YES
CONTENT_DOES_NOT_CONTAIN_CONFIDENTIAL_EMPLOYER_OR_CLIENT_INFORMATION=YES
THIRD_PARTY_MATERIAL_IS_IDENTIFIED_AND_RIGHTS_BOUND=YES_IF_PRESENT
```

A false, missing, unresolved, or materially inconsistent representation is fail-closed.

## 5. Third-party material rule

```text
UNDECLARED_THIRD_PARTY_MATERIAL=PROHIBITED
THIRD_PARTY_SOURCE_WITH_UNRESOLVED_RIGHTS=BLOCKED
THIRD_PARTY_SOURCE_WITH_INCOMPATIBLE_RIGHTS=PROHIBITED

TRANSLATION_OR_PARAPHRASE_DOES_NOT_CREATE_NEW_RIGHTS=YES
DERIVATION_RETAINS_PARENT_RIGHTS_RESTRICTIONS=YES
```

Any third-party parent must remain identity-bound through lineage/provenance records.

## 6. Private Gold firewall

```text
PRIVATE_GOLD_CASE_CONTENT_MAY_BE_A_CONTRIBUTION_SOURCE=NO
PRIVATE_GOLD_CASE_CONTENT_MAY_BE_A_DERIVATION_PARENT=NO
PRIVATE_GOLD_CASE_CONTENT_MAY_BE_A_TRANSLATION_SEED=NO
PRIVATE_GOLD_CASE_CONTENT_MAY_BE_A_PARAPHRASE_SEED=NO
PRIVATE_GOLD_RUBRICS_OR_ANSWERS_MAY_BE_AUTHORING_SEEDS=NO

PUBLIC_GOLD_PROTOCOL_METADATA_MAY_GUIDE_COVERAGE_TAXONOMY=YES
```

The contributor instrument cannot waive or weaken canonical Gold quarantine.

## 7. Required identity-bound acceptance evidence

The future acceptance evidence must be represented without exposing unnecessary personal information in the open repository.

Minimum record:

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

The open repository may carry only a minimal identity/audit pointer if the underlying signed or attributable evidence is stored in an appropriate protected system.

```text
PUBLIC_REPO_MUST_STORE_SIGNED_PERSONAL_DOCUMENT=NO
AUDITABLE_ACCEPTANCE_EVIDENCE_REQUIRED=YES
```

## 8. Versioning and change control

```text
INSTRUMENT_VERSION_CHANGE_CREATES_NEW_INSTRUMENT_IDENTITY=YES
SILENT_IN_PLACE_RIGHTS_SCOPE_REINTERPRETATION=PROHIBITED

CONTRIBUTION_ACCEPTED_UNDER_OLD_INSTRUMENT_AUTOMATICALLY_INHERITS_BROADER_NEW_RIGHTS=NO
```

If an accepted contribution later loses usable rights or the contributor raises a valid withdrawal/authority dispute:

```text
SILENT_DELETE_FROM_FROZEN_SUITE=PROHIBITED
AFFECTED_CONTENT_STATUS=BLOCKED_PENDING_GOVERNED_DISPOSITION
MATERIAL_SUITE_CHANGE_REQUIRES_NEW_ARTIFACT_IDENTITY=YES
REVIEW_AND_SELECTION_EVIDENCE_REBIND_REQUIRED=YES
```

This is a scientific identity rule, not a statement that all legal revocation questions have one universal answer.

## 9. Rights-state mapping

The future A5 evidence must map cleanly to the existing lineage vocabulary:

```text
SUPPORTED=exact intended selection-development rights evidenced
CONDITIONAL=rights depend on unresolved condition; construction use blocked until resolved
UNRESOLVED=insufficient evidence; blocked
INCOMPATIBLE=prohibited for intended use
```

For initial Arabic selection construction:

```text
REQUIRED_RIGHTS_STATE=SUPPORTED
CONDITIONAL_RIGHTS_ALLOWED_TO_ENTER_SCORABLE_SELECTION_SUITE=NO
UNRESOLVED_RIGHTS_ALLOWED=NO
INCOMPATIBLE_RIGHTS_ALLOWED=NO
```

## 10. No automatic contributor engagement authority

```text
INSTRUMENT_DESIGN_DOES_NOT_AUTHORIZE_RECRUITMENT=YES
INSTRUMENT_DESIGN_DOES_NOT_AUTHORIZE_PAYMENT=YES
INSTRUMENT_DESIGN_DOES_NOT_AUTHORIZE_CASE_AUTHORING=YES

CURRENT_AUTHORIZED_SPEND_USD=0
PAID_CONTRIBUTOR_ENGAGEMENT_AUTHORITY=NONE
VOLUNTEER_OR_INTERNAL_AUTHORING_AUTO_AUTHORIZED=NO
```

## 11. A5 exit evidence required before construction readiness

A5 may become `PASS` only after a future canonical artifact proves:

```text
EXACT_INSTRUMENT_TEXT_CANONICAL=YES
EXACT_INSTRUMENT_VERSION_AND_SHA_BOUND=YES
EXACT_DECLARED_SELECTION_USE_COVERED=YES
PAIR_TRANSLATION_ADAPTATION_RIGHTS_COVERED=YES
PRIVATE_GOLD_NONUSE_CLAUSE_PRESENT=YES
NO_PHI_RESTRICTED_DATA_CLAUSE_PRESENT=YES
THIRD_PARTY_PARENT_DISCLOSURE_RULE_PRESENT=YES
IDENTITY_BOUND_ACCEPTANCE_MECHANISM_DEFINED=YES
CHANGE_CONTROL_DEFINED=YES
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

This Q3 satisfies none of those implementation/acceptance facts by itself.

## 12. Authority boundary

```text
PLAN_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A5_INSTRUMENT_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
