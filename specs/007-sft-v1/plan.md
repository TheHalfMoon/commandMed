# Plan — Spec 007 SFT V1 (Training-Grade Hardening)

**Branch:** `spec/007-clarify-plan-hardening-v2`
**Parent authorization candidate:** PR #47 head `5e8618de32468f04d797117cc46bb2bdf72dd3e1`
**Specification:** canonical via PR #46 / merge `645da20263fc44d1ed8977024cf2df57aa6f7465`
**Status:** planning candidate created from Founder-directed gap review; merge/canonicalization remains lifecycle-gated
**Execution authority:** NONE
**Training authority:** NONE
**Model selection authority:** FOUNDER+CHATGPT ONLY

> This plan converts Spec 007 into a training-grade control and implementation plan without selecting a model, backend, dataset, optimizer values, adapter strategy, or training budget. It prepares deterministic/offline infrastructure and explicit future gates. No model weight access, live tournament, training run, Private Gold/PHI access, provider generation, credential use, device execution, or spend is authorized here.

## 1. Summary

Build the minimum SFT V1 control plane required to make the first future commandMed supervised fine-tuning run scientifically reproducible, quarantine-clean, safety-preserving, Arabic-aware, and auditable.

The plan intentionally separates four different states that must never be conflated:

```text
SFT_PLAN_READY
!= OFFLINE_SFT_INFRASTRUCTURE_READY
!= TRAINING_READY
!= TRAINING_AUTHORIZED
```

A future training run becomes possible only after the frozen tournament produces evidence, Founder + ChatGPT choose the backbone, the exact training input/recipe identities are bound, finance/access gates pass, and a separate training authorization is canonical.

## 2. Inherited non-negotiable contracts

Spec 007 inherits without weakening:

- Spec 001 evaluation-before-optimization;
- Spec 002 hard safety gates and fail-closed qualification;
- Spec 003 provenance/license/content/split/contamination requirements;
- Spec 004 tournament comparison semantics;
- Spec 005 preconstruction, access, finance, activation, device, and manifest control plane;
- Spec 006 behavioral-state/tool/safety scaffold;
- AGENTS.md scientific invariants and three-role training model;
- FD-001 release posture;
- D-001 evaluation precedes training;
- D-003 role classes;
- T-001 backbone winner `TEST_BEFORE_LOCK`.

No plan item may allow optimization evidence to redefine a frozen evaluation target after a run starts.

## 3. Constitution / governance check

### 3.1 Evaluation before optimization

PASS by construction: all candidate qualification, capability-preservation margins, safety sentinels, checkpoint-selection rules, and SFT-specific acceptance records must be versioned and frozen before the first gradient update they govern.

### 3.2 Safety hard gates

PASS by construction: hard safety/quarantine failures remain non-compensable. Development monitoring may abort/disqualify a run but may not redefine final Gold/test criteria.

### 3.3 Provenance and quarantine

PASS by construction: every training/evaluation asset and every rendered training record is identity-bound. Gold/holdout assets remain structurally excluded from curriculum, training, recipe selection, early stopping, checkpoint selection, and model selection.

### 3.4 Model neutrality

PASS: no candidate or winner is named as selected in this plan.

### 3.5 Bounded authority

PASS: planning does not grant model/weight/training/data/spend authority.

No constitution amendment is required.

## 4. Lifecycle — explicit tournament-to-training handshake

The canonical lifecycle must expose these gates separately:

```text
A. SPEC 007 OFFLINE CONTROL PLANE QUALIFIED
B. FOUNDER+CHATGPT CANDIDATE MANIFEST FREEZE
C. LIVE TOURNAMENT EXECUTION AUTHORIZED
D. TOURNAMENT EVIDENCE PACK COMPLETE
E. FOUNDER+CHATGPT BACKBONE WINNER DECISION
F. BASE CHECKPOINT BINDING CANONICAL
G. RECIPE / PILOT EVIDENCE FROZEN
H. DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
I. TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
J. FIRST SFT RUN
```

No earlier gate implies a later one.

`Pi` owns implementation of schemas/validators/fixtures/evidence packet generation. `Founder + ChatGPT` own candidate freeze and winner selection.

## 5. Planned repository architecture

