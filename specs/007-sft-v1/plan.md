# Plan — Spec 007 SFT V1 (Record-Grade Compact Medical Core)

**Branch:** `spec/007-plan-record-frontier`  
**Canonical planning base:** `981987390f60302d4c38ae6d54c101aa78c12f4e`  
**Planning authorization:** PR #50 / merge `981987390f60302d4c38ae6d54c101aa78c12f4e`  
**Canonical clarification:** PR #49 / merge `16ae16b50680469fe14f44c1e3fdcb655d34b822`  
**Qualified clarification head:** `1919779ba87725b7d529ba35465dc546f61fbc13`  
**Strategy:** `docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md`  
**Lifecycle:** `AUTHORIZED_TO_PLAN`  
**Execution authority:** NONE  
**Training authority:** NONE  
**Model selection authority:** FOUNDER + CHATGPT ONLY

> This plan defines the complete non-executing architecture and task boundary for commandMed's first supervised-fine-tuned compact Core candidate. It does not select a model, backend, dataset payload, update strategy, hyperparameter values, compute budget, teacher, quantization method, or winner. It does not authorize model access, tournament execution, training, Private Gold/PHI access, restricted data, device execution, credentials, provider generation, or spend.

## 1. Planning objective

Build the smallest robust **SFT V1 control plane** needed to make a future commandMed Core training run:

- scientifically pre-registered;
- provenance-complete;
- quarantine-clean;
- safety-capped;
- tokenizer/template/loss aware;
- Arabic-aware;
- tool-native;
- abstention-native;
- reproducible and resumable;
- resource-accounted;
- auditable end to end;
- suitable for later medical-intelligence-density and record-class evaluation without optimizing against protected final evidence.

Spec 007 must answer one bounded research question when execution is later authorized:

> How much verified role adaptation, medical reasoning behavior, evidence/tool behavior, abstention behavior, English/Arabic clinical communication, and safety preservation can be obtained from the Founder+ChatGPT-selected compact base using the smallest defensible SFT curriculum and the least irreversible complexity?

Spec 007 is the first **Core** adaptation stage. It is not the Nano program, CPT, distillation, RLVR, calibration deepening, quantization, multimodal adaptation, human evaluation, or release review.

## 2. State separation

These states are deliberately non-equivalent:

```text
SPEC007_PLAN_READY
!= SPEC007_OFFLINE_CONTROL_PLANE_READY
!= MODEL_TOURNAMENT_READY
!= MODEL_SELECTED
!= DATA_READY
!= TRAINING_READY
!= TRAINING_AUTHORIZED
!= CANDIDATE_QUALIFIED
!= RELEASE_READY
```

No earlier state grants a later one.

## 3. Inherited non-negotiable contracts

Spec 007 inherits without weakening:

- Spec 001 evaluation-before-optimization and metric identity;
- Spec 002 hard safety gates and fail-closed qualification;
- Spec 003 provenance, license, content identity, split, contamination, and verification rules;
- Spec 004 deterministic tournament comparison semantics;
- Spec 005 tournament/preconstruction/finance/access/activation/device/manifest control plane;
- Spec 006 behavioral states, deterministic tool authority, traceability, and safety precedence;
- AGENTS.md scientific and Ponytail constraints;
- D-001 evaluation precedes training;
- D-003 three role classes;
- T-001 backbone winner `TEST_BEFORE_LOCK`;
- FD-001 permissive downstream-release posture;
- FD-002/related device-resource definition of compactness.

No optimization result may redefine the frozen evaluation target that judges it.

## 4. Current authority boundary

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE

MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Planning may define schemas, validators, synthetic fixtures, decision packets, future evidence requirements, and task dependencies. It may not convert an unresolved future input into an implicit permission.

## 5. Constitution and safety assessment

### 5.1 Evaluation before optimization

PASS by construction if implementation enforces:

- frozen evaluation protocol identity;
- frozen hard-gate identities;
- pre-run acceptance records;
- pre-registered checkpoint policy;
- pre-registered abort-only sentinel policy if one exists;
- no protected evaluation feedback into tuning.

### 5.2 Hard safety gates

Safety and quarantine are non-compensable. A quality average cannot offset:

- emergency/escalation hard-gate failure;
- medication-critical failure;
- deterministic-tool authority violation;
- quarantine leak;
- provenance failure;
- unauthorized execution.

### 5.3 Complete quarantine firewall

The canonical purpose→allowed-sources matrix is authoritative, not prose copies in this plan.

At minimum, sources identified by Spec 007 FR-003 such as:

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

plus every additional source governed by the frozen matrix for a prohibited SFT purpose are structurally excluded from prohibited:

- curriculum construction;
- gradient-bearing SFT input;
- optimization-affecting monitoring;
- hyperparameter selection;
- update-strategy/recipe selection;
- preferred-checkpoint early stopping;
- checkpoint ranking/selection;
- model selection;
- any equivalent tuning surface.

Labels such as `DEV`, `PILOT`, or `CHECKPOINT_SELECTION` do not create exceptions.

## 6. Tournament-to-training handshake

The future lifecycle is explicit:

```text
A. SPEC007 OFFLINE CONTROL PLANE QUALIFIED
B. FOUNDER+CHATGPT CANDIDATE MANIFEST FROZEN
C. LIVE TOURNAMENT EXECUTION SEPARATELY AUTHORIZED
D. TOURNAMENT EVIDENCE PACK COMPLETE
E. FOUNDER+CHATGPT BACKBONE WINNER DECISION
F. BASE CHECKPOINT BINDING CANONICAL
G. NON_EXECUTING_RECIPE_EVIDENCE FROZEN
H. FROZEN EVALUATION PROTOCOL BOUND
I. DATA / ACCESS / FINANCE / DEVICE / ACTIVATION GATES PASS
J. TRAINING_AUTHORITY=AUTHORIZED_TO_RUN
K. FIRST SFT RUN
L. PRE-REGISTERED CHECKPOINT IDENTITY RESOLVED
M. FULL FROZEN QUALIFICATION
N. CANDIDATE ACCEPT / REJECT / NARROW-SCOPE DECISION
```

A pilot, smoke-train, adapter probe, one-step gradient update, micro-training experiment, or convergence experiment is a **training run** for authority purposes.

## 7. Non-executing recipe evidence

Before training authority, `NON_EXECUTING_RECIPE_EVIDENCE` may contain only static/control-plane evidence such as:

- schema completeness;
- documented architecture/backend compatibility;
- static memory and compute estimates;
- tokenizer/template/rendering conformance definitions;
- loss-mask conformance definitions;
- packing/truncation conformance requirements;
- provenance/quarantine bindings;
- environment identity requirements;
- artifact/export requirements;
- license posture.

It MUST NOT contain execution-derived evidence such as:

- loss curves;
- gradients;
- convergence observations;
- trained outputs;
- checkpoint comparisons;
- benchmark execution;
- live model outputs;
- empirical update-strategy comparisons.

## 8. Planned repository surface

Ponytail discipline applies: use typed records + validators + synthetic fixtures before adding trainer frameworks.

```text
specs/007-sft-v1/
  spec.md
  clarification.md
  research.md
  plan.md
  data-model.md
  quickstart.md
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
    record-class-definition.schema.json
    resource-accounting.schema.json
    efficiency-scorecard.schema.json
    failure-taxonomy.schema.json
  checklists/requirements.md
  tasks.md
  analysis.md

src/commandmed/spec007/                 # only after implementation authorization
  __init__.py
  curriculum.py
  rendering.py
  masking.py
  quarantine.py
  checkpoint.py
  config.py
  reproducibility.py
  scorecards.py
  failure_taxonomy.py
  selection.py
  activation.py

tests/spec007/                          # synthetic/offline until later authority
  ...

data/spec007/                           # closed vocabularies / typed prerequisites only
  vocabularies.json
  evidence_prerequisites.json
```

Exact module count may be reduced during implementation if existing modules satisfy the contracts. Empty abstraction layers are prohibited.

## 9. Core planning entities

### 9.1 CurriculumRecord

Every admitted future SFT example binds:

- `record_id`;
- canonical record identity;
- content SHA-256;
- source authority identity;
- source license identity;
- source verification state;
- split identity;
- contamination state;
- review/adjudication state;
- role class;
- curriculum domains/strata;
- language metadata;
- conversation structure identity;
- risk/safety tags where applicable;
- evidence/tool requirement tags;
- knowledge-placement disposition;
- quarantine disposition;
- rendered supervised-token accounting once a concrete tokenizer is bound.

