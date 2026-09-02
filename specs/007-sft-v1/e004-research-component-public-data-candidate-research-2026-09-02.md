# E004 Research Component Public Data Candidate Research — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Canonical base:** `ae4b5ac2153bd93f75bb15c6f1cd922281995abb`  
**Artifact class:** public-source candidate research only  
**Authority effect:** NONE  
**Data download authority created:** NONE  
**Data admission authority created:** NONE  
**Contamination assessment authority created:** NONE  
**Model execution authority created:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Purpose

Reduce ambiguity around possible future **human-authored, public, non-clinical research-component curriculum sources** without downloading, admitting, transforming, screening, or using any dataset.

This record is upstream public research only. It does not create a DatasetSnapshot, CurriculumRecord, source-authority PASS, license PASS, privacy/non-PHI PASS, contamination PASS, quarantine PASS, scope-verification PASS, RunManifest, execution authority, or training authority.

The controlling execution frontier remains:

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v13-2026-09-02.md
CURRENT_COMPONENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v12-2026-09-02.md
CURRENT_COMPONENT_PREFLIGHT_BLOCKER_PACKET=specs/007-sft-v1/e004-research-component-execution-preflight-blocker-packet-2026-09-02.md
COMPONENT_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
```

## 2. Governing source boundary

Current canonical governance prohibits using model/provider output as an authoring source for real governed content without separately applicable authority:

```text
EXTERNAL_MODEL_OR_PROVIDER_CASE_AUTHORING=NOT_AUTHORIZED
EXTERNAL_MODEL_OR_PROVIDER_PHI_SCREENING=NOT_AUTHORIZED
MODEL_OUTPUT_AS_AUTHORING_SOURCE=NOT_AUTHORIZED
PROVIDER_GENERATION_AUTHORITY=NONE
```

Therefore this research considers only public datasets whose documented provenance includes human-authored or human-annotated material. A dataset-level description is not enough to admit any individual record.

For every future admitted record, the existing Spec 007 contracts still require exact provenance, source/license identity, role/scope classification, verification, split identity, quarantine, contamination state, and content identity.

## 3. Candidate A — CohereLabs Aya Dataset

Public source:

- `https://huggingface.co/datasets/CohereLabs/aya_dataset`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/main/README.md`

Observed public evidence on 2026-09-02:

```text
CANDIDATE_ID=COHERELABS_AYA_DATASET
PUBLIC_REPOSITORY=CohereLabs/aya_dataset
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
DECLARED_LICENSE=Apache-2.0
DOCUMENTED_DATASET_SIZE=204K_HUMAN_ANNOTATED_PROMPT_COMPLETION_PAIRS
DOCUMENTED_LANGUAGE_SCOPE=65_LANGUAGES_71_WITH_DIALECTS_AND_SCRIPTS
ENGLISH_PRESENT=YES
ARABIC_PRESENT=YES_STANDARD_AND_MULTIPLE_VARIETIES
ORIGINAL_ANNOTATION_COUNT=138844_DOCUMENTED
REANNOTATION_COUNT=65270_DOCUMENTED
EXACT_ADMISSION_REVISION=NEEDS_EVIDENCE
EXACT_ADMISSION_FILE_SHA256_SET=NEEDS_EVIDENCE
CANDIDATE_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY
```

The dataset card distinguishes:

1. original annotations — brand-new prompts/completions written by annotators; and
2. re-annotations — human edits of automatically generated prompts/completions.

Because current commandMed governance prohibits model output as an authoring source, only the **original-annotation** class is a candidate for later consideration. Re-annotations remain excluded unless a separate canonical authority/policy changes that boundary.

The public card/viewer currently exposes a naming inconsistency that MUST be resolved against pinned bytes before any filter is treated as executable: prose refers to `original_annotations`, while examples/viewer expose `original-annotations`. No admission filter is frozen from this research document.

Privacy/data-minimization boundary:

```text
AYA_DEMOGRAPHICS_CONFIG_ADMISSION=PROHIBITED_BY_THIS_RESEARCH
AYA_USER_ID_AS_TRAINING_FEATURE=PROHIBITED_BY_THIS_RESEARCH
AYA_ORIGINAL_ANNOTATION_RECORDS_AUTOMATICALLY_NON_PHI=NO
AYA_ORIGINAL_ANNOTATION_RECORDS_AUTOMATICALLY_IN_SCOPE=NO
AYA_ORIGINAL_ANNOTATION_RECORDS_AUTOMATICALLY_CONTAMINATION_CLEAN=NO
```

Any later candidate extraction must exclude the demographics configuration, omit annotator `user_id` from any training representation, and independently screen content for PII/PHI, rights/provenance, excluded clinical capabilities, prohibited evaluation overlap, and contamination.

Research disposition:

```text
AYA_COMPONENT_RESEARCH_PRIORITY=1
RATIONALE=MULTILINGUAL_HUMAN_ORIGINAL_ANNOTATIONS_PLUS_ENGLISH_AND_ARABIC_COVERAGE_PLUS_APACHE_2_0
ADMISSION_DISPOSITION=NOT_ADMITTED
```

