# Session 12 Q2 — Exact Selection-Source Route and Derivation Contract

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 12 Q2 only. It freezes the governance design for A10, the exact selection-source route and derivation contract that must exist before the A9 provenance template can be finalized and before Arabic selection-suite construction can be authorized. It does **not** create, import, access, transform, translate, derive, review, bind, or execute any case or payload; implement A1; access Private Gold; access benchmark payloads; spend funds; execute models; or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION12_Q2_POLICY=ROUTE_EXPLICIT_PARENT_PRESERVING_SELECTION_SOURCE_CONTRACT_WITH_ORIGINAL_NON_PHI_DEFAULT

A10_GOVERNANCE_DESIGN=FROZEN
A10_IMPLEMENTED_AND_EXECUTED=NO
A10_GATE_STATUS=BLOCKED_PENDING_CANONICAL_ROUTE_RECORDS_AND_EXACT_SOURCE_IDENTITIES

CLARIFICATION_SESSION_12=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_12_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

## 2. Governing principle

Every item admitted to the future Arabic selection-development suite must have one explicit source route. The route is part of scientific identity and cannot be inferred from surface appearance, public availability, or a human claim that the item is "original enough."

```text
SOURCE_ROUTE_REQUIRED_PER_ROOT_TASK_OR_DERIVED_COMPONENT=YES
SOURCE_ROUTE_MUST_BE_PREDECLARED_BEFORE_CONTENT_ADMISSION=YES
UNKNOWN_SOURCE_ROUTE=BLOCKED
MIXED_UNDECLARED_SOURCE_ROUTE=BLOCKED

PUBLIC_VISIBILITY_EQUALS_SELECTION_ELIGIBILITY=NO
TRANSLATION_EQUALS_ORIGINAL_SOURCE=NO
PARAPHRASE_EQUALS_ORIGINAL_SOURCE=NO
DEIDENTIFICATION_EQUALS_ORIGINAL_SOURCE=NO
```

A route is admissible only if all relevant rights, privacy, provenance, purpose/quarantine, exact-binding, contamination, and review requirements are satisfied for that exact route.

## 3. Closed route classes

The future A10 protocol must use the following top-level route classes:

```text
ROUTE_1=ORIGINAL_HUMAN_AUTHORED_NON_PHI
ROUTE_2=PUBLIC_DEV_DIRECT
ROUTE_3=PUBLIC_DEV_DERIVED
ROUTE_4=AUTHORIZED_INTERNAL_DERIVED
ROUTE_5=MODEL_OR_PROVIDER_GENERATED
ROUTE_6=PROHIBITED_OR_BLOCKED_SOURCE
```

`ROUTE_5` is representable for future governance completeness but is not currently authorized.

## 4. Default route — ORIGINAL_HUMAN_AUTHORED_NON_PHI

The default and preferred initial source route is:

```text
SOURCE_ROUTE=ORIGINAL_HUMAN_AUTHORED_NON_PHI
ORIGIN_TYPE=ORIGINAL
DECLARED_USE=DEVELOPMENT_EVALUATION
PURPOSE=CHECKPOINT_SELECTION
REQUIRED_PRIVACY_STATE=NO_PHI_KNOWN
REQUIRED_RIGHTS_STATE=SUPPORTED
PRIVATE_GOLD_PARENT_COUNT=0
PUBLIC_TEST_PARENT_COUNT=0
```

The author may use general professional knowledge and independently authored fictional/composite clinical scenarios, but may not copy, reconstruct, translate, paraphrase, or lightly perturb a real patient record, Private Gold case, prohibited public test case, or unresolved third-party case.

```text
GENERAL_CLINICAL_KNOWLEDGE_MAY_INFORM_ORIGINAL_AUTHORING=YES
IDENTIFIABLE_SOURCE_CASE_MAY_BE_SILENTLY_RECAST_AS_ORIGINAL=NO
MEMORABLE_REAL_PATIENT_CASE_WITH_SURFACE_DETAILS_CHANGED=PROHIBITED
PRIVATE_GOLD_CASE_WITH_SURFACE_DETAILS_CHANGED=PROHIBITED
PUBLIC_TEST_CASE_WITH_SURFACE_DETAILS_CHANGED=PROHIBITED
```

