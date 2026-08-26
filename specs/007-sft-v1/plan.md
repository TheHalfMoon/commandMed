# Plan — Spec 007 SFT V1 (Training-Grade Hardening)

**Branch:** `spec/007-clarify-plan-hardening-v2`
**Parent authorization candidate:** PR #47 head `5e8618de32468f04d797117cc46bb2bdf72dd3e1`
**Specification:** canonical via PR #46 / merge `645da20263fc44d1ed8977024cf2df57aa6f7465`
**Status:** non-canonical planning candidate created from Founder-directed gap review; clarification may become canonical only after PR #47, and this `plan.md` itself must not become canonical until the repository separately records planning-stage authority
**Execution authority:** NONE
**Training authority:** NONE
**Model selection authority:** FOUNDER+CHATGPT ONLY

> This plan converts Spec 007 into a training-grade control and implementation plan without selecting a model, backend, dataset, optimizer values, adapter strategy, or training budget. It prepares deterministic/offline infrastructure and explicit future gates. No model weight access, live tournament, training run, Private Gold/PHI access, provider generation, credential use, device execution, or spend is authorized here.

## 1. Summary

Build the minimum SFT V1 control plane required to make the first future commandMed supervised fine-tuning run scientifically reproducible, quarantine-clean, safety-preserving, Arabic-aware, and auditable.

The plan intentionally separates states that must never be conflated:

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

PASS by construction: candidate qualification rules, capability-preservation rules, any abort-only sentinel thresholds, fixed checkpoint policy, and SFT-specific acceptance records must be versioned and frozen before the first gradient update they govern.

### 3.2 Safety hard gates

PASS by construction: hard safety/quarantine failures remain non-compensable. A permissible abort-only safety sentinel may terminate or invalidate a future run, but it cannot rank checkpoints, choose recipes, alter hyperparameters, or create an early-stopping preference.

### 3.3 Provenance and complete quarantine firewall

PASS by construction: every training/evaluation asset and every rendered training record is identity-bound. The canonical quarantine source matrix from `eval_contract.validate` / its frozen quarantine data is authoritative.

For Spec 007 SFT tuning surfaces, the sources explicitly named by FR-003 are structurally excluded from curriculum construction, gradient-bearing SFT data, monitoring that can influence optimization, hyperparameter/recipe selection, early stopping, checkpoint ranking/selection, model selection, and every other tuning or selection surface:

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

The same exclusion applies to every additional source identifier governed by the frozen canonical matrix for a prohibited SFT tuning purpose, including public canonical-test sources. The implementation must bind to the canonical matrix identity rather than treating this copied list as the sole authority. `CALIBRATION_HOLD_OUT_SPLIT` remains calibration-only.

A label such as `DEV` or `CHECKPOINT_SELECTION` does not create an exception to Spec 007 FR-003.

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
G. NON_EXECUTING_RECIPE_EVIDENCE_FROZEN
H. DATA / ACCESS / FINANCE / ACTIVATION GATES PASS
I. TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
J. FIRST SFT RUN
```

No earlier gate implies a later one.

`NON_EXECUTING_RECIPE_EVIDENCE` is limited to static/control-plane evidence that does not require loading or executing model weights and does not perform gradient-bearing work. It may bind recipe schema completeness, documented winner/backend compatibility, prompt-rendering/loss-mask/packing/truncation conformance, static memory/compute estimates, provenance/quarantine evidence, environment identity, and other non-executing preflight facts. It excludes loss curves, gradient behavior, convergence, candidate outputs, benchmark execution, and any empirical evidence requiring model execution.

Any experiment described as a pilot, smoke-train, adapter pilot, one-step train, gradient probe, or equivalent is a training run for authority purposes. It may occur only after all model/weight/data/device/finance/training authorities applicable to that run are canonical. No pilot is implied or authorized by gate G.

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

Defines base-vs-SFT paired qualification slices for:

- general reasoning;
- instruction following;
- medical core;
- Arabic;
- tool use;
- uncertainty/abstention;
- safety.

Any slice that is part of the canonical quarantine matrix is final/qualification evidence only and cannot be recycled into tuning or checkpoint selection.

### 6.8 CheckpointSelectionPolicy

The checkpoint-selection rule is frozen pre-run and must not consume any asset in the canonical quarantine-controlled source set.

Default policy while no separately authorized, non-quarantined SFT selection source exists:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
CHECKPOINT_RULE=PREDECLARED_FINAL_STEP_OR_TOKEN_BUDGET
EVALUATION_ASSET_RANKING=PROHIBITED
ABORT_SENTINEL_CAN_RANK=NO
```

A future evidence-driven ranking policy is permitted only after a separately canonicalized source/purpose authority proves that its selection evidence is outside the prohibited quarantine set for the exact SFT selection surface. Training loss or evaluator output cannot silently create such authority.

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

### 7.4 Duplicate/contamination/quarantine firewall

Before admission and again after transformations/rendering:

- exact duplicate detection;
- normalized near-duplicate detection;
- benchmark overlap detection;
- canonical quarantine-source matching against the frozen matrix identity;
- repeated-content concentration detection.

A post-rendering transformation must not reintroduce an overlap missed at raw-record stage. A source permitted for one canonical purpose is not automatically permitted for SFT training, monitoring, selection, or tuning.

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

Any quarantined evaluation slice is qualification-only and cannot be used to tune the recipe or select the checkpoint.

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

MedAraBench and MedArabiQ are candidates for development/evaluation research only after exact identity/license/split/contamination review. No automatic training use and no checkpoint/recipe-selection use unless a future explicit source/purpose policy authorizes that exact surface without violating FR-003.

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

### 11.1 Base qualification baselines

Before any future run, freeze base-checkpoint qualification baselines on the required canonical protocol dimensions:

- Spec 002 hard gates;
- Spec 006 behavioral-state/tool fixtures;
- abstention;
- general reasoning;
- instruction following;
- Arabic;
- medical core.

If an underlying asset belongs to the canonical quarantine matrix, its base result is retained for later paired qualification only. It cannot be exposed during optimization or used to rank checkpoints/recipes.

### 11.2 Abort-only checkpoint sentinel gates

Intra-run monitoring is optional, not an exception to quarantine.

A separately identity-bound `SFT_ABORT_SENTINEL_SET` may be used only if pre-run validation proves:

- none of its source identities belong to the canonical quarantine-controlled set for a prohibited SFT tuning purpose;
- Spec 003 provenance/license/split/contamination/source-verification requirements pass;
- it is excluded from gradient-bearing curriculum/training data;
- thresholds are frozen pre-run;
- the only allowed action is `CONTINUE`, `ABORT_RUN`, or `DISQUALIFY_RUN`.

It must not:

- rank checkpoints;
- choose a recipe/update strategy;
- change hyperparameters;
- drive early stopping toward a preferred checkpoint;
- select a model.

If such a sentinel cannot be established, no intra-run evaluator is permitted to bypass the quarantine firewall. The pre-registered fixed checkpoint schedule remains in force.

### 11.3 Final qualification

After checkpoint identity is frozen by the pre-registered quarantine-safe rule, evaluate against the full frozen canonical protocol. Hard failures are non-compensable. Final results cannot retroactively alter the recipe/checkpoint and then be re-used as untouched holdout evidence.

## 12. Checkpoint selection firewall

Checkpoint policy must exist before the run.

### 12.1 Canonical prohibited inputs

No source governed by Spec 007 FR-003's canonical quarantine set may influence checkpoint ranking/selection, early stopping, hyperparameter selection, recipe selection, model selection, or another tuning surface. This includes at minimum:

- `COMMANDMED_CLINICAL_GOLD`;
- `COMMANDMED_ARABIC_GOLD`;
- `COMMANDMED_MULTIMODAL_GOLD`;
- `CALIBRATION_HOLD_OUT_SPLIT`;
- `MODEL_SELECTION_DEV_SET`;
- `PUBLIC_BENCHMARK_DEV_SPLITS`;
- `HELD_OUT_SYNTHETIC_PILOT_CASES`;
- `VERIFIED_DEV_SPLIT`;
- every other source identifier controlled by the same frozen matrix for a prohibited SFT tuning purpose.

The implementation validates against the canonical matrix identity, not only this prose list.

### 12.2 Current default selection rule

