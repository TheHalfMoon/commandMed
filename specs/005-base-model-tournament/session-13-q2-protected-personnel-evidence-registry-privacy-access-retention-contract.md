# Session 13 Q2 — Protected Personnel-Evidence Registry Privacy, Access, and Retention Contract

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 13 Q2 only. It freezes the governance design for the protected evidence surface supporting A7 personnel identity, qualification, conflict, Private-Gold nonexposure, role eligibility, assignment, transition, suspension, and revocation decisions. It does **not** create storage, ingest or inspect any real personnel record, verify any credential, identify or assign any person, access Private Gold, grant role or payload access, provision A13 controls, spend funds, execute models, implement A1, authorize A15, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION13_Q2_POLICY=DUAL_SURFACE_DATA_MINIMIZED_PROTECTED_PERSONNEL_EVIDENCE_VAULT_WITH_OPAQUE_PUBLIC_PROOFS_LEAST_PRIVILEGE_VERIFIER_ACCESS_AND_APPEND_ONLY_CORRECTION

A7_PROTECTED_EVIDENCE_REGISTRY_PRIVACY_ACCESS_RETENTION_DESIGN=FROZEN
A7_PROTECTED_EVIDENCE_REGISTRY_IMPLEMENTED=NO
A7_PROTECTED_EVIDENCE_STORAGE_PROVISIONED=NO

A7_GATE_STATUS=BLOCKED_PENDING_CANONICAL_REGISTRY_IMPLEMENTATION_EXACT_PERSONNEL_EVIDENCE_AND_INDEPENDENT_REVIEW

CLARIFICATION_SESSION_13=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q2 defines how future protected evidence may be held and verified. It does not create the evidence or make A7 operationally PASS.

## 2. Core dual-surface architecture

The future A7 implementation must separate:

```text
SURFACE_1=OPAQUE_GOVERNANCE_INDEX
SURFACE_2=PROTECTED_PERSONNEL_EVIDENCE_STORE
```

Surface 1 may be referenced by repository-visible governance artifacts. Surface 2 contains sensitive supporting evidence and must not be exposed through ordinary repository access.

```text
PUBLIC_OR_BROADLY_VISIBLE_GOVERNANCE_INDEX_MAY_CONTAIN_RAW_PERSONNEL_EVIDENCE=NO
PROTECTED_PERSONNEL_EVIDENCE_STORE_MAY_BE_PUBLIC_GIT_REPOSITORY=NO
```

The two surfaces may be implemented by separate systems or independently enforceable access partitions, but a filename convention or nominal folder separation alone is insufficient.

```text
DIRECTORY_NAME_ONLY_COUNTS_AS_PERSONNEL_PRIVACY_BOUNDARY=NO
POLICY_TEXT_WITHOUT_ENFORCEABLE_ACCESS_CONTROL=INSUFFICIENT
```

## 3. Surface 1 — opaque governance index

Surface 1 exists to make scientific and governance decisions reproducible without publishing sensitive personnel data.

Permitted examples include:

```text
personnel_reference
role_class
suite_or_scope_id
eligibility_disposition
qualification_disposition
conflict_disposition
gold_exposure_disposition
role_assignment_state
role_transition_disposition
policy_id
policy_version
record_id
record_version
record_canonical_sha256
protected_evidence_bundle_reference
```

Surface 1 must not expose raw evidence such as:

```text
real_name_unless_separately_and_voluntarily_published_for_an_unrelated_reason
personal_email
phone_number
home_address
identity_document
passport_or_national_id_number
professional_license_number
credential_document_image
signed_attestation_body
employment_contract
financial_statement
raw_conflict_disclosure_details
private_personnel_notes
private_gold_access_log_details_that_identify_protected_artifacts
```

```text
OPAQUE_PUBLIC_REFERENCE_MUST_NOT_BE_REVERSIBLE_BY_DESIGN_TO_SENSITIVE_SOURCE_DATA=YES
```

A deterministic scientific record does not require public disclosure of the underlying person's identity.

## 4. Surface 2 — protected personnel evidence

The protected store may hold only evidence necessary for authorized A7 verification and governance.

Potential evidence classes include:

```text
IDENTITY_VERIFICATION_EVIDENCE
PROFESSIONAL_QUALIFICATION_EVIDENCE
ROLE_SCOPE_COMPETENCE_EVIDENCE
LANGUAGE_OR_REGIONAL_COMPETENCE_EVIDENCE_WHERE_REQUIRED
CONFLICT_DISCLOSURE_EVIDENCE
PRIVATE_GOLD_NONEXPOSURE_ATTESTATION
PRIVATE_GOLD_ACCESS_REGISTRY_RECONCILIATION_EVIDENCE
ROLE_TRANSITION_PREREQUISITE_EVIDENCE
SUSPENSION_OR_REVOCATION_EVIDENCE
CORRECTION_OR_APPEAL_EVIDENCE
```

