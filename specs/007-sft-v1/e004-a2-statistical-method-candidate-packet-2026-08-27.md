# E004 A2 Statistical-Method Candidate Packet — 2026-08-27

**Spec:** 007 SFT V1  
**Related control plane:** Spec 005 A2 + atomic A3/A4 scientific readiness  
**Canonical base:** `e6d148a433d596165688a656b21d134f04fc8987`  
**Artifact class:** read-only public-method research / review packet  
**Authority effect:** NONE  
**Validator input:** NO

This packet narrows the unresolved statistical-method surface for the six canonical hard-gate metric families without freezing a confidence level, alpha, beta, power target, threshold, margin, target coverage, nuisance parameter, sample size, allocation, reviewer disposition, or executable evaluation record.

It is **not** a `ThresholdPolicy`, **not** a `StatisticalDesign`, **not** an A2 PASS record, and **not** evidence of clinical/statistical approval.

```text
A2_STATISTICAL_METHOD_PACKET_ONLY=YES
CANDIDATE_METHOD_ONLY=YES
REAL_THRESHOLD_RECORDS_CREATED=0
REAL_STATISTICAL_DESIGN_RECORDS_CREATED=0
QUALIFIED_STATISTICAL_REVIEW_DISPOSITIONS_CREATED=0
QUALIFIED_CLINICAL_REVIEW_DISPOSITIONS_CREATED=0
NUMERIC_THRESHOLDS_FROZEN=0
NUMERIC_CONFIDENCE_LEVELS_FROZEN=0
NUMERIC_ALPHA_FROZEN=0
NUMERIC_BETA_FROZEN=0
NUMERIC_POWER_TARGETS_FROZEN=0
NUMERIC_N_FROZEN=0
TARGET_COVERAGE_FROZEN=NO
A2_STATE=INCOMPLETE_REAL_EVIDENCE_AND_REVIEW_REQUIRED
D34_A3_A4=BLOCKED_BY_T1
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Current authority boundary

This packet changes no authority.

```text
E002_NON_EXECUTING_SOURCE_WEIGHT_ACQUISITION_AND_STATIC_INTEGRITY_WORK=AUTHORIZED_WITHIN_EXACT_E002_SCOPE
E002_PRECONVERTED_BYTE_ACQUISITION=AUTHORIZED_FOR_EXACT_TWO_ENTRY_ALLOWLIST_ONLY

E003_MODEL_EXECUTION=BLOCKED_BY_INCOMPLETE_E004_PREFLIGHT
E003_A15_BOUND_BENCHMARK_EXECUTION=BLOCKED_BY_INCOMPLETE_A15_PREFLIGHT_BINDINGS
E003_DEVICE_QUALIFICATION_EXECUTION=BLOCKED_BY_INCOMPLETE_PREEXECUTION_STATE

MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

No model, benchmark payload, selection suite, physical device, conversion, contamination assessment, Private Gold, PHI, gated asset, provider, personnel engagement, or spend action occurred while producing this packet.

## 2. Frozen statistical constraints

Session 9 Q3 remains controlling.

```text
UNIVERSAL_SAMPLE_SIZE_N=PROHIBITED
RULE_OF_THUMB_SAMPLE_SIZE_AS_PRIMARY_JUSTIFICATION=PROHIBITED
ONE_SAMPLE_SIZE_FOR_ALL_METRICS=PROHIBITED
POINT_ESTIMATE_ALONE_SUFFICIENT_FOR_POPULATION_HARD_GATE_PASS=NO
LOWER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=UPPER_BOUND_AGAINST_FROZEN_MAXIMUM
HIGHER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=LOWER_BOUND_AGAINST_FROZEN_MINIMUM
ZERO_OBSERVED_FAILURES_IMPLIES_ZERO_POPULATION_ERROR_RATE=NO
ZERO_OBSERVED_FAILURES_ELIMINATES_UNCERTAINTY=NO
ZERO_OBSERVED_FAILURES_STILL_REQUIRES_UNCERTAINTY_BOUND=YES
EXACT_CONFIDENCE_LEVEL=NOT_YET_FROZEN
EXACT_CONFIDENCE_INTERVAL_METHOD_BY_METRIC=NOT_YET_FROZEN
ROOT_CASE_DEPENDENCY_MUST_BE_REFLECTED_IN_SAMPLE_SIZE=YES
MULTIPLICITY_STRUCTURE_MUST_BE_PREDECLARED=YES
CANDIDATE_RESULT_DRIVEN_NUISANCE_OR_N_CHANGE=PROHIBITED
UNPLANNED_OPTIONAL_STOPPING=PROHIBITED
```

