# Session 13 Q4 — Verifier/Approver Separation of Duties and Personnel-Governance Decision Authority Contract

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 13 Q4 only. It freezes the verifier/approver separation-of-duties, personnel-governance decision-authority, disagreement, escalation, and downstream-consumption architecture for future A7 personnel governance. It does **not** identify or assign any person, verify any credential, ingest or access protected personnel evidence, provision storage, grant an A7 role, grant A13 payload/result access, access Private Gold, create or review selection cases, execute contamination assessment, execute models, spend funds, implement A1, authorize A15, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION13_Q4_POLICY=ROLE_SPECIFIC_EVIDENCE_VERIFICATION_AND_DISPOSITION_AUTHORITY_WITH_SEPARATION_OF_DUTIES_CONFLICT_SCREENING_FAIL_CLOSED_DISAGREEMENT_AND_NO_CUSTODIAN_OVERRIDE

A7_VERIFIER_APPROVER_SEPARATION_ARCHITECTURE=FROZEN
A7_PERSONNEL_DECISION_AUTHORITY_CONTRACT=FROZEN
A7_DISAGREEMENT_ESCALATION_ARCHITECTURE=FROZEN

A7_VERIFIER_ROSTER_ASSIGNED=NO
A7_APPROVER_ROSTER_ASSIGNED=NO
A7_ADJUDICATOR_ROSTER_ASSIGNED=NO
A7_DECISION_WORKFLOW_IMPLEMENTED=NO

A7_GATE_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY

CLARIFICATION_SESSION_13=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q4 distinguishes evidence custody, evidence verification, scientific/governance disposition, assignment, access enforcement, correction, and audit. No actor obtains all of these authorities merely through organizational seniority or system-administrator capability.

## 2. Separation-of-duties principle

Future A7 implementation must explicitly identify duties that require separation and bind system authorizations to those duties.

```text
SEPARATION_OF_DUTIES_REQUIRED_FOR_MATERIAL_PERSONNEL_GOVERNANCE=YES
LEAST_PRIVILEGE_REQUIRED_FOR_PERSONNEL_GOVERNANCE=YES
```

Methodological consistency reference:

```text
REFERENCE=NIST_SP_800_53_REV5_AC_5_SEPARATION_OF_DUTIES
REFERENCE=NIST_SP_800_53_REV5_AC_6_LEAST_PRIVILEGE
```

These references support the architectural principle only. Q4 does not claim NIST certification, regulatory compliance, or completeness against any external control framework.

```text
Q4_CLAIMS_EXTERNAL_COMPLIANCE=NO
```

## 3. No arbitrary global panel size

Q4 does not invent one universal verifier count or committee size.

```text
ONE_FIXED_VERIFIER_COUNT_FOR_ALL_EVIDENCE_CLASSES=PROHIBITED
ONE_FIXED_APPROVER_COUNT_FOR_ALL_DECISION_CLASSES=PROHIBITED
EXACT_PANEL_SIZE_BY_DECISION_CLASS=NOT_YET_FROZEN
```

Instead, separation is defined by **incompatible duties and actor identities**, not by a convenience headcount.

```text
DUTY_SEPARATION_MAY_NOT_BE_SATISFIED_BY_RENAMING_ONE_ACTOR_IN_MULTIPLE_FIELDS=YES
```

Where Q4 requires verifier/approver independence, the authoritative actor references must be distinct even if the future organization is small.

## 4. Authoritative functional roles

Future A7 must be able to represent at least these governance functions:

```text
PERSONNEL_SUBJECT_OR_EVIDENCE_PROVIDER
PERSONNEL_REGISTRY_CUSTODIAN
IDENTITY_EVIDENCE_VERIFIER
QUALIFICATION_EVIDENCE_VERIFIER
ROLE_SCOPE_QUALIFICATION_APPROVER
CONFLICT_REVIEWER
GOLD_EXPOSURE_RECONCILER
ROLE_ELIGIBILITY_DECISION_AUTHORITY
ROLE_ASSIGNMENT_AUTHORITY
ROLE_TRANSITION_DECISION_AUTHORITY
PERSONNEL_RECORD_CORRECTION_REVIEWER
PERSONNEL_GOVERNANCE_ADJUDICATOR
GOVERNANCE_AUDITOR
A13_ACCESS_GRANT_AUTHORITY
A13_ACCESS_REVOCATION_ENFORCER
```

These are governance capabilities, not employment titles.

```text
JOB_TITLE_ALONE_GRANTS_ANY_Q4_AUTHORITY=NO
FOUNDER_STATUS_ALONE_GRANTS_ANY_Q4_SCIENTIFIC_DISPOSITION_AUTHORITY=NO
REPOSITORY_ADMIN_STATUS_ALONE_GRANTS_ANY_Q4_SCIENTIFIC_DISPOSITION_AUTHORITY=NO
STORAGE_ADMIN_STATUS_ALONE_GRANTS_ANY_Q4_SCIENTIFIC_DISPOSITION_AUTHORITY=NO
```

## 5. Custody is not verification or approval

A future `PERSONNEL_REGISTRY_CUSTODIAN` may operate record lifecycle and protected-storage functions only within its exact scope.

```text
CUSTODIAN_MAY_MARK_IDENTITY_VERIFIED_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_MARK_QUALIFICATION_ACCEPTED_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_CLEAR_CONFLICT_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_MARK_GOLD_NONEXPOSED_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_COMPUTE_FINAL_ELIGIBILITY_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_ASSIGN_SCIENTIFIC_ROLE_BY_CUSTODY_ALONE=NO
CUSTODIAN_MAY_GRANT_A13_ACCESS_BY_CUSTODY_ALONE=NO
```

