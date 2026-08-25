# Session 13 Q3 — A7 Eligibility/Assignment State Machine and Fail-Closed Validator Contract

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 13 Q3 only. It freezes the state-machine and validation architecture that must govern future A7 personnel identity, qualification, eligibility, role assignment, suspension, revocation, transition, and A13 access-handshake decisions. It does **not** implement the registry, create or verify any personnel record, assign any person, grant any A13 access, provision storage, ingest protected evidence, access Private Gold, create or review selection cases, execute models, spend funds, implement A1, authorize A15, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION13_Q3_POLICY=SEPARATE_IDENTITY_ELIGIBILITY_ASSIGNMENT_AND_ACCESS_STATE_MACHINES_WITH_EVENT_DRIVEN_STALENESS_AND_FAIL_CLOSED_A13_HANDSHAKE

A7_STATE_MACHINE_ARCHITECTURE=FROZEN
A7_FAIL_CLOSED_VALIDATOR_CONTRACT=FROZEN
A7_A13_HANDSHAKE_ARCHITECTURE=FROZEN

A7_STATE_MACHINE_IMPLEMENTED=NO
A7_VALIDATOR_IMPLEMENTED=NO
A7_A13_HANDSHAKE_IMPLEMENTED=NO

A7_GATE_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY

CLARIFICATION_SESSION_13=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

The central rule is that personnel identity, scientific eligibility, role assignment, and resource access are distinct state machines. No single status such as `ACTIVE` or `VERIFIED` may silently stand in for all of them.

```text
ONE_COMPOSITE_PERSON_STATUS_CONTROLS_ALL_AUTHORITY=PROHIBITED
```

## 2. Four authoritative state domains

A future A7 implementation must preserve these independent domains:

```text
DOMAIN_1=IDENTITY_STATE
DOMAIN_2=ELIGIBILITY_STATE
DOMAIN_3=ASSIGNMENT_STATE
DOMAIN_4=ACCESS_HANDSHAKE_STATE
```

Authority split:

```text
A7_AUTHORITATIVE_FOR_IDENTITY_ELIGIBILITY_AND_ASSIGNMENT=YES
A13_AUTHORITATIVE_FOR_ACTUAL_PAYLOAD_OR_RESULT_ACCESS=YES

A7_MAY_DIRECTLY_GRANT_A13_ACCESS=NO
A13_MAY_RECOMPUTE_A7_SCIENTIFIC_ELIGIBILITY=NO
```

## 3. Identity state machine

Closed identity states:

```text
REGISTERED_UNVERIFIED
VERIFIED
SUSPENDED
RETIRED
```

Allowed core transitions:

```text
REGISTERED_UNVERIFIED -> VERIFIED
REGISTERED_UNVERIFIED -> RETIRED

VERIFIED -> SUSPENDED
VERIFIED -> RETIRED

SUSPENDED -> VERIFIED
SUSPENDED -> RETIRED
```

The transition `SUSPENDED -> VERIFIED` requires fresh authoritative evidence resolving the suspension reason; it is not an administrative toggle.

```text
SUSPENSION_CLEAR_WITHOUT_RESOLUTION_EVIDENCE=PROHIBITED
```

A retired identity may remain historically referenceable but may not receive a new active assignment unless a separately versioned re-registration policy explicitly permits it.

```text
RETIRED_AUTO_REACTIVATION=PROHIBITED
```

## 4. Identity-state consequences

```text
REGISTERED_UNVERIFIED_MAY_BE_ELIGIBLE=NO
REGISTERED_UNVERIFIED_MAY_HAVE_ACTIVE_ASSIGNMENT=NO

VERIFIED_MAY_PROCEED_TO_ELIGIBILITY_COMPUTATION=YES

SUSPENDED_MAY_HAVE_NEW_ACTIVE_ASSIGNMENT=NO
SUSPENDED_REQUIRES_EXISTING_ACTIVE_ASSIGNMENTS_TO_SUSPEND=YES
SUSPENDED_REQUIRES_A13_ACCESS_REVIEW_OR_REVOCATION_IF_ACCESS_EXISTS=YES

RETIRED_MAY_HAVE_ACTIVE_ASSIGNMENT=NO
RETIRED_REQUIRES_A13_ACCESS_REVOCATION_IF_ACCESS_EXISTS=YES
```

Historical records remain reproducible after suspension or retirement.

## 5. Eligibility is scoped, not global

Eligibility is always bound to an exact tuple:

```text
personnel_reference
role_class
suite_or_scope_id
qualification_scope
eligibility_policy_id
eligibility_policy_version
input_record_identities[]
```

A person cannot be globally declared `ELIGIBLE` for every future role or suite.

```text
GLOBAL_UNSCOPED_ELIGIBLE_STATE=PROHIBITED
```

## 6. Eligibility states

Closed eligibility states:

```text
NOT_COMPUTED
ELIGIBLE
ELIGIBLE_WITH_SCOPE_LIMIT
BLOCKED_PENDING_EVIDENCE
INELIGIBLE
STALE_RECOMPUTE_REQUIRED
```

