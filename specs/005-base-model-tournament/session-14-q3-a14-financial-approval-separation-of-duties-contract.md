# Session 14 Q3 — A14 Authorization Approval Authority and Segregation of Financial Duties

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 14 Q3 only. It freezes the governance architecture for who may approve an A14 authorization, who may create a financial or engagement commitment, who may execute payment, who may reconcile/audit the transaction, and how conflicts involving a payee, vendor, contractor, reviewer, author, or other beneficiary are handled. It does not assign any person, select any vendor or payee, approve any amount, execute any payment or contract, provision any service, engage any reviewer/author, access any payment instrument, or authorize PLAN, construction, model execution, payload access, or Private Gold access.

## 1. Frozen decision

```text
SESSION14_Q3_POLICY=SEGREGATED_PRECOMMITMENT_FINANCIAL_APPROVAL_WITH_NO_SELF_APPROVAL_PAYEE_CONFLICT_SCREENING_SEPARATE_PAYMENT_EXECUTION_AND_INDEPENDENT_RECONCILIATION

A14_APPROVAL_AUTHORITY_ARCHITECTURE=FROZEN
A14_FINANCIAL_SEPARATION_OF_DUTIES=FROZEN
A14_PAYEE_VENDOR_CONFLICT_RULES=FROZEN
A14_PAYMENT_RECONCILIATION_ARCHITECTURE=FROZEN

A14_APPROVER_ROSTER_ASSIGNED=NO
A14_PAYMENT_EXECUTOR_ASSIGNED=NO
A14_RECONCILER_ASSIGNED=NO
A14_AUTHORIZATION_RECORD_ISSUED=NO
A14_OPERATIONAL_PASS=NO

CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE

CLARIFICATION_SESSION_14=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_14_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q3 changes no spend boundary. Session 6 Q5 and Session 14 Q1/Q2 remain intact.

## 2. Distinct financial-governance functions

Future A14 implementation must treat the following functions as distinct governance roles, even if a small organization later uses the same person for more than one non-conflicting function under an explicitly reviewed exception:

```text
REQUIREMENT_DETERMINATION_AUTHORITY
A14_AUTHORIZATION_APPROVER
COMMITMENT_OR_CONTRACT_EXECUTOR
PAYMENT_EXECUTOR
PAYMENT_RECONCILER
FINANCIAL_GOVERNANCE_AUDITOR
PAYEE_OR_BENEFICIARY
VENDOR_OR_SERVICE_PROVIDER
```

Scientific role authorities remain separate:

```text
A7_ROLE_ELIGIBILITY_AUTHORITY
A7_ROLE_ASSIGNMENT_AUTHORITY
A13_ACCESS_AUTHORITY
A15_CONSTRUCTION_ACTIVATION_AUTHORITY
```

The following equivalences are prohibited:

```text
REQUIREMENT_DETERMINATION_EQUALS_SPEND_AUTHORIZATION=NO
SPEND_AUTHORIZATION_EQUALS_PAYMENT_EXECUTION=NO
PAYMENT_EXECUTION_EQUALS_RECONCILIATION=NO
PAYMENT_RECONCILIATION_EQUALS_SCIENTIFIC_ELIGIBILITY=NO
CONTRACT_EXECUTION_EQUALS_PAYLOAD_ACCESS=NO
```

## 3. Requirement determination is advisory to authorization, not itself authority

Session 14 Q2 may conclude that A14 is `REQUIRED`, but that conclusion grants no commitment authority.

```text
A14_REQUIRED_PENDING_AUTHORIZATION_EQUALS_FINANCIAL_AUTHORITY=NO
WORKLOAD_MANIFEST_EQUALS_PURCHASE_APPROVAL=NO
CAPACITY_GAP_EQUALS_VENDOR_SELECTION_AUTHORITY=NO
```

An authorization approver must independently confirm that the proposed authorization is bounded by the exact requirement identity produced under Q2.

## 4. Authorization approver authority

A future `A14_AUTHORIZED_PASS` requires one or more identified approval authorities whose scope is explicit and current.

The approval function must verify at least:

```text
EXACT_REQUIREMENT_DISPOSITION
EXACT_BOUNDED_SCOPE
EXACT_SPEND_OR_ENGAGEMENT_CLASS
EXACT_CAP_AND_CURRENCY
EXACT_PERIOD_OR_EXPIRY
EXACT_STOP_CONDITIONS
EXACT_PAYEE_VENDOR_OR_PERSONNEL_REFERENCES_WHERE_KNOWN
EXACT_PRICING_OR_COMPENSATION_BASIS
EXACT_A7_CONFLICT_AND_ELIGIBILITY_REFERENCES_WHERE_APPLICABLE
EXACT_INDEPENDENCE_REFERENCES_WHERE_APPLICABLE
```

The approver may not broaden the scientific or resource requirement beyond the exact Q2 evidence merely because funds are available.

```text
APPROVER_MAY_ADD_UNDECLARED_SCOPE=NO
APPROVER_MAY_LOWER_SCIENTIFIC_REQUIREMENT_TO_FIT_BUDGET=NO
APPROVER_MAY_OVERRIDE_A7_INELIGIBILITY=NO
APPROVER_MAY_OVERRIDE_A13_DENY=NO
```

## 5. No self-approval of personal financial benefit

A person who is the direct proposed payee or direct beneficiary of an A14 payment must not be the sole authorization approver for that payment.

```text
DIRECT_PAYEE_MAY_SOLE_APPROVE_OWN_PAYMENT=NO
DIRECT_BENEFICIARY_MAY_SOLE_APPROVE_OWN_COMPENSATION=NO
CONTRACTOR_MAY_SOLE_APPROVE_OWN_CONTRACT=NO
REVIEWER_MAY_SOLE_APPROVE_OWN_REVIEW_FEE=NO
AUTHOR_MAY_SOLE_APPROVE_OWN_AUTHORING_FEE=NO
```

This applies even if the amount is small or the work is scientifically valuable.

## 6. Vendor and related-party conflicts

Future authorization must record conflict disposition when an approval, contracting, payment, reconciliation, or auditing actor has a material relationship to the proposed vendor/payee.

Material relationships include at least:

```text
DIRECT_FINANCIAL_INTEREST
BENEFICIAL_OWNERSHIP_OR_CONTROL
IMMEDIATE_PERSONAL_FINANCIAL_BENEFIT
CURRENT_EMPLOYMENT_OR_CONTRACTING_RELATIONSHIP
MATERIAL_FAMILY_OR_CLOSE_BUSINESS_RELATIONSHIP_WHERE_RELEVANT
OTHER_MATERIAL_RELATIONSHIP_THAT_COULD_AFFECT_IMPARTIALITY
```

Future conflict dispositions are:

```text
NO_MATERIAL_CONFLICT_IDENTIFIED
DISCLOSED_AND_REVIEWED_NO_DISQUALIFYING_CONFLICT
MATERIAL_CONFLICT_REQUIRING_RECUSAL
UNKNOWN_OR_UNRESOLVED
```

Rules:

```text
UNKNOWN_OR_UNRESOLVED_CONFLICT=BLOCKED
MATERIAL_CONFLICT_REQUIRING_RECUSAL_MAY_APPROVE=NO
MATERIAL_CONFLICT_REQUIRING_RECUSAL_MAY_RECONCILE=NO
MATERIAL_CONFLICT_REQUIRING_RECUSAL_MAY_AUDIT=NO
```

Q3 does not define a universal prohibition on every prior professional relationship; it requires evidence-bound disposition and recusal when material.

## 7. Founder and governance authority

Founder or repository governance authority may hold a financial approval role if separately assigned and conflict-cleared, but title alone is insufficient.

```text
FOUNDER_STATUS_ALONE_EQUALS_A14_APPROVAL_AUTHORITY=NO
FOUNDER_STATUS_ALONE_CLEARS_PAYEE_CONFLICT=NO
FOUNDER_MAY_SOLE_APPROVE_OWN_COMPENSATION=NO
FOUNDER_MAY_OVERRIDE_REQUIRED_RECUSAL=NO
```

The founder may authorize governance architecture or appoint bounded approval authorities through a separately canonical process, but scientific qualification, conflict, Gold, access, and payment controls remain independent.

## 8. Commitment / contract execution

A future commitment or contract may be executed only after a matching valid authorization exists.

```text
COMMITMENT_BEFORE_AUTHORIZATION=PROHIBITED
CONTRACT_EXECUTION_BEFORE_AUTHORIZATION=PROHIBITED
PURCHASE_ORDER_BEFORE_AUTHORIZATION=PROHIBITED
SERVICE_ACTIVATION_BEFORE_AUTHORIZATION=PROHIBITED
```

The commitment executor must verify that the proposed terms are within the authorization.

```text
COMMITMENT_SCOPE_MISMATCH=BLOCKED
COMMITMENT_CAP_MISMATCH=BLOCKED
COMMITMENT_PERIOD_MISMATCH=BLOCKED
MATERIAL_VENDOR_OR_PAYEE_SUBSTITUTION=BLOCKED_PENDING_REBINDING
MATERIAL_TERMS_CHANGE=BLOCKED_PENDING_NEW_OR_AMENDED_AUTHORIZATION
```

## 9. Payment execution

Payment execution is an implementation function, not approval authority.

A future payment executor must verify:

```text
VALID_CURRENT_A14_AUTHORIZATION
VALID_MATCHING_COMMITMENT_OR_INVOICE_EVIDENCE_AS_APPLICABLE
PAYEE_OR_VENDOR_MATCH
AMOUNT_AND_CURRENCY_MATCH
CAP_REMAINING_SUFFICIENT
PERIOD_NOT_EXPIRED
STOP_CONDITIONS_NOT_TRIGGERED
```

Payment executor rules:

```text
PAYMENT_EXECUTOR_MAY_CREATE_NEW_SCOPE=NO
PAYMENT_EXECUTOR_MAY_RAISE_CAP=NO
PAYMENT_EXECUTOR_MAY_CHANGE_PAYEE=NO
PAYMENT_EXECUTOR_MAY_IGNORE_EXPIRED_AUTHORIZATION=NO
PAYMENT_EXECUTOR_MAY_TREAT_INVOICE_AS_AUTHORIZATION=NO
```

## 10. Approval and payment separation

For any material nonzero external payment or commitment, Q3 freezes a default separation rule:

```text
AUTHORIZATION_APPROVER_AND_PAYMENT_EXECUTOR_SHOULD_BE_DISTINCT_CONTROL_FUNCTIONS=YES
```

A future implementation may determine whether one individual can hold both functions for a narrowly scoped low-risk case only if an explicit policy and compensating-control record is separately approved. Q3 does not grant such an exception.

```text
CURRENT_APPROVER_PAYMENT_EXECUTOR_COLOCATION_EXCEPTION=NONE
```

Therefore no future system may assume that one-person approval/payment is acceptable merely because the repository is founder-led or small.

## 11. Independent reconciliation

After any future payment, reconciliation must verify the transaction against the exact authorization and supporting records.

The reconciliation record should bind at least:

```text
reconciliation_record_id
payment_record_id
a14_authorization_id
commitment_or_invoice_identity
payee_or_vendor_reference
amount
currency
transaction_date_or_period
authorization_cap_before
authorization_cap_after
scope_match_disposition
period_match_disposition
conflict_or_independence_reference
reconciler_reference
record_canonical_sha256
```

Rules:

```text
DIRECT_PAYEE_MAY_RECONCILE_OWN_PAYMENT=NO
PAYMENT_EXECUTOR_MAY_BE_SOLE_INDEPENDENT_RECONCILER_OF_OWN_PAYMENT=NO
AUTHORIZATION_APPROVER_MAY_SILENTLY_REWRITE_RECONCILIATION=NO
```

If the same organization cannot provide a distinct reconciler for a material transaction, the transaction remains blocked until a separately approved compensating-control mechanism exists.

## 12. Financial governance audit

A financial governance auditor may inspect the authorization, commitment, payment, reconciliation, and conflict records but may not silently rewrite them.

```text
AUDITOR_MAY_REWRITE_ORIGINAL_PAYMENT_RECORD_IN_PLACE=NO
AUDITOR_MAY_REWRITE_ORIGINAL_AUTHORIZATION_IN_PLACE=NO
AUDITOR_MAY_CREATE_FINDING_OR_CORRECTION_RECORD=YES
AUDITOR_MAY_REQUIRE_REAUTHORIZATION_OR_REMEDIATION=YES
```

A material audit finding may force A14 back to blocked or stale state.

## 13. Error correction and overpayment

Errors are corrected additively and transparently.

```text
SILENT_PAYMENT_RECORD_CORRECTION=PROHIBITED
SILENT_AUTHORIZATION_RECORD_CORRECTION=PROHIBITED
RETROACTIVE_SCOPE_EXPANSION_TO_MAKE_PAYMENT_LOOK_AUTHORIZED=PROHIBITED
RETROACTIVE_CAP_INCREASE_TO_CURE_OVERRUN=PROHIBITED
```

If a payment was made outside valid authority, Q3 does not define it as authorized after the fact. The event must remain recorded as an exception/failure and any remediation must be separately governed.

## 14. Separation from scientific review compensation outcomes

Even when a reviewer, author, adjudicator, or statistician is paid, financial approvers may not control the scientific disposition.

```text
PAYMENT_APPROVER_MAY_REQUIRE_PREFERRED_SCIENTIFIC_RESULT=NO
PAYMENT_EXECUTOR_MAY_WITHHOLD_VALID_PAYMENT_TO_FORCE_PREFERRED_RESULT=NO
RECONCILER_MAY_CHANGE_SCIENTIFIC_REVIEW_DISPOSITION=NO
```

Compensation remains candidate-neutral and outcome-independent as frozen by Q1.

## 15. Personnel role conflicts

When a proposed payee is also a governed scientific actor, both A7 and A14 must be satisfied independently.

```text
A14_APPROVAL_MAY_OVERRIDE_A7_CONFLICT=NO
A14_APPROVAL_MAY_OVERRIDE_GOLD_EXPOSURE_BLOCK=NO
A14_APPROVAL_MAY_OVERRIDE_QUALIFICATION_BLOCK=NO
A14_PAYMENT_MAY_CREATE_SCIENTIFIC_ROLE_ASSIGNMENT=NO
```

The payment relationship itself may create or modify a conflict record that A7 must evaluate where material.

## 16. Storage / service-provider conflicts and access

If a paid service relates to protected selection content:

```text
A14_VENDOR_APPROVAL_EQUALS_A13_ACCESS_APPROVAL=NO
A14_PAYMENT_EQUALS_VENDOR_PAYLOAD_ACCESS=NO
A14_CONTRACT_EQUALS_DATA_TRANSFER_AUTHORITY=NO
```

A13 remains the authority for storage/access/firewall requirements.

## 17. Authorization approval record

A future approval decision must be separately identity-bound from the A14 authorization payload itself.

Minimum approval-decision record architecture:

```text
a14_approval_decision_id
a14_authorization_id
a14_authorization_sha256
requirement_manifest_id
requirement_manifest_sha256
approval_scope
approval_disposition
approver_governance_reference
approver_authority_scope_reference
payee_vendor_conflict_disposition_reference
independence_or_separation_validation_reference
approval_policy_id
approval_policy_version
timestamp
record_canonical_sha256
```

Future dispositions:

```text
APPROVED
BLOCKED_CONFLICT
BLOCKED_SCOPE_OR_CAP_MISMATCH
BLOCKED_STALE_OR_EXPIRED_INPUT
BLOCKED_INCOMPLETE_EVIDENCE
REJECTED
```

Caller-owned free-text `approved=true` is not authoritative.

## 18. Payment execution record

A future payment record should bind at least:

```text
payment_record_id
a14_authorization_id
a14_approval_decision_id
commitment_or_invoice_identity
payee_or_vendor_reference
amount
currency
execution_actor_reference
execution_timestamp
remaining_cap_after_payment
payment_instrument_opaque_reference_if_needed
record_canonical_sha256
```

Raw payment credentials remain prohibited in canonical repository records.

## 19. No arbitrary universal headcount

Q3 freezes separation by function rather than a fixed universal number of people.

```text
ONE_FIXED_FINANCIAL_APPROVER_COUNT_FOR_ALL_COMMITMENTS=PROHIBITED
ONE_FIXED_RECONCILER_COUNT_FOR_ALL_TRANSACTIONS=PROHIBITED
```

However, material conflict and self-benefit rules may force additional distinct actors in a specific transaction.

## 20. Candidate neutrality and result firewall

Financial governance must remain candidate-neutral.

```text
PREFERRED_CANDIDATE_MAY_TRIGGER_APPROVER_CHANGE=NO
PREFERRED_CANDIDATE_MAY_TRIGGER_PAYEE_CHANGE_TO_AFFECT_OUTCOME=NO
POST_RESULT_PAYMENT_CAP_EXPANSION=PROHIBITED
CANDIDATE_SPECIFIC_REVIEWER_BONUS=PROHIBITED
```

## 21. Future A14 operational PASS implications

Q3 does not make A14 PASS.

```text
A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_AUTHORIZED_PASS=NO
A14_NOT_REQUIRED_PASS=NO
A14_OPERATIONAL_PASS=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

