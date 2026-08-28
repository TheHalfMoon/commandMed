# E004 Decision B Non-Weight Input Hash Review Surface — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `1a66efb145b8850c326d3a54dcfde7a6ef6314df`  
**Authority basis:** canonical E002 static public-source integrity/provenance authority plus canonical `ARTIFACT_DECISION_B` preparation authority  
**Authorized converter source:** `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`  
**Artifact class:** static evidence-request / conversion-subject closure preparation only  
**Model/source-weight download performed by this record:** NO  
**Model loading performed:** NO  
**Converter execution performed:** NO  
**Model conversion performed:** NO  
**Quantization performed:** NO  
**Inference/benchmark/device/training performed:** NO  
**Spend:** USD 0

This record narrows the unresolved Decision B field:

```text
EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
```

into a source-derived review surface. It does not claim any file hash that has not yet been independently recomputed from the exact frozen-revision bytes, and it does not make either conversion subject executable.

## 1. Exact Decision B subject scope

```text
GRANITE_PRIMARY=
  ibm-granite/granite-4.0-350m-base@
  a50b46cef21c8a86b15f0496cb794487a78a910b

QWEN_CONTROL=
  Qwen/Qwen3-4B-Base@
  906bfd4b4dc7f14ee4320094d8b41684abff8539
```

No Qwen3-0.6B, Qwen3.5-0.8B, alternate Granite product, alternate revision, preconverted GGUF, or other candidate is added to Decision B by this record.

## 2. Exact converter-source identities used to derive the review surface

The canonical conversion-toolchain record already binds the top-level entrypoint:

```text
CONVERTER_ENTRYPOINT=convert_hf_to_gguf.py
CONVERTER_ENTRYPOINT_GIT_BLOB=78ad26c6563062e2a801c9f76f77a7ce196dd195
CONVERTER_ENTRYPOINT_BYTES=12798
```

This review surface additionally binds the exact implementation modules inspected at the same authorized source revision:

```text
BASE_CONVERSION_MODULE=conversion/base.py
BASE_CONVERSION_MODULE_GIT_BLOB=56547ace009fd4d719a641f910e3f0890587d9b9
BASE_CONVERSION_MODULE_BYTES=139890

GRANITE_CONVERSION_MODULE=conversion/granite.py
GRANITE_CONVERSION_MODULE_GIT_BLOB=796d37cca269a71e014759cb0f6c5c1342c7615b
GRANITE_CONVERSION_MODULE_BYTES=38552

QWEN_CONVERSION_MODULE=conversion/qwen.py
QWEN_CONVERSION_MODULE_GIT_BLOB=cdba8a63e9c919232e2ec80e88b01afec7967dc4
QWEN_CONVERSION_MODULE_BYTES=36961

LLAMA_CONVERSION_MODULE=conversion/llama.py
LLAMA_CONVERSION_MODULE_GIT_BLOB=41d8c2309281911564ab3604d84a2f30010ef7cc
LLAMA_CONVERSION_MODULE_BYTES=21362
```

These are source identities only. They are not executable SHA-256 identities and do not prove conversion success.

## 3. What the exact converter source proves

### 3.1 Configuration input

`ModelBase.load_hparams(...)` uses Hugging Face `AutoConfig.from_pretrained(..., trust_remote_code=False)` for a local model directory and falls back to reading `config.json` directly.

Therefore:

```text
CONFIG_JSON_BEHAVIOR_INPUT=REQUIRED_BY_EXACT_SOURCE
REMOTE_CODE_REQUIRED=NO
```

### 3.2 Sharded safetensors index input

For local safetensors, `ModelBase.index_tensors(...)` detects `model.safetensors.index.json` when present, parses its `weight_map`, and validates tensor/file consistency against the shard files.

Therefore for Qwen3-4B CONTROL:

```text
MODEL_SAFETENSORS_INDEX_JSON_BEHAVIOR_INPUT=REQUIRED_BY_EXACT_SOURCE
```

Granite PRIMARY uses a single `model.safetensors` and its frozen repository does not expose a safetensors index file, so no index file is proposed for Granite.

### 3.3 Tokenizer input behavior

Qwen3 inherits Qwen2 vocabulary handling. Qwen2 attempts sentencepiece vocabulary handling and falls back to GPT-2 vocabulary handling; the GPT-2 path invokes `AutoTokenizer.from_pretrained(self.dir_model)`.

Granite inherits `LlamaModel`. The exact `LlamaModel.set_vocab()`:

- conditionally reads `tokenizer_config.json` when present;
- then attempts sentencepiece handling;
- then Hugging Face tokenizer handling;
- then GPT-2/AutoTokenizer handling.

The exact repositories expose tokenizer assets including `tokenizer.json`, `tokenizer_config.json`, `merges.txt`, and `vocab.json`; Granite also exposes `special_tokens_map.json`.

Static source inspection cannot safely reduce all possible tokenizer file reads to one file without executing the library stack, which this evidence lane does not do. The review surface therefore uses a conservative tokenizer-associated content set rather than claiming a minimal set prematurely.

### 3.4 Qwen3 README is behavior-affecting

The exact `Qwen3Model._is_qwen3_reranker()` reads `README.md` when the file exists and inspects it for Qwen3 reranker markers before conversion behavior is finalized.

Therefore for Qwen3-4B CONTROL:

```text
README_MD_BEHAVIOR_INPUT=REQUIRED_BY_EXACT_SOURCE_FOR_RERANKER_CLASSIFICATION
```

This is a behavior-input statement, not a claim that README contains model weights or executable code.

### 3.5 Files not currently proven conversion-required