The protected personnel store must not become a case-content or result store.

```text
PROTECTED_PERSONNEL_STORE_CONTAINS_SELECTION_CASE_PAYLOAD=NO
PROTECTED_PERSONNEL_STORE_CONTAINS_PRIVATE_GOLD_CASE_PAYLOAD=NO
PROTECTED_PERSONNEL_STORE_CONTAINS_PRIVATE_GOLD_ANSWERS_OR_RUBRICS=NO
PROTECTED_PERSONNEL_STORE_CONTAINS_CANDIDATE_OUTPUTS_OR_SCORES=NO
```

Gold nonexposure reconciliation must use role/access-event metadata only and must not require revealing the Gold content itself.

## 5. Data-minimization principle

The future implementation must collect and retain only evidence necessary to establish an exact governance fact for an exact role and scope.

```text
DATA_MINIMIZATION_REQUIRED=YES
PURPOSE_LIMITATION_REQUIRED=YES
COLLECT_JUST_IN_CASE_PERSONNEL_DATA=PROHIBITED
```

If a verified disposition can remain auditable using an evidence reference, digest, verifier record, and protected source locator, raw duplicates should not be multiplied across systems.

```text
DUPLICATE_RAW_CREDENTIAL_STORAGE_BY_DEFAULT=PROHIBITED
DUPLICATE_IDENTITY_DOCUMENT_STORAGE_BY_DEFAULT=PROHIBITED
```

Q2 does not require retention of raw identity documents after verification when a future lawful and scientifically sufficient verification record can preserve the needed governance fact.

```text
RAW_IDENTITY_DOCUMENT_RETENTION_ALWAYS_REQUIRED=NO
RAW_CREDENTIAL_DOCUMENT_RETENTION_ALWAYS_REQUIRED=NO
```

The exact evidence class that may be reduced to a verified record depends on implementation, legal obligations, auditability, and scientific reproducibility and remains unresolved until implementation review.

## 6. Sensitive attributes not to infer

A7 qualification evidence must not infer sensitive personal traits merely because a role needs competence evidence.

```text
INFER_NATIONALITY_FROM_ARABIC_COMPETENCE=PROHIBITED
INFER_ETHNICITY_FROM_DIALECT_COMPETENCE=PROHIBITED
INFER_RELIGION_FROM_LANGUAGE_OR_REGION=PROHIBITED
```

Where language or regional competence is scientifically necessary, the registry stores the scoped competence disposition and protected evidence reference, not an inferred demographic identity.

```text
SCOPED_LANGUAGE_COMPETENCE_DISPOSITION_ALLOWED=YES
SCOPED_REGIONAL_REGISTER_COMPETENCE_DISPOSITION_ALLOWED=YES
DEMOGRAPHIC_INFERENCE_FROM_COMPETENCE_EVIDENCE=PROHIBITED
```

## 7. Evidence sensitivity classes

Within the protected store, future records should be classified at least as:

```text
PROTECTED_STANDARD
PROTECTED_HIGH_SENSITIVITY
```

Examples of `PROTECTED_HIGH_SENSITIVITY` include:

```text
identity_documents
raw_professional_credential_documents
raw_conflict_or_financial_relationship_evidence
signed_private_gold_nonexposure_attestations
private_gold_access_reconciliation_records
personnel_investigation_or_correction_evidence
```

High-sensitivity evidence must receive narrower access than routine eligibility outputs.

```text
ALL_A7_VERIFIERS_AUTOMATICALLY_SEE_ALL_PROTECTED_EVIDENCE=NO
```

## 8. Functional verifier roles

Q2 freezes verifier functions without assigning real people:

```text
PERSONNEL_REGISTRY_CUSTODIAN
IDENTITY_VERIFIER
QUALIFICATION_VERIFIER
CONFLICT_REVIEWER
GOLD_EXPOSURE_RECONCILER
ROLE_ELIGIBILITY_COMPUTATION_SERVICE_OR_REVIEWER
GOVERNANCE_AUDITOR
PERSONNEL_RECORD_CORRECTION_REVIEWER
```

These functions are distinct from selection-content roles and from A13 payload roles.

```text
A7_VERIFIER_ROLE_AUTO_CREATES_SELECTION_PAYLOAD_ACCESS=NO
A7_VERIFIER_ROLE_AUTO_CREATES_CANDIDATE_RESULT_ACCESS=NO
A7_VERIFIER_ROLE_AUTO_CREATES_PRIVATE_GOLD_CASE_ACCESS=NO
```

