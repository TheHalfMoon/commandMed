# commandMed Medical Intelligence Density Strategy v0.1

**Date:** 2026-08-27
**Status:** ADDITIVE PLANNING STRATEGY — does not amend execution authority
**Parent baseline:** `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
**Current lifecycle:** Spec 007 `AUTHORIZED_TO_START` — bounded offline deterministic I001-I045 implementation only; this strategy itself grants no execution authority
**Training authority:** NONE
**Model selection authority:** FOUNDER + CHATGPT ONLY
**Current Core/Nano interpretation:** `docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1-EDITORIAL-AMENDMENT-2026-08-27.md` supersedes the approximate parameter-band interpretation in §4.1–§4.2 while preserving this original text as historical planning evidence.

> **Editorial notice (2026-08-27):** Read §4.1–§4.2 together with the amendment above. `CORE=CAPABILITY_SAFETY_PRODUCT_CONTRACT`; `MASS_REACH_CORE=CANDIDATE_SATISFYING_CURRENT_FROZEN_SPEC005_CORE_CONTRACT`; `NANO` is a future separately scoped derived/distilled/compressed tier. Parameter bands are research hypotheses, not Core/Nano definitions and not overrides of frozen Spec 005 resource gates.

## 1. Purpose

commandMed will compete on **verified medical intelligence density**, not on vague model-size marketing or a single exam benchmark.

The strategic target is:

> **The highest verified Health & Medical usefulness and safety density achievable by an openly releasable compact model family, measured under leakage-resistant evaluation and real-device constraints in English and Arabic.**

The north-star objective remains the Grand Master Plan:

> verified medical usefulness and safety per byte, joule, and second.

This additive strategy makes that objective operational by adding explicit record classes, resource-normalized metrics, data-efficiency rules, failure-conditioned learning, later-stage distillation/RL/compression hypotheses, and release evidence requirements.

Nothing in this document authorizes model access, tournament execution, training, restricted data access, device execution, credentials, or spend.

## 2. Non-negotiable scientific rule

A record is not a goal declaration. A record exists only after:

1. the comparison class is defined before measurement;
2. candidate artifacts are identity-bound;
3. evaluation versions and splits are frozen;
4. contamination and quarantine checks pass;
5. safety hard gates pass;
6. resource measurements use named hardware/software;
7. comparison baselines are genuinely comparable;
8. statistical uncertainty is reported where applicable;
9. the result is reproducible from released evidence or independently auditable evidence;
10. the public claim is narrower than or equal to what the evidence proves.

`#1`, `SOTA`, `best`, and `record` are prohibited claims until these conditions are met.

## 3. Strict small-model accounting

commandMed will not use active/effective parameter marketing as its sole size definition.

Every release/comparison must report at least:

- total parameter count;
- active parameters per token where architecture makes that meaningful;
- BF16/FP16 reference bytes;
- shipped artifact bytes for the tested build;
- tokenizer/config/adapter bytes required for operation;
- peak RAM/VRAM on the named device;
- KV-cache growth at the tested context;
- TTFT;
- prefill rate;
- decode rate;
- sustained throughput;
- energy per evaluated case where measurement is available;
- thermals or throttling state for sustained on-device runs.

A model belongs to a commandMed record class by **actual delivered resource footprint**, not branding.

## 4. Product/research family strategy

### 4.1 commandMed Core

> **Historical wording notice:** the approximate `2–4B` phrase below is superseded for current interpretation by `COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1-EDITORIAL-AMENDMENT-2026-08-27.md`. Core is defined by the capability/safety/product/resource contract, not a parameter-count band.

Primary research target: the strongest compact general Health & Medical core that can plausibly live in the roughly 2–4B-class frontier or an equivalently small delivered-resource class.

The exact backbone is not selected here.

Core must optimize simultaneously for:

- medical knowledge and reasoning;
- active information acquisition;
- evidence/tool routing;
- abstention/selective risk;
- patient communication;
- professional utility;
- English and Arabic;
- general capability preservation;
- real-device efficiency;
- safe quantization/compression headroom.

### 4.2 commandMed Nano

> **Historical wording notice:** the approximate `0.6–1.5B` phrase below is superseded for current interpretation by the same editorial amendment. Nano is a future separately scoped tier defined by an explicit resource contract and capability-retention target, not parameter count alone.

Nano is a later hypothesis, not part of Spec 007 SFT V1.

Target research class: approximately 0.6–1.5B-class or an equivalently small delivered-resource class.

Nano should be attempted only after Core has a proven capability surface worth preserving. Its likely path is evidence-backed distillation/compression rather than premature direct optimization of an ultra-small base.