The A5 contributor-rights instrument and A6 non-PHI attestation remain prerequisites for this route.

## 5. PUBLIC_DEV_DIRECT route

A direct public-development component may be admissible only when the exact source split is scientifically appropriate for selection and every source-level gate is resolved.

Required conditions:

```text
SOURCE_ROUTE=PUBLIC_DEV_DIRECT
SOURCE_SPLIT_ROLE=DEV_OR_EXPLICIT_SELECTION_COMPATIBLE
PUBLIC_TEST_SPLIT=NO
TRAIN_SPLIT_RELABELED_AS_SELECTION_DEV=NO_UNLESS_SEPARATELY_JUSTIFIED_AND_CANONICALLY_AUTHORIZED
EXACT_SOURCE_IDENTIFIER_REQUIRED=YES
IMMUTABLE_SOURCE_REVISION_OR_DIRECT_DIGEST_REQUIRED=YES
EXACT_ARTIFACT_BINDING_REQUIRED=YES
RIGHTS_STATE=SUPPORTED
PRIVACY_STATE=NO_PHI_KNOWN_OR_SEPARATELY_AUTHORIZED_EQUIVALENT
PURPOSE=CHECKPOINT_SELECTION
DECLARED_USE=DEVELOPMENT_EVALUATION
CONTAMINATION_DISPOSITION_REQUIRED_BEFORE_SELECTION_USE=YES
```

Public accessibility alone does not establish rights or scientific role.

```text
PUBLIC_DATASET_HOME_PAGE_IS_EXACT_ARTIFACT_BINDING=NO
MUTABLE_LATEST_REVISION_ALLOWED=NO
PUBLIC_TEST_SET_MAY_BE_RELABELED_AS_DEV=NO
```

## 6. PUBLIC_DEV_DERIVED route

Any translation, adaptation, paraphrase, restructuring, normalization that changes semantic content, or other derived use of a public-development parent is a derived route.

```text
SOURCE_ROUTE=PUBLIC_DEV_DERIVED
ORIGIN_TYPE=DERIVED
PARENT_ASSET_IDS_REQUIRED=YES
PARENT_ROUTE_IDENTITIES_REQUIRED=YES
PARENT_RIGHTS_PROPAGATE=YES
PARENT_PURPOSE_RESTRICTIONS_PROPAGATE=YES
PARENT_PRIVACY_RESTRICTIONS_PROPAGATE=YES
PARENT_CONTAMINATION_STATE_PROPAGATES_UNTIL_REASSESSED=YES
```

Derivation does not create broader rights or a cleaner scientific role than the parent possessed.

```text
TRANSLATION_CREATES_NEW_RIGHTS=NO
PARAPHRASE_CREATES_NEW_RIGHTS=NO
FORMAT_CONVERSION_CREATES_NEW_RIGHTS=NO
DERIVED_CHILD_MAY_ESCAPE_PARENT_TEST_SPLIT_PROHIBITION=NO
DERIVED_CHILD_MAY_ESCAPE_PARENT_PRIVATE_GOLD_PROHIBITION=NO
```

If modification/translation rights are not supported for the exact parent, the derived route is blocked.

## 7. AUTHORIZED_INTERNAL_DERIVED route

A future internally authored root case may have language variants, scoring specifications, or other selection artifacts derived from it after the root itself is admitted.

```text
SOURCE_ROUTE=AUTHORIZED_INTERNAL_DERIVED
ORIGIN_TYPE=DERIVED
PARENT_MUST_ALREADY_HAVE_ADMISSIBLE_INTERNAL_IDENTITY=YES
PARENT_ASSET_IDS_REQUIRED=YES
DERIVATION_METHOD_REQUIRED=YES
DERIVATION_ACTOR_OR_PROCESS_REFERENCE_REQUIRED=YES
```

For the Arabic-English paired suite:

```text
ROOT_SEMANTIC_SPECIFICATION_IS_PARENT_IDENTITY=YES
ARABIC_VARIANT_PARENT_INCLUDES_ROOT_ID=YES
ENGLISH_VARIANT_PARENT_INCLUDES_ROOT_ID=YES
PAIR_ID_SHARED=YES
ROOT_TASK_ID_SHARED=YES
CLINICAL_SEMANTIC_EQUIVALENCE_REVIEW_REQUIRED=YES
```

