# E004 DatasetSnapshot and Quarantine Founder Decision Request — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Current global frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v25-2026-09-04.md`  
**Canonical base:** `b7b4c9aaae8e76bdcef2c3def0cd856038e25558`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**DatasetSnapshot created:** NO  
**Quarantine PASS created:** NO  
**Near-duplicate PASS created:** NO  
**Model execution performed:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve the earliest dependency-safe authority gap after canonical freeze of the exact Aya-43 curriculum, all 43 content-scope verification identities, and the exact seven research-component sentinel fixtures: whether repository work may construct and freeze the exact DatasetSnapshot dependency for this bounded component, including the supporting duplicate/near-duplicate, contamination, and quarantine verification evidence required to make that snapshot meaningful and fail closed.

This request does not itself create any authority, supporting PASS, DatasetSnapshot, model identity, model winner, conversion, A15 activation, inference, training, credential, procurement, payment, or spend permission.

## 2. Exact already-canonical input subject

Any Decision B is restricted to the exact existing Aya-43 component subject and the already-frozen sentinel boundary:

```text
COMPONENT_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
FINAL_CURRICULUM_SOURCE_SET=COHERELABS_AYA_EXACT_43_ONLY
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
AYA_43_PERSISTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_LICENSE_ID=COHERELABS_AYA_DATASET_F9EA04583F02A8F86404FF6C58BF75FE637DF8A2_APACHE_2_0
SOURCE_AUTHORITY_ID=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
SPLIT_ID=VERIFIED_SFT_CURRICULUM_DATA
PURPOSE=TRAIN
CONTENT_SCOPE_VERIFICATION_COUNT=43
SENTINEL_FIXTURE_RECORD_COUNT=7
SENTINEL_FIXTURE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
```

Decision B cannot add, replace, remove, reorder by caller preference, or substitute a different dataset source. Any mismatch is fail closed.

## 3. Existing contamination and exact-duplicate evidence

The already-canonical Aya candidate path provides evidence that may be reused only within its exact declared meaning:

```text
CANDIDATE_CONSTRUCTION_FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
PROVISIONAL_CANDIDATE_COUNT=135
SOURCE_ROWS_EXCLUDED_AS_EXACT_DUPLICATE_CONTENT=3
CANDIDATE_CONTENT_SHA256_SET_UNIQUE=YES
CONTAMINATION_METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
CONTAMINATION_SUMMARY_SHA256=35cf4db119dd21c32a05ddd7e222cc2d6bf1f9ee5c5c694b6e682f784eb02e89
CONTAMINATION_ASSESSED_CLEAN_COUNT=135
CONTAMINATION_OVERLAP_OR_HIGH_RISK_COUNT=0
CONTAMINATION_UNRESOLVED_COUNT=0
PRIVATE_GOLD_USED=false
PUBLIC_EXTERNAL_EVAL_USED_AS_TRAINING_SOURCE=false
```

These facts do not establish semantic or near-duplicate independence among the 43 admitted records. The canonical `DuplicateContaminationReport` contract permits `PASS` only when no prohibited exact, near-duplicate, benchmark, quarantine, or post-render overlap remains. No independent near-duplicate PASS for the exact Aya-43 subject is canonical at this frontier.

Therefore Decision B, if selected, authorizes a bounded pre-result near-duplicate assessment; it does not predeclare that assessment's result.

## 4. Predeclared DatasetSnapshot identity semantics

Decision B fixes the following construction semantics before any new result is observed:

```text
DATASET_SNAPSHOT_CANDIDATE_ID=e004-aya-43-research-component-dataset-snapshot-v1
CANONICAL_ORDER_IDENTITY=AYA_43_CURRICULUM_RECORD_ID_ASCENDING_V1
CANONICAL_ORDER_RULE=LEXICOGRAPHIC_ASCENDING_CURRICULUM_RECORD_ID
EXPECTED_RECORD_COUNT=43
RECORD_SET_MUST_EQUAL_EXACT_AYA_43=YES
RENDERED_TOKEN_COUNT=null
SUPERVISED_TOKEN_COUNT=null
CALLER_SELECTED_RECORD_ORDER=PROHIBITED
CALLER_SELECTED_SUPPORTING_PASS=PROHIBITED
```

