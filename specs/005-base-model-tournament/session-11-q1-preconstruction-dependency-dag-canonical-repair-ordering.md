# Session 11 Q1 — Preconstruction Dependency DAG and Canonical Repair Ordering

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 11 Q1 only. It freezes the dependency graph and ordering constraints for the Session 10 Q5 preconstruction gates A1–A14. It does not authorize or implement metrics-v2 corrective maintenance, threshold freeze, case construction, reviewer engagement, spend, payload access, model execution, Private Gold access, provider generation, contamination execution, or transition to PLAN.

## 1. Frozen decision

```text
SESSION11_Q1_POLICY=DEPENDENCY_ORDERED_PARALLEL_PRECONSTRUCTION_DAG_WITH_ATOMIC_STATISTICAL_ALLOCATION_NODE

PRECONSTRUCTION_DEPENDENCY_DAG=FROZEN
CANONICAL_REPAIR_ORDERING=FROZEN_STRUCTURALLY

LINEAR_A1_THROUGH_A14_EXECUTION_ORDER_REQUIRED=NO
PARALLEL_GOVERNANCE_WORK_ALLOWED=YES
CIRCULAR_DEPENDENCY_BY_POST_HOC_RETROFIT=PROHIBITED

A1_METRICS_V2_REPAIR_IS_SEPARATE_CORRECTIVE_MAINTENANCE=YES
PR34_MAY_IMPLEMENT_A1=NO

A3_AND_A4_FORM_ONE_ATOMIC_DESIGN_NODE=YES
A3_FINAL_FREEZE_WITHOUT_A4_FINAL_ALLOCATION=PROHIBITED
A4_FINAL_FREEZE_WITHOUT_A3_STATISTICAL_JUSTIFICATION=PROHIBITED

A15_REMAINS_SEPARATE_EXPLICIT_ACTIVATION_AFTER_A1_TO_A14_PASS=YES
```

## 2. Canonical starting state

Session 10 Q5 freezes fifteen gates:

```text
A1=METRICS_V2_CANONICAL_IMPLEMENTATION
A2=EXACT_SELECTION_THRESHOLD_OR_MARGIN_POLICY
A3=EXACT_PAIRED_STATISTICAL_DESIGN_AND_PAIR_COUNTS
A4=EXACT_COVERAGE_AND_ROLE_ALLOCATION
A5=CONTRIBUTOR_AND_CONTENT_RIGHTS_INSTRUMENT
A6=NON_PHI_AUTHORING_POLICY_AND_ATTESTATION
A7=PERSONNEL_ROSTER_AND_PRIVATE_GOLD_NONEXPOSURE_ATTESTATIONS
A8=AUTHORING_REVIEW_AND_DISAGREEMENT_PROTOCOL
A9=VERSIONED_PROVENANCE_CASE_TEMPLATE
A10=EXACT_SOURCE_ROUTE_AND_DERIVATION_RULES
A11=PREDECLARED_CONTAMINATION_ASSESSMENT_PLAN
A12=CASE_CHANGE_CONTROL_AND_INVALID_CASE_POLICY
A13=SELECTION_CONTENT_STORAGE_ACCESS_AND_CANDIDATE_FEEDBACK_FIREWALL
A14=ANY_REQUIRED_SPEND_OR_ENGAGEMENT_AUTHORITY
A15=SEPARATE_EXPLICIT_CONSTRUCTION_ACTIVATION
```

Current Q5 result remains:

```text
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

Q1 does not change any gate disposition to PASS.

## 3. Dependency-node model

The preconstruction work is frozen as a directed acyclic graph rather than a flat checklist.

The main nodes are:

```text
R1=A1_METRICS_V2_CORRECTIVE_MAINTENANCE
G1=A5_RIGHTS_INSTRUMENT
G2=A6_NON_PHI_POLICY
G3=A8_AUTHORING_REVIEW_PROTOCOL
G4=A12_CHANGE_CONTROL
S1=A10_EXACT_SOURCE_ROUTE
P1=A9_PROVENANCE_TEMPLATE
C1=A11_CONTAMINATION_PLAN
T1=A2_THRESHOLD_OR_MARGIN_POLICY
D34=ATOMIC_A3_STATISTICAL_DESIGN_PLUS_A4_COVERAGE_ALLOCATION
H1=A7_FINAL_PERSONNEL_ROSTER_AND_GOLD_NONEXPOSURE
I1=A13_STORAGE_ACCESS_AND_FEEDBACK_FIREWALL
F1=A14_SPEND_OR_ENGAGEMENT_AUTHORITY_IF_REQUIRED
J1=A1_TO_A14_PREACTIVATION_RECHECK
ACT=A15_EXPLICIT_CONSTRUCTION_ACTIVATION
```

## 4. Mandatory dependency edges

The following directed edges are frozen:

```text
R1 -> T1

