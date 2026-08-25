# Spec 005 — Session 9 Q3 Statistical Rationale and Sample-Size/Power Architecture

**Lifecycle:** CLARIFY ONLY  
**Evidence capture date:** 2026-08-23  
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Predecessor PR head:** `243fce905f5e82eee86934db1458a7baa558b762`

> This artifact freezes statistical-design architecture only. It does not choose numeric sample sizes, confidence levels, alpha, beta, power targets, effect sizes, margins, clinical thresholds, or aggregation weights. It does not create or access benchmark payloads, generate splits, run models, access model weights, access Private Gold, access PHI/restricted data, authorize corrective maintenance, or advance to PLAN.

## 1. Q3 decision

```text
SESSION9_Q3_POLICY=ESTIMAND_DECISION_RULE_SPECIFIC_PRECISION_AND_POWER_ARCHITECTURE

STATISTICAL_RATIONALE_ARCHITECTURE=FROZEN
SAMPLE_SIZE_POWER_ARCHITECTURE=FROZEN_STRUCTURALLY

UNIVERSAL_SAMPLE_SIZE_N=PROHIBITED
RULE_OF_THUMB_SAMPLE_SIZE_AS_PRIMARY_JUSTIFICATION=PROHIBITED
ONE_SAMPLE_SIZE_FOR_ALL_LANES=PROHIBITED
ONE_SAMPLE_SIZE_FOR_ALL_METRICS=PROHIBITED
```

Sample size must be derived from the exact scientific claim and exact analysis design rather than chosen as a convenient round number.

## 2. Canonical basis

The canonical evaluation contract already establishes that:

1. hard-gate failure cannot be averaged away;
2. incomplete required hard-gate evidence prevents PASS;
3. sentinel zero violations are fixture evidence, not a population zero-error claim;
4. population/statistical thresholds remain non-passable until intended use/population, evaluation design, identity-bound evidence, clinical review authority, and statistical rationale are bound;
5. the six pending hard-gate families include emergency miss rate, medication critical-error rate, selective risk at target coverage, citation entailment fidelity, Arabic clinical parity gap, and lab-report extraction accuracy;
6. Session 9 Q1 freezes role/language/use-context evaluation populations without claiming a real-world clinical cohort;
7. Session 9 Q2 freezes a stratum-first, paired, candidate-neutral design with root-case dependency tracking.

Q3 does not alter the canonical metric identities or hard-gate evaluator semantics.

```text
Q3_REDEFINES_CANONICAL_METRIC_VALUE=NO
Q3_REPLACES_CANONICAL_HARD_GATE_EVALUATOR=NO
Q3_GRANTS_POPULATION_LEVEL_PASS=NO
```

## 3. Required order before sample-size freeze

A numeric sample size may be frozen only after the following are resolved for the exact lane/metric/stratum claim:

```text
SAMPLE_SIZE_PREREQUISITE_1=INTENDED_USE_AND_EVALUATION_POPULATION
SAMPLE_SIZE_PREREQUISITE_2=EVALUATION_DESIGN_AND_UNIT_OF_ANALYSIS
SAMPLE_SIZE_PREREQUISITE_3=METRIC_AND_ESTIMAND_IDENTITY
SAMPLE_SIZE_PREREQUISITE_4=DECISION_ROLE_QUALIFICATION_OR_COMPARATIVE_CLAIM
SAMPLE_SIZE_PREREQUISITE_5=THRESHOLD_MARGIN_OR_TARGET_PRECISION_WHERE_APPLICABLE
SAMPLE_SIZE_PREREQUISITE_6=UNCERTAINTY_OR_INFERENCE_METHOD_CLASS
SAMPLE_SIZE_PREREQUISITE_7=NUISANCE_ASSUMPTIONS_OR_PILOT_BASIS
SAMPLE_SIZE_PREREQUISITE_8=DEPENDENCY_CLUSTERING_AND_PAIRING_STRUCTURE
SAMPLE_SIZE_PREREQUISITE_9=MULTIPLICITY_STRUCTURE_IF_ANY
SAMPLE_SIZE_PREREQUISITE_10=NUMERIC_N_DERIVATION
```

