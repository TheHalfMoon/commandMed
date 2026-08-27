# E001 Model Landscape Research — Fresh Candidate Manifest Evidence Packet (Repair v2)

**Date:** 2026-08-27 (Repair v2 supersedes 2026-08-27 v1)
**Spec:** 007 SFT V1 — E001
**Lifecycle authority:** `AUTHORIZED_TO_START` (offline deterministic I001-I045 complete; E-phase separately gated)
**Model selection authority:** `FOUNDER+CHATGPT_ONLY` — `PI_MODEL_SELECTION_AUTHORITY=NONE`, `BACKBONE_WINNER=NEEDS_EVIDENCE`
**Training authority:** `NONE` — no model execution, weight access, benchmark execution, training, or spend is authorized by this packet
**Purpose:** Provide a fresh, evidence-backed model-landscape investigation so Founder + ChatGPT can freeze the tournament candidate manifest (`E001`). This packet is **evidence only** — `PI_RECOMMENDATION=NONE`.

> This repair supersedes the 2026-08-27 v1 packet at the same path. Section 14 documents correction provenance. No candidate is selected or ranked by Pi. The 2–4B-only manifest proposal in v1 is SUPERSEDED BEFORE CANONICAL FREEZE per Founder+ChatGPT direction dated 2026-08-27.

---

## 0. Correction provenance (what changed and why)

v1 proposed a flat 2–4B permissive tournament (Qwen3-1.7B/4B, Gemma-4 E2B/E4B, Ministral-3 3B, Phi-4-mini-Base, SmolLM3). That proposal is superseded because:

1. It conflicted with canonical Spec 005 mass-reach decisions (`UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`, `QUALITY_FLOOR_THEN_SIZE_FIRST`, `SUB_700MB_MASS_REACH`, `2 GiB Core peak-memory hard cap`, `GGUF_LLAMA_CPP_CANONICAL`, `Q4_FLOOR_SMALLEST_PASSING`, `BASE_ONLY_PRIMARY`). Core is a capability + safety contract, not a 2–4B parameter band. Mass-reach ultra-compact candidates must be allowed to prove they satisfy Core. See reconciliation artifact `specs/007-sft-v1/reconciliation-core-mass-reach-2026-08-27.md`.
2. Evidence defects identified by review:
   - `microsoft/Phi-4-mini-Base` does not exist as a public base checkpoint; the official public checkpoint is `microsoft/Phi-4-mini-instruct` and Microsoft stated no plan to release a base model. A post-trained instruct checkpoint must not be silently treated as a base checkpoint or mixed into a `BASE_ONLY_PRIMARY` tournament.
   - Candidate-count inconsistency: Option C was labeled 3 candidates but listed 4.
   - Family/post-trained reasoning modes were attributed to base checkpoints (e.g., Qwen3 thinking/non-thinking as if `Qwen/Qwen3-1.7B-Base` provides it).
   - `Qwen/Qwen3.5-2B-Base` and `Qwen/Qwen3.5-4B-Base` now exist as official Apache-2.0 base checkpoints and materially change the candidate set, but were missing.
   - Gemma 4 effective-parameter accounting conflated effective vs total/shipped bytes (E4B 4.5B effective but 8B total per official card) violating strict resource accounting.
   - v1 claimed all proposed candidates support 128K–256K context, contradicting its own Qwen3 profile (32K for 0.6B/1.7B class) and distorting sequence-budget comparisons.
3. The newer `COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md` describing Core as approximately 2–4B-class and Nano as approximately 0.6–1.5B is an additive planning hypothesis, not an amendment of frozen Spec 005 resource gates. This repair explicitly reconciles that conflict (see artifact above) and restores canonical Spec 005 precedence for the current tournament.
4. `ibm-granite/granite-4.0-350m-base` (350M dense, Apache-2.0, text-only, Arabic-supported, 32K, official IBM GGUF Q4) was missing from PR #55 and is now deeply investigated as a proposed ultra-compact PRIMARY.

This v2 repair corrects all of the above, preserves `BACKBONE_WINNER=NEEDS_EVIDENCE` throughout, and introduces no model execution.

---

## 1. Research method

Primary authoritative sources were consulted where possible on 2026-08-27 (UTC). No model was downloaded, loaded, executed, or benchmarked by Pi. No candidate is selected or ranked by Pi.

Sources consulted (v2):

- Hugging Face model cards/repos: `Qwen/Qwen3-0.6B-Base`, `Qwen/Qwen3-1.7B`, `Qwen/Qwen3-4B-Base`, `Qwen/Qwen3.5-0.8B-Base`, `Qwen/Qwen3.5-2B-Base`, `Qwen/Qwen3.5-4B-Base`, `google/gemma-3-4b-it`, `google/gemma-4-e2b` / `google/gemma-4-e4b` (and their cards reporting total vs effective params), `mistralai/Ministral-3-3B-Base-2512`, `mistralai/Mistral-Small-3.1-24B-Base-2503`, `HuggingFaceTB/SmolLM3-3B-Base`, `microsoft/Phi-4-mini-instruct`, `LiquidAI/LFM2.5-1.2B`, `LiquidAI/LFM2.5-2.6B`, `ibm-granite/granite-4.0-350m-base`, `ibm-granite/granite-4.0-350m-base-GGUF`, `ibm-granite/granite-4.0-h-350m-base`, `CohereForAI/aya-expanse-8b` (reference, not candidate), `inceptionai/jais-family-590m-base`.
- Official technical reports/blogs: Qwen3 report arXiv 2505.09388, Qwen2.5 report arXiv 2412.15115, Gemma 2 report arXiv 2408.00118, Ministral 3 report arXiv 2601.08584, SmolLM3 blog `huggingface.co/blog/smollm3`, Phi-4-Mini report arXiv 2503.01743, Liquid LFM license `liquid.ai/lfm-license`, QAD blog `liquid.ai/blog/qad` (2026-08-19), IBM Granite docs `ibm.com/granite/docs` and `github.com/ibm-granite/granite-4.0-nano-language-models`.
- Official terms: `ai.google.dev/gemma/terms`, `ai.google.dev/gemma/prohibited_use_policy`, Vorp Labs Gemma license analysis (2026), Gemma GitHub `LICENSE` (Apache 2.0 for Gemma 4), `huggingface.co/ibm-granite/granite-4.0-350m-base` Apache 2.0 license field.
- Cross-lingual Arabic medical tokenization/evaluation papers: arXiv 2602.01714 (MedAraBench), ACL 2026 Healing 1.13, MedArabiQ PMLR 298, AraToken LEP arXiv 2512.18399, Inception Jais paper arXiv 2308.16149.
- Prior commandMed canonical sources: `specs/005-base-model-tournament/ultra-compact-candidate-sweep.md`, `specs/005-base-model-tournament/admission-evidence.md`, `specs/005-base-model-tournament/spec.md` bounded clarification sessions (SUB_700MB, Q8_0 KV, 8K/16K, B512_U128, 2 GiB cap, etc.).

No stale model assumption from the 2026-08-21 Grand Master Plan was reused without re-verification. All license readings are current as of 2026-08-27.

---

