# COMMANDMED GRAND MASTER PLAN v0.1

**Date:** 2026-08-21
**Status:** FROZEN PLANNING BASELINE — IMPLEMENTATION REQUIRES BOUNDED SPEC AUTHORITY
**Training authority:** NONE

## 1. North Star

Build commandMed as a universal, multimodal Health & Medical Intelligence system whose quality is judged by **verified medical usefulness and safety per byte, joule, and second**.

The project aims to make frontier-class health intelligence practical on personal devices without pretending that small size excuses unsafe behavior or weak evidence.

Long-term product/research users:

- patients;
- caregivers;
- physicians;
- nurses;
- pharmacists;
- students;
- researchers.

English and Arabic are first-class research languages. Arabic quality is measured, not assumed.

## 2. What commandMed is not

commandMed is not:

- a MedQA leaderboard project;
- a thin fine-tune of a single medical checkpoint;
- a symptom checker that always says "go to the ER";
- a monolithic VLM that treats screenshots as sufficient clinical perception;
- a static medical-knowledge dump inside weights;
- a claim that a compact model can replace clinicians;
- a license-blind distillation project;
- a Colab-only fiction for compute-heavy stages.

## 3. Success hierarchy

### Level A — Scientific integrity

Must always hold:

- frozen evaluation before optimization;
- reproducible identities and manifests;
- license/provenance evidence;
- contamination controls;
- safety hard gates;
- honest claims.

### Level B — Medical capability

Measure:

- medical knowledge;
- clinical reasoning;
- evidence use;
- active information acquisition;
- longitudinal reasoning;
- patient communication;
- professional workflow utility;
- multimodal interpretation where authorized;
- tools/FHIR;
- uncertainty and abstention;
- safety and escalation.

### Level C — Resource frontier

Measure on named devices:

- package bytes;
- peak memory;
- TTFT;
- prefill/decode rate;
- sustained throughput;
- energy/battery;
- thermals;
- context/KV behavior;
- medical-quality regression after compression.

### Level D — Claims

Only after independent evidence may the project use terms such as:

- best under a stated resource class;
- SOTA on a named evaluation and protocol;
- record medical intelligence density;
- patient-facing utility.

Claims must be narrower than or equal to the evidence.

## 4. System architecture

### 4.1 Shared Health & Medical Intelligence Core

A compact core should learn stable capabilities:

- medical/biomedical reasoning;
- structured clinical problem representation;
- uncertainty and missing-information detection;
- evidence selection and use;
- tool routing;
- safe communication;
- role-conditioned detail;
- multilingual clinical language.

The core is not assumed to contain every current guideline, formulary update, interaction table, or measurement algorithm.

### 4.2 Evidence and tool plane

Mutable/authoritative truth should be externalized where practical:

- guidelines and policies;
- drug labels/formularies/interactions;
- medical literature;
- calculators and validated clinical scores;
- FHIR/schema validators;
- local institutional evidence packs.

The core consumes verified results and provenance.

### 4.3 Patient safety shield

Patient-facing operation uses defense in depth:

`natural language -> active history -> model reasoning -> deterministic/authoritative safety checks -> evidence/tools -> calibrated response/escalation`

Non-overridable safety mechanisms may force `ASK_MORE`, `ABSTAIN`, `ESCALATE`, or `EMERGENCY` when the frozen policy requires it.

The model must not own pediatric dosing, safety-critical arithmetic, interactions, or validated scoring rules when deterministic/authoritative mechanisms exist.

### 4.4 Multimodal senses

commandMed uses a common evidence contract rather than demanding one encoder for every modality.

**V1 research focus:**

- text;
- documents;
- laboratory reports;
- general photographs with conservative behavior.

**Specialist-module path:**

- raw ECG;
- wearables/PPG/time series;
- CT/MRI volumes;
- whole-slide pathology;
- specialist ophthalmology/dermatology when validation requires it;
- medical audio;
- real-time video.

External modules remain commandMed components if they output structured, identity-bound evidence to the shared core.

## 5. Behavioral architecture

### Training classes

Use three classes unless data demonstrates a need for finer specialization:

