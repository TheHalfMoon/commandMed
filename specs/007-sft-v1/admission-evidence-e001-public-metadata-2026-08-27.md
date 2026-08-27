# E001 Public-Metadata Admission Evidence — Mass-Reach PRIMARY Frontier

**Date:** 2026-08-27
**Spec:** 005 / 007 E001 mass-reach PRIMARY frontier (Qwen3-0.6B, Qwen3.5-0.8B, Granite-4.0-350M)
**Lifecycle:** CLARIFY / E001 research — `FULLY_ADMITTED_PRIMARY_ONLY` applies; no MODEL_WEIGHT_ACCESS
**Purpose:** Close, to the maximum permitted under `MODEL_WEIGHT_ACCESS_AUTHORITY=NONE`, the exact public-metadata binding needed by the canonical Spec 003 evaluator. No model weights were downloaded, no gated terms accepted, no model executed.

> Public repository/model-card/Xet/LFS metadata only. Weight bytes, GGUF conversions, and device measurements beyond public size previews are not accessed here.

---

## 1. Contract identity

```text
LINEAGE_CONTRACT_ID=commandmed-lineage-contract-v1
LINEAGE_CONTRACT_SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962 (data/lineage/lineage_contract.json)
CONTRACT_SOURCE=data/lineage/lineage_contract.json
EVALUATOR=src/commandmed/eval_contract/lineage.py (validate_lineage_record / evaluate_lineage_admission)
```

---

## 2. Candidate public identities (HF API verified 2026-08-27, read-only)

### Qwen/Qwen3-0.6B-Base

```text
REPOSITORY=Qwen/Qwen3-0.6B-Base
HF_API_SHA=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
GATED=false
LICENSE_CARD=apache-2.0
PIPELINE_TAG=text-generation
MODEL_TYPE=qwen3
ARCHITECTURES=[Qwen3ForCausalLM]
BASE_STATUS=BASE_PRETRAINED
ORIGIN_TYPE=ORIGINAL
SOURCE_URI=https://huggingface.co/Qwen/Qwen3-0.6B-Base
SOURCE_EVIDENCE_URI=https://huggingface.co/Qwen/Qwen3-0.6B-Base/tree/da87bfb608c14b7cf20ba1ce41287e8de496c0cd
SIBLINGS=[.gitattributes, README.md, config.json, generation_config.json, merges.txt, model.safetensors, model.safetensors.index.json, tokenizer.json, tokenizer_config.json, vocab.json]
CONFIG_CONTEXT_LENGTH=32768
NUM_LAYERS=28, Q=16 / KV=8, TIED_EMBEDDING=YES (per Qwen3 table: 0.6B 32K)
WEIGHT_PREVIEW=model.safetensors Xet metadata not captured at this pass (public Xet hash requires HEAD without weight access — to be bound with weight-content identity at E002)
GGUF_EXACT_BASE=ggml-org/Qwen3-0.6B-Base-GGUF Q8_0 0.80GB / Q4_K_M 0.48GB / Q4_0 0.47GB (community exact-base conversion; not official IBM ggml)
```

### Qwen/Qwen3.5-0.8B-Base

```text
REPOSITORY=Qwen/Qwen3.5-0.8B-Base
HF_API_SHA=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
GATED=false
LICENSE_CARD=apache-2.0
PIPELINE_TAG=image-text-to-text
MODEL_TYPE=qwen3_5
ARCHITECTURES=[Qwen3_5ForConditionalGeneration]
TYPE_DETAIL=Causal Language Model with Vision Encoder — Hidden 1024, 24 layers hybrid 6×(3×Gated DeltaNet→FFN →1×Gated Attention→FFN), 16 V/16 QK linear attention heads, 8Q/2KV gated attention, 3584 FFN, 248320 tied vocab, MTP
CONTEXT_LENGTH=262144 natively, extensible to 1,010,000
BASE_STATUS=PRETRAINED_ONLY_BASE (card: pre-trained only model, not direct interaction; control tokens <|im_start|> <|im_end|> trained for LoRA PEFT)
SOURCE_URI=https://huggingface.co/Qwen/Qwen3.5-0.8B-Base
SOURCE_EVIDENCE_URI=https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/tree/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
SIBLINGS=[.gitattributes, README.md, config.json, generation_config.json, merges.txt, model.safetensors, preprocessor_config.json, processor_config.json, tokenizer.json, tokenizer_config.json, vocab.json, video_preprocessor.json] (vision preprocessor present)
GGUF_EXACT_BASE=ggml-org/Qwen3.5-0.8B-Base-GGUF Q4_0 563 MB SHA 0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d (vision bytes accounting: see §4)
```