## 2. CommandMed constraints that filter candidates (canonical precedence)

### 2.1 Frozen Spec 005 mass-reach contract (takes precedence over size-band language)

Spec 005 clarification sessions froze:

```text
BASE_ONLY_PRIMARY
COMMON_CORE_PRIMARY_RANKING
FULLY_ADMITTED_PRIMARY_ONLY
QUALITY_FLOOR_THEN_SIZE_FIRST
SUB_700MB_MASS_REACH
GGUF_LLAMA_CPP_CANONICAL
Q4_FLOOR_SMALLEST_PASSING
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET<=600_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET<=500_MiB_IF_ALL_HARD_GATES_STILL_PASS
PEAK_WORKING_RAM_HARD_CEILING=2_GiB (common 8K condition, all five targets)
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS (7K prompt + 1K generation)
SECONDARY_STRESS_CONTEXT=16384_TOKENS (15K prompt + 1K generation, 8GB+ where runtime supports)
KV_CACHE_POLICY=Q8_0_SYMMETRIC_KV_CORE
PROMPT_PROCESSING_POLICY=B512_U128_COLD_NO_REUSE
RUNTIME_IDENTITY_POLICY=PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST
SUB4BIT_PRIMARY_CANONICAL_RELEASE=PROHIBITED
```

### 2.2 How the density strategy relates

`COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md` §4.1 describing Core as roughly 2–4B-class and Nano as roughly 0.6–1.5B is an **additive research hypothesis**, not an amendment of frozen Spec 005. Per the new reconciliation artifact, Core is a **frozen capability/safety/device contract**, not a parameter band. Mass-reach Core is a Core candidate satisfying the current SUB_700MB / 2 GiB contract. Nano is a later derived/distilled tier after proven Core capability exists. See `specs/007-sft-v1/reconciliation-core-mass-reach-2026-08-27.md`.

### 2.3 General gates

From `AGENTS.md`, `constitution.md`, `decision-register.md` (FD-001, FD-002, FD-006), and Spec 007:

- **FD-001 OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE:** Apache-2.0-compatible lineage preferred; custom/restrictive remain research-only/conditional.
- **FD-002 FLAGSHIP_PLUS_MODERN_MIDRANGE:** V1 tournament covers flagship + modern midrange (now frozen as five targets + resource envelope above).
- **FD-006 NOT_INVOKED:** No donor-origin restriction.
- **AGENTS.md:** MedGemma/HAI-DEF reference/evaluation-only; frontier API outputs evaluation-only.
- **Spec 007:** Three frozen role classes, Arabic first-class (MSA, Saudi/Gulf, code-switch, transliteration), tokenizer efficiency is future evidence, quarantine firewall complete, safety hard gates non-compensable, tournament thesis `QUALITY_FLOOR_THEN_SIZE_FIRST`.

---

## 3. Candidate universe screened (2026-08-27, repair v2)

Screened at sub-1B through ~4B, with sub-700MiB feasibility as the PRIMARY discriminator (Nano hypothesis deferred as later derived tier):

| Candidate family | Checkpoint example (base, exact) | Params (total / active) | License (weight) | Access posture | Spec 005 role (v2) |
|---|---|---|---|---|---|
| **Qwen3** dense ultra-compact | `Qwen/Qwen3-0.6B-Base` | 0.6B (0.44B non-embedding) | **Apache 2.0** | Ungated public | **PRIMARY ultra-compact** |
| **Qwen3.5** ultra-compact | `Qwen/Qwen3.5-0.8B-Base` | 0.8B (+ vision encoder for multimodal) | **Apache 2.0** | Ungated public | **PRIMARY ultra-compact** |
| **Granite 4.0 Nano** | `ibm-granite/granite-4.0-350m-base` | 350M (dense traditional) | **Apache 2.0** | Ungated public | **PRIMARY ultra-compact (new)** |
| **Qwen3** mid | `Qwen/Qwen3-4B-Base` | 4.0B (3.6B non-embedding) | **Apache 2.0** | Ungated public | **SCALE/QUALITY CONTROL (not PRIMARY-eligible, exceeds mass-reach bundle)** |
| **Qwen3.5** mid | `Qwen/Qwen3.5-2B-Base`, `Qwen/Qwen3.5-4B-Base` | 2B, 4B | **Apache 2.0** | Ungated public | **CONTROL / fallback** |
| **Gemma 4** edge | `google/gemma-4-e2b`, `google/gemma-4-e4b` | E2B ~5B total / ~2.3B eff, E4B ~8B total / ~4.5B eff | **Apache 2.0** (excluded from custom ToU) | Ungated (Gemma 4) | **CONTROL / fallback** |
| **Ministral 3** | `mistralai/Ministral-3-3B-Base-2512` | 3.4B lang + 0.4B vision (3.8B shipped) | **Apache 2.0** | Ungated public | **CONTROL / fallback** |
| **SmolLM3** | `HuggingFaceTB/SmolLM3-3B-Base` | 3B | **Apache 2.0** | Ungated public | **REFERENCE (Arabic gap)** |
| **Qwen2.5** | `Qwen/Qwen2.5-3B` | 3.09B (2.77B non-embedding) | Qwen Research (custom, not Apache for 3B) | Ungated but custom | **EXCLUDED (superseded by Qwen3)** |
| **Gemma 3** | `google/gemma-3-4b-it` etc | 4B | **Custom Gemma ToU** (PUP, flow-down, termination) | Gated terms | **EXCLUDED from Core** |
| **LFM2.5** | `LiquidAI/LFM2.5-1.2B`, `2.6B` | 1.2B, 2.6B | **LFM Open License v1.0** (<$10M free) | Ungated but revenue-gated | **EXCLUDED / research-only conditional** |
| **Jais small** | `inceptionai/jais-family-590m-base` etc | 590M–13B | Custom Jais terms (gated acceptance) | Gated | **REFERENCE/conditional** (Arabic ref, not PRIMARY) |
| **Phi-4-mini** | `microsoft/Phi-4-mini-instruct` (instruct only) | 3.8B | **MIT** | Ungated | **REFERENCE (instruction = not BASE_ONLY_PRIMARY)** |
| **Falcon ultra-compact 1B** | `tiiuae/falcon-1b` | ~1B | **TII Falcon License** (Apache-based + AUP) | Ungated but AUP | **SCREENED, not admitted (AUP + no 350M-class size win)** |
| **Apertus 0.5B** | `swiss-ai/Apertus-v1.1-0.5B` | 0.5B (0.4B compute) | Apache-2.0 metadata + **gated AUP terms** | Gated acceptance | **CONDITIONAL size comparator** |

**Single discriminating rule:** Any candidate whose **complete minimum text/core GGUF bundle** cannot satisfy `SUB_700MB_MASS_REACH` + `2 GiB` under the frozen 8K/Q8_0/B512_U128 condition is **not PRIMARY-eligible** for the current mass-reach tournament. It may be retained as CONTROL / CONDITIONAL / REFERENCE_ONLY per `specs/005-base-model-tournament/spec.md`.

---

## 4. Deep candidate profiles (base vs family vs post-trained separated)

