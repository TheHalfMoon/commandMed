# CommandMed v2 Internal Source Map

**Snapshot date:** 2026-09-29  
**Purpose:** identify reusable research knowledge already present across TheHalfMoon repositories before duplicating work  
**Status:** planning reference only; no donor code or model artifact is admitted by this document

## 1. Why this map exists

CommandMed v2 should reuse proven research artifacts, literature mapping, evaluation ideas, and governance patterns from the founder's existing repositories where they are relevant and license/provenance compatible.

This does **not** mean copying code blindly. Every source must still be classified under CommandMed's external/internal source-adoption rules, and historical evidence remains bound to its original repository/revision.

## 2. Gax — strongest System-One / medical decision research source

Repository:

```text
TheHalfMoon/Gax
snapshot observed: a1432dc81d48407c551b1b8ddefefa478a2cd33f
```

High-value artifacts:

- `docs/research/LITERATURE_MAP.md`
- `docs/research/MASTER_PLAN.md`
- `docs/research/P08_EVALUATION_PROTOCOL.md`
- `docs/research/P08_REAL_INVENTORY.md`
- `registry/baselines.json`
- `registry/p08_real_inventory.json`
- `paper/references.bib`

What CommandMed should reuse conceptually:

- TypeSafe Jev as a System-One reference, without inferring unpublished internals;
- `Contrastive-LM/CLM` as a state/action contrastive baseline;
- Laya as a compact non-autoregressive typed-decision baseline;
- `Mapika/decider` as a Qwen-family one-pass typed-decision baseline;
- restricted-logit/open-Jev alternatives as no-task-training controls;
- calibration, proper-scoring, selective-risk, and AURC evaluation;
- MedAgentBench/FHIR-AgentBench for action selection and FHIR-oriented evaluation;
- Med-PRM-style evidence verification as neighboring verifier research;
- MedQAbstain-style missing-information/overcommitment evaluation;
- explicit negative-result and blocked-baseline accounting.

CommandMed-specific extension:

Gax studies the decision-model class itself. CommandMed v2 should study whether a comparable decision capability can become a native head/path of the same medical checkpoint that also generates language and images.

## 3. MESC — Qwen3.8 and medical evaluation/research governance

Repository:

```text
TheHalfMoon/MESC
snapshot observed in current search results: 6a18b317a384749431146a8f3f7c1747e6e0f3bb
```

High-value artifacts observed:

- `specs/mesc-experiment-0/README.md`
- `docs/adr/0036-performance-first-health-model-strategy.md`
- `docs/strategy/mesc_health_model_program_2026-09-05.md`
- `docs/strategy/mesc_health_model_architecture_2026-09-05.md`
- `specs/mesc-backbone-tournament/CURRENT_STATUS.md`
- `specs/mesc-research-loop-v1/mrl-0801-active-candidate-set-v1.md`
- runtime feasibility and candidate-roster tooling around `Qwen/Qwen3.8-27B`

What CommandMed should reuse conceptually:

- exact-revision freezing for Qwen3.8-27B;
- resource-first medical model evaluation;
- evidence-first separation between a preferred strategy candidate and a proven winner;
- no unsupported model-family merging without a scientifically valid method;
- contamination, exact identity, runtime feasibility, and no-fabrication discipline;
- medical evidence/citation and FHIR-aware evaluation experience where applicable.

Important distinction:

MESC's Qwen3.8 work is evidence about that repository's research program. CommandMed must not import MESC performance claims without re-running the relevant CommandMed protocol.

## 4. Inercative — CLM deep dive and source-adoption discipline

Repository:

```text
TheHalfMoon/Inercative
snapshot observed: 3a4713c47d36722c564f185bc4a8c02ad57da05c
```

High-value artifacts:

- `docs/research/CLM_INTERNAL_SOURCE_DEEP_DIVE_2026-09-24.md`
- `docs/canonical/SOURCE_LEDGER.md`

The Inercative deep dive records:

```text
Contrastive-LM/CLM revision:
7956937c58ed5839c06ddc4dc6b6b61c3a3e4094
observed code/weights license: Apache-2.0
```

What CommandMed should reuse conceptually:

- state/action disaggregation;
- candidate ranking and fast typed decisions;
- action-vector caching;
- fine-tunable projection heads;
- explicit source revision/license recording;
- separating `REFERENCE`, `ADAPT`, `DEPEND`, and benchmark roles rather than treating a useful source as automatic production code.

## 5. MSTR — broad model landscape and lineage screening

Repository:

```text
TheHalfMoon/MSTR
snapshot observed: e87328872232471fa0e1eb05d74223bc0aeaafd3
```

High-value artifacts:

- `evidence/T021-landscape-rescan.md`
- `artifacts/candidates/*`
- `docs/canonical/TRAINING_EXECUTION_STRATEGY.md`
- `specs/002-code-model-supremacy-foundation/research.md`

What CommandMed should reuse conceptually:

- broad candidate scanning before lineage lock;
- exact upstream revision and license recording;
- distinguishing reference/teacher candidates from releasable foundation lineage;
- explicit warning that teacher output is evidence candidate rather than truth;
- evidence-first compute/training gates.

MSTR also contains prior Arcee-family candidate research, which is useful context when adding Arcee AI MergeKit to the CommandMed external source ledger.

## 6. CommandMed historical assets that remain useful

Existing CommandMed v0.1 work should not be discarded.

Retain and adapt where still valid:

- evaluation-before-optimization constitution;
- exact provenance/license/data-lineage contracts;
- contamination and holdout quarantine;
- deterministic safety/tool boundaries;
- Arabic/English medical evaluation;
- private Gold design;
- patient/professional role slicing;
- resource accounting;
- quantization re-gating;
- evidence/citation fidelity;
- active-information acquisition;
- security and agent/tool trust work;
- negative-result and fail-closed governance.

The architecture thesis changes; assurance work does not become obsolete merely because the model architecture changes.

## 7. Source adoption priorities for v2

### Priority A — direct research reuse

- Gax literature/baseline taxonomy;
- MESC Qwen3.8 identity/resource research;
- Inercative CLM deep dive;
- CommandMed existing evaluation/safety/provenance framework.

### Priority B — external sources to freeze next

- `QwenLM/Qwen3.8` / `Qwen/Qwen3.8-27B`;
- `QwenLM/Qwen-Image-2.1`;
- `jaredpalmer/kev`;
- `Mapika/decider`;
- `Contrastive-LM/CLM`;
- `arcee-ai/mergekit`;
- `WalkerWorldPeace/MLLMerging` (OptMerge);
- `Littleor/ExpertMerging`;
- MedUAG;
- UniMedVL;
- SynerMedGen.

### Priority C — medical evaluation sources

Refresh the strongest currently reproducible representatives for:

- clinical reasoning;
- multimodal medicine;
- evidence/citation verification;
- FHIR/EHR action selection;
- abstention/selective prediction;
- patient communication;
- Arabic clinical language;
- medical image generation/editing.

## 8. Reuse rule

A source from another TheHalfMoon repository may provide:

- a literature reference;
- a design pattern;
- a frozen upstream revision;
- a test/evaluation idea;
- a governance pattern;
- reusable code when provenance and license permit.

It does not automatically provide:

- CommandMed empirical evidence;
- CommandMed training authority;
- CommandMed release rights;
- CommandMed clinical claims;
- a valid cross-repository benchmark result.

Every promoted v2 claim must be generated under CommandMed's own frozen protocol.