## 9. Custody versus scientific adjudication

A registry custodian may operate storage or record lifecycle functions but may not unilaterally determine scientific qualification, conflict, or Gold-exposure eligibility by virtue of custody alone.

```text
CUSTODIAN_ROLE_ALONE_MAY_MARK_QUALIFIED=NO
CUSTODIAN_ROLE_ALONE_MAY_CLEAR_CONFLICT=NO
CUSTODIAN_ROLE_ALONE_MAY_MARK_GOLD_NONEXPOSED=NO
```

The exact verifier/approver separation model remains subject to implementation review, but the storage administrator cannot silently become the sole scientific authority.

## 10. Least-privilege verifier access

The default protected-evidence policy is deny.

```text
DEFAULT_PROTECTED_PERSONNEL_EVIDENCE_ACCESS=DENY
UNSCOPED_VERIFIER_ACCESS=PROHIBITED
BULK_BROWSE_BY_DEFAULT=PROHIBITED
```

An access grant must be limited by:

```text
personnel_or_case_scope
record_or_evidence_class
verification_purpose
allowed_action
start_condition
expiry_or_revocation_condition
```

A verifier should receive only the evidence necessary for the assigned decision.

Examples:

```text
IDENTITY_VERIFIER_NEEDS_FULL_CONFLICT_EVIDENCE_BY_DEFAULT=NO
QUALIFICATION_VERIFIER_NEEDS_RAW_FINANCIAL_CONFLICT_EVIDENCE_BY_DEFAULT=NO
CONFLICT_REVIEWER_NEEDS_PRIVATE_GOLD_CASE_CONTENT=NO
GOLD_EXPOSURE_RECONCILER_NEEDS_GOLD_CASE_TEXT=NO
```

## 11. Read versus write separation

```text
READ_ACCESS_IMPLIES_WRITE_ACCESS=NO
WRITE_METADATA_IMPLIES_EDIT_RAW_EVIDENCE=NO
VERIFY_EVIDENCE_IMPLIES_DELETE_EVIDENCE=NO
```

Raw evidence mutation, disposition issuance, correction, deletion, and export must be distinct controlled actions.

## 12. Protected access-event identity

Every protected-evidence access must be auditable.

Minimum future access-event fields:

```text
access_event_id
actor_governance_reference
verifier_role_class
personnel_reference_or_scope
evidence_record_id_or_class
action
purpose
authorization_reference
outcome
event_time
audit_record_sha256
```

Minimum action vocabulary:

```text
READ
VERIFY
WRITE_NEW_VERSION
ANNOTATE
EXPORT
CORRECT
SUSPEND
REVOKE
RETENTION_REVIEW
DELETE_OR_CRYPTOGRAPHIC_DESTROY_IF_GOVERNED
ACCESS_DENIED
```

```text
PROTECTED_ACCESS_AUDIT_APPEND_ONLY_OR_EQUIVALENT_TAMPER_EVIDENT=REQUIRED
FAILED_OR_DENIED_PROTECTED_ACCESS_AUDITED=YES
SILENT_ACCESS_LOG_REWRITE=PROHIBITED
```

## 13. No public audit leakage

Access auditing must not itself publish sensitive evidence.

```text
PUBLIC_AUDIT_LOG_MAY_CONTAIN_RAW_PERSONNEL_EVIDENCE=NO
PUBLIC_AUDIT_LOG_MAY_CONTAIN_REAL_NAME_BY_DEFAULT=NO
PUBLIC_AUDIT_LOG_MAY_CONTAIN_RAW_CONFLICT_DETAILS=NO
```

An opaque audit event identity and high-level disposition are sufficient for broadly visible governance where detailed evidence is not required.

## 14. Export restrictions

Protected evidence must not leave the governed boundary through ad hoc copies.

```text
COPY_TO_PUBLIC_REPOSITORY=PROHIBITED
COPY_TO_PUBLIC_CHAT_OR_ISSUE=PROHIBITED
COPY_TO_PERSONAL_CLOUD_STORAGE=PROHIBITED
COPY_TO_UNMANAGED_LOCAL_DEVICE=PROHIBITED_BY_DEFAULT
COPY_TO_UNAUTHORIZED_MODEL_OR_PROVIDER=PROHIBITED
```

Any future export must bind:

```text
export_authorization_id
actor_governance_reference
source_record_ids[]
destination_class
purpose
minimum_required_fields_or_redaction_policy
expiry_or_retention_condition_if_applicable
audit_event_id
```

```text
BULK_EXPORT_BY_DEFAULT=PROHIBITED
```

Q2 authorizes no export.

## 15. Model/provider boundary

