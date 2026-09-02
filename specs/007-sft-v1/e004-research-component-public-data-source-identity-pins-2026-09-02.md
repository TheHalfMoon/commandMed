# E004 Research Component Public Data Source Identity Pins — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base:** `80924a5036659a336458c05011a8eabc832600b3`  
**Artifact class:** public metadata identity evidence only  
**Authority effect:** NONE  
**Data download performed:** NO  
**Dataset byte materialization performed:** NO  
**Data admission performed:** NO  
**Privacy/PHI screening performed:** NO  
**Contamination assessment performed:** NO  
**Model execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Purpose

Reduce one repository-only ambiguity left by the public candidate research record by pinning immutable public repository revisions and publicly exposed large-file content identities where the source host provides them without downloading dataset bytes.

This record is **due-diligence identity evidence only**. It is not an admission record and does not create a `DatasetSnapshot`, `CurriculumRecord`, source/license PASS, privacy/non-PHI PASS, contamination PASS, quarantine PASS, content-scope PASS, RunManifest, execution authority, or training authority.

Controlling records remain:

- `e004-research-component-public-data-candidate-research-2026-09-02.md`
- `e004-research-component-execution-preflight-blocker-packet-2026-09-02.md`
- `e004-successor-scope-execution-authorization-decision-request-2026-09-02.md`

```text
COMPONENT_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 2. Identity semantics

The identities below mean only:

> At the public source, an immutable repository revision and/or source-file content identity was observable on 2026-09-02.

They do **not** mean:

- the dataset or file is admitted;
- every record is human-authored;
- a record is in scope;
- privacy/PII/PHI review passed;
- license or downstream rights review passed;
- contamination review passed;
- a split is approved for training/evaluation;
- a source file may be downloaded or materialized;
- a future admission pin may silently reuse this due-diligence pin.

A future admitted source must be separately bound by the exact admission authority and evidence contracts then in force.

## 3. Candidate A — CohereLabs Aya Dataset

Public source:

- `https://huggingface.co/datasets/CohereLabs/aya_dataset`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/tree/main`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/commit/f9ea04583f02a8f86404ff6c58bf75fe637df8a2`

Fresh public observation:

```text
CANDIDATE_ID=COHERELABS_AYA_DATASET
PUBLIC_REPOSITORY=CohereLabs/aya_dataset
DUE_DILIGENCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
DUE_DILIGENCE_REVISION_ROLE=PUBLIC_SOURCE_METADATA_PIN_ONLY
REVISION_OBSERVED_AS_MAIN_TREE_HEAD=YES
REVISION_VERIFIED_BADGE_OBSERVED=YES
PUBLIC_ACCESS=YES_OBSERVED
DECLARED_LICENSE=Apache-2.0
ADMISSION_DISPOSITION=NOT_ADMITTED
```

The current public dataset card documents human annotations, including original annotations and re-annotations, and separately exposes annotator demographics. Current commandMed governance continues to treat only the original-human-annotation class as a possible future candidate; re-annotations are excluded under the no-model-output-as-authoring-source rule unless governance changes.

Public large-file metadata exposed for the default training parquet:

```text
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
SOURCE_FILE_REMOTE_SIZE_OBSERVED=137_MB
SOURCE_FILE_IDENTITY_ROLE=DUE_DILIGENCE_ONLY
```

The public tree also exposes `data/test-00000-of-00001.parquet`, but this record does not infer a SHA-256 for it from repository history when an exact current pointer identity was not directly established in this due-diligence pass.

```text
AYA_TEST_FILE_EXACT_SHA256=NEEDS_EVIDENCE
AYA_DEMOGRAPHICS_CONFIG_ADMISSION=PROHIBITED_BY_THIS_RECORD
AYA_USER_ID_AS_TRAINING_FEATURE=PROHIBITED_BY_THIS_RECORD
EXACT_ADMISSION_REVISION=NEEDS_SEPARATE_CANONICAL_PIN
```

A later standalone public commit `0e6fedcd23e3301f48de28b4b509234fa80e04e4` was observable as adding a `LICENSE` file with parent `f9ea04583f02a8f86404ff6c58bf75fe637df8a2`; the available fresh public `main` tree and `main` README history surfaces still identified `f9ea045...` as the `main` head. This record therefore does not infer that standalone commit as the current `main` revision.

## 4. Candidate B — OpenAssistant OASST1

Public source:

- `https://huggingface.co/datasets/OpenAssistant/oasst1`
- `https://huggingface.co/api/datasets/OpenAssistant/oasst1`
- `https://huggingface.co/datasets/OpenAssistant/oasst1/tree/main`

