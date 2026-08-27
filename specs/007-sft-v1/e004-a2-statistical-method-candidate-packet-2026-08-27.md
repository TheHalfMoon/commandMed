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
D34_STATE=BLOCKED_BY_A2
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Current authority boundary

The current frontier overlay at canonical main distinguishes E002 non-executing acquisition from E003 execution. This packet changes neither.

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

## 2. Frozen canonical constraints that this packet must obey

Session 9 Q3 remains controlling for statistical architecture.

```text
UNIVERSAL_SAMPLE_SIZE_N=PROHIBITED
ONE_SAMPLE_SIZE_FOR_ALL_METRICS=PROHIBITED
POINT_ESTIMATE_ALONE_SUFFICIENT_FOR_POPULATION_HARD_GATE_PASS=NO
LOWER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=UPPER_BOUND_AGAINST_FROZEN_MAXIMUM
HIGHER_BETTER_POPULATION_GATE_EVIDENCE_DIRECTION=LOWER_BOUND_AGAINST_FROZEN_MINIMUM
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

The candidate methods below are admissible for later qualified review only to the extent that they preserve these frozen constraints.

## 3. Public method-source inventory

The following sources are method references, not commandMed operating-point evidence.

| ID | Source | Stable locator | Candidate use | Transfer limitation |
|---|---|---|---|---|
| `A2STAT-001` | Brown, Cai, DasGupta, *Interval Estimation for a Binomial Proportion* | DOI `10.1214/ss/1009213286` | binomial interval behavior; Wilson/exact interval appraisal; avoid naive Wald defaults | does not choose commandMed confidence level, threshold, event rate, or N |
| `A2STAT-002` | Field, Welsh, *Bootstrapping Clustered Data* | DOI `10.1111/j.1467-9868.2007.00593.x` | cluster-resampling rationale when observations share a root/cluster | does not prove a particular commandMed bootstrap variant is valid for an unresolved estimand |
| `A2STAT-003` | Berger, Hsu, *Bioequivalence Trials, Intersection-Union Tests and Equivalence Confidence Sets* | DOI `10.1214/ss/1032280304` | intersection-union/equivalence decision architecture and confidence-set interpretation | bioequivalence margins/settings are not commandMed margins or confidence levels |
| `A2STAT-004` | Angelopoulos et al., *Learn then Test: Calibrating Predictive Algorithms to Achieve Risk Control* | arXiv `2110.01052` | finite-sample risk-control calibration candidate; predeclared testing procedure | assumptions and risk definition must match commandMed; no target risk/coverage transfers |
| `A2STAT-005` | Bates et al., *Distribution-Free, Risk-Controlling Prediction Sets* | DOI `10.1145/3478535` | held-out, distribution-free expected-risk control candidate | set-prediction examples are not automatically selective-risk semantics |
| `A2STAT-006` | Angelopoulos et al., *Conformal Risk Control* | ICLR 2024; arXiv `2208.02814` | monotone-loss conformal risk-control candidate | requires compatible loss/parameter monotonicity and exchangeability; no operating point transfers |
| `A2STAT-007` | Takahashi et al., *Confidence interval for micro-averaged F1 and macro-averaged F1 scores* | DOI `10.1007/s10489-021-02635-5`; PMID `35317080` | analytic F1 interval candidate under its scoring/independence assumptions | commandMed root-case dependence may invalidate direct use |
| `A2STAT-008` | Takahashi et al., *Hypothesis testing procedure for binary and multi-class F1-scores in the paired design* | DOI `10.1002/sim.9853`; PMID `37527903` | paired F1 inference reference | Arabic parity is not automatically an F1 comparison; use only if the frozen estimand matches |
| `A2STAT-009` | Hsu, Liu, Shyr, *A Unified Framework for Statistical Inference and Power Analysis of Single and Comparative F-beta Scores* | DOI `10.1002/sim.70557`; PMID `42050845` | exact/large-sample F1/F-beta interval and power/sample-size candidate | commandMed scoring unit/dependency structure must match before adoption |

No source above is a qualified statistical-review disposition. Public method publication is evidence that a method exists, not evidence that it is the correct commandMed method.

## 4. Candidate-method status vocabulary

```text
PRIMARY_CANDIDATE_FOR_REVIEW=
  strongest current method candidate given the frozen estimand family and dependency rules;
  not frozen and not approved

CONDITIONAL_CANDIDATE=
  potentially valid only if future exact scoring-unit/independence/distribution assumptions hold

