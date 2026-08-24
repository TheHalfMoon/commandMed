# Session 13 Q1 — Personnel Qualification, Private-Gold Nonexposure, and Role-Transition Registry

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 13 Q1 only. It freezes the governance design for A7: the personnel qualification, conflict, Private-Gold nonexposure, role-assignment, and role-transition registry that must exist before any person may receive a formal Spec 005 Arabic selection-suite content role. It does **not** identify, recruit, assign, approve, compensate, credential, or grant access to any person; access Private Gold; create or review cases; provision storage; run contamination assessment; execute models; spend funds; implement A1; authorize A15; or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION13_Q1_POLICY=QUALIFICATION_BOUND_OPAQUE_PERSONNEL_REGISTRY_WITH_FAIL_CLOSED_GOLD_NONEXPOSURE_AND_ROLE_TRANSITION_FIREWALL

A7_GOVERNANCE_DESIGN=FROZEN
A7_IMPLEMENTED_AND_EXECUTED=NO
A7_GATE_STATUS=BLOCKED_PENDING_CANONICAL_REGISTRY_ATTESTATIONS_EXACT_ROSTER_AND_INDEPENDENT_REVIEW

CLARIFICATION_SESSION_13=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

A7 is a personnel-governance prerequisite. A7 design freeze does not create a roster and does not grant any A13 payload role.

```text
A7_PASS_EQUALS_ROLE_GRANT=NO
A7_PASS_EQUALS_PAYLOAD_ACCESS=NO
A7_PASS_EQUALS_CONSTRUCTION_AUTHORITY=NO
A7_PASS_EQUALS_REVIEW_EXECUTION_AUTHORITY=NO
```

## 2. Governing separation

The future process must separate four decisions that must not be conflated:

```text
1. PERSON_IDENTITY_REGISTRATION
2. ROLE_SPECIFIC_QUALIFICATION_ELIGIBILITY
3. ROLE_ASSIGNMENT_OR_GRANT
4. PAYLOAD_OR_RESULT_ACCESS
```

A person may be qualified but not assigned; assigned but not yet granted payload access; or granted one scoped capability without receiving unrelated access.

```text
QUALIFIED_IMPLIES_ASSIGNED=NO
ASSIGNED_IMPLIES_PAYLOAD_ACCESS=NO
PAYLOAD_ACCESS_IMPLIES_WRITE_ACCESS=NO
ORGANIZATIONAL_TITLE_IMPLIES_SCIENTIFIC_AUTHORITY=NO
```

A13 remains authoritative for actual payload access-control implementation.

## 3. Registry record types

The future A7 registry must support logically separate identity-bound records:

```text
A7_RECORD_1=PERSONNEL_REGISTRY_HEADER
A7_RECORD_2=PERSONNEL_IDENTITY_RECORD
A7_RECORD_3=QUALIFICATION_EVIDENCE_RECORD
A7_RECORD_4=CONFLICT_DISCLOSURE_AND_DISPOSITION_RECORD
A7_RECORD_5=PRIVATE_GOLD_NONEXPOSURE_ATTESTATION_RECORD
A7_RECORD_6=PRIVATE_GOLD_EXPOSURE_EVENT_RECORD
A7_RECORD_7=ROLE_ELIGIBILITY_RECORD
A7_RECORD_8=ROLE_ASSIGNMENT_RECORD
A7_RECORD_9=ROLE_TRANSITION_RECORD
A7_RECORD_10=ROLE_REVOCATION_OR_SUSPENSION_RECORD
```

Each record must have deterministic identity and versioning.

```text
RECORD_ID_REQUIRED=YES
RECORD_VERSION_REQUIRED=YES
RECORD_CANONICAL_SHA256_REQUIRED=YES
SILENT_IN_PLACE_PERSONNEL_RECORD_REINTERPRETATION=PROHIBITED
```

## 4. Data-minimization and public-repository boundary

The open repository must not become a personnel credential store.

Public or broadly visible Spec 005 metadata may contain only opaque governance references and non-sensitive eligibility/disposition values needed for reproducibility.

```text
PUBLIC_REPOSITORY_PERSONNEL_REFERENCE=OPAQUE_ID_ONLY
PUBLIC_REPOSITORY_REAL_NAME_REQUIRED=NO
PUBLIC_REPOSITORY_EMAIL_REQUIRED=NO
PUBLIC_REPOSITORY_PHONE_REQUIRED=NO
PUBLIC_REPOSITORY_LICENSE_NUMBER_REQUIRED=NO
PUBLIC_REPOSITORY_IDENTITY_DOCUMENT_REQUIRED=NO
PUBLIC_REPOSITORY_CREDENTIAL_DOCUMENT_REQUIRED=NO
PUBLIC_REPOSITORY_SIGNED_ATTESTATION_CONTENT_REQUIRED=NO
```

