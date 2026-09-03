# E004 Aya GitHub Transport Bridge Founder Decision Request — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Current global frontier:** `e004-registry-current-state-reconciliation-v18-2026-09-03.md`  
**Canonical base:** `67a61b012e15557c259279e7cf2612879d3b498a`  
**Artifact class:** Founder transport-environment decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Dataset payload materialized:** NO  
**Dataset payload parsed:** NO  
**Spend:** USD 0

## 1. Purpose

Resolve the remaining execution-environment byte-materialization blocker without changing the already-authorized Aya byte subject or moving any record parsing, schema inspection, privacy screening, human inspection, candidate construction, contamination assessment, model execution, or training work to an external provider.

The current canonical route decision authorizes the public Hugging Face `main` alias only as a transport resolver after exact pin prechecks. V18 records that those prechecks pass and that the route resolves to the exact canonical Xet subject, but the current local execution environment cannot receive outbound payload bytes even when the resolved Xet endpoint IP addresses are supplied directly.

The narrowly proposed bridge would use one standard GitHub-hosted runner only to transport the exact verified bytes into a short-lived GitHub Actions artifact. The artifact would then be downloaded into the local execution environment, locally SHA-256 verified before any parsing, and deleted from GitHub Actions as soon as local materialization is confirmed or the bounded attempt terminates.

This request does not authorize the bridge. It creates only the exact post-canonical Founder decision surface required to preserve or narrowly expand the transport environment.

## 2. Existing exact Aya byte subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
DECLARED_LICENSE=Apache-2.0
```

No alternate repository, revision, file, mirror, converted parquet, derivative, test split, demographics payload, OASST1 payload, or Dolly payload is eligible under either decision class.

## 3. Existing canonical authority remains controlling

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE

FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY=AUTHORIZED_ONLY_FOR_CANONICAL_XET_AND_SHA256_SUBJECT
AYA_BYTE_SUBJECT_EXPANSION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This request does not weaken or replace either canonical Decision B. A selected bridge class would be additive and narrower than general external-provider processing.

## 4. Current blocker proven after V18

The local environment was rechecked after V18:

```text
LOCAL_HUGGINGFACE_DNS_RESOLUTION=UNAVAILABLE
LOCAL_DIRECT_HTTPS_TO_RESOLVED_XET_IPS=UNAVAILABLE
RESOLVED_XET_IP_COUNT_TESTED=11
RESOLVED_XET_HTTPS_RESULTS=HTTP_000_ALL_TESTED_ADDRESSES
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
LOCAL_PAYLOAD_BYTES_RECEIVED=0
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
```

The public source remains observable and the canonical file metadata still reports:

```text
OBSERVED_TRAIN_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
OBSERVED_TRAIN_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
OBSERVED_PUBLIC_FILE_SIZE=137_MB
```

The remaining blocker is therefore current local outbound transport, not a byte-subject mismatch and not evidence of source unavailability.

## 5. Why GitHub Actions is proposed only as a byte bridge

The repository already uses GitHub-hosted execution for bounded evidence workflows. The proposed bridge would not use a hosted runner to interpret dataset records. It would be limited to deterministic byte-transport operations:

1. repeat all mandatory Aya route prechecks;
2. download only the exact authorized public file;
3. compute SHA-256 over the downloaded bytes on the runner;
4. require equality with the canonical SHA-256 before artifact publication;
5. publish only the exact verified payload as a short-lived GitHub Actions artifact;
6. expose no record content in logs;
7. perform no Parquet parsing or schema/record inspection on the runner;
8. perform no PII/PHI screening, scope classification, candidate construction, contamination assessment, model call, or AI/provider processing on the runner;
9. download the artifact into the local execution environment;
10. compute the local SHA-256 again before any local parsing;
11. delete the remote artifact immediately after confirmed local materialization or bounded termination.

The bridge therefore separates external byte transport from the still-local-only content-processing boundary.

## 6. Decision classes

The Founder must select exactly one class after this decision surface becomes canonical.

### `E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_A` — preserve current local-only transport state

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_A
AYA_GITHUB_ACTIONS_TRANSPORT_BRIDGE_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_TRANSIENT_ARTIFACT_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_EPHEMERAL_RUNTIME_CREDENTIAL_AUTHORITY=NONE
AYA_EXTERNAL_BYTE_TRANSPORT_ENVIRONMENT_EXPANSION=NONE
```