SENSITIVITY_CANDIDATE=
  method useful as a predeclared robustness comparison, not the primary basis by default

REJECT_AS_DEFAULT=
  method should not become the default without a new explicit statistical justification

NEEDS_EXACT_ESTIMAND=
  method cannot be selected until exact estimand/scoring unit is identity-bound

NEEDS_QUALIFIED_STATISTICAL_REVIEW=
  no repository agent may convert the candidate into an approved method
```

## 5. Cross-metric inferential architecture candidates

### 5.1 Directional one-sided qualification evidence

The canonical hard gates are directional. A natural candidate architecture is therefore one-sided qualification evidence:

```text
LOWER_BETTER_GATE:
  candidate evidence = one-sided upper uncertainty bound
  future PASS condition = upper bound <= separately frozen maximum

HIGHER_BETTER_GATE:
  candidate evidence = one-sided lower uncertainty bound
  future PASS condition = lower bound >= separately frozen minimum
```

This merely restates the frozen Q3 direction in method-ready terms. The confidence level remains unresolved.

### 5.2 Root-first independence

The default candidate rule is:

```text
INDEPENDENT_N_UNIT=ROOT_CASE_OR_OTHER_EXACT_CANONICAL_ANALYSIS_UNIT
VARIANTS_WITHIN_ONE_ROOT=NOT_INDEPENDENT_N
MATCHED_ARABIC_ENGLISH_PAIR=ONE_PAIRED_ANALYSIS_UNIT
```

If the metric is computed from multiple dependent sub-observations inside one root case, candidate inference must either:

1. collapse them to a predeclared root-level metric before inference; or
2. use a dependency-aware method such as cluster resampling/modeling that preserves the root as the resampling cluster.

A naive row-level bootstrap that independently resamples dependent variants/claims/fields is not a candidate.

### 5.3 Cluster bootstrap candidate

`A2STAT-002` supports cluster bootstrap as a general dependency-aware candidate. For commandMed the proposed cluster identity is the canonical root case unless an exact future design proves another unit.

```text
CLUSTER_BOOTSTRAP_PRIMARY_RESAMPLING_UNIT=ROOT_CASE_CANDIDATE_ONLY
RESAMPLE_WITHIN_ROOT_INDEPENDENTLY=NO_BY_DEFAULT
BOOTSTRAP_VARIANT_PERCENTILE_BCA_STUDENTIZED=NOT_YET_SELECTED
BOOTSTRAP_REPETITION_COUNT=NOT_YET_FROZEN
SMALL_CLUSTER_COUNT_ACCEPTABILITY=NEEDS_STATISTICAL_REVIEW
```

This is a method family, not a frozen implementation.

### 5.4 Global hard-gate multiplicity candidate

Because overall quality-floor PASS requires every noncompensable hard gate to pass, an **intersection-union** formulation is a candidate for the global conjunction claim.

`A2STAT-003` supports review of intersection-union semantics, but commandMed must first define the exact null/alternative family.

Candidate question for statistical review:

```text
IF_GLOBAL_PASS_NULL=
  AT_LEAST_ONE_REQUIRED_GATE_FAILS_ITS_FROZEN_BOUND

AND_GLOBAL_PASS_ALTERNATIVE=
  EVERY_REQUIRED_GATE_SATISFIES_ITS_FROZEN_BOUND

THEN=
  INTERSECTION_UNION_TEST_ARCHITECTURE_IS_CANDIDATE_FOR_GLOBAL_PASS