Sensitive identity, credential, employment, conflict, or signed-attestation evidence must remain in a separately controlled personnel-governance store if later implemented.

```text
A7_PERSONNEL_REGISTRY_CONTAINS_CASE_PAYLOAD=NO
A7_PERSONNEL_REGISTRY_CONTAINS_PRIVATE_GOLD_CASE_CONTENT=NO
A7_PERSONNEL_REGISTRY_CONTAINS_CANDIDATE_OUTPUTS=NO
```

## 5. Personnel identity record

Minimum future personnel identity fields:

```text
personnel_reference
personnel_record_version
identity_verification_evidence_reference
identity_status
registry_scope
record_canonical_sha256
```

Allowed identity-status vocabulary:

```text
VERIFIED
PENDING_VERIFICATION
SUSPENDED
RETIRED
```

```text
PENDING_VERIFICATION_MAY_RECEIVE_FORMAL_ROLE_GRANT=NO
SUSPENDED_MAY_RECEIVE_ACTIVE_ROLE_GRANT=NO
```

The exact identity-verification technology is not frozen.

## 6. Functional role classes

A7 must be able to qualify and bind the functional roles already introduced by A8 and A13:

```text
ROOT_CONTENT_AUTHOR
PAIR_ADAPTER_OR_PARALLEL_AUTHOR
CLINICAL_PAIR_REVIEWER
CLINICAL_ADJUDICATOR
RIGHTS_PRIVACY_PROVENANCE_REVIEWER
PAYLOAD_CUSTODIAN
CONTAMINATION_ASSESSOR
EVALUATION_EXECUTOR
CANDIDATE_RESULT_ANALYST
PRIVATE_GOLD_TRUSTEE_OR_FINAL_AUDIT_ROLE
```

These are capability/governance roles, not job titles.

```text
JOB_TITLE_ALONE_PROVES_ROLE_QUALIFICATION=NO
FOUNDER_STATUS_ALONE_PROVES_ROLE_QUALIFICATION=NO
REPOSITORY_COLLABORATOR_STATUS_ALONE_PROVES_ROLE_QUALIFICATION=NO
```

## 7. Qualification evidence model

Every role eligibility decision must bind evidence relevant to the exact role and scope.

Minimum qualification-evidence fields:

```text
qualification_evidence_id
personnel_reference
role_class
qualification_scope
competence_domains[]
evidence_type
evidence_reference
verification_disposition
verifier_governance_reference
validity_or_review_condition
record_canonical_sha256
```

Allowed qualification dispositions:

```text
QUALIFIED
QUALIFIED_WITH_SCOPE_LIMIT
INELIGIBLE
BLOCKED_PENDING_EVIDENCE
```

```text
BLOCKED_PENDING_EVIDENCE_MAY_RECEIVE_ROLE_GRANT=NO
INELIGIBLE_MAY_RECEIVE_ROLE_GRANT=NO
QUALIFIED_WITH_SCOPE_LIMIT_MAY_EXCEED_SCOPE=NO
```

A7 does not freeze one global credential jurisdiction, degree name, or professional board. Evidence must be scientifically appropriate and independently verifiable for the assigned scope.

## 8. Root-content author qualification

The root semantic specification establishes clinical facts, intended safe behavior, and task meaning. Clinical scientific responsibility therefore requires documented clinical competence.

```text
ROOT_CONTENT_AUTHOR_CLINICAL_COMPETENCE_REQUIRED=YES
ROOT_CONTENT_AUTHOR_ASSIGNED_DOMAIN_COMPETENCE_REQUIRED=YES
ROOT_CONTENT_AUTHOR_ROLE_AND_USE_CONTEXT_COMPETENCE_REQUIRED=YES
```

For clinically material root content, at least one person holding scientific author responsibility must have a recognized clinical professional qualification appropriate to the content domain.

```text
ROOT_SCIENTIFIC_RESPONSIBILITY_REQUIRES_RECOGNIZED_CLINICAL_PROFESSIONAL=YES
```

Language editors or non-clinical contributors may assist only through separately scoped roles and may not replace clinical scientific responsibility.

## 9. Pair-adapter or parallel-author qualification

The Arabic-English pair role may change safety-relevant meaning and therefore requires documented clinical-language competence.

```text
PAIR_ADAPTER_ARABIC_ENGLISH_COMPETENCE_REQUIRED=YES
PAIR_ADAPTER_CLINICAL_LANGUAGE_COMPETENCE_REQUIRED=YES
PAIR_ADAPTER_ASSIGNED_ANCHOR_COMPETENCE_REQUIRED_WHERE_APPLICABLE=YES
```

For Saudi/Gulf colloquial, code-switching, or local medication nomenclature content:

```text
RELEVANT_REGIONAL_OR_REGISTER_COMPETENCE_REQUIRED=YES
```