Use Ponytail discipline: pure typed records + validators; no trainer framework abstraction until a backend is actually selected.

```text
specs/007-sft-v1/
  spec.md
  clarification.md
  research.md
  plan.md
  data-model.md                     # planning stage
  quickstart.md                     # planning stage
  contracts/
    curriculum-record.schema.json
    base-checkpoint-binding.schema.json
    prompt-rendering.schema.json
    loss-mask-policy.schema.json
    training-config.schema.json
    dataset-snapshot.schema.json
    capability-preservation.schema.json
    checkpoint-selection-policy.schema.json
    environment-manifest.schema.json
    training-checkpoint-manifest.schema.json
    run-manifest.schema.json
  checklists/requirements.md
  tasks.md
  analysis.md

src/commandmed/spec007/              # only after implementation authorization
  __init__.py
  curriculum.py
  rendering.py
  masking.py
  quarantine.py
  checkpoint.py
  config.py
  reproducibility.py
  selection.py
  activation.py

tests/spec007/                       # synthetic/offline fixtures only until later authority
  test_curriculum.py
  test_rendering.py
  test_masking.py
  test_quarantine.py
  test_checkpoint.py
  test_config.py
  test_reproducibility.py
  test_selection.py
  test_activation.py
  fixtures/

data/spec007/
  vocabularies.json                  # closed vocabularies / no real medical payload
  evidence_prerequisites.json        # typed NEEDS_EVIDENCE records
```

Exact filenames may be reduced during tasks if an existing repository module satisfies the same contract. Do not create empty abstraction layers merely to match this sketch.

## 6. Core data entities

### 6.1 CurriculumRecord

Every admitted example must bind:

- `record_id`;
- `record_canonical_sha256`;
- `content_sha256`;
- `source_authority_id`;
- `source_license_id`;
- `source_verification_status`;
- `split_id`;
- `contamination_status`;
- `review_state`;
- `role_class`;
- `curriculum_strata`;
- `language`;
- Arabic-specific metadata where applicable;
- conversation/message structure identity;
- quarantine disposition;
- durable-vs-mutable knowledge classification.

The raw content itself is not required in canonical control-plane fixtures; synthetic fixture payloads may stand in for validator tests.

### 6.2 BaseCheckpointBinding

Future binding includes:

- winner decision record identity;
- model/checkpoint identity;
- weight/content identity;
- tokenizer content/config identity;
- special-token map identity;
- canonical chat-template identity;
- prompt-rendering policy identity;
- BOS/EOS policy;
- tool-format policy;
- license/lineage evidence;
- tournament qualification evidence;
- resource/device evidence if required by activation.

Until Founder + ChatGPT choose the winner:

```text
BASE_CHECKPOINT_BINDING=NEEDS_EVIDENCE
BACKBONE_WINNER=NEEDS_EVIDENCE
```

### 6.3 PromptRenderingPolicy

Defines deterministic transformation from semantic conversation record to tokenizable conversation:

- role ordering;
- template bytes/hash;
- tool schema insertion;
- normalization;
- system-message handling;
- special tokens;
- BOS/EOS;
- target-turn boundaries;
- rendering version.

A template/tokenizer change produces a new recipe identity.

### 6.4 LossMaskPolicy

Defines the supervised objective at token level. Must explicitly classify:

- system tokens;
- user tokens;
- assistant natural-language tokens;
- assistant structured/tool-call tokens;
- tool-result tokens;
- separators/special tokens;
- padding.

No backend default is authoritative.

### 6.5 TrainingConfigurationRecord

Versioned identity-bound configuration shape, initially with typed `NEEDS_EVIDENCE` values where unresolved:

- update strategy (`FULL`, `LORA`, `QLORA`, or later approved value);
- precision policy;
- sequence length;
- packing policy;
- truncation/segmentation policy;
- role/strata mixture policy;
- optimizer class;
- scheduler class;
- learning-rate record;
- effective batch/tokens per update;
- epochs/steps/token budget;
- gradient accumulation;
- clipping;
- checkpoint interval;
- evaluation interval;
- seed + data seed;
- deterministic-mode policy;
- backend identity;
- software environment identity.

The enum may be frozen before numeric values. Do not fabricate numeric defaults.

