# E004 A2 Public Threshold-Evidence Discovery — 2026-08-27

**Spec:** 007 SFT V1  
**Related control plane:** Spec 005 A2 scientific threshold/margin readiness  
**Canonical research base:** `446ac00a8466de8de243f300abdce0ec33d36e57`  
**Lifecycle:** public research only  
**Authority effect:** NONE

This packet records a bounded read-only public-literature discovery pass for the six Spec 005 hard-gate population metrics. Its purpose is to identify potentially useful evidence classes and methodological anchors for later qualified clinical/statistical review.

It does **not** freeze a numeric threshold, margin, target coverage, confidence level, sample size, power target, reviewer identity, suite identity, metric implementation, or Founder decision. It does not replace the canonical threshold-readiness matrix and does not make any hard gate ready to freeze.

```text
A2_PUBLIC_EVIDENCE_DISCOVERY_ONLY=YES
A2_NUMERIC_THRESHOLD_FREEZE_AUTHORITY=NONE
A2_CLINICAL_REVIEW_AUTHORITY_IDENTITIES=UNRESOLVED
A2_STATISTICAL_REVIEW_AUTHORITY_IDENTITIES=UNRESOLVED
A2_CANONICAL_GOVERNANCE_ADOPTION=NOT_PERFORMED
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
```

## 1. Canonical A2 question

The canonical threshold contract requires, before any statistical threshold may freeze:

```text
INTENDED_USE_AND_POPULATION
EVALUATION_DESIGN
IDENTITY_BOUND_EVIDENCE
CLINICAL_REVIEW_AUTHORITY
STATISTICAL_RATIONALE
SAMPLE_SIZE_OR_POWER_RATIONALE
CANONICAL_GOVERNANCE_ADOPTION
```

The six current hard-gate population metrics are:

```text
emergency_miss_rate
medication_critical_error_rate
selective_risk_at_target_coverage
citation_entailment_fidelity
arabic_clinical_parity_gap
lab_report_field_extraction_accuracy
```

The question for this packet is deliberately narrower than threshold freeze:

> Does current public evidence provide useful, identity-bound scientific context or method candidates for later expert review, and does any source justify copying a universal numeric threshold directly into commandMed?

Current result:

```text
PUBLIC_METHOD_OR_RISK_CONTEXT_EVIDENCE_FOUND=YES
UNIVERSALLY_TRANSFERABLE_COMMANDMED_NUMERIC_THRESHOLD_FOUND=NO
A2_THRESHOLD_FREEZE_STATUS_CHANGED=NO
```

## 2. Cross-cutting regulatory and scientific context

### 2.1 WHO — intended-use-specific analytical and clinical validation

WHO's *Regulatory considerations on artificial intelligence for health* states that evaluation of AI performance claims requires a clear use-case description plus analytical and clinical validation, including safety/performance evidence and assessment of bias/discrimination.

Public source:

- `https://iris.who.int/bitstream/handle/10665/373421/9789240078871-eng.pdf`

Evidence use in commandMed:

```text
WHO_AI_HEALTH_VALIDATION_SOURCE_CLASS=AUTHORITATIVE_GOVERNANCE_CONTEXT
WHO_SOURCE_SUPPORTS_INTENDED_USE_SPECIFIC_VALIDATION=YES
WHO_SOURCE_SUPPLIES_COMMANDMED_METRIC_SPECIFIC_NUMERIC_THRESHOLD=NO
```

### 2.2 FDA — intended use, inputs, methods and clinical validation

FDA's January 2026 *Clinical Decision Support Software* final guidance emphasizes intended use/user/population, required medical inputs, description of the underlying methods/data, and clinical validation evidence sufficient for independent review of recommendation bases.

Public sources:

- `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software`
- `https://www.fda.gov/medical-devices/digital-health-center-excellence/step-6-software-function-intended-provide-clinical-decision-support`

Evidence use in commandMed:

```text
FDA_CDS_SOURCE_CLASS=AUTHORITATIVE_REGULATORY_CONTEXT
FDA_SOURCE_SUPPORTS_INTENDED_USE_AND_VALIDATION_BINDING=YES
FDA_SOURCE_SUPPLIES_COMMANDMED_UNIVERSAL_NUMERIC_THRESHOLD=NO
```

### 2.3 American Heart Association — risk-proportionate health-AI evaluation

