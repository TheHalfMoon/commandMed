# E004 Aya GitHub Transport Bridge Founder Decision — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision surface:** `specs/007-sft-v1/e004-aya-github-transport-bridge-founder-decision-request-2026-09-03.md`  
**Canonical decision-surface merge:** `6eb7a469e1555b4c511f7c49411670dadff5840c`  
**Canonical base at capture:** `6eb7a469e1555b4c511f7c49411670dadff5840c`  
**Decision owner:** Founder  
**Decision state:** SELECTED  
**Selected class:** `E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B`  
**Current authorized spend:** USD 0

## 1. Operative Founder response

The Founder supplied the exact post-canonical operative token required by the canonical transport-environment decision surface:

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
```

This record captures that exact decision and only the authority explicitly defined by the controlling decision surface. It does not infer broader authority from ordinary approvals.

## 2. Exact Aya byte subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

No alternate repository, revision, file, mirror, converted parquet, derivative, test split, demographics payload, OASST1 payload, or Dolly payload is authorized by this decision.

## 3. Authority created by Decision B

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
AYA_GITHUB_ACTIONS_TRANSPORT_BRIDGE_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_SUBJECT_BYTE_TRANSPORT_ONLY
AYA_GITHUB_ACTIONS_TRANSIENT_ARTIFACT_AUTHORITY=AUTHORIZED_EXACT_VERIFIED_PAYLOAD_MINIMUM_RETENTION_ONLY
AYA_GITHUB_ACTIONS_EPHEMERAL_RUNTIME_CREDENTIAL_AUTHORITY=AUTHORIZED_PLATFORM_RUNTIME_ONLY_FOR_ARTIFACT_TRANSPORT_AND_CLEANUP
AYA_GITHUB_ACTIONS_USER_SECRET_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_REMOTE_PARSE_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_REMOTE_SCHEMA_INSPECTION_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_REMOTE_RECORD_INSPECTION_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_REMOTE_PII_PHI_SCREENING_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_REMOTE_CANDIDATE_CONSTRUCTION_AUTHORITY=NONE
AYA_BYTE_SUBJECT_EXPANSION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The hosted runner is a deterministic byte-transport bridge only. It is not an authorized content-processing environment.

## 4. Mandatory bridge prechecks

Before any hosted runner requests payload bytes, all controlling route checks must pass in the same bounded run:

```text
PRECHECK_REPOSITORY=CohereLabs/aya_dataset
PRECHECK_MAIN_HEAD_MUST_EQUAL=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
PRECHECK_FILE_MUST_EQUAL=data/train-00000-of-00001.parquet
PRECHECK_XET_HASH_MUST_EQUAL=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
PRECHECK_PUBLISHED_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PRECHECK_PUBLIC_ACCESS_MUST_EQUAL=YES
PRECHECK_GATED_MUST_EQUAL=NO
PRECHECK_USER_CREDENTIAL_REQUIRED_MUST_EQUAL=NO
PRECHECK_INCREMENTAL_SPEND_REQUIRED_MUST_EQUAL=NO
PRECHECK_REPOSITORY_VISIBILITY_MUST_EQUAL=PUBLIC
PRECHECK_RUNNER_CLASS_MUST_EQUAL=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
```

Any mismatch aborts before payload download.

## 5. Hosted-runner byte-verification boundary

The runner may perform only deterministic route checks, byte download, SHA-256 verification, transient artifact publication, and cleanup operations required by the canonical surface.

```text
REMOTE_SHA256_REQUIRED=YES
REMOTE_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
REMOTE_PARSE_BEFORE_SHA256_MATCH=PROHIBITED
REMOTE_PARSE_AFTER_SHA256_MATCH=PROHIBITED
REMOTE_RECORD_CONTENT_LOGGING=PROHIBITED
REMOTE_SCHEMA_READ=PROHIBITED
REMOTE_CONTENT_CLASSIFICATION=PROHIBITED
DELETE_LOCAL_RUNNER_PAYLOAD_ON_SHA256_MISMATCH=REQUIRED
PUBLISH_ARTIFACT_ON_SHA256_MISMATCH=PROHIBITED
```

A remote SHA-256 match is transport-integrity evidence only.

## 6. Transient artifact and runtime credential boundary

If and only if the remote SHA-256 matches:

```text
ARTIFACT_CONTENT=EXACT_VERIFIED_AYA_PAYLOAD_ONLY
ARTIFACT_NAME=E004_AYA_EXACT_PAYLOAD_TRANSPORT_BRIDGE
ARTIFACT_RETENTION_DAYS_MAX=1
ARTIFACT_CANONICAL_REPOSITORY_PERSISTENCE=PROHIBITED
ARTIFACT_RELEASE_ASSET_PERSISTENCE=PROHIBITED
ARTIFACT_CACHE_PERSISTENCE=PROHIBITED
ARTIFACT_PUBLICATION_OUTSIDE_GITHUB_ACTIONS=PROHIBITED
ARTIFACT_RECORD_CONTENT_LOGGING=PROHIBITED
ARTIFACT_DELETE_AFTER_CONFIRMED_LOCAL_MATERIALIZATION=REQUIRED
ARTIFACT_DELETE_AFTER_BOUNDED_FAILURE=REQUIRED

