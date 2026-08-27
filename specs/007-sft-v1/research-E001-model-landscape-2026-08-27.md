# E001 Model Landscape Research — Fresh Candidate Manifest Evidence Packet

**Date:** 2026-08-27
**Spec:** 007 SFT V1 — E001
**Lifecycle authority:** `AUTHORIZED_TO_START` (offline deterministic I001-I045 complete; E-phase separately gated)
**Model selection authority:** `FOUNDER+CHATGPT_ONLY` — `PI_MODEL_SELECTION_AUTHORITY=NONE`, `BACKBONE_WINNER=NEEDS_EVIDENCE`
**Training authority:** `NONE` — no model execution, weight access, benchmark execution, training, or spend is authorized by this packet
**Purpose:** Provide a fresh, evidence-backed model-landscape investigation so Founder + ChatGPT can freeze the tournament candidate manifest (`E001`). This packet is **evidence only** — `PI_RECOMMENDATION=NONE`.

> All repository-facing technical content in this packet is in English per repository policy. Founder-facing summary is delivered separately.

---

## 1. Research method

Primary authoritative sources were consulted where possible on 2026-08-27 (UTC). No model was downloaded, loaded, executed, or benchmarked by Pi. No candidate is selected or ranked by Pi.

Sources consulted:

- Hugging Face model cards and repositories: `Qwen/Qwen2.5-3B`, `Qwen/Qwen2.5-3B-Instruct`, `Qwen/Qwen3-...`, `google/gemma-3-4b-it`, `HuggingFaceTB/SmolLM3-3B`, `microsoft/Phi-4-mini-instruct`, `mistralai/Ministral-3-3B-Instruct-2512`, `mistralai/Mistral-Small-3.1-24B`, `LiquidAI/LFM2.5-1.2B`, `LiquidAI/LFM2.5-2.6B`.
- Official technical reports and blogs: Qwen3 technical report arXiv 2505.09388, Qwen2.5 technical report arXiv 2412.15115, Gemma 2 report arXiv 2408.00118, Ministral 3 report arXiv 2601.08584, SmolLM3 blog `huggingface.co/blog/smollm3`, Phi-4-Mini technical report arXiv 2503.01743, Liquid AI LFM license docs `liquid.ai/lfm-license`, QAD blog `liquid.ai/blog/qad` (2026-08-19).
- Official terms: `ai.google.dev/gemma/terms`, `ai.google.dev/gemma/prohibited_use_policy`, Vorp Labs license analysis (2026), Gemma GitHub `LICENSE` (Apache 2.0 for Gemma 4).
- Cross-lingual Arabic medical tokenization/evaluation papers: arXiv 2602.01714 (MedAraBench Arabic medical benchmark pipeline), ACL 2026 Healing 1.13 (cross-lingual Arabic medical LM evaluation), MedArabiQ PMLR 298 (Arabic medical benchmark), AraToken LEP paper arXiv 2512.18399.
- Third-party SLM surveys (2026-03-17 LocalAI Master, Bentoml blog 2026-03-09) used only as secondary aggregators; primary model-card/terms data is cited above.

No stale model assumption from the 2026-08-21 Grand Master Plan was reused without re-verification. All license readings are current as of 2026-08-27.

---

## 2. CommandMed constraints that filter candidates

From `AGENTS.md`, `constitution.md`, `decision-register.md` (FD-001, FD-002, FD-006), and Spec 007 `spec.md`/`clarification.md`/`plan.md`/`data-model.md`:

- **FD-001 OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE:** Preference for Apache-2.0-compatible lineage where legally supportable; permissive redistribution and commercial downstream use must be compatible. Custom/restrictive candidates are research-only/conditional until proven compatible.
- **FD-002 FLAGSHIP_PLUS_MODERN_MIDRANGE:** V1 tournament must cover flagship and modern midrange phones. Exact numeric thresholds are frozen later in Spec 005, but the resource class is ~2–4B-class (or equivalently small shipped bytes / peak RAM). Midrange fit is a hard filter.
- **FD-006 NOT_INVOKED:** No inherited donor-origin restriction beyond commandMed's own contracts.
- **AGENTS.md:** MedGemma/HAI-DEF are reference/evaluation-only; frontier API outputs are evaluation-only by default. Not candidates.
- **Spec 007:** Three frozen role classes (`PATIENT_CAREGIVER`, `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER`); Arabic is first-class (MSA, Saudi/Gulf colloquial, code-switch, transliteration); tokenizer efficiency is future model-selection evidence; quarantine firewall is complete; safety hard gates are non-compensable.

---

## 3. Candidate universe screened (2026-08-27)

Screened at the ~0.6B–4B-class (Nano hypothesis deferred to later spec; 14B+ noted only as controls/teachers):

| Candidate family | Checkpoint example (base) | Params | License (weight) | Status vs FD-001 |
|---|---|---|---|---|
| **Qwen3** dense | `Qwen/Qwen3-0.6B`, `Qwen/Qwen3-1.7B`, `Qwen/Qwen3-4B` | 0.6B, 1.7B, 4B | **Apache 2.0** (GitHub `QwenLM/Qwen3` LICENSE, HF repos flagged `apache-2.0`) | **Compatible** |
| **Qwen3.5** multimodal small | `Qwen/Qwen3.5-0.8B`, `Qwen/Qwen3.5-2B`, `Qwen/Qwen3.5-4B` | 0.8B–4B (+ vision encoder) | **Apache 2.0** (inherits Qwen3 licensing) | **Compatible** |
| **Qwen2.5** | `Qwen/Qwen2.5-3B` | 3.09B (2.77B non-embedding) | `Qwen Research` for 3B per table in report (0.5B/1.5B Apache, 7B+ Apache); 3B is **custom Qwen terms** — not Apache | **Conditional** |
| **Gemma 3** | `google/gemma-3-4b-it` etc (1B/4B/12B/27B) | 1B–27B | **Custom Gemma Terms of Use** (last modified 2026-04-01 per ToU page; Appendix lists Gemma 1 through 3n + specialized variants) — incorporates Prohibited Use Policy, flow-down, unilateral termination | **Not compatible as Core backbone** |
| **Gemma 4** | `google/gemma-4-e2b`, `google/gemma-4-e4b` (released 2026-04-02) | E2B ~2.3B eff (5B raw), E4B ~4.5B eff | **Apache 2.0** (official Apache text; ToU page expressly excludes Gemma 4; HF repos flagged `apache-2.0` ungated) | **Compatible** |
| **Ministral 3** | `mistralai/Ministral-3-3B-Base-2512`, `Ministral-3-8B` | 3.4B lang + 0.4B vision (3B), 8B, 14B | **Apache 2.0** (HF card `license: apache-2.0`) | **Compatible** |
| **Mistral Small 3(.1)** | `mistralai/Mistral-Small-3.1-24B-Base-2503` | 24B | **Apache 2.0** (announcement 2025-01-30) | **Compatible but out of V1 resource class** (control/teacher only) |
| **Phi-4-mini** | `microsoft/Phi-4-mini-instruct` (and base) | 3.8B | **MIT** (HF `license: mit`, OSI-approved, permits commercial use) | **Compatible** |
| **SmolLM3** | `HuggingFaceTB/SmolLM3-3B-Base` / `HuggingFaceTB/SmolLM3-3B` | 3B | **Apache 2.0** (HF `license: apache-2.0`) | **Compatible** |
| **LFM2.5** | `LiquidAI/LFM2.5-1.2B`, `LiquidAI/LFM2.5-2.6B` | 1.2B, 2.6B | **LFM Open License v1.0** (Apache-based + commercial-use threshold $10M revenue, Sec 5; derivatives inherit restriction) | **Not compatible as Core release lineage** under FD-001 (research-only/conditional) |
| **Llama 3.2 3B** | `meta-llama/Llama-3.2-3B` | 3.2B | Meta custom (not screened as Apache) — not listed as Apache candidate | **Not in permissive set** |

