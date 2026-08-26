# Research — Spec 007 SFT V1 planning hardening

**Branch:** `spec/007-clarify-plan-hardening-v2`
**Parent authorization candidate:** PR #47 head `5e8618de32468f04d797117cc46bb2bdf72dd3e1`
**Status:** clarification/planning research candidate; not executable authority
**Execution authority:** NONE
**Model selection authority:** FOUNDER+CHATGPT ONLY

> This research note hardens the SFT V1 planning package before implementation. It does not select a model, download weights, construct a real training dataset, run a tournament, execute training, access Gold/PHI, or authorize spend. Any concrete backbone remains `BACKBONE_WINNER=NEEDS_EVIDENCE` until Founder + ChatGPT bind an authorized tournament result.

## 1. Research objective

Identify technical requirements that must be frozen before commandMed can honestly call SFT V1 training-ready. The existing specification is strong on provenance, quarantine, safety composition, role classes, and pre-run evaluation. This review focuses on training-mechanics gaps that can silently invalidate otherwise well-governed fine-tuning.

The resulting design must remain:

- model-neutral;
- backend-neutral;
- deterministic/fail-closed at the control-plane layer;
- explicit about the limits of GPU reproducibility;
- compatible with the three frozen role classes;
- safe under multi-turn/tool-use interactions;
- quarantine-clean across every monitoring, tuning, recipe, and checkpoint-selection surface.

## 2. Findings and planning decisions

### R-001 — Tokenizer and chat-template identity are first-class training inputs

A checkpoint identifier alone is insufficient to reproduce conversational SFT. The training input rendering depends on tokenizer files, special-token mapping, chat template, tool-call formatting, BOS/EOS behavior, and truncation policy.

**Decision:** `BaseCheckpointBinding` and `TrainingConfigurationRecord` must bind, before activation:

- exact checkpoint identity;
- tokenizer revision/content identity;
- tokenizer configuration identity;
- special-token map identity;
- canonical chat-template bytes/hash;
- BOS/EOS policy;
- tool-schema rendering policy;
- prompt rendering version.

A changed tokenizer/template invalidates comparability with a previous run unless explicitly treated as a new recipe identity.

Primary reference: Hugging Face TRL `SFTTrainer` / chat-template behavior.

### R-002 — Loss masking must be frozen, not inherited from trainer defaults

Conversational SFT can compute loss over the whole sequence, completion only, or assistant messages only. These are materially different objectives. Tool-call tokens may also need explicit inclusion/exclusion semantics.

**Decision:** freeze a versioned `LossMaskPolicy` before any run. It must define:

- whether user/system tokens receive loss;
- whether only assistant generations receive loss;
- whether tool-call arguments receive loss;
- whether tool results receive loss;
- treatment of safety-control tokens / structured outputs;
- token-level mask-generation algorithm and identity;
- positive/negative fixture proofs for masking boundaries.

No trainer default may silently determine the objective.

### R-003 — Packing and truncation require safety-aware boundaries

Packing improves token utilization, but incorrect packing or truncation can create cross-example leakage or silently remove medically/safety-critical turns.

**Decision:** the plan must freeze:

- whether packing is enabled;
- attention-isolation/boundary semantics for packed examples;
- sequence-length ceiling;
- deterministic truncation/segmentation policy;
- rules forbidding silent removal of system safety instructions, tool schemas, emergency context, labels, or terminal assistant targets;
- rejection/segmentation reason codes when an example cannot be represented safely.

### R-004 — Data quality is a coverage/quality problem, not a volume contest

LIMA and later targeted-selection work support the repository's existing preference for fewer verified examples over large noisy corpora. No specific algorithm such as LESS should become mandatory without evidence.

**Decision:** curriculum construction optimizes a declared multi-dimensional record score/coverage report rather than a raw row-count target. Required reporting dimensions:

- frozen curriculum stratum coverage;
- role-class coverage;
- Arabic/English coverage;
- provenance quality;
- review/adjudication state;
- novelty / near-duplicate status;
- contamination status;
- token contribution after rendering;
- safety/abstention/tool/multi-turn coverage.

Large duplicated or low-value datasets cannot satisfy readiness by volume.

### R-005 — Multi-turn and tool-use behavior must exist in the SFT contract

Real health interactions are frequently multi-turn, context-seeking, and tool/evidence mediated. Tool calling also has failure modes beyond simple schema validity.

**Decision:** the curriculum/evaluation plan must include bounded synthetic/verified examples covering:

- `ASK_MORE -> ANSWER`;
- `ASK_MORE -> ESCALATE`;
- `RETRIEVE_EVIDENCE -> ANSWER/ABSTAIN`;
- `USE_TOOL -> validated result -> explanation`;
- unavailable tool -> fail-closed;
- nonexistent tool hallucination;
- invalid arguments;
- wrong tool selection;
- multi-turn state drift;
- tool-format sensitivity;
- tool-result spoof/injection resistance through the Spec 006 boundary.

BFCL-style dimensions may inform methodology, but no external benchmark is automatically a release gate.

### R-006 — Safety preservation during a run must not create a quarantine leak

Published evidence shows that downstream fine-tuning can degrade an aligned model's safety even when fine-tuning data is not intentionally adversarial. That does not justify reusing quarantined evaluation assets as optimization feedback.

**Decision:** the canonical Spec 007 FR-003 quarantine matrix remains authoritative across monitoring, early stopping, recipe selection, and checkpoint selection. A future authorized run may use a separately identity-bound `SFT_ABORT_SENTINEL_SET` only if its source identities are outside the prohibited canonical quarantine set for the exact SFT monitoring purpose, all Spec 003 evidence passes, the set is excluded from gradient-bearing data, and its only permitted actions are `CONTINUE`, `ABORT_RUN`, or `DISQUALIFY_RUN`.

An abort-only sentinel must never:

- rank checkpoints;
- choose a recipe/update strategy;
- change hyperparameters;
- drive early stopping toward a preferred checkpoint;
- select a model.

If no permissible abort-only sentinel exists, intra-run monitoring does not become an exception: the pre-registered run schedule continues and final qualification occurs after checkpoint identity is frozen.

### R-007 — Catastrophic forgetting requires an explicit preservation contract without tuning on holdouts

Spec 007 already requires base-vs-SFT paired deltas, but the plan must make the preservation set and decision rule operational without leaking quarantined assets into optimization.

**Decision:** create a versioned `CapabilityPreservationBinding` covering at minimum:

- general reasoning;
- instruction following;
- Arabic capability;
- tool use;
- uncertainty/abstention;
- safety;
- core medical strata.

When those slices are backed by canonical quarantine-controlled sources, they are qualification evidence only. They cannot rank checkpoints, alter the recipe, set hyperparameters, or otherwise influence optimization. Abort-only drift detection, if used, must satisfy R-006's separate non-quarantined sentinel contract.

### R-008 — Checkpoint selection needs the complete canonical quarantine firewall

Selecting the "best" checkpoint by repeatedly consulting test, Gold, development, benchmark, pilot, or other quarantine-controlled evidence creates hidden optimization leakage.

**Decision:** all source identities governed by Spec 007 FR-003's canonical quarantine matrix are structurally excluded from SFT checkpoint ranking/selection, recipe selection, hyperparameter selection, early stopping, and every other tuning surface. This includes the explicitly named sources `COMMANDMED_CLINICAL_GOLD`, `COMMANDMED_ARABIC_GOLD`, `COMMANDMED_MULTIMODAL_GOLD`, `CALIBRATION_HOLD_OUT_SPLIT`, `MODEL_SELECTION_DEV_SET`, `PUBLIC_BENCHMARK_DEV_SPLITS`, `HELD_OUT_SYNTHETIC_PILOT_CASES`, `VERIFIED_DEV_SPLIT`, plus every additional source identifier in the frozen matrix for a prohibited SFT tuning purpose. `CALIBRATION_HOLD_OUT_SPLIT` remains calibration-only.

Until a separate canonical source/purpose authority admits a demonstrably non-quarantined SFT checkpoint-selection source, the checkpoint rule is fixed before training — e.g. the final checkpoint at the pre-registered step/token budget — with no evaluation asset used to rank checkpoints. Abort-only sentinels cannot rank.

### R-009 — GPU reproducibility must be defined realistically

PyTorch explicitly does not guarantee complete reproducibility across releases, commits, platforms, or CPU/GPU environments, even with identical seeds.

**Decision:** use two levels:

- `EXACT_ENVIRONMENT_REPLAY`: same pinned model/tokenizer/data/config/software/hardware class, deterministic mode where supported, identical seed/RNG/data order; target is the strongest reproducibility the chosen stack can provide.
- `CROSS_ENVIRONMENT_REPRODUCIBILITY`: repeated runs across allowed equivalent environments are compared statistically/behaviorally; byte-identical weights are not required unless empirically proven.

The environment manifest must capture:

- Python/framework/backend versions;
- CUDA/ROCm/Metal/runtime versions as applicable;
- GPU/device identity;
- kernel/attention backend identity;
- precision policy;
- seeds and data seed;
- optimizer/scheduler state;
- RNG state;
- dataset cursor/order state;
- checkpoint/resume identity.

Claims of deterministic training beyond what the selected runtime can prove are prohibited.

### R-010 — Resume integrity is part of reproducibility

