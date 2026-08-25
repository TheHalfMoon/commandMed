# Spec 005 — Session 9 Q4 Clinical-Review Authority and Threshold/Margin Evidence Governance

**Lifecycle:** CLARIFY ONLY  
**Evidence capture date:** 2026-08-23  
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Predecessor PR head:** `6f3b8462eac446dd3399fb8d18b5a0f0d3931c97`

> This artifact freezes authority and evidence-governance architecture only. It does not choose a numeric clinical threshold, margin, confidence level, sample size, power target, aggregation weight, reviewer identity, or founder decision. It does not create/access benchmark payloads, run models, access model weights, access Private Gold, access PHI/restricted data, authorize corrective maintenance, or advance to PLAN.

## 1. Q4 decision

```text
SESSION9_Q4_POLICY=MULTI_ROLE_CLINICAL_STATISTICAL_EVIDENCE_GOVERNANCE_BEFORE_THRESHOLD_FREEZE

CLINICAL_REVIEW_AUTHORITY_ARCHITECTURE=FROZEN
THRESHOLD_MARGIN_EVIDENCE_GOVERNANCE_ARCHITECTURE=FROZEN

SINGLE_PERSON_CLINICAL_THRESHOLD_AUTHORITY=PROHIBITED
FOUNDER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO
CLINICIAN_SOLE_STATISTICAL_METHOD_AUTHORITY=NO
STATISTICIAN_SOLE_CLINICAL_ACCEPTABILITY_AUTHORITY=NO
EVALUATION_OWNER_SOLE_CLINICAL_THRESHOLD_AUTHORITY=NO

EXACT_REVIEWER_IDENTITIES=NOT_YET_FROZEN
EXACT_REVIEWER_COUNT=NOT_YET_FROZEN
EXACT_NUMERIC_CLINICAL_STATISTICAL_THRESHOLDS=NOT_YET_FROZEN
EXACT_NUMERIC_MARGINS=NOT_YET_FROZEN
```

A clinical/statistical threshold is a scientific policy identity, not a convenience parameter. It may become canonical only after the required clinical interpretation, statistical justification, evidence provenance, and repository-governance adoption are all resolved.

## 2. Canonical basis

Spec 002 is `CLOSED_CANONICAL` and already establishes:

1. population/statistical thresholds must not be invented without clinical/statistical evidence;
2. `PENDING_CLINICAL_EVIDENCE` requires intended use/population, evaluation design, identity-bound evidence, clinical review authority, statistical rationale, and sample-size/power rationale;
3. `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE` adds a founder/product-policy decision only when the contract explicitly requires it;
4. any future frozen threshold must bind value/operator/unit, intended role/population/use case, language/modality, evidence source identities, clinical/statistical rationale, reviewer/owner authority, freeze date, canonical policy identity, and supersession metadata;
5. changing a frozen threshold creates a new scientific policy identity and prior results cannot silently inherit it.

Q4 does not alter these canonical threshold classes or the hard-gate evaluator.

```text
Q4_REDEFINES_SPEC002_THRESHOLD_CLASS=NO
Q4_REPLACES_HARD_GATE_EVALUATOR=NO
Q4_GRANTS_STATISTICAL_PASS=NO
```

## 3. Threshold-freeze authority model

For any clinical/statistical threshold or margin used by the Spec 005 quality floor, three authority functions are required.

### 3.1 Clinical-domain review

```text
THRESHOLD_AUTHORITY_FUNCTION_1=CLINICAL_DOMAIN_REVIEW
CLINICAL_DOMAIN_REVIEW_REQUIRED=YES
```

Clinical-domain review is responsible for whether the proposed threshold/margin is clinically interpretable and compatible with the exact intended role, population, use context, harm model, language/modality, and capability scope.

The exact profession or specialty depends on the metric and claim.

```text
CLINICAL_REVIEW_EXPERTISE_MUST_MATCH_METRIC_HARM_DOMAIN=YES
GENERIC_CLINICAL_TITLE_ALONE_PROVES_METRIC_SPECIFIC_EXPERTISE=NO
EXACT_CLINICAL_CREDENTIAL_REQUIREMENTS=NOT_YET_FROZEN
```

