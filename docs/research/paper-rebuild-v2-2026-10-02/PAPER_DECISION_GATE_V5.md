# PAPER_DECISION_GATE_V5

Status: `PRIMARY_PAPER_SELECTED_CONDITIONALLY`; `SCIENTIFIC_FREEZE_OPEN`; `EXECUTION_NOT_AUTHORIZED`.

## Current best primary paper

**When Reliability Fixes Collide: Cross-Property Interference in Medical Foundation Model Decisions**

Primary scientific object: the **reliability intervention matrix** — paired changes across independently reported assurance properties after targeted reliability interventions.

Formal foundation: `formal-assurance-framework.md`.

Medical oracle substrate: qualified deterministic rules / guideline decision logic applied to synthetic or explicitly licensed inputs, plus separate public medical QA/evidence tasks where rights permit.

V4 survives as the assurance-theory layer. V3 survives as one intervention family and diagnostic. T5 survives as the matched readout/supervision ablation. HCF remains a separate, later model-architecture research program rather than being forced into Paper V5.
## Heuristic planning scores

These are ordinal research-prioritization judgments, not acceptance probabilities or scientific measurements.

| Criterion | V5 |
|---|---:|
| Novelty | 4/5 conditional |
| Importance | 5/5 |
| Falsifiability | 5/5 |
| Reproducibility | 5/5 |
| Baseline strength | 5/5 |
| Zero-cost feasibility | 4/5 conditional |
| Meaningful negative-result value | 5/5 |
| Publication strength | 4/5 conditional |
| Concurrent differentiation | 4/5 conditional |
| PhD portfolio value | 5/5 |
| Artifact value | 5/5 |

Equal-weight planning mean = `4.636/5`.

This exceeds the previous V3/T5 planning rankings, but the numerical difference is not meaningful. V5 is selected because its scientific question is broader than a specific head while remaining experimentally identifiable.
## Major-contribution gate

V5 does **not** pass the requested major-paper bar merely by producing a heatmap.

At least one of the following must emerge under the frozen confirmatory design:

1. a replicated target-improvement / hard-gate-degradation effect large enough to change how reliability interventions should be selected;
2. a replicated non-additive interaction showing that individually favorable interventions cannot be safely composed by assumption;
3. a strong equivalence/null result demonstrating modularity for a meaningful intervention family under prespecified margins;
4. a non-compensatory assurance result that reverses a conclusion supported by a conventional aggregate score and is traceable to a consequential failure mode;
5. a new intervention derived from the observed matrix that moves the Pareto frontier without violating hard gates, followed by independent confirmation.

A collection of small statistically significant non-target effects is insufficient.

## Kill criteria

- prior work is found with substantially the same cross-intervention/cross-property medical design;
- intervention attribution is confounded by unequal supervision, capacity, compute, or evaluation access;
- reliability axes cannot be measured with adequate construct validity;
- all non-target effects are negligible under meaningful frozen margins;
- effects fail independent-family replication;
- result depends on private/restricted data or paid compute that violates program constraints.

## 2026-10-02 refresh decision

A new adversarial search against MedHELM, recent medical trustworthiness surveys, MedQAbstain, abstention frameworks, ProMedical and deterministic clinical-tool studies did not identify the full V5 controlled intervention-by-assurance design. However, it substantially narrows the permissible novelty language.

The paper may **not** claim novelty for multidimensional medical evaluation, calibration-plus-robustness analysis, medical abstention, multi-criteria medical alignment, Pareto reliability profiling, or deterministic clinical calculator use. Those are established prior art.

The surviving primary thesis is narrower: whether targeted reliability interventions exhibit material cross-property transfer/interference or non-additive composition under matched medical decision experiments, and whether those effects change conclusions under a noncompensatory assurance rule.

Decision: `KEEP_V5_AS_PRIMARY_CONDITIONAL`; `NOVELTY_NOT_CLEARED_FOR_FIRST_CLAIMS`; `SCIENTIFIC_FREEZE_OPEN`; `EXECUTION_NOT_AUTHORIZED`.


## 2026-10-02 pre-freeze binding pass

The V5 paper remains primary and conditional. The study is now narrower and more reproducible, but not confirmatory-frozen.

Bound in this pass:
- exact Qwen3.5-0.8B-Base primary revision and SmolLM2-1.7B independent-family revision;
- public-domain AgentMD/RiskCalcs/RiskQA lineage at exact repository/blob identities;
- deterministic `RULE_ORACLE` source design with 64 calculators, each exposing at least `1024` static candidate states; `4,096` development and `4,096` calibration cases are fixed before model work, while the planned `4,096` confirmatory and `4,096` reserve cases are selected only after the implementation freeze using future public randomness;
- deterministic static RiskCalcs selectors, including a hardened numeric/Boolean threshold rule-oracle audit with `82` eligible candidates across `15` first-listed source specialty strata, each exposing at least `1024` prospective input states, and a deterministic 64-entry manifest;
- family-wise alpha `0.05`, Holm control, desired power `0.90`, and learned-intervention seeds `11/29/47`;
- relative hard-gate noninferiority `Delta[i,j] >= -m_j` rather than an arbitrary universal clinical threshold.

Still unresolved: B1/C1/C2 learned model-integration qualification, numeric native-unit margins from development-only repeatability/pilot evidence, final power at those margins, final clean implementation bindings, and confirmatory membership materialization after the clean freeze event plus future public randomness. Current-care clinical-validity interpretation remains out of scope unless separately qualified; it is not required for the primary rule-conformance construct. The narrow SQuAD retention control and quarantine mechanics are now admitted/bound; neither closes the remaining empirical gates.

Decision remains: `KEEP_V5_AS_PRIMARY_CONDITIONAL`; `SCIENTIFIC_FREEZE_OPEN`; `EXECUTION_NOT_AUTHORIZED`.
