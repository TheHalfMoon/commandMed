# E004 Aya 135-Candidate Qualification and Admission Founder Decision Request — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Current global frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v19-2026-09-03.md`  
**Canonical base:** `6bca22be4ee569402530fc5a15dea60d4e6c4ad9`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Admission performed:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve the earliest dependency-safe authority gap after V19: allow or decline one tightly bounded qualification-and-evaluator-owned-admission pass over the already-fixed Aya candidate identity set produced by `AYA_SP007_RO_001_CANDIDATE_FILTER_V1`.

This surface does not itself admit any record. It does not create a DatasetSnapshot, final curriculum, model winner, conversion, A15 activation, model execution, or training authority.

## 2. Exact fixed candidate subject

Decision B, if selected after this surface becomes canonical, binds only the following already-established subject:

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
CURRENT_CANDIDATE_STATE=BLOCKED_NON_ADMITTING
```

No source, revision, file, filter, candidate count, candidate-set identity, language lane, or capability-scope expansion is authorized by this surface.

## 3. Decision classes

### `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_A` — preserve current state

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_A
AYA_135_QUALIFICATION_EVIDENCE_AUTHORITY=NONE
AYA_135_SPEC003_ADMISSION_EVALUATION_AUTHORITY=NONE
AYA_135_CURRICULUM_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=NONE
```

Effect: the 135 fixed candidates remain non-admitted V19 evidence only.

### `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B` — authorize bounded qualification and evaluator-owned admission evaluation

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

Decision B permits evidence gathering and deterministic evaluator execution only. A record becomes `ELIGIBLE` only if the canonical Spec 003 evaluator computes that result from complete evidence for the exact declared use. Founder authorization is not itself an admission PASS.

## 4. Exact replay boundary

The full per-record hash list was deliberately not persisted in canonical source. Qualification may therefore replay the same bounded extraction only if every identity check remains exact.

The existing canonical Aya route and GitHub byte-transport decisions may be reused only for the same exact byte subject and only with their existing prechecks, remote SHA-256 verification, transient-artifact restrictions, local SHA-256-before-parse requirement, and cleanup requirements.

A replay MUST require:

```text
REPLAY_SOURCE_SHA256_MATCH=REQUIRED
REPLAY_SOURCE_XET_HASH_MATCH=REQUIRED
REPLAY_FILTER_ID_MATCH=REQUIRED
REPLAY_CANDIDATE_COUNT_MUST_EQUAL=135
REPLAY_MANIFEST_SHA256_MUST_EQUAL=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
REPLAY_RECORD_ID_SET_SHA256_MUST_EQUAL=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
REPLAY_CONTENT_SHA256_SET_SHA256_MUST_EQUAL=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
```

Any mismatch aborts without substitution, filter repair, candidate-set widening, or post-result rule change.

## 5. Rights and license evidence boundary

The source currently declares Apache-2.0. Dataset-level license metadata is evidence, not automatic proof that every embedded record or quoted source passage is independently cleared for the exact optimization use.

Decision B may:

- bind the exact dataset-level license/source evidence to the immutable Aya subject;
- inspect only the exact fixed candidate records locally where necessary to determine record-level provenance or embedded-source risk;
- conservatively exclude records whose rights state cannot be supported by evidence;
- invoke the canonical Spec 003 rights state and admission evaluator.

It may not:

- provide legal advice;
- infer `SUPPORTED` from a repository badge alone when material record-level rights remain unresolved;
- widen rights from dataset-level metadata to unrelated embedded material;
- change `CONDITIONAL`, `UNRESOLVED`, or `INCOMPATIBLE` evidence into `SUPPORTED` without supporting evidence.

```text
RIGHTS_SUPPORTED_REQUIRES_EVIDENCE=YES
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
LEGAL_ADVICE=NO
```

## 6. Privacy boundary

Decision B preserves the existing no-external-provider content boundary.