The snapshot SHA-256 is not predeclared. It must be computed only after all exact supporting identities are constructed and validated, using the canonical Spec 007 DatasetSnapshot serialization and self-excluding SHA-256 rule. Any change to record membership, order, semantically material metadata, or supporting identity changes the snapshot identity.

## 5. Predeclared duplicate and near-duplicate assessment

Decision B authorizes only the following bounded duplicate-report construction class for the exact Aya-43 subject:

```text
DUPLICATE_REPORT_CANDIDATE_ID=e004-aya-43-duplicate-contamination-report-v1
DUPLICATE_ASSESSMENT_METHOD_ID=AYA_43_INTERNAL_13_TOKEN_EXACT_NEAR_DUPLICATE_V1
EXACT_DUPLICATE_EVIDENCE_SOURCE=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
NEAR_DUPLICATE_NGRAM_LENGTH_TOKENS=13
NEAR_DUPLICATE_NORMALIZATION=UNICODE_NFKC_CASEFOLD
NEAR_DUPLICATE_TOKENIZATION=PYTHON_UNICODE_REGEX_WORD_TOKENS
NEAR_DUPLICATE_COMPARE_FIELDS=INPUTS_AND_TARGETS_SEPARATELY
NEAR_DUPLICATE_COMPARISON_UNIVERSE=EXACT_AYA_43_AGAINST_EXACT_AYA_43
SEMANTIC_JUDGE=NONE
MODEL_INFERENCE=NONE
POST_RESULT_THRESHOLD_CHANGE=PROHIBITED
POST_RESULT_METHOD_CHANGE=PROHIBITED
```

The assessment must exclude self-comparisons and must report any cross-record 13-token exact overlap fail closed as a `near_duplicate_groups` finding. It may reuse the already-canonical external benchmark contamination result for `benchmark_overlap_findings` only within the exact frozen method/universe described above.

If any prohibited exact duplicate, near duplicate, benchmark overlap, quarantine overlap, or post-render overlap remains, the report disposition must not be `PASS` and the DatasetSnapshot must not be frozen.

No raw Aya text, matched n-gram, user identifier, or comparison payload text may be persisted in canonical source.

## 6. Exact-byte rematerialization boundary for the near-duplicate replay

Because repository-safe Aya-43 artifacts contain hashes and categorical metadata rather than raw text, the predeclared near-duplicate assessment may require rematerializing the exact already-qualified Aya source bytes. Decision B authorizes only that exact public byte subject for this assessment under the already-established exact-byte verification and cleanup discipline:

```text
REMATERIALIZATION_SOURCE_REPOSITORY=CohereLabs/aya_dataset
REMATERIALIZATION_SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
REMATERIALIZATION_SOURCE_FILE=data/train-00000-of-00001.parquet
REMATERIALIZATION_REQUIRED_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
REMATERIALIZATION_SCOPE=LOCAL_DETERMINISTIC_AYA_43_NEAR_DUPLICATE_REPLAY_ONLY
USER_ID_READ=PROHIBITED
REMOTE_MODEL_OR_AI_RECORD_PROCESSING=PROHIBITED
RAW_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
TRANSIENT_RAW_BYTES_CLEANUP_REQUIRED=YES
INCREMENTAL_SPEND_USD=0
```

Any inability to obtain and verify the exact bytes leaves the duplicate report `BLOCKED`; it does not permit an alternate revision, mirror, source, heuristic PASS, or reduced subject.

## 7. Quarantine verification subject

Decision B authorizes construction of one exact research-component quarantine verification identity only after rereading the canonical quarantine matrix at the implementation head:

```text
QUARANTINE_VERIFICATION_CANDIDATE_ID=e004-aya-43-train-quarantine-verification-v1
QUARANTINE_PURPOSE=TRAIN
QUARANTINE_SOURCE_ID=VERIFIED_SFT_CURRICULUM_DATA
QUARANTINE_MATRIX_IDENTITY_REQUIRED=EXACT_CANONICAL_CURRENT_HEAD
QUARANTINE_ALLOWED_REQUIRED=true
QUARANTINE_CAN_TRAIN_REQUIRED=true
QUARANTINE_CAN_SELECT_MODEL_REQUIRED=false
QUARANTINE_STATUS_IF_ALL_CHECKS_MATCH=PASS
```

If the canonical matrix no longer allows `VERIFIED_SFT_CURRICULUM_DATA` for `TRAIN`, or any identity is stale/mismatched, status must not be `PASS` and the DatasetSnapshot must not be frozen.

This quarantine verification concerns the split/purpose identity. It does not reinterpret the Founder provenance field `source_authority_id` as a quarantine source identifier.

## 8. Narrow DatasetSnapshot builder corrective repair

The current `src/commandmed/spec007/snapshot.py` `_validated_records()` evaluates both `source_authority_id` and `split_id` as if both were canonical quarantine-matrix source IDs for purpose `TRAIN`.

For the exact canonical Aya-43 records:

```text
source_authority_id=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
split_id=VERIFIED_SFT_CURRICULUM_DATA
```

The first value is provenance/authority identity; the second is the training split/source identity that is represented in the canonical quarantine matrix. Treating the Founder authority ID as a quarantine source causes a deterministic false block and conflicts with the distinct field semantics in the Spec 007 data model.

Decision B therefore authorizes one narrow corrective repair to `src/commandmed/spec007/snapshot.py` and directly dependent tests only:

```text
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=AUTHORIZED_ONLY_IF_DECISION_B_SELECTED
REMOVE_SOURCE_AUTHORITY_AS_QUARANTINE_SOURCE_CHECK=YES
PRESERVE_CURRICULUM_RECORD_VALIDATION=YES
PRESERVE_SPLIT_TRAIN_QUARANTINE_CHECK=YES
PRESERVE_FAIL_CLOSED_UNKNOWN_OR_PROHIBITED_SPLIT=YES
PRESERVE_CANONICAL_QUARANTINE_MATRIX_BINDING=YES
PRESERVE_ALL_DATASET_SNAPSHOT_CROSS_FIELD_INVARIANTS=YES
WIDEN_ALLOWED_TRAIN_SOURCES=NO
CHANGE_AYA_43_FROZEN_RECORD_IDENTITIES=NO
CHANGE_QUARANTINE_JSON_POLICY=NO
```

This repair may not weaken quarantine policy, add an allowlist entry, mutate any frozen Aya-43 record, or bypass the separately persisted quarantine verification PASS required by the activation preflight.

## 9. Decision classes