The 2026 AHA science advisory *Pragmatic Approaches to the Evaluation and Monitoring of Artificial Intelligence in Health Care* addresses risk-proportionate evaluation/monitoring of predictive, generative and agentic health AI.

Public source:

- `https://pubmed.ncbi.nlm.nih.gov/41208719/`

Evidence use in commandMed:

```text
AHA_HEALTH_AI_SOURCE_CLASS=PROFESSIONAL_SCIENTIFIC_GOVERNANCE_CONTEXT
AHA_SOURCE_SUPPORTS_RISK_PROPORTIONATE_EVALUATION=YES
AHA_SOURCE_SUPPLIES_ALL_COMMANDMED_NUMERIC_THRESHOLDS=NO
```

The cross-cutting sources support commandMed's existing governance architecture. They do not replace metric-specific clinical/statistical evidence.

## 3. `emergency_miss_rate`

Canonical evidence need:

```text
REQUIRED_EVIDENCE=Clinical adjudication panel on emergency evaluation suite
CLINICAL_DOMAIN_REVIEW=RELEVANT_ACUTE_OR_EMERGENCY_CLINICAL_REVIEW
STATISTICAL_METHOD_REVIEW=REQUIRED
```

### Public evidence candidates

#### 3.1 Prospective emergency-department chatbot triage evaluation

PubMed PMID `39420246` reports a prospective study of 500 emergency-department patients. Relative to emergency physicians, the evaluated chatbots showed materially high under-triage; the best-performing chatbot still under-triaged substantial proportions of yellow/red cases. The authors concluded that sole reliance on the evaluated AI models was not appropriate.

- `https://pubmed.ncbi.nlm.nih.gov/39420246/`

#### 3.2 Systematic review of prospective AI triage studies

A 2025 systematic review examined prospective clinical applications of AI triage and the effects on under-triage/over-triage and emergency-department workflow.

- PMID `39262027`
- `https://pubmed.ncbi.nlm.nih.gov/39262027/`

#### 3.3 Large retrospective LLM triage evaluation

A 2026 retrospective evaluation of multiple LLMs in 39,375 emergency-department patients found inconsistent performance and concluded that current LLMs were more appropriate as supervised support than autonomous triage.

- PMID `41753200`
- `https://pubmed.ncbi.nlm.nih.gov/41753200/`

#### 3.4 START and CTAS reproducibility studies

Commercial-LLM triage studies report nontrivial under-triage, over-triage, and repeatability/reproducibility limitations under START and Canadian Triage and Acuity Scale protocols.

- START: PMID `39348189` — `https://pubmed.ncbi.nlm.nih.gov/39348189/`
- CTAS: PMID `38206515` — `https://pubmed.ncbi.nlm.nih.gov/38206515/`

### Discovery disposition

These sources are useful for:

- confirming emergency under-triage is a clinically material harm dimension;
- informing evaluation-design failure modes and comparator design;
- justifying clinically qualified acute/emergency review;
- motivating reproducibility and uncertainty reporting.

They do **not** establish a universally acceptable commandMed `emergency_miss_rate` population threshold because the source tasks, triage scales, populations, model roles, and intended uses differ.

```text
EMERGENCY_PUBLIC_RISK_CONTEXT=FOUND
EMERGENCY_PUBLIC_METHOD_CONTEXT=FOUND
EMERGENCY_TRANSFERABLE_NUMERIC_THRESHOLD=NOT_ESTABLISHED
EMERGENCY_THRESHOLD_FREEZE_READINESS=NOT_READY_TO_FREEZE
```

## 4. `medication_critical_error_rate`

Canonical evidence need:

```text
REQUIRED_EVIDENCE=Deterministic drug-interaction lookup and clinical pharmacology review
REQUIRED_RESULT_IDENTITY_FIELDS=source_id,source_revision,result_digest
CLINICAL_DOMAIN_REVIEW=RELEVANT_MEDICATION_OR_PHARMACOLOGY_SAFETY_REVIEW
STATISTICAL_METHOD_REVIEW=REQUIRED
```

### Public evidence candidates

#### 4.1 Complex medication-regimen LLM evaluation

A 2025/2026 case-based evaluation of LLM management of complex ICU medication regimens found multiple medication errors per regimen and life-threatening recommendations in a material fraction of generated regimens.

- PMID `41368579`
- `https://pubmed.ncbi.nlm.nih.gov/41368579/`