A custodian may record an already-authorized disposition but may not manufacture the disposition while acting only as custodian.

## 6. Subject self-verification prohibition

The person whose eligibility is being determined may provide evidence and attestations but may not be the sole independent authority establishing the corresponding material governance fact.

```text
SUBJECT_MAY_SUBMIT_IDENTITY_EVIDENCE=YES
SUBJECT_MAY_SUBMIT_QUALIFICATION_EVIDENCE=YES
SUBJECT_MAY_SUBMIT_CONFLICT_DISCLOSURE=YES
SUBJECT_MAY_SUBMIT_GOLD_NONEXPOSURE_ATTESTATION=YES

SUBJECT_MAY_SOLE_VERIFY_OWN_IDENTITY=NO
SUBJECT_MAY_SOLE_VERIFY_OWN_QUALIFICATION=NO
SUBJECT_MAY_SOLE_CLEAR_OWN_CONFLICT=NO
SUBJECT_MAY_SOLE_RECONCILE_OWN_GOLD_EXPOSURE=NO
SUBJECT_MAY_SOLE_APPROVE_OWN_ELIGIBILITY=NO
SUBJECT_MAY_SOLE_APPROVE_OWN_ROLE_TRANSITION=NO
```

The subject may challenge or correct factual records through the Q2 correction channel, but cannot directly set the resulting disposition.

## 7. Verification versus disposition

Q4 distinguishes:

```text
EVIDENCE_VERIFICATION=
  determine whether evidence is authentic_current_bound_and_supports_the_stated_fact

SCIENTIFIC_OR_GOVERNANCE_DISPOSITION=
  determine whether the verified fact is sufficient_for_the_exact_role_scope_under_the_current_policy
```

A verifier must not silently broaden the meaning of verified evidence into a role authorization.

```text
VERIFIED_EVIDENCE_EQUALS_ROLE_ELIGIBILITY=NO
VERIFIED_CREDENTIAL_EQUALS_UNBOUNDED_CLINICAL_SCOPE=NO
VERIFIED_IDENTITY_EQUALS_ROLE_ASSIGNMENT=NO
```

## 8. Material verifier/approver separation

For a decision that materially changes whether a person may author, adapt, accept, adjudicate, access controlled selection content, transition into result access, or satisfy a critical A7 eligibility prerequisite:

```text
MATERIAL_DECISION_REQUIRES_BOUND_EVIDENCE_VERIFICATION=YES
MATERIAL_DECISION_REQUIRES_IDENTIFIED_DISPOSITION_AUTHORITY=YES
```

Where the same actor both verifies evidence and issues the disposition, that overlap must be explicitly permitted by a future decision-class policy and must not violate any Q4 incompatible-duty rule.

```text
UNDECLARED_VERIFIER_APPROVER_COLOCATION=PROHIBITED
```

Q4 requires stronger separation for the decision classes explicitly named below. It does not assert that every clerical metadata field requires a second human reviewer.

## 9. Identity verification authority

Identity verification establishes that the opaque personnel reference resolves to the governed person.

```text
IDENTITY_SUBJECT != IDENTITY_EVIDENCE_VERIFIER
```

Minimum authoritative identity-verification record:

```text
identity_verification_decision_id
personnel_reference
identity_evidence_record_ids[]
verification_method_identity
verifier_governance_reference
verification_disposition
verification_scope
verification_event_or_version
record_canonical_sha256
```

Allowed dispositions:

```text
IDENTITY_VERIFIED
IDENTITY_NOT_VERIFIED
IDENTITY_BLOCKED_PENDING_EVIDENCE
IDENTITY_CONFLICTING_EVIDENCE
```

`IDENTITY_VERIFIED` may support the Q3 transition to `VERIFIED`; it does not create qualification, eligibility, assignment, or access.

## 10. Qualification evidence verification

Qualification evidence verification establishes provenance/authenticity/currentness of the claimed credential or competence evidence.

```text
QUALIFICATION_SUBJECT != QUALIFICATION_EVIDENCE_VERIFIER
```

The verifier must bind the exact evidence and claimed scope.

```text
QUALIFICATION_EVIDENCE_VERIFICATION_MAY_INFER_BROADER_SCOPE_THAN_EVIDENCE=NO
```

Minimum verification output:

```text
qualification_verification_record_id
personnel_reference
qualification_evidence_record_id
claimed_role_class
claimed_competence_scope
verification_disposition
verified_scope_if_any
validity_or_review_condition
verifier_governance_reference
record_canonical_sha256
```

## 11. Role-scope qualification approval

Whether verified evidence is scientifically sufficient for an exact Spec 005 role/scope is a distinct role-scope decision.

For clinically material content roles:

```text
ROLE_SCOPE_QUALIFICATION_APPROVER_MUST_HAVE_AUTHORITY_TO_ASSESS_ROLE_COMPETENCE=YES
```

The approver must not simply equate possession of a credential with competence across unrelated specialties, languages, registers, or use contexts.

```text
CREDENTIAL_EXISTS_EQUALS_ALL_CLINICAL_SCOPE_QUALIFIED=NO
```

For clinically material content roles, the qualification evidence verifier and role-scope qualification approver must be independently identifiable authorities.

```text
CLINICALLY_MATERIAL_ROLE_SCOPE_APPROVAL_REQUIRES_VERIFIER_APPROVER_SEPARATION=YES
```

This does not freeze an exact committee size.

## 12. Conflict disclosure and decision authority

The subject owns the duty to disclose; a separate conflict reviewer owns the disposition.