Effect: retain V18. Execution waits for a local environment with direct outbound access to the already-authorized exact Aya subject.

### `E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B` — authorize one exact-subject GitHub transport bridge

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

Decision B would authorize only the exact bridge protocol below.

## 7. Mandatory bridge prechecks

Before the hosted runner requests payload bytes, all canonical route prechecks must pass in the same bounded run:

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

## 8. Hosted-runner byte verification

The runner may perform only byte-level integrity checks before publishing an artifact:

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

The remote SHA-256 is transport-integrity evidence only. It does not substitute for the mandatory local SHA-256 gate.

## 9. Transient GitHub Actions artifact boundary

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
```

The artifact is a transport envelope only. Its existence does not authorize later external processing.

## 10. Runtime credential boundary

Decision B would authorize only platform-generated ephemeral GitHub Actions runtime credentials required by the standard Actions artifact transport and cleanup mechanisms.

```text
GITHUB_ACTIONS_EPHEMERAL_RUNTIME_CREDENTIALS=AUTHORIZED_TRANSPORT_AND_CLEANUP_ONLY
USER_OR_FOUNDER_PERSONAL_ACCESS_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
ORGANIZATION_SECRET_USE=PROHIBITED
HUGGINGFACE_TOKEN_USE=PROHIBITED
GATED_ASSET_CREDENTIAL_USE=PROHIBITED
LONG_LIVED_CREDENTIAL_PERSISTENCE=PROHIBITED
```

No user-managed credential, secret, API key, or gated-token authority is created.

## 11. Mandatory local verification before parsing

After the Actions artifact is downloaded into the local ephemeral workspace:

```text
LOCAL_POSTTRANSPORT_SHA256_REQUIRED=YES
LOCAL_POSTTRANSPORT_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
LOCAL_PARSE_BEFORE_SHA256_MATCH=PROHIBITED
DELETE_LOCAL_PAYLOAD_ON_SHA256_MISMATCH=REQUIRED
DELETE_REMOTE_ARTIFACT_ON_LOCAL_SHA256_MISMATCH=REQUIRED
```

Only after the local SHA-256 matches may the already-canonical public-data Decision B permit local parsing and bounded candidate construction.

## 12. Existing local-only content-processing boundary remains unchanged

Even under transport bridge Decision B:

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

All exact original-human-annotation determination, re-annotation exclusion, demographics exclusion, `user_id` removal, `SP007-RO-001` scope filtering, PII/PHI risk screening, bounded human inspection, record/content identity construction, and aggregate reason-code production remain local after local SHA-256 verification.

## 13. Still non-admitting

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_THIS_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
```

Transport success cannot be represented as admission, eligibility, quarantine PASS, license PASS, or contamination PASS.

## 14. No contamination, model, A15, or training expansion

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION_FROM_THIS_DECISION=NONE
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

## 15. Protected, gated, paid, and provider-generation boundaries remain closed

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
HUGGINGFACE_CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
EXTERNAL_MODEL_OUTPUT_AS_TRAINING_DATA=PROHIBITED
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Standard GitHub-hosted runner use is eligible only if it requires no incremental spend for this public repository. If any billable incremental spend is required, the bridge aborts.

## 16. Required cleanup proof

A successful bridge is incomplete until the remote artifact cleanup is verified.

Repository-safe evidence may record only:

```text
BRIDGE_WORKFLOW_IDENTITY
BRIDGE_RUN_IDENTITY
EXACT_SOURCE_IDENTITIES
REMOTE_SHA256_RESULT
ARTIFACT_IDENTITY_AND_SIZE
LOCAL_SHA256_RESULT
REMOTE_ARTIFACT_DELETION_RESULT
LOCAL_TRANSIENT_PAYLOAD_CLEANUP_RESULT_WHEN_NO_LONGER_REQUIRED
NO_RECORD_CONTENT
NO_SIGNED_DOWNLOAD_QUERY
NO_USER_SECRET
NO_RAW_PAYLOAD_IN_CANONICAL_REPOSITORY
```

