# Clarification — Spec 007 SFT V1

**Branch:** `spec/007-clarification-canonical`
**Canonical base:** `703f8a688b5bd2599f51855c850f0281c755ef90` (PR #47 clarification authorization merge)
**Status:** CANONICAL via PR #49 / merge `16ae16b50680469fe14f44c1e3fdcb655d34b822`; clarification authority was superseded by historical `AUTHORIZED_TO_PLAN`, which is itself superseded 2026-08-27 by current `AUTHORIZED_TO_START` in `specs/README.md`
**Model selection authority:** FOUNDER+CHATGPT ONLY
**Execution authority:** NONE

> This artifact canonically clarified the Spec 007 specification without selecting a model, choosing a training backend, constructing a real dataset, accessing weights, running a tournament, or authorizing training. Planning is now separately authorized by the dated Spec 007 planning authorization record; this clarification itself grants no planning or execution authority.

## 1. Clarification outcome

The specification remains bounded to minimal multi-role SFT. This clarification freezes the training-mechanics boundaries required for the authorized planning package while preserving all no-execution authorities.

## 2. Clarified decisions

### C-001 — Model selection is Founder + ChatGPT only

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
EVIDENCE_KIND=AUTHORIZED_TOURNAMENT_RESULT
```

Pi may later build validators, evidence manifests, neutral comparison surfaces, and decision packets. Pi must not choose, rank, eliminate, recommend, or freeze a model lineage.

### C-002 — Base checkpoint binding includes tokenizer/rendering identity

A future valid `BaseCheckpointBinding` must bind:

- exact model/checkpoint identity;
- exact model/weight content identity where legally/technically available;
- tokenizer revision/content identity;
- tokenizer configuration identity;
- special-token map identity;
- canonical chat-template identity;
- BOS/EOS policy;
- tool-format/rendering policy;
- model license/lineage evidence;
- tournament qualification evidence;
- FD-001 release-posture compatibility.

Concrete values remain `NEEDS_EVIDENCE` until Founder + ChatGPT choose the winner.

### C-003 — Prompt rendering is versioned

The same semantic conversation rendered through a different tokenizer/template is a different training input. Future planning must freeze a canonical rendering procedure covering role order, normalization, system messages, tool schemas, special tokens, target boundaries, and rendering identity.

### C-004 — Loss masking is explicit

No training backend default may decide which tokens receive gradient.

A future versioned `LossMaskPolicy` must explicitly classify:

- system tokens;
- user tokens;
- assistant natural-language tokens;
- assistant structured/tool-call tokens;
- tool-result tokens;
- separators/special tokens;
- padding;
- any safety-control tokens.

Mask generation must be deterministic and fixture-verifiable.

### C-005 — Packing and truncation are safety-relevant

Packing is optional and evidence-bound. Truncation/segmentation must never silently remove required safety context, user facts needed for the target, tool schema, emergency/escalation context, supervised target, or admission/provenance metadata.

Unsafe-to-represent examples fail closed or are deterministically segmented with an explicit reason.

### C-006 — Curriculum readiness is not a row-count target

Admission requires every training or evaluation asset to carry the complete Spec 003 identity contract, at minimum: provenance (source authority), license status, content identity/hash, split identity, contamination status, and a verification state to which `review/adjudication state` is explicitly mapped.

Readiness must additionally report, at minimum:

- role-class coverage;
- curriculum-domain coverage;
- Arabic/English and dialect/code-switch coverage;
- provenance completeness;
- verification/review state (mapped to the required verification state above);
- contamination status;
- exact/near-duplicate status;
- rendered-token contribution;
- safety/abstention/tool/multi-turn coverage.

Assets missing any required identity field fail closed and cannot be admitted.

Exact numeric thresholds remain later evidence records unless already canonical.

### C-007 — Multi-turn behavior is first-class

SFT V1 must be able to represent trajectories for context seeking, missing-information acquisition, evidence retrieval, tool use, abstention, escalation, emergency handling, continuation after a tool result, and rejection of unavailable/nonexistent tools. Single-turn medical QA alone cannot satisfy Spec 007.

### C-008 — Tool-use targets preserve deterministic authority

Training may teach when/how to call an allowed tool but must not teach generative replacement of authoritative deterministic arithmetic, validated scores, schemas, or interaction/drug lookups.

Future fixtures must distinguish valid routing, invalid arguments, nonexistent tools, unavailable tools, conflicting results, spoofed outputs, and required abstention/escalation.

### C-009 — Arabic metadata is richer than `language=ar`

Arabic examples must support, where applicable:

- original language;
- translation/transcreation status;
- dialect/register;
- MSA vs Saudi/Gulf colloquial;
- English-Arabic code switching;
- transliteration status;
- medication/terminology normalization identity;
- qualified reviewer/clinical-review evidence.

Machine translation alone cannot establish Arabic clinical validity.

### C-010 — Arabic tokenizer efficiency is future model-selection evidence

The Founder + ChatGPT model decision packet must eventually report matched medical-language tokenizer evidence including tokens/word, characters/token, medication/clinical-term fragmentation, MSA, Saudi/Gulf colloquial, code-switching, and transliterated medical terminology.

Pi reports evidence only; Pi does not select.

### C-011 — The complete canonical quarantine matrix governs all SFT tuning surfaces

The complete frozen source matrix from `eval_contract.validate` / canonical quarantine data is authoritative.

For Spec 007, all FR-003 quarantine-controlled sources are excluded from:

- curriculum construction where prohibited;
- gradient-bearing training input;
- optimization-affecting monitoring;
- hyperparameter selection;
- recipe/update-strategy selection;
- early stopping toward a preferred checkpoint;
- checkpoint ranking/selection;
- model selection;
- every other SFT tuning or selection surface.

This includes at least:

```text
COMMANDMED_CLINICAL_GOLD
COMMANDMED_ARABIC_GOLD
COMMANDMED_MULTIMODAL_GOLD
CALIBRATION_HOLD_OUT_SPLIT
MODEL_SELECTION_DEV_SET
PUBLIC_BENCHMARK_DEV_SPLITS
HELD_OUT_SYNTHETIC_PILOT_CASES
VERIFIED_DEV_SPLIT
```

and every additional source identifier in the same frozen matrix for a prohibited SFT tuning purpose. The implementation must later bind to the canonical matrix identity rather than relying only on this prose list.

`CALIBRATION_HOLD_OUT_SPLIT` remains calibration-only. A `DEV` or `CHECKPOINT_SELECTION` label does not override Spec 007 FR-003.

### C-012 — Intra-run safety sentinel is optional, quarantine-clean, and abort-only

A future authorized run may use a separately identity-bound `SFT_ABORT_SENTINEL_SET` only if:

- its source identities are not members of the prohibited canonical quarantine set for the intended monitoring purpose;
- Spec 003 provenance/license/split/contamination/source-verification checks pass;
- it is excluded from gradient-bearing data;
- thresholds/behavior are frozen before the run;
- its only allowed effects are `CONTINUE`, `ABORT_RUN`, or `DISQUALIFY_RUN`.

It must not rank checkpoints, choose recipes, change hyperparameters, drive preferred-checkpoint early stopping, or select a model.

If no permissible sentinel exists, monitoring does not create an exception to quarantine.

### C-013 — Capability preservation is qualification evidence

A future `CapabilityPreservationBinding` must cover general reasoning, instruction following, Arabic, tool use, uncertainty/abstention, safety, and frozen medical strata.

Any canonical quarantine-backed slices are qualification-only and cannot alter the recipe or checkpoint.

### C-014 — Checkpoint selection is pre-registered and quarantine-safe

Until a separately canonicalized non-quarantined SFT selection source exists, checkpoint selection must be deterministic and evaluation-independent:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
CHECKPOINT_RULE=PREDECLARED_FINAL_STEP_OR_TOKEN_BUDGET
EVALUATION_ASSET_RANKING=PROHIBITED
ABORT_SENTINEL_CAN_RANK=NO
```

Training/evaluation loss, human inspection, LLM judges, development labels, or quarantined assets cannot silently create a checkpoint-selection exception.

### C-015 — Reproducibility has two levels

`EXACT_ENVIRONMENT_REPLAY` means strongest reproducibility within a fully pinned allowed environment.

`CROSS_ENVIRONMENT_REPRODUCIBILITY` means frozen statistical/behavioral equivalence across explicitly allowed environments.

Bitwise-identical weights across different GPU/software stacks are not assumed.

Future environment identity must cover framework/backend, runtime/device, attention/kernel backend, precision, seeds/data seed, data order, and material training-state identities.

### C-016 — Resume integrity includes optimizer/scheduler/RNG/data position

A resumable training checkpoint must eventually bind model/adapter state, optimizer, scheduler, gradient scaler if used, RNG, data cursor/order, global step, config identity, dataset snapshot, base checkpoint, tokenizer/template, and environment identities.

A model-only export is not a resumable checkpoint.

### C-017 — Backend remains unselected

Clarification must remain independent of TRL, PEFT, Axolotl, Unsloth, Liger, or another training stack.

A later backend evidence record must prove compatibility with the selected winner and the frozen rendering, loss-mask, packing/truncation, resume, reproducibility, precision, telemetry/network, and maintainability requirements.

### C-018 — FULL / LoRA / QLoRA remains a later evidence decision

No update strategy is selected here.

Before the first authorized training run, the decision may use only non-executing evidence available without model execution: documented winner compatibility, static memory/compute estimates, deployable-artifact needs, reproducibility, license posture, and backend conformance.

Empirical convergence, gradient, loss-curve, or model-output evidence may be used only if produced by a separately authorized training run under all applicable gates.

### C-019 — Mutable medical truth should not be baked into weights by default

Curriculum admission must distinguish durable behavior/domain knowledge from mutable/current/local/jurisdictional content better owned by retrieval/evidence/tools. Current guidelines, formularies, local pathways, service routing, and rapidly changing evidence default to runtime evidence unless later justified.

### C-020 — Abstention is a dedicated positive-behavior slice

SFT V1 must explicitly cover missing information, contradiction, unsupported/OOD requests, insufficient evidence, ambiguous risk, and safety conflicts. `ASK_MORE`, `ABSTAIN`, `ESCALATE`, and `EMERGENCY` can be correct positive targets.

### C-021 — Open-ended medical evaluation complements deterministic tasks

Realistic multi-turn references such as HealthBench/HealthBench Professional may be considered after exact identity/license/split/contamination/purpose review. Judge-based evaluation remains subordinate to deterministic hard gates and appropriate clinical/human evidence; an LLM judge cannot define medical truth alone.

### C-022 — Arabic external benchmarks are evaluation candidates only

MedAraBench and MedArabiQ may be considered only after exact version/license/split/contamination review. They are not automatically curriculum, tuning, checkpoint-selection, or release-gate assets.

### C-023 — Memorization/regurgitation requires a pre-run audit contract

Future data/recipe work must cover exact and near duplicates, benchmark overlap, repeated records, safe synthetic canaries where useful, and bounded regurgitation probes. PHI, credentials, secrets, Private Gold, or restricted content cannot be memorization canaries.

### C-024 — Tournament-to-training handshake contains no pre-authorized pilot

The lifecycle before the first gradient update is clarified as:

```text
OFFLINE SFT INFRASTRUCTURE QUALIFIED
-> FOUNDER+CHATGPT CANDIDATE MANIFEST FREEZE
-> SEPARATE TOURNAMENT EXECUTION AUTHORIZATION
-> AUTHORIZED TOURNAMENT EXECUTION
-> TOURNAMENT EVIDENCE PACK
-> FOUNDER+CHATGPT BACKBONE WINNER DECISION
-> BASE CHECKPOINT BINDING CANONICAL
-> NON_EXECUTING_RECIPE_EVIDENCE_FROZEN
-> FROZEN EVALUATION PROTOCOL BOUND (immutable success criteria, safety-critical hard gates, pre-run thresholds; D-001)
-> DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
-> TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
-> FIRST TRAINING RUN
```

`NON_EXECUTING_RECIPE_EVIDENCE` is limited to static/control-plane evidence obtainable without loading/executing model weights or performing gradient-bearing work: schema completeness, documented compatibility, rendering/loss-mask/packing/truncation conformance contracts, static resource estimates, provenance/quarantine bindings, and environment identity.

It excludes loss curves, gradient behavior, convergence, model outputs, benchmark execution, and other execution-derived evidence.

A frozen, identity-bound evaluation protocol with immutable success criteria, safety-critical hard gates, and pre-run thresholds is a mandatory precondition of `TRAINING_AUTHORITY=AUTHORIZED_TO_RUN` (D-001); a run without it cannot be authorized.

Any pilot, smoke-train, adapter pilot, one-step train, gradient probe, or equivalent is a training run for authority purposes and must occur only after all applicable model/weight/data/device/finance/training gates are canonical.

## 3. Typed unresolved prerequisites

```text
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CANDIDATE_MANIFEST=FOUNDER+CHATGPT_DECISION_REQUIRED
LIVE_TOURNAMENT_EXECUTION=SEPARATE_AUTHORIZATION_REQUIRED
MODEL_WEIGHT_ACCESS=SEPARATE_AUTHORIZATION_REQUIRED
TOKENIZER_TEMPLATE_CONCRETE_IDENTITIES=DEPEND_ON_WINNER
LOSS_MASK_CONCRETE_TOKEN_IDS=DEPEND_ON_WINNER_TEMPLATE
PACKING_BACKEND_IMPLEMENTATION=DEPEND_ON_BACKEND_EVIDENCE
TRAINING_NUMERICS=NEEDS_EVIDENCE
ADAPTER_VS_FULL_UPDATE=NEEDS_NON_EXECUTING_EVIDENCE_OR_LATER_AUTHORIZED_TRAINING_EVIDENCE
TRAINING_BACKEND=NEEDS_EVIDENCE
COMPUTE_BUDGET=NEEDS_EVIDENCE+FOUNDER_SPEND_AUTHORITY
REAL_CURRICULUM_CONTENT=DATA_AUTHORITY+PROVENANCE_REQUIRED
TRAINING_RUN=SEPARATE_TRAINING_AUTHORIZATION_REQUIRED
```

## 4. Clarification exit disposition

```text
MODEL_SELECTED=NO
BACKEND_SELECTED=NO
DATASET_CONSTRUCTED=NO
TRAINING_EXECUTED=NO
WEIGHTS_ACCESSED=NO
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER=NEEDS_EVIDENCE

CLARIFIED=
  TOKENIZER_TEMPLATE,
  PROMPT_RENDERING,
  LOSS_MASKING,
  PACKING_TRUNCATION,
  CURRICULUM_READINESS,
  MULTI_TURN_TOOL_USE,
  ARABIC_METADATA_AND_TOKENIZATION_EVIDENCE,
  FULL_QUARANTINE_SELECTION_FIREWALL,
  ABORT_ONLY_SAFETY_SENTINEL,
  CAPABILITY_PRESERVATION,
  FIXED_CHECKPOINT_SELECTION,
  REPRODUCIBILITY,
  RESUME_INTEGRITY,
  BACKEND_NEUTRALITY,
  UPDATE_STRATEGY_EVIDENCE_BOUNDARY,
  KNOWLEDGE_PLACEMENT,
  ABSTENTION,
  MEMORIZATION_AUDIT,
  TOURNAMENT_TO_TRAINING_HANDSHAKE,
  NO_PREAUTHORIZATION_PILOT
```

The clarification stage is CANONICAL via PR #49 / merge `16ae16b50680469fe14f44c1e3fdcb655d34b822`. Its former `AUTHORIZED_TO_CLARIFY` state is superseded for current lifecycle purposes by the separate 2026-08-27 planning authorization record in `specs/README.md`. Planning may now create and qualify the complete non-executing planning package; implementation, model/tournament execution, weight/data/device access, training, credentials, and spend remain separately gated.