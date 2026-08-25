# Session 14 Q1 — A14 Spend and Engagement Authorization Architecture

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 14 Q1 only. It freezes the architecture for A14 (`ANY_REQUIRED_SPEND_OR_ENGAGEMENT_AUTHORITY`) without authorizing any spend, payment, procurement, reimbursement, contract, reviewer/author engagement, storage provisioning, provider/API use, model or benchmark execution, Private Gold access, personnel assignment, case construction, or transition to PLAN.

## 1. Frozen decision

```text
SESSION14_Q1_POLICY=PRECOMMITMENT_FAIL_CLOSED_SPEND_AND_ENGAGEMENT_AUTHORIZATION_WITH_EXACT_SCOPE_CAP_PERIOD_APPROVAL_AND_NO_RETROACTIVE_RATIFICATION

A14_SPEND_ENGAGEMENT_AUTHORIZATION_ARCHITECTURE=FROZEN
A14_REQUIREMENT_DISPOSITION_ARCHITECTURE=FROZEN
A14_AUTHORIZATION_RECORD_SCHEMA=FROZEN_STRUCTURALLY

A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_OPERATIONAL_PASS=NO
A14_GATE_STATUS=BLOCKED_PENDING_UPSTREAM_REQUIREMENTS_AND_EXACT_CANONICAL_DISPOSITION

CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE

CLARIFICATION_SESSION_14=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_14_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q1 does not weaken Session 6 Q5. The current authorized spend remains exactly USD 0 until a future separate canonical authorization explicitly changes that boundary.

## 2. Canonical relationship to the existing zero-spend boundary

The existing Session 6 policy remains authoritative:

```text
TOURNAMENT_COMPUTE_SPEND_POLICY=ZERO_SPEND_PREEXECUTION_SEPARATE_ACTIVATION_REQUIRED
CURRENT_AUTHORIZED_SPEND_USD=0
UNDECLARED_SPEND=PROHIBITED
POST_RESULT_BUDGET_EXPANSION=PROHIBITED
CANDIDATE_SPECIFIC_SPEND_EXCEPTION=PROHIBITED
```

Q1 extends the preconstruction governance architecture for A14. It does not activate or amend the compute/execution budget.

```text
A14_AUTHORIZATION_EQUALS_EXECUTION_BUDGET_ACTIVATION=NO
A14_AUTHORIZATION_EQUALS_MODEL_EXECUTION_AUTHORITY=NO
A14_AUTHORIZATION_EQUALS_PROVIDER_GENERATION_AUTHORITY=NO
```

## 3. A14 is a conditional gate, but silence is not a PASS

A14 exists because construction may require money and/or a new engagement commitment after the exact statistical allocation, review protocol, and personnel roster are known.

The only future terminal PASS modes are:

```text
A14_NOT_REQUIRED_PASS
A14_AUTHORIZED_PASS
```

`A14_NOT_REQUIRED_PASS` means exact canonical evidence proves that the bounded construction scope requires neither:

1. a new financial commitment; nor
2. a new personnel/service engagement commitment beyond already-authorized active roles/resources.

It may not be inferred from lack of a purchase order, lack of an invoice, or use of a nominally free service.

```text
A14_NOT_REQUIRED_BY_SILENCE=PROHIBITED
A14_NOT_REQUIRED_BY_ASSUMPTION=PROHIBITED
A14_NOT_REQUIRED_BY_FOUNDER_CONVENIENCE=PROHIBITED
```

`A14_AUTHORIZED_PASS` means every required spend or engagement commitment has been predeclared and bound to an exact canonical authorization record satisfying this contract.

All other states are fail-closed:

```text
A14_REQUIRED_BUT_UNAUTHORIZED=BLOCKED
A14_REQUIREMENT_UNKNOWN=BLOCKED
A14_AUTHORIZATION_EXPIRED=BLOCKED
A14_AUTHORIZATION_SCOPE_MISMATCH=BLOCKED
A14_AUTHORIZATION_CAP_EXCEEDED_OR_WOULD_BE_EXCEEDED=BLOCKED
A14_MATERIAL_TERMS_CHANGED=BLOCKED_PENDING_NEW_AUTHORIZATION
```

## 4. Upstream prerequisites for final requirement determination

The frozen preconstruction DAG already requires:

```text
D34 -> A14
A8_AUTHORING_REVIEW_PROTOCOL -> A14
A7_FINAL_PERSONNEL_ROSTER_AND_GOLD_NONEXPOSURE -> A14
```

Therefore the final A14 requirement cannot be declared while those inputs remain unresolved.

```text
A14_FINAL_REQUIREMENT_DETERMINATION_BEFORE_D34_FINAL=NO
A14_FINAL_REQUIREMENT_DETERMINATION_BEFORE_A8_FINAL=NO
A14_FINAL_REQUIREMENT_DETERMINATION_BEFORE_A7_FINAL=NO
```

The reason is practical and scientific: exact case counts, review workload, role allocations, and the roster determine whether additional authors, reviewers, adjudicators, storage, services, or other paid resources are actually required.

Q1 adds no new execution authority and does not change the frozen DAG ordering.

## 5. Separate financial commitment, payment, engagement, and technical authority

Future implementation must not collapse distinct authorities into one boolean.

```text
FINANCIAL_COMMITMENT_AUTHORITY != PAYMENT_EXECUTION_AUTHORITY
PAYMENT_EXECUTION_AUTHORITY != SCIENTIFIC_ROLE_ELIGIBILITY
SCIENTIFIC_ROLE_ELIGIBILITY != PERSONNEL_ASSIGNMENT_AUTHORITY
PERSONNEL_ASSIGNMENT_AUTHORITY != A13_ACCESS_AUTHORITY
SPEND_AUTHORIZATION != RESOURCE_PROVISIONING_AUTHORITY
RESOURCE_PROVISIONING_AUTHORITY != PAYLOAD_ACCESS_AUTHORITY
```

A person or organization may be scientifically eligible under A7 without any authority to pay them. Conversely, a payment operator may execute an already-authorized payment without gaining scientific or data-access authority.

## 6. Spend classes governed by A14

If required for the bounded preconstruction/construction scope, A14 must cover at least these spend classes explicitly rather than through a generic budget pool:

```text
PERSONNEL_COMPENSATION_OR_CONTRACTOR_FEES
INDEPENDENT_REVIEW_OR_ADJUDICATION_FEES
TRANSLATION_OR_LANGUAGE_SERVICE_FEES
DATA_OR_CONTENT_RIGHTS_FEES
PROTECTED_STORAGE_OR_SECURITY_SERVICE_FEES
NON_EXECUTING_INFRASTRUCTURE_OR_TOOLING_FEES
OTHER_EXACTLY_NAMED_PRECONSTRUCTION_COST
```

A class that is not named in the authorization receives no spend authority.

```text
GENERIC_MISCELLANEOUS_UNBOUNDED_SPEND_BUCKET=PROHIBITED
UNDECLARED_COST_CATEGORY=PROHIBITED
```

Model execution, benchmark execution, paid provider inference, training, weight retrieval, or device execution remain outside Q1 and require their own separately authorized gates even if money were available.

## 7. Engagement classes governed by A14

A14 also governs creation of a new commitment for a person or external service to perform bounded work for Spec 005.

Examples include:

```text
NEW_EXTERNAL_CASE_AUTHOR_ENGAGEMENT
NEW_EXTERNAL_CLINICAL_REVIEWER_ENGAGEMENT
NEW_EXTERNAL_BILINGUAL_REVIEWER_ENGAGEMENT
NEW_EXTERNAL_ADJUDICATOR_ENGAGEMENT
NEW_EXTERNAL_STATISTICAL_OR_METHODS_REVIEW_ENGAGEMENT
NEW_EXTERNAL_CONTENT_RIGHTS_OR_LANGUAGE_SERVICE_ENGAGEMENT
```

An engagement may be paid or unpaid. A zero-dollar engagement is not automatically authorized merely because it produces no invoice.

```text
ZERO_DOLLAR_EXTERNAL_ENGAGEMENT_EQUALS_AUTOMATIC_AUTHORITY=NO
UNPAID_EXTERNAL_WORK_BYPASSES_A7=NO
UNPAID_EXTERNAL_WORK_BYPASSES_CONTRIBUTOR_RIGHTS=NO
```

Existing internal activity already authorized under another exact governance scope is not automatically a new A14 engagement, but that status must be demonstrable rather than assumed.

## 8. Required future authorization record

Any future `A14_AUTHORIZED_PASS` must bind a canonical record containing at least:

```text
a14_authorization_id
authorization_version
spec_id
purpose_and_bounded_scope
dependency_snapshot_ids
requirement_disposition
spend_categories[]
engagement_classes[]
exact_vendor_or_payee_opaque_references[]
exact_personnel_or_role_references_where_applicable
pricing_or_compensation_basis
currency
max_committed_amount
max_payable_amount
recurring_or_one_time_classification
authorized_period_or_expiry
allowed_cost_components
prohibited_cost_components
stop_conditions
approval_authority_references[]
required_independence_or_conflict_dispositions[]
related_a7_assignment_references_where_applicable
related_resource_or_service_identity_references[]
record_canonical_sha256
```

The record must be fixed before the commitment it authorizes.

```text
AUTHORIZATION_RECORD_AFTER_COMMITMENT=PROHIBITED
AUTHORIZATION_RECORD_AFTER_PAYMENT=PROHIBITED
RETROACTIVE_RATIFICATION_OF_UNAUTHORIZED_SPEND=PROHIBITED
RETROACTIVE_RATIFICATION_OF_UNAUTHORIZED_ENGAGEMENT=PROHIBITED
```

## 9. Exact cap and period are mandatory for nonzero spend

Any future nonzero authorization must have a finite monetary ceiling and time/scope boundary.

```text
NONZERO_SPEND_REQUIRES_EXACT_MAXIMUM=YES
NONZERO_SPEND_REQUIRES_EXPLICIT_CURRENCY=YES
NONZERO_SPEND_REQUIRES_PERIOD_OR_EXPIRY=YES
NONZERO_SPEND_REQUIRES_STOP_CONDITIONS=YES
UNBOUNDED_VARIABLE_USAGE_SPEND=PROHIBITED
UNBOUNDED_RECURRING_COMMITMENT=PROHIBITED
```

Q1 chooses no numeric cap.

```text
FUTURE_A14_MAX_USD=NOT_YET_FROZEN
FUTURE_A14_RECURRING_CAP_USD=NOT_YET_FROZEN
FUTURE_A14_DURATION=NOT_YET_FROZEN
```

Until a separate authorization freezes an exact nonzero value, the active spend boundary remains:

```text
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. All-in cost treatment