```

This packet does **not** freeze `NO_MULTIPLICITY_ADJUSTMENT`. Simultaneous subgroup/stratum claims, multiple candidate comparisons, secondary analyses, or a differently formulated family may still require explicit multiplicity control.

```text
AUTOMATIC_BONFERRONI=NOT_FROZEN
AUTOMATIC_NO_CORRECTION=NOT_FROZEN
GLOBAL_IUT_CANDIDATE_REQUIRES_QUALIFIED_STATISTICAL_REVIEW=YES
```

## 6. `emergency_miss_rate`

Canonical family:

```text
METRIC_ID=emergency_miss_rate
DIRECTION=LOWER_BETTER
UNIT_OR_SCALE=ratio
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
```

### Primary candidate for review

If each independent root case contributes one predeclared binary emergency-miss outcome:

```text
PRIMARY_CANDIDATE_METHOD=ONE_SIDED_EXACT_BINOMIAL_UPPER_CONFIDENCE_BOUND
REFERENCE=A2STAT-001
```

Rationale:

- safety-critical miss events may be rare;
- zero observed misses cannot imply zero population risk;
- exact binomial inversion remains defined at boundary counts;
- Q3 requires an upper bound against a future frozen maximum.

### Conditional dependency-aware route

If a root produces multiple dependent emergency decisions rather than one binary root-level outcome:

```text
OPTION_A=PREDECLARE_ROOT_LEVEL_WORST_CASE_OR_OTHER_ROOT_SUMMARY_THEN_APPLY_APPROPRIATE_ROOT_LEVEL_METHOD
OPTION_B=ROOT_CLUSTER_BOOTSTRAP_OR_OTHER_CLUSTER_AWARE_METHOD
REFERENCE_FOR_OPTION_B=A2STAT-002
```

The root summary itself must be frozen before seeing candidate results.

### Sensitivity candidate

A Wilson/score-type one-sided interval may be reviewed as a sensitivity/efficiency comparison under independent Bernoulli assumptions, informed by `A2STAT-001`.

### Rejected default

```text
NAIVE_WALD_NORMAL_INTERVAL=REJECT_AS_DEFAULT
ZERO_EVENT_POINT_ESTIMATE_AS_PASS=PROHIBITED
RULE_OF_THREE_AS_COMPLETE_SCIENTIFIC_JUSTIFICATION=REJECT_AS_DEFAULT
```

### Still unresolved

```text
EXACT_ROOT_OUTCOME_DEFINITION=NEEDS_EVIDENCE
EXACT_MAXIMUM_MISS_RATE=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PRIMARY_INTERVAL_VARIANT=NEEDS_QUALIFIED_STATISTICAL_REVIEW
ANTICIPATED_OR_CONSERVATIVE_EVENT_RATE_FOR_N=NEEDS_EVIDENCE
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 7. `medication_critical_error_rate`

Canonical family:

```text
METRIC_ID=medication_critical_error_rate
DIRECTION=LOWER_BETTER
UNIT_OR_SCALE=ratio
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
```

### Primary candidate for review

The same exact-binomial upper-bound family is a candidate **only if** one independent root case contributes one predeclared binary critical-medication-error outcome.

```text
PRIMARY_CANDIDATE_METHOD=ONE_SIDED_EXACT_BINOMIAL_UPPER_CONFIDENCE_BOUND_IF_ROOT_LEVEL_BERNOULLI
REFERENCE=A2STAT-001
```

### Dependency-aware candidate

Medication tasks may contain multiple medications, interactions, doses, or sub-decisions within one root. Those sub-decisions must not be counted as independent N merely because they are separately scorable.

```text
MULTIPLE_SUBDECISIONS_PER_ROOT_INDEPENDENT_N=NO
ROOT_CLUSTER_BOOTSTRAP_OR_PREDECLARED_ROOT_SUMMARY=CANDIDATE
REFERENCE=A2STAT-002
```

### Required non-statistical bindings remain upstream

```text
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_IDENTITY=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_REVISION=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_RESULT_DIGEST_CONTRACT=NEEDS_EVIDENCE
```

The statistical method cannot compensate for unresolved medication-reference truth.

### Still unresolved

```text
EXACT_CRITICAL_ERROR_EVENT_DEFINITION=NEEDS_EVIDENCE
EXACT_MAXIMUM_CRITICAL_ERROR_RATE=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PRIMARY_INTERVAL_OR_CLUSTER_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 8. `selective_risk_at_target_coverage`

Canonical family:

```text
METRIC_ID=selective_risk_at_target_coverage
DIRECTION=LOWER_BETTER
UNIT_OR_SCALE=score
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=CALIBRATION_OR_SELECTIVE_RISK_SCORE
```

A binary-rate interval must **not** be copied into this metric by convenience.

### Primary candidate family for review

A held-out finite-sample risk-control framework is the strongest current candidate family:

```text
PRIMARY_CANDIDATE_FAMILY=PREDECLARED_HELDOUT_RISK_CONTROL
CANDIDATE_METHODS=
  LEARN_THEN_TEST,
  CONFORMAL_RISK_CONTROL,
  DISTRIBUTION_FREE_RISK_CONTROLLING_PREDICTION_METHODS_IF_SEMANTICS_MATCH
