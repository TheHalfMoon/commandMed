# E004 Aya-43 Curriculum Construction Method V1 — 2026-09-04

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Authority:** `E004_FINAL_CURRICULUM_ADMISSION_DECISION_B`
**Canonical authority merge:** `79ced30d21da6be4e087c683e5655166082015e4`
**Method ID:** `AYA_43_HASH_BOUND_CURRICULUM_CONSTRUCTION_V1`
**Artifact class:** pre-result deterministic construction method
**Raw Aya repository persistence:** PROHIBITED
**Remote model/AI record processing:** PROHIBITED
**DatasetSnapshot authority:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Freeze the deterministic method used to construct repository-safe `CurriculumRecord` metadata and research-component content-scope verification records for the exact 43 Aya records authorized by the Founder after corrected Spec 003 `DIRECT_DIGEST` qualification.

This method is frozen before any new content-dependent Aya-43 curriculum output is accepted as canonical evidence. It creates no DatasetSnapshot, rendering output, RunManifest, model execution, conversion, A15 activation, training, credential, or spend authority.

## 2. Exact subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_MANIFEST_FILE_SHA256=bbc7188613f242b428b4ac4cad0297c9dfb31403f6fab146a1a8491a106b2d6e
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
SPEC003_CORRECTED_DIRECT_DIGEST_RESULTS_SHA256=a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
```

The exact 43 admitted record IDs are the `rights_supported_candidate_ids` set in `e004-aya-135-deterministic-admission-projection-v1.json`. Every admitted record must also appear with the same `content_sha256` in the five canonical direct-digest map parts.

## 3. Inputs

The construction implementation may consume only:

1. a locally regenerated exact candidate manifest produced by the canonical `scripts/e004_aya_candidate_pass.py` from the verified Aya payload;
2. `specs/007-sft-v1/e004-aya-135-deterministic-admission-projection-v1.json`;
3. the five canonical `e004-aya-135-candidate-content-digest-map-v1-part-*.json` files;
4. `specs/007-sft-v1/e004-aya-135-qualification-evidence-v1.json`;
5. the current canonical `CurriculumRecord` and research-component content-scope contracts and validators.

The local candidate manifest must match both the frozen semantic SHA-256 and frozen file SHA-256 above before construction continues.

## 4. Raw-data boundary

The local candidate-manifest regeneration step may read only the fields already frozen by `e004_aya_candidate_pass.py`. The construction step itself consumes no raw `inputs` or `targets`.

```text
RAW_AYA_TEXT_IN_CONSTRUCTION_OUTPUT=PROHIBITED
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
USER_ID_READ=FALSE
REMOTE_RECORD_PROCESSING=FALSE
MODEL_OR_AI_SEMANTIC_JUDGE=FALSE
EXTERNAL_PROVIDER_USE=FALSE
```

Only hashes, categorical metadata, contract records, and derived immutable identities may be emitted.

## 5. CurriculumRecord mapping

For each exact admitted candidate `candidate_record_id`, construct one `CurriculumRecord` with:

```text
schema_version=1
record_id=aya-43:<candidate_record_id>
content_sha256=<exact DIRECT_DIGEST content hash>
source_authority_id=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
source_license_id=COHERELABS_AYA_DATASET_F9EA04583F02A8F86404FF6C58BF75FE637DF8A2_APACHE_2_0
source_verification_status=VERIFIED
split_id=VERIFIED_SFT_CURRICULUM_DATA
contamination_status=ASSESSED_CLEAN
review_state=PASS
role_class=LEARNER_RESEARCHER
conversation_structure_id=single-turn-v1
knowledge_placement=DURABLE_WEIGHT_ELIGIBLE
quarantine_disposition=PASS
```

`review_state=PASS` is bound to the already-canonical deterministic FD-008 evidence and corrected Spec 003 eligibility; it is not a human-review claim.

`quarantine_disposition=PASS` is record-level use-policy disposition for the canonical `VERIFIED_SFT_CURRICULUM_DATA` / `TRAIN` source class under the existing quarantine policy. It is not a DatasetSnapshot-wide quarantine verification and does not create DatasetSnapshot authority.

The `source_license_id` is an immutable identifier for the pinned Aya Apache-2.0 dataset-level license evidence. Record-level embedded-source clearance remains supplied by the deterministic evidence that produced the exact 43 admitted set.

### 5.1 Language profile

For `language_code=eng`:

```text
primary_language=en
authored_language=en
translation_state=ORIGINAL
dialect_or_register=GENERAL
```

For `language_code=arb`:

```text
primary_language=ar
authored_language=ar
translation_state=ORIGINAL
dialect_or_register=AR_MSA
```

For both:

```text
code_switch_state=NOT_CLASSIFIED
transliteration_state=NOT_CLASSIFIED
terminology_normalization_id=null
qualified_review_state=PASS
```

`NOT_CLASSIFIED` is deliberately conservative and creates no favorable code-switch or transliteration claim.

### 5.2 Curriculum strata

Start with the exact `verified_target_capability_ids` from the frozen candidate manifest and map them deterministically:

```text
GENERAL_INSTRUCTION_FOLLOWING -> general_instruction_following
GENERAL_ENGLISH_LANGUAGE -> general_english_language
GENERAL_ARABIC_LANGUAGE_NON_CLINICAL -> general_arabic_language_non_clinical
NON_CLINICAL_RESEARCH_LEARNING_FORMATTING -> non_clinical_research_learning_formatting
```

No other capability is expected for the frozen Aya candidate filter. Unknown capability IDs fail closed. The resulting `curriculum_strata` list is lexicographically sorted and must be nonempty.

### 5.3 Canonical record identity

Compute `record_canonical_sha256` with the current canonical `compute_curriculum_record_sha256()` implementation. The hash is self-excluding as defined by the existing validator.

No rendering bundle fields are included. In particular, this method does not create or freeze tokenizer/template/rendered-input identities or token counts.

## 6. Content-scope verification mapping

For every successfully validated CurriculumRecord, construct exactly one research-component content-scope verification:

```text
schema_version=1
verification_id=aya-43-scope:<candidate_record_id>
scope_id=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
record_id=<CurriculumRecord.record_id>
record_canonical_sha256=<CurriculumRecord.record_canonical_sha256>
record_content_sha256=<CurriculumRecord.content_sha256>
verified_target_capability_ids=<exact frozen candidate capability list>
excluded_capability_hits=[]
verification_method=DETERMINISTIC_SCOPE_CLASSIFICATION
disposition=PASS
```

Compute `verification_sha256` using the current canonical `compute_research_component_content_scope_verification_sha256()` implementation.

A PASS here is justified only because the exact candidate-manifest filter and the already-canonical deterministic record evidence both established the bounded `SP007-RO-001` scope for the exact content identity. This step does not inspect or reinterpret raw text.

## 7. Mandatory fail-closed checks

Construction must stop with no canonical output if any of these conditions fails:

- source payload SHA-256 before candidate replay;
- candidate manifest semantic or file SHA-256;
- candidate count or exact 43-set identity;
- any direct-digest candidate/content correspondence;
- any admitted ID not present in the canonical projection and digest map;
- any of the blocked 92 appearing in the output;
- contamination evidence identity or state;
- unsupported language code;
- unknown target capability;
- `CurriculumRecord` validation;
- `CurriculumRecord` canonical hash validation;
- research content-scope verification validation;
- content-scope verification canonical hash validation;
- output count not exactly 43;
- duplicate record or verification identity.

No replacement record may be selected after a failure.

## 8. Repository-safe output bundle

The implementation emits one canonical JSON bundle containing:

- method and authority identities;
- exact input evidence roots and result hashes;
- 43 `CurriculumRecord` objects;
- 43 content-scope verification objects;
- aggregate language/task/capability counts;
- no raw Aya text.

The output bundle SHA-256 is computed over canonical JSON plus one terminating newline and recorded in the execution evidence.

## 9. Local execution and cleanup

Any raw Aya payload needed to regenerate the exact candidate manifest must remain transient. Before parse, the source file SHA-256 must equal `51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06`.

After the currently authorized raw-dependent derivation is complete and the repository-safe bundle is verified, transient raw Aya material must be removed. No raw payload is uploaded to CI for this method.

## 10. Authority boundary after successful construction

Even a fully valid 43-record bundle leaves the next gate closed:

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

A later canonical decision surface is required before DatasetSnapshot construction or freezing.