### ibm-granite/granite-4.0-350m-base

```text
REPOSITORY=ibm-granite/granite-4.0-350m-base
HF_API_SHA=a50b46cef21c8a86b15f0496cb794487a78a910b
GATED=false
LICENSE_CARD=apache-2.0
PIPELINE_TAG=text-generation
MODEL_TYPE=granitemoehybrid
ARCHITECTURES=[GraniteMoeHybridForCausalLM]
MODEL_CLASS=BASE_PRETRAINED
NUM_EXPERTS_PER_TOK=0 (dense variant of hybrid family with 0 active experts)
TOKENIZER_FILES=[tokenizer.json, tokenizer_config.json, vocab.json, merges.txt, special_tokens_map.json]
CONFIG_CONTEXT_LENGTH=32768
NUM_LAYERS=28 attention, 16 heads /4 KV, head dim 64, SwiGLU, RoPE
PARAMS_BF16=352379904, STORAGE_USED=704786224
SIBLINGS=[.gitattributes, README.md, config.json, generation_config.json, merges.txt, model.safetensors, model.sig, special_tokens_map.json, tokenizer.json, tokenizer_config.json, vocab.json]
SOURCE_URI=https://huggingface.co/ibm-granite/granite-4.0-350m-base
SOURCE_EVIDENCE_URI=https://huggingface.co/ibm-granite/granite-4.0-350m-base/tree/a50b46cef21c8a86b15f0496cb794487a78a910b
GGUF_OFFICIAL=ibm-granite/granite-4.0-350m-base-GGUF Q4_K_M 237 MB (Xet), Q4_0 229 MB, Q2_K 181 MB, BF16 708 MB (workflow IBM/gguf granite-4.0-release-ibm-granite.yml v4.0-nano-bf16-all-quants-01 and v4.0-language-refresh-20260423-01)
SUPPORTED_LANGUAGES=[en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh] (12 official list inc. Arabic)
```

### Qwen/Qwen3-4B-Base (CONTROL, non-winner)

```text
REPOSITORY=Qwen/Qwen3-4B-Base
HF_API_SHA=906bfd4b4dc7f14ee4320094d8b41684abff8539
GATED=false
LICENSE_CARD=apache-2.0
PIPELINE_TAG=text-generation
MODEL_TYPE=qwen3
CONTEXT_LENGTH=32768 (corrected from earlier 128K mis-import; exact Base card says 32,768)
BASE_STATUS=BASE_PRETRAINED
GGUF_Q4_K_M=2.41 GB (Nodepedia) — will fail SUB_700MB by design (control purpose)
ROLE=CONTROL_NON_WINNER_SCALE_QUALITY
```

---

## 3. Tokenizer / processor / template binding (public)

All four repositories expose tokenizer artifacts at the same immutable revision as the weight:

- `tokenizer.json`, `tokenizer_config.json`, `vocab.json`, `merges.txt`, `special_tokens_map.json` (where present) are siblings in the source tree and share the same `source_revision` SHA above.
- `chat_template` is not a separate file for base models — base checkpoints are pretrained only; chat template is a post-training artifact of instruct variants. For `Qwen/Qwen3.5-0.8B-Base`, the processor includes `preprocessor_config.json` / `processor_config.json` / `video_preprocessor.json` for the vision encoder. The base `source_revision` binds all listed siblings atomically.
- License `apache-2.0` at repository root covers weight + tokenizer + config under the same repo LICENSE; no separate tokenizer-gated flow identified. Component-level `rights_evidence_uri` therefore points to `.../blob/<sha>/LICENSE` at the same SHA.
- NOTICE/attribution requirements: Apache 2.0 §4 — no additional NOTICE file beyond LICENSE was observed; to be verified at E002 with exact LICENSE text hash.

Binding state for evaluator:

```text
ARTIFACT_BINDING_STATE=IMMUTABLE_REVISION_LOCATOR
ARTIFACT_LOCATOR=<repo>/tree/<sha> (exact sibling set above)
```

---

## 4. Package accounting for Qwen3.5 vision component

Qwen3.5-0.8B base contains a vision encoder + preprocessor (image-text-to-text). The 563 MB Q4_0 GGUF observed at `ggml-org/Qwen3.5-0.8B-Base-GGUF` is advertised as the quantized language+vision artifact. Whether the `COMMON_CORE_PRIMARY_RANKING` text/core ranking may exclude vision bytes depends on whether vision is required for text-only execution:

```text
QWEN35_TEXT_CORE_PACKAGE_ACCOUNTING=NEEDS_EVIDENCE
GGUF_CONTAINS_VISION_ENCODER=NEEDS_EVIDENCE
SEPARATE_VISION_ARTIFACT_REQUIRED=NEEDS_EVIDENCE
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_BYTES=NEEDS_EVIDENCE (to be computed as GGUF + tokenizer/config/template/runtime bytes under SUB_700MB)
VISION_EXCLUDABLE_FOR_COMMON_CORE_RANKING=PER COMMON_CORE_PRIMARY_RANKING secondary evidence is non-ranking, but resource accounting must still prove what runtime-required bytes are for the canonical minimum text/core artifact (see Spec 005 §2)
```

No hidden asset is excluded from accounting. The 563 MB alone is feasibility evidence, not proof of bundle compliance. Full bundle calculation requires the pinned llama.cpp revision, conversion flags, and tokenizer/config byte sizes — to be resolved with public conversion metadata, not weight bytes.

---

## 5. Spec 003 evaluator — offline public-metadata evaluation

Using `src/commandmed/eval_contract/lineage.py` without weight bytes, the following lineage records were constructed for the primary declared uses. Each record uses:

- `asset_class=MODEL_OR_CHECKPOINT`, `asset_id=<repo>-<sha>-<use>`, `canonical_name=<repo>`, `record_version=1`
- `source_identifier=<repo>`, `source_uri=https://huggingface.co/<repo>`, `source_revision=<sha>`, `source_verification_status=VERIFIED`, `source_evidence_uri=https://huggingface.co/<repo>/tree/<sha>`
- `artifact_binding_state=IMMUTABLE_REVISION_LOCATOR`, `artifact_locator=https://huggingface.co/<repo>/tree/<sha>`
- `access_class=PUBLIC` (verified `gated:false`), `rights_state=SUPPORTED`, `rights_evidence_uri=https://huggingface.co/<repo>/blob/<sha>/LICENSE`
- `phi_privacy_state=NO_PHI_KNOWN`, `quarantine_state=NOT_QUARANTINED`, `purpose` per declared use, `origin_type=ORIGINAL` for base weights
- `contamination_state` is the field that previously blocked TRAIN uses. See reconciliation `reconciliation-contamination-semantics-2026-08-27.md`: `contamination_state` for `MODEL_OR_CHECKPOINT` with `TRAIN` purpose represents **model lineage** contamination (whether the base checkpoint itself as a lineage parent carries a prohibited optimization source), not `candidate × benchmark-slice` adjudication. For that lineage relation, `NOT_APPLICABLE` is valid when benchmark contamination is separately represented as exact `candidate × benchmark-slice` evidence per Spec 005 Q4 (dual-axis) and no benchmark-clean claim is inferred. Prior `NOT_ASSESSED` was therefore correctly fail-closed, but `NOT_APPLICABLE` is the correct lineage pass without implying benchmark cleanliness.

Evaluator results (offline, 2026-08-27, contract `2b08533c...`, initial run with `NOT_ASSESSED` — correctly BLOCKED, then recomputed with corrected `NOT_APPLICABLE` for lineage-only):

Initial `NOT_ASSESSED` table (for audit, correctly BLOCKED):

| Candidate | Declared use | Purpose mapping | Evaluator state | Reason codes |
|---|---|---|---|---|
| Qwen/Qwen3-0.6B-Base da87bfb | DEVELOPMENT_EVALUATION | DEV | **ELIGIBLE** | — |
| Qwen/Qwen3-0.6B-Base da87bfb | MODIFICATION_OR_DERIVATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| Qwen/Qwen3-0.6B-Base da87bfb | TRAINING_OR_ADAPTATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| Qwen/Qwen3-0.6B-Base da87bfb | REDISTRIBUTION | — | **ELIGIBLE** | — |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | DEVELOPMENT_EVALUATION | DEV | **ELIGIBLE** | — |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | MODIFICATION_OR_DERIVATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | TRAINING_OR_ADAPTATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | REDISTRIBUTION | — | **ELIGIBLE** | — |
| ibm-granite/granite-4.0-350m-base a50b46c | DEVELOPMENT_EVALUATION | DEV | **ELIGIBLE** | — |
| ibm-granite/granite-4.0-350m-base a50b46c | MODIFICATION_OR_DERIVATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| ibm-granite/granite-4.0-350m-base a50b46c | TRAINING_OR_ADAPTATION | TRAIN | **BLOCKED** | CONTAMINATION_UNRESOLVED |
| ibm-granite/granite-4.0-350m-base a50b46c | REDISTRIBUTION | — | **ELIGIBLE** | — |
| Qwen/Qwen3-4B-Base 906bfd4 | DEVELOPMENT_EVALUATION | DEV | **ELIGIBLE** | — (CONTROL, not mass-reach) |