### 9.2 BaseCheckpointBinding

Future binding includes:

- Founder+ChatGPT winner-decision record identity;
- model/checkpoint identity;
- weight/content identity;
- total parameter count;
- active-parameter semantics if relevant;
- tokenizer revision/content/config identity;
- special-token map;
- canonical chat template;
- BOS/EOS policy;
- tool format;
- license/lineage evidence;
- tournament evidence identity;
- resource/device evidence required by activation.

Until the winner is selected:

```text
BASE_CHECKPOINT_BINDING=NEEDS_EVIDENCE
BACKBONE_WINNER=NEEDS_EVIDENCE
```

### 9.3 PromptRenderingPolicy

Deterministically defines semantic conversation → model input, including:

- role order;
- system-message handling;
- tool schema insertion;
- normalization;
- special tokens;
- BOS/EOS;
- target-turn boundaries;
- multi-turn continuation;
- rendering version/hash.

A template/tokenizer change creates a new recipe/input identity.

### 9.4 LossMaskPolicy

Explicitly classifies gradient contribution for:

- system tokens;
- user tokens;
- assistant natural-language tokens;
- assistant structured/tool-call tokens;
- tool-result tokens;
- safety-control tokens if any;
- separators/special tokens;
- padding.

Backend defaults are never authoritative.

### 9.5 TrainingConfigurationRecord

Versioned fields include:

- update strategy enum (`FULL`, `LORA`, `QLORA`, or later-approved value);
- precision policy;
- sequence length;
- packing policy;
- truncation/segmentation policy;
- role/strata mixture policy;
- optimizer/scheduler classes;
- learning-rate record;
- batch/tokens-per-update semantics;
- epochs/steps/token budget;
- gradient accumulation;
- clipping;
- checkpoint interval;
- seed + data seed;
- deterministic-mode policy;
- backend identity;
- software environment identity.

Unresolved numeric values remain `NEEDS_EVIDENCE`.

### 9.6 DatasetSnapshot

Binds exact admitted record IDs, ordering, rendered-token accounting, source/license summary, duplicate/near-duplicate report, contamination report, quarantine identity, role/language/domain coverage, and snapshot hash.

### 9.7 CapabilityPreservationBinding

Defines paired base-vs-SFT qualification for:

- general reasoning;
- instruction following;
- medical core;
- Arabic;
- tool behavior;
- abstention/selective risk;
- safety.

Protected qualification evidence cannot become a tuning oracle.

### 9.8 CheckpointSelectionPolicy

