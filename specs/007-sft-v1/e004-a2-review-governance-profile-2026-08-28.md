# E004 A2 Qualified Review Governance Profile — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** procedural scientific-review governance only  
**Canonical base at branch creation:** `271712bbea9ef631510c8892ca9ce33ab21d054d`  
**Authority effect:** review-process governance only  
**Scientific review performed:** NO  
**Reviewer appointed or engaged:** NO  
**Threshold/margin frozen:** NO  
**Statistical design frozen:** NO  
**Model/benchmark/device execution:** NO  
**Spend:** USD 0

## Purpose

Resolve only the procedural reviewer-governance fields that canonical Session 9 Q4 and the A2 qualified-review request brief intentionally left unresolved:

```text
EXACT_REVIEWER_COUNT
EXACT_CLINICAL_REVIEWER_CREDENTIAL_REQUIREMENTS
EXACT_STATISTICAL_REVIEWER_CREDENTIAL_REQUIREMENTS
EXACT_QUORUM_RULE
EXACT_THRESHOLD_REVIEW_DISPOSITION_VOCABULARY
EXACT_THRESHOLD_DISAGREEMENT_RESOLUTION_PROTOCOL
```

This record does not supply clinical evidence, statistical rationale, a reviewer identity, a review disposition, a numeric policy, or canonical adoption of any threshold. It creates a deterministic process that future qualified human review evidence must satisfy.

The Founder direction on 2026-08-28 to continue with all ordinary project approval is interpreted narrowly here as approval to freeze this repository-governance mechanism only. It is not interpreted as clinical review, statistical review, reviewer engagement, model execution, conversion, training, credentials, procurement, or spend authority.

## Controlling sources

```text
CONSTITUTION=.specify/memory/constitution.md
SESSION9_Q3=specs/005-base-model-tournament/session-9-q3-statistical-rationale-sample-size-power-architecture.md
SESSION9_Q4=specs/005-base-model-tournament/session-9-q4-clinical-review-threshold-margin-governance.md
SESSION9_Q5=specs/005-base-model-tournament/session-9-q5-per-metric-threshold-freeze-readiness-matrix.md
A2_EVIDENCE_DISCOVERY=specs/007-sft-v1/e004-a2-public-threshold-evidence-discovery-2026-08-27.md
A2_EVIDENCE_WORKBENCH=specs/007-sft-v1/e004-a2-evidence-package-workbench-2026-08-27.md
A2_METHOD_PACKET=specs/007-sft-v1/e004-a2-statistical-method-candidate-packet-2026-08-27.md
A2_REVIEW_BRIEF=specs/007-sft-v1/e004-a2-qualified-review-request-brief-2026-08-27.md
```

The closed Spec 005 artifacts remain controlling. This profile may narrow procedure but may not weaken any scientific, independence, provenance, quarantine, or pre-result requirement in those sources.

## 1. Required authority functions and minimum people

Every A2 metric policy proposed for canonical freeze requires three separately recorded functions:

```text
FUNCTION_1=CLINICAL_DOMAIN_REVIEW
FUNCTION_2=STATISTICAL_METHOD_REVIEW
FUNCTION_3=CANONICAL_GOVERNANCE_ADOPTION
```

Minimum personnel separation for one metric policy:

```text
MINIMUM_DISTINCT_CLINICAL_REVIEWERS=1
MINIMUM_DISTINCT_STATISTICAL_REVIEWERS=1
MINIMUM_DISTINCT_GOVERNANCE_ADOPTERS=1
MINIMUM_DISTINCT_PEOPLE_PER_METRIC_POLICY=3

CLINICAL_REVIEWER_MAY_EQUAL_STATISTICAL_REVIEWER=NO
CLINICAL_REVIEWER_MAY_EQUAL_GOVERNANCE_ADOPTER=NO
STATISTICAL_REVIEWER_MAY_EQUAL_GOVERNANCE_ADOPTER=NO
```

This is a minimum, not a cap. A metric may require additional reviewers when one person cannot credibly cover the required harm domain, language, modality, or method family.

One qualified person may review more than one metric only when the review record independently proves scope-relevant competence for every metric reviewed. Role title alone is insufficient.