REFERENCES=A2STAT-004,A2STAT-005,A2STAT-006
```

Candidate architecture:

```text
1. freeze exact loss/risk estimand before candidate results;
2. freeze target-coverage semantics before candidate results;
3. bind an immutable selection-safe calibration/holdout identity;
4. apply one predeclared calibration/risk-control procedure identically to comparable candidates;
5. evaluate the resulting selective risk with the method's valid finite-sample guarantee;
6. keep candidate-result-driven method switching prohibited.
```

### Mandatory assumption checks before adoption

```text
LOSS_MONOTONICITY_IF_CRC_USED=NEEDS_PROOF_FOR_EXACT_PARAMETERIZATION
CALIBRATION_TARGET_EXCHANGEABILITY=NEEDS_EVIDENCE
DISTRIBUTION_SHIFT_HANDLING=NEEDS_PREDECLARED_POLICY
CALIBRATION_AND_EVALUATION_DATA_REUSE_SEMANTICS=NEEDS_EXACT_METHOD_JUSTIFICATION
TARGET_COVERAGE=NEEDS_NUMERIC_POLICY
ACCEPTABLE_RISK=NEEDS_NUMERIC_POLICY
```

### Rejected default

```text
COPY_80_OR_90_OR_95_PERCENT_COVERAGE_FROM_PUBLIC_PAPER=PROHIBITED
TREAT_CONFIDENCE_SCORE_AS_CALIBRATED_PROBABILITY_WITHOUT_EVIDENCE=REJECT_AS_DEFAULT
REUSE_BINARY_RATE_N_FORMULA_WITHOUT_METHOD_DERIVATION=PROHIBITED
```

## 9. `citation_entailment_fidelity`

Canonical family:

```text
METRIC_ID=citation_entailment_fidelity
DIRECTION=HIGHER_BETTER
UNIT_OR_SCALE=percentage
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=HIGHER_BETTER_PROPORTION_OR_FIDELITY
```

Citation presence is not entailment. The deterministic verifier and clinician-audit identities remain separate prerequisites.

### Primary candidate for review

Because one answer/root case may contain multiple dependent claims/citations, the current primary candidate is a **root-case cluster bootstrap lower confidence bound** on the exact future fidelity estimand.

```text
PRIMARY_CANDIDATE_METHOD=ROOT_CASE_CLUSTER_BOOTSTRAP_ONE_SIDED_LOWER_BOUND
REFERENCE=A2STAT-002
```

This candidate preserves all within-root citation/claim structure while resampling roots.

### Conditional candidate

If the final scoring contract instead proves exactly one independent Bernoulli entailment outcome per root case, a one-sided Wilson/score or exact-binomial lower bound becomes a conditional candidate informed by `A2STAT-001`.

```text
BINOMIAL_METHOD_ALLOWED_ONLY_IF_EXACT_SCORING_UNIT_IS_INDEPENDENT_BERNOULLI=YES
```

### Still unresolved

```text
EXACT_FIDELITY_ESTIMAND=NEEDS_EVIDENCE
DETERMINISTIC_VERIFIER_IDENTITY=NEEDS_EVIDENCE
CLINICIAN_AUDIT_PROTOCOL_IDENTITY=NEEDS_EVIDENCE
MINIMUM_ACCEPTABLE_POPULATION_FIDELITY=NEEDS_NUMERIC_POLICY
BOOTSTRAP_VARIANT_AND_REPLICATION_COUNT=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 10. `arabic_clinical_parity_gap`

Canonical V2 family:

```text
METRIC_ID=arabic_clinical_parity_gap
METRIC_EVIDENCE_ROLE=SELECTION_DEV
DIRECTION=LOWER_BETTER
UNIT_OR_SCALE=relative_gap
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=PAIRED_LANGUAGE_GAP
ANALYSIS_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
```

### Primary candidate for review

A **paired root-task bootstrap** preserving the Arabic-English pair is the current primary general candidate when the exact gap functional may be nonlinear or non-normal.

```text
PRIMARY_CANDIDATE_METHOD=PAIRED_ROOT_TASK_BOOTSTRAP_ONE_SIDED_UPPER_BOUND
RESAMPLING_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
REFERENCE_FAMILY=A2STAT-002
```

Every resample must move the Arabic and English realizations of a root together. Resampling Arabic and English items independently is prohibited.

### Conditional analytic candidate

If the exact frozen estimand reduces to a regular paired mean difference/gap with assumptions supporting a large-sample analytic interval, a paired analytic/studentized approach may be reviewed as an efficiency/sensitivity candidate.

If the parity metric itself is F1-based, `A2STAT-008` becomes directly relevant; otherwise it remains only a paired-design precedent and must not be copied mechanically.

### Equivalence/noninferiority decision architecture candidate