Default while no separately authorized, non-quarantined SFT selection source exists:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
CHECKPOINT_RULE=PREDECLARED_FINAL_STEP_OR_TOKEN_BUDGET
EVALUATION_ASSET_RANKING=PROHIBITED
ABORT_SENTINEL_CAN_RANK=NO
```

### 9.9 EnvironmentManifest

Pins material software/hardware/runtime identities, including:

- OS/container;
- Python;
- model framework;
- training backend;
- PEFT/quantization support libraries where used;
- CUDA/ROCm/other runtime;
- device model;
- driver;
- attention/kernel backend;
- compiler flags where material;
- precision;
- seeds/data seed;
- deterministic mode;
- dependency-lock identity.

### 9.10 TrainingCheckpointManifest

A resumable checkpoint is not just model weights. It must bind:

- model/adapter state;
- optimizer;
- scheduler;
- scaler if present;
- RNG state;
- data position/order;
- global step;
- training config;
- base checkpoint;
- dataset snapshot;
- tokenizer/template/rendering;
- environment.

### 9.11 RunManifest

Future activation unit tying all immutable run identities plus:

- frozen evaluation protocol;
- software commit/tree;
- access grants;
- A14 finance requirement/authorization;
- training authorization.

A schema-valid RunManifest is not execution authority.

## 10. Medical-intelligence-density entities

These entities support honest future record measurement without turning records into training targets.

### 10.1 RecordClassDefinition

Versioned definition for a future claim class, with:

- class ID/version;
- inclusion/exclusion rules;
- total-parameter accounting rule;
- active-parameter accounting rule where relevant;
- shipped-byte accounting rule;
- peak-memory accounting rule;
- required device/runtime evidence;
- required medical/evaluation slices;
- mandatory safety disposition;
- statistical/uncertainty policy;
- tie-break rule;
- contamination/quarantine prerequisites;
- allowed/disallowed public claim language.

### 10.2 ResourceAccountingRecord

Reports raw resource values without collapsing them into marketing labels:

- total parameters;
- active parameters if applicable;
- reference precision bytes;
- shipped artifact bytes;
- tokenizer/config/adapter bytes;
- peak RAM/VRAM;
- context/KV-cache conditions;
- TTFT;
- prefill/decode rate;
- sustained throughput;
- energy per case if measured;
- thermal/throttling condition.

Spec 007 implementation may define/validate the record shape offline. Real device values remain later evidence.

### 10.3 EfficiencyScorecard

Carries raw metrics plus derived views such as quality/GB or qualified-correctness/joule. Raw values always remain visible. Hard safety failures invalidate record qualification regardless of derived score.

### 10.4 FailureTaxonomyRecord

Development failure classification used by later authorized iterations. Categories must separate, at minimum:

- knowledge/factual;
- reasoning;
- missing-information acquisition;
- evidence-use;
- tool-selection/arguments;
- tool-result trust;
- abstention/over-answering;
- escalation/emergency;
- patient communication;
- professional workflow;
- Arabic/translation/code-switch;
- formatting/schema;
- provenance/data issue;
- evaluation ambiguity;
- mutable-knowledge placement;
- general-capability regression.

A failure category suggests a remediation surface; it does not automatically create a training example.

## 11. Core vs Nano boundary

Spec 007 plans **commandMed Core only**.

The approximately 0.6–1.5B/equivalent-resource Nano hypothesis is deferred until:

- Core has qualified capability worth preserving;
- Nano resource class is explicitly defined;
- legal teacher/student lineage exists;
- distillation/compression authority exists;
- capability-retention and safety gates are pre-registered;
- a distinct device tier justifies Nano.

Spec 007 MUST NOT optimize prematurely for Nano.

## 12. Curriculum — maximum information per gradient

Raw example count is not a readiness metric.

Planning objective:

> maximize verified capability coverage and future gain per admitted supervised token while minimizing duplicate, mutable, contaminated, low-confidence, and redundant content.

### 12.1 Frozen role classes

Exactly:

```text
PATIENT_CAREGIVER
CLINICAL_PROFESSIONAL
LEARNER_RESEARCHER
```

Finer personas are metadata/evaluation slices unless D-003 changes later.

### 12.2 Required curriculum domains

At minimum:

- factual medical fundamentals;
- clinical problem representation;
- differential reasoning;
- active information acquisition;
- patient explanation;
- professional workflow;
- evidence use;
- uncertainty/abstention;
- deterministic tools/structured outputs;
- English/Arabic clinical language;
- adversarial/unsafe cases.

### 12.3 Coverage dimensions

Coverage reporting should include:

- role;
- specialty/domain;
- reasoning type;
- risk/severity;
- missing-information pattern;
- evidence/tool requirement;
- outcome state;
- language/register;
- communication difficulty;
- source concentration;
- verification/review state;
- duplicate/near-duplicate burden;
- contamination state;
- multi-turn proportion;
- rendered supervised-token contribution;
- knowledge-placement disposition.

No fixed row count is accepted as evidence of readiness by itself.

### 12.4 Duplicate and contamination firewall

Run at both raw-record and post-transformation/rendering stages:

- exact duplicates;
- normalized near duplicates;
- benchmark overlap;
- canonical quarantine-source matching;
- repeated-content concentration.

Post-rendering transformations must not reintroduce overlap.

### 12.5 Knowledge placement

Every proposed record receives one of:

```text
DURABLE_WEIGHT_ELIGIBLE
MUTABLE_RUNTIME_EVIDENCE_PREFERRED
DETERMINISTIC_TOOL_REQUIRED
REJECTED
```

Current guidelines, formularies, interactions, jurisdictional pathways, local routing, and rapidly changing evidence default away from weights when authoritative runtime retrieval/tools are more appropriate.

## 13. Failure-conditioned development hooks

Spec 007 control-plane implementation should define the taxonomy and evidence structure for a future loop, but must not run the loop before training/data authority exists.

Future authorized lifecycle:

```text
QUALIFIED NON-PROTECTED DEVELOPMENT FAILURE
-> FAILURE TAXONOMY
-> ROOT-CAUSE CLASS
-> REMEDIATION SURFACE DECISION
-> VERIFIED/LICENSE-CLEAN REPAIR DATA IF TRAINING IS APPROPRIATE
-> NEW DATASET SNAPSHOT
-> NEW SEPARATELY AUTHORIZED EXPERIMENT
```

Possible remediation surfaces:

- SFT data;
- retrieval/evidence;
- deterministic tool;
- safety rule;
- evaluation repair;
- no action.

Private Gold/final/release evidence is never recycled into optimization.

## 14. Multi-turn behavioral curriculum

Training representation must support trajectories such as:

```text
UNDER-SPECIFIED -> ASK_MORE
CONTEXT ACQUIRED -> ANSWER
AUTHORITATIVE EVIDENCE NEEDED -> RETRIEVE_EVIDENCE
DETERMINISTIC TOOL NEEDED -> USE_TOOL
UNSUPPORTED / INSUFFICIENT -> ABSTAIN
HIGH RISK -> ESCALATE
EMERGENCY POLICY -> EMERGENCY
```

Single-turn MCQ competence cannot satisfy SFT V1.

## 15. Medical tool intelligence

Future curriculum/evaluation fixtures must cover:

- valid tool selection;
- nonexistent tool hallucination;
- malformed/missing arguments;
- unavailable tool;
- multi-turn continuation after results;
- spoofed provenance/results;
- conflicting authoritative results;
- format/schema sensitivity;
- required abstention/escalation.

Generative text may never replace deterministic safety-critical arithmetic, validated scores, interaction checks, or schema validation when authoritative mechanisms exist.

## 16. Abstention as positive behavior

Dedicated coverage is required for:

- missing critical information;
- contradictory facts;
- ambiguity;
- OOD/unsupported requests;
- insufficient evidence;
- tool unavailability;
- safety conflicts.

Future evaluation should expose risk-vs-coverage behavior, dangerous over-answering, unnecessary abstention, information acquisition, and escalation/over-triage behavior. No single confidence scalar is sufficient.

## 17. Arabic as a first-class capability

### 17.1 Metadata

Where applicable, Arabic records include:

- original language;
- translation/transcreation state;
- dialect/register;
- MSA vs Saudi/Gulf colloquial;
- English-Arabic code switching;
- transliteration state;
- medication/clinical-term normalization identity;
- qualified review status.

Machine translation alone does not prove clinical validity.

### 17.2 Future candidate evidence

Founder+ChatGPT candidate packet should eventually include matched medical-language tokenizer measurements:

- tokens/word;
- characters/token;
- medication-name fragmentation;
- clinical-term fragmentation;
- MSA;
- Saudi/Gulf colloquial;
- code-switch;
- transliterated medical terminology.

Pi reports; Pi does not select.

## 18. Rendering, masking, packing, truncation

These are P0 training-contract surfaces.

### 18.1 Rendering

Before a future run, bind exact tokenizer/template revisions and deterministic representative conformance fixtures.

### 18.2 Loss masking

Tests must prove that only frozen target token classes contribute supervised loss. A backend is inadmissible if this cannot be verified.

### 18.3 Packing

`NEEDS_EVIDENCE` until concrete backend support is known. If enabled, implementation must prove no unintended cross-example attention or label bleed.

### 18.4 Truncation/segmentation

Never silently remove:

- required patient facts;
- safety/emergency context;
- tool schema needed by the target;
- supervised target;
- relevant conversation state.

Examples that cannot be represented safely are rejected or deterministically segmented with typed reason codes.

## 19. Safety-preservation and catastrophic-forgetting controls

Before any future run, freeze base qualification evidence for required dimensions. Protected evidence remains qualification-only.

### 19.1 Optional abort-only sentinel

A future `SFT_ABORT_SENTINEL_SET` is allowed only if it is:

- outside the prohibited quarantine set for its exact monitoring purpose;
- provenance/license/split/contamination verified;
- excluded from gradient-bearing data;
- threshold-frozen pre-run;
- limited to `CONTINUE`, `ABORT_RUN`, `DISQUALIFY_RUN`.

It cannot:

- rank checkpoints;
- select recipe/update strategy;
- change hyperparameters;
- prefer an early-stopping checkpoint;
- select a model.

### 19.2 Final qualification

After the checkpoint identity is determined using the pre-registered quarantine-safe rule, run the frozen full qualification. Final results cannot be used to modify the same recipe/checkpoint while retaining untouched-holdout status.

## 20. Checkpoint-selection firewall

Default policy:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
RULE=FINAL_CHECKPOINT_AT_FROZEN_STEP_OR_TOKEN_BUDGET
```

