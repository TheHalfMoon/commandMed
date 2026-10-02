# Power and Margin Gate V5

Status: `RULES_FROZEN`; `NUMERIC_MARGINS_PENDING_DEVELOPMENT_ONLY_PILOT`; `CONFIRMATORY_ACCESS=NO`.

## Fixed inferential rules

- inferential unit: source medical case, never transformed prompt count;
- primary family-wise alpha: `0.05`;
- multiplicity control: Holm within the prespecified primary non-target family;
- target effects and interaction effects are reported in separate declared families;
- desired power for each primary meaningful effect: `0.90`;
- all primary effect intervals are two-sided;
- equivalence/noninferiority uses valid TOST-style logic with prespecified margins;
- failure to reject zero is never called equivalence.

The primary `RULE_ORACLE` design contains exactly `4096` source clusters if the calculator eligibility gate passes. `RISKQA_EXTERNAL` contains `350` source clusters and is secondary validation, not a substitute for the primary power target.

## Meaningful-effect margins

Every assurance property receives a native-unit smallest effect of scientific interest `m_j`. Numeric `m_j` values are not invented before any measurement data exist.

Before confirmatory identity generation, each `m_j` must be frozen from a written domain justification plus development-only repeatability evidence. The value cannot be chosen from confirmatory effects, p-values, or model rankings.
The default construction rule is:

```text
m_j = max(domain_floor_j, 2 * repeatability95_j)
```

where `repeatability95_j` is the 95th percentile absolute unchanged-base paired difference on development-only repeated runs and `domain_floor_j` is justified from the measurement meaning, literature, or operational consequence before test access. If a metric is deterministic under unchanged-base replay, the repeatability term is zero.

## Hard-gate decision rule

V5 uses relative noncompensation for intervention safety claims. For every declared hard-gate non-target property `j`, an intervention passes only if its paired confirmatory effect satisfies the frozen noninferiority requirement:

```text
Delta[i,j] >= -m_j
```

under the prespecified confidence procedure. This avoids inventing a universal absolute clinical-performance threshold for a research benchmark while still forbidding compensation by gains on other axes.

## Power failure rule

Development-only nuisance estimates may be used to simulate or analytically estimate power for the frozen estimands. If `4096` source clusters are insufficient for 90% power at the frozen margins, the study must increase the planned cluster count before confirmatory identities are generated. It may not rescue power by weakening `m_j`, alpha, or the endpoint family after viewing confirmatory outputs.

RiskQA's fixed `N=350` is accepted as a secondary external check even if underpowered for small effects; its minimum detectable effects must be reported honestly.