Because PASS means the paired gap must remain below a future maximum acceptable margin, the statistical review should explicitly consider one-sided noninferiority/equivalence-style confidence-bound semantics, informed by `A2STAT-003`, without importing bioequivalence margins.

### Still unresolved

```text
SELECTION_SAFE_PAIRED_SUITE_IDENTITY=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
PAIRED_GAP_EXACT_FORMULA=NEEDS_EVIDENCE
MAXIMUM_ACCEPTABLE_PARITY_GAP=NEEDS_NUMERIC_POLICY
EXACT_CONFIDENCE_LEVEL=NEEDS_QUALIFIED_STATISTICAL_REVIEW
EXACT_PAIRED_BOOTSTRAP_OR_ANALYTIC_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
WITHIN_PAIR_VARIANCE_OR_CONSERVATIVE_PLANNING_INPUT=NEEDS_EVIDENCE
COMPLETE_PAIR_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
ANCHOR_ROLE_STRATUM_ALLOCATION=NEEDS_STATISTICAL_DESIGN
```

## 11. `lab_report_field_extraction_accuracy`

Canonical family:

```text
METRIC_ID=lab_report_field_extraction_accuracy
DIRECTION=HIGHER_BETTER
UNIT_OR_SCALE=f1_score
DECISION_ROLE=HARD_GATE
ESTIMAND_FAMILY=NONLINEAR_SUMMARY_SUCH_AS_F1
```

### Candidate hierarchy for review

The exact future scoring contract must determine whether direct F1-specific analytic inference is valid or whether root-case dependency requires resampling.

#### Candidate A — F1-specific exact/analytic method

If the metric can be represented by the assumptions required by the F1 inference framework and the statistical unit is independent at the required level:

```text
CANDIDATE_A=F1_SPECIFIC_EXACT_OR_VALIDATED_LARGE_SAMPLE_INTERVAL_AND_POWER_METHOD
REFERENCES=A2STAT-007,A2STAT-009
```

`A2STAT-009` is particularly relevant because it includes interval estimation and power/sample-size analysis for F1/F-beta, but commandMed must validate its assumptions against the exact field-extraction confusion structure before adoption.

#### Candidate B — root-case cluster bootstrap

If multiple extracted fields within one report/root are dependent and the final F1 is a nonlinear aggregate over them:

```text
CANDIDATE_B=ROOT_CASE_CLUSTER_BOOTSTRAP_OF_EXACT_F1_FUNCTIONAL
REFERENCE=A2STAT-002
```

This preserves within-report field dependence and directly recomputes F1 for each root-resampled dataset.

### Rejected default

```text
NAIVE_NORMAL_INTERVAL_AROUND_F1_WITHOUT_VALIDATION=REJECT_AS_DEFAULT
FIELD_COUNT_AS_INDEPENDENT_N_WHEN_FIELDS_SHARE_REPORT_ROOT=PROHIBITED
REUSE_BINARY_ACCURACY_INTERVAL_AS_F1_INTERVAL=PROHIBITED
```

### Still unresolved

```text
EXACT_F1_VARIANT_MICRO_MACRO_OTHER=NEEDS_EVIDENCE
EXACT_SCORING_UNIT=NEEDS_EVIDENCE
ROOT_REPORT_DEPENDENCY_STRUCTURE=NEEDS_EVIDENCE
MINIMUM_ACCEPTABLE_F1=NEEDS_NUMERIC_POLICY
PRIMARY_F1_INFERENCE_METHOD=NEEDS_QUALIFIED_STATISTICAL_REVIEW
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 12. Sample-size derivation candidates by metric family

No numeric N is computed here. The packet narrows only the derivation class.

| Metric family | Candidate N derivation class | Required planning inputs still missing |
|---|---|---|
| emergency miss rate | exact/score one-sided binomial decision or precision inversion; cluster-aware simulation if clustered | threshold/margin, confidence/error rate, anticipated/conservative event rate, root outcome definition |
| medication critical error rate | exact/score binomial inversion if root Bernoulli; cluster-aware simulation otherwise | threshold, confidence/error rate, event-rate assumption, dependency, medication truth bindings |
| selective risk | method-specific calibration/risk-control sample-size or finite-sample guarantee analysis | target coverage, risk budget, loss definition, calibration assumptions, error probability |
| citation fidelity | cluster-bootstrap/simulation precision or threshold-crossing design; binomial only if exact independent Bernoulli unit | threshold, root/claim structure, nuisance variance, confidence level |
| Arabic parity | paired precision/noninferiority design using paired variance or conservative bound; simulation if nonlinear | maximum gap, paired variance, confidence/error rate, anchor/role allocation |
| lab F1 | F1-specific exact/analytic power calculation where assumptions fit; otherwise root-cluster simulation | minimum F1, prevalence/sensitivity/precision planning inputs, root dependency, scoring variant |

All nuisance assumptions must be candidate-neutral, pre-result, provenance-bound, and accompanied by sensitivity analysis or a conservative justification when materially uncertain.

## 13. Candidate method-selection decision tree

A future qualified statistical reviewer should be able to apply the following fail-closed sequence.

```text
STEP_1: bind exact metric/estimand/scoring unit/required stratum
  if unresolved -> BLOCKED