### 3.2 Statistical/methodological review

```text
THRESHOLD_AUTHORITY_FUNCTION_2=STATISTICAL_METHOD_REVIEW
STATISTICAL_METHOD_REVIEW_REQUIRED=YES
```

Statistical/methodological review is responsible for the estimand, decision rule, uncertainty method, sample-size/power rationale, pairing/clustering structure, multiplicity structure where relevant, nuisance assumptions, and whether the proposed numeric value is supportable by the evidence rather than chosen post hoc.

```text
STATISTICAL_REVIEW_MUST_BE_METRIC_METHOD_COMPATIBLE=YES
GENERIC_SIGNIFICANCE_TEST_ALONE_SUFFICIENT=NO
EXACT_STATISTICAL_REVIEWER_CREDENTIAL_REQUIREMENTS=NOT_YET_FROZEN
```

### 3.3 Canonical governance adoption

```text
THRESHOLD_AUTHORITY_FUNCTION_3=CANONICAL_GOVERNANCE_ADOPTION
CANONICAL_GOVERNANCE_ADOPTION_REQUIRED=YES
```

The repository/evaluation governance owner is responsible for ensuring the approved scientific policy is identity-bound, provenance-complete, versioned, reviewable, and adopted on canonical GitHub history.

Governance adoption does not itself supply clinical or statistical evidence.

```text
CANONICAL_GOVERNANCE_OWNER_MAY_REPLACE_CLINICAL_REVIEW=NO
CANONICAL_GOVERNANCE_OWNER_MAY_REPLACE_STATISTICAL_REVIEW=NO
```

## 4. Required concurrence before a numeric freeze

A numeric threshold/margin cannot be frozen for Spec 005 selection use unless all required authority functions have compatible recorded dispositions.

```text
CLINICAL_REVIEW_DISPOSITION_REQUIRED=YES
STATISTICAL_REVIEW_DISPOSITION_REQUIRED=YES
CANONICAL_GOVERNANCE_ADOPTION_RECORD_REQUIRED=YES

UNRESOLVED_MATERIAL_CLINICAL_DISSENT=BLOCKED
UNRESOLVED_MATERIAL_STATISTICAL_DISSENT=BLOCKED
MISSING_REQUIRED_REVIEW_DISPOSITION=INCOMPLETE
```

Q4 does not define majority voting, quorum, or an exact reviewer count.

```text
MAJORITY_VOTE_AS_AUTOMATIC_THRESHOLD_AUTHORITY=NO
EXACT_QUORUM_RULE=NOT_YET_FROZEN
EXACT_DISAGREEMENT_RESOLUTION_PROTOCOL=NOT_YET_FROZEN
```

## 5. Independence and conflict controls

Threshold review must be insulated from candidate-result pressure.

```text
THRESHOLD_MUST_BE_FROZEN_BEFORE_RELEVANT_CANDIDATE_RESULTS=YES
THRESHOLD_REVIEWERS_MAY_USE_TOURNAMENT_CANDIDATE_RESULTS_TO_SET_THRESHOLD=NO
THRESHOLD_REVIEWERS_MAY_USE_PREFERRED_CANDIDATE_PERFORMANCE_TO_SET_MARGIN=NO

THRESHOLD_PROPOSAL_AUTHOR_MAY_BE_SOLE_FINAL_APPROVER=NO
REVIEWER_CONFLICT_OR_ROLE_DISCLOSURE_REQUIRED=YES
```

Candidate identity blinding is preferred where technically relevant, but pre-result threshold governance is the primary control.

```text
CANDIDATE_IDENTITY_BLINDING_REQUIRED_WHERE_TECHNICALLY_FEASIBLE=YES
PRE_RESULT_THRESHOLD_FREEZE_REMAINS_REQUIRED_EVEN_IF_BLINDED=YES
```

## 6. Founder authority boundary

The founder/project owner may define product goals and may resolve an explicitly canonical founder-policy tradeoff when the threshold class requires it.

```text
FOUNDER_PRODUCT_GOAL_AUTHORITY=PRESERVED
FOUNDER_POLICY_DECISION_REQUIRED_ONLY_WHEN_CANONICAL_THRESHOLD_CLASS_REQUIRES_IT=YES
```