A pair adapter need not independently satisfy the final clinical-review credential if their role is strictly adaptation and the root scientific responsibility plus independent clinical review remain intact.

```text
PAIR_ADAPTER_AUTOMATICALLY_COUNTS_AS_FINAL_CLINICAL_REVIEWER=NO
```

## 10. Clinical pair-reviewer qualification

Every final pair reviewer must be a recognized clinical professional and must be able to assess the matched Arabic-English clinical task.

```text
EACH_FINAL_PAIR_REVIEWER_RECOGNIZED_CLINICAL_PROFESSIONAL=YES
EACH_FINAL_PAIR_REVIEWER_CLINICAL_DOMAIN_COMPETENCE_REQUIRED=YES
BILINGUAL_CLINICAL_COMPARISON_COMPETENCE_REQUIRED_ACROSS_REVIEW_PAIR=YES
```

The reviewer pair must collectively satisfy the already-frozen language requirements:

```text
AT_LEAST_ONE_FINAL_REVIEWER_NATIVE_ARABIC_SPEAKING_CLINICAL_PROFESSIONAL=YES
REGIONAL_OR_DIALECT_COMPETENCE_REQUIRED_WHERE_SEMANTICALLY_APPLICABLE=YES
```

A7 does not publish or infer anyone's language, nationality, ethnicity, or professional identity; qualification evidence is bound through protected governance references.

## 11. Clinical adjudicator qualification

An adjudicator resolving material reviewer disagreement must satisfy at least reviewer-level clinical competence for the disputed content and must be capable of independently assessing the Arabic-English clinical meaning.

```text
ADJUDICATOR_RECOGNIZED_CLINICAL_PROFESSIONAL=YES
ADJUDICATOR_BILINGUAL_CLINICAL_COMPARISON_COMPETENCE_REQUIRED=YES
ADJUDICATOR_ASSIGNED_DOMAIN_COMPETENCE_REQUIRED=YES
ADJUDICATOR_REGIONAL_OR_DIALECT_COMPETENCE_REQUIRED_WHERE_APPLICABLE=YES
```

For an Arabic semantic dispute, the adjudicator must have professional-level Arabic clinical competence; a purely administrative tie-breaker is prohibited.

## 12. Rights/privacy/provenance reviewer qualification

This role requires documented competence applying the exact A5/A6/Spec 003 governance contracts to the assigned source/evidence scope.

```text
RIGHTS_PRIVACY_PROVENANCE_REVIEWER_POLICY_COMPETENCE_REQUIRED=YES
LEGAL_COUNSEL_TITLE_AUTOMATICALLY_REQUIRED_BY_A7=NO
CLINICAL_PROFESSIONAL_TITLE_AUTOMATICALLY_REQUIRED_BY_A7=NO
```

The role may block admission but may not rewrite clinical content or expand rights by interpretation.

## 13. Payload-custodian qualification

A payload custodian requires documented security/operations competence appropriate to the future A13 implementation.

```text
PAYLOAD_CUSTODIAN_SECURITY_OPERATIONS_COMPETENCE_REQUIRED=YES
PAYLOAD_CUSTODIAN_SCIENTIFIC_EDIT_AUTHORITY_BY_ROLE=NO
```

Administrative capability alone does not authorize plaintext scientific-content inspection.

## 14. Contamination-assessor qualification

A contamination assessor requires documented competence with the predeclared A11 exact/semantic methods and evidence-binding rules.

```text
CONTAMINATION_ASSESSOR_METHOD_COMPETENCE_REQUIRED=YES
CONTAMINATION_ASSESSOR_A11_PROTOCOL_COMPETENCE_REQUIRED=YES
CONTAMINATION_ASSESSOR_MAY_EDIT_SELECTION_CONTENT=NO
```

Exact method-specific credentials cannot be frozen until the A11 implementation/method registry is canonical.

## 15. Evaluation-executor qualification

An evaluation executor requires documented competence operating the future frozen harness and identity-bound manifest without editing scientific content.

```text
EVALUATION_EXECUTOR_HARNESS_COMPETENCE_REQUIRED=YES
EVALUATION_EXECUTOR_CONTENT_EDIT_AUTHORITY=NO
EVALUATION_EXECUTOR_SCORING_POLICY_EDIT_AUTHORITY=NO
```

No evaluation executor is assigned by Q1.

## 16. Candidate-result analyst qualification

A result analyst requires documented statistical/evaluation competence appropriate to the future ranking and qualification analysis.

```text
CANDIDATE_RESULT_ANALYST_EVALUATION_COMPETENCE_REQUIRED=YES
CANDIDATE_RESULT_ANALYST_RESULT_ACCESS_IMPLIES_CONTENT_EDIT_AUTHORITY=NO
```

Any final scientific decision authority remains separately governed; A7 does not create a winner-selection authority.