A future `A14_AUTHORIZED_PASS` requires Q1 + Q2 + Q3-compliant exact records and all other applicable upstream gates.

## 22. Authority boundary

```text
A14_REQUIREMENT_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A14_SPEND_EXECUTION_AUTHORITY=NONE
A14_PAYMENT_EXECUTION_AUTHORITY=NONE
A14_CONTRACT_EXECUTION_AUTHORITY=NONE
A14_REIMBURSEMENT_AUTHORITY=NONE
A14_PAID_ENGAGEMENT_AUTHORITY=NONE
A14_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
A14_VENDOR_PROVISIONING_AUTHORITY=NONE

PAYMENT_INSTRUMENT_ACCESS_AUTHORITY=NONE
PAYEE_VENDOR_SELECTION_AUTHORITY=NONE
A14_APPROVER_ASSIGNMENT_AUTHORITY=NONE
A14_PAYMENT_EXECUTOR_ASSIGNMENT_AUTHORITY=NONE
A14_RECONCILER_ASSIGNMENT_AUTHORITY=NONE

A7_BOOTSTRAP_EXECUTION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE
A13_RESULT_ACCESS_AUTHORITY=NONE
A15_CONSTRUCTION_ACTIVATION_AUTHORITY=NONE

MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
```

## 23. Current disposition after Q3

```text
A14_APPROVAL_AUTHORITY_ARCHITECTURE=FROZEN
A14_FINANCIAL_SEPARATION_OF_DUTIES=FROZEN
A14_PAYEE_VENDOR_CONFLICT_RULES=FROZEN
A14_PAYMENT_RECONCILIATION_ARCHITECTURE=FROZEN

A14_GATE_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A14_OPERATIONAL_PASS=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

Q3 is clarification only. Do not interpret this document as authorization to spend, contract, pay, reimburse, engage, provision, access, construct, execute, merge, mark PR #34 Ready, or transition to PLAN.