A model-only checkpoint does not reproduce an interrupted training trajectory when optimizer/scheduler/RNG/data-position state is missing.

**Decision:** `TrainingCheckpointManifest` must distinguish:

- inference/export checkpoint;
- resumable training checkpoint.

A resumable checkpoint must bind model/adapter state, optimizer, scheduler, scaler where applicable, RNG, data position/order, global step, configuration identity, and base/dataset/template identities. Incomplete checkpoints fail closed for resume.

### R-011 — Arabic tokenization efficiency is a tournament and SFT planning axis

Recent cross-lingual medical evaluation reports persistent Arabic performance gaps and structural tokenization fragmentation in Arabic medical text.

**Decision:** before Founder + ChatGPT choose a backbone, the authorized tournament evidence packet must report language-aware tokenizer measurements including:

- tokens per word / characters per token on matched English/Arabic medical samples;
- fragmentation of medication names and common clinical terms;
- Modern Standard Arabic;
- Saudi/Gulf colloquial samples;
- English-Arabic code switching;
- transliterated medication/medical terminology.

These are evidence inputs to Founder + ChatGPT, not a model-selection decision by Pi.

### R-012 — Arabic data needs provenance beyond `language=ar`

**Decision:** Arabic curriculum records must additionally represent, when applicable:

- `original_language`;
- translation/transcreation status;
- translator/reviewer evidence identity;
- dialect/register tag;
- code-switch status;
- transliteration status;
- terminology normalization identity;
- clinician/qualified-review status where required.

Machine translation alone cannot create a claim of Arabic clinical validity.

### R-013 — Mutable clinical truth belongs outside weights where practical

AGENTS.md invariant 7 already freezes this principle.

**Decision:** curriculum admission must classify knowledge as either:

- durable behavioral/domain pattern suitable for weights; or
- mutable/local/jurisdiction-specific/current-guideline content that should remain in retrieval/tool/evidence layers unless a later evidence-backed exception is approved.

This protects against turning SFT weights into a stale guideline database.

### R-014 — Backend neutrality should survive through planning

TRL/Transformers, PEFT, Axolotl, Unsloth, Liger, or other stacks may be useful, but the winning backbone, target hardware, recipe, numerical behavior, and licensing constraints are not known yet.

**Decision:** freeze a backend-independent training contract first. Backend selection is a later evidence record that must prove:

- support for the winner architecture/tokenizer/template;
- required loss masking;
- packing/truncation semantics;
- resume integrity;
- reproducibility controls;
- required precision/adapter mode;
- no hidden network/telemetry/provider dependency;
- numerical/behavioral equivalence acceptable for the experiment.

Do not canonically preselect Unsloth, Axolotl, raw TRL, PEFT mode, LoRA, QLoRA, or full update during clarification.

### R-015 — Open-ended and realistic medical evaluation should complement MCQ evidence without becoming hidden tuning feedback

HealthBench uses realistic multi-turn health conversations and physician-authored rubrics. HealthBench Professional extends this toward clinician workflows. These are useful evaluation references because commandMed targets patient and professional behavior rather than only exam accuracy.

**Decision:** planning maintains two distinct evaluation families:

- structured/verifiable tasks where deterministic scoring is defensible;
- open-ended conversation/workflow tasks with physician-derived rubrics and explicit evaluator-validation limits.

An LLM judge is never the sole medical truth authority. Admission of an external suite as evaluation evidence does not authorize its use for checkpoint/recipe selection. Any judge-derived result that is backed by a quarantined source is qualification-only under FR-003; a future optimization-affecting use would require a separately canonicalized, non-quarantined source/purpose authority.

### R-016 — Abstention needs a dedicated curriculum/evaluation slice

MedAbstain-style evidence reinforces that high task accuracy does not imply knowing when to abstain.

**Decision:** SFT V1 requires dedicated curriculum coverage and final-evaluation slices for:

- missing information;
- contradictory information;
- ambiguous risk;
- OOD/unsupported question;
- insufficient evidence;
- `ASK_MORE`;
- `ABSTAIN`;
- `ESCALATE`;
- `EMERGENCY`.

Correctly not answering can be a positive target. Quarantined final/development evaluation sources remain outside tuning and checkpoint selection.

### R-017 — Memorization/regurgitation requires explicit auditability

**Decision:** before any dataset activation, the data plan must include:

- exact and near-duplicate detection;
- repeated-record detection;
- benchmark overlap detection;
- bounded canary strategy for memorization testing using non-sensitive synthetic strings;
- verbatim-regurgitation probes on licensed/public evidence where legally appropriate;
- no PHI or secrets used as canaries.

Any audit asset that belongs to the canonical quarantine set is evidence-only and cannot be fed back into recipe/checkpoint tuning.