```text
GENERIC_CLINICAL_TITLE_PROVES_ALL_METRIC_EXPERTISE=NO
GENERIC_STATISTICAL_TITLE_PROVES_ALL_METHOD_EXPERTISE=NO
CROSS_METRIC_REVIEW_REQUIRES_SCOPE_COMPETENCE_EVIDENCE=YES
```

## 2. Clinical reviewer qualification

A clinical-domain reviewer must have identity-bound evidence of a recognized clinical professional qualification or equivalent clinical-domain authority appropriate to the reviewed harm/metric, plus documented relevant expertise.

The public repository need not publish personal credential documents. It must bind an auditable credential-evidence reference.

Minimum review record requirements:

```text
CLINICAL_QUALIFICATION_EVIDENCE_REFERENCE=REQUIRED
METRIC_HARM_DOMAIN_COMPETENCE=REQUIRED
ROLE_OR_CONFLICT_DISCLOSURE=REQUIRED
CANDIDATE_RESULT_EXPOSURE_STATE=REQUIRED
```

Metric-specific minimum competence follows canonical Q4 and the A2 review brief:

```text
emergency_miss_rate -> acute/emergency clinical expertise
medication_critical_error_rate -> medication/pharmacology safety expertise
selective_risk_at_target_coverage -> clinical safety expertise
citation_entailment_fidelity -> clinical evidence interpretation expertise
arabic_clinical_parity_gap -> Arabic-speaking clinical professional with bilingual clinical comparison competence
lab_report_field_extraction_accuracy -> laboratory medicine/pathology or clinically relevant laboratory/clinical-informatics expertise
```

A reviewer may satisfy a listed domain by equivalent documented professional scope; labels alone do not prove competence.

## 3. Statistical reviewer qualification

A statistical-method reviewer must have identity-bound evidence of professional or academic competence in biostatistics, statistics, epidemiologic/clinical quantitative methods, or an equivalent methodologically rigorous field, and must be competent in the exact method family under review.

Minimum review record requirements:

```text
STATISTICAL_QUALIFICATION_EVIDENCE_REFERENCE=REQUIRED
METHOD_FAMILY_COMPETENCE=REQUIRED
CLINICAL_OR_MEDICAL_EVALUATION_CONTEXT_COMPETENCE=REQUIRED_OR_EXPLICITLY_PAIRED_WITH_CLINICAL_REVIEW
ROLE_OR_CONFLICT_DISCLOSURE=REQUIRED
CANDIDATE_RESULT_EXPOSURE_STATE=REQUIRED
```

A generic significance-test background does not establish competence for clustered rare-event inference, paired noninferiority/equivalence, selective-risk control, nonlinear F1 inference, or other specialized method families.

## 4. Closed review disposition vocabulary

Reuse the already-frozen fail-closed review vocabulary instead of inventing a parallel state machine:

```text
ACCEPT
REVISE
REJECT
BLOCKED
```

Semantics for A2 scientific review:

```text
ACCEPT=no material issue in the reviewer's assigned authority function; limitations are recorded separately
REVISE=repairable material issue; policy is not eligible for adoption until revised and freshly reviewed
REJECT=proposal is not acceptable under the current evidence/design
BLOCKED=required evidence, competence, scope, identity, or prerequisite is absent/unresolved
```

`ACCEPT` with documented non-material limitations is represented as `ACCEPT` plus `material_limitations`; no `ACCEPT_WITH_EXCEPTIONS` shortcut is created.

## 5. Quorum and adoption rule

A metric threshold/margin policy is eligible for canonical governance adoption only when the exact same proposed policy identity has:

```text
REQUIRED_CLINICAL_DISPOSITION=ACCEPT
REQUIRED_STATISTICAL_DISPOSITION=ACCEPT
UNRESOLVED_MATERIAL_CLINICAL_DISSENT=NO
UNRESOLVED_MATERIAL_STATISTICAL_DISSENT=NO
CANDIDATE_RESULT_EXPOSURE_POLICY=PRE_RESULT_ONLY
GOVERNANCE_ADOPTION_RECORD=REQUIRED
```