A transient signed Hugging Face URL or signed GitHub artifact URL must not be persisted in canonical evidence.

## 17. Failure conditions

Decision B must fail closed without substitution on any condition below:

```text
MAIN_HEAD_NOT_EXACT_PIN
PUBLISHED_XET_HASH_MISMATCH
PUBLISHED_SHA256_MISMATCH
ACCESS_GATED_OR_HUGGINGFACE_CREDENTIAL_REQUIRED
INCREMENTAL_SPEND_REQUIRED
NONSTANDARD_OR_BILLABLE_RUNNER_REQUIRED
REMOTE_DOWNLOADED_SHA256_MISMATCH
REMOTE_PARSE_OR_RECORD_INSPECTION_REQUIRED
REMOTE_PII_PHI_SCREENING_REQUIRED
ARTIFACT_UPLOAD_CANNOT_BE_RESTRICTED_TO_EXACT_VERIFIED_PAYLOAD
LOCAL_ARTIFACT_DOWNLOAD_UNAVAILABLE
LOCAL_SHA256_MISMATCH
REMOTE_ARTIFACT_CLEANUP_UNAVAILABLE
USER_MANAGED_CREDENTIAL_REQUIRED
```

Failure does not authorize another dataset, route, mirror, provider, credential, storage mechanism, or paid path.

## 18. E004 effect

Neither decision class completes E004.

```text
E004_COMPLETE_FROM_TRANSPORT_BRIDGE_DECISION=NO
AYA_CANDIDATE_CONSTRUCTION_COMPLETE_FROM_TRANSPORT_BRIDGE_DECISION=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

## 19. ChatGPT recommendation for Founder review

```text
CHATGPT_AYA_GITHUB_TRANSPORT_BRIDGE_POSITION=RECOMMEND_E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
RATIONALE_1=THE_EXACT_BYTE_SUBJECT_AND_HASHES_DO_NOT_CHANGE
RATIONALE_2=THE_CURRENT_LOCAL_ENVIRONMENT_HAS_PROVEN_OUTBOUND_TRANSPORT_UNAVAILABLE
RATIONALE_3=THE_HOSTED_RUNNER_PERFORMS_BYTE_TRANSPORT_AND_SHA256_ONLY_WITH_NO_RECORD_PARSE_OR_SCREENING
RATIONALE_4=THE_LOCAL_SHA256_GATE_REMAINS_MANDATORY_BEFORE_ANY_PARSE
RATIONALE_5=REMOTE_ARTIFACT_RETENTION_IS_MINIMIZED_AND_DELETION_IS_REQUIRED_AFTER_LOCAL_TRANSFER
RATIONALE_6=NO_USER_SECRET_GATED_ACCESS_MODEL_PROCESSING_ADMISSION_CONTAMINATION_A15_TRAINING_OR_SPEND_AUTHORITY_IS_CREATED
```

This recommendation is not a Founder decision.

## 20. Exact Founder response required

To preserve the current V18 local-only transport boundary:

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_A
```

To authorize the exact GitHub Actions byte-transport bridge defined by this canonical surface:

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
```

A broad continuation instruction, ordinary approval, statement that all approvals are granted, prior public-data Decision B, or prior route Decision B does not substitute for this new transport-environment decision.

The operative Founder token must occur after this decision surface becomes canonical and must be captured separately before any GitHub-hosted runner downloads or temporarily stores the Aya payload.

## 21. Current state until an operative bridge decision is canonical

```text
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=ABSENT
AYA_GITHUB_ACTIONS_TRANSPORT_BRIDGE_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_TRANSIENT_ARTIFACT_AUTHORITY=NONE
AYA_GITHUB_ACTIONS_EPHEMERAL_RUNTIME_CREDENTIAL_AUTHORITY=NONE
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
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

## 22. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision-request artifact.

Before merge, verify exact base/head/diff, correspondence to V18 and the two existing canonical Aya Decision B records, exact byte-subject preservation, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