`STALE_RECOMPUTE_REQUIRED` is distinct from scientific `INELIGIBLE`. It means an earlier disposition may have been valid but can no longer be relied upon because one or more bound inputs changed, expired, were superseded, or became unresolved.

```text
STALE_ELIGIBILITY_MAY_BE_USED_FOR_NEW_ASSIGNMENT=NO
STALE_ELIGIBILITY_MAY_SUPPORT_EXISTING_ACTIVE_ACCESS=NO
```

## 7. Eligibility computation prerequisites

Before an eligibility result may be `ELIGIBLE` or `ELIGIBLE_WITH_SCOPE_LIMIT`, all applicable authoritative inputs must be current and valid.

At minimum:

```text
IDENTITY_STATE=VERIFIED
ROLE_SPECIFIC_QUALIFICATION_DISPOSITION=CURRENT_AND_NONDISQUALIFYING
CONFLICT_DISPOSITION=CURRENT_AND_NONDISQUALIFYING
GOLD_EXPOSURE_DISPOSITION=CURRENT_AND_ELIGIBLE_IF_REQUIRED
ROLE_POLICY_IDENTITY=CURRENT
SUITE_OR_SCOPE_ID=EXACT
```

For content-facing selection roles:

```text
GOLD_EXPOSURE_DISPOSITION_ALLOWED=
  NO_KNOWN_PRIVATE_GOLD_CASE_CONTENT_EXPOSURE
  OR PUBLIC_GOLD_PROTOCOL_METADATA_ONLY
```

Fail-closed inputs include:

```text
UNKNOWN_OR_UNRESOLVED_GOLD_EXPOSURE
CONFLICTING_GOLD_EXPOSURE_EVIDENCE
PRIVATE_GOLD_CASE_CONTENT_EXPOSED
UNKNOWN_OR_UNRESOLVED_CONFLICT
MATERIAL_CONFLICT_DISQUALIFYING
BLOCKED_PENDING_QUALIFICATION_EVIDENCE
UNVERIFIED_OR_SUSPENDED_IDENTITY
```

## 8. Eligibility computation is evaluator-owned

The authoritative eligibility disposition must be computed from exact bound inputs.

```text
CALLER_ASSERTED_ELIGIBLE_AUTHORITATIVE=NO
MANUAL_FREE_TEXT_ELIGIBILITY_OVERRIDE=PROHIBITED
```

Minimum future derived eligibility record:

```text
role_eligibility_record_id
personnel_reference
role_class
suite_or_scope_id
identity_record_id
qualification_evidence_record_ids[]
conflict_record_id
gold_exposure_record_id_or_explicit_not_required
role_policy_id
role_policy_version
eligibility_disposition
scope_limit_if_any
computed_from_record_sha256s[]
record_version
record_canonical_sha256
```

## 9. Eligibility state transitions

Representative allowed transitions:

```text
NOT_COMPUTED -> ELIGIBLE
NOT_COMPUTED -> ELIGIBLE_WITH_SCOPE_LIMIT
NOT_COMPUTED -> BLOCKED_PENDING_EVIDENCE
NOT_COMPUTED -> INELIGIBLE

ELIGIBLE -> STALE_RECOMPUTE_REQUIRED
ELIGIBLE_WITH_SCOPE_LIMIT -> STALE_RECOMPUTE_REQUIRED
BLOCKED_PENDING_EVIDENCE -> STALE_RECOMPUTE_REQUIRED
INELIGIBLE -> STALE_RECOMPUTE_REQUIRED

STALE_RECOMPUTE_REQUIRED -> ELIGIBLE
STALE_RECOMPUTE_REQUIRED -> ELIGIBLE_WITH_SCOPE_LIMIT
STALE_RECOMPUTE_REQUIRED -> BLOCKED_PENDING_EVIDENCE
STALE_RECOMPUTE_REQUIRED -> INELIGIBLE
```

An eligibility record is immutable by identity. Re-evaluation creates a new record rather than rewriting the prior disposition in place.

```text
ELIGIBILITY_DISPOSITION_IN_PLACE_REWRITE=PROHIBITED
```

## 10. Assignment states

Q3 preserves the assignment vocabulary already frozen by Q1:

```text
PROPOSED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
```

It does not add `ACCESS_GRANTED` to the A7 assignment state because A13 owns actual resource access.

```text
A7_ASSIGNMENT_STATE_CONTAINS_ACCESS_GRANTED=NO
```

## 11. Assignment creation prerequisites

A new assignment may be proposed only if:

```text
PERSONNEL_REFERENCE_VALID=YES
ROLE_CLASS_VALID=YES
SUITE_OR_SCOPE_ID_EXACT=YES
ELIGIBILITY_RECORD_CURRENT=YES
ELIGIBILITY_DISPOSITION_IN={ELIGIBLE,ELIGIBLE_WITH_SCOPE_LIMIT}
ASSIGNMENT_SCOPE_WITHIN_ELIGIBILITY_SCOPE=YES
ASSIGNMENT_AUTHORITY_REFERENCE_PRESENT=YES
```