```text
CONFLICT_DISCLOSER=SUBJECT_OR_AUTHORIZED_SOURCE
CONFLICT_DECISION_AUTHORITY=CONFLICT_REVIEWER
SUBJECT_MAY_CLEAR_OWN_CONFLICT=NO
```

The conflict reviewer must have no material conflict in the decision being reviewed.

```text
CONFLICT_REVIEWER_WITH_MATERIAL_CONFLICT_FOR_SAME_DECISION=BLOCKED
```

Allowed final conflict dispositions remain:

```text
NO_MATERIAL_CONFLICT_IDENTIFIED
DISCLOSED_AND_REVIEWED_NO_DISQUALIFYING_CONFLICT
MATERIAL_CONFLICT_DISQUALIFYING
UNKNOWN_OR_UNRESOLVED
```

A conflict reviewer may not erase a disclosed relationship merely because the candidate outcome would otherwise be inconvenient.

```text
CANDIDATE_OUTCOME_MAY_RELAX_CONFLICT_DISPOSITION=NO
```

## 13. Gold nonexposure reconciliation authority

A self-attestation is evidence input, not the final Gold-exposure disposition.

```text
SELF_ATTESTATION_ALONE_EQUALS_CLEAN_GOLD_DISPOSITION=NO
GOLD_EXPOSURE_RECONCILER != PERSONNEL_SUBJECT
```

The reconciler consumes only the metadata/evidence permitted by Q1/Q2 and does not gain Private Gold case-content access merely to determine exposure status.

```text
GOLD_EXPOSURE_RECONCILIATION_REQUIRES_PRIVATE_GOLD_CASE_CONTENT=NO
```

If attestation and audit/access evidence conflict:

```text
GOLD_EXPOSURE_DISPOSITION=CONFLICTING_EVIDENCE
ELIGIBILITY_CONSEQUENCE=BLOCKED
```

No founder, custodian, or assignment authority may override that conflict by convenience.

## 14. Eligibility decision authority

The Q3 eligibility state must be evaluator/policy derived from current authoritative inputs.

The `ROLE_ELIGIBILITY_DECISION_AUTHORITY` is responsible for validating that all required inputs are current, scope-compatible, non-conflicting, and governed by the current policy identity.

```text
ELIGIBILITY_DECISION_AUTHORITY_MAY_REWRITE_SOURCE_VERIFICATION_RECORDS=NO
ELIGIBILITY_DECISION_AUTHORITY_MAY_CLEAR_CONFLICT_WITHOUT_CONFLICT_DECISION=NO
ELIGIBILITY_DECISION_AUTHORITY_MAY_DECLARE_GOLD_NONEXPOSURE_WITHOUT_RECONCILIATION=NO
ELIGIBILITY_DECISION_AUTHORITY_MAY_IGNORE_STALE_INPUT=NO
```

Where eligibility can be deterministically computed from canonical inputs, the final derived state may be produced by an automated evaluator.

```text
DETERMINISTIC_ELIGIBILITY_COMPUTATION_ALLOWED=YES
AUTOMATED_ELIGIBILITY_COMPUTATION_MAY_INVENT_MISSING_EVIDENCE=NO
AUTOMATED_ELIGIBILITY_COMPUTATION_MAY_OVERRIDE_HUMAN_GOVERNANCE_DISPOSITION=NO
```

## 15. Assignment authority is downstream of eligibility

`ROLE_ASSIGNMENT_AUTHORITY` may bind an eligible person to an exact role/suite/content scope, but cannot alter eligibility to make the assignment possible.

```text
ASSIGNMENT_AUTHORITY_MAY_CHANGE_ELIGIBILITY_DISPOSITION=NO
ASSIGNMENT_AUTHORITY_MAY_BROADEN_ELIGIBILITY_SCOPE=NO
ASSIGNMENT_AUTHORITY_MAY_ASSIGN_INELIGIBLE_PERSON=NO
ASSIGNMENT_AUTHORITY_MAY_ASSIGN_STALE_ELIGIBILITY=NO
```

An assignment record must reference the exact current eligibility record it consumes.

## 16. Assignment authority and scientific content independence

The assignment authority may coordinate staffing but does not become an author/reviewer merely by making the assignment.

```text
ASSIGNMENT_AUTHORITY_IMPLIES_CONTENT_EDIT_AUTHORITY=NO
ASSIGNMENT_AUTHORITY_IMPLIES_FINAL_REVIEW_AUTHORITY=NO
```

If an assignment authority is also proposed for a scientific content role, that second role must independently satisfy A7 eligibility and A8 independence rules.

## 17. Role-transition decision authority

Transitions across information domains require a specific `ROLE_TRANSITION_DECISION_AUTHORITY` consuming the Q3 transition prerequisites.

Examples include:

```text
CONTENT_ROLE -> CANDIDATE_RESULT_ANALYST
SELECTION_ROLE -> PRIVATE_GOLD_TRUSTEE_OR_FINAL_AUDIT_ROLE
SUSPENDED -> REACTIVATED_ELIGIBILITY_PATH
```

The transition decision authority cannot manufacture prerequisite closure.

```text
TRANSITION_AUTHORITY_MAY_IGNORE_OPEN_CONTENT_TASKS=NO
TRANSITION_AUTHORITY_MAY_TREAT_RESULT_ACCESS_REVOCATION_AS_RESULT_BLINDNESS=NO
TRANSITION_AUTHORITY_MAY_ERASE_VALID_GOLD_EXPOSURE_HISTORY=NO
```

## 18. A13 grant authority is separate from A7 eligibility/assignment

A7 may emit an opaque `ALLOW_GRANT_CONSIDERATION` signal only after current eligibility and active assignment are valid.

A13 owns the actual grant decision and enforcement.

