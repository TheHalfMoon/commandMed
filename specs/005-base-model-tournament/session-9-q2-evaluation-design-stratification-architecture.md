# Spec 005 — Session 9 Q2 Evaluation-Design and Population-Stratification Architecture

**Lifecycle:** CLARIFY ONLY  
**Evidence capture date:** 2026-08-23  
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Predecessor PR head:** `5031e4cd2b99566a2fcf2c4bf7607827b26bcb19`

> This artifact freezes evaluation-design structure only. It does not create or access benchmark payloads, generate splits, define sample sizes or power values, define numeric clinical/statistical thresholds, run models, access model weights, access Private Gold, access PHI/restricted data, authorize corrective maintenance, or advance to PLAN.

## 1. Q2 decision

```text
SESSION9_Q2_POLICY=STRATUM_FIRST_PAIRED_CANDIDATE_NEUTRAL_EVALUATION_DESIGN

EVALUATION_DESIGN_ARCHITECTURE=FROZEN_STRUCTURALLY
EXACT_SAMPLE_COUNTS=NOT_YET_FROZEN
EXACT_POWER_TARGETS=NOT_YET_FROZEN
EXACT_CONFIDENCE_INTERVAL_METHODS=NOT_YET_FROZEN
EXACT_MULTIPLICITY_METHOD=NOT_YET_FROZEN
EXACT_CROSS_STRATUM_AGGREGATION_WEIGHTS=NOT_YET_FROZEN
NUMERIC_CLINICAL_STATISTICAL_THRESHOLDS=NOT_YET_FROZEN
```

The purpose of this decision is to prevent a later evaluation from becoming valid merely because one large or easy subgroup dominates a pooled score.

The design is candidate-neutral and result-independent. It must be frozen before candidate results can be used for selection.

## 2. Canonical basis

This clarification preserves the canonical rules already established by Specs 001–002 and Session 8–9 Q1:

1. hard-gate failures cannot be averaged away by high mean performance;
2. incomplete required hard-gate evidence prevents PASS;
3. population/statistical thresholds require intended-use/population, evaluation design, identity-bound evidence, clinical review authority, statistical rationale, and sample-size/power rationale;
4. Private Gold is prohibited for backbone/checkpoint selection;
5. Spec 005 uses a noncompensable multi-lane quality architecture;
6. the intended evaluation population is defined through role, language, and use-context task populations rather than a claimed real-world clinical cohort.

## 3. Required design axes

For every executable selection-dev component, the evaluation manifest must support the following design axes where applicable to that lane:

```text
REQUIRED_DESIGN_AXIS_1=QUALITY_LANE
REQUIRED_DESIGN_AXIS_2=ROLE
REQUIRED_DESIGN_AXIS_3=LANGUAGE_WHERE_APPLICABLE
REQUIRED_DESIGN_AXIS_4=USE_CONTEXT_OR_TASK_STRATUM
REQUIRED_DESIGN_AXIS_5=SOURCE_OR_COMPONENT_IDENTITY
```

The exact required values of `ROLE`, `LANGUAGE`, and `USE_CONTEXT_OR_TASK_STRATUM` are lane-specific and inherit Session 9 Q1.

Future demographic, disease, specialty, severity, geographic, dialect, or other population axes may be added only when separately frozen with an evidence basis.

```text
UNFROZEN_POPULATION_AXIS_MAY_BE_SILENTLY_ASSUMED=NO
UNFROZEN_POPULATION_AXIS_MAY_BE_USED_FOR_POST_RESULT_REWEIGHTING=NO
```

## 4. Unit of analysis

### 4.1 Atomic case identity

The default evaluation unit is one identity-bound evaluation case or scenario, not one output token, one rubric atom, or one model turn.

```text
DEFAULT_UNIT_OF_ANALYSIS=IDENTITY_BOUND_EVALUATION_CASE

EACH_CASE_REQUIRES_STABLE_CASE_ID=YES
EACH_CASE_REQUIRES_SOURCE_COMPONENT_ID=YES
EACH_CASE_REQUIRES_LANE_ASSIGNMENT=YES
EACH_CASE_REQUIRES_ROLE_ASSIGNMENT_WHERE_APPLICABLE=YES
EACH_CASE_REQUIRES_LANGUAGE_ASSIGNMENT_WHERE_APPLICABLE=YES
EACH_CASE_REQUIRES_USE_CONTEXT_OR_TASK_STRATUM=YES
```

### 4.2 Multi-turn scenarios