A proposed assignment may not become `ACTIVE` unless all exact activation prerequisites remain current.

For content-facing selection roles, these include:

```text
IDENTITY_STATE=VERIFIED
ELIGIBILITY_RECORD_CURRENT=YES
A8_REVIEW_OR_AUTHORING_PROTOCOL_IDENTITY_AS_APPLICABLE=CURRENT
A13_ACCESS_POLICY_IDENTITY=CURRENT
EXACT_SUITE_OR_DRAFT_SCOPE=BOUND
```

`ACTIVE` means the role assignment exists and is scientifically/governance valid. It does not mean the person can read or write any payload until A13 separately grants exact access.

```text
ACTIVE_A7_ASSIGNMENT_WITHOUT_A13_GRANT=VALID_STATE
ACTIVE_A7_ASSIGNMENT_AUTO_CREATES_A13_GRANT=NO
```

## 12. Assignment transitions

Allowed core transitions:

```text
PROPOSED -> ACTIVE
PROPOSED -> REVOKED
PROPOSED -> EXPIRED

ACTIVE -> SUSPENDED
ACTIVE -> REVOKED
ACTIVE -> EXPIRED

SUSPENDED -> ACTIVE
SUSPENDED -> REVOKED
SUSPENDED -> EXPIRED
```

`SUSPENDED -> ACTIVE` requires fresh validation of all activation prerequisites and a new transition/audit record.

```text
SUSPENDED_ASSIGNMENT_AUTO_REACTIVATION=PROHIBITED
```

`REVOKED` and `EXPIRED` are terminal for the exact assignment ID.

```text
REVOKED_ASSIGNMENT_REACTIVATION_IN_PLACE=PROHIBITED
EXPIRED_ASSIGNMENT_REACTIVATION_IN_PLACE=PROHIBITED
```

If a new assignment is scientifically appropriate, it must receive a new assignment identity.

## 13. Automatic suspension triggers

An active assignment must transition to `SUSPENDED` or an equivalent fail-closed state when any bound eligibility prerequisite becomes unresolved or stale.

Triggers include at least:

```text
IDENTITY_STATE_BECOMES_SUSPENDED
IDENTITY_VERIFICATION_RECORD_SUPERSEDED_MATERIALLY
QUALIFICATION_EVIDENCE_EXPIRES_OR_BECOMES_UNRESOLVED
QUALIFICATION_SCOPE_NO_LONGER_COVERS_ASSIGNMENT
NEW_MATERIAL_CONFLICT_DISCLOSURE
CONFLICT_RECORD_BECOMES_UNKNOWN_OR_UNRESOLVED
RECORDED_OR_SUSPECTED_PRIVATE_GOLD_EXPOSURE
GOLD_EXPOSURE_RECORD_BECOMES_CONFLICTING_OR_UNRESOLVED
PROTECTED_EVIDENCE_DIGEST_MISMATCH
MATERIAL_A7_SECURITY_OR_INTEGRITY_INCIDENT
MATERIAL_CORRECTION_REQUEST_THAT_CAN_CHANGE_ELIGIBILITY
ROLE_POLICY_IDENTITY_SUPERSEDED_MATERIALLY
SUITE_OR_SCOPE_IDENTITY_CHANGE_INVALIDATING_ASSIGNMENT_SCOPE
```

```text
ACTIVE_ASSIGNMENT_MAY_REMAIN_ACTIVE_WHILE_MATERIAL_ELIGIBILITY_INPUT_IS_UNRESOLVED=NO
```

## 14. Stale evidence invalidation

A future implementation must distinguish evidence that is historically valid from evidence that is current for a new decision.

Every eligibility input should expose or derive a freshness state such as:

```text
CURRENT
SUPERSEDED
REVALIDATION_REQUIRED
BLOCKED_UNRESOLVED
```

The exact implementation type is not frozen, but the semantics are.

```text
ANY_REQUIRED_INPUT_NOT_CURRENT -> ELIGIBILITY_NOT_RELIABLE_FOR_NEW_AUTHORITY
```

Staleness propagation:

```text
MATERIAL_INPUT_CHANGE
  -> MARK_DEPENDENT_ELIGIBILITY_STALE_RECOMPUTE_REQUIRED
  -> SUSPEND_DEPENDENT_ACTIVE_ASSIGNMENT_IF_RELIED_UPON
  -> EMIT_A13_DENY_OR_REVOKE_REQUIRED_SIGNAL_IF_ACCESS_EXISTS
```

## 15. Non-material evidence updates

Purely administrative metadata changes that provably do not alter identity, scope, competence, conflict, exposure, or decision semantics need not invalidate eligibility.

However:

```text
CALLER_SELF_CLASSIFIES_CHANGE_AS_NONMATERIAL_WITHOUT_POLICY=PROHIBITED
```

The materiality rule must itself be versioned and auditable.

## 16. Gold exposure event precedence