The canonical governance adopter acts only after the scientific dispositions exist and may verify identity, provenance, process compliance, and versioning. The adopter cannot manufacture or override scientific evidence.

```text
FOUNDER_OR_GOVERNANCE_OWNER_MAY_OVERRIDE_CLINICAL_REVISE_REJECT_BLOCKED=NO
FOUNDER_OR_GOVERNANCE_OWNER_MAY_OVERRIDE_STATISTICAL_REVISE_REJECT_BLOCKED=NO
MAJORITY_VOTE_CAN_OVERRIDE_MATERIAL_DISSENT=NO
NO_RESPONSE_EQUALS_ACCEPT=NO
CODE_REVIEW_BOT_OR_LLM_EQUALS_SCIENTIFIC_ACCEPT=NO
```

If more than the minimum reviewer count is used in one authority function, every reviewer designated as required for that review round must return `ACCEPT`; convenience majority voting is prohibited.

## 6. Disagreement and re-review

Clinical and statistical functions answer different questions. A disagreement is not resolved by choosing one function over the other.

```text
ANY_REQUIRED_REVISE=NOT_ELIGIBLE_FOR_ADOPTION
ANY_REQUIRED_REJECT=NOT_ELIGIBLE_FOR_ADOPTION
ANY_REQUIRED_BLOCKED=NOT_ELIGIBLE_FOR_ADOPTION
```

One bounded clarification exchange may be used to resolve misunderstandings without changing the proposed scientific identity. If the policy, threshold/margin, evidence set, estimand, method family, confidence/error-rate semantics, or material rationale changes, the proposal receives a new identity and fresh required review.

If material disagreement remains after clarification:

```text
DISPOSITION=BLOCKED_PENDING_REVISED_PROPOSAL_OR_ADDITIONAL_QUALIFIED_REVIEW
FOUNDER_TIE_BREAK=PROHIBITED
SIMPLE_AVERAGING=PROHIBITED
SELECTIVE_DISCARD_OF_DISSENT=PROHIBITED
```

An additional reviewer may be added to the disputed authority function, but doing so does not erase an existing material finding. The proposal must resolve the finding or remain blocked.

## 7. Independence and conflict controls

Every required reviewer must disclose at least:

```text
proposal_authorship_or_material_contribution
candidate_or_vendor_conflict
financial_or_engagement_conflict
organizational_conflict
relevant prior candidate_result_exposure
relevant Private_Gold exposure
other material conflict_or_limitation
```

Required rules:

```text
POLICY_PROPOSAL_AUTHOR_MAY_BE_SOLE_REVIEWER=NO
REVIEWER_WITH_MATERIAL_UNMANAGED_CONFLICT=BLOCKED
TOURNAMENT_CANDIDATE_RESULTS_AVAILABLE_TO_REVIEW=NO
PREFERRED_CANDIDATE_RESULTS_AVAILABLE_TO_REVIEW=NO
PRIVATE_GOLD_SELECTION_RESULTS_AVAILABLE_TO_REVIEW=NO
DESIRED_PASS_RATE_OR_WINNER_AS_REVIEW_BASIS=PROHIBITED
```

Public protocol metadata is not Private Gold case-content exposure, but actual protected case/result exposure must be disclosed and handled fail-closed.

## 8. Immutable review evidence record

Each scientific review disposition must bind at least:

```text
review_record_id
review_record_version
review_authority_function
reviewer_reference
qualification_evidence_reference
review_scope
metric_or_metric_family_scope
reviewed_policy_id
reviewed_policy_canonical_sha256
reviewed_artifact_ids_and_exact_revisions
review_date_or_audit_sequence
candidate_result_exposure_state
conflict_disclosures
review_disposition
reasoned_findings
material_limitations
review_evidence_id
record_canonical_sha256
```

A public repository record may use non-personal reviewer references when the underlying identity/credential evidence is retained in an appropriate protected audit system.

```text
PUBLIC_REPO_REQUIRES_PERSONAL_CREDENTIAL_DOCUMENTS=NO
AUDITABLE_IDENTITY_AND_CREDENTIAL_EVIDENCE_REQUIRED=YES
MUTABLE_LATEST_REVIEW_BINDING=PROHIBITED
```

