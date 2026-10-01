# AGENTS.md

## Mission

Build commandMed as a universal Health & Medical Intelligence research program whose prospective v2 target is a **single-checkpoint medical foundation model** unifying autoregressive reasoning, native multimodal understanding, one-pass typed decisions, and visual generation around one shared Qwen-family semantic backbone.

The optimization target remains **verified health and medical intelligence per byte, joule, and second**. Parameter count, training completion, public benchmark wins, attractive demos, or a single paper claim are not success criteria by themselves.

## Authority and reading order

Before doing work, read in this order:

1. `.specify/memory/constitution.md`
2. `docs/COMMANDMED-V2-FOUNDER-DIRECTION-2026-09-29.md`
3. `docs/COMMANDMED-GRAND-MASTER-PLAN-v2.0.md`
4. `docs/research/COMMANDMED-V2-PAPER-AND-NOVELTY-PROGRAM.md`
5. `docs/decision-register.md`
6. `specs/README.md`
7. the active bounded spec and its plan/tasks/checklist

The older `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md` remains historical planning/evidence and is superseded only for prospective architecture and roadmap planning.

If an older planning record conflicts with the v2 founder-direction document on the prospective one-checkpoint research target, the v2 direction governs prospectively. Historical execution evidence is never rewritten.

The active bounded spec is the execution authority. Adjacent roadmap items are not implicitly authorized.

## Absolute research rule

> **NO TRAINING RUN IS ALLOWED TO DEFINE SUCCESS. SUCCESS IS DEFINED BY A FROZEN EVALUATION PROTOCOL CREATED BEFORE THE RUN.**

## Current global state

`RESEARCH_PLANNING`

Unless a later bounded spec explicitly authorizes otherwise:

- DO NOT download, load, or execute model weights.
- DO NOT run inference against candidate backbones.
- DO NOT execute model merging, conversion, adapter application, or weight transformation merely because v2 describes them.
- DO NOT run continued pretraining, SFT, LoRA, QLoRA, full fine-tuning, distillation, DPO, GRPO, RL, flow/diffusion training, bridge training, or QAT.
- DO NOT access PHI, restricted clinical datasets, credentials, or gated model assets.
- DO NOT send private/restricted health data to third-party APIs.
- DO NOT use any external model output as training data without explicit lineage/rights authority.
- DO NOT declare CommandMed One successful.
- DO NOT declare Qwen3.8, Qwen-Image, Kev, decider, or any merge method a proven winner merely because it is preferred in planning.
- DO NOT claim SOTA, clinical superiority, diagnosis performance, safety, release readiness, or publication novelty wider than the evidence.

## v2 research target

The primary hypothesis is one model/checkpoint with:

- one shared Qwen-family medical semantic backbone;
- an autoregressive language/multimodal reasoning path;
- a native one-pass typed decision head;
- a visual bridge into an image-generation DiT/VAE path;
- no separately served Jev-like foundation model in the target architecture;
- no separately served Qwen-Image semantic encoder in the target architecture after successful encoder replacement;
- deterministic/authoritative clinical tools remaining external by design.

A single checkpoint may contain heterogeneous internal modules. “One model” does not require unrelated tensors to be averaged or every submodule to use the same transformer block.

## Heterogeneous Capability Fusion discipline

`Heterogeneous Capability Fusion (HCF)` is a working research method name. Treat it as unproven.

Separate the problem into:

1. architecture-compatible Qwen expert/task-vector merging;
2. decision-head integration/transplantation;
3. representation alignment between the shared backbone and image generator;
4. replacement of duplicated image semantic encoders;
5. joint stabilization;
6. later consolidation/compression only if evidence supports it.

Do not perform naive weight averaging across incompatible causal-language, decision-head, diffusion/flow, or VAE tensors.

Required merging baselines should include applicable MergeKit methods, OptMerge, Expert Merging/Expert Merging++, ordinary adapter composition, and matched joint training when the corresponding bounded spec reaches execution authority.

## Paper-first discipline

A publication-quality paper is a primary project deliverable.

Before confirmatory experiments:

- freeze the exact research questions;
- freeze primary endpoints and safety gates;
- freeze baseline-search/tuning budgets;
- freeze evaluation and statistical plans;
- freeze source revisions, licenses, and data lineage;
- quarantine confirmatory test material from optimization;
- maintain a claim ledger whose default state is `UNPROVEN`;
- treat repeatedly inspected tests as development/regression evidence;
- preserve negative results.

Do not use `first`, `best`, `SOTA`, `safe`, `clinical-grade`, or `revolutionary` as scientific conclusions until the exact claim is evidence-backed and the related-work search supports it.

## Scientific invariants

1. Evaluation precedes optimization.
2. Safety-critical metrics are hard gates; averages cannot compensate for critical failures.
3. Gold/holdout artifacts are quarantined from training, teacher generation, prompt tuning, merging coefficient search, RL, DPO, hyperparameter selection, checkpoint selection, and model selection.
4. Every training/evaluation data asset must have provenance, license status, content identity/hash, split identity, contamination status, and verification state.
5. Public benchmark performance is development evidence, not sufficient release evidence.
6. General reasoning, instruction following, English, Arabic, tool use, calibration, multimodal understanding, and safety must be checked for regression after specialization or fusion.
7. Mutable medical truth belongs in evidence/retrieval/tool layers where practical; weights must not be treated as a current guideline database.
8. A model may route to or explain deterministic tools but must not replace deterministic arithmetic, validated clinical scores, schema validation, or authoritative interaction/drug lookups where those exist.
9. Patient-facing claims require human evaluation, not model-only scores.
10. Each modality has an independent maturity/evaluation gate. Accepting or generating an image does not make that modality clinically mature.
11. Generated/edited pixels are not clinical evidence for the source case.
12. A merged or unified checkpoint cannot inherit safety, calibration, medical, or licensing claims from its donors; it must be re-evaluated.

## Probability, calibration, and unsupported certainty

v2 does not require a separately served uncertainty model.

Typed probabilities should be native decision-head outputs and must be evaluated using appropriate metrics such as NLL, Brier score, calibration diagnostics, risk-coverage/AURC, and task/language/safety slices.

The target is calibrated decisiveness, not universal confidence. Unsupported certainty remains a failure mode.

## Required behavioral states

The system design must support at least:

- `ANSWER`
- `ASK_MORE`
- `USE_TOOL`
- `RETRIEVE_EVIDENCE`
- `ABSTAIN`
- `ESCALATE`
- `EMERGENCY`

Critical escalation rules and deterministic safety checks are not overridable by generative text or decision-head confidence.

## Training-role model

Training behavior is grouped into three classes to avoid needless persona fragmentation:

1. `PATIENT_CAREGIVER`
2. `CLINICAL_PROFESSIONAL`
3. `LEARNER_RESEARCHER`

Evaluation may and should slice physicians, nurses, pharmacists, patients, caregivers, students, and researchers separately.

## Multimodal boundary

The v2 primary neural research hypothesis is a single checkpoint with a shared semantic backbone.

This does not eliminate modality-specific evaluation or deterministic external tools. It also does not prove that raw ECG, CT/MRI volumes, whole-slide pathology, specialist ophthalmology/dermatology, medical audio, or real-time video are mature merely because a unified model can accept or generate related content.

Each specialized modality must still earn its own evidence.

## Model and license discipline

The current preferred research lineage is Qwen-family, especially `Qwen/Qwen3.8-27B` for the shared semantic backbone, Qwen-derived Jev/System-One alternatives for decision research, and Qwen-Image-family work for the visual-generation path.

This is a founder-selected research direction, not a license waiver or a proven model winner.

Before execution, record exact:

- model/repository identity;
- revision;
- architecture/configuration;
- tokenizer/processor identity;
- license and research/commercial/redistribution constraints;
- derivative and publication implications;
- known post-training provenance limitations.

Qwen-Image-2.1 has a distinct research-license posture at the current planning snapshot. Do not imply that CommandMed’s Apache-2.0 software license relicenses Qwen-Image material or derivatives.

## Ponytail execution discipline

Use the smallest mechanism that satisfies the active spec:

1. Does this need to exist?
2. Can an existing repository mechanism be reused?
3. Can the language standard library do it?
4. Can the native platform do it?
5. Can an already-approved dependency do it?
6. Can it be one small implementation instead of a framework?
7. Only then introduce a new mechanism.

Avoid speculative abstractions, registries, plugins, services, databases, queues, wrappers, base classes, factories, and configuration layers.

### Ponytail safety carve-out

Minimalism MUST NOT remove or weaken:

- clinical validation;
- security and trust-boundary validation;
- privacy protections;
- provenance and license evidence;
- reproducibility;
- data integrity checks;
- holdout/quarantine controls;
- deterministic safety checks;
- tests for safety-critical behavior;
- auditability;
- explicit failure handling;
- paper claim traceability;
- statistical validity;
- negative-result preservation.

These are requirements, not overengineering.

## Spec Kit workflow

For each bounded spec, use the Spec Kit lifecycle:

`specify -> clarify -> plan -> checklist -> tasks -> analyze -> implement -> verify/close`

Rules:

- Never implement when `analyze` reports unresolved contradictions or missing hard requirements.
- Never silently broaden the active spec.
- Do not fully design later specs merely because they are visible in the roadmap.
- Prefer a small number of independently verifiable tasks.
- Every spec must state explicit exclusions and exit evidence.
- New v2 prospective work must enter through new bounded specs rather than rewriting closed historical specs.

## Git discipline

- Verify live repository truth before mutation.
- Never force-push.
- Never rewrite shared history destructively.
- Work on feature branches and use draft PRs while evidence is incomplete.
- Keep generated/experimental outputs out of canonical source unless the active spec names them as artifacts.
- Do not merge a planning or implementation PR merely because checks are green; its spec/decision exit gate must also be satisfied.
- Preserve exact historical SHAs, run IDs, and negative evidence.
- Use normal merge commits when merging governed work unless a bounded authority explicitly requires otherwise.

## Review workflow

Use Alibaba Open Code Review as part of code review where code is introduced and use Jev as an independent review/qualification tool where applicable under the founder’s standing workflow.

Do not use CodeRabbit, Qodo, Cubic, or similar services as project qualification evidence.

Automated review never substitutes for qualified clinical, statistical, privacy, rights, or human-factor evidence.

## Claims discipline

Use language such as `candidate`, `preferred research donor`, `measured`, `observed`, `not yet validated`, `unproven`, and `reference` until evidence supports stronger wording.

Never equate:

- benchmark score with clinical safety;
- medical QA with patient utility;
- model-only performance with human+AI performance;
- quantization success with medical equivalence;
- synthetic teacher agreement with truth;
- model size with on-device feasibility;
- one checkpoint with successful capability integration;
- generation quality with diagnostic validity;
- a donor model’s license with a derivative model’s release eligibility;
- an attractive research hypothesis with a publishable contribution.

<!-- graft:start -->
## Graft — repository context layer

Use Graft (https://github.com/trailhq/Graft, `@nanonets/graft`) only as local developer/agent tooling for repository context and code navigation. This does not authorize model-weight access, inference, training, external medical-data egress, or any execution forbidden by the active bounded spec.

If Graft is unavailable or the local `graft/` graph is absent/stale, run `graft init`, select the active agent(s), then run `graft build`. Prefer `graft check`, `graft map`, `graft ask "<question>" --source`, `graft skeleton <file>`, `graft callers <symbol>`, and `graft grep "<literal>"` before broad source exploration. After material code changes, run `graft build` again.

Treat `graft/` as a local regenerable cache and do not commit it. Keep usage zero-cost: deterministic structural graph operations are permitted; do not introduce paid model/API usage. Any model-backed enrichment would require separate authorization under the active spec and applicable data/egress rules.

Graft output is navigation context, not medical evidence, scientific evidence, evaluation evidence, safety evidence, or qualification authority. Existing frozen evaluation, Spec Kit, Jev, Alibaba Open Code Review, CI, security, privacy, provenance, licensing, and claims gates remain authoritative. Never fabricate Graft output, tool execution, CI, reviews, or evidence.
<!-- graft:end -->
