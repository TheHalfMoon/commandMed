# Session 10 Q3 — Arabic Selection Evidence Provenance / Source Architecture

Status: ACCEPTED_BOUNDED_CLARIFICATION

This artifact records Session 10 Q3 only. It does not implement corrective maintenance, create an Arabic evaluation payload, authorize Private Gold access, authorize provider generation, authorize benchmark payload access/execution, authorize model execution, or advance Spec 005 beyond CLARIFY.

## 1. Frozen decision

```text
SESSION10_Q3_POLICY=INDEPENDENT_NON_GOLD_IDENTITY_BOUND_ARABIC_PAIRED_MODEL_SELECTION_DEV_PROVENANCE

ARABIC_SELECTION_EVIDENCE_SOURCE_ARCHITECTURE=FROZEN
ARABIC_SELECTION_EVIDENCE_PAYLOAD_CREATED=NO
ARABIC_SELECTION_EVIDENCE_EXACT_SUITE_IDENTITY=NOT_YET_FROZEN
ARABIC_SELECTION_EVIDENCE_CASE_COUNT=NOT_YET_FROZEN
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
```

The selection-safe Arabic-English parity evidence source must be independently governed from Private Gold and must satisfy canonical Spec 001 purpose/quarantine semantics plus Spec 003 lineage, rights, privacy, exact-binding, and contamination requirements before it can become an executable selection source.

## 2. Canonical source class and purpose

The authoritative selection role remains the Session 10 Q2 mapping:

```text
EVIDENCE_ROLE=SELECTION_DEV
PURPOSE=CHECKPOINT_SELECTION
DECLARED_USE=DEVELOPMENT_EVALUATION
```

For canonical Spec 001 quarantine compatibility:

```text
PRIMARY_SELECTION_SOURCE_CLASS=MODEL_SELECTION_DEV_SET
PUBLIC_DEV_COMPONENT_SOURCE_CLASS=PUBLIC_BENCHMARK_DEV_SPLITS
```

A future commandMed-authored Arabic-English paired suite intended to select a backbone or checkpoint must therefore be registered as a `MODEL_SELECTION_DEV_SET` for `CHECKPOINT_SELECTION`; it must not be relabeled as Private Gold, public external evaluation, training data, or a generic test split.

```text
PRIVATE_GOLD_AS_SELECTION_SOURCE=PROHIBITED
PUBLIC_CANONICAL_TEST_SPLIT_AS_SELECTION_SOURCE=PROHIBITED
TRAINING_CORPUS_AS_SELECTION_SOURCE=PROHIBITED
CALIBRATION_SET_AS_PRIMARY_SELECTION_SOURCE=PROHIBITED
REFERENCE_ONLY_AS_SELECTION_SOURCE=PROHIBITED
UNBOUND_AS_SELECTION_SOURCE=PROHIBITED
```

`HELD_OUT_SYNTHETIC_PILOT_CASES` is a canonical `DEV` source class, not automatically a `CHECKPOINT_SELECTION` source class. Q3 does not silently remap it.

## 3. Gold payload firewall

`COMMANDMED_ARABIC_GOLD` remains `PRIVATE_GOLD` and non-selection final-audit evidence.

Selection-suite construction must be content-independent from Private Gold:

```text
PRIVATE_GOLD_CASE_CONTENT_AS_SELECTION_SOURCE=PROHIBITED
PRIVATE_GOLD_CASE_CONTENT_AS_PARENT_ASSET=PROHIBITED
PRIVATE_GOLD_CASE_TEXT_AS_AUTHORING_SEED=PROHIBITED
PRIVATE_GOLD_ANSWER_OR_RUBRIC_AS_AUTHORING_SEED=PROHIBITED
PRIVATE_GOLD_TRANSLATION_AS_SELECTION_CASE=PROHIBITED
PRIVATE_GOLD_PARAPHRASE_AS_SELECTION_CASE=PROHIBITED
PRIVATE_GOLD_DERIVATION_AS_SELECTION_CASE=PROHIBITED
PRIVATE_GOLD_CASE_IDENTITY_LEAKAGE_TO_SELECTION_MANIFEST=PROHIBITED
```

The existing public Gold metadata may constrain coverage taxonomy only:

```text
PRIVATE_GOLD_STRATA_METADATA_MAY_INFORM_COVERAGE_TAXONOMY=YES
PRIVATE_GOLD_METADATA_MAY_AUTHORIZE_CASE_CONTENT_ACCESS=NO
PRIVATE_GOLD_METADATA_MAY_AUTHORIZE_CASE_DERIVATION=NO
```

Current public Arabic Gold strata may therefore remain design anchors such as:

```text
MODERN_STANDARD_ARABIC_CLINICAL
SAUDI_GULF_COLLOQUIAL_PATIENT
ARABIC_ENGLISH_CODE_SWITCHING
LOCAL_MEDICATION_NOMENCLATURE
ARABIC_EMERGENCY_TRIAGE
```

These labels do not reveal or authorize any Gold case payload.

A content firewall is required:

```text
SELECTION_SUITE_AUTHORS_MUST_NOT_REQUIRE_PRIVATE_GOLD_PAYLOAD_ACCESS=YES
SELECTION_SUITE_CONTENT_PROVENANCE_MUST_BE_PROVABLY_NON_GOLD=YES
GOLD_CASE_CONTENT_MUST_NOT_FLOW_INTO_SELECTION_SUITE_AUTHORING=YES
```

Exact human-role assignments for that firewall are not frozen by Q3.

## 4. Preferred source architecture

The preferred baseline provenance is independently authored, non-PHI clinical development evidence:

```text
PREFERRED_ROOT_ORIGIN_TYPE=ORIGINAL
PREFERRED_ROOT_CONTENT=INDEPENDENT_HUMAN_AUTHORED_CLINICAL_NON_PHI
PREFERRED_PRIVATE_GOLD_PARENT_COUNT=0
```

This preference minimizes rights, privacy, contamination, and derivation ambiguity. It does not authorize creation of the cases in this clarification.

A future selection suite may be multi-component. Permissible architectural source paths are:

### 4.1 Original commandMed-authored selection-dev component

```text
ORIGIN_TYPE=ORIGINAL
PURPOSE=CHECKPOINT_SELECTION
SOURCE_CLASS=MODEL_SELECTION_DEV_SET
PRIVATE_GOLD_PARENT=NO
REAL_PATIENT_PHI_SOURCE=NO
```

It must use independently authored fictional/synthetic clinical scenarios or other non-PHI material with resolved contributor/content rights. Q3 does not freeze an exact contributor agreement or license instrument.

### 4.2 Verified public dev component

An existing public source may contribute only when it has an exact development split compatible with `PUBLIC_BENCHMARK_DEV_SPLITS` and can satisfy the paired Arabic-English design.

```text
PUBLIC_DEV_COMPONENT_ALLOWED=CONDITIONAL
PUBLIC_DEV_EXACT_SPLIT_REQUIRED=YES
PUBLIC_DEV_IMMUTABLE_SOURCE_REVISION_REQUIRED=YES
PUBLIC_DEV_EXACT_ARTIFACT_BINDING_REQUIRED=YES
PUBLIC_DEV_RIGHTS_SUPPORTED_FOR_EVALUATION_USE=YES
PUBLIC_DEV_MODIFICATION_OR_TRANSLATION_RIGHTS_REQUIRED_IF_DERIVED=YES
PUBLIC_DEV_TEST_SPLIT_REUSE=PROHIBITED
```

No public source is declared admitted by Q3.

### 4.3 Derived selection-safe component

A derived component may be considered only from non-Gold parents whose exact declared use, rights, privacy, artifact binding, purpose, and contamination evidence permit the derivation and downstream selection use.

```text
DERIVED_COMPONENT_PARENT_LINEAGE_REQUIRED=YES
DERIVED_COMPONENT_PARENT_ASSET_IDS_REQUIRED=YES
DERIVED_COMPONENT_PARENT_RIGHTS_PROPAGATE=YES
DERIVED_COMPONENT_PARENT_PURPOSE_RESTRICTIONS_PROPAGATE=YES
DERIVED_COMPONENT_PRIVATE_GOLD_PARENT=PROHIBITED
DERIVED_COMPONENT_PUBLIC_TEST_PARENT=PROHIBITED_FOR_SELECTION
DERIVED_COMPONENT_UNRESOLVED_PARENT=BLOCKED
```

A narrower parent right cannot be expanded by translation, paraphrase, reformatting, or relabeling.

### 4.4 Synthetic or model-generated component

