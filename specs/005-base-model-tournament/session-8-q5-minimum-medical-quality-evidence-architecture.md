# Spec 005 — Session 8 Q5 Minimum Medical-Quality Evidence Architecture

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 8 — Q5  
**Exact predecessor head:** `bed456f9d531681ca914ff005b3a4fea2a43de77`  
**Canonical base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** freeze the minimum evidence architecture that any future primary-selection manifest must satisfy before `QUALITY_FLOOR_THEN_SIZE_FIRST` can produce a canonical winner, without creating benchmark payloads, generating splits, running models, or inventing numeric clinical thresholds.

> This artifact is governance/research only. It does not authorize benchmark payload access, split generation, model or weight access, inference, training, device execution, Private Gold access, provider/API generation, PHI/restricted-data access, gated-asset access, corrective maintenance, Ready, merge, or transition to PLAN.

## 1. Canonical constraints reviewed

The canonical commandMed safety and metric contracts establish that medical quality is not reducible to one MCQ score.

The current hard-gate metrics include:

- `emergency_miss_rate`;
- `medication_critical_error_rate`;
- `selective_risk_at_target_coverage`;
- `citation_entailment_fidelity`;
- `arabic_clinical_parity_gap`;
- `lab_report_field_extraction_accuracy`.

The canonical safety policy also requires system capability coverage for:

- `ARABIC_CLINICAL`;
- `PATIENT_CAREGIVER_SAFETY`;
- `EVIDENCE_GROUNDED_CLINICAL`.

For pending statistical gates, canonical threshold freeze requires all of:

```text
INTENDED_USE_AND_POPULATION
EVALUATION_DESIGN
IDENTITY_BOUND_EVIDENCE
CLINICAL_REVIEW_AUTHORITY
STATISTICAL_RATIONALE
SAMPLE_SIZE_OR_POWER_RATIONALE
```

and `pass_allowed=false` remains canonical until those requirements are satisfied.

Session 8 Q4 additionally freezes that HealthBench and MedXpertQA test assets remain `PUBLIC_EXTERNAL_EVAL`, while the official PubMedQA PQA-L cross-validation pool may become one future selection-dev component only after exact derived-artifact binding and all other gates are satisfied.

## 2. External methodological alignment

Two external clinical-AI reporting frameworks are consistent with, but do not override, the canonical commandMed contracts:

- DECIDE-AI emphasizes intended patient and user populations, safety, user variability, generalizability, and reproducible evaluation of clinical AI systems: `https://www.nature.com/articles/s41591-022-01772-9`.
- TRIPOD+AI states that evaluation data should be distinct from data used for training, hyperparameter tuning, or model selection and should represent the intended-use population: `https://www.bmj.com/content/385/bmj-2023-078378`.

These references support the existing commandMed separation between selection-dev evidence and protected external evaluation; they do not create new authority or numeric thresholds.

## 3. Accepted architecture

`NONCOMPENSABLE_MULTI_LANE_SELECTION_DEV_QUALITY_FLOOR` is frozen:

```text
MINIMUM_MEDICAL_QUALITY_EVIDENCE_ARCHITECTURE=
NONCOMPENSABLE_MULTI_LANE_SELECTION_DEV_QUALITY_FLOOR

QUALITY_FLOOR_IS_SINGLE_BENCHMARK_SCORE=NO
QUALITY_FLOOR_IS_SINGLE_AGGREGATE_SCORE=NO
QUALITY_FLOOR_IS_SINGLE_EXTERNAL_DATASET=NO

PRIMARY_SELECTION_REQUIRES_MULTI_SOURCE_EVIDENCE=YES
REQUIRED_EVIDENCE_LANES_ARE_NONCOMPENSABLE=YES
SIZE_CAN_COMPENSATE_FOR_MISSING_OR_FAILED_QUALITY_LANE=NO
SECONDARY_CAPABILITY_SCORE_CAN_COMPENSATE_FOR_MISSING_OR_FAILED_QUALITY_LANE=NO

QUALITY_FLOOR_THEN_SIZE_FIRST=PRESERVED
SIZE_RANKING_STARTS_ONLY_AFTER_ALL_REQUIRED_QUALITY_AND_HARD_GATES_PASS=YES
```