Therefore:

```text
NUMERIC_N_MAY_BE_FROZEN_BEFORE_ESTIMAND=NO
NUMERIC_N_MAY_BE_FROZEN_BEFORE_DECISION_RULE=NO
NUMERIC_N_MAY_BE_FROZEN_BEFORE_REQUIRED_MARGIN_OR_THRESHOLD=NO
NUMERIC_N_MAY_BE_FROZEN_FROM_CANDIDATE_RESULTS=NO
```

## 4. Estimand-first requirement

Every statistical claim used by the selection-dev quality floor must identify one primary estimand before a sample-size calculation is accepted.

```text
PRIMARY_ESTIMAND_REQUIRED_PER_STATISTICAL_CLAIM=YES
ESTIMAND_MUST_BIND_METRIC_ID=YES
ESTIMAND_MUST_BIND_LANE=YES
ESTIMAND_MUST_BIND_REQUIRED_STRATUM_OR_EXPLICIT_CROSS_STRATUM_SCOPE=YES
ESTIMAND_MUST_BIND_UNIT_OF_ANALYSIS=YES
ESTIMAND_MUST_BIND_DIRECTION=YES
```

Examples of estimand classes already implied by canonical metrics include:

```text
LOWER_BETTER_RATE_OR_RISK
HIGHER_BETTER_PROPORTION_OR_FIDELITY
PAIRED_LANGUAGE_GAP
NONLINEAR_SUMMARY_SUCH_AS_F1
CALIBRATION_OR_SELECTIVE_RISK_SCORE
HUMAN_ADJUDICATED_UTILITY_OR_ACTIONABILITY
```

Q3 does not assign a new metric ID to any class.

## 5. Population hard-gate uncertainty requirement

For a future population/statistical hard-gate qualification, a point estimate alone is not sufficient scientific evidence.

```text
POPULATION_HARD_GATE_POINT_ESTIMATE_ALONE_SUFFICIENT_FOR_PASS=NO
POPULATION_HARD_GATE_UNCERTAINTY_EVIDENCE_REQUIRED=YES
```

The canonical point estimate remains the reported metric value. Q3 requires additional uncertainty evidence; it does not redefine the metric.

```text
CANONICAL_POINT_ESTIMATE_REMAINS_REPORTED_METRIC_VALUE=YES
UNCERTAINTY_BOUND_IS_ADDITIONAL_QUALIFICATION_EVIDENCE=YES
```

For lower-better population gates, the future evidence plan must support an upper uncertainty bound against the separately frozen maximum acceptable threshold.

```text
LOWER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=UPPER_BOUND_AGAINST_FROZEN_MAXIMUM
```

For higher-better population gates, the future evidence plan must support a lower uncertainty bound against the separately frozen minimum acceptable threshold.

```text
HIGHER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=LOWER_BOUND_AGAINST_FROZEN_MINIMUM
```

Exact confidence level and exact interval method remain unresolved.

```text
EXACT_CONFIDENCE_LEVEL=NOT_YET_FROZEN
EXACT_CONFIDENCE_INTERVAL_METHOD_BY_METRIC=NOT_YET_FROZEN
```

## 6. Zero observed failures are not zero population risk

For rare or safety-critical adverse-event metrics:

```text
ZERO_OBSERVED_FAILURES_IMPLIES_ZERO_POPULATION_ERROR_RATE=NO
ZERO_OBSERVED_FAILURES_ELIMINATES_UNCERTAINTY=NO
ZERO_OBSERVED_FAILURES_STILL_REQUIRES_UNCERTAINTY_BOUND=YES
```

This preserves the canonical distinction between a zero-violation sentinel fixture and a population clinical error-rate claim.

## 7. Sample-size objective classes

