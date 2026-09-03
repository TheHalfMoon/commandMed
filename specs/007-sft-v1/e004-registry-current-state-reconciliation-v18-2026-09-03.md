# E004 Registry Current-State Reconciliation V18 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `169db96c8b7a013f3dda20ed5f8da400dce0019d`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the global E004 current view after canonical Founder Aya route Decision B and the first bounded verified-alias materialization attempt.

This record supersedes V17 only for later current-state interpretation. Historical evidence remains immutable.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v17-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v18-2026-09-03.md
COMPONENT_POLICY_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
SUCCESSOR_EXECUTION_DECISION_RECORD=specs/007-sft-v1/e004-successor-scope-execution-authorization-founder-decision-2026-09-02.md
PUBLIC_DATA_ACCESS_DECISION_RECORD=specs/007-sft-v1/e004-public-data-payload-access-founder-decision-2026-09-03.md
AYA_ROUTE_DECISION_REQUEST=specs/007-sft-v1/e004-aya-content-addressed-access-route-founder-decision-request-2026-09-03.md
AYA_ROUTE_DECISION_RECORD=specs/007-sft-v1/e004-aya-content-addressed-access-route-founder-decision-2026-09-03.md
AYA_VERIFIED_ALIAS_ATTEMPT_RECORD=specs/007-sft-v1/e004-aya-verified-alias-materialization-attempt-2026-09-03.md
AUTHORITY_EXPANSION_FROM_V18=NONE
```

## 2. Canonical successor and public-data authority remain unchanged

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
PUBLIC_DATA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
PUBLIC_DATA_BYTE_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
PUBLIC_DATA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
PUBLIC_DATA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
PUBLIC_DATA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Exact Aya byte subject remains:

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

## 3. Founder Aya route Decision B is canonical

PR #192 / merge `169db96c8b7a013f3dda20ed5f8da400dce0019d` captured the exact post-canonical Founder response:

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY=AUTHORIZED_ONLY_FOR_CANONICAL_XET_AND_SHA256_SUBJECT
AYA_BYTE_SUBJECT_EXPANSION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The route decision changes transport only. Mutable `main` is not an identity authority and no alternate byte subject becomes eligible.

## 4. Immediate alias-route prechecks passed

The first post-decision bounded attempt rechecked the public source before requesting bytes through the `main` alias.

```text
PRECHECK_MAIN_HEAD_OBSERVED=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
PRECHECK_MAIN_HEAD_MATCH=PASS
PRECHECK_FILE_OBSERVED=data/train-00000-of-00001.parquet
PRECHECK_FILE_MATCH=PASS
PRECHECK_XET_HASH_OBSERVED=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
PRECHECK_XET_HASH_MATCH=PASS
PRECHECK_PUBLISHED_SHA256_OBSERVED=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PRECHECK_PUBLISHED_SHA256_MATCH=PASS
PRECHECK_PUBLIC_ACCESS=YES_OBSERVED
PRECHECK_GATED=NO_OBSERVED
PRECHECK_CREDENTIAL_REQUIRED=NO_OBSERVED
PRECHECK_INCREMENTAL_SPEND_REQUIRED=NO_OBSERVED
ROUTE_PRECHECK_RESULT=PASS
```

The authorized alias route then resolved to signed public Xet transport bound to the exact canonical Xet hash.

```text
AUTHORIZED_ALIAS_ROUTE_REQUESTED=YES
RESOLVED_TRANSPORT_CLASS=SIGNED_PUBLIC_XET
RESOLVED_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
RESOLVED_XET_HASH_MATCH=PASS
MUTABLE_MAIN_USED_AS_IDENTITY=NO
```

## 5. Local materialization still failed closed before bytes

The current execution environment could resolve the authorized route but could not receive the resolved payload bytes locally.

```text
MATERIALIZATION_ATTEMPT_RESULT=BLOCKED_FAIL_CLOSED
MATERIALIZATION_BLOCKER=AUTHORIZED_ROUTE_RESOLVED_BUT_LOCAL_BYTE_MATERIALIZATION_UNAVAILABLE
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
LOCAL_PAYLOAD_BYTES_RECEIVED=0
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
```

This is not a source-identity mismatch and not evidence that the pinned source is unavailable. It is a current execution-environment byte-materialization limitation after successful authorized route resolution.

No alternate route, dataset, file, revision, mirror, converted parquet, credential, paid provider, or hosted payload-processing path was substituted.

## 6. Raw/transient material cleanup is complete

```text
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTED=NO
LOCAL_WORKSPACE_FILE_COUNT_AFTER_ATTEMPT=0
LOCAL_WORKSPACE_TOTAL_BYTES_AFTER_ATTEMPT=0
LOCAL_TRANSIENT_WORKSPACE_REMOVED=YES
RAW_OR_TRANSIENT_AYA_PAYLOAD_REMAINING=NO
```

## 7. No payload-derived schema, provenance, privacy, or candidate evidence exists yet

Because no local payload bytes were materialized, the mandatory post-download SHA-256 gate could not run. Parsing therefore remained prohibited and was not performed.

```text
AYA_SCHEMA_FROM_LOCAL_PAYLOAD_INSPECTED=NO
ORIGINAL_HUMAN_ANNOTATION_FILTER_FROZEN=NO
REANNOTATION_EXCLUSION_EXECUTED=NO
DEMOGRAPHICS_EXCLUSION_EXECUTED=NO
USER_ID_REMOVAL_FROM_CANDIDATE_REPRESENTATION_EXECUTED=NO
SP007_RO_001_RECORD_SCOPE_FILTER_EXECUTED=NO
AYA_RECORD_LEVEL_SCREENING_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO
AYA_PRIVACY_SCREENING_PERFORMED=NO
AYA_HUMAN_INSPECTION_OF_RECORD_CONTENT_PERFORMED=NO
AYA_CANDIDATE_RECORD_IDENTITIES_CREATED=NO
AYA_CANDIDATE_CONTENT_IDENTITIES_CREATED=NO
```

Source-document metadata continues to be metadata evidence only and is not substituted for exact verified-payload parsing.

## 8. Data admission and contamination remain separately closed

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

## 9. Live component preflight remains blocked in dependency order

The component construction order still begins with real provenance/rights/privacy/contamination-qualified content. Because the Aya bounded candidate pass has not produced verified candidate records and admission/contamination remain separately closed, no later live component binding may be fabricated.

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

## 10. No dependency-safe later execution unit is currently reachable

The current blocker does not justify skipping to E005 or to any later component/tournament/training operation.

```text
NO_ELIGIBLE_DEPENDENCY_ORDERED_SUCCESSOR_EXECUTION_AVAILABLE=YES
E005_REACHABLE=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
```

The bounded public-data candidate-construction pass remains the earliest live evidence dependency that can advance the research component, and its next step requires actual local byte materialization of the already-authorized exact Aya subject.

## 11. Conversion, A15, model execution, and training remain closed

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

## 12. Protected, credentialed, paid, external-provider, and clinical resources remain closed

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 13. Dependency-safe next action

Decision B remains valid for the exact byte subject. A retry of the same subject does not require a new Founder route decision merely because the current local environment could not receive the bytes.

Every future retry must re-run the immediate prechecks before requesting bytes.

```text
NEXT_ACTION=MATERIALIZE_THE_ALREADY_AUTHORIZED_EXACT_AYA_XET_SUBJECT_IN_A_LOCAL_EXECUTION_ENVIRONMENT_CAPABLE_OF_RECEIVING_THE_BYTES
FIRST_REQUIRED_POSTDOWNLOAD_ACTION=COMPUTE_SHA256_BEFORE_PARSING
EXPECTED_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
NEW_FOUNDER_ROUTE_DECISION_REQUIRED_FOR_SAME_EXACT_SUBJECT=NO
```

No current canonical authority permits changing the source, revision, file, mirror, access class, privacy-processing location, credential boundary, or spend boundary to overcome the environment limitation.

## 14. Current terminal state

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
ROUTE_PRECHECK_RESULT=PASS
RESOLVED_XET_HASH_MATCH=PASS
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

## 15. Explicit exclusions

This reconciliation performs or authorizes no payload parsing, candidate admission, contamination assessment, model conversion, quantization, inference, tournament execution, A15 activation, training, reviewer outreach, protected/gated access, credential use, provider generation, procurement, payment, spend, or source substitution.

## 16. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only reconciliation.

Before merge, verify exact base/head/diff, correspondence to the canonical route decision and verified-alias attempt, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
