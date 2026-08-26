# Clarification — Spec 007 SFT V1

**Branch:** `spec/007-clarify-plan-hardening-v2`
**Parent authorization candidate:** PR #47 head `5e8618de32468f04d797117cc46bb2bdf72dd3e1`
**Status:** clarification candidate; merge blocked until clarification authority is canonical
**Model selection authority:** FOUNDER+CHATGPT ONLY
**Execution authority:** NONE

> This artifact clarifies the canonical Spec 007 specification without selecting a model, choosing a training backend, constructing a real dataset, accessing weights, or authorizing training. The parent authorization transition in PR #47 must become canonical before this clarification can be merged as lifecycle evidence.

## 1. Clarification outcome

The specification is materially complete for clarification after the decisions below are adopted. The core SFT objective remains unchanged: produce one minimally adapted, role-aware commandMed candidate while preserving safety, Arabic/English capability, general capability, provenance, quarantine, and frozen evaluation semantics.

The clarification closes training-mechanics ambiguities that would otherwise make two apparently identical SFT runs scientifically incomparable.

## 2. Frozen clarification decisions

### C-001 — Model selection remains outside Pi authority

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
EVIDENCE_KIND=AUTHORIZED_TOURNAMENT_RESULT
```

Pi may build validators, manifests, comparison surfaces, and decision packets. Pi must not choose, rank, eliminate, recommend, or freeze a model lineage.

### C-002 — Base checkpoint binding is broader than model weights

A valid `BaseCheckpointBinding` must eventually bind all of the following before a training activation can pass:

- exact model/checkpoint identity;
- exact model content/weight identity where legally and technically available;
- tokenizer revision/content identity;
- tokenizer configuration identity;
- special-token map identity;
- canonical chat-template identity;
- BOS/EOS policy;
- tool-format/rendering policy;
- model license/lineage evidence;
- tournament qualification evidence;
- release-posture compatibility under FD-001.

All concrete values remain `NEEDS_EVIDENCE` until Founder + ChatGPT select the winner from authorized tournament evidence.

### C-003 — Prompt rendering must be versioned

The same semantic conversation rendered through a different tokenizer/chat template is a different training input.

Freeze a canonical prompt-rendering procedure and identity before any run. It must cover system/user/assistant/tool roles, special tokens, tool schemas, and exact normalization rules.

### C-004 — Loss masking is an explicit training contract

No training backend default may decide which tokens receive gradient.

A versioned `LossMaskPolicy` must define at minimum:

- user-token loss inclusion/exclusion;
- system-token loss inclusion/exclusion;
- assistant-token loss inclusion;
- tool-call argument-token handling;
- tool-result-token handling;
- structured-output token handling;
- any safety-control token handling;
- deterministic mask-generation identity.

The plan must provide fixtures proving the intended mask on representative multi-turn examples.

### C-005 — Packing and truncation are safety-relevant

Packing is optional and may be enabled only when the selected backend proves example-boundary semantics compatible with the frozen contract.

Truncation must never silently remove:

- system safety context;
- user facts required to interpret the target;
- tool schema needed for the target tool call;
- emergency/escalation context;
- the supervised assistant target;
- provenance/classification metadata needed for admission.

Unsafe-to-represent examples are rejected or deterministically segmented with a reason code.

### C-006 — Curriculum readiness is not a row-count threshold

Curriculum readiness is determined by frozen coverage/quality criteria, not by a minimum number of examples alone.

Required reporting dimensions:

- role-class coverage;
- curriculum-domain coverage;
- Arabic/English and dialect/code-switch coverage;
- provenance completeness;
- verification/review state;
- contamination status;
- exact/near-duplicate status;
- rendered-token contribution;
- safety/abstention/tool/multi-turn coverage.

Any future numeric minimums are planning-stage evidence records, not invented during clarification.

### C-007 — Multi-turn behavior is first-class SFT scope

SFT V1 must be capable of representing and evaluating multi-turn trajectories, including:

- context seeking;
- acquiring missing information;
- evidence retrieval;
- tool use;
- abstention;
- escalation;
- emergency handling;
- continuation after a tool result;
- rejection of unavailable/nonexistent tools.

Single-turn QA alone cannot satisfy Spec 007.

### C-008 — Tool-use training must preserve the Spec 006 authority boundary

A supervised target may teach when/how to call an allowed tool, but must not train the model to replace authoritative deterministic calculations, schemas, validated scores, or interaction/drug lookups.

Tool-call examples must bind the tool schema/version and distinguish:

- valid tool selection;
- invalid argument structure;
- nonexistent tool hallucination;
- unavailable tool;
- conflicting tool results;
- spoofed tool output;
- required abstention/escalation.

### C-009 — Arabic coverage has richer metadata than `language=ar`

Arabic examples must support, where applicable:

- original language;
- translation/transcreation status;
- dialect/register;
- MSA vs Saudi/Gulf colloquial;
- English-Arabic code switching;
- transliteration status;
- medication/terminology normalization identity;
- reviewer/clinical-review evidence.

Arabic validity cannot be inferred from machine translation alone.

### C-010 — Arabic tokenizer efficiency is part of future model evidence

The future Founder + ChatGPT model-selection packet must include tokenizer-efficiency evidence over matched medical-language samples. At minimum:

- tokens per word / characters per token;
- medication-name fragmentation;
- clinical-term fragmentation;
- MSA;
- Saudi/Gulf colloquial;
- code-switching;
- transliterated medical terms.

This is evidence for selection, not a decision rule delegated to Pi.

### C-011 — Safety preservation uses an abort-only, quarantine-clean sentinel path

The complete canonical quarantine source matrix defined by `eval_contract.validate` / its frozen quarantine data is authoritative. Every asset governed by that matrix is excluded from SFT curriculum construction, gradient-bearing training, monitoring that can influence optimization, early stopping, hyperparameter/recipe selection, checkpoint selection, model selection, and every other tuning or selection surface unless the canonical purpose→allowed-sources policy explicitly permits that exact purpose. Spec 007 is stricter for SFT tuning surfaces: the sources explicitly named by FR-003 — `COMMANDMED_CLINICAL_GOLD`, `COMMANDMED_ARABIC_GOLD`, `COMMANDMED_MULTIMODAL_GOLD`, `CALIBRATION_HOLD_OUT_SPLIT`, `MODEL_SELECTION_DEV_SET`, `PUBLIC_BENCHMARK_DEV_SPLITS`, `HELD_OUT_SYNTHETIC_PILOT_CASES`, `VERIFIED_DEV_SPLIT` — plus every additional source identifier in the same frozen matrix (including public canonical-test sources) must not influence SFT recipe/checkpoint/tuning decisions. `CALIBRATION_HOLD_OUT_SPLIT` remains calibration-only.

A future authorized run may optionally use a separately identity-bound `SFT_ABORT_SENTINEL_SET` only when all of the following are proven before activation:

- its source identities are not members of the canonical quarantine-controlled source set for a prohibited SFT tuning purpose;
- provenance, license, split, contamination, and source-verification state pass Spec 003;
- it is excluded from gradient-bearing curriculum/training data;
- its thresholds and behavior are frozen pre-run;
- it is **abort/disqualify-only**: it may terminate or invalidate an unsafe run, but it must not rank checkpoints, choose a recipe, alter hyperparameters, drive early stopping toward a preferred checkpoint, or select a model.

If no such permissible abort-only sentinel can be established, intra-run safety monitoring does not become an exception to quarantine. The run follows its pre-registered schedule and final qualification occurs only after checkpoint choice is frozen by a quarantine-safe rule.

### C-012 — Capability preservation is explicit

A `CapabilityPreservationBinding` must eventually cover:

- general reasoning;
- instruction following;
- Arabic;
- tool use;
- uncertainty/abstention;
- safety;
- frozen medical strata.

The plan must distinguish abort-only, quarantine-clean drift detection from final qualification. No canonical quarantined source may influence optimization or checkpoint/recipe selection merely because it is labeled a development slice.

### C-013 — Checkpoint selection must be pre-registered and enforce the complete quarantine firewall

The complete canonical quarantine-controlled source set is prohibited from influencing:

- checkpoint ranking or selection;
- hyperparameter selection;
- recipe/update-strategy selection;
- early stopping toward a preferred checkpoint;
- model selection;
- any other SFT tuning or selection surface.

This prohibition includes the FR-003 sources `COMMANDMED_CLINICAL_GOLD`, `COMMANDMED_ARABIC_GOLD`, `COMMANDMED_MULTIMODAL_GOLD`, `CALIBRATION_HOLD_OUT_SPLIT`, `MODEL_SELECTION_DEV_SET`, `PUBLIC_BENCHMARK_DEV_SPLITS`, `HELD_OUT_SYNTHETIC_PILOT_CASES`, `VERIFIED_DEV_SPLIT`, and all other members of the frozen canonical matrix. A purpose label such as `DEV` or `CHECKPOINT_SELECTION` does not override Spec 007's stricter structural exclusion for SFT tuning surfaces.

Therefore the pre-run `CheckpointSelectionPolicy` must use one of these fail-closed forms:

1. a deterministic fixed checkpoint rule frozen before training (for example, the final checkpoint at a pre-registered step/token budget), with no evaluation asset used to rank checkpoints; or
2. a separately authorized, identity-bound selection evidence source that is demonstrably outside the prohibited canonical quarantine set for the intended SFT selection purpose and is admitted under an explicit canonical policy added before the run.

Until option 2 exists canonically, option 1 is the default. Abort-only sentinels from C-011 cannot rank checkpoints or recipes. Training/evaluation loss alone cannot silently create a selection exception.

### C-014 — Reproducibility has two levels

`EXACT_ENVIRONMENT_REPLAY` means reproducibility within the same fully pinned environment to the strongest level supported by the chosen framework/hardware.

`CROSS_ENVIRONMENT_REPRODUCIBILITY` means behavior/statistical equivalence across explicitly allowed equivalent environments.

Bitwise-identical weights across different GPU stacks are not assumed.

Required environment identity includes framework/backend versions, device identity, attention/kernel backend, precision, seeds/data seed, data order, and training-state identities.

### C-015 — Resume integrity is mandatory for resumable checkpoints

A resumable training checkpoint must bind:

- model/adapter state;
- optimizer state;
- scheduler state;
- gradient scaler if used;
- RNG state;
- data cursor/order;
- global step;
- configuration identity;
- dataset snapshot identity;
- base checkpoint identity;
- tokenizer/template identities.

A model-only export is not a resumable checkpoint.

### C-016 — Backend remains unselected during clarification

The plan must be expressible independently of TRL, PEFT, Axolotl, Unsloth, Liger, or any other training stack.

Backend selection occurs later through a versioned compatibility/evidence record after the winning model and intended hardware are known.

No backend may change the frozen loss mask, chat rendering, packing/truncation semantics, or resume contract without creating a new recipe identity.

### C-017 — LoRA/QLoRA/full-update mode remains a later evidence decision

No update strategy is selected by clarification.

Before the first authorized training run, the update-strategy decision may use only non-executing evidence available without model execution: winner architecture support, documented adapter/full-update compatibility, static memory/compute estimates, intended deployable-artifact needs, reproducibility requirements, license implications, and backend conformance evidence. Empirical convergence, gradient, loss-curve, or model-output evidence is not a prerequisite unless it was produced by a separately authorized training execution under all applicable gates.

Any later pilot or gradient-bearing experiment used to compare `FULL`, `LORA`, `QLORA`, or another strategy is itself a training run for authority purposes and cannot occur before training authority. Its results also cannot influence recipe/hyperparameter/checkpoint selection unless a separately authorized policy satisfies the full FR-003 quarantine firewall.

### C-018 — Mutable medical truth should not be baked into weights by default

Curriculum admission must distinguish durable knowledge/behavior from content better owned by evidence/retrieval/tools due to temporal, local, or jurisdictional mutability.

Examples of usually mutable content include current guidelines, formularies, local pathways, service routing, and rapidly changing evidence.

### C-019 — Abstention is a dedicated curriculum/evaluation slice

SFT V1 must include explicit targets for correct non-answer behavior under:

- missing information;
- contradiction;
- unsupported/OOD request;
- insufficient evidence;
- ambiguous risk;
- safety-policy conflict.

`ASK_MORE`, `ABSTAIN`, `ESCALATE`, and `EMERGENCY` are valid positive targets when appropriate.

### C-020 — Open-ended medical evaluation complements deterministic tasks

The plan may use realistic open-ended/multi-turn evaluation references such as HealthBench/HealthBench Professional after exact identity/license/contamination review.

An LLM judge cannot become the sole authority for medical truth. Judge-based evaluation requires evaluator validation and must remain subordinate to deterministic hard gates and appropriately qualified human/clinical evidence.

### C-021 — Arabic external benchmarks are evaluation candidates only

MedAraBench and MedArabiQ may be considered for development/evaluation after exact version, license, split, and contamination review.

They are not automatically curriculum sources and are not automatically release gates.

### C-022 — Memorization/regurgitation needs a pre-run audit plan

The future dataset/recipe plan must include:

- exact duplicate detection;
- near-duplicate detection;
- benchmark overlap checks;
- repeated-record detection;
- safe synthetic canaries where useful;
- bounded regurgitation probes.

No PHI, credentials, secrets, or restricted content may be used as memorization canaries.

### C-023 — Tournament-to-training handshake is explicit and contains no pre-authorized pilot

The lifecycle before the first gradient update is frozen as:

```text
OFFLINE SFT INFRASTRUCTURE QUALIFIED
-> FOUNDER+CHATGPT CANDIDATE MANIFEST FREEZE
-> SEPARATE TOURNAMENT EXECUTION AUTHORIZATION
-> AUTHORIZED TOURNAMENT EXECUTION
-> EVIDENCE PACK RETURNED
-> FOUNDER+CHATGPT BACKBONE WINNER DECISION
-> BASE CHECKPOINT BINDING CANONICAL
-> NON_EXECUTING_RECIPE_EVIDENCE_FROZEN
-> DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
-> TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
-> FIRST TRAINING RUN
```

`NON_EXECUTING_RECIPE_EVIDENCE` is limited to static/control-plane evidence obtainable without loading model weights or performing gradient-bearing work: schema completeness, backend/model compatibility declarations, rendering/loss-mask/packing/truncation conformance contracts, static compute/resource estimates, provenance/quarantine bindings, environment identity, and other non-executing preflight evidence. It does not include loss curves, gradient behavior, convergence, model outputs, benchmark results, or any empirical evidence that requires model execution.

Any experiment called a pilot, smoke-train, adapter pilot, one-step train, gradient probe, or equivalent is a training run for authority purposes. It must occur only after model/weight/data/device/finance/training authorities applicable to that run are canonical. Its results cannot select recipe/hyperparameters/checkpoints unless a separately authorized policy also satisfies the complete FR-003 quarantine firewall.

Spec 007 planning and offline implementation may prepare for these gates, but cannot silently satisfy them.

## 3. Typed unresolved prerequisites

The following remain unresolved by design:

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

## 4. Clarification exit check

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

AMBIGUOUS_TRAINING_MECHANICS_CLOSED=
  TOKENIZER_TEMPLATE,
  LOSS_MASKING,
  PACKING_TRUNCATION,
  MULTI_TURN_TOOL_USE,
  SAFETY_MONITORING,
  CAPABILITY_PRESERVATION,
  FULL_QUARANTINE_SELECTION_FIREWALL,
  REPRODUCIBILITY,
  RESUME_INTEGRITY,
  ARABIC_METADATA,
  KNOWLEDGE_PLACEMENT,
  MEMORIZATION_AUDIT,
  TOURNAMENT_TO_TRAINING_HANDSHAKE,
  NO_PREAUTHORIZATION_PILOT
```

Planning must implement these decisions without expanding into actual model selection or training execution.