## 17. Private-Gold trustee/final-audit role

The Private-Gold trustee/final-audit role belongs to the separate Gold trust domain.

```text
PRIVATE_GOLD_TRUSTEE_ROLE_IS_SELECTION_CONTENT_ROLE=NO
PRIVATE_GOLD_TRUSTEE_ROLE_GRANT_ALONE_EQUALS_CASE_CONTENT_EXPOSURE=NO
ACTUAL_PRIVATE_GOLD_CASE_CONTENT_ACCESS_IS_CONTROLLING=YES
```

Q1 does not authorize this role or access to Gold.

## 18. Private-Gold exposure disposition vocabulary

The future A7 registry must use the following closed exposure-disposition vocabulary:

```text
NO_KNOWN_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE
PUBLIC_GOLD_PROTOCOL_METADATA_ONLY
PRIVATE_GOLD_CASE_CONTENT_EXPOSED
UNKNOWN_OR_UNRESOLVED
CONFLICTING_EVIDENCE
```

Semantics:

```text
NO_KNOWN_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE=
  no known case-content exposure after required attestation and available-record reconciliation

PUBLIC_GOLD_PROTOCOL_METADATA_ONLY=
  exposure limited to public protocol/taxonomy metadata; not private case content

PRIVATE_GOLD_CASE_CONTENT_EXPOSED=
  actual private case, answer, rubric, hidden case-derived content, or materially equivalent protected content was accessed

UNKNOWN_OR_UNRESOLVED=
  required evidence is missing or exposure history cannot be resolved

CONFLICTING_EVIDENCE=
  attestation and available access/audit evidence materially disagree
```

A clean disposition is not a metaphysical proof that exposure could never have occurred.

```text
NO_KNOWN_EXPOSURE_EQUALS_ABSOLUTE_PROOF_OF_NO_EXPOSURE=NO
```

## 19. Gold-nonexposure evidence requirements

Before a person may receive a content-facing selection role, the registry must bind a nonexposure evidence package.

Required evidence classes, where applicable and available, include:

```text
PERSON_SIGNED_OR_EQUIVALENT_NONEXPOSURE_ATTESTATION
PRIVATE_GOLD_ACCESS_REGISTRY_CHECK
KNOWN_GOLD_TRUSTEE_OR_FINAL_AUDIT_ROSTER_CHECK
KNOWN_GOLD_WORKSPACE_ACCESS_LOG_RECONCILIATION
PRIOR_RECORDED_GOLD_EXPOSURE_EVENT_CHECK
```

```text
SELF_ATTESTATION_ALONE_AUTOMATICALLY_PROVES_CLEAN=NO
KNOWN_CONTRADICTORY_ACCESS_EVIDENCE_MAY_BE_IGNORED=NO
MISSING_REQUIRED_RECONCILIATION_EVIDENCE=BLOCKED
```

The evidence review itself must not reveal Gold case content; it needs access-event/role metadata only.

```text
NONEXPOSURE_VERIFICATION_REQUIRES_PRIVATE_GOLD_CASE_CONTENT_ACCESS=NO
```

## 20. Eligibility consequence of Gold exposure

Under the current selection firewall, the following roles require an eligible nonexposure disposition before assignment:

```text
ROOT_CONTENT_AUTHOR
PAIR_ADAPTER_OR_PARALLEL_AUTHOR
CLINICAL_PAIR_REVIEWER
CLINICAL_ADJUDICATOR
```

Eligible dispositions:

```text
NO_KNOWN_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE
PUBLIC_GOLD_PROTOCOL_METADATA_ONLY
```

Fail-closed dispositions:

```text
UNKNOWN_OR_UNRESOLVED=BLOCKED
CONFLICTING_EVIDENCE=BLOCKED
PRIVATE_GOLD_CASE_CONTENT_EXPOSED=INELIGIBLE_UNDER_CURRENT_POLICY
```

The exposure restriction applies to prior exposure, not merely current role title.

```text
ROLE_TITLE_ALONE_EQUALS_GOLD_EXPOSURE=NO
RECORDED_PRIVATE_GOLD_CASE_ACCESS_EVENT_UPDATES_EXPOSURE_DISPOSITION=YES
```

A person with actual prior Private-Gold case-content exposure may not be reclassified as clean merely because access was later revoked.

```text
GOLD_ACCESS_REVOCATION_ERASES_PRIOR_EXPOSURE=NO
```

## 21. Human Zone-2 plaintext-access rule

To reinforce A13 trust-domain separation, any future human role receiving plaintext Zone-2 selection-content access before candidate selection completes must have a resolved Gold-exposure disposition.

