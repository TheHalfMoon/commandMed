# Reliability intervention matrix protocol

Status: PROSPECTIVE DRAFT; no execution authority.

## 1. Unit of scientific inference

The core unit is an original decision item/case, not an individual prompt variant. All transformations derived from one item remain clustered under that source identity.

For intervention `i` and assurance property `j`, estimate the paired effect:

```text
Delta[i,j] = R_j(intervention_i) - R_j(base)
```

in the native metric of property `j`, with orientation declared so positive means better.

The public heatmap is a visualization. The scientific result is the table of raw paired effects, confidence intervals, multiplicity status, and meaningful-effect classification.

## 2. Effect classification

For each property `j`, freeze a scientifically meaningful margin `m_j > 0` before confirmatory access.

- `IMPROVE`: lower confidence bound for `Delta[i,j]` exceeds `m_j`.
- `HARM`: upper confidence bound is below `-m_j`.
- `EQUIVALENT`: the entire confidence interval lies inside `[-m_j, +m_j]` under a valid equivalence design.
- `INCONCLUSIVE`: none of the above.

Absence of statistical significance is never labeled equivalence.
## 3. Assurance properties

Primary matrix columns:

- `P1_CANONICAL_DECISION`: NLL/Brier and accuracy on canonical items.
- `P2_CALIBRATION`: proper-score calibration diagnostics under the frozen extraction method.
- `P3_COHERENCE`: probability/logical relation residuals on linked questions.
- `P4_SEMANTIC_STABILITY`: distribution change under validated meaning-preserving transforms.
- `P5_EVIDENCE_RESPONSIVENESS`: compliance with exact direction/target relations under meaning-changing interventions.
- `P6_RULE_CONFORMANCE`: declared deterministic decision-rule compliance; clinical validity is a separate qualification.
- `P7_SELECTIVE_CONTROL`: risk together with coverage; both must be reported.
- `P8_CAPABILITY_RETENTION`: prespecified medical/nonmedical generation or reasoning tasks after model-level adaptation.

A column may be excluded from a specific task family if the construct is undefined. Missing constructs are marked `NOT_APPLICABLE`; they are never imputed as passes.

## 4. Intervention levels

Interventions are grouped by where they act so causal interpretation is not blurred:

- Level A: probability/readout post-processing;
- Level B: decision interface/readout architecture;
- Level C: model adaptation/training objective;
- Level D: deployment policy/tool composition.

Primary causal contrasts are within a declared level or factorial pair. Cross-level comparisons are system comparisons, not mechanism-isolation experiments.
## 5. Candidate confirmatory interventions

The confirmatory set must be small enough for fair tuning and complete cross-property evaluation.

**A1 — Temperature scaling.** Clean-development post-hoc calibration; expected target is probability calibration without changing base logits ordering.

**A2 — Selection-bias correction.** PriDe or a reproducible permutation-based correction where task assumptions hold; target is option/identifier stability.

**B1 — Matched typed readout.** Same base representation and supervision as an LM-logit control; target is decision-interface efficiency/quality, not assumed reliability.

**C1 — Contract regularization.** Semantics-preserving consistency objective with explicit exclusion of meaning-changing transformations; target is semantic stability.

**C2 — Contract regularization + maintenance.** Same C1 objective plus a frozen language-maintenance objective; target is stability with bounded retention loss.

**D1 — Selective act/defer policy.** Frozen threshold or error-controlled policy on the same underlying probabilities; target is selective risk at declared coverage/error constraints.

**D2 — Deterministic clinical-rule tool route.** The model extracts/selects inputs but arithmetic/rule execution is deterministic; target is exact rule conformance on rule-governed cases; clinical validity is not inferred from deterministic execution.

Coherence projection remains a secondary candidate until an exact reproducible implementation and task interface are qualified.
## 6. Selected interaction tests

Two interaction families are scientifically motivated before results:

1. `A1 x A2`: calibration correction × selection-bias correction. This tests whether improving probability calibration and presentation robustness is additive, antagonistic, or redundant.
2. `A1 x C1`: post-hoc calibration × contract-regularized training. This tests whether stability-oriented adaptation changes the calibration map enough that the effects do not compose additively.

No other pairwise interaction enters the confirmatory family unless preregistered before test access.

## 7. Fair-comparison rules

- Same source item identities across paired systems.
- Same model revision for all interventions that do not require retraining.
- Same admissible training examples for matched trained interventions.
- Tuning budgets frozen per intervention family and reported explicitly.
- Additional parameters, inference calls, latency and memory are reported rather than hidden.
- Calibration data are disjoint from confirmatory data.
- Transformation generators and semantic validators are frozen before confirmatory outputs.
- A method cannot use the confirmatory set to choose thresholds, prompts, head size, regularization, or checkpoint.

## 8. Replication

The primary matrix is developed on one small permissive backbone. The decisive interaction/trade-off must be repeated on a second independently structured open-weight family before any general cross-model claim. A 27B model is optional, not required for methodological validity.## 9. Ordered composition and interaction identifiability

Intervention composition is not assumed commutative. For an ordered joint application in which `I_b` is applied first and `I_a` second, define

```text
Gamma[a|b,j] = R_j(I_a(I_b(f))) - R_j(I_b(f)) - R_j(I_a(f)) + R_j(f).
```

This is a difference-in-differences estimand: it asks whether the effect of `I_a` changes when `I_b` is already present. If both orders are operationally meaningful, estimate both `Gamma[a|b,j]` and `Gamma[b|a,j]` and report the order gap

```text
Kappa[a,b,j] = R_j(I_a(I_b(f))) - R_j(I_b(I_a(f))).
```

A symmetric “interaction” claim is not made when only one order is meaningful. For `A1 x C1`, the natural joint procedure is C1 model adaptation followed by a fresh A1 calibration fit on the declared calibration split; the reverse order is not treated as equivalent because C1 would invalidate a previously fitted calibrator. For `A1 x A2`, both orders are tested if both implementations permit them; otherwise the joint procedure is frozen explicitly.

Only ordered or jointly defined compositions enter confirmatory interaction claims. The paper must not hide order dependence inside an ambiguous `I_ab` symbol.
