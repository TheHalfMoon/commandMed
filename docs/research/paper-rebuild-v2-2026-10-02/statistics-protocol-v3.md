# Prospective statistical protocol v3

Status: DRAFT; numerical margins and sample sizes remain UNFROZEN.

## Primary estimands

1. Paired difference in Contract Equivariance Divergence (CED) between CRDI and the strongest matched baseline across validated E-family transformations.
2. Paired difference in decision NLL on canonical items.
3. Change in evidence responsiveness under C-family interventions, evaluated separately from E-family invariance.
4. Retained-capability change under the same adapted checkpoint.

No single estimand can compensate for failure on the others.

## CED definition

For item `i` and semantics-preserving transform `t`, inverse-map the transformed distribution to canonical candidate meanings and compute Jensen-Shannon divergence from the canonical distribution. Aggregate at item level after transformation-level summaries so items with more generated variants do not receive uncontrolled extra weight.

Report mean, median, upper quantiles, bootstrap confidence intervals, and transform-family stratification.
## Pairing and dependence

Use paired item-level comparisons. When multiple questions share a source document/case, resampling must preserve that cluster. When multiple transformations derive from one item, the item remains the primary sampling unit unless the frozen analysis specifies a hierarchical model.

Binary top-1 changes may use McNemar-style paired analysis where assumptions fit. Continuous/proper scores use paired bootstrap or a justified hierarchical alternative. Effect size and interval are primary; p-values are secondary.

## Multiplicity

Freeze one primary CRDI-versus-baseline contract contrast. Other interfaces, transformation families and intervention strata are prespecified secondary families with an explicit multiplicity procedure. Exploratory decompositions remain labeled exploratory.

## Equivalence and noninferiority

No margin will be reverse-engineered from observed confirmatory results. Meaningful margins for retained competence and canonical decision quality require development evidence and scientific/clinical justification before confirmatory access.

## Replication

The decisive effect must be reproduced on a second backbone family under the same directional estimand. One-family significance cannot support a general architecture claim.