```text
HUMAN_ZONE2_PLAINTEXT_ACCESS_WITH_UNKNOWN_GOLD_EXPOSURE=PROHIBITED
HUMAN_ZONE2_PLAINTEXT_ACCESS_WITH_PRIVATE_GOLD_CASE_EXPOSURE=PROHIBITED_UNDER_CURRENT_POLICY
```

Machine/service identities with no human-readable plaintext access remain governed by A13 implementation security and are not treated as human personnel records.

## 22. Conflict-of-interest disclosure

Before scientific content assignment, every person must have a current conflict record for the exact role and suite scope.

Minimum future conflict fields:

```text
conflict_record_id
personnel_reference
role_class
suite_or_scope_id
disclosed_relationship_categories[]
disposition
reviewer_governance_reference
record_canonical_sha256
```

Closed dispositions:

```text
NO_MATERIAL_CONFLICT_IDENTIFIED
DISCLOSED_AND_REVIEWED_NO_DISQUALIFYING_CONFLICT
MATERIAL_CONFLICT_DISQUALIFYING
UNKNOWN_OR_UNRESOLVED
```

Potentially material categories include:

```text
DIRECT_CANDIDATE_MODEL_DEVELOPMENT_OR_MAINTENANCE_ROLE
MATERIAL_FINANCIAL_INTEREST_IN_CANDIDATE_OUTCOME
CURRENT_PAID_CANDIDATE_ADVOCACY_OR_MARKETING_RELATIONSHIP
DIRECT_CANDIDATE_SPECIFIC_TUNING_OR_EVALUATION_ROLE_THAT_CREATES_MATERIAL_BIAS
DIRECT_AUTHOR_REVIEW_DEPENDENCY_FOR_THE_SAME_CONTENT
```

```text
UNDISCLOSED_OR_UNRESOLVED_CONFLICT=BLOCKED
MATERIAL_CANDIDATE_SPECIFIC_CONFLICT_FOR_CONTENT_ACCEPTANCE_ROLE=INELIGIBLE
```

A7 does not require publication of personal financial or employment details; the protected evidence record may be represented publicly only by an opaque disposition reference.

## 23. Pair-level independence validation

A7 must support deterministic independence checks against A8 assignments.

For every pair:

```text
REVIEWER_1_PERSONNEL_REFERENCE != ROOT_AUTHOR_PERSONNEL_REFERENCE
REVIEWER_2_PERSONNEL_REFERENCE != ROOT_AUTHOR_PERSONNEL_REFERENCE
REVIEWER_1_PERSONNEL_REFERENCE != PAIR_ADAPTER_PERSONNEL_REFERENCE
REVIEWER_2_PERSONNEL_REFERENCE != PAIR_ADAPTER_PERSONNEL_REFERENCE
REVIEWER_1_PERSONNEL_REFERENCE != REVIEWER_2_PERSONNEL_REFERENCE
```

If adjudication is required:

```text
ADJUDICATOR_PERSONNEL_REFERENCE != ROOT_AUTHOR_PERSONNEL_REFERENCE
ADJUDICATOR_PERSONNEL_REFERENCE != PAIR_ADAPTER_PERSONNEL_REFERENCE
ADJUDICATOR_PERSONNEL_REFERENCE != REVIEWER_1_PERSONNEL_REFERENCE
ADJUDICATOR_PERSONNEL_REFERENCE != REVIEWER_2_PERSONNEL_REFERENCE
```

A person may hold multiple roles elsewhere, but not in ways that violate these exact-content independence constraints.

## 24. Role eligibility record

Before any assignment, the registry must compute a role-eligibility disposition from authoritative identity, qualification, conflict, and Gold-exposure evidence.

Minimum fields:

```text
role_eligibility_record_id
personnel_reference
role_class
suite_or_scope_id
identity_record_id
qualification_evidence_ids[]
conflict_record_id
gold_nonexposure_record_id_if_required
eligibility_disposition
eligibility_policy_id
eligibility_policy_version
record_canonical_sha256
```

Closed eligibility dispositions:

```text
ELIGIBLE
ELIGIBLE_WITH_SCOPE_LIMIT
INELIGIBLE
BLOCKED_PENDING_EVIDENCE
```

Caller-owned eligibility is non-authoritative.

```text
CALLER_ASSERTED_ELIGIBLE_AUTHORITATIVE=NO
ELIGIBILITY_MUST_BE_COMPUTED_FROM_VALID_BOUND_EVIDENCE=YES
```

## 25. Role assignment record

A role assignment is separate from eligibility.

Minimum fields:

```text
role_assignment_id
personnel_reference
role_class
suite_or_scope_id
eligible_record_id
assigned_content_ids_or_scope
allowed_governance_actions
assignment_state
assignment_authority_reference
start_event_or_time
expiry_or_revocation_condition
record_canonical_sha256
```

Allowed states:

```text
PROPOSED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
```