A future authorization must define whether taxes, platform fees, payment fees, currency-conversion costs, and other unavoidable charges are inside the cap. They may not silently cause an overrun.

```text
KNOWN_OR_REASONABLY_ESTIMABLE_MANDATORY_FEES_MUST_BE_ACCOUNTED_FOR=YES
UNKNOWN_MANDATORY_COST_THAT_COULD_BREACH_CAP=BLOCKED_PENDING_REAUTHORIZATION
```

A quote or estimate is evidence for planning only; it is not authority to incur the quoted cost.

```text
QUOTE_EQUALS_SPEND_AUTHORITY=NO
INVOICE_EQUALS_SPEND_AUTHORITY=NO
AVAILABLE_FUNDS_EQUALS_SPEND_AUTHORITY=NO
```

## 11. Recurring services and automatic renewal

For any future subscription or recurring engagement:

```text
AUTOMATIC_RENEWAL_BY_DEFAULT=PROHIBITED
RECURRING_PERIOD_MUST_BE_PREDECLARED=YES
RECURRING_CAP_MUST_BE_PREDECLARED=YES
MATERIAL_RENEWAL_REQUIRES_FRESH_AUTHORIZATION=YES
```

Q1 does not select or subscribe to any service.

## 12. Overrun and scope-change behavior

