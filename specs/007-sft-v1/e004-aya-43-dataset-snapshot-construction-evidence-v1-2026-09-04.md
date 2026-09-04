# E004 Aya-43 DatasetSnapshot Construction Evidence V1 — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Authority source:** `e004-dataset-snapshot-quarantine-founder-decision-2026-09-04.md`  
**Authority effect:** NONE beyond the already-canonical Founder Decision B  
**Model inference performed:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Exact authorized subject

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
AYA_43_PERSISTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
EXPECTED_RECORD_COUNT=43
EXPECTED_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
DATASET_SNAPSHOT_ID=e004-aya-43-research-component-dataset-snapshot-v1
CANONICAL_ORDER_IDENTITY=AYA_43_CURRICULUM_RECORD_ID_ASCENDING_V1
```

The construction surface consumes only the already-persisted repository-safe Aya-43 hash/categorical bundle and repository-safe evidence. It does not read raw Aya text, user identifiers, model weights, credentials, or a network resource.

## 2. Exact pre-persistence qualification

The exact pre-persistence PR head was:

```text
PR=244
QUALIFICATION_HEAD_SHA=8ffcb147834ee7a91772503366aa62d08599d1cd
QUALIFICATION_HEAD_TREE_SHA=09112a80ce81752edfe6a4ca4307519ecf7b2e44
BASE_SHA=c1fa05fea5bef5be20c8a6c5bdedeec096e9dd0f
WORKFLOW_RUN_ID=33880609783
WORKFLOW_JOB_ID=101048063079
WORKFLOW_NAME=E004 Aya-43 DatasetSnapshot construction V1
WORKFLOW_CONCLUSION=success
```

The exact-head job completed every required construction step successfully: exact-head checkout/binding, Founder-authority binding, compile, focused fail-closed tests, deterministic construction, privacy/non-execution assertions, diff check, and repository-safe artifact publication.

This record does not treat that earlier-head success as final persistence-head qualification. Adding the committed bundle/evidence/current-state records changes the PR head, so a fresh exact-head workflow run is mandatory before merge.

## 3. Repository-safe generated artifact

The exact run published one repository-safe artifact:

```text
GITHUB_ACTIONS_ARTIFACT_ID=9939667369
GITHUB_ACTIONS_ARTIFACT_NAME=E004_AYA_43_DATASET_SNAPSHOT_SAFE_BUNDLE_V1
GITHUB_ACTIONS_ARTIFACT_ZIP_SHA256=08681460a67b14d773bfdd0f9012d652b7359ad7db68eb60cefab6f16876425a
GENERATED_JSON_FILE_SHA256=53d3863986f87634146a39cca0d5695191ba8bad5b34ef5ae23a3f441edc4266
GENERATED_JSON_FILE_BYTES=6055
```

The committed JSON is the exact generated repository-safe JSON payload, not a re-authored approximation.

## 4. Duplicate and contamination binding

```text
NEAR_DUPLICATE_METHOD_ID=AYA_43_INTERNAL_13_TOKEN_EXACT_NEAR_DUPLICATE_V1
SELECTED_RECORD_COUNT=43
SELECTED_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
INPUT_WINDOW_COUNT=46
TARGET_WINDOW_COUNT=480
NEAR_DUPLICATE_PAIR_COUNT=0
DUPLICATE_REPORT_DISPOSITION=PASS
DUPLICATE_REPORT_CANONICAL_SHA256=562c3f3726538d27f2d40e2f20a762764b9f21c3675a3621672755c7cbc9d6b0
CONTAMINATION_REPORT_ID=e004-aya-135-qualification-evidence-v1
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
CONTAMINATION_SUMMARY_SHA256=35cf4db119dd21c32a05ddd7e222cc2d6bf1f9ee5c5c694b6e682f784eb02e89
```

The duplicate report canonical SHA was recomputed from the generated safe artifact and matched the claimed identity. No raw comparison text or matched n-gram is persisted.

## 5. Exact quarantine binding

The exact implementation head reread the canonical quarantine matrix through the canonical Spec 007 quarantine module and constructed this binding:

```text
QUARANTINE_VERIFICATION_ID=e004-aya-43-train-quarantine-verification-v1
QUARANTINE_VERIFICATION_STATUS=PASS
QUARANTINE_VERIFICATION_CANONICAL_SHA256=d19d74610d242008ec8d72231140e86a38bebc3af9ecf523ccb6e499569188f6
QUARANTINE_MATRIX_SHA256=e2b2fd52e2eef007935ffe497fb50656960fa4ab82caac45138e117594475477
QUARANTINE_PURPOSE=TRAIN
QUARANTINE_SOURCE_ID=VERIFIED_SFT_CURRICULUM_DATA
QUARANTINE_ALLOWED=true
QUARANTINE_CAN_TRAIN=true
QUARANTINE_CAN_SELECT_MODEL=false
SOURCE_AUTHORITY_TREATED_AS_QUARANTINE_SOURCE=false
```

`source_authority_id=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B` remains provenance only. The canonical `split_id=VERIFIED_SFT_CURRICULUM_DATA` remains the TRAIN quarantine subject. No quarantine allowlist was widened and no frozen Aya-43 record was mutated.

## 6. DatasetSnapshot result

```text
DATASET_SNAPSHOT_ID=e004-aya-43-research-component-dataset-snapshot-v1
DATASET_SNAPSHOT_RECORD_COUNT=43
DATASET_SNAPSHOT_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
CANONICAL_ORDER_RULE=LEXICOGRAPHIC_ASCENDING_CURRICULUM_RECORD_ID
CANONICAL_ORDER_RULE_RESULT=PASS
RENDERED_TOKEN_COUNT=null
SUPERVISED_TOKEN_COUNT=null
DATASET_SNAPSHOT_VALIDATOR=PASS
DATASET_SNAPSHOT_SHA256_RECOMPUTATION=PASS
DATASET_SNAPSHOT_SHA256=c81da713b01d5ed9470ae9853834087bb6166f8f628d426371643a75064c1117
```

The snapshot SHA was independently recomputed using the canonical Spec 007 self-excluding DatasetSnapshot SHA rule and matched the generated value.

## 7. Privacy, execution, and spend boundary

```text
RAW_AYA_TEXT_PERSISTED=false
MATCHED_NGRAM_PERSISTED=false
USER_ID_READ=false
MODEL_INFERENCE_USED=false
TRAINING_PERFORMED=false
CREDENTIAL_OR_GATED_ASSET_USE=false
CURRENT_AUTHORIZED_SPEND_USD=0
```

No raw Aya prompt/target text, matched n-gram text, user identifier, model inference result, training result, credential, gated asset, procurement, payment, or spend evidence is contained in the committed safe bundle.

## 8. Final persistence-head gate

Before PR #244 may merge, its exact final head must freshly validate the committed safe JSON via `scripts/e004_aya_43_dataset_snapshot_v1.py validate`, rerun focused tests and compile, reassert the privacy/non-execution boundary, and pass the exact-head diff check. No earlier-head success is substituted for that required final run.

```text
FINAL_PERSISTENCE_HEAD_QUALIFICATION=REQUIRED_BEFORE_MERGE
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
```

## 9. Authority exclusions

```text
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
SENTINEL_GUARD_PASS_CREATED=NO
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
