# E004 A2 Qualified Clinical / Statistical Review Request Brief — 2026-08-27

**Spec:** 007 SFT V1  
**Parent candidate packet head:** `ae8efae8cb5fd3015db4acdf1cfd227166390d61`  
**Parent candidate packet path:** `specs/007-sft-v1/e004-a2-statistical-method-candidate-packet-2026-08-27.md`  
**Artifact class:** reviewer-request template / coordination metadata only  
**Authority effect:** NONE  
**Review disposition created:** NO  
**Reviewer appointed:** NO  
**Validator input:** NO

This brief turns the already-frozen Session 9 Q3/Q4 governance requirements and the candidate-only A2 statistical-method packet into a bounded request that a future qualified reviewer can answer. It does **not** appoint a reviewer, assert credentials, create an authority identity, define a new disposition vocabulary, approve a method, freeze a threshold/margin, freeze a confidence level, freeze numeric N, or create a `ThresholdPolicy` / `StatisticalDesign` record.

```text
REVIEW_REQUEST_ONLY=YES
CLINICAL_REVIEW_AUTHORITY_IDENTITY=UNRESOLVED
STATISTICAL_REVIEW_AUTHORITY_IDENTITY=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
CANONICAL_GOVERNANCE_ADOPTION=ABSENT
NUMERIC_THRESHOLD_OR_MARGIN_FREEZE=NO
NUMERIC_CONFIDENCE_LEVEL_FREEZE=NO
NUMERIC_ALPHA_BETA_POWER_FREEZE=NO
NUMERIC_N_FREEZE=NO
A2_REAL_PASS=NO
D34_REAL_PASS=NO
E004_STATE=BLOCKED_PREFLIGHT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling governance

Session 9 Q4 requires three distinct authority functions before any numeric threshold/margin can become canonical:

```text
1. CLINICAL_DOMAIN_REVIEW
2. STATISTICAL_METHOD_REVIEW
3. CANONICAL_GOVERNANCE_ADOPTION
```

No one function may substitute for another.

```text
FOUNDER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO
CLINICIAN_SOLE_STATISTICAL_METHOD_AUTHORITY=NO
STATISTICIAN_SOLE_CLINICAL_ACCEPTABILITY_AUTHORITY=NO
EVALUATION_OWNER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO
```

This request therefore separates the clinical and statistical questions below. A reviewer may answer only the scope for which their future authority is independently established.

## 2. What this brief deliberately does not define

Canonical governance has **not** frozen:

```text
EXACT_REVIEWER_IDENTITIES
EXACT_REVIEWER_COUNT
EXACT_REVIEWER_CREDENTIAL_REQUIREMENTS
EXACT_QUORUM_RULE
EXACT_DISAGREEMENT_RESOLUTION_PROTOCOL
EXACT_REVIEW_DISPOSITION_VOCABULARY_FOR_THRESHOLD_GOVERNANCE
```

This brief must not fill those gaps by convention.

In particular:

```text
DOCUMENT_AUTHOR_IS_REVIEWER=NO
GITHUB_PR_REVIEW_EQUALS_QUALIFIED_CLINICAL_REVIEW=NO
GITHUB_PR_REVIEW_EQUALS_QUALIFIED_STATISTICAL_REVIEW=NO
QODO_OR_OTHER_CODE_REVIEW_EQUALS_SCIENTIFIC_REVIEW=NO
LLM_GENERATED_RECOMMENDATION_EQUALS_QUALIFIED_REVIEW=NO
SILENCE_OR_NO_COMMENT_EQUALS_APPROVAL=NO
MAJORITY_VOTE_AUTO_AUTHORITY=NO
```

A future canonical review artifact must use whatever exact disposition vocabulary and identity mechanism is separately governed at that time. Until then, this brief requests **reasoned findings**, not a fabricated enum.

## 3. Immutable review inputs

A future qualified review should bind exact versions of at least:

```text
A2_PUBLIC_EVIDENCE_DISCOVERY
  specs/007-sft-v1/e004-a2-public-threshold-evidence-discovery-2026-08-27.md

A2_EVIDENCE_WORKBENCH
  specs/007-sft-v1/e004-a2-evidence-package-workbench-2026-08-27.md

A2_STATISTICAL_METHOD_CANDIDATE_PACKET
  specs/007-sft-v1/e004-a2-statistical-method-candidate-packet-2026-08-27.md
  exact parent head at request creation = ae8efae8cb5fd3015db4acdf1cfd227166390d61

