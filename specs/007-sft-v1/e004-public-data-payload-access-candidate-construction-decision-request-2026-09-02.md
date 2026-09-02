# E004 Public Data Payload Access and Candidate Construction Decision Request — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Current global frontier:** `e004-registry-current-state-reconciliation-v15-2026-09-02.md`  
**Canonical base:** `013973e948b66a4f1c9a0cb4373d6cb32b381a4c`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Dataset download performed:** NO  
**Dataset materialization performed:** NO  
**Candidate construction performed:** NO  
**Data admission performed:** NO  
**Contamination assessment performed:** NO  
**Model execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Purpose

Resolve the next dependency-safe authority gap identified by V15: permit or decline one narrowly bounded public/ungated dataset payload access and deterministic **non-admitting** candidate-construction pass for the already-canonical priority-1 public source.

This surface does not select data for training and does not create admission, contamination, model, conversion, A15, or training authority.

Controlling records include:

- `e004-research-component-public-data-candidate-research-2026-09-02.md`;
- `e004-research-component-public-data-source-identity-pins-2026-09-02.md`;
- `e004-research-component-execution-preflight-blocker-packet-2026-09-02.md`;
- `e004-successor-scope-execution-authorization-founder-decision-2026-09-02.md`;
- `e004-registry-current-state-reconciliation-v15-2026-09-02.md`;
- Spec 003 data/license/provenance contracts.

## 2. Why one source only

Canonical public research ranks the candidate sources:

```text
PUBLIC_DATA_CANDIDATE_PRIORITY_1=CohereLabs/aya_dataset
PUBLIC_DATA_CANDIDATE_PRIORITY_2=OpenAssistant/oasst1
PUBLIC_DATA_CANDIDATE_PRIORITY_3=databricks/databricks-dolly-15k
```

Ponytail/YAGNI therefore requires the smallest useful first access subject rather than authorizing all candidate datasets at once.

This decision surface binds only the priority-1 Aya source. OASST1 and Dolly remain metadata-only candidates unless separately authorized later.

## 3. Exact Aya payload subject

The canonical due-diligence record already binds the public source metadata identity:

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

The payload identity above is the only dataset byte subject eligible under Decision B below.

No mutable `main`, latest file, alternate parquet, test parquet, demographics configuration, mirror, derivative, or newer source revision is authorized by this surface.

## 4. Candidate-content boundary

Canonical source research distinguishes original human annotations from re-annotations involving automatically generated material.

Current commandMed governance therefore permits only the original-human-annotation class to remain a candidate.

A Decision B pass would be required to fail closed until the downloaded exact pinned bytes establish the exact field/value semantics used by that revision.

```text
ORIGINAL_HUMAN_ANNOTATION_CLASS=CANDIDATE
REANNOTATION_CLASS=EXCLUDED
DEMOGRAPHICS_CONFIG=EXCLUDED
MODEL_OUTPUT_AS_AUTHORING_SOURCE=NOT_AUTHORIZED
USER_ID_AS_TRAINING_FEATURE=PROHIBITED
```

No filter string is frozen by this request before the exact bytes are inspected.

## 5. Decision classes

The Founder must select exactly one class after this decision surface becomes canonical.

### `E004_PUBLIC_DATA_ACCESS_DECISION_A` — preserve current state

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_A
AYA_PAYLOAD_ACCESS_AUTHORITY=NONE
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=NONE
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=NONE
AYA_PRIVACY_SCREENING_AUTHORITY=NONE
```

Effect: the Aya source remains public metadata due diligence only.

### `E004_PUBLIC_DATA_ACCESS_DECISION_B` — authorize exact Aya read-only candidate-construction pass

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B authorizes only the bounded evidence work in the next section.

## 6. Decision B permitted actions

After canonical capture of Decision B, the exact bounded pass may:

1. download/materialize only the exact public Aya train parquet bound in §3;
2. compute SHA-256 over the downloaded bytes and require exact equality with the canonical source identity before parsing;
3. abort and delete the local payload if the SHA-256 does not match;
4. inspect the exact pinned schema/config fields needed to resolve the original-annotation naming/field ambiguity;
5. identify records belonging to the original-human-annotation class using semantics proven from the exact pinned bytes and source metadata;
6. exclude every re-annotation record and every record whose human-origin state cannot be established fail closed;
7. exclude demographics data and prevent `user_id` from entering any candidate training representation;
8. apply the exact `SP007-RO-001` non-clinical scope boundary and reject records that positively target excluded patient/caregiver or clinical-professional capabilities;
9. perform local deterministic PII/PHI risk screening and bounded human inspection where necessary without sending content to an external model/provider/API;
10. compute immutable candidate record/content identities for records surviving the bounded filters;
11. produce aggregate counts, reason-coded exclusions, source/schema observations, and candidate lineage metadata;
12. produce candidate Spec 003 lineage evidence with unresolved dimensions explicitly retained as unresolved;
13. retain only repository-safe derived metadata/manifests/evidence records after verification;
14. delete or leave outside canonical repository source the raw downloaded dataset payload and any transient sensitive inspection material.

## 7. Decision B is explicitly non-admitting

Decision B does not authorize an `ELIGIBLE` or admitted result.

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_THIS_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
```