Protected personnel evidence may not be sent to an external or local model simply because a model is available.

```text
PERSONNEL_EVIDENCE_SERIALIZATION_TO_MODEL=NOT_AUTHORIZED
PERSONNEL_EVIDENCE_UPLOAD_TO_PROVIDER=NOT_AUTHORIZED
LLM_ASSISTED_CREDENTIAL_OR_CONFLICT_REVIEW=NOT_AUTHORIZED_BY_Q2
```

Any future use would require separate privacy/security/rights governance and explicit authority.

## 16. Authentication and encryption baseline

The exact technology is not selected, but a future protected store must provide:

```text
ANONYMOUS_ACCESS=PROHIBITED
AUTHENTICATED_ROLE_BOUND_ACCESS_REQUIRED=YES
ENCRYPTED_TRANSPORT_REQUIRED=YES
ENCRYPTED_STORAGE_REQUIRED=YES
```

Unresolved:

```text
EXACT_PERSONNEL_EVIDENCE_STORAGE_VENDOR=NOT_YET_FROZEN
EXACT_STORAGE_REGION=NOT_YET_FROZEN
EXACT_KEY_MANAGEMENT_IMPLEMENTATION=NOT_YET_FROZEN
EXACT_IDENTITY_PROVIDER=NOT_YET_FROZEN
EXACT_AUTHENTICATION_FACTOR_POLICY=NOT_YET_FROZEN
```

Q2 does not provision any infrastructure.

## 17. Separation from A13 payload storage

The protected personnel evidence store and A13 selection-content payload store are distinct information domains.

```text
A7_PROTECTED_PERSONNEL_STORE_EQUALS_A13_ZONE2_PAYLOAD_STORE=NO
A7_PROTECTED_PERSONNEL_STORE_EQUALS_A13_ZONE3_RESULT_STORE=NO
```

A13 needs only a bounded A7 output such as:

```text
personnel_reference
role_assignment_id
role_class
suite_or_scope_id
assignment_state
eligibility_record_id
gold_exposure_disposition_reference_if_required
allowed_governance_actions
expiry_or_revocation_condition
```

A13 must not need raw credentials, identity documents, signed attestations, or raw conflict evidence to enforce an access grant.

```text
A13_ACCESS_CONTROL_CONSUMES_OPAQUE_A7_ELIGIBILITY_AND_ASSIGNMENT_REFERENCES=YES
A13_ACCESS_CONTROL_CONSUMES_RAW_A7_CREDENTIAL_DOCUMENTS=NO
```

## 18. Separation from Private Gold

The A7 protected evidence store may hold access-event metadata needed to reconcile Gold exposure, but not Gold case content.

```text
A7_PROTECTED_STORE_MAY_HOLD_GOLD_ACCESS_EVENT_REFERENCE=YES
A7_PROTECTED_STORE_MAY_HOLD_GOLD_ROLE_OR_AUTHORIZATION_REFERENCE=YES
A7_PROTECTED_STORE_MAY_HOLD_PRIVATE_GOLD_CASE_TEXT=NO
A7_PROTECTED_STORE_MAY_HOLD_PRIVATE_GOLD_ANSWER_OR_RUBRIC=NO
```

No verifier obtains Private Gold payload access merely to determine exposure status.

## 19. Correction versus deletion

Personnel evidence can be wrong. Correction must preserve the history of the governance decision without perpetuating incorrect data as current truth.

```text
SILENT_IN_PLACE_EVIDENCE_CORRECTION=PROHIBITED
SILENT_IN_PLACE_DISPOSITION_REWRITE=PROHIBITED
```

A correction must create a new version or correction record that binds:

```text
correction_record_id
subject_record_id
prior_record_sha256
correction_reason_class
corrected_record_id_or_disposition
reviewer_governance_reference
correction_evidence_reference
current_effective_state
record_canonical_sha256
```

The prior record remains historical but must be clearly marked superseded/non-current when appropriate.

```text
SUPERSEDED_INCORRECT_RECORD_MAY_REMAIN_CURRENT=NO
HISTORICAL_DECISION_CONTEXT_MUST_REMAIN_AUDITABLE=YES
```

## 20. Correction reason classes

Minimum future reason classes:

```text
IDENTITY_DATA_ERROR
CREDENTIAL_VERIFICATION_ERROR
QUALIFICATION_SCOPE_ERROR
CONFLICT_RECORD_ERROR
GOLD_EXPOSURE_RECONCILIATION_ERROR
DUPLICATE_PERSONNEL_RECORD
ROLE_ASSIGNMENT_SCOPE_ERROR
AUDIT_OR_SYSTEM_MIGRATION_ERROR
SUBJECT_PROVIDED_CORRECTION_WITH_VALID_EVIDENCE
```