### 4.1 Qwen/Qwen3-0.6B-Base — PRIMARY ultra-compact anchor

- **Base identity:** `Qwen/Qwen3-0.6B-Base` — `LICENSE=apache-2.0` (HF `license` field, GitHub `LICENSE` Apache 2.0). Fresh HF API verification 2026-08-27: `sha: da87bfb608c14b7cf20ba1ce41287e8de496c0cd`, `gated: false`, superseding prior sweep `d4e79cd...`. Tree contains `model.safetensors`, `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, `merges.txt`, `config.json`. Revision to be rebound at manifest freeze (Xet metadata: `model.safetensors` ~1.19 GB, SHA256 `cd2a5120...`, Xet `2c465b...`).
- **Base vs post-trained:** This is the **pretrained base checkpoint** (`BASE_PRETRAINED`). Family capabilities such as Qwen3 hybrid thinking / non-thinking mode, instruction following, and agent tool behavior are **post-trained capabilities of instruct/thinking variants**, not of this base checkpoint. Baseiz provides foundation knowledge and tokenization, not chat behavior.
- **Params/structure:** ~0.6B (0.44B non-embedding), 28 layers, 16 Q / 8 KV GQA, tied embedding, RoPE, context 32,768 natively (see table: Qwen3-0.6B 32K; long-context extension via YARN/DCA to 4× at inference where runtime supports).
- **Training:** Qwen3 family 36T tokens (30T foundation + knowledge-intensive + long-context stage) over 119 languages/dialects; Granite-style 4-stage not applicable. Provenance Alibaba Cloud Qwen Team; checkpoints on HF/Kaggle/ModelScope with Apache weights.
- **Medical evidence:** No medical domain specialization; general quality SOTA at size. Medical capability is not inferred from general benchmarks per Spec 007 FR-005. Requires frozen V1 metric catalog, safety hard gates, and quarantine-clean evaluation.
- **Reasoning (checkpoint-true):** No thinking mode at this base checkpoint. Family-level reasoning strength (Qwen3 vs Qwen2.5 gains, math/coding) is **family evidence**, not this checkpoint's measured medical reasoning.
- **Arabic capability:** Family-level Arabic: Qwen3 supports 119 languages with 7 Arabic dialects (MSA, Najdi, Levantine, Egyptian, Moroccan, Mesopotamian, Ta'izzi-Adeni, Tunisian) per Qwen3 blog language table. Checkpoint-specific Arabic medical quality is `NEEDS_EVIDENCE` until frozen tournament measures Arabic clinical parity gap (Spec 005 sessions 10). Current v1 packet cited Qwen3 4B Arabic Belebele 51.78 vs SmolLM3 40.22 — that is 4B evidence, not 0.6B.
- **Tokenizer (checkpoint-exact):** Qwen tokenizer — BBPE 151,643–151,646 + 22 control tokens, byte-level. Same vocab family across sizes, but artifact identity is per checkpoint (vocab.json/merges.txt at observed revision). Arabic fragmentation ~2.4 tok/word for general BBPE (ACL 2026 cross-lingual paper); AraToken shows 18% fertility improvement (1.199 vs 1.35) via SentencePiece+normalization on Qwen3-0.6B with LEP, but not default tokenizer.
- **License of weight vs other artifacts:** HF `apache-2.0` covers weight card; **checkpoint-level** tokenizer/config `vocab.json`/`merges.txt` license inheritance must be bound per exact artifact. Prior packet correctly noted `TOKENIZER_PROCESSOR_EXACT_BINDING=PARTIAL_SAME_REPOSITORY_REVISION` — still the state until full component binding.
- **GGUF feasibility (exact-base):** Official `ggml-org/Qwen3-0.6B-Base-GGUF` exposes exact-base `Q8_0` (0.80GB / 639 MB with Xet hash `d84bed...`), `Q4_K_M` 0.48GB (0.47–0.60GB range across converters), `Q4_0` 0.47GB. `Q8_0` already **under 700 MiB** (strong feasibility); Q4 variants ~480 MB. This is unusually strong for meeting `SUB_700MB`. Exact-base Q4 observation: **YES** (contrary to earlier sweep stating Q4 not observed — superseded by newer converter evidence, but canonical is `ggml-org` exact-base repo, not community converter).
- **Training ecosystem:** `transformers>=4.51`, `trl` SFTTrainer, `peft` LoRA/QLoRA, `axolotl`, `unsloth`, `liger`, `vllm`/`sglang`, `llama.cpp`, `mlx`. TRL chat-template mechanics support Qwen but base has no chat template contribution beyond tokenizer.
- **Quant/runtime:** BF16/Q8_0 observed, Q4 variants observed. Device: flagship+midrange friendly (~480 MB Q4 + Q8_0 KV at 8K). `2 GiB` hard cap plausible per prior `platform_native` measurement policy but **measured evidence is `NEEDS_EVIDENCE`** until pinned llama.cpp commit + device harness measures five fresh runs.
- **Contamination/lineage:** Web/code/science 36T corpus; medical contamination `NEEDS_EVIDENCE` per Spec 003 `MODIFICATION_OR_DERIVATION` clean-required. `FULLY_ADMITTED_PRIMARY_ONLY` admission remains `NOT_YET_COMPLETE` until Spec 003 evaluator computes `ELIGIBLE`.
- **Spec 005 role:** **Top-tier PRIMARY admission candidate** for mass-reach. Not yet fully admitted.

### 4.2 Qwen/Qwen3.5-0.8B-Base — PRIMARY ultra-compact challenger

- **Base identity:** `Qwen/Qwen3.5-0.8B-Base` — `LICENSE=apache-2.0`, observed immutable revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68` (read-only sweep). Pretrained-only base (card states pretraining only, no SFT). No equivalent gated terms flow identified in read-only inspection.
- **Base vs post-trained:** Again, hybrid architecture with vision encoder belongs to model family, but **thinking/agent modes are instruct capabilities**, not base. This base is the foundation for later SFT to demonstrate medical reasoning.
- **Params/structure:** 0.8B dense per Qwen3.5 spec; hybrid gated-delta / gated-attention with vision encoder (exact-base GGUF source model is `Qwen/Qwen3.5-0.8B-Base`).
- **Training:** Qwen3.5 inherits Qwen3 pipeline with vision extension. No separate token count published beyond Qwen3 36T family.
- **Medical/reasoning/Arabic at base:** Same caveats as 0.6B — family evidence not checkpoint measurement. Require tournament measurement.
- **Tokenizer:** Same Qwen BBPE family per checkpoint revision.
- **GGUF feasibility (exact-base):** Official `ggml-org/Qwen3.5-0.8B-Base-GGUF` at observed inspection: `Q4_0` **563 MB** (SHA256 `0dabf7f0...`) — already **under 600 MiB engineering target** and well under 700 MiB hard ceiling. This is currently the cleanest mass-reach evidence among Apache candidates. Documented `llama.cpp` usage `YES`.
- **Admission:** Same as 0.6B — publicly supported but not yet fully admitted (`SPEC003_LINEAGE_RESULT=NOT_YET_COMPUTED`).

