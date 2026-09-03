# E004 Final Curriculum Admission Founder Decision Request — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Current global frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v22-2026-09-04.md`  
**Canonical base:** `dbee3cc1b52915362c509adfefebee88dae4a5fa`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Curriculum admission performed:** NO  
**DatasetSnapshot created:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve the earliest dependency-safe authority gap after corrected V22: whether the exact 43 Aya records already computed `ELIGIBLE` by the canonical Spec 003 `DIRECT_DIGEST` evaluator may become the complete admitted gradient-bearing content set for the current bounded research-engineering component subject.

This surface does not itself admit any record and creates no DatasetSnapshot, model winner, conversion, A15 activation, model execution, training, credential, procurement, payment, or spend authority.

## 2. Exact qualified Aya subject

Any Decision B is limited to the already-qualified exact subject:

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

The 43-record identity is the canonical `rights_supported_candidate_ids` set from the verified deterministic projection. The corrected Spec 003 result has exactly 92 blocked records, equal to the 92 `RIGHTS_UNRESOLVED` records; the 17 privacy-unresolved records are contained inside that blocked set. Therefore the exact 43 `ELIGIBLE` records are the exact `rights_supported_candidate_ids` set above.

Per-record content identity remains bound by the five exact content-digest map parts already canonicalized by PR #226 and by the corrected `DIRECT_DIGEST` replay. No raw Aya text is persisted by this decision surface.

## 3. Decision classes

### `E004_FINAL_CURRICULUM_ADMISSION_DECISION_A` — preserve current state

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_A
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
CURRICULUM_RECORD_CONSTRUCTION_AUTHORITY=NONE
CONTENT_SCOPE_VERIFICATION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
```

Effect: the exact 43 records remain Spec 003 eligible evidence only and do not become the final admitted gradient-bearing set.

### `E004_FINAL_CURRICULUM_ADMISSION_DECISION_B` — authorize the exact Aya-43 research-component curriculum

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

Decision B makes the exact Aya-43 set the complete admitted gradient-bearing content set for the current `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1` subject only. It does not define or admit a broader full-role Spec 007 curriculum and does not authorize later addition, substitution, or expansion of records or sources.

Decision B also permits deterministic repository-safe `CurriculumRecord` metadata construction and exact content-scope verification for those same 43 records only. It does not authorize raw Aya text persistence in canonical source.

## 4. Exact content boundary

Decision B does not permit caller-selected content.

Every admitted record must satisfy all of the following simultaneously:

```text
RECORD_ID_MEMBER_OF_EXACT_43_SET=YES
DIRECT_DIGEST_CONTENT_BINDING_REQUIRED=YES
SPEC003_STATE_MUST_EQUAL=ELIGIBLE
ROLE_CLASS=LEARNER_RESEARCHER
KNOWLEDGE_PLACEMENT=DURABLE_WEIGHT_ELIGIBLE
PURPOSE=TRAIN
CONTAMINATION_STATE=ASSESSED_CLEAN
QUARANTINE_POLICY_BINDING_REQUIRED=YES
CONTENT_SCOPE_VERIFICATION_REQUIRED=YES
```

Any identity mismatch, missing digest, invalid CurriculumRecord, content-scope failure, or stale/mismatched evidence excludes the affected record fail closed. Decision B does not authorize replacement records.

## 5. Other public-data candidates remain research-only

Earlier public research ranked Aya first, OASST1 second, and Dolly 15k third. Only Aya has completed the exact qualification/admission path now bound by V22.

Decision B therefore creates no authority to download, filter, qualify, admit, or use OASST1, Dolly 15k, or another source as gradient-bearing content.

```text
OPENASSISTANT_OASST1_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY
DATABRICKS_DOLLY_15K_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY_CONDITIONAL_RIGHTS
SOURCE_EXPANSION_FROM_DECISION_B=PROHIBITED
```

A future source expansion requires a separate canonical authority and its own evidence path; it cannot mutate this exact component subject after results are observed.

## 6. Privacy and repository persistence boundary

This decision surface contains only repository-safe hashes, categorical state, and authority metadata.

```text
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
AYA_USER_ID_READ_OR_PERSISTENCE=PROHIBITED
REMOTE_MODEL_OR_AI_RECORD_PROCESSING_AUTHORITY_CREATED=NONE
EXTERNAL_PROVIDER_PII_PHI_SCREENING_AUTHORITY_CREATED=NONE
IDENTITY_RECONSTRUCTION=PROHIBITED
```

If exact source bytes must later be rematerialized for an already-authorized local operation, all applicable existing exact-byte transport, SHA-256 verification, privacy, transient-retention, and cleanup boundaries remain mandatory. This decision does not widen those authorities.

## 7. DatasetSnapshot remains a later dependency

The canonical component construction order requires exact content-scope verification identities after admitted content and before the DatasetSnapshot.

Decision B therefore intentionally leaves:

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
```

Only after all exact 43 CurriculumRecord and content-scope verification identities are valid and canonical may a later authority surface consider freezing the DatasetSnapshot and quarantine verification identity.

## 8. Model, execution, and training boundaries remain unchanged

The previously canonical `E004_SUCCESSOR_EXECUTION_DECISION_B` remains applicable only after exact PASS preflight. This decision does not make preflight PASS and does not create a runnable component subject.

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

## 9. E004 effect

Even successful Decision B capture cannot complete E004 by itself.

```text
E004_COMPLETE_FROM_FINAL_CURRICULUM_DECISION_B=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

Decision B only opens the first dependency-safe construction step and the immediately dependent deterministic content-scope verification step.

## 10. Exact Founder response required

To preserve current state:

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_A
```

To authorize the exact Aya-43 bounded component curriculum:

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
```

A broad continuation instruction, generic approval, statement that all ordinary approvals are granted, PR merge, or an earlier Founder token is not substituted for this exact decision.

The operative Founder response must occur after this decision surface is canonical and must be captured in a separate decision record before newly authorized curriculum construction/admission work is executed.

## 11. Current state until an operative decision is canonical

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=ABSENT
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
CURRICULUM_RECORD_CONSTRUCTION_AUTHORITY=NONE
CONTENT_SCOPE_VERIFICATION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 12. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded decision-request artifact. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact V22 evidence identities, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