```text
PROPOSED_IMPLIES_PAYLOAD_ACCESS=NO
ACTIVE_IMPLIES_ONLY_SCOPED_ROLE_AUTHORITY=YES
UNBOUNDED_ROLE_SCOPE_BY_DEFAULT=PROHIBITED
```

Q1 creates no assignment records.

## 26. Role-grant prerequisite ordering

Before a content role can become `ACTIVE`, at least the following must be valid:

```text
VERIFIED_PERSONNEL_IDENTITY
ROLE_SPECIFIC_QUALIFICATION
RESOLVED_NONDISQUALIFYING_CONFLICT_DISPOSITION
ELIGIBLE_GOLD_NONEXPOSURE_DISPOSITION
A8_PROTOCOL_IDENTITY
A13_ACCESS_POLICY_IDENTITY
EXACT_SUITE_OR_DRAFT_SCOPE
```

And actual content access remains separately governed by A13.

```text
ACTIVE_A7_ROLE_WITHOUT_A13_ACCESS_GRANT_MAY_EXIST=YES
ACTIVE_A7_ROLE_AUTO_CREATES_A13_ACCESS_GRANT=NO
```

## 27. Role-transition registry

Every transition between materially different information domains must be explicitly recorded.

Minimum transition fields:

```text
role_transition_id
personnel_reference
suite_or_scope_id
from_role_assignment_id
from_role_class
to_role_class
from_role_revocation_or_close_event_id
transition_prerequisite_evidence_ids[]
transition_disposition
effective_event_or_time
transition_authority_reference
record_canonical_sha256
```

Closed transition dispositions:

```text
ALLOWED_PENDING_SEPARATE_ACCESS_GRANT
BLOCKED
PROHIBITED
```

## 28. Content-role to candidate-result-role transition

For the same suite identity, a content-role holder may become eligible for a future candidate-result role only after all of the following:

```text
SUITE_STATE=FROZEN_ACTIVE
CONTENT_ROLE_ASSIGNMENT_REVOKED_OR_CLOSED=YES
NO_OPEN_CONTENT_REVIEW_OR_ADJUDICATION_TASKS=YES
NO_PENDING_CONTENT_CHANGE_REQUESTS_ASSIGNED_TO_PERSON=YES
ROLE_TRANSITION_RECORD_CANONICAL=YES
SEPARATE_STAGE_B_RESULT_ACCESS_AUTHORITY_REQUIRED=YES
```

```text
CONTENT_ROLE_TO_RESULT_ROLE_AUTO_ACTIVATION=NO
```

Once candidate results for that suite have actually been accessed:

```text
RETURN_TO_ACTIVE_CONTENT_ROLE_FOR_SAME_SUITE_IDENTITY=PROHIBITED
RESULT_ACCESS_REVOCATION_RESTORES_RESULT_BLINDNESS=NO
```

The evaluated suite remains immutable regardless of personnel transition.

## 29. Result-exposed person and future distinct suites

Candidate-result exposure is not treated as Private-Gold exposure. A person who has seen candidate results may participate in a **future distinct suite** only if the future design explicitly records that the person is not result-blind and governance permits a result-informed new scientific identity.

```text
RESULT_EXPOSED_PERSON_MAY_CLAIM_RESULT_BLIND_FOR_FUTURE_RELATED_SUITE=NO
RESULT_INFORMED_FUTURE_SUITE_REQUIRES_NEW_SCIENTIFIC_IDENTITY=YES
RESULT_INFORMED_FUTURE_SUITE_REQUIRES_SEPARATE_GOVERNANCE=YES
```

This does not permit modifying or repairing the already evaluated suite identity using candidate feedback.

## 30. Selection-role to Private-Gold role transition

A selection author/reviewer may later enter a Private-Gold trustee/final-audit role only through a recorded transition and separate Gold authority after the selection suite is frozen.

```text
SELECTION_ROLE_TO_GOLD_ROLE_AUTO_ACTIVATION=NO
SEPARATE_PRIVATE_GOLD_AUTHORITY_REQUIRED=YES
```

Granting the role title does not itself establish case-content exposure. If actual Private-Gold case content is accessed, the exposure event becomes durable history.

```text
ACTUAL_GOLD_CASE_ACCESS_CREATES_DURABLE_EXPOSURE_EVENT=YES
```

After such exposure, the person becomes ineligible under the current policy for future selection author/adaptation/final-review/adjudication assignments unless a later separately reviewed policy explicitly supersedes this rule.

```text
POST_GOLD_EXPOSURE_SELECTION_CONTENT_ROLE_ELIGIBILITY=INELIGIBLE_UNDER_CURRENT_POLICY
SIMPLE_ROLE_REVOCATION_RESETS_GOLD_EXPOSURE=NO
```

## 31. Private-Gold exposure event record

A future exposure event record must not contain the Gold content itself.

Minimum fields:

```text
gold_exposure_event_id
personnel_reference
gold_trust_domain_id
gold_access_authorization_reference
exposure_class
protected_artifact_scope_reference
access_event_reference
recorded_event_or_time
record_canonical_sha256
```

Allowed exposure classes:

```text
PUBLIC_PROTOCOL_METADATA_ONLY
PRIVATE_CASE_CONTENT
PRIVATE_ANSWER_OR_RUBRIC
PROTECTED_CASE_DERIVED_REVIEW_OR_ADJUDICATION_CONTENT
```

```text
EXPOSURE_EVENT_RECORD_MAY_EMBED_GOLD_CASE_TEXT=NO
```

## 32. Attestation renewal and event-driven re-evaluation

A Gold-nonexposure/conflict/qualification disposition must be re-evaluated whenever a material personnel-governance event occurs.

Material events include:

```text
NEW_ROLE_WITH_BROADER_CONTENT_ACCESS
NEW_SUITE_ASSIGNMENT_REQUIRING_FRESH_SCOPE
RECORDED_OR_SUSPECTED_GOLD_EXPOSURE
NEW_MATERIAL_CONFLICT_DISCLOSURE
CREDENTIAL_OR_QUALIFICATION_STATUS_CHANGE
ROLE_SUSPENSION_OR_REVOCATION_EVENT
RESULT_ACCESS_TRANSITION
```

Q1 does not invent an arbitrary calendar re-attestation interval.

```text
FIXED_PERIODIC_REATTESTATION_INTERVAL=NOT_YET_FROZEN
EVENT_DRIVEN_REEVALUATION_REQUIRED=YES
```

## 33. Suspension and emergency fail-closed behavior

If qualification, conflict, identity, or Gold-exposure evidence becomes unresolved after assignment:

```text
ACTIVE_ROLE_STATUS=SUSPEND_PENDING_REVIEW
NEW_PAYLOAD_ACCESS=DENY
NEW_REVIEW_ACCEPTANCE=DENY
NEW_CONTENT_WRITE=DENY
```

Previously frozen scientific records remain historical; suspension does not silently delete them.

## 34. Audit requirements

Every material personnel-governance action must be auditable.

At minimum:

```text
PERSONNEL_IDENTITY_VERIFICATION
QUALIFICATION_DISPOSITION
CONFLICT_DISPOSITION
GOLD_NONEXPOSURE_DISPOSITION
ROLE_ELIGIBILITY_COMPUTATION
ROLE_ASSIGNMENT
ROLE_SUSPENSION
ROLE_REVOCATION
ROLE_TRANSITION
GOLD_EXPOSURE_EVENT
```

Audit records must be append-only or equivalently tamper-evident.

```text
SILENT_PERSONNEL_AUDIT_REWRITE=PROHIBITED
```

## 35. Relationship to A8 clinical review

A8 remains authoritative for review process semantics. A7 proves whether a named/opaque person is eligible and correctly assigned to an A8 role.

```text
A7_MAY_OVERRIDE_A8_INDEPENDENCE_RULE=NO
A7_MAY_REDUCE_TWO_REVIEWER_REQUIREMENT=NO
A7_MAY_SUBSTITUTE_ADMINISTRATIVE_TITLE_FOR_CLINICAL_COMPETENCE=NO
```

Review records must bind the exact A7 reviewer assignment evidence.

## 36. Relationship to A9 metadata

A9 may reference opaque A7 identities such as:

```text
content_authoring_record_id
pair_review_binding_id
gold_nonexposure_attestation_reference
```

A9 must not embed sensitive credential or conflict evidence.

```text
A9_PERSONNEL_REFERENCE_MUST_RESOLVE_TO_VALID_A7_RECORD=YES
```

## 37. Relationship to A13 access control

A7 establishes who is eligible and assigned; A13 enforces actual resource access.

```text
A7_PERSONNEL_IDENTITY_AND_NONEXPOSURE -> A13_ROLE_GRANTS
A7_ROLE_TRANSITION -> A13_ACCESS_REVOCATION_OR_NEW_GRANT
```

A13 must fail closed when an A7 role is suspended, revoked, expired, ineligible, or has unresolved Gold exposure where required.

## 38. Relationship to Private Gold governance