If one language realization is created from the other rather than in parallel from the root, that additional derivation relationship must be recorded rather than hidden.

```text
ARABIC_TRANSLATED_FROM_ENGLISH_MUST_RECORD_ENGLISH_AS_ADDITIONAL_PARENT_OR_DERIVATION_INPUT=YES
ENGLISH_TRANSLATED_FROM_ARABIC_MUST_RECORD_ARABIC_AS_ADDITIONAL_PARENT_OR_DERIVATION_INPUT=YES
PARALLEL_AUTHORING_FROM_ROOT_MAY_RECORD_ROOT_AS_COMMON_PARENT=YES
```

The scientific unit remains the matched root-task pair; the derivation graph does not create extra independent N.

## 8. MODEL_OR_PROVIDER_GENERATED route

This route remains non-authorized but must fail closed rather than being represented as human-original content.

```text
SOURCE_ROUTE=MODEL_OR_PROVIDER_GENERATED
ORIGIN_TYPE=MODEL_GENERATED_OR_SYNTHETIC
CURRENT_ROUTE_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
```

If separately authorized in the future, it would require at minimum:

```text
GENERATOR_IDENTITY
GENERATOR_MODEL_OR_SERVICE_IDENTITY
GENERATOR_VERSION_OR_REVISION
GENERATION_CONFIG_IDENTITY
INPUT_PARENT_ASSET_IDS
OUTPUT_USE_RIGHTS_EVIDENCE
PRIVACY_REVIEW
CONTAMINATION_REVIEW
HUMAN_CLINICAL_REVIEW
```

Model/provider output may not be silently relabeled as `ORIGINAL_HUMAN_AUTHORED_NON_PHI`.

## 9. Prohibited source routes

The following routes are prohibited for the current selection-development purpose:

```text
PRIVATE_GOLD_CASE_CONTENT
PRIVATE_GOLD_TRANSLATION
PRIVATE_GOLD_PARAPHRASE
PRIVATE_GOLD_DERIVATION
PRIVATE_GOLD_ANSWER_OR_RUBRIC_DERIVATION

PUBLIC_EXTERNAL_TEST_SPLIT_DIRECT
PUBLIC_EXTERNAL_TEST_SPLIT_TRANSLATION
PUBLIC_EXTERNAL_TEST_SPLIT_PARAPHRASE_OR_DERIVATION

REAL_PATIENT_PHI_OR_RESTRICTED_CLINICAL_DATA
UNRESOLVED_PRIVACY_SOURCE

UNRESOLVED_RIGHTS_SOURCE
INCOMPATIBLE_RIGHTS_SOURCE

UNBOUND_EXACT_BYTE_SOURCE_WHERE_EXACT_BINDING_REQUIRED
MUTABLE_UNPINNED_SOURCE

PROHIBITED_GATED_SOURCE_WITHOUT_SEPARATE_AUTHORITY
```

No contributor attestation, translation, deidentification claim, or reviewer preference may convert a prohibited route into an admissible selection route.

## 10. Private Gold metadata exception is taxonomy-only

Publicly disclosed Gold protocol metadata may constrain coverage taxonomy but is not case-content provenance.

```text
PUBLIC_GOLD_PROTOCOL_METADATA_MAY_INFORM_COVERAGE_TAXONOMY=YES
PUBLIC_GOLD_PROTOCOL_METADATA_COUNTS_AS_CASE_PARENT=NO
PUBLIC_GOLD_PROTOCOL_METADATA_AUTHORIZES_CASE_LEVEL_MIMICRY=NO
HIDDEN_GOLD_DISTRIBUTION_HINTS_MAY_BE_USED=NO
```

The five Arabic coverage anchors frozen in Session 10 remain taxonomy labels only; they do not authorize reconstruction of Gold cases or hidden distributions.

## 11. Parent-lineage closure

For every derived component, parent lineage must be transitively closed enough to prove the restrictions that govern the child.