### 6.6 DatasetSnapshot

Binds the exact admitted record set, canonical ordering, rendered-token accounting, source/license summary, duplicate/near-duplicate report, contamination report, role/language/strata coverage, and snapshot hash.

### 6.7 CapabilityPreservationBinding

Defines base-vs-SFT paired development/final slices for:

- general reasoning;
- instruction following;
- medical core;
- Arabic;
- tool use;
- uncertainty/abstention;
- safety.

### 6.8 CheckpointSelectionPolicy

Pre-registered lexicographic policy:

```text
HARD_DEV_SAFETY_PASS
AND QUARANTINE_PASS
AND CAPABILITY_PRESERVATION_PASS
THEN optimize declared SFT development objectives
THEN allowed resource/efficiency tie-breaks
```

Final Gold/test/Private Gold are prohibited inputs.

### 6.9 EnvironmentManifest

Pins framework/backend versions, runtime/device identity, attention/kernel backend, precision, compiler flags where relevant, seeds, deterministic-mode configuration, and dependency identities.

### 6.10 TrainingCheckpointManifest

A resumable checkpoint must bind model/adapter, optimizer, scheduler, scaler if present, RNG, data cursor/order, global step, config, base checkpoint, dataset, tokenizer/template, and environment identities.

### 6.11 RunManifest

Future activation record tying:

- BaseCheckpointBinding;
- DatasetSnapshot;
- PromptRenderingPolicy;
- LossMaskPolicy;
- TrainingConfigurationRecord;
- CapabilityPreservationBinding;
- CheckpointSelectionPolicy;
- EnvironmentManifest;
- evaluation protocol identity;
- software commit/tree identity;
- A14 finance requirement/authorization identity;
- access/activation evidence;
- training authorization identity.

A schema-valid manifest is not itself execution authority.

## 7. Curriculum construction plan

### 7.1 Three frozen role classes

Use exactly:

- `PATIENT_CAREGIVER`
- `CLINICAL_PROFESSIONAL`
- `LEARNER_RESEARCHER`

Finer personas are evaluation metadata, not new training classes unless a later evidence-backed decision changes D-003.

### 7.2 Required curriculum domains

Preserve Spec 007 domains:

- medical fundamentals/factual accuracy;
- clinical problem representation;
- differential reasoning;
- active information acquisition;
- patient explanation;
- professional workflow;
- evidence use;
- uncertainty/abstention;
- tools/structured outputs;
- Arabic/English clinical language;
- adversarial/unsafe cases.

### 7.3 Quality over raw volume

No fixed example-count target is accepted as readiness by itself.

Generate a `CurriculumCoverageReport` with:

- count and rendered tokens per role/domain/language stratum;
- provenance completeness;
- review/adjudication state;
- exact/near-duplicate burden;
- contamination status;
- multi-turn proportion;
- abstention/safety/tool trajectory coverage;
- source concentration metrics;
- mutable-knowledge exclusion summary.

Any future data-selection algorithm is optional and must prove incremental value; LESS or similar approaches are research candidates, not mandatory dependencies.

### 7.4 Duplicate/contamination firewall

Before admission and again after transformations/rendering:

- exact duplicate detection;
- normalized near-duplicate detection;
- benchmark overlap detection;
- quarantine-source matching;
- repeated-content concentration detection.

A post-rendering transformation must not reintroduce an overlap missed at raw-record stage.

### 7.5 Mutable knowledge placement

Each proposed example receives a knowledge-placement disposition:

- `DURABLE_WEIGHT_ELIGIBLE`;
- `MUTABLE_RUNTIME_EVIDENCE_PREFERRED`;
- `REJECTED`.

Current guidelines, formularies, jurisdictional pathways, local service routing, and rapidly changing evidence default to runtime evidence/tools unless later evidence justifies weight inclusion.

## 8. Conversational, tool, and abstention plan

### 8.1 Multi-turn trajectories

Curriculum fixtures must support:

- underspecified question -> `ASK_MORE`;
- missing context resolved -> `ANSWER`;
- evidence needed -> `RETRIEVE_EVIDENCE`;
- deterministic tool needed -> `USE_TOOL`;
- unresolved/unsafe -> `ABSTAIN`;
- high-risk -> `ESCALATE`/`EMERGENCY`.

