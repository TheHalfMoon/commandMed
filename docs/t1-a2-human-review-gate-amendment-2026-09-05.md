# T1/A2 Human Review Gate Amendment — 2026-09-05

**Decision class:** Founder bounded scientific-governance amendment  
**Decision ID:** `FD-009`  
**Decision:** `REMOVE_MANDATORY_T1_A2_EXTERNAL_HUMAN_REVIEW_GATE`  
**Effective when:** this amendment and aligned current-state records are canonically merged  
**Scope:** Spec 005 / E004 T1-A2 threshold-and-margin preconstruction only  
**Current authorized spend:** USD 0

## Operative Founder direction

On 2026-09-05, after the bounded reviewer-prescreen lane had been canonically authorized but before any prescreen email was sent, the Founder explicitly directed:

```text
do not send anything , i told you we dont need human reviewr , just build the fucking project
```

The connected Gmail account was checked immediately afterward and no matching prescreen message existed in `SENT`.

This record treats the direction as a bounded scientific-governance amendment for the current T1/A2 preconstruction blocker. It does not infer removal of human evidence from later patient-facing benefit/safety claims or release validation.

## Prior rule

The controlling Session 9 Q4 governance required three distinct authority functions before threshold freeze:

```text
THRESHOLD_AUTHORITY_FUNCTION_1=CLINICAL_DOMAIN_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_2=STATISTICAL_METHOD_REVIEW
THRESHOLD_AUTHORITY_FUNCTION_3=CANONICAL_GOVERNANCE_ADOPTION
CLINICAL_DOMAIN_REVIEW_REQUIRED=YES
STATISTICAL_METHOD_REVIEW_REQUIRED=YES
CLINICAL_REVIEW_DISPOSITION_REQUIRED=YES
STATISTICAL_REVIEW_DISPOSITION_REQUIRED=YES
```

That architecture made external domain-qualified human reviewers a mandatory T1/A2 transition dependency.

## Replacement rule

For the exact Spec 005 / E004 T1-A2 preconstruction edge, external human reviewer participation is no longer a mandatory evidence mechanism.

The replacement path must remain evidence-bound, deterministic, reproducible, pre-result, candidate-neutral, and fail-closed.

```text
T1_A2_EXTERNAL_HUMAN_REVIEW_REQUIRED=NO
T1_A2_EXTERNAL_REVIEWER_OUTREACH_REQUIRED=NO
T1_A2_REVIEWER_APPOINTMENT_REQUIRED=NO
T1_A2_CLINICAL_REVIEWER_DISPOSITION_REQUIRED=NO
T1_A2_STATISTICAL_REVIEWER_DISPOSITION_REQUIRED=NO
T1_A2_CANONICAL_GOVERNANCE_ADOPTION_REQUIRED=YES
T1_A2_NUMERIC_POLICY_REQUIRED=YES
T1_A2_STATISTICAL_JUSTIFICATION_REQUIRED=YES
T1_A2_EVIDENCE_PROVENANCE_REQUIRED=YES
T1_A2_PRE_RESULT_FREEZE_REQUIRED=YES
T1_A2_CANDIDATE_NEUTRALITY_REQUIRED=YES
```

Human-review fields in older schemas or records must not be populated with fabricated people, fake dispositions, AI personas, or proxy identities. Where the existing machine schema requires an authority reference, the successor implementation must use an explicit non-human evidence-policy authority identity only after the schema/validator is amended to permit it.

## Replacement scientific-evidence mechanism

A future T1/A2 PASS may be created only from an exact canonical evidence package that collectively binds:

```text
metric_id
intended_use
role_population_scope
language_modality_scope
metric_direction
decision_role
threshold_kind
unit_or_scale
exact_public_evidence_source_ids_and_revisions
commandmed_specific_evidence_ids_where_required
evidence_transfer_assumptions_and_limitations
clinical_meaningfulness_rationale
statistical_rationale
uncertainty_method_identity
sample_size_or_precision_rationale
multiplicity_or_dependency_model_where_applicable
numeric_threshold_or_margin
candidate_neutrality_attestation
pre_result_freeze
canonical_policy_identity
record_canonical_sha256
```

