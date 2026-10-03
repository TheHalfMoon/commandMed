# Paper V3 proposal — CommandMed Contract

Status: CANDIDATE PRIMARY THESIS; UNPROVEN; NO EXECUTION AUTHORITY.

Working title: **Meaning Before Labels: Contract-Equivariant and Calibrated Medical Decisions from Foundation Models**.

Working system name: **CommandMed Contract**.

## Core research question

Can a machine-consumable medical decision interface preserve the meaning of its probability distribution under semantics-preserving interface transformations, while responding appropriately to evidence-altering interventions and preserving the underlying model's useful language capability?

This proposal does not claim that typed heads, permutation invariance, calibration, abstention, or metamorphic testing are individually novel. Each has substantial prior art. The candidate contribution is a single falsifiable framework that separates two requirements that are often conflated:

1. **contract equivariance** when the meaning of the decision problem is unchanged; and
2. **calibration responsiveness** when the available evidence or valid answer set genuinely changes.

The paper succeeds only if this separation produces a nontrivial empirical or theoretical result beyond existing selection-bias, typed-decision, and calibration work.
## Formal decision contract

Let `x` denote state/evidence and let `C = {c_1, ..., c_K}` denote candidate meanings. A decision interface returns `p_theta(. | x, C)` on the probability simplex.

For a semantics-preserving transformation `T` with candidate permutation `pi`, the required relation is:

```text
p_theta(. | T(x, C)) ~= P_pi p_theta(. | x, C)
```

where `P_pi` is the permutation operator that maps transformed candidate indices back to their original meanings.

This is stronger than preserving only the argmax. A model can keep the same answer while substantially changing confidence, selective-risk behavior, or downstream threshold decisions.

For a semantics-preserving paraphrase with no candidate permutation, the target relation is distributional invariance rather than token identity.

For a semantics-changing intervention, invariance is explicitly the wrong requirement. Removing necessary evidence, inserting contradictory evidence, or removing the valid answer should trigger a predictable change in the distribution or rejection behavior.
## Proposed transformation families

**E1 — option order.** Reorder candidates while preserving candidate semantics.

**E2 — opaque identifiers.** Rename candidates using semantically neutral identifiers while preserving rubrics.

**E3 — semantic-preserving rubric paraphrase.** Rewrite the rubric without changing its decision meaning; this requires human or carefully bounded validation before confirmatory use.

**E4 — formatting perturbation.** Change whitespace, list syntax, or equivalent serialization without changing semantics.

**C1 — rubric/name rebinding.** Hold option names and rubric texts fixed but change their binding; the output should follow the rubric meaning rather than semantic priors in the label.

**C2 — valid-answer removal.** Remove the correct candidate and require a declared reject/other behavior where the task contract supports it.

**C3 — evidence removal.** Remove required evidence under an adjudicated transformation.

**C4 — evidence contradiction.** Add a controlled contradictory source and measure whether confidence, ranking, and selective behavior respond appropriately.

The E-family tests invariance/equivariance. The C-family tests semantic responsiveness. Mixing them into one generic robustness score is prohibited.
## Candidate metrics

**Contract Equivariance Divergence (CED).** Mean Jensen-Shannon divergence between the baseline distribution and the inverse-mapped transformed distribution. Report the full distribution and quantiles, not only a mean.

**Contract Argmax Flip Rate (CAFR).** Coarse decision instability after a semantics-preserving transform. This is intentionally secondary to CED.

**Semantic Rebinding Fidelity (SRF).** Whether the model follows the rubric meaning after a controlled name/rubric rebinding rather than following the surface label.

**Reject Responsiveness (RR).** Change in rejection/other probability or selective action after a valid-answer or evidence-sufficiency intervention.

**Calibration Transport Gap (CTG).** Change in proper scoring and calibration diagnostics when a calibration map frozen on the development distribution is applied to each prespecified intervention stratum.

**Selective Risk Transport (SRT).** Coverage achievable at a fixed risk target under each intervention, using thresholds frozen before confirmatory access.

**Capability Retention (CR).** Separate scorecard for autoregressive medical and nonmedical competence. It cannot be traded away inside an average robustness score.
## Candidate method — Contract-Regularized Decision Interface (CRDI)

CRDI is a prospective method, not a result.

1. Candidate identifiers are treated as external indices or randomized opaque symbols rather than semantic supervision.
2. Candidate rubrics are encoded independently or with a set-equivariant scoring path so order is not used as meaning.
3. A shared state representation scores each candidate meaning.
4. Semantics-preserving transformed pairs receive a distribution-consistency objective after inverse mapping.
5. Evidence-changing examples receive ordinary proper-scoring supervision or a validated reject target rather than invariance loss.
6. If the language backbone is adapted, a separate maintenance objective preserves bounded autoregressive competence.
7. Post-hoc temperature scaling remains a baseline and must not be confused with intrinsic robustness.

Candidate loss sketch:

```text
L = L_decision + lambda_eq * L_contract_equivariance
  + lambda_shift * L_evidence_conditioned_proper_score
  + lambda_retain * L_language_maintenance
```

The exact parameterization, coefficients, and transformation mix remain development variables until frozen.
## Mandatory baselines

- autoregressive structured generation;
- restricted candidate-token LM logits;
- fitted linear/MLP typed head on the same frozen representation;
- current typed-decision donor/baseline where lawful and reproducible;
- Dyad-like semantic candidate scoring;
- permutation inference controls and PriDe-style debiasing where applicable;
- permutation-aware training such as PA-GRPO where reproducible and budget-matched;
- Set-LLM or an equivalent architecture-level permutation baseline where lawful and tractable;
- post-hoc temperature scaling and no-calibration control;
- a separately served decision specialist if lawful and resource-matched.

## Bounded novelty assessment

Prior work already establishes option-order sensitivity, token/label selection bias, permutation-aware mitigation, permutation-equivariant architectures, failures of typed option-name/rubric binding, medical missing-answer/metacognition failures, and medical probability-calibration weaknesses.

Therefore this proposal must not claim those components individually.

The prospective gap is narrower: **distribution-level semantic contract behavior across both meaning-preserving interface transformations and meaning-changing evidence interventions, evaluated jointly with calibration transport and retained generative capability in medical decision models**.

The gap is not proven. A refreshed adversarial search can still kill this thesis.