# 3. Formal Problem

Let `x` be the observed state/evidence and `C=(c_1,...,c_K)` an ordered presentation of candidate meanings. A decision system returns `p_theta(y | x,C)` over indices `1..K` plus an optional explicitly defined rejection action.

The order and surface identifiers of `C` are presentation choices; the semantic objects are the candidate meanings themselves. Let `T_e` be a semantics-preserving transformation with known bijection `pi_e` between transformed and canonical candidate indices. Let `P_pi` denote the corresponding permutation operator.

## 3.1 Contract equivariance

For a valid semantics-preserving transformation, the desired relation is:

```text
p_theta(. | T_e(x,C)) = P_pi p_theta(. | x,C)
```

up to stochastic/numerical tolerance fixed before confirmatory analysis. We measure deviation rather than assuming exact equality.

When `pi` is the identity, the property reduces to distributional invariance. The object of interest is the full distribution, not only the predicted class.
## 3.2 Semantic responsiveness

Let `T_c` be a semantics-changing intervention: required evidence is removed, contradictory evidence is introduced, or the valid answer set changes. There is no invariance requirement. Instead, the intervention defines a new target distribution or action under the frozen task policy.

A reliable system should distinguish `T_e` from `T_c`. Excessive invariance is itself a failure if the model ignores clinically relevant evidence changes.

## 3.3 Contract Equivariance Divergence

For canonical distribution `p_i` and transformed distribution `q_it`, inverse-map `q_it` to canonical candidate meanings and define:

```text
CED(i,t) = JS(p_i || P_pi^{-1} q_it)
```

where `JS` is Jensen-Shannon divergence. CED is bounded and symmetric, but no clinical meaning is assigned to an arbitrary numerical threshold without development evidence.

We also report argmax flips, total-variation distance and action-threshold flips as secondary diagnostics to test whether CED adds information beyond existing measures.

## 3.4 Evidence responsiveness and transport

For C-family intervention `c`, compare proper scoring, rejection probability and selective-risk behavior with the clean condition. A calibration map or action threshold fitted on clean development data is frozen before testing transport to intervention strata. The resulting transport gap is an empirical property, not a distribution-free guarantee.