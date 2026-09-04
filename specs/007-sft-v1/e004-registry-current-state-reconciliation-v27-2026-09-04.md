# E004 Registry Current-State Reconciliation V27 — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Reconciliation class:** append-only current-state overlay  
**Supersedes as current view:** `e004-registry-current-state-reconciliation-v26-2026-09-04.md`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Canonicalization condition

This V27 is intended to become the current canonical view only when it is merged together with the exact repository-safe DatasetSnapshot bundle and supporting construction evidence on PR #244 after fresh exact-head validation of the committed bundle. It does not infer final-head PASS from the earlier pre-persistence head.

If this file is read from canonical `main` after that guarded merge, the statements below describe the canonical post-DatasetSnapshot state. If that merge did not occur, V26 remains the controlling current-state overlay.

## 2. Founder authority and narrow repair remain bounded

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B
DATASET_SNAPSHOT_AUTHORITY=AUTHORIZED_CONDITIONAL_EXACT_AYA_43_RESEARCH_COMPONENT_ONLY
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_AYA_43_PREDECLARED_METHOD_ONLY
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_VERIFIED_SFT_CURRICULUM_DATA_TRAIN_BINDING_ONLY
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=AUTHORIZED_NARROW_PROVENANCE_VS_QUARANTINE_SEMANTICS_REPAIR_ONLY
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

PR #243 already canonically repaired only the provenance-vs-quarantine semantic defect. `source_authority_id` remains provenance, `split_id` remains the canonical TRAIN quarantine subject, prohibited/unknown splits remain fail closed, the quarantine policy was not widened, and the frozen Aya-43 identities were not changed.

## 3. Exact Aya-43 supporting evidence is established

```text
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
AYA_43_PERSISTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
NEAR_DUPLICATE_ASSESSMENT_METHOD_ID=AYA_43_INTERNAL_13_TOKEN_EXACT_NEAR_DUPLICATE_V1
NEAR_DUPLICATE_PAIR_COUNT=0
DUPLICATE_REPORT_DISPOSITION=PASS
DUPLICATE_REPORT_CANONICAL_SHA256=562c3f3726538d27f2d40e2f20a762764b9f21c3675a3621672755c7cbc9d6b0
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
CONTAMINATION_SUMMARY_SHA256=35cf4db119dd21c32a05ddd7e222cc2d6bf1f9ee5c5c694b6e682f784eb02e89
```

The near-duplicate replay result was established under the predeclared exact method. Only repository-safe hashes, counts, categorical metadata, and approved evidence are persisted.

## 4. DatasetSnapshot dependency result

The exact pre-persistence PR #244 head `8ffcb147834ee7a91772503366aa62d08599d1cd` qualified in workflow run `33880609783`, job `101048063079`, and generated the exact safe bundle later persisted by this PR.

```text
DATASET_SNAPSHOT_ID=e004-aya-43-research-component-dataset-snapshot-v1
DATASET_SNAPSHOT_RECORD_COUNT=43
DATASET_SNAPSHOT_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
CANONICAL_ORDER_IDENTITY=AYA_43_CURRICULUM_RECORD_ID_ASCENDING_V1
DATASET_SNAPSHOT_VALIDATOR=PASS
DATASET_SNAPSHOT_SHA256_RECOMPUTATION=PASS
DATASET_SNAPSHOT_SHA256=c81da713b01d5ed9470ae9853834087bb6166f8f628d426371643a75064c1117
```

No caller-selected record order or supporting PASS was used.

## 5. Exact quarantine verification result

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
SOURCE_AUTHORITY_NOT_TREATED_AS_QUARANTINE_SOURCE=PASS
```

The exact current-head quarantine matrix therefore satisfies the predeclared Decision B condition for this split/purpose binding only.

## 6. Component dependency order after DatasetSnapshot

When this V27 is canonical with the committed bundle after exact-head qualification, the component dependency state is:

```text
DEPENDENCY_1_EXACT_ADMITTED_GRADIENT_CONTENT=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_2_CONTENT_SCOPE_VERIFICATION_IDENTITIES=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_3_EXACT_SEVEN_SENTINEL_FIXTURE_IDENTITIES=CONSTRUCTED_FROZEN_VALIDATED_EXACT_SUBJECT
DEPENDENCY_4_DATASET_SNAPSHOT_AND_QUARANTINE_IDENTITY=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_5_BASE_CHECKPOINT_BINDING=BLOCKED_BY_REQUIRED_UPSTREAM_WINNER_MODEL_DECISION
```

The canonical dependency order requires an exact `BaseCheckpointBinding` only after the required upstream winner/model decision exists. No such decision is created by the DatasetSnapshot work.

```text
NEXT_COMPONENT_DEPENDENCY=BASE_CHECKPOINT_BINDING
UPSTREAM_WINNER_MODEL_DECISION=ABSENT
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
NEXT_ELIGIBLE_REPOSITORY_ONLY_REAL_GATE_TRANSITION=NONE
```

This is a fail-closed dependency result, not permission to skip ahead to E005.

## 7. Cleanup truth reconciliation

The earlier Aya-135 local transient cleanup evidence recorded `LOCAL_TRANSIENT_CLEANUP_COMPLETE=YES` for the bounded paths observed at that time. Later, stale local raw Aya transport and tooling ZIP material was discovered, so that older completion claim cannot be used as current cleanup truth.

The exact Aya Parquet was reverified before the authorized near-duplicate replay and matched the canonical source SHA-256. This repository-safe reconciliation does not have evidence that every stale local/transient Aya/tooling path in the prior execution environment has since been removed and verified absent.

```text
PRIOR_LOCAL_TRANSIENT_CLEANUP_COMPLETE_CLAIM_CURRENTLY_RELIABLE=NO
LATER_STALE_RAW_AYA_TRANSPORT_MATERIAL_DISCOVERED=YES
LATER_STALE_TOOLING_TRANSPORT_MATERIAL_DISCOVERED=YES
EXACT_PARQUET_REVERIFIED_BEFORE_NEAR_DUPLICATE_REPLAY=YES
EXACT_PARQUET_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
CURRENT_LOCAL_TRANSIENT_CLEANUP_VERIFICATION=UNVERIFIED
LOCAL_TRANSIENT_CLEANUP_COMPLETE=NOT_CLAIMED
RAW_AYA_TEXT_REPOSITORY_PERSISTED=NO
```

A future cleanup-complete statement requires an actual fresh absence check in the local environment that held the transient material. No raw Aya content is persisted by this correction.

## 8. Privacy, execution, and zero-spend boundary

```text
RAW_AYA_TEXT_PERSISTED=false
MATCHED_NGRAM_PERSISTED=false
USER_ID_READ=false
MODEL_INFERENCE_USED=false
TRAINING_PERFORMED=false
CURRENT_AUTHORIZED_SPEND_USD=0
```

The DatasetSnapshot result is deterministic repository evidence only. It is not tournament execution, sentinel guard execution, conversion, A15 activation, or training evidence.

## 9. Later boundaries remain closed

```text
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
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
```

## 10. E004 / E005 / project state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

The DatasetSnapshot closes only component dependency item 4. E005 remains not reached because E004's tournament evidence pack is not complete, and no generic continuation approval can substitute for the required upstream winner/model decision or any later exact Founder gate.

## 11. Merge qualification boundary

Before PR #244 may merge, verify the exact final head, exact committed-bundle validation, all required workflow/check results, review/thread state, mergeability, current `main`, branch/ruleset state, and the expected-head merge guard. Any change to the PR head requires fresh exact-head qualification.