Q3 permits two broad statistical planning objectives, chosen per claim before execution.

### 7.1 Precision-driven estimation

Use when the scientific requirement is to estimate a metric with sufficiently narrow uncertainty.

```text
PRECISION_DRIVEN_SAMPLE_SIZE_ALLOWED=YES
TARGET_PRECISION_MUST_BE_PREDECLARED=YES
TARGET_PRECISION_MAY_BE_CHOSEN_AFTER_CANDIDATE_RESULTS=NO
```

### 7.2 Decision/power-driven qualification or comparison

Use when a claim requires demonstrating compatibility with a predeclared threshold, margin, or candidate-neutral comparative criterion.

```text
POWER_OR_DECISION_DRIVEN_SAMPLE_SIZE_ALLOWED=YES
DECISION_THRESHOLD_OR_MARGIN_MUST_BE_PREDECLARED=YES
POWER_TARGET_MUST_BE_PREDECLARED=YES
POST_RESULT_POWER_TARGET_CHANGE=PROHIBITED
POST_RESULT_MARGIN_CHANGE=PROHIBITED
```

Q3 does not choose which objective applies to every metric; that must be bound metric-by-metric.

## 8. Metric-family planning rules

### 8.1 Binary adverse-event rates

Metrics such as emergency miss rate or medication critical-error rate are lower-better rates.

Their sample-size rationale must depend on the planned threshold/margin, uncertainty method, anticipated event-rate assumption or conservative bound, and required precision/power.

```text
BINARY_RATE_N_DEPENDS_ON_EXPECTED_OR_CONSERVATIVE_RATE_ASSUMPTION=YES
BINARY_RATE_N_DEPENDS_ON_REQUIRED_UNCERTAINTY_OR_DECISION_RULE=YES
FIXED_EVENT_COUNT_RULE_OF_THUMB_AS_SOLE_JUSTIFICATION=PROHIBITED
```

Exact rate assumptions and interval method are not frozen.

### 8.2 Proportion/fidelity metrics

For higher-better proportion-like metrics such as citation entailment fidelity, planning must use the exact target threshold or precision requirement and an appropriate uncertainty model.

```text
PROPORTION_METRIC_POINT_ESTIMATE_ONLY_FOR_PASS=NO
PROPORTION_METRIC_N_REQUIRES_PREDECLARED_PRECISION_OR_DECISION_TARGET=YES
```

### 8.3 Selective-risk and calibration-family scores

For bounded or curve-derived scores, sample size must be tied to the exact estimand, acceptance criterion, and validated uncertainty method rather than borrowed from a binary-rate calculation.

```text
SELECTIVE_RISK_SAMPLE_SIZE_MAY_REUSE_BINARY_RATE_FORMULA_WITHOUT_JUSTIFICATION=NO
CALIBRATION_SAMPLE_SIZE_MAY_REUSE_BINARY_RATE_FORMULA_WITHOUT_JUSTIFICATION=NO
```

### 8.4 Nonlinear metrics such as F1

For nonlinear summaries such as lab-report field-extraction F1, the uncertainty and sample-size method must account for the exact scoring unit and dependence structure.

```text
F1_NORMAL_APPROXIMATION_ASSUMED_BY_DEFAULT=NO
F1_UNCERTAINTY_METHOD_MUST_BE_PREDECLARED=YES
F1_ROOT_CASE_DEPENDENCY_MUST_BE_ACCOUNTED_FOR=YES
```

The exact analytic, resampling, or simulation method is not frozen by Q3.

### 8.5 Human-adjudicated metrics

For human-adjudicated utility, communication, or workflow outcomes, the future power/precision plan must account for case-level and reviewer-level dependence where applicable.

```text
HUMAN_RATING_RAW_RATING_COUNT_EQUALS_INDEPENDENT_N=NO
REPEATED_RATINGS_OF_ONE_CASE_COUNT_AS_INDEPENDENT_CASES=NO
REVIEWER_DEPENDENCY_MUST_BE_ADDRESSED_WHERE_APPLICABLE=YES
```