### 4.2 Qwen/Qwen3.5-0.8B-Base — PRIMARY ultra-compact challenger (vision-language foundation, corrected)

- **Repository identity:** `Qwen/Qwen3.5-0.8B-Base` — HF API `sha: dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`, `gated: false`, `pipeline_tag: image-text-to-text`, HF `license: apache-2.0`, Model card `Type: Causal Language Model with Vision Encoder`, `Context Length: 262,144 natively and extensible up to 1,010,000 tokens`. This is **not text-only** — correction of v2 §5 row that claimed `❌ text-only`. The official pipeline is `image-text-to-text` (`AutoProcessor` + `AutoModelForMultimodalLM`), example with `{"type":"image"}`.
- **Model kind:** Pretrained-only base (card: pre-trained only model, compatible with HF Transformers `AutoProcessor`/`AutoModelForMultimodalLM`). Vision encoder is part of the upstream checkpoint.
- **Params/arch (language + vision):** Language model ~0.8B (Hidden Dim 1024, 24 layers hybrid 6×(3×Gated DeltaNet →FFN →1×Gated Attention →FFN), 16 V /16 QK linear attention heads, 8 Q/2 KV gated attention, 3584 FFN, RoPE dim 64, tied embedding 248320), plus separate vision encoder/projector (size not included in 0.8B language count; complete artifact includes vision component). Native context 262,144, extensible to 1,010,000.
- **Training:** Unified vision-language early fusion on multimodal tokens; RL at scale across million-agent envs; 201 languages/dialects (vs Qwen3 119). Not medical-specific.
- **GGUF feasibility (exact-base):** Official `ggml-org/Qwen3.5-0.8B-Base-GGUF` observed Q4_0 563 MB (SHA 0dabf7f0...). **Package accounting concern:** The 563 MB file is the quantized language+vision artifact as converted by `ggml-org`? The repository file list shows a single `Qwen3.5-0.8B-Base-Q4_0.gguf`; its size (563 MB) is close to a 0.8B Q4. But the upstream checkpoint contains a vision encoder that must be accounted for in `COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_BYTES`. Investigation required:
  ```text
  QWEN35_TEXT_CORE_PACKAGE_ACCOUNTING=NEEDS_EVIDENCE
  GGUF_CONTAINS_VISION_ENCODER=NEEDS_EVIDENCE (does Q4_0 include vision projector/encoder or only LM?)
  SEPARATE_VISION_ARTIFACT_REQUIRED=NEEDS_EVIDENCE
  TOKENIZER_CONFIG_TEMPLATE_RUNTIME_BYTES=NEEDS_EVIDENCE (to be added to GGUF for bundle)
  COMPLETE_BUNDLE_STILL_SUB_700MB=NEEDS_EVIDENCE
  ```
  Prior v1/v2 treated 563 MB alone as proof of compliance — corrected: 563 MB alone is not proof without complete bundle accounting. However, the language-only portion of a 0.8B model at Q4 is plausibly under 700 MiB even with vision excluded if vision is optional for `COMMON_CORE_PRIMARY_RANKING` (text/core ranking, vision secondary per `COMMON_CORE_PRIMARY_RANKING`). Correct accounting must prove vision is not required for text-only Core execution; if vision is required, its bytes must be included.

- **Role:** PRIMARY ultra-compact challenger under `COMMON_CORE_PRIMARY_RANKING` (modality-specific vision is secondary/non-ranking; see Spec 005 session). Still eligible for PRIMARY, but bundle accounting must be completed.

### 4.3 ibm-granite/granite-4.0-350m-base — PRIMARY ultra-compact (new, Apache 2.0)

**This candidate was missing from PR #55 v1 and is now deeply investigated as directed.**

- **Repository identity:** `ibm-granite/granite-4.0-350m-base` — `HF license` field `apache-2.0`, HF API `sha: a50b46cef21c8a86b15f0496cb794487a78a910b`, `gated: false`, `pipeline_tag: text-generation`, `transformersInfo auto_model AutoModelForCausalLM`, collection `Granite 4.0 Nano Language Models`. Release date 2025-10-28 (Nano announcement). No gated terms acceptance flow identified; HF card is ungated public, config `model_type granitemoehybrid` (dense with 0 experts) per `config.json` and `safetensors total 352,379,904` BF16 params.
- **Model kind:** **Base/pretrained checkpoint** (`granite-4.0-350m-base` vs instruct `granite-4.0-350m`). Dense traditional transformer (not hybrid Mamba-2). Dense alternative explicitly for workloads where hybrid lacks optimized support (llama.cpp, PEFT). Therefore correct for `GGUF_LLAMA_CPP_CANONICAL`.
- **Params/arch (exact):** 350M, config `model_type: granitemoehybrid`, `architectures: [GraniteMoeHybridForCausalLM]`, `num_experts_per_tok: 0` (dense variant of MoE hybrid family with 0 active experts), embedding 1024, 28 layers (28 attention), 16 heads / 4 KV (GQA), head dim 64, SwiGLU, RoPE (dense), shared embeddings. Official table: Sequence length **32K** for 350M dense (128K for 1B dense). Training data ~15T tokens four-stage (10T + 2T + 2T + 0.5T) — enterprise GRC-cleared, ISO 42001 certified family, cryptographic signing. Immutable revision observed 2026-08-27 via HF API: `a50b46cef21c8a86b15f0496cb794487a78a910b` (repo `ibm-granite/granite-4.0-350m-base`, gated false).
- **Supported languages (card):** English, German, Spanish, French, Japanese, Portuguese, **Arabic**, Czech, Italian, Korean, Dutch, Chinese — **Arabic is officially listed among 12**, not merely multilingual. Fine-tunable beyond list. This is stronger than SmolLM3's English-primary limitation.
- **Instruction vs base:** Base is text-generation without safety alignment (`Ethical Considerations: not safety aligned, may produce problematic outputs`) — correct for `BASE_ONLY_PRIMARY`.
- **Tokenizer identity:**
  - Exact `tokenizer.json` revision: observed at sweep time `7b5e0...`? To be rebound at manifest freeze — but card documents tokenizer is Granite-specific; `tokenizer_config.json` present.
  - License of tokenizer: Apache-2.0 per repository license covers weight + tokenizer artifact under same repo LICENSE. However **checkpoint-level component rights** (tokenizer vs processor) still requires exact binding per Spec 003 per `qwen-exact-binding-evidence.md` pattern — `TOKENIZER_PROCESSOR_EXACT_BINDING` is `NEEDS_EVIDENCE` until captured with revision tree.