Training loss, human inspection, LLM judges, protected development assets, or abort-only sentinels cannot override it.

Any future evidence-ranked checkpoint policy requires a separately canonical, non-quarantined source/purpose authority frozen before the run.

## 21. Evaluation portfolio

Spec 007 uses inherited canonical evaluation identities first.

New external suites are candidates only after exact version, license, purpose, split, and contamination review. The portfolio should eventually cover:

- factual knowledge;
- clinical reasoning;
- open-ended health conversations;
- active follow-up questioning;
- evidence fidelity;
- professional workflows;
- tool behavior;
- multi-turn drift;
- selective risk/abstention;
- emergency/escalation;
- Arabic;
- adversarial robustness;
- resource efficiency.

Traditional exam QA is supporting evidence, not the sole objective.

Judge-based scores never override deterministic hard gates and protected judge results cannot leak into tuning.

## 22. Medical intelligence density and record classes

Spec 007 control-plane implementation may define/validate record-class and scorecard schemas, but it cannot claim a record.

Candidate future record classes include:

- best verified medical quality in a defined small-resource class;
- quality per shipped GB;
- quality per peak memory;
- Arabic+English quality in the same class;
- selective-risk/abstention frontier;
- medical tool-use reliability;
- patient communication utility;
- open-ended medical utility per parameter;
- energy per medically correct qualified case;
- correctness per reasoning token;
- capability retention after compression;
- real-device Pareto frontier.