## 9. Material-change rule

A prior review disposition does not transfer across a material policy change.

Material changes include at least:

```text
numeric threshold or margin
operator or direction
intended role/population/use context
metric or estimand definition
uncertainty or statistical method family
confidence/error-rate semantics
sample-size/power design basis
evidence-source identity
review-governance requirements
```

For any material change:

```text
NEW_POLICY_IDENTITY_REQUIRED=YES
FRESH_CLINICAL_REVIEW_REQUIRED=YES
FRESH_STATISTICAL_REVIEW_REQUIRED=YES
FRESH_GOVERNANCE_ADOPTION_REQUIRED=YES
```

## 10. What this resolves

After canonical qualification and merge of this record, these procedural fields may be treated as frozen for the current A2 pathway:

```text
EXACT_REVIEWER_COUNT=MINIMUM_1_CLINICAL_PLUS_1_STATISTICAL_PLUS_1_DISTINCT_GOVERNANCE_ADOPTER_PER_METRIC_POLICY
EXACT_CLINICAL_REVIEWER_CREDENTIAL_REQUIREMENTS=IDENTITY_BOUND_METRIC_HARM_DOMAIN_COMPETENCE_AS_DEFINED_HERE
EXACT_STATISTICAL_REVIEWER_CREDENTIAL_REQUIREMENTS=IDENTITY_BOUND_METHOD_FAMILY_COMPETENCE_AS_DEFINED_HERE
EXACT_QUORUM_RULE=ALL_REQUIRED_SCIENTIFIC_REVIEWERS_ACCEPT_THEN_DISTINCT_GOVERNANCE_ADOPTION
EXACT_THRESHOLD_REVIEW_DISPOSITION_VOCABULARY=ACCEPT_REVISE_REJECT_BLOCKED
EXACT_THRESHOLD_DISAGREEMENT_RESOLUTION_PROTOCOL=FAIL_CLOSED_REVISE_OR_ADDITIONAL_QUALIFIED_REVIEW_NO_TIE_BREAK
```

These remain unresolved:

```text
EXACT_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
COMMANDMED_SPECIFIC_NUMERIC_THRESHOLD_OR_MARGIN_POLICY=ABSENT
NUMERIC_CONFIDENCE_OR_ERROR_RATE_POLICY=ABSENT
NUMERIC_SAMPLE_SIZE_OR_POWER_DESIGN=ABSENT
CANONICAL_THRESHOLD_POLICY_ADOPTION=ABSENT
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
```

## 11. Authority boundary

```text
REVIEWER_APPOINTMENT_AUTHORITY_CREATED=NO
REVIEWER_ENGAGEMENT_AUTHORITY_CREATED=NO
PAID_REVIEWER_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

MODEL_WEIGHT_ACCESS_AUTHORITY=UNCHANGED_EXISTING_E002_ONLY
MODEL_EXECUTION_AUTHORITY=UNCHANGED_EXISTING_E003_ONLY_SUBJECT_TO_PREFLIGHT
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
E004_EXECUTION_OCCURRED=NO
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## Exclusions

This artifact performs no reviewer outreach, appointment, payment, scientific review, threshold/margin selection, sample-size freeze, benchmark/model/device execution, model conversion, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, or spend.

## Exit evidence for this procedural-governance slice

```text
PROCEDURAL_FIELDS_EXPLICITLY_RESOLVED=YES
SCIENTIFIC_AUTHORITY_FUNCTIONS_REMAIN_SEPARATE=YES
FOUNDER_SOLE_SCIENTIFIC_AUTHORITY=NO
DISPOSITION_VOCABULARY_REUSES_EXISTING_FAIL_CLOSED_STATES=YES
MATERIAL_DISSENT_FAILS_CLOSED=YES
PRE_RESULT_FIREWALL_PRESERVED=YES
NO_REVIEWER_IDENTITY_OR_CREDENTIAL_FABRICATED=YES
NO_NUMERIC_POLICY_FABRICATED=YES
NO_EXECUTION_OR_SPEND_AUTHORITY_CREATED=YES
T1_A2_REMAINS_INCOMPLETE=YES
```
