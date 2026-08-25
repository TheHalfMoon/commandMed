# Session 11 Q2 — Exact A1 Corrective-Maintenance Preflight Manifest

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 11 Q2 only. It freezes the exact preflight scope and qualification contract for a future separately authorized A1 metrics-v2 corrective-maintenance repair. It does **not** authorize or implement A1, create a branch or pull request for A1, mutate canonical Spec 001/004 contracts, change any metric threshold, construct Arabic selection cases, access Private Gold, access benchmark payloads, execute models, spend funds, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION11_Q2_POLICY=EXACT_MINIMAL_ADDITIVE_A1_PREFLIGHT_WITH_V1_IMMUTABILITY_AND_VERSIONED_V2_CONSUMER_BINDING

A1_PREFLIGHT_MANIFEST=FROZEN
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE
A1_MERGE_AUTHORITY=NONE

A1_MUST_USE_SEPARATE_CORRECTIVE_MAINTENANCE_BRANCH_AND_PR=YES
PR34_MAY_IMPLEMENT_A1=NO
```

A future implementation may start only after separate explicit authorization that binds the then-live canonical `main` SHA and the exact A1 scope frozen here. This Q2 is not that authorization.

## 2. Canonical facts driving the preflight

Current canonical V1 facts:

```text
CANONICAL_MAIN_AT_Q2_PREFLIGHT=19aa95bbd122f3e01421ba2618dc1efe2f088289
CANONICAL_METRICS_V1_PATH=data/eval/metrics.json
CANONICAL_METRICS_V1_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a

V1_METRIC_RECORD_EVIDENCE_FIELD=required_evidence
V1_METRIC_RECORD_EVIDENCE_ROLE_DIMENSION=NONE

SPEC004_V1_CONSUMER_PIN=CANONICAL_UPSTREAM_IDENTITIES_V1.metrics_sha256
SPEC004_V1_PIN_VALUE=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

The existing V1 metric schema is flat and stores one `required_evidence` string. The current semantic canonicalizer does not have an `evidence_role` record sort key because V1 has no evidence-role record list. The Spec 004 fixture-only harness validates the canonical metrics artifact and requires its computed identity to equal `CANONICAL_UPSTREAM_IDENTITIES_V1`.

Therefore A1 must be additive and versioned. Replacing V1 in place is prohibited.

## 3. A1 exact scientific scope

A1 exists to repair the already-established metric evidence-role representation defect needed by the Arabic parity selection/final-audit separation.

```text
A1_PRIMARY_DEFECT=V1_METRIC_REQUIRED_EVIDENCE_CANNOT_MACHINE_READABLY_SEPARATE_SELECTION_DEV_FROM_PRIVATE_GOLD_FINAL_AUDIT

A1_REQUIRED_REPAIR=VERSIONED_METRICS_V2_WITH_EXPLICIT_EVIDENCE_ROLES

A1_ARABIC_PARITY_SELECTION_ROLE=SELECTION_DEV
A1_ARABIC_PARITY_SELECTION_PURPOSE=CHECKPOINT_SELECTION
A1_ARABIC_PARITY_SELECTION_SOURCE_POLICY=SELECTION_SAFE_NON_GOLD

A1_ARABIC_PARITY_FINAL_ROLE=PRIVATE_GOLD_FINAL_AUDIT
A1_ARABIC_PARITY_FINAL_PURPOSE=PRIVATE_GOLD
A1_ARABIC_PARITY_FINAL_SOURCE_POLICY=PRIVATE_GOLD_FAMILY
```

A1 must preserve `COMMANDMED_ARABIC_GOLD` as non-selection final-audit evidence and must not weaken Gold quarantine.

### Explicit scope exclusion: MedXpertQA metric expansion

Session 8 established that MedXpertQA `Text/dev` is not scientifically adequate as the sole primary quality-floor/winner-selection slice. A1 therefore must not smuggle a new MedXpertQA-specific or generic medical-MCQ metric into this repair solely because an earlier metric-identity gap was discovered.