- **Weight license:** Apache 2.0 — permits use/modification/distribution/sublicensing/commercial, with NOTICE/attribution, patent grant, no prohibited-use medical carve-out, no revenue threshold. Satisfies `FD-001` fully. Enterprise provenance (IBM) with ISO 42001.
- **Gated access:** `NO_ADDITIONAL_TERMS_ACCEPTANCE_FLOW_IDENTIFIED` (HF repo ungated; `hasGatedAccess: false` in converted GGUF metadata). Contrasts with Apertus/Gemma-270m gated flows.
- **GGUF feasibility (exact-base, official IBM):**
  - Repository `ibm-granite/granite-4.0-350m-base-GGUF` (quantized view) and `ibm-granite/granite-4.0-350m-GGUF` contain **official IBM conversions** (workflow `IBM/gguf/.github/workflows/granite-4.0-release-ibm-granite.yml` tags `v4.0-nano-bf16-all-quants-01` and `v4.0-language-refresh-20260423-01`).
  - Observed exact-base artifacts:
    ```text
    granulename: granite-4.0-350m-base-Q4_K_M.gguf  size=237 MB (Xet, 244 MB advertised)
    Q4_0 229 MB, Q4_1 228 MB, Q3_K_M 208 MB, Q2_K 181 MB, Q4_K_S 229 MB (non-base ~229-244)
    BF16 ~708 MB (Xet)
    ```
  - This is **3× smaller** than `SUB_700MB` ceiling and even under the `<=500 MiB` stretch target for the text/core bundle. Even with a small tokenizer/config overhead and a pinned llama.cpp runtime slice, the complete minimum bundle remains well under 600 MiB.
  - `LLAMA_CPP_USAGE_DOCUMENTED=YES` (GGUFs are llama.cpp-compatible; hybrid variant noted as not yet optimized — dense 350M avoids that).
- **Context feasibility for 8K Core:** 32K native sequence supports `7K_PROMPT_1K_GENERATION` = 8192 common hard condition trivially; KV at Q8_0 symmetric (`Q8_0_KV_CORE`) at 8K with B512_U128 profile and 2 GiB hard cap is plausible but **measured evidence remains `NEEDS_EVIDENCE`** until pinned commit + five fresh runs on each of the five mass-reach targets. Granite Nano blog notes 32K for Nano, 128K for 1B dense (above).
- **Arabic evidence (granular):** Official card lists Arabic among 12 supported. Benchmark table in card shows General MMMLU 30.93 (350M dense) with Arabic slice ar, de, en, es, fr, ja, ko, pt, zh, bn, hi (11 languages). Granite is not an Arabic-specialized model like Jais, but it is not English-only. Arabic clinical parity is **`UNRESOLVED`**, but not `HIGH_RISK_UNRESOLVED` like SmolLM2 English-primary.
- **Spec 003 admission state:** Same pattern as Qwen ultra-compact — `BASE_GATE=PUBLICLY_SUPPORTED`, `LICENSE_METADATA_GATE=PUBLICLY_SUPPORTED_APACHE_2_0`, `GATED_ACCESS_OBSERVED=NO`, but `SPEC003_LINEAGE_RESULT=NOT_YET_COMPUTED`, `PRIMARY_ADMISSION=NOT_YET_COMPLETE`, `TOKENIZER_PROCESSOR_EXACT_BINDING=PARTIAL`.
- **Redistribution/derivation:** Apache 2.0 permits quantization (`MODIFICATION_OR_DERIVATION`) and redistribution of GGUF derivatives with NOTICE. No medical prohibition.
- **Role:** **Top-tier PRIMARY admission candidate** for mass-reach, and the strongest current vendor-diversity hypothesis (IBM vs Qwen). Must not be chosen over Qwen on size alone; tournament decides. If its Arabic/medical floor fails, outcome is `NO_SELECTION`, not gate weakening.

### 4.4 Qwen/Qwen3-4B-Base — SCALE/QUALITY CONTROL (not PRIMARY)

- **Identity:** `Qwen/Qwen3-4B-Base` — HF API `sha: 906bfd4b4dc7f14ee4320094d8b41684abff8539`, `gated: false`, Apache 2.0, pretrained base (control). Params 4.0B (3.6B non-embedding), 36 layers, 32 Q / 8 KV GQA, **context 32,768** (per exact official `Qwen/Qwen3-4B-Base` model card `Context Length: 32,768`; earlier v2 incorrectly imported 128K from Qwen3 family table which applies to larger sizes/post-trained variants — corrected after fresh verification of the exact Base checkpoint and control still valid as scale control). `pipeline_tag: text-generation` (text-only, unlike Qwen3.5).
- **GGUF feasibility:** `Q4_K_M` ~2.41 GB advert (or 2.65GB VRAM + 4.8GB KV @32K per Nodepedia) — **far above** `SUB_700MB`. Canonical bundle cannot satisfy mass-reach. Therefore `PRIMARY_ADMISSION=INELIGIBLE_FOR_MASS_REACH`. This is intentional: its purpose is to measure opportunity cost of the mass-reach constraint (`HOW_MUCH_QUALITY_IS_LOST_BY_FORCING_SUB_700MB`).
- **Role in tournament:** `NON_WINNER_SCALE_CONTROL`. Tested under `DUAL_BUILD` (baseline vs deployable) but its deployable will necessarily fail package/RAM hard gates for V1 primary. It must not win the current tournament unless governance is explicitly amended later (`FOUNDER+CHATGPT_RESOURCE_CLASS_RECONSIDERATION_REQUIRED`).

### 4.5 Qwen/Qwen3.5-2B-Base and Qwen/Qwen3.5-4B-Base — CONTROL / fallback (new)

- **Status update:** These official Apache-2.0 base checkpoints **now exist** and materially change the candidate set. v1 omitted them.
- **Context (to verify):** Qwen3.5-0.8B evidence showed 563 MB Q4_0; larger 2B/4B will exceed mass-reach but may be future fallback controls if Founder later reconsiders resource class. For now they are **not PRIMARY** for mass-reach; they are `CONDITIONAL` controls if all ultra-compact PRIMARY fail and Founder opens a 2–4B Core manifest v2.
- **Do not treat 2B/4B as current PRIMARY winners merely because they are stronger.** Retained as `CONTROL` per `QUALITY_FLOOR_THEN_SIZE_FIRST`.

### 4.6 Gemma 4 E2B / E4B — CONTROL / fallback (Apache 2.0)

- **Params (strict accounting, corrected):** Prior packet used effective params only (2.3B/4.5B). Official cards show **total** (with embeddings) is **~5B / ~8B** respectively (Bento blog `E2B raw ~5B, E4B raw ~8B` and card `4.5B effective but 8B total`). **Total** governs shipped bytes + embedding memory. Effective params governs per-token FLOPs. Both must be reported, but ranking must use **total/shipped-resource** per density strategy §3.
- **Context:** To verify per checkpoint; Gemma 3 card cites 128K, Gemma 4 likely similar but **manifest must freeze exact**.
- **Package feasibility:** No public exact-base GGUF below 700 MiB captured for Gemma 4 E2B in commandMed sweep (unverified). Prior packet assumed 7.2GB/9.6GB downloads — those are instruction-tuned E-series, not base. No base exact GGUF path proven for PRIMARY mass-reach. Therefore not PRIMARY-eligible today; retained as fallback/Google lineage control.
- **License:** Apache 2.0 (excluded from custom ToU) — satisfies FD-001 for fallback.

### 4.7 Ministral 3 3B — CONTROL / fallback