The phrase “additional broad selection-dev source” from Q4 is clarified to permit an identity-bound **suite/portfolio of selection-dev components** rather than forcing one monolithic benchmark to represent every clinical requirement.

```text
ADDITIONAL_BROAD_SELECTION_DEV_SOURCE_MAY_BE_MULTI_COMPONENT_SUITE=YES
ONE_MONOLITHIC_BENCHMARK_REQUIRED=NO
```

## 4. Required evidence lanes

A future primary-selection evidence architecture must cover each lane below. Exact payload identities, sample sizes, and thresholds remain separately unresolved.

### Lane A — Medical knowledge and biomedical reasoning

Purpose: ensure the candidate demonstrates useful medical/biomedical knowledge and reasoning rather than merely safe refusal behavior.

```text
QUALITY_LANE_A=MEDICAL_KNOWLEDGE_AND_BIOMEDICAL_REASONING
QUALITY_LANE_A_REQUIRED=YES
QUALITY_LANE_A_MAY_INCLUDE_PUBMEDQA_CV=YES_IF_SEPARATELY_BOUND_AND_AUTHORIZED
QUALITY_LANE_A_MAY_BE_SATISFIED_BY_MEDXPERTQA_TEXT_DEV=NO
QUALITY_LANE_A_MAY_USE_PUBLIC_EXTERNAL_TEST_FOR_SELECTION=NO
QUALITY_LANE_A_EXACT_METRICS=NOT_YET_FROZEN
QUALITY_LANE_A_NUMERIC_THRESHOLD=NOT_YET_FROZEN
```

PubMedQA CV may become one component of this lane, but Q4 remains controlling: it cannot be the sole medical-quality floor or sole winner-selection evidence.

### Lane B — Patient/caregiver clinical safety behavior

Purpose: cover dangerous failures where a medically knowledgeable model may still behave unsafely.

Required task classes include, at minimum, emergency recognition and medication-critical behavior.

```text
QUALITY_LANE_B=PATIENT_CAREGIVER_CLINICAL_SAFETY
QUALITY_LANE_B_REQUIRED=YES
QUALITY_LANE_B_REQUIRED_METRICS=emergency_miss_rate,medication_critical_error_rate
QUALITY_LANE_B_SENTINEL_POLICY=ZERO_VIOLATION_MECHANICS_PRESERVED
QUALITY_LANE_B_POPULATION_THRESHOLDS=NOT_YET_FROZEN
QUALITY_LANE_B_CLINICAL_REVIEW_REQUIRED=YES
```

A knowledge score cannot compensate for a decisive emergency or medication sentinel violation.

### Lane C — Uncertainty, abstention, and missing-information behavior

Purpose: require the candidate to avoid unsafe confident answering when information is insufficient or uncertainty is high.

```text
QUALITY_LANE_C=UNCERTAINTY_ABSTENTION_AND_INFORMATION_SEEKING
QUALITY_LANE_C_REQUIRED=YES
QUALITY_LANE_C_REQUIRED_METRIC=selective_risk_at_target_coverage
QUALITY_LANE_C_REQUIRED_BEHAVIOR_STATES=ASK_MORE,ABSTAIN,ESCALATE,EMERGENCY
QUALITY_LANE_C_STATISTICAL_THRESHOLD=NOT_YET_FROZEN
QUALITY_LANE_C_SAMPLE_SIZE_OR_POWER_RATIONALE_REQUIRED=YES
```

The canonical `MISSING_CRITICAL_INFORMATION -> ASK_MORE` and hard escalation/emergency precedence rules remain preserved.

### Lane D — Evidence-grounded clinical behavior

Purpose: prevent medically fluent but unsupported factual clinical claims.

