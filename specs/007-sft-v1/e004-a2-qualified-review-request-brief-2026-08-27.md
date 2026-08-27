# E004 A2 Qualified Clinical / Statistical Review Request Brief — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `90dcf60b4d91b5588dc1bcca3c45feaa076d6c6b`  
**Canonical method-packet merge:** PR #78 / `90dcf60b4d91b5588dc1bcca3c45feaa076d6c6b`  
**Qualified method-packet head:** `4c71f5063263d553fa432df9a5198d192cef942c`  
**Artifact class:** reviewer-request template / coordination metadata only  
**Authority effect:** NONE  
**Reviewer appointed:** NO  
**Review disposition created:** NO  
**Validator input:** NO

This brief turns the frozen Session 9 Q3/Q4 governance and the now-canonical A2 statistical-method candidate packet into a bounded request that future qualified clinical and statistical reviewers can answer. It does **not** appoint a reviewer, assert credentials, define a new disposition vocabulary, approve a method, freeze a threshold/margin, freeze a confidence/error rate, freeze numeric `N`, or create a `ThresholdPolicy` / `StatisticalDesign` record.

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
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
E004_STATE=BLOCKED_PREFLIGHT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling authority model

Session 9 Q4 requires three distinct functions before any clinical/statistical threshold or margin can become canonical:

```text
THRESHOLD_AUTHORITY_FUNCTION_1=CLINICAL_DOMAIN_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_2=STATISTICAL_METHOD_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_3=CANONICAL_GOVERNANCE_ADOPTION
```

No one function substitutes for another.

```text
FOUNDER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO
CLINICIAN_SOLE_STATISTICAL_METHOD_AUTHORITY=NO
STATISTICIAN_SOLE_CLINICAL_ACCEPTABILITY_AUTHORITY=NO
EVALUATION_OWNER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO
```

This brief therefore separates clinical and statistical questions and never treats repository governance as scientific evidence.

## 2. Unresolved reviewer-governance fields remain unresolved

Canonical governance has not frozen:

```text
EXACT_REVIEWER_IDENTITIES
EXACT_REVIEWER_COUNT
EXACT_CLINICAL_REVIEWER_CREDENTIAL_REQUIREMENTS
EXACT_STATISTICAL_REVIEWER_CREDENTIAL_REQUIREMENTS
EXACT_QUORUM_RULE
EXACT_THRESHOLD_REVIEW_DISPOSITION_VOCABULARY
EXACT_THRESHOLD_DISAGREEMENT_RESOLUTION_PROTOCOL
```

This template must not fill those gaps by convenience.

```text
DOCUMENT_AUTHOR_IS_REVIEWER=NO
GITHUB_PR_REVIEW_EQUALS_QUALIFIED_CLINICAL_REVIEW=NO
GITHUB_PR_REVIEW_EQUALS_QUALIFIED_STATISTICAL_REVIEW=NO
QODO_CODERABBIT_CUBIC_OR_OTHER_CODE_REVIEW_EQUALS_SCIENTIFIC_REVIEW=NO
LLM_GENERATED_RECOMMENDATION_EQUALS_QUALIFIED_REVIEW=NO
NO_COMMENT_EQUALS_APPROVAL=NO
MAJORITY_VOTE_AUTO_AUTHORITY=NO
```

A future canonical review artifact must use the exact identity/disposition mechanism governed at that future point. Until then, this brief requests reasoned findings only.

## 3. Immutable review-input set

A future qualified review should bind exact revisions of at least:

```text
STATISTICAL_ARCHITECTURE=
  specs/005-base-model-tournament/session-9-q3-statistical-rationale-sample-size-power-architecture.md

REVIEW_GOVERNANCE=
  specs/005-base-model-tournament/session-9-q4-clinical-review-threshold-margin-governance.md

THRESHOLD_FREEZE_READINESS_MATRIX=
  specs/005-base-model-tournament/session-9-q5-per-metric-threshold-freeze-readiness-matrix.md

A2_PUBLIC_EVIDENCE_DISCOVERY=
  specs/007-sft-v1/e004-a2-public-threshold-evidence-discovery-2026-08-27.md

A2_EVIDENCE_WORKBENCH=
  specs/007-sft-v1/e004-a2-evidence-package-workbench-2026-08-27.md

A2_STATISTICAL_METHOD_CANDIDATE_PACKET=
  specs/007-sft-v1/e004-a2-statistical-method-candidate-packet-2026-08-27.md
  QUALIFIED_HEAD=4c71f5063263d553fa432df9a5198d192cef942c
  CANONICAL_MERGE=90dcf60b4d91b5588dc1bcca3c45feaa076d6c6b

CURRENT_FRONTIER=
  specs/007-sft-v1/e004-current-frontier-reconciliation-2026-08-27.md
```

A material change to a reviewed scientific input before policy adoption requires re-binding/re-review; the old review cannot silently follow mutable `latest` content.

## 4. Candidate-result firewall

Threshold/method review must remain pre-result and candidate-neutral.

```text
TOURNAMENT_CANDIDATE_RESULTS_AVAILABLE_TO_SET_THRESHOLD=NO
PREFERRED_CANDIDATE_RESULT_AVAILABLE_TO_SET_MARGIN=NO
PRIVATE_GOLD_SELECTION_RESULTS_AVAILABLE_TO_SET_POLICY=NO
PUBLIC_EXTERNAL_TEST_RESULTS_USED_POST_HOC=NO
DESIRED_PASS_RATE_AS_POLICY_BASIS=NO
DESIRED_WINNER_AS_POLICY_BASIS=NO
COMPUTE_OR_BUDGET_CONVENIENCE_AS_SCIENTIFIC_THRESHOLD_BASIS=NO
```

Any review materially dependent on those inputs is not eligible to support the frozen pre-result A2 pathway.

## 5. Future auditable review metadata

This brief does not create these identities, but a future review should be able to bind:

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
review_disposition_under_then_canonical_vocabulary
```

A future threshold policy must ultimately bind both:

```text
clinical_review_authority_identity_and_disposition
statistical_review_authority_identity_and_disposition
```

plus material conflicts/limitations and canonical governance adoption.

## 6. Statistical reviewer — cross-metric questions

### S1 — exact estimand

For every hard-gate metric:

1. Is the candidate estimand family aligned with the metric semantics?
2. What exact estimand must be frozen before a method can be approved?
3. What is the exact unit of analysis?
4. What unresolved ambiguity still blocks method selection?

### S2 — independence / clustering / pairing

For every metric:

1. What is the independent statistical unit?
2. Which observations share a canonical root and cannot count as independent `N`?
3. Should dependent observations be collapsed into a predeclared root-level estimand or modeled/resampled as a cluster?
4. If resampling is used, what must move together in one resample?

Arabic parity must preserve:

```text
ANALYSIS_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
UNPAIRED_TWO_SAMPLE_LANGUAGE_SHORTCUT=PROHIBITED
```

### S3 — directional decision evidence

Confirm or reject the frozen architecture:

```text
LOWER_BETTER -> one-sided upper uncertainty bound vs frozen maximum
HIGHER_BETTER -> one-sided lower uncertainty bound vs frozen minimum
```

If another construction is necessary, provide the mathematical reason without weakening noncompensable hard-gate semantics.

### S4 — confidence / error-rate semantics

Do not choose `0.05`, `95%`, or another conventional value merely by habit.

State instead:

- what error probability the final decision must control;
- whether the decision is qualification, noninferiority, equivalence, calibration/risk-control, or another exact form;
- whether the error parameter is per-gate, simultaneous, family-wise, or conditional;
- what evidence is needed before a numeric level can be frozen.

### S5 — multiplicity

Assess separately:

- the global all-hard-gates-must-pass conjunction;
- simultaneous required strata;
- multiple candidate comparisons;
- repeated endpoints inside a metric family;
- secondary/sensitivity claims;
- any subgroup claims.

The candidate packet proposes an intersection-union architecture for **review**, not an automatic multiplicity waiver.

### S6 — nuisance inputs / sensitivity

For each planning input that materially affects `N` or operating characteristics, state:

```text
required_nuisance_parameter
acceptable_evidence_source_class
conservative_planning_alternative_if_needed
predeclared_sensitivity_range_or_analysis
whether_simulation_is_required
```

Candidate-result-derived nuisance estimates are prohibited as the primary planning basis.

### S7 — rare-event boundary safety

For safety-critical adverse-event rates, explicitly assess behavior at:

```text
0 observed events
1 observed event
small independent-root N
moderate independent-root N
clustered sub-decisions within roots
```

A valid future construction must preserve nonzero population uncertainty at zero observed failures. An unadjusted empirical cluster bootstrap that collapses to a zero upper bound is not acceptable.

### S8 — D34 readiness

For each metric, state whether the **method/derivation class** is sufficiently specified to proceed later to atomic A3+A4 **after** A2 numeric policy becomes canonical.

Do not provide final numeric `N` while the required threshold/margin/confidence/error-rate inputs remain unfrozen.

## 7. Clinical reviewer — cross-metric questions

For each metric:

1. Is the metric clinically interpretable for the exact intended role/population/use context?
2. What harm/failure mode does the hard gate need to bound?
3. What evidence is relevant to clinical acceptability versus method context only?
4. Are public sources transferable, partially transferable, or non-transferable to commandMed numeric policy?
5. What commandMed-specific evidence remains necessary?
6. What material clinical dissent or limitation must be recorded?
7. What specialty/domain expertise is necessary beyond a generic clinical credential?

Clinical review does not determine statistical adequacy by itself.

## 8. `emergency_miss_rate`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
ROOT_BERNOULLI_CANDIDATE=ONE_SIDED_BOUNDARY_SAFE_BINOMIAL_UPPER_BOUND
CLUSTERED_FALLBACK=BOUNDARY_SAFE_CLUSTER_AWARE_RARE_EVENT_METHOD_ONLY
```