### R-018 — The tournament-to-training handshake must not imply a pre-authorized pilot

Spec 007 assumes a qualified winner but must not create one. No training-like pilot may run before the same controlled authorities required for training are canonical.

**Decision:** the pre-training sequence is:

```text
SFT OFFLINE INFRASTRUCTURE READY
-> FOUNDER+CHATGPT CANDIDATE MANIFEST FREEZE
-> SEPARATE AUTHORIZED TOURNAMENT EXECUTION
-> EVIDENCE PACK RETURNED
-> FOUNDER+CHATGPT BACKBONE WINNER DECISION
-> BASE CHECKPOINT BINDING CANONICAL
-> NON_EXECUTING_RECIPE_EVIDENCE_FROZEN
-> DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
-> TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
-> FIRST TRAINING RUN
```

`NON_EXECUTING_RECIPE_EVIDENCE` means only static/control-plane evidence available without loading model weights or performing gradient-bearing work: recipe schema completeness, backend compatibility declarations, loss-mask/rendering/packing/truncation conformance contracts, compute/resource estimates, provenance/quarantine bindings, environment identity, and other non-executing preflight evidence. It does **not** include loss curves, gradient behavior, convergence, model outputs, benchmark results, or any empirical evidence requiring model execution.

Any later experiment described as a pilot, smoke-train, adapter pilot, one-step train, gradient probe, or equivalent is a training run for authority purposes. It requires model/weight/data/device/finance/training gates before execution and cannot select recipe/hyperparameters/checkpoints unless a separately authorized policy also satisfies the complete FR-003 quarantine firewall.

Pi may prepare schemas, validators, manifests, and decision packets. Pi must not perform the candidate freeze or winner decision.

## 3. Evaluation/reference candidates discovered in this review

These are research/evaluation candidates only and require their own license, identity, version, contamination, admissibility, and quarantine-purpose review before use:

- HealthBench — realistic multi-turn health conversations with physician-authored rubrics.
- HealthBench Professional — clinician-facing care consult, writing/documentation, and medical-research tasks.
- MedAbstain — abstention under medical uncertainty.
- MedAraBench — large-scale Arabic medical QA across specialties/difficulty levels.
- MedArabiQ — multiple Arabic medical task formats.
- BFCL V4 methodology — tool/function-calling accuracy, multi-turn behavior, hallucination measurement, format sensitivity.

None is automatically a training source, tuning source, checkpoint-selection source, or release gate.

## 4. Primary research sources

- Hugging Face TRL — SFTTrainer: https://huggingface.co/docs/trl/sft_trainer
- Hugging Face Transformers — Trainer recipes/checkpoint resume: https://huggingface.co/docs/transformers/trainer_recipes
- PyTorch — Reproducibility: https://docs.pytorch.org/docs/stable/notes/randomness.html
- OpenAI — HealthBench: https://openai.com/index/healthbench/
- OpenAI — HealthBench Professional overview: https://openai.com/index/making-chatgpt-better-for-clinicians/
- Berkeley — BFCL V4: https://gorilla.cs.berkeley.edu/leaderboard
- LIMA: https://arxiv.org/abs/2305.11206
- LESS: https://arxiv.org/abs/2402.04333
- Fine-tuning Aligned Language Models Compromises Safety: https://arxiv.org/abs/2310.03693
- MedAraBench: https://arxiv.org/abs/2602.01714
- MedArabiQ: https://arxiv.org/abs/2505.03427
- Cross-Lingual Empirical Evaluation of LLMs for Arabic Medical Tasks: https://arxiv.org/abs/2602.05374
- MedAbstain: https://arxiv.org/abs/2601.12471

## 5. Research disposition

```text
MODEL_PRESELECTION=NO
BACKEND_PRESELECTION=NO
TRAINING_EXECUTION=NO
REAL_DATA_CONSTRUCTION=NO
WEIGHT_ACCESS=NO
TRAINING_AUTHORITY=NONE
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY

P0_PLAN_HARDENING_REQUIRED=
  TOKENIZER_TEMPLATE_IDENTITY,
  LOSS_MASK_POLICY,
  PACKING_TRUNCATION_POLICY,
  FULL_QUARANTINE_SELECTION_FIREWALL,
  ABORT_ONLY_SAFETY_SENTINEL_GATE,
  CAPABILITY_PRESERVATION,
  REPRODUCIBILITY_LEVELS,
  RUN_RESUME_INTEGRITY,
  TOURNAMENT_TO_TRAINING_HANDSHAKE,
  NO_PREAUTHORIZATION_PILOT
```

These findings should be incorporated into clarification and plan before Spec 007 implementation is authorized.