A multi-turn clinical dialogue or information-acquisition scenario is one scenario-level unit unless a future metric contract explicitly defines a different unit.

```text
MULTI_TURN_DEFAULT_UNIT=SCENARIO_NOT_INDIVIDUAL_TURN
TURNS_FROM_ONE_SCENARIO_COUNT_AS_INDEPENDENT_CASES=NO
```

Per-turn evidence may be retained diagnostically, but turns from the same scenario must not silently inflate the sample size.

### 4.3 Multiple metrics on the same case

One case scored under multiple metrics remains one underlying case for independence and sample-size reasoning.

```text
MULTIPLE_METRICS_ON_SAME_CASE_CREATE_MULTIPLE_INDEPENDENT_CASES=NO
DEPENDENCY_MUST_BE_RECORDED=YES
```

## 5. Root-case and derived-variant dependency

When multiple evaluation items derive from one underlying clinical scenario, source record, translated prompt, paraphrase, modality transformation, or controlled perturbation, they must share a root-case identity.

```text
ROOT_CASE_ID_REQUIRED_FOR_KNOWN_DERIVED_VARIANTS=YES
DERIVED_VARIANTS_FROM_ONE_ROOT_COUNT_AS_INDEPENDENT_CASES=NO
DERIVED_VARIANT_DEPENDENCY_MUST_BE_RECORDED=YES
```

This prevents apparent sample-size growth through repeated variants of the same underlying scenario.

The exact statistical treatment of clustered variants is not frozen by Q2.

```text
EXACT_CLUSTER_ROBUST_STATISTICAL_METHOD=NOT_YET_FROZEN
```

## 6. Arabic-English paired evaluation

Lane E is explicitly paired.

The analysis unit for Arabic-English parity is the matched task pair, not two unrelated language items.

```text
LANE_E_UNIT_OF_ANALYSIS=MATCHED_ARABIC_ENGLISH_TASK_PAIR
LANE_E_PAIR_ID_REQUIRED=YES
LANE_E_ARABIC_AND_ENGLISH_VARIANTS_SHARE_ROOT_TASK_ID=YES
LANE_E_UNPAIRED_LANGUAGE_COMPARISON_AS_PRIMARY_PARITY_EVIDENCE=PROHIBITED
```

A valid pair must preserve the intended clinical task and decision-relevant semantics while allowing linguistically appropriate adaptation.

```text
LANE_E_LITERAL_TRANSLATION_REQUIRED=NO
LANE_E_CLINICAL_SEMANTIC_EQUIVALENCE_REQUIRED=YES
LANE_E_PAIR_CONSTRUCTION_REVIEW_REQUIRED_BEFORE_EXECUTION=YES
EXACT_PAIR_REVIEW_AUTHORITY=NOT_YET_FROZEN
```

If one side of a required pair is missing, invalid, or unevaluable, that pair is incomplete for parity evidence.

```text
ONE_SIDE_MISSING_FROM_REQUIRED_PAIR=PAIR_INCOMPLETE
PAIR_INCOMPLETE_MAY_BE_RECAST_AS_ENGLISH_ONLY_OR_ARABIC_ONLY_PARITY_EVIDENCE=NO
```

Exact Arabic dialect proportions remain unfrozen.

## 7. Candidate-neutral manifest requirement

All comparable PRIMARY candidates must be evaluated against the same exact selection-dev case identities and the same frozen design labels.

```text
SAME_EXACT_CASE_MANIFEST_ACROSS_PRIMARY_CANDIDATES=REQUIRED
SAME_STRATUM_ASSIGNMENTS_ACROSS_PRIMARY_CANDIDATES=REQUIRED
SAME_METRIC_MAPPING_ACROSS_PRIMARY_CANDIDATES=REQUIRED
SAME_PAIR_IDENTITIES_ACROSS_PRIMARY_CANDIDATES=REQUIRED
SAME_FOLD_IDENTITIES_WHERE_APPLICABLE=REQUIRED

CANDIDATE_SPECIFIC_CASE_SUBSET=PROHIBITED
CANDIDATE_SPECIFIC_STRATUM_REDEFINITION=PROHIBITED
CANDIDATE_SPECIFIC_PAIRING=PROHIBITED
CANDIDATE_SPECIFIC_METRIC_MAPPING=PROHIBITED
```

A candidate failure or missing output does not authorize removing that item from the other candidates.

## 8. Stratum-first reporting

Every required stratum must be reported separately before any cross-stratum aggregate is interpreted.

