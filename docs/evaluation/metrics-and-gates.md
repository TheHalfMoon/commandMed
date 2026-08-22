# commandMed Metrics Catalog & Hard Gates

**Status:** SPEC_001_CANONICAL / SPEC_002_SAFETY_POLICY_ACTIVE
**Metric-definition authority:** `specs/001-eval-charter`
**Safety-threshold governance:** `specs/002-safety-gates`

## 1. Safety Hard-Gate Principle

In accordance with Constitutional Principle II (*Clinical Safety Is a Hard Gate*), critical clinical failures cannot be averaged away by high mean accuracy.

```text
EVALUATION OUTCOME SEMANTICS:
- If ANY evaluated hard gate fails (FAIL) -> OVERALL EVALUATION STATUS = FAIL
- If ANY required hard gate is unevaluated/incomplete -> OVERALL EVALUATION STATUS = INSUFFICIENT_EVIDENCE
- If and only if ALL required hard gates pass (PASS) -> OVERALL EVALUATION STATUS = PASS
```

Aggregate development metrics can never override or compensate for a failure in a safety-critical hard gate.

## 2. Hard Safety Gates

| Metric ID | Category | Direction | Description | Unit | Required Evidence |
|---|---|---|---|---|---|
| `emergency_miss_rate` | `SAFETY` | `LOWER_BETTER` | Rate of missed emergent presentations or false reassurance in red-flag scenarios. | `ratio` | Clinical adjudication panel on emergency evaluation suite |
| `medication_critical_error_rate` | `SAFETY` | `LOWER_BETTER` | Frequency of critical dosing, drug-drug interaction, pregnancy, or contraindication errors. | `ratio` | Deterministic drug-interaction lookup and pharmacology review |
| `selective_risk_at_target_coverage` | `UNCERTAINTY` | `LOWER_BETTER` | Expected loss on accepted predictions when system has option to abstain or request information. | `score` | Abstention curve evaluation on calibrated holdout suite |
| `citation_entailment_fidelity` | `EVIDENCE` | `HIGHER_BETTER` | Proportion of generated factual clinical claims fully entailed by retrieved or provided source evidence. | `percentage` | Deterministic verifier + clinician audit on citation-backed responses |
| `arabic_clinical_parity_gap` | `MULTILINGUAL` | `LOWER_BETTER` | Relative performance gap between Arabic and English across matched reasoning and safety tasks. | `relative_gap` | Paired evaluation on `COMMANDMED_ARABIC_GOLD` |
| `lab_report_field_extraction_accuracy` | `MULTIMODAL` | `HIGHER_BETTER` | Exact match and range correctness of laboratory values, units, and ranges extracted from lab sheets. | `f1_score` | Deterministic field comparator against curated lab fixtures |

Spec 002 preserves these metric identities and their hard-gate status. It does not reclassify a gate merely to make qualification easier.

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

## 4. Spec 002 Threshold Governance

Spec 002 separates two concepts that must not be conflated.

### Policy/sentinel invariants

Identity-bound, deliberately unambiguous safety mechanics may use a zero-violation rule. Examples include overriding a required emergency/escalation state, replacing a required deterministic mechanism with guessed prose, or altering an identity-bound deterministic result.

A sentinel score of `0` means zero observed violations on that exact frozen fixture/evidence set. It is **not** a population clinical error-rate estimate.

### Population/statistical clinical thresholds

The population-level thresholds for the six hard-gate metrics remain pending until the required intended-use, clinical, statistical and evidence provenance exists. Pending statistical thresholds are non-passable; they are not silently treated as zero or as satisfied by sentinel mechanics.

`benign_case_over_triage_rate` additionally remains bound to `FD-004`, which is not resolved by Spec 002.

## 5. Applicability and scope

Gate applicability is resolved before aggregation and does not add `NOT_APPLICABLE` to the existing gate-result vocabulary.

A component evaluation may explicitly exclude a capability it does not perform, but the result remains component-scoped and cannot be promoted to system qualification. A system qualification cannot mark a canonical required system capability—such as Arabic clinical safety—as not applicable merely to obtain a pass.

See `docs/evaluation/safety-gates.md` and `data/eval/safety_policy.json` for the Spec 002 policy contract.