```text
A1_ADD_NEW_MEDXPERTQA_METRIC=NO
A1_ADD_GENERIC_MEDICAL_MCQ_ACCURACY_METRIC=NO
A1_REDEFINE_MEDQA_USMLE_ACCURACY=NO
A1_WIDEN_MEDQA_USMLE_ACCURACY_TO_MEDXPERTQA=NO

SEPARATE_FUTURE_METRIC_ADDITION_REQUIRES_SEPARATE_JUSTIFICATION_AND_SCOPE_AUTHORIZATION=YES
```

This keeps A1 minimal and prevents unrelated scientific-policy changes from riding on the evidence-role repair.

## 4. Exact V1 immutability contract

The following are frozen invariants:

```text
DATA_EVAL_METRICS_JSON_CONTENT_MUTATION=PROHIBITED
DATA_EVAL_METRICS_JSON_DELETION=PROHIBITED
DATA_EVAL_METRICS_JSON_RENAME=PROHIBITED

CANONICAL_UPSTREAM_IDENTITIES_V1_MUTATION=PROHIBITED
CANONICAL_UPSTREAM_IDENTITIES_V1_METRICS_SHA_REPLACEMENT=PROHIBITED

HISTORICAL_V1_REPORT_SEMANTICS_MUTATION=PROHIBITED
HISTORICAL_V1_CLOSEOUT_REWRITE=PROHIBITED
HISTORICAL_V1_SPEC_REWRITE_TO_PRETEND_V2_EXISTED=PROHIBITED

V1_CANONICAL_METRICS_SHA256_MUST_REMAIN=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

The canonicalizer may receive additive V2 normalization support only if tests prove the V1 canonical digest remains exactly unchanged.

## 5. Exact A1 required path manifest

A future A1 implementation is bounded to the following **required paths** unless a pre-mutation exact-head inspection proves a required path has moved in canonical main. Any moved path must be re-authorized before mutation.

```text
A1_REQUIRED_PATH_01=ADD:data/eval/metrics-v2.json
A1_REQUIRED_PATH_02=MODIFY:src/commandmed/eval_contract/model.py
A1_REQUIRED_PATH_03=MODIFY:src/commandmed/eval_contract/validate.py
A1_REQUIRED_PATH_04=MODIFY:src/commandmed/eval_contract/canonical.py
A1_REQUIRED_PATH_05=MODIFY:src/commandmed/eval_contract/__init__.py
A1_REQUIRED_PATH_06=MODIFY:src/commandmed/tournament.py
A1_REQUIRED_PATH_07=ADD:tests/eval_contract/test_metrics_v2.py
A1_REQUIRED_PATH_08=ADD:tests/test_tournament_metrics_v2_identity.py
A1_REQUIRED_PATH_09=MODIFY:docs/evaluation/tournament-harness.md
A1_REQUIRED_PATH_10=ADD:specs/001-eval-charter/corrective-maintenance-metrics-v2.md
```

These ten paths are the predeclared minimal implementation surface.

### Why each path is required

```text
data/eval/metrics-v2.json
    -> new additive V2 catalog; V1 file remains untouched

src/commandmed/eval_contract/model.py
    -> controlled V2 evidence-role/schema types while preserving V1 types

src/commandmed/eval_contract/validate.py
    -> fail-closed V2 validator and cross-field role/purpose/source-policy invariants

src/commandmed/eval_contract/canonical.py
    -> deterministic V2 evidence-role record ordering without changing V1 digest

src/commandmed/eval_contract/__init__.py
    -> explicit public exports for the V2 contract/validator without removing V1 exports

src/commandmed/tournament.py
    -> additive versioned V2 consumer identity binding while preserving CANONICAL_UPSTREAM_IDENTITIES_V1 and V1 harness behavior

tests/eval_contract/test_metrics_v2.py
    -> focused V2 schema, validation, canonicalization, V1-preservation, and Arabic role tests