For the current Spec 002 contract, `benign_case_over_triage_rate` remains the explicit example:

```text
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_CLASS=PENDING_FOUNDER_AND_CLINICAL_EVIDENCE
BENIGN_CASE_OVER_TRIAGE_FOUNDER_DECISION_ID=FD-004
```

Founder preference alone is not scientific evidence and cannot waive the other prerequisites.

```text
FOUNDER_PREFERENCE_ALONE_IS_CLINICAL_EVIDENCE=NO
FOUNDER_PREFERENCE_ALONE_IS_STATISTICAL_RATIONALE=NO
FOUNDER_DECISION_CAN_OVERRIDE_REQUIRED_CLINICAL_REVIEW=NO
FOUNDER_DECISION_CAN_OVERRIDE_REQUIRED_STATISTICAL_REVIEW=NO
```

For metrics whose canonical state is `PENDING_CLINICAL_EVIDENCE` with no founder-decision field, no new founder veto/approval requirement is invented by Q4.

## 7. Evidence classes permitted for future threshold justification

A future threshold proposal may use evidence classes that are fit for the exact intended use and metric, provided exact source identity, version/date, relevance, and limitations are recorded.

```text
ALLOWED_THRESHOLD_EVIDENCE_CLASS_1=AUTHORITATIVE_CLINICAL_STANDARD_OR_GUIDELINE
ALLOWED_THRESHOLD_EVIDENCE_CLASS_2=PEER_REVIEWED_CLINICAL_OR_VALIDATION_EVIDENCE
ALLOWED_THRESHOLD_EVIDENCE_CLASS_3=SYSTEMATIC_REVIEW_OR_META_ANALYTIC_EVIDENCE
ALLOWED_THRESHOLD_EVIDENCE_CLASS_4=HIGH_QUALITY_PUBLISHED_METHOD_OR_PERFORMANCE_EVIDENCE
ALLOWED_THRESHOLD_EVIDENCE_CLASS_5=SEPARATELY_AUTHORIZED_IDENTITY_BOUND_NON_GOLD_PRETOURNAMENT_PILOT
ALLOWED_THRESHOLD_EVIDENCE_CLASS_6=DOCUMENTED_EXPERT_CONSENSUS_WITH_LIMITATIONS_WHEN_STRONGER_EVIDENCE_IS_UNAVAILABLE
```

No evidence class is automatically sufficient merely because it belongs to the list.

```text
EVIDENCE_FIT_TO_INTENDED_USE_MUST_BE_JUSTIFIED=YES
EVIDENCE_POPULATION_AND_CONTEXT_TRANSFER_MUST_BE_JUSTIFIED=YES
EVIDENCE_VERSION_OR_REVISION_IDENTITY_REQUIRED=YES
EVIDENCE_LIMITATIONS_MUST_BE_RECORDED=YES
```

Expert consensus must not be silently represented as equivalent to a strong empirical or authoritative evidence base.

```text
EXPERT_CONSENSUS_MAY_BE_MISREPRESENTED_AS_EMPIRICAL_VALIDATION=NO
EXPERT_CONSENSUS_MAY_HIDE_EVIDENCE_GAPS=NO
```

Q4 authorizes no pilot access or execution.

## 8. Evidence explicitly prohibited as the sole or primary scientific basis

```text
PROHIBITED_THRESHOLD_BASIS_1=TOURNAMENT_CANDIDATE_RESULTS
PROHIBITED_THRESHOLD_BASIS_2=PREFERRED_CANDIDATE_RESULT
PROHIBITED_THRESHOLD_BASIS_3=DESIRED_PASS_RATE
PROHIBITED_THRESHOLD_BASIS_4=DESIRED_WINNER_IDENTITY
PROHIBITED_THRESHOLD_BASIS_5=ROUND_NUMBER_OR_CONVENIENCE
PROHIBITED_THRESHOLD_BASIS_6=COMPUTE_OR_BUDGET_CONVENIENCE
PROHIBITED_THRESHOLD_BASIS_7=MODEL_LEADERBOARD_OR_VENDOR_MARKETING_ALONE
PROHIBITED_THRESHOLD_BASIS_8=PRIVATE_GOLD_SELECTION_RESULTS
PROHIBITED_THRESHOLD_BASIS_9=PUBLIC_EXTERNAL_EVAL_TEST_RESULTS_USED_POST_HOC
PROHIBITED_THRESHOLD_BASIS_10=LLM_GENERATED_RECOMMENDATION_WITHOUT_QUALIFIED_EVIDENCE_REVIEW
PROHIBITED_THRESHOLD_BASIS_11=SENTINEL_ZERO_VIOLATIONS_AS_POPULATION_ZERO_RISK
PROHIBITED_THRESHOLD_BASIS_12=STATISTICAL_SIGNIFICANCE_ALONE_WITHOUT_CLINICAL_INTERPRETATION
```