Any candidate lineage record produced by the pass must remain `BLOCKED`, `REFERENCE_ONLY`, `NEEDS_EVIDENCE`, or another truthful non-admitted state wherever a required dimension is unresolved.

Spec 003 admission remains evaluator-owned. The pass may not write a caller-controlled `ELIGIBLE` result.

## 8. Privacy boundary

The source is public, but public availability does not prove that every record is free of PII/PHI or otherwise suitable for optimization.

Decision B would permit local screening only for the exact candidate-construction purpose.

```text
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
PRIVATE_OR_RESTRICTED_DATA_ACCESS=PROHIBITED
PHI_COLLECTION_OR_ENRICHMENT=PROHIBITED
IDENTITY_RECONSTRUCTION=PROHIBITED
USER_ID_PERSISTENCE_IN_CANDIDATE_REPRESENTATION=PROHIBITED
```

Any record with unresolved privacy risk remains excluded from candidate construction or marked fail closed according to the controlling evidence contract.

## 9. Rights/license boundary

The source currently declares Apache-2.0, but this request does not convert a source declaration into a complete downstream rights/admission PASS.

The bounded pass may record and bind exact license/source evidence available for the pinned revision. It may not make legal claims beyond the evidence or infer rights for embedded/record-level material merely from the dataset-level license declaration.

```text
LICENSE_DECLARATION_RESEARCH_EVIDENCE=PERMITTED
LICENSE_COMPATIBILITY_ADMISSION_PASS=NOT_CREATED
LEGAL_ADVICE=NO
```

## 10. Contamination remains separately gated

Decision B does not authorize benchmark/holdout contamination assessment.

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
```

Candidate records may be constructed with contamination explicitly unresolved, but they cannot become admitted optimization content until the separately applicable contamination path is satisfied.

## 11. No model, conversion, or training expansion

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION_FROM_THIS_DECISION=NONE
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

Decision B here is a data-evidence construction authority only. It does not cause model execution to become preflight-eligible.

## 12. No protected, gated, credentialed, or paid resources

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The bounded pass must abort rather than request credentials, accept new gated terms, incur incremental spend, or switch to a paid provider.

## 13. Persistence and repository boundary

Decision B would authorize ephemeral local materialization only.

Raw Aya payload bytes must not be committed to canonical repository source.

Repository persistence is limited to source-safe derived artifacts such as:

- exact source/hash verification evidence;
- exact schema/field observations;
- deterministic filter definitions after the pinned schema is established;
- aggregate inclusion/exclusion counts;
- reason-code summaries;
- content hashes/record identities that do not reveal disallowed raw personal content;
- lineage/admission-evaluator input records with unresolved states preserved;
- bounded execution reports.

Any derived artifact containing raw PII/PHI or disallowed personal identifiers must remain outside canonical source.

## 14. Failure conditions

The pass must fail closed without substitution if any of the following occurs:

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

Failure does not authorize switching to OASST1, Dolly, another Aya revision, another file, or another access route.

## 15. Relationship to E004

Even successful completion of the bounded pass would not complete E004.

At most it can create exact candidate-source evidence needed for later data admission work.

```text
E004_COMPLETE_FROM_PUBLIC_DATA_ACCESS_DECISION_B=NO
COMPONENT_E004_COMPLETE_FROM_PUBLIC_DATA_ACCESS_DECISION_B=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
```

## 16. ChatGPT recommendation for Founder review

```text
CHATGPT_PUBLIC_DATA_ACCESS_POSITION=RECOMMEND_E004_PUBLIC_DATA_ACCESS_DECISION_B
RATIONALE_1=AYA_IS_THE_CANONICAL_PRIORITY_1_PUBLIC_DATA_CANDIDATE
RATIONALE_2=THE_EXACT_PUBLIC_PAYLOAD_IDENTITY_IS_ALREADY_CANONICALLY_PINNED
RATIONALE_3=THE_PASS_IS_READ_ONLY_NON_ADMITTING_ZERO_SPEND_AND_NO_CREDENTIAL
RATIONALE_4=THE_PASS_CAN_REDUCE_REAL_SCHEMA_PROVENANCE_PRIVACY_AND_SCOPE_UNCERTAINTY_WITHOUT_TRAINING_OR_MODEL_EXECUTION
RATIONALE_5=CONTAMINATION_AND_FINAL_ADMISSION_REMAIN_SEPARATELY_FAIL_CLOSED
```

This recommendation is not a Founder decision.

## 17. Exact Founder response required

To preserve the current state:

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_A
```

To authorize the bounded exact Aya candidate-construction pass:

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
```

A broad continuation instruction, generic approval, repository merge, or statement that all ordinary approvals are granted is not substituted for this exact payload-access decision.

The operative response must occur after this decision surface is canonical and must be captured in a separate decision record before any dataset payload is downloaded or materialized.

## 18. Current state until an operative decision is canonical

```text
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=ABSENT
AYA_PAYLOAD_ACCESS_AUTHORITY=NONE
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=NONE
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=NONE
AYA_PRIVACY_SCREENING_AUTHORITY=NONE
DATA_ADMISSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 19. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded decision-request artifact.

Before merge, verify exact base/head/diff, canonical Aya source identity correspondence, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
