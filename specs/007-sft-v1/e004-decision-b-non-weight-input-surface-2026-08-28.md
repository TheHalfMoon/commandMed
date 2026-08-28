# E004 Decision B Non-Weight Input Surface — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `1a66efb145b8850c326d3a54dcfde7a6ef6314df`  
**Artifact class:** non-executing static converter-input analysis / hash-probe candidate  
**Authority effect:** NONE  
**Model/source-weight download performed:** NO  
**Model load performed:** NO  
**Converter execution performed:** NO  
**Conversion/quantization performed:** NO  
**Spend:** USD 0

This record narrows the non-weight local input surface for the two already-authorized `ARTIFACT_DECISION_B` conversion-subject preparations by reading the exact pinned `llama.cpp` converter source. It does not authorize conversion and does not claim raw-file SHA-256 values that have not yet been independently recomputed from exact frozen-revision bytes.

```text
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
PREPARED_SOURCE_MODE=EXACT_LOCAL_DIRECTORY
REMOTE_CONVERSION_MODE_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
```

## 1. Exact source-code basis

The pinned converter source establishes these relevant behaviors:

```text
CONVERT_ENTRYPOINT_SOURCE=convert_hf_to_gguf.py
MODEL_BASE_SOURCE=conversion/base.py
MODEL_BASE_GIT_BLOB=56547ace009fd4d719a641f910e3f0890587d9b9
GRANITE_CONVERTER_SOURCE=conversion/granite.py
GRANITE_CONVERTER_GIT_BLOB=796d37cca269a71e014759cb0f6c5c1342c7615b
QWEN_CONVERTER_SOURCE=conversion/qwen.py
QWEN_CONVERTER_GIT_BLOB=cdba8a63e9c919232e2ec80e88b01afec7967dc4
MAMBA_CONVERTER_SOURCE=conversion/mamba.py
SPECIAL_VOCAB_SOURCE=gguf-py/gguf/vocab.py
```

Observed source behavior:

1. Local conversion loads model hyperparameters from the local directory; the Granite/Mamba2 path directly reads `config.json` and the generic path uses local Hugging Face configuration with `trust_remote_code=False`.
2. `ModelBase.index_tensors()` reads `model.safetensors.index.json` when present and uses its `weight_map` to identify sharded safetensors parts. This makes the index a hard non-weight input for the frozen sharded Qwen subject.
3. `Qwen3Model` inherits `Qwen2Model.set_vocab()`, which attempts SentencePiece then GPT-2 vocabulary handling.
4. `GraniteHybridModel` delegates vocabulary handling through `Mamba2Model.set_vocab()`. At the frozen Granite tree there is no `tokenizer.model` and there is `tokenizer.json`, therefore the selected local path is GPT-2 vocabulary handling.
5. GPT-2 handling calls `AutoTokenizer.from_pretrained(local_directory)` and `SpecialVocab(local_directory, load_merges=True)`.
6. Pinned `SpecialVocab` reads `tokenizer.json` directly when present, reads `tokenizer_config.json` when present, obtains merges from `tokenizer.json` when embedded, and falls back to `merges.txt` only when requested merges were not found there.
7. Qwen3 reranker detection reads `README.md` if present, but the frozen `Qwen3-4B-Base` architecture is `Qwen3ForCausalLM`; the README read is therefore classified separately as optional behavior-preservation input rather than a core model/tokenizer dependency.

No generic converter helper containing `trust_remote_code=True` is authorized merely because it exists in the source tree.

```text
REMOTE_CODE_EXECUTION_AUTHORITY=NONE
E002_NO_REMOTE_CODE_EXECUTION=ENFORCED
TRUST_REMOTE_CODE_TRUE_PATH_SELECTED_FOR_DECISION_B_SUBJECTS=NO
```

## 2. Classification vocabulary

```text
HARD_CONVERTER_INPUT=
  explicitly required by the selected pinned converter path for this exact subject

TOKENIZER_RESOLUTION_BUNDLE=
  frozen local tokenizer file retained to make Transformers tokenizer resolution deterministic;
  may be redundant when tokenizer.json already contains equivalent vocabulary/merge data

OPTIONAL_READ_IF_PRESENT=
  pinned converter reads the file when present but absence does not establish that conversion is impossible

NOT_SELECTED_CONVERSION_INPUT=
  repository file not required by the selected local conversion path established here
```

This classification does not permit deleting provider files from a future exact source acquisition. It only identifies which non-weight bytes need explicit conversion-subject identity binding before execution authorization can be considered.

## 3. Granite PRIMARY non-weight surface

Frozen identity:

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
HF_ARCHITECTURE_CLASS=GraniteMoeHybridForCausalLM
```

Frozen provider tree includes `config.json`, `tokenizer.json`, `tokenizer_config.json`, `merges.txt`, `vocab.json`, `special_tokens_map.json`, `generation_config.json`, `README.md`, `model.sig`, and the already-bound weight file.

Candidate classification:

| Path | Classification | Static reason |
|---|---|---|
| `config.json` | `HARD_CONVERTER_INPUT` | Granite/Mamba2 local initialization reads local config/hparams. |
| `tokenizer.json` | `HARD_CONVERTER_INPUT` | Its presence selects GPT-2 vocab handling; AutoTokenizer and SpecialVocab consume the local tokenizer surface. |
| `tokenizer_config.json` | `HARD_CONVERTER_INPUT_WHEN_PRESENT` | Pinned SpecialVocab reads it when present for special tokens/chat-template metadata. |
| `merges.txt` | `TOKENIZER_RESOLUTION_BUNDLE_CONDITIONAL_FALLBACK` | SpecialVocab falls back to it only when merges are not already available from tokenizer.json. |
| `vocab.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserve deterministic local AutoTokenizer resolution even if fast tokenizer data is sufficient. |
| `special_tokens_map.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserve exact frozen local tokenizer metadata surface used by Transformers resolution. |
| `README.md` | `NOT_SELECTED_CONVERSION_INPUT_FOR_GRANITE` | No selected Granite path identified here requires it. |
| `generation_config.json` | `NOT_SELECTED_CONVERSION_INPUT` | Generation configuration is not part of conversion input discovery established by the pinned path. |
| `model.sig` | `NOT_SELECTED_CONVERSION_INPUT` | No selected converter read established. |

Before this classification can close Granite's `EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET`, exact frozen-revision raw-byte identities must be bound for the conservative conversion-input bundle:

```text
GRANITE_HASH_PROBE_PATHS=
  config.json
  tokenizer.json
  tokenizer_config.json
  merges.txt
  vocab.json
  special_tokens_map.json

GRANITE_RAW_SHA256_SET=NEEDS_INDEPENDENT_RAW_BYTE_PROBE
GRANITE_RAW_INTEGER_BYTE_SET=NEEDS_INDEPENDENT_RAW_BYTE_PROBE
```

## 4. Qwen3-4B CONTROL non-weight surface

Frozen identity:

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
HF_ARCHITECTURE_CLASS=Qwen3ForCausalLM
ROLE=CONTROL
WINNER_ELIGIBLE=NO
```

Frozen provider tree includes `config.json`, `model.safetensors.index.json`, `tokenizer.json`, `tokenizer_config.json`, `merges.txt`, `vocab.json`, `generation_config.json`, `README.md`, and the already-bound three weight shards.

Candidate classification:

| Path | Classification | Static reason |
|---|---|---|
| `config.json` | `HARD_CONVERTER_INPUT` | Local hparams and exact Qwen architecture identity. |
| `model.safetensors.index.json` | `HARD_CONVERTER_INPUT` | `ModelBase.index_tensors()` opens the index, reads `weight_map`, and resolves sharded tensor parts. |
| `tokenizer.json` | `HARD_CONVERTER_INPUT` | Selected Qwen2/Qwen3 vocabulary path falls to GPT-2 handling for this frozen tokenizer surface; AutoTokenizer/SpecialVocab consume local tokenizer data. |
| `tokenizer_config.json` | `HARD_CONVERTER_INPUT_WHEN_PRESENT` | Pinned SpecialVocab reads it when present and AutoTokenizer may use it for local tokenizer resolution. |
| `merges.txt` | `TOKENIZER_RESOLUTION_BUNDLE_CONDITIONAL_FALLBACK` | SpecialVocab fallback if tokenizer.json does not supply merges. |
| `vocab.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserve deterministic local AutoTokenizer resolution. |
| `README.md` | `OPTIONAL_READ_IF_PRESENT` | Qwen3 reranker detection reads README when present; exact base architecture remains non-reranker. |
| `generation_config.json` | `NOT_SELECTED_CONVERSION_INPUT` | No selected conversion read established. |

Required raw-byte probe before closing the Qwen non-weight hash set:

```text
QWEN_HASH_PROBE_PATHS=
  config.json
  model.safetensors.index.json
  tokenizer.json
  tokenizer_config.json
  merges.txt
  vocab.json
  README.md

QWEN_MODEL_INDEX_RAW_SHA256=NEEDS_INDEPENDENT_RAW_BYTE_PROBE
QWEN_RAW_SHA256_SET=NEEDS_INDEPENDENT_RAW_BYTE_PROBE
QWEN_RAW_INTEGER_BYTE_SET=NEEDS_INDEPENDENT_RAW_BYTE_PROBE
```

`README.md` is included in the probe so a future exact local directory can preserve the pinned converter's optional reranker-detection read without allowing mutable prose to enter unbound.

## 5. Reviewer hash-probe requirements

A fresh independent review of this exact head is requested to query Hugging Face at the **exact frozen revisions** and calculate SHA-256 over the raw bytes returned for every path above. The reviewer must not use `main`, a moving branch, a mirror revision, or reconstructed pretty-printed JSON.

For each path return:

```text
repository
revision
path
raw_integer_bytes
raw_sha256
provider_oid_or_xet_identity_if_exposed
```

The reviewer should additionally verify:

```text
GRANITE_TOKENIZER_JSON_CONTAINS_MERGES=<YES|NO>
QWEN_TOKENIZER_JSON_CONTAINS_MERGES=<YES|NO>
```

If the embedded merge list is present and complete for a subject, `merges.txt` may remain in the conservative local-bundle hash set while being classified as non-hard fallback data. Do not remove it merely to minimize the bundle before exact local execution planning is reviewed.

The initial review is an evidence probe, not final qualification. After reviewer raw hashes are returned, this branch must be updated to bind those exact values and receive a **new exact-head review** before merge.

```text
INITIAL_HEAD_ELIGIBLE_FOR_CANONICAL_MERGE=NO
REVIEWER_HASH_PROBE_REQUIRED=YES
POST_HASH_BINDING_FRESH_EXACT_HEAD_REVIEW_REQUIRED=YES
```

## 6. Fail-closed boundaries

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
REVIEWER_RAW_DOWNLOAD_EQUALS_COMMANDMED_LOCAL_SOURCE_BUNDLE_MATERIALIZATION=NO
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
MODEL_SOURCE_WEIGHT_LOCAL_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

The independent raw hash probe may improve provider-byte provenance. It cannot substitute for later local acquisition/integrity evidence required by an execution-authoritative conversion subject.

## 7. Current state

```text
DECISION_B_NON_WEIGHT_INPUT_SURFACE=CLASSIFIED_PENDING_RAW_HASH_BINDING
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=INCOMPLETE_PENDING_RAW_HASH_PROBE
QWEN_EXACT_MODEL_INDEX_SHA256=INCOMPLETE_PENDING_RAW_HASH_PROBE
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=INCOMPLETE_PENDING_RAW_HASH_PROBE
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO
E004_STATE=BLOCKED_PREFLIGHT
```

## Exclusions

This artifact performs no model/source-weight download, model loading, converter execution, model conversion, quantization, inference, benchmark/device execution, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, personnel engagement, payment, or spend. It creates no workflow and consumes no authorized workflow run.
