# COMMANDMED GRAND MASTER PLAN v2.0

**Date:** 2026-09-29  
**Status:** PROPOSED RESEARCH RESET — NO TRAINING OR MODEL EXECUTION AUTHORITY  
**Supersedes for prospective planning:** `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`  
**Preserves:** all prior canonical evidence, exact identities, closed specs, historical decisions, and negative results  
**Training authority:** NONE  
**Model execution authority:** unchanged from the current bounded spec  

## 0. Purpose of this reset

CommandMed v2 changes the research thesis before expensive training begins.

The primary research target is no longer a compact medical system that may be composed from multiple independently served neural models. The new primary target is a **single-checkpoint medical foundation model** that unifies three computational capabilities inside one model artifact:

1. autoregressive medical language and multimodal reasoning;
2. one-pass typed medical decisions with calibrated probability distributions;
3. image generation/editing through a flow/diffusion visual-generation path.

The working architecture name is **CommandMed One**. The working method name is **Heterogeneous Capability Fusion (HCF)**. Both names are provisional and may change before publication.

This document is a roadmap and scientific design. It does not authorize downloading weights, running models, training, benchmarking, spending money, accessing restricted assets, or bypassing any existing bounded-spec authority.

## 1. Research thesis

### 1.1 Primary thesis

The central hypothesis is:

> A shared Qwen-family medical representation can support autoregressive clinical reasoning, native multimodal understanding, calibrated one-pass typed decisions, and visual generation in one checkpoint, while eliminating duplicated semantic encoders and preserving or improving capability-per-byte relative to separately served specialist models.

The paper is not justified by merely placing several modules in one package. The contribution must be demonstrated through measurable representation sharing, capability transfer, parameter duplication reduction, controlled ablations, and strong comparison with model-merging and joint-training baselines.

### 1.2 What “one model” means

For this program, a qualifying single model must satisfy all of the following:

- one versioned model artifact/checkpoint family;
- one model class and one inference contract;
- one shared semantic/medical backbone used by language, decision, and visual-generation paths;
- no separately served Jev-like decision model;
- no separately served Qwen-Image text/condition encoder after the target architecture is reached;
- no external orchestration that chooses between independently complete foundation models to create the appearance of unity;
- task-specific heads/modules are allowed when they are components of the same checkpoint and depend on the shared backbone;
- deterministic clinical tools may remain external because deterministic authority is intentionally not replaced by neural inference.

A single checkpoint does not require every tensor to have the same transformer architecture. A unified model may contain a shared Qwen semantic backbone, a decision head, a visual-generation DiT, and a VAE, provided they are trained/qualified as one model and do not duplicate a second complete semantic foundation model.

### 1.3 What this paper must not claim without evidence

Do not claim any of the following before the corresponding evidence exists:

- “best medical model”;
- “first unified medical model”;
- “first model to understand and generate medical images”;
- “clinically safe”;
- “SOTA”;
- “revolutionary” as a scientific conclusion;
- “no uncertainty” or perfect certainty;
- superiority caused by merging rather than by scale, data, evaluation leakage, or extra compute.

The project may aim for a revolutionary result. The paper must earn that description through experiments.

## 2. Foundation lineage

### 2.1 Primary semantic backbone candidate

The current preferred research backbone is:

```text
Qwen/Qwen3.8-27B
```

Rationale at the 2026-09-29 landscape snapshot:

- current Qwen open-family flagship dense model at this scale;
- native multimodal image-text understanding;
- 27B dense capacity suitable for a high-capability research teacher/core;
- Apache-2.0 model license reported by the upstream model repository;
- already studied elsewhere in TheHalfMoon research programs;
- compatible in principle with the currently released Kev-27B decision architecture because Kev-27B also uses Qwen3.8-27B as its backbone.

This is a **preferred research donor**, not a scientifically proven winner. The exact revision, architecture, tokenizer, processor, license, and redistribution implications must be frozen before any authorized execution.

### 2.2 System-One / Jev-like capability donors and baselines

Primary open references:

- `jaredpalmer/kev` — Qwen-family one-pass decision models; Kev-27B is a LoRA plus pointer head on Qwen3.8-27B;
- `Mapika/decider` — Qwen3.5-family one-pass typed decisions with explicit probability distributions, calibration metrics, and vision experiments;
- `Contrastive-LM/CLM` — contrastive state/action modeling and cached action representations;
- `NandhaKishorM/laya` — compact non-autoregressive typed-decision approach;
- `ikermoel/open-alternative-jev` — restricted-logit no-task-training baseline;
- other Gax-registered baselines only after exact revision/license/access freeze.

CommandMed must not copy unpublished Jev internals by inference. TypeSafe Jev may be used only as an externally measurable baseline when terms and reproducibility allow it.

### 2.3 Image-generation donor

Primary frontier research donor:

```text
QwenLM/Qwen-Image-2.1
```

Observed architecture at the 2026-09-29 snapshot:

- 7B, 32-layer single-stream DiT visual-generation component;
- Qwen3-VL-8B text/condition encoder;
- VAE supporting RGBA/transparency;
- flow-matching scheduler;
- text-to-image generation and image editing.

The key research opportunity is to **remove the duplicate Qwen3-VL-8B semantic encoder** from the target unified architecture and condition the visual-generation path from representations produced by the shared CommandMed/Qwen3.8 backbone.

### 2.4 Qwen-Image-2.1 licensing constraint

Qwen-Image-2.1 is distributed under a Qwen Research License at this snapshot, not the same permissive Apache-2.0 posture as Qwen3.8-27B.

Therefore CommandMed v2 has two separate lineages:

- **Frontier research lineage:** may study Qwen-Image-2.1 only when its exact research terms permit the planned experiment. A paper does not imply that derived weights can be redistributed or commercialized.
- **Permissive release lineage:** must use components whose complete derivative chain supports the founder’s intended open-weight/permissive downstream posture. Qwen-Image/Qwen-Image-2.0-family assets or another permissive donor may be evaluated when exact terms are proven compatible.

No distillation, transplantation, or weight transformation is assumed to erase upstream license obligations. Rights analysis is a hard gate.

## 3. Target architecture: CommandMed One

### 3.1 High-level structure

```text
                       multimodal input
                text / image / document / EHR
                              |
                              v
                +---------------------------+
                | Shared CommandMed/Qwen    |
                | medical semantic backbone |
                +-------------+-------------+
                              |
            +-----------------+------------------+
            |                 |                  |
            v                 v                  v
     Generative LM       Decision head     Visual bridge
       language          typed choices       projector
     / reasoning       probabilities             |
            |                 |                  v
            |                 |            image DiT
            |                 |                  |
            |                 |                 VAE
            |                 |                  |
            v                 v                  v
          text         typed decisions         image
```

### 3.2 Shared semantic backbone

The shared backbone owns:

- medical and biomedical representation;
- English and Arabic clinical language;
- multimodal image understanding;
- document/lab understanding where qualified;
- evidence-grounded reasoning representations;
- tool/FHIR intent and structured reasoning;
- shared hidden states consumed by the decision and image-generation paths.

The backbone does not replace deterministic calculators, authoritative drug-interaction sources, schema validators, or hard safety rules.

### 3.3 Language head

The ordinary autoregressive path supports:

- clinical reasoning and explanation;
- patient/caregiver communication;
- professional workflow assistance;
- evidence-grounded synthesis;
- structured outputs and tool calls;
- Arabic/English bilingual operation;
- multimodal understanding.

### 3.4 Native decision head

The decision path is part of the same checkpoint. It should return typed distributions without autoregressive prose decoding.

Candidate decision primitives:

```text
NOUL    -> probability of yes/no
CHOICE  -> probability over explicit options
SCORE   -> probability over ordered levels
RANK    -> distribution/ranking over candidate actions
```

Medical examples include:

- presence/absence of a specified red flag;
- next best information request from a fixed candidate set;
- tool-selection decision;
- evidence-sufficiency decision;
- triage class under a frozen policy;
- citation-support verdict;
- contradiction detection;
- structured finding classification.

The target is not a second decision model. It is a head/adapter path attached to the shared backbone and trained jointly or through controlled capability transplantation.