```text
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
REMOTE_RECORD_INSPECTION=PROHIBITED
REMOTE_MODEL_OR_AI_RECORD_PROCESSING=PROHIBITED
IDENTITY_RECONSTRUCTION=PROHIBITED
USER_ID_READ_FOR_QUALIFICATION=PROHIBITED
USER_ID_PERSISTENCE=PROHIBITED
PHI_COLLECTION_OR_ENRICHMENT=PROHIBITED
```

Qualification may use local deterministic screening and bounded local human inspection only. The V19 deterministic screen does not silently become final privacy clearance.

If final privacy evidence cannot be established within the authorized local boundary, the affected record remains `UNRESOLVED` or is excluded fail closed.

```text
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
HUMAN_INSPECTION_UNAVAILABLE_IMPLIES_PASS=NO
```

## 7. Split and quarantine boundary

Any candidate being evaluated for gradient-bearing use must use the canonical training-purpose quarantine policy. Current canonical `data/eval/quarantine.json` permits training only from verified training-source classes and prohibits commandMed Gold and public external evaluation material from training.

Decision B may create evidence-bound split/quarantine dispositions for the fixed 135-candidate set only. It may not access Private Gold, use Gold to optimize or admit records, or relabel evaluation content as training data.

```text
PURPOSE=TRAIN
ROLE_CLASS=LEARNER_RESEARCHER
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_AS_TRAINING_SOURCE=PROHIBITED
PUBLIC_EXTERNAL_EVAL_AS_TRAINING_SOURCE=PROHIBITED
QUARANTINE_PASS_INFERRED_FROM_DECISION=NO
```

## 8. Curriculum-specific contamination boundary

This decision creates no authority to repurpose the existing tournament A11 contamination request. The A11 tournament sequence remains unchanged.

Decision B may perform a curriculum-candidate contamination assessment only for the exact 135-candidate set and only against an exact predeclared, non-protected comparison universe whose identities are bound before the assessment.

Permitted comparison evidence is limited to public/ungated canonical evaluation or benchmark assets whose exact immutable identities and authorized comparison purpose are already established or are separately bound before payload access. Private Gold, PHI, gated assets, credentials, paid providers, and mutable/unbound benchmark content remain prohibited.

The assessment must be fail closed:

```text
TOURNAMENT_A11_REPURPOSED=NO
CURRICULUM_CANDIDATE_SET_FIXED_BEFORE_ASSESSMENT=YES
COMPARISON_UNIVERSE_FIXED_BEFORE_ASSESSMENT=YES
POST_RESULT_THRESHOLD_CHANGE=PROHIBITED
POST_RESULT_UNIVERSE_SUBSETTING=PROHIBITED
PRIVATE_GOLD_COMPARISON=PROHIBITED
GATED_OR_CREDENTIALED_COMPARISON_ASSET=PROHIBITED
EXTERNAL_PROVIDER_SEMANTIC_JUDGE=PROHIBITED
CONTAMINATION_CLEAN_INFERRED_FROM_NO_MATCH=NO_UNLESS_PREDECLARED_METHOD_AND_COVERAGE_SUPPORT_IT
```

If the complete required comparison universe or a justified predeclared method cannot be bound, contamination remains `NOT_ASSESSED`, `PENDING`, or otherwise unresolved and cannot support admission.

Decision B does not authorize model inference for contamination assessment.

## 9. Record-level scope verification

Every candidate evaluated for admission must remain inside `SP007-RO-001`:

```text
REQUIRED_ROLE_CLASS=LEARNER_RESEARCHER
PATIENT_CAREGIVER_POSITIVE_CAPABILITY=PROHIBITED
CLINICAL_PROFESSIONAL_POSITIVE_CAPABILITY=PROHIBITED
EXCLUDED_CLINICAL_CAPABILITY_HIT_CAN_PASS=NO
```

The V19 deterministic candidate filter is upstream evidence. Admission still requires exact record-level verification compatible with the canonical Spec 007 curriculum and research-scope validators.

## 10. Spec 003 evaluator is the only admission authority under Decision B

Decision B does not permit a handwritten `ELIGIBLE` result.

For each exact candidate, evidence supplied to the canonical Spec 003 evaluator must truthfully bind the exact declared use and all required source, artifact, rights, privacy, purpose/split, quarantine, contamination, origin, and provenance fields.