STATISTICAL_ARCHITECTURE
  specs/005-base-model-tournament/session-9-q3-statistical-rationale-sample-size-power-architecture.md

REVIEW_GOVERNANCE
  specs/005-base-model-tournament/session-9-q4-clinical-review-threshold-margin-governance.md

CURRENT_FRONTIER
  specs/007-sft-v1/e004-current-frontier-reconciliation-2026-08-27.md
```

If any reviewed input changes materially before adoption, the review must be treated as stale until re-bound/re-reviewed.

## 4. Candidate-result firewall

The review must occur without using tournament candidate performance to choose the scientific policy.

```text
TOURNAMENT_CANDIDATE_RESULTS_AVAILABLE_TO_SET_THRESHOLD=NO
PREFERRED_CANDIDATE_RESULT_AVAILABLE_TO_SET_MARGIN=NO
PRIVATE_GOLD_SELECTION_RESULTS_AVAILABLE_TO_SET_POLICY=NO
PUBLIC_EXTERNAL_TEST_RESULTS_USED_POST_HOC=NO
DESIRED_PASS_RATE_AS_POLICY_BASIS=NO
DESIRED_WINNER_AS_POLICY_BASIS=NO
```

Any response that relies materially on such information is not eligible to support a pre-result A2 freeze.

## 5. Required identity / conflict disclosures for a future review record

This brief does not create the identities, but a future auditable review should be able to bind:

```text
review_authority_identity
review_scope
metric_or_metric_family_scope
reviewed_artifact_ids_and_revisions
review_date_or_audit_sequence
candidate_result_exposure_state
role_or_conflict_disclosures
material_limitations
reasoned_findings
review_disposition_under_then-canonical-vocabulary
```

For threshold adoption, the future policy must ultimately bind both:

```text
clinical_review_authority_identity_and_disposition
statistical_review_authority_identity_and_disposition
```

plus governance adoption and any conflict/disagreement records required by the then-current canonical rules.

## 6. Statistical-method reviewer — cross-metric questions

A future qualified statistical/methodological reviewer is requested to answer the following **without** choosing values from candidate results.

### S-1 — estimand compatibility

For each hard-gate metric:

- Is the proposed estimand family mathematically aligned with the canonical metric semantics?
- What exact estimand definition must be frozen before a method can be approved?
- Is the proposed unit of analysis compatible with that estimand?
- What ambiguity, if any, blocks method selection?

### S-2 — independence / dependence structure

For each metric:

- What is the independent statistical unit?
- Which observations share a canonical root and therefore cannot be counted as independent `N`?
- Is root aggregation scientifically preferable to cluster-aware inference for this metric?
- If resampling is used, what must move together in each resample?

Arabic review must preserve:

```text
INDEPENDENT_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
UNPAIRED_TWO_SAMPLE_LANGUAGE_SHORTCUT=PROHIBITED
```

### S-3 — uncertainty direction

Confirm or reject the canonical directional architecture:

```text
LOWER_BETTER_GATE -> one-sided upper uncertainty bound vs frozen maximum
HIGHER_BETTER_GATE -> one-sided lower uncertainty bound vs frozen minimum
```

If another construction is required, explain why it is mathematically preferable without weakening the hard-gate semantics.

### S-4 — exact method family

For each metric, assess the candidate method family in Sections 8–13 below and state:

- assumptions required;
- assumptions currently evidenced;
- assumptions still unproven;
- method variants that remain scientifically plausible;
- variants that should be excluded;
- whether the search space is sufficiently narrow for a later numeric design.

### S-5 — confidence / error-rate semantics

Do **not** supply a numeric confidence level merely by convention.

Instead state:

- what error probability the final rule should control;
- whether the rule is estimation-, qualification-, noninferiority-, equivalence-, or other decision-oriented;
- whether the error-rate parameter is per-gate, family-wise, simultaneous, or conditional on another structure;
- what additional evidence is required before choosing a numeric level.

### S-6 — multiplicity structure

Assess whether the overall all-required-hard-gates-must-pass claim is naturally represented as an intersection-union structure.

Separately identify multiplicity created by:

- simultaneous required strata;
- multiple candidate comparisons;
- repeated endpoints within a metric family;
- secondary/sensitivity claims;
- any later subgroup claims.

This request does not presume either Bonferroni or no adjustment.

### S-7 — nuisance assumptions and sensitivity analysis

For every planning input that materially changes N or operating characteristics, state:

- required nuisance parameter;
- acceptable evidence source class;
- conservative planning alternative if no strong estimate exists;
- sensitivity range that should be predeclared;
- whether simulation is required instead of a closed-form calculation.

### S-8 — small-sample / rare-event behavior

For binary safety gates, explicitly assess boundary behavior when zero or few failures are observed. Point estimate zero may never be treated as zero population risk.

### S-9 — sample-size derivation readiness

For each metric, conclude whether the **derivation class** is sufficiently specified to proceed later to D34 once A2 numeric policy exists.

Do not provide final numeric N unless the required A2 threshold/margin/error-rate inputs have already become canonically frozen through the proper process.

## 7. Clinical-domain reviewer — cross-metric questions

A future qualified clinical-domain reviewer is requested to evaluate clinical meaningfulness separately from statistical adequacy.

For each metric:

- Is the metric clinically interpretable for the exact intended role/population/use context?
- What harm or failure mode does the threshold need to bound?
- What evidence is relevant to clinical acceptability, and what evidence is merely contextual?
- Are the public sources transferable to commandMed, partially transferable, or non-transferable for a numeric policy?
- What commandMed-specific evidence must exist before a threshold can be clinically supported?
- What material clinical dissent or limitation must be recorded?
- Does the metric require specialty-specific review beyond a generic clinical credential?

Clinical review must not determine statistical adequacy by itself.

## 8. Metric brief — `emergency_miss_rate`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
CANDIDATE_METHOD=ONE_SIDED_ROOT_LEVEL_BINOMIAL_BOUND_IF_ONE_BERNOULLI_OUTCOME_PER_ROOT
DEPENDENCY_FALLBACK=ROOT_SUMMARY_OR_CLUSTER_AWARE_METHOD
```

