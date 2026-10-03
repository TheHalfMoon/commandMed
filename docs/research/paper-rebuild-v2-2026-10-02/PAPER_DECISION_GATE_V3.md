# PAPER_DECISION_GATE_V3

Status: PRIMARY_THESIS_SELECTED_CONDITIONALLY; SCIENTIFIC_FREEZE_OPEN; EXECUTION_NOT_AUTHORIZED.

## Decision

PRIMARY_PAPER_V3 = **Meaning Before Labels: Contract-Equivariant and Calibrated Medical Decisions from Foundation Models**.

SYSTEM / METHOD CANDIDATE = **CommandMed Contract / Contract-Regularized Decision Interface (CRDI)**.

SECONDARY_METHOD_STUDY = T5, matched-supervision readout and capability-interference analysis.

SECONDARY_EVIDENCE_STUDY = T7, calibration transport under medical source failures.

OPTIONAL_FOLLOW_UP = T3, semantic encoder replacement only if later resource evidence justifies it.

HCF_STATUS = DEFERRED_UNPROVEN_FUTURE_RESEARCH.

This gate replaces the V2 paper-selection preference prospectively. It does not delete or invalidate V1/V2 evidence.
## Heuristic ranking

The eleven criteria are the same as V2 and remain ordinal planning judgments, not acceptance probabilities.

| Criterion | T9 score |
|---|---:|
| Novelty | 4/5 |
| Importance | 5/5 |
| Falsifiability | 5/5 |
| Reproducibility | 5/5 |
| Baseline strength | 5/5 |
| Zero-cost feasibility | 4/5 |
| Meaningful negative-result value | 5/5 |
| Publication strength | 4/5 |
| Concurrent differentiation | 3/5 |
| PhD portfolio value | 5/5 |
| Artifact value | 5/5 |

EQUAL_WEIGHT_MEAN = 4.545/5. SCIENCE_PRIORITY_MEAN = 4.4/5. RESOURCE_PRIORITY_MEAN = 4.75/5.

T9 narrowly outranks T5's prior planning mean of 4.455. The difference is not statistically meaningful; selection is based on the stronger problem formulation and reviewer-resistant experimental contract.
## Why V3 is stronger

T5 asks whether a typed readout matters after supervision is matched. That remains an essential ablation, but current typed-decision literature makes a head-centric paper vulnerable to being read as a replication.

T9 instead defines a behavioral contract for machine-consumable decisions. A valid decision distribution should change when evidence meaning changes and should not change merely because candidate order, neutral identifiers, or equivalent serialization changes. This distinction is directly relevant to downstream thresholds and automation because probability instability can alter actions even when top-1 accuracy is unchanged.

The contribution is not generic permutation invariance. Prior work already addresses order bias, debiasing, permutation-aware training, permutation-equivariant architectures, and metamorphic semantic testing. T9 must show that the **joint contract of semantic equivariance + evidence responsiveness + calibration transport + retained generative competence** provides a new, useful and reproducible evaluation/methodology for medical decision models.

## Kill criteria

- A prior paper is found that already evaluates this full joint contract with substantially the same estimands and interventions.
- Contract metrics reduce to ordinary MCQ order robustness without new decision-relevant information.
- CRDI fails to improve contract behavior over strong matched baselines or improves it only by sacrificing decision quality or retained capability.
- Semantics-preserving transformations cannot be validated reliably enough for confirmatory use.
- Evidence-changing labels cannot be established without restricted/private data or unsupported clinical adjudication.
- The effect fails independent-backbone replication.

READY_FOR_SMALL_SCALE_EXPERIMENTS = NO until rights, transformation validity, dataset admission, baseline artifacts, numeric statistical freeze and truly free compute are bound.