G1 -> S1
G2 -> S1

G1 -> P1
G2 -> P1
G3 -> P1
G4 -> P1
S1 -> P1

S1 -> C1
P1 -> C1

T1 -> D34

G1 -> H1
G2 -> H1
G3 -> H1
D34 -> H1

G2 -> I1
G3 -> I1
G4 -> I1
P1 -> I1
H1 -> I1

D34 -> F1
G3 -> F1
H1 -> F1

R1 -> J1
T1 -> J1
D34 -> J1
G1 -> J1
G2 -> J1
G3 -> J1
G4 -> J1
S1 -> J1
P1 -> J1
C1 -> J1
H1 -> J1
I1 -> J1
F1 -> J1

J1 -> ACT
```

No edge grants execution authority. It only identifies prerequisite ordering.

## 5. Why A3 and A4 are one atomic node

Session 10 Q5 contains a genuine two-way scientific dependency:

- A3 needs exact total pair count, count per coverage anchor, and role-by-anchor counts.
- A4 says the exact anchor/role allocation must be driven by the statistical and intended-use design rather than by author convenience.

Freezing A3 first would risk inventing N without a valid allocation. Freezing A4 first would risk assigning counts without statistical justification.

Therefore Q1 resolves the apparent cycle by treating them as one atomic design identity:

```text
D34=ATOMIC_STATISTICAL_AND_ALLOCATION_DESIGN

D34_INPUTS_INCLUDE=
SESSION9_Q1_INTENDED_USE_POPULATION_MATRIX,
SESSION9_Q2_STRATIFICATION_ARCHITECTURE,
SESSION9_Q3_STATISTICAL_ARCHITECTURE,
SESSION10_Q4_FIVE_COVERAGE_ANCHORS,
A2_EXACT_THRESHOLD_OR_MARGIN_POLICY

D34_OUTPUTS_INCLUDE=
EXACT_TOTAL_PAIR_COUNT,
EXACT_COUNT_PER_COVERAGE_ANCHOR,
EXACT_ROLE_BY_ANCHOR_COUNTS,
EXACT_REQUIRED_STATISTICAL_STRATA,
EXACT_CONFIDENCE_OR_ERROR_PARAMETERS,
EXACT_SAMPLE_SIZE_OR_POWER_DERIVATION,
EXACT_ALLOCATION_RATIONALE
```

Rules:

```text
AUTHORING_CAPACITY_MAY_DETERMINE_D34_N=NO
AVAILABLE_CASE_COUNT_MAY_DETERMINE_D34_N=NO
PREFERRED_CANDIDATE_RESULT_MAY_DETERMINE_D34_N=NO