```text
PRIMARY_REPORTING_ORDER=STRATUM_FIRST_THEN_ANY_PREDECLARED_AGGREGATE
REQUIRED_STRATUM_RESULT_VISIBILITY=MANDATORY
POOLED_SCORE_WITHOUT_REQUIRED_STRATUM_RESULTS=INSUFFICIENT_EVIDENCE
```

A pooled micro-average is not allowed to hide missing or adverse evidence in a required stratum.

```text
POOLED_MICRO_SCORE_CAN_REPLACE_REQUIRED_STRATUM_EVIDENCE=NO
LARGE_STRATUM_CAN_DILUTE_REQUIRED_SMALLER_STRATUM_FAILURE=NO
```

Where a canonical hard gate is evaluated within multiple required strata:

```text
OBSERVED_HARD_GATE_FAILURE_IN_ANY_REQUIRED_APPLICABLE_STRATUM_CANNOT_BE_AVERAGED_AWAY=YES
MISSING_REQUIRED_HARD_GATE_STRATUM_EVIDENCE_PREVENTS_PASS=YES
```

This preserves canonical hard-gate dominance.

## 9. Cross-stratum aggregation governance

Q2 does not freeze one universal macro-average or one universal weighting scheme.

Any future cross-stratum aggregate used for selection must satisfy all of the following:

```text
CROSS_STRATUM_AGGREGATION_MUST_BE_PREDECLARED_BEFORE_CANDIDATE_RESULTS=YES
CROSS_STRATUM_AGGREGATION_WEIGHTS_MUST_BE_CANDIDATE_NEUTRAL=YES
CROSS_STRATUM_AGGREGATION_WEIGHTS_MUST_HAVE_DOCUMENTED_EVIDENCE_BASIS=YES
POST_RESULT_REWEIGHTING=PROHIBITED
WEIGHTING_BY_OBSERVED_CANDIDATE_PERFORMANCE=PROHIBITED
WEIGHTING_TO_RESCUE_A_CANDIDATE=PROHIBITED
```

Until those weights and their scientific rationale are separately frozen:

```text
EXACT_CROSS_STRATUM_AGGREGATION_WEIGHTS=NOT_YET_FROZEN
UNWEIGHTED_MACRO_AVERAGE_AS_AUTOMATIC_DEFAULT=NO
SAMPLE_SIZE_WEIGHTED_MICRO_AVERAGE_AS_AUTOMATIC_DEFAULT=NO
```

Stratum-level completeness and hard-gate semantics remain authoritative regardless of any later secondary aggregate.

## 10. Required-stratum completeness

A future exact selection-dev manifest must identify every required stratum and whether each has complete executable evidence.

```text
ALL_REQUIRED_STRATA_MUST_BE_DECLARED_BEFORE_EXECUTION=YES
ALL_REQUIRED_STRATA_MUST_HAVE_EXACT_EVIDENCE_IDENTITIES_BEFORE_EXECUTION=YES

MISSING_REQUIRED_STRATUM=INCOMPLETE
UNBOUND_REQUIRED_STRATUM=INCOMPLETE
UNRESOLVED_REQUIRED_STRATUM_PURPOSE=INCOMPLETE
UNRESOLVED_REQUIRED_STRATUM_METRIC_MAPPING=INCOMPLETE
```

A missing required stratum cannot be silently removed from the denominator or reclassified as optional after results are observed.

```text
POST_RESULT_REQUIRED_STRATUM_REMOVAL=PROHIBITED
POST_RESULT_REQUIRED_TO_OPTIONAL_DOWNGRADE=PROHIBITED
```

## 11. Specialty and disease stratification

Q2 does not invent a specialty or disease distribution.

```text
DISEASE_OR_SPECIALTY_MIX=NOT_YET_FROZEN
DISEASE_PREVALENCE=NOT_YET_FROZEN
SEVERITY_MIX=NOT_YET_FROZEN
COMORBIDITY_MIX=NOT_YET_FROZEN
```

If future evidence requires specialty, disease, severity, or comorbidity strata, their definitions and inclusion rules must be frozen before results and must apply identically across candidates.

```text
FUTURE_SPECIALTY_OR_DISEASE_STRATA_MUST_BE_PREDECLARED=YES
FUTURE_SPECIALTY_OR_DISEASE_STRATA_MUST_BE_CANDIDATE_NEUTRAL=YES
POST_RESULT_SPECIALTY_SELECTION=PROHIBITED
```