**Excluded from Core backbone shortlist:**

- **Gemma 3** (custom ToU, Prohibited Use Policy lists medical/health professional practice as restricted; derivative inherits; flow-down to Hosted Service; unilateral termination — high dependency risk for a health product).
- **LFM2.5** (revenue-gated commercial use — violates `OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE` for a product intended to scale beyond $10M).
- **Qwen2.5-3B base** (non-Apache Qwen terms for that size) — not recommended when Qwen3-1.7B/4B are Apache and newer.
- Models > ~4B effective (e.g., Mistral Small 24B) as Core — retained as possible teacher/reference only.

---

## 4. Deep candidate profiles

### 4.1 Qwen3 family (Apache 2.0)

- **Architecture:** Dense decoder-only Transformer; RoPE, SwiGLU, RMSNorm, QKV bias, GQA (report 2505.09388). Dense sizes 0.6B, 1.7B, 4B, 8B, 14B, 32B + MoE 30B-A3B (3B active) and 235B-A22B (22B active). Qwen3.5 adds vision encoder to 0.8B/2B/4B while preserving Apache.
- **Params (non-embedding):** Qwen2.5-3B reference 2.77B/3.09B total; Qwen3-4B similar class (exact count to be bound in tournament manifest with repository notation).
- **Context:** Qwen2.5-3B card lists 32,768 tokens full (8K generation). Qwen3 dense models list 32K for 0.6B–4B and 128K for 7B+ in the Qwen2.5 report table; Qwen3.5 reports 256K for the small multimodal variants; Qwen3 announcement cites 128K–1M with YaRN/LongRoPE extensions for MoE variants. Candidate manifest must freeze exact context per checkpoint.
- **Pretraining:** Qwen3 reports ~36T tokens over 119 languages/dialects (vs Qwen2.5 29 languages), including explicitly Arabic (MSA, Najdi, Levantine, Egyptian, Moroccan, Mesopotamian, Ta'izzi-Adeni, Tunisian) per Qwen3 blog language table.
- **Medical evidence:** No dedicated medical pretraining claim; general SOTA at size (Qwen3-4B dense matches Qwen2.5-72B-Instruct per blog — 18× compression). Qwen2.5 technical report shows Qwen2.5-3B competitive on math/coding at 3B. Medical capability is not proven; requires frozen evaluation (HealthBench/MedHELM etc.) under FR-005.
- **Reasoning:** Hybrid thinking/non-thinking mode unified framework with thinking-budget control (Qwen3 innovation). Strong on math/coding benchmarks (MATH 75.5 for 7B-Instruct, HumanEval 84.8). Small reasoning variant (`SmolLM3`-style think mode has analogue; Qwen3 has native thinking mode).
- **Arabic capability:** Strongest small-model Arabic among permissive candidates per SmolLM3 report: Arabic Belebele 51.78 for Qwen3 4B Base vs 40.22 SmolLM3 3B vs 44.22 Qwen2.5-3B vs 45.33 Llama 3.2 3B; Global MMLU CF Arabic 31.85 vs 28.57; Flores 200 comparable. 119-language pretraining with explicit Arabic dialects is a differentiator. Earlier MedArabiQ evaluation showed Qwen2.5-7B-Instruct strongest among open-access models on Arabic medical tasks — Qwen3 inherits/extends that line.
- **Tokenizer:** Qwen tokenizer — BBPE with 151,643–151,646 tokens + 22 control tokens unified across sizes (report 2412.15115). Byte-level; handles Arabic morphology but general-purpose. Arabic fragmentation (~2.4 tok/word for general tokenizers per ACL 2026 paper) applies; AraToken research shows 18% fertility improvement is possible with Arabic-optimized SentencePiece (1.199 vs 1.35 tok/word), but no Qwen3 Arabic tokenizer optimization is pre-assumed.
- **Licensing/provenance:** Apache 2.0 — permits fine-tune, commercial product, redistribution with NOTICE/attribution; no prohibited-use medical carve-out; no revenue threshold. Provenance: Alibaba Cloud Qwen Team; checkpoints on HF/Kaggle/ModelScope; synthetic data use disclosed (Phi comparison similar, but Qwen synthetic pipeline less disclosed — still Apache weight lineage is clean).
- **Training ecosystem:** Fully supported — `transformers>=4.51`, `trl` SFTTrainer, `peft` LoRA/QLoRA, `axolotl`, `unsloth`, `liger`, `vllm`, `sglang`, `llama.cpp`, `mlx`. TRL SFTTrainer chat-template mechanics explicitly support Qwen.
- **Quantization/runtime:** BF16/FP16, Q8–Q4 GGUF, MLX, LiteRT, ollama (`qwen3:4b`, `qwen3.5:4b`). Hardware: flagship + midrange friendly (~3GB VRAM Q4 for 3–4B). Attention kernel: Flash Attention / SDPA.
- **Reproducibility:** Standard PyTorch/transformers determinism; exact-environment replay vs cross-environment equivalence distinction per Spec 007 C-015 applies. No cross-stack bitwise guarantee.
- **Safety/contamination:** General-purpose web/code/science data (18T for Qwen2.5 3B class, 36T for Qwen3). Medical benchmark contamination status is `NEEDS_EVIDENCE` — must be checked before evaluation per FR-004.
- **Compatibility:** Fully compatible with Spec 007 contracts (rendering, loss mask, packing/truncation, checkpoint manifest, environment pin, resume). Base checkpoint binding can carry full tokenizer/template/weight identities under Apache.

### 4.2 Gemma 4 E2B / E4B (Apache 2.0) — released 2026-04-02

- **Architecture:** Edge-optimized dense models derived from Gemini research; E2B ~2.3B effective (~5B raw), E4B ~4.5B effective. E-series designed for on-device / low-resource deployment. Details per Bento/LMA survey: download 7.2GB (E2B) / 9.6GB (E4B) — larger bytes than param count suggests due to effective-vs-raw accounting per device dim.
- **Context:** To be frozen per checkpoint — survey cites Gemma 3 128K context; Gemma 4 inherits similar; manifest must verify.
- **Medical:** Not domain-specific. General multimodal (text + image + audio + video in → text out via Gemma 3n). Performance competitive but no medical frontier claim.
- **Reasoning:** Native function calling / structured outputs noted in survey (Gemma 4 E4B "native function calling") — relevant to tool-use reliability.
- **Arabic:** Gemma 3 card cites 140+ languages; Gemma 4 inherits. Gemma-3-4B tokenization study (ACL paper): Gemma-3-4B-it tok/word 2.30 Arabic vs 1.57 English — fragmented but multilingual-efficient (better than Llama 3.3 2.42). No dialect-specific claim.
- **Tokenizer:** To be bound — survey does not list Gemma 4 vocab, but Gemma family uses SentencePiece-like 256,128 vocab (Gemma 2 table) with GeGLU/GQA. Exact counts per checkpoint needed.
- **Licensing:** **Apache 2.0** — this is the only Google Gemma line currently Apache; ToU page expressly excludes Gemma 4 from custom terms; HF repos are ungated and flagged `apache-2.0` without Prohibited Use Policy. This is an independent reading, not legal advice.
- **Ecosystem/quantization:** `transformers`, `gemma.cpp`, `llama.cpp`, `ollama` (`gemma4:e2b`, `gemma4:e4b`), LiteRT, JAX. Quantization Q4–Q8 GGUF described (Bento survey). Device-friendly per design (phones/Raspberry Pi for E2B).
- **Compatibility:** Compatible; tokenizer/template/binding straightforward. Medical-intelligence-density accounting must use shipped bytes + peak RAM, not marketing param count (E-series effective-vs-raw is a known accounting trap — Spec 007 §3 strict accounting applies).

### 4.3 Gemma 3 4B (CUSTOM — excluded as Core backbone)

- **Architecture:** 4B text+vision (1B/4B/12B/27B family), 128K context (Gemma 3 announcement), GeGLU, GQA, sliding-window = 4096, vocab 256,128 (Gemma 2 table representative).
- **Context:** 128K (announcement).
- **Medical:** Not domain-specific.
- **Arabic:** 140+ languages claimed; tokenization measured 2.30 tok/word Arabic (paper) — plausible.
- **Tokenizer:** 256K SentencePiece family.
- **Licensing:** **Custom Gemma Terms of Use** — incorporates Prohibited Use Policy which restricts "health-related professional practices" (medical diagnosis) and other sensitive categories; defines Distribution to include Hosted Service (API counts as Distribution triggering flow-down); requires downstream users be bound to same restrictions; unilateral update/termination right (Sec 3–4). Derivative remains subject to same Terms (not Apache). **Incompatible with FD-001 for a health product intending permissive commercial downstream use.** Even if technically strong, lineage is rejected for canonical Core.
- **Ecosystem:** Strong (Hugging Face, Ollama, Gemma.cpp, etc.) — irrelevant given license block.
- **Contamination/safety:** Same general data caveats plus policy risk.

### 4.4 Ministral 3 3B (Apache 2.0)

- **Architecture:** Dense decoder with vision encoder (3.4B language + 0.4B vision ≈ 3.8B shipped); GQA; Cascade Distillation from Mistral Small 3.1 (24B parent) over 1–3T tokens (vs 36T/15T for Qwen3/Llama) — report 2601.08584.
- **Variants:** 3B, 8B, 14B each in Base / Instruct / Reasoning — 9 models total. Ministral 3 3B Instruct/Reasoning relevant; 3B base is tournament anchor.
- **Context:** 256K (128K for reasoning variant) — largest among 3B candidates.
- **Medical:** Not domain-specific; general reasoning via distillation lineage from Small 3.1.
- **Reasoning:** Reasoning variant exists natively (distilled reasoning track) — relevant to RLVR hypothesis later.
- **Arabic:** Supports Arabic among "dozens of languages" (card lists ar, en, fr, es, de, it, pt, nl, zh, ja, ko) — but Arabic is not among top-tier per-language claims; no Arabic medical benchmark leadership shown. European languages strongest per card.
- **Tokenizer:** Tekken tokenizer, 131K vocab (Mistral Small 3.1 spec). Fragmentation for Arabic unknown — needs measurement (tokenizer-efficiency evidence per C-010/011).
- **Licensing:** **Apache 2.0** — clean for FD-001.
- **Ecosystem:** `transformers>=4.53`, `vllm`, `trl`, `peft`; Ollama `ministral-3:3b`. Quantization GGUF Q4_K_M (~3.4GB BF16 7.8GB → ~3.4GB quantized). Edge-deployed (~8GB VRAM FP8).
- **Compatibility:** Compatible; vision+text multimodal fits Spec 007 V1 research focus (documents/photos via structured perception — but plan says V1 focuses on text/docs/photos with conservative safety; Ministral vision is bonus, not requirement).

### 4.5 Phi-4-mini 3.8B (MIT)

- **Architecture:** Dense decoder-only Transformer; 32 layers (?), 3.8B params, 200K vocab (`o200k` tiktoken base), GQA, shared embedding, LongRoPE for 128K context. Performance per HF card: 67.3% MMLU, 74.4% HumanEval for 3.8B (vs 63.4% Llama 3.2 3B, 59.6% Gemma 3 4B reference).
- **Context:** **128K** tokens (card).
- **Pretraining:** 5T tokens (Nov–Dec 2024, cutoff June 2024) — 512×A100-80G, 21 days. Synthetic + filtered web, reasoning-dense.
- **Medical:** Not domain-specific. Strong math/coding/reasoning at size (74.4% HumanEval > Gemma 3 4B 36%, Qwen2.5 stronger math claim but Phi-4-mini matches/beats 2× larger). No medical benchmark edge claimed; needs frozen evaluation.
- **Reasoning:** Competitive reasoning at 3.8B — matches DeepSeek-R1-Distill 7B/8B per 2503.01743 report (reasoning-enhanced experimental variant noted as preview not released — base instruct is the candidate).
- **Arabic:** Supported among 23–25 languages including Arabic (card lists Arabic explicitly). HF card multilingual list includes ar, he, etc. No dialect claim; tokenization Arabic behavior not deeply characterized. Empirical Llama comparison (SmolLM3 report) suggests moderate — but specific Arabic medical fragmentation not yet measured for Phi.
- **Tokenizer:** 200,064 tiktoken `o200k` base — large vocab benefits multilingual compression. No published Arabic tok/word for Phi-4-mini in ACL study — to be measured.
- **Licensing:** **MIT** — OSI-approved, permissive, allows commercial use/modification/distribution for any purpose (no revenue threshold, no prohibited-use medical carve-out beyond "evaluate for high-risk scenarios" guidance). Most permissive among candidates. Compatible with FD-001 without flow-down medical restriction.
- **Ecosystem:** `transformers`, `trl`, `peft`, `onnx`, `ollama` (`phi4-mini`), `llama.cpp` GGUF, `mlx`. Quantization Q4 ~3GB VRAM. TRL-compatible (report cites SFT/DPO enhancement process).
- **Safety:** Model card notes "not specifically designed or evaluated for all downstream purposes; high-risk scenarios require evaluation" — honest; fits Spec 007 hard-gate approach.
- **Compatibility:** Fully compatible; MIT removes redistribution friction.

### 4.6 SmolLM3 3B (Apache 2.0)

- **Architecture:** Dense decoder, GQA, **NoPE** (no RoPE) with YaRN for 128K context; trained on 11T tokens public data.
- **Context:** 128K (NoPE + YaRN).
- **Medical:** Not domain-specific. Strong at 3B SOTA claim — "SoTA at 3B scale, competitive with 4B (Qwen3 & Gemma3)" per HF blog. Benchmark table: English-heavy eval (MMLU, etc.) not medical. No medical edge.
- **Reasoning:** Dual `think`/`no_think` modes (similar to Qwen3 thinking). Instruct model supports reasoning toggle.
- **Arabic:** **Weakest Arabic among candidates.** Trained on Arabic (standard) + Chinese/Russian but "fewer tokens" than core 6 (en, fr, es, de, it, pt). Empirical: Belebele Arabic 40.22 (worst among 3B set: Qwen2.5-3B 44.22, Llama 3.2 3B 45.33, Qwen3-4B 51.78); Flores-200 Arabic 40.22. Core-6 languages are en, fr, es, de, it, pt — Arabic is explicitly secondary. For an Arabic first-class requirement (MSA + Saudi/Gulf colloquial + code-switch), this is a disqualifying signal unless later Arabic deepening (Spec 013) can rescue — but for V1 Core selection, risk is high.
- **Tokenizer:** Llama 3 tokenizer variant: 128K vocab (100K tiktoken3 + 28K non-English), characters/token improvement 3.17→3.94 en. No Arabic-specific optimization; fragmentation not better than Qwen/Phi.
- **Licensing:** **Apache 2.0** — compatible.
- **Ecosystem:** `transformers>=4.53`, `vllm`, `trl`, `llama.cpp`, `mlx`. Open weights + full recipe + intermediate checkpoints — strong reproducibility.
- **Compatibility:** Compatible technically, but Arabic gap makes it a weak fit for commandMed's bilingual thesis.

### 4.7 LFM2.5 1.2B / 2.6B (LFM Open License v1.0 — conditional/research-only)

- **Architecture:** Dense LFM2.5 family (conv-hybrid efficiency focus); 32K context (1.2B), 128K (2.6B). QAD checkpoint for edge (Q4_0 with 96–97% BF16 recovery per 2026-08-19 QAD blog).
- **Medical:** Not domain-specific; agentic/tool-calling focus (trained inside Hermes/Claw/ Pi harnesses).
- **Reasoning:** Tool/agent capable but not general medical reasoning leader.
- **Arabic:** Listed among 16 languages but no Arabic medical strength shown; no Arabic dialect claim.
- **Tokenizer:** Not characterized for Arabic in sources — assumed general.
- **Licensing:** **LFM Open License v1.0** — Apache-based + **Commercial Use Limitation Sec 5:** free commercial use only if `annual revenue < $10M`; above threshold, commercial use is **not licensed** and requires paid license from `sales@liquid.ai`. Applies to derivatives. Qualified non-profit research exempt. This fails `FD-001` permissive downstream use at scale — enterprise release would require separate negotiation. Incomplete for open-weights permissive product.
- **Ecosystem:** `transformers>=5.2`, `peft` TRL compatible (SFT/DPO/GRPO), but smaller community than Qwen/Phi.
- **Compatibility:** Technically compatible, legally **not selectable as canonical Core backbone** under current founder posture without separate commercial license. Remains as optional efficiency-first research reference only.

---

## 5. Comparative matrix (2026-08-27 evidence snapshot)

| Dimension | Qwen3 1.7B / 4B (Apache) | Gemma 4 E2B/E4B (Apache) | Ministral 3 3B (Apache) | Phi-4-mini 3.8B (MIT) | SmolLM3 3B (Apache) | LFM2.5 1.2B/2.6B (LFM v1) | Gemma 3 4B (Custom) |
|---|---|---|---|---|---|---|---|
| **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 | MIT | Apache 2.0 | LFM v1 (<$10M free) | Custom ToU + PUP |
| **FD-001 fit** | ✅ | ✅ | ✅ | ✅ (most permissive) | ✅ | ❌ (conditional) | ❌ (medical restricted) |
| **Params (shipped)** | ~1.7B / ~4B dense | ~2.3B eff / ~4.5B eff (5B/9B raw) | 3.4B +0.4B vision | 3.8B | 3B | 1.2B / 2.6B | 4B |
| **Context** | 32K (0.6-4B) / 128K+ (7B+) ; Qwen3.5 256K | To verify (≈128K) | **256K** (128K reasoning) | **128K** (LongRoPE) | 128K (NoPE+YaRN) | 32K / 128K | 128K |
| **Architecture** | Dense RoPE/SwiGLU/GQA/QKV bias | Edge dense (Gemini-derived) | Dense + vision, cascade distilled | Dense GQA 200K tiktoken | Dense NoPE GQA | Dense LFM hybrid | Dense GQA GeGLU |
| **Vision** | Qwen3.5 multimodal | ✅ (Gemma 3n multimodal) | ✅ (native) | ❌ (text only; multimodal is Phi-4-multimodal separate) | ❌ | ❌ | ✅ |
| **Pretrain tokens** | 36T (Qwen3) / ~? for Qwen3.5 | Not disclosed (Gemini tech) | 1–3T via cascade (teacher Small 3.1) | 5T (synthetic-heavy) | 11T public | Not disclosed | Not disclosed |
| **Arabic languages** | 119 inc. 7 Arabic dialects explicit | 140+ (unspecified dialects) | Dozens incl. Arabic | 23 inc. Arabic | 6 core + Arabic secondary (<tokens) | 16 inc. Arabic | 140+ |
| **Arabic medical evidence** | Strongest 3B-class: Belebele 51.78 (4B) | Unknown (not benchmarked Arabic med) | Unknown (no Arabic med bench) | Unknown (but supported) | Weak: Belebele 40.22 | Unknown | Tokenization 2.30 tok/wd (fragmented) |
| **Reasoning** | Hybrid think mode; strong MMLU/Math/HumanEval | Function calling; general SOTA | Reasoning variant exists | Strong 67.3 MMLU /74.4 HumanEval at 3.8B | Think/no_think dual mode | Agentic/tool | Strong but restricted |
| **BBPE/Tokenizer** | 151K BBPE +22 ctrl | Gemma 256K SP family | Tekken 131K | 200K o200k tiktoken | 128K Llama3 ext | Liquid tok | 256K |
| **Arabic tok fragmentation** | ~2.4 tok/wd expected (general); no optimized | ~2.3 (measured on 3-4B) | Not measured | Not measured | Not measured | Not measured | 2.30 (measured) |
| **Training ecosystem** | ✅ full (trl/peft/axolotl/unsloth/vllm/llama.cpp/mlx) | ✅ (transformers/gemma.cpp/ollama) | ✅ (transformers/vllm) | ✅ (trl/peft/onnx) | ✅ (transformers>=4.53) | ⚠️ narrow (TF>=5.2) | ✅ but blocked |
| **Quant / runtime** | Q4 GGUF ~3GB, ollama `qwen3.5:4b` | Q6_K/Q4_K_M (~7GB/9GB), llamafile | Q4_K_M 3.4GB, BF16 7.8GB | Q4 ~3GB, onnx | GGUF via llama | GGUF Q4_0 + QAD 96% | Q6_K etc |
| **Device midrange** | ✅ flagship+midrange (fits 8GB Q4) | ⚠️ E2B phone-class OK, E4B ~7-9GB heavier | ✅ fits 8GB class | ✅ fits 8GB class | ✅ fits | ✅ (edge-tuned) | ✅ but blocked |
| **Provenance** | Alibaba Qwen Team, HF/Kaggle/MS, open weights | Google DeepMind, HF Kaggle Vertex, gated HF for 3 | Mistral AI, HF, Apache, cascade paper | Microsoft, HF MIT ungated | HuggingFace TB, HF, full recipe | Liquid AI, HF gated by license | Google, HF gated |
| **Contamination risk** | General web incl. benchmarks — NEEDS_EVIDENCE per FR-004 | Same — NEEDS_EVIDENCE | Same | Synthetic mix — NEEDS_EVIDENCE | Public 11T — NEEDS_EVIDENCE | Unknown — NEEDS_EVIDENCE | Same — NEEDS_EVIDENCE |
| **Medical product safety** | General model, no medical prohibition in license | MIT/Apache — no medical prohibition | Apache — no prohibition | MIT — requires high-risk eval per card (compatible) | Apache — no prohibition | LFM ToU — no medical carve-out | **Prohibited Use Policy: medical diagnosis is restricted use** |

> Shaded: Green = compatible with FD-001 permissive lineage; Red = incompatible or conditional for Core.

---

## 6. Detailed axis assessments

### 6.1 Medical-capability evidence

No candidate is a medical-domain model. All are general-purpose base/instruct models whose medical capability must be measured under the frozen evaluation protocol (Spec 001–002). Public benchmark evidence is **development signal only**:

- Phi-4-mini 3.8B dominates reasoning/math at 3B scale (67.3 MMLU / 74.4 HumanEval) — suggests strong instruction/reasoning base for differential reasoning, active information acquisition, and tool routing after SFT.
- Qwen3-4B matches Qwen2.5-72B per vendor claim — 18× parameter efficiency — and leads small-model Arabic MMLU (31.85) among 3B peers, relevant to bilingual medical QA.
- Ministral 3 via cascade distillation claims competitive with models trained on 36T/15T tokens while using only 1–3T from parent — efficient data-recipe angle.
- SmolLM3 claims SoTA at 3B vs Llama 3.2 3B / Qwen2.5 3B — but Arabic medical is weaker (see §6.3).

**No candidate may be chosen on MedQA/MMed claims alone.** Spec 007 FR-005 requires frozen V1 metric catalog + hard gates + stratification; SC-002/SC-003 require zero quarantine leak.

### 6.2 Reasoning capability

- **Unified thinking:** Qwen3 (and SmolLM3) provide explicit thinking control (thinking budget / think-no_think). This maps directly to Spec 010 reasoning-efficiency and Spec 007 abstention/multi-turn hypotheses (correct reasoning vs token waste).
- **Math/coding as proxy:** Phi-4-mini (5T synthetic reasoning-dense) and Qwen3 (36T) lead general reasoning — correlates with differential reasoning and structured-output fidelity but is not causal for medical correctness.
- **Distilled reasoning:** Ministral 3 Reasoning variant and cascade approach show reasoning can be transferred without full pretrain replay — informs Spec 009 distillation strategy.

### 6.3 Arabic capability

Critical for commandMed's bilingual thesis (MSA + Saudi/Gulf colloquial + code-switch + transliterated medication names per `plan.md` §17):

- **Best evidence:** Qwen3 4B Arabic Belebele **51.78** is the clear leader among Apache 3B/4B peers per SmolLM3 report (vs SmolLM3 40.22, Qwen2.5-3B 44.22, Llama 3.2 3B 45.33). Qwen3 also lists 7 Arabic dialects in pretraining (Najdi etc.) vs Gemma 3's undifferentiated 140+ and Phi's unquantified 23-language inclusion. Earlier MedArabiQ evaluation (2025) found Qwen2.5-7B strongest among open-access on Arabic medical — Qwen3 retains that lineage.
- **Mid:** Phi-4-mini supports Arabic (23 languages) with 200K vocab — plausible strong Arabic given tiktoken breadth, but no Arabic medical benchmark published for 3.8B. Ministral 3 3B supports Arabic among "dozens" but not top claim.
- **Weak:** SmolLM3-3B Arabic Belebele 40.22 — explicitly trained with fewer Arabic tokens; core languages are European. For commandMed Arabic Gulf focus, this is a material risk without Spec 013 rescue.
- **All:** General tokenizer fragmentation for Arabic is structural: ACL 2026 paper reports ~2.4 tok/word for Arabic vs ~1.5–1.6 for English across model-native tokenizers; MedArabiQ/Qwen analyses confirm. Gemma-3-4B-it measured 2.30 tok/word Arabic vs 1.57 English. Without Arabic-optimized tokenizer, longer effective sequences and sharper degradation with input length occur. No candidate ships with AraToken-optimized vocab by default.

### 6.4 Tokenizer suitability

| Candidate | Vocab | Arabic tok behavior (2026-08-27) |
|---|---|---|
| Qwen3 | 151,643–151,646 BBPE +22 ctrl | General BBPE; fragmentation ~2.4 tok/word (general family). AraToken LEP shows 18% fertility improvement (1.199 vs 1.35) via SentencePiece+normalization + vocab extension on Qwen3-0.6B, but not default. |
| Gemma 4 (est.) | 256,128 (Gemma 2/3 family) | Similar fragmentation (Gemma-3-4B 2.30 tok/wd). Multilingual-efficient but not Arabic-focused. |
| Ministral 3 Tekken | 131,072 | Not measured for Arabic; 131K is smaller than Qwen 152K / Gemma 256K / Phi 200K — may be less suited for Arabic morphology. |
| Phi-4-mini o200k | 200,064 | Large tiktoken; likely best compression among candidates given 200K breadth, but no published Arabic tok/word. |
| SmolLM3 Llama3 | 128,256 (100K+28K ext) | 3.94 chars/token en; Arabic not characterized; 28K non-English expansion helps but Arabic still secondary. |

Tokenizer choice affects `supervised_token_count` vs `rendered_token_count` invariants (§10 DatasetSnapshot), packing/truncation safety (required safety context must not be truncated), and peak memory at context. Evaluation protocol must freeze rendering/loss-mask identities per checkpoint.

### 6.5 Licensing & redistribution constraints (FD-001 decision-critical)

See §3 and §4 license rows and sources cited in §1. Key points:

- **Apache 2.0 (Qwen3, Gemma 4, Ministral 3, SmolLM3):** Permits use, modification, distribution, sublicensing, commercial use, with NOTICE/attribution to downstream users; patent grant; no prohibited-use medical carve-out; no unilateral termination on policy change; derivatives may carry additional terms if not conflicting. This satisfies `OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE`.
- **MIT (Phi-4-mini):** Even more permissive — OSI-approved, allows unrestricted commercial use/modification/distribution with attribution; no flow-down medical restriction beyond general "evaluate high-risk" guidance. Satisfies FD-001 optimally.
- **LFM Open License v1.0:** Grants copyright/patent "subject to Section 5" commercial limitation — free commercial use **only if annual revenue <$10M**; above threshold, commercial use is **not licensed** (requires paid license from Liquid AI). Derivatives inherit. Qualified non-profit research exempt. This creates a commercialization cliff incompatible with a permissive open-weights product intended to scale. Remains research-only/conditional per Grand Master Plan §6 and FD-001.
- **Gemma Terms of Use (Gemma 3):** Not Apache/OSI; incorporates Prohibited Use Policy (restricts health-related professional practices), defines Distribution to include Hosted Service (API counts as distribution triggering flow-down), requires downstream users be bound to same restrictions, reserves unilateral term modification and termination, and applies to derivatives. For commandMed — a health intelligence system - this is a **direct license conflict**: training or serving a Gemma-3-derived medical model would remain subject to the health-practice prohibition and could expose downstream distributors to breach/termination. **Recommendation in this packet: exclude Gemma 3 weights from Core tournament.** Gemma 4 Apache resolves this; Gemma 3 does not.

> All licensing interpretations in this packet are independent readings of linked texts, not legal advice. Final lineage clearance requires counsel review of the exact model revision, dataset license, and derivative posture before any admission (FR-004).

### 6.6 Model size, architecture, context, hardware/runtime implications

- **Size for FLAGSHIP_PLUS_MODERN_MIDRANGE:** 3–4B dense is the viable window (8GB VRAM Q4 ~3GB). 1.7B may be too small for medical reasoning retention; 24B+ (Mistral Small 3.1) is out-of-class for V1 Core (teacher/control only). Gemma 4 E-series effective-vs-raw accounting is a trap: E2B ~2.3B eff but 7.2GB download / larger bytes than 3B dense — strict shipped-bytes + peak-RAM accounting per §3 of density strategy required, not parameter marketing.
- **Context:** Ministral 3 256K is the widest; Phi-4-mini and SmolLM3 128K; Qwen3 32K (small) / 128K (larger) / 256K (Qwen3.5 multimodal). Longer context helps with RAG evidence/tool traces but KV-cache cost must be measured on real devices (Spec 012). For V1 SFT, sequence budget and packing/truncation policy must be frozen before training (FR-006, C-005).
- **Architecture trade-offs:** Qwen3 BBPE + hybrid thinking; Phi-4 synthetic-dense reasoning; SmolLM3 NoPE (long-context alternative to RoPE, YaRN-extended); Ministral cascade (compute-efficient distillation from 24B parent over 1–3T vs 11–36T). Each changes pretraining compute vs inheritance — but V1 SFT selection is on frozen tournament evidence, not architecture aesthetics.
- **Runtime implications:** All candidates run on `transformers` + `trl` + `peft`; quantized inference via `llama.cpp` GGUF or `mlx` or `ollama`. Gemma 4 edge-tuned for phones/Raspberry Pi (E2B); LFM2.5 edge-tuned with QAD. On-device thermals/energy per Spec 012 remain NEEDS_EVIDENCE until device execution authority.

### 6.7 Training ecosystem support

Qwen3 > Phi-4-mini > SmolLM3 > Ministral 3 > Gemma 4 in community breadth as of 2026-03 surveys, but **all Apache/MIT candidates are TRL-compatible** for SFT/DPO/GRPO, support loss-mask by token class (to be verified per backend per C-004), support resume (optimizer/scheduler/RNG/data position — per C-016), and have `vllm`/`sglang` inference for tournament fixture harness (which must stay deterministic and fixture-only per Spec 004). LFM2.5 ecosystem is narrower (transformers >=5.2 only per docs) — not a blocker but a maintainability cost.

### 6.8 Quantization support

- Standard GGUF Q4_K_M / Q5 / Q8 supported across Qwen3, Gemma 4, Ministral 3 (3.4GB vs 7.8GB BF16), Phi-4-mini, SmolLM3, LFM2.5 (plus Liquid QAD Q4_0 at 96–97% BF16). QAD is the relevant compression research for Spec 012: QAD closes 48–73% of BF16→Q4 gap vs PTQ (QAD paper 2026-08-19, four scales). However QAD is an **experiment**, not a baseline claim (density strategy §17). Medical equivalence after quantization must be re-proven per level (Spec 012) — 96% generic retention ≠ medical safety equivalence.
- LiteRT / `gemma.cpp` (Gemma), MLX (Apple Silicon) relevant to named device matrix; to be verified per Runtime/Backend evidence before any training authorization.

### 6.9 Reproducibility

No candidate offers cross-stack bitwise determinism. PyTorch docs (cited in research.md R-009) explicitly do not guarantee full reproducibility across releases/platforms/hardware. Spec 007 C-015 levels apply: `EXACT_ENVIRONMENT_REPLAY` (pinned OS/container+Python+framework+backend+runtime+device+driver+attention kernel+precision+seeds+data order) vs `CROSS_ENVIRONMENT_REPRODUCIBILITY` (statistical/behavioral equivalence). Environment pinning is a planning invariant; actual nondeterminism list is implementation evidence.

### 6.10 Model provenance & safety implications

- **Qwen3 / Qwen2.5:** Alibaba Cloud; Apache weights but pretraining data mixture not fully open (36T web/code/science multilingual). No declared PHI. Safety is general; not medical-aligned.
- **Gemma 4:** Google DeepMind Gemini technology lineage; Apache weights (4 only) with HF ungated distribution; prior Gemma safety investigations but not medical.
- **Ministral 3:** Mistral AI; cascade from Mistral Small 3.1 (Apache); 1–3T tokens via teacher; not medical.
- **Phi-4-mini:** Microsoft; 5T tokens synthetic + filtered web; safety via SFT+DPO enhancement; not medical.
- **SmolLM3:** HuggingFace TB; 11T public data mixture + full recipe + intermediate checkpoints — highest transparency among candidates.
- **LFM2.5:** Liquid AI; agentic pretraining inside harness; not medical.

**Safety note:** Smaller models are not presumed safer. Fine-tuning can degrade aligned behavior (research.md R-006 cites Fine-tuning Aligned LMs Compromises Safety). Spec 007 requires abort-only sentinel (abort/disqualify only, no ranking), capability-preservation binding, and full hard-gate requalification after any stage.

### 6.11 Benchmark contamination concerns

Every candidate's pretraining corpus (11T–36T web) plausibly contains public medical benchmarks (MedQA, PubMedQA, MedMCQA) and possibly Arabic medical benchmarks (MedAraBench). SmolLM3's public 11T is most auditable. Qwen3 36T is least auditable but largest. **Contamination status remains `NEEDS_EVIDENCE` per FR-004 / C-006:** before any evaluation payload is admitted, exact version, split, overlap detection, and quarantine disposition must be frozen and verified. No public score is treated as release evidence.

### 6.12 Compatibility with frozen architecture & frozen evaluation protocol

All permissive candidates are compatible with Spec 007's frozen contracts:

- Strict record parsing (`foundation.py` closed vocabularies, duplicate-key-safe JSON, SHA-256).
- CurriculumRecord with `knowledge_placement` (durable vs mutable vs tool) and full provenance bundle (FR-004).
- LanguageProfile with dialect/code-switch/transliteration/terminology-normalization (C-009/010).
- Rendering/loss-mask/packing as versioned policies (C-003/004/005) — backend neutrality preserved until `BackendCandidateEvidence` freezes.
- Full quarantine matrix binding (C-011, FR-003) with canonical `quarantine.json` identity (not prose copy).
- Capability preservation + abort-only sentinel + fixed checkpoint rule (C-012–014) — no checkpoint ranking via protected assets.
- Environment/Resume/RunManifest chain (C-015–016, data-model.md).
- Frozen evaluation protocol binding that is a **precondition** of `TRAINING_AUTHORITY=AUTHORIZED_TO_RUN` (C-018 handshake, FR-005).

Band selection (FULL / LORA / QLoRA) is **not selected** here; Spec 007 C-017/018 requires `NON_EXECUTING_RECIPE_EVIDENCE` (static estimates, documented compatibility, rendering/loss/packing conformance) before any training authorization — empirical loss/gradient evidence would require separate execution authority and is not in this packet.

---

## 7. Proposed candidate manifest structures for Founder+ChatGPT

This packet **does not freeze** the manifest. It proposes manifest shapes so Founder + ChatGPT can choose exactly. The tournament harness (Spec 004) will compare candidates under the frozen protocol across: core medical quality, patient conversational quality, uncertainty/abstention, Arabic/English, general-preservation potential, multimodal/document where applicable, fine-tuning stability, bytes/peak-RAM, real measured on-device performance, and license/lineage fit (Grand Master Plan §6, Tournament axes).

### Option A — Permissive-only compact tournament (recommended shape given FD-001)

Freeze **exactly** the permissive Apache/MIT candidates whose pretraining lineage and redistribution fit `OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE`, covering flagship+midrange:

```
CANDIDATE_MANIFEST_A (permissive-only)
  - Qwen3-1.7B-Base (Apache 2.0)           — smallest Apache dense with thinking mode
  - Qwen3-4B-Base (Apache 2.0)            — strongest Arabic 3B-class per Belebele
  - Gemma-4-E2B-Base (Apache 2.0)         — edge edge-class anchor (~2.3B eff)
  - Gemma-4-E4B-Base (Apache 2.0)         — mid-resource Apache Google alternative
  - Ministral-3-3B-Base-2512 (Apache 2.0) — 256K + vision small
  - Phi-4-mini-Base (MIT)                 — strongest math/reasoning per GB
  - SmolLM3-3B-Base (Apache 2.0)         — most transparent 11T recipe
  (total 7 candidates)
```

- **Rationale:** Every weight lineage is Apache 2.0 or MIT; no revenue threshold; no medical prohibited-use; all fit 8GB Q4 class; all support 128K–256K context; together they span Qwen synthetic/thinking (36T), Gemma edge (Gemini tech), Mistral cascade (1–3T teacher transfer), Phi synthetic-reasoning (5T), and SmolLM full-openness (11T). Medical capability remains to be measured — not assumed.
- **Not included:** Gemma 3 (custom ToU), LFM2.5 (revenue-gated), Qwen2.5-3B (custom Qwen terms superseded by Qwen3), >4B+ (control only).

### Option B — Permissive primary + single conditional efficiency probe (research track, not Core release lineage)

```
CANDIDATE_MANIFEST_B = MANIFEST_A + one conditional probe
  + LFM2.5-1.2B-Base (LFM v1)   — OR LFM2.5-2.6B (pick one, not both) as efficiency-first research reference only
```

- **Rationale:** If Founder wants to test LFM's QAD/compression efficiency thesis (96–97% BF16 at Q4) as a **research-only** comparator, admit exactly one LFM probe under explicit annotation `TRACK=M_EFFICIENCY_CONDITIONAL — NOT EligibleForCoreRelease`. Tournament axes must then score LFM on efficiency exclusively and ignore it for final winner. Legal exposure: derivative commercial use above $10M would require separate Liquid AI paid license; must not taint Core.

### Option C — Minimal 3-candidate tournament (lowest operational cost)

```
CANDIDATE_MANIFEST_C (minimal)
  - Qwen3-1.7B-Base + Qwen3-4B-Base (Apache 2.0 — brackets size)
  - Phi-4-mini-Base (MIT — strongest permissive reasoning)
  - Ministral-3-3B-Base (Apache 2.0 — vision+256K edge probe)
```

- **Rationale:** Lowest device/operation cost while still covering Arabic leader (Qwen), reasoning leader (Phi), vision/long-context edge (Ministral). Gemma 4 could substitute for Ministral if Founder prefers Google lineage. Trade-off: less recipe transparency (SmolLM) and no Gemma edge.

**All options require before freeze:**

- Exact HF revision + weight content SHA where available (`weight_content_identity` per data-model.md §8) — not just repo tag.
- Exact tokenizer revision/content/config identity, special-token map, chat-template identity, BOS/EOS/tool-format policy (C-002).
- Exact license evidence artifact per checkpoint for FD-001 verification.
- Device/runtime `ResourceAccountingRecord` shape validated offline (real measurements remain `NEEDS_EVIDENCE` until device authority).
- Arabic tokenizer-efficiency measurement protocol frozen (tokens/word, chars/token, med-term fragmentation per plan.md §17.2) — to be populated by tournament harness, not this packet.

### What is NOT a valid manifest

- Any manifest naming Gemma 3 weights as candidate — fails FD-001.
- Any manifest mixing LFM candidates into the Core winner pool — contaminates permissive lineage unless explicitly gated as research-only with no path to release.
- Any manifest frozen without exact tokenizer/template/revision identities — creates new recipe identity risk (C-002/003).
- Any manifest that selects a backbone winner — `BACKBONE_WINNER=NEEDS_EVIDENCE` remains; selection is Founder+ChatGPT only **after** authorized tournament evidence exists (C-001).

---

## 8. Decision required from Founder + ChatGPT

To unblock `E001` → `E002`/`E003`, the following **explicit** Founder+ChatGPT decision must be recorded canonically (and reflected in `specs/README.md` decision register and/or a separate `E001` closeout artifact) with exact identities:

```
FOUNDER+CHATGPT_DECISION_E001:
  CANDIDATE_MANIFEST_FROZEN=<Option A | Option B (with probe scope) | Option C | custom exact list provided by Founder>
  MANIFEST_VERSION=<frozen version string>
  MANIFEST_CONTENT_SHA256=<hash over full manifest JSON>
  MANIFEST_SOURCE_AUTHORITY_ID=<provenance/License DS>
  EXACT_CHECKPOINTS=[
    {checkpoint_identity, model_repository_id, model_revision, weight_content_identity, tokenizer_identity, chat_template_identity, license_evidence_id}
  ]
  ARABIC_TOKENIZER_EFFICIENCY_MEASUREMENT_PROTOCOL_FROZEN=<yes/no — if yes, bind identity>
  QUARANTINE_MATRIX_IDENTITY=<bound to Spec 004-005 canonical quarantine set, not prose copy>
  NOTES=<any Founder-provided scope caveat, e.g., "LFM probe is TRACK=M and ineligible for Core">
  FOUNDER_SIGNOFF_AT=<ISO-8601 timestamp>
  CHATGPT_CONCURRENCE_AT=<ISO-8601 timestamp>
```

No PI selection. No tournament execution. No training.

---

## 9. What remains gated after E001

| Gate | Authority |
|---|---|
| E002 Model/weight access | `SEPARATE_AUTHORIZATION_REQUIRED` |
| E003 Live tournament execution | `SEPARATE_AUTHORIZATION_REQUIRED` |
| E004 Tournament evidence pack | `EXECUTION_REQUIRED` (depends on E003 + frozen protocol + effective manifest) |
| E005 Backbone winner | `FOUNDER+CHATGPT_DECISION_REQUIRED` (after E004) |
| E006 Tokenizer/template/checkpoint identities | Depends on E005 |
| E007 Backend/update strategy | Depends on E005–E006 |
| E008 Real curriculum | `DATA_AUTHORITY_REQUIRED` |
| E009 Snapshot + numerics | Depends on E007–E008 |
| E010 Protocol/device/finance/activation | Depends on E005–E009 |
| E011 Training authority | `FOUNDER_AUTHORIZATION_REQUIRED` (exact RunManifest) |
| E012 First SFT run | `TRAINING_EXECUTION` (after E011) |
| ... | ... |

This packet does not change `TRAINING_AUTHORITY`, `MODEL_EXECUTION_AUTHORITY`, `MODEL_WEIGHT_ACCESS_AUTHORITY`, `SPEND_AUTHORITY`, or any other execution authority — all remain `NONE`.

---

## 10. Preservation controls enforced in this packet

- Every unresolved numeric/license binding is typed `NEEDS_EVIDENCE` — no placeholder fiction.
- No dataset snapshot is constructed or claimed valid.
- No protected Gold/quarantine source enters any tuning surface.
- No backend default determines rendering or loss masking.
- No public record is claimed (`#1`/`SOTA` prohibited until pre-registered `RecordClassDefinition` + reproducible evidence).
- No training pilot is performed or implied.

---

## 11. Recommended Founder next steps

After reviewing this packet, Founder + ChatGPT should:

1. Choose exactly one manifest option (A/B/C) or supply a custom exact list — annotate any conditional research track as `NOT EligibleForCoreRelease`.
2. Freeze the manifest with version, SHA, full checkpoint+tokenizer+template identities, and license evidences.
3. Canonicalize that decision (merge to `main`) so E002/E003 can be separately authorized.
4. Separately grant (or defer) weight-access and tournament-execution authorities — they are not implied by manifest freeze.

---

## 12. Sources (primary, fetched 2026-08-27)

- `huggingface.co/Qwen/Qwen2.5-3B` and `huggingface.co/Qwen/Qwen2.5-3B-Instruct` — model cards (Apache vs Qwen terms per size, 151K BBPE, 32K context, etc.)
- `github.com/QwenLM/Qwen3` and `qwenlm.github.io/blog/qwen3` (2025-04-29) — Apache 2.0 claim, 119 languages, thinking mode, 36T tokens
- `arxiv.org/abs/2505.09388` (Qwen3 Technical Report) — architecture, 36T, 119 languages, thinking budget
- `huggingface.co/blog/smollm3` and `huggingface.co/HuggingFaceTB/SmolLM3-3B*` README — 3B 11T, NoPE+YaRN 128K, 6 core languages, Arabic secondary, Apache 2.0, Belebele table (Arabic 40.22 vs Qwen3 4B 51.78)
- `github.com/huggingface/smollm` — SmolLM family overview, Apache
- `huggingface.co/microsoft/Phi-4-mini-instruct` README — MIT, 3.8B, 200K tiktoken, 128K, 5T tokens, 23 languages inc. Arabic
- `arxiv.org/abs/2503.01743` — Phi-4-Mini Technical Report (reasoning-dense synthetic, LongRoPE, matches R1-Distill 7B)
- `huggingface.co/mistralai/Ministral-3-3B-Instruct-2512` and `huggingface.co/mistralai/Ministral-3-3B-Base-2512` + `huggingface.co/mistralai/Mistral-Small-3.1-24B*` — Apache 2.0, Tekken 131K, 256K context, vision, cascade distillation
- `arxiv.org/abs/2601.08584` — Ministral 3 report (9 models, 1–3T via cascade from Small 3.1)
- `mistral.ai/news/mistral-small-3` (2025-01-30) — Small 3 Apache announcement
- `huggingface.co/LiquidAI/LFM2.5-2.6B` and `huggingface.co/LiquidAI/LFM2.5-1.2B` — LFM1.0 license, 32K/128K, agentic
- `liquid.ai/lfm-license` and `docs.liquid.ai/lfm/help/model-license` and `liquid.ai/blog/qad` (2026-08-19) — LFM revenue threshold $10M, QAD 96–97% BF16 at Q4_0
- `ai.google.dev/gemma/terms` and `ai.google.dev/gemma/prohibited_use_policy` + `vorplabs.com/models/gemma-license` + `github.com/google-deepmind/gemma/blob/main/LICENSE` (branch showing Apache for Gemma 4) — Gemma 3 custom vs Gemma 4 Apache 2.0 distinction (Vorp analysis, 2026-04-02/04-01 per custom terms)
- `developers.googleblog.com/.../introducing-gemma3` (2025-03-12) — Gemma 3 multimodal 128K, 140+ languages
- `aclanthology.org/2026.healing-1.13.pdf` (Cross-Lingual Arabic medical LM, 2026-03-28) — tokenization fragmentation 2.4 vs 1.5 tok/word, Gemma-3-4B 2.30 tok/wd
- `arxiv.org/abs/2512.18399` (AraToken LEP, Qwen3) — SentencePiece 1.199 fertility, 18% improvement, LEP on Qwen3
- `proceedings.mlr.press/v298/daoud25a` (MedArabiQ) and `arxiv.org/abs/2505.03427` — Arabic medical benchmark methodology
- Secondary aggregator `localaimaster.com/blog/small-language-models-guide-2026` and `bentoml.com/blog/best-open-source-slms-2026` — used only to cross-check SLM rankings and Ollama footprints, not as primary license/performance source

All benchmark numbers above are per-source claims, not commandMed measurements. They are **not** frozen evaluation results and cannot authorize a backbone winner.

---

## 13. Packet integrity

```
PI_RECOMMENDATION=NONE
DECISION_OWNER=FOUNDER+CHATGPT
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PACKET_KIND=E001_EVIDENCE_ONLY
PACKET_VERSION=2026-08-27-E001-FRESH-LANDSCAPE-v1
VERIFICATION_STATE=PRIMARY_SOURCES_FETCHED_2026-08-27_PRIMARY_CARDS_TERMS_REPORTS
```

This packet may be reviewed, commented upon, and canonically merged as documentation/research — it does not itself satisfy `E001` until Founder + ChatGPT explicitly freeze the manifest with exact identities in a canonical decision record.

---

**Prepared by:** Pi (evidence synthesis only) — no selection, no ranking, no training, no model execution.
**Next frontier after canonical freeze:** `E002` (model/weight access) / `E003` (tournament execution) — each `SEPARATE_AUTHORIZATION_REQUIRED`.
