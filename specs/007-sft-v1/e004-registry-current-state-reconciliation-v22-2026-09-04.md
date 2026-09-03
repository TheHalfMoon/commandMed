# E004 Registry Current-State Reconciliation V22 — 2026-09-04

**Spec:** 007 SFT V1
**Task:** E004
**Artifact class:** append-only global current-state reconciliation
**Canonical base at branch creation:** `4f9a3b6c9d65b0ece41e2100ed3290178d3d2b84`
**Authority source:** `FD-008` / `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the E004 global frontier after the exact Aya-135 deterministic FD-008 categorical evidence was bound to the exact candidate content digests and evaluated by the canonical Spec 003 lineage evaluator.

This record supersedes V21 only for prospective current-state interpretation. V21 and all earlier source, transport, candidate-construction, contamination, human-boundary, deterministic-method, materialization, cleanup, and Spec 003 audit records remain immutable historical evidence under their original identities.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v21-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v22-2026-09-04.md
FOUNDER_AMENDMENT=docs/aya-135-human-review-gate-amendment-2026-09-03.md
FD008_DECISION=REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE
AUTHORITY_EXPANSION_FROM_V22=NONE
```

An older unmerged divergent branch named `docs/e004-aya-deterministic-results-v22` is not canonical `main` history and does not govern this record. Its historical committed deterministic evidence failed byte-identity verification against the SHA-256 it declared. V22 therefore uses the corrected direct-digest replay qualified by PR #226 rather than importing that stale evidence or stale cleanup state.