Synthetic/model-generated evidence is not forbidden architecturally, but it is not authorized by Q3.

```text
SYNTHETIC_OR_MODEL_GENERATED_COMPONENT_CURRENT_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
```

If separately authorized in the future, canonical Spec 003 lineage must bind at least:

```text
parent_asset_ids
generator_identity
generation_config_id
output_use_evidence_uri
exact source/artifact identity
rights_state and rights evidence
privacy state
purpose and quarantine state
contamination disposition
```

Provider output never becomes selection-safe merely because generation is technically available.

## 5. Exact identity requirements

Before a future suite can become selection-eligible it must have exact scientific identity using one canonical Spec 003 binding form:

```text
DIRECT_DIGEST
or
IMMUTABLE_REVISION_LOCATOR
```

A mutable branch, `latest`, landing page, convenience URL, or human-readable version name is insufficient.

At suite/component level the future manifest must bind at least:

```text
suite_id
source_component_id
asset_id
asset_class
record_version
canonical_name
source_identifier
source_uri
source_revision
source_verification_status
source_evidence_uri
declared_use
purpose
access_class
rights_state
rights_evidence_uri
artifact_binding_state
content_sha256_or_exact_artifact_locator
phi_privacy_state
quarantine_state
contamination_state
origin_type
parent_asset_ids_if_applicable
```

The exact final manifest schema remains separate from corrective-maintenance implementation and may add fields without weakening these requirements.

## 6. Rights and license gate

Selection evidence is not usable because a source is merely public or easy to access.

```text
SELECTION_SOURCE_RIGHTS_STATE_REQUIRED=SUPPORTED
SELECTION_SOURCE_RIGHTS_EVIDENCE_REQUIRED=RESOLVED
UNRESOLVED_RIGHTS=BLOCKED
CONDITIONAL_RIGHTS=BLOCKED_UNTIL_RESOLVED_FOR_EXACT_SELECTION_USE
INCOMPATIBLE_RIGHTS=PROHIBITED
```

Where a selection component is translated, adapted, paraphrased, curated, or otherwise derived from an external source:

```text
DERIVATIVE_OR_MODIFICATION_RIGHTS_REQUIRED=YES
TRANSLATION_DOES_NOT_CREATE_NEW_RIGHTS=YES
PUBLIC_VISIBILITY_DOES_NOT_EQUAL_PERMISSION=YES
FRAMEWORK_OR_CODE_LICENSE_DOES_NOT_AUTOMATICALLY_LICENSE_DATA=YES
```

The exact license/rights instruments for a future suite remain unresolved.

## 7. Privacy and PHI gate

The bounded Spec 005 selection suite must remain outside PHI/restricted-data access.

```text
SELECTION_ARABIC_PRIVACY_POLICY=NO_PHI_KNOWN_REQUIRED
RESTRICTED_OR_PHI_SELECTION_SOURCE=PROHIBITED
UNRESOLVED_PRIVACY_SELECTION_SOURCE=BLOCKED
REAL_PATIENT_PHI_ACCESS_AUTHORITY=NONE
```

A `DEIDENTIFIED` label alone is not proof of selection eligibility or rights. Use of a deidentified real-patient source would require separate, explicit privacy/rights evidence and authority and is not authorized by Q3.

The preferred source architecture is independently authored fictional/non-PHI material.

## 8. Paired-task provenance

Arabic parity evidence must remain matched at the root-task level.

For each future Arabic-English pair, provenance must preserve at least:

```text
root_task_id
pair_id
arabic_variant_id
english_variant_id
source_component_id
origin_type
parent_asset_ids_if_applicable
pair_creation_method
clinical_semantic_equivalence_review_identity
```

The two language variants are dependent observations from one root task; they are not two independent cases.

```text
PAIR_ROOT_IDENTITY_SHARED=YES
UNPAIRED_LANGUAGE_COMPARISON_AS_PRIMARY_PARITY_EVIDENCE=PROHIBITED
CLINICAL_SEMANTIC_EQUIVALENCE_REQUIRED=YES
LITERAL_TRANSLATION_REQUIRED=NO
```

Permissible future pair-construction architectures include independent bilingual parallel authoring or human clinical adaptation of a selection-safe source. Q3 does not authorize machine/provider translation.

```text
PROVIDER_ASSISTED_PAIR_CREATION_AUTHORITY=NONE
```