### Statistical review

- What root-level event definition is needed for Bernoulli inference?
- Exact inversion, score-type bound, or another boundary-safe one-sided construction?
- If multiple emergency decisions share one root, is a clinically valid binary root summary preferable to cluster-aware inference?
- If cluster-aware inference is required, what method remains valid when **all observed roots have zero events**?
- What event-rate planning evidence and sensitivity analysis are required?

### Clinical review

- What precisely is a clinically critical emergency miss?
- Which acute/emergency expertise is required?
- What evidence could justify a future maximum acceptable population miss rate?
- Are severity classes distinct enough to require metric redesign before thresholding?

## 9. `medication_critical_error_rate`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=LOWER_BETTER_RATE_OR_RISK
ROOT_BERNOULLI_CANDIDATE=ONE_SIDED_BOUNDARY_SAFE_BINOMIAL_UPPER_BOUND
CLUSTERED_FALLBACK=BOUNDARY_SAFE_CLUSTER_AWARE_RARE_EVENT_METHOD_ONLY
```

### Statistical review

- Can each root yield one clinically valid critical-error indicator?
- If multiple medication decisions are nested in a root, what cluster-aware construction avoids pseudo-replication?
- What method remains boundary-safe at zero observed errors?
- What anticipated/conservative event-rate inputs are supportable for planning?

### Clinical review

- What error taxonomy qualifies as `critical`?
- What medication/pharmacology safety expertise is required?
- What authoritative medication-source identity/revision must ground scoring?
- What evidence could support a future maximum acceptable critical-error rate?

Statistical method choice cannot compensate for unresolved medication truth-source identity.

## 10. `selective_risk_at_target_coverage`

```text
DIRECTION=LOWER_BETTER
ESTIMAND_FAMILY=CALIBRATION_OR_SELECTIVE_RISK_SCORE
CANDIDATE_FAMILY=HELDOUT_FINITE_SAMPLE_RISK_CONTROL
METHOD_CANDIDATES=LEARN_THEN_TEST,CONFORMAL_RISK_CONTROL,OTHER_RISK_CONTROL_IF_SEMANTICS_MATCH
```

### Statistical review

- What exact loss/risk functional is controlled?
- What exactly is target coverage?
- Do loss/parameterization satisfy any monotonicity requirement of the proposed method?
- What exchangeability assumptions are needed?
- How is distribution shift handled?
- Must calibration and evaluation identities be disjoint?
- Which finite-sample guarantee aligns with the hard gate?
- What sample-size/calibration-size derivation follows from the chosen framework?

### Clinical review

- Which abstentions are clinically useful/safe and which are harmful non-answers?
- What clinical harms define risk?
- What coverage/risk tradeoff is clinically meaningful for the exact user role?

Public `80%`, `90%`, or `95%` coverage points must not be copied as commandMed policy without evidence.

## 11. `citation_entailment_fidelity`

```text
DIRECTION=HIGHER_BETTER
ESTIMAND_FAMILY=HIGHER_BETTER_PROPORTION_OR_FIDELITY
CLUSTER_CANDIDATE=ROOT_CASE_CLUSTER_RESAMPLING_LOWER_BOUND_WHEN_MULTIPLE_CLAIMS_SHARE_ROOT
BINOMIAL_CONDITIONAL=ONLY_IF_EXACT_ONE_INDEPENDENT_BERNOULLI_OUTCOME_PER_ROOT
```

### Statistical review

- What exact fidelity estimand is intended: root-weighted, claim-weighted, macro/micro, or another definition?
- Do multiple citations/claims inside one answer require root-cluster inference?
- Which bootstrap/resampling interval construction is acceptable at the planned independent-cluster count?
- What boundary/degeneracy checks are required?

### Clinical review

- What constitutes clinically sufficient entailment/support rather than citation presence?
- What deterministic-verifier + clinician-audit identity is required?
- What clinical evidence expertise is necessary?
- What evidence could justify a future minimum acceptable fidelity?

## 12. `arabic_clinical_parity_gap`

```text
DIRECTION=LOWER_BETTER
EVIDENCE_ROLE=SELECTION_DEV
ESTIMAND_FAMILY=PAIRED_LANGUAGE_GAP
ANALYSIS_UNIT=COMPLETE_MATCHED_ROOT_TASK_PAIR
PRIMARY_GENERAL_CANDIDATE=PAIRED_ROOT_TASK_RESAMPLING_ONE_SIDED_UPPER_BOUND
```

### Statistical review

- What exact paired gap functional should be frozen?
- Is paired root resampling appropriate, or is a paired analytic/studentized method justified?
- Should the future decision use one-sided noninferiority-to-maximum-gap semantics, equivalence, or another exact construction?
- What paired variance/planning inputs are needed?
- How should five Arabic coverage anchors, role strata, and overlapping strata enter D34 allocation/multiplicity?

### Clinical review

- Does the exact paired suite preserve clinical semantic equivalence?
- What Arabic-English clinical semantic expertise is required?
- How should Modern Standard Arabic, Saudi/Gulf colloquial, code-switching, local medication nomenclature, and emergency triage anchors affect acceptability?
- What evidence could justify a maximum acceptable parity gap?

Private Gold remains a separate final-audit role and cannot become selection evidence.

## 13. `lab_report_field_extraction_accuracy`

```text
DIRECTION=HIGHER_BETTER
UNIT_OR_SCALE=f1_score
ESTIMAND_FAMILY=NONLINEAR_SUMMARY_SUCH_AS_F1
CANDIDATE_A=F1_SPECIFIC_EXACT_OR_VALIDATED_ANALYTIC_METHOD_IF_ASSUMPTIONS_FIT
CANDIDATE_B=ROOT_CASE_CLUSTER_RESAMPLING_OF_EXACT_F1_FUNCTIONAL_IF_FIELDS_CLUSTER_WITHIN_REPORT
```

### Statistical review

- What exact F1 variant is canonical?
- What is the independent unit: report/root, field, or another identity?
- Do published F1 interval/power methods match the exact confusion/prevalence/dependency structure?
- If not, is root-case cluster resampling valid at the planned cluster count?
- What prevalence/sensitivity/precision nuisance inputs are required for planning?
- How should rare fields/field families be handled without pseudo-replication?

### Clinical review

- Which lab fields are clinically material versus administrative?
- Are some field failures safety-critical enough to require a separate hard gate rather than aggregate F1?
- What lab-document / clinical-informatics expertise is required?
- What evidence could justify a future minimum acceptable extraction performance?

## 14. Global hard-gate conjunction review

The statistical reviewer is asked to evaluate—not automatically accept—the candidate formulation:

```text
H0_GLOBAL=AT_LEAST_ONE_REQUIRED_HARD_GATE_FAILS_ITS_OWN_FROZEN_BOUND
H1_GLOBAL=EVERY_REQUIRED_HARD_GATE_SATISFIES_ITS_OWN_FROZEN_BOUND
```

If intersection-union is appropriate, document its exact consequence for global error control **and separately** identify multiplicity still created by strata, candidate comparisons, secondary endpoints, or sensitivities.

```text
AUTOMATIC_MULTIPLICITY_WAIVER=NO
AUTOMATIC_BONFERRONI=NO
```

## 15. Source appraisal requested from future reviewers

For every source materially relied upon, record:

```text
source_identity
source_revision_or_publication_date
claim_supported
population_or_problem_setting
methodological_or_clinical_relevance
transferability_to_commandmed
material_limitations
context_only_or_policy_supporting
```

A publication locator alone is not identity-bound commandMed evidence.

## 16. Dissent / conflict handling

Canonical Q4 says unresolved material clinical/statistical dissent blocks threshold freeze, but exact quorum/disagreement mechanics remain unfrozen.

```text
MATERIAL_DISSENT_MUST_BE_RECORDED=YES
MATERIAL_DISSENT_MAY_BE_SILENTLY_IGNORED=NO
FOUNDER_PREFERENCE_ALONE_MAY_RESOLVE_CLINICAL_OR_STATISTICAL_DISSENT=NO
THIS_TEMPLATE_CREATES_SIMPLE_MAJORITY_RULE=NO
```

If material disagreement exists, the review should expose it and stop short of a canonical concurrence claim until a valid governed resolution path exists.

## 17. What a real review would still not authorize

Even a properly identity-bound qualified clinical/statistical review would not by itself authorize:

```text
ARABIC_SELECTION_SUITE_CONSTRUCTION
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