### 4.3 Large models

Large open or closed models may serve as reference/teacher candidates only when lineage, license, data-use, provider, and execution rules allow it.

A larger teacher is never medical truth by authority and is never evidence that the compact student is safe.

## 5. commandMed Record Board

The project should pre-register and measure a multi-axis record board instead of optimizing one leaderboard number.

Candidate record classes:

1. **Verified Medical Quality — Small Resource Class**
2. **Medical Quality per Shipped GB**
3. **Medical Quality per Peak RAM/VRAM**
4. **Arabic + English Medical Quality — Same Resource Class**
5. **Selective Risk / Abstention — Small Medical Model Class**
6. **Medical Tool-Use Reliability — Small Model Class**
7. **Patient Communication Utility — Small Model Class**
8. **Open-Ended Clinical Utility per Parameter**
9. **Expert Medical Reasoning per Shipped GB**
10. **Energy per Medically Correct Qualified Case**
11. **Medical Correctness per Reasoning Token**
12. **Capability Retention after Q4 Compression**
13. **Real-Device Medical Pareto Frontier**

Each record class must have a versioned definition containing:

- inclusion/exclusion rules;
- total-parameter and resource accounting rules;
- required safety gate;
- required evaluation suites/slices;
- score aggregation policy;
- uncertainty treatment;
- tie-break policy;
- device/runtime protocol where applicable;
- contamination policy;
- disallowed claims.

No record-board metric may compensate for a safety hard-gate failure.

## 6. Evaluation strategy — beat real medicine, not only exams

Traditional medical QA remains useful but insufficient.

The evaluation portfolio should represent:

- factual medical knowledge;
- diagnostic/clinical reasoning;
- open-ended patient conversations;
- active follow-up questioning;
- missing-information detection;
- evidence fidelity;
- professional workflow utility;
- tool use;
- longitudinal multi-turn stability;
- abstention/selective risk;
- emergency/escalation behavior;
- Arabic strata;
- adversarial/prompt-injection robustness;
- resource efficiency.

External candidates may include, after exact version/license/purpose/contamination review:

- HealthBench families;
- MedHELM;
- MedXpertQA;
- MedQA / MedMCQA / PubMedQA as supporting rather than sole metrics;
- medical abstention suites;
- Arabic medical benchmarks;
- tool-use methodologies inspired by BFCL-style failure dimensions.

Primary references for planning research include:

- HealthBench: https://openai.com/index/healthbench/
- MedHELM: https://crfm.stanford.edu/helm/medhelm/latest/
- MedXpertQA: https://arxiv.org/abs/2501.18362
- BFCL: https://gorilla.cs.berkeley.edu/leaderboard

Presence in this list is not admission authority and is not a release-gate decision.

## 7. Abstention as a signature capability

Compact medical systems should win partly by knowing when **not** to answer.

The seven canonical commandMed states are a competitive architecture:

```text
ANSWER
ASK_MORE
USE_TOOL
RETRIEVE_EVIDENCE
ABSTAIN
ESCALATE
EMERGENCY
```

The record program should measure:

- risk at fixed coverage;
- coverage at fixed risk;
- unnecessary abstention;
- dangerous over-answering;
- correct information acquisition;
- escalation sensitivity;
- benign-case over-triage;
- calibration within language/specialty strata.

Recent abstention research is a planning signal, not canonical benchmark authority:

- MedQAbstain / medical abstention work: https://aclanthology.org/2026.acl-long.1365/

## 8. Medical tool intelligence

A compact model can outperform much larger standalone models as a **medical system** if it reliably delegates authoritative operations.

commandMed should measure whether the model:

- selects the right deterministic tool;
- refuses nonexistent tools;
- emits schema-valid arguments;
- supplies required arguments;
- handles unavailable tools;
- continues correctly after tool results;
- rejects spoofed/untrusted results;
- handles conflicting authoritative results through deterministic precedence;
- does not replace safety-critical arithmetic, interactions, validated scores, or schema validation with prose.

Tool-use success is judged together with Spec 006 safety composition.

## 9. Maximum information per gradient

Training-set size is not a success metric.

The SFT data objective is:

> **maximum verified capability gain per admitted gradient-bearing token.**

Every admitted curriculum record should justify capacity consumption through coverage or measured failure repair.

Minimum planning dimensions include:

- role class;
- specialty/domain;
- reasoning type;
- risk/severity;
- missing-information pattern;
- evidence/tool requirement;
- uncertainty state;
- language/register;
- communication difficulty;
- durable-vs-mutable knowledge disposition;
- provenance/license/verification state;
- exact/near-duplicate burden;
- rendered supervised-token contribution.