#### 4.2 Medication-safety LLM/CDSS evaluation across specialties

A prospective study across 16 specialties evaluated LLM-based prescribing-error detection and pharmacist+LLM co-pilot strategies; performance varied and the combined approach outperformed some alternatives for serious-harm detection.

- PMID `40997804`
- `https://pubmed.ncbi.nlm.nih.gov/40997804/`

#### 4.3 Rx-LLM medication benchmark

Rx-LLM reports task-specific variation across drug-drug interaction, dose adjustment, formulation, ordering and other medication tasks, with no model uniformly superior across medication-safety tasks.

- PMID `41404284`
- `https://pubmed.ncbi.nlm.nih.gov/41404284/`

#### 4.4 DDI alert systematic review

A systematic review/meta-analysis found very high clinician override rates for drug-drug interaction alerts, illustrating that alert prevalence and alert acceptance cannot be treated as a direct proxy for clinically critical error rate or acceptable safety threshold.

- PMID `38899788`
- `https://pubmed.ncbi.nlm.nih.gov/38899788/`

### Discovery disposition

The literature supports:

- task-specific medication evaluation rather than a single generic score;
- clinical-pharmacology review of severity/relevance;
- deterministic authoritative drug-interaction identity where used;
- distinguishing false alerts from clinically material errors.

It does not establish one acceptable commandMed population `medication_critical_error_rate`.

```text
MEDICATION_PUBLIC_RISK_CONTEXT=FOUND
MEDICATION_PUBLIC_METHOD_CONTEXT=FOUND
MEDICATION_TRANSFERABLE_NUMERIC_THRESHOLD=NOT_ESTABLISHED
MEDICATION_AUTHORITATIVE_LOOKUP_IDENTITY_FOR_SPEC005=STILL_UNRESOLVED
MEDICATION_THRESHOLD_FREEZE_READINESS=NOT_READY_TO_FREEZE
```

## 5. `selective_risk_at_target_coverage`

Canonical evidence need:

```text
REQUIRED_EVIDENCE=Abstention curve evaluation on calibrated holdout suite
EXACT_TARGET_COVERAGE=NOT_YET_FROZEN
EXACT_ACCEPTABLE_RISK_THRESHOLD_OR_MARGIN=NOT_YET_FROZEN
```

### Public evidence candidates

#### 5.1 Selective prediction with coverage guarantees

Feng et al. describe healthcare selective prediction as a middle ground between always requiring clinician oversight and deploying predictions without oversight, with formal coverage-rate guarantees.

- PMID `34854476`
- DOI `10.1111/biom.13612`
- `https://pubmed.ncbi.nlm.nih.gov/34854476/`

#### 5.2 Cost-aware conformal selective prediction for clinical triage

A 2026 Scientific Reports study evaluates conformal selective prediction and cost-aware deferral under temporal distribution shift. It demonstrates risk-coverage analysis at selected operating points, including an 80% coverage example, while deriving the deferral decision from a task-specific clinical cost model and held-out calibration set.

- PMID `41721063`
- DOI `10.1038/s41598-026-40637-w`
- `https://pubmed.ncbi.nlm.nih.gov/41721063/`

#### 5.3 Health-care LLM abstention review

A 2026 review introduces a decision-theoretic framing for LLM abstention in health care and emphasizes uncertainty- and safety-driven abstention rather than a universal confidence cutoff.

- PMID `42298124`
- `https://pubmed.ncbi.nlm.nih.gov/42298124/`

### Discovery disposition

The sources support:

- predeclared risk-coverage curves;
- held-out calibration;
- explicit clinical cost/harm preferences;
- subgroup/distribution-shift analysis;
- uncertainty/abstention as a safety mechanism.

The published 70%, 80%, 90%, 95%, or other task-specific operating points are **not** transferable commandMed targets. The canonical matrix explicitly prohibits inferring target coverage from another project or benchmark.

```text
SELECTIVE_RISK_PUBLIC_METHOD_CONTEXT=FOUND_STRONG
SELECTIVE_RISK_UNIVERSAL_TARGET_COVERAGE=NOT_ESTABLISHED
SELECTIVE_RISK_UNIVERSAL_ACCEPTABLE_RISK=NOT_ESTABLISHED
SELECTIVE_RISK_THRESHOLD_FREEZE_READINESS=NOT_READY_TO_FREEZE
```