Corrected lineage results with `contamination_state=NOT_APPLICABLE` (and all other fields identical, no benchmark claim) via `PYTHONPATH=src python -c "evaluate_lineage_admission(..., contamination_state='NOT_APPLICABLE')" ` — existing contract already returns ELIGIBLE:

| Candidate | Declared use | Purpose | Evaluator state | Reason codes |
|---|---|---|---|---|
| Qwen/Qwen3-0.6B-Base da87bfb | TRAINING_OR_ADAPTATION | TRAIN | **ELIGIBLE** | — |
| Qwen/Qwen3-0.6B-Base da87bfb | MODIFICATION_OR_DERIVATION | TRAIN | **ELIGIBLE** | — |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | TRAINING_OR_ADAPTATION | TRAIN | **ELIGIBLE** | — |
| Qwen/Qwen3.5-0.8B-Base dc7cdfe | MODIFICATION_OR_DERIVATION | TRAIN | **ELIGIBLE** | — |
| ibm-granite/granite-4.0-350m-base a50b46c | TRAINING_OR_ADAPTATION | TRAIN | **ELIGIBLE** | — |
| ibm-granite/granite-4.0-350m-base a50b46c | MODIFICATION_OR_DERIVATION | TRAIN | **ELIGIBLE** | — |

All three PRIMARY are therefore **MODEL_LINEAGE_ELIGIBLE=YES** without implying `MEDXPERTQA_SELECTION_CONTAMINATION=ASSESSED_CLEAN`. Benchmark selection contamination remains `NOT_ASSESSED` → `INCOMPLETE` → `CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE` per Spec 005 Q5, and tournament execution remains blocked until contamination evidence for the required primary slices is separately bound. See `reconciliation-contamination-semantics-2026-08-27.md` §2–§6.

No `PROHIBITED` or `REFERENCE_ONLY` due rights/gated terms — Apache 2.0 is correctly `SUPPORTED` where evaluated. The universal blocker is `CONTAMINATION_UNRESOLVED` for training-family uses, which is exactly the boundary between `PUBLIC_METADATA_RESOLVABLE` and the deeper benchmark-overlap assessment that Spec 005/003 reserve for post-tournament evaluation or contamination-mapping evidence.

The following fields remain `PUBLIC_METADATA_RESOLVABLE` but not yet bound as evaluator inputs because they require a separate contamination-assessment artifact:

- `contamination_state` for TRAIN-family uses (needs exact benchmark overlap mapping per `BENCHMARKS_IDENTITY=7f58edb...`)
- `origin_type` for derived GGUF (GGUF is `DERIVED` with `parent_asset_ids` pointing to base weight; here evaluated as `ORIGINAL` weight — GGUF derivation lineage is a separate `MODIFICATION_OR_DERIVATION` record to be evaluated after E002 with exact transform identity)
- `artifact_binding_state` for GGUF `DIRECT_DIGEST` (requires SHA256 of exact GGUF file — public Xet preview SHA exists but exact commandMed conversion identity remains to be frozen with pinned toolchain)

---

## 6. What is complete vs blocked without E002 (after contamination semantics clarification)

**PUBLIC_METADATA_RESOLVABLE — complete at this file:**

- Repository identity, immutable revision (40-hex), gated false, pipeline tag, model_type, base status, source URI/evidence URI, license `apache-2.0` with evidence URI to LICENSE at same SHA, tokenizer/processor sibling set, access class PUBLIC, rights_state SUPPORTED, artifact binding IMMUTABLE_REVISION_LOCATOR.
- **Corrected:** With `contamination_state=NOT_APPLICABLE` for `MODEL_OR_CHECKPOINT` lineage records where the contamination condition is genuinely outside the lineage relation (benchmark contamination is separately adjudicated per exact `candidate × benchmark-slice`), `TRAINING_OR_ADAPTATION` and `MODIFICATION_OR_DERIVATION` are now **ELIGIBLE** for lineage admission (see table above and `reconciliation-contamination-semantics-2026-08-27.md`). No benchmark-clean claim is inferred.

**STILL BLOCKED — benchmark contamination adjudication (separate evidence, not weight bytes):**

- `MEDXPERTQA_TEXT_DEV_CONTAMINATION_DISPOSITION=NOT_ASSESSED` → `INCOMPLETE_CONTAMINATION_GATE` → `CANDIDATE_SLICE_NOT_SELECTION_ELIGIBLE` per Spec 005 Q5. This is `candidate × benchmark-slice` evidence, not model lineage. It correctly blocks **selection/tournament execution**, not lineage. No `NOT_APPLICABLE` shortcut is allowed for this selection slice (Q4).