```text
A7_ROLE_ELIGIBILITY_DECISION_AUTHORITY_MAY_DIRECTLY_CREATE_A13_ACCESS_GRANT=NO
A7_ROLE_ASSIGNMENT_AUTHORITY_MAY_DIRECTLY_CREATE_A13_ACCESS_GRANT=NO

A13_ACCESS_GRANT_AUTHORITY_MAY_RECOMPUTE_A7_ELIGIBILITY=NO
A13_ACCESS_GRANT_AUTHORITY_MAY_OVERRIDE_A7_DENY=NO
A13_ACCESS_GRANT_AUTHORITY_MAY_OVERRIDE_A7_REVOKE_REQUIRED=NO
```

This is a cross-system separation-of-duties boundary.

## 19. A13 grant inputs

A13 may consume only the minimum opaque current-state contract frozen by Q2/Q3, including:

```text
personnel_reference
role_eligibility_record_id
role_assignment_id
role_class
suite_or_scope_id
assignment_state
allowed_governance_actions
eligibility_policy_identity
current_record_hashes
A7_handshake_signal
expiry_or_revocation_condition
```

A13 must not demand raw credentials or conflict evidence in order to enforce the grant.

## 20. Revocation enforcement separation

If A7 emits `REVOKE_REQUIRED`, A13 must enforce revocation under its own access-control mechanism.

```text
A7_REVOKE_REQUIRED_EQUALS_A13_IGNORE_ALLOWED=NO
A13_REVOCATION_ENFORCER_MAY_REOPEN_A7_ELIGIBILITY=NO
```

An A13 enforcement failure does not make the A7 state valid; it is a separate fail-closed integration defect.

```text
A7_REVOKED_BUT_A13_ACCESS_ACTIVE=FAIL_CLOSED_GATE_FAILURE
```

## 21. Audit administration separation

The actor capable of granting/revoking controlled access must not have unilateral ability to erase or rewrite the audit evidence proving those actions.

```text
ACCESS_CONTROL_ADMINISTRATOR_MAY_SILENTLY_REWRITE_AUDIT_LOG=NO
AUDIT_LOG_ADMINISTRATOR_MAY_SILENTLY_CREATE_ACCESS_GRANT=NO
```

A future implementation may use technical controls rather than separate full-time employees, but the incompatible authorities must remain independently enforceable.

```text
SAME_ORGANIZATION_MAY_IMPLEMENT_TECHNICAL_SEPARATION=YES
SAME_UNCONTROLLED_CREDENTIAL_MAY_HOLD_BOTH_ACCESS_AND_AUDIT_SUPERUSER_AUTHORITY=NO
```

## 22. Governance auditor role

`GOVERNANCE_AUDITOR` evaluates whether the process and records conform to the frozen policy but does not automatically become the original decision authority.

```text
AUDITOR_MAY_INSPECT_AUTHORIZED_OPAQUE_GOVERNANCE_RECORDS=YES
AUDITOR_RAW_EVIDENCE_ACCESS_BY_DEFAULT=NO
AUDITOR_MAY_REWRITE_ORIGINAL_DISPOSITION_IN_PLACE=NO
AUDITOR_MAY_CREATE_CORRECTION_OR_ESCALATION_FINDING=YES
```

An auditor who materially participated in the original disputed decision is not independent for the independent-audit function of that same decision.

```text
ORIGINAL_DECISION_ACTOR_COUNTS_AS_INDEPENDENT_AUDITOR_FOR_SAME_DECISION=NO
```

## 23. Correction authority

A correction request must be reviewed by `PERSONNEL_RECORD_CORRECTION_REVIEWER` under Q2 append-only correction semantics.

```text
SUBJECT_MAY_REQUEST_CORRECTION=YES
SUBJECT_MAY_APPROVE_OWN_CORRECTION=NO
```

If the correction alleges an error, conflict, or misconduct by the original decision authority:

```text
ORIGINAL_DISPUTED_DECISION_ACTOR_MAY_BE_SOLE_CORRECTION_APPROVER=NO
```

The original actor may provide evidence or explanation but cannot alone decide the challenge to their own disputed decision.

## 24. Disagreement classes

Q4 freezes minimum disagreement classes:

```text
EVIDENCE_AUTHENTICITY_DISAGREEMENT
EVIDENCE_SCOPE_DISAGREEMENT
QUALIFICATION_SCOPE_DISAGREEMENT
CONFLICT_MATERIALITY_DISAGREEMENT
GOLD_EXPOSURE_RECONCILIATION_DISAGREEMENT
ELIGIBILITY_INPUT_CONSISTENCY_DISAGREEMENT
ROLE_TRANSITION_PREREQUISITE_DISAGREEMENT
CORRECTION_DISPOSITION_DISAGREEMENT
POLICY_INTERPRETATION_AMBIGUITY
```

Disagreement does not become PASS by majority convenience or founder preference.

## 25. Fail-closed disagreement state

When a material disagreement is unresolved:

```text
MATERIAL_DISAGREEMENT_STATE=BLOCKED_PENDING_ADJUDICATION
NEW_ROLE_ASSIGNMENT=DENY
NEW_A13_ACCESS_GRANT=DENY
NEW_CONTENT_WRITE_OR_FINAL_REVIEW_ACCEPTANCE=DENY_IF_DECISION_IS_RELEVANT
```

If the disputed fact is already relied upon by an active role:

```text
DEPENDENT_ELIGIBILITY=STALE_RECOMPUTE_REQUIRED_OR_BLOCKED_AS_POLICY_REQUIRES
DEPENDENT_ASSIGNMENT=SUSPEND_IF_MATERIAL
A13_HANDSHAKE=REVALIDATION_REQUIRED_OR_REVOKE_REQUIRED
```