## 9. Contamination gate

A newly authored or newly bound selection suite does not self-certify as contamination-safe.

The Session 7 contamination policy remains controlling:

```text
SPLIT_SPECIFIC_CONTAMINATION_EVIDENCE_REQUIRED=YES
CANDIDATE_OR_CANDIDATE_CORPUS_BINDING_REQUIRED=YES
EXACT_MATCH_AND_SEMANTIC_DIMENSIONS_REQUIRED=YES
SELF_ASSERTED_CLEAN=PROHIBITED
SELF_ASSERTED_NOT_APPLICABLE=PROHIBITED
```

Current Q3 authority remains:

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
```

Therefore no suite can become selection-eligible merely from this architecture document.

## 10. Candidate-neutrality and pre-result freeze

The same exact Arabic-English suite, pair identities, source components, metric mapping, and scoring policy must apply to all primary candidates.

```text
CANDIDATE_SPECIFIC_ARABIC_SELECTION_SUITE=PROHIBITED
CANDIDATE_SPECIFIC_PAIR_SET=PROHIBITED
CANDIDATE_SPECIFIC_SOURCE_COMPONENT=PROHIBITED
POST_RESULT_CASE_REPLACEMENT=PROHIBITED
POST_RESULT_SOURCE_SUBSTITUTION=PROHIBITED
POST_RESULT_PAIR_REMOVAL=PROHIBITED
POST_RESULT_PROVENANCE_RELAXATION=PROHIBITED
```

Any material source/rights/pair/provenance identity change after candidate results requires a fresh canonical evidence identity and fresh evaluation; it cannot silently inherit old results.

## 11. Review requirements before binding

Before a future exact suite can be bound for selection, at minimum the evidence package must demonstrate:

```text
BILINGUAL_CLINICAL_REVIEW_REQUIRED=YES
RIGHTS_PROVENANCE_REVIEW_REQUIRED=YES
PRIVACY_NON_PHI_REVIEW_REQUIRED=YES
PAIR_SEMANTIC_EQUIVALENCE_REVIEW_REQUIRED=YES
CONTAMINATION_EVIDENCE_REVIEW_REQUIRED=YES
```

Exact reviewer identities, credentials, count, quorum, and disagreement protocol remain unresolved under Session 9 governance.

## 12. Current source-admission state

Q3 freezes an architecture, not a dataset admission.

```text
EXACT_SELECTION_SAFE_ARABIC_SUITE_IDENTITY=NOT_YET_FROZEN
EXACT_SELECTION_SAFE_ARABIC_SOURCE_COMPONENTS=NOT_YET_FROZEN
EXACT_SELECTION_SAFE_ARABIC_ARTIFACT_SHA256=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_RIGHTS_EVIDENCE=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_PRIVACY_EVIDENCE=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_CONTAMINATION_EVIDENCE=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_REVIEWER_IDENTITIES=UNRESOLVED
EXACT_SELECTION_SAFE_ARABIC_CASE_COUNT=NOT_YET_FROZEN
EXACT_SELECTION_SAFE_ARABIC_STRATUM_COUNTS=NOT_YET_FROZEN

ARABIC_SELECTION_SOURCE_ADMISSION=BLOCKED_NOT_YET_CONSTRUCTED_OR_BOUND
ARABIC_PARITY_THRESHOLD_FREEZE_READINESS=BLOCKED
CANONICAL_QUALITY_FLOOR_PASS_CURRENTLY_POSSIBLE=NO
SIZE_RANKING_MAY_START=NO
WINNER_SELECTION_MAY_START=NO
```

## 13. Corrective-maintenance interaction

Session 10 Q2's future metrics-v2 corrective maintenance remains a separate dependency.

The source architecture in Q3 does not create `data/eval/metrics-v2.json`, edit the lineage contract, alter quarantine rules, or bind a new evaluation asset.

Future canonical admission requires both:

```text
METRICS_V2_EVIDENCE_ROLE_CONTRACT_CANONICAL=YES
SELECTION_SAFE_ARABIC_SUITE_EXACT_LINEAGE_CANONICAL=YES
```

Neither condition is satisfied by Q3.

## 14. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE

MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE

BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_PAYLOAD_ACCESS_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_EVIDENCE_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE

PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 15. Lifecycle

```text
CLARIFICATION_SESSION_10=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_10_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```
