# E004 A2 Evidence-Package Workbench — 2026-08-27

**Spec:** 007 SFT V1  
**Related control plane:** Spec 005 A2 + atomic A3/A4 scientific readiness  
**Canonical base:** `823a03f52b75b5753e5fc16849c57c3c9d67134d`  
**Artifact class:** metadata-only review workbench  
**Authority effect:** NONE  
**Validator input:** NO

This workbench converts the canonical A2 public-evidence inventory into a review-ready metadata structure without manufacturing any scientific PASS condition.

It is **not** a `ThresholdPolicy` record, **not** a `StatisticalDesign` record, **not** an executable selection manifest, and **not** evidence that a qualified reviewer has approved anything. It must not be supplied to `validate_threshold_policy()`, `validate_statistical_design()`, or `evaluate_scientific_selection_readiness()` as though unresolved workbench fields were canonical values.

```text
A2_WORKBENCH_ONLY=YES
A2_REAL_THRESHOLD_RECORDS_CREATED=0
A2_REAL_STATISTICAL_DESIGN_RECORDS_CREATED=0
A2_REAL_REVIEW_DISPOSITIONS_CREATED=0
A2_REAL_NUMERIC_THRESHOLDS_FROZEN=0
A2_REAL_NUMERIC_N_FROZEN=0
A2_REAL_SELECTION_SUITE_BOUND=NO
A2_STATE=INCOMPLETE_REAL_EVIDENCE_AND_REVIEW_REQUIRED
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Canonical authority state preserved

This workbench has no authority effect. Current repository authority remains:

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY

CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The bounded E002/E003 authorities are not currently executable because `E004_STATE=BLOCKED_PREFLIGHT`.

## 2. Why this workbench exists

Canonical `src/commandmed/spec005/science.py` and `data/spec005/selection_quality_contract.json` already define the machine-verifiable A2/A3+A4 surfaces. The remaining gap is not another schema. The gap is real evidence and review input.

This artifact therefore does only three things:

1. binds stable publication locators already found in the public discovery pass to each hard-gate metric;
2. records what each source can and cannot support;
3. projects the unresolved fields that a future real `ThresholdPolicy` and `StatisticalDesign` must fill before canonical validation can PASS.

No workbench field has authority merely because it is written here.

## 3. Canonical machine-record targets

### 3.1 Future A2 `ThresholdPolicy`

The actual validator requires these fields:

```text
threshold_policy_id
threshold_policy_version
metric_id
metric_evidence_role
lane_id
required_stratum_or_scope
estimand_id
metric_direction
decision_role
threshold_kind
unit_or_scale
clinical_meaningfulness_evidence_ids
statistical_justification_evidence_ids
clinical_review_authority_reference
statistical_review_authority_reference
conflict_disposition_record_ids
pre_result_freeze
record_canonical_sha256
threshold_value_or_margin   # conditionally required; absence blocks PASS
```

This workbench does not assign a real threshold-policy ID/version/SHA and does not set `pre_result_freeze=true`, because no numeric policy has been scientifically approved and frozen.

### 3.2 Future atomic A3+A4 `StatisticalDesign`

The actual validator requires:

```text
statistical_design_id
design_version
quality_lane
metric_id_or_metric_mapping_id
required_stratum_or_scope
estimand
unit_of_analysis
decision_role
threshold_policy_id_or_explicit_not_applicable
precision_or_power_objective
confidence_or_error_rate_parameters
anticipated_rate_variance_or_other_nuisance_inputs
source_and_provenance_for_planning_inputs
pairing_or_cluster_dependency_model
multiplicity_structure
planned_numeric_n
coverage_allocation_design
rounding_or_allocation_rule
software_formula_or_method_identity
sensitivity_analysis_identity_or_explicit_not_required
candidate_neutral
pre_result_freeze
record_canonical_sha256
```

This workbench leaves all numeric and method-selection values unresolved.

## 4. Source-binding status vocabulary

```text
BOUND_PUBLICATION_LOCATOR=
  stable DOI, PMID, or arXiv identifier is recorded