Candidate performance or preferred outcome is not a valid correction reason.

```text
CANDIDATE_RESULT_DRIVEN_PERSONNEL_DISPOSITION_CORRECTION=PROHIBITED
```

## 21. Exposure-event correction boundary

An actual Gold exposure event is durable history when validly established, but erroneous exposure records must be correctable through evidence-bound governance.

```text
VALID_GOLD_EXPOSURE_EVENT_ERASED_BY_ROLE_REVOCATION=NO
VALID_GOLD_EXPOSURE_EVENT_ERASED_BY_SIMPLE_REQUEST=NO
ERRONEOUS_GOLD_EXPOSURE_EVENT_MAY_BE_CORRECTED_WITH_EVIDENCE_AND_REVIEW=YES
```

A correction must not imply that previously recorded access evidence never existed; it must explain why the prior disposition was erroneous or superseded.

## 22. Suspension on unresolved correction

If a correction request could materially affect active role eligibility and cannot be resolved immediately:

```text
ACTIVE_ROLE_STATUS=SUSPEND_PENDING_REVIEW
NEW_PROTECTED_EVIDENCE_ACCESS=DENY_IF_NOT_REQUIRED_FOR_REVIEW
NEW_SELECTION_PAYLOAD_ACCESS=DENY
NEW_CONTENT_WRITE=DENY
NEW_FINAL_REVIEW_ACCEPTANCE=DENY
```

Historical frozen scientific artifacts remain unchanged pending the personnel-governance resolution.

## 23. Data-subject correction channel

A future implementation must provide a governed means for a person to challenge or correct factual records about themselves without giving them unilateral authority over eligibility outcomes.

```text
PERSON_MAY_REQUEST_RECORD_CORRECTION=YES
PERSON_MAY_UNILATERALLY_SET_ELIGIBILITY_DISPOSITION=NO
PERSON_MAY_UNILATERALLY_DELETE_CONFLICT_HISTORY=NO
PERSON_MAY_UNILATERALLY_DELETE_VALID_GOLD_EXPOSURE_HISTORY=NO
```

The exact user interface or process is not frozen.

## 24. Retention architecture

Q2 does not choose one arbitrary global retention period.

```text
ONE_RETENTION_DURATION_FOR_ALL_PERSONNEL_EVIDENCE=PROHIBITED
EXACT_NUMERIC_RETENTION_PERIODS=NOT_YET_FROZEN
```

Retention must be defined by data class, purpose, active governance need, reproducibility need, legal obligation where applicable, and minimization.

At minimum the future policy must distinguish:

```text
RAW_IDENTITY_OR_CREDENTIAL_EVIDENCE
SIGNED_ATTESTATION_EVIDENCE
RAW_CONFLICT_EVIDENCE
GOLD_EXPOSURE_RECONCILIATION_EVIDENCE
OPAQUE_ELIGIBILITY_AND_ASSIGNMENT_RECORDS
ROLE_TRANSITION_AND_REVOCATION_RECORDS
AUDIT_EVENTS
CORRECTION_HISTORY
```

## 25. Active-state retention

While a person has an active assignment or an eligibility decision is being relied upon:

```text
EVIDENCE_NEEDED_TO_SUPPORT_ACTIVE_GOVERNANCE_DECISION_MUST_REMAIN_AVAILABLE=YES
```

However, raw evidence duplication remains prohibited and unnecessary evidence should not be retained solely because an assignment is active.

## 26. Historical reproducibility versus raw-data retention

Scientific reproducibility often requires knowing **which decision was in force**, not retaining every raw personal document indefinitely.

Therefore a future policy may retain long-lived opaque historical records such as:

```text
personnel_reference
role_assignment_id
eligibility_disposition
conflict_disposition
gold_exposure_disposition
policy_identity
record_hash
supersession_or_revocation_state
```

while allowing raw supporting evidence to expire or be destroyed when no longer required by the governed purpose, audit need, dispute/legal requirement, or implementation policy.

```text
HISTORICAL_GOVERNANCE_REPRODUCIBILITY_REQUIRES_INDEFINITE_RAW_IDENTITY_DOCUMENT_RETENTION=NO
```

## 27. Event-driven retention review

Retention must be reconsidered on material events including:

```text
ROLE_EXPIRY
ROLE_REVOCATION
PERSONNEL_RETIREMENT_FROM_REGISTRY_SCOPE
QUALIFICATION_REPLACEMENT_OR_EXPIRY
CONFLICT_RESOLUTION_OR_SUPERSESSION
GOLD_EXPOSURE_EVENT
CORRECTION_OR_APPEAL_CLOSURE
LEGAL_OR_AUDIT_HOLD_START
LEGAL_OR_AUDIT_HOLD_RELEASE
REGISTRY_MIGRATION
```