tests/test_tournament_metrics_v2_identity.py
    -> focused V1/V2 consumer identity separation and no-fallback tests

docs/evaluation/tournament-harness.md
    -> current documentation distinguishes historical V1 harness identity from additive V2 metric-contract identity

specs/001-eval-charter/corrective-maintenance-metrics-v2.md
    -> additive corrective-maintenance evidence record; historical Spec 001 lifecycle documents remain unchanged
```

## 6. Conditional path rule

A1 must not silently expand beyond the ten required paths.

A conditional path may be added only when all of the following are true before mutation:

```text
CONDITIONAL_PATH_NECESSITY_PROVEN_BY_LIVE_CANONICAL_CODE=YES
CONDITIONAL_PATH_DIRECTLY_REQUIRED_FOR_V2_CONTRACT_OR_IDENTITY_COMPATIBILITY=YES
CONDITIONAL_PATH_SCOPE_JUSTIFICATION_RECORDED=YES
CONDITIONAL_PATH_PREMUTATION_AUTHORIZATION_OBTAINED=YES
```

Potential conditional test paths, if the exact implementation proves necessary, are:

```text
CONDITIONAL:tests/eval_contract/test_canonical.py
CONDITIONAL:tests/eval_contract/test_hard_gates.py
CONDITIONAL:tests/eval_contract/test_fail_closed.py
CONDITIONAL:tests/test_tournament.py
CONDITIONAL:tests/test_tournament_contract_hardening.py
```

Default disposition is **do not edit them**. The new focused V2 test files should carry the new contract whenever possible. Existing tests must still run unchanged as regression evidence.

## 7. Exact no-go path classes

The following paths/classes must not be changed by A1:

```text
NO_GO:data/eval/metrics.json
NO_GO:data/eval/benchmarks.json
NO_GO:data/eval/gold_protocols.json
NO_GO:data/eval/quarantine.json
NO_GO:data/eval/safety_policy.json
NO_GO:data/lineage/lineage_contract.json

NO_GO:specs/001-eval-charter/spec.md
NO_GO:specs/001-eval-charter/plan.md
NO_GO:specs/001-eval-charter/tasks.md
NO_GO:specs/001-eval-charter/closeout.md

