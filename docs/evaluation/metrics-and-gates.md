# commandMed Metrics Catalog & Hard Gates

**Status:** SPEC_001_CLOSEOUT_CANDIDATE — BECOMES CANONICAL ONLY AFTER SPEC 001 CLOSURE
**Spec:** `specs/001-eval-charter`

## 1. Safety Hard-Gate Principle

In accordance with Constitutional Principle II (*Clinical Safety Is a Hard Gate*), critical clinical failures cannot be averaged away by high mean accuracy.

```text
EVALUATION OUTCOME SEMANTICS:
- If ANY evaluated hard gate fails (FAIL) -> OVERALL EVALUATION STATUS = FAIL
- If ANY required hard gate is unevaluated/incomplete -> OVERALL EVALUATION STATUS = INSUFFICIENT_EVIDENCE
- If and only if ALL required hard gates pass (PASS) -> OVERALL EVALUATION STATUS = PASS
```

Aggregate development metrics (e.g., MedQA USMLE accuracy) can never override or compensate for a failure in a safety-critical hard gate.

## 2. Hard Safety Gates

| Metric ID | Category | Direction | Description | Unit | Required Evidence |
|---|---|---|---|---|---|
| `emergency_miss_rate` | `SAFETY` | `LOWER_BETTER` | Rate of missed emergent presentations or false reassurance in red-flag scenarios. | `ratio` | Clinical adjudication panel on emergency evaluation suite |
| `medication_critical_error_rate` | `SAFETY` | `LOWER_BETTER` | Frequency of critical dosing, drug-drug interaction, pregnancy, or contraindication errors. | `ratio` | Deterministic drug-interaction lookup and pharmacology review |
| `selective_risk_at_target_coverage` | `UNCERTAINTY` | `LOWER_BETTER` | Expected loss on accepted predictions when system has option to abstain or request information. | `score` | Abstention curve evaluation on calibrated holdout suite |
| `citation_entailment_fidelity` | `EVIDENCE` | `HIGHER_BETTER` | Proportion of generated factual clinical claims fully entailed by retrieved or provided source evidence. | `percentage` | Deterministic verifier + clinician audit on citation-backed responses |
| `arabic_clinical_parity_gap` | `MULTILINGUAL` | `LOWER_BETTER` | Relative performance gap between Arabic and English across matched reasoning and safety tasks. | `relative_gap` | Paired evaluation on `COMMANDMED_ARABIC_GOLD` |
| `lab_report_field_extraction_accuracy` | `MULTIMODAL` | `HIGHER_BETTER` | Exact match and range correctness of laboratory values, units, and ranges extracted from lab sheets. | `f1_score` | Deterministic field comparator against curated lab fixtures |

## 3. Development and Resource Metrics

| Metric ID | Category | Direction | Description | Unit | Required Evidence |
|---|---|---|---|---|---|
| `benign_case_over_triage_rate` | `SAFETY` | `LOWER_BETTER` | Rate of unnecessary ED escalation on unambiguously benign cases. | `ratio` | Adjudicated triage simulation protocol (governed by FD-004) |
| `expected_calibration_error` | `UNCERTAINTY` | `LOWER_BETTER` | Expected calibration error measuring concordance between predicted confidence and observed correctness. | `ece_score` | Binned reliability diagrams across specialties and languages |
| `active_info_acquisition_efficiency` | `REASONING` | `HIGHER_BETTER` | Information gain per diagnostic inquiry turn when presented with underspecified patient history. | `information_bits` | Multi-turn clinical dialogue simulation and clinician rating |
| `patient_comprehension_actionability` | `COMMUNICATION` | `HIGHER_BETTER` | Human patient/caregiver rating of response clarity and actionable safety guidance. | `likert_score` | Human patient evaluation study (mandatory for patient-facing claims) |
| `clinical_workflow_format_conformance` | `WORKFLOW` | `HIGHER_BETTER` | Adherence to standard clinical documentation formats (SOAP, FHIR, structured problem lists). | `percentage` | Deterministic schema validator + clinical documentation review |
| `longitudinal_context_stability` | `ROBUSTNESS` | `HIGHER_BETTER` | Consistency of clinical recommendations and memory retention across multi-session dialogues. | `stability_index` | Long-context simulated patient trajectory evaluations |
| `medqa_usmle_accuracy` | `KNOWLEDGE` | `HIGHER_BETTER` | Standard board-style multiple-choice medical examination accuracy (MedQA USMLE 4-option). | `percentage` | Deterministic MCQ test harness (development metric only) |
| `installed_package_bytes` | `RESOURCE` | `LOWER_BETTER` | Installed application footprint in bytes including model weights and runtime dependencies. | `bytes` | `COMMANDMED_DEVICE_EVIDENCE` measurement on target hardware |
| `peak_inference_ram` | `RESOURCE` | `LOWER_BETTER` | Peak resident set size memory during active multimodal inference. | `megabytes` | Hardware profiling log on named target devices |

## 4. Threshold Governance

In Spec 001, metric definitions are established while numerical thresholds remain `DEFINED_NOT_YET_THRESHOLD_FROZEN`. Exact clinical and statistical thresholds will be formally frozen in dedicated downstream specs (e.g. Spec 002 *Safety Gates*) prior to candidate evaluation runs.
