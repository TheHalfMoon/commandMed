# Paper V5 proposal — cross-property reliability interference

Status: CANDIDATE PRIMARY THESIS; UNPROVEN; NO EXECUTION AUTHORITY.

Working title: **When Reliability Fixes Collide: Cross-Property Interference in Medical Foundation Model Decisions**.

Alternative title: **Reliability Does Not Automatically Compose: A Controlled Intervention Study of Medical Foundation Model Decisions**.

Working program name: **CommandMed Assurance**.

## Core research question

When an intervention is designed to improve one reliability property of a medical foundation-model decision system, what happens to the other reliability properties?

The paper tests whether calibration, semantic stability, coherence, evidence responsiveness, selective behavior, deterministic rule conformance, and retained language capability behave as mutually reinforcing objectives, independent properties, or competing objectives under controlled interventions.

This is not a claim that reliability never composes. `DOES_NOT_AUTOMATICALLY_COMPOSE` is the falsifiable hypothesis.
## Reliability intervention matrix

Let `R_j(f)` be the frozen score for assurance property `j` and let `I_i` be a declared intervention targeting one or more properties. Define:

```text
Delta[i,j] = R_j(I_i(f)) - R_j(f)
```

Rows are interventions; columns are assurance properties. Each cell is declared before analysis as `TARGET`, `NON_TARGET`, or `NOT_APPLICABLE`. Target cells capture intended effects; non-target cells capture transfer, neutrality, or interference.

The matrix is estimated with paired items and confidence intervals. It is never collapsed into one mean for the primary analysis.

Candidate interventions include:

- post-hoc temperature scaling / multicalibration-style confidence correction;
- option-order or selection-bias correction such as PriDe or permutation-aware consistency;
- coherence projection or coherence-constrained post-processing where reproducible;
- selective answer/defer policy;
- evidence-sufficiency gating;
- typed decision readout versus restricted LM logits under matched supervision;
- CRDI-style semantic contract regularization;
- deterministic clinical-rule tool routing as a system-level control.

Only interventions with exact lawful artifacts and comparable task semantics enter the confirmatory matrix.
## Cross-intervention interaction

For selected intervention pairs `I_a` and `I_b`, composition order is frozen rather than assumed commutative. If `I_b` is applied first and `I_a` second, define:

```text
Gamma[a|b,j] = R_j(I_a(I_b(f))) - R_j(I_b(f)) - R_j(I_a(f)) + R_j(f)
```

`Gamma=0` is an additive-effects reference, not an assumption. If both orders are operationally meaningful, estimate both ordered interactions and the order gap `Kappa[a,b,j]`. A symmetric interaction claim is not made when only one order is scientifically meaningful.

Only a small preregistered subset of scientifically motivated pairs should be tested to avoid a combinatorial search.

## Primary hypotheses

H1. At least one targeted intervention produces a non-negligible non-target change on another assurance property.

H2. At least one intervention that improves its target property fails to improve, or materially harms, another noncompensable property.

H3. Model rankings or pass/fail conclusions differ between compensatory aggregate scoring and the non-compensatory assurance test.

H4. At least one major cross-property effect replicates directionally across two independently structured backbone families.

H5. A selected pair of interventions exhibits a non-additive interaction on at least one preregistered assurance property.

Each hypothesis can be rejected. No cross-property trade-off is assumed before execution.
## Why this is stronger than V4 alone

V4 establishes that a weighted average can hide failure and supplies explicit non-implication witnesses. Those are useful foundations but are not enough for a major paper because multidimensional and non-compensatory evaluation already exists in medicine.

V5 asks an empirical scientific question that can change model-development practice: **do reliability interventions transfer across properties, remain isolated, or interfere?**

A positive result would warn against optimizing calibration, robustness, abstention, or coherence in isolation. A null result would be equally informative if carefully powered: it would support modular reliability engineering for the studied intervention/task families.

The contribution bar is therefore not “we created more metrics.” It is a controlled map from reliability interventions to cross-property consequences, grounded by a formal non-compensatory assurance analysis and exact medical decision oracles.

## Required negative controls

- sham transformation with no semantic change;
- calibration-only intervention expected not to modify argmax decisions;
- randomized intervention assignment/configuration where feasible;
- unchanged-base repeated-run control to estimate stochastic jitter;
- capacity/tuning-budget matched controls for trained interventions;
- no-tool and deterministic-tool controls for clinical-rule tasks.

Without these controls, non-target changes cannot be attributed to the intended intervention.
