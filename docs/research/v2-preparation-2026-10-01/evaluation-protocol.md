# Evaluation and statistical protocol — candidate v0.1

State: **DRAFT_BLOCKED_BEFORE_FREEZE**. All numeric procedural choices below are proposed design settings, not observations or authorized resource commitments. No execution until dataset identities, meaningful margins, sample sizes, rights, environment and authority are bound. Preserve the previous protocol version if a change is needed; do not revise primary hypotheses after seeing confirmatory results.

## Estimand and outcome structure

Evaluate an independently versioned frozen candidate against preselected baselines on the same eligible cases. Keep four scorecards: medical reasoning/communication, typed probability decisions, visual understanding/generation, and systems resources. A capability-preservation or safety failure cannot be offset by improvements elsewhere. An efficiency claim requires a quality-qualified comparison; bytes alone do not prove quality per byte. No single weighted headline score.

| Hypothesis family | Proposed primary estimand | Required freeze input |
|---|---|---|
| Vault H1 / canonical H2 | Decision NLL difference; medical LM/VLM quality noninferiority | Reference donor, same-task cases, quality endpoint and justified margin |
| Vault H2 / canonical H1 | Generation/editing fidelity noninferiority with original encoder; exact encoder-removal/storage accounting | Modality-specific primary fidelity rubric, expert validity evidence, original pipeline settings, margin |
| H3 | HCF vs selected conventional merge and ordinary joint training on a conjunctive retained-quality/resource comparison | Matched data/compute ledger, selected baselines, primary comparison family |
| H4 | Predeclared directed transfer contrast against corresponding single-objective/null ablation | One transfer direction/task fixed before confirmation; other cells exploratory |
| H5 | Actual installed/checkpoint bytes and peak-memory differences at qualified quality | Named hardware/runtime, deployment packaging, offload/caching policy |
| H6 | Paired NLL as proper scoring endpoint; multiclass Brier and risk/coverage support | Held-out task/language distribution, independent calibration split, loss/coverage definition |
| H7 | English/Arabic paired quality and safety contrasts, including MSA, Saudi/Gulf and code-switching | Translation/annotation validity, slices and justified parity margins |
| H8 | Canonical independent hard gates | Qualified clinical/statistical threshold authority and exact evidence identities |

## Data firewall

Declare train, development/selection, calibration and confirmatory partitions by immutable identity and group-disjoint root provenance. Group related questions, patient/case, document, image/reference and translation variants together. No confirmatory content in training, teacher generation, prompt design, calibration, coefficient optimization, checkpoint or baseline selection. Store access events. Repeatedly inspected tests become development/regression evidence; retire them for confirmatory novelty claims. Public benchmark results are development evidence and known post-training overlap remains a limitation. No PHI, Gold or restricted dataset payload access is authorized.

Every dataset record must bind source ID/revision, license, content/split hashes, intended purpose, patient/PHI status, contamination method/results and label authority. The packet has **no admitted dataset**. Synthetic arithmetic/schema cases may later test mechanics but cannot qualify medical population claims. Teacher agreement is weak supervision, not clinical truth.

## Metrics and numerical conventions

For question i with eligible options k: `NLL_i = -log p_i(y_i)`; `Brier_i = sum_k (p_ik - 1[k=y_i])^2`, no unreported division by option count. Aggregate with frozen task weights; report option-count/type/language strata. Treat invalid/nonfinite/non-normalized outputs as failures, never silently discard them. Record numeric precision, stable log-softmax policy and probability clipping if any before execution. Compare raw and separately calibrated probabilities; fit a single positive temperature on the calibration set by NLL as the first calibration control. No test-derived temperatures or abstention thresholds.

Report accuracy, class-specific errors, NLL, Brier and top-label ECE with proposed 15 fixed equal-width bins, bin counts and reliability curves. ECE is a diagnostic, not the sole calibration endpoint. Risk-coverage uses the frozen confidence/risk definition and deterministic sample-ID tie breaking; proposed discrete AURC is the mean risk over accepted-set sizes 1..n. Report clinical and type-specific risks separately. Missing-valid-option, contradictory evidence, OOD, option-order/semantic-label permutation, multi-question isolation, prompt injection and deterministic tool dependence are required stress slices.