1. `PATIENT_CAREGIVER`
2. `CLINICAL_PROFESSIONAL`
3. `LEARNER_RESEARCHER`

### Evaluation slices

Keep role-specific metrics for:

- patient;
- caregiver;
- physician;
- nurse;
- pharmacist;
- student;
- researcher.

### Internal outcome states

At minimum:

`ANSWER | ASK_MORE | USE_TOOL | RETRIEVE_EVIDENCE | ABSTAIN | ESCALATE | EMERGENCY`

## 6. Model tournament

No backbone is preselected.

### Track U — compact unified multimodal

Primary research candidates at this planning snapshot:

- Qwen3.5-2B Base;
- Ministral 3 3B Base;
- Gemma 4 E2B Base, conditional on actual byte/RAM/device fit.

### Track M — efficiency-first/modular

Conditional-license research candidates:

- LFM2.5-1.2B Base;
- LFM2.5-2.6B Base;
- LFM2.5-VL-3B.

### Controls

- SmolLM3-3B Base;
- Phi-4-mini family.

### Reference-only default

- MedGemma family;
- frontier closed models;
- other restricted/gated medical models whose output lineage is not approved.

### Tournament axes

Every serious candidate must be compared under a frozen protocol across:

- core medical quality;
- patient conversational quality;
- uncertainty/abstention;
- Arabic/English;
- general-capability preservation potential;
- multimodal/document capability where applicable;
- fine-tuning tooling and stability;
- package bytes/peak RAM;
- measured local performance;
- license/lineage fit.

The tournament may choose different research winners for different tracks, but a final release family must justify why multiple cores are worth their maintenance cost.

## 7. Evaluation program

### External/public development references

The Evaluation Charter must independently bind exact current versions before execution. Candidate families include:

- MedHELM;
- HealthBench, Hard, Consensus and Professional;
- MedXpertQA text/multimodal;
- MedQA;
- MedMCQA;
- PubMedQA;
- medical abstention/uncertainty suites such as MedQAbstain and MedAbstain;
- relevant 2026 diagnostic/counterfactual/tool-use suites after verification.

No public suite is automatically a release gate merely because it exists.

### Private Gold

Use three protected families:

1. `COMMANDMED_CLINICAL_GOLD`
2. `COMMANDMED_ARABIC_GOLD`
3. `COMMANDMED_MULTIMODAL_GOLD`

These require controlled access, power analysis, clinician involvement appropriate to the task, and strict non-optimization quarantine.

### Device evidence

`COMMANDMED_DEVICE_EVIDENCE` records exact hardware/software/model build plus resource and medical-equivalence results. It is a performance evidence pack, not semantic training/evaluation data.

### Required evaluation dimensions

- knowledge;
- reasoning;
- evidence fidelity/citation entailment;
- missing-information detection;
- active history taking;
- safety;
- emergency sensitivity and benign-case over-triage;
- medication and calculation safety;
- abstention/selective risk;
- calibration;
- patient comprehension/actionability;
- professional utility;
- Arabic dialect/code-switch robustness;
- temporal/OOD robustness;
- adversarial document/prompt-injection robustness;
- longitudinal multi-turn drift;
- multimodal extraction/interpretation;
- resource efficiency.

## 8. Data and lineage program

Every ingestible asset must carry enough metadata to establish identity, rights, split, and contamination state.

No broad corpus source is presumed uniformly licensed.

Before ingestion, classify:

- permitted research use;
- commercial implications;
- redistribution rights;
- modification rights;
- privacy/PHI status;
- source reliability;
- benchmark overlap risk.

### Explicit defaults

- No PHI in V1 repository artifacts.
- Restricted datasets are not pulled merely because they are common in medical ML.
- HAI-DEF model outputs do not train commandMed by default.
- Frontier API outputs do not train commandMed by default.
- Custom-license base models remain conditional until the intended use is compatible.

## 9. Knowledge strategy

Do not assume medical continued pretraining is necessary.

Run a pre-registered ablation after the tournament and minimal SFT baseline:

**Null/cheaper strategy:** strong base + high-quality role SFT + evidence retrieval/tools + license-clean distillation.

