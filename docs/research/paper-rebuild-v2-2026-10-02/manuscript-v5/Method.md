# 4. Method

## 4.1 Reliability intervention matrix

Every admitted intervention is applied to the same base revision, source-item identities and frozen evaluation transformations whenever its mechanism permits. The intervention is classified by locus: post-processing, decision interface, model adaptation, or deployment policy/tool composition. Mechanism claims are limited to within-level contrasts; cross-level rows are system comparisons.

The primary matrix reports native-metric paired effects with confidence intervals and meaningful-effect classes. Every intervention-property cell is preregistered as `TARGET`, `NON_TARGET`, or `NOT_APPLICABLE`; interventions may have more than one target. A heatmap is visualization only. We preserve unfavorable and null non-target cells.

## 4.2 Candidate intervention families

A1 temperature scaling targets calibration while preserving logit ordering. A2 selection-bias correction targets option/identifier instability. B1 matched typed readout changes the decision interface under matched supervision. C1 semantic-contract regularization targets invariance only on validated meaning-preserving transformations. C2 adds capability-maintenance training. D1 selective act/defer policy targets risk at declared coverage. D2 deterministic clinical-rule routing delegates arithmetic or rule execution to an authoritative executable component.

Only implementations with exact revisions, lawful use, reproducibility and fair tuning budgets enter confirmation. Methods that cannot meet these conditions remain related-work references.

## 4.3 Medical rule oracle layer

For rule-governed tasks, the model extracts or selects declared inputs, but the reference score/action is computed by versioned deterministic logic. Threshold-crossing counterfactuals are generated from valid input domains and independently verified. The model is never treated as the oracle for its own evaluation.

## 4.4 Transformation contracts

Meaning-preserving transformations have known inverse mappings and require stability/equivariance. Meaning-changing interventions have explicit expected label, action or directional probability relations and require responsiveness. The same transformation cannot be used in both families.

## 4.5 Interactions

The confirmatory interaction set is intentionally small. Current candidates are `A1 x A2` and `A1 x C1`. Composition order is frozen. For `A1 x C1`, the natural joint procedure is C1 adaptation followed by a fresh A1 calibration fit; a calibrator fitted before C1 is not assumed valid afterward. For `A1 x A2`, both orders are evaluated when both implementations permit them; otherwise the single lawful order is declared. Additional pairs are exploratory unless preregistered before test access.

## 4.6 Policy, coupling and cost controls

For probability-transforming interventions, primary action/selective outcomes use the same frozen downstream thresholds; a refit-policy analysis is secondary. Endpoint relationships are labeled before results as `STRUCTURALLY_DISTINCT`, `SHARED_INPUT`, or `MATHEMATICALLY_COUPLED`, and mechanically coupled changes cannot carry the main novelty claim. Learned interventions use prespecified independent training seeds. Every intervention reports an explicit resource-cost vector rather than hiding extra parameters, inference calls, memory, latency or tool use.