## 12. Demographic and geographic stratification

Q2 preserves the unresolved status from Q1:

```text
AGE_BANDS=NOT_YET_FROZEN
SEX_OR_GENDER_DISTRIBUTION=NOT_YET_FROZEN
PREGNANCY_PREVALENCE_OR_SAMPLING_FRACTION=NOT_YET_FROZEN
PEDIATRIC_REPRESENTATION=NOT_YET_FROZEN
GERIATRIC_REPRESENTATION=NOT_YET_FROZEN
HEALTH_LITERACY_DISTRIBUTION=NOT_YET_FROZEN
GEOGRAPHIC_DISTRIBUTION=NOT_YET_FROZEN
SOCIOECONOMIC_DISTRIBUTION=NOT_YET_FROZEN
ACCESSIBILITY_OR_DISABILITY_STRATA=NOT_YET_FROZEN
EXACT_ARABIC_DIALECT_DISTRIBUTION=NOT_YET_FROZEN
```

These dimensions may not be represented as if they were validated populations until separately frozen with an evidence basis.

## 13. Source-component stratification

Because the quality floor is multi-source, source/component identity must remain visible.

```text
SOURCE_COMPONENT_IDENTITY_MUST_BE_RETAINED_IN_RESULTS=YES
SOURCE_COMPONENT_RESULTS_MUST_BE_TRACEABLE=YES
CROSS_SOURCE_POOLING_WITHOUT_SOURCE_LEVEL_RESULTS=PROHIBITED
```

This prevents one large public development component from silently dominating a smaller curated component.

PubMedQA CV remains only a future conditional selection component. Q2 does not generate or bind its derived folds.

```text
PUBMEDQA_CV_SPLIT_GENERATION_AUTHORITY=NONE
PUBMEDQA_CV_DERIVED_ARTIFACT_BINDING=NOT_YET_PERFORMED
PUBMEDQA_CV_EXACT_FOLD_AGGREGATION_ROLE=NOT_YET_FROZEN
```

## 14. Case ordering and adaptive evaluation

Measured scientific evaluation must not adapt case inclusion or ordering in response to observed candidate performance.

```text
CASE_ORDER_POLICY=PREDECLARED_OR_DETERMINISTIC_SEED_BOUND
ADAPTIVE_CASE_SELECTION_BASED_ON_CANDIDATE_RESULTS=PROHIBITED
POST_RESULT_CASE_ADDITION_TO_RESCUE_A_CANDIDATE=PROHIBITED
POST_RESULT_CASE_REMOVAL=PROHIBITED
```

The exact seed and order are not frozen by Q2.

```text
EXACT_EVALUATION_CASE_ORDER=NOT_YET_FROZEN
EXACT_EVALUATION_ORDER_SEED=NOT_YET_FROZEN
```

## 15. Missingness, invalid cases, and failed candidate outputs

A candidate-specific failure does not change the case manifest.

```text
FAILED_CANDIDATE_OUTPUT_CAUSES_CASE_REMOVAL=NO
MISSING_CANDIDATE_OUTPUT_CAUSES_CASE_REMOVAL=NO
CANDIDATE_SPECIFIC_CASE_REPLACEMENT=PROHIBITED
```

The exact metric-specific consequence of a missing or malformed output must be defined before execution.

```text
EXACT_MISSING_OUTPUT_SCORING_RULE=NOT_YET_FROZEN
EXACT_INVALID_CASE_PREEXECUTION_EXCLUSION_RULE=NOT_YET_FROZEN
```

If an evaluation case itself is proven invalid after manifest freeze, handling requires separately reviewable canonical evidence; silent exclusion is prohibited.

## 16. Human and clinical adjudication design

Q2 does not appoint the clinical review authority, but it freezes bias-control requirements for future human-adjudicated selection-dev evidence.

```text
EXACT_CLINICAL_REVIEW_AUTHORITY=NOT_YET_FROZEN

HUMAN_ADJUDICATION_PROTOCOL_MUST_BE_FROZEN_BEFORE_EXECUTION=YES
HUMAN_ADJUDICATORS_MUST_NOT_USE_CANDIDATE_REPUTATION_AS_EVIDENCE=YES
CANDIDATE_IDENTITY_BLINDING_REQUIRED_WHERE_TECHNICALLY_FEASIBLE=YES
ADJUDICATION_DISAGREEMENT_POLICY_REQUIRED_BEFORE_EXECUTION=YES
```

Private Gold adjudicators and Private Gold case content remain outside selection use.