Historical frozen scientific artifacts are not silently rewritten.

## 26. Personnel-governance adjudicator

A `PERSONNEL_GOVERNANCE_ADJUDICATOR` may resolve a material governance disagreement only if qualified for the exact decision class and independent of the specific conflicting interests.

At minimum:

```text
ADJUDICATOR != PERSONNEL_SUBJECT
ADJUDICATOR_WITH_MATERIAL_CONFLICT_FOR_DECISION=BLOCKED
ADJUDICATOR_MUST_NOT_BE_THE_SOLE_ORIGINAL_DISPUTED_DECISION_ACTOR=YES
```

Where the disagreement concerns a role-scope clinical qualification, the adjudicator must have competence sufficient to assess that scope; an administrative tie-breaker is insufficient.

```text
CLINICAL_SCOPE_DISAGREEMENT_ADMINISTRATIVE_TIEBREAKER_ONLY=PROHIBITED
```

## 27. No automatic majority rule

Q4 does not freeze a majority-vote panel model.

```text
SIMPLE_MAJORITY_VOTE_ALWAYS_CONTROLS_PERSONNEL_GOVERNANCE=NO
UNANIMOUS_PANEL_ALWAYS_REQUIRED=NO
```

The exact adjudication method may vary by decision class, but it must be predeclared, conflict-screened, evidence-bound, and fail closed when the required decision cannot be reached.

```text
EXACT_ADJUDICATION_METHOD_BY_DECISION_CLASS=NOT_YET_FROZEN
```

## 28. No founder override of scientific eligibility facts

Repository/founder authority may approve governance policy, budgets, activation boundaries, or staffing processes when separately authorized, but it cannot substitute for a required qualified verifier/reviewer/adjudicator on a scientific personnel disposition.

```text
FOUNDER_MAY_UNILATERALLY_MARK_UNVERIFIED_IDENTITY_VERIFIED=NO
FOUNDER_MAY_UNILATERALLY_MARK_UNQUALIFIED_PERSON_QUALIFIED=NO
FOUNDER_MAY_UNILATERALLY_CLEAR_MATERIAL_CONFLICT=NO
FOUNDER_MAY_UNILATERALLY_MARK_CONFLICTING_GOLD_EVIDENCE_CLEAN=NO
FOUNDER_MAY_UNILATERALLY_OVERRIDE_INDEPENDENCE_COLLISION=NO
```

A later governance-policy change may change future policy only through versioned review; it cannot retroactively rewrite the historical decision record.

## 29. No candidate-result override

Personnel-governance decisions must remain candidate-neutral.

```text
CANDIDATE_RESULT_MAY_SELECT_VERIFIER=NO
CANDIDATE_RESULT_MAY_SELECT_APPROVER=NO
CANDIDATE_RESULT_MAY_RELAX_QUALIFICATION_REQUIREMENT=NO
CANDIDATE_RESULT_MAY_RELAX_CONFLICT_RULE=NO
CANDIDATE_RESULT_MAY_RELAX_GOLD_NONEXPOSURE_RULE=NO
CANDIDATE_RESULT_MAY_RELAX_INDEPENDENCE_RULE=NO
```

A preferred candidate performing poorly or well is never a valid reason to change who is considered qualified for an already governed decision.

## 30. Reviewer independence from candidate developers

For personnel decisions controlling scientific content acceptance, a materially candidate-conflicted actor is not an acceptable independent approver.

```text
MATERIAL_CANDIDATE_CONFLICTED_APPROVER_FOR_CONTENT_ACCEPTANCE_ROLE=BLOCKED
```

This does not declare every prior model-related activity disqualifying; the exact conflict disposition remains evidence-bound under Q1.

## 31. Verifier qualification

Each verifier/approver/adjudicator must themselves have an A7 governance identity and a qualification/conflict disposition appropriate to the assigned decision function.

```text
ANONYMOUS_VERIFIER=PROHIBITED
ANONYMOUS_APPROVER=PROHIBITED
ANONYMOUS_ADJUDICATOR=PROHIBITED

UNQUALIFIED_VERIFIER_FOR_DECISION_CLASS=BLOCKED
UNQUALIFIED_APPROVER_FOR_DECISION_CLASS=BLOCKED
UNQUALIFIED_ADJUDICATOR_FOR_DECISION_CLASS=BLOCKED
```

Q4 does not create an infinite regress requiring each verifier to verify their own eligibility. The future governance bootstrap/root-of-trust procedure remains a separate implementation prerequisite and must itself be independently reviewed before operational PASS.

```text
EXACT_A7_GOVERNANCE_BOOTSTRAP_ROOT_OF_TRUST=UNRESOLVED
```

## 32. Machine/service verification boundary

Automated systems may support deterministic authenticity checks, digest verification, expiry checks, policy evaluation, and state-machine validation where the exact method is canonical.

```text
AUTOMATED_DETERMINISTIC_EVIDENCE_CHECK_ALLOWED=YES
AUTOMATED_STATE_MACHINE_VALIDATION_ALLOWED=YES
```

Automation does not automatically replace qualified human scientific judgment where scope/clinical competence/conflict interpretation is materially judgment-dependent.

```text
AUTOMATION_MAY_UNILATERALLY_DECIDE_JUDGMENT_DEPENDENT_CLINICAL_SCOPE=NO
AUTOMATION_MAY_UNILATERALLY_CLEAR_AMBIGUOUS_MATERIAL_CONFLICT=NO
AUTOMATION_MAY_UNILATERALLY_RESOLVE_CONFLICTING_GOLD_EXPOSURE_EVIDENCE=NO
```