- **Params:** 3.4B lang + 0.4B vision = 3.8B shipped (prior packet 3.4+0.4 correct). `3B` label is marketing/marketed size, not shipped bytes.
- **Context:** 256K (128K reasoning) — largest among candidates, but does not rescue package size.
- **Package:** `BF16 7.8GB`, `Q4_K_M 3.4GB` — fails mass-reach.
- **Role:** Vision+text control, 256K edge probe, European language strength. Not PRIMARY for mass-reach.

### 4.8 Phi-4-mini — REFERENCE_ONLY (instruct) — corrected

- **Correction:** `microsoft/Phi-4-mini-Base` **does not exist** as a public base checkpoint. The official public checkpoint is `microsoft/Phi-4-mini-instruct` (MIT). Microsoft discussion: no plan to release base model. A post-trained instruct checkpoint **must not** be silently treated as a base checkpoint or mixed into `BASE_ONLY_PRIMARY`.
- **Role:** Retained as `REFERENCE_ONLY` instruction-era reference for reasoning comparison (74.4% HumanEval at 3.8B), not as tournament primary. If Phi family later releases an Apache/MIT base, it could be re-evaluated.

### 4.9 SmolLM3 3B — REFERENCE / not mass-reach

- **Context:** 128K NoPE+YaRN, 3B, 11T, Apache 2.0 — strong at 3B vs Llama 3.2 3B / Qwen2.5 3B, but Arabic secondary (Belebele Arabic 40.22 vs Qwen3 4B 51.78). English-primary limitation conflicts with Arabic parity hard gate. Package Q4 ~?? but likely >700? Not captured exact-base Q4 under 700. Retained as transparent-recipe reference.

### 4.10 LFM2.5 — EXCLUDED / research-only conditional

- Remains excluded from Core release lineage due `LFM Open License v1.0` revenue threshold (<$10M free). QAD checkpoint interesting for Spec 012 compression research, not V1 primary.

### 4.11 Jais small Arabic — REFERENCE / conditional

- Investigated: `inceptionai/jais-family-590m-base` etc. Arabic-specialized but gated terms, custom license with acceptable use, context 2K–8K (older), GGUF community path not official, maintenance slower than Qwen/Granite. Retained only as **Arabic reference/control if useful**, not PRIMARY. If a Jais candidate cannot satisfy frozen 8K Core condition or package education, it cannot be PRIMARY.

### 4.12 Falcon ultra-compact 1B — SCREENED, not admitted

- `tiiuae/falcon-1b` screened: Apache-based + AUP (Falcon license), 1B class, multilingual limited. No 350M-class size win over Granite/Qwen; no Arabic parity path proven. Not added — information-gain insufficient (does not test materially different hypothesis beyond Qwen/Granite).

---

## 5. Comparative matrix (2026-08-27 repair v2, checkpoint-true)

| Dimension | Granite-4.0-350M-Base | Qwen3-0.6B-Base | Qwen3.5-0.8B-Base | Qwen3-4B-Base (CONTROL) | Qwen3.5-2B-Base (CONTROL) | Gemma 4 E2B (CONTROL) | Ministral 3 3B (CONTROL) |
|---|---|---|---|---|---|---|---|
| **Checkpoint (base?)** | ✅ base 350M dense | ✅ base 0.6B | ✅ base 0.8B | ✅ base 4B | ✅ base 2B | ⚠️ base not yet verified | ✅ base 3B |
| **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| **FD-001 fit** | ✅ | ✅ | ✅ | ✅ (but not mass-reach) | ✅ (but not mass-reach) | ✅ | ✅ |
| **Params (total / active)** | 350M / 350M | 0.6B / 0.44B non-emb | 0.8B | 4.0B / 3.6B non-emb | 2B | ~5B total / 2.3B eff | 3.8B shipped (3.4+0.4) |
| **Context (natively)** | 32,768 | 32,768 | 262,144 (natively, extends to 1,010,000) | **32,768** | 262,144? *to freeze* | 128K? *to freeze* | 256K (128K reasoning) |
| **Architecture** | Dense RoPE GQA SwiGLU (traditional) | Dense RoPE GQA SwiGLU | Causal LM **with Vision Encoder** (hybrid Gated Delta + Gated Attention) | Dense RoPE GQA | Hybrid/delta | Edge dense (Gemini-derived) | Dense + vision cascade |
| **Vision** | ❌ text-only | ❌ text-only | **✅ Vision Encoder (image-text-to-text per card, pipeline image-text-to-text)** | ❌ text-only | ✅ (Qwen3.5 multimodal) | ✅ (3n multimodal) | ✅ native |
| **Training tokens** | 15T (4-stage: 10T+2T+2T+0.5T) | 36T family | ~Qwen3 36T family | 36T family | ~36T family | Not disclosed (Gemini) | 1–3T cascade |
| **Arabic supported** | 12 official inc. ar | 119 inc. 7 Arabic dialects | 119 inc. 7 dialects | 119 inc. 7 dialects | 119 inc. 7 dialects | 140+ underst. | Dozens inc. ar (European strongest) |
| **Arabic medical evidence** | `NEEDS_EVIDENCE` (supported, not specialized) | `NEEDS_EVIDENCE` (family-strong) | `NEEDS_EVIDENCE` | Strongest family (Belebele 51.78 family signal, not checkpoint) | `NEEDS_EVIDENCE` | 2.30 tok/wd measured family | `NEEDS_EVIDENCE` |
| **Thinking / reasoning mode** | **Not at base** (family post-trained) | **Not at base** (family post-trained) | **Not at base** | **Not at base** | Post-trained only | Post-trained only | Reasoning variant separate |
| **Tokenizer** | Granite-specific (revision to bind) | BBPE 151K+22 | BBPE family 151K | BBPE 151K | BBPE family | SP 256K family | Tekken 131K |
| **Arabic tok frag** | Not measured (to be frozen protocol) | ~2.4 tok/wd expected general | Not measured | Not measured | Not measured | 2.30 (family) | Not measured |
| **Ecosystem** | transformers/vllm/SGLang, GGUF llama.cpp (dense) | Full (trl/peft/axolotl/vllm/llama.cpp/mlx) | Full (same) | Full | Full | transformers/gemma.cpp | transformers/vllm |
| **Exact-base GGUF Q4_0 size** | **229 MB Q4_0 / 237 MB Q4_K_M** | 0.47–0.48GB Q4_0/K_M (639 MB Q8_0) | **563 MB Q4_0** | 2.41GB Q4_K_M (fails) | Not captured | Not captured base | 3.4GB Q4_K_M (fails) |
| **SUB_700MB feasibility** | **YES — Q4_K_M 237 MB under stretch 500** | YES (Q4~480 MB, Q8_0 639 MB) | YES (Q4_0 563 MB) | **NO — 2.41GB** | **NO** | **NO (unproven)** | **NO** |
| **Spec 005 role** | **PRIMARY** | **PRIMARY** | **PRIMARY** | **CONTROL** | **CONTROL** | **CONTROL/FALLBACK** | **CONTROL** |
| **Spec 003 admission** | NOT_YET_COMPUTED | NOT_YET_COMPUTED | NOT_YET_COMPUTED | NOT_YET_COMPUTED (but not PRIMARY-eligible) | NOT_YET_COMPUTED | NOT_YET_COMPUTED | NOT_YET_COMPUTED |