For selection content roles, a valid new `PRIVATE_GOLD_CASE_CONTENT_EXPOSED` event overrides any earlier clean/nonexposed disposition for future eligibility under the current policy.

```text
VALID_PRIVATE_GOLD_EXPOSURE_EVENT
  -> PRIOR_CLEAN_DISPOSITION_SUPERSEDED_FOR_FUTURE_ELIGIBILITY
  -> CONTENT_ROLE_ELIGIBILITY=INELIGIBLE_UNDER_CURRENT_POLICY
  -> ACTIVE_CONTENT_ASSIGNMENT=SUSPEND_OR_REVOKE_AS_GOVERNED
  -> A13_ACCESS=REVOKE_REQUIRED_IF_GRANTED
```

Simple role revocation or lapse of time cannot restore a clean disposition.

```text
TIME_PASSAGE_RESTORES_GOLD_NONEXPOSURE=NO
```

An exposure record proven erroneous through Q2 correction governance may be superseded by a new authoritative correction record; it may not be deleted silently.

## 17. Conflict-event precedence

A newly identified material disqualifying conflict for an active content-acceptance role requires fail-closed suspension.

```text
MATERIAL_DISQUALIFYING_CONFLICT
  -> ELIGIBILITY=INELIGIBLE_OR_STALE_PENDING_RECOMPUTE
  -> ACTIVE_ASSIGNMENT=SUSPENDED_OR_REVOKED
  -> A13_ACCESS=DENY_OR_REVOKE_REQUIRED
```

A newly disclosed relationship is not automatically disqualifying; it must be reviewed. Until materially relevant uncertainty is resolved:

```text
UNRESOLVED_MATERIAL_CONFLICT=BLOCKED
```

## 18. Same-suite result exposure state

Candidate-result exposure is not represented as a generic conflict and is not Private-Gold exposure. It is a durable suite-specific information-domain fact.

Future registry support must record at least:

```text
personnel_reference
suite_id
result_access_event_id
result_access_scope
result_access_authorization_reference
result_exposure_state
record_canonical_sha256
```

Closed result-exposure states:

```text
NO_RESULT_ACCESS_RECORDED
RESULT_ACCESS_GRANTED_NOT_YET_USED
RESULT_EXPOSED
RESULT_ACCESS_REVOKED_AFTER_EXPOSURE
```

Once `RESULT_EXPOSED` occurs for a suite:

```text
SAME_SUITE_CONTENT_ROLE_ELIGIBILITY=PROHIBITED
RESULT_ACCESS_REVOCATION_RESTORES_RESULT_BLINDNESS=NO
```

`RESULT_ACCESS_GRANTED_NOT_YET_USED` must not be treated as actual exposure unless audit evidence establishes that content/results were accessed, but concurrent active content-role and result-access grants for the same suite remain prohibited by A13.

## 19. Content-to-result role transition

A content-role assignment may transition toward candidate-result analysis for the same suite only when:

```text
SUITE_STATE=FROZEN_ACTIVE
CONTENT_ASSIGNMENT_STATE_IN={REVOKED,EXPIRED}
NO_OPEN_CONTENT_REVIEW_OR_ADJUDICATION_TASKS=YES
NO_PENDING_CONTENT_CHANGE_REQUESTS_ASSIGNED_TO_PERSON=YES
ROLE_TRANSITION_RECORD_VALID=YES
RESULT_ROLE_ELIGIBILITY_CURRENT=YES
SEPARATE_STAGE_B_RESULT_ACCESS_AUTHORITY_EXISTS=YES
```

Q3 does not create that authority.

```text
CONTENT_ROLE_TO_RESULT_ROLE_AUTO_GRANT=NO
```

## 20. Result-to-content return prohibition for same suite

If actual candidate-result exposure has occurred:

```text
RESULT_EXPOSED + SAME_SUITE_CONTENT_ROLE_ASSIGNMENT_PROPOSAL = REJECT
```

This applies to:

```text
ROOT_CONTENT_AUTHOR
PAIR_ADAPTER_OR_PARALLEL_AUTHOR
CLINICAL_PAIR_REVIEWER
CLINICAL_ADJUDICATOR
```

A future distinct suite may use result-informed personnel only through a separately governed new scientific identity and may not claim result-blind construction.

## 21. Pair-level independence validation

Before a final-review assignment can become `ACTIVE`, exact pair-level identities must satisfy:

```text
REVIEWER_1 != ROOT_AUTHOR
REVIEWER_2 != ROOT_AUTHOR
REVIEWER_1 != PAIR_ADAPTER
REVIEWER_2 != PAIR_ADAPTER
REVIEWER_1 != REVIEWER_2
```

If adjudication is required:

```text
ADJUDICATOR != ROOT_AUTHOR
ADJUDICATOR != PAIR_ADAPTER
ADJUDICATOR != REVIEWER_1
ADJUDICATOR != REVIEWER_2
```

```text
PAIR_LEVEL_INDEPENDENCE_COLLISION=BLOCKED
```

A person may hold multiple roles elsewhere if the exact-content independence constraints remain satisfied.