Exact reviewer model and variance structure remain unresolved.

## 9. Arabic-English paired parity

Lane E retains the matched Arabic-English pair as the analysis unit.

```text
LANE_E_SAMPLE_SIZE_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIRS
LANE_E_INDEPENDENT_TWO_SAMPLE_LANGUAGE_POWER_MODEL=PROHIBITED
LANE_E_PAIRED_DIFFERENCE_OR_GAP_ESTIMAND_REQUIRED=YES
LANE_E_WITHIN_PAIR_VARIABILITY_OR_EQUIVALENT_PAIRED_UNCERTAINTY_INPUT_REQUIRED=YES
```

For the lower-better `arabic_clinical_parity_gap`, future population qualification must be based on uncertainty around the paired gap relative to a separately frozen maximum acceptable gap.

```text
ARABIC_PARITY_GATE_EVIDENCE_DIRECTION=UPPER_BOUND_ON_PAIRED_GAP_AGAINST_FROZEN_MAXIMUM_GAP
```

Exact parity margin, confidence level, and paired-analysis method remain unresolved.

```text
EXACT_ARABIC_PARITY_MAXIMUM_GAP=NOT_YET_FROZEN
EXACT_ARABIC_PARITY_CONFIDENCE_LEVEL=NOT_YET_FROZEN
EXACT_ARABIC_PARITY_PAIRED_ANALYSIS_METHOD=NOT_YET_FROZEN
```

## 10. Root-case clustering and effective sample size

Session 9 Q2 already prohibits counting derived variants as independent cases. Q3 makes that binding for power and precision calculations.

```text
RAW_VARIANT_COUNT_MAY_BE_USED_AS_INDEPENDENT_N=NO
ROOT_CASE_DEPENDENCY_MUST_BE_REFLECTED_IN_SAMPLE_SIZE=YES
```

If the final design analyzes multiple dependent variants rather than collapsing to root-case summaries, the statistical plan must account for clustering/correlation.

```text
DEPENDENT_VARIANT_ANALYSIS_REQUIRES_CLUSTER_AWARE_POWER_OR_PRECISION=YES
INTRACLUSTER_OR_EQUIVALENT_DEPENDENCY_PARAMETER_REQUIRED_IF_METHOD_REQUIRES_IT=YES
```

Exact ICC, design effect, mixed model, GEE, bootstrap cluster method, or other cluster-aware method is not frozen.

```text
EXACT_CLUSTER_DEPENDENCY_METHOD=NOT_YET_FROZEN
EXACT_ICC_OR_DEPENDENCY_PARAMETER=NOT_YET_FROZEN
```

## 11. PubMedQA CV dependency

If PubMedQA official CV is later admitted as a selection component, sample-size accounting must count unique held-out root cases rather than repeated fold memberships or training complements.

```text
PUBMEDQA_CV_EFFECTIVE_N_MAY_SUM_REPEATED_FOLD_MEMBERSHIPS=NO
PUBMEDQA_CV_SAMPLE_SIZE_UNIT=UNIQUE_HELD_OUT_ROOT_CASES_OR_EQUIVALENT_DEPENDENCY_AWARE_UNIT
```

Q3 does not generate folds, bind derived artifacts, or freeze fold aggregation.

```text
PUBMEDQA_CV_SPLIT_GENERATION_AUTHORITY=NONE
PUBMEDQA_CV_DERIVED_ARTIFACT_BINDING=NOT_YET_PERFORMED
PUBMEDQA_CV_EXACT_FOLD_AGGREGATION_ROLE=NOT_YET_FROZEN
```

## 12. Stratum-level sample-size sufficiency

Because required strata are noncompensable, pooled total N cannot establish adequacy for a required stratum that lacks its own evidence basis.