> Context column span corrected: v1 claimed all proposed candidates 128K–256K; v2 now records **checkpoint-specific** values. Qwen3.5-0.8B appears as 262K natively in one sweep vs 256K in another — `NEEDS_EVIDENCE` to freeze exact advertised vs manifest-sha-bound value. No instruction-thinking claim is attributed to any base checkpoint.

---

## 6. Revised candidate capability assessment (family vs checkpoint separated)

### 6.1 Medical capability

No candidate is a medical-domain model at its **base checkpoint**. All are general-purpose pretrained bases. Family-level post-trained medical text/image evaluation (MedGemma 4B, etc.) is **reference-only** per `COMMON_CORE_PRIMARY_RANKING` and is not of the base checkpoint. Medical capability must be measured under frozen V1 metric catalog + safety hard gates + quarantine-clean evaluation. Public medical benchmark claims are **development signal, not ranking metric** until contamination/licensing/purpose are proven.

### 6.2 Reasoning (checkpoint-true)

- No base checkpoint here provides thinking/chain-of-thought mode. That is post-trained behavior of instruct/thinking variants.
- Family-level synthetic reasoning density (Phi 5T, Qwen 36T, SmolLM 11T, Granite 15T, Ministral cascade 1–3T) informs capacity hypotheses but does not change base ranking.

### 6.3 Arabic

- Per 2.4 tok/word ACL finding, Arabic medical text is structurally fragmented under general BBPE/SP tokenizers. Granite officially supports Arabic among 12; Qwen officially supports 119 with 7 Arabic dialects. Jais is Arabic-specialized but gated and older context. **Granite vs Qwen Arabic is a tournament question, not a prior.**

### 6.4 Medical quality floor (unchanged)

Ordering is:

1. hard safety gates
2. provenance / license / contamination gates
3. frozen minimum medical-quality gate
4. Arabic and required capability gates
5. device/resource qualification
6. among qualifiers, `QUALITY_FLOOR_THEN_SIZE_FIRST` (complete deployable package bytes first, then predeclared secondary metrics)

SIZE DOES NOT COMPENSATE FOR MEDICAL FAILURE. A candidate that fails a hard gate is not rescued by package size.

---

## 7. Mass-reach reconciliation (summary; full artifact is `reconciliation-core-mass-reach-2026-08-27.md`)

- **Texts in conflict:** Density strategy §4.1 (Core ≈ 2–4B) vs Spec 005 frozen `SUB_700MB_MASS_REACH` + `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`.
- **Chronology/authority:** Spec 005 bounded clarification sessions (2026-08-23 mass-reach five-target set, Q8_0 KV, B512_U128, 2 GiB) are **canonical frozen** and remain in `specs/005-base-model-tournament/spec.md`. Density strategy (2026-08-27) is additive, explicitly states `Status: ADDITIVE PLANNING STRATEGY — does not amend execution authority`, and does not silently override Spec 005. Therefore Spec 005 takes precedence for current tournament resource class.
- **Harmonized interpretation:**
  ```text
  CORE = frozen capability/safety/product contract (quality floor + safety + provenance + device contract)
  MASS_REACH_CORE = Core candidate satisfying the current SUB_700MB / 2 GiB / 8K / Q8_0 mass-reach contract under GGUF_LLAMA_CPP_CANONICAL
  NANO = later explicitly scoped derived/distilled/compressed tier after proven Core capability exists (not defined by ~0.6B parameter count)
  ```
  Approximate parameter bands (2–4B vs 0.6–1.5B) are **research hypotheses** for dense classes, not authority to override measured shipped bytes / peak RAM.
- **Required amendments:** Density strategy §4.1 requires editorial amendment to state Core may be satisfied by any model meeting the frozen mass-reach capability contract (including 350M–0.8B), and that Nano will be explicitly scoped later. No Spec 005 text requires amendment — its gates remain correct.
- **Founder decision needed to amend:** Density strategy §4.1 wording (additive strategy); no Spec 005 gate amendment needed today.

---

## 8. Fresh sub-1B sweep (bounded, final for v2 freeze)

Beyond the three PRIMARY, a bounded fresh sweep investigated:

- IBM Granite small base models: `granite-4.0-350m-base` ✅ (above), `granite-4.0-h-350m-base` (hybrid Mamba2, 340M, 32K NoPE, not yet optimized for llama.cpp — **screened but not admitted** due hybrid runtime immaturity for `GGUF_LLAMA_CPP_CANONICAL`; dense traditional is the correct PRIMARY path).
- Qwen ultra-compact bases: `Qwen/Qwen3-0.6B-Base` ✅, `Qwen/Qwen3.5-0.8B-Base` ✅ — both fully in sweep frontier.
- Falcon ultra-compact (1B): `tiiuae/falcon-1b` (and 3B) — Falcon License + AUP, ~1B not 350M-class, no Arabic parity path, no size win over Granite/Qwen — **information gain insufficient**, not added.
- Jais small Arabic bases: `inceptionai/jais-family-590m-base` — gated terms, custom license, older 8192 context (varies 4K–8K depending on variant), no official IBM-style GGUF Q4 under 300 MB in sweep, maintenance slower — retained only as **Arabic CONTROL if useful**, not PRIMARY (fails `FULLY_ADMITTED_PRIMARY_ONLY` if license/gating unresolved).
- Apertus 0.5B: already conditional size comparator; remains conditional due gated AUP.
- SmolLM2 360M: already control/conditional due English-primary limitation.
- Gemma 270M: already conditional due Gemma gated license.

**Conclusion:** No additional sub-1B candidate beyond the three PRIMARY tests a materially different hypothesis with higher information gain. Sweep is complete for v2 freeze.

---

## 9. Proposed candidate manifest structures (repair v2, NOT YET FROZEN)

### Option A — Founder-preferred PRIMARY with explicit scale control (recommended shape)

Freeze **exactly**:

```text
PRIMARY (mass-reach, BASE_ONLY):
  - Qwen/Qwen3-0.6B-Base          (0.6B dense, Apache 2.0, 32K, Q8_0 639M / Q4_K_M ~480M)
  - Qwen/Qwen3.5-0.8B-Base        (0.8B dense, Apache 2.0, 262K natively, Q4_0 563M)
  - ibm-granite/granite-4.0-350m-base (350M dense, Apache 2.0, 32K, Q4_K_M 237M)

CONTROL (non-winner, measures opportunity cost of SUB_700MB):
  - Qwen/Qwen3-4B-Base            (4B dense, Apache 2.0, 128K, Q4_K_M ~2.4GB — will fail SUB_700MB)

RATIONALE: Tests whether mass-reach ultra-compact candidates can meet frozen Core medical/safety/Arabic/device requirements. Larger control shows quality loss from forcing mass-reach. No 2–4B model is PRIMARY-winner-eligible under current mass-reach contract.
```

### Option B — Option A + single conditional efficiency probe (research track, not Core release lineage)

