# Research — Spec 007 SFT V1 hardening

**Branch:** `spec/007-clarification-canonical`
**Canonical base:** `703f8a688b5bd2599f51855c850f0281c755ef90` (PR #47 clarification authorization merge)
**Lifecycle authority:** `AUTHORIZED_TO_CLARIFY`
**Execution authority:** NONE
**Model selection authority:** FOUNDER+CHATGPT ONLY

> This research supports the bounded Spec 007 clarification stage. It does not create planning authority, select a model, choose a training backend, construct a real training dataset, access weights, run a tournament, execute training, access Gold/PHI, or authorize spend. Concrete backbone identity remains `BACKBONE_WINNER=NEEDS_EVIDENCE` until Founder + ChatGPT bind an authorized tournament result.

## 1. Purpose

The canonical specification is strong on provenance, quarantine, safety composition, role classes, and evaluation-before-training. The clarification research closes technical ambiguities that could otherwise make two nominally identical SFT runs scientifically incomparable or allow hidden optimization leakage.

Required outcomes remain:

- model-neutral;
- backend-neutral;
- fail-closed at the control-plane layer;
- realistic about GPU reproducibility;
- compatible with the three frozen role classes;
- safe for multi-turn/tool-use behavior;
- quarantine-clean across all optimization-affecting surfaces.

## 2. Research findings

### R-001 — Tokenizer and chat-template identity are training inputs

A checkpoint identifier alone does not reproduce conversational SFT. Rendering depends on tokenizer files/configuration, special-token mapping, chat template, BOS/EOS behavior, tool formatting, and normalization.

**Clarification requirement:** future `BaseCheckpointBinding` / training records must bind exact tokenizer revision/content identity, tokenizer config, special-token map, chat-template identity, BOS/EOS policy, tool-format policy, and prompt-rendering version.

A tokenizer/template change creates a new recipe identity.

Reference: Hugging Face TRL conversational SFT/chat-template mechanics.

### R-002 — Loss masking cannot be a trainer default

Whole-sequence, completion-only, assistant-only, and tool-call masking are materially different objectives.

**Clarification requirement:** freeze a versioned `LossMaskPolicy` covering user/system/assistant/tool-call/tool-result/structured-output/special/padding token classes and deterministic mask-generation identity. Future fixtures must prove intended boundaries.

### R-003 — Packing and truncation are safety-relevant

Packing can improve utilization, but boundary mistakes can leak attention/labels across examples. Truncation can silently delete safety/tool context or the supervised target.

**Clarification requirement:** packing remains optional and evidence-bound; truncation must fail closed rather than silently remove required system safety context, user facts, tool schema, emergency/escalation context, target completion, or admission metadata.

### R-004 — Curriculum quality is multidimensional

The repository's preference for fewer verified examples over noisy scale is consistent with evidence such as LIMA and targeted data-selection research. No particular algorithm should become mandatory by fashion.

**Clarification requirement:** readiness depends on role/domain/language coverage, provenance, review state, contamination, novelty/duplicates, rendered-token contribution, and safety/abstention/tool/multi-turn coverage—not row count alone.

### R-005 — Multi-turn and tool behavior are first-class

Health interactions require information acquisition, evidence/tool routing, abstention, escalation, and continuation after tool results.

**Clarification requirement:** represent and test trajectories including `ASK_MORE`, `RETRIEVE_EVIDENCE`, `USE_TOOL`, unavailable/nonexistent tools, malformed arguments, spoofed/conflicting tool results, and multi-turn drift. BFCL-style dimensions may inform methodology but do not become an automatic release gate.

### R-006 — Safety monitoring must not bypass quarantine

Fine-tuning can degrade aligned behavior, but that does not authorize holdout reuse as optimization feedback.

**Clarification requirement:** the canonical Spec 007 FR-003 quarantine matrix controls monitoring, early stopping, recipe/hyperparameter selection, checkpoint selection, model selection, and all tuning surfaces.

A future run may use an identity-bound `SFT_ABORT_SENTINEL_SET` only if it is demonstrably outside the prohibited canonical quarantine set for that exact purpose, passes Spec 003 provenance/license/split/contamination/source-verification checks, is excluded from gradient-bearing data, has frozen thresholds, and is **abort/disqualify-only**.

It must never rank checkpoints, select a recipe, change hyperparameters, drive preferred-checkpoint early stopping, or select a model.

### R-007 — Catastrophic forgetting needs qualification evidence, not tuning leakage

Capability preservation must cover general reasoning, instruction following, Arabic, tool use, uncertainty/abstention, safety, and core medical strata.

When those slices use canonical quarantine-controlled sources, they are qualification-only and cannot alter the recipe or checkpoint. Any intra-run drift sentinel must independently satisfy R-006.

### R-008 — Checkpoint selection requires the complete FR-003 firewall

The complete canonical source matrix—not a Gold-only subset—must be excluded from SFT selection/tuning surfaces. This includes at least:

- `COMMANDMED_CLINICAL_GOLD`;
- `COMMANDMED_ARABIC_GOLD`;
- `COMMANDMED_MULTIMODAL_GOLD`;
- `CALIBRATION_HOLD_OUT_SPLIT`;
- `MODEL_SELECTION_DEV_SET`;
- `PUBLIC_BENCHMARK_DEV_SPLITS`;
- `HELD_OUT_SYNTHETIC_PILOT_CASES`;
- `VERIFIED_DEV_SPLIT`;
- every additional source identifier governed by the frozen matrix for a prohibited SFT tuning purpose.

`CALIBRATION_HOLD_OUT_SPLIT` remains calibration-only.

**Clarification requirement:** until a separately canonicalized non-quarantined SFT selection source exists, checkpoint choice is fixed pre-run (for example, final checkpoint at a pre-registered step/token budget) with no evaluation asset used to rank checkpoints.

### R-009 — GPU reproducibility must have explicit levels

PyTorch does not guarantee full reproducibility across releases/platforms/hardware even with identical seeds.

**Clarification requirement:** distinguish:

- `EXACT_ENVIRONMENT_REPLAY` — strongest reproducibility inside a fully pinned allowed environment;
- `CROSS_ENVIRONMENT_REPRODUCIBILITY` — frozen statistical/behavioral equivalence across explicitly allowed environments.

No cross-stack bitwise-weight identity claim is assumed.

Environment identity must include framework/backend, runtime, device, kernel/attention backend, precision, seeds/data seed, data order, and material training-state identities.

### R-010 — Resume integrity includes training state

A model-only export cannot reproduce an interrupted training trajectory.

**Clarification requirement:** resumable checkpoints bind model/adapter, optimizer, scheduler, scaler if applicable, RNG state, data cursor/order, global step, config, base checkpoint, dataset snapshot, tokenizer/template, and environment identities.

### R-011 — Arabic tokenizer efficiency belongs in future model evidence

Arabic medical performance can be harmed by inefficient fragmentation. The future Founder + ChatGPT candidate packet should therefore include matched Arabic/English tokenizer measurements: tokens/word, characters/token, medication/clinical-term fragmentation, MSA, Saudi/Gulf colloquial, code-switching, and transliterated medical terminology.

These are evidence inputs; Pi does not choose the model.

### R-012 — Arabic provenance is richer than `language=ar`

Arabic curriculum records should support original language, translation/transcreation status, dialect/register, code-switching, transliteration, terminology-normalization identity, and qualified review evidence where applicable. Machine translation alone cannot establish Arabic clinical validity.

### R-013 — Mutable medical truth belongs in runtime evidence where practical

AGENTS.md already requires mutable medical truth to remain in evidence/retrieval/tool layers where practical.

**Clarification requirement:** classify candidate curriculum knowledge as durable weight-eligible behavior/domain knowledge, mutable runtime-evidence-preferred content, or rejected content.

### R-014 — Backend neutrality should survive clarification

TRL/Transformers, PEFT, Axolotl, Unsloth, Liger, or another stack may eventually be appropriate, but clarification must not preselect one.

A later backend evidence record must prove winner architecture/template support, loss-mask semantics, packing/truncation conformance, resume integrity, reproducibility controls, required precision/update strategy, and absence of unauthorized telemetry/network/provider dependencies.

### R-015 — Open-ended health evaluation complements deterministic scoring

HealthBench / HealthBench Professional are useful research candidates for realistic multi-turn and clinician-workflow behavior. They require exact identity/license/split/contamination/purpose review before use.

An LLM judge cannot be the sole medical-truth authority, and admission as evaluation evidence never makes an asset eligible for checkpoint/recipe tuning.

### R-016 — Abstention is a dedicated positive-behavior slice

SFT V1 needs explicit coverage of missing information, contradictions, ambiguity, OOD/unsupported requests, insufficient evidence, `ASK_MORE`, `ABSTAIN`, `ESCALATE`, and `EMERGENCY`.

Correct non-answer behavior is not a failure merely because no answer is produced.

### R-017 — Memorization/regurgitation needs a pre-run audit contract

Future data activation must include exact/near duplicate detection, repeated-record detection, benchmark-overlap checks, safe synthetic canaries where useful, and bounded regurgitation probes. PHI, credentials, secrets, Private Gold, or restricted content cannot be canaries.

### R-018 — There is no pre-authorized training pilot

The pre-training lifecycle must not imply that empirical pilot evidence is available before training authority.

Clarified sequence:

```text
OFFLINE SFT INFRASTRUCTURE QUALIFIED
-> FOUNDER+CHATGPT CANDIDATE MANIFEST FREEZE
-> SEPARATE TOURNAMENT EXECUTION AUTHORIZATION
-> AUTHORIZED TOURNAMENT EXECUTION
-> TOURNAMENT EVIDENCE PACK
-> FOUNDER+CHATGPT BACKBONE WINNER DECISION
-> BASE CHECKPOINT BINDING CANONICAL
-> NON_EXECUTING_RECIPE_EVIDENCE_FROZEN
-> DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
-> TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
-> FIRST TRAINING RUN
```

`NON_EXECUTING_RECIPE_EVIDENCE` means static/control-plane evidence obtainable without loading/executing model weights or performing gradient-bearing work: schema completeness, documented compatibility, rendering/loss-mask/packing/truncation contracts, static resource estimates, provenance/quarantine bindings, and environment identity.

It explicitly excludes loss curves, gradients, convergence, model outputs, benchmark execution, and other execution-derived evidence.

Any pilot, smoke-train, adapter pilot, one-step train, gradient probe, or equivalent is a training run for authority purposes and requires all applicable model/weight/data/device/finance/training gates first.

## 3. External reference candidates

These are evaluation/research candidates only, subject to exact license/identity/split/contamination/purpose review:

- HealthBench;
- HealthBench Professional;
- MedAbstain;
- MedAraBench;
- MedArabiQ;
- BFCL V4 methodology.

None is automatically a training source, tuning source, checkpoint-selection source, or release gate.

## 4. Primary research references

- Hugging Face TRL SFTTrainer: https://huggingface.co/docs/trl/sft_trainer
- Hugging Face Transformers Trainer recipes/checkpoint resume: https://huggingface.co/docs/transformers/trainer_recipes
- PyTorch Reproducibility: https://docs.pytorch.org/docs/stable/notes/randomness.html
- OpenAI HealthBench: https://openai.com/index/healthbench/
- OpenAI HealthBench Professional overview: https://openai.com/index/making-chatgpt-better-for-clinicians/
- Berkeley BFCL V4: https://gorilla.cs.berkeley.edu/leaderboard
- LIMA: https://arxiv.org/abs/2305.11206
- LESS: https://arxiv.org/abs/2402.04333
- Fine-tuning Aligned Language Models Compromises Safety: https://arxiv.org/abs/2310.03693
- MedAraBench: https://arxiv.org/abs/2602.01714
- MedArabiQ: https://arxiv.org/abs/2505.03427
- Cross-Lingual Empirical Evaluation of LLMs for Arabic Medical Tasks: https://arxiv.org/abs/2602.05374
- MedAbstain: https://arxiv.org/abs/2601.12471

## 5. Clarification research disposition

```text
MODEL_PRESELECTION=NO
BACKEND_PRESELECTION=NO
TRAINING_EXECUTION=NO
REAL_DATA_CONSTRUCTION=NO
WEIGHT_ACCESS=NO
TRAINING_AUTHORITY=NONE
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER=NEEDS_EVIDENCE

CLARIFICATION_HARDENING=
  TOKENIZER_TEMPLATE_IDENTITY,
  LOSS_MASK_POLICY,
  PACKING_TRUNCATION_POLICY,
  FULL_QUARANTINE_SELECTION_FIREWALL,
  ABORT_ONLY_SAFETY_SENTINEL_GATE,
  CAPABILITY_PRESERVATION,
  REPRODUCIBILITY_LEVELS,
  RUN_RESUME_INTEGRITY,
  ARABIC_PROVENANCE_AND_TOKENIZATION_EVIDENCE,
  BACKEND_NEUTRALITY,
  MEMORIZATION_AUDIT,
  TOURNAMENT_TO_TRAINING_HANDSHAKE,
  NO_PREAUTHORIZATION_PILOT
```

These findings constrain the later, separately authorized planning stage; they do not themselves authorize planning or implementation.