## 6. `citation_entailment_fidelity`

Canonical evidence need:

```text
REQUIRED_EVIDENCE=Deterministic verifier + clinician audit on citation-backed responses
EXACT_DETERMINISTIC_VERIFIER_IDENTITY=UNRESOLVED
EXACT_CLINICIAN_AUDIT_PROTOCOL_AND_AUTHORITY_IDENTITIES=UNRESOLVED
```

### Public evidence candidates

#### 6.1 SourceCheckup medical citation-support framework

Wu et al., *An automated framework for assessing how well LLMs cite relevant medical references*, Nature Communications (2025), introduces SourceCheckup and evaluates statement/source support in medical responses. The work validates automated source-verification judgments against physician review and reports substantial unsupported-citation failure rates across evaluated systems.

- DOI `10.1038/s41467-025-58551-6`
- `https://www.nature.com/articles/s41467-025-58551-6`

The paper is methodologically relevant because it separates source validity/relevance from whether a source actually supports a generated statement and includes clinician validation of automated assessment.

#### 6.2 Evidence-grounded clinical response datasets

Recent clinical datasets evaluate factual grounding/relevance using explicit evidence alignment and F1-style measures, reinforcing the need to bind the exact evidence unit and scoring semantics rather than using citation presence alone.

Representative source:

- `https://www.nature.com/articles/s41597-026-06639-z`

### Discovery disposition

These sources can inform:

- deterministic-verifier design candidates;
- statement-level versus response-level evidence semantics;
- clinician-audit sampling and disagreement analysis;
- the distinction between URL validity and claim entailment/support.

They do not define a universally acceptable population `citation_entailment_fidelity` percentage for commandMed's intended use.

```text
CITATION_PUBLIC_VERIFICATION_METHOD_CONTEXT=FOUND_STRONG
CITATION_PUBLIC_CLINICIAN_VALIDATION_PRECEDENT=FOUND
CITATION_TRANSFERABLE_NUMERIC_THRESHOLD=NOT_ESTABLISHED
CITATION_EXACT_COMMANDMED_VERIFIER_IDENTITY=UNRESOLVED
CITATION_THRESHOLD_FREEZE_READINESS=NOT_READY_TO_FREEZE
```

## 7. `arabic_clinical_parity_gap`

Canonical state includes an independent evidence-role conflict:

```text
CANONICAL_REQUIRED_EVIDENCE=Paired evaluation on COMMANDMED_ARABIC_GOLD
PRIVATE_GOLD_CAN_SELECT_MODEL=NO
ARABIC_PARITY_SELECTION_THRESHOLD_EVIDENCE_ROLE_CONFLICT=YES
ARABIC_PARITY_THRESHOLD_FREEZE_READINESS=BLOCKED_BY_CANONICAL_EVIDENCE_ROLE_CONFLICT
```

### Public evidence candidates

#### 7.1 Cross-lingual Arabic medical evaluation

*Cross-Lingual Empirical Evaluation of Large Language Models for Arabic Medical Tasks* (2026) reports a persistent English/Arabic performance gap that worsens with task complexity and identifies Arabic tokenization/reliability limitations.

- arXiv `2602.05374`
- `https://arxiv.org/abs/2602.05374`

#### 7.2 MedArabiQ

MedArabiQ introduces an Arabic medical benchmark spanning multiple task types and documents cross-model variability in Arabic medical performance.

- arXiv `2505.03427`
- `https://arxiv.org/abs/2505.03427`

#### 7.3 Recent linguistic-equity evidence

A 2026 npj Digital Medicine analysis reports materially lower medical-exam performance in Arabic than high-resource reference languages across evaluated LLMs, supporting explicit language-specific evaluation rather than assuming multilingual parity.

- `https://www.nature.com/articles/s41746-026-03093-4`

### Discovery disposition

These sources support:

- explicit paired/cross-lingual evaluation;
- task-complexity stratification;
- avoiding inference of Arabic safety from English performance;
- language-aware reliability analysis.

Observed gaps in individual studies are not transferable as commandMed's maximum acceptable parity gap. More importantly, this public research does not resolve the canonical evidence-role conflict between Private Gold and selection-safe evidence.