```text
QUALITY_LANE_D=EVIDENCE_GROUNDED_CLINICAL
QUALITY_LANE_D_REQUIRED=YES
QUALITY_LANE_D_REQUIRED_METRIC=citation_entailment_fidelity
QUALITY_LANE_D_REQUIRED_UNAVAILABLE_EVIDENCE_BEHAVIOR=RETRIEVE_EVIDENCE_OR_SAFE_FALLBACK
QUALITY_LANE_D_SENTINEL_POLICY=ZERO_VIOLATION_MECHANICS_PRESERVED
QUALITY_LANE_D_POPULATION_THRESHOLD=NOT_YET_FROZEN
```

No public benchmark score may substitute for identity-bound evidence-grounding qualification.

### Lane E — Arabic-English paired clinical capability

Purpose: prevent an English-strong candidate from entering size ranking without credible Arabic clinical capability.

```text
QUALITY_LANE_E=ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY
QUALITY_LANE_E_REQUIRED=YES
QUALITY_LANE_E_REQUIRED_METRIC=arabic_clinical_parity_gap
QUALITY_LANE_E_REQUIRES_MATCHED_ENGLISH_ARABIC_TASK_DESIGN=YES
QUALITY_LANE_E_REQUIRES_PATIENT_CAREGIVER_COVERAGE=YES
QUALITY_LANE_E_REQUIRES_CLINICAL_PROFESSIONAL_COVERAGE=YES
QUALITY_LANE_E_POST_RESULT_TRANSLATION_OR_CASE_SUBSTITUTION=PROHIBITED
QUALITY_LANE_E_STATISTICAL_THRESHOLD=NOT_YET_FROZEN
QUALITY_LANE_E_SAMPLE_SIZE_OR_POWER_RATIONALE_REQUIRED=YES
```

The exact Arabic source/suite and exact dialect/register composition remain unresolved. This Q5 does not authorize Private Gold access or creation.

### Lane F — Clinical professional / workflow behavior

Purpose: ensure that patient-facing safety evidence does not silently stand in for clinician-facing utility and format discipline.

```text
QUALITY_LANE_F=CLINICAL_PROFESSIONAL_REASONING_AND_WORKFLOW
QUALITY_LANE_F_REQUIRED=YES
QUALITY_LANE_F_REQUIRED_ROLE=CLINICAL_PROFESSIONAL
QUALITY_LANE_F_MAY_INCLUDE_METRIC=clinical_workflow_format_conformance
QUALITY_LANE_F_EXACT_METRIC_SET=NOT_YET_FROZEN
QUALITY_LANE_F_NUMERIC_THRESHOLD=NOT_YET_FROZEN
```

This lane is part of the broad quality evidence architecture even when an individual metric is not itself a canonical hard gate.

### Lane G — Lab/document structured qualification

Purpose: preserve the canonical lab-document hard gate without incorrectly turning modality-specific evidence into the primary winner-ranking score.

```text
QUALITY_LANE_G=LAB_DOCUMENT_STRUCTURED_QUALIFICATION
QUALITY_LANE_G_REQUIRED_FOR_FULL_SAFETY_QUALIFICATION=YES
QUALITY_LANE_G_REQUIRED_METRIC=lab_report_field_extraction_accuracy
QUALITY_LANE_G_PRIMARY_WINNER_RANKING_SCORE=NO
QUALITY_LANE_G_STATISTICAL_THRESHOLD=NOT_YET_FROZEN
QUALITY_LANE_G_SAMPLE_SIZE_OR_POWER_RATIONALE_REQUIRED=YES
```

This is consistent with `COMMON_CORE_PRIMARY_RANKING`: modality/document qualification may be mandatory as a hard qualification condition without becoming the common-core primary ranking score.

## 5. Required role and language coverage

The future selection-dev portfolio must explicitly bind coverage rather than infer it from benchmark branding.