Fresh public API observation:

```text
CANDIDATE_ID=OPENASSISTANT_OASST1
PUBLIC_REPOSITORY=OpenAssistant/oasst1
DUE_DILIGENCE_REVISION=fdf72ae0827c1cda404aff25b6603abec9e3399b
DUE_DILIGENCE_REVISION_ROLE=PUBLIC_SOURCE_METADATA_PIN_ONLY
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
DECLARED_LICENSE=Apache-2.0
DOCUMENTED_PROVENANCE=HUMAN_GENERATED_HUMAN_ANNOTATED_ASSISTANT_STYLE_CONVERSATIONS
ADMISSION_DISPOSITION=NOT_ADMITTED
```

The public API exposes record fields including `user_id`, `synthetic`, `model_name`, `deleted`, and labels. Dataset-level human provenance therefore remains insufficient for admission; any later authorized path must fail closed at record level.

Public large-file identities observed without downloading file bytes:

```text
SOURCE_FILE=2023-04-12_oasst_ready.messages.jsonl.gz
SOURCE_FILE_SHA256=286a6e9a5a413b3272ae9c0b5a20d327983dea1c24342ae28cb244a6da65185c
SOURCE_FILE_XET_HASH=dbbf84d48de831f52eeb6e8e3828a363bb9e162e7bb35a9131add2ceef04207f
SOURCE_FILE_REMOTE_SIZE_BYTES=34196309
SOURCE_FILE_IDENTITY_ROLE=DUE_DILIGENCE_ONLY

SOURCE_FILE=data/train-00000-of-00001-b42a775f407cee45.parquet
SOURCE_FILE_SHA256=bbfadf5ed1278ba2208c837fdcad865adf65f5df55d80abadab2745db13fcb5e
SOURCE_FILE_XET_HASH=fe27014395cfbb2fdf141c3eaad59986c4c68dc808bef7369aa2abb85b3d4306
SOURCE_FILE_REMOTE_SIZE_BYTES=39516251
SOURCE_FILE_IDENTITY_ROLE=DUE_DILIGENCE_ONLY

SOURCE_FILE=data/validation-00000-of-00001-134b8fd0c89408b6.parquet
SOURCE_FILE_SHA256=24002597bb13a7edd42d92f773762f25e285f72c31a70449393d0ded1dc7b416
SOURCE_FILE_XET_HASH=b2775f2f0e63212082e66e08fd20ca90f3d228b2e83a5cf991ffe4a8b20fd6c2
SOURCE_FILE_REMOTE_SIZE_BYTES=2080179
SOURCE_FILE_IDENTITY_ROLE=DUE_DILIGENCE_ONLY
```

```text
EXACT_ADMISSION_REVISION=NEEDS_SEPARATE_CANONICAL_PIN
RECORD_LEVEL_HUMAN_ORIGIN_FILTER=NEEDS_AUTHORIZED_EVIDENCE_PATH
RECORD_LEVEL_PRIVACY_PII_PHI_SCREENING=NOT_PERFORMED
CONTAMINATION_ASSESSMENT=NOT_PERFORMED
```

## 5. Candidate C — Databricks Dolly 15k

Public source:

- `https://huggingface.co/datasets/databricks/databricks-dolly-15k`
- `https://huggingface.co/api/datasets/databricks/databricks-dolly-15k`
- `https://huggingface.co/datasets/databricks/databricks-dolly-15k/tree/main`

Fresh public API observation:

```text
CANDIDATE_ID=DATABRICKS_DOLLY_15K
PUBLIC_REPOSITORY=databricks/databricks-dolly-15k
DUE_DILIGENCE_REVISION=bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a
DUE_DILIGENCE_REVISION_ROLE=PUBLIC_SOURCE_METADATA_PIN_ONLY
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
DECLARED_LICENSE=CC-BY-SA-3.0
DOCUMENTED_LANGUAGE=English
DOCUMENTED_RECORD_COUNT=15011
ADMISSION_DISPOSITION=NOT_ADMITTED_CONDITIONAL_RIGHTS
```

The public dataset card continues to describe employee-authored instruction/response records and Wikipedia-derived material in some categories. This pin does not resolve attribution, share-alike, embedded-source, or downstream compatibility requirements.

Public large-file identity observed without downloading file bytes:

```text
SOURCE_FILE=databricks-dolly-15k.jsonl
SOURCE_FILE_SHA256=2df9083338b4abd6bceb5635764dab5d833b393b55759dffb0959b6fcbf794ec
SOURCE_FILE_XET_HASH=63c4dabe683d7254493568d2d3995c0e51abc8528ef3b4936497c538cb501e93
SOURCE_FILE_REMOTE_SIZE_OBSERVED=13.1_MB
SOURCE_FILE_IDENTITY_ROLE=DUE_DILIGENCE_ONLY
```