Every future `#1`, `SOTA`, `best`, or `record` claim requires a pre-existing `RecordClassDefinition` and independently auditable evidence. Safety hard-gate failure makes a candidate ineligible regardless of headline score.

## 23. Training backend neutrality

Backend remains `NEEDS_EVIDENCE`.

Potential implementations such as Transformers/TRL/PEFT, Axolotl, Unsloth, Liger-assisted paths, or later alternatives are **candidates only**.

Before any future training authorization, a `BackendCandidateEvidence` assessment must establish, without executing model weights where authority is absent:

- winner-architecture support;
- tokenizer/chat-template fidelity;
- exact loss-mask semantics;
- packing/truncation support;
- resume-state fidelity;
- reproducibility controls;
- required precision/update-strategy support;
- offline/no-hidden-telemetry compatibility;
- maintainability and dependency cost.

Optimization claims from a backend vendor are not scientific qualification by themselves.

## 24. Update strategy neutrality

`FULL`, `LORA`, and `QLORA` remain unresolved.

A future choice may use static/non-executing evidence such as:

- selected winner architecture;
- static memory estimates;
- deployment artifact needs;
- backend support;
- license posture;
- reproducibility requirements.

If empirical gradient/convergence evidence is needed, it requires a separately authorized training experiment first.

## 25. Memorization and regurgitation audit

Pre-run audit contract should cover:

- exact/near duplicate reports;
- source concentration;
- benchmark overlap;
- repeated rare sequences;
- safe synthetic canaries if useful;
- bounded regurgitation probes;
- acceptance/failure criteria.

PHI, credentials, secrets, Private Gold, or restricted content may not be used as canaries.

## 26. Reproducibility

### 26.1 Exact environment replay

Strongest reproducibility inside a fully pinned approved environment:

- same model/tokenizer/template/data/config;
- same software/device class;
- same seeds/data order;
- deterministic algorithms where available;
- explicit list of remaining nondeterminism.