```text
TOTAL_PORTFOLIO_N_ALONE_ESTABLISHES_STRATUM_ADEQUACY=NO
EACH_REQUIRED_STATISTICAL_STRATUM_NEEDS_OWN_ADEQUACY_RATIONALE=YES
```

A case may legitimately contribute to more than one reported stratum when predeclared, but overlapping stratum counts must not be summed as if they were unique independent cases.

```text
OVERLAPPING_STRATUM_COUNTS_MAY_BE_SUMMED_AS_UNIQUE_N=NO
ROOT_CASE_IDENTITY_REMAINS_AUTHORITATIVE_FOR_INDEPENDENCE=YES
```

## 13. Cross-stratum and cross-lane inference

Q3 does not freeze aggregate weighting. It does require the inferential structure to be explicit before simultaneous statistical claims are made.

```text
MULTIPLICITY_STRUCTURE_MUST_BE_PREDECLARED=YES
AUTOMATIC_BONFERRONI_OR_OTHER_CORRECTION_REQUIRED_BY_Q3=NO
AUTOMATIC_NO_CORRECTION_REQUIRED_BY_Q3=NO
```

The exact need for and form of multiplicity control must be justified by the final hypothesis/interval structure, including whether the claim uses intersection-union hard-gate semantics, simultaneous subgroup claims, or secondary comparisons.

```text
EXACT_MULTIPLICITY_CONTROL=NOT_YET_FROZEN
```

## 14. Candidate-neutral nuisance assumptions

All numerical assumptions used to calculate sample size must be fixed before candidate results and must apply identically to comparable candidates.

```text
SAMPLE_SIZE_ASSUMPTIONS_MUST_BE_CANDIDATE_NEUTRAL=YES
CANDIDATE_SPECIFIC_EXPECTED_RATE_OR_VARIANCE=PROHIBITED_FOR_SHARED_GATE_DESIGN
POST_RESULT_NUISANCE_ASSUMPTION_CHANGE=PROHIBITED
```

Permissible future assumption sources, once separately authorized and rights/provenance are resolved, may include:

```text
PUBLISHED_EXTERNAL_EVIDENCE
SEPARATELY_AUTHORIZED_NON_GOLD_PRETOURNAMENT_PILOT_EVIDENCE
CONSERVATIVE_PREDECLARED_ASSUMPTION_WITH_SENSITIVITY_ANALYSIS
```

Private Gold and tournament candidate results are prohibited sources for power tuning.

```text
PRIVATE_GOLD_MAY_BE_USED_TO_ESTIMATE_SELECTION_SAMPLE_SIZE=NO
PRIVATE_GOLD_MAY_BE_USED_TO_TUNE_SELECTION_MARGIN=NO
TOURNAMENT_CANDIDATE_RESULTS_MAY_BE_USED_TO_RECALCULATE_N=NO
TOURNAMENT_CANDIDATE_RESULTS_MAY_BE_USED_TO_TUNE_EXPECTED_EFFECT=NO
```

No pilot access or execution is authorized by Q3.

## 15. Sensitivity analysis for uncertain planning inputs

When a nuisance parameter materially affects N and is uncertain, the statistical design must examine a predeclared plausible range or otherwise justify a conservative value.

```text
MATERIAL_SAMPLE_SIZE_ASSUMPTION_UNCERTAINTY_REQUIRES_SENSITIVITY_ANALYSIS_OR_CONSERVATIVE_JUSTIFICATION=YES
SENSITIVITY_RANGE_MAY_BE_SELECTED_AFTER_CANDIDATE_RESULTS=NO
```

Exact ranges remain unfrozen.

## 16. Missing outputs are not sample attrition

A candidate's failure, refusal, malformed output, or timeout does not reduce the planned evaluation sample size and does not authorize replacement cases.

```text
CANDIDATE_OUTPUT_FAILURE_COUNTS_AS_STATISTICAL_ATTRITION=NO
CANDIDATE_OUTPUT_FAILURE_AUTHORIZES_CASE_REPLACEMENT=NO
CANDIDATE_SPECIFIC_SAMPLE_REPLENISHMENT=PROHIBITED
```