## 22. A7 to A13 access-handshake outputs

A7 may emit only bounded authoritative governance outputs to A13.

Minimum future grant-consideration payload:

```text
personnel_reference
role_assignment_id
role_class
suite_or_scope_id
assignment_state
eligibility_record_id
eligibility_disposition
gold_exposure_disposition_reference_if_required
allowed_governance_actions
assignment_expiry_or_revocation_condition
A7_policy_id
A7_policy_version
A7_record_canonical_sha256
```

It must not contain raw protected evidence.

```text
A7_TO_A13_RAW_CREDENTIALS=PROHIBITED
A7_TO_A13_RAW_CONFLICT_EVIDENCE=PROHIBITED
A7_TO_A13_SIGNED_ATTESTATION_BODY=PROHIBITED
```

## 23. A7 grant-consideration signals

Q3 freezes only semantic signals, not an implementation protocol.

```text
ALLOW_GRANT_CONSIDERATION
DENY_GRANT
REVOKE_REQUIRED
REVALIDATION_REQUIRED
```

Semantics:

```text
ALLOW_GRANT_CONSIDERATION=
  A7 prerequisites are currently satisfied for the exact scoped assignment;
  A13 still performs its own access-policy checks and requires separate authority.

DENY_GRANT=
  no new A13 grant may be issued for the referenced assignment.

REVOKE_REQUIRED=
  an existing A13 grant tied to the assignment must no longer remain effective.

REVALIDATION_REQUIRED=
  A7 evidence is stale or unresolved; A13 must deny new access and suspend/revoke existing access as defined by the future exact implementation.
```

```text
ALLOW_GRANT_CONSIDERATION_EQUALS_ACCESS_AUTHORIZATION=NO
```

## 24. A13 acknowledgement back-reference

If A13 later issues a grant, the grant must bind the exact A7 assignment/eligibility identity on which it relied.

Minimum conceptual back-reference:

```text
A13_access_grant_id
personnel_reference
role_assignment_id
eligibility_record_id
suite_or_scope_id
allowed_actions
A13_policy_id
A13_policy_version
A7_record_canonical_sha256_used_for_grant
```

A7 may record the opaque A13 grant reference for audit, but it does not own the A13 grant state.

## 25. Revocation handshake

When an A7 event makes an existing assignment suspended, revoked, expired, stale, or ineligible:

```text
A7_EMITS_REVOKE_REQUIRED=YES
A13_MUST_NOT_CONTINUE_TO_TREAT_PRIOR_GRANT_AS_CURRENT=YES
```

Future implementation evidence must prove the revocation path cannot silently fail open.

```text
A7_REVOKED_BUT_A13_ACCESS_REMAINS_ACTIVE=FAIL_CLOSED_GATE_FAILURE
```

Q3 does not choose synchronous versus asynchronous transport. It freezes only the required end-state semantics.

## 26. Race-condition / ordering rule

A13 must evaluate the **current** A7 record identity at grant use, not only the historical identity that existed when access was first granted.

```text
STALE_A7_GRANT_REFERENCE_MAY_AUTHORIZE_ACCESS=NO
```

A future implementation may use push revocation, pull validation, short-lived grants, or another mechanism, but must prove fail-closed behavior for stale state.

## 27. Assignment scope narrowing

If an assignment is narrowed but remains eligible:

```text
OLD_BROADER_ASSIGNMENT_SCOPE_MAY_REMAIN_ACTIVE=NO
OLD_BROADER_A13_ACCESS_MAY_REMAIN_ACTIVE=NO
```

A new versioned assignment or governed scope-change record must become authoritative, and A13 access must be reconciled to the new narrower scope.

Scope broadening always requires fresh eligibility validation.

```text
ASSIGNMENT_SCOPE_BROADENING_WITHOUT_FRESH_ELIGIBILITY=PROHIBITED
```

## 28. Evidence correction propagation

Under Q2, corrections create new versions rather than rewriting history. Q3 freezes downstream propagation:

```text
CORRECTION_MATERIALLY_CHANGES_IDENTITY_QUALIFICATION_CONFLICT_OR_EXPOSURE
  -> PRIOR_ELIGIBILITY_STALE_RECOMPUTE_REQUIRED
  -> DEPENDENT_ASSIGNMENT_SUSPEND_IF_ACTIVE
  -> A13_REVALIDATION_OR_REVOKE_REQUIRED
```

A correction that strengthens or clears evidence does not automatically restore prior authority.

```text
CORRECTION_AUTO_REACTIVATES_ASSIGNMENT=NO
```

Fresh eligibility and assignment validation are required.

## 29. Incident propagation

A material protected-registry security or integrity incident may trigger:

```text
IDENTITY_STATE=SUSPENDED
OR ELIGIBILITY_STATE=STALE_RECOMPUTE_REQUIRED
OR ASSIGNMENT_STATE=SUSPENDED
```

according to exact affected scope.

The implementation must minimize blast radius but may not ignore uncertainty merely because broad suspension is inconvenient.