## 2. Exact Aya subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
```

No source, revision, file, filter, record set, content set, language, role, capability, or candidate expansion is created by V22.

## 3. Preserved contamination evidence

```text
CONTAMINATION_METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
ASSESSED_CLEAN=135
OVERLAP_OR_HIGH_RISK=0
CONTAMINATION_UNRESOLVED=0
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
```

`ASSESSED_CLEAN` retains only the meaning of that exact frozen method and comparison universe. V22 does not broaden the claim.

## 4. FD-008 deterministic evidence and exact content binding

The deterministic method remains frozen:

```text
DETERMINISTIC_METHOD_ID=AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1
DETERMINISTIC_EVIDENCE_OUTPUT_SHA256=129688b220a75773a7709c656a2aa313f2aed770541dc62a39b3351848beb07d
DETERMINISTIC_PROJECTION_SHA256=1c696862705e50f10b8621f425389f8f9db0122ef8cc3027e46d50d6835430e7
CANDIDATE_COUNT=135
SCOPE_PASS=135
SCOPE_FAIL=0
SCOPE_UNRESOLVED=0
PRIVACY_NO_PHI_KNOWN=118
PRIVACY_UNRESOLVED=17
PRIVACY_RESTRICTED_OR_PHI=0
RECORD_LEVEL_RIGHTS_SUPPORTED=43
RECORD_LEVEL_RIGHTS_UNRESOLVED=92
```

PR #226 adds only repository-safe candidate identifiers, exact content digests, and categorical evidence. It contains no Aya raw input/target text and no `user_id`.

The exact content-digest map parts are:

```text
CONTENT_DIGEST_MAP_PART_01_SHA256=b6028a65c05d41a251ef8b4a5073d30e8b4048322853a97ad020783cdea79687
CONTENT_DIGEST_MAP_PART_02_SHA256=59d1445a98f6ac5bfc8d50fb125700fbbd590d61f17b7fd35e1f9d0f428923a3
CONTENT_DIGEST_MAP_PART_03_SHA256=48310fdf92872e39d0c4f9527dab52e6682b9a117040f2cedef70fcf4eb63ef2
CONTENT_DIGEST_MAP_PART_04_SHA256=5d58375d6a36eaa1abb5fedda95004d12381e685b09b20c129171ddadf2d4b95
CONTENT_DIGEST_MAP_PART_05_SHA256=13014dcfab8fc511554c2f4fcd7afa105a84c7ccd43cf449b583627ed0fb1597
CONTENT_DIGEST_MAP_RECORD_COUNT=135
CONTENT_DIGEST_MAP_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CONTENT_DIGEST_MAP_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
```

The deterministic evidence never computes admission. Caller-controlled `ELIGIBLE` remains prohibited.

## 5. Corrected canonical Spec 003 direct-digest result

The corrected replay binds every fixed candidate identity directly to its exact content SHA-256 and delegates admission to the canonical Spec 003 evaluator.

```text
SPEC003_EVALUATOR_LINEAGE_GIT_BLOB=5d7a5b6a8b48b2b5a7afea35ed18ceb1c9fe6425
SPEC003_LINEAGE_CONTRACT_GIT_BLOB=692de9b32271031b0f1dd9cc6edc98bc44b580b5
ARTIFACT_BINDING_STATE=DIRECT_DIGEST
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
```

The first qualified corrected exact-head replay used PR #226 head `75708143be5cc040d7bb8ea8a2d65c1e5ab0b981`, Actions run `33808884207`, job `100825795693`, and produced:

```text
SPEC003_CORRECTED_DIRECT_DIGEST_RESULTS_SHA256=a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4
SPEC003_CANDIDATE_COUNT=135
SPEC003_ELIGIBLE_COUNT=43
SPEC003_BLOCKED_COUNT=92
SPEC003_VALIDATION_ERROR_COUNT=0
RIGHTS_UNRESOLVED_REASON_COUNT=92
PRIVACY_UNRESOLVED_REASON_COUNT=17
```

The pull request must reproduce this exact result on its final exact head before merge. Any identity, root, state-count, reason-count, validation-count, or result-SHA mismatch fails closed.

The superseded historical result SHA `3e7e4f15a913ca5e72c091aee4dda563f48037ed6fd67a3781fef1ade71d21ef` is not used as current admission evidence because its historical committed deterministic evidence did not satisfy the declared byte identity.

## 6. Data-admission interpretation

```text
AYA_135_SPEC003_EVALUATION_EXECUTED=YES
AYA_135_EXACT_ELIGIBLE_RECORD_COUNT=43
AYA_135_EXACT_BLOCKED_RECORD_COUNT=92
AYA_135_VALIDATION_ERROR_COUNT=0
AYA_135_ELIGIBILITY_SOURCE=CANONICAL_SPEC003_EVALUATOR_DIRECT_DIGEST_ONLY
AYA_135_BLOCKED_RECORDS_DOWNSTREAM_ADMISSION=PROHIBITED
```

Only the exact 43 candidate identities computed `ELIGIBLE` by the corrected canonical direct-digest replay may be described as Spec 003 eligible. The other 92 remain blocked.

This is record-level Spec 003 eligibility evidence only. It is not final gradient-bearing curriculum admission, a DatasetSnapshot, quarantine PASS, live RunManifest, guard PASS, tournament evidence pack, backbone-winner selection, or training authorization.

## 7. Exact next dependency-safe frontier

The canonical component construction order requires exact admitted gradient-bearing content to be frozen before content-scope identities, sentinel fixtures, DatasetSnapshot, RunManifest, real guard results, and execution preflight can become complete.

The exact 43 eligible records do not by themselves grant final curriculum admission authority.

```text
CURRENT_AYA_DATA_FRONTIER=SPEC003_EXACT_43_ELIGIBLE_RECORD_SET_ESTABLISHED
NEXT_COMPONENT_DEPENDENCY=FREEZE_EXACT_ADMITTED_GRADIENT_BEARING_CONTENT
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
```

A separately canonical authority surface is required before final curriculum construction/admission or DatasetSnapshot creation may be asserted.

## 8. Preserved successor execution decision

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
```

These authorities remain conditional on exact PASS preflight and do not provide the missing curriculum, snapshot, scope, guard, access, finance/resource, conversion, or training prerequisites.

## 9. Broader E004 gates remain closed

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

V22 creates no authority to bypass any of these gates.

## 10. E004/E005 state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
E005_REACHABLE=NO
PROJECT_FINISHED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

The E004 blocker has advanced: deterministic record evidence and corrected direct-digest Spec 003 admission are complete for the fixed Aya-135 subject, while final curriculum admission/DatasetSnapshot authority and the remaining component preflight prerequisites are still absent or unauthorized.

## 11. Explicit exclusions

V22 performs or claims no final curriculum construction/admission, DatasetSnapshot freeze, quarantine PASS, model conversion, quantization, model inference, tournament execution, live guard execution, A15 activation, training, Private Gold/PHI/gated access, credential use, provider generation, procurement, payment, spend, clinical qualification, release readiness, patient benefit, or project completion.

## 12. Repository qualification

Under FD-007, independent repository review is optional by default. Before merge, verify final exact base/head/diff, exact-head corrected direct-digest replay, status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.