## 17. Design independence from candidate results

All evaluation-design decisions covered by Q2 are pre-result decisions.

```text
STRATIFICATION_SCHEMA_MAY_CHANGE_AFTER_CANDIDATE_RESULTS=NO
UNIT_OF_ANALYSIS_MAY_CHANGE_AFTER_CANDIDATE_RESULTS=NO
PAIRING_RULE_MAY_CHANGE_AFTER_CANDIDATE_RESULTS=NO
REQUIRED_STRATUM_SET_MAY_CHANGE_AFTER_CANDIDATE_RESULTS=NO
AGGREGATION_POLICY_MAY_CHANGE_AFTER_CANDIDATE_RESULTS=NO
```

A later scientifically justified correction requires explicit canonical evidence and cannot be used retroactively to reinterpret an already-observed tournament result without separately governed invalidation/re-execution.

## 18. Manifest schema requirements created by Q2

A future exact selection-dev manifest must bind, directly or through an identity-bound referenced artifact, at least:

```text
case_id
root_case_id_or_explicit_none
quality_lane
role
language_or_explicit_not_applicable
use_context_or_task_stratum
source_component_id
quarantine_purpose
metric_id_or_metric_mapping_id
pair_id_or_explicit_none
fold_id_or_explicit_none
artifact_identity
source_revision
contamination_evidence_identity_or_unresolved_state
```

This is a design requirement only. Q2 does not create the manifest or access the underlying payload.

## 19. Statistical work deliberately deferred

Q2 structurally completes the `EVALUATION_DESIGN` prerequisite only at the architecture level.

It does not complete the statistical prerequisites needed to freeze population-level clinical thresholds.

```text
EVALUATION_DESIGN_ARCHITECTURE=FROZEN
EVALUATION_DESIGN_EXACT_CASE_MANIFEST=NOT_YET_FROZEN
EVALUATION_DESIGN_STATISTICAL_SPECIFICATION=NOT_YET_COMPLETE

STATISTICAL_RATIONALE=NOT_YET_FROZEN
SAMPLE_SIZE_OR_POWER_RATIONALE=NOT_YET_FROZEN
EXACT_CONFIDENCE_INTERVAL_METHODS=NOT_YET_FROZEN
EXACT_HYPOTHESIS_TESTS=NOT_YET_FROZEN
EXACT_MULTIPLICITY_CONTROL=NOT_YET_FROZEN
EXACT_EFFECT_SIZE_OR_MARGIN=NOT_YET_FROZEN
NUMERIC_CLINICAL_STATISTICAL_THRESHOLDS=NOT_YET_FROZEN
```

## 20. External methodological consistency

Q2 is consistent with external methodological principles without importing any numeric requirement from them:

- DECIDE-AI emphasizes explicit intended use, patient/user variability, safety, generalizability, and reproducibility in clinical AI evaluation.
- TRIPOD+AI distinguishes evaluation data from model-development/model-selection data and emphasizes representative evaluation of intended populations and relevant subgroups.

These references support explicit population and subgroup design. They do not authorize Spec 005 to make real-world clinical claims or invent demographic distributions, thresholds, or sample sizes.

## 21. Current quality-manifest consequence

```text
MINIMUM_MEDICAL_QUALITY_EVIDENCE_ARCHITECTURE=NONCOMPENSABLE_MULTI_LANE_SELECTION_DEV_QUALITY_FLOOR
SESSION9_Q1_POLICY=ROLE_LANGUAGE_USE_CONTEXT_INTENDED_POPULATION_MATRIX
SESSION9_Q2_POLICY=STRATUM_FIRST_PAIRED_CANDIDATE_NEUTRAL_EVALUATION_DESIGN

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED

PRIMARY_SELECTION_MANIFEST_BLOCKER_EVALUATION_DESIGN_ARCHITECTURE=RESOLVED_BY_Q2
PRIMARY_SELECTION_MANIFEST_BLOCKER_EXACT_CASE_STRATA_AND_IDENTITIES=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_STATISTICAL_RATIONALE=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_SAMPLE_SIZE_POWER=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_METRIC_MAPPING=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_CONTAMINATION=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_ACCESS_EXECUTION_AUTHORITY=UNRESOLVED

MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
CANONICAL_QUALITY_FLOOR_PASS_CURRENTLY_POSSIBLE=NO
```

## 22. Authority boundary

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

PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## 23. Session state

```text
CLARIFICATION_SESSION_9=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_9_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```
