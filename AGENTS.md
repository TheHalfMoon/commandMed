# AGENTS.md

## Mission

Build commandMed as a universal, multimodal Health & Medical Intelligence research system for patients, caregivers, clinical professionals, learners, and researchers, with exceptional on-device efficiency and evidence-bound safety.

The optimization target is **verified health and medical intelligence per byte, joule, and second**. Parameter count, training completion, public benchmark wins, and attractive demos are not success criteria by themselves.

## Authority and reading order

Before doing work, read in this order:

1. `.specify/memory/constitution.md`
2. `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
3. `docs/decision-register.md`
4. `specs/README.md`
5. the active bounded spec and its plan/tasks/checklist

The active bounded spec is the execution authority. Adjacent roadmap items are not implicitly authorized.

## Absolute research rule

> **NO TRAINING RUN IS ALLOWED TO DEFINE SUCCESS. SUCCESS IS DEFINED BY A FROZEN EVALUATION PROTOCOL CREATED BEFORE THE RUN.**

## Current global state

`RESEARCH_PLANNING`

Unless a later bounded spec explicitly authorizes otherwise:

- DO NOT download, load, or execute model weights.
- DO NOT run inference against candidate backbones.
- DO NOT run continued pretraining, SFT, LoRA, QLoRA, full fine-tuning, distillation, DPO, GRPO, RL, or QAT.
- DO NOT access PHI, restricted clinical datasets, credentials, or gated model assets.
- DO NOT send private/restricted health data to third-party APIs.
- DO NOT use any external model output as training data.
- DO NOT declare a winning backbone.
- DO NOT claim SOTA, clinical superiority, diagnosis performance, or release readiness.

## Scientific invariants

1. Evaluation precedes optimization.
2. Safety-critical metrics are hard gates; averages cannot compensate for critical failures.
3. Gold/holdout artifacts are quarantined from training, teacher generation, prompt tuning, RL, DPO, hyperparameter selection, checkpoint selection, and model selection.
4. Every training/evaluation data asset must have provenance, license status, content identity/hash, split identity, contamination status, and verification state.
5. Public benchmark performance is development evidence, not sufficient release evidence.
6. General reasoning, instruction following, Arabic capability, tool use, and safety must be checked for regression after specialization.
7. Mutable medical truth belongs in evidence/retrieval/tool layers where practical; weights must not be treated as a current guideline database.
8. A model may route to or explain deterministic tools but must not replace deterministic arithmetic, validated clinical scores, schema validation, or authoritative interaction/drug lookups where those exist.
9. Patient-facing claims require human evaluation, not model-only scores.
10. Each modality has an independent maturity/evaluation gate. Accepting an input type does not make that modality clinically mature.

## Required behavioral states

The system design must support at least:

- `ANSWER`
- `ASK_MORE`
- `USE_TOOL`
- `RETRIEVE_EVIDENCE`
- `ABSTAIN`
- `ESCALATE`
- `EMERGENCY`

Critical escalation rules and deterministic safety checks are not overridable by generative text.

## Training-role model

Training behavior is grouped into three classes to avoid needless persona fragmentation:

1. `PATIENT_CAREGIVER`
2. `CLINICAL_PROFESSIONAL`
3. `LEARNER_RESEARCHER`

Evaluation may and should slice physicians, nurses, pharmacists, patients, caregivers, students, and researchers separately.

## Multimodal boundary

Treat commandMed as one medical intelligence system with multiple senses, not necessarily one monolithic network.

V1 research prioritizes:

- text;
- documents and laboratory reports;
- ordinary photos with conservative safety behavior.

Specialized signals/volumes such as raw ECG, wearables, CT/MRI volumes, whole-slide pathology, and later audio/video may remain external specialist modules that emit structured, provenance-bound findings into the commandMed evidence contract.

## Model and license neutrality

No model is preselected.

A candidate may enter research only after its license and redistribution/commercial constraints are recorded. A technically strong candidate can be rejected for lineage or deployment constraints.

Until an explicit decision changes this rule:

- MedGemma/HAI-DEF models are reference/evaluation assets only; their outputs must not train commandMed.
- LFM-family models are conditional-license research candidates, not a locked commercial lineage.
- Frontier API outputs are evaluation/reference-only unless their terms explicitly permit the intended training use.

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
- explicit failure handling.

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

## Git discipline

- Verify live repository truth before mutation.
- Never force-push.
- Never rewrite shared history destructively.
- Work on feature branches and use draft PRs while evidence is incomplete.
- Keep generated/experimental outputs out of canonical source unless the active spec names them as artifacts.
- Do not merge a planning or implementation PR merely because checks are green; its spec exit gate must also be satisfied.
- Independent repository/PR review is optional by default under constitutional amendment `FD-007`; a later bounded authority may explicitly require it for a named task.

## Claims discipline

Use language such as `candidate`, `measured`, `observed`, `not yet validated`, and `reference` until evidence supports stronger wording.

Never equate:

- benchmark score with clinical safety;
- medical QA with patient utility;
- model-only performance with human+AI performance;
- quantization success with medical equivalence;
- synthetic teacher agreement with truth;
- model size with on-device feasibility.