A7 does not grant or inspect Private Gold.

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_TRUSTEE_ASSIGNMENT_AUTHORITY=NONE
```

The selection registry may consume only Gold access-event/role metadata necessary to determine exposure disposition, without reading case payload.

## 39. Exact roster boundary

Q1 freezes the registry design only. It does not freeze any real person.

```text
EXACT_PERSONNEL_ROSTER=UNRESOLVED
EXACT_ROOT_AUTHOR_IDENTITIES=UNRESOLVED
EXACT_PAIR_ADAPTER_IDENTITIES=UNRESOLVED
EXACT_CLINICAL_REVIEWER_IDENTITIES=UNRESOLVED
EXACT_CLINICAL_ADJUDICATOR_IDENTITIES=UNRESOLVED
EXACT_RIGHTS_PRIVACY_PROVENANCE_REVIEWER_IDENTITIES=UNRESOLVED
EXACT_PAYLOAD_CUSTODIAN_IDENTITIES=UNRESOLVED
EXACT_CONTAMINATION_ASSESSOR_IDENTITIES=UNRESOLVED
EXACT_EVALUATION_EXECUTOR_IDENTITIES=UNRESOLVED
EXACT_CANDIDATE_RESULT_ANALYST_IDENTITIES=UNRESOLVED
```

## 40. A7 operational PASS requirements

Before A7 may become operationally `PASS`, future canonical evidence must prove at least:

```text
A7_REGISTRY_SCHEMA_AND_POLICY_CANONICAL=YES
EXACT_PERSONNEL_ROSTER_BOUND=YES
ALL_ACTIVE_PERSONNEL_IDENTITIES_VERIFIED=YES
ALL_ROLE_ASSIGNMENTS_HAVE_ROLE_SPECIFIC_QUALIFICATION_EVIDENCE=YES
ALL_REQUIRED_CONFLICT_DISPOSITIONS_RESOLVED=YES
ALL_CONTENT_FACING_ROLES_HAVE_ELIGIBLE_GOLD_NONEXPOSURE_DISPOSITIONS=YES
ALL_PAIR_LEVEL_INDEPENDENCE_CONSTRAINTS_VALIDATE=YES
ALL_ROLE_ASSIGNMENTS_ARE_SCOPED_AND_VERSIONED=YES
ROLE_TRANSITION_AND_REVOCATION_PROTOCOL_CANONICAL=YES
A13_INTEGRATION_CONTRACT_CANONICAL=YES
FRESH_INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Q1 satisfies none of these implementation/roster evidence requirements by itself.

## 41. Fail-closed validation semantics

A future A7 implementation must fail closed on at least:

```text
UNKNOWN_PERSONNEL_REFERENCE
UNVERIFIED_PERSONNEL_IDENTITY
MISSING_ROLE_QUALIFICATION_EVIDENCE
QUALIFICATION_OUTSIDE_ASSIGNED_SCOPE
UNKNOWN_OR_UNRESOLVED_CONFLICT
MATERIAL_DISQUALIFYING_CONFLICT
MISSING_GOLD_NONEXPOSURE_RECORD_FOR_CONTENT_ROLE
UNKNOWN_OR_UNRESOLVED_GOLD_EXPOSURE
CONFLICTING_GOLD_EXPOSURE_EVIDENCE
PRIVATE_GOLD_CASE_CONTENT_EXPOSED_FOR_SELECTION_CONTENT_ROLE
AUTHOR_REVIEWER_IDENTITY_COLLISION
ADAPTER_REVIEWER_IDENTITY_COLLISION
REVIEWER_REVIEWER_IDENTITY_COLLISION
ADJUDICATOR_INDEPENDENCE_COLLISION
ACTIVE_CONTENT_ROLE_PLUS_CANDIDATE_RESULT_ACCESS_FOR_SAME_SUITE
RETURN_TO_CONTENT_ROLE_AFTER_RESULT_ACCESS_FOR_SAME_SUITE
UNSCOPED_ROLE_ASSIGNMENT
EXPIRED_OR_REVOKED_ROLE_USED_AS_ACTIVE
```

## 42. Current readiness

```text
A7_REGISTRY_SCHEMA_IMPLEMENTATION=NO
A7_EXACT_PERSONNEL_ROSTER=UNRESOLVED
A7_EXACT_QUALIFICATION_EVIDENCE=UNRESOLVED
A7_EXACT_CONFLICT_RECORDS=UNRESOLVED
A7_EXACT_GOLD_NONEXPOSURE_ATTESTATIONS=UNRESOLVED
A7_EXACT_ROLE_ASSIGNMENTS=NONE
A7_EXACT_ROLE_TRANSITIONS=NONE

A7_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
```

## 43. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE

A7_PERSONNEL_REGISTRY_IMPLEMENTATION_AUTHORITY=NONE
A7_PERSONNEL_VERIFICATION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A7_QUALIFICATION_ADJUDICATION_AUTHORITY=NONE
A7_GOLD_NONEXPOSURE_ATTESTATION_EXECUTION_AUTHORITY=NONE
A7_ROLE_TRANSITION_EXECUTION_AUTHORITY=NONE

A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_ROLE_ASSIGNMENT_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE

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

## 44. Session 13 state after Q1

Acceptance of this question advances bounded Session 13 only.

```text
CLARIFICATION_SESSION_13=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

No A1–A15 implementation gate becomes operationally PASS merely because its clarification design is frozen.