**CPT strategy:** bounded Health & Medical continued pretraining with general/multilingual replay and explicit regression gates.

CPT becomes canonical only if it improves the selected primary medical metrics without unacceptable general, Arabic, instruction, safety, or efficiency regressions relative to the null.

CPT token budget and compute are experiment decisions, not roadmap promises.

## 10. Post-training strategy

### SFT

Create a high-quality curriculum around:

- medical fundamentals and factual accuracy;
- clinical problem representation;
- differential reasoning;
- active information acquisition;
- patient explanations;
- professional workflows;
- evidence use;
- uncertainty/abstention;
- tools and structured outputs;
- Arabic/English clinical language;
- adversarial/unsafe cases.

Prefer fewer verified examples over large noisy synthetic corpora.

### Distillation

Start with the minimum license-clean teacher arrangement.

Teacher outputs are never truth by authority. Gold labels, deterministic verifiers, authoritative evidence, or clinician adjudication remain the truth boundary.

Prioritize on-policy distillation as an experiment because it can target the student's actual failure distribution. Add teacher specialization/ensembles only when a measured gap warrants the complexity.

### Preference optimization

DPO is optional. Run it only if pre-registered analysis shows a meaningful preference/communication/alignment gap that SFT/calibration/RLVR do not solve.

### RLVR

Use reinforcement learning only where rewards are defensible, e.g.:

- medical arithmetic;
- units;
- structured extraction;
- FHIR/schema conformance;
- executable tool calls;
- retrieval/citation support;
- verified-answer tasks;
- other objectively checked behaviors.

Do not let an LLM judge define medical truth.

## 11. Uncertainty, abstention, and calibration

Confidence is not a cosmetic number.

Research must measure selective risk and behavior under missing/contradictory/OOD input. Calibration may need stratification by specialty/task/population/language rather than one global confidence scalar.

The model must learn that acquiring more information or abstaining can be correct behavior.

## 12. Patient intelligence program

Core patient capabilities:

- understand colloquial/incomplete symptom descriptions;
- normalize patient language into a clinical problem representation;
- ask a small number of high-value follow-up questions;
- recognize missing context;
- explain risk without false reassurance or unnecessary alarm;
- provide safe next-step navigation;
- surface red flags;
- use deterministic medication/calculation tools;
- preserve longitudinal context where the product storage design permits it;
- support caregiver scenarios.

### Human evaluation requirement

Patient-facing claims require actual human testing of comprehension, action selection, escalation behavior, and failure modes. Simulated-user success is development evidence only.

## 13. Arabic Health & Medical program

Arabic is not a translation pass.

Required evaluation strata include:

- Modern Standard Arabic;
- Saudi/Gulf colloquial language;
- English-Arabic code switching;
- transliterated/variant medication names;
- patient descriptions that do not use clinical terminology;
- risk communication and numeracy;
- professional terminology and documentation.

`COMMANDMED_ARABIC_GOLD` should be created with appropriately qualified Arabic-speaking clinical reviewers. English-Arabic performance gaps are reported rather than hidden.

## 14. Compression and deployment

Compression follows evidence, not marketing.

Candidate sequence may include:

`BF16/FP16 reference -> Q8 -> Q6/Q5 -> Q4 -> optional QAT/recovery -> Q3/Q2 research`

A lower-bit build cannot inherit a higher-precision medical result. Each meaningful compression level must re-run required safety/equivalence gates.

### Runtimes to evaluate, not precommit

Depending on the winning architecture:

- llama.cpp/GGUF;
- MLX;
- ExecuTorch;
- LiteRT;
- ONNX/vendor NPU routes.

Use the minimum runtime set that covers the named device matrix.

### Context

Do not assume advertised 128K/256K contexts are usable on-device. Measure KV-cache cost and test bounded local context plus structured longitudinal memory/retrieval.

## 15. Compute policy

### Free/low-cost Colab

Appropriate for:

- fixture evaluation development;
- small candidate probes after authorization;
- LoRA/QLoRA pilots that fit;
- notebook reproducibility examples.