### 3.5 Probability and calibration policy

CommandMed v2 will not contain a separate “uncertainty model.” Probability quality is intrinsic to the native decision path.

The model must be evaluated with proper scoring and selective prediction metrics such as:

- NLL;
- Brier score;
- ECE or stronger calibration diagnostics;
- risk-coverage/AURC;
- class/task/language-specific calibration;
- confidence under missing, contradictory, OOD, and adversarial input.

The scientific goal is calibrated decisiveness, not unsupported certainty. A model that is always certain is not considered stronger.

### 3.6 Visual-generation path

The initial donor architecture contains a dedicated Qwen3-VL-8B encoder before the Qwen-Image-2.1 DiT. The CommandMed target replaces that duplicated encoder with a learned bridge from the shared Qwen3.8/CommandMed hidden representation.

Target:

```text
shared CommandMed hidden states
           |
           v
representation adapter / projector
           |
           v
Qwen-Image-derived DiT
           |
           v
VAE
           |
           v
image
```

Research must test whether the bridge can preserve visual-generation quality while reducing duplicate semantic parameters and enabling medically useful shared representations.

### 3.7 Generated-image truth boundary

Generated pixels are not clinical evidence.

A generated or edited image must never silently become the evidence used to diagnose the original input. All experiments must distinguish:

- observed patient/source image;
- model-derived interpretation;
- generated educational/synthetic image;
- edited visualization;
- benchmark target.

Clinical-image generation may be studied for education, simulation, annotation, counterfactual research, reconstruction, augmentation, and representation analysis, but downstream diagnostic claims require modality-specific validation.

## 4. Heterogeneous Capability Fusion (HCF)

### 4.1 Research problem

Conventional weight merging is strongest when models share architecture and parameter correspondence. CommandMed intentionally combines three different computational behaviors:

- autoregressive token generation;
- one-pass typed decision readout;
- flow/diffusion visual generation.

Simple tensor averaging cannot directly merge all of them because the image-generation DiT and VAE do not share a one-to-one parameter structure with the causal language backbone.

HCF is the research program for combining them while preserving one shared semantic model.

### 4.2 HCF stages

HCF should be decomposed and falsified stage by stage:

1. **Shared-base expert merging** — merge compatible Qwen3.8 medical adapters/task vectors into one semantic backbone.
2. **Decision capability transplantation** — attach and adapt a pointer/decision head and, where justified, transfer compatible low-rank/task-vector updates from Kev/decider-style training.
3. **Representation alignment** — learn a mapping from shared Qwen hidden states to the conditioning representation expected by the image-generation DiT.
4. **Encoder replacement** — remove/freeze out the original Qwen3-VL image-model encoder and measure whether the shared backbone can replace it.
5. **Joint stabilization** — train a bounded multi-objective stage so improvements in one path do not catastrophically degrade the others.
6. **Compression/merge consolidation** — where empirically justified, consolidate compatible adapters/deltas using model-merging methods into the shared backbone.

### 4.3 Candidate objective

A conceptual multi-objective form is:

```text
L_total =
    lambda_lm       * L_lm
  + lambda_decision * L_decision
  + lambda_flow     * L_flow
  + lambda_align    * L_representation
  + lambda_ground   * L_medical_grounding
  + lambda_preserve * L_capability_preservation
```

The exact losses, coefficients, curricula, and optimizer schedules are experimental variables and must be pre-registered before confirmatory runs.

### 4.4 Merge baselines

At minimum, compatible Qwen expert merging must compare against:

- simple linear averaging/model soup where valid;
- SLERP or generalized interpolation where valid;
- task arithmetic;
- TIES;
- DARE-TIES;
- DELLA;
- Model Stock;
- Arcee Fusion;
- relevant MergeKit multi-stage configurations;
- OptMerge where architecture/task assumptions apply;
- Expert Merging / Expert Merging++ where reproducible;
- ordinary adapter composition;
- joint multitask training from the same starting checkpoint;
- separate specialist models at matched total parameter/storage cost.

MergeKit is a baseline/tooling dependency candidate, not the novelty claim by itself.

## 5. Scientific questions