A metric threshold must be clinically/statistically meaningful for its exact use, not selected to create a convenient tournament outcome.

## 9. Clinical meaningfulness and statistical evidence are distinct

```text
STATISTICAL_SIGNIFICANCE_EQUALS_CLINICAL_ACCEPTABILITY=NO
CLINICAL_ACCEPTABILITY_EQUALS_STATISTICAL_ADEQUACY=NO
BOTH_CLINICAL_AND_STATISTICAL_JUSTIFICATION_REQUIRED_WHERE_APPLICABLE=YES
```

A margin/threshold may be numerically estimable yet clinically unacceptable, or clinically desirable yet unsupported by the available sample size/uncertainty. Both dimensions must be resolved before freeze.

## 10. Metric-specific clinical authority matching

Q4 freezes expertise matching by domain without appointing people.

### Emergency / acute safety

```text
EMERGENCY_MISS_THRESHOLD_REQUIRES_RELEVANT_ACUTE_OR_EMERGENCY_CLINICAL_REVIEW=YES
```

### Medication safety

```text
MEDICATION_CRITICAL_ERROR_THRESHOLD_REQUIRES_RELEVANT_MEDICATION_OR_PHARMACOLOGY_SAFETY_REVIEW=YES
```

### Selective risk / abstention

```text
SELECTIVE_RISK_THRESHOLD_REQUIRES_CLINICAL_SAFETY_AND_STATISTICAL_METHOD_REVIEW=YES
```

### Citation/evidence fidelity

```text
CITATION_ENTAILMENT_THRESHOLD_REQUIRES_CLINICAL_EVIDENCE_INTERPRETATION_AND_METHOD_REVIEW=YES
```

### Arabic clinical parity

```text
ARABIC_PARITY_THRESHOLD_REQUIRES_ARABIC_ENGLISH_CLINICAL_SEMANTIC_REVIEW_CAPABILITY=YES
ARABIC_PARITY_THRESHOLD_REQUIRES_PAIRED_STATISTICAL_METHOD_REVIEW=YES
```

### Lab/document extraction

```text
LAB_EXTRACTION_THRESHOLD_REQUIRES_RELEVANT_LAB_DOCUMENT_OR_CLINICAL_INFORMATICS_REVIEW=YES
```

Exact credentials, organizations, jurisdictions, and reviewer identities remain unresolved.

## 11. Threshold record provenance requirements

A future frozen threshold/margin used by Spec 005 must bind, directly or by immutable referenced artifacts, at least:

```text
threshold_id
metric_id
decision_role
comparison_operator
numeric_value_or_range
unit
intended_use
role_population_scope
language_modality_scope
estimand_identity
unit_of_analysis
required_strata_scope
evidence_source_ids_and_revisions
evidence_appraisal_summary
clinical_rationale
statistical_rationale
sample_size_or_power_rationale
uncertainty_method_identity
clinical_review_authority_identity_and_disposition
statistical_review_authority_identity_and_disposition
governance_adoption_identity
founder_decision_identity_or_explicit_not_required
material_conflicts_or_limitations
freeze_date
canonical_policy_revision_or_hash
supersedes_threshold_id_or_explicit_none
```

Q4 creates the governance requirement only; it does not create any threshold record.

## 12. Source freshness and supersession

Clinical guidance and evidence may change. Therefore a threshold proposal must identify the exact version/date/revision of its sources.