Visual tasks retain exact source/reference/target identities, modality, resolution, edit mask, inference steps, guidance, random seeds and negative prompts. Candidate metric families include SSIM/PSNR for paired reconstruction and clinically meaningful anatomy/pathology fidelity with qualified review; FID or generic embedding similarity alone cannot establish medical fidelity. Primary visual endpoint selection remains blocked until modality and label/rater validity are known. Generated images never become diagnostic evidence for their source cases.

## Baselines and equal treatment

Include base and medical-only Qwen, autoregressive structured output with parse failures, restricted-logit/no-task-training readout, native pointer/slot/contrastive alternatives, separate specialists, adapter composition, compatible linear/task arithmetic/TIES/DARE-TIES/DELLA/Model Stock/Arcee Fusion where supported, original OptMerge, Expert Merging++, ordinary joint multi-head training, and overlapping medical unified-model controls where reproducible. Missing/blocked baselines get a reason; they are not represented as defeated.

Proposed development-search cap: 8 configurations per method per experimental family, including failed configurations; no hidden additional prompt/temperature/coefficient searches. Same development splits and selection rule; freeze candidate identity and selected conventional baseline before test access. Specify a full-pipeline ledger: upstream base, expert construction, data/teacher generation, merge optimization, head/bridge training, stabilization, calibration, evaluation and retries. Compare both fixed-expert fusion costs and total end-to-end costs; do not grant HCF extra experts/data/updates without accounting. Optimizer/update-token ceilings, wall-clock/hardware and total resource ceilings are currently unbound, so matched-budget freeze is incomplete.

Select only among candidates with development safety/regression gates satisfied. Within that set use frozen primary endpoints and Pareto dominance; resolve remaining ties by lower total storage then fixed method ID. Do not search an aggregate score or select the best confirmatory seed.

## Replication and uncertainty

Proposed training seed list: `[17,29,43]`; generation random seeds must be paired across compared configurations and registered separately. Insufficient free resources block the protocol rather than silently dropping seeds. More seeds may be required after a prospective variability/power assessment on development material. Never claim three seeds alone establishes adequate power.

Proposed 10,000 paired cluster bootstrap resamples, analysis RNG seed `20261001`. Resample independent provenance/case clusters; questions, image variants and translations from a cluster move together. Preserve pairing across models and seeds. Show per-seed effects; where estimating training-process effects, use a preregistered hierarchical model/bootstrap rather than treating questions as independent trained models. Three training seeds impose an explicit precision limitation.

Report effect sizes and 95% confidence intervals. For noninferiority require the bound in the correct direction to remain within a clinically justified frozen margin; an insignificant difference is not equivalence. For superiority claims across selected comparisons/endpoints use a declared Holm family at alpha 0.05; the exact family and interval construction must be frozen before execution by statistical review. Conjunctive retention claims require every specified component criterion, not a significant macro average. Predefine cluster/sample count using development-only variance, desired detectable effect and power; **no confirmatory sample size is yet bound**.

## Safety, kill rules and deviations

Inherit `emergency_miss_rate`, `medication_critical_error_rate`, `selective_risk_at_target_coverage`, `citation_entailment_fidelity`, `arabic_clinical_parity_gap`, and `lab_report_field_extraction_accuracy` and governed benign over-triage policy. Their clinical thresholds remain `NEEDS_EVIDENCE`; do not substitute zero or make them passable. Zero violations on identity-bound mechanical sentinels is distinct from population zero clinical error. Any hard-gate FAIL dominates; missing/blocked required evidence prevents PASS under the canonical aggregator.

Abort or disqualify on identity/license mismatch, unauthorized cost/resource use, quarantine leak, PHI encounter, malformed probabilities, nonfinite optimization, omitted raw outputs, deterministic safety override or prespecified clinical failure. Predeclare bounded mitigation/retry rules before development runs. Preserve every failure. Hardware interruptions may restart only under a frozen resumability rule with the same identity/seed and no result-based choice. Withdraw confirmation if test exposure or protocol deviation invalidates the estimand; record the deviation, affected claim and new protocol version.

## Freeze checklist

Need exact model/data/runtime manifests; label and clinical-review authority; primary visual/medical endpoints; thresholds/margins; sample size/power; baseline search and full training budgets; seeds; inference settings; statistical comparison family; quarantine/storage/access policy; artifact schema; and bounded execution authority. Until these are complete, this document is a preparation draft, not a frozen evaluation contract.