### RQ1 — Can one shared Qwen semantic backbone replace separately served language and typed-decision foundation models?

Measure decision quality, generation quality, latency, memory, and interference.

### RQ2 — Can shared Qwen hidden states replace the Qwen-Image semantic encoder?

Measure image-generation/editing quality, alignment, identity preservation, text rendering where relevant, and medical-task fidelity.

### RQ3 — Does heterogeneous fusion beat naive joint training or orchestration?

Compare HCF against joint multitask training, adapters, conventional merging, and multiple-model serving under matched resource accounting.

### RQ4 — Is there positive transfer between medical understanding, decisions, and visual generation?

Test whether training one capability improves or harms the others and whether shared representation alignment explains transfer.

### RQ5 — Does a single checkpoint improve efficiency?

Report installed bytes, active/resident memory, duplicated parameters removed, TTFT/decision latency, image-generation latency, throughput, and energy on named hardware where feasible.

### RQ6 — Does the unified model preserve calibration and safety?

Measure probability quality and hard medical safety gates independently from average capability.

### RQ7 — Does bilingual medical specialization survive heterogeneous fusion?

Measure English, Modern Standard Arabic, Saudi/Gulf colloquial Arabic, code switching, medication-name variants, and clinical terminology.

## 6. Novelty boundary and related-work positioning

As of the 2026-09-29 landscape snapshot, unified medical understanding-and-generation is already an active research area. MedUAG, UniMedVL, and SynerMedGen are evidence that “one medical model can understand and generate images” is not sufficient novelty.

CommandMed should therefore position its prospective contribution around the intersection of:

```text
medical foundation modeling
        x
autoregressive reasoning
        x
one-pass calibrated typed decisions
        x
visual flow/diffusion generation
        x
heterogeneous capability/model fusion
        x
single-checkpoint efficiency
```

The strongest paper claim, if supported, is not “we added image generation.” It is that heterogeneous computational paradigms can be consolidated around a shared medical semantic backbone with measurable parameter reuse and preserved specialist quality.

A formal literature refresh is mandatory before submission. Any “first” claim must be backed by a documented search protocol and narrowed if concurrent work closes the gap.

## 7. Evaluation hierarchy

### 7.1 Four independent scorecards

Do not collapse the research into one headline average.

**A. Medical reasoning and communication**

- medical knowledge/reasoning suites;
- evidence-grounded QA;
- longitudinal cases;
- patient communication;
- professional workflow utility;
- Arabic/English slices.

**B. Typed decision quality**

- accuracy;
- NLL/Brier;
- calibration;
- risk-coverage/AURC;
- missing-information and contradiction cases;
- tool/FHIR routing;
- clinical decision tasks with verifiable labels.

**C. Multimodal understanding and visual generation**

- medical-image understanding;
- document/lab extraction;
- image generation/editing benchmarks;
- modality-specific quality metrics;
- human/expert evaluation where metric validity is insufficient;
- generated-image truth-boundary tests.

**D. Systems efficiency**

- total checkpoint bytes;
- duplicated semantic parameters;
- peak resident memory;
- active parameters where meaningful;
- latency/throughput;
- energy/thermal evidence on named devices;
- quality per GB and quality per joule.

### 7.2 Safety remains noncompensable

High image quality or benchmark accuracy cannot compensate for a failed critical safety gate.

The existing deterministic safety/tool boundaries remain applicable. The single-checkpoint research target does not authorize neural replacement of authoritative calculations, drug interactions, schema validation, or hard escalation rules.

## 8. Required baselines

The paper should include, where rights and compute permit:

1. Qwen3.8-27B unmodified baseline;
2. medical-adapted Qwen3.8 language/multimodal baseline;
3. Kev-27B or reproducible equivalent decision baseline;
4. decider Qwen-family baseline at matched or normalized scale;
5. Qwen-Image-2.1 research baseline for generation/editing;
6. permissive Qwen-Image lineage baseline when relevant to release claims;
7. separately served language + decision + image models;
8. ordinary multi-head joint training without HCF;
9. adapter composition;
10. MergeKit best compatible merge from a frozen search budget;
11. OptMerge where applicable;
12. Expert Merging++ where applicable;
13. recent unified medical understanding/generation models for overlapping tasks, including MedUAG/UniMedVL/SynerMedGen when reproducible and comparable.

