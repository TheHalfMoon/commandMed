# E004 A11 Contamination-Assessment Authority Request Template — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `57e7a172ca888333255d4c12a441dbe9fd97c811`  
**Artifact class:** prospective exact-scope authority request template only  
**Authority owner:** Founder  
**Current authority state:** ABSENT  
**Activatable now:** NO  
**Payload access performed:** NO  
**Contamination assessment performed:** NO

This document prepares the future separate A11 contamination-assessment payload-access and execution authorization required by the frozen Session 12 Q4 sequence. It intentionally cannot grant or activate that authority now because the exact frozen selection-suite identities and all required assessment bindings do not yet exist.

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
PROSPECTIVE_REQUEST_TEMPLATE_ONLY=YES
AUTHORITY_ACTIVATABLE_NOW=NO
SELECTION_SUITE_CONSTRUCTED=NO
EXACT_SELECTION_SUITE_IDENTITY=ABSENT
A15_CONSTRUCTION_AUTHORITY=ABSENT
CONTAMINATION_PASS_CREATED=NO
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling temporal sequence

The frozen A11 design requires this order:

```text
1_FREEZE_A11_PLAN_BEFORE_AUTHORING
2_COMPLETE_ALL_OTHER_PRECONSTRUCTION_GATES
3_RECEIVE_SEPARATE_A15_CONSTRUCTION_AUTHORITY
4_CONSTRUCT_AND_FREEZE_EXACT_SELECTION_SUITE_IDENTITIES
5_RECEIVE_SEPARATE_CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AND_EXECUTION_AUTHORITY
6_EXECUTE_PREDECLARED_A11_METHODS_ON_EXACT_FROZEN_IDENTITIES
7_FREEZE_EVIDENCE_BOUND_CONTAMINATION_DISPOSITIONS
8_ONLY_THEN_MAY_CONTAMINATION_PREREQUISITE_BE_SATISFIED_FOR_FUTURE_SELECTION
```

This template prepares step 5 only. It cannot move step 5 before steps 3–4.

```text
PROSPECTIVE_TEMPLATE_MAY_BYPASS_A15_CONSTRUCTION_AUTHORITY=NO
PROSPECTIVE_TEMPLATE_MAY_BIND_MUTABLE_FUTURE_SUITE=NO
PROSPECTIVE_TEMPLATE_MAY_AUTHORIZE_UNKNOWN_PAYLOADS=NO
```

## 2. Plan gate is not evidence gate

```text
A11_PRECONSTRUCTION_OBJECT=ASSESSMENT_PLAN
A11_PLAN_PASS_EQUALS_CONTAMINATION_PASS=NO
A11_PLAN_PASS_GRANTS_ASSESSMENT_EXECUTION_AUTHORITY=NO
A11_PLAN_PASS_GRANTS_SELECTION_EXECUTION_AUTHORITY=NO
```

Likewise, canonical merge of this request template is not a contamination-assessment authorization.

## 3. Future authority subject must be exact

A future active authorization must bind one immutable request subject containing all required identities below. Any placeholder, mutable alias, `latest`, unresolved revision, or unknown universe keeps authority blocked.

### 3.1 Selection-suite identity

```text
selection_suite_id
selection_suite_version
selection_suite_canonical_sha256
selection_suite_content_universe_sha256
preconstruction_snapshot_sha256
a15_construction_activation_id
a15_construction_activation_sha256
```

The selection universe must cover the full required leakage-bearing content universe, not a sample.

```text
ASSESSMENT_UNIVERSE_POLICY=FULL_REQUIRED_SELECTION_CONTENT_UNIVERSE
SAMPLING_SELECTION_CASES_TO_PROVE_CLEAN=PROHIBITED
RESULT_DRIVEN_SUBSETTING=PROHIBITED
CANDIDATE_SPECIFIC_SELECTION_CONTENT_SUBSET=PROHIBITED
```

The bound universe must include, where applicable:

```text
ROOT_SEMANTIC_SPECIFICATIONS
ARABIC_LANGUAGE_VARIANTS
ENGLISH_LANGUAGE_VARIANTS
SCORING_OR_EXPECTED_BEHAVIOR_ARTIFACT_IDENTITIES_WHERE_CONTAMINATION_RELEVANT
MATERIAL_EXTERNAL_OR_INTERNAL_PARENT_CONTENT_IDENTITIES
```

## 4. Candidate/corpus binding required for every declared candidate

The future request must bind every frozen E001 candidate and CONTROL that participates in the assessment protocol.

For each candidate:

```text
candidate_id
candidate_exact_revision_or_identity
candidate_role
candidate_training_or_adaptation_corpus_evidence_identity_or_explicit_unavailable
candidate_corpus_coverage_state
candidate_corpus_coverage_evidence_id_or_reference
```

Allowed corpus coverage states remain:

```text
FULLY_BOUND
PARTIALLY_BOUND
UNAVAILABLE_OR_UNKNOWN
AUTHORITATIVE_EXTERNAL_DECONTAMINATION_EVIDENCE
```

```text
PARTIALLY_BOUND_CAN_PROVE_GLOBAL_CHECKED_CLEAN=NO
UNAVAILABLE_OR_UNKNOWN_CAN_PROVE_DIRECT_CORPUS_CHECKED_CLEAN=NO
GENERIC_MODEL_CARD_OR_VENDOR_DECONTAMINATION_CLAIM_SUFFICIENT=NO
```

## 5. Parent-aware scope

```text
PARENT_AWARE_CONTAMINATION_ASSESSMENT_REQUIRED=YES
DIRECT_PARENT_IDENTITIES_REQUIRED=YES
MATERIAL_ANCESTOR_RESTRICTIONS_AND_IDENTITIES_TRACEABLE=YES
CHILD_PARAPHRASE_ERASES_PARENT_CONTAMINATION_RISK=NO
TRANSLATION_ERASES_PARENT_CONTAMINATION_RISK=NO
SURFACE_REWRITE_ERASES_PARENT_CONTAMINATION_RISK=NO
```

A prohibited Private Gold or public-test parent cannot be laundered by a clean child-surface assessment.

## 6. Exact-axis authority binding

The future authority request must bind an already-predeclared exact-axis implementation, not merely a method family name.

```text
exact_method_id
exact_method_version_or_revision
exact_method_implementation_sha256_or_commit
exact_normalization_policy_id
exact_comparison_unit_definition
exact_selection_content_universe_identity
exact_candidate_corpus_identity_or_authoritative_evidence_identity
exact_corpus_coverage_state
exact_evidence_record_schema_id
exact_runtime_or_tool_identity
exact_runtime_or_tool_sha256_or_commit
```

```text
EXACT_METHOD_OPERATION_SET_PREDECLARED=YES
POST_RESULT_NORMALIZATION_CHANGE=PROHIBITED
POST_RESULT_EXACT_MATCH_RULE_CHANGE=PROHIBITED
```

## 7. Semantic-axis authority binding

The future request must separately bind:

```text
semantic_method_id
semantic_method_version_or_revision
semantic_method_family
semantic_implementation_identity
semantic_input_representation_policy_id
semantic_language_handling_policy_id
semantic_threshold_policy_id
semantic_threshold_policy_version
semantic_validation_or_calibration_evidence_reference
semantic_selection_content_universe_identity
semantic_candidate_or_corpus_binding_id
semantic_evidence_record_schema_id
semantic_runtime_or_tool_identity
semantic_runtime_or_tool_sha256_or_commit
```

No numeric semantic threshold is invented by this template.

```text
EXACT_NUMERIC_SEMANTIC_THRESHOLD=NOT_YET_FROZEN
SEMANTIC_THRESHOLD_MUST_BE_PREDECLARED_BEFORE_ASSESSMENT=YES
SEMANTIC_THRESHOLD_MUST_BE_FROZEN_BEFORE_CANDIDATE_RESULTS=YES
CANDIDATE_SPECIFIC_SEMANTIC_THRESHOLD=PROHIBITED
POST_RESULT_SEMANTIC_THRESHOLD_CHANGE=PROHIBITED
```

Until the exact threshold policy and its evidence are frozen, semantic-assessment execution remains blocked even if all other fields exist.

## 8. Arabic / English / cross-lingual scope

```text
ARABIC_CONTENT_SEMANTIC_ASSESSMENT_REQUIRED=YES
ENGLISH_CONTENT_SEMANTIC_ASSESSMENT_REQUIRED=YES
CROSS_LINGUAL_SEMANTIC_RISK_MUST_BE_ADDRESSED=YES
ENGLISH_ONLY_SEMANTIC_SCAN_PROVES_ARABIC_LOW_RISK=NO
ARABIC_ONLY_SEMANTIC_SCAN_PROVES_ENGLISH_LOW_RISK=NO
TRANSLATION_EQUIVALENCE_ALONE_PROVES_LOW_CONTAMINATION_RISK=NO
```

The future semantic method must explicitly identify how cross-lingual risk is assessed and validate that method for its claimed use.

## 9. Future authority action classes

The future Founder authorization must distinguish payload access from assessment execution.

### `A11_AUTHORITY_ACCESS`

Permits only the exact bytes needed for the bound contamination assessment subject.

```text
PURPOSE=CONTAMINATION_ASSESSMENT_ONLY
SELECTION_OR_RANKING_EXECUTION=PROHIBITED
MODEL_INFERENCE=PROHIBITED_UNLESS_A_SPECIFIC_PREDECLARED_CONTAMINATION_METHOD_SEPARATELY_REQUIRES_AND_AUTHORIZES_IT
TRAINING_OR_ADAPTATION=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_OR_RESTRICTED_DATA=PROHIBITED
GATED_OR_CREDENTIALED_ASSETS=PROHIBITED_UNLESS_SEPARATELY_AUTHORIZED
PROVIDER_GENERATION=PROHIBITED
SPEND=PROHIBITED_UNLESS_SEPARATELY_AUTHORIZED
```