```text
EXACT_ADMISSION_REVISION=NEEDS_SEPARATE_CANONICAL_PIN
RIGHTS_COMPATIBILITY_DISPOSITION=NEEDS_GOVERNANCE_AND_LICENSE_REVIEW
PRIVACY_PII_PHI_SCREENING=NOT_PERFORMED
CONTAMINATION_ASSESSMENT=NOT_PERFORMED
```

## 6. Due-diligence pins are not admission pins

The following distinction is mandatory:

```text
PUBLIC_DUE_DILIGENCE_REVISION_PIN_PRESENT=YES
PUBLIC_DUE_DILIGENCE_FILE_IDENTITY_EVIDENCE_PRESENT=PARTIAL_BY_SOURCE
ADMISSION_REVISION_PIN_PRESENT=NO
ADMISSION_FILE_IDENTITY_SET_PRESENT=NO
DATASET_SNAPSHOT_PRESENT=NO
CURRICULUM_RECORD_SET_PRESENT=NO
LICENSE_EVIDENCE_PASS_PRESENT=NO
PRIVACY_NON_PHI_PASS_PRESENT=NO
QUARANTINE_PASS_PRESENT=NO
CONTAMINATION_PASS_PRESENT=NO
CONTENT_SCOPE_PASS_PRESENT=NO
```

A later admission path must choose and bind exact bytes under its own authority. It must not silently promote these public due-diligence identities into admitted content identities.

## 7. No execution or materialization occurred

This due-diligence pass used public repository metadata and file-pointer metadata only.

```text
DATASET_DOWNLOAD_PERFORMED=NO
DATASET_BYTE_MATERIALIZATION_PERFORMED=NO
DATASET_FILTERING_PERFORMED=NO
DATASET_ADMISSION_PERFORMED=NO
CURRICULUM_RECORD_CREATION_PERFORMED=NO
PRIVACY_SCREENING_PERFORMED=NO
CONTAMINATION_EXECUTION_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
TRAINING_PERFORMED=NO
SPEND_USD=0
```

## 8. Preserved authority boundary

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=ABSENT
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

The generic continuation/approval instruction does not substitute for the exact founder decision defined by the canonical successor execution decision request, and this identity record does not select that decision.

## 9. Remaining evidence boundary

This record narrows source-identity uncertainty only. The component remains blocked by absent real admitted content and the rest of the exact preflight chain, including as applicable:

- separately authorized data admission;
- exact record-level provenance and human-origin filtering;
- privacy/PII/PHI screening;
- rights/license evidence suitable for the intended use;
- content-scope verification;
- contamination assessment under separate authority;
- exact admitted file/revision identities and `DatasetSnapshot`;
- quarantine evidence;
- exact sentinel and guard identities;
- upstream winner/base-checkpoint binding;
- exact RunManifest and scope binding;
- resource/access/finance/model/weight/device authority;
- exact successor execution authority;
- separately explicit training authority before any gradient-bearing run.

## 10. Public evidence locations used

Observed on 2026-09-02:

### Aya

- `https://huggingface.co/datasets/CohereLabs/aya_dataset/tree/main`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/main/README.md`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/commit/f9ea04583f02a8f86404ff6c58bf75fe637df8a2`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/main/data/train-00000-of-00001.parquet`

### OASST1

- `https://huggingface.co/api/datasets/OpenAssistant/oasst1`
- `https://huggingface.co/datasets/OpenAssistant/oasst1/tree/main`
- `https://huggingface.co/datasets/OpenAssistant/oasst1/blob/main/2023-04-12_oasst_ready.messages.jsonl.gz`
- `https://huggingface.co/datasets/OpenAssistant/oasst1/blob/main/data/train-00000-of-00001-b42a775f407cee45.parquet`
- `https://huggingface.co/datasets/OpenAssistant/oasst1/blob/main/data/validation-00000-of-00001-134b8fd0c89408b6.parquet`

### Dolly

- `https://huggingface.co/api/datasets/databricks/databricks-dolly-15k`
- `https://huggingface.co/datasets/databricks/databricks-dolly-15k/tree/main`
- `https://huggingface.co/datasets/databricks/databricks-dolly-15k/blob/main/databricks-dolly-15k.jsonl`

## 11. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded documentation-only due-diligence artifact.

Before merge, verify exact base/head/diff, public-source claims, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
