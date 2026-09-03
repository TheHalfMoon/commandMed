# E004 Registry Current-State Reconciliation V21 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base at branch creation:** `5cf54f7e1d7a9407d4240a6050dcea345cdef748`  
**Authority source:** `FD-008` / `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the E004 frontier after the Founder explicitly removed mandatory local human inspection as the evidence mechanism for the exact fixed Aya 135 qualification line.

This record supersedes V20 only for prospective current-state interpretation. V20 and all earlier Aya transport, candidate construction, contamination, Spec 003, human-boundary, and cleanup records remain valid audit history under their original identities.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v20-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v21-2026-09-03.md
FOUNDER_AMENDMENT=docs/aya-135-human-review-gate-amendment-2026-09-03.md
FD008_DECISION=REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE
AUTHORITY_EXPANSION_FROM_V21=EXACT_AYA_135_DETERMINISTIC_RECORD_EVIDENCE_ONLY
```

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

No source, revision, file, filter, record-set, content-set, language, role, or capability expansion is authorized.

## 3. Preserved completed evidence

The frozen contamination method and universe remain complete and unchanged:

```text
METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
ASSESSED_CLEAN=135
OVERLAP_OR_HIGH_RISK=0
CONTAMINATION_UNRESOLVED=0
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
```

The canonical post-contamination Spec 003 evaluation also remains unchanged:

```text
SPEC003_CANDIDATE_COUNT=135
SPEC003_ELIGIBLE_COUNT=0
SPEC003_BLOCKED_COUNT=135
SPEC003_VALIDATION_ERROR_COUNT=0
RIGHTS_UNRESOLVED=135
PRIVACY_UNRESOLVED=135
SPEC003_POST_CONTAMINATION_RESULTS_SHA256=19e6c10fcf9667ec0d8074c3e8dac70f96c085db364a9909fd94ed9d5002c876
```

Removing mandatory human review does not retroactively modify those results.

## 4. Human review is no longer the required mechanism

Historical state remains truthful:

```text
HUMAN_REVIEW_EXECUTED=NO
```

Under FD-008, that fact no longer blocks progress by itself.

```text
AYA_135_HUMAN_REVIEW_REQUIRED=NO
AI_ASSISTANT_SUBSTITUTES_FOR_HUMAN_REVIEW=NOT_APPLICABLE_AS_REQUIRED_MECHANISM
AYA_135_DETERMINISTIC_RECORD_EVIDENCE_ALLOWED=YES
```

The prior human-review script and boundary remain historical artifacts; they are not deleted or rewritten.

## 5. Rights, privacy, and scope still require evidence

FD-008 changes the required evidence mechanism, not the substantive evidence obligations.

```text
RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
PRIVACY_STATE=UNRESOLVED
SCOPE_RECORD_EVIDENCE=NOT_YET_EXECUTED_UNDER_FD008
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
DEFAULT_PASS=PROHIBITED
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
```

Dataset-level Apache-2.0 metadata remains supported at the pinned Aya source, but embedded or quoted third-party risk must still be handled conservatively. Ambiguous records must remain blocked or be excluded.

## 6. New dependency-safe continuation frontier

The next machine-authorized unit is to predeclare and implement an exact deterministic, local-only record-evidence method for the fixed 135 candidates.

The method must be frozen before real-result execution and must satisfy all of the following:

```text
EXACT_SOURCE_SHA256_BINDING=REQUIRED
EXACT_CANDIDATE_IDENTITY_BINDING=REQUIRED
USER_ID_READ=PROHIBITED
NETWORK_ACCESS=PROHIBITED
EXTERNAL_AI_OR_MODEL_RECORD_PROCESSING=PROHIBITED
EXTERNAL_PROVIDER_SCREENING=PROHIBITED
RAW_TEXT_OUTPUT=PROHIBITED
RAW_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
AMBIGUITY_POLICY=FAIL_CLOSED
SPEC003_EVALUATOR_OWNS_ELIGIBLE=YES
POST_RESULT_METHOD_CHANGE=PROHIBITED
```

A valid successor may conservatively exclude records that cannot be deterministically cleared. It may not create a default rights/privacy/scope PASS.

## 7. Data-admission state

```text
DATA_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_135_SPEC003_EVALUATOR_ONLY
DATA_ADMISSION_STATE=BLOCKED
CURRENT_AYA_DATA_FRONTIER=REQUIRED_PREDECLARED_DETERMINISTIC_RECORD_RIGHTS_PRIVACY_SCOPE_EVIDENCE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
```

The data-admission edge cannot advance until deterministic record evidence is actually executed on the exact verified local payload and supplied to the canonical Spec 003 evaluator.

## 8. Broader E004 gates remain closed

FD-008 does not grant later tournament/model/training authority.

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
CURRENT_AUTHORIZED_SPEND_USD=0
```

No later component, model conversion, tournament execution, A15, E005, or training unit may bypass the remaining evidence-dependent data-admission edge.

## 9. E004/E005 state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
CURRENT_AYA_DATA_FRONTIER=REQUIRED_PREDECLARED_DETERMINISTIC_RECORD_RIGHTS_PRIVACY_SCOPE_EVIDENCE
AYA_135_HUMAN_REVIEW_REQUIRED=NO
HUMAN_REVIEW_EXECUTED=NO
DATA_ADMISSION_STATE=BLOCKED
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
E005_REACHABLE=NO
PROJECT_FINISHED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. Explicit exclusions

V21 performs or claims no deterministic record-evidence result, record-level rights PASS, privacy PASS, scope PASS, data admission, final curriculum construction, DatasetSnapshot freeze, model conversion, model inference, tournament execution, A15 activation, training, Private Gold/PHI/gated access, credential use, external provider generation, procurement, payment, spend, clinical qualification, release claim, or project completion.

## 11. Repository qualification

Under FD-007, independent repository review is optional by default. Before merge, verify exact base/head/diff, correspondence to the Founder's explicit FD-008 direction, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