The metric-specific scoring consequence remains to be frozen before execution.

Pre-execution handling of objectively invalid cases remains governed by the future invalid-case rule and cannot be improvised after candidate results.

## 17. Optional stopping and adaptive N

Sample size must not be expanded or truncated after looking at candidate results unless a separately frozen sequential/adaptive design explicitly controls the relevant error/precision properties.

```text
UNPLANNED_OPTIONAL_STOPPING=PROHIBITED
POST_RESULT_SAMPLE_SIZE_INCREASE_TO_RESCUE_A_CANDIDATE=PROHIBITED
POST_RESULT_EARLY_STOP_BECAUSE_PREFERRED_CANDIDATE_IS_AHEAD=PROHIBITED
```

A future adaptive/sequential design is not prohibited in principle, but it requires separate pre-result clarification.

```text
ADAPTIVE_OR_SEQUENTIAL_DESIGN_CURRENTLY_FROZEN=NO
```

## 18. Qualification versus ranking evidence

Q3 distinguishes qualification evidence from optional comparative/ranking evidence.

```text
QUALIFICATION_SAMPLE_SIZE_AND_RANKING_SAMPLE_SIZE_MAY_BE_ASSUMED_IDENTICAL=NO
```

For any future candidate comparison using the same exact case manifest, a paired same-case comparison is preferred where the metric admits a per-case comparison, because candidate outputs are observed on the same cases.

```text
CANDIDATE_COMPARATIVE_ANALYSIS_MUST_PRESERVE_SHARED_CASE_PAIRING_WHERE_APPLICABLE=YES
INDEPENDENT_TWO_SAMPLE_CANDIDATE_MODEL_ASSUMPTION_WHEN_SAME_CASES_ARE_USED=PROHIBITED_WITHOUT_JUSTIFICATION
```

Q3 does not freeze any secondary ranking metric, effect size, superiority margin, or winner-selection statistical test.

## 19. Statistical design artifact required before execution

Before execution can be authorized, each statistical claim used for qualification or selection must be represented in a reviewable identity-bound statistical-design artifact containing at least:

```text
statistical_design_id
quality_lane
metric_id_or_metric_mapping_id
required_stratum_or_scope
estimand
unit_of_analysis
decision_role
threshold_or_margin_identity_or_explicit_not_applicable
precision_or_power_objective
confidence_or_error_rate_parameters
anticipated_rate_variance_or_other_nuisance_inputs
source_and_provenance_for_planning_inputs
pairing_or_cluster_dependency_model
multiplicity_structure
planned_numeric_n
rounding_or_allocation_rule
software_formula_or_method_identity
sensitivity_analysis_identity_or_explicit_not_required
```

Q3 creates the schema requirement only; it does not create a numeric statistical-design artifact.

## 20. Reproducibility requirements

Any future numerical N calculation must be reproducible from recorded inputs and method identity.

```text
SAMPLE_SIZE_CALCULATION_INPUTS_MUST_BE_RECORDED=YES
SAMPLE_SIZE_FORMULA_OR_SOFTWARE_IDENTITY_MUST_BE_RECORDED=YES
SAMPLE_SIZE_SOFTWARE_VERSION_OR_COMMIT_MUST_BE_PINNED_WHERE_USED=YES
MANUAL_UNTRACEABLE_N_SELECTION=PROHIBITED
```

Q3 authorizes no dependency installation or software execution.

## 21. External methodological consistency

Q3 uses external methodology as a consistency check only and imports no numeric threshold or power target.