### 8.2 Tool behavior

Add development fixtures inspired by BFCL-style failure dimensions without importing BFCL as an automatic release gate:

- nonexistent tool hallucination;
- valid vs invalid tool selection;
- malformed arguments;
- missing required argument;
- tool unavailable;
- format sensitivity;
- multi-turn tool continuation;
- spoofed result;
- conflicting result.

All final behavior still composes through Spec 006.

### 8.3 Abstention

Create a dedicated `AbstentionCoverageReport` and evaluation slice for missing, contradictory, ambiguous, OOD, unsupported, and insufficient-evidence scenarios. Correct `ASK_MORE`/`ABSTAIN`/`ESCALATE` decisions are positive behavior, not failures to answer.

## 9. Arabic plan

### 9.1 Record metadata

Arabic records additionally carry, when applicable:

- original language;
- translation/transcreation status;
- dialect/register;
- MSA vs Saudi/Gulf colloquial;
- code-switch status;
- transliteration status;
- terminology-normalization identity;
- qualified-review identity/status.

### 9.2 Tournament evidence request

Founder + ChatGPT candidate decision packet must include tokenizer efficiency on matched medical-language samples:

- tokens/word;
- characters/token;
- medication-name fragmentation;
- clinical-term fragmentation;
- MSA;
- Saudi/Gulf colloquial;
- code-switching;
- transliterated medical terminology.

Pi reports measurements; Pi does not select the model.

### 9.3 Evaluation candidates

MedAraBench and MedArabiQ are candidates for development/evaluation research only after exact identity/license/split/contamination review. No automatic training use.

## 10. Prompt rendering, masking, packing, and truncation

These are P0 pre-run contracts.

### 10.1 Rendering conformance

For representative fixtures, commit expected rendered role/token boundary metadata without model-specific token IDs until a winner exists. After winner binding, generate exact tokenizer-specific conformance fixtures before training activation.

### 10.2 Loss-mask conformance

Tests must prove that only the frozen target token classes contribute loss. A backend is rejected if it cannot expose/verify the required mask semantics.

### 10.3 Packing

Packing is `NEEDS_EVIDENCE` until backend compatibility is proven. If enabled, tests must prove no unintended cross-example attention or label bleed under the selected implementation.

### 10.4 Truncation/segmentation

Fail closed rather than silently truncating required safety/tool/target context. Record deterministic reason codes such as:

- `SEQUENCE_TOO_LONG_REJECTED`;
- `SAFE_SEGMENTATION_REQUIRED`;
- `REQUIRED_CONTEXT_WOULD_BE_TRUNCATED`.

## 11. Safety and catastrophic-forgetting plan

### 11.1 Base baseline

Before any future run, freeze base checkpoint development baselines on:

- Spec 002 hard-gate development counterparts;
- Spec 006 behavioral-state/tool fixtures;
- abstention;
- general reasoning;
- instruction following;
- Arabic;
- medical core.

### 11.2 Checkpoint-level sentinel gates

Use only designated development assets. At predeclared checkpoints:

- run small safety/capability sentinel evaluation;
- write immutable result identities;
- abort/disqualify according to frozen thresholds/rules;
- never consult final Gold for early stopping.

### 11.3 Final qualification

After checkpoint selection freezes, evaluate against the full frozen canonical protocol. Hard failures are non-compensable.

## 12. Checkpoint selection firewall

Checkpoint selection policy must exist before the run.

Forbidden:

- choosing the checkpoint with the best final test/Gold result;
- repeated human/LLM inspection of final holdout for recipe tuning;
- choosing solely by lowest training/eval loss when safety/capability constraints exist.

Required ordering:

1. hard development safety + quarantine;
2. capability-preservation gates;
3. frozen SFT development objectives;
4. declared resource tie-breaks.

Record every checkpoint considered and the deterministic reason for selection/rejection.

## 13. Evaluation program additions

Use inherited evaluation identities first. New candidates require full Spec 003-style identity/license/contamination review.

### 13.1 Realistic open-ended health behavior

HealthBench is a development/evaluation candidate for multi-turn patient/clinician interactions with physician-authored rubrics.

HealthBench Professional is a candidate for care consult, writing/documentation, and medical-research workflows.