### Statistical review questions

1. Should exact binomial inversion remain the primary candidate at plausible low event counts, or should a score/other one-sided interval be preferred for operating-characteristic reasons?
2. What root-level binary event definition is necessary for the binomial model to be valid?
3. If multiple emergency decisions occur inside one root, should the primary analysis collapse to a predeclared worst-case/root indicator or use cluster-aware inference?
4. What planning event-rate or conservative bound can be justified without candidate results?
5. What sensitivity analysis is required for rare-event uncertainty?

### Clinical review questions

1. What exactly constitutes a clinically critical emergency miss in the intended-use scope?
2. Which acute/emergency expertise is required to assess that definition?
3. What evidence could justify the future maximum acceptable population miss rate?
4. Are any miss classes noncompensable or severity-weighted in a way that requires metric redesign before thresholding?

## 9. Metric brief — `medication_critical_error_rate`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
CANDIDATE_METHOD=ONE_SIDED_ROOT_LEVEL_BINOMIAL_BOUND_IF_ONE_BERNOULLI_OUTCOME_PER_ROOT
DEPENDENCY_FALLBACK=ROOT_SUMMARY_OR_CLUSTER_AWARE_METHOD
```

### Statistical review questions

1. Can one root case yield one predeclared critical-error indicator without discarding clinically important dependence?
2. If multiple medication sub-decisions are scored, what root-cluster method is appropriate?
3. What event-rate nuisance assumptions are acceptable for N planning?
4. What boundary behavior is required when zero critical errors are observed?

### Clinical review questions

1. What error taxonomy qualifies as `critical`?
2. What medication/pharmacology safety expertise is required?
3. Is an authoritative medication lookup/source identity required for every scored decision, and what revision/freshness rules apply?
4. What evidence could support the future maximum acceptable critical-error rate?

Unresolved medication truth-source identity cannot be cured by statistical method choice.

## 10. Metric brief — `selective_risk_at_target_coverage`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=CALIBRATION_OR_SELECTIVE_RISK_SCORE
CANDIDATE_FAMILY=HELDOUT_FINITE_SAMPLE_RISK_CONTROL
METHOD_CANDIDATES=LEARN_THEN_TEST,CONFORMAL_RISK_CONTROL,OTHER_DISTRIBUTION_FREE_RISK_CONTROL_IF_SEMANTICS_MATCH
```

### Statistical review questions

1. What exact loss/risk functional is commandMed controlling?
2. What exactly does target coverage mean for the intended abstention behavior?
3. Do the exact loss/parameterization satisfy monotonicity assumptions required by Conformal Risk Control if used?
4. What exchangeability or distributional assumptions are required, and how should expected shift be handled?
5. Must calibration and final evaluation use disjoint identity-bound data?
6. Which finite-sample guarantee is scientifically aligned with the hard gate?
7. What sample-size/calibration-size derivation follows from the chosen framework?