GITHUB_ACTIONS_EPHEMERAL_RUNTIME_CREDENTIALS=AUTHORIZED_TRANSPORT_AND_CLEANUP_ONLY
USER_OR_FOUNDER_PERSONAL_ACCESS_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
ORGANIZATION_SECRET_USE=PROHIBITED
HUGGINGFACE_TOKEN_USE=PROHIBITED
GATED_ASSET_CREDENTIAL_USE=PROHIBITED
LONG_LIVED_CREDENTIAL_PERSISTENCE=PROHIBITED
```

## 7. Mandatory local verification before parsing

After the artifact is downloaded into the local ephemeral workspace:

```text
LOCAL_POSTTRANSPORT_SHA256_REQUIRED=YES
LOCAL_POSTTRANSPORT_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
LOCAL_PARSE_BEFORE_SHA256_MATCH=PROHIBITED
DELETE_LOCAL_PAYLOAD_ON_SHA256_MISMATCH=REQUIRED
DELETE_REMOTE_ARTIFACT_ON_LOCAL_SHA256_MISMATCH=REQUIRED
```

Only after exact local SHA-256 equality may the already-canonical public-data Decision B permit local parsing and bounded `SP007-RO-001` candidate construction.

## 8. Existing local-only content-processing boundary remains controlling

```text
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
REMOTE_SCHEMA_INSPECTION=PROHIBITED
REMOTE_RECORD_INSPECTION=PROHIBITED
REMOTE_SCOPE_CLASSIFICATION=PROHIBITED
REMOTE_CANDIDATE_CONSTRUCTION=PROHIBITED
REMOTE_HUMAN_INSPECTION=PROHIBITED
REMOTE_MODEL_OR_AI_PROCESSING=PROHIBITED
```

After local byte verification, the bounded local pass may only perform the work already allowed by the canonical public-data Decision B: exact schema/source inspection, original-human semantics determination, re-annotation and demographics exclusion, `user_id` removal from candidate representation, `SP007-RO-001` scope filtering, deterministic local PII/PHI risk screening, bounded human inspection, immutable candidate identity construction, aggregate reason-coded evidence, and repository-safe lineage. Raw payload remains outside canonical repository source.

## 9. Authorities that remain closed

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_THIS_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
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
HUGGINGFACE_CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. Fail-closed conditions

Execution aborts without substitution on any controlling failure, including identity mismatch, gated or credentialed access, incremental spend, nonstandard or billable runner requirements, remote SHA mismatch, required remote parsing or screening, artifact transport failure, local SHA mismatch, cleanup failure, or a requirement for user-managed credentials.

Failure does not authorize another dataset, route, mirror, provider, credential, storage mechanism, or paid path.

## 11. E004 effect

This decision removes only the transport-environment authority blocker defined by the canonical surface.

```text
E004_COMPLETE_FROM_TRANSPORT_BRIDGE_DECISION=NO
AYA_CANDIDATE_CONSTRUCTION_COMPLETE_FROM_TRANSPORT_BRIDGE_DECISION=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

## 12. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision capture.

Before merge, verify exact base/head/diff, exact correspondence to the canonical transport-bridge decision surface and Founder token, applicable status/CI checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