## 4. Candidate B — OpenAssistant OASST1

Public source:

- `https://huggingface.co/datasets/OpenAssistant/oasst1`
- `https://huggingface.co/api/datasets/OpenAssistant/oasst1`

Observed public evidence on 2026-09-02:

```text
CANDIDATE_ID=OPENASSISTANT_OASST1
PUBLIC_REPOSITORY=OpenAssistant/oasst1
OBSERVED_PUBLIC_REVISION=fdf72ae0827c1cda404aff25b6603abec9e3399b
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
DECLARED_LICENSE=Apache-2.0
DOCUMENTED_PROVENANCE=HUMAN_GENERATED_HUMAN_ANNOTATED_ASSISTANT_STYLE_CONVERSATIONS
DOCUMENTED_MESSAGES=161443
DOCUMENTED_LANGUAGES=35
ARABIC_PRESENT=YES
DATA_FIELDS_INCLUDE_USER_ID=YES
DATA_FIELDS_INCLUDE_SYNTHETIC_FLAG=YES
DATA_FIELDS_INCLUDE_MODEL_NAME=YES
DATA_FIELDS_INCLUDE_PII_REVIEW_LABEL=YES_WITHIN_LABELS
EXACT_ADMISSION_REVISION=NEEDS_SEPARATE_CANONICAL_PIN
EXACT_ADMISSION_FILE_SHA256_SET=NEEDS_EVIDENCE
CANDIDATE_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY
```

Even though the current public dataset description characterizes OASST1 as human-generated/human-annotated, a later extraction MUST fail closed on the record-level provenance fields rather than rely only on the dataset-level label.

Minimum prospective filters, if separately authorized later, include:

```text
REQUIRE_SYNTHETIC_FALSE=YES
REQUIRE_MODEL_NAME_NULL_OR_EQUIVALENT_HUMAN_PROVENANCE=YES
DROP_USER_ID_FROM_TRAINING_REPRESENTATION=YES
REQUIRE_NOT_DELETED=YES
REQUIRE_SCOPE_CLASSIFICATION=YES
REQUIRE_PII_PHI_SCREENING=YES
REQUIRE_LICENSE_PROVENANCE_BINDING=YES
REQUIRE_CONTAMINATION_ASSESSMENT=YES
```

The exact filter semantics must be frozen against the pinned revision and actual bytes before admission. The presence of Arabic does not establish adequate Arabic quantity, quality, dialect balance, or capability-preservation coverage.

Research disposition:

```text
OASST1_COMPONENT_RESEARCH_PRIORITY=2
RATIONALE=HUMAN_FEEDBACK_MULTILINGUAL_GENERAL_INSTRUCTION_DATA_PLUS_APACHE_2_0_WITH_RECORD_LEVEL_PROVENANCE_FILTERS_REQUIRED
ADMISSION_DISPOSITION=NOT_ADMITTED
```

## 5. Candidate C — Databricks Dolly 15k

Public source:

- `https://huggingface.co/datasets/databricks/databricks-dolly-15k`
- `https://huggingface.co/api/datasets/databricks/databricks-dolly-15k`

Observed public evidence on 2026-09-02:

```text
CANDIDATE_ID=DATABRICKS_DOLLY_15K
PUBLIC_REPOSITORY=databricks/databricks-dolly-15k
OBSERVED_PUBLIC_REVISION=bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a
PUBLIC_ACCESS=YES_OBSERVED
GATED=NO_OBSERVED
DECLARED_LICENSE=CC-BY-SA-3.0
DOCUMENTED_RECORD_COUNT=15011
DOCUMENTED_LANGUAGE=English
DOCUMENTED_AUTHORING=DATBRICKS_EMPLOYEE_HUMAN_AUTHORED
DOCUMENTED_GENERATIVE_AI_AVOIDANCE_INSTRUCTION=YES
DOCUMENTED_WIKIPEDIA_CONTEXT_PRESENT_IN_SOME_CATEGORIES=YES
EXACT_ADMISSION_REVISION=NEEDS_SEPARATE_CANONICAL_PIN
EXACT_ADMISSION_FILE_SHA256_SET=NEEDS_EVIDENCE
CANDIDATE_STATE=PUBLIC_RESEARCH_CANDIDATE_ONLY_CONDITIONAL_RIGHTS
```

The dataset card states that Databricks contributors were explicitly instructed to avoid generative AI when formulating instructions or responses. It also documents Wikipedia-derived reference text in some categories.

The `CC-BY-SA-3.0` license and embedded Wikipedia-derived contexts create a stronger downstream rights/attribution/share-alike review requirement than the Apache-2.0 candidates. No compatibility conclusion is made here.

Research disposition:

```text
DOLLY_COMPONENT_RESEARCH_PRIORITY=3
RIGHTS_DISPOSITION=CONDITIONAL_NEEDS_GOVERNANCE_AND_LICENSE_REVIEW
ARABIC_COVERAGE=NO_DOCUMENTED
ADMISSION_DISPOSITION=NOT_ADMITTED
```