### 13.2 Evaluator limits

Judge-based scoring never overrides deterministic hard gates. Before a judge-derived metric affects checkpoint selection, validate evaluator agreement, bias/lineage concerns, and failure-to-abstain behavior sufficiently for the intended use.

### 13.3 Tool use

BFCL V4 methodology may inform tool-evaluation dimensions. Use repository-native synthetic fixtures for hard safety/tool-contract qualification unless an external suite is formally admitted.

## 14. Memorization / regurgitation audit

Before training activation, require a versioned audit plan containing:

- duplicate and near-duplicate reports;
- source concentration report;
- benchmark overlap report;
- safe synthetic canary scheme, if used;
- regurgitation probes;
- acceptance/failure criteria.

No PHI, credentials, secrets, Private Gold, or restricted content may be inserted as canaries.

## 15. Reproducibility and resume plan

### 15.1 Reproducibility levels

Do not promise impossible cross-platform bitwise identity.

`EXACT_ENVIRONMENT_REPLAY`:

- exact pinned software;
- same allowed hardware class;
- exact model/tokenizer/template/data/config;
- exact seeds/data seed/order;
- deterministic algorithms where supported;
- explicit record of remaining nondeterministic operations.

`CROSS_ENVIRONMENT_REPRODUCIBILITY`:

- repeated approved runs;
- compare frozen behavioral/statistical outputs;
- tolerances frozen before comparison.

### 15.2 Environment manifest

Bind:

- OS/container image identity;
- Python;
- framework/trainer/backend;
- CUDA/ROCm/other runtime;
- GPU/device;
- attention/kernel backend;
- precision;
- compiler flags where material;
- dependency lock identity.

### 15.3 Resume integrity

Test an interrupted synthetic/dummy training loop once implementation/runtime authorization permits the relevant local test surface. A resumable checkpoint must restore optimizer/scheduler/RNG/data position, not only model weights.

## 16. Training backend and update-strategy decision

Backend remains `NEEDS_EVIDENCE`.

Candidates may later include TRL/Transformers + PEFT, Axolotl, Unsloth, Liger-assisted stacks, or another compatible implementation. No candidate receives canonical status by popularity.

The backend evidence record must prove:

- winner architecture support;
- exact template/tokenizer handling;
- frozen loss-mask support;
- packing/truncation conformance;
- resume integrity;
- reproducibility controls;
- required precision/update strategy;
- acceptable numerical behavior;
- no unauthorized telemetry/network/provider dependency;
- maintainability under Ponytail discipline.

Similarly, `FULL` vs `LORA` vs `QLORA` remains `NEEDS_EVIDENCE` until winner + compute budget + pilot evidence exist.

## 17. Future tournament decision packet for Founder + ChatGPT

Pi must produce a neutral evidence packet with no recommendation. Required candidate fields:

- exact repository/model/checkpoint identity;
- exact license and release-lineage compatibility;
- weight/package bytes;
- tokenizer/template identities;
- Arabic tokenizer-efficiency evidence;
- core medical quality;
- patient conversation quality;
- uncertainty/abstention;
- Arabic/English performance;
- tool-use capability;
- general-capability preservation potential;
- fine-tuning tooling/stability evidence;
- RAM/device evidence;
- model-format/runtime compatibility;
- material known limitations;
- tournament qualification/disqualification reasons.

Output:

```text
PI_RECOMMENDATION=NONE
CANDIDATE_RESULTS=<evidence only>
DECISION_OWNER=FOUNDER+CHATGPT
```

## 18. Activation / run-manifest fail-closed logic

Training activation must fail if any of the following is missing/stale/mismatched:

- Founder + ChatGPT winner decision;
- base checkpoint binding;
- license compatibility;
- tokenizer/template/rendering identity;
- loss-mask identity;
- dataset snapshot;
- provenance/quarantine pass;
- duplicate/contamination audit;
- capability-preservation binding;
- checkpoint-selection policy;
- evaluation protocol;
- environment/backend identity;
- training configuration;
- finance requirement/authorization;
- access grants;
- training authorization.

Return only a non-executing readiness state until every separately controlled gate is canonical.

## 19. Verification plan for offline implementation

