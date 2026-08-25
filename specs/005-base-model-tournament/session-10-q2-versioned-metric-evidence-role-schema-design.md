# Spec 005 — Session 10 Q2 Versioned Metric / Evidence-Role Schema Design

**Lifecycle:** CLARIFY ONLY  
**Evidence capture date:** 2026-08-23  
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Predecessor PR head:** `f59de186dcb88bf7facd912ccdbe2f550bc81237`

> This artifact freezes a corrective-maintenance **design contract only**. It does not implement or authorize corrective maintenance, modify `data/eval/metrics.json`, access Private Gold, create selection-dev payloads, execute benchmarks/models, access weights, freeze numeric thresholds, or advance to PLAN.

## 1. Q2 decision

```text
SESSION10_Q2_POLICY=VERSIONED_METRICS_V2_EXPLICIT_EVIDENCE_ROLE_SCHEMA

METRICS_V1_IN_PLACE_MUTATION=PROHIBITED
METRICS_V1_IN_PLACE_REINTERPRETATION=PROHIBITED
METRICS_V1_HISTORICAL_SEMANTICS_PRESERVED=YES

VERSIONED_METRICS_V2_REQUIRED=YES
V2_CORRECTIVE_MAINTENANCE_IMPLEMENTED=NO
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
```

The current canonical metric model is a flat record with one textual `required_evidence` field. The validator requires that field to be a non-empty string but has no machine-readable concept of selection evidence versus final-audit evidence. Q2 therefore freezes a separate V2 contract rather than silently changing the meaning of V1.

## 2. Exact V2 catalog envelope

A future separately authorized corrective-maintenance implementation MUST use a new catalog identity rather than overwrite the historical V1 catalog identity.

Proposed canonical V2 path and envelope:

```text
V2_CATALOG_PATH=data/eval/metrics-v2.json
V2_SCHEMA_ID=commandmed-metrics-catalog
V2_SCHEMA_VERSION=2.0
```

Exact top-level shape:

```json
{
  "schema_id": "commandmed-metrics-catalog",
  "schema_version": "2.0",
  "supersedes_metrics_v1_sha256": "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a",
  "metrics": []
}
```

Rules:

```text
V2_TOP_LEVEL_IS_OBJECT=YES
V2_METRICS_FIELD_IS_NONEMPTY_LIST=YES
V2_SCHEMA_ID_EXACT_MATCH_REQUIRED=YES
V2_SCHEMA_VERSION_EXACT_MATCH_REQUIRED=YES
V2_SUPERSEDES_V1_SHA_REQUIRED=YES

V1_FILE_DELETION=PROHIBITED
V1_FILE_REPLACEMENT_BY_V2=PROHIBITED
```

The exact future V2 semantic SHA-256 remains unresolved until an authorized implementation creates and validates the complete catalog.

```text
METRICS_V2_SHA256=UNRESOLVED_UNTIL_AUTHORIZED_IMPLEMENTATION
```

## 3. V2 metric record shape

Each V2 metric record MUST preserve the established metric identity fields while replacing the single-role evidence ambiguity with an explicit list of evidence-role requirements.

Exact required V2 metric fields:

```text
metric_id
name
category
description
direction
unit
is_hard_gate
threshold_state
applicable_roles
applicable_modalities
applicable_languages
evidence_requirements
```

`required_evidence` is a historical V1 field and MUST NOT remain the authoritative V2 evidence contract.

```text
V2_REQUIRED_EVIDENCE_STRING_IS_AUTHORITATIVE=NO
V2_EVIDENCE_REQUIREMENTS_LIST_IS_AUTHORITATIVE=YES
```

A future implementation MAY retain a clearly labeled non-authoritative legacy display field only if needed for migration tooling, but it MUST NOT be used for eligibility, threshold, selection, or audit decisions.

```text
OPTIONAL_V2_LEGACY_DISPLAY_FIELD=legacy_required_evidence_v1
LEGACY_DISPLAY_FIELD_GOVERNS_EXECUTION_OR_SELECTION=NO
```

## 4. Exact evidence-role record schema

Each element of `evidence_requirements` MUST be an object with these exact required fields:

```text
evidence_role
purpose
evidence_kind
binding_mode
source_policy
requirement
```

Controlled `evidence_role` vocabulary for V2:

```text
SELECTION_DEV
PRIVATE_GOLD_FINAL_AUDIT
PUBLIC_EXTERNAL_EVAL
QUALIFICATION_ONLY
```

Q2 does not require every metric to use every role. A metric MUST contain only the roles genuinely required by its governed lifecycle use.

Controlled `binding_mode` vocabulary:

```text
MANIFEST_BOUND
CANONICAL_FAMILY_BOUND
```

Controlled `source_policy` vocabulary:

```text
SELECTION_SAFE_NON_GOLD
PRIVATE_GOLD_FAMILY
PUBLIC_EXTERNAL_TEST_ONLY
IDENTITY_BOUND_QUALIFICATION_ASSET
```

`purpose` MUST use the existing canonical `Purpose` vocabulary. V2 MUST NOT invent a second purpose vocabulary.

## 5. Role-to-purpose invariants

The V2 validator MUST enforce these mappings:

```text
SELECTION_DEV -> purpose=CHECKPOINT_SELECTION
PRIVATE_GOLD_FINAL_AUDIT -> purpose=PRIVATE_GOLD
PUBLIC_EXTERNAL_EVAL -> purpose=PUBLIC_EXTERNAL_EVAL
QUALIFICATION_ONLY -> purpose=DEV
```

For V2 purposes, model-selection eligibility MUST be derived from the canonical quarantine contract for `purpose`; it MUST NOT be duplicated as an independently editable `can_select_model` field in the metric record.

```text
V2_METRIC_CAN_SELECT_MODEL_FIELD=PROHIBITED_AS_DUPLICATE_SOURCE_OF_TRUTH
SELECTION_ELIGIBILITY_DERIVED_FROM_QUARANTINE_PURPOSE=YES
```

If the V2 role/purpose combination conflicts with the canonical quarantine contract, validation MUST fail closed.

## 6. Arabic parity exact V2 evidence-role contract

The future V2 record for `arabic_clinical_parity_gap` MUST preserve its existing metric semantics:

```text
metric_id=arabic_clinical_parity_gap
direction=LOWER_BETTER
unit=relative_gap
is_hard_gate=true
applicable_languages=ar
```

Its authoritative V2 `evidence_requirements` MUST contain exactly two lifecycle roles unless a later separately reviewed scientific change explicitly revises that requirement:

### 6.1 Selection role

```json
{
  "evidence_role": "SELECTION_DEV",
  "purpose": "CHECKPOINT_SELECTION",
  "evidence_kind": "IDENTITY_BOUND_CLINICAL_EVIDENCE",
  "binding_mode": "MANIFEST_BOUND",
  "source_policy": "SELECTION_SAFE_NON_GOLD",
  "requirement": "Matched Arabic-English clinical task-pair evidence from an identity-bound selection-safe development suite"
}
```

Selection-role invariants:

```text
SELECTION_ROLE_PRIVATE_GOLD_SOURCE=PROHIBITED
SELECTION_ROLE_PUBLIC_EXTERNAL_TEST_SOURCE=PROHIBITED
SELECTION_ROLE_TRAIN_SOURCE=PROHIBITED
SELECTION_ROLE_EXACT_ARTIFACT_BINDING_REQUIRED=YES
SELECTION_ROLE_IMMUTABLE_SOURCE_REVISION_REQUIRED=YES
SELECTION_ROLE_RIGHTS_AND_LICENSE_RESOLUTION_REQUIRED=YES
SELECTION_ROLE_PRIVACY_AND_PHI_CLEARANCE_REQUIRED=YES
SELECTION_ROLE_CONTAMINATION_DISPOSITION_REQUIRED=YES
SELECTION_ROLE_MATCHED_ARABIC_ENGLISH_PAIR_DESIGN_REQUIRED=YES
```

### 6.2 Final-audit role

```json
{
  "evidence_role": "PRIVATE_GOLD_FINAL_AUDIT",
  "purpose": "PRIVATE_GOLD",
  "evidence_kind": "IDENTITY_BOUND_CLINICAL_EVIDENCE",
  "binding_mode": "CANONICAL_FAMILY_BOUND",
  "source_policy": "PRIVATE_GOLD_FAMILY",
  "requirement": "Paired final safety audit on COMMANDMED_ARABIC_GOLD"
}
```

For this role the canonical family binding MUST remain:

```text
PRIVATE_GOLD_FINAL_AUDIT_FAMILY=COMMANDMED_ARABIC_GOLD
PRIVATE_GOLD_FINAL_AUDIT_CAN_SELECT_MODEL=NO
PRIVATE_GOLD_FINAL_AUDIT_CAN_TRAIN=NO
```

A future implementation SHOULD encode the family identity in an explicit role-specific field such as `family_id` only for `CANONICAL_FAMILY_BOUND` records. Q2 does not require nullable placeholder fields on roles where they do not apply.

## 7. Evidence-role uniqueness and completeness

Validator invariants:

```text
EVIDENCE_REQUIREMENTS_NONEMPTY=YES
EVIDENCE_ROLE_UNIQUE_WITHIN_METRIC=YES
UNKNOWN_EVIDENCE_ROLE=REJECT
UNKNOWN_BINDING_MODE=REJECT
UNKNOWN_SOURCE_POLICY=REJECT
UNKNOWN_PURPOSE=REJECT
EMPTY_REQUIREMENT=REJECT

SELECTION_DEV_WITH_PRIVATE_GOLD_FAMILY_SOURCE_POLICY=REJECT
PRIVATE_GOLD_FINAL_AUDIT_WITH_SELECTION_SAFE_NON_GOLD_SOURCE_POLICY=REJECT
PUBLIC_EXTERNAL_EVAL_WITH_SELECTION_CAPABLE_PURPOSE=REJECT
```

For `arabic_clinical_parity_gap` specifically:

```text
MISSING_SELECTION_DEV_ROLE=REJECT_FOR_V2_CANONICAL_RECORD
MISSING_PRIVATE_GOLD_FINAL_AUDIT_ROLE=REJECT_FOR_V2_CANONICAL_RECORD
DUPLICATE_SELECTION_DEV_ROLE=REJECT
DUPLICATE_PRIVATE_GOLD_FINAL_AUDIT_ROLE=REJECT
```

## 8. Separation of threshold identities by lifecycle role

V2 evidence-role separation does not imply one numeric threshold serves both selection and final audit.

Future threshold policy identities MUST be explicit and versioned outside the evidence-role text itself.

```text
SELECTION_THRESHOLD_POLICY_ID_REQUIRED_BEFORE_SELECTION_PASS=YES
FINAL_AUDIT_THRESHOLD_POLICY_ID_REQUIRED_BEFORE_FINAL_AUDIT_PASS=YES

SAME_NUMERIC_THRESHOLD_ACROSS_ROLES_ASSUMED=NO
ROLE_SPECIFIC_THRESHOLD_POLICY_MAY_DIFFER=YES_IF_SEPARATELY_EVIDENCE_JUSTIFIED
```

The metric record MUST NOT embed an ungoverned numeric threshold as a shortcut around the canonical threshold-freeze process.

## 9. Exact report / manifest identity contract for V2 consumption

Any future evaluation artifact that consumes V2 MUST bind its metric contract explicitly. At minimum it MUST carry:

```text
metrics_contract_schema_id
metrics_contract_schema_version
metrics_catalog_sha256
metrics_catalog_path
```

For V2, required values are:

```text
metrics_contract_schema_id=commandmed-metrics-catalog
metrics_contract_schema_version=2.0
metrics_catalog_path=data/eval/metrics-v2.json
metrics_catalog_sha256=<exact authorized V2 canonical SHA-256>
```

Historical V1 reports remain bound to the historical V1 identity and MUST NOT be silently interpreted under V2.

```text
V1_REPORT_AUTOMATICALLY_UPGRADED_TO_V2=NO
V2_REPORT_MAY_OMIT_VERSION_AND_SHA=NO
V2_CONSUMER_MAY_FALL_BACK_TO_V1_ON_MISMATCH=NO
V1_CONSUMER_MAY_FALL_FORWARD_TO_V2=NO
```

Any version/SHA/path mismatch MUST fail closed before scoring or selection.

## 10. Canonical semantic hashing requirements

The future V2 catalog MUST use deterministic semantic canonicalization.

Because `evidence_requirements` is semantically a set of uniquely keyed role records rather than an ordered narrative sequence, corrective maintenance MUST update canonical normalization so these records are deterministically ordered by `evidence_role`.

```text
CANONICAL_RECORD_SORT_KEY_ADD=evidence_role
EVIDENCE_REQUIREMENTS_ORDER_IS_SEMANTICALLY_SET_LIKE_BY_UNIQUE_ROLE=YES
CANONICAL_HASH_MUST_BE_ORDER_INVARIANT_ACROSS_EVIDENCE_ROLE_RECORD_ORDER=YES
```

The implementation MUST NOT change the historical V1 canonical SHA by retroactively normalizing V1 differently.

## 11. Required V2 validator surface

A future corrective-maintenance implementation MUST provide a version-specific validator rather than weakening V1 validation.

Design requirement:

```text
VALIDATE_METRICS_CATALOG_V1=PRESERVED
VALIDATE_METRICS_CATALOG_V2=NEW_VERSION_SPECIFIC_VALIDATION
```

The exact function name is implementation-local, but behavior MUST be version-specific and fail closed.

Minimum V2 validation coverage:

```text
TOP_LEVEL_SCHEMA_ID_AND_VERSION
SUPERSEDES_V1_SHA
METRIC_ID_UNIQUENESS
EXISTING_METRIC_ENUM_VALIDATION
EVIDENCE_ROLE_ENUM_VALIDATION
ROLE_PURPOSE_COMPATIBILITY
ROLE_SOURCE_POLICY_COMPATIBILITY
ROLE_BINDING_MODE_COMPATIBILITY
ARABIC_PARITY_REQUIRED_DUAL_ROLE_PRESENCE
PRIVATE_GOLD_NON_SELECTION_INVARIANT
SELECTION_NON_GOLD_INVARIANT
CANONICAL_HASH_DETERMINISM
```

## 12. Backward-compatibility policy

Corrective maintenance MUST be additive/versioned, not destructive.

```text
V1_REMAINS_READABLE=YES
V1_REMAINS_HASH_REPRODUCIBLE=YES
V1_VALIDATOR_REMAINS_AVAILABLE_FOR_HISTORICAL_ARTIFACTS=YES

V2_BECOMES_CURRENT_FOR_NEW_SELECTION_ONLY_AFTER_CANONICAL_MERGE_AND_EXPLICIT_CONSUMER_BINDING=YES
V2_EXISTENCE_ALONE_CHANGES_SPEC005_CURRENT_CONTRACT=NO
```

No consumer may infer "latest" dynamically.

```text
MUTABLE_LATEST_METRICS_CONTRACT_SELECTION=PROHIBITED
EXPLICIT_VERSION_AND_SHA_BINDING_REQUIRED=YES
```

## 13. Atomic corrective-maintenance boundary

A future authorized repair MUST reconcile all current consumers atomically enough that canonical main never claims V2 selection while its current selection consumer is pinned only to incompatible V1 semantics.

Required repair scope includes:

```text
ADD_METRICS_V2_CATALOG
ADD_V2_MODEL_OR_SCHEMA_TYPES
ADD_V2_VALIDATION
ADD_V2_CANONICAL_NORMALIZATION_RULES
ADD_OR_UPDATE_VERSIONED_CURRENT_IDENTITY_BINDING
PRESERVE_HISTORICAL_V1_IDENTITY_BINDING
ADD_V1_V2_COMPATIBILITY_TESTS
ADD_NEGATIVE_CROSS_VERSION_TESTS
ADD_ARABIC_PARITY_ROLE_INVARIANT_TESTS
RUN_FOCUSED_SPEC001_SPEC002_SPEC004_VALIDATION
RUN_FULL_OFFLINE_SUITE
FRESH_INDEPENDENT_EXACT_HEAD_REVIEW
```

The exact repaired V2 content, SHA, consumer binding version name, and migration mechanics remain implementation decisions for the separately authorized corrective-maintenance PR.

## 14. No schema-level payload authority

The V2 schema can describe evidence requirements. It does not authorize access to the evidence.

```text
SCHEMA_ROLE_DEFINITION_GRANTS_PAYLOAD_ACCESS=NO
SCHEMA_ROLE_DEFINITION_GRANTS_PRIVATE_GOLD_ACCESS=NO
SCHEMA_ROLE_DEFINITION_GRANTS_BENCHMARK_EXECUTION=NO
SCHEMA_ROLE_DEFINITION_GRANTS_MODEL_EXECUTION=NO
SCHEMA_ROLE_DEFINITION_GRANTS_SELECTION=NO
```

Selection remains blocked until exact evidence identities, contamination, rights/privacy, threshold policies, sample-size/statistical prerequisites, and execution authority are separately canonical.

## 15. Items intentionally unresolved by Q2

```text
EXACT_METRICS_V2_SHA256=UNRESOLVED
EXACT_V2_FULL_CATALOG_CONTENT=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_SUITE_IDENTITY=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_SUITE_SOURCE=UNRESOLVED
EXACT_ARABIC_PARITY_SELECTION_THRESHOLD_POLICY_ID=UNRESOLVED
EXACT_ARABIC_PARITY_FINAL_AUDIT_THRESHOLD_POLICY_ID=UNRESOLVED
EXACT_NUMERIC_ARABIC_PARITY_THRESHOLD_OR_MARGIN=UNRESOLVED
EXACT_SAMPLE_SIZE_OR_POWER=UNRESOLVED
EXACT_REVIEWER_IDENTITIES=UNRESOLVED
EXACT_VERSIONED_CURRENT_CONSUMER_BINDING_NAME=UNRESOLVED
```

## 16. Authority boundary

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
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 17. Lifecycle state after Q2

```text
CLARIFICATION_SESSION_10=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_10_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Q2 freezes the exact V2 schema design only. It neither implements the repair nor resolves the Arabic parity evidence blocker on live canonical main.