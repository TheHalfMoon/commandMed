# E004 Registry Current-State Reconciliation V22 — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base at branch creation:** `4f9a3b6c9d65b0ece41e2100ed3290178d3d2b84`  
**Authority source:** `FD-008` / `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the E004 global frontier after the exact Aya-135 deterministic record-evidence result was supplied to the canonical Spec 003 evaluator and produced concrete fail-closed admission states.

This record supersedes V21 only for prospective current-state interpretation. V21 and all earlier Aya source, transport, candidate-construction, contamination, Spec 003, human-boundary, deterministic-method, materialization, and cleanup records remain immutable audit history under their original identities.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v21-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v22-2026-09-04.md
FOUNDER_AMENDMENT=docs/aya-135-human-review-gate-amendment-2026-09-03.md
FD008_DECISION=REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE
AUTHORITY_EXPANSION_FROM_V22=NONE
```

An older unmerged divergent branch named `docs/e004-aya-deterministic-results-v22` is not canonical `main` history and does not govern this current-state record. This V22 is bound only to the exact current PR #225 evidence path and its qualified result identities.

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

No source, revision, file, filter, record-set, content-set, language, role, capability, or candidate expansion is created by V22.

## 3. Preserved contamination evidence

The frozen contamination result remains unchanged:

```text
CONTAMINATION_METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
ASSESSED_CLEAN=135
OVERLAP_OR_HIGH_RISK=0
CONTAMINATION_UNRESOLVED=0
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
```

`ASSESSED_CLEAN` retains only the meaning defined by that exact frozen method and universe. V22 does not broaden that claim.

## 4. Deterministic FD-008 record evidence is executed

The frozen deterministic method remains:

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

The repository-safe projection contains hashes and categorical outcomes only. It contains no Aya raw input/target text and no `user_id`.

The deterministic method does not compute admission. Caller-controlled `ELIGIBLE` remains prohibited.

## 5. Canonical Spec 003 admission result

PR #225 binds the exact deterministic projection and the preserved contamination evidence to the canonical Spec 003 evaluator.

The qualified evaluator source identities are:

```text
SPEC003_EVALUATOR_LINEAGE_GIT_BLOB=5d7a5b6a8b48b2b5a7afea35ed18ceb1c9fe6425
SPEC003_LINEAGE_CONTRACT_GIT_BLOB=692de9b32271031b0f1dd9cc6edc98bc44b580b5
SPEC003_LINEAGE_CONTRACT_CANONICAL_SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
ARTIFACT_BINDING_STATE=IMMUTABLE_REVISION_LOCATOR
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
```

The first exact-head qualification run on PR #225 used head `ecf805529d869c23f32a2abbc62cbde7f2bc7157`, Actions run `33804877840`, job `100812840521`, and produced:

```text
SPEC003_POST_FD008_RESULTS_SHA256=a6b21bd273b43f0912fbc8a0732d981fd7ebe8622a1c9a87cb1218286805818a
SPEC003_CANDIDATE_COUNT=135
SPEC003_ELIGIBLE_COUNT=43
SPEC003_BLOCKED_COUNT=92
SPEC003_VALIDATION_ERROR_COUNT=0
RIGHTS_UNRESOLVED_REASON_COUNT=92
PRIVACY_UNRESOLVED_REASON_COUNT=17
```

The pull request must reproduce the same result on its final exact head before merge. A mismatch fails closed and invalidates merge qualification for this record.

## 6. Data-admission interpretation

The evidence-dependent Aya-135 Spec 003 evaluator edge is no longer globally blocked at `0/135`.

The only records that may be described as eligible at this stage are the exact 43 candidate identities computed `ELIGIBLE` by the canonical evaluator. The other 92 remain blocked and must not be admitted by downstream callers.

```text
AYA_135_SPEC003_EVALUATION_EXECUTED=YES
AYA_135_EXACT_ELIGIBLE_RECORD_COUNT=43
AYA_135_EXACT_BLOCKED_RECORD_COUNT=92
AYA_135_VALIDATION_ERROR_COUNT=0
AYA_135_ELIGIBILITY_SOURCE=CANONICAL_SPEC003_EVALUATOR_ONLY
AYA_135_BLOCKED_RECORDS_DOWNSTREAM_ADMISSION=PROHIBITED
```

This is record-level Spec 003 eligibility evidence only. It is not a final gradient-bearing curriculum decision, DatasetSnapshot, quarantine PASS, live RunManifest, guard PASS, tournament evidence pack, backbone-winner decision, or training authorization.

## 7. Exact next dependency-safe frontier

The component dependency order remains governed by the canonical research-component policy and execution-preflight blocker packet.

The first component construction step after eligible record evidence is to freeze exact admitted gradient-bearing content with provenance, rights/license, privacy, split, verification, and contamination state. That step cannot be performed merely because 43 records are Spec 003 `ELIGIBLE`; the current global authority surface still withholds final curriculum admission and DatasetSnapshot authority.

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

Therefore the next real transition requires a separately canonical authority/evidence surface for final curriculum construction/admission before any gradient-bearing content set or DatasetSnapshot is asserted.

## 8. Preserved successor-scope execution authority

The earlier Founder successor execution Decision B remains canonical and unchanged:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
```

Those authorities remain conditional on exact PASS preflight and do not supply the missing curriculum, snapshot, scope, guard, access, finance/resource, conversion, or training prerequisites.

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

The reason E004 remains incomplete has advanced: the deterministic Aya evidence and exact Spec 003 admission computation are now complete for the fixed 135 subject, while final curriculum/DatasetSnapshot and the remaining component preflight prerequisites are still absent or unauthorized.

## 11. Explicit exclusions

V22 performs or claims no final curriculum construction/admission, DatasetSnapshot freeze, quarantine PASS, model conversion, quantization, model inference, tournament execution, live guard execution, A15 activation, training, Private Gold/PHI/gated access, credential use, external provider generation, procurement, payment, spend, clinical qualification, release readiness, patient benefit, or project completion.

## 12. Repository qualification

Under FD-007, independent repository review is optional by default. Before merge, verify the final exact base/head/diff, exact-head replay of the Spec 003 result, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.