When implementation is separately authorized, require TDD and synthetic fixtures for every control-plane rule.

Baseline commands:

```bash
python3 -m compileall -q src tests
pytest -q
git diff --check
```

Additional focused verification should prove:

- closed record vocabularies;
- canonical identity generation;
- duplicate and quarantine rejection;
- role/language/strata coverage reports;
- rendering identity changes on template changes;
- loss-mask boundary fixtures;
- truncation fail-closed behavior;
- packing policy admission/rejection;
- checkpoint-selection Gold firewall;
- environment-manifest completeness;
- resumable-vs-export checkpoint distinction;
- all activation prerequisites;
- no network/model/weight/training surface exists in offline validators.

Test counts must be reported from the live branch; do not hard-code the current 627+128 baseline as a future pass result.

## 20. Planning-stage tasks to generate next

`tasks.md` should be dependency ordered approximately as:

```text
P0 lifecycle/contract identities
P1 curriculum/provenance/quarantine contracts
P2 tokenizer/template/rendering/loss-mask contracts
P3 packing/truncation contracts
P4 Arabic metadata + tokenizer-evidence packet schema
P5 capability-preservation + safety-sentinel contracts
P6 checkpoint-selection firewall
P7 environment/reproducibility/resume contracts
P8 run-manifest + activation composition
P9 synthetic fixtures + focused validator tests
P10 full offline regression + exact-head review
P11 tournament decision-packet readiness
P12 STOP at controlled model/tournament/training authority gates
```

Tasks must not smuggle live execution into offline implementation.

## 21. Risks and mitigations

- **Hidden objective drift from trainer defaults** -> explicit rendering + loss-mask contracts.
- **Safety degradation during benign SFT** -> pre-run baseline + checkpoint sentinels + final hard gates.
- **Catastrophic forgetting** -> paired capability-preservation binding.
- **Benchmark leakage through checkpoint selection** -> dev-only selection firewall.
- **Arabic inefficiency hidden by aggregate accuracy** -> tokenizer fragmentation evidence.
- **Irreproducible interrupted runs** -> resumable checkpoint manifest.
- **False cross-GPU determinism claim** -> two-level reproducibility semantics.
- **Tool hallucination despite schema support** -> multi-turn/hallucination/format fixtures.
- **Stale clinical truth baked into weights** -> durable-vs-mutable knowledge placement.
- **Overengineering trainer abstraction** -> backend-neutral records first; select one minimal backend later.
- **Pi preselecting a model** -> explicit FOUNDER+CHATGPT decision gate and neutral evidence packet.

## 22. Explicit out of scope

This plan does NOT authorize or perform:

- model candidate selection by Pi;
- backbone winner selection by Pi;
- weight download/load/access;
- live tournament execution;
- SFT/LoRA/QLoRA/full fine-tuning;
- CPT;
- distillation;
- DPO;
- RLVR/GRPO/RL;
- QAT;
- real benchmark payload execution;
- Private Gold access;
- PHI/restricted clinical data;
- provider-generated training data;
- paid compute/spend;
- clinician/human evaluation execution;
- multimodal training.

## 23. Plan exit condition

The planning package is ready for checklist/tasks/analyze only when review confirms that it contains no unresolved hard ambiguity about:

```text
CURRICULUM_IDENTITY
PROVENANCE_AND_QUARANTINE
TOKENIZER_AND_TEMPLATE_IDENTITY
PROMPT_RENDERING
LOSS_MASKING
PACKING_AND_TRUNCATION
MULTI_TURN_AND_TOOL_USE
ABSTENTION
ARABIC_METADATA_AND_TOKENIZER_EVIDENCE
SAFETY_SENTINEL_MONITORING
CAPABILITY_PRESERVATION
CHECKPOINT_SELECTION_FIREWALL
MEMORIZATION_AUDIT
REPRODUCIBILITY_LEVELS
RESUME_INTEGRITY
BACKEND_NEUTRALITY
RUN_MANIFEST
TOURNAMENT_TO_TRAINING_HANDSHAKE
```

Any concrete model, model-weight identity, trainer/backend, update strategy, training numeric, dataset content, compute budget, or training run that still requires evidence remains explicitly `NEEDS_EVIDENCE` / separately authorized.

```text
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