```text
ARABIC_PUBLIC_DISPARITY_EVIDENCE=FOUND
ARABIC_PUBLIC_METHOD_CONTEXT=FOUND
ARABIC_TRANSFERABLE_MAXIMUM_GAP=NOT_ESTABLISHED
ARABIC_SELECTION_SAFE_PAIRED_EVIDENCE_IDENTITY=UNRESOLVED
ARABIC_CANONICAL_EVIDENCE_ROLE_CONFLICT=UNRESOLVED
ARABIC_PARITY_THRESHOLD_FREEZE_READINESS=BLOCKED_BY_CANONICAL_EVIDENCE_ROLE_CONFLICT
```

## 8. `lab_report_field_extraction_accuracy`

Canonical evidence need:

```text
REQUIRED_EVIDENCE=Deterministic field comparator against curated lab fixtures
EXACT_SELECTION_DEV_CURATED_FIXTURE_IDENTITIES=UNRESOLVED
EXACT_FIELD_SCHEMA_AND_COMPARATOR_IDENTITIES=UNRESOLVED
```

### Public evidence candidates

#### 8.1 Paper laboratory report extraction

A 2023 BMC Medical Informatics and Decision Making study evaluated extraction from 153 paper-based laboratory reports and reported overall information-extraction F1 around 0.86 for test item, result, unit and reference-range entities.

- PMID `37932733`
- DOI `10.1186/s12911-023-02346-6`
- `https://pubmed.ncbi.nlm.nih.gov/37932733/`

#### 8.2 Laboratory-report repository NLP

A clinical laboratory NLP system evaluated on 87,500 unique reports reported micro-F1 above 94% overall, while showing substantially worse performance for some rarer detected-virus labels. This illustrates why aggregate F1 can conceal clinically important subgroup/field variation.

- PMID `38875570`
- `https://pubmed.ncbi.nlm.nih.gov/38875570/`

#### 8.3 Clinical-report information extraction

Recent clinical-report extraction studies report task-specific high performance, including noninferiority to human annotators in some settings and F1 above 95% for selected structured biomarker extraction tasks.

- PMID `41286063` — `https://pubmed.ncbi.nlm.nih.gov/41286063/`
- PMID `41707099` — `https://pubmed.ncbi.nlm.nih.gov/41707099/`

### Discovery disposition

The literature demonstrates that reported F1 values vary materially with:

- report type and layout;
- field/entity definition;
- internal versus external validation;
- label prevalence/imbalance;
- document-level versus patient-level aggregation;
- exact-match versus partial extraction semantics.

Therefore published F1 values are useful performance references but are not a defensible universal commandMed minimum acceptable F1.

```text
LAB_PUBLIC_PERFORMANCE_CONTEXT=FOUND
LAB_PUBLIC_METHOD_CONTEXT=FOUND
LAB_TRANSFERABLE_MINIMUM_F1=NOT_ESTABLISHED
LAB_EXACT_COMMANDMED_FIXTURE_IDENTITY=UNRESOLVED
LAB_EXACT_COMMANDMED_COMPARATOR_IDENTITY=UNRESOLVED
LAB_THRESHOLD_FREEZE_READINESS=NOT_READY_TO_FREEZE
```

## 9. Evidence-transfer classification

The public evidence found in this pass is classified conservatively:

| Metric | Risk/context evidence | Method-design evidence | Direct commandMed numeric threshold evidence |
|---|---|---|---|
| `emergency_miss_rate` | `FOUND` | `FOUND` | `NO` |
| `medication_critical_error_rate` | `FOUND` | `FOUND` | `NO` |
| `selective_risk_at_target_coverage` | `FOUND` | `FOUND_STRONG` | `NO` |
| `citation_entailment_fidelity` | `FOUND` | `FOUND_STRONG` | `NO` |
| `arabic_clinical_parity_gap` | `FOUND` | `FOUND` | `NO` |
| `lab_report_field_extraction_accuracy` | `FOUND` | `FOUND` | `NO` |

`NO` in the final column means this bounded research pass found no source that can be responsibly copied as the commandMed numeric threshold under the current intended-use/evidence contract. It is not a claim that no future evidence can ever support a threshold.

## 10. Why benchmark or literature numbers are not copied

Examples found in public studies include:

- specific emergency under-triage/over-triage rates;
- selective-prediction operating points at specific coverage levels;
- model-specific citation-support rates;
- Arabic-versus-reference-language performance gaps;
- laboratory extraction F1 values ranging materially across tasks and datasets.

