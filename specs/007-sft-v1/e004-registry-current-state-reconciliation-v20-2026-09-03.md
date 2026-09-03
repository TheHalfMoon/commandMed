# E004 Registry Current-State Reconciliation V20 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `de5875603f3337116dd4531f6bbb7c257abec4bb`  
**Authority effect:** NONE  
**Execution-authority effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the E004 frontier after the exact Aya 135 qualification authority was exercised through deterministic contamination assessment, exact Spec 003 evaluation, repository-safe evidence binding, canonical local-human-review tooling, and final local transient cleanup.

This record supersedes V19 only for current-state interpretation. Historical V19 transport/candidate-construction evidence remains valid audit history.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v19-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v20-2026-09-03.md
AYA_QUALIFICATION_EVIDENCE=specs/007-sft-v1/e004-aya-135-qualification-evidence-v1.json
AYA_HUMAN_REVIEW_BOUNDARY=specs/007-sft-v1/e004-aya-135-local-human-review-boundary-2026-09-03.md
AYA_HUMAN_REVIEW_IMPLEMENTATION=scripts/e004_aya_135_human_review_v2.py
AYA_LOCAL_CLEANUP_EVIDENCE=specs/007-sft-v1/e004-aya-135-local-transient-cleanup-evidence-v2-2026-09-03.md
AUTHORITY_EXPANSION_FROM_V20=NONE
```

## 2. Exact Aya candidate subject remains unchanged

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

No source, filter, record-set, content-set, role, or language expansion occurred.

## 3. Qualification Decision B was exercised without caller-controlled admission

The canonical exact-set decision remains:

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B
DATA_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_135_SPEC003_EVALUATOR_ONLY
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The evaluator, not the caller or Founder authorization itself, remains responsible for any future `ELIGIBLE` disposition.

## 4. Curriculum-specific contamination assessment is complete for the frozen method

PR #216 / merge `c3eef58ca89bdf007c6d8eb8004253333be95e27` froze the comparison universe and scientific method before any result existed. V1 implementation later aborted before comparison because of a row-bound candidate replay defect. PR #217 / merge `c3decb3aefe7f22769b86e943936b4e92785b3df` repaired replay before any contamination disposition existed and did not change the scientific method or comparison universe.

The executed frozen method was:

```text
METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
UNIVERSE_CANONICAL_SHA256=e473b2607b28467f3bd055fb34a1e1092fc15f87558185e989d8e4c483c0e98e
COMPARISON_FILE_COUNT=9
COMPARISON_FILES_VERIFIED=9
COMPARISON_STRING_LEAVES_PROCESSED=472773
COMPARISON_13_TOKEN_WINDOWS_PROCESSED=13320906
ASSESSED_CLEAN=135
OVERLAP_OR_HIGH_RISK=0
SEMANTIC_JUDGE_USED=NO
MODEL_INFERENCE_USED=NO
PRIVATE_GOLD_USED=NO
GATED_OR_CREDENTIALED_ASSET_USED=NO
RAW_MATCHED_TEXT_EMITTED=NO
POST_RESULT_THRESHOLD_CHANGE=NO
POST_RESULT_UNIVERSE_CHANGE=NO
```

Repository-safe result identities:

```text
CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
CONTAMINATION_SUMMARY_SHA256=35cf4db119dd21c32a05ddd7e222cc2d6bf1f9ee5c5c694b6e682f784eb02e89
```

`ASSESSED_CLEAN` is limited to the exact frozen 13-token method and exact bound universe. It is not a universal no-contamination claim.

## 5. Dataset-level license evidence is established; record-level rights remain unresolved

The pinned Aya dataset metadata declares Apache-2.0 and describes training/fine-tuning/evaluation use. Canonical governance explicitly prohibits silently extending dataset-level license evidence to embedded or quoted third-party material whose record-level rights risk remains unresolved.

```text
DATASET_LEVEL_LICENSE=Apache-2.0
DATASET_LEVEL_RIGHTS_EVIDENCE=SUPPORTED_AT_PINNED_DATASET_METADATA
RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
LEGAL_ADVICE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
```

The remaining record-level rights question is therefore not represented as `SUPPORTED` without the required bounded human evidence.

## 6. Split/quarantine evidence is compatible but not an admission substitute

The exact source file is the Aya `train` split. Canonical quarantine policy allows verified training-source classes for `PURPOSE=TRAIN` and prohibits Private Gold and public external evaluation material as training sources.

The bounded pass observed no use of Private Gold or public external evaluation content as Aya training source:

```text
PURPOSE=TRAIN
SOURCE_SPLIT=train
QUARANTINE_CONFLICT_OBSERVED=NO
QUARANTINE_STATE=NOT_QUARANTINED
PRIVATE_GOLD_USED=NO
PUBLIC_EXTERNAL_EVAL_USED_AS_TRAINING_SOURCE=NO
```

This evidence does not independently create final curriculum admission or DatasetSnapshot authority.

## 7. Canonical Spec 003 evaluation remains blocked only on unresolved human-evidence classes

After contamination evidence was supplied truthfully as `ASSESSED_CLEAN`, the exact canonical Spec 003 evaluator processed all 135 records with zero validation errors.

```text
SPEC003_CANDIDATE_COUNT=135
SPEC003_ELIGIBLE_COUNT=0
SPEC003_BLOCKED_COUNT=135
SPEC003_VALIDATION_ERROR_COUNT=0
RIGHTS_UNRESOLVED=135
PRIVACY_UNRESOLVED=135
CONTAMINATION_UNRESOLVED=0
```

Repository-safe exact result identity:

```text
SPEC003_POST_CONTAMINATION_RESULTS_SHA256=19e6c10fcf9667ec0d8074c3e8dac70f96c085db364a9909fd94ed9d5002c876
```

A temporary local hypothetical rights-supported evaluation was not canonical evidence and was deleted during cleanup. V20 makes no record-level rights PASS claim from that hypothetical run.

## 8. Exact remaining human evidence gate is canonical

PR #218 / merge `de5875603f3337116dd4531f6bbb7c257abec4bb` canonically bound the repository-safe qualification evidence and the exact local-human-review implementation.

```text
REVIEW_METHOD_ID=AYA_135_LOCAL_HUMAN_PRIVACY_EMBEDDED_SOURCE_REVIEW_V2
REVIEW_SCRIPT=scripts/e004_aya_135_human_review_v2.py
REVIEW_SCRIPT_SHA256=a1d0fc68f14783bc7aa8b0d4f35f6b7bec590b93db2c7c89f9acccce34bec4de
REPLAY_ONLY_VALIDATION_CANDIDATES=135
HUMAN_REVIEW_EXECUTED=NO
```

For every exact candidate, a real local human must record privacy, embedded-source-risk, and `SP007-RO-001` scope evidence. No default PASS is permitted.

```text
HUMAN_INSPECTION_UNAVAILABLE_IMPLIES_PASS=NO
AI_ASSISTANT_SUBSTITUTES_FOR_HUMAN_REVIEW=NO
REMOTE_MODEL_OR_AI_RECORD_PROCESSING=PROHIBITED
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
```

This is the earliest non-delegable dependency boundary for the Aya candidate-admission line.

## 9. Local transient cleanup is complete

After PR #218 made the safe evidence/tooling canonical and no further machine-authorized content-processing unit remained in this session, the local transient material was removed.

```text
PRE_CLEANUP_FILE_COUNT=914
PRE_CLEANUP_BYTES=779130083
POST_CLEANUP_REMAINING_TARGET_PATH_COUNT=0
LOCAL_RAW_AYA_PAYLOAD_REMAINING=NO
LOCAL_COMPARISON_PAYLOAD_REMAINING=NO
LOCAL_TOOLING_ENVIRONMENT_REMAINING=NO
LOCAL_HYPOTHETICAL_RIGHTS_PASS_OUTPUT_REMAINING=NO
LOCAL_TRANSIENT_CLEANUP_COMPLETE=YES
```

GitHub-hosted transport artifacts were configured with one-day retention and runner-local cleanup succeeded. No remote-artifact deletion is claimed where no authorized deletion tool was available.

## 10. Dependency-safe continuation boundary

The existence of 135 fixed identities plus contamination-clean evidence does not satisfy the data-admission edge. The next dependency-ordered unit on the Aya line requires genuine local human evidence first.

```text
LIVE_COMPONENT_ADMITTED_GRADIENT_CONTENT=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT_AS_FINAL_ADMISSION_ARTIFACT
LIVE_COMPONENT_LICENSE_PASS_BINDING=ABSENT_AT_RECORD_LEVEL
BASE_PREFLIGHT_ALLOWED=NO
COMPONENT_PREFLIGHT_ALLOWED=NO
```

No later component, model conversion, tournament execution, A15, or training unit may be pulled forward to bypass this edge.

## 11. Broader E004 gates remain closed

V20 does not rewrite earlier E004 tournament/preflight requirements. In addition to the Aya human-evidence boundary, canonical model/conversion/A15/runtime/tournament prerequisites remain governed by their existing exact records and must be independently satisfied before any live tournament or model execution.

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
```

## 12. E004/E005 state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
CURRENT_AYA_DATA_FRONTIER=REQUIRED_LOCAL_HUMAN_PRIVACY_EMBEDDED_SOURCE_AND_SCOPE_REVIEW
DATA_ADMISSION_STATE=BLOCKED
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
E005_REACHABLE=NO
PROJECT_FINISHED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 13. Explicit exclusions

V20 performs or authorizes no human-review fabrication, record-level rights PASS, privacy PASS, data admission, final curriculum construction, DatasetSnapshot freeze, model conversion, model inference, tournament execution, A15 activation, training, Private Gold/PHI/gated access, credential use, provider generation, procurement, payment, spend, clinical qualification, release claim, or project-completion claim.

## 14. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded evidence/reconciliation package. Before merge, verify exact base/head/diff, correspondence to PR #216/#217/#218 canonical evidence, cleanup counts, applicable status/CI, unresolved review threads, mergeability, ruleset/branch state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