Authorization is a hard ceiling, not a target.

```text
SPEND_CAP_OVERRUN=PROHIBITED
COMMITMENT_THAT_WOULD_EXCEED_CAP=PROHIBITED
SCOPE_EXPANSION_WITHOUT_NEW_AUTHORIZATION=PROHIBITED
PAYEE_OR_VENDOR_SUBSTITUTION_WITHOUT_REBINDING=PROHIBITED_IF_MATERIAL
ENGAGEMENT_ROLE_EXPANSION_WITHOUT_REAUTHORIZATION=PROHIBITED
```

Unused budget from one category may not silently fund another category.

```text
CROSS_CATEGORY_BUDGET_TRANSFER_BY_DEFAULT=PROHIBITED
UNUSED_BUDGET_CREATES_FUTURE_AUTHORITY=NO
```

## 13. No outcome-contingent scientific compensation

Compensation for scientific, clinical, bilingual, contamination, or adjudication work must not depend on producing a preferred candidate, threshold, finding, or PASS result.

```text
CANDIDATE_OUTCOME_CONTINGENT_COMPENSATION=PROHIBITED
PASS_RESULT_CONTINGENT_REVIEWER_COMPENSATION=PROHIBITED
THRESHOLD_RELAXATION_CONTINGENT_COMPENSATION=PROHIBITED
DISAGREEMENT_RESOLUTION_PAYMENT_FOR_PREFERRED_OUTCOME=PROHIBITED
```