Arabic parity remains matched-pair only:

```text
LANE_E_SAMPLE_SIZE_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIRS
LANE_E_INDEPENDENT_TWO_SAMPLE_LANGUAGE_POWER_MODEL=PROHIBITED
LANE_E_PAIRED_DIFFERENCE_OR_GAP_ESTIMAND_REQUIRED=YES
```

F1 remains nonlinear and dependency-sensitive:

```text
F1_NORMAL_APPROXIMATION_ASSUMED_BY_DEFAULT=NO
F1_UNCERTAINTY_METHOD_MUST_BE_PREDECLARED=YES
F1_ROOT_CASE_DEPENDENCY_MUST_BE_ACCOUNTED_FOR=YES
```

## 3. Public method-source inventory

These sources establish method candidates only; none supplies a transferable commandMed operating point.

| ID | Source | Stable locator | Candidate use | Transfer limitation |
|---|---|---|---|---|
| `A2STAT-001` | Brown, Cai, DasGupta, *Interval Estimation for a Binomial Proportion* | DOI `10.1214/ss/1009213286` | binomial interval appraisal; avoid naive Wald defaults | no commandMed confidence level, threshold, event-rate assumption, or N |
| `A2STAT-002` | Field, Welsh, *Bootstrapping Clustered Data* | DOI `10.1111/j.1467-9868.2007.00593.x` | cluster-resampling rationale when observations share a root/cluster | bootstrap validity depends on model/estimand; no boundary-safe rare-event guarantee is implied |
| `A2STAT-003` | Berger, Hsu, *Bioequivalence Trials, Intersection-Union Tests and Equivalence Confidence Sets* | DOI `10.1214/ss/1032280304` | intersection-union/equivalence decision architecture | bioequivalence margins/settings are not commandMed policy |
| `A2STAT-004` | Angelopoulos et al., *Learn then Test: Calibrating Predictive Algorithms to Achieve Risk Control* | arXiv `2110.01052` | finite-sample risk-control calibration candidate | exact commandMed loss/risk semantics and assumptions must match |
| `A2STAT-005` | Bates et al., *Distribution-Free, Risk-Controlling Prediction Sets* | DOI `10.1145/3478535` | held-out distribution-free expected-risk control candidate | prediction-set examples are not automatically selective-risk semantics |
| `A2STAT-006` | Angelopoulos et al., *Conformal Risk Control* | ICLR 2024; arXiv `2208.02814` | monotone-loss conformal risk-control candidate | requires compatible loss/parameter monotonicity and exchangeability |
| `A2STAT-007` | Takahashi et al., *Confidence interval for micro-averaged F1 and macro-averaged F1 scores* | DOI `10.1007/s10489-021-02635-5`; PMID `35317080` | F1-specific interval candidate | commandMed root-case dependence may invalidate direct use |
| `A2STAT-008` | Takahashi et al., *Hypothesis testing procedure for binary and multi-class F1-scores in the paired design* | DOI `10.1002/sim.9853`; PMID `37527903` | paired F1 inference reference | Arabic parity is not automatically an F1 comparison |
| `A2STAT-009` | Hsu, Liu, Shyr, *A Unified Framework for Statistical Inference and Power Analysis of Single and Comparative F-beta Scores* | DOI `10.1002/sim.70557`; PMID `42050845` | F1/F-beta interval, testing, power/sample-size candidate | scoring unit/dependency assumptions must match before adoption |

No source above is a qualified statistical-review disposition.

## 4. Candidate status vocabulary

```text
PRIMARY_CANDIDATE_FOR_REVIEW=
  strongest current candidate given the frozen estimand/dependency architecture;
  not frozen and not approved

CONDITIONAL_CANDIDATE=
  potentially valid only if exact future assumptions hold

SENSITIVITY_CANDIDATE=
  potential robustness comparison rather than primary basis

REJECT_AS_DEFAULT=
  not eligible as a default without new explicit statistical justification

NEEDS_QUALIFIED_STATISTICAL_REVIEW=
  repository agents cannot convert a candidate into approval
```

## 5. Cross-metric inferential architecture

### 5.1 Directional one-sided qualification