D34_MUST_BE_PRE_RESULT=YES
D34_MUST_BE_CANDIDATE_NEUTRAL=YES
D34_MUST_BE_IDENTITY_BOUND=YES
```

## 6. A1 is the mandatory separate corrective-maintenance track

A1 changes an upstream canonical evaluation contract and its exact semantic identity. Existing policy already requires:

```text
A1_SEPARATE_EXPLICIT_AUTHORIZATION=REQUIRED
A1_SEPARATE_BRANCH=REQUIRED
A1_SEPARATE_PR=REQUIRED
A1_BASE=LIVE_CANONICAL_MAIN
A1_INDEPENDENT_EXACT_HEAD_REVIEW=REQUIRED
A1_EXACT_HEAD_QUALIFICATION=REQUIRED
A1_GUARDED_MERGE=REQUIRED
A1_RESULTING_MAIN_REVERIFICATION=REQUIRED
```

The repair must preserve historical V1 reproducibility while creating an explicit versioned V2 identity and compatible current-consumer binding.

```text
A1_IN_PLACE_V1_REINTERPRETATION=PROHIBITED
A1_HISTORICAL_V1_REWRITE=PROHIBITED
A1_UNRELATED_CONTRACT_CHANGES=PROHIBITED
```

PR #34 remains a Spec 005 clarification carrier and MUST NOT implement A1.

## 7. PR #34 reconciliation after a future A1 merge

If A1 is later separately authorized, reviewed, and merged while PR #34 remains open:

```text
CANONICAL_MAIN_ADVANCE_DOES_NOT_INVALIDATE_HISTORY=YES
FORCE_PUSH_PR34_AFTER_A1_MERGE=PROHIBITED
REBASE_PR34_AFTER_A1_MERGE=PROHIBITED
```

Required sequence:

```text
1. A1_MERGE_TO_CANONICAL_MAIN
2. REVERIFY_NEW_MAIN_SHA_TREE_AND_V2_IDENTITY
3. REVERIFY_PR34_BASE_AND_HEAD
4. ADD_NONDESTRUCTIVE_PR34_RECONCILIATION_COMMIT_IF_BINDINGS_OR_DOCS_REQUIRE_UPDATE
5. MERGE_CANONICAL_MAIN_INTO_PR34_ONLY_IF_NEEDED_FOR_CONFLICT_OR_EXACT_INTEGRATION; NO_REBASE
6. RECOMPUTE_PR34_EXACT_DELTA_AGAINST_NEW_BASE
7. FRESH_EXACT_HEAD_QUALIFICATION
8. FRESH_INDEPENDENT_REVIEW_WHEN_REQUIRED
```

A base-branch advance alone is not a PASS. PR #34 must be requalified against the new canonical base.

## 8. A2 ordering relative to A1

Scientific research and evidence appraisal for A2 may proceed read-only before A1 is implemented, but final canonical A2 identity must bind the repaired selection evidence role rather than an obsolete V1 ambiguity.

```text
A2_READ_ONLY_EVIDENCE_RESEARCH_MAY_PARALLEL_A1=YES
A2_FINAL_CANONICAL_FREEZE_BEFORE_A1_CANONICAL=NO
A2_FINAL_POLICY_ID_MUST_BIND_CURRENT_VERSIONED_METRIC_ROLE=YES
```

A2 is not classified by Q1 as corrective maintenance merely because it freezes a previously pending threshold. It is a scientific-policy freeze anticipated by the threshold-governance architecture.

However:

```text
IF_A2_REQUIRES_MUTATING_CLOSED_UPSTREAM_SCHEMA_OR_REDEFINING_EXISTING_HISTORICAL_SEMANTICS=
SEPARATE_CORRECTIVE_MAINTENANCE_REQUIRED
```

Q1 does not authorize that contingency.

## 9. Governance-foundation branch can proceed in parallel

These nodes have no dependency on metrics-v2 implementation and may be clarified in parallel as documentation/governance work:

```text
G1=A5_CONTRIBUTOR_AND_CONTENT_RIGHTS_INSTRUMENT
G2=A6_NON_PHI_AUTHORING_POLICY_AND_ATTESTATION
G3=A8_AUTHORING_REVIEW_AND_DISAGREEMENT_PROTOCOL
G4=A12_CASE_CHANGE_CONTROL_AND_INVALID_CASE_POLICY
```

They remain blocked until exact canonical artifacts exist, but their design does not need to wait for A1.

```text
A1_BLOCKS_G1_DESIGN=NO
A1_BLOCKS_G2_DESIGN=NO
A1_BLOCKS_G3_DESIGN=NO
A1_BLOCKS_G4_DESIGN=NO
```

This parallel branch is the preferred way to avoid unnecessary idle work without crossing into construction.

## 10. Exact source route comes after rights and privacy rules

A10 cannot be finalized before the rights and privacy framework is known.

```text
A5 -> A10
A6 -> A10
```

For an original commandMed-authored fictional/non-PHI route, A10 may eventually declare zero external content parents.

For any public-dev or derived route, A10 must bind exact source identities and prove the relevant rights/lineage before PASS.

```text
EXTERNAL_SOURCE_ROUTE_WITH_UNRESOLVED_RIGHTS=BLOCKED
EXTERNAL_SOURCE_ROUTE_WITH_UNRESOLVED_PRIVACY=BLOCKED
PRIVATE_GOLD_PARENT=PROHIBITED
PUBLIC_EXTERNAL_TEST_PARENT_FOR_SELECTION=PROHIBITED
```

## 11. Provenance template follows the policies it must encode

A9 must not be finalized before the policies that define its semantic fields.

Required inputs:

```text
A5_RIGHTS_POLICY
A6_PRIVACY_POLICY
A8_REVIEW_POLICY
A10_SOURCE_ROUTE
A12_CHANGE_CONTROL_POLICY
```

Therefore:

```text
A5,A6,A8,A10,A12 -> A9
```

The template must encode policy identities rather than retroactively attach labels to already-created content.

## 12. Contamination plan follows source and provenance design

The preconstruction contamination plan A11 does not require actual cases, but it does require knowing:

- source/derivation route;
- provenance fields and identity model;
- exact-match and semantic-overlap evidence schema;
- candidate/candidate-corpus binding plan.

Therefore:

```text
A10 -> A11
A9 -> A11
```

Actual contamination evidence remains a postconstruction Stage-B artifact and is not created by Q1.

```text
Q1_AUTHORIZES_CONTAMINATION_PAYLOAD_ACCESS=NO
Q1_AUTHORIZES_CONTAMINATION_EXECUTION=NO
```

## 13. Final personnel roster is late-bound, not an early bootstrap

Reviewer/author eligibility rules may be designed early through A8, but the final A7 roster should be bound only after:

```text
A5_RIGHTS_AND_CONTRIBUTOR_TERMS
A6_PRIVACY_ATTESTATION_REQUIREMENTS
A8_REVIEWER_ELIGIBILITY_AND_GOLD_FIREWALL_RULES
D34_EXPECTED_WORKLOAD_AND_REQUIRED_COUNTS
```

Thus:

```text
A5,A6,A8,D34 -> A7
```

This prevents selecting a roster first and then changing scientific N or review rules to fit available personnel.

Q1 does not name, contact, appoint, or evaluate any person.

## 14. Storage/access policy requires finalized roles and provenance

A13 exact PASS needs more than a generic storage statement. It must encode actual access roles and leakage controls.

Therefore:

```text
A6_PRIVACY_POLICY
A8_ROLE_AND_REVIEW_POLICY
A12_CHANGE_CONTROL
A9_PROVENANCE_TEMPLATE
A7_FINAL_ROSTER
    -> A13