Those numbers are empirical results under other populations, tasks, model roles, comparator definitions, and evaluation designs. Copying any of them into commandMed as a hard gate would violate the repository's pre-result, intended-use-specific, evidence-bound threshold governance.

```text
EXTERNAL_STUDY_RESULT_EQUALS_COMMANDMED_THRESHOLD=NO
LITERATURE_OPERATING_POINT_EQUALS_COMMANDMED_POLICY=NO
BEST_PUBLISHED_MODEL_PERFORMANCE_EQUALS_MINIMUM_ACCEPTABLE_THRESHOLD=NO
ROUNDING_EXTERNAL_RESULT_INTO_POLICY=PROHIBITED
```

## 11. What this pass materially advances

The pass creates a public source inventory that can be used later by qualified reviewers to build metric-specific evidence packages.

Potential downstream uses, all still separately governed:

1. intended-use/harm framing;
2. comparator and adjudication design;
3. uncertainty/risk-coverage method selection;
4. clinical-audit and verifier design;
5. subgroup/language stratification;
6. external-validation and robustness expectations;
7. evidence appraisal and limitations statements.

It does not supply the missing real A2 records.

```text
A2_PUBLIC_EVIDENCE_SOURCE_INVENTORY=AVAILABLE_FOR_LATER_REVIEW
A2_REAL_THRESHOLD_RECORDS_CREATED=0
A2_REAL_REVIEW_DISPOSITIONS_CREATED=0
A2_REAL_NUMERIC_THRESHOLDS_FROZEN=0
```

## 12. Remaining A2 blockers after public evidence discovery

The canonical blockers remain materially unchanged:

```text
EXACT_IDENTITY_BOUND_SELECTION_DEV_EVIDENCE_PACKAGES=UNRESOLVED
EXACT_PRIMARY_SELECTION_MANIFEST=NOT_YET_FROZEN
EXACT_CLINICAL_REVIEW_AUTHORITY_IDENTITIES=UNRESOLVED
EXACT_STATISTICAL_REVIEW_AUTHORITY_IDENTITIES=UNRESOLVED
EXACT_REVIEWER_COUNT_OR_QUORUM=UNRESOLVED
EXACT_DISAGREEMENT_RESOLUTION_PROTOCOL=UNRESOLVED
EXACT_NUMERIC_THRESHOLDS_OR_MARGINS=NOT_YET_FROZEN
EXACT_UNCERTAINTY_METHODS_BY_METRIC=NOT_YET_FROZEN
EXACT_SAMPLE_SIZE_OR_POWER_DERIVATIONS=NOT_YET_FROZEN
CANONICAL_GOVERNANCE_ADOPTION_OF_NUMERIC_THRESHOLDS=NOT_PERFORMED
ARABIC_PARITY_CANONICAL_EVIDENCE_ROLE_CONFLICT=UNRESOLVED
```

The order dependency also remains important: actual contamination results require a frozen suite plus separate assessment authority; public evidence discovery does not authorize case construction, benchmark access, or contamination execution.

## 13. Next dependency-safe A2 work classes

Without expanding authority, later work may:

1. deepen public evidence appraisal for a specific metric/harm domain;
2. bind exact publication/revision identities and limitations into draft evidence-package metadata;
3. identify candidate statistical methods without selecting numeric inputs post hoc;
4. prepare review templates for qualified clinical and statistical reviewers without appointing or impersonating them;
5. document the unresolved Arabic evidence-role conflict for a separate governance decision.

The following remain outside current authority:

- inventing or freezing numeric thresholds;
- claiming qualified clinical/statistical review without actual reviewers;
- using candidate tournament results to calibrate thresholds;
- creating/using benchmark or selection-suite payloads;
- generating a selection suite through a provider;
- contamination execution;
- model/device execution;
- conversion/training/spend.

## 14. Research-pass result

```text
A2_PUBLIC_EVIDENCE_DISCOVERY_RESULT=METHOD_AND_RISK_CONTEXT_FOUND_NO_TRANSFERABLE_NUMERIC_POLICY
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
A2_STATE=INCOMPLETE_REAL_EVIDENCE_AND_REVIEW_REQUIRED
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 15. Non-events

No benchmark, selection-suite, Private Gold, PHI/restricted, model-weight, GGUF, credential, device, payment, or provider payload was accessed. No model, benchmark, contamination, conversion, quantization, device, tournament, or training execution occurred. All external work in this packet was read-only public literature/governance research.