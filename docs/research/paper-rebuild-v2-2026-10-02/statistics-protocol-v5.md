# Statistics protocol V5

Status: partially bound freeze candidate; execution remains unauthorized.

## Primary estimands

For intervention `i` and assurance property `j`, the primary estimand is the paired source-item effect `Delta[i,j] = R_j(I_i(f)) - R_j(f)` in the native metric of property `j`, oriented so positive is better. For preregistered ordered intervention pairs, `Gamma[a|b,j] = R_j(I_a(I_b(f))) - R_j(I_b(f)) - R_j(I_a(f)) + R_j(f)`. If both orders are meaningful, estimate both ordered interactions and `Kappa[a,b,j]` as the order gap.

The source medical case/item is the inferential cluster. Prompt variants, candidate permutations, paraphrases and evidence perturbations derived from one source never count as independent observations.

## Policy and endpoint coupling estimands

For interventions that transform probabilities, the primary operational contrast holds downstream action and abstention thresholds fixed at their preregistered values. A refit-policy contrast may be reported secondarily, but it is a different estimand and cannot replace the fixed-policy result.

Before confirmatory access, each pair of assurance endpoints is tagged `STRUCTURALLY_DISTINCT`, `SHARED_INPUT`, or `MATHEMATICALLY_COUPLED`. Mechanical changes among coupled endpoints are reported but cannot by themselves support the headline interference claim; the strongest claim requires a material effect on a structurally distinct or clinically consequential hard-gate property.

For learned interventions, training randomness is part of the design. The independent training seeds are fixed at `11`, `29`, and `47`. Inference combines source-item clustering with between-training-run variability rather than treating checkpoints as fixed when they are stochastic products of training.

## Primary confirmatory family

The confirmatory family contains: target-property effects for each admitted intervention; non-target effects on declared hard-gate properties; the two preregistered interaction families; and the aggregate-vs-noncompensatory decision reversal analysis. Exploratory cells remain visibly labeled and cannot promote a primary claim.

## Effect decisions

Each property receives a prespecified meaningful margin `m_j`. A paired effect is classified as `IMPROVE`, `HARM`, `EQUIVALENT`, or `INCONCLUSIVE` using confidence intervals and valid equivalence procedures. Failure to reject zero is never evidence of equivalence.

For hard-gate non-target properties, relative noninferiority takes precedence over a global mean: every required cell must satisfy `Delta[i,j] >= -m_j` under the frozen confidence procedure. The global assurance certificate is the intersection of these hard-gate requirements; gains elsewhere cannot compensate for a failed cell.

## Multiplicity and replication

Primary non-target claims use family-wise alpha `0.05` with Holm control in the prespecified family. Interaction tests form a separate family. The independent-backbone replication is confirmatory only for effects nominated before seeing the replication data; it is not another search stage.
## Interval and resampling rules

Use paired or cluster-preserving bootstrap intervals only when the resampling unit matches the source-item cluster and the statistic is bootstrap-appropriate. Use exact/binomial or score intervals for simple rates when their assumptions fit. For repeated stochastic generations, summarize within source item before between-item inference unless the model explicitly treats run as a crossed random factor.

All seeds, decoding settings, prompt templates, evaluators and transformation generators are frozen before confirmatory access. Model-as-judge outputs cannot be the sole basis for a safety-critical primary endpoint; where judgment is unavoidable, agreement with a qualified human rubric must be established on an independent calibration sample.

## Power and sample-size gate

The desired power is `0.90`. The planned primary RULE_ORACLE family contains `4096` source clusters. No confirmatory run begins until every primary estimand has a meaningful margin, expected variance or conservative variance bound, verified power at the frozen margin, and a missing-data rule. Pilot data may estimate nuisance parameters but may not be reused as confirmatory observations.

The paper must report minimum detectable effects rather than claiming that a null result proves modularity when the study is underpowered. Equivalence claims require margins justified before confirmatory access.

## Missingness and failures

Invalid outputs, parser failures, tool errors and abstentions are outcomes, not silently dropped records. The protocol declares per-axis handling in advance. Infrastructure failures unrelated to model behavior may trigger a documented rerun only under a prespecified retry rule.

## Reporting

Report raw effects, confidence intervals, corrected p-values where used, standardized effect sizes only as secondary summaries, per-axis thresholds, coverage for selective policies, and the complete intervention matrix including unfavorable cells. No single composite score is a primary endpoint.