### 26.2 Cross-environment reproducibility

Do not promise bitwise-identical weights across different accelerator/software stacks. Compare frozen statistical/behavioral outputs under pre-registered tolerances instead.

## 27. Resume integrity

A future interrupted-run test must prove restoration of:

- model/adapter;
- optimizer;
- scheduler;
- scaler if used;
- RNG;
- data cursor/order;
- global step;
- all recipe and environment identities.

A model-only export is not a resumable training checkpoint.

## 28. Founder + ChatGPT candidate decision packet

Pi's future output is neutral evidence only.

Required candidate fields should include:

- exact model/checkpoint identity;
- license/release-lineage compatibility;
- total and active parameter accounting;
- weight/package bytes;
- tokenizer/template identities;
- Arabic tokenizer-efficiency evidence;
- core medical performance;
- patient conversation performance;
- abstention/selective risk;
- Arabic/English performance;
- tool behavior;
- general-capability preservation potential;
- supported training/tooling evidence;
- memory/device evidence;
- runtime/export compatibility;
- known limitations;
- tournament qualification/disqualification reason codes.

Output contract:

```text
PI_RECOMMENDATION=NONE
CANDIDATE_RESULTS=<EVIDENCE_ONLY>
DECISION_OWNER=FOUNDER+CHATGPT
```

## 29. Run activation — fail closed

Future training activation fails if any required identity/evidence is missing, stale, or mismatched, including:

- winner decision;
- base checkpoint binding;
- license evidence;
- tokenizer/template/rendering;
- loss-mask policy;
- dataset snapshot;
- provenance/quarantine pass;
- duplicate/contamination audit;
- capability-preservation binding;
- checkpoint-selection policy;
- frozen evaluation protocol;
- environment/backend identity;
- training configuration;
- non-executing recipe evidence;
- access grants;
- device requirement if applicable;
- finance authorization;
- training authorization.

A valid schema does not substitute for authority.

## 30. Offline implementation scope after separate authorization

When and only when implementation is later authorized, expected offline work includes:

- parsers/validators for all planned record types;
- deterministic identity generation;
- canonical JSON serialization where repository precedent requires it;
- full quarantine matrix enforcement;
- rendering/mask contract validation;
- packing/truncation admission rules;
- coverage reports;
- fixed checkpoint-policy validation;
- environment/resume manifest validation;
- record-class/resource scorecard validation;
- failure taxonomy validation;
- composed activation preflight that remains non-executing;
- synthetic fixtures and regression tests.

No trainer or model runtime is required to complete this offline control plane unless a later authorized task proves otherwise.

## 31. Verification plan

Implementation-stage TDD will be required for every fail-closed rule.

Baseline repository checks at planning qualification:

```bash
python3 -m compileall -q src tests
pytest -q
git diff --check
```

Future focused tests must prove at minimum:

- closed vocabularies;
- deterministic identities;
- strict schemas / undeclared-field rejection where applicable;
- full Spec 003 identity requirements;
- duplicate and contamination rejection;
- complete quarantine purpose enforcement;
- calibration split restricted to calibration;
- abort-only sentinel cannot tune/rank;
- fixed checkpoint selection default;
- execution-derived recipe evidence rejected before authority;
- role/domain/language coverage accounting;
- rendering identity changes on template changes;
- deterministic loss-mask boundary validation;
- safe truncation/packing admission;
- Arabic metadata validation;
- environment manifest completeness;
- resumable-vs-export checkpoint distinction;
- resource/record-class scorecard validation;
- failure-taxonomy validation;
- activation prerequisites;
- no network/model/weight/training surface in offline validators.

Never hard-code an old test count as a current PASS claim.

## 32. Planning task streams

The resulting `tasks.md` must be dependency-ordered approximately as:

```text
P0  lifecycle/evidence/authority identities
P1  data model + closed vocabularies
P2  curriculum/provenance/quarantine contracts
P3  tokenizer/template/rendering/loss-mask contracts
P4  packing/truncation + multi-turn/tool contracts
P5  Arabic metadata + tokenizer-evidence packet contract
P6  abstention + capability-preservation + abort-sentinel contracts
P7  checkpoint-selection firewall
P8  environment/reproducibility/resume contracts
P9  medical-intelligence-density record/resource/scorecard contracts
P10 failure taxonomy + future development-loop contract
P11 non-executing recipe evidence + RunManifest + activation composition
P12 quickstart + synthetic fixture matrix
P13 requirements checklist + static analyze
P14 full planning qualification + exact-head independent review
P15 STOP at implementation/model/tournament/training authority gates
```