## 6. Cross-candidate scope filters

No candidate is suitable for direct ingestion into `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1` without a separately authorized and evidence-producing admission path.

Any future candidate subset MUST exclude positive target content for every capability excluded by `SP007-RO-001`, including patient-specific diagnosis, treatment, triage, emergency disposition, medication advice, clinical professional decision support, clinical workflow recommendations, medical citation-support claims, Arabic-clinical parity claims, and other declared excluded capabilities.

Out-of-scope clinical content may not silently become gradient-bearing data merely because it occurs inside a broadly licensed public dataset.

```text
PUBLIC_DATASET_LICENSE_ALONE_SUFFICIENT_FOR_ADMISSION=NO
DATASET_LEVEL_HUMAN_LABEL_ALONE_SUFFICIENT_FOR_ADMISSION=NO
PUBLIC_AVAILABILITY_ALONE_SUFFICIENT_FOR_ADMISSION=NO
NON_GATED_STATUS_ALONE_SUFFICIENT_FOR_ADMISSION=NO
RECORD_LEVEL_SCOPE_CLASSIFICATION_REQUIRED=YES
RECORD_LEVEL_PROVENANCE_REQUIRED=YES
RECORD_LEVEL_PRIVACY_SCREENING_REQUIRED=YES
RECORD_LEVEL_CONTAMINATION_STATE_REQUIRED=YES
QUARANTINE_BINDING_REQUIRED=YES
```

## 7. Public-research ranking only

This ranking is a **research prioritization for future due diligence**, not a dataset selection or admission decision:

```text
PUBLIC_RESEARCH_PRIORITY_1=COHERELABS_AYA_ORIGINAL_ANNOTATIONS_ONLY
PUBLIC_RESEARCH_PRIORITY_2=OPENASSISTANT_OASST1_HUMAN_ONLY_FILTERED_SUBSET
PUBLIC_RESEARCH_PRIORITY_3=DATABRICKS_DOLLY_15K_CONDITIONAL_RIGHTS
DATASET_WINNER_SELECTED=NO
DATASET_SNAPSHOT_CREATED=NO
CURRICULUM_RECORDS_CREATED=NO
```

Rationale:

- Aya offers the strongest documented English+Arabic multilingual coverage and a separable original-human-annotation class under Apache-2.0.
- OASST1 offers human-feedback conversational/instruction data under Apache-2.0 but requires strict record-level provenance/privacy/scope filtering and does not establish sufficient Arabic coverage by itself.
- Dolly provides unusually clear documented human authoring/no-generative-AI instructions but is English-only and carries CC-BY-SA/Wikipedia-related rights complexity.

## 8. Exact next evidence required before any admission

For any candidate to advance beyond public research, a separately authorized evidence-producing path must bind at minimum:

```text
EXACT_DATASET_REPOSITORY_ID
EXACT_IMMUTABLE_REVISION
EXACT_SELECTED_FILE_PATHS
EXACT_SELECTED_FILE_SHA256_SET
EXACT_DECLARED_LICENSE_TEXT_IDENTITY
RIGHTS_SCOPE_DISPOSITION
RECORD_SELECTION_RULE_IDENTITY
RECORD_SELECTION_CODE_IDENTITY_IF_ANY
HUMAN_ORIGIN_FILTER_EVIDENCE
NON_CLINICAL_SCOPE_FILTER_EVIDENCE
PII_PHI_SCREENING_EVIDENCE
SOURCE_VERIFICATION_EVIDENCE
SPLIT_ASSIGNMENT
QUARANTINE_VERIFICATION
CONTAMINATION_ASSESSMENT
FINAL_SELECTED_RECORD_CONTENT_IDENTITY_SET
```

No field in this list is satisfied by this document.

## 9. Current effect on E004

```text
PUBLIC_DATA_CANDIDATE_RESEARCH=PREPARED
REAL_COMPONENT_DATASET=ABSENT
REAL_COMPONENT_DATASET_SNAPSHOT=ABSENT
REAL_COMPONENT_CURRICULUM_RECORDS=ABSENT
REAL_COMPONENT_SCOPE_BINDING=ABSENT
REAL_COMPONENT_GUARD_EVIDENCE=ABSENT
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

This research reduces source-candidate ambiguity only. It does not move an evidence gate to PASS.

## 10. Explicit exclusions

This artifact performs or authorizes none of the following:

- dataset download, checkout, materialization, transformation, filtering, or admission;
- storage of public dataset bytes in the repository or an external workspace;
- PII/PHI screening execution;
- contamination assessment;
- source/license/rights acceptance;
- creation of a real DatasetSnapshot or gradient-bearing CurriculumRecord;
- model/source-weight access, conversion, loading, inference, or tournament execution;
- A15 activation;
- training, SFT, LoRA, QLoRA, full fine-tuning, distillation, DPO, GRPO, RL, or QAT;
- Private Gold, PHI, restricted, or gated asset access;
- credential use or provider generation;
- procurement, payment, or spend.

## 11. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded public-research-only documentation artifact. Before merge, verify exact base/head/diff, public-source claims, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation.