```text
DECLARED_USE=TRAINING_OR_ADAPTATION
PURPOSE=TRAIN
ORIGIN_TYPE=ORIGINAL
SPEC003_EVALUATOR_REQUIRED=YES
CALLER_CONTROLLED_ADMISSION_STATE=PROHIBITED
CALLER_CONTROLLED_RECORD_IDENTITY=PROHIBITED_WHERE_EVALUATOR_RECOMPUTES_IDENTITY
```

Evaluator dispositions retain their canonical meanings:

```text
ELIGIBLE=LINEAGE_EVIDENCE_SATISFIED_FOR_EXACT_DECLARED_USE_ONLY
REFERENCE_ONLY=NOT_TRAINING_ADMISSION
BLOCKED=REQUIRED_EVIDENCE_OR_GATE_UNRESOLVED
PROHIBITED=INCOMPATIBLE_OR_FORBIDDEN_FOR_EXACT_USE
```

`ELIGIBLE` does not imply clinical safety, product release readiness, legal clearance, model-selection success, DatasetSnapshot freeze, training authority, or patient use.

## 11. Repository persistence boundary

Repository-safe persistence may include:

- exact source/filter/replay identities;
- evaluator input/output records that contain no raw personal content;
- record/content hashes;
- reason-coded aggregate dispositions;
- rights/privacy/split/quarantine/contamination evidence references;
- exact method and comparison-universe identities;
- current-state reconciliation.

Raw Aya payload bytes, raw record text, `user_id`, transient human-inspection material, credentials, or protected evaluation payloads must not be committed to canonical source.

## 12. Authorities that remain closed under Decision B

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

## 13. Fail-closed conditions

Qualification/admission execution must stop or leave affected records non-admitted on any of the following:

```text
EXACT_REPLAY_IDENTITY_MISMATCH
RIGHTS_EVIDENCE_UNRESOLVED
PRIVACY_EVIDENCE_UNRESOLVED
SPLIT_OR_QUARANTINE_EVIDENCE_UNRESOLVED
SCOPE_VERIFICATION_UNRESOLVED
CONTAMINATION_UNRESOLVED
REQUIRED_COMPARISON_UNIVERSE_UNBOUND
REQUIRED_EXTERNAL_PROVIDER_USE
GATED_OR_CREDENTIALED_ASSET_REQUIRED
PRIVATE_GOLD_OR_PHI_ACCESS_REQUIRED
INCREMENTAL_SPEND_REQUIRED
SPEC003_VALIDATION_FAILURE
SPEC003_EVALUATOR_BLOCKED_OR_PROHIBITED
```

Failure does not authorize another dataset, filter, candidate expansion, protected asset, external model, credential, paid route, or weaker evaluator rule.

## 14. E004 effect

Even a successful Decision B pass cannot complete E004 by itself.

```text
E004_COMPLETE_FROM_AYA_135_DECISION_B=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

At most, it can produce exact admitted-or-rejected curriculum candidate evidence needed by the first live component dependency. Later dependency-ordered work remains separately governed.

## 15. Exact Founder response required

To preserve the V19 state:

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_A
```

To authorize the bounded exact-set qualification and Spec 003 evaluator-owned admission path:

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B
```

A broad continuation instruction, generic approval, statement that all ordinary approvals are granted, PR merge, or earlier Founder token is not substituted for this exact decision.

The operative Founder response must occur after this decision surface is canonical and must be captured in a separate decision record before the newly authorized qualification/admission operations are executed.

## 16. Current state until an operative decision is canonical

```text
FOUNDER_AYA_135_QUALIFICATION_ADMISSION_DECISION=ABSENT
AYA_135_QUALIFICATION_EVIDENCE_AUTHORITY=NONE
AYA_135_SPEC003_ADMISSION_EVALUATION_AUTHORITY=NONE
AYA_135_CURRICULUM_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 17. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only Founder decision request.

Before merge, verify exact base/head/diff, correspondence to canonical V19 and the fixed Aya candidate identity roots, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