```text
LOWER_BETTER_GATE:
  candidate evidence = one-sided upper uncertainty bound
  future PASS = upper bound <= separately frozen maximum

HIGHER_BETTER_GATE:
  candidate evidence = one-sided lower uncertainty bound
  future PASS = lower bound >= separately frozen minimum
```

The confidence/error-rate level remains unresolved.

### 5.2 Root-first independence

```text
INDEPENDENT_N_UNIT=ROOT_CASE_OR_OTHER_EXACT_CANONICAL_ANALYSIS_UNIT
VARIANTS_WITHIN_ONE_ROOT=NOT_INDEPENDENT_N
MATCHED_ARABIC_ENGLISH_PAIR=ONE_PAIRED_ANALYSIS_UNIT
```

When multiple dependent observations occur within one root, candidate inference must either:

1. collapse them to a predeclared root-level estimand; or
2. use a dependency-aware method that preserves the root as a cluster.

Naive row-level resampling of dependent variants/claims/fields is not a candidate.

### 5.3 Cluster-resampling candidate and rare-event boundary safeguard

`A2STAT-002` supports cluster-resampling as a method family for clustered data. It does **not** establish that every empirical cluster bootstrap is valid for every commandMed estimand or boundary case.

```text
CLUSTER_RESAMPLING_UNIT=ROOT_CASE_CANDIDATE_ONLY
RESAMPLE_WITHIN_ROOT_INDEPENDENTLY=NO_BY_DEFAULT
BOOTSTRAP_VARIANT=NOT_YET_SELECTED
BOOTSTRAP_REPETITION_COUNT=NOT_YET_FROZEN
SMALL_CLUSTER_COUNT_ACCEPTABILITY=NEEDS_STATISTICAL_REVIEW
```

For rare/safety-critical adverse-event rates there is an additional non-negotiable boundary rule:

```text
UNADJUSTED_EMPIRICAL_CLUSTER_BOOTSTRAP_AT_ALL_ZERO_EVENT_BOUNDARY=REJECT_AS_DEFAULT
ZERO_EVENT_CLUSTER_RESAMPLES_MAY_PRODUCE_ZERO_POPULATION_UPPER_BOUND=PROHIBITED
RARE_EVENT_CLUSTERED_METHOD_MUST_RETAIN_NONZERO_POPULATION_UNCERTAINTY=YES
BOUNDARY_SAFE_RARE_EVENT_METHOD_OR_CONSERVATIVE_SAFEGUARD=REQUIRED
EXACT_BOUNDARY_SAFE_CLUSTER_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
```

A cluster-aware method is therefore only a **conditional family** for emergency/medication adverse-event gates until a qualified reviewer selects a boundary-safe construction. Dependency-awareness cannot weaken the frozen zero-event uncertainty rule.

### 5.4 Global hard-gate conjunction

Because overall quality-floor PASS requires every noncompensable hard gate to pass, an intersection-union formulation is a candidate for the global conjunction claim.

```text
IF_GLOBAL_PASS_NULL=AT_LEAST_ONE_REQUIRED_GATE_FAILS_ITS_FROZEN_BOUND
AND_GLOBAL_PASS_ALTERNATIVE=EVERY_REQUIRED_GATE_SATISFIES_ITS_FROZEN_BOUND
THEN=INTERSECTION_UNION_TEST_ARCHITECTURE_IS_CANDIDATE_FOR_REVIEW
```

This does **not** freeze a multiplicity waiver.

```text
AUTOMATIC_BONFERRONI=NOT_FROZEN
AUTOMATIC_NO_CORRECTION=NOT_FROZEN
SIMULTANEOUS_STRATA_COMPARISONS_AND_SECONDARY_CLAIMS_REQUIRE_SEPARATE_MULTIPLICITY_APPRAISAL=YES
GLOBAL_IUT_CANDIDATE_REQUIRES_QUALIFIED_STATISTICAL_REVIEW=YES
```

## 6. `emergency_miss_rate`

```text
METRIC_ID=emergency_miss_rate
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
```

If each independent root contributes one predeclared binary miss outcome:

```text
PRIMARY_CANDIDATE_METHOD=ONE_SIDED_EXACT_BINOMIAL_UPPER_CONFIDENCE_BOUND
REFERENCE=A2STAT-001
```

This candidate is attractive for review because zero observed misses still produce positive population uncertainty under a boundary-safe exact construction.

If a root produces multiple dependent emergency decisions:

```text
OPTION_A=PREDECLARE_ROOT_LEVEL_WORST_CASE_OR_OTHER_CLINICALLY_VALID_BINARY_ROOT_SUMMARY_THEN_USE_BOUNDARY_SAFE_ROOT_LEVEL_RATE_METHOD
OPTION_B=BOUNDARY_SAFE_CLUSTER_AWARE_RARE_EVENT_METHOD
OPTION_B_GENERIC_CLUSTER_RESAMPLING_REFERENCE=A2STAT-002
```

For Option B:

```text
UNCORRECTED_EMPIRICAL_CLUSTER_BOOTSTRAP_AT_ZERO_EVENTS=PROHIBITED
BOUNDARY_SAFE_NONZERO_UPPER_UNCERTAINTY_AT_ZERO_EVENTS=REQUIRED
EXACT_CLUSTER_RARE_EVENT_CONSTRUCTION=NEEDS_QUALIFIED_STATISTICAL_REVIEW
```

A Wilson/score-type one-sided interval remains a sensitivity candidate under independent Bernoulli assumptions.

```text
NAIVE_WALD_NORMAL_INTERVAL=REJECT_AS_DEFAULT
ZERO_EVENT_POINT_ESTIMATE_AS_PASS=PROHIBITED
RULE_OF_THREE_AS_COMPLETE_SCIENTIFIC_JUSTIFICATION=REJECT_AS_DEFAULT
```

Still unresolved:

```text
EXACT_ROOT_OUTCOME_DEFINITION=NEEDS_EVIDENCE
EXACT_MAXIMUM_MISS_RATE=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PRIMARY_INTERVAL_OR_BOUNDARY_SAFE_CLUSTER_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
ANTICIPATED_OR_CONSERVATIVE_EVENT_RATE_FOR_N=NEEDS_EVIDENCE
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 7. `medication_critical_error_rate`

```text
METRIC_ID=medication_critical_error_rate
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
```

If one independent root contributes one predeclared binary critical-error outcome:

```text
PRIMARY_CANDIDATE_METHOD=ONE_SIDED_EXACT_BINOMIAL_UPPER_CONFIDENCE_BOUND_IF_ROOT_LEVEL_BERNOULLI
REFERENCE=A2STAT-001
```

If multiple medications/interactions/doses/sub-decisions occur within one root:

```text
MULTIPLE_SUBDECISIONS_PER_ROOT_INDEPENDENT_N=NO
OPTION_A=PREDECLARED_CLINICALLY_VALID_BINARY_ROOT_SUMMARY_WITH_BOUNDARY_SAFE_RATE_METHOD
OPTION_B=BOUNDARY_SAFE_CLUSTER_AWARE_RARE_EVENT_METHOD
OPTION_B_GENERIC_CLUSTER_RESAMPLING_REFERENCE=A2STAT-002
UNCORRECTED_EMPIRICAL_CLUSTER_BOOTSTRAP_AT_ZERO_EVENTS=PROHIBITED
BOUNDARY_SAFE_NONZERO_UPPER_UNCERTAINTY_AT_ZERO_EVENTS=REQUIRED
```

Required non-statistical bindings remain upstream:

```text
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_IDENTITY=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_REVISION=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_RESULT_DIGEST_CONTRACT=NEEDS_EVIDENCE
```

Still unresolved:

```text
EXACT_CRITICAL_ERROR_EVENT_DEFINITION=NEEDS_EVIDENCE
EXACT_MAXIMUM_CRITICAL_ERROR_RATE=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PRIMARY_INTERVAL_OR_BOUNDARY_SAFE_CLUSTER_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 8. `selective_risk_at_target_coverage`

```text
METRIC_ID=selective_risk_at_target_coverage
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=CALIBRATION_OR_SELECTIVE_RISK_SCORE
```

A binary-rate interval must not be copied into this metric by convenience.

```text
PRIMARY_CANDIDATE_FAMILY=PREDECLARED_HELDOUT_RISK_CONTROL
CANDIDATE_METHODS=LEARN_THEN_TEST,CONFORMAL_RISK_CONTROL,DISTRIBUTION_FREE_RISK_CONTROL_IF_SEMANTICS_MATCH
REFERENCES=A2STAT-004,A2STAT-005,A2STAT-006
```

Candidate architecture:

```text
1. freeze exact loss/risk estimand before candidate results
2. freeze target-coverage semantics before candidate results
3. bind immutable selection-safe calibration/holdout identity
4. apply one predeclared risk-control procedure identically to comparable candidates
5. require the exact method assumptions to hold
6. prohibit candidate-result-driven method switching
```

Mandatory unresolved checks:

```text
LOSS_MONOTONICITY_IF_CRC_USED=NEEDS_PROOF_FOR_EXACT_PARAMETERIZATION
CALIBRATION_TARGET_EXCHANGEABILITY=NEEDS_EVIDENCE
DISTRIBUTION_SHIFT_HANDLING=NEEDS_PREDECLARED_POLICY
CALIBRATION_AND_EVALUATION_DATA_REUSE_SEMANTICS=NEEDS_EXACT_METHOD_JUSTIFICATION
TARGET_COVERAGE=NEEDS_NUMERIC_POLICY
ACCEPTABLE_RISK=NEEDS_NUMERIC_POLICY
```

```text
COPY_PUBLIC_80_90_95_PERCENT_COVERAGE_AS_COMMANDMED_POLICY=PROHIBITED
TREAT_RAW_CONFIDENCE_AS_CALIBRATED_PROBABILITY_WITHOUT_EVIDENCE=REJECT_AS_DEFAULT
REUSE_BINARY_RATE_N_FORMULA_WITHOUT_DERIVATION=PROHIBITED
```

## 9. `citation_entailment_fidelity`

```text
METRIC_ID=citation_entailment_fidelity
DIRECTION=HIGHER_BETTER
ESTIMAND_FAMILY=HIGHER_BETTER_PROPORTION_OR_FIDELITY
```

Because one answer/root may contain multiple dependent claims/citations, the current primary candidate is:

```text
PRIMARY_CANDIDATE_METHOD=ROOT_CASE_CLUSTER_RESAMPLING_ONE_SIDED_LOWER_BOUND
REFERENCE=A2STAT-002
```

This candidate is not automatically valid; exact bootstrap construction, cluster count, and estimand must be reviewed. The zero-event adverse-rate boundary issue above does not mechanically transfer to a higher-better fidelity functional, but all relevant boundary/degeneracy behavior must still be checked.

If the final scoring contract proves exactly one independent Bernoulli entailment outcome per root, a one-sided score/exact-binomial lower bound becomes a conditional candidate informed by `A2STAT-001`.

Still unresolved:

```text
EXACT_FIDELITY_ESTIMAND=NEEDS_EVIDENCE
DETERMINISTIC_VERIFIER_IDENTITY=NEEDS_EVIDENCE
CLINICIAN_AUDIT_PROTOCOL_IDENTITY=NEEDS_EVIDENCE
MINIMUM_ACCEPTABLE_POPULATION_FIDELITY=NEEDS_NUMERIC_POLICY
EXACT_CLUSTER_RESAMPLING_OR_BINOMIAL_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 10. `arabic_clinical_parity_gap`

```text
METRIC_ID=arabic_clinical_parity_gap
METRIC_EVIDENCE_ROLE=SELECTION_DEV
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=PAIRED_LANGUAGE_GAP
ANALYSIS_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
```

A paired root-task bootstrap is the current primary general candidate when the exact gap functional may be nonlinear/non-normal:

```text
PRIMARY_CANDIDATE_METHOD=PAIRED_ROOT_TASK_BOOTSTRAP_ONE_SIDED_UPPER_BOUND
RESAMPLING_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
```

Every resample must move Arabic and English realizations of a root together. Independent language resampling is prohibited.

If the frozen estimand is regular enough for a defensible paired analytic/studentized interval, that remains a conditional efficiency/sensitivity candidate. If parity itself is F1-based, `A2STAT-008` becomes directly relevant; otherwise it is only paired-design precedent.

Because PASS means a paired gap stays below a future maximum, one-sided noninferiority/equivalence-style confidence-bound semantics informed by `A2STAT-003` are candidates for qualified review without importing bioequivalence margins.

Still unresolved:

```text
SELECTION_SAFE_PAIRED_SUITE_IDENTITY=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
PAIRED_GAP_EXACT_FORMULA=NEEDS_EVIDENCE
MAXIMUM_ACCEPTABLE_PARITY_GAP=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PAIRED_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
WITHIN_PAIR_VARIANCE_OR_CONSERVATIVE_PLANNING_INPUT=NEEDS_EVIDENCE
COMPLETE_PAIR_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
ANCHOR_ROLE_STRATUM_ALLOCATION=NEEDS_STATISTICAL_DESIGN
```

## 11. `lab_report_field_extraction_accuracy`

```text
METRIC_ID=lab_report_field_extraction_accuracy
DIRECTION=HIGHER_BETTER
UNIT_OR_SCALE=f1_score
ESTIMAND_FAMILY=NONLINEAR_SUMMARY_SUCH_AS_F1
```

Candidate hierarchy:

```text
CANDIDATE_A=F1_SPECIFIC_EXACT_OR_VALIDATED_LARGE_SAMPLE_INTERVAL_AND_POWER_METHOD_IF_ASSUMPTIONS_FIT
REFERENCES_A=A2STAT-007,A2STAT-009