```

The policy must preserve:

```text
PRIVATE_GOLD_CONTENT_FLOW_INTO_SELECTION_WORKSPACE=PROHIBITED
CANDIDATE_RESULTS_AVAILABLE_TO_AUTHORS_BEFORE_FREEZE=NO
CANDIDATE_RESULTS_AVAILABLE_TO_REVIEWERS_BEFORE_FREEZE=NO
```

Q1 does not create a workspace or grant access.

## 15. Spend/engagement authority is intentionally late

A14 cannot be meaningfully bounded until the exact workload and personnel model are known.

Therefore:

```text
D34_EXACT_COUNTS
A8_REVIEW_REQUIREMENTS
A7_FINAL_PERSONNEL_ROSTER
    -> A14
```

Rules:

```text
CURRENT_AUTHORIZED_SPEND_USD=0
A14_MAY_BE_INFERRED_FROM_ZERO_COST_ROUTE=NO
A14_MAY_BE_INFERRED_FROM_PR34_APPROVAL=NO
A14_MAY_BE_INFERRED_FROM_GENERIC_GO_AHEAD=NO
```

If no paid engagement is needed, A14 still requires an explicit disposition establishing the authorized zero-spend construction route. If paid engagement is required, a separate bounded spend authorization is required before commitment.

## 16. Recommended dependency waves

The DAG may be executed as the following dependency waves when each wave is separately authorized for its exact scope.

### Wave 0 — current CLARIFY architecture

```text
SESSION11_Q1_DAG_DESIGN_ONLY
NO_IMPLEMENTATION
```

### Wave 1A — separate upstream repair track

```text
R1=A1_METRICS_V2_CORRECTIVE_MAINTENANCE
```

This wave requires separate explicit authorization and a separate PR. Q1 does not authorize it.

### Wave 1B — parallel governance-foundation track

```text
G1=A5_RIGHTS_INSTRUMENT
G2=A6_NON_PHI_POLICY
G3=A8_REVIEW_PROTOCOL
G4=A12_CHANGE_CONTROL
```

These may be clarified in parallel as docs/governance work; no case content is created.

### Wave 2A — threshold policy after canonical V2

```text
R1 -> T1=A2_THRESHOLD_OR_MARGIN_POLICY
```

Read-only evidence appraisal may begin earlier, but final identity waits for canonical V2.

### Wave 2B — source route

```text
G1+G2 -> S1=A10_EXACT_SOURCE_ROUTE
```

### Wave 3A — atomic statistical/allocation design

```text
T1 -> D34=A3_PLUS_A4_ATOMIC_DESIGN
```

### Wave 3B — provenance template

```text
G1+G2+G3+G4+S1 -> P1=A9_PROVENANCE_TEMPLATE
```

### Wave 4A — contamination plan

```text
S1+P1 -> C1=A11_CONTAMINATION_PLAN
```

### Wave 4B — final personnel roster

```text
G1+G2+G3+D34 -> H1=A7_FINAL_PERSONNEL_ROSTER
```

### Wave 5A — storage/access policy

```text
G2+G3+G4+P1+H1 -> I1=A13_STORAGE_ACCESS_POLICY
```

### Wave 5B — spend/engagement disposition

```text
D34+G3+H1 -> F1=A14_SPEND_OR_ENGAGEMENT_AUTHORITY
```

### Wave 6 — preactivation join

```text
R1+T1+D34+G1+G2+G3+G4+S1+P1+C1+H1+I1+F1
    -> J1=FRESH_A1_TO_A14_READINESS_RECHECK