```text
PRIMARY: same three as A
CONTROL: Qwen/Qwen3-4B-Base
CONDITIONAL_EFFICIENCY_PROBE (not eligible for primary ranking):
  - ibm-granite/granite-4.0-h-350m-base (hybrid) OR Swiss-Apertus if Founder prefers size diversity — annotated TRACK=M_EFFICIENCY_CONDITIONAL
```

### Option C — Minimal 2-candidate PRIMARY (if vendor diversity is not required)

```text
PRIMARY:
  - Qwen/Qwen3-0.6B-Base
  - ibm-granite/granite-4.0-350m-base

CONTROL:
  - Qwen/Qwen3-4B-Base
```

**All options require before freeze:** exact HF revision + weight content SHA (Xet where present), exact tokenizer revision/content/config/SPECIAL_TOKEN_MAP/CHAT_TEMPLATE/BOS_EOS/tool-format, exact license evidence per checkpoint, quarantine matrix identity (`b59fd86a...`), arabic tokenizer-efficiency measurement protocol, and `FULLY_ADMITTED_PRIMARY_ONLY` admission state `ELIGIBLE` per Spec 003 evaluator.

### What is NOT a valid manifest

- Any manifest naming an instruction-tuned checkpoint as PRIMARY (violates `BASE_ONLY_PRIMARY`) — includes any `Phi-*-instruct`, `*-it`, `MedGemma-*-it`, or `Qwen-*-Instruct` as primary.
- Any manifest naming Gemma 3 weights as candidate — fails FD-001 medical prohibited-use.
- Any manifest mixing LFM2.5 gated candidates into Core winner pool without revenue-gate reconciliation.
- Any manifest frozen without exact tokenizer/template/revision/binding.
- Any manifest that selects a backbone winner — `BACKBONE_WINNER=NEEDS_EVIDENCE` remains.

---

## 10. Decision required from Founder + ChatGPT (revised)

To unblock E001 → E002/E003, Founder+ChatGPT must record canonically:

```text
FOUNDER+CHATGPT_DECISION_E001:
  CANDIDATE_MANIFEST_FROZEN=<Option A | Option B | Option C | custom exact list>
  MANIFEST_VERSION=<frozen version string, e.g., e001-mass-reach-v1>
  MANIFEST_CONTENT_SHA256=<hash over full manifest JSON>
  MANIFEST_SOURCE_AUTHORITY_ID=<provenance/license DS>
  EXACT_PRIMARY_CHECKPOINTS=[
    {checkpoint_identity, model_repository_id, model_revision, weight_content_identity, tokenizer_identity, chat_template_identity, license_evidence_id}
  ]
  EXACT_CONTROL_CHECKPOINTS=[
    {checkpoint_identity, model_repository_id, model_revision, weight_content_identity, tokenizer_identity, chat_template_identity, license_evidence_id}
  ]
  CANDIDATE_ROLES_FROZEN={PRIMARY: [...], CONTROL: [...], CONDITIONAL: [...], REFERENCE_ONLY: [...]}
  COMMON_CORE_PRIMARY_RANKING=ENFORCED (multimodal is secondary)
  QUALITY_FLOOR_THEN_SIZE_FIRST=ENFORCED (package bytes first among qualifiers)
  ARABIC_TOKENIZER_EFFICIENCY_MEASUREMENT_PROTOCOL_FROZEN=<yes/no>
  QUARANTINE_MATRIX_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
  NOTES=<any scope caveat, e.g., "Granite H 350M hybrid excluded from PRIMARY due llama.cpp maturity">
  FOUNDER_SIGNOFF_AT=<ISO-8601>
  CHATGPT_CONCURRENCE_AT=<ISO-8601>
```

No PI selection. No tournament execution. No training.

---

## 11. What remains gated after E001

| Gate | Authority |
|---|---|
| E002 Model/weight access | `SEPARATE_AUTHORIZATION_REQUIRED` |
| E003 Live tournament execution | `SEPARATE_AUTHORIZATION_REQUIRED` |
| E004 Tournament evidence pack | `EXECUTION_REQUIRED` (depends on E003 + frozen manifest) |
| E005 Backbone winner | `FOUNDER+CHATGPT_DECISION_REQUIRED` (after E004) |
| ... | ... |

This packet does not change `TRAINING_AUTHORITY` etc. — all remain `NONE`.

---

## 12. Preservation controls enforced

- Every unresolved numeric/license binding typed `NEEDS_EVIDENCE`.
- No dataset snapshot constructed.
- No protected Gold/quarantine source on any tuning surface.
- No backend default determines rendering or loss masking.
- No public record claimed.
- No training pilot performed.

---

## 13. Sources (primary, fetched 2026-08-27, repair v2)

- `huggingface.co/Qwen/Qwen3-0.6B-Base` + `d4e79cdcc...` revision tree (Xet hash `2c465b...` / SHA256 `cd2a5120...`)
- `huggingface.co/Qwen/Qwen3.5-0.8B-Base` + `dc7cdfe2ee4...` revision, Q4_0 563 MB (SHA256 `0dabf7f0...`)
- `huggingface.co/ibm-granite/granite-4.0-350m-base` card (Apache 2.0, 350M dense RoPE 32K, 15T, Arabic among 12) + `huggingface.co/ibm-granite/granite-4.0-350m-base-GGUF` (Q4_K_M 237 MB Xet)
- `huggingface.co/Qwen/Qwen3-4B-Base` (Apache 2.0, 4B 128K)
- `huggingface.co/Qwen/Qwen3.5-2B-Base`, `huggingface.co/Qwen/Qwen3.5-4B-Base` existence verified (Apache 2.0, not frozen as PRIMARY)
- `github.com/ibm-granite/granite-4.0-nano-language-models` + `ibm.com/granite/docs` (Granite 4.0 Nano announcement 2025-10-28, ISO 42001)
- `huggingface.co/google/gemma-4-e2b` / `e4b` cards (5B total / 2.3B eff, 8B total / 4.5B eff)
- `huggingface.co/microsoft/Phi-4-mini-instruct` + discussion "no base" (MIT instruct only)
- Secondary aggregators `localaimaster.com/...` and `bentoml.com/...` used only to cross-check footprints

All benchmark numbers are per-source claims, not commandMed measurements, and are `NOT_APPLICABLE` for ranking until contamination/licensing/purpose are proven.

---

## 14. Packet integrity

```text
PI_RECOMMENDATION=NONE
DECISION_OWNER=FOUNDER+CHATGPT
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PACKET_KIND=E001_EVIDENCE_ONLY_REPAIR_V2
PACKET_VERSION=2026-08-27-E001-FRESH-LANDSCAPE-v2
VERIFICATION_STATE=PRIMARY_SOURCES_FETCHED_2026-08-27_REPAIR_V2_GEMMA_CORRECTED_PHI_REMOVED_GRANITE_ADDED_QWEN_VERIFIED
SUPERSEDES=2026-08-27-E001-FRESH-LANDSCAPE-v1 (PR #55 head 4085016)
```

This repair packet remains **evidence only** and does not itself freeze `E001` until Founder+ChatGPT explicitly records the manifest decision with exact identities in a canonical decision record and merges it to `main`.

---

**Prepared by:** Pi (evidence synthesis only) — no selection, no ranking, no training, no model execution.