CANDIDATE_B=ROOT_CASE_CLUSTER_RESAMPLING_OF_EXACT_F1_FUNCTIONAL_IF_FIELDS_CLUSTER_WITHIN_REPORT
REFERENCE_B=A2STAT-002
```

`A2STAT-009` is relevant because it explicitly includes interval estimation and power/sample-size analysis for F1/F-beta, but commandMed must validate its assumptions against the exact field-extraction confusion/dependency structure before adoption.

For root-cluster resampling, the entire report/root moves together and F1 is recomputed on each root-resampled dataset. Bootstrap variant, independent-cluster sufficiency, and degeneracy/boundary behavior remain review items.

```text
NAIVE_NORMAL_INTERVAL_AROUND_F1_WITHOUT_VALIDATION=REJECT_AS_DEFAULT
FIELD_COUNT_AS_INDEPENDENT_N_WHEN_FIELDS_SHARE_REPORT_ROOT=PROHIBITED
REUSE_BINARY_ACCURACY_INTERVAL_AS_F1_INTERVAL=PROHIBITED
```

Still unresolved:

```text
EXACT_F1_VARIANT_MICRO_MACRO_OTHER=NEEDS_EVIDENCE
EXACT_SCORING_UNIT=NEEDS_EVIDENCE
ROOT_REPORT_DEPENDENCY_STRUCTURE=NEEDS_EVIDENCE
MINIMUM_ACCEPTABLE_F1=NEEDS_NUMERIC_POLICY
PRIMARY_F1_INFERENCE_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 12. Sample-size derivation classes

No numeric N is computed here.

| Metric family | Candidate N derivation class | Required planning inputs still missing |
|---|---|---|
| emergency miss | boundary-safe one-sided binomial inversion at root level; boundary-safe cluster-aware rare-event simulation/method only if root Bernoulli summary is unsuitable | threshold, confidence/error rate, event-rate assumption, root outcome/dependency |
| medication critical error | same boundary-safe rate family, with cluster-aware rare-event method only if necessary | threshold, confidence/error rate, event-rate assumption, medication truth/dependency |
| selective risk | method-specific calibration/risk-control finite-sample analysis | target coverage, risk budget, loss, exchangeability/error probability |
| citation fidelity | cluster-aware resampling/simulation or binomial only if exact independent root Bernoulli unit | threshold, root/claim structure, nuisance variance, confidence level |
| Arabic parity | paired precision/noninferiority design using paired variance or simulation for nonlinear gaps | maximum gap, paired variance, confidence/error rate, anchor/role allocation |
| lab F1 | F1-specific power calculation where assumptions fit; otherwise root-cluster simulation | minimum F1, prevalence/sensitivity/precision inputs, root dependency, F1 variant |

All nuisance assumptions must be candidate-neutral, pre-result, provenance-bound, and accompanied by sensitivity analysis or conservative justification when materially uncertain.

## 13. Fail-closed method-selection sequence

```text
STEP_1: bind exact metric/estimand/scoring unit/required stratum
  unresolved -> BLOCKED

STEP_2: bind independence/dependency structure
  root Bernoulli -> binomial family may be considered
  dependent observations within root -> root summary or cluster-aware method
  rare-event clustered gate -> method must be boundary-safe, including all-zero observations
  Arabic paired -> complete matched-pair method
  nonlinear F1 -> F1-specific or dependency-aware resampling method
  selective risk -> risk-control framework

STEP_3: bind directional rule
  lower-better -> upper bound vs frozen maximum
  higher-better -> lower bound vs frozen minimum

STEP_4: bind exact confidence/error-rate semantics
  unresolved -> no final method PASS and no numeric N freeze

STEP_5: bind nuisance/planning inputs and sensitivity analysis
  candidate-result-derived -> PROHIBITED

STEP_6: bind multiplicity structure
  global IUT is candidate-only; simultaneous strata/comparisons assessed separately

STEP_7: qualified statistical review disposition
  repository agent cannot self-approve

STEP_8: only after A2 policy freeze may D34 numeric N/allocation be frozen
```