```text
EVENT_DRIVEN_RETENTION_REVIEW_REQUIRED=YES
FIXED_REVIEW_INTERVAL_MAY_BE_ADDED_LATER=YES
EXACT_PERIODIC_RETENTION_REVIEW_INTERVAL=NOT_YET_FROZEN
```

## 28. Destruction semantics

When protected raw evidence is eligible for deletion/destruction under a future policy:

```text
DELETION_OR_CRYPTOGRAPHIC_DESTRUCTION_MUST_BE_AUTHORIZED_AND_AUDITED=YES
UNLOGGED_DELETION=PROHIBITED
```

A minimal tombstone may remain to prove that an evidence object existed and was governed, provided it does not recreate sensitive content.

Potential tombstone fields:

```text
record_id
prior_record_sha256
evidence_class
destruction_authorization_id
destruction_event_id
destruction_disposition
```

```text
TOMBSTONE_MAY_EMBED_DESTROYED_RAW_EVIDENCE=NO
```

## 29. Legal/audit holds

Q2 does not determine a jurisdiction-specific retention law. A future implementation must be able to suspend ordinary destruction when a valid legal, security, investigation, or audit hold exists.

```text
VALID_HOLD_OVERRIDES_NORMAL_DESTRUCTION_SCHEDULE=YES
HOLD_SCOPE_MUST_BE_MINIMIZED=YES
HOLD_MUST_BE_AUDITABLE=YES
```

A hold must not silently broaden role or payload access.

```text
RETENTION_HOLD_IMPLIES_ACCESS_GRANT=NO
```

## 30. Revocation semantics

Role revocation and evidence retention are distinct.

```text
ROLE_REVOCATION_REQUIRES_A13_ACCESS_REVOCATION_IF_ACCESS_EXISTS=YES
ROLE_REVOCATION_AUTO_DELETES_PERSONNEL_EVIDENCE=NO
ROLE_REVOCATION_AUTO_ERASES_HISTORICAL_GOVERNANCE_DECISIONS=NO
```

Revoked access must cease according to the future exact enforcement mechanism; evidence needed to prove why the revocation occurred may remain under the retention policy.

## 31. Security incident or unauthorized-access response

The future protected registry must have a fail-closed response for suspected unauthorized access, evidence tampering, or exposure.

At minimum:

```text
SUSPECTED_UNAUTHORIZED_ACCESS -> SUSPEND_AFFECTED_ACCESS_WHERE_SAFE
SUSPECTED_EVIDENCE_TAMPERING -> BLOCK_AFFECTED_DISPOSITION_RELIANCE
SUSPECTED_CREDENTIAL_OR_ATTESTATION_LEAK -> ROTATE_OR_REVOKE_RELEVANT_ACCESS_MECHANISMS
MATERIAL_INCIDENT -> CREATE_INCIDENT_RECORD_AND_SCOPE_REVIEW
```

Q2 does not freeze an incident-response vendor or notification workflow.

```text
EXACT_INCIDENT_RESPONSE_IMPLEMENTATION=UNRESOLVED
```

## 32. Breach does not silently alter scientific records

A privacy/security incident may invalidate confidence in a personnel decision, but it must not silently rewrite already-frozen scientific history.

```text
INCIDENT_MAY_TRIGGER_PERSONNEL_ROLE_SUSPENSION=YES
INCIDENT_MAY_TRIGGER_FRESH_ELIGIBILITY_REVIEW=YES
INCIDENT_SILENTLY_REWRITES_HISTORICAL_SUITE_IDENTITY=NO
```

If a validly established personnel-governance defect materially undermines a historical scientific artifact, the consequence must be handled through separately governed scientific change-control rather than retroactive file mutation.

## 33. Backup and replica rules

Backups and replicas count as protected evidence copies.

```text
BACKUP_COUNTS_AS_PROTECTED_PERSONNEL_EVIDENCE_COPY=YES
BACKUP_ACCESS_CONTROL_MUST_BE_NO_WEAKER_THAN_PRIMARY=YES
UNENCRYPTED_UNCONTROLLED_BACKUP=PROHIBITED
PUBLIC_BACKUP_OR_SNAPSHOT=PROHIBITED
```

Retention/destruction policies must account for backups rather than deleting only the primary record and assuming the evidence is gone.

```text
BACKUP_RETENTION_MUST_ALIGN_WITH_GOVERNED_RETENTION_POLICY=YES
```

## 34. Integrity and identity binding

Each protected evidence record must be identity-bound.