STEP_2: identify independence structure
  if one independent Bernoulli per root -> binomial family may be considered
  if multiple dependent observations per root -> root aggregation or cluster-aware method required
  if Arabic paired -> complete matched-pair method required
  if nonlinear F1 -> F1-specific or resampling method required
  if selective-risk calibration -> risk-control framework required

STEP_3: bind directional decision rule
  lower-better -> upper bound against frozen maximum
  higher-better -> lower bound against frozen minimum

STEP_4: bind exact confidence/error-rate semantics
  if unresolved -> no final method PASS and no numeric N freeze

STEP_5: bind nuisance/planning inputs and sensitivity analysis
  if candidate-result-derived -> PROHIBITED

STEP_6: bind multiplicity structure
  assess global IUT candidate and any simultaneous subgroup/comparison family separately

STEP_7: qualified statistical review disposition
  repository agent cannot self-approve

STEP_8: only after A2 policy freeze may D34 numeric N/allocation be frozen
```

## 14. Methods explicitly not selected by this packet

```text
CLOPPER_PEARSON_AS_UNIVERSAL_DEFAULT=NO
WILSON_AS_UNIVERSAL_DEFAULT=NO
CLUSTER_BOOTSTRAP_AS_UNIVERSAL_DEFAULT=NO
CONFORMAL_RISK_CONTROL_AS_UNIVERSAL_DEFAULT=NO
LEARN_THEN_TEST_AS_UNIVERSAL_DEFAULT=NO
PSF1_AS_UNIVERSAL_DEFAULT=NO
PAIRED_BOOTSTRAP_AS_UNIVERSAL_DEFAULT=NO
BONFERRONI_AS_UNIVERSAL_DEFAULT=NO
NO_MULTIPLICITY_ADJUSTMENT_AS_UNIVERSAL_DEFAULT=NO
```

The purpose is to reduce the method search space without replacing expert review.

## 15. Exact review questions now ready for a qualified statistician

The following questions are now concrete enough for external statistical review without requiring candidate results:

1. For `emergency_miss_rate`, should the primary population qualification use an exact one-sided binomial upper bound at the root level, or a score/other interval with better operating characteristics at the expected N/event-rate regime?
2. For `medication_critical_error_rate`, what exact root-level adverse-event definition avoids pseudo-replication across multiple medication sub-decisions, and which one-sided method should govern the bound?
3. For `selective_risk_at_target_coverage`, does the exact commandMed loss/abstention parameterization satisfy the assumptions for Learn-Then-Test, Conformal Risk Control, another risk-controlling prediction procedure, or none of them?
4. For `citation_entailment_fidelity`, should inference use a root-case cluster bootstrap because one answer contains multiple dependent claims/citations, and which bootstrap interval construction is acceptable at the planned cluster count?
5. For `arabic_clinical_parity_gap`, what exact paired gap estimand and one-sided paired uncertainty method should govern noninferiority to the maximum acceptable gap?
6. For `lab_report_field_extraction_accuracy`, does the exact F1 scoring structure fit the assumptions of published F1-specific interval/power methods, or is root-case cluster resampling required?
7. For the overall all-hard-gates-must-pass claim, is an intersection-union test formulation the correct global multiplicity architecture, and what additional simultaneous stratum/candidate claims require separate adjustment?
8. What pre-result sensitivity analyses are mandatory for uncertain event rates, paired variance, prevalence, root-cluster dependence, and selective-risk calibration assumptions?

No answer to these questions is fabricated here.

## 16. Current frontier after this research packet

If this packet is later reviewed and merged, the state remains:

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

The next valid transition is not to fill numeric placeholders. It is qualified clinical/statistical appraisal of identity-bound commandMed evidence and the candidate method set, followed by a pre-result numeric policy freeze only if the evidence supports one.