Research such as LESS is a signal that selective data can outperform indiscriminate volume, but no particular selection algorithm is mandatory:

- LESS: https://arxiv.org/abs/2402.04333

## 10. Failure-conditioned curriculum loop

After execution is separately authorized, development should prefer capability-directed repair over blind dataset growth:

```text
QUALIFIED DEVELOPMENT FAILURE
-> FAILURE TAXONOMY CLASSIFICATION
-> ROOT-CAUSE CATEGORY
-> LICENSE-CLEAN / VERIFIED REPAIR EXAMPLES
-> TRAINING-DATA ADMISSION CHECKS
-> NEW VERSIONED DATA SNAPSHOT
-> NEW AUTHORIZED EXPERIMENT
```

Quarantined final/Gold/release evidence never becomes the optimization oracle.

A failure can lead to:

- new training example(s);
- retrieval/tool improvement;
- deterministic safety rule;
- evaluation clarification;
- no action if evidence is insufficient.

Not every failure belongs in the weights.

## 11. Knowledge placement

Before admitting content to weights, classify it:

```text
DURABLE_WEIGHT_ELIGIBLE
MUTABLE_RUNTIME_EVIDENCE_PREFERRED
DETERMINISTIC_TOOL_REQUIRED
REJECTED
```

Current guidelines, formularies, drug interactions, jurisdiction-specific pathways, local service routing, and rapidly changing evidence default away from durable weights unless a later experiment proves a reason to encode them.

This protects freshness while conserving compact-model capacity for durable reasoning and behavior.

## 12. Spec 007 — SFT V1 objective

Spec 007 should create the first **Core** candidate, not Nano and not the final product.

Its scientific purpose is to answer:

> How much role adaptation, medical reasoning behavior, evidence/tool behavior, abstention behavior, English/Arabic clinical communication, and safety preservation can be obtained from the selected compact base with the smallest verified SFT curriculum and the least irreversible complexity?

SFT V1 must remain backend-neutral until the winner and environment are known.

No pre-training pilot is implied by planning.

## 13. Spec 008 — Knowledge + Data Strategy Ablation

Spec 008 should test whether continued medical pretraining is actually needed.

Minimum comparison hypothesis:

```text
STRONG BASE + VERIFIED SFT + TOOLS/RETRIEVAL
vs
BOUNDED MEDICAL CPT + GENERAL/MULTILINGUAL REPLAY + VERIFIED SFT + TOOLS/RETRIEVAL
```

Also evaluate whether data-selection/hardness policies produce better medical gain per training token.

CPT is accepted only if the gain survives general-capability, Arabic, safety, and efficiency regression gates.

## 14. Spec 009 — Failure-conditioned / on-policy distillation

Distillation should prioritize the student's actual failure distribution rather than generic teacher dumping.

Research hypothesis:

```text
STUDENT ATTEMPT
-> IDENTIFIED DEVELOPMENT FAILURE
-> AUTHORITATIVE LABEL / VERIFIER / EVIDENCE BOUNDARY
-> TEACHER CORRECTION OR EXPLANATION WHERE LEGALLY ALLOWED
-> VERIFIED STUDENT LEARNING RECORD
```

Teacher output remains advisory unless independently verified.

The spec should compare on-policy/failure-conditioned distillation with a simpler offline baseline and kill the extra complexity if it does not produce statistically meaningful gains.

## 15. Spec 010 — Verifiable RL and reasoning efficiency

RL is allowed only where the reward can be defended.

Candidate task classes:

- medical arithmetic;
- units;
- structured extraction;
- FHIR/schema conformance;
- executable tool calls;
- evidence/citation support;
- exact-answer verified tasks;
- answerability/abstention where a defensible label exists.

Add explicit efficiency research:

- correctness per reasoning token;
- unnecessary reasoning-token rate;
- latency/energy impact of reasoning;
- accuracy under bounded reasoning budgets.

Longer reasoning is not automatically better reasoning.

## 16. Spec 011 — Calibration and selective risk

Calibration is stratified, not cosmetic.

Evaluate by:

- role;
- specialty/task;
- language;
- severity;
- in-domain vs OOD;
- evidence availability;
- tool availability.

Release claims should include selective-risk curves, not only a global confidence score.

## 17. Spec 012 — compression as a medical experiment

Compression cannot inherit BF16 medical claims.

Candidate ladder:

```text
BF16/FP16 REFERENCE
-> Q8
-> Q6/Q5
-> Q4 PTQ
-> Q4 QUANTIZATION-AWARE DISTILLATION (QAD) EXPERIMENT
-> QAT / RECOVERY IF JUSTIFIED
-> Q3/Q2 RESEARCH ONLY
```

Every meaningful artifact requires medical/safety/resource requalification.

QAD is an experiment, not a guaranteed method. Planning reference:

- Liquid QAD research: https://www.liquid.ai/blog/qad

## 18. Spec 013 — Arabic as a moat

Arabic is an independent capability frontier.

Required strata should include:

- MSA;
- Saudi/Gulf colloquial patient language;
- English-Arabic code switching;
- transliterated medication and medical terms;
- risk communication;
- numeracy;
- professional terminology/documentation.

The tournament decision packet should eventually measure tokenizer efficiency on matched medical samples:

- tokens/word;
- characters/token;
- medication-name fragmentation;
- clinical-term fragmentation;
- code-switch fragmentation.

Arabic parity is never assumed from multilingual marketing.

## 19. Core → Nano research gate

Nano is not started because Core exists.

A Nano program requires:

1. a qualified Core capability baseline;
2. explicit Nano resource class;
3. a pre-registered capability-retention target;
4. legal teacher/student lineage;
5. distillation/compression authority;
6. safety requalification;
7. evidence that Nano adds a materially useful device tier.

If Nano cannot retain a useful medical/safety surface, killing Nano is a successful research result.

## 20. Hugging Face release strategy

A competitive release is an evidence ecosystem, not a weights upload.

Potential release surface after authorization and qualification:

```text
commandMed-Core
commandMed-Core-GGUF
commandMed-Core-MLX
commandMed-Nano
commandMed-Nano-GGUF
commandMed-Evals
commandMed-Data (only redistributable/licensed assets)
commandMed Space
commandMed Collection
commandMed paper / technical report
```

Release requirements should include:

- Safetensors where appropriate;
- exact model/tokenizer/config revisions;
- quantized variants separated and clearly identified;
- one-command inference examples;
- one-command evaluation where licenses permit;
- pinned reproducibility notebook(s);
- complete model card and limitations;
- dataset cards/provenance summaries;
- `.eval_results/` or current Hugging Face evaluation metadata integration where applicable;
- real-device evidence;
- no inflated or incomparable leaderboard claims.

Planning reference:

- Hugging Face model release checklist: https://huggingface.co/docs/hub/en/model-release-checklist

## 21. Efficiency scorecards

For each qualified artifact, generate a scorecard containing raw metrics plus resource-normalized views.

Do not collapse everything to one scalar for scientific decisions.

Required views should include:

```text
RAW_MEDICAL_QUALITY
HARD_SAFETY_DISPOSITION
SELECTIVE_RISK
ARABIC_QUALITY
TOOL_RELIABILITY
GENERAL_CAPABILITY_DELTA
SHIPPED_BYTES
TOTAL_PARAMETERS
PEAK_MEMORY
TTFT
DECODE_TOKENS_PER_SECOND
ENERGY_PER_CASE
AVERAGE_REASONING_TOKENS_PER_QUALIFIED_CASE
```

Derived comparisons may include quality/GB, quality/peak-RAM, and qualified-correctness/joule, but raw values remain visible.

## 22. Kill criteria for record chasing

Kill or narrow a record attempt if:

- it incentivizes evaluation leakage;
- it weakens a safety hard gate;
- the comparison class is not defensible;
- parameter/resource accounting is misleading;
- a gain disappears under uncertainty analysis;
- a gain requires disproportionate compute or complexity;
- it relies on inaccessible evidence;
- Arabic/general capability regresses beyond frozen margins;
- the claim cannot be reproduced or independently audited;
- the improvement is benchmark-specific with no broader medical utility evidence.

## 23. Research-to-roadmap handoff

This strategy changes **what later specs should test**, not their current authority.

| Spec | Strategy handoff |
|---|---|
| 007 | Core SFT, capability-density accounting, failure taxonomy hooks, training-grade reproducibility |
| 008 | CPT vs no-CPT plus data-efficiency ablations |
| 009 | failure-conditioned/on-policy distillation experiment |
| 010 | verifiable RL + reasoning-efficiency experiments |
| 011 | selective-risk and stratified calibration frontier |
| 012 | real-device Pareto frontier + QAD experiment |
| 013 | Arabic gap closure and tokenizer-efficiency evidence |
| 015 | human utility/communication validation |
| 017 | independent claims/record/HF/paper audit |

No downstream spec is authorized by this table.

## 24. Current authority boundary

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The purpose of this strategy is to make the future experiment stronger, not to skip the experiment.