All comparisons must state differences in model size, training data, compute, image resolution, context, and evaluation protocol.

## 9. Ablation matrix

A publication-quality result requires at least the following ablations when technically applicable:

- shared Qwen backbone vs separate semantic encoders;
- original Qwen-Image encoder vs CommandMed shared-backbone bridge;
- frozen bridge vs trainable bridge;
- linear projector vs deeper adapter/cross-attention bridge;
- no decision head vs decision head;
- decision head only vs decision-adapter/task-vector transfer;
- LM-only medical SFT vs decision-only vs image-only vs joint;
- joint training vs staged training;
- merge-before-joint-stabilization vs merge-after-stabilization;
- TIES/DARE/DELLA/Arcee Fusion/other winner vs HCF;
- with/without representation alignment loss;
- with/without capability-preservation replay;
- English-only vs bilingual curriculum where scientifically useful;
- parameter-matched and storage-matched controls;
- post-merge calibration before/after temperature or other frozen calibration method;
- Qwen-Image-2.1 research lineage vs permissive image lineage if both are legally executable.

Negative ablations are publishable evidence and must not be hidden.

## 10. Data strategy

### 10.1 Data classes

Every example must be classified by role and rights before use:

- medical language/reasoning;
- multimodal medical understanding;
- typed decision supervision;
- evidence/citation verification;
- FHIR/tool actions;
- bilingual Arabic/English;
- image generation/editing;
- representation-alignment pairs;
- safety/adversarial cases;
- general-capability replay.

### 10.2 No synthetic-authority shortcut

Teacher-generated data may propose training examples but does not become truth through consensus. Use authoritative evidence, deterministic verification, human adjudication where required, or clearly labeled weak/synthetic supervision.

### 10.3 Contamination controls

Paper-facing evaluation sets must be separated from:

- training;
- prompt optimization;
- merge coefficient optimization;
- checkpoint selection;
- calibration fitting unless a designated calibration split exists;
- hyperparameter selection.

Repeatedly exposed tests become regression sets rather than fresh confirmatory evidence.

## 11. Compute strategy under the zero-cost founder constraint

The founder’s direct-cost constraint is preserved: do not introduce paid compute or paid APIs as a requirement.

The research plan therefore separates experiments into tiers:

### Tier A — CPU/local/static

- architecture inspection;
- source/license freeze;
- parameter mapping;
- merge feasibility analysis;
- tiny synthetic/unit fixtures;
- paper/literature work;
- deterministic evaluation tooling.

### Tier B — free research compute when genuinely available

- Google Colab free allocations;
- free academic/community compute grants;
- donated credits that impose no founder payment obligation;
- provider-sponsored research programs with acceptable terms.

### Tier C — high-compute experiments

27B full adaptation and image-generator training may exceed free opportunistic resources. Those stages remain blocked until no-cost capacity is actually available. Do not fabricate feasibility from a notebook that cannot run the experiment.

The paper may still progress through architecture, bridge pilots at smaller scales, ablations on smaller Qwen variants, and preregistered scaling laws before the full 27B confirmation.

## 12. Scale ladder

To reduce scientific and financial risk, validate the method before the flagship run.

Suggested ladder, subject to exact available Qwen releases and licenses:

```text
Stage S0: tiny/synthetic architecture fixtures
Stage S1: sub-2B/2B Qwen-family method prototype
Stage S2: ~4B decision + multimodal method study
Stage S3: mid-scale unified bridge study
Stage S4: Qwen3.8-27B flagship semantic backbone
Stage S5: full CommandMed One confirmatory experiment
```

A larger stage is not authorized merely because the smaller stage works. Each stage must define a falsification criterion and resource requirement.

## 13. Paper program

### 13.1 Working title

Primary working title:

> **CommandMed One: Heterogeneous Capability Fusion for Unified Clinical Reasoning, Calibrated Decisions, and Medical Image Generation**

Alternative title:

> **One Model, Three Computations: Unifying Autoregressive Reasoning, Typed Decisions, and Flow Generation for Medicine**

### 13.2 Prospective contributions

Only contributions validated by experiments should survive to the abstract. Candidate contributions are:

1. a single-checkpoint medical architecture sharing one semantic Qwen backbone across language, one-pass decision, and visual-generation paths;
2. HCF, a method for combining compatible weight-space merging with head transplantation and cross-architecture representation alignment;
3. replacement of a duplicate image-model semantic encoder with the shared medical backbone;
4. a comprehensive evaluation of capability interference/transfer across reasoning, calibrated decisions, and medical visual generation;
5. resource accounting showing whether semantic sharing improves capability per byte/memory/joule;
6. bilingual English/Arabic medical evaluation;
7. reproducible negative results and failure modes for heterogeneous model fusion.

### 13.3 Publication-quality evidence requirements

Before submission, require:

- frozen hypotheses and primary metrics;
- exact revisions and data lineage;
- at least one strong conventional merge baseline;
- at least one joint-training baseline;
- parameter/storage-matched controls;
- multiple seeds where training stochasticity materially affects claims;
- confidence intervals or appropriate uncertainty estimates for primary comparisons;
- explicit test-set access discipline;
- ablations that isolate the causal source of gains;
- compute and carbon/resource reporting where feasible;
- license/redistribution statement;
- limitations and clinical-use boundary;
- reproducible code/configs sufficient to reconstruct reported experiments when licenses allow.

### 13.4 Venue strategy

Venue selection happens after results, not before. Candidate classes include:

- top general ML venues for a genuinely new heterogeneous fusion method;
- top multimodal/vision-language venues if the primary novelty is representation unification;
- medical AI / clinical informatics venues if the strongest contribution is medical evaluation and utility;
- arXiv as the public preprint after the evidence package is mature enough to defend.

Do not rush an arXiv upload merely to establish a timestamp if the core experiments are not reproducible.

## 14. Prospective paper figures

Plan experiments to support figures rather than creating figures after the fact.

**Figure 1 — Architecture**  
Shared Qwen backbone with language, decision, and visual-generation paths.

**Figure 2 — HCF method**  
Compatible expert deltas + decision-head transplantation + representation alignment + encoder replacement + stabilization.

**Figure 3 — Quality/resource Pareto frontier**  
CommandMed One vs separate specialists vs joint training vs merge baselines.

**Figure 4 — Cross-capability interference matrix**  
How each training/fusion stage changes language, decision, and visual-generation quality.

**Figure 5 — Encoder replacement result**  
Generation quality and parameter/memory effect as the Qwen-Image semantic encoder is replaced.

**Figure 6 — Calibration/risk coverage**  
Typed medical decision quality before and after fusion.

**Figure 7 — English/Arabic and medical safety slices**  
No hidden average-only story.

## 15. Failure conditions

The single-checkpoint hypothesis should be rejected or narrowed if evidence shows any of the following:

- image generation requires the original image-model semantic encoder with no acceptable replacement;
- decision capability materially damages medical reasoning after reasonable mitigation;
- joint stabilization destroys calibration;
- the unified checkpoint is larger/slower than separate specialists without a compensating capability benefit;
- HCF does not outperform simpler adapter/joint-training baselines;
- gains vanish under contamination-resistant evaluation;
- licensing prevents publication/reproduction of the key experiment;
- critical safety regressions cannot be corrected without abandoning the architecture;
- compute requirements make reproducible research infeasible under available no-cost resources.

A negative result can still support a valuable paper if the study is rigorous and explains why heterogeneous fusion fails.

## 16. Execution map

This v2 roadmap intentionally separates planning from authority. The existing canonical Spec 000–007 history remains valid as historical evidence. Prospective v2 work must be introduced through new bounded specs rather than silently rewriting old closed specs.

Proposed prospective program:

| ID | Program unit | Core question / exit evidence |
|---|---|---|
| V2-000 | Research Reset & Claim Charter | v2 thesis, one-checkpoint target, rights boundary, no-execution posture frozen |
| V2-001 | Literature & Novelty Freeze | systematic search, competitor matrix, first-claim ledger, target contribution narrowed |
| V2-002 | Unified Evaluation Charter | primary metrics, hard gates, statistical plan, holdouts, paper baselines frozen |
| V2-003 | Source & License Ledger | exact Qwen/Kev/decider/CLM/MergeKit/OptMerge/image donor revisions and rights classified |
| V2-004 | Architecture Feasibility | tensor/module maps; one-checkpoint contract; no model execution required for initial exit |
| V2-005 | Decision-Head Prototype | typed-decision path validated at small scale with calibration and regression gates |
| V2-006 | Compatible Qwen Expert Merge Study | MergeKit/OptMerge/Expert-Merging-compatible baselines under frozen search budget |
| V2-007 | Visual Bridge Prototype | shared-backbone-to-DiT conditioning bridge tested at feasible scale |
| V2-008 | Encoder Replacement Study | original image encoder vs shared-backbone replacement; parameter/quality trade-off |
| V2-009 | HCF Method v1 | staged heterogeneous fusion method frozen and falsifiable |
| V2-010 | Medical/Bilingual Adaptation | English/Arabic medical specialization under capability-preservation gates |
| V2-011 | Evidence/FHIR/Tool Integration | evidence-grounded and typed tool decisions without replacing deterministic authority |
| V2-012 | Joint Stabilization | LM + decision + visual objectives with interference matrix |
| V2-013 | Flagship Qwen3.8-27B Confirmation | full-scale run only when lawful no-cost capacity exists |
| V2-014 | Compression & Efficiency | quantization/compression with full re-gating, not inherited claims |
| V2-015 | Independent Paper Evaluation | locked confirmatory test, ablations, baselines, statistical analysis |
| V2-016 | Reproduction & Artifact Package | code/config/model-card/data statements/negative-result ledger |
| V2-017 | Paper & Release Review | arXiv/venue manuscript, claims check, license review, clinical-use limitations |

No row is execution authority merely because it appears here.

## 17. Immediate next bounded actions

The safe next actions after this planning PR are:

1. freeze the v2 research reset as a canonical planning decision;
2. run a fresh systematic literature/competitor search and create the paper claim ledger;
3. freeze exact source revisions and license terms;
4. create V2-002 evaluation/statistics protocol before any model optimization;
5. design the module/tensor compatibility map for Qwen3.8, Kev/decider-style heads, Qwen-Image, and merge baselines;
6. start only the smallest no-weight/static feasibility work authorized by a dedicated spec;
7. defer model execution/training until the corresponding authority and no-cost resources exist.

## 18. Research-source snapshot

The plan was informed by the following source classes and must be refreshed before experiment freeze:

- Qwen3.8 official repository/model card;
- Qwen-Image-2.1 official repository and license;
- Arcee AI MergeKit and supported merge methods;
- OptMerge / MLLMerging (ICLR 2026);
- Expert Merging / Expert Merging++ (ICLR 2026);
- Kev and Kev-27B;
- Mapika/decider;
- Contrastive-LM/CLM;
- Gax literature and baseline registry;
- MedUAG;
- UniMedVL;
- SynerMedGen;
- current medical evaluation, abstention, FHIR/agent, evidence-verification, and multimodal benchmarks already tracked by CommandMed/Gax/MESC.

External source URLs and a dated research summary should be maintained in the dedicated v2 paper/landscape document rather than treating this plan as a permanent literature database.

## 19. Governance statement

This reset changes the prospective research direction; it does not erase history.

- closed prior specs remain closed historical evidence;
- prior run IDs, SHAs, reviews, and measurements remain immutable records;
- v0.1 is marked superseded for prospective architecture/roadmap planning only;
- no previous empirical claim is retroactively reinterpreted as evidence for v2;
- no model winner has been proven by this planning decision;
- no training authority is created;
- no clinical deployment claim is created;
- no paid-compute authority is created.

The goal is ambitious: one medical foundation model that reasons, decides, understands images, and generates images. The scientific standard is equally ambitious: the model and the paper must survive falsification, strong baselines, rights review, contamination control, safety gating, and reproducibility review.