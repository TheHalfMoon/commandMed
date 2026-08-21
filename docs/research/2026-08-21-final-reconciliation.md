# Final Research Reconciliation — 2026-08-21

**Status:** FINAL PLANNING EVIDENCE RECONCILIATION

This document reconciles the commandMed primary research with the independent GLM-5.3 adversarial consultation received on 2026-08-21. It records what was accepted, corrected, rejected, or converted into a bounded experiment before the Grand Master Plan was frozen.

## Method

A consultant statement is not treated as truth merely because it is adversarial. Each load-bearing claim is classified as one of:

- `ACCEPT` — supported and adopted;
- `ACCEPT_WITH_REPAIR` — direction is useful but implementation/framing changed;
- `REJECT_FACTUAL` — contradicted by verified current evidence;
- `TEST_BEFORE_LOCK` — plausible hypothesis that must be decided empirically;
- `FOUNDER_DECISION` — evidence cannot decide the product/research-owner tradeoff.

## Reconciliation table

| Topic | GLM-5.3 position | Final disposition | CommandMed decision |
|---|---|---|---|
| Program verdict | GO_WITH_MAJOR_REPAIRS | ACCEPT | Proceed, but evaluation/safety/license/device foundations precede training. |
| MedHELM / abstention benchmarks | Could not verify; remove until verified | REJECT_FACTUAL | MedHELM, MedQAbstain and MedAbstain are verified current assets and remain tracked. |
| Gemma 4 E2B size | Active parameters hide total resident footprint | ACCEPT | Candidate qualification is by bytes/RAM/device behavior, not marketing parameter count. |
| MedGemma teacher use | HAI-DEF lineage risk | ACCEPT, strengthened | MedGemma defaults to reference/evaluation only. No MedGemma outputs may train commandMed without explicit lineage/license approval. |
| LFM license | Custom license creates commercial risk | ACCEPT | LFM remains conditional-license research candidate; no commercial lineage lock until terms/threshold fit the intended release. |
| Qwen3.5-2B vision | Conflicting reports; verify | REJECT_FACTUAL after verification | Official current model card identifies native image-text capability; still measure it empirically. |
| Patient triage | Do not trust 2–3B model alone | ACCEPT_WITH_REPAIR | Use active interviewing + generative reasoning behind a non-overridable deterministic/authoritative safety shield. Do not replace the whole interview with a rigid rules-only graph. |
| Six private Gold families | Too expensive/noisy | ACCEPT_WITH_REPAIR | Consolidate to three Gold families plus separate device evidence pack. |
| CPT | Conditional; compare against cheaper null | ACCEPT | CPT must beat a no-CPT/distillation+retrieval alternative under pre-registered evaluation before it becomes canonical. |
| Seven roles | Too fragmented for SFT | ACCEPT_WITH_REPAIR | Train three behavioral classes; evaluate professions/audiences separately. |
| Multi-teacher distillation | Too complex for V1 | ACCEPT_WITH_REPAIR | Start with the minimum license-clean teacher strategy; add teachers only for measured gaps. |
| On-policy distillation | High value | ACCEPT | Retain as a priority research technique after minimal SFT baseline. |
| DPO | Do not make mandatory | ACCEPT | DPO is conditional on a measured preference/alignment gap. |
| RL | Only verifiable domains | ACCEPT | RLVR/GRPO is limited to objectively checkable or clinician-adjudicated tasks with anti-reward-hacking tests. |
| LLM judge | Cannot define medical truth | ACCEPT | Judges may assist communication/format scoring only after meta-evaluation; never become sole truth authority. |
| Multimodal | Hybrid boundary preferred | ACCEPT_WITH_REPAIR | Hybrid is architectural default; unified vs modular document perception remains a falsification experiment. External specialist modules remain part of commandMed, not out-of-scope products. |
| CT/MRI/WSI/video | Keep out of compact core | ACCEPT | Treat as specialist modules producing structured evidence; never infer maturity from VLM input support. |
| ECG/wearables | External specialist modules | ACCEPT | Prefer raw-signal processing + verifier/encoder + shared reasoning contract. |
| Arabic | Do not promise parity without measurement | ACCEPT | Arabic is first-class scope, but parity is a measured target, never an assumed claim. |
| Compute | Colab cannot carry heavy CPT/QAT | ACCEPT | Colab/Unsloth for pilots; heavy stages require explicit rented-compute budgets or are not authorized. |
| Human evaluation | Required for patient claims | ACCEPT | Human comprehension/decision quality is a release gate for patient-facing claims. |
| Spec Kit | Reject monolithic plan | ACCEPT | Use spec-of-specs with dependency-ordered bounded specs. |
| Ponytail | Useful but dangerous if applied to assurance | ACCEPT | Minimal mechanism with explicit safety/provenance/privacy/reproducibility carve-outs. |

## Verified corrections to consultant uncertainty

### MedHELM exists

Stanford CRFM's current MedHELM evaluation describes 121 clinical tasks across 35 benchmarks, including public, gated, and private components. It remains useful as a broad external reference suite.

### MedQAbstain and MedAbstain exist

Both are current 2026 research lines explicitly studying medical uncertainty/abstention. They remain research/evaluation references. Their exact artifacts, licenses, versions, and intended use must still be recorded by the Evaluation Charter before execution.

### Qwen3.5-2B has native image-text capability