```text
DIRECT_PARENT_IDS_REQUIRED=YES
MATERIAL_GRANDPARENT_RESTRICTIONS_MUST_REMAIN_TRACEABLE=YES
ORPHAN_DERIVED_ARTIFACT=BLOCKED
UNKNOWN_PARENT=BLOCKED
PARENT_WITH_BLOCKED_OR_PROHIBITED_ROUTE_CANNOT_YIELD_ADMISSIBLE_CHILD=YES
```

A child may be scientifically cleaner in wording but cannot outrun unresolved or incompatible parent rights, privacy, Gold, test-split, or provenance restrictions.

## 12. Route-specific rights semantics

A5 remains the governing contributor/content-rights architecture. A10 adds route-specific requirements:

```text
ORIGINAL_HUMAN_AUTHORED_NON_PHI
    -> contributor authority + project development-evaluation/adaptation/review grant

PUBLIC_DEV_DIRECT
    -> exact source evaluation-use rights for direct inclusion

PUBLIC_DEV_DERIVED
    -> direct-use rights plus modification/translation/derivation rights

AUTHORIZED_INTERNAL_DERIVED
    -> parent internal rights must already cover the derivative operation

MODEL_OR_PROVIDER_GENERATED
    -> generator/input/output rights all required if ever separately authorized
```

Rights may be narrower than technically possible operations.

```text
TECHNICALLY_POSSIBLE_TRANSLATION_IMPLIES_TRANSLATION_RIGHT=NO
TECHNICALLY_POSSIBLE_DOWNLOAD_IMPLIES_SELECTION_USE_RIGHT=NO
```

## 13. Route-specific privacy semantics

A6 remains the governing privacy architecture.

For the initial selection route:

```text
DEFAULT_ALLOWED_PRIVACY_STATE=NO_PHI_KNOWN
DEIDENTIFIED_REAL_PATIENT_SOURCE_AUTO_ALLOWED=NO
RESTRICTED_OR_PHI=PROHIBITED
UNRESOLVED=BLOCKED
```

Every derived child must receive its own privacy disposition where transformation could introduce or preserve identifying content.

```text
CLEAN_PARENT_AUTOMATICALLY_PROVES_CLEAN_CHILD=NO
CLEAN_ENGLISH_VARIANT_AUTOMATICALLY_PROVES_CLEAN_ARABIC_VARIANT=NO
```

## 14. Route-specific contamination semantics

A route may be admissible for authoring/provenance purposes yet still remain blocked from final selection use until contamination evidence is resolved.

```text
SOURCE_ROUTE_ADMISSIBILITY_EQUALS_CONTAMINATION_PASS=NO
CONTAMINATION_PASS_EQUALS_SOURCE_ROUTE_ADMISSIBILITY=NO
```

For external or derived sources where overlap risk is scientifically applicable:

```text
EXACT_SOURCE_OR_PARENT_IDENTITY_REQUIRED_FOR_CONTAMINATION_ANALYSIS=YES
SPLIT_SPECIFIC_CONTAMINATION_EVIDENCE_REQUIRED=YES
CANDIDATE_OR_CANDIDATE_CORPUS_BINDING_REQUIRED=YES
SELF_ASSERTED_CLEAN=PROHIBITED
```

Current authority remains:

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
```

## 15. Route decision record

Before an item may be represented by A9 provenance records, its future A10 route decision must bind at least:

```text
source_route_protocol_id
source_route_protocol_version
source_route_protocol_canonical_sha256
route_record_id
content_or_component_reference
source_route_class
origin_type
declared_use
purpose
source_identifier
source_revision_or_digest
artifact_binding_state
parent_asset_ids
rights_state
rights_evidence_id_or_reference
privacy_state
privacy_evidence_id_or_reference
quarantine_state
contamination_state
route_reviewer_reference_or_governance_disposition
route_status
```

For original human-authored content, source URI may be not applicable, but contributor/authoring evidence and content identity remain required. `NOT_APPLICABLE` must not be used to hide a real external parent.

## 16. Route status vocabulary

The future A10 protocol must use a closed route-status vocabulary:

```text
ADMISSIBLE_FOR_GOVERNED_CONSTRUCTION
BLOCKED_PENDING_EVIDENCE
PROHIBITED
SUPERSEDED
```

Semantics:

```text
ADMISSIBLE_FOR_GOVERNED_CONSTRUCTION
    = route evidence is sufficient for construction-stage provenance, subject to all other preconstruction gates and separate A15 activation

