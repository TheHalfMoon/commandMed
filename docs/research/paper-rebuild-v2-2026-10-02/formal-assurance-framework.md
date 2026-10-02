# Formal assurance framework

Status: prospective theory candidate; definitions and counterexamples must be independently checked before publication.

## 1. Finite decision setting

Let `X` be a finite set of decision instances and `Y` a finite outcome set. A probabilistic decision system returns `p_x in Delta(Y)` for each `x in X`. Some studies additionally expose related propositions, semantics-preserving transformations, semantics-changing interventions, a deterministic action policy, and an abstention mechanism.

An assurance profile is deliberately vector-valued:

```text
R(f) = (R_corr, R_cal, R_coh, R_stab, R_resp, R_act, R_sel, R_ret)
```

Every coordinate is normalized only for comparison inside a frozen study. The vector does not assert that the coordinates are interchangeable.

## 2. Correspondence

For a classification task with true label `y_x`, define top-1 correspondence as `1 - E[1{argmax p_x != y_x}]`. Proper-score correspondence is reported separately using log loss or Brier score.

Perfect top-1 correspondence means every argmax is correct; it does not constrain the numerical probability attached to the correct class beyond being maximal.
## 3. Calibration

For binary events with predicted probability `P` and outcome `Y`, perfect population calibration means:

```text
E[Y | P = q] = q
```

for every prediction value `q` with positive probability. Multiclass calibration requires an explicitly chosen definition; the paper must not treat ECE as a universal substitute for calibration.

## 4. Coherence

Suppose the system is queried about logically related events in a finite event algebra. Instancewise coherence requires the returned probabilities to obey the probability axioms for those events. For example, for event `A` and its complement:

```text
p_x(A) + p_x(not A) = 1
```

Other relations include non-negativity, normalization, and finite additivity for declared disjoint events. Coherence is a constraint on relationships among beliefs, not their empirical truth.

## 5. Semantic stability

Let `G_eq` be a declared set of semantics-preserving transformations with a known mapping `M_g` back to the canonical output space. Perfect stability requires:

```text
M_g p_{g(x)} = p_x
```

for every admitted `g in G_eq`. Approximate stability is measured with a frozen distribution distance.
## 6. Evidence responsiveness

Let `G_change` contain interventions whose semantics are declared to change. Each intervention has a frozen target relation: a new label, a deterministic action change, a direction of probability movement, or a new admissible answer set. Responsiveness measures compliance with that relation.

This definition intentionally does not reward arbitrary sensitivity. A change must be tied to a validated semantic intervention.

## 7. Action validity

Given a declared deterministic policy `a*(x)` derived from a qualified rule or decision threshold, action validity is the probability that the model-induced action equals `a*(x)` on the admitted test distribution.

A model may execute the correct action while its probability estimates are poor. Conversely, a calibrated probabilistic model may be paired with an incorrect downstream policy. These are separate system properties.

## 8. Selective control

For an acceptance indicator `S(x)` and loss `L`, selective risk is:

```text
R_sel = E[L | S=1]
```

and coverage is `Pr(S=1)`. A selective claim must report both. A zero-error statement with zero or negligible coverage is not useful assurance.

## 9. Capability retention

For a foundation model adapted for decision behavior, retention is evaluated on a prespecified, separate set of capabilities. It is not mathematically intrinsic to the decision task; it is a system-level deployment constraint.
# 10. Explicit non-implication witnesses

The examples below establish only the named non-implications under the definitions above.

### Witness 1 — perfect top-1 correspondence does not imply calibration

Consider a binary task in which all observed labels are `Y=1`. Predict `p(Y=1)=0.51` for every item. The argmax is correct on every item, so top-1 correspondence is perfect. But among predictions with value `0.51`, the empirical event frequency is `1`, not `0.51`; perfect calibration fails.

### Witness 2 — perfect calibration does not imply useful correspondence/discrimination

Let half of the items have `Y=1` and half `Y=0`. Predict `p(Y=1)=0.5` for every item. The predictor is perfectly calibrated at its only prediction value because the empirical event frequency is `0.5`. Yet it provides no discrimination, and any deterministic tie-breaking classifier has only chance-level accuracy on a balanced construction.

These examples show that correctness and calibration answer different questions even before language-model complications are introduced.
### Witness 3 — marginal calibration does not imply instancewise probability coherence

Use four contexts with truth values for event `A` equal to `[1,1,0,0]`; truth for `not A` is `[0,0,1,1]`.

For `A`, predict `[1, 1/3, 1/3, 1/3]`. The `1` bin contains one positive, and the `1/3` bin contains one positive among three items: this forecast is calibrated.

For `not A`, predict `[2/3, 0, 2/3, 2/3]`. The `0` bin contains one negative, and the `2/3` bin contains two positives among three items: this forecast is also calibrated.

Yet on the first item `p(A)+p(not A)=5/3`, and on the second it equals `1/3`. Both marginal forecasts are calibrated while the paired beliefs violate complement coherence.

### Witness 4 — coherence does not imply correctness

On contexts where `A` is always true, predict `p(A)=0.1` and `p(not A)=0.9`. The beliefs satisfy complement coherence exactly but are systematically wrong and yield the wrong top-1 event.
### Witness 5 — semantic stability does not imply evidence responsiveness