```text
MUTABLE_LATEST_GUIDANCE_AS_UNBOUND_THRESHOLD_BASIS=PROHIBITED
EXACT_SOURCE_VERSION_OR_DATE_REQUIRED=YES
```

If materially relevant source evidence changes before execution, the threshold must be re-reviewed rather than silently inheriting the earlier evidence appraisal.

```text
MATERIAL_SOURCE_CHANGE_BEFORE_EXECUTION_REQUIRES_THRESHOLD_REVIEW=YES
```

## 13. Threshold amendment and result-reuse governance

Changing a frozen threshold or margin creates a new scientific policy identity.

```text
THRESHOLD_AMENDMENT_CREATES_NEW_POLICY_IDENTITY=YES
SILENT_IN_PLACE_THRESHOLD_REINTERPRETATION=PROHIBITED
HISTORICAL_THRESHOLD_IDENTITY_MUST_REMAIN_REPRODUCIBLE=YES
```

A threshold may not be changed after candidate results merely to rescue, eliminate, or reorder candidates.

```text
POST_RESULT_THRESHOLD_CHANGE_TO_RESCUE_CANDIDATE=PROHIBITED
POST_RESULT_MARGIN_CHANGE_TO_REORDER_CANDIDATES=PROHIBITED
```

If a legitimate scientific correction creates a new threshold after candidate results have already been observed, those old results do not automatically become selection evidence under the new threshold.

```text
OLD_RESULTS_AUTOMATICALLY_INHERIT_NEW_THRESHOLD=NO
NEW_THRESHOLD_REQUIRES_SEPARATELY_GOVERNED_FRESH_SELECTION_EVIDENCE=YES
```

Q4 does not authorize such execution.

## 14. External methodological consistency

Q4 is consistent with, but does not claim compliance with, current primary guidance:

- WHO, *Ethics and governance of artificial intelligence for health* (2021): human autonomy, safety, transparency, accountability, and defined use contexts are central governance principles. `https://www.who.int/publications/i/item/9789240029200`
- WHO, *Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models* (2025): general-purpose health AI requires governance proportionate to risk and intended use. `https://www.who.int/publications/i/item/9789240084759`
- FDA, *Clinical Decision Support Software* Final Guidance (January 2026): intended user/patient context and the ability to independently review recommendation bases are relevant to CDS risk and oversight. `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software`

These sources do not provide one universal acceptable numeric threshold for commandMed. They support risk-based, intended-use-specific, reviewable governance.

## 15. Q4 does not establish regulatory status

```text
Q4_DETERMINES_MEDICAL_DEVICE_STATUS=NO
Q4_CLAIMS_FDA_OR_WHO_COMPLIANCE=NO
Q4_CREATES_REGULATORY_RELEASE_AUTHORITY=NO
```

Any future legal/regulatory review remains separate and depends on concrete intended use, claims, users, deployment, and jurisdiction.

## 16. Current prerequisite state

Q4 resolves the authority/governance architecture, but not the exact authority identities or numeric threshold values.

```text
CLINICAL_REVIEW_AUTHORITY_ARCHITECTURE=FROZEN
CLINICAL_REVIEW_AUTHORITY_EXACT_IDENTITIES=UNRESOLVED
STATISTICAL_REVIEW_AUTHORITY_EXACT_IDENTITIES=UNRESOLVED

THRESHOLD_MARGIN_EVIDENCE_GOVERNANCE_ARCHITECTURE=FROZEN
THRESHOLD_MARGIN_EXACT_EVIDENCE_PACKAGES=UNRESOLVED

NUMERIC_CLINICAL_STATISTICAL_THRESHOLDS=NOT_YET_FROZEN
EXACT_NUMERIC_MARGINS=NOT_YET_FROZEN
THRESHOLD_FREEZE_ALLOWED_BY_Q4_ALONE=NO
```

The canonical quality floor therefore remains non-passable.

```text
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
MINIMUM_MEDICAL_QUALITY_THRESHOLD=NOT_YET_FROZEN
CANONICAL_QUALITY_FLOOR_PASS_CURRENTLY_POSSIBLE=NO
```

## 17. Authority boundary

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

## 18. Session state

```text
CLARIFICATION_SESSION_9=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_9_STATUS=IN_PROGRESS
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```
