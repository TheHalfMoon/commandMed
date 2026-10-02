# 3. Formal Problem

Let a medical decision system `f` map case `x` to a probability distribution, action, optional abstention decision and auxiliary outputs. Let the frozen assurance profile be

```text
R(f) = (R_corr, R_cal, R_coh, R_stab, R_resp, R_act, R_sel, R_ret).
```

The coordinates are deliberately non-interchangeable. Section 10 of `../formal-assurance-framework.md` gives explicit witnesses showing that several pairs do not imply one another, while the weighted-score theorem shows when a compensatory average can pass despite a zero score on one coordinate.

For a targeted intervention `I_i`, define the cross-property effect

```text
Delta[i,j] = R_j(I_i(f)) - R_j(f).
```

Intervention-property cells are preregistered as `TARGET`, `NON_TARGET`, or `NOT_APPLICABLE`. Non-target entries quantify transfer or interference. The primary object is the full matrix `Delta`, not a scalar average.

For selected intervention pairs, composition order is frozen. If `I_b` is applied first and `I_a` second, define

```text
Gamma[a|b,j] = R_j(I_a(I_b(f))) - R_j(I_b(f)) - R_j(I_a(f)) + R_j(f).
```

If both orders are operationally meaningful, also estimate `Gamma[b|a,j]` and the order gap `Kappa[a,b,j] = R_j(I_a(I_b(f))) - R_j(I_b(I_a(f)))`. An interaction is therefore an ordered or jointly defined estimand, not an assumption that interventions commute. A non-zero interaction does not by itself imply harm; direction and the property-specific meaningful margin determine interpretation.

For noncompensable coordinates with prespecified thresholds `tau_j`, define the assurance region `A_tau = {r: r_j >= tau_j for all required j}`. Global certification is an intersection-union test: a system passes only when every required component clears its threshold. This controls false certification without allowing strong coordinates to compensate for a failed hard gate.

The empirical study does not assume the assurance coordinates are statistically independent or exhaustive. It tests correlations, intervention effects and selected interactions directly.