```text
PROTECTED_RECORD_ID_REQUIRED=YES
PROTECTED_RECORD_VERSION_REQUIRED=YES
PROTECTED_RECORD_CANONICAL_SHA256_REQUIRED=YES
```

Where a raw binary artifact cannot be semantically canonicalized, exact byte digest or immutable revision identity is required.

```text
RAW_EVIDENCE_ARTIFACT_IDENTITY_REQUIRED=YES
PROTECTED_EVIDENCE_DIGEST_MISMATCH=BLOCKED
```

## 35. Eligibility consumption boundary

Downstream consumers must receive only the minimum authoritative decision output required for their function.

For A8 review assignment, A9 metadata, and A13 access control, the authoritative inputs should be opaque records such as:

```text
personnel_reference
role_eligibility_record_id
role_assignment_id
qualification_disposition
conflict_disposition
gold_exposure_disposition_reference
assignment_state
suite_or_scope_id
record_canonical_sha256
```

Downstream consumers must not recompute qualification from raw protected documents.

```text
A8_RECOMPUTES_A7_QUALIFICATION_FROM_RAW_EVIDENCE=NO
A9_EMBEDS_A7_RAW_EVIDENCE=NO
A13_RECOMPUTES_A7_GOLD_NONEXPOSURE_FROM_RAW_EVIDENCE=NO
```

A7 remains authoritative for personnel eligibility; A13 remains authoritative for resource access enforcement.

## 36. Protected verifier independence/conflicts

A person verifying protected evidence must themselves have a scoped governance identity and conflict disposition appropriate to the decision.

```text
ANONYMOUS_VERIFIER=PROHIBITED
UNBOUND_VERIFIER_IDENTITY=PROHIBITED
VERIFIER_WITH_MATERIAL_CONFLICT_FOR_DECISION=BLOCKED
```

Self-verification is prohibited for material eligibility evidence.

```text
PERSON_MAY_BE_SOLE_VERIFIER_OF_OWN_IDENTITY_EVIDENCE=NO
PERSON_MAY_BE_SOLE_VERIFIER_OF_OWN_QUALIFICATION_EVIDENCE=NO
PERSON_MAY_BE_SOLE_CONFLICT_REVIEWER_FOR_OWN_DISCLOSURE=NO
PERSON_MAY_BE_SOLE_GOLD_EXPOSURE_RECONCILER_FOR_OWN_RECORD=NO
```

Q2 does not freeze the exact number of verifiers per evidence class beyond prohibiting sole self-verification.

## 37. Request-to-know / verifier minimization

Verification tasks should expose evidence through task-scoped views rather than unrestricted archive browsing where technically feasible.

```text
TASK_SCOPED_EVIDENCE_VIEW_PREFERRED=YES
FULL_ARCHIVE_BROWSE_NOT_REQUIRED_FOR_ROUTINE_VERIFICATION=YES
```

The exact implementation is unresolved.

## 38. Public/private consistency

Every public opaque disposition must resolve to one valid protected authoritative record or a documented protected record set.

```text
PUBLIC_OPAQUE_DISPOSITION_WITHOUT_PROTECTED_AUTHORITY=BLOCKED
PROTECTED_RECORD_VERSION_MISMATCH=BLOCKED
PUBLIC_HASH_MISMATCH_WITH_PROTECTED_RECORD=BLOCKED
```

A protected record may contain more detail than the public index, but it may not contradict the published disposition without creating a new version/correction record.

## 39. No sensitive information in candidate-result domain

Candidate result records need personnel role references only when necessary for audit. They must not contain raw credential, conflict, or nonexposure evidence.

```text
ZONE3_RESULT_STORE_CONTAINS_RAW_A7_PERSONNEL_EVIDENCE=NO
```

Result analysts must not gain protected A7 evidence access merely because they have result access.

## 40. No sensitive information in selection payload domain

Likewise:

```text
ZONE2_SELECTION_PAYLOAD_STORE_CONTAINS_RAW_A7_PERSONNEL_EVIDENCE=NO
```

A content artifact may reference an opaque author/reviewer governance ID but not embed credential or conflict records.

## 41. Current unresolved implementation choices

