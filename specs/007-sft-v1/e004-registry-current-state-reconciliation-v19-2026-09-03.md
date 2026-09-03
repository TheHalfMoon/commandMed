# E004 Registry Current-State Reconciliation V19 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `21a00936f38b11adfc9141bc7cf83dff70b4d3bc`  
**Authority effect:** NONE  
**Execution-authority effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the global E004 frontier after canonical Aya GitHub transport Decision B, successful exact-byte transport, mandatory local SHA-256 verification, local exact-schema inspection, bounded non-admitting `SP007-RO-001` candidate construction, and raw/transient cleanup.

This record supersedes V18 only for later current-state interpretation. Historical records, including failed materialization and first cleanup attempts, remain immutable audit evidence.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v18-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v19-2026-09-03.md
COMPONENT_POLICY_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
AYA_CANDIDATE_EVIDENCE=specs/007-sft-v1/e004-aya-local-candidate-construction-evidence-2026-09-03.md
AYA_CANDIDATE_HASH_ROOTS=specs/007-sft-v1/e004-aya-candidate-hash-roots-v1.json
AYA_CANDIDATE_SUMMARY=specs/007-sft-v1/e004-aya-candidate-pass-summary-v1.json
AYA_CANDIDATE_FILTER_IMPLEMENTATION=scripts/e004_aya_candidate_pass.py
AUTHORITY_EXPANSION_FROM_V19=NONE
```

## 2. Canonical Founder authority now includes the bounded transport bridge

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
FOUNDER_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION=E004_AYA_GITHUB_TRANSPORT_BRIDGE_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
CURRENT_AUTHORIZED_SPEND_USD=0
```

The bridge decision is canonical via PR #196 / merge `5be3205d79c14633973c8f745659e0b6490bb7f6`. It changed transport environment only and did not create remote record-processing authority.