Compensation may be based on predeclared time, workload, deliverables, or another candidate-neutral basis if separately authorized.

## 14. Candidate neutrality and post-result expansion

The Session 6 rules remain intact:

```text
POST_RESULT_BUDGET_EXPANSION=PROHIBITED
CANDIDATE_SPECIFIC_SPEND_EXCEPTION=PROHIBITED
```

Q1 additionally freezes:

```text
PREFERRED_CANDIDATE_MAY_TRIGGER_EXTRA_REVIEW_BUDGET=NO
WEAK_CANDIDATE_MAY_RECEIVE_EXTRA_PAID_RESCUE_WORK=NO
CANDIDATE_RESULT_MAY_SELECT_PAYEE_OR_REVIEWER_TO_CHANGE_OUTCOME=NO
```

Any permitted future contingency must be candidate-neutral and predeclared before relevant results are visible.

## 15. Free tiers, credits, and donated resources

A zero-dollar price does not create technical or legal authority.

```text
FREE_TIER_EQUALS_EXECUTION_AUTHORITY=NO
FREE_TRIAL_EQUALS_EXECUTION_AUTHORITY=NO
PROMOTIONAL_CREDIT_EQUALS_EXECUTION_AUTHORITY=NO
DONATED_RESOURCE_EQUALS_EXECUTION_AUTHORITY=NO
```

If a free tier, trial, promotional credit, or donated resource creates a new account, terms acceptance, external dependency, resource provisioning, data transfer, access route, or material candidate-specific resource advantage, the corresponding nonfinancial authorization remains required and the resource must be declared where scientifically relevant.

```text
ZERO_CASH_COST_BYPASSES_GATED_TERMS=NO
ZERO_CASH_COST_BYPASSES_RESOURCE_PROVISIONING_AUTHORITY=NO
ZERO_CASH_COST_BYPASSES_DATA_ACCESS_GOVERNANCE=NO
```

## 16. Reimbursement and personal payment

A person may not bypass A14 by paying personally and requesting reimbursement later.

```text
PERSONAL_PAYMENT_TO_BYPASS_A14=PROHIBITED
REIMBURSEMENT_OF_UNAUTHORIZED_SPEND=PROHIBITED
REIMBURSEMENT_REQUEST_CREATES_RETROACTIVE_AUTHORITY=NO
```

Q1 does not inspect, request, or authorize any payment credential.

## 17. Credentials and payment instruments

A14 governance records must never contain raw payment credentials, banking credentials, API keys, card data, or other secrets.

```text
RAW_PAYMENT_CREDENTIAL_IN_CANONICAL_REPO=PROHIBITED
RAW_PROVIDER_SECRET_IN_A14_RECORD=PROHIBITED
PAYMENT_INSTRUMENT_REFERENCE_MAY_BE_OPAQUE_IF_NEEDED=YES
```

This clarification grants no authority to access payment instruments or credentials.

## 18. Relationship to A7 personnel governance

If spend or engagement involves a person performing a governed scientific role:

```text
A7_ROLE_ELIGIBILITY_REQUIRED_WHERE_APPLICABLE=YES
A7_CURRENT_ASSIGNMENT_REQUIRED_BEFORE_ROLE_WORK_WHERE_APPLICABLE=YES
A14_PAYMENT_AUTHORIZATION_MAY_OVERRIDE_A7_INELIGIBILITY=NO
A14_ENGAGEMENT_AUTHORIZATION_MAY_OVERRIDE_GOLD_EXPOSURE_BLOCK=NO
A14_ENGAGEMENT_AUTHORIZATION_MAY_OVERRIDE_CONFLICT_BLOCK=NO
```

A14 decides whether the commitment may be made; A7 decides whether the person is eligible and assigned for the scientific role.

## 19. Relationship to A13 storage/access governance

If a paid or external service is used for protected selection content, A14 financial authority is insufficient by itself.

```text
A14_PAID_STORAGE_AUTHORIZATION_EQUALS_A13_PASS=NO
A14_VENDOR_PAYMENT_EQUALS_PAYLOAD_ACCESS_AUTHORITY=NO
A14_VENDOR_CONTRACT_EQUALS_RESULT_ACCESS_AUTHORITY=NO
```

A13 must independently authorize the storage/access/firewall architecture before protected content is placed into the service.

## 20. Relationship to A15 construction activation

A14 is a preconstruction gate only.

```text
A14_NOT_REQUIRED_PASS_EQUALS_A15_ACTIVATION=NO
A14_AUTHORIZED_PASS_EQUALS_A15_ACTIVATION=NO
A14_PASS_EQUALS_CASE_CONSTRUCTION_AUTHORITY=NO
```

A15 remains a separate explicit activation after A1–A14 have independently reached their required PASS states and the preactivation recheck succeeds.

## 21. Future A14 PASS evidence

A future A14 PASS record must be bound to exact current evidence rather than prose assertion alone.

For `A14_NOT_REQUIRED_PASS`, the minimum evidence architecture is:

```text
exact_d34_identity
exact_a8_protocol_identity
exact_a7_roster_identity
exact_bounded_construction_scope
resource_and_workload_requirements_manifest
no_new_spend_attestation
no_new_engagement_attestation
independent_or_governance_review_record_as_required
canonical_pass_record_sha256
```

For `A14_AUTHORIZED_PASS`, minimum evidence additionally includes:

```text
exact_a14_authorization_record
exact_cap_and_currency
exact_authorized_period_or_expiry
exact_cost_and_engagement_classes
exact_payee_vendor_or_personnel_references
exact_stop_conditions
exact_approval_authority_references
current_conflict_or_independence_dispositions_where_applicable
canonical_pass_record_sha256
```

```text
A14_PASS_FROM_PR_BODY_TEXT_ONLY=NO
A14_PASS_FROM_FOUNDER_INTENT_ONLY=NO
A14_PASS_FROM_AVAILABLE_CASH_ONLY=NO
A14_PASS_FROM_VENDOR_QUOTE_ONLY=NO
```

## 22. Current exact disposition after Q1

Q1 freezes architecture only. It does not determine whether A14 will eventually be not-required or require a bounded authorization.

```text
A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_NOT_REQUIRED_PASS=NO
A14_AUTHORIZED_PASS=NO
A14_OPERATIONAL_PASS=NO

CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE

A14_SPEND_EXECUTION_AUTHORITY=NONE
A14_PAYMENT_EXECUTION_AUTHORITY=NONE
A14_CONTRACT_EXECUTION_AUTHORITY=NONE
A14_REIMBURSEMENT_AUTHORITY=NONE
A14_VENDOR_PROVISIONING_AUTHORITY=NONE
```

No payment, contract, engagement, procurement, reimbursement, subscription, storage provisioning, or provider action was performed by Q1.

## 23. Authority boundary

```text
PLAN_AUTHORITY=NONE
A15_CONSTRUCTION_ACTIVATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
A7_PERSONNEL_ASSIGNMENT_AUTHORITY=NONE
A13_STORAGE_PROVISIONING_AUTHORITY=NONE
A13_PAYLOAD_ACCESS_AUTHORITY=NONE
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

## 24. Session 14 progress

Acceptance of Q1 advances only the bounded clarification session:

```text
CLARIFICATION_SESSION_14=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_14_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Session 14 Q1 does not authorize Q2 automatically and does not complete the overall CLARIFY lifecycle.