METHOD_OR_RISK_CONTEXT_ONLY=
  source may inform design/appraisal but cannot be copied into commandMed policy

NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE=
  public literature is insufficient; a commandMed-specific evidence artifact is still required

NEEDS_QUALIFIED_CLINICAL_REVIEW=
  no review disposition exists

NEEDS_QUALIFIED_STATISTICAL_REVIEW=
  no review disposition exists

NEEDS_NUMERIC_POLICY=
  no threshold/margin is frozen

NEEDS_STATISTICAL_DESIGN=
  no exact uncertainty/power/N/allocation design is frozen
```

`BOUND_PUBLICATION_LOCATOR` does **not** mean the publication alone satisfies `IDENTITY_BOUND_EVIDENCE` for commandMed selection.

## 5. `emergency_miss_rate` workbench

Canonical mapping:

```text
METRIC_ID=emergency_miss_rate
LANE_ID=B_PATIENT_CAREGIVER_CLINICAL_SAFETY
METRIC_EVIDENCE_ROLE=QUALIFICATION_ONLY
METRIC_DIRECTION=LOWER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=ratio
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Public source locators:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-EMER-001` | PMID `39420246`; DOI `10.1080/00325481.2024.2418806` | prospective ED under-triage harm/context | evaluated chatbot/triage setting is not commandMed intended-use evidence and observed rates are not policy |
| `A2PUB-EMER-002` | PMID `39262027`; DOI `10.1111/jnu.13024` | systematic prospective triage evidence context | heterogeneous systems/outcomes cannot define one commandMed threshold |
| `A2PUB-EMER-003` | PMID `41753200`; DOI `10.3390/jcm15041512` | large retrospective LLM triage context | retrospective supervised-support conclusion is not a threshold derivation |

Future real A2 fields still required:

```text
REQUIRED_STRATUM_OR_SCOPE=NEEDS_EVIDENCE
ESTIMAND_ID=NEEDS_EVIDENCE
THRESHOLD_KIND=NEEDS_EVIDENCE
CLINICAL_MEANINGFULNESS_EVIDENCE_IDS=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
STATISTICAL_JUSTIFICATION_EVIDENCE_IDS=NEEDS_EVIDENCE
CLINICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_CLINICAL_REVIEW
STATISTICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_STATISTICAL_REVIEW
CONFLICT_DISPOSITION_RECORD_IDS=NEEDS_EVIDENCE
THRESHOLD_VALUE_OR_MARGIN=NEEDS_NUMERIC_POLICY
```

Future A3+A4 fields still required:

```text
PRECISION_OR_POWER_OBJECTIVE=NEEDS_STATISTICAL_DESIGN
CONFIDENCE_OR_ERROR_RATE_PARAMETERS=NEEDS_STATISTICAL_DESIGN
NUISANCE_INPUTS=NEEDS_STATISTICAL_DESIGN
PAIRING_OR_CLUSTER_DEPENDENCY_MODEL=NEEDS_STATISTICAL_DESIGN
MULTIPLICITY_STRUCTURE=NEEDS_STATISTICAL_DESIGN
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
COVERAGE_ALLOCATION_DESIGN=NEEDS_STATISTICAL_DESIGN
SOFTWARE_FORMULA_OR_METHOD_IDENTITY=NEEDS_STATISTICAL_DESIGN
```

Required future clinical expertise remains acute/emergency-domain review plus statistical-method review. No reviewer is appointed here.

## 6. `medication_critical_error_rate` workbench

Canonical mapping:

```text
METRIC_ID=medication_critical_error_rate
LANE_ID=B_PATIENT_CAREGIVER_CLINICAL_SAFETY
METRIC_EVIDENCE_ROLE=QUALIFICATION_ONLY
METRIC_DIRECTION=LOWER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=ratio
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Public source locators:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-MED-001` | PMID `41368579`; DOI `10.3389/fphar.2025.1514445` | medication-regimen harm taxonomy/context | ICU case-based error frequencies are not a universal acceptable rate |
| `A2PUB-MED-002` | PMID `40997804`; DOI `10.1016/j.xcrm.2025.102323` | pharmacist/LLM co-pilot evaluation context | prescribing-error detection workflow differs from commandMed gate semantics |
| `A2PUB-MED-003` | PMID `41404284`; DOI `10.64898/2025.12.01.25341004` | medication-task coverage/method context | benchmark task variation cannot define commandMed policy |
| `A2PUB-MED-004` | PMID `38899788`; DOI `10.1177/14604582241263242` | DDI-alert override context | override prevalence is not clinically critical error prevalence or acceptability |

Additional unresolved identity required by canonical policy:

```text
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_IDENTITY=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_SOURCE_REVISION=NEEDS_EVIDENCE
AUTHORITATIVE_MEDICATION_LOOKUP_RESULT_DIGEST_CONTRACT=NEEDS_EVIDENCE
```

Future real A2/A3+A4 fields remain unresolved exactly as required by the validator, including threshold/margin, clinical-pharmacology review, statistical review, uncertainty method, N, allocation, and method identity.

## 7. `selective_risk_at_target_coverage` workbench

Canonical mapping:

```text
METRIC_ID=selective_risk_at_target_coverage
LANE_ID=C_UNCERTAINTY_ABSTENTION_INFORMATION_SEEKING
METRIC_EVIDENCE_ROLE=QUALIFICATION_ONLY
METRIC_DIRECTION=LOWER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=score
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Public source locators:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-SEL-001` | PMID `34854476`; DOI `10.1111/biom.13612` | selective-prediction/coverage methodology | methodology does not supply commandMed target coverage or acceptable risk |
| `A2PUB-SEL-002` | PMID `41721063`; DOI `10.1038/s41598-026-40637-w` | held-out calibration, risk-coverage, cost-aware deferral context | reported 80%/90%/95% quantities have different task-specific meanings and are not transferable |
| `A2PUB-SEL-003` | PMID `42298124`; DOI `10.1038/s41746-026-02882-1` | healthcare LLM abstention decision framing | review does not define a universal confidence/risk cutoff |

Future real record blockers:

```text
CALIBRATED_HOLDOUT_IDENTITY=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
TARGET_COVERAGE=NEEDS_NUMERIC_POLICY
ACCEPTABLE_RISK_THRESHOLD_OR_MARGIN=NEEDS_NUMERIC_POLICY
LOSS_OR_RISK_ESTIMAND=NEEDS_EVIDENCE
CLINICAL_SAFETY_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_CLINICAL_REVIEW
STATISTICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_STATISTICAL_REVIEW
UNCERTAINTY_METHOD_IDENTITY=NEEDS_STATISTICAL_DESIGN
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

