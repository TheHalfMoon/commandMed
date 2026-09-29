# CommandMed v2 Paper and Novelty Program

**Snapshot date:** 2026-09-29  
**Status:** PROSPECTIVE RESEARCH DESIGN — CLAIMS NOT YET PROVEN  
**Execution authority:** NONE  

## 1. Why the paper needs a new thesis

A paper whose main claim is only “one medical model can understand and generate medical images” is no longer sufficiently differentiated.

By late September 2026, the literature already contains multiple unified medical understanding/generation efforts, including MedUAG, UniMedVL, and SynerMedGen. General multimodal models also increasingly unify perception and generation.

CommandMed therefore needs a narrower and more technically demanding contribution:

> **Unify three computational paradigms — autoregressive medical reasoning, one-pass calibrated typed decisions, and flow/diffusion visual generation — around one shared medical semantic backbone and one checkpoint.**

The paper should be written around this hypothesis only if the experiments support it.

## 2. Working paper identity

### Primary working title

**CommandMed One: Heterogeneous Capability Fusion for Unified Clinical Reasoning, Calibrated Decisions, and Medical Image Generation**

### Alternative title

**One Model, Three Computations: Unifying Autoregressive Reasoning, Typed Decisions, and Flow Generation for Medicine**

### Working method name

**Heterogeneous Capability Fusion (HCF)**

HCF is only a useful paper contribution if it provides a reproducible method and measurable improvement over simpler baselines. If the final result is just ordinary adapter composition, the method name must be removed.

## 3. Prospective novelty claim

The strongest prospective claim is:

> CommandMed One studies whether heterogeneous capabilities normally implemented as separate foundation-model systems can be consolidated around a single Qwen-family medical semantic backbone. The method combines compatible weight-space expert fusion, typed-decision head transplantation, cross-architecture representation alignment, image-encoder replacement, and joint stabilization to produce a single-checkpoint model supporting medical language/multimodal reasoning, calibrated one-pass decisions, and visual generation.

The words `first`, `state of the art`, `best`, `clinical-grade`, `safe`, and `revolutionary` are prohibited in the final abstract until a dated claim ledger proves that the exact claim is defensible.

## 4. Research gaps to test

### Gap G1 — Heterogeneous model merging

Conventional merge methods generally exploit parameter correspondence among models with compatible architectures. CommandMed intentionally crosses a boundary between:

- causal/autoregressive language modeling;
- typed discriminative/probabilistic decision readout;
- diffusion/flow image generation.

The paper must show whether useful capability fusion is possible without pretending that incompatible tensors can simply be averaged.

### Gap G2 — Duplicate semantic encoders

Qwen-Image-2.1 uses a Qwen3-VL-8B text/condition encoder plus a 7B DiT and VAE. A single-checkpoint CommandMed should test whether the shared Qwen3.8 medical backbone can replace that duplicate semantic encoder.

The result must be measured in both directions:

- generation/editing quality retained or improved;
- parameters/storage/memory actually saved.

### Gap G3 — Native decision behavior inside a generative foundation model

Jev-like systems such as Kev and decider show that one-pass typed probability distributions can be produced from Qwen-family representations.

CommandMed should test whether this capability can live natively beside autoregressive generation without requiring a separately served decision foundation model.

### Gap G4 — Cross-capability interference

Joint capability does not imply successful unification. The paper must explicitly measure whether language adaptation damages calibration, decision training damages generation, image alignment damages reasoning, or bilingual specialization damages any other path.

### Gap G5 — Medical-specific evidence

A general merging result is not automatically a medical result. The paper must evaluate clinical reasoning, evidence use, safety, bilingual medical language, medical multimodal understanding, and medically relevant decision tasks.

## 5. Landscape snapshot

The following items are research references, not endorsements. Exact revisions/licenses must be frozen before experiments.

### Qwen3.8-27B

Source:

- https://github.com/QwenLM/Qwen3.8
- https://huggingface.co/Qwen/Qwen3.8-27B

Snapshot observations:

- released 2026-08-14;
- 27B dense model;
- native multimodal image-text understanding;
- Apache-2.0 model license reported by the upstream model repository;
- suitable as the high-capability shared semantic backbone candidate;
- it is a post-trained release, so controlled claims about the effect of HCF must account for unknown upstream post-training data.

### Qwen-Image-2.1

Source:

- https://github.com/QwenLM/Qwen-Image-2.1

Snapshot observations:

- released 2026-09-20;
- 7B, 32-layer single-stream DiT visual generator;
- Qwen3-VL-8B text/condition encoder;
- VAE with RGBA/transparency support;
- flow matching;
- unified text-to-image and image editing;
- Qwen Research License rather than Apache-2.0 at this snapshot.

Research implication: use as a frontier research donor only after exact terms are reviewed. Do not assume public redistribution/commercial rights for derivative weights.

### Kev

Source:

- https://github.com/jaredpalmer/kev

Snapshot observations:

- open Jev-like typed-decision research;
- Kev-27B uses Qwen3.8-27B plus a LoRA and pointer head;
- one document/state plus typed questions in, probability distributions out;
- no text decoding in the decision path;
- calibration and risk-coverage measurements are first-class.

Research implication: a closely related semantic backbone makes Kev-27B a particularly important architecture baseline for native decision-head integration.

### Mapika/decider

Source:

- https://github.com/Mapika/decider

Snapshot observations:

- Qwen3.5-family one-pass typed decisions;
- Choice, Score, and Noul-style interfaces;
- supervised training, probability metrics, calibration/selective evaluation;
- multiple model scales and a vision variant;
- useful open baseline for decision-head design, serving fidelity, and negative-result discipline.

### Contrastive-LM/CLM

Source:

- https://github.com/Contrastive-LM/CLM

Research implication:

- state/action disaggregation;
- contrastive candidate scoring;
- hard-negative training;
- cached action representations;
- alternative decision paradigm to pointer/option-logit readout.

### Arcee AI MergeKit

Source:

- https://github.com/arcee-ai/mergekit

Snapshot observations:

- open model-merging toolkit;
- supports task arithmetic, TIES, DARE, DELLA, Model Stock, Arcee Fusion, multiple interpolation methods, multi-stage merging, raw PyTorch model merging, tokenizer transplantation, and MoE-related workflows;
- designed to combine specialized capabilities while preserving single-model inference cost when architectures are compatible.

Research implication: required conventional merging baseline and implementation reference; not sufficient novelty by itself.

### OptMerge / MLLMerging

Source:

- https://github.com/WalkerWorldPeace/MLLMerging

Snapshot observation:

- ICLR 2026 work on unifying multimodal LLM capabilities/modalities via model merging;
- includes QwenVL merging workflows.

Research implication: important recent multimodal merge baseline and related work.

### Expert Merging / Expert Merging++

Source:

- https://github.com/Littleor/ExpertMerging
- ICLR 2026 proceedings

Snapshot observation:

- learns a small number of layer-wise merge coefficients from unlabeled calibration data;
- aligns hidden states/logits to experts;
- Expert Merging++ allocates coefficients using importance-guided layer chunking;
- evaluated on LLM and MLLM backbones including Qwen2-VL.

Research implication: strong training-light merging baseline.

### MedUAG

Source:

- https://arxiv.org/abs/2608.18937

Snapshot observation:

- unified medical understanding and generation;
- MedUAGCorpus reports more than six million instances across 14 imaging modalities;
- dedicated understanding/generation benchmark and end-to-end model.

Research implication: prevents CommandMed from claiming novelty merely for medical understanding+generation.

### UniMedVL

Source:

- https://arxiv.org/abs/2510.15710

Research implication: another major medical understanding/generation reference that must be included in the final related-work search and comparison where reproducible.

### SynerMedGen

Source:

- https://arxiv.org/abs/2605.08724

Snapshot observation:

- explicitly studies synergy between medical understanding and image generation;
- generation-aligned understanding tasks and staged training;
- therefore highly relevant to any CommandMed claim about positive transfer between understanding and generation.

## 6. Claims ledger

The final paper must maintain a machine-readable or tabular claim ledger with at least these fields:

| Claim ID | Proposed claim | Required evidence | Competing work checked | Status |
|---|---|---|---|---|
| C1 | one shared semantic backbone supports language + decisions + image generation | architecture + checkpoint inspection + ablations | unified multimodal and decision-model literature | UNPROVEN |
| C2 | shared backbone can replace Qwen-Image semantic encoder | quality/resource ablation | Qwen-Image derivatives, UAG models | UNPROVEN |
| C3 | HCF outperforms conventional merging | frozen baseline search budget + confirmatory tests | MergeKit, OptMerge, Expert Merging++ | UNPROVEN |
| C4 | HCF outperforms naive joint multitask training | matched data/compute baseline | multitask/unified models | UNPROVEN |
| C5 | fusion preserves/improves calibrated decisions | Brier/NLL/ECE/AURC + CIs | Kev, decider, Jev if measurable | UNPROVEN |
| C6 | single checkpoint improves efficiency | exact bytes/RAM/latency/energy | separate specialists | UNPROVEN |
| C7 | medical bilingual quality is preserved | English/Arabic frozen evaluation | medical multilingual baselines | UNPROVEN |
| C8 | method is first of its exact kind | systematic dated literature search | all close prior/concurrent work | UNPROVEN |