### `E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_A` — preserve current state

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_A
DATASET_SNAPSHOT_AUTHORITY=NONE
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=NONE
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=NONE
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=NONE
```

Effect: V25 remains the active frontier and no DatasetSnapshot dependency is constructed.

### `E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B` — authorize the exact bounded supporting-evidence and snapshot path

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B
DATASET_SNAPSHOT_AUTHORITY=AUTHORIZED_CONDITIONAL_EXACT_AYA_43_RESEARCH_COMPONENT_ONLY
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_AYA_43_PREDECLARED_METHOD_ONLY
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_VERIFIED_SFT_CURRICULUM_DATA_TRAIN_BINDING_ONLY
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=AUTHORIZED_NARROW_PROVENANCE_VS_QUARANTINE_SEMANTICS_REPAIR_ONLY
DATASET_SNAPSHOT_FREEZE_REQUIRES_DUPLICATE_REPORT_PASS=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_CONTAMINATION_EVIDENCE_MATCH=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_QUARANTINE_VERIFICATION_PASS=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_EXACT_AYA_43_IDENTITY_MATCH=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_VALIDATOR_PASS=YES
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
MODEL_INFERENCE_AUTHORITY_EXPANSION=NONE
MODEL_WINNER_SELECTION_AUTHORITY_EXPANSION=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B authorizes construction; it does not predetermine a PASS result. If any supporting assessment fails or remains unavailable, the snapshot stays absent and the component remains blocked.

## 10. Authorized implementation surface under Decision B

Only after Decision B is separately captured canonically, its implementation may touch the minimum necessary paths in these families:

```text
src/commandmed/spec007/snapshot.py
scripts/e004_aya_43_dataset_snapshot_*.py
tests/spec007/test_quarantine_snapshot.py
tests/spec007/test_e004_aya_43_dataset_snapshot_*.py
.github/workflows/e004-aya-43-dataset-snapshot-*.yml
specs/007-sft-v1/e004-aya-43-dataset-snapshot-*
specs/007-sft-v1/e004-registry-current-state-reconciliation-v*.md
specs/007-sft-v1/tasks.md
specs/README.md
```

Changes outside this bounded set require separate applicable authority. A workflow, if needed, may transport only exact public bytes or perform repository-only deterministic validation consistent with the exact boundaries above; it may not receive Private Gold, gated assets, credentials, or model weights.

## 11. Qualification requirements under Decision B

Before any implementation PR may merge, the exact final head must prove at minimum:

```text
BOUNDED_DIFF_SCOPE=PASS
EXACT_AYA_43_INPUT_BINDING=PASS
EXACT_RECORD_COUNT_43=PASS
CANONICAL_ORDER_RULE=PASS
EXACT_DUPLICATE_EVIDENCE_BINDING=PASS
NEAR_DUPLICATE_ASSESSMENT_COMPLETED_OR_SNAPSHOT_BLOCKED=PASS
EXTERNAL_CONTAMINATION_EVIDENCE_IDENTITY_MATCH=PASS
QUARANTINE_MATRIX_IDENTITY_BINDING=PASS
QUARANTINE_TRAIN_SPLIT_DECISION_MATCH=PASS
SOURCE_AUTHORITY_NOT_TREATED_AS_QUARANTINE_SOURCE=PASS
FROZEN_AYA_43_IDENTITIES_UNCHANGED=PASS
DATASET_SNAPSHOT_VALIDATOR=PASS_IF_SNAPSHOT_CREATED
SNAPSHOT_SHA256_RECOMPUTATION=PASS_IF_SNAPSHOT_CREATED
NO_MODEL_INFERENCE=PASS
NO_TRAINING=PASS
NO_CREDENTIAL_OR_GATED_ASSET_USE=PASS
CURRENT_AUTHORIZED_SPEND_USD=0
FOCUSED_TESTS=PASS
COMPILEALL=PASS
DIFF_CHECK=PASS
```

No CI, evidence, assessment, quarantine, or snapshot PASS may be inferred from silence or from an earlier head.

## 12. Later boundaries remain closed

Even a successfully frozen DatasetSnapshot closes only dependency item 4 of the component preflight order. It does not select the tournament backbone or make E004 executable by itself.

```text
BASE_CHECKPOINT_BINDING=ABSENT_UNTIL_REQUIRED_UPSTREAM_WINNER_DECISION
MODEL_WINNER_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
SENTINEL_GUARD_PASS_CREATED=NO
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 13. Exact Founder response required

To preserve current state:

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_A
```

To authorize only the exact bounded path described above:

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B
```

A broad continuation instruction, generic approval, statement that all ordinary approvals are granted, PR merge, or an earlier Founder token is not substituted for this exact post-canonical decision.

The operative Founder response must occur after this decision-request surface is canonical and must be captured in a separate decision record before any newly authorized repair, near-duplicate replay, quarantine PASS construction, or DatasetSnapshot freeze occurs.

## 14. Current state until an operative decision is canonical

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=ABSENT
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=NONE
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=NONE
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 15. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded decision-request artifact. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, V25 and Aya-43/sentinel evidence identities, the current DatasetSnapshot/quarantine implementation semantics, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