### Colab Pro / single high-memory GPU

Potentially appropriate for:

- serious small-model SFT/LoRA;
- selected distillation/RL pilots;
- teacher/evaluation generation where legal and authorized.

### Rented multi-GPU

Expected for any serious:

- CPT;
- large-scale distillation;
- full multimodal adaptation;
- QAT;
- repeated RL rollouts beyond pilot scale.

A spec must include a compute budget before authorizing these stages. If the budget is absent, the stage is not authorized.

## 16. Spec-of-Specs execution map

Roadmap order is dependency-driven, not a calendar promise.

| ID | Spec | Depends on | Core exit |
|---|---|---|---|
| 000 | Program Charter | — | constitution/authority/roadmap frozen |
| 001 | Evaluation Charter | 000 | verified benchmark/metric/Gold/quarantine contract |
| 002 | Safety Gates | 001 | hard gates + escalation/tool truth boundaries |
| 003 | Data, License & Provenance | 001 | machine-verifiable lineage contract |
| 004 | Tournament Harness | 001–003 | fixture-only deterministic harness |
| 005 | Base Model Tournament | 004 + founder license/device decisions | backbone evidence; no training |
| 006 | Patient Safety Scaffold & Deterministic Tools | 002–005 | safe interaction/tool boundary baseline |
| 007 | SFT V1 | 003–006 | minimal multi-role adapted candidate |
| 008 | Knowledge Strategy Ablation | 007 | CPT vs no-CPT/distill+RAG decision |
| 009 | Distillation V1 | 008 | justified license-clean distillation result |
| 010 | RLVR V1 | 009 | verified-task RL result or NO-GO |
| 011 | Calibration & Abstention | 007–010 as applicable | selective-risk/safety gates |
| 012 | Quantization & Device | 011 | exact-device equivalence evidence |
| 013 | Arabic Deepening | 007 + Gold readiness | quantified/fixed Arabic gaps |
| 014 | Multimodal Documents & Labs | 004–006 | unified-vs-structured perception decision |
| 015 | Human Evaluation | 011–014 | patient/professional human evidence |
| 016 | Advanced Modality Adapters | release-specific | separately validated specialist modalities |
| 017 | Release Review & Paper | all claimed capabilities | independent evidence/claims package |

Only the active bounded spec is execution authority.

## 17. Kill criteria

A research branch/candidate/stage may be killed for:

- incompatible or unresolved license lineage;
- failure to fit named resource/device budget;
- safety hard-gate failure;
- unacceptable general/Arabic capability regression;
- lack of statistically meaningful benefit over simpler alternative;
- irreproducible evidence;
- benchmark contamination;
- compute cost disproportionate to measured gain;
- modality performance too weak to justify a user-facing claim.

Killing a hypothesis is a valid successful research outcome.

## 18. Founder decisions

The decision register owns unresolved owner-level tradeoffs. The most time-sensitive are:

- intended open-weight/commercial licensing posture;
- target device tier and therefore byte/RAM budget;
- clinician/human-evaluation budget;
- acceptable benign-case over-triage policy;
- release fallback if one user mode fails a hard gate;
- whether any donor-origin restrictions from related projects should apply here.

Specs should not block on a founder decision until the decision becomes necessary for the next irreversible action.

## 19. Research paper strategy

Strongest likely thesis:

> **The safety-capped Health & Medical capability frontier of compact open models under leakage-resistant evaluation and real-device constraints.**

Potential secondary contributions if validated:

- active patient information acquisition at compact scale;
- Arabic/Gulf clinical evaluation artifact;
- verifiable medical RL for tool/evidence behaviors;
- on-policy medical distillation;
- medical intelligence density/resource frontier;
- quantization-induced medical reliability analysis;
- structured hybrid multimodal evidence architecture.

The paper must remain publishable even if the smallest-model moonshot fails; negative/ablation results are part of the scientific contribution.

## 20. Immediate next action

Implement **Spec 001 — Evaluation Charter only** after Spec Kit/Antigravity bootstrap is reconciled with the canonical planning files.

Spec 001 must not download/run/train any model. Its job is to make later optimization judgeable.