No public operating point is adopted here.

## 8. `citation_entailment_fidelity` workbench

Canonical mapping:

```text
METRIC_ID=citation_entailment_fidelity
LANE_ID=D_EVIDENCE_GROUNDED_CLINICAL
METRIC_EVIDENCE_ROLE=QUALIFICATION_ONLY
METRIC_DIRECTION=HIGHER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=percentage
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Public source locator:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-CITE-001` | DOI `10.1038/s41467-025-58551-6` | SourceCheckup statement/source support methodology and medical-expert validation precedent | verifier design and measured support rates are not commandMed verifier identity or threshold |

Future real blockers:

```text
SELECTION_DEV_EVIDENCE_SUITE_IDENTITY=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
DETERMINISTIC_VERIFIER_IDENTITY=NEEDS_EVIDENCE
CLINICIAN_AUDIT_PROTOCOL_IDENTITY=NEEDS_EVIDENCE
CLINICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_CLINICAL_REVIEW
STATISTICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_STATISTICAL_REVIEW
MINIMUM_ACCEPTABLE_POPULATION_FIDELITY=NEEDS_NUMERIC_POLICY
UNCERTAINTY_METHOD_IDENTITY=NEEDS_STATISTICAL_DESIGN
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

Citation presence alone is not treated as entailment evidence.

## 9. `arabic_clinical_parity_gap` workbench

Canonical V2 mapping:

```text
METRIC_ID=arabic_clinical_parity_gap
LANE_ID=E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY
METRIC_EVIDENCE_ROLE=SELECTION_DEV
METRIC_DIRECTION=LOWER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=relative_gap
V2_EVIDENCE_ROLE_SCHEMA_CONFLICT=RESOLVED_BY_A1
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Private Gold is a separate V2 lifecycle role:

```text
PRIVATE_GOLD_FINAL_AUDIT_PURPOSE=PRIVATE_GOLD
PRIVATE_GOLD_FINAL_AUDIT_SOURCE_POLICY=PRIVATE_GOLD_FAMILY
PRIVATE_GOLD_CAN_SELECT_MODEL=NO
```

Public source locators:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-AR-001` | arXiv `2602.05374` | cross-lingual Arabic medical performance-gap/task-complexity context | observed gap is not commandMed maximum acceptable parity gap |
| `A2PUB-AR-002` | arXiv `2505.03427` | Arabic medical task-suite/domain coverage context | benchmark is not automatically a commandMed selection-safe paired suite |

Future real blockers:

```text
SELECTION_SAFE_PAIRED_ARABIC_ENGLISH_SUITE_IDENTITY=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
MATCHED_ROOT_TASK_PAIR_IDENTITY=NEEDS_EVIDENCE
REQUIRED_ARABIC_COVERAGE_ANCHORS_BINDING=NEEDS_EVIDENCE
REQUIRED_ROLE_COVERAGE_BINDING=NEEDS_EVIDENCE
MAXIMUM_ACCEPTABLE_PARITY_GAP=NEEDS_NUMERIC_POLICY
PAIRED_ESTIMAND=NEEDS_EVIDENCE
PAIRED_DEPENDENCY_MODEL=NEEDS_STATISTICAL_DESIGN
CLINICAL_SEMANTIC_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_CLINICAL_REVIEW
STATISTICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_STATISTICAL_REVIEW
COMPLETE_PAIR_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
ALLOCATION_ACROSS_ANCHORS_ROLES_STRATA=NEEDS_STATISTICAL_DESIGN
```

An unpaired independent-two-sample shortcut remains prohibited by the canonical validator. No selection suite is created or accessed here.

## 10. `lab_report_field_extraction_accuracy` workbench

Canonical mapping:

```text
METRIC_ID=lab_report_field_extraction_accuracy
LANE_ID=G_LAB_DOCUMENT_STRUCTURED_QUALIFICATION
METRIC_EVIDENCE_ROLE=QUALIFICATION_ONLY
METRIC_DIRECTION=HIGHER_BETTER
DECISION_ROLE=HARD_GATE
UNIT_OR_SCALE=f1_score
CURRENT_THRESHOLD_READINESS=NOT_READY_TO_FREEZE
```

Public source locators:

| Workbench source | Stable locator | Evidence use | Transfer limitation |
|---|---|---|---|
| `A2PUB-LAB-001` | PMID `37932733`; DOI `10.1186/s12911-023-02346-6` | paper-laboratory-report extraction performance/method context | field definitions/report layouts differ; observed F1 is not a minimum policy |
| `A2PUB-LAB-002` | PMID `38875570` | large laboratory-report NLP performance/subgroup context | overall micro-F1 can conceal rare-label failure and does not bind commandMed schema/comparator |

Future real blockers:

```text
SELECTION_DEV_CURATED_FIXTURE_IDENTITIES=NEEDS_IDENTITY_BOUND_COMMANDMED_EVIDENCE
FIELD_SCHEMA_IDENTITY=NEEDS_EVIDENCE
DETERMINISTIC_COMPARATOR_IDENTITY=NEEDS_EVIDENCE
CLINICAL_INFORMATICS_OR_LAB_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_CLINICAL_REVIEW
STATISTICAL_REVIEW_AUTHORITY_REFERENCE=NEEDS_QUALIFIED_STATISTICAL_REVIEW
MINIMUM_ACCEPTABLE_F1=NEEDS_NUMERIC_POLICY
F1_UNCERTAINTY_METHOD=NEEDS_STATISTICAL_DESIGN
ROOT_CASE_DEPENDENCY_MODEL=NEEDS_STATISTICAL_DESIGN
PLANNED_NUMERIC_N=NEEDS_STATISTICAL_DESIGN
```

## 11. Cross-metric review-input template

For each future metric-specific evidence package, a qualified reviewer should receive at least the following metadata. This list is an input checklist, not an approval form and not a quorum rule.

```text
METRIC_ID
LANE_ID
DECISION_ROLE
INTENDED_USE
ROLE_POPULATION_SCOPE
LANGUAGE_MODALITY_SCOPE
PROPOSED_ESTIMAND
PROPOSED_UNIT_OF_ANALYSIS
PROPOSED_THRESHOLD_KIND
PROPOSED_NUMERIC_VALUE_OR_MARGIN
PUBLIC_EVIDENCE_SOURCE_IDENTITIES
COMMANDMED_SPECIFIC_EVIDENCE_ARTIFACT_IDENTITIES
EVIDENCE_APPRAISAL_SUMMARY
TRANSFERABILITY_LIMITATIONS
PROPOSED_UNCERTAINTY_METHOD
PROPOSED_SAMPLE_SIZE_OR_POWER_RATIONALE
PROPOSED_PAIRING_OR_CLUSTER_DEPENDENCY_MODEL
PROPOSED_MULTIPLICITY_STRUCTURE
KNOWN_CONFLICTS_OR_DISSENT
CANDIDATE_RESULT_EXPOSURE=NO_REQUIRED
```

The reviewer identity, reviewer count, quorum, disagreement-resolution mechanism, and actual disposition remain unresolved under current governance. This workbench does not invent them.

## 12. Review-output boundary

A future actual review disposition must be created by the required qualified human authority and bound canonically. ChatGPT/repository automation cannot impersonate that authority.

```text
CLINICAL_REVIEW_PERFORMED_BY_THIS_WORKBENCH=NO
STATISTICAL_REVIEW_PERFORMED_BY_THIS_WORKBENCH=NO
REVIEWER_IDENTITIES_ASSIGNED_BY_THIS_WORKBENCH=NO
REVIEWER_COUNT_FROZEN_BY_THIS_WORKBENCH=NO
QUORUM_FROZEN_BY_THIS_WORKBENCH=NO
DISAGREEMENT_PROTOCOL_FROZEN_BY_THIS_WORKBENCH=NO
```

Founder preference alone also remains insufficient for the clinical/statistical prerequisites.

## 13. Promotion rule from workbench to real records

No section in this file may be copied into a canonical PASS record merely by replacing `NEEDS_EVIDENCE` with a value.

Promotion requires all of the following independently:

1. exact commandMed intended-use/population and evaluation-design binding;
2. exact immutable evidence artifact identities and provenance;
3. qualified clinical-domain review disposition where required;
4. qualified statistical-method review disposition;
5. conflict/dissent disposition under then-canonical governance;
6. exact pre-result numeric threshold/margin when required;
7. exact atomic A3+A4 statistical design, including numeric N/allocation and method identity;
8. canonical serialization/identity generation through repository code;
9. validation against the then-current canonical metrics-v2 and selection-quality contract;
10. separate canonical governance adoption before use.

Any missing item remains fail closed.

## 14. Current frontier after workbench preparation

```text
PUBLIC_EVIDENCE_LOCATORS_BOUND_IN_WORKBENCH=YES
COMMANDMED_SPECIFIC_A2_EVIDENCE_PACKAGES_COMPLETE=NO
QUALIFIED_CLINICAL_REVIEW_COMPLETE=NO
QUALIFIED_STATISTICAL_REVIEW_COMPLETE=NO
NUMERIC_THRESHOLDS_FROZEN=0
STATISTICAL_DESIGNS_FROZEN=0
PRIMARY_SELECTION_MANIFEST_FROZEN=NO
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 15. Non-events

No benchmark, selection-suite, Private Gold, PHI/restricted, model-weight, GGUF, credential, device, payment, or provider payload was accessed. No model, benchmark, contamination, conversion, quantization, device, tournament, or training execution occurred. No clinical or statistical reviewer was represented as having reviewed or approved this workbench.