```

### Wave 7 — explicit activation

```text
J1=PASS
AND
SEPARATE_EXPLICIT_CONSTRUCTION_AUTHORIZATION
    -> A15
```

Nothing in Q1 authorizes any future wave automatically.

## 17. Carrier / PR classification

Q1 freezes the following carrier rules.

### Mandatory separate corrective-maintenance PR

```text
A1=YES
```

### May be carried as Spec 005 CLARIFY governance artifacts when docs-only and local to Spec 005

```text
A2=YES_SUBJECT_TO_NO_UPSTREAM_SCHEMA_MUTATION
A3+A4=YES
A5=YES
A6=YES
A8=YES
A9=YES
A10=YES
A11=YES
A12=YES
A13=YES
```

This does not mean they are complete or canonical merely because a draft artifact exists. They become canonical only through the repository's eventual guarded lifecycle closure/merge.

### Governance records requiring minimal disclosure

```text
A7=CANONICAL_POINTER_OR_AUDIT_DISPOSITION_ALLOWED
```

Exact personnel attestations may require a controlled record. Public repository artifacts should bind only the minimum necessary identity/disposition and MUST NOT require unnecessary sensitive personal details.

### Separate bounded authorizations, not corrective-maintenance repairs

```text
A14=SPEND_OR_ENGAGEMENT_AUTHORIZATION_IF_REQUIRED
A15=CONSTRUCTION_ACTIVATION_AUTHORIZATION
```

If any supposedly local gate later requires changing a closed upstream schema or rewriting historical semantics, it must be reclassified to separately reviewed corrective maintenance before mutation.

## 18. No circular-repair exception

The following shortcuts are prohibited:

```text
IMPLEMENT_A1_AND_PR34_CHANGES_IN_ONE_UNREVIEWED_BRANCH=PROHIBITED
FREEZE_A2_AGAINST_OBSOLETE_V1_THEN_RETROFIT_TO_V2=PROHIBITED
SET_A3_N_FROM_AVAILABLE_AUTHORED_CASES=PROHIBITED
SET_A4_ALLOCATION_FROM_AVAILABLE_AUTHORED_CASES=PROHIBITED
SELECT_PERSONNEL_THEN_REDUCE_D34_TO_FIT_AVAILABILITY=PROHIBITED
CREATE_CASES_THEN_BACKFILL_A5_A6_A8_A9_A11_A12_A13=PROHIBITED
USE_A14_BUDGET_PRESSURE_TO_LOWER_SCIENTIFIC_N=PROHIBITED
```

## 19. Critical-path interpretation

The scientific/contract critical path is:

```text
A1 -> A2 -> ATOMIC(A3+A4)
```

The governance/content-integrity path proceeds in parallel:

```text
A5+A6+A8+A12
    -> A10
    -> A9
    -> A11
```

The human/access path joins after the statistical design is known:

```text
A5+A6+A8+ATOMIC(A3+A4)
    -> A7
    -> A13

ATOMIC(A3+A4)+A8+A7
    -> A14
```

All paths converge before A15.

```text
NO_SINGLE_PATH_COMPLETION_IS_SUFFICIENT_FOR_CONSTRUCTION=YES
```

## 20. Current readiness after Q1

Q1 freezes ordering only. It does not complete any implementation gate.

```text
A1_STATUS=BLOCKED
A2_STATUS=BLOCKED
A3_A4_ATOMIC_STATUS=BLOCKED
A5_STATUS=BLOCKED
A6_STATUS=BLOCKED
A7_STATUS=BLOCKED
A8_STATUS=BLOCKED
A9_STATUS=BLOCKED
A10_STATUS=PARTIAL_ARCHITECTURE_ONLY
A11_STATUS=BLOCKED
A12_STATUS=BLOCKED
A13_STATUS=BLOCKED
A14_STATUS=BLOCKED
A15_STATUS=BLOCKED

ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
```

## 21. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 22. Lifecycle

```text
CLARIFICATION_SESSION_11=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_11_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Acceptance of Q1 does not authorize Q2 automatically, does not authorize A1 repair, does not authorize any A5–A14 implementation, and does not authorize construction.