```text
KNOWN_MATERIAL_INTEGRITY_UNCERTAINTY_FAILS_OPEN=NO
```

## 30. Expiry semantics

Q3 does not choose arbitrary fixed credential or assignment lifetimes.

```text
EXACT_CALENDAR_EXPIRY_INTERVALS=NOT_YET_FROZEN
```

But when a bound evidence or assignment-specific expiry condition is reached:

```text
EXPIRED_EVIDENCE_MAY_SUPPORT_CURRENT_ELIGIBILITY=NO
EXPIRED_ASSIGNMENT_MAY_SUPPORT_A13_ACCESS=NO
```

## 31. Historical reproducibility

Historical states must remain reconstructable from immutable/versioned records.

For any scientific artifact that relied on personnel governance, it must be possible to determine:

```text
WHICH_PERSONNEL_REFERENCE_WAS_USED
WHICH_ROLE_ASSIGNMENT_ID_WAS_CURRENT
WHICH_ELIGIBILITY_RECORD_ID_WAS_CURRENT
WHICH_POLICY_VERSION_WAS_APPLIED
WHICH_A13_GRANT_REFERENCE_IF_ANY_WAS_IN_FORCE
WHETHER_LATER_SUSPENSION_OR_REVOCATION_OCCURRED
```

This does not require publication of raw credentials or personal identity.

## 32. Validator layers

A future A7 implementation must separate validation layers rather than returning one unstructured boolean.

Minimum conceptual layers:

```text
VALIDATE_RECORD_IDENTITY_AND_SCHEMA
VALIDATE_IDENTITY_STATE
VALIDATE_QUALIFICATION_EVIDENCE
VALIDATE_CONFLICT_DISPOSITION
VALIDATE_GOLD_EXPOSURE_DISPOSITION
VALIDATE_ROLE_ELIGIBILITY
VALIDATE_ASSIGNMENT_SCOPE_AND_STATE
VALIDATE_PAIR_LEVEL_INDEPENDENCE_IF_APPLICABLE
VALIDATE_RESULT_EXPOSURE_COMPATIBILITY
DERIVE_A7_TO_A13_ACCESS_SIGNAL
```

Each layer must fail closed on unknown vocabulary or unresolved required references.

## 33. Unknown values

```text
UNKNOWN_IDENTITY_STATE=REJECT
UNKNOWN_ELIGIBILITY_STATE=REJECT
UNKNOWN_ASSIGNMENT_STATE=REJECT
UNKNOWN_RESULT_EXPOSURE_STATE=REJECT
UNKNOWN_ROLE_CLASS=REJECT
UNKNOWN_TRANSITION=REJECT
```

No unknown value may silently map to the nearest permissive state.

## 34. Record identity validation

Every authoritative state or transition record must bind:

```text
record_id
record_version
policy_id
policy_version
record_canonical_sha256
supersedes_record_id_or_explicit_none
```

Where input records are referenced:

```text
REFERENCED_RECORD_MUST_EXIST=YES
REFERENCED_RECORD_HASH_MUST_MATCH=YES
REFERENCED_RECORD_VERSION_MUST_MATCH=YES
```

## 35. Invalid state combinations

A future validator must reject at least:

```text
IDENTITY_REGISTERED_UNVERIFIED + ELIGIBLE
IDENTITY_SUSPENDED + ACTIVE_ASSIGNMENT
IDENTITY_RETIRED + ACTIVE_ASSIGNMENT

ELIGIBILITY_NOT_COMPUTED + ACTIVE_ASSIGNMENT
ELIGIBILITY_BLOCKED_PENDING_EVIDENCE + ACTIVE_ASSIGNMENT
ELIGIBILITY_INELIGIBLE + ACTIVE_ASSIGNMENT
ELIGIBILITY_STALE_RECOMPUTE_REQUIRED + ACTIVE_ASSIGNMENT

ASSIGNMENT_PROPOSED + A13_ACTIVE_PAYLOAD_ACCESS
ASSIGNMENT_SUSPENDED + A13_ACTIVE_PAYLOAD_ACCESS
ASSIGNMENT_REVOKED + A13_ACTIVE_PAYLOAD_ACCESS
ASSIGNMENT_EXPIRED + A13_ACTIVE_PAYLOAD_ACCESS

CONTENT_ROLE + PRIVATE_GOLD_CASE_CONTENT_EXPOSED
CONTENT_ROLE + SAME_SUITE_RESULT_EXPOSED

REVIEWER_AUTHOR_IDENTITY_COLLISION
REVIEWER_ADAPTER_IDENTITY_COLLISION
REVIEWER_REVIEWER_IDENTITY_COLLISION
ADJUDICATOR_INDEPENDENCE_COLLISION
```

## 36. Stale-reference invalidation

A downstream record that references a superseded material eligibility or assignment record must not silently remain current.

```text
SUPERSEDED_MATERIAL_A7_RECORD_USED_AS_CURRENT=REJECT
```

A13 may retain the old reference only as historical audit evidence, never as active access authority.

## 37. No privilege inference