```text
SELECTION_DEV_REQUIRED_ROLE_COVERAGE=PATIENT_CAREGIVER,CLINICAL_PROFESSIONAL,LEARNER_RESEARCHER
SELECTION_DEV_REQUIRED_CLINICAL_LANGUAGES=en,ar

PATIENT_CAREGIVER_ROLE_MAY_BE_INFERRED_FROM_GENERIC_MEDICAL_QA=NO
CLINICAL_PROFESSIONAL_ROLE_MAY_BE_INFERRED_FROM_GENERIC_MEDICAL_QA=NO
LEARNER_RESEARCHER_ROLE_MAY_BE_INFERRED_FROM_PATIENT_SAFETY_CASES=NO
ARABIC_CAPABILITY_MAY_BE_INFERRED_FROM_MULTILINGUAL_LABEL=NO
```

Exact per-role and per-language sample counts remain unresolved pending evidence design and sample-size/power rationale.

## 6. Permitted future source classes

Q5 freezes source-class rules only; it does not create or access a source.

```text
SELECTION_DEV_ALLOWED_SOURCE_CLASS_1=VERIFIED_PUBLIC_DEV_OR_CV_SPLIT
SELECTION_DEV_ALLOWED_SOURCE_CLASS_2=IDENTITY_BOUND_SYNTHETIC_OR_CURATED_DEV_SUITE

PUBLIC_EXTERNAL_EVAL_AS_SELECTION_SOURCE=PROHIBITED
PRIVATE_GOLD_AS_SELECTION_SOURCE=PROHIBITED
TRAIN_SPLIT_AS_SELECTION_SOURCE=PROHIBITED
REFERENCE_ONLY_AS_SELECTION_SOURCE=PROHIBITED
UNBOUND_ASSET_AS_SELECTION_SOURCE=PROHIBITED
GATED_ASSET_WITHOUT_SEPARATE_AUTHORIZATION_AS_SELECTION_SOURCE=PROHIBITED
PHI_OR_RESTRICTED_PATIENT_DATA_AS_SELECTION_SOURCE=PROHIBITED
```

Any future synthetic or curated development suite must still satisfy provenance, rights/privacy, identity, clinical-review, contamination, and purpose-binding requirements. Q5 grants no authority to generate such a suite with an external provider.

## 7. Exact manifest requirements before candidate execution

Every required selection-dev component must be bound before model results are observed.

```text
EACH_SELECTION_DEV_COMPONENT_REQUIRES_EXACT_SOURCE_IDENTITY=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_IMMUTABLE_REVISION_OR_ARTIFACT_DIGEST=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_PURPOSE_BINDING=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_LICENSE_AND_ACCESS_RESOLUTION=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_CONTAMINATION_DISPOSITION=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_METRIC_MAPPING=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_SCORING_DIRECTION=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_ROLE_AND_LANGUAGE_MAPPING=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_SAMPLE_SIZE_OR_POWER_RATIONALE_WHERE_STATISTICAL_CLAIM_IS_USED=YES
EACH_SELECTION_DEV_COMPONENT_REQUIRES_CLINICAL_REVIEW_AUTHORITY_WHERE_CLINICAL_ADJUDICATION_IS_USED=YES

SAME_EXACT_SELECTION_DEV_MANIFEST_ACROSS_PRIMARY_CANDIDATES=YES
CANDIDATE_SPECIFIC_CASE_SUBSETS=PROHIBITED
CANDIDATE_SPECIFIC_SCORING_RULES=PROHIBITED
POST_RESULT_CASE_ADDITION_OR_REMOVAL=PROHIBITED
POST_RESULT_WEIGHTING_CHANGE=PROHIBITED
POST_RESULT_METRIC_SUBSTITUTION=PROHIBITED
```

## 8. Aggregation and non-compensation semantics

Q5 intentionally does not freeze a numeric composite score.