BLOCKED_PENDING_EVIDENCE
    = route may be potentially compatible but required evidence is unresolved

PROHIBITED
    = route conflicts with current purpose or hard boundary

SUPERSEDED
    = historical route record retained for reproducibility but replaced by a new identity
```

`ADMISSIBLE_FOR_GOVERNED_CONSTRUCTION` does not authorize construction by itself.

## 17. Route changes are material

A change in source route, parentage, rights basis, privacy basis, or purpose is material scientific/governance change.

```text
SOURCE_ROUTE_CHANGE_REQUIRES_NEW_ROUTE_RECORD_IDENTITY=YES
PARENT_SET_CHANGE_REQUIRES_NEW_CONTENT_OR_PROVENANCE_IDENTITY=YES
RIGHTS_BASIS_CHANGE_REQUIRES_REVIEW=YES
PRIVACY_BASIS_CHANGE_REQUIRES_REVIEW=YES
PURPOSE_CHANGE_REQUIRES_FRESH_ROUTE_ADJUDICATION=YES
```

A10 therefore composes with A12 change control; silent relabeling is prohibited.

## 18. Relationship to A9 provenance template

A10 is a prerequisite to A9 because A9 must encode the frozen route semantics rather than invent source categories later.

```text
A10_GOVERNANCE_DESIGN_BEFORE_A9_FINAL_TEMPLATE=REQUIRED
A9_TEMPLATE_MUST_ENCODE_A10_ROUTE_CLASS=YES
A9_TEMPLATE_MUST_ENCODE_PARENT_LINEAGE=YES
A9_TEMPLATE_MUST_ENCODE_RIGHTS_PRIVACY_PURPOSE_AND_BINDING=YES
```

Q2 freezes the route contract only; it does not make A9 complete.

## 19. A10 exit evidence required before construction readiness

A10 may become `PASS` only after a future canonical artifact proves:

```text
EXACT_SOURCE_ROUTE_PROTOCOL_CANONICAL=YES
PROTOCOL_VERSION_AND_SHA_BOUND=YES
CLOSED_ROUTE_CLASS_VOCABULARY_DEFINED=YES
ORIGINAL_HUMAN_NON_PHI_ROUTE_DEFINED=YES
PUBLIC_DEV_DIRECT_ROUTE_DEFINED=YES
PUBLIC_DEV_DERIVED_ROUTE_DEFINED=YES
AUTHORIZED_INTERNAL_DERIVED_ROUTE_DEFINED=YES
MODEL_PROVIDER_ROUTE_FAIL_CLOSED=YES
PROHIBITED_ROUTE_SET_DEFINED=YES
PRIVATE_GOLD_AND_PUBLIC_TEST_FIREWALL_DEFINED=YES
PARENT_LINEAGE_PROPAGATION_RULE_DEFINED=YES
ROUTE_SPECIFIC_RIGHTS_RULE_DEFINED=YES
ROUTE_SPECIFIC_PRIVACY_RULE_DEFINED=YES
ROUTE_SPECIFIC_CONTAMINATION_RULE_DEFINED=YES
ROUTE_DECISION_RECORD_SCHEMA_DEFINED=YES
INDEPENDENT_GOVERNANCE_REVIEW_COMPLETE=YES
```

Additionally, the exact source identities used by the future suite must be individually bound before construction/use; freezing this generic route architecture alone does not satisfy that requirement.

## 20. Resulting DAG state

Q2 resolves A10's design ambiguity but does not make A10 operationally complete.

```text
A1_STATUS=BLOCKED_NOT_IMPLEMENTED
A2_STATUS=BLOCKED
A3_A4_ATOMIC_STATUS=BLOCKED
A5_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A6_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A7_STATUS=BLOCKED
A8_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A9_STATUS=BLOCKED
A10_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
A11_STATUS=BLOCKED
A12_STATUS=BLOCKED_GOVERNANCE_DESIGN_FROZEN_ONLY
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
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE
A10_PROTOCOL_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