```text
FOUNDER_STATUS_IMPLIES_ELIGIBILITY=NO
REPOSITORY_COLLABORATOR_STATUS_IMPLIES_ELIGIBILITY=NO
SYSTEM_ADMIN_STATUS_IMPLIES_SCIENTIFIC_ROLE=NO
A7_VERIFIER_ROLE_IMPLIES_SELECTION_PAYLOAD_ROLE=NO
SELECTION_PAYLOAD_ROLE_IMPLIES_RESULT_ACCESS=NO
RESULT_ACCESS_IMPLIES_WINNER_SELECTION_AUTHORITY=NO
```

## 38. No branch-by-preferred-candidate semantics

The personnel state machine must not depend on candidate performance or preferred candidate identity.

```text
PREFERRED_CANDIDATE_RESULT_MAY_CHANGE_PERSONNEL_ELIGIBILITY=NO
PREFERRED_CANDIDATE_RESULT_MAY_TRIGGER_REVIEWER_REMOVAL=NO
PREFERRED_CANDIDATE_RESULT_MAY_TRIGGER_ROLE_REASSIGNMENT=NO
```

Legitimate independent personnel-governance events remain valid regardless of candidate outcomes.

## 39. No hidden manual override

Any future emergency or exceptional override mechanism must be explicitly designed, separately authorized, versioned, and audited. Q3 creates no such override.

```text
UNRECORDED_ADMIN_OVERRIDE=PROHIBITED
FAIL_OPEN_OVERRIDE_BY_FOUNDER=PROHIBITED
FAIL_OPEN_OVERRIDE_BY_STORAGE_ADMIN=PROHIBITED
```

## 40. A8 integration

A8 remains authoritative for clinical-review process and acceptance semantics. A7/Q3 only determines whether a person is validly eligible and assigned.

```text
A7_ACTIVE_REVIEWER_ASSIGNMENT_CAN_REDUCE_A8_TWO_REVIEWER_REQUIREMENT=NO
A7_MAY_ACCEPT_CASE_ON_BEHALF_OF_A8=NO
```

A review record must bind the exact current reviewer assignment identities used for that review.

## 41. A9 integration

A9 metadata may reference:

```text
content_authoring_record_id
pair_review_binding_id
personnel_reference
role_assignment_id
eligibility_record_id
```

A9 must not embed raw A7 protected evidence or independently claim a person is qualified.

```text
A9_CALLER_ASSERTED_PERSONNEL_ELIGIBILITY=NONAUTHORITATIVE
```

## 42. A12 integration

If a personnel-governance defect is discovered after a scientific artifact is frozen, the personnel record may be corrected through A7/Q2 governance, but the scientific consequence must be separately handled under A12.

```text
PERSONNEL_CORRECTION_SILENTLY_REWRITES_FROZEN_CASE_HISTORY=NO
```

## 43. A13 integration

A13 consumes only current opaque A7 outputs and remains responsible for enforcement.

```text
A7_VALIDATOR_PASS_EQUALS_A13_ACCESS_PASS=NO
A13_ACCESS_POLICY_PASS_EQUALS_A7_ELIGIBILITY_PASS=NO
```

Both domains must be valid for resource access.

## 44. Private Gold boundary

Q3 does not grant or verify Gold access.

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_TRUSTEE_ASSIGNMENT_AUTHORITY=NONE
```

Only Gold access-event/role metadata may inform the A7 exposure disposition under Q1/Q2.

## 45. Future test matrix

A future implementation should include at least deterministic tests for:

```text
UNVERIFIED_IDENTITY_CANNOT_BECOME_ELIGIBLE
SUSPENDED_IDENTITY_SUSPENDS_ACTIVE_ASSIGNMENT
RETIRED_IDENTITY_CANNOT_HAVE_ACTIVE_ASSIGNMENT

MISSING_QUALIFICATION_BLOCKS_ELIGIBILITY
OUT_OF_SCOPE_QUALIFICATION_BLOCKS_ASSIGNMENT
UNRESOLVED_CONFLICT_BLOCKS_ELIGIBILITY
DISQUALIFYING_CONFLICT_BLOCKS_CONTENT_ASSIGNMENT

UNKNOWN_GOLD_EXPOSURE_BLOCKS_CONTENT_ROLE
PRIVATE_GOLD_EXPOSURE_MAKES_CONTENT_ROLE_INELIGIBLE
GOLD_ACCESS_REVOCATION_DOES_NOT_ERASE_EXPOSURE
ERRONEOUS_EXPOSURE_CORRECTION_REQUIRES_NEW_RECORD

ELIGIBILITY_INPUT_CHANGE_MARKS_PRIOR_ELIGIBILITY_STALE
STALE_ELIGIBILITY_SUSPENDS_DEPENDENT_ASSIGNMENT
SUSPENDED_ASSIGNMENT_EMITS_REVOKE_REQUIRED

