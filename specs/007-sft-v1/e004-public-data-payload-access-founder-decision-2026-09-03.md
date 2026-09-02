# E004 Public Data Payload Access Founder Decision — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision surface:** `specs/007-sft-v1/e004-public-data-payload-access-candidate-construction-decision-request-2026-09-02.md`  
**Canonical base at capture:** `c0b2b1ef649c75c254475fa3ea4ef184cb746ad7`  
**Decision owner:** Founder  
**Decision state:** SELECTED  
**Selected class:** `E004_PUBLIC_DATA_ACCESS_DECISION_B`  
**Current authorized spend:** USD 0

## 1. Operative Founder response

The Founder supplied the exact post-canonical operative token required by the canonical decision surface:

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
```

This record captures that exact decision and only the authority explicitly defined by the controlling decision surface.

## 2. Exact authorized Aya subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
DECLARED_LICENSE=Apache-2.0
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
```

No mutable `main`, latest revision, alternate Aya file, demographics configuration, mirror, derivative, OASST1 payload, Dolly payload, or substitute source is authorized by this decision.

## 3. Authority created by Decision B

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 4. Permitted execution

After this decision record becomes canonical, the bounded execution may:

1. download or materialize only the exact pinned Aya parquet identified above;
2. compute SHA-256 before parsing and require exact equality with the canonical expected hash;
3. abort and delete the payload on hash mismatch;
4. inspect the pinned schema and source metadata needed to establish exact original-human-annotation semantics;
5. retain only original-human-annotation records whose origin is established from the exact pinned evidence;
6. exclude re-annotations and unresolved human-origin records fail closed;
7. exclude demographics data and prohibit `user_id` from candidate training representation;
8. enforce `SP007-RO-001` non-clinical learner/researcher scope and exclude positive patient/caregiver or clinical-professional capability content;
9. perform local deterministic PII/PHI risk screening and bounded human inspection without sending record content to an external model, provider, or API;
10. compute immutable candidate record/content identities and aggregate inclusion/exclusion counts with reason codes;
11. produce repository-safe candidate lineage and execution evidence while preserving unresolved admission dimensions;
12. keep raw payload bytes and transient sensitive inspection material outside canonical repository source and remove them when no longer required by the bounded pass.

## 5. Decision B remains non-admitting

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_THIS_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
```

No result of this pass may be represented as admitted, `ELIGIBLE`, quarantine-passed, license-compatible for admission, or contamination-passed unless a later separately authorized evaluator path proves that state.

## 6. Contamination remains separately blocked

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
```

## 7. No model, conversion, A15, or training expansion

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
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

## 8. Protected, credentialed, paid, and external-provider boundaries

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The pass must abort rather than request credentials, accept new gated terms, use a paid provider, or incur incremental spend.

## 9. Fail-closed conditions

Execution must stop without substitution if any of the following occurs:

```text
DOWNLOADED_SHA256_MISMATCH
PINNED_SOURCE_UNAVAILABLE
ACCESS_BECOMES_GATED_OR_CREDENTIAL_REQUIRED
INCREMENTAL_SPEND_REQUIRED
SCHEMA_AMBIGUITY_UNRESOLVED
ORIGINAL_HUMAN_ORIGIN_NOT_ESTABLISHED
REANNOTATION_EXCLUSION_NOT_PROVABLE
PRIVACY_RISK_NOT_RESOLVABLE_WITHIN_AUTHORIZED_LOCAL_SCREENING
REQUIRED_EXTERNAL_PROVIDER_USE
SCOPE_CLASSIFICATION_NOT_DETERMINISTICALLY_ENFORCEABLE
```

Failure does not authorize switching to another dataset, revision, file, mirror, or access route.

## 10. E004 effect

This Founder decision removes only the exact Aya public-data payload-access/candidate-construction authority blocker.

```text
E004_COMPLETE_FROM_THIS_DECISION=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

E004 remains incomplete until the separately required evidence, admission, contamination, preflight, tournament, and other canonical gates are satisfied.

## 11. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision capture.

Before merge, verify exact base/head/diff, correspondence to the canonical decision surface, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