The current official Hugging Face model metadata identifies the 2B family as image-text-to-text. This resolves the consultant's discovery conflict but does not establish medical visual quality.

## Licensing conclusions

### HAI-DEF / MedGemma

The relevant terms define model derivatives broadly enough to include models created through distillation or synthetic outputs used to train another model. Therefore a MedGemma teacher run is not a harmless detached experiment: it can affect the downstream model's legal lineage.

**Default rule:** MedGemma is reference/evaluation-only. Training on its outputs is prohibited until an explicit license/lineage decision records why it is allowed and what obligations follow.

### LFM Open License v1.0

LFM-family candidates are scientifically valuable, particularly for efficient local inference and published on-policy post-training design. Their custom license includes commercial-use conditions tied to revenue thresholds, so they cannot be treated as equivalent to Apache-2.0 candidates.

**Default rule:** LFM is a conditional-license research track. Commercial lineage remains open.

### Frontier model APIs

No frontier provider is assumed to permit competitive model training from its outputs. Evaluation/reference use and training-data generation are separate rights questions.

**Default rule:** no third-party API output becomes commandMed training data without a recorded permission analysis.

## Candidate set after reconciliation

### Primary permissive candidates

- Qwen3.5-2B Base — native image/text; Apache-2.0; must pass Arabic, medical, device, and fine-tuning tests.
- Ministral 3 3B Base — image/text; Apache-2.0; must pass Arabic and multi-turn instruction robustness tests.
- Gemma 4 E2B Base — multimodal and Apache-2.0; qualifies only if actual package/peak-RAM/device budget is acceptable despite total resident parameters.

### Conditional-license research candidates

- LFM2.5-1.2B Base — extreme-small efficiency hypothesis.
- LFM2.5-2.6B Base — text/reasoning efficiency hypothesis.
- LFM2.5-VL-3B — unified edge vision-language comparison.

### Scientific controls

- SmolLM3-3B Base.
- Phi-4-mini family.

### Reference-only by default

- MedGemma 1.5 4B and larger MedGemma-family references.
- Frontier closed models.
- Medical speech/perception models with incompatible or unresolved downstream terms.

The tournament may add/remove candidates only through a recorded evidence update before the candidate set is frozen.

## Architecture decision

**LOCK NOW:** commandMed is a hybrid multimodal medical-intelligence system with a compact shared reasoning core and a common evidence contract. A modality may be integrated or external according to empirical safety/resource evidence.

**TEST BEFORE LOCK:** for documents/labs/general photos, compare end-to-end unified perception against a structured pipeline (OCR/perception -> typed extraction -> deterministic validation -> reasoning) under the same quality and device budgets.

**EXTERNAL SPECIALIST BY DEFAULT:** raw ECG, wearables, CT/MRI volumes, whole-slide pathology, and later real-time audio/video. Their structured findings can feed commandMed; the specialist remains independently validated.

## Gold consolidation

Use three protected Gold families:

1. `COMMANDMED_CLINICAL_GOLD` — patient, caregiver, professional and critical-safety strata.
2. `COMMANDMED_ARABIC_GOLD` — MSA, Saudi/Gulf dialects, code-switching, transliterated medicines, risk/numeracy and health literacy.
3. `COMMANDMED_MULTIMODAL_GOLD` — documents/labs/photos first; later modality strata only after a bounded modality spec authorizes them.

Device benchmarking uses `COMMANDMED_DEVICE_EVIDENCE`, an exact-device performance/equivalence evidence pack rather than a fourth semantic Gold set.

Each Gold family requires a power-analysis plan and controlled access before its results can authorize a claim.

## Training strategy after reconciliation

The research ladder is conditional rather than a 16-step ritual:

1. Freeze evaluation, safety, provenance, and licensing contracts.
2. Tournament candidate baselines.
3. Establish minimal multi-role SFT baseline.
4. Run knowledge-strategy ablation: no-CPT/distillation+retrieval vs bounded CPT.
5. Keep CPT only if pre-registered evidence justifies it without unacceptable general/Arabic regression.
6. Apply minimal license-clean distillation; prioritize on-policy distillation if it beats simpler alternatives.
7. Use DPO only for measured preference gaps.
8. Use RLVR only where reward correctness is defensible.
9. Calibrate/abstain.
10. Compress and re-gate medically at every meaningful quantization step.
11. Evaluate on named real devices.
12. Use protected Gold and independent/human evaluation for release claims.

## Research thesis after reconciliation

The strongest defensible contribution is not "we fine-tuned the smallest medical chatbot."

It is:

> **Measure and push the safety-capped Health & Medical capability frontier of compact open models under leakage-resistant evaluation, human-role diversity, multilingual requirements, multimodal evidence, and real-device constraints.**

A second strong contribution, if evidence supports it, is active patient information acquisition with calibrated escalation at compact-model scale.

## Sources to re-verify in the Evaluation Charter

This reconciliation is a planning snapshot. Before executable evaluation, the registry must bind exact versions/artifacts/terms for every external suite/model. Primary source families include:

- Stanford CRFM MedHELM;
- OpenAI HealthBench family;
- MedXpertQA;
- ACL/EACL 2026 medical abstention work;
- Google Gemma / HAI-DEF / MedGemma documentation;
- Hugging Face model cards for candidate open models;
- Liquid AI LFM model cards/license;
- GitHub Spec Kit Antigravity integration documentation.

No URL in a planning document substitutes for a frozen, hashed evaluation/data manifest.