No model/LLM use is authorized by Q4.

```text
LLM_ASSISTED_PERSONNEL_GOVERNANCE=NOT_AUTHORIZED
```

## 33. Decision record identity

Every material disposition must create an identity-bound decision record.

Minimum fields:

```text
decision_record_id
decision_class
personnel_reference
role_class_or_explicit_not_applicable
suite_or_scope_id_or_explicit_not_applicable
input_record_ids[]
input_record_sha256s[]
verifier_governance_references[]
approver_or_decision_authority_reference
decision_disposition
decision_policy_id
decision_policy_version
independence_validation_record_id
conflict_screening_record_id
adjudication_record_id_or_explicit_none
supersedes_decision_record_id_or_explicit_none
record_version
record_canonical_sha256
```

Raw protected evidence must not be copied into the broadly visible decision record.

## 34. Independence validation record

Before a material decision becomes effective, future A7 must validate incompatible-duty constraints.

Minimum output:

```text
independence_validation_record_id
decision_record_id
subject_reference
verifier_references[]
approver_reference
adjudicator_reference_or_none
custodian_reference_if_relevant
assignment_authority_reference_if_relevant
incompatible_duty_checks[]
conflict_checks[]
disposition
record_canonical_sha256
```

Allowed disposition:

```text
PASS
FAIL
BLOCKED_PENDING_EVIDENCE
```

Only `PASS` may support the governed material decision becoming effective.

## 35. Incompatible-duty minimum rules

The future validator must fail closed on at least:

```text
SUBJECT_IS_SOLE_IDENTITY_VERIFIER
SUBJECT_IS_SOLE_QUALIFICATION_VERIFIER
SUBJECT_IS_OWN_CONFLICT_DECISION_AUTHORITY
SUBJECT_IS_OWN_GOLD_EXPOSURE_RECONCILER
SUBJECT_IS_OWN_ELIGIBILITY_OVERRIDE_AUTHORITY

CUSTODIAN_ALONE_ISSUES_SCIENTIFIC_DISPOSITION
CUSTODIAN_ALONE_GRANTS_ROLE_OR_ACCESS

CLINICAL_ROLE_SCOPE_VERIFIER_APPROVER_SEPARATION_REQUIRED_BUT_COLLIDES

MATERIAL_CONFLICTED_VERIFIER_OR_APPROVER
UNBOUND_VERIFIER_OR_APPROVER_IDENTITY
UNQUALIFIED_VERIFIER_OR_APPROVER_FOR_DECISION_CLASS

ASSIGNMENT_AUTHORITY_ALTERS_ELIGIBILITY
A13_GRANT_AUTHORITY_OVERRIDES_A7_DENY_OR_REVOKE

ACCESS_ADMIN_CAN_UNILATERALLY_ERASE_AUDIT_TRAIL
AUDITOR_CAN_UNILATERALLY_CREATE_ACCESS_GRANT

DISPUTED_ORIGINAL_ACTOR_SOLE_APPROVES_CORRECTION
DISPUTED_ORIGINAL_ACTOR_SOLE_ADJUDICATES_OWN_DECISION
```

## 36. Pair-review independence remains separate

Q4 does not replace A8's content-level reviewer independence constraints.

```text
A7_PERSONNEL_DECISION_SOD_MAY_OVERRIDE_A8_AUTHOR_REVIEWER_SEPARATION=NO
A7_PERSONNEL_DECISION_SOD_MAY_REDUCE_A8_CLINICAL_REVIEW_REQUIREMENT=NO
```

A future personnel assignment must satisfy both Q4 personnel-governance separation and A8 content-review independence.

## 37. Public/private boundary

Broadly visible governance artifacts may expose only opaque actor references and dispositions needed for reproducibility.

```text
PUBLIC_DECISION_RECORD_MAY_CONTAIN_RAW_IDENTITY_DOCUMENT=NO
PUBLIC_DECISION_RECORD_MAY_CONTAIN_RAW_CREDENTIAL=NO
PUBLIC_DECISION_RECORD_MAY_CONTAIN_RAW_CONFLICT_DISCLOSURE=NO
PUBLIC_DECISION_RECORD_MAY_CONTAIN_SIGNED_GOLD_ATTESTATION_BODY=NO
```

Protected details remain in the Q2 protected store.

## 38. Decision authority does not imply protected-evidence browsing

An approver should receive only the evidence/dispositions necessary to make the assigned decision.

```text
APPROVER_DEFAULT_FULL_ARCHIVE_ACCESS=NO
APPROVER_DEFAULT_RAW_HIGH_SENSITIVITY_EVIDENCE_ACCESS=NO
TASK_SCOPED_DECISION_VIEW_PREFERRED=YES
```

For example, an assignment authority normally consumes a valid eligibility output rather than raw credential documents.

## 39. Decision supersession

A new corrected or re-evaluated decision must supersede, not silently rewrite, prior history.

```text
SILENT_IN_PLACE_DECISION_REWRITE=PROHIBITED
SUPERSEDED_DECISION_REMAINS_HISTORICALLY_AUDITABLE=YES
SUPERSEDED_DECISION_MAY_REMAIN_CURRENT=NO
```

Candidate performance is not a valid supersession cause.

## 40. Policy-version changes

A material Q4 policy change requires a new policy identity.

```text
SILENT_DECISION_AUTHORITY_POLICY_REINTERPRETATION=PROHIBITED
HISTORICAL_DECISION_POLICY_IDENTITY_MUST_REMAIN_REPRODUCIBLE=YES
```

A new policy may trigger revalidation of future or active eligibility if explicitly governed, but cannot silently alter historical records.