### Clinical review questions

1. Which abstentions are clinically safe/useful versus harmful non-answers?
2. What clinical harms define the risk function?
3. What coverage tradeoff is clinically meaningful for the exact user role?
4. Why should any future numeric risk/coverage operating point be acceptable?

Public 80/90/95% operating points are not transferable policy by default.

## 11. Metric brief — `citation_entailment_fidelity`

```text
DIRECTION=HIGHER_BETTER
ESTIMAND_FAMILY=HIGHER_BETTER_PROPORTION_OR_FIDELITY
PRIMARY_CANDIDATE=ROOT_CASE_CLUSTER_BOOTSTRAP_ONE_SIDED_LOWER_BOUND_IF_MULTIPLE_CLAIMS_PER_ROOT
CONDITIONAL_BINOMIAL_ROUTE=ONLY_IF_EXACT_ONE_INDEPENDENT_BERNOULLI_OUTCOME_PER_ROOT
```

### Statistical review questions

1. What is the exact population fidelity estimand: claim-weighted, root-weighted, macro/micro, or another construct?
2. Are multiple citations/claims inside one answer dependent enough to require root-cluster resampling?
3. What bootstrap interval construction and minimum independent-cluster regime are acceptable?
4. If a root-level Bernoulli simplification is proposed, what information loss does it create?

### Clinical review questions

1. What constitutes clinically sufficient entailment/support rather than mere citation presence?
2. What clinician-audit protocol must validate deterministic verifier behavior?
3. What evidence-grounded clinical expertise is required for review?
4. What minimum fidelity could be clinically meaningful, without using candidate results to set it?

## 12. Metric brief — `arabic_clinical_parity_gap`

```text
DIRECTION=LOWER_BETTER
EVIDENCE_ROLE=SELECTION_DEV
ESTIMAND_FAMILY=PAIRED_LANGUAGE_GAP
ANALYSIS_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
PRIMARY_GENERAL_CANDIDATE=PAIRED_ROOT_TASK_BOOTSTRAP_ONE_SIDED_UPPER_BOUND
UNPAIRED_ROUTE=PROHIBITED
```

### Statistical review questions

1. What exact paired gap functional should be frozen?
2. Is paired root bootstrap appropriate for that functional, or does a more efficient paired analytic/studentized method have defensible assumptions?
3. Should the future decision be framed as one-sided noninferiority to a maximum acceptable gap, equivalence, or another exact rule?
4. What within-pair variability/planning inputs are required?
5. How must five Arabic coverage anchors, role strata, and overlapping strata enter D34 allocation and multiplicity?

### Clinical review questions

1. Does the exact paired suite preserve clinical semantic equivalence across Arabic and English?
2. What Arabic-English clinical semantic expertise is required?
3. How should Saudi/Gulf colloquial, code-switching, medication nomenclature, emergency triage, and Modern Standard Arabic anchors affect clinical acceptability?
4. What maximum gap could be clinically meaningful, and what evidence would justify it?

Private Gold remains a separate final-audit role and cannot supply selection policy from candidate results.

## 13. Metric brief — `lab_report_field_extraction_accuracy`

```text
DIRECTION=HIGHER_BETTER
ESTIMAND_FAMILY=NONLINEAR_SUMMARY_SUCH_AS_F1
CANDIDATE_A=F1_SPECIFIC_VALIDATED_ANALYTIC_OR_EXACT_METHOD_IF_ASSUMPTIONS_FIT
CANDIDATE_B=ROOT_CASE_CLUSTER_BOOTSTRAP_OF_EXACT_F1_FUNCTIONAL_IF_FIELDS_CLUSTER_WITHIN_REPORT
```

### Statistical review questions

1. What exact F1 variant is canonical: micro, macro, another aggregation, or a different metric?
2. What is the independent unit: report/root, field, or another identity?
3. Do published F1 interval/power methods fit the exact confusion/prevalence/dependency structure?
4. If not, is root-case cluster bootstrap valid at the expected cluster count?
5. What prevalence/sensitivity/precision nuisance inputs are required for planning?
6. How should rare fields or field-family strata be handled without pseudo-replication?

### Clinical review questions