NO_GO:specs/002-safety-gates/**
NO_GO:specs/003-data-license-provenance/**
NO_GO:specs/004-tournament-harness/spec.md
NO_GO:specs/004-tournament-harness/plan.md
NO_GO:specs/004-tournament-harness/tasks.md
NO_GO:specs/004-tournament-harness/analysis.md
NO_GO:specs/004-tournament-harness/closeout.md

NO_GO:specs/005-base-model-tournament/**
```

Exception: A1 may not edit PR #34's Spec 005 clarification artifacts. PR #34 reconciliation occurs **after** A1 is independently merged to canonical main.

Also prohibited:

```text
NO_GO:workflow_changes
NO_GO:dependency_changes
NO_GO:runtime_or_model_execution_surface
NO_GO:benchmark_payloads
NO_GO:private_gold_payloads
NO_GO:credentials_or_secrets
NO_GO:PHI_OR_RESTRICTED_DATA
```

Any need to touch a no-go path is a scope failure requiring a new explicit authorization; it is not an implementation convenience exception.

## 8. Exact metrics-v2 envelope requirements

The V2 catalog path and outer identity are frozen from Session 10 Q2:

```text
METRICS_V2_PATH=data/eval/metrics-v2.json
METRICS_V2_SCHEMA_ID=commandmed-metrics-catalog
METRICS_V2_SCHEMA_VERSION=2.0
METRICS_V2_SUPERSEDES_V1_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

Every V2 metric record must preserve the scientific identity fields of its V1 counterpart unless a separately justified metric-specific correction is explicitly in A1 scope.

For this A1:

```text
V1_METRIC_IDS_REMOVED=0
V1_METRIC_IDS_RENAMED=0
V1_DIRECTIONS_CHANGED=0
V1_UNITS_CHANGED=0
V1_HARD_GATE_FLAGS_CHANGED=0
V1_APPLICABILITY_SEMANTICS_CHANGED=0
V1_THRESHOLD_VALUES_CREATED=0
V1_THRESHOLD_STATES_PROMOTED_TO_FROZEN=0
```

The authoritative V2 evidence field is:

```text
EVIDENCE_REQUIREMENTS_FIELD=evidence_requirements
```

Each evidence requirement must include exactly the Session 10 Q2 semantic fields:

```text
evidence_role
purpose
evidence_kind
binding_mode
source_policy
requirement
```

Unknown role/purpose/binding/source-policy values fail closed.

## 9. V2 migration rule for non-Arabic metrics

A1 must not accidentally grant new selection authority to every metric while migrating the catalog.

For metrics other than `arabic_clinical_parity_gap`:

```text
NEW_SELECTION_DEV_ROLE_AUTO_CREATED=NO
NEW_PRIVATE_GOLD_ROLE_AUTO_CREATED=NO
NEW_PUBLIC_EXTERNAL_EVAL_ROLE_AUTO_CREATED=NO

EXISTING_V1_REQUIRED_EVIDENCE_TEXT_MUST_REMAIN_TRACEABLE=YES
MIGRATION_MAY_USE_NON_SELECTION_QUALIFICATION_ROLE_ONLY_WHEN_SEMANTICALLY_LOSSLESS=YES
```

If a non-Arabic metric cannot be migrated without inventing a lifecycle role, that metric's V2 evidence role must remain explicitly unresolved/fail-closed according to the V2 schema design or the repair must stop for separate clarification. It must not infer selection eligibility from convenience.

## 10. Arabic parity V2 invariant

The V2 `arabic_clinical_parity_gap` record must contain exactly one role record for each required role:

```text
REQUIRED_ROLE_1=SELECTION_DEV
REQUIRED_ROLE_2=PRIVATE_GOLD_FINAL_AUDIT

DUPLICATE_SELECTION_DEV=REJECT
DUPLICATE_PRIVATE_GOLD_FINAL_AUDIT=REJECT
MISSING_SELECTION_DEV=REJECT
MISSING_PRIVATE_GOLD_FINAL_AUDIT=REJECT
```

Selection role:

```text
purpose=CHECKPOINT_SELECTION
source_policy=SELECTION_SAFE_NON_GOLD
PRIVATE_GOLD_SOURCE=REJECT
```

Final audit role:

```text
purpose=PRIVATE_GOLD
source_policy=PRIVATE_GOLD_FAMILY
CAN_SELECT_MODEL=NO_BY_CANONICAL_QUARANTINE
```

A1 does not bind an actual selection-safe Arabic suite; it only makes the evidence role representable. The exact suite identity remains a later A10/A9/Stage-B dependency.

## 11. Canonicalization invariants

The A1 canonicalizer change must be strictly additive:

```text
ADD_V2_RECORD_SORT_KEY=evidence_role
V2_EVIDENCE_REQUIREMENT_RECORD_ORDER_SEMANTICALLY_SET_LIKE=YES

V1_METRICS_DIGEST_BEFORE=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V1_METRICS_DIGEST_AFTER_MUST_EQUAL=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

Reordering `evidence_requirements` by JSON presentation order must not change the V2 semantic digest when role records are otherwise identical.

Changing any evidence-role semantic field must change the V2 digest.

## 12. Versioned consumer-binding contract

`src/commandmed/tournament.py` currently pins the V1 artifact map and validates supplied artifacts against it. A1 must preserve this V1 path exactly.

```text
CANONICAL_UPSTREAM_IDENTITIES_V1_PRESERVED=YES
V1_TOURNAMENT_SCHEMA_VERSION_1_0_BEHAVIOR_PRESERVED=YES
V1_ARTIFACT_KEYS_PRESERVED=YES
```

A1 must add an explicit V2 metric-contract identity binding without making V1 silently consume V2.

The V2 binding must carry at least:

```text
metrics_contract_schema_id=commandmed-metrics-catalog
metrics_contract_schema_version=2.0
metrics_catalog_path=data/eval/metrics-v2.json
metrics_catalog_sha256=<EXACT_V2_SHA_COMPUTED_FROM_CANONICAL_CONTENT>
```

Rules:

```text
V1_CONSUMER_FALL_FORWARD_TO_V2=PROHIBITED
V2_CONSUMER_FALL_BACK_TO_V1=PROHIBITED
MUTABLE_LATEST_METRICS_CONTRACT=PROHIBITED
SCHEMA_VERSION_MISMATCH=FAIL_CLOSED
PATH_MISMATCH=FAIL_CLOSED
SHA_MISMATCH=FAIL_CLOSED
```

A1 does not authorize a real Spec 005 tournament runner or benchmark execution. The binding is contract identity only.

## 13. Corrective-maintenance evidence record

The new additive maintenance record at:

```text
specs/001-eval-charter/corrective-maintenance-metrics-v2.md
```

must record at least:

```text
PRE_REPAIR_CANONICAL_MAIN_SHA
PRE_REPAIR_CANONICAL_MAIN_TREE
EXACT_REPAIR_BRANCH
EXACT_REPAIR_HEAD_SHA
EXACT_CHANGED_PATH_SET
V1_METRICS_SHA256_BEFORE
V1_METRICS_SHA256_AFTER
V2_METRICS_SHA256
V2_SCHEMA_ID
V2_SCHEMA_VERSION
V2_CATALOG_PATH
V2_CONSUMER_BINDING_IDENTITY
FOCUSED_TEST_RESULTS
FULL_OFFLINE_SUITE_RESULT
EXACT_HEAD_STATUS_CHECKS
INDEPENDENT_EXACT_HEAD_REVIEW_DISPOSITION
GUARDED_MERGE_RESULT
POST_MERGE_CANONICAL_MAIN_SHA
POST_MERGE_CANONICAL_MAIN_TREE
```

The file must not rewrite historical Spec 001 closeout claims.

## 14. Focused test matrix

The future A1 repair must add focused tests proving at least:

```text
T01_V1_METRICS_FILE_EXISTS_AND_UNCHANGED
T02_V1_METRICS_SHA_EXACTLY_304c980c...
T03_V1_VALIDATOR_STILL_ACCEPTS_CANONICAL_V1
T04_V1_TOURNAMENT_IDENTITY_MAP_UNCHANGED
T05_V1_TOURNAMENT_FIXTURE_BEHAVIOR_UNCHANGED

T06_V2_CATALOG_EXISTS_AND_VALIDATES
T07_V2_SCHEMA_ID_AND_VERSION_EXACT
T08_V2_SUPERSEDES_EXACT_V1_SHA
T09_V2_METRIC_IDS_PRESERVE_V1_METRIC_SET
T10_V2_NON_EVIDENCE_METRIC_FIELDS_PRESERVE_V1_SEMANTICS

T11_ARABIC_PARITY_HAS_EXACT_TWO_REQUIRED_EVIDENCE_ROLES
T12_ARABIC_SELECTION_ROLE_REJECTS_PRIVATE_GOLD_SOURCE
T13_ARABIC_FINAL_ROLE_REJECTS_SELECTION_SOURCE_POLICY
T14_UNKNOWN_EVIDENCE_ROLE_REJECTED
T15_UNKNOWN_PURPOSE_REJECTED
T16_UNKNOWN_BINDING_MODE_REJECTED
T17_UNKNOWN_SOURCE_POLICY_REJECTED
T18_DUPLICATE_ROLE_REJECTED
T19_MISSING_REQUIRED_ARABIC_ROLE_REJECTED

T20_V2_EVIDENCE_ROLE_RECORD_REORDERING_DIGEST_INVARIANT
T21_V2_SEMANTIC_ROLE_MUTATION_CHANGES_DIGEST
T22_V1_DIGEST_UNCHANGED_BY_CANONICALIZER_UPDATE

T23_V2_CONSUMER_BINDING_EXACT_SCHEMA_VERSION_PATH_SHA
T24_V1_TO_V2_FALL_FORWARD_REJECTED
T25_V2_TO_V1_FALLBACK_REJECTED
T26_V2_SHA_MISMATCH_REJECTED
T27_V2_PATH_MISMATCH_REJECTED
T28_V2_SCHEMA_VERSION_MISMATCH_REJECTED
```

## 15. Regression/full-suite matrix

No dependency installation is authorized by A1. Use only the repository's already-available Python runtime and standard-library test suite.

Required focused command set, subject to exact live repository import paths at implementation time:

```text
python -m unittest tests.eval_contract.test_metrics_v2
python -m unittest tests.test_tournament_metrics_v2_identity

python -m unittest \
  tests.eval_contract.test_canonical \
  tests.eval_contract.test_hard_gates \
  tests.eval_contract.test_fail_closed \
  tests.test_tournament \
  tests.test_tournament_contract_hardening
```

Required full offline regression:

```text
python -m unittest discover -s tests -p "test_*.py"
```

Requirements:

```text
FOCUSED_TESTS=PASS_REQUIRED
FULL_OFFLINE_SUITE=PASS_REQUIRED
NO_NETWORK_TEST_DEPENDENCY=REQUIRED
NO_MODEL_RUNTIME_REQUIRED=YES
NO_BENCHMARK_PAYLOAD_REQUIRED=YES
NO_PRIVATE_GOLD_PAYLOAD_REQUIRED=YES
```

A test result from a head older than the final repair head is not qualification evidence.

## 16. Diff and scope gates

Before review, the exact repair head must prove:

```text
EXACT_CHANGED_PATH_SET_EQUALS_AUTHORIZED_REQUIRED_PLUS_EXPLICITLY_AUTHORIZED_CONDITIONAL_PATHS=YES
UNAUTHORIZED_PATH_COUNT=0
WORKFLOW_PATH_CHANGES=0
DEPENDENCY_FILE_CHANGES=0
V1_METRICS_JSON_CHANGES=0
HISTORICAL_CLOSEOUT_REWRITES=0
SPEC005_PR34_FILE_CHANGES=0
```

Any unexpected changed path is a pre-review blocker.

## 17. Exact-head qualification gates

The future A1 repair may not be marked Ready or merged until all are true on one exact repair head:

```text
LIVE_BASE_REVERIFIED=PASS
EXACT_PATH_PREFLIGHT=PASS
V1_IDENTITY_PRESERVATION=PASS
V2_SCHEMA_VALIDATION=PASS
V2_IDENTITY_BINDING=PASS
FOCUSED_TESTS=PASS
FULL_OFFLINE_SUITE=PASS
STATUS_CHECKS=PASS_OR_EXPLICITLY_ACCOUNTED_FOR_WITH_NO_FALSE_CI_CLAIM
INDEPENDENT_EXACT_HEAD_REVIEW=NO_MATERIAL_BLOCKER
DRAFT_TO_READY_GATE_SEPARATELY_AUTHORIZED=YES
MERGE_GATE_SEPARATELY_AUTHORIZED=YES
```

CodeRabbit success alone is not independent exact-head review and is not GitHub Actions CI.

## 18. Guarded merge contract

If A1 is later separately authorized for merge:

```text
EXPECTED_HEAD_SHA_REQUIRED=YES
FORCE_PUSH=PROHIBITED
REBASE=PROHIBITED
MERGE_ONLY_AFTER_EXACT_HEAD_STABILITY_RECHECK=YES
POST_MERGE_MAIN_SHA_REVERIFICATION=REQUIRED
POST_MERGE_MAIN_TREE_REVERIFICATION=REQUIRED
POST_MERGE_V1_METRICS_SHA_REVERIFICATION=REQUIRED
POST_MERGE_V2_METRICS_SHA_REVERIFICATION=REQUIRED
```

A merge result is not complete until the resulting canonical `main` and both V1/V2 identities are reverified.

## 19. PR #34 post-A1 reconciliation contract

A1 merge does not automatically update or qualify PR #34.

Required sequence after a future A1 canonical merge:

```text
1. VERIFY_RESULTING_CANONICAL_MAIN_SHA_TREE
2. VERIFY_CANONICAL_V1_METRICS_SHA_UNCHANGED
3. VERIFY_CANONICAL_V2_SCHEMA_VERSION_PATH_SHA
4. REVERIFY_PR34_LIVE_HEAD_AND_BASE
5. NO_FORCE_PUSH_PR34
6. NO_REBASE_PR34
7. NONDESTRUCTIVE_RECONCILIATION_COMMIT_ONLY_IF_REQUIRED
8. MERGE_NEW_MAIN_INTO_PR34_ONLY_IF_NEEDED_FOR_EXACT_INTEGRATION_OR_CONFLICT
9. RECOMPUTE_PR34_DELTA_AGAINST_NEW_MAIN
10. FRESH_SPEC005_CLARIFICATION_BINDS_EXACT_V2_IDENTITY
11. FRESH_PR34_EXACT_HEAD_QUALIFICATION
12. FRESH_INDEPENDENT_REVIEW_WHEN_REQUIRED
```

A1 canonical merge does not freeze A2 automatically and does not grant Arabic construction authority.

## 20. A1 stop conditions

A future A1 implementation must stop fail-closed if any of the following occurs:

```text
LIVE_MAIN_MOVED_FROM_AUTHORIZED_BASE_BEFORE_MUTATION
REQUIRED_PATH_MOVED_OR_SEMANTICS_CHANGED_MATERIALLY
V1_METRICS_SHA_DIFFERS_FROM_EXPECTED_PRE_REPAIR_IDENTITY
A1_NEEDS_NO_GO_PATH_MUTATION
A1_NEEDS_WORKFLOW_OR_DEPENDENCY_CHANGE
V2_REQUIRES_UNPLANNED_NEW_METRIC_SEMANTICS
V2_MIGRATION_CANNOT_PRESERVE_NON_ARABIC_METRIC_SEMANTICS_FAIL_CLOSED
V1_DIGEST_CHANGES
V1_TOURNAMENT_BEHAVIOR_REGRESSES
FOCUSED_TEST_FAILURE
FULL_SUITE_FAILURE
EXACT_HEAD_REVIEW_MATERIAL_BLOCKER
```

A stop condition requires a new bounded decision; it does not authorize implementation improvisation.

## 21. Current A1 readiness after Q2

Q2 freezes the implementation preflight but does not satisfy implementation authority.

```text
A1_PREFLIGHT_SCOPE=FROZEN
A1_IMPLEMENTATION=NOT_STARTED
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH=NONE_CREATED_BY_Q2
A1_PR=NONE_CREATED_BY_Q2
A1_V2_SHA=UNRESOLVED_UNTIL_IMPLEMENTATION

A1_STATUS=BLOCKED_PENDING_SEPARATE_EXPLICIT_AUTHORIZATION
A2_STATUS=BLOCKED
A3_A4_ATOMIC_STATUS=BLOCKED
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
```

## 22. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
A1_IMPLEMENTATION_AUTHORITY=NONE
A1_BRANCH_CREATION_AUTHORITY=NONE
A1_PR_CREATION_AUTHORITY=NONE
A1_MERGE_AUTHORITY=NONE
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

## 23. Lifecycle

```text
CLARIFICATION_SESSION_11=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_11_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Acceptance of Q2 does not authorize Session 11 Q3 automatically, does not authorize A1 implementation, and does not authorize construction.
