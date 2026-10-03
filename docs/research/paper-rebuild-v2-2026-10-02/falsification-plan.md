# Falsification plan


The program is designed to reject weak stories early.

## F1 — Head novelty falsification

Fit the same-capacity post-hoc head to frozen representations and compare with candidate-logit readout. If the trained typed head's advantage disappears, attribute gains to representation/supervision rather than head novelty. Visual Jev is a direct warning against claiming the head itself as the source of accuracy [@arxiv260925845].

## F2 — Supervision confounding

Match examples, optimization budget and maintenance data across readout conditions. If decision-only adaptation helps decision metrics but harms retained language competence, report the trade-off instead of a single aggregate score.

## F3 — Backbone dependence

Replicate the decisive interaction on a second architecture family. A one-backbone effect is a model-specific result, not a general architectural principle.

## F4 — Calibration failure

A model with better accuracy but worse NLL/Brier or selective risk does not pass the decision-quality claim. Post-hoc temperature scaling is a calibration baseline, not evidence that the underlying model is intrinsically calibrated [@arxiv170604599].

## F5 — Distribution shift

Freeze a calibration map on clean development data and test prespecified shift strata separately. If reliability collapses under shift, narrow the claim [@arxiv190602530].

## F6 — Novelty killer

Before submission, rerun targeted searches for typed decisions, matched readout controls, medical capability interference, selective calibration and decision-specific adaptation. If a concurrent paper contains the same causal design and central result, downgrade novelty or pivot.

## F7 — Practical irrelevance

If effect sizes are statistically detectable but below the frozen minimum meaningful effect, the result is scientifically negative. A tiny benchmark gain is not promoted to a major contribution.