## 14. Methods explicitly not selected

```text
CLOPPER_PEARSON_AS_UNIVERSAL_DEFAULT=NO
WILSON_AS_UNIVERSAL_DEFAULT=NO
CLUSTER_BOOTSTRAP_AS_UNIVERSAL_DEFAULT=NO
CONFORMAL_RISK_CONTROL_AS_UNIVERSAL_DEFAULT=NO
LEARN_THEN_TEST_AS_UNIVERSAL_DEFAULT=NO
F1_ANALYTIC_METHOD_AS_UNIVERSAL_DEFAULT=NO
PAIRED_BOOTSTRAP_AS_UNIVERSAL_DEFAULT=NO
BONFERRONI_AS_UNIVERSAL_DEFAULT=NO
NO_MULTIPLICITY_ADJUSTMENT_AS_UNIVERSAL_DEFAULT=NO
```

## 15. Exact review questions for a future qualified statistician

1. For `emergency_miss_rate`, should the primary root-level population qualification use exact inversion, a score-type method, or another boundary-safe one-sided construction at the expected N/event regime?
2. If emergency decisions are clustered within roots and cannot be reduced to a clinically valid Bernoulli root outcome, which **boundary-safe** cluster-aware rare-event method preserves nonzero uncertainty when zero events are observed?
3. For `medication_critical_error_rate`, what root-level adverse-event definition avoids pseudo-replication, and what boundary-safe method governs the upper bound under both zero and nonzero observed error counts?
4. For `selective_risk_at_target_coverage`, does the exact commandMed loss/abstention parameterization satisfy Learn-Then-Test, Conformal Risk Control, another risk-control framework, or none?
5. For `citation_entailment_fidelity`, should inference preserve claims/citations within answer root through cluster resampling, and which interval construction is acceptable at the planned cluster count?
6. For `arabic_clinical_parity_gap`, what exact paired gap estimand and one-sided paired uncertainty method should govern comparison with the maximum acceptable gap?
7. For `lab_report_field_extraction_accuracy`, do published F1-specific interval/power methods fit the exact scoring/dependency structure, or is root-cluster resampling required?
8. For the all-hard-gates-must-pass claim, is intersection-union the correct global structure, and what additional simultaneous stratum/candidate claims require multiplicity adjustment?
9. What pre-result sensitivity analyses are mandatory for event rates, paired variance, prevalence, root-cluster dependence, and selective-risk calibration assumptions?

No answer is fabricated here.

## 16. Review-remediation record for PR #78

The first exact-head review of this packet identified two material defects on head `ae8efae8cb5fd3015db4acdf1cfd227166390d61`:

```text
FINDING_1=GENERIC_CLUSTER_BOOTSTRAP_COULD_COLLAPSE_TO_ZERO_UPPER_BOUND_AT_ALL_ZERO_RARE_EVENT_BOUNDARY
FINDING_1_DISPOSITION=REPAIRED_BY_EXPLICIT_BOUNDARY_SAFE_RARE_EVENT_REQUIREMENT

FINDING_2=NONCANONICAL_D34_STATE_ALIAS_BLOCKED_BY_A2
FINDING_2_DISPOSITION=REPAIRED_TO_D34_A3_A4_BLOCKED_BY_T1
```

The old head is historical and cannot qualify the repaired head. A fresh exact-head review is required after this repair.

## 17. Current frontier

```text
R1_A1=CANONICAL_COMPLETE
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
A2_METHOD_SEARCH_SPACE=NARROWED_CANDIDATE_ONLY
D34_A3_A4=BLOCKED_BY_T1
REAL_THRESHOLD_POLICY_PASS_COUNT=0
REAL_STATISTICAL_DESIGN_PASS_COUNT=0
REAL_A2_TO_A14_SNAPSHOT=ABSENT
REAL_A15_ACTIVATION=ABSENT
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next valid transition is qualified clinical/statistical appraisal of identity-bound commandMed evidence and the candidate method set, not filling numeric placeholders.