```text
GLOBAL_MEDICAL_QUALITY_COMPOSITE_SCORE=NOT_FROZEN
WEIGHTED_AVERAGE_ACROSS_REQUIRED_HARD_GATES=PROHIBITED_AS_PASS_SUBSTITUTE

ANY_REQUIRED_HARD_GATE_FAIL=QUALITY_FLOOR_FAIL
ANY_REQUIRED_HARD_GATE_INCOMPLETE=QUALITY_FLOOR_INCOMPLETE
ANY_REQUIRED_SELECTION_LANE_WITH_UNRESOLVED_REQUIRED_EVIDENCE=QUALITY_FLOOR_INCOMPLETE

QUALITY_FLOOR_FAIL_OR_INCOMPLETE_CAN_ENTER_SIZE_RANKING=NO
QUALITY_FLOOR_FAIL_OR_INCOMPLETE_CAN_BE_CANONICAL_SELECTED_WINNER=NO

NO_COMPLETE_QUALITY_FLOOR_PASS=TOURNAMENT_NO_SELECTION
```

A later clarification may freeze predeclared secondary ranking metrics only after the noncompensable quality floor is fully specified.

## 9. Current state after Q5

Q5 closes the architecture question but does not freeze an executable manifest.

```text
MINIMUM_MEDICAL_QUALITY_EVIDENCE_ARCHITECTURE=
NONCOMPENSABLE_MULTI_LANE_SELECTION_DEV_QUALITY_FLOOR

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED

PUBMEDQA_CV_DERIVED_ARTIFACT_BINDING=NOT_YET_PERFORMED
ADDITIONAL_BROAD_SELECTION_DEV_EXACT_SOURCE=NOT_YET_FROZEN
SELECTION_DEV_EXACT_METRIC_MAPPING=NOT_YET_FROZEN
SELECTION_DEV_EXACT_SAMPLE_SIZE_OR_POWER_RATIONALE=NOT_YET_FROZEN
SELECTION_DEV_EXACT_CLINICAL_REVIEW_AUTHORITY=NOT_YET_FROZEN
SELECTION_DEV_CONTAMINATION_GATES=NOT_RESOLVED

MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
CANONICAL_QUALITY_FLOOR_PASS_CURRENTLY_POSSIBLE=NO
```

The existing pending clinical/statistical gates remain `NO_PASS_UNTIL_FROZEN`.

## 10. Q4 research-boundary exception remains historical only

Session 8 Q4 recorded an unintended read-only HealthBench Professional dataset-viewer preview. Q5 does not repeat or expand that access.

```text
Q4_UNINTENDED_PAYLOAD_PREVIEW_OCCURRED=YES
Q5_NEW_BENCHMARK_PAYLOAD_ACCESS_PERFORMED=NO
Q5_BENCHMARK_PAYLOAD_DOWNLOAD_PERFORMED=NO
Q5_BENCHMARK_PAYLOAD_COPY_OR_CACHE_CREATED=NO
Q5_BENCHMARK_PAYLOAD_EXECUTION_PERFORMED=NO
```

## 11. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0
PLAN_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PUBMEDQA_SPLIT_GENERATION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 12. Session 8 closeout

Acceptance of Q5 completes only bounded Session 8:

```text
CLARIFICATION_SESSION_8=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_8_STATUS=COMPLETE_BOUNDED_SESSION

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

Session 8 completion does not complete the overall CLARIFY lifecycle, does not freeze the exact primary-selection manifest, does not authorize corrective maintenance, and does not authorize transition to PLAN.

## 13. Remaining clarification scope

Remaining clarification includes, at minimum:

- exact identity and governance path for the additional broad selection-dev suite/components;
- PubMedQA CV derived-artifact binding governance and exact fold/aggregation role;
- exact metric mappings for legitimate selection-dev components;
- exact intended-use/population statements for pending statistical gates;
- exact evaluation design, clinical review authority, statistical rationale, and sample-size/power rationale;
- exact numeric clinical/statistical thresholds once separately justified;
- contamination-assessment access route and actual candidate-specific contamination evidence;
- exact component rights/privacy/license evidence;
- exact llama.cpp/build/tokenizer/instrumentation identities;
- numeric performance thresholds and watchdog/failure-signal identities;
- thermal/energy signal identities and calibration details;
- secondary ranking order;
- fresh independent exact-head review;
- final clarification lifecycle closure.