- Riley et al., BMJ 2024, *Evaluation of clinical prediction models (part 3): calculating the sample size required for an external validation study*, emphasizes tailoring validation sample size to the exact performance measure and desired precision rather than relying on blanket rules of thumb.
- Vasey et al., Nature Medicine 2022, DECIDE-AI, emphasizes intended patient/user populations, variability, generalizability, safety, and reproducibility in clinical AI evaluation.
- ICH E9 statistical principles state that sample size should be tied to the primary analysis and, for equivalence/non-inferiority objectives, to confidence intervals relative to a clinically acceptable difference. Q3 uses only the general principle that the decision criterion and uncertainty target must precede N.
- Standard clustered-design methodology establishes that correlated observations reduce effective independent information; Q3 applies that principle to root-case/derived-variant dependence without importing a numerical design effect.

These references do not make Spec 005 a clinical trial, do not establish real-world effectiveness, and do not authorize population clinical claims.

## 22. What remains deliberately unresolved

```text
EXACT_NUMERIC_N_BY_LANE_METRIC_STRATUM=NOT_YET_FROZEN
EXACT_POWER_TARGET=NOT_YET_FROZEN
EXACT_ALPHA_OR_TYPE_I_ERROR_TARGET=NOT_YET_FROZEN
EXACT_BETA_OR_TYPE_II_ERROR_TARGET=NOT_YET_FROZEN
EXACT_CONFIDENCE_LEVEL=NOT_YET_FROZEN
EXACT_PRECISION_TARGET=NOT_YET_FROZEN
EXACT_EFFECT_SIZE=NOT_YET_FROZEN
EXACT_NONINFERIORITY_EQUIVALENCE_OR_ACCEPTABILITY_MARGIN=NOT_YET_FROZEN
EXACT_EXPECTED_EVENT_RATES=NOT_YET_FROZEN
EXACT_VARIANCE_INPUTS=NOT_YET_FROZEN
EXACT_CLUSTER_DEPENDENCY_PARAMETER=NOT_YET_FROZEN
EXACT_CONFIDENCE_INTERVAL_METHOD_BY_METRIC=NOT_YET_FROZEN
EXACT_MULTIPLICITY_CONTROL=NOT_YET_FROZEN
EXACT_STATISTICAL_SOFTWARE_OR_IMPLEMENTATION=NOT_YET_FROZEN
EXACT_CLINICAL_REVIEW_AUTHORITY=NOT_YET_FROZEN
NUMERIC_CLINICAL_STATISTICAL_THRESHOLDS=NOT_YET_FROZEN
```

## 23. Current quality-manifest consequence

```text
MINIMUM_MEDICAL_QUALITY_EVIDENCE_ARCHITECTURE=NONCOMPENSABLE_MULTI_LANE_SELECTION_DEV_QUALITY_FLOOR
SESSION9_Q1_POLICY=ROLE_LANGUAGE_USE_CONTEXT_INTENDED_POPULATION_MATRIX
SESSION9_Q2_POLICY=STRATUM_FIRST_PAIRED_CANDIDATE_NEUTRAL_EVALUATION_DESIGN
SESSION9_Q3_POLICY=ESTIMAND_DECISION_RULE_SPECIFIC_PRECISION_AND_POWER_ARCHITECTURE

STATISTICAL_RATIONALE_ARCHITECTURE=FROZEN
SAMPLE_SIZE_POWER_ARCHITECTURE=FROZEN_STRUCTURALLY

EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED

PRIMARY_SELECTION_MANIFEST_BLOCKER_STATISTICAL_ARCHITECTURE=RESOLVED_BY_Q3
PRIMARY_SELECTION_MANIFEST_BLOCKER_EXACT_NUMERIC_SAMPLE_SIZE_POWER=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_EXACT_CASE_STRATA_AND_IDENTITIES=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_METRIC_MAPPING=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_CONTAMINATION=UNRESOLVED
PRIMARY_SELECTION_MANIFEST_BLOCKER_ACCESS_EXECUTION_AUTHORITY=UNRESOLVED

MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
CANONICAL_QUALITY_FLOOR_PASS_CURRENTLY_POSSIBLE=NO
```

## 24. Authority boundary

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

## 25. Session state

```text
CLARIFICATION_SESSION_9=3_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_9_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```