## 3. Exact Aya subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
SOURCE_FILE_SIZE_BYTES=137195800
```

No byte-subject expansion occurred.

## 4. Former local byte-materialization blocker is resolved

PR #197 / merge `d4ab43d359e3820f6d7d3514f1f22ceba3710de4` executed the bounded GitHub-hosted transport bridge after canonical Founder authority existed. Run `33760893301` / job `100666636213` passed all exact route checks, remote SHA verification, artifact transport, and runner cleanup.

The payload was then materialized locally and verified before parsing:

```text
AYA_PAYLOAD_MATERIALIZED=YES_EPHEMERAL
LOCAL_PAYLOAD_BYTES_RECEIVED=137195800
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=YES
LOCAL_SHA256_OBSERVED=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
LOCAL_SHA256_MATCH=PASS
PARSE_BEFORE_LOCAL_SHA256_MATCH=NO
FORMER_MATERIALIZATION_BLOCKER=RESOLVED
```

The transient Aya transport artifact was deleted after confirmed local materialization. Cleanup run `33761433144` / job `100668465648` succeeded after the first formatting-sensitive cleanup attempt was repaired; the original bridge run subsequently exposed no artifact.

## 5. Exact schema and human-origin semantics are now byte-derived

Local parsing occurred only after SHA-256 verification.

```text
AYA_PAYLOAD_PARSED=YES_LOCAL_AFTER_SHA256_PASS
EXACT_SCHEMA_FIELDS=inputs,targets,language,language_code,annotation_type,user_id
SOURCE_ROWS=202362
EXACT_ANNOTATION_TYPE_ORIGINAL=original-annotations
EXACT_ANNOTATION_TYPE_REANNOTATION=re-annotations
EXACT_ORIGINAL_ANNOTATION_ROWS=137092
EXACT_REANNOTATION_ROWS=65270
ANNOTATION_TYPE_NULLS=0
ORIGINAL_HUMAN_ANNOTATION_FILTER_FROZEN=YES
REANNOTATION_EXCLUSION_PROVABLE=YES
```

The prior public-research documentation recorded `138844` originals from source metadata. Exact pinned bytes contain `137092`. V19 preserves that discrepancy and treats the byte-derived count as controlling only for this exact file identity.

```text
PRIOR_DOCUMENTED_ORIGINAL_COUNT=138844
EXACT_PINNED_BYTE_ORIGINAL_COUNT=137092
COUNT_DISCREPANCY=1752
```

## 6. Data-minimization boundaries were preserved

```text
USER_ID_SCHEMA_FIELD_OBSERVED=YES
USER_ID_COLUMN_READ=NO
USER_ID_PERSISTED=NO
USER_ID_IN_CANDIDATE_REPRESENTATION=NO
DEMOGRAPHICS_CONFIGURATION_USED=NO
RAW_RECORD_TEXT_SENT_TO_EXTERNAL_MODEL_PROVIDER_OR_API=NO
EXTERNAL_RECORD_PROCESSING=NO
```

ChatGPT was not used for record-level judgment. No Aya record text was surfaced to the assistant.

## 7. Bounded local deterministic candidate pass completed

```text
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
EXECUTED_LOCAL_SCRIPT_SHA256=12ecee629f5558bb347ad0f14ff75cea9f3b00d90030ad19513d4e87bd566f8f
SP007_RO_001_RECORD_SCOPE_FILTER_EXECUTED=YES_DETERMINISTIC_CONSERVATIVE
LOCAL_DETERMINISTIC_PRIVACY_RISK_SCREENING_PERFORMED=YES
HUMAN_RECORD_INSPECTION_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=YES_NON_ADMITTING
```

The conservative V1 filter retained only exact `eng`/`English` and `arb`/`Standard Arabic` lanes, excluded clinical-positive patterns and deterministic privacy-risk hits, and excluded any record whose admitted non-clinical task family could not be deterministically established. Other Arabic varieties were not promoted by inference.

Exact aggregate reconciliation:

```text
SOURCE_ROWS=202362
EXCLUDE_NON_ADMITTED_LANGUAGE=132172
EXCLUDE_REANNOTATION=65270
EXCLUDE_SCOPE_NOT_DETERMINISTICALLY_ENFORCEABLE=2623
EXCLUDE_CLINICAL_SCOPE=2131
EXCLUDE_PRIVACY_PATTERN=24
EXCLUDE_INVALID_TEXT_SHAPE=4
EXCLUDE_DUPLICATE_CONTENT=3
PROVISIONAL_CANDIDATES=135
COUNT_RECONCILIATION=PASS
```

Candidate language counts:

```text
eng=88
arb=47
```

## 8. Exact non-admitting candidate identity roots exist

```text
PROVISIONAL_CANDIDATE_COUNT=135
LOCAL_FULL_HASH_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
LOCAL_FULL_HASH_MANIFEST_FILE_SHA256=bbc7188613f242b428b4ac4cad0297c9dfb31403f6fab146a1a8491a106b2d6e
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
FULL_PER_RECORD_HASH_LIST_REPOSITORY_PERSISTED=NO
RAW_RECORD_TEXT_REPOSITORY_PERSISTED=NO
```

Repository persistence is deliberately limited to aggregate evidence and set roots.

## 9. Raw/transient cleanup is complete

The exact source hash and size were rechecked before local deletion.

```text
PREDELETE_SOURCE_SHA256_MATCH=PASS
PREDELETE_SOURCE_SIZE_MATCH=PASS
RAW_AYA_PARQUET_DELETED=YES
TRANSIENT_AYA_WORKSPACE_REMOVED=YES
RAW_OR_TRANSIENT_AYA_PAYLOAD_REMAINING=NO
REMOTE_AYA_TRANSPORT_ARTIFACT_REMAINING=NO
REMOTE_PARQUET_TOOLING_ARTIFACT_REMAINING=NO
```

The public `pyarrow` tooling wheel was transported separately and never touched Aya content. Its remote artifact cleanup completed successfully through PR #202 / merge `21a00936f38b11adfc9141bc7cf83dff70b4d3bc`, run `33763407701`.

## 10. Candidate state is still fail-closed and non-admitted

The public-data Decision B explicitly did not authorize admission. V19 therefore preserves unresolved evidence rather than fabricating a PASS:

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
CURRICULUM_RECORD_SET_PRESENT=NO
RIGHTS_STATE=UNRESOLVED
FINAL_PRIVACY_STATE=UNRESOLVED
CONTAMINATION_STATE=NOT_ASSESSED
QUARANTINE_PASS=NO
LICENSE_COMPATIBILITY_ADMISSION_PASS=NO
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
```

