# E004 Aya Content-Addressed Access Route Founder Decision — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision surface:** `specs/007-sft-v1/e004-aya-content-addressed-access-route-founder-decision-request-2026-09-03.md`  
**Canonical decision-surface merge:** `fabdc289ca7391c0aed1a90d7a1ff05215e3233c`  
**Canonical base at capture:** `fabdc289ca7391c0aed1a90d7a1ff05215e3233c`  
**Decision owner:** Founder  
**Decision state:** SELECTED  
**Selected class:** `E004_AYA_ACCESS_ROUTE_DECISION_B`  
**Current authorized spend:** USD 0

## 1. Operative Founder response

The Founder supplied the exact post-canonical operative token required by the canonical route-decision surface:

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
```

This record captures that exact decision and only the authority explicitly defined by the controlling decision surface. It does not infer broader authority from ordinary approvals or from the prior public-data decision.

## 2. Exact Aya byte subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

Decision B changes transport resolution only. It does not authorize another repository, revision, file, dataset, mirror, derivative, or alternate parquet path.

## 3. Authority created by Decision B

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY=AUTHORIZED_ONLY_FOR_CANONICAL_XET_AND_SHA256_SUBJECT
AYA_BYTE_SUBJECT_EXPANSION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The public `main` alias may be used only as a transport resolver for the already-authorized exact byte subject and only after all mandatory pre-download checks pass in the same bounded attempt.

## 4. Mandatory pre-download checks

Before requesting payload bytes through the public `main` alias, require exact equality for every controlling identity and access property:

```text
PRECHECK_REPOSITORY=CohereLabs/aya_dataset
PRECHECK_MAIN_HEAD_MUST_EQUAL=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
PRECHECK_FILE_MUST_EQUAL=data/train-00000-of-00001.parquet
PRECHECK_XET_HASH_MUST_EQUAL=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
PRECHECK_PUBLISHED_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PRECHECK_PUBLIC_ACCESS_MUST_EQUAL=YES
PRECHECK_GATED_MUST_EQUAL=NO
PRECHECK_CREDENTIAL_REQUIRED_MUST_EQUAL=NO
PRECHECK_INCREMENTAL_SPEND_REQUIRED_MUST_EQUAL=NO
```

Any mismatch aborts before download. The alias must not follow a moved `main` to a new identity.

## 5. Mandatory post-download byte verification

Downloaded bytes remain untrusted until their local SHA-256 is computed and exactly matches the canonical expected hash.

```text
POSTDOWNLOAD_SHA256_REQUIRED=YES
POSTDOWNLOAD_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PARSE_BEFORE_POSTDOWNLOAD_SHA256_MATCH=PROHIBITED
DELETE_ON_SHA256_MISMATCH=REQUIRED
```

A SHA-256 match proves only exact byte identity. It does not create admission, quarantine, license-compatibility, contamination, model, A15, or training authority.

## 6. Existing public-data Decision B remains controlling after byte verification

The previously canonical Founder decision remains unchanged:

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

After exact payload bytes are successfully verified, the bounded pass may only:

1. inspect the exact pinned schema and source metadata;
2. establish exact original-human-annotation semantics from pinned evidence;
3. include only records whose original human origin is established;
4. exclude re-annotations;
5. exclude unresolved human-origin records fail closed;
6. exclude demographics;
7. prohibit `user_id` from candidate training representation;
8. enforce `SP007-RO-001` non-clinical learner/researcher scope;
9. exclude positive patient/caregiver and clinical-professional capability content;
10. perform local deterministic PII/PHI risk screening and bounded human inspection only;
11. send no record content to any external model, AI provider, or API;
12. compute immutable candidate record/content identities;
13. aggregate deterministic inclusion/exclusion counts and reason codes;
14. produce repository-safe lineage/evidence only;
15. persist no raw Aya payload in canonical repository source;
16. remove raw/transient sensitive material when the bounded pass no longer requires it.

## 7. Authorities that remain closed

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_PUBLIC_DATA_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_PUBLIC_DATA_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_PUBLIC_DATA_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_PUBLIC_DATA_DECISION=NONE
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
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Fail-closed transport conditions

Execution must abort without substitution if any of the following occurs:

```text
MAIN_HEAD_NOT_EXACT_PIN
PUBLISHED_XET_HASH_MISMATCH
PUBLISHED_SHA256_MISMATCH
ACCESS_GATED_OR_CREDENTIAL_REQUIRED
INCREMENTAL_SPEND_REQUIRED
DOWNLOAD_REDIRECT_CANNOT_BE_BOUND_TO_AUTHORIZED_ROUTE
DOWNLOADED_SHA256_MISMATCH
```

Failure does not authorize another route, file, revision, dataset, mirror, credential, provider, or paid path.

## 9. E004 effect

This decision removes only the route-authority blocker defined by the canonical decision surface.

```text
E004_COMPLETE_FROM_ROUTE_DECISION=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

E004 remains incomplete until separately required evidence and later canonical gates are actually satisfied.

## 10. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision capture.

Before merge, verify exact base/head/diff, exact correspondence to the canonical route-decision surface and Founder token, applicable status/CI checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