PROPOSED_ASSIGNMENT_DOES_NOT_AUTHORIZE_A13_ACCESS
ACTIVE_ASSIGNMENT_WITHOUT_A13_GRANT_IS_VALID
REVOKED_ASSIGNMENT_CANNOT_REACTIVATE_IN_PLACE
EXPIRED_ASSIGNMENT_CANNOT_REACTIVATE_IN_PLACE

PAIR_REVIEWER_INDEPENDENCE_COLLISIONS_REJECT
ADJUDICATOR_INDEPENDENCE_COLLISIONS_REJECT

ACTIVE_CONTENT_ROLE_PLUS_SAME_SUITE_RESULT_ACCESS_REJECTS
RESULT_EXPOSED_PERSON_CANNOT_RETURN_TO_SAME_SUITE_CONTENT_ROLE
RESULT_ACCESS_REVOCATION_DOES_NOT_RESTORE_RESULT_BLINDNESS

A7_ALLOW_GRANT_CONSIDERATION_IS_NOT_ACCESS_AUTHORIZATION
A13_GRANT_BINDS_CURRENT_A7_RECORD_HASH
STALE_A7_REFERENCE_CANNOT_KEEP_ACCESS_ACTIVE
A7_REVOKE_REQUIRED_FORCES_FAIL_CLOSED_A13_RECONCILIATION

UNKNOWN_ENUM_VALUE_REJECTS
DIGEST_MISMATCH_REJECTS
SILENT_DISPOSITION_REWRITE_REJECTS
```

## 46. Current unresolved implementation choices

```text
EXACT_A7_STATE_MACHINE_SCHEMA_PATH=UNRESOLVED
EXACT_A7_VALIDATOR_IMPLEMENTATION_PATH=UNRESOLVED
EXACT_A7_CANONICALIZATION_RULES=UNRESOLVED
EXACT_A7_A13_HANDSHAKE_TRANSPORT=UNRESOLVED
EXACT_A7_A13_REVOCATION_LATENCY_REQUIREMENT=NOT_YET_FROZEN
EXACT_A7_REVALIDATION_INTERVALS=NOT_YET_FROZEN
EXACT_A7_CALENDAR_EXPIRY_RULES=NOT_YET_FROZEN
EXACT_A7_OVERRIDE_OR_BREAK_GLASS_POLICY=NONE_NOT_AUTHORIZED
EXACT_PERSONNEL_ROSTER=UNRESOLVED
EXACT_VERIFIER_IDENTITIES=UNRESOLVED
```

## 47. Future operational PASS requirements

Before A7 may be considered operationally PASS, future canonical evidence must prove at least:

```text
A7_STATE_MACHINE_SCHEMA_CANONICAL=YES
A7_FAIL_CLOSED_VALIDATOR_IMPLEMENTED_AND_TESTED=YES
A7_RECORD_CANONICALIZATION_AND_HASHING_IMPLEMENTED=YES
A7_STALE_EVIDENCE_PROPAGATION_IMPLEMENTED=YES
A7_ASSIGNMENT_SUSPENSION_REVOCATION_IMPLEMENTED=YES
A7_A13_GRANT_CONSIDERATION_HANDSHAKE_IMPLEMENTED=YES
A7_A13_REVOKE_REQUIRED_HANDSHAKE_IMPLEMENTED=YES
A7_A13_STALE_REFERENCE_FAIL_CLOSED_BEHAVIOR_PROVEN=YES
EXACT_PERSONNEL_ROSTER_BOUND=YES
EXACT_REQUIRED_EVIDENCE_BOUND=YES
PAIR_LEVEL_INDEPENDENCE_VALIDATES=YES
SAME_SUITE_RESULT_EXPOSURE_FIREWALL_VALIDATES=YES
FRESH_INDEPENDENT_GOVERNANCE_REVIEW=YES
```

Q3 satisfies none of these implementation facts by itself.

## 48. Current readiness

```text
A7_STATE_MACHINE_IMPLEMENTATION=NO
A7_VALIDATOR_IMPLEMENTATION=NO
A7_A13_HANDSHAKE_IMPLEMENTATION=NO
EXACT_PERSONNEL_ROSTER=UNRESOLVED
EXACT_ROLE_ASSIGNMENTS=NONE
EXACT_A13_GRANTS=NONE

A7_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

## 49. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE

A7_STATE_MACHINE_IMPLEMENTATION_AUTHORITY=NONE
A7_VALIDATOR_IMPLEMENTATION_AUTHORITY=NONE
A7_PROTECTED_STORAGE_PROVISIONING_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_INGEST_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_ACCESS_AUTHORITY=NONE
A7_PERSONNEL_VERIFICATION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A7_QUALIFICATION_ADJUDICATION_AUTHORITY=NONE
A7_ROLE_TRANSITION_EXECUTION_AUTHORITY=NONE

A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY=NONE
A13_ROLE_ASSIGNMENT_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE
A13_RESULT_ACCESS_AUTHORITY=NONE

ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
```

## 50. Session 13 state after Q3

Acceptance of Q3 advances bounded Session 13 only.

```text
CLARIFICATION_SESSION_13=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

No A1–A15 implementation gate becomes operationally PASS merely because its clarification design is frozen.