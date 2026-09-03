# E004 Aya 135-Candidate Qualification and Admission Founder Decision — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision surface:** `specs/007-sft-v1/e004-aya-135-candidate-qualification-admission-founder-decision-request-2026-09-03.md`  
**Canonical decision-surface merge:** `a4e15139953316595e2c138b268e403097ce189f`  
**Canonical base at capture:** `a4e15139953316595e2c138b268e403097ce189f`  
**Decision owner:** Founder  
**Decision state:** SELECTED  
**Selected class:** `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B`  
**Current authorized spend:** USD 0

## 1. Operative Founder response

The Founder supplied the exact post-canonical operative token required by the canonical decision surface:

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B
```

This record captures that exact decision only. It does not infer broader authority from ordinary approvals or any earlier Founder decision.

## 2. Exact fixed subject

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

No source, revision, file, filter, candidate count, language lane, capability scope, or candidate identity expansion is authorized.

## 3. Authority created by Decision B

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B
AYA_135_QUALIFICATION_EVIDENCE_AUTHORITY=AUTHORIZED_EXACT_FIXED_IDENTITY_SET_ONLY
AYA_135_EXACT_REPLAY_AUTHORITY=AUTHORIZED_SAME_EXACT_SOURCE_AND_FILTER_ONLY
AYA_135_RIGHTS_EVIDENCE_EVALUATION_AUTHORITY=AUTHORIZED_EVIDENCE_ONLY_NOT_LEGAL_ADVICE
AYA_135_PRIVACY_EVIDENCE_EVALUATION_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_ONLY_NO_EXTERNAL_PROVIDER
AYA_135_SPLIT_QUARANTINE_EVIDENCE_AUTHORITY=AUTHORIZED_EXACT_TRAINING_CANDIDATE_SET_ONLY
AYA_135_RECORD_SCOPE_VERIFICATION_AUTHORITY=AUTHORIZED_SP007_RO_001_ONLY
AYA_135_CURRICULUM_CONTAMINATION_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_FIXED_CANDIDATE_SET_ONLY
DATA_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_135_SPEC003_EVALUATOR_ONLY
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Founder authorization is not itself an admission PASS. A record can become `ELIGIBLE` only if the canonical Spec 003 evaluator computes that disposition from complete evidence for the exact declared use.

## 4. Replay and content-processing boundary

The existing canonical Aya route and GitHub transport decisions remain controlling for any same-subject replay. Exact remote prechecks, remote SHA-256 verification, transient-artifact rules, local SHA-256-before-parse, and cleanup remain mandatory.

```text
REPLAY_SOURCE_SHA256_MATCH=REQUIRED
REPLAY_SOURCE_XET_HASH_MATCH=REQUIRED
REPLAY_FILTER_ID_MATCH=REQUIRED
REPLAY_CANDIDATE_COUNT_MUST_EQUAL=135
REPLAY_MANIFEST_SHA256_MUST_EQUAL=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
REPLAY_RECORD_ID_SET_SHA256_MUST_EQUAL=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
REPLAY_CONTENT_SHA256_SET_SHA256_MUST_EQUAL=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
REMOTE_RECORD_INSPECTION=PROHIBITED
REMOTE_MODEL_OR_AI_RECORD_PROCESSING=PROHIBITED
USER_ID_READ_FOR_QUALIFICATION=PROHIBITED
USER_ID_PERSISTENCE=PROHIBITED
```

Any mismatch or requirement for a prohibited processing route aborts without substitution or widening.

## 5. Qualification and admission semantics

The bounded pass may gather and evaluate rights/license, privacy, training split/quarantine, `SP007-RO-001` scope, and curriculum-specific contamination evidence for the exact fixed set only.

```text
DECLARED_USE=TRAINING_OR_ADAPTATION
PURPOSE=TRAIN
ORIGIN_TYPE=ORIGINAL
REQUIRED_ROLE_CLASS=LEARNER_RESEARCHER
SPEC003_EVALUATOR_REQUIRED=YES
CALLER_CONTROLLED_ADMISSION_STATE=PROHIBITED
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
CONTAMINATION_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
PRIVATE_GOLD_AS_TRAINING_SOURCE=PROHIBITED
PUBLIC_EXTERNAL_EVAL_AS_TRAINING_SOURCE=PROHIBITED
TOURNAMENT_A11_REPURPOSED=NO
```

The curriculum-specific contamination assessment must use an exact predeclared, non-protected comparison universe bound before assessment. Private Gold, PHI, gated or credentialed assets, paid providers, external semantic judges, and model inference remain prohibited.

## 6. Repository persistence boundary

Repository-safe evidence may include hashes, aggregate dispositions, evaluator records without raw personal content, and evidence/method identities. Raw Aya payload bytes, raw record text, `user_id`, transient human-inspection material, credentials, and protected evaluation payloads must not be committed.

## 7. Authorities that remain closed

```text
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
TOURNAMENT_A11_AUTHORITY_EXPANSION=NONE
MODEL_WINNER_SELECTION_AUTHORITY_EXPANSION=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
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
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. E004 effect

```text
E004_COMPLETE_FROM_AYA_135_DECISION_B=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

The decision authorizes only the bounded exact-set qualification/evaluator path. Later dependency-ordered work remains separately governed.

## 9. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision capture. Before merge, verify exact base/head/diff, exact correspondence to the canonical decision surface and Founder token, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