The deterministic privacy screen is risk reduction only. Because bounded human record inspection was not performed, it is not represented as final privacy clearance.

## 11. First live component dependency remains incomplete

The dependency-safe component order begins with exact admitted gradient-bearing content whose provenance, rights/license, privacy, split, verification, contamination, and quarantine state are complete.

V19 now has a fixed non-admitting candidate identity set, but not admitted content:

```text
LIVE_COMPONENT_ADMITTED_GRADIENT_CONTENT=ABSENT
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT
LIVE_COMPONENT_LICENSE_PASS_BINDING=ABSENT
LIVE_COMPONENT_BASE_CHECKPOINT_BINDING=ABSENT
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
BASE_PREFLIGHT_ALLOWED=NO
COMPONENT_PREFLIGHT_ALLOWED=NO
```

No later dependency may be fabricated from the existence of 135 provisional hashes.

## 12. Tournament A11 contamination authority is not the current Aya admission path

The existing `e004-a11-contamination-assessment-authority-request-template-2026-08-27.md` is bound to the frozen tournament selection-suite/candidate-corpus sequence and requires upstream preconstruction plus completed A15 suite construction before activation.

```text
A11_TOURNAMENT_CONTAMINATION_TEMPLATE_REPURPOSED_FOR_AYA_CURRICULUM=NO
A11_ACTIVE_REQUEST=ABSENT
A11_ASSESSMENT_AUTHORITY=NONE
```

V19 does not bypass that temporal sequence or relabel it as curriculum-data authority.

## 13. Dependency-safe next authority gap

The former payload-access/candidate-construction gap is closed as bounded evidence. The earliest remaining Aya component data gap is an exact, separately authorized qualification/admission evidence path over the fixed 135-candidate identity set.

Such a future surface must not silently grant admission. It must bind this exact candidate identity set and define what rights/license, final privacy, split/quarantine, record-level verification, and curriculum-specific contamination evidence may be gathered or evaluated, preserving fail-closed states until the relevant evaluator proves them.

```text
NEXT_REPOSITORY_ACTION=PREPARE_EXACT_AYA_135_CANDIDATE_QUALIFICATION_ADMISSION_AUTHORITY_SURFACE
NEXT_ACTION_AUTHORITY_EFFECT=NONE_UNTIL_POST_CANONICAL_FOUNDER_DECISION
BROAD_CONTINUATION_APPROVAL_SUBSTITUTES_FOR_FUTURE_EXACT_DECISION=NO
```

A future decision surface must distinguish this curriculum-candidate path from tournament A11 contamination and from training authority.

## 14. Conversion, A15, model execution, and training remain closed

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

## 15. E004/E005 state

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
E005_REACHABLE=NO
PROJECT_FINISHED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

The successful Aya bounded pass is real progress but does not produce tournament evidence or make E005 reachable.

## 16. Explicit exclusions

V19 performs or authorizes no data admission, final curriculum construction, DatasetSnapshot freeze, quarantine PASS, license-compatibility PASS, contamination assessment, model conversion, model inference, tournament execution, A15 activation, training, Private Gold/PHI/gated access, credential use, provider generation, procurement, payment, spend, patient-use claim, clinical qualification, release claim, or project-completion claim.

## 17. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded evidence/reconciliation package. Before merge, verify exact base/head/diff, script/evidence correspondence, aggregate-count reconciliation, applicable status/CI, unresolved review threads, mergeability, ruleset/branch state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