Let a system output the same fixed distribution for every input. It is perfectly invariant to every semantics-preserving transformation, so its stability score can be maximal. If a validated evidence intervention changes the correct state or required action, the same constant distribution does not respond at all. Stability alone therefore cannot certify evidence use.

### Witness 6 — evidence responsiveness does not imply semantic stability

Consider two evidence states `x0` and `x1` for which the true binary state changes from `0` to `1`. Under canonical presentation, predict `p(Y=1)=0.1` on `x0` and `0.9` on `x1`. Under a semantically equivalent presentation, predict `0.4` and `0.6`. Both presentations move in the correct direction after the evidence change, so a directional responsiveness criterion can be satisfied, while the probability distribution remains materially presentation-dependent.

### Witness 7 — correct threshold action does not imply probability accuracy

Suppose the qualified action policy is `act` whenever true risk exceeds `0.5`, and every test instance has true risk `0.9`. A model predicting `0.51` for all items triggers the correct action on every item while remaining badly miscalibrated as a risk estimator.

### Witness 8 — error among accepted cases without coverage can be vacuous

A policy that abstains on every item makes no accepted-case errors. Therefore any selective reliability report that omits coverage can reward a useless system. This is why the assurance axis records the risk-coverage pair rather than error alone.
# 11. Weighted-average certification theorem

Let a normalized assurance vector be `r in [0,1]^m`. Let a compensatory score be

```text
S(r) = sum_j w_j r_j
```

with positive weights summing to one. Suppose a system passes when `S(r) >= tau`.

For any coordinate `k`, the tight lower bound implied by this pass rule is:

```text
r_k >= max(0, (tau - (1 - w_k)) / w_k).
```

**Proof.** Since every other coordinate is at most one,

```text
S(r) <= w_k r_k + (1 - w_k).
```

Thus `S(r) >= tau` requires `w_k r_k >= tau-(1-w_k)`. Non-negativity yields the bound. Tightness follows by setting all other coordinates to one and choosing `r_k` at the bound.

**Corollary.** If `tau <= 1-w_k`, a system can have `r_k=0` and still pass by scoring perfectly on every other coordinate. A weighted mean therefore provides no positive floor for axis `k` in that regime.
# 12. Non-compensatory assurance region

For task-specific thresholds `tau=(tau_1,...,tau_m)`, define

```text
A_tau = { r in [0,1]^m : r_j >= tau_j for every noncompensable coordinate j }.
```

Membership in `A_tau` is a conjunction, not an average. A system that exceeds seven thresholds but fails one designated hard gate remains outside the region.

The coordinatewise partial order `r >= s` means `r_j >= s_j` for every axis. Under this order, `[0,1]^m` is a product lattice with meet and join given by coordinatewise minimum and maximum. This mathematical fact is useful for reasoning about dominance, but the paper should call the operational object an **assurance vector/region**, not market “lattice” as the novelty.

If neither of two systems dominates the other, they occupy different trade-off points. Such incomparable systems should be shown as a Pareto set or full profile rather than forced into an arbitrary total ranking.

# 13. Scientific boundary

The counterexamples above establish separations under explicit definitions. They do not prove that the empirical coordinates will be statistically independent, that every pair of assurance notions is logically independent, or that the proposed vector is complete. The empirical paper must test correlations and intervention effects rather than assuming orthogonality.
# 14. Global non-compensatory certification as an intersection-union test

Suppose every high-is-good assurance coordinate has a prespecified threshold `tau_j`. Let

```text
H0_j: mu_j <= tau_j
H1_j: mu_j > tau_j
```

and define the global hypotheses

```text
H0: at least one required assurance coordinate fails its threshold
H1: every required assurance coordinate exceeds its threshold.
```

This is an intersection-union testing problem: `H0 = union_j H0_j` and `H1 = intersection_j H1_j`.

A global certificate is issued only when **every** component null is rejected. If each component test has size at most `alpha`, the global test also has size at most `alpha` without a Bonferroni correction.

**Proof.** Under the global null, at least one component null, say `H0_k`, is true. The event that all component nulls are rejected is a subset of the event that `H0_k` is rejected. Its probability is therefore at most `alpha`.

This controls false certification. It does not remove the need to predeclare thresholds, estimands, units, test procedures, or distributional assumptions for each component.
# 15. Simultaneous descriptive lower bounds

For visualization and post-test interpretation, simultaneous lower confidence bounds are still useful. If independent evaluation units yield bounded scores `Z_ij in [0,1]`, with `n_j` units for axis `j`, Hoeffding plus a union bound gives:

```text
LCB_j = mean(Z_j) - sqrt(log(m/delta) / (2 n_j)).
```

With probability at least `1-delta`, all population means exceed their corresponding `LCB_j` simultaneously. Cross-axis dependence within the same evaluation unit does not invalidate the union bound; independence/appropriate clustering across evaluation units remains an assumption.

These bounds are conservative and are not proposed as a new concentration result. The final analysis may replace them with prespecified tighter valid intervals when assumptions justify doing so.

For a benchmark generator rather than a clinical sampling frame, any confidence statement refers to the declared generator/test distribution. It must not be presented as a population-level clinical guarantee.

## Assurance margin

For descriptive purposes define the bottleneck margin:

```text
M = min_j (LCB_j - tau_j).
```

`M >= 0` means every simultaneous lower bound clears its threshold. Unlike a weighted average, one deficient hard-gate coordinate cannot be offset by stronger performance elsewhere. The individual coordinates remain the primary report.