The exact reviewed path has not established these as required inputs for the two prepared subjects:

```text
GENERATION_CONFIG_JSON_CONVERSION_REQUIRED=NOT_PROVEN
LICENSE_CONVERSION_REQUIRED=NO_EVIDENCE
MODEL_SIG_CONVERSION_REQUIRED=NO_EVIDENCE
GITATTRIBUTES_CONVERSION_REQUIRED=NO_EVIDENCE
```

They must not be silently added to the execution-authoritative required-input set merely because they are present in the source repositories or included by a broad remote-download convenience pattern.

## 4. Granite PRIMARY proposed non-weight hash set

Frozen source:

```text
REPOSITORY=ibm-granite/granite-4.0-350m-base
REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
```

### Required by exact converter source

| File | Necessity class | Exact SHA-256 | Exact integer bytes |
|---|---|---|---:|
| `config.json` | `REQUIRED_BY_EXACT_SOURCE` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `tokenizer_config.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `tokenizer.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `merges.txt` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `vocab.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `special_tokens_map.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |

### Present but not frozen as required by this record

```text
generation_config.json=NOT_PROVEN_REQUIRED
README.md=NOT_PROVEN_REQUIRED_FOR_GRANITE_PATH
model.sig=NOT_PROVEN_REQUIRED
.gitattributes=NOT_PROVEN_REQUIRED
```

The reviewer must tighten or correct this set from exact source evidence rather than accept it by default.

## 5. Qwen3-4B CONTROL proposed non-weight hash set

Frozen source:

```text
REPOSITORY=Qwen/Qwen3-4B-Base
REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
```

### Required by exact converter source or behavior classification

| File | Necessity class | Exact SHA-256 | Exact integer bytes |
|---|---|---|---:|
| `config.json` | `REQUIRED_BY_EXACT_SOURCE` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `model.safetensors.index.json` | `REQUIRED_BY_EXACT_SOURCE` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `README.md` | `REQUIRED_BY_EXACT_SOURCE_FOR_RERANKER_CLASSIFICATION` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `tokenizer_config.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `tokenizer.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `merges.txt` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |
| `vocab.json` | `REQUIRED_OR_TOKENIZER_DEPENDENCY` | `NEEDS_REVIEW_COMPUTATION` | `NEEDS_REVIEW_COMPUTATION` |

### Present but not frozen as required by this record

```text
generation_config.json=NOT_PROVEN_REQUIRED
LICENSE=NOT_PROVEN_REQUIRED
.gitattributes=NOT_PROVEN_REQUIRED
```

The reviewer must tighten or correct this set from exact source evidence rather than accept it by default.

## 6. Hash evidence semantics

The desired next evidence is cryptographic SHA-256 over the exact raw public file bytes at each frozen Hugging Face revision, plus the exact integer byte count of the same response/file identity.

```text
REVIEWER_RECOMPUTED_PUBLIC_RAW_BYTES_SHA256=ACCEPTABLE_STATIC_PROVIDER_EVIDENCE_FOR_REPOSITORY_RECONCILIATION
REVIEWER_RECOMPUTED_PUBLIC_RAW_BYTES_SHA256_EQUALS_LOCAL_EXECUTION_WORKSPACE_VERIFICATION=NO
```

Even after these remote raw-byte hashes are bound:

```text
LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
LOCAL_FILE_SHA256_RECOMPUTATION=NEEDS_EVIDENCE
```

A later execution-authoritative conversion subject must still satisfy whatever local-byte integrity mechanism is required at that future execution gate.

## 7. Requested independent review work

Fresh exact-head review must independently inspect the exact authorized converter revision and exact frozen model revisions, then return a concrete evidence table for every file it concludes belongs in the conservative complete non-weight behavior/input set:

```text
subject
source_repository
source_revision
file
necessity_class
exact_sha256_of_raw_frozen_revision_bytes
exact_integer_bytes
source_url_or_provider_surface
```

The reviewer must also explicitly report:

1. whether any proposed file should be removed from the required/conservative set;
2. whether any omitted file must be added because exact converter source reads it or because it is necessary for the tokenizer path used by these repositories;
3. whether `generation_config.json` is actually required by the exact conversion path;
4. whether Qwen3 `README.md` is correctly treated as behavior-affecting for reranker classification;
5. whether the Qwen safetensors index is required and whether its exact raw-byte SHA-256 can be independently recomputed;
6. whether any file would require repository-supplied executable code or `trust_remote_code`; if yes, fail closed rather than execute it.

No tokenizer/model/converter execution is requested. The review is static source inspection plus exact public raw-byte hashing only.

## 8. Current unresolved subject fields

Until a later commit binds reviewed values:

```text
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
QWEN_EXACT_MODEL_INDEX_SHA256=NEEDS_EVIDENCE
```

No placeholder in this record is execution authority.

## 9. No authority expansion

```text
E002_AUTHORITY=AUTHORIZED_EXISTING_FROZEN_PUBLIC_CANDIDATES_ONLY
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED_EXISTING
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY

MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_QUALIFICATION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
SELECTION_SUITE_CONSTRUCTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

```text
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 10. Current lifecycle effect

```text
DECISION_B_NON_WEIGHT_INPUT_HASH_REVIEW_SURFACE=PREPARED_FOR_EXACT_HEAD_REVIEW
NON_WEIGHT_HASH_VALUES_BOUND=NO
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Canonical merge of this placeholder-bearing review surface is not the intended terminal state. If exact-head review produces concrete hashes or corrects the proposed set, this branch must be updated, the old review becomes historical, and a new fresh exact-head review is required before merge.