## 41. Event-driven revalidation

Material events that must trigger decision revalidation where relevant include:

```text
VERIFIER_OR_APPROVER_CONFLICT_DISCOVERED
VERIFIER_OR_APPROVER_QUALIFICATION_INVALIDATED
EVIDENCE_RECORD_SUPERSEDED_OR_CORRECTED
GOLD_EXPOSURE_EVENT_RECORDED
MATERIAL_CONFLICT_DISCLOSURE_CHANGED
IDENTITY_SUSPENDED_OR_RETIRED
ROLE_POLICY_VERSION_CHANGED
DECISION_INDEPENDENCE_COLLISION_DISCOVERED
AUDIT_INTEGRITY_INCIDENT
```

Consequences follow Q3 staleness propagation.

## 42. Disagreement audit record

Every material disagreement/escalation must be identity-bound.

Minimum future fields:

```text
disagreement_record_id
decision_class
personnel_reference
subject_decision_record_id_or_evidence_ids[]
disagreement_class
positions_or_dispositions_by_opaque_actor_reference
protected_rationale_references[]
adjudicator_governance_reference_or_none
resolution_disposition
resulting_decision_record_id_or_none
record_canonical_sha256
```

Public metadata must not expose raw protected rationale.

## 43. Allowed disagreement resolutions

Minimum closed resolution vocabulary:

```text
RESOLVED_UPHOLD
RESOLVED_SUPERSEDE_WITH_NEW_DECISION
BLOCKED_PENDING_ADDITIONAL_EVIDENCE
INELIGIBLE_OR_DENIED
ESCALATED_TO_SEPARATE_POLICY_REVIEW
```

There is no `FOUNDER_OVERRIDE_PASS` disposition.

## 44. Policy ambiguity

If the disagreement is caused by policy ambiguity rather than evidence conflict:

```text
CURRENT_DECISION=BLOCKED_IF_AMBIGUITY_IS_MATERIAL
POLICY_CHANGE_REQUIRES_VERSIONED_GOVERNANCE=YES
```

The policy must be clarified prospectively; the ambiguity cannot be resolved by silently choosing whichever interpretation admits a preferred person.

## 45. Emergency security suspension

A future security incident may require immediate suspension/revocation before full adjudication.

```text
EMERGENCY_FAIL_CLOSED_SUSPENSION_ALLOWED=YES_IF_SEPARATELY_IMPLEMENTED_AND_AUTHORIZED
EMERGENCY_SUSPENSION_EQUALS_FINAL_MISCONDUCT_FINDING=NO
```

Emergency action must be audited and later reconciled through normal governance.

Q4 itself authorizes no suspension because no operational registry exists.

## 46. Relationship to Q1

Q1 remains authoritative for:

```text
ROLE_SPECIFIC_QUALIFICATION_REQUIREMENTS
GOLD_EXPOSURE_DISPOSITION_VOCABULARY
CONFLICT_DISPOSITION_VOCABULARY
PAIR_LEVEL_PERSONNEL_INDEPENDENCE
ROLE_TRANSITION_FIREWALL
```

Q4 specifies who may verify/decide those facts; it does not weaken them.

## 47. Relationship to Q2

Q2 remains authoritative for:

```text
PROTECTED_PERSONNEL_EVIDENCE_STORAGE_BOUNDARY
DATA_MINIMIZATION
LEAST_PRIVILEGE_PROTECTED_EVIDENCE_ACCESS
APPEND_ONLY_CORRECTION
RETENTION_AND_DESTRUCTION_ARCHITECTURE
AUDIT_PRIVACY
```

Q4 decision authorities consume protected evidence only through Q2-authorized views.

## 48. Relationship to Q3

Q3 remains authoritative for:

```text
IDENTITY_STATE_MACHINE
ELIGIBILITY_STATE_MACHINE
ASSIGNMENT_STATE_MACHINE
A7_A13_HANDSHAKE_STATE
STALE_RECOMPUTE_PROPAGATION
```

Q4 decision records are inputs to the Q3 state transitions; Q4 does not add a bypass transition.

```text
Q4_DECISION_AUTHORITY_MAY_BYPASS_Q3_STATE_MACHINE=NO
```

## 49. Relationship to A13

A13 remains authoritative for actual access-control enforcement.

```text
Q4_DECISION_AUTHORITY_MAY_GRANT_ZONE2_OR_ZONE3_ACCESS_DIRECTLY=NO
A13_MAY_TREAT_OPAQUE_Q4_DECISION_AS_RAW_PERSONNEL_EVIDENCE=NO
```

Q4 only ensures that the A7 input consumed by A13 was produced under the required personnel-governance authority contract.

## 50. Operational PASS prerequisites

Before Q4's governance component can be considered operationally PASS, future canonical evidence must prove at least:

```text
EXACT_DECISION_CLASS_REGISTRY_CANONICAL=YES
EXACT_INCOMPATIBLE_DUTY_MATRIX_CANONICAL=YES
EXACT_VERIFIER_AUTHORITY_BINDINGS_CANONICAL=YES
EXACT_APPROVER_AUTHORITY_BINDINGS_CANONICAL=YES
EXACT_ADJUDICATOR_AUTHORITY_BINDINGS_CANONICAL=YES
EXACT_CONFLICT_SCREENING_MECHANISM_CANONICAL=YES
EXACT_INDEPENDENCE_VALIDATOR_IMPLEMENTED=YES
EXACT_DISAGREEMENT_AND_ESCALATION_WORKFLOW_CANONICAL=YES
EXACT_CORRECTION_REVIEW_SEPARATION_CANONICAL=YES
EXACT_A13_GRANT_REVOCATION_HANDSHAKE_IMPLEMENTED=YES
EXACT_AUDIT_SEPARATION_ENFORCEMENT_CANONICAL=YES
EXACT_PERSONNEL_ROSTER_BOUND=YES
FRESH_INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Q4 proves none of these implementation facts by itself.

## 51. Current unresolved implementation choices

```text
EXACT_VERIFIER_IDENTITIES=UNRESOLVED
EXACT_APPROVER_IDENTITIES=UNRESOLVED
EXACT_ADJUDICATOR_IDENTITIES=UNRESOLVED
EXACT_ASSIGNMENT_AUTHORITY_IDENTITIES=UNRESOLVED
EXACT_A13_ACCESS_GRANT_AUTHORITY_IDENTITIES=UNRESOLVED
EXACT_GOVERNANCE_AUDITOR_IDENTITIES=UNRESOLVED

EXACT_PANEL_SIZE_BY_DECISION_CLASS=NOT_YET_FROZEN
EXACT_ADJUDICATION_METHOD_BY_DECISION_CLASS=NOT_YET_FROZEN
EXACT_AUTOMATION_MECHANISM=UNRESOLVED
EXACT_GOVERNANCE_BOOTSTRAP_ROOT_OF_TRUST=UNRESOLVED
```

## 52. Fail-closed conditions

Future Q4 validation must fail closed on at least:

```text
UNKNOWN_DECISION_CLASS
UNKNOWN_OR_UNBOUND_SUBJECT_IDENTITY
UNKNOWN_OR_UNBOUND_VERIFIER_IDENTITY
UNKNOWN_OR_UNBOUND_APPROVER_IDENTITY
UNKNOWN_OR_UNBOUND_ADJUDICATOR_IDENTITY_WHERE_REQUIRED

SOLE_SELF_VERIFICATION_OF_MATERIAL_EVIDENCE
SOLE_SELF_APPROVAL_OF_MATERIAL_ELIGIBILITY_DECISION
CUSTODIAN_ONLY_SCIENTIFIC_DISPOSITION

MATERIAL_VERIFIER_OR_APPROVER_CONFLICT
QUALIFICATION_OUTSIDE_DECISION_AUTHORITY_SCOPE
CLINICAL_ROLE_SCOPE_APPROVAL_WITHOUT_REQUIRED_COMPETENCE

REQUIRED_VERIFIER_APPROVER_SEPARATION_COLLISION
DISPUTED_ORIGINAL_ACTOR_SOLE_CORRECTION_APPROVER
DISPUTED_ORIGINAL_ACTOR_SOLE_ADJUDICATOR

UNRESOLVED_MATERIAL_DISAGREEMENT
POLICY_AMBIGUITY_MATERIALLY_AFFECTING_DECISION

ASSIGNMENT_AUTHORITY_OVERRIDES_ELIGIBILITY
A13_GRANT_AUTHORITY_OVERRIDES_A7_DENY
A13_GRANT_AUTHORITY_OVERRIDES_A7_REVOKE_REQUIRED

ACCESS_ADMIN_UNILATERALLY_REWRITES_AUDIT
AUDITOR_UNILATERALLY_CREATES_ACCESS_GRANT

CANDIDATE_RESULT_DRIVEN_PERSONNEL_GOVERNANCE_RELAXATION
FOUNDER_CONVENIENCE_OVERRIDE_OF_REQUIRED_SCIENTIFIC_DISPOSITION
```

## 53. Current readiness

```text
A7_DECISION_AUTHORITY_WORKFLOW_IMPLEMENTED=NO
A7_INDEPENDENCE_VALIDATOR_IMPLEMENTED=NO
A7_DISAGREEMENT_WORKFLOW_IMPLEMENTED=NO
A7_EXACT_VERIFIER_ROSTER=UNRESOLVED
A7_EXACT_APPROVER_ROSTER=UNRESOLVED
A7_EXACT_ADJUDICATOR_ROSTER=UNRESOLVED
A7_EXACT_PERSONNEL_ROSTER=UNRESOLVED

A7_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
```

## 54. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE

A7_DECISION_WORKFLOW_IMPLEMENTATION_AUTHORITY=NONE
A7_STATE_MACHINE_IMPLEMENTATION_AUTHORITY=NONE
A7_VALIDATOR_IMPLEMENTATION_AUTHORITY=NONE
A7_PROTECTED_STORAGE_PROVISIONING_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_INGEST_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_ACCESS_AUTHORITY=NONE
A7_PERSONNEL_VERIFICATION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A7_QUALIFICATION_ADJUDICATION_AUTHORITY=NONE
A7_CONFLICT_ADJUDICATION_AUTHORITY=NONE
A7_GOLD_NONEXPOSURE_ATTESTATION_EXECUTION_AUTHORITY=NONE
A7_GOLD_EXPOSURE_RECONCILIATION_AUTHORITY=NONE
A7_ROLE_TRANSITION_EXECUTION_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_EXPORT_AUTHORITY=NONE
A7_PERSONNEL_EVIDENCE_DESTRUCTION_AUTHORITY=NONE

A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY=NONE
A13_PAYLOAD_UPLOAD_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE
A13_RESULT_ACCESS_AUTHORITY=NONE
A13_ROLE_ASSIGNMENT_AUTHORITY=NONE

ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
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
PRIVATE_GOLD_TRUSTEE_ASSIGNMENT_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
```

## 55. Session 13 state after Q4

Acceptance of Q4 advances bounded Session 13 only.

```text
CLARIFICATION_SESSION_13=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_13_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

No A1–A15 implementation gate becomes operationally PASS merely because Q4 governance design is frozen.