**MODEL_WEIGHT_ACCESS_REQUIRED — blocked exactly as (unchanged):**

- `MODIFICATION_OR_DERIVATION` for GGUF quantization provenance: exact transform/toolchain identity, frozen flags, and content SHA256 for the produced artifact. Public `ggml-org` and `ibm-granite/granite-4.0-350m-base-GGUF` Xet metadata provides preview sizes/SHAs (Qwen3.5 563 MB `0dabf...`, Granite Q4_K_M 237 MB), but commandMed's canonical conversion identity (pinned `llama.cpp` + convert flags) is not yet frozen — needs manifest, not weight download.
- Derived GGUF `parent_asset_ids` linkage: the linkage proof needs the exact base `content_sha256` (weight SHA256) which is stored in Xet as `2c465b...` style but validated via HEAD without weight bytes — reachable without full download via HEAD/Xet preview, still within public metadata, to be completed in next admission pass after this file.

**Credentials / gated terms:** NONE required (all three PRIMARY are ungated). No `extra_gated_prompt` for these repos.

**Estimated bytes if E002 were granted:** Weight access would transfer ~500–700 MB per candidate for full `model.safetensors` verification (Qwen3-0.6B ~1.19 GB BF16, Qwen3.5-0.8B ~? similar, Granite 350M ~704 MB BF16). No such transfer occurred here. Public Xet preview suffices for `DIRECT_DIGEST` without full download; full weight is needed only for device execution or training.

---

## 7. PRIMARY admission consequence (FULLY_ADMITTED_PRIMARY_ONLY — corrected)

```text
CANDIDATE_MANIFEST_FROZEN=NO
FULLY_ADMITTED_PRIMARY_CANDIDATES (MODEL_LINEAGE)=[Qwen/Qwen3-0.6B-Base, Qwen/Qwen3.5-0.8B-Base, ibm-granite/granite-4.0-350m-base] — each ELIGIBLE for TRAINING_OR_ADAPTATION / MODIFICATION_OR_DERIVATION with contamination_state=NOT_APPLICABLE (no benchmark claim)
FULLY_ADMITTED_FOR_BENCHMARK_SELECTION=[] (empty — benchmark selection contamination is separate and remains NOT_ASSESSED → INCOMPLETE)
PUBLIC_METADATA_PRIMARY_LEAD=Qwen/Qwen3.5-0.8B-Base, Qwen/Qwen3-0.6B-Base, ibm-granite/granite-4.0-350m-base (all three lineage-ELIGIBLE, no rights/gated disqualifier)
CONTROL_RETAINED=Qwen/Qwen3-4B-Base 32K (CONTROL_NON_WINNER, ELIGIBLE for DEVELOPMENT_EVALUATION)
SPEC003_LINEAGE_RESULT=ELIGIBLE_FOR_TRAIN_LINEAGE (with NOT_APPLICABLE where genuinely outside — see reconciliation)
PRIMARY_ADMISSION=BLOCKED_PENDING_BENCHMARK_CONTAMINATION_EVIDENCE (lineage eligible, selection not)
```

No candidate failed a rights/gated hard gate or lineage contamination — all three are now **model-lineage ELIGIBLE**. Benchmark selection remains `INCOMPLETE` because `MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE` — this correctly blocks **tournament execution / primary ranking**, not lineage. The next required evidence is therefore **not** a model-weight download, but separate exact `candidate × benchmark-slice` contamination evidence (dual-axis exact+semantic with resolved artifact binding) before any `REQUIRED_PRIMARY_SELECTION` slice can be used.

Until benchmark contamination evidence for the required primary slices is bound, the correct return per Spec 005 Q5 is:

```text
PRIMARY_RESULT=NO_SELECTION_YET (benchmark selection contamination gate INCOMPLETE — lineage eligible, selection blocked)
FOUNDER+CHATGPT_RESOURCE_CLASS_RECONSIDERATION_REQUIRED=NO (mass-reach hypothesis not yet falsified — candidates lineage-eligible, evidence incomplete on selection axis)
```

---

**Prepared by:** Pi (public metadata only) — no weight download, no gated acceptance, no execution, no spend.
**Contract:** `data/lineage/lineage_contract.json` (SHA `2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962`)
**Evaluator:** `src/commandmed/eval_contract/lineage.py` (offline, deterministic)
**Next authorized work:** Founder+ChatGPT decide whether to grant a narrow contamination-assessment authorization that does not imply E002 weight access, or to grant E002 and bind exact weight digests for derived GGUF lineage.