1. Which lab fields are clinically material versus administrative?
2. Are some field extraction failures safety-critical enough to require a separate hard gate rather than aggregate F1?
3. What lab-document / clinical-informatics expertise is required?
4. What minimum extraction performance could be clinically meaningful for the exact intended use?

## 14. Required review of `emergency_miss_rate` and `medication_critical_error_rate` as rare-event gates

The statistical reviewer should explicitly record whether a future method remains scientifically valid under:

```text
0 observed events
1 observed event
small independent-root N
moderate independent-root N
clustered sub-decisions within roots
```

A future PASS mechanism must not collapse uncertainty merely because the observed count is zero.

## 15. Required review of global hard-gate conjunction

The statistical reviewer should state whether this proposed global framing is correct:

```text
H0_GLOBAL = at least one required hard gate fails its own frozen bound
H1_GLOBAL = every required hard gate satisfies its own frozen bound
```

If that structure supports an intersection-union approach, the reviewer should explain the consequence for global type-I error **and separately** identify any multiplicity still requiring control for strata, candidate comparisons, secondary endpoints, or sensitivities.

No automatic multiplicity waiver is requested.

## 16. Required source appraisal

For every publication or external source relied upon, the future reviewer should record:

```text
source_identity
source_revision_or_publication_date
claim_supported
population_or_problem_setting
methodological_relevance
transferability_to_commandmed
material_limitations
whether_source_is_context_only_or_policy_supporting
```

A public publication locator alone is not identity-bound commandMed evidence.

## 17. Required clinical / statistical disagreement handling

Canonical Q4 says unresolved material clinical or statistical dissent blocks threshold freeze, but exact quorum/disagreement protocol is not frozen.

Therefore this request requires only:

```text
MATERIAL_DISSENT_MUST_BE_RECORDED=YES
MATERIAL_DISSENT_MAY_BE_SILENTLY_IGNORED=NO
MATERIAL_DISSENT_MAY_BE_RESOLVED_BY_FOUNDER_PREFERENCE_ALONE=NO
MATERIAL_DISSENT_MAY_BE_RESOLVED_BY_SIMPLE_MAJORITY_BY_THIS_TEMPLATE=NO
```

If disagreement exists, the response should identify the disagreement and stop short of claiming canonical concurrence until an exact governed resolution path exists.

## 18. What a completed qualified review still would not authorize

Even a real, properly bound clinical/statistical review would not by itself authorize:

```text
SELECTION_SUITE_CONSTRUCTION
MODEL_EXECUTION
BENCHMARK_EXECUTION
DEVICE_EXECUTION
CONTAMINATION_ASSESSMENT
MODEL_CONVERSION
PRIVATE_GOLD_ACCESS
PHI_ACCESS
GATED_ASSET_ACCESS
PROVIDER_GENERATION
TRAINING
SPEND
```

It would only supply required evidence toward a later A2 policy freeze and, after A2, the atomic D34 design/allocation work.

## 19. Future adoption sequence

The safe sequence remains:

```text
1. bind exact reviewer authority identities through separately valid governance
2. bind exact reviewed packet/source revisions
3. perform clinical-domain review
4. perform statistical-method review
5. record material dissent/limitations
6. resolve disagreement only through a then-canonical mechanism
7. construct proposed A2 threshold/margin policy with evidence references
8. obtain canonical governance adoption
9. only then freeze A2 numeric policy pre-result
10. only after A2 is frozen, construct atomic D34 numeric N/allocation design
11. continue remaining A5-A14 real evidence gates
12. perform J1 recheck
13. obtain separate A15 activation if all prerequisites PASS
```

No step is auto-activated by completion of this template.

## 20. Current state

```text
A2_PUBLIC_EVIDENCE=AVAILABLE_CONTEXT_ONLY_AND_WORKBENCH_BOUND
A2_METHOD_CANDIDATES=DOCUMENTED_ON_PARENT_BRANCH_PENDING_CANONICAL_REVIEW_MERGE
A2_QUALIFIED_REVIEW_REQUEST=PREPARED_TEMPLATE_ONLY
A2_QUALIFIED_REVIEW_PERFORMED=NO
A2_THRESHOLD_FREEZE=NO
D34_NUMERIC_DESIGN=NO
REAL_A2_TO_A14_SNAPSHOT=ABSENT
REAL_A15_ACTIVATION=ABSENT
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This branch should not be proposed for canonical merge until the parent statistical-method packet is itself canonically merged or otherwise reconciled to the exact final parent identity.