### `A11_AUTHORITY_EXECUTE`

Permits only the predeclared exact and semantic contamination methods against the exact bound suite/candidate/corpus universe.

```text
METHOD_SWITCH_AFTER_RESULTS=PROHIBITED
THRESHOLD_CHANGE_AFTER_RESULTS=PROHIBITED
UNIVERSE_SUBSETTING_AFTER_RESULTS=PROHIBITED
CANDIDATE_SPECIFIC_RULE_CHANGE=PROHIBITED
ASSESSMENT_OUTPUT_MAY_RANK_MODELS=NO
ASSESSMENT_OUTPUT_MAY_AUTHORIZE_TRAINING=NO
```

The Founder may grant access and execution together only if every exact subject field is already bound and review-qualified; otherwise the request remains blocked.

## 10. Minimum execution-boundary metadata

A future active request must also bind:

```text
request_id
request_version
request_canonical_sha256
canonical_repository_commit
input_storage_locations_or_content_addresses
input_sha256_set
output_evidence_directory_or_content_address
runtime_environment_manifest_sha256
network_egress_policy
credential_state
spend_limit_usd
retention_and_deletion_policy
operator_or_executor_identity_if_required
independent_verifier_identity_if_required
```

No personal identity is invented by this template. If real personnel are required, their evidence remains external and identity-bound.

## 11. Frozen adjudication semantics

Future evidence must preserve:

```text
EXACT_AXIS_PASS_STATE=CHECKED_CLEAN
SEMANTIC_AXIS_PASS_STATE=ASSESSED_LOW_RISK
PASS_PAIR=CHECKED_CLEAN_PLUS_ASSESSED_LOW_RISK_WITH_ALL_EVIDENCE_BINDINGS
PASS_COMPOSITE=ASSESSED_CLEAN

EXACT_OVERLAP_FOUND=FAIL_CONTAMINATION_GATE
SEMANTIC_ASSESSED_HIGH_RISK=FAIL_CONTAMINATION_GATE
BLOCKED=BLOCKED_CONTAMINATION_GATE
PENDING=INCOMPLETE_CONTAMINATION_GATE
NOT_ASSESSED=INCOMPLETE_CONTAMINATION_GATE
INVALID_EVIDENCE=INVALID_EVIDENCE_INCOMPLETE
```

A clean claim is bounded to the declared, evidenced coverage; it is never a metaphysical claim of no contamination anywhere.

## 12. Fail-closed activation predicate

The prospective request becomes eligible to present for Founder authorization only if all conditions are true:

```text
A15_CONSTRUCTION_AUTHORITY_BOUND=YES
EXACT_SELECTION_SUITE_IDENTITY_BOUND=YES
FULL_REQUIRED_SELECTION_CONTENT_UNIVERSE_BOUND=YES
ALL_CANDIDATE_IDENTITIES_BOUND=YES
ALL_CANDIDATE_CORPUS_COVERAGE_STATES_BOUND=YES
PARENT_CHAIN_SCOPE_BOUND=YES
EXACT_METHOD_IDENTITY_BOUND=YES
SEMANTIC_METHOD_IDENTITY_BOUND=YES
SEMANTIC_THRESHOLD_POLICY_BOUND=YES
CROSS_LINGUAL_METHOD_BOUND=YES
RUNTIME_ENVIRONMENT_IDENTITY_BOUND=YES
INPUT_AND_OUTPUT_IDENTITY_SCHEME_BOUND=YES
ACCESS_CREDENTIAL_SPEND_BOUNDARIES_RESOLVED=YES
```

If any condition is false:

```text
A11_AUTHORITY_REQUEST_STATE=NOT_ACTIVATABLE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
```

## 13. Founder decision capture requirement

A future Founder response may become authority only when immediately preceded by the exact fully populated request subject and explicit action class(es). A generic continuation instruction cannot be retroactively interpreted as contamination payload-access/execution authority.

## 14. Current state after creating this template

```text
A11_REQUEST_TEMPLATE=PREPARED
A11_ACTIVE_REQUEST=ABSENT
A11_FOUNDER_DECISION=ABSENT
A11_ASSESSMENT_AUTHORITY=NONE
A11_ASSESSMENT_EXECUTION_OCCURRED=NO
CONTAMINATION_DISPOSITIONS_CREATED=0
E004_STATE=BLOCKED_PREFLIGHT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next A11 transition is not execution. It is completion of the upstream preconstruction/A15 construction sequence and identity binding required to make an exact authority request possible.