The numeric value may not be invented merely to unblock execution. It must be derivable from documented evidence plus a predeclared conservative rule.

```text
ROUND_NUMBER_OR_CONVENIENCE_AS_SOLE_BASIS=PROHIBITED
DESIRED_PASS_RATE_AS_BASIS=PROHIBITED
DESIRED_WINNER_AS_BASIS=PROHIBITED
TOURNAMENT_RESULTS_AS_THRESHOLD_DERIVATION_INPUT=PROHIBITED
PRIVATE_GOLD_SELECTION_RESULTS_AS_THRESHOLD_DERIVATION_INPUT=PROHIBITED
LLM_FREEFORM_NUMERIC_RECOMMENDATION_AS_SOLE_BASIS=PROHIBITED
```

An LLM may assist with source discovery, drafting, consistency checks, and implementation, but every scientific numeric claim used for canonical threshold policy must be traceable to explicit source evidence or deterministic computation. The LLM itself is not represented as a clinician or statistician.

## Outreach supersession

The Founder direction supersedes the practical use of the reviewer-prescreen lane created through PR #246.

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_B_HISTORICAL_CANONICAL_RECORD
PRESCREEN_OUTREACH_EXECUTION_CURRENTLY_DESIRED=NO
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_FOR_EXECUTION_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED_BY_FD009_CURRENT_POLICY
EXTERNAL_REVIEWER_APPOINTMENT_AUTHORITY=NONE
SCIENTIFIC_REVIEW_ENGAGEMENT_AUTHORITY=NONE
```

PR #246 remains valid audit history. FD-009 does not rewrite the fact that Decision B was selected and merged; it prospectively closes that execution lane because the Founder has now chosen the no-human-review path for T1/A2.

## What this amendment does not change

This amendment does not remove:

- Constitution clinical-safety hard gates;
- provenance, rights, privacy, contamination, identity, or holdout requirements;
- deterministic validator requirements;
- evidence-dependent numeric threshold and statistical-design requirements;
- `D-010`, which requires human evidence for patient-facing benefit/safety claims;
- any later explicit human-factor or release-human-evidence requirement;
- zero-spend, credential, PHI, Private Gold, protected-data, conversion, A15, tournament, or training authority gates.

It does not claim that T1/A2 is already PASS.

## Immediate successor authority

After canonical merge, repository-only implementation is authorized to replace the T1/A2 reviewer-dependent schema/validator path with an exact non-human evidence-policy path, including tests and aligned documentation, provided that the implementation:

- does not invent numeric policy values;
- does not access candidate tournament results;
- does not execute models, conversion, contamination assessment, A15, tournament, or training without separate existing authority;
- does not contact external reviewers;
- preserves fail-closed behavior for incomplete evidence;
- preserves compatibility with D-010 for later patient-facing claims.

```text
FD009_DECISION=REMOVE_MANDATORY_T1_A2_EXTERNAL_HUMAN_REVIEW_GATE
T1_A2_EXTERNAL_HUMAN_REVIEW_REQUIRED=NO
T1_A2_NON_HUMAN_EVIDENCE_POLICY_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REPOSITORY_ONLY
T1_A2_NUMERIC_POLICY_AUTOMATICALLY_PASSED=NO
T1_A2_STATE=INCOMPLETE_PENDING_EVIDENCE_POLICY_IMPLEMENTATION_AND_NUMERIC_FREEZE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Historical preservation

Earlier Q4, reviewer-slate, outreach, and reconciliation records remain immutable audit history. They are superseded prospectively only where they require an external human reviewer as the mandatory mechanism for the exact current T1/A2 preconstruction transition.
