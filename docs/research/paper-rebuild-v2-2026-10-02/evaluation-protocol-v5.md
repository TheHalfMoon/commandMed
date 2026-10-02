# Evaluation protocol V5

Status: prospective freeze candidate; no model execution authority.

## Evaluation objective

Determine whether targeted reliability interventions improve only their intended property, transfer beneficially, remain neutral, or create cross-property interference in medical foundation-model decision systems.

## Assurance axes

1. Canonical decision quality: NLL, Brier score, accuracy and task-specific utility.
2. Probability calibration: reliability curves plus prespecified calibration error diagnostics.
3. Probabilistic/logical coherence: complement/additivity/transitivity residuals where the task exposes linked propositions.
4. Semantic stability: distributional change under validated meaning-preserving transformations.
5. Evidence responsiveness: required direction or target change under validated meaning-changing interventions.
6. Action validity: agreement with qualified deterministic rules or frozen action thresholds.
7. Selective control: risk-coverage behavior and decision-theoretic abstention metrics.
8. Capability retention: prespecified language/reasoning tasks for any intervention that changes model parameters.

Axes are reported independently. A missing or undefined construct is `NOT_APPLICABLE`, never imputed.

Endpoint relationships are preregistered pairwise as `STRUCTURALLY_DISTINCT`, `SHARED_INPUT`, or `MATHEMATICALLY_COUPLED`. This label is descriptive of the measurement construction, not an empirical result. Mechanical coupling cannot be promoted as a surprising cross-property effect.

## Medical oracle hierarchy

Preferred oracle order is: qualified deterministic clinical rule with explicit inputs; executable guideline-derived logic with versioned source; expert-adjudicated public benchmark item; public benchmark gold label with known limitations; model-based rubric only as a secondary measure. Generated clinical text is never its own ground truth.
## Transformation families

Meaning-preserving families include candidate permutation, opaque identifier rebinding, validated paraphrase, serialization changes and clinically irrelevant text perturbations. Meaning-changing families include evidence removal/addition, controlled contradiction, threshold-crossing risk-factor changes, answer-set changes and rule-input changes. Every transformation has a machine-readable provenance record and an explicit expected relation.

Semantic validators are frozen before confirmatory use. A transformation rejected by the validator is excluded before any model output is observed.

## Intervention families

Admitted confirmatory interventions are restricted to methods with lawful artifacts, exact reproducibility and fair comparison. Current candidates are temperature scaling, a selection-bias correction, a matched typed readout, contract regularization, contract regularization with capability maintenance, selective act/defer policy and deterministic clinical-rule routing.

Trained interventions require matched data, optimizer budget, parameter budget and checkpoint-selection access, plus a prespecified number of independent training seeds. Post-hoc interventions use the same base predictions and calibration split whenever possible.

Every intervention has a frozen cost vector: added trainable parameters, training compute where measurable, inference calls, latency, peak memory, persistent storage and external deterministic-tool calls. Reliability gains are interpreted jointly with these costs but are not collapsed into a single utility score.

For probability-transforming interventions, the primary operational evaluation keeps downstream action/abstention thresholds fixed. A separately labeled refit-policy analysis may ask what happens after downstream policy re-optimization.

## Task-family separation

`RULE_ORACLE` families use deterministic calculators or executable rules and support exact action-validity counterfactuals. `OPEN_CLINICAL_REASONING` families use auditable public labels or qualified adjudication and probe evidence use, robustness and reasoning under less deterministic semantics. Their effects are reported separately and are not averaged into one primary effect.

## Controls

Required controls are unchanged-base repeated runs, sham semantic-preserving transformations, calibration-only intervention expected not to change argmax ranking, no-tool vs deterministic-tool execution, and matched-supervision/capacity controls for learned readouts.

## Confirmatory quarantine

Final source-item identities, transformation seeds, held-out action thresholds and expert adjudications are unavailable to prompt design, intervention tuning, calibration fitting, model selection and code debugging. Any accidental exposure is logged and removes the affected material from confirmatory status.

## Success boundary

A major paper contribution requires a replicated material cross-property effect, a replicated non-additive interaction, a strong equivalence result under meaningful margins, a consequential aggregate-vs-hard-gate reversal, or a new Pareto-improving intervention independently confirmed. A colorful heatmap alone is not success.