It would supply evidence toward a later A2 numeric policy freeze. D34 remains downstream of T1.

## 18. Future adoption sequence

```text
1. establish exact reviewer authority identities through separately valid governance
2. bind exact reviewed source/artifact revisions
3. perform clinical-domain review
4. perform statistical-method review
5. record material limitations/dissent/conflicts
6. resolve disagreement only through a then-canonical mechanism
7. construct proposed A2 threshold/margin policy using the reviewed evidence
8. obtain canonical governance adoption
9. freeze A2 numeric policy pre-result only if all requirements are satisfied
10. construct atomic D34 numeric N/allocation design only after T1/A2 is canonical
11. continue remaining A5-A14 real-evidence gates
12. perform J1 recheck
13. obtain separate A15 activation only after all prerequisites PASS
```

No step auto-activates from this request template.

## 19. Current state after preparing this request surface

```text
A2_PUBLIC_EVIDENCE_DISCOVERY=CANONICAL_CONTEXT_AVAILABLE
A2_EVIDENCE_WORKBENCH=CANONICAL_NONVALIDATOR_WORKBENCH_AVAILABLE
A2_STATISTICAL_METHOD_CANDIDATE_PACKET=CANONICAL_CANDIDATE_ONLY
A2_QUALIFIED_REVIEW_REQUEST_SURFACE=DOCUMENTED_TEMPLATE_ONLY
A2_QUALIFIED_REVIEW_PERFORMED=NO
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
REAL_THRESHOLD_POLICY_PASS_COUNT=0
REAL_STATISTICAL_DESIGN_PASS_COUNT=0
REAL_A15_ACTIVATION=ABSENT
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```