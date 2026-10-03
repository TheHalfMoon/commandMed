# Reviewer red-team V5

Status: internal adversarial review; intended to kill weak claims before execution.

## Major objections

1. **Novelty could collapse to “metrics disagree.”** Prior work already shows calibration, robustness, coherence, abstention and safety are distinct. The paper must identify intervention-induced cross-property effects, not merely correlations among metrics.
2. **The matrix has no literal diagonal.** Rows are interventions and columns are properties; some interventions target multiple properties. Use declared `TARGET` cells rather than calling all target effects a diagonal.
3. **Interaction order may matter.** `I_a` and `I_b` may not commute. A single `I_ab` is ambiguous unless the joint intervention is defined independently or both ordered compositions are evaluated.
4. **Policy refitting can erase or manufacture transfer.** Temperature scaling can mechanically change a fixed probability threshold. The protocol must distinguish fixed downstream policy from refit-policy estimands.
5. **Cross-level interventions are not mechanistically comparable.** A deterministic tool route and a calibration transform operate at different system loci. Cross-level rows are operational system comparisons, not isolated causal mechanism estimates.
6. **Trained interventions introduce stochastic confounding.** Adaptation effects require matched initialization/data/budget, multiple training seeds, and a declared estimator across training randomness.
7. **Construct overlap can create tautological off-diagonal effects.** Calibration, selective risk and confidence-based abstention share probability inputs. The paper must label mathematically coupled endpoints and avoid presenting mechanical coupling as surprising interference.
8. **Clinical-rule tasks can be too clean.** Exact calculators strengthen rule-conformance measurement but may overstate clinical relevance if treated as current clinical ground truth. A separate natural-language/evidence task family is required for external validity.
9. **Thresholds can be arbitrary.** Noncompensatory assurance is meaningful only if `tau_j` and `m_j` are justified before test access and sensitivity analyses are secondary.
10. **Two backbones do not establish universality.** Replication supports transport across the named model families only.
11. **Backbone size differs.** The Qwen and SmolLM candidates are not parameter matched; replication must therefore test prespecified within-family intervention effects, never interpret absolute between-family score differences as architecture or scale effects.
## Required repairs before freeze

- Replace `diagonal/off-diagonal` shorthand with `target/non-target` cells throughout the confirmatory protocol.
- Define ordered composition explicitly: `I_b∘I_a` and `I_a∘I_b`; test order sensitivity before using an additive factorial interpretation.
- For each intervention, record whether downstream thresholds/policies are held fixed or refit. Primary operational effect uses the same frozen downstream policy; a refit-policy analysis is secondary and separately labeled.
- Tag endpoint relationships as `MATHEMATICALLY_COUPLED`, `SHARED_INPUT`, or `STRUCTURALLY_DISTINCT` before results. Claims of unexpected interference should prioritize structurally distinct endpoints.
- For trained interventions, use at least a prespecified set of independent training seeds and estimate intervention effects across both source-item and training-run variability.
- Separate `RULE_ORACLE` task families from `OPEN_CLINICAL_REASONING` families; do not average them into one primary effect.
- Limit generalization language to evaluated model families, task generators and operational profiles.
- Treat independent-family replication as a within-family directional/effect replication only; forbid absolute cross-family architecture or scale comparisons.
- Predeclare an intervention cost vector (parameters, training FLOPs where measurable, inference calls, latency, memory, external tool calls) so reliability gains are not presented without resource consequences.

## Decision after red-team

V5 remains scientifically interesting only if these repairs are incorporated. Without them, the design is vulnerable to a reviewer concluding that it measures expected mathematical coupling and heterogeneous system changes rather than a new reliability phenomenon.
## Repair status — 2026-10-02

- `RESOLVED_IN_PROTOCOL`: matrix cells now use `TARGET`, `NON_TARGET`, and `NOT_APPLICABLE`; the scientific protocol no longer assumes a literal diagonal.
- `RESOLVED_IN_PROTOCOL`: ordered composition uses `Gamma[a|b,j]`; `Kappa[a,b,j]` records order dependence when both orders are meaningful.
- `RESOLVED_IN_PROTOCOL`: probability-transforming interventions use a frozen downstream policy for the primary operational contrast; refit-policy analysis is secondary.
- `RESOLVED_IN_PROTOCOL`: endpoint pairs are preregistered as `STRUCTURALLY_DISTINCT`, `SHARED_INPUT`, or `MATHEMATICALLY_COUPLED`; mechanically coupled changes cannot carry the headline novelty claim.
- `RESOLVED_IN_PROTOCOL`: learned interventions require prespecified independent training seeds and inference that acknowledges training-run variability.
- `RESOLVED_IN_PROTOCOL`: `RULE_ORACLE` and `OPEN_CLINICAL_REASONING` families are reported separately rather than averaged into one primary effect.
- `RESOLVED_IN_PROTOCOL`: intervention cost vectors report parameter, compute, inference-call, latency, memory, storage and deterministic-tool costs.
- `RESOLVED_IN_PROTOCOL`: transport language is restricted to the named evaluated model families and task distributions.
- `RESOLVED_IN_PROTOCOL`: Qwen/SmolLM replication is explicitly within-family; unequal parameter counts cannot support an architecture/scale comparison.

These repairs improve identifiability but do not promote any V5 claim. Scientific freeze remains open until the exact models, datasets, margins, thresholds, power, intervention revisions and rights are frozen.