Until a separate canonical policy admits an expressly non-quarantined selection source for SFT V1, checkpoint selection is deterministic and evaluation-independent:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
RULE=FINAL_CHECKPOINT_AT_FROZEN_STEP_OR_TOKEN_BUDGET
```

Training loss, abort-only sentinels, human inspection, LLM judges, or quarantined development assets cannot override this rule.

### 12.3 Future optional selection evidence

A later evidence-ranking policy may exist only if, before the run:

- the source is outside the prohibited canonical quarantine set for the exact intended purpose;
- source/purpose authority is explicit and canonical;
- provenance/license/contamination checks pass;
- selection rule and thresholds are frozen;
- no final qualification asset is recycled into tuning.

Record every checkpoint considered and the deterministic reason for selection/rejection.

## 13. Evaluation program additions

Use inherited evaluation identities first. New candidates require full Spec 003-style identity/license/contamination review.

### 13.1 Realistic open-ended health behavior

HealthBench is a development/evaluation candidate for multi-turn patient/clinician interactions with physician-authored rubrics.

HealthBench Professional is a candidate for care consult, writing/documentation, and medical-research workflows.

Their admission as evaluation assets does not make them eligible for recipe/checkpoint/tuning decisions. Purpose-specific quarantine rules remain authoritative.

### 13.2 Evaluator limits

Judge-based scoring never overrides deterministic hard gates. Under the current Spec 007 quarantine contract, judge-derived results from quarantined evaluation assets cannot influence checkpoint or recipe selection. Any future selection use requires a separately admitted non-quarantined source/purpose record and validated evaluator agreement, bias/lineage behavior, and failure-to-abstain behavior.

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

The backend evidence record must prove, using non-executing evidence before the first training authorization:

- documented winner architecture support;
- exact template/tokenizer handling contract;
- frozen loss-mask support;
- packing/truncation conformance;
- resume-state capability;
- reproducibility controls;
- required precision/update-strategy support;
- no unauthorized telemetry/network/provider dependency;
- maintainability under Ponytail discipline.

For the first authorized run, `FULL` vs `LORA` vs `QLORA` remains `NEEDS_EVIDENCE` until the winner, static memory/compute budget, deployable artifact requirements, license posture, and non-executing backend compatibility evidence are bound. It must **not** depend on an unauthorized pilot.

If empirical convergence/stability/gradient/model-output evidence is desired to compare update strategies, that evidence may only be generated by a separately authorized training run after all applicable model/weight/data/device/finance/training gates pass. Such results cannot select recipe/hyperparameters/checkpoints unless a separately authorized policy satisfies the complete FR-003 quarantine firewall.

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
- fine-tuning tooling/stability evidence that exists lawfully before selection;
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
- non-executing recipe evidence identity;
- finance requirement/authorization;
- access grants;
- training authorization.

Activation must additionally verify that no canonical quarantined source is bound to a prohibited training/monitoring/selection/tuning surface and that any abort-only sentinel has `CAN_RANK_CHECKPOINTS=false`, `CAN_TUNE_RECIPE=false`, and `CAN_CHANGE_HYPERPARAMETERS=false` semantics.

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
- duplicate rejection;
- canonical quarantine-matrix identity binding;
- rejection of every quarantined source on curriculum/training/monitoring/early-stopping/recipe/checkpoint/model-selection surfaces where FR-003 prohibits it;
- calibration split accepted only for calibration;
- abort-only sentinel cannot rank/select/tune;
- fixed pre-registered checkpoint rule when no separately admitted selection source exists;
- `NON_EXECUTING_RECIPE_EVIDENCE` rejects loss curves, gradient evidence, model outputs, or other execution-derived evidence before training authority;
- role/language/strata coverage reports;
- rendering identity changes on template changes;
- loss-mask boundary fixtures;
- truncation fail-closed behavior;
- packing policy admission/rejection;
- environment-manifest completeness;
- resumable-vs-export checkpoint distinction;
- all activation prerequisites;
- no network/model/weight/training surface exists in offline validators.

Test counts must be reported from the live branch; do not hard-code the current 627+128 baseline as a future pass result.

## 20. Planning-stage tasks to generate next

`tasks.md` should be dependency ordered approximately as:

```text
P0 lifecycle/contract identities
P1 curriculum/provenance/full-quarantine contracts
P2 tokenizer/template/rendering/loss-mask contracts
P3 packing/truncation contracts
P4 Arabic metadata + tokenizer-evidence packet schema
P5 capability-preservation + abort-only safety-sentinel contracts
P6 fixed checkpoint-selection firewall + optional future selection-source gate
P7 environment/reproducibility/resume contracts
P8 non-executing recipe evidence + run-manifest + activation composition
P9 synthetic fixtures + focused validator tests
P10 full offline regression + exact-head review
P11 tournament decision-packet readiness
P12 STOP at controlled model/tournament/training authority gates
```

Tasks must not smuggle live execution into offline implementation.

## 21. Risks and mitigations

- **Hidden objective drift from trainer defaults** -> explicit rendering + loss-mask contracts.
- **Safety degradation during benign SFT** -> pre-run qualification baseline + optional abort-only, quarantine-clean sentinel + final hard gates.
- **Catastrophic forgetting** -> paired capability-preservation binding used for qualification, never as a hidden tuning leak.
- **Benchmark/holdout leakage through selection or monitoring** -> full canonical quarantine firewall across all optimization-affecting surfaces.
- **Unauthorized pilot smuggled into preflight** -> non-executing recipe-evidence definition; every gradient-bearing pilot is a training run requiring training authority.
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
- training pilots, smoke-training, one-step gradient probes, or adapter pilots;
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

This non-canonical planning candidate is ready to enter the repository's separately authorized planning lifecycle only when review confirms that it contains no unresolved hard ambiguity about:

```text
CURRICULUM_IDENTITY
PROVENANCE_AND_FULL_QUARANTINE_FIREWALL
TOKENIZER_AND_TEMPLATE_IDENTITY
PROMPT_RENDERING
LOSS_MASKING
PACKING_AND_TRUNCATION
MULTI_TURN_AND_TOOL_USE
ABSTENTION
ARABIC_METADATA_AND_TOKENIZER_EVIDENCE
ABORT_ONLY_SAFETY_MONITORING
CAPABILITY_PRESERVATION
FIXED_CHECKPOINT_SELECTION_FIREWALL
NON_EXECUTING_RECIPE_EVIDENCE
NO_PREAUTHORIZATION_PILOT
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
