# 4. Method

## 4.1 Contract-Regularized Decision Interface

CRDI is a candidate method whose purpose is to reduce dependence on non-semantic presentation while retaining sensitivity to evidence.

Given state representation `h_x` and candidate-rubric representations `h_cj`, a scorer produces one logit per candidate meaning. Candidate surface identifiers are not treated as semantic labels; they are external indices or randomized opaque symbols. The scorer may be a dot-product/pointer function or a capacity-matched MLP, selected only through development data.

The simplest candidate form is:

```text
s_j = <W_x h_x, W_c h_cj> / sqrt(d)
p = softmax(s)
```

A set-equivariant implementation is preferred where candidate order can otherwise leak through positional representations. The exact implementation must be compared against a simple same-capacity head so architecture complexity cannot masquerade as the contribution.
## 4.2 Contract regularization

For canonical item `z` and a validated semantics-preserving transformation `T_e(z)` with inverse candidate mapping, define a consistency term between canonical and inverse-mapped transformed distributions. Jensen-Shannon divergence is the default development candidate because it is symmetric and bounded; alternatives are ablated.

```text
L_eq = JS(p_theta(.|z) || P_pi^-1 p_theta(.|T_e(z)))
```

This objective is never applied to transformations that alter decision semantics.

## 4.3 Evidence-conditioned objective

For an adjudicated semantics-changing intervention `T_c(z)`, optimize the task's proper scoring loss against the intervention-specific target. Where the frozen task contract includes a reject/other action, that action is supervised explicitly rather than inferred from low confidence.

```text
L_shift = ProperScore(p_theta(.|T_c(z)), y_c)
```

## 4.4 Capability maintenance

If the shared language backbone is updated, a bounded maintenance objective is applied on prespecified language tasks. This is not used to inflate an aggregate score; retained competence is reported independently.

```text
L = L_decision + lambda_eq L_eq + lambda_shift L_shift + lambda_retain L_lm
```

All coefficients, transformation ratios and training schedules are development variables and must be frozen before confirmatory evaluation.