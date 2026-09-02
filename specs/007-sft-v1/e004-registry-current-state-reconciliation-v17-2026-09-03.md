# E004 Registry Current-State Reconciliation V17 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `34c89dc710eeaeb1952d76f65c55e30b2eb9462a`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the global E004 current view after canonical Founder public-data access Decision B and the first bounded exact-payload materialization attempt.

This record supersedes V16 only for later current-state interpretation. Historical evidence remains immutable.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v16-2026-09-02.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v17-2026-09-03.md
COMPONENT_POLICY_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
SUCCESSOR_EXECUTION_DECISION_RECORD=specs/007-sft-v1/e004-successor-scope-execution-authorization-founder-decision-2026-09-02.md
PUBLIC_DATA_ACCESS_DECISION_REQUEST=specs/007-sft-v1/e004-public-data-payload-access-candidate-construction-decision-request-2026-09-02.md
PUBLIC_DATA_ACCESS_DECISION_RECORD=specs/007-sft-v1/e004-public-data-payload-access-founder-decision-2026-09-03.md
PUBLIC_DATA_MATERIALIZATION_ATTEMPT_RECORD=specs/007-sft-v1/e004-aya-exact-payload-materialization-attempt-2026-09-03.md
AUTHORITY_EXPANSION_FROM_V17=NONE
```

## 2. Successor execution authority remains canonical

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 3. Founder public-data access Decision B is canonical

PR #189 / merge `34c89dc710eeaeb1952d76f65c55e30b2eb9462a` captured the exact post-canonical Founder response:

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
```

The resulting bounded authority is:

```text
PUBLIC_DATA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
PUBLIC_DATA_BYTE_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
PUBLIC_DATA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
PUBLIC_DATA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
PUBLIC_DATA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Exact subject:

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

Decision B does not authorize a mutable source alias, alternate file/path/revision, mirror, derivative, OASST1, or Dolly substitution.

## 4. First materialization attempt failed closed at the execution environment boundary

The exact immutable payload route was attempted after Decision B became canonical. The current execution environment could not materialize the exact authorized binary route without substituting an unauthorized path.

The source itself remains publicly observable at metadata/source-document level; no source-side unavailability is asserted.

```text
MATERIALIZATION_ATTEMPT_RESULT=BLOCKED_FAIL_CLOSED
MATERIALIZATION_BLOCKER=EXACT_PIN_MATERIALIZATION_BLOCKED_BY_EXECUTION_ENVIRONMENT
MUTABLE_MAIN_PAYLOAD_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
REFS_CONVERT_PARQUET_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
MIRROR_OR_DERIVATIVE_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
ALTERNATE_SOURCE_SUBSTITUTION=REJECTED_NOT_AUTHORIZED
```

No payload-derived PASS is inferred from public metadata correspondence.

## 5. Exact Aya execution state

```text
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
AYA_SCHEMA_FROM_LOCAL_PAYLOAD_INSPECTED=NO
AYA_RECORD_LEVEL_SCREENING_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO
AYA_PRIVACY_SCREENING_PERFORMED=NO
AYA_HUMAN_INSPECTION_OF_RECORD_CONTENT_PERFORMED=NO
AYA_CANDIDATE_RECORD_IDENTITIES_CREATED=NO
AYA_CANDIDATE_CONTENT_IDENTITIES_CREATED=NO
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTED=NO
```

The expected SHA-256 is canonical identity evidence only until local bytes are materialized and hashed.

## 6. Metadata-only source semantics do not substitute for local payload inspection

Public source documentation identifies the relevant source fields and the distinction between original annotations and re-annotations. That evidence can guide the later exact-byte pass but cannot be promoted into record-level execution evidence.

```text
ORIGINAL_HUMAN_ANNOTATION_FILTER_FROZEN=NO
REANNOTATION_EXCLUSION_EXECUTED=NO
DEMOGRAPHICS_EXCLUSION_EXECUTED=NO
USER_ID_REMOVAL_FROM_CANDIDATE_REPRESENTATION_EXECUTED=NO
SP007_RO_001_RECORD_SCOPE_FILTER_EXECUTED=NO
```

## 7. Data admission and contamination remain separately blocked

Decision B is explicitly non-admitting and created no contamination authority.

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
CURRICULUM_RECORD_SET_PRESENT=NO
PRIVACY_PII_PHI_SCREENING_EVIDENCE=ABSENT_PAYLOAD_NOT_SCREENED
LICENSE_ADMISSION_PASS=NO
QUARANTINE_PASS=NO
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
```

## 8. Live component preflight remains blocked

```text
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
LIVE_COMPONENT_BASE_CHECKPOINT_BINDING=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT
LIVE_COMPONENT_LICENSE_PASS_BINDING=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
LIVE_COMPONENT_RESOURCE_FINANCE_BINDINGS=INCOMPLETE
LIVE_COMPONENT_ACCESS_BINDINGS=INCOMPLETE
BASE_PREFLIGHT_ALLOWED=NO
COMPONENT_PREFLIGHT_ALLOWED=NO
```

Decision B removed the public-data access authority blocker only. It did not manufacture any live preflight binding.

## 9. Conversion, A15, and training remain blocked

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
A1_A14_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

## 10. Protected, credentialed, paid, and clinical/system resources remain blocked

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

## 11. Dependency-safe next action

The current Decision B authority remains valid for the exact pinned Aya subject. A retry does not require a new Founder decision if an execution environment becomes available that can materialize that exact immutable subject under the existing zero-spend/no-credential boundary.

The next payload-derived action is therefore:

```text
NEXT_ACTION=MATERIALIZE_EXACT_AUTHORIZED_AYA_IMMUTABLE_SUBJECT_IN_CAPABLE_EXECUTION_ENVIRONMENT
FIRST_REQUIRED_PAYLOAD_CHECK=COMPUTE_SHA256_BEFORE_PARSING
EXPECTED_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
```

A widening to mutable `main`, an alternate path/revision/file, mirror, derivative, or another source is not implied and would require separately canonical authority.

## 12. Current terminal state

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
PUBLIC_DATA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO
DATA_ADMISSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

## 13. Explicit exclusions

This reconciliation performs or authorizes no alternate-path payload materialization, data admission, contamination assessment, model conversion, inference, tournament execution, A15 activation, training, reviewer outreach, protected/gated access, credential use, provider generation, procurement, payment, or spend.

## 14. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only reconciliation.

Before merge, verify exact base/head/diff, correspondence to Decision B and the execution-attempt record, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
