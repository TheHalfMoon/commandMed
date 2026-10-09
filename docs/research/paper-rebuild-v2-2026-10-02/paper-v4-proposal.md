# Paper V4 proposal — reliability is non-compensatory

Status: CANDIDATE PRIMARY THESIS; UNPROVEN; NO EXECUTION AUTHORITY.

Working title: **Reliability Is Not Scalar: A Non-Compensatory Assurance Framework for Medical Foundation Model Decisions**.

Working artifact name: **CommandMed Assurance Matrix**.

## Core question

Can medical foundation-model decision reliability be decomposed into distinct obligations that neither accuracy nor calibration nor any other single score can certify, and can these obligations be measured with mechanically verifiable medical decision transformations without private clinical data?

The intended contribution is not “another multidimensional benchmark.” Existing medical benchmarks already use many dimensions, and recent confidence work already separates calibration, coherence, robustness, stability and sensitivity. V4 must earn its value through a formal non-implication structure, deterministic/metamorphic medical oracles, non-compensatory certification, and an empirical demonstration that common interventions move different reliability axes in different directions.
## Proposed assurance vector

For a decision system `f`, report a vector rather than a single trust score:

1. **Correspondence** — correctness/proper loss against the task oracle.
2. **Calibration** — whether stated probabilities match empirical correctness at the declared level of conditioning.
3. **Coherence** — compatibility with probability/logical constraints across related questions.
4. **Semantic stability** — invariance/equivariance under validated meaning-preserving transformations.
5. **Evidence responsiveness** — appropriate movement under validated meaning-changing evidence interventions.
6. **Action validity** — whether the resulting action obeys a declared decision rule, guideline, utility or threshold when such a rule exists.
7. **Selective control** — error control under abstention/deferral together with non-vacuous coverage.
8. **Capability retention** — for shared foundation models, whether improving the decision interface materially damages prespecified language/multimodal capability.

These axes are reported separately. No weighted average may convert failure of a noncompensable axis into a pass.
## Formal contribution candidates

### Proposition family A — non-implication witnesses

Construct finite decision problems showing that important reliability properties do not imply one another. Candidate witnesses include:

- perfect accuracy with poor probability calibration;
- perfect marginal calibration with no discrimination or useful action ranking;
- perfect calibration with probability-axiom/logical incoherence;
- perfect coherence with systematically wrong beliefs;
- perfect semantic invariance from a constant predictor with zero evidence responsiveness;
- strong evidence responsiveness combined with instability to irrelevant presentation changes;
- perfect action-rule compliance with poor underlying probability estimates;
- nominal selective-risk control achieved vacuously by near-zero coverage.

The theorem set must be stated only for properties whose definitions make the construction rigorous. It must not overclaim pairwise independence where mathematical implications actually exist.
### Proposition family B — non-compensatory certification

For commonly used compensatory scalarizations such as weighted means, demonstrate explicitly that a high score does not guarantee a lower bound on every constituent reliability property. A safety-critical certification rule must therefore either retain the vector or encode hard component constraints.

This is a limited mathematical statement, not a claim that scalar summaries are never useful.

### Assurance region

For prespecified thresholds `tau_j`, define the assurance region:

```text
A_tau = { f : R_j(f) >= tau_j for every noncompensable axis j }
```

Thresholds are task-specific scientific/deployment choices, not universal constants. The research contribution is the measurable structure and separation of obligations; the paper will not invent clinically meaningful thresholds without appropriate evidence.

### Pareto analysis

When no system satisfies all thresholds, compare reliability profiles by componentwise dominance and Pareto front rather than hiding trade-offs in one headline rank.
## Mechanically verifiable medical testbed

The preferred zero-cost testbed uses public, deterministic clinical decision rules only when their definitions, thresholds and downstream use rights are qualified. The benchmark is not intended to predict patient outcomes. It tests whether a model can execute and preserve declared medical decision logic.

Candidate source families include validated risk/decision scores, public guideline decision tables, and synthetic patient states generated from their explicit variables. Prior work already shows that LLMs can fail clinical score computation and that deterministic pipelines can outperform standalone generation; those systems are baselines, not novelty.

For each admitted rule, generate paired item families with an exact transformation oracle:

- equivalent reordering/paraphrase of the same facts;
- irrelevant evidence additions that should not change the rule output;
- one-variable changes that stay within the same decision region;
- one-variable changes that cross a deterministic threshold;
- missing required variables;
- internally contradictory input;
- option/label permutation where a candidate interface is used.

Every pair carries the exact source rule, variable delta, expected score/action relation and generator hash.
## Mandatory novelty threats

V4 must explicitly compare itself with and cite work showing:

- calibration is not sufficient for coherent or semantically stable confidence;
- robustness/stability/sensitivity under language variations are distinct;
- semantic maps can recover stable application-state probabilities under rewording and altered evidence;
- non-compensatory medical evaluation already exists in application-specific frameworks;
- medical benchmark ecosystems already evaluate safety/effectiveness across many dimensions;
- conformal/selective frameworks already provide explicit action/defer error control;
- counterfactual clinical benchmarks already test sensitivity and monotonicity;
- clinical-calculator agents/pipelines already use deterministic medical rules;
- prediction-side certificates may fail to certify internal/explanatory competence.

The paper is rejected as novelty if it becomes merely a new checklist, composite score, generic robustness benchmark, calculator benchmark, or repackaging of these dimensions.