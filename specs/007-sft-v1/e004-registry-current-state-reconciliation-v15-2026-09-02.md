# E004 Registry Current-State Reconciliation V15 — 2026-09-02

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only global current-state reconciliation  
**Canonical base:** `54c192248f09bf93730604e83947a135583ef162`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the global E004 current view after canonical capture of the Founder's exact post-surface successor execution Decision B in PR #184 / merge `54c192248f09bf93730604e83947a135583ef162`.

This record supersedes V14 only for later current-state interpretation. Historical evidence remains immutable.

```text
PREVIOUS_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v14-2026-09-02.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v15-2026-09-02.md
COMPONENT_POLICY_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
SUCCESSOR_EXECUTION_DECISION_RECORD=specs/007-sft-v1/e004-successor-scope-execution-authorization-founder-decision-2026-09-02.md
V15_SUPERSEDES_V14_ONLY_FOR_LATER_CURRENT_STATE=YES
AUTHORITY_EXPANSION_FROM_V15=NONE
```

## 2. Decision B is now canonical

The canonical decision request was already merged in PR #181 / `80924a5036659a336458c05011a8eabc832600b3`.

The Founder subsequently supplied the exact required response and PR #184 canonically captured it:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is a real authority transition relative to V14, but it removes only the successor-scope execution-authority blocker. It does not create or imply PASS for any other prerequisite.

## 3. Candidate boundary remains unchanged

Decision B remains limited to the exact already-frozen E001 candidate identities:

### PRIMARY

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
```

### CONTROL

```text
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

No candidate or revision is added by V15.

## 4. Decision B does not make execution startable

The canonical base activation preflight still requires an exact valid RunManifest and exact component records plus matching training, finance, access, model-execution, weight-access, and device-execution authority bindings.

The research-component preflight additionally requires an exact successor scope binding, exact RunManifest identity match, exact scope authority match, and a real PASS guard snapshot for the exact seven sentinel fixtures.

Therefore the current state is:

```text
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY_BLOCKER=REMOVED_CANONICAL
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

No synthetic fixture result may be promoted into these live fields.

## 5. Data due diligence remains metadata-only

Canonical PRs #180 and #182 established public candidate research and public metadata/file identity pins for:

```text
PUBLIC_DATA_CANDIDATE_PRIORITY_1=CohereLabs/aya_dataset
PUBLIC_DATA_CANDIDATE_PRIORITY_2=OpenAssistant/oasst1
PUBLIC_DATA_CANDIDATE_PRIORITY_3=databricks/databricks-dolly-15k
```

The currently recorded due-diligence source identities remain:

```text
AYA_DUE_DILIGENCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
AYA_TRAIN_PARQUET_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
OASST1_DUE_DILIGENCE_REVISION=fdf72ae0827c1cda404aff25b6603abec9e3399b
OASST1_READY_MESSAGES_SHA256=286a6e9a5a413b3272ae9c0b5a20d327983dea1c24342ae28cb244a6da65185c
OASST1_TRAIN_PARQUET_SHA256=bbfadf5ed1278ba2208c837fdcad865adf65f5df55d80abadab2745db13fcb5e
OASST1_VALIDATION_PARQUET_SHA256=24002597bb13a7edd42d92f773762f25e285f72c31a70449393d0ded1dc7b416
DOLLY_DUE_DILIGENCE_REVISION=bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a
DOLLY_JSONL_SHA256=2df9083338b4abd6bceb5635764dab5d833b393b55759dffb0959b6fcbf794ec
```

These remain due-diligence identities only:

```text
DATASET_DOWNLOAD_AUTHORITY=NONE
DATASET_BYTE_MATERIALIZATION_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=NONE
PRIVACY_PII_PHI_SCREENING_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
ADMISSION_REVISION_PIN_PRESENT=NO
DATASET_SNAPSHOT_PRESENT=NO
CURRICULUM_RECORD_SET_PRESENT=NO
```

Decision B does not change these fields.

## 6. Conversion remains blocked

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
MERGE_OR_ADAPTER_APPLICATION_AUTHORITY=NONE
```

If an E002-authorized exact candidate artifact cannot execute in the required runtime without conversion or weight transformation, Decision B does not permit that transformation.

## 7. Contamination remains blocked

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
```

The existing A11 contamination authority request template remains downstream and does not itself create authority.

## 8. A15 remains blocked

```text
A1_A14_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

Decision B does not replace A1-A14 or A15 requirements where the controlling execution contract makes them applicable.

## 9. Training remains blocked

The activation control plane requires a non-`NONE`, identity-matched `training_authorization_id` before it can return `allowed=true` for an exact RunManifest.

Current state remains:

```text
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

No gradient-bearing execution is startable.

## 10. Protected, credentialed, and paid resources remain blocked

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Global/full-scope clinical blockers remain unchanged

The broader multi-role/full-system lane remains blocked independently of the research-engineering component:

```text
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

Decision B applies only to `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1` and creates no clinical/system qualification.

## 12. Dependency-safe next frontier

Decision B makes it meaningful to continue constructing the exact component subject, but repository-only prose cannot manufacture the missing payload-derived evidence.

The next dependency-safe authority gap is the absence of a bounded public-data payload access / candidate-construction path for the already-researched public curriculum candidates.

A future bounded decision surface may authorize only the minimum public/ungated payload access and deterministic non-admitting screening needed to construct exact candidate records. Such a surface must not pre-authorize final admission, contamination PASS, training, model execution beyond Decision B, protected/gated data, credentials, or spend.

After that access is separately and exactly authorized, the dependency-safe work would be:

1. acquire only exact authorized public/ungated payload bytes;
2. verify downloaded bytes against the canonical source identity before parsing;
3. perform exact record-level provenance/human-origin filtering under the frozen non-clinical scope;
4. perform separately authorized privacy/PII/PHI screening required by the exact candidate-construction authority;
5. produce candidate lineage/content identities without calling them admitted while contamination remains unresolved;
6. obtain separately applicable contamination authority only when its prerequisites become satisfied;
7. compute admission through the canonical Spec 003 evaluator rather than self-asserting `ELIGIBLE`;
8. proceed to DatasetSnapshot, quarantine, exact scope binding, sentinel identities, guard evidence, resource/access/finance bindings, exact RunManifest, and only then re-run preflight.

## 13. Task-ledger interpretation

The current `specs/007-sft-v1/tasks.md` E004 paragraph still records `FOUNDER_SUCCESSOR_EXECUTION_DECISION=ABSENT` because it predates PR #184.

Until a bounded task-ledger reconciliation is merged, V15 supersedes that stale field for current-state interpretation only. The E004 checkbox remains correctly unchecked.

```text
E004_TASK_CHECKBOX=UNCHECKED_CORRECT
TASK_LEDGER_SUCCESSOR_DECISION_FIELD=STALE_ABSENT
CURRENT_SUCCESSOR_DECISION_FIELD=DECISION_B_CANONICAL
AUTHORITY_EXPANSION_FROM_THIS_SUPERSESSION=NONE
```

## 14. Current terminal state

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
MODEL_CONVERSION_AUTHORITY=NONE
DATASET_DOWNLOAD_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
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

This reconciliation performs or authorizes none of the following:

- dataset/model payload download or byte materialization;
- dataset admission, privacy screening, or contamination assessment;
- model/source-weight conversion, quantization, loading, or inference;
- tournament execution;
- A15 activation;
- training or gradient updates;
- external reviewer outreach;
- Private Gold, PHI, restricted, or gated asset access;
- credential use or provider generation;
- procurement, payment, or spend.

## 16. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only current-state reconciliation.

Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact Decision B correspondence, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