Tasks must clearly distinguish planning-complete work, future offline implementation tasks, and external evidence/authority gates.

## 33. Downstream research handoffs — not Spec 007 scope

This plan records interfaces only:

- **Spec 008:** CPT vs no-CPT plus data-efficiency/hardness ablations;
- **Spec 009:** failure-conditioned/on-policy distillation versus simpler baseline;
- **Spec 010:** verifiable RL plus reasoning-token efficiency where rewards are defensible;
- **Spec 011:** stratified calibration/selective risk;
- **Spec 012:** BF16→Q8→Q6/Q5→Q4 PTQ, QAD experiment, QAT/recovery if justified, then lower-bit research;
- **Spec 013:** measured Arabic gap closure/tokenizer-efficiency work;
- **Spec 015:** real patient/professional human utility evidence;
- **Spec 017:** independent record/claim audit and Hugging Face/paper evidence package.

No downstream spec is authorized by this plan.

## 34. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Trainer defaults silently change objective | explicit rendering + loss-mask contracts |
| Benchmark/Gold leakage through monitoring | full purpose-aware quarantine firewall |
| SFT causes safety regression | base qualification + hard final gates + optional abort-only sentinel |
| Catastrophic forgetting | paired capability-preservation qualification |
| Arabic weakness hidden by aggregate score | dedicated strata + tokenizer fragmentation evidence |
| Tool hallucination | multi-turn negative fixtures + Spec 006 composition |
| Stale medical truth consumes model capacity | knowledge-placement disposition |
| Dataset volume substitutes for quality | coverage/token accounting, no row-count readiness |
| Record chasing biases development | pre-registered claim classes; protected evidence not tuning input |
| Backend marketing drives architecture | neutral backend evidence contract |
| Unauthorized empirical pilot | all gradient-bearing probes classified as training |
| False reproducibility claim | exact-environment vs cross-environment distinction |
| Non-resumable experiments | full checkpoint-state manifest |
| Pi selects a model | Founder+ChatGPT-only gate + evidence-only packet |
| Premature Nano work dilutes Core | explicit Core→Nano later gate |
| Overengineering | Ponytail discipline, reuse existing modules, minimal dependencies |

## 35. Explicit exclusions

This planning package does not authorize or perform:

- Pi model selection or ranking;
- backbone selection;
- model/weight access;
- live tournament execution;
- real benchmark payload execution;
- SFT/LoRA/QLoRA/full fine-tuning;
- training pilots or gradient probes;
- CPT;
- distillation;
- DPO/preference optimization;
- RL/RLVR/GRPO;
- QAT/QAD execution;
- quantization/device execution;
- Private Gold access;
- PHI/restricted data access;
- provider-generated training data;
- paid compute/spend;
- clinician/human evaluation;
- multimodal training;
- public record/SOTA claims.

## 36. Plan exit criteria

The Spec 007 planning package is qualifiable only when repository artifacts prove:

```text
PLAN_COMPLETE=YES
DATA_MODEL_COMPLETE=YES
CONTRACT_SET_COMPLETE=YES
QUICKSTART_COMPLETE=YES
REQUIREMENTS_CHECKLIST_COMPLETE=YES
TASKS_DEPENDENCY_ORDERED=YES
STATIC_ANALYZE_CRITICAL=0
STATIC_ANALYZE_HIGH=0
UNRESOLVED_HARD_CONTRADICTIONS=0
MODEL_SELECTED=NO
BACKEND_SELECTED=NO
REAL_DATASET_CONSTRUCTED=NO
MODEL_EXECUTION=NO
TRAINING_EXECUTED=NO
TRAINING_AUTHORITY=NONE
```

Material review findings must be repaired and the exact current head re-reviewed before canonical merge.

After planning becomes canonical, implementation still requires a separate founder authorization. Model/tournament/training gates remain separately controlled.
