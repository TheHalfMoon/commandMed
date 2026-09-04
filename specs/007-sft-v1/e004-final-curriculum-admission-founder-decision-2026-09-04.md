# E004 Final Curriculum Admission Founder Decision — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision-request merge:** `9ecc4b76ccae4244e532b5ff3f2a61318647fb16`  
**Canonical base for this decision record:** `9ecc4b76ccae4244e532b5ff3f2a61318647fb16`  
**Decision owner:** Founder  
**Decision class:** `E004_FINAL_CURRICULUM_ADMISSION_DECISION_B`  
**Decision state:** SELECTED  
**Curriculum construction performed by this decision record:** NO  
**DatasetSnapshot created by this decision record:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Operative Founder decision

After the canonical decision surface was merged, the Founder supplied the exact required decision text:

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
```

This is the exact Decision B token defined by:

`specs/007-sft-v1/e004-final-curriculum-admission-founder-decision-request-2026-09-04.md`

Therefore the exact bounded curriculum authority becomes:

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
FINAL_CURRICULUM_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_SP007_RESEARCH_COMPONENT_ONLY
FINAL_CURRICULUM_SOURCE_SET=COHERELABS_AYA_EXACT_43_ONLY
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
FINAL_CURRICULUM_SPEC003_RESULT_SHA256=a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4
CURRICULUM_RECORD_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_HASH_BOUND_METADATA_ONLY
CONTENT_SCOPE_VERIFICATION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_ONLY
BLOCKED_AYA_92_DOWNSTREAM_ADMISSION=PROHIBITED
OASST1_ADMISSION_AUTHORITY=NONE
DOLLY_15K_ADMISSION_AUTHORITY=NONE
OTHER_DATASET_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. Exact admitted content identity

The authority is limited to the exact 43-record set already computed `ELIGIBLE` by the corrected canonical Spec 003 `DIRECT_DIGEST` replay:

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
SPEC003_CORRECTED_DIRECT_DIGEST_RESULTS_SHA256=a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4
SPEC003_ELIGIBLE_COUNT=43
SPEC003_BLOCKED_COUNT=92
SPEC003_VALIDATION_ERROR_COUNT=0
ELIGIBLE_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
```

Per-record content identity remains bound by the five exact candidate content-digest map parts canonicalized by PR #226. The 43 admitted record IDs are exactly the `rights_supported_candidate_ids` set in the canonical deterministic admission projection. No raw Aya text is admitted into repository source by this decision record.

## 3. Exact construction authority

Decision B authorizes only deterministic repository-safe construction for the exact 43-record subject:

- construct hash-bound `CurriculumRecord` metadata for those exact records;
- bind each record to its exact direct content digest;
- classify each admitted record as `LEARNER_RESEARCHER` and `DURABLE_WEIGHT_ELIGIBLE` only within `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`;
- bind purpose `TRAIN` and existing contamination/quarantine evidence as required by the controlling contracts;
- produce exact content-scope verification identities for those same 43 records;
- fail closed on any identity mismatch, schema failure, stale evidence, or content-scope failure.

This authority does not permit caller-selected replacement content or expansion beyond the exact 43 identities.

## 4. Blocked and non-Aya content remain excluded

```text
AYA_BLOCKED_RECORD_COUNT=92
AYA_BLOCKED_RECORD_DOWNSTREAM_ADMISSION=PROHIBITED
OPENASSISTANT_OASST1_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY
DATABRICKS_DOLLY_15K_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY_CONDITIONAL_RIGHTS
SOURCE_EXPANSION_AUTHORITY=NONE
```

No later convenience, count target, class-balance concern, or observed result may silently substitute another record or source into this exact subject.

## 5. Privacy and persistence boundary

```text
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
AYA_USER_ID_READ_OR_PERSISTENCE=PROHIBITED
REMOTE_MODEL_OR_AI_RECORD_PROCESSING_AUTHORITY_CREATED=NONE
EXTERNAL_PROVIDER_PII_PHI_SCREENING_AUTHORITY_CREATED=NONE
IDENTITY_RECONSTRUCTION=PROHIBITED
```

Only hashes, categorical evidence, contract-valid metadata, and derived immutable identities may be persisted by the newly authorized construction work unless a separately applicable canonical authority says otherwise.

## 6. DatasetSnapshot remains unauthorized

This decision intentionally stops before the next dependency-safe authority boundary:

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
```

The exact 43 CurriculumRecord and content-scope verification identities must first be constructed and validated. A later canonical authority surface may consider DatasetSnapshot and quarantine-verification freezing only after those prerequisites are evidenced.

## 7. Model, execution, and training boundaries remain unchanged

```text
MODEL_WINNER_SELECTION_AUTHORITY_EXPANSION=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The previously canonical `E004_SUCCESSOR_EXECUTION_DECISION_B` remains necessary but insufficient for later execution and remains constrained by exact PASS preflight.

## 8. E004 effect

Decision B removes only the final-curriculum authority blocker for the exact Aya-43 research-component subject and authorizes the immediately dependent deterministic construction work.

```text
FINAL_CURRICULUM_DECISION_CAPTURED=YES
EXACT_AYA_43_CURRICULUM_CONSTRUCTION_REACHABLE=YES
EXACT_AYA_43_CONTENT_SCOPE_VERIFICATION_REACHABLE=YES
DATASET_SNAPSHOT_REACHABLE=NO_PENDING_SEPARATE_AUTHORITY
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 9. Relationship to generic continuation approval

The exact Founder token above is the sole source of the new curriculum authority. Generic continuation instructions and ordinary approvals remain project intent but are not used to manufacture DatasetSnapshot, conversion, A15, training, protected-data, credential, payment, procurement, or spend authority.

## 10. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded Founder-decision capture artifact.

Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact Decision B correspondence with the canonical decision surface, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