```text
EXACT_A7_PROTECTED_STORAGE_VENDOR=NOT_YET_FROZEN
EXACT_A7_PROTECTED_STORAGE_REGION=NOT_YET_FROZEN
EXACT_A7_IDENTITY_PROVIDER=NOT_YET_FROZEN
EXACT_A7_KEY_MANAGEMENT=NOT_YET_FROZEN
EXACT_A7_ACCESS_CONTROL_IMPLEMENTATION=UNRESOLVED
EXACT_A7_AUDIT_LOG_IMPLEMENTATION=UNRESOLVED
EXACT_A7_BACKUP_IMPLEMENTATION=UNRESOLVED
EXACT_A7_RETENTION_DURATIONS_BY_CLASS=NOT_YET_FROZEN
EXACT_A7_DESTRUCTION_IMPLEMENTATION=UNRESOLVED
EXACT_A7_CORRECTION_WORKFLOW_IMPLEMENTATION=UNRESOLVED
EXACT_A7_INCIDENT_RESPONSE_IMPLEMENTATION=UNRESOLVED
EXACT_A7_VERIFIER_IDENTITIES=UNRESOLVED
```

## 42. Future operational PASS evidence

Before this protected-registry component may be considered operationally PASS, future canonical evidence must prove at least:

```text
EXACT_PROTECTED_STORAGE_BOUNDARY_IDENTITY
EXACT_SURFACE1_SURFACE2_SEPARATION_MECHANISM
EXACT_ACCESS_CONTROL_IMPLEMENTATION
EXACT_VERIFIER_ROLE_AND_SCOPE_BINDING
EXACT_ENCRYPTED_STORAGE_AND_TRANSPORT_POSTURE
EXACT_AUDIT_LOG_IMPLEMENTATION
EXACT_CORRECTION_AND_SUPERSESSION_MECHANISM
EXACT_RETENTION_POLICY_BY_EVIDENCE_CLASS
EXACT_DELETION_OR_DESTRUCTION_MECHANISM
EXACT_BACKUP_AND_REPLICA_POSTURE
EXACT_INCIDENT_RESPONSE_POSTURE
EXACT_A13_OPAQUE_REFERENCE_INTEGRATION
EXACT_PERSONNEL_ROSTER_AND_PROTECTED_EVIDENCE_BINDINGS
FRESH_INDEPENDENT_GOVERNANCE_REVIEW
```

Q2 proves none of these implementation facts by itself.

## 43. Fail-closed conditions

A future implementation must fail closed on at least:

```text
RAW_PERSONNEL_EVIDENCE_IN_PUBLIC_REPOSITORY
PUBLICLY_EXPOSED_IDENTITY_OR_CREDENTIAL_DOCUMENTS
ANONYMOUS_PROTECTED_EVIDENCE_ACCESS
UNSCOPED_VERIFIER_ACCESS
UNAUDITED_PROTECTED_EVIDENCE_READ_OR_EXPORT
UNMANAGED_RAW_EVIDENCE_COPY
PROTECTED_RECORD_DIGEST_MISMATCH
PUBLIC_OPAQUE_DISPOSITION_WITHOUT_PROTECTED_AUTHORITY
SILENT_IN_PLACE_CORRECTION
SILENT_IN_PLACE_DISPOSITION_REWRITE
SELF_VERIFICATION_AS_SOLE_MATERIAL_VERIFICATION
UNRESOLVED_VERIFIER_CONFLICT
RETENTION_HOLD_USED_AS_ACCESS_GRANT
ROLE_REVOCATION_WITHOUT_REQUIRED_A13_ACCESS_REVOCATION
PROTECTED_PERSONNEL_EVIDENCE_IN_SELECTION_PAYLOAD_OR_RESULT_STORE
```

## 44. Current readiness

```text
A7_PROTECTED_EVIDENCE_REGISTRY_IMPLEMENTATION=NO
EXACT_A7_PROTECTED_STORAGE_BOUNDARY=UNRESOLVED
EXACT_A7_VERIFIER_ROSTER=UNRESOLVED
EXACT_A7_PERSONNEL_EVIDENCE=UNRESOLVED
EXACT_A7_RETENTION_POLICY_BY_CLASS=UNRESOLVED
EXACT_A7_ACCESS_CONTROL_IMPLEMENTATION=UNRESOLVED

A7_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
```

## 45. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE

A7_PROTECTED_STORAGE_PROVISIONING_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_INGEST_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_ACCESS_AUTHORITY=NONE
A7_PERSONNEL_VERIFICATION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A7_QUALIFICATION_ADJUDICATION_AUTHORITY=NONE
A7_GOLD_NONEXPOSURE_ATTESTATION_EXECUTION_AUTHORITY=NONE
A7_ROLE_TRANSITION_EXECUTION_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_EXPORT_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_DESTRUCTION_AUTHORITY=NONE

A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY=NONE
A13_PAYLOAD_UPLOAD_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE
A13_ROLE_ASSIGNMENT_AUTHORITY=NONE

ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
```

## 46. Session 13 state after Q2

Acceptance of Q2 advances bounded Session 13 only.

```text
CLARIFICATION_SESSION_13=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

No A1–A15 implementation gate becomes operationally PASS merely because its clarification design is frozen.