`UNPROVEN` must remain the default until evidence is attached.

## 7. Hypotheses

### H1 — Semantic encoder replacement

A learned bridge from the shared Qwen3.8 medical representation can replace the original Qwen-Image semantic encoder with no unacceptable degradation on a frozen generation/editing evaluation while materially reducing duplicated semantic parameters.

### H2 — Decision coexistence

A native decision head can achieve competitive typed-decision accuracy/calibration without materially degrading autoregressive medical reasoning or multimodal understanding.

### H3 — HCF vs simple composition

HCF yields a better multi-capability Pareto frontier than naive adapter composition, ordinary compatible weight merging, or simple joint multitask training at matched resource budgets.

### H4 — Medical transfer

Medical representation sharing creates measurable positive transfer on at least one preregistered cross-capability task, rather than only preventing regression.

### H5 — Efficiency

The unified model removes enough duplicate semantic capacity to improve capability-per-byte and/or capability-per-resident-memory over separately served equivalents.

These hypotheses may fail. Failure must be reported.

## 8. Experimental families

### E1 — Decision-head integration

Compare:

- unmodified Qwen;
- Qwen + restricted-logit baseline;
- Qwen + pointer head;
- Qwen + decision LoRA + pointer head;
- decider-style slot readout;
- CLM-style contrastive decision path where appropriate.

Metrics:

- accuracy;
- NLL;
- Brier;
- ECE/calibration curves;
- AURC/risk coverage;
- latency;
- memory;
- language/multimodal regression.

### E2 — Compatible semantic expert merging

Create matched medical specialization experts only after training authority exists, then compare:

- adapter stacking;
- linear/task arithmetic;
- TIES;
- DARE-TIES;
- DELLA;
- Model Stock;
- Arcee Fusion;
- OptMerge/Expert Merging where applicable;
- HCF-compatible merge stage.

The hyperparameter/merge search budget must be frozen to prevent unfair tuning.

### E3 — Image conditioning bridge

Compare:

- original Qwen-Image encoder;
- frozen shared-backbone + linear projector;
- shared-backbone + MLP projector;
- shared-backbone + cross-attention bridge;
- staged alignment then generation training;
- joint alignment/generation training.

Measure generation quality plus representation similarity and resource changes.

### E4 — Encoder removal

The crucial ablation:

```text
Original:
Qwen3-VL-8B -> image DiT -> VAE

Target:
CommandMed shared Qwen backbone -> bridge -> image DiT -> VAE
```

Report:

- exact parameter counts;
- exact checkpoint bytes;
- resident memory;
- latency;
- generation/editing quality;
- text rendering;
- reference-image fidelity;
- medically relevant image criteria;
- failure cases.

### E5 — Joint stabilization

Compare sequential and joint curricula:

- language -> decision -> image;
- image -> language -> decision;
- decision -> language -> image;
- separate specialists then fusion;
- joint multi-objective training;
- HCF staged fusion then joint stabilization.

Create a cross-capability interference matrix after each stage.

### E6 — Full medical/bilingual validation

Evaluate:

- medical reasoning;
- evidence/citation support;
- patient/professional communication;
- FHIR/tool action selection;
- typed medical decisions;
- medical multimodal understanding;
- image generation/editing;
- safety;
- English;
- Modern Standard Arabic;
- Saudi/Gulf colloquial Arabic;
- code switching.

## 9. Statistical plan

Before confirmatory evaluation:

- define primary endpoints;
- designate development, calibration, and confirmatory splits;
- freeze seed count;
- freeze model-selection rule;
- freeze baseline-search budget;
- predefine equivalence/noninferiority margins where appropriate;
- use paired tests when examples are shared;
- report confidence intervals for primary deltas;
- correct or clearly scope multiple comparisons;
- report effect sizes, not only p-values;
- preserve per-task and safety-stratum results instead of hiding them in one macro average.

Repeated test access converts a set into a development/regression set.

## 10. Paper table plan

### Table 1 — Main capability comparison

Rows:

- base Qwen3.8;
- medical Qwen3.8;
- separate specialist system;
- naive joint model;
- best conventional merge;
- HCF / CommandMed One.

Columns:

- medical reasoning;
- multimodal understanding;
- decision accuracy;
- decision Brier/AURC;
- visual generation;
- Arabic;
- safety gate summary;
- total bytes;
- peak memory.

### Table 2 — Decision ablations

Head design, training method, calibration, latency.

### Table 3 — Image encoder replacement

Original encoder vs shared backbone bridges.

### Table 4 — Merge method comparison

MergeKit families, OptMerge, Expert Merging++, HCF.

### Table 5 — Cross-capability interference

Delta after each training/fusion stage.

### Table 6 — Efficiency

Checkpoint bytes, resident memory, active parameters, latency, energy where available.

### Table 7 — Medical safety and bilingual slices

No aggregate-only conclusion.

## 11. Figure plan

### Figure A — One checkpoint, three computations

Show the shared backbone and three output paths.

### Figure B — HCF algorithm

Show:

1. compatible Qwen expert/task-vector merge;
2. decision head transplantation;
3. hidden-state alignment;
4. image encoder replacement;
5. joint stabilization.

### Figure C — Pareto frontier

Medical capability vs bytes/RAM/latency.

### Figure D — Cross-capability interference heatmap

Training stage on rows, evaluated capability on columns.

### Figure E — Calibration/risk coverage

Decision quality before and after fusion.

### Figure F — Encoder replacement curve

Image quality vs percentage of original image semantic encoder retained/removed, if a staged removal study is technically meaningful.

## 12. Reproducibility package

The paper artifact should include, subject to upstream rights:

- exact git SHA;
- environment lock;
- model/dataset revision manifest;
- license/provenance ledger;
- merge configs;
- bridge configs;
- training configs;
- evaluation configs;
- seeds;
- raw metric outputs;
- statistical-analysis scripts;
- claim ledger;
- negative-result ledger;
- model card;
- data statement;
- compute/resource statement;
- known-limitations document;
- clinical-use boundary.

When weights cannot be redistributed, publish enough code/configuration and lawful metadata to reproduce the method with independently obtained upstream assets.

## 13. Review strategy

Before paper freeze, conduct separate reviews for:

- method correctness;
- statistical design;
- medical evaluation validity;
- data contamination;
- licensing/provenance;
- safety claims;
- reproducibility;
- paper novelty/related work.

Repository review tooling may include Jev where applicable and Alibaba Open Code Review for code review under the founder’s standing workflow, but automated review never substitutes for qualified clinical/statistical or rights review.

## 14. Publication strategy

### Stage P0 — internal pre-registration

Freeze hypotheses, metrics, baseline search budget, and failure criteria before confirmatory experiments.

### Stage P1 — method note

Write architecture/method sections early but mark all results placeholders as `TBD/UNPROVEN`.

### Stage P2 — development experiments

Use development/regression sets. Do not repeatedly inspect confirmatory tests.

### Stage P3 — confirmatory run

Run the frozen configuration once per predeclared seed/evaluation protocol.

### Stage P4 — independent claim audit

Verify that every abstract/conclusion sentence maps to evidence.

### Stage P5 — arXiv preprint

Upload only when the central method and main tables are reproducible and defensible.

### Stage P6 — venue submission

Choose venue based on what the evidence actually contributes:

- general ML if HCF is a broadly useful fusion method;
- multimodal/vision-language if cross-architecture representation unification is the central advance;
- medical AI/clinical informatics if the strongest advance is medical modeling/evaluation.

## 15. What would make the paper genuinely strong

The highest-value outcome is not the largest benchmark number. It is a causal story supported by ablations:

1. a shared semantic backbone removes a redundant encoder;
2. the model retains strong medical language and multimodal understanding;
3. typed decisions remain well calibrated;
4. image generation remains competitive;
5. HCF beats simpler merging/composition baselines;
6. the unified checkpoint achieves a better quality/resource frontier;
7. failures and limitations are transparently documented.

If these seven points are demonstrated under contamination-resistant evaluation, the work is potentially much stronger than a conventional medical fine-tuning paper.

## 16. Immediate research backlog

Before any training:

1. freeze exact upstream revisions and licenses;
2. inspect Qwen3.8 and Qwen-Image hidden-state/interface shapes;
3. map which Kev/decider components are architecture-compatible versus conceptual-only;
4. define the minimum decision-head API;
5. define the shared-backbone-to-DiT bridge interface;
6. build a static parameter-duplication accounting model;
7. define the paper’s primary endpoints and baseline budget;
8. create a systematic literature-search protocol;
9. create the machine-readable claim ledger;
10. create a small-scale method ladder before any flagship 27B experiment.

This backlog is planning only. It does not override the active bounded spec or create model execution authority.