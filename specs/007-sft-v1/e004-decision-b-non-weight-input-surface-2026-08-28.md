# E004 Decision B Non-Weight Input Surface — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `1a66efb145b8850c326d3a54dcfde7a6ef6314df`  
**Initial probe head:** `dfe3fefa7be2286bf91f9b35e444d45595ff5567`  
**Artifact class:** non-executing static converter-input analysis plus exact frozen-provider raw-byte provenance  
**Authority effect:** NONE  
**Model/source-weight download performed by commandMed:** NO  
**Local source-bundle materialization performed:** NO  
**Model load performed:** NO  
**Converter execution performed:** NO  
**Conversion/quantization performed:** NO  
**Spend:** USD 0

This record narrows and identity-binds the non-weight input surface for the two already-authorized `ARTIFACT_DECISION_B` conversion-subject preparations by reading the exact pinned `llama.cpp` converter source and binding independent raw-byte probes from the exact frozen Hugging Face revisions.

The raw-byte probe improves **provider-byte provenance only**. It is not commandMed local source-bundle materialization and cannot satisfy the later local-integrity requirements of an execution-authoritative conversion subject.

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

The pinned converter source identities used for this classification are:

```text
CONVERT_ENTRYPOINT_SOURCE=convert_hf_to_gguf.py
MODEL_BASE_SOURCE=conversion/base.py
MODEL_BASE_GIT_BLOB=56547ace009fd4d719a641f910e3f0890587d9b9
GRANITE_CONVERTER_SOURCE=conversion/granite.py
GRANITE_CONVERTER_GIT_BLOB=796d37cca269a71e014759cb0f6c5c1342c7615b
QWEN_CONVERTER_SOURCE=conversion/qwen.py
QWEN_CONVERTER_GIT_BLOB=cdba8a63e9c919232e2ec80e88b01afec7967dc4
MAMBA_CONVERTER_SOURCE=conversion/mamba.py
MAMBA_CONVERTER_GIT_BLOB=0a4dd73982df9dc92fbe98d87c0094199bddeb43
SPECIAL_VOCAB_SOURCE=gguf-py/gguf/vocab.py
SPECIAL_VOCAB_GIT_BLOB=d93b94f2d792147276be21db004dbd8d4edef82c
```

Observed source behavior:

1. Local conversion loads model hyperparameters from the local directory; the Granite/Mamba2 path reads local `config.json`, while the generic local configuration path uses `trust_remote_code=False`.
2. `ModelBase.index_tensors()` reads `model.safetensors.index.json` when present and uses its `weight_map` to identify sharded safetensors parts. The index is therefore a hard non-weight input for the frozen sharded Qwen subject.
3. `Qwen3Model` inherits `Qwen2Model.set_vocab()`, which attempts SentencePiece and then GPT-2 vocabulary handling.
4. `GraniteHybridModel` delegates vocabulary handling through `Mamba2Model.set_vocab()`. The frozen Granite tree has no `tokenizer.model` and does have `tokenizer.json`, so the selected local path falls to GPT-2 vocabulary handling.
5. GPT-2 handling calls `AutoTokenizer.from_pretrained(local_directory)` and `SpecialVocab(local_directory, load_merges=True)`.
6. Pinned `SpecialVocab` reads `tokenizer.json` directly when present, reads `tokenizer_config.json` when present, obtains merges from `tokenizer.json` when embedded, and falls back to `merges.txt` only when requested merges were not found there.
7. Qwen3 reranker detection reads `README.md` if present; the frozen `Qwen3-4B-Base` architecture remains `Qwen3ForCausalLM`, so README is classified as optional behavior-preservation input rather than a core model/tokenizer dependency.

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
  frozen local tokenizer file retained to make local Transformers tokenizer resolution deterministic;
  may be redundant when tokenizer.json already contains equivalent vocabulary/merge data

OPTIONAL_READ_IF_PRESENT=
  pinned converter reads the file when present but absence does not establish that conversion is impossible

NOT_SELECTED_CONVERSION_INPUT=
  repository file not required by the selected local conversion path established here
```

This classification does not permit deleting provider files from a future exact source acquisition. It identifies the conservative non-weight byte surface that must remain identity-bound before execution authorization can be considered.

## 3. Initial independent evidence probe

The initial PR head was deliberately not merge-eligible. It requested an independent exact-revision raw-byte probe and a source-classification review before any hash values could become part of this record.

```text
INITIAL_PROBE_HEAD=dfe3fefa7be2286bf91f9b35e444d45595ff5567
INITIAL_HEAD_ELIGIBLE_FOR_CANONICAL_MERGE=NO
INITIAL_REVIEW_SOURCE_CLASSIFICATION_MATERIAL_FINDING=NO
INITIAL_REVIEW_RAW_ACTIONS_RUNS=0
INITIAL_REVIEWER_HASH_PROBE_COMPLETED=YES
INITIAL_REVIEWER_HASH_PROBE_USED_EXACT_FROZEN_REVISIONS=YES
INITIAL_REVIEWER_HASH_PROBE_USED_RAW_BYTES=YES
```

The reviewer independently obtained bytes from exact frozen Hugging Face revision paths, measured `len(raw)`, calculated `sha256(raw)`, and reported provider Git OIDs. The reviewer download is evidence about provider bytes only.

```text
REVIEWER_RAW_DOWNLOAD_EQUALS_COMMANDMED_LOCAL_SOURCE_BUNDLE_MATERIALIZATION=NO
REVIEWER_RAW_HASH_EQUALS_LOCAL_POST_ACQUISITION_INTEGRITY_VERIFICATION=NO
```

## 4. Granite PRIMARY non-weight surface

Frozen identity:

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
HF_ARCHITECTURE_CLASS=GraniteMoeHybridForCausalLM
```

Classification:

| Path | Classification | Static reason |
|---|---|---|
| `config.json` | `HARD_CONVERTER_INPUT` | Granite/Mamba2 local initialization reads local config/hparams. |
| `tokenizer.json` | `HARD_CONVERTER_INPUT` | Its presence selects GPT-2 vocab handling; local AutoTokenizer and SpecialVocab consume the tokenizer surface. |
| `tokenizer_config.json` | `HARD_CONVERTER_INPUT_WHEN_PRESENT` | Pinned SpecialVocab reads it when present for special-token/chat-template metadata. |
| `merges.txt` | `TOKENIZER_RESOLUTION_BUNDLE_CONDITIONAL_FALLBACK` | SpecialVocab falls back to it only when merges are not already available from `tokenizer.json`. |
| `vocab.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserves deterministic local tokenizer resolution even if fast-tokenizer data is sufficient. |
| `special_tokens_map.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserves the exact frozen local tokenizer metadata surface for tokenizer resolution. |
| `README.md` | `NOT_SELECTED_CONVERSION_INPUT_FOR_GRANITE` | No selected Granite path identified here requires it. |
| `generation_config.json` | `NOT_SELECTED_CONVERSION_INPUT` | Generation configuration is not part of the selected conversion input discovery. |
| `model.sig` | `NOT_SELECTED_CONVERSION_INPUT` | No selected converter read established. |

### Granite exact provider raw-byte identities

All rows are bound to frozen revision `a50b46cef21c8a86b15f0496cb794487a78a910b`.

| Path | Raw integer bytes | Raw SHA-256 | Provider Git OID |
|---|---:|---|---|
| `config.json` | `1764` | `089690e22b9eafadcdd385afa5b6f3ea2446674ff5398c71df23be059d7c795d` | `2cb1a8bd37fd1aa27ae6a799314e4a9374912691` |
| `tokenizer.json` | `7153421` | `e2bad66439538cb4d5a7580680932432ed9ece9d3b8577e675512bdf11599253` | `d7e1714703eb97dcef3435aa50eb1de1cf241d62` |
| `tokenizer_config.json` | `17659` | `a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86` | `7a6b382740c0c6587ae8af40aeb4b40f8fb8c431` |
| `merges.txt` | `916646` | `b6fe424e334903f7fb84d3a106d9730455f4744b9fe3c21ee136d97a00e72502` | `354558edcdbd64ca7abd407b8be3d5d09d39d781` |
| `vocab.json` | `1612704` | `8af71076de8b0b626eed0f4c984faf0a7c062479164b2a31308a948524d4f69c` | `4764ec73731a47701c2f49b01bb428342870f498` |
| `special_tokens_map.json` | `579` | `c08676c49fd7969a3130f72be6d4bf34da66aa484a6e21dffe359893a1bd5f2e` | `3f67e7c50d57b16925f4f15469a774e7bf439047` |

The frozen `tokenizer.json` contains a non-empty embedded merge list:

```text
GRANITE_TOKENIZER_JSON_CONTAINS_NONEMPTY_MERGES=YES
GRANITE_EMBEDDED_MERGE_COUNT=100000
GRANITE_MERGES_TXT_CLASSIFICATION=CONSERVATIVE_FALLBACK_NOT_PRIMARY_EMBEDDED_MERGE_SOURCE
GRANITE_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
GRANITE_PROVIDER_NON_WEIGHT_RAW_INTEGER_BYTE_SET=BOUND
```

The provider-bound set is not a local-integrity claim:

```text
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=PROVIDER_BOUND_LOCAL_UNVERIFIED
```

## 5. Qwen3-4B CONTROL non-weight surface

Frozen identity:

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
HF_ARCHITECTURE_CLASS=Qwen3ForCausalLM
ROLE=CONTROL
WINNER_ELIGIBLE=NO
```

Classification:

| Path | Classification | Static reason |
|---|---|---|
| `config.json` | `HARD_CONVERTER_INPUT` | Local hparams and exact Qwen architecture identity. |
| `model.safetensors.index.json` | `HARD_CONVERTER_INPUT` | `ModelBase.index_tensors()` opens the index, reads `weight_map`, and resolves sharded tensor parts. |
| `tokenizer.json` | `HARD_CONVERTER_INPUT` | Selected Qwen2/Qwen3 vocabulary path falls to GPT-2 handling; local AutoTokenizer/SpecialVocab consume tokenizer data. |
| `tokenizer_config.json` | `HARD_CONVERTER_INPUT_WHEN_PRESENT` | Pinned SpecialVocab reads it when present and local AutoTokenizer may use it during resolution. |
| `merges.txt` | `TOKENIZER_RESOLUTION_BUNDLE_CONDITIONAL_FALLBACK` | SpecialVocab fallback if `tokenizer.json` does not supply merges. |
| `vocab.json` | `TOKENIZER_RESOLUTION_BUNDLE` | Preserves deterministic local tokenizer resolution. |
| `README.md` | `OPTIONAL_READ_IF_PRESENT` | Qwen3 reranker detection reads README when present; exact base architecture remains non-reranker. |
| `generation_config.json` | `NOT_SELECTED_CONVERSION_INPUT` | No selected conversion read established. |

### Qwen exact provider raw-byte identities

All rows are bound to frozen revision `906bfd4b4dc7f14ee4320094d8b41684abff8539`.

| Path | Raw integer bytes | Raw SHA-256 | Provider Git OID |
|---|---:|---|---|
| `config.json` | `727` | `304b2545a258d35620f1d4bf46940c0471d9baa00715ff8e77f84c2fca5057c1` | `df6b6d9d0d1ce7d1456641adb64a5aefe1c4c9bc` |
| `model.safetensors.index.json` | `32819` | `d6c42883a895dfef5b0080ed2116a1bcd764f558406b98923d675978a1abf29c` | `4747b0297d3109f14db49886972e3369c9a00b2a` |
| `tokenizer.json` | `7031645` | `c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` | `443909a61d429dff23010e5bddd28ff530edda00` |
| `tokenizer_config.json` | `9678` | `3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5` | `6a3829ee9491f36113e64df37573be81df0366f5` |
| `merges.txt` | `1671853` | `8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5` | `31349551d90c7606f325fe0f11bbb8bd5fa0d7c7` |
| `vocab.json` | `2776833` | `ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910` | `4783fe10ac3adce15ac8f358ef5462739852c569` |
| `README.md` | `2937` | `9fd20ab531a1dc75ae18fcde658dd69d04173fdb93311091c38a7098e3d4b4a1` | `83a7f3264b60636c4c59377ac2024165f33bbb8f` |

The frozen `tokenizer.json` contains a non-empty embedded merge list:

```text
QWEN_TOKENIZER_JSON_CONTAINS_NONEMPTY_MERGES=YES
QWEN_EMBEDDED_MERGE_COUNT=151387
QWEN_MERGES_TXT_CLASSIFICATION=CONSERVATIVE_FALLBACK_NOT_PRIMARY_EMBEDDED_MERGE_SOURCE
QWEN_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
QWEN_PROVIDER_NON_WEIGHT_RAW_INTEGER_BYTE_SET=BOUND
QWEN_EXACT_MODEL_INDEX_PROVIDER_RAW_SHA256=BOUND
QWEN_EXACT_MODEL_INDEX_PROVIDER_RAW_SHA256_VALUE=d6c42883a895dfef5b0080ed2116a1bcd764f558406b98923d675978a1abf29c
QWEN_EXACT_MODEL_INDEX_SHA256=PROVIDER_BOUND_LOCAL_UNVERIFIED
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=PROVIDER_BOUND_LOCAL_UNVERIFIED
```

`README.md` remains bound because the pinned converter may read it for reranker detection. Binding it does not elevate README prose to model identity or scientific evidence.

## 6. Provider evidence disposition

The initial probe materially advances the prepared conversion subjects at the provider-provenance layer:

```text
SOURCE_CLASSIFICATION_MATERIAL_FINDING=NO
GRANITE_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
QWEN_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
QWEN_EXACT_MODEL_INDEX_PROVIDER_RAW_SHA256=BOUND
PROVIDER_NON_WEIGHT_BYTE_IDENTITIES_REVIEWER_RECOMPUTED=YES
PROVIDER_NON_WEIGHT_BYTE_IDENTITIES_BOUND_TO_EXACT_FROZEN_REVISIONS=YES
```

It does **not** prove that a future local acquisition contains those bytes. Before any conversion execution authorization, a future exact local source bundle must be materialized under then-current authority and independently checked against the provider-bound identities.

Required local evidence remains:

```text
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
GRANITE_LOCAL_NON_WEIGHT_SHA256_RECOMPUTATION=NEEDS_EVIDENCE
QWEN_LOCAL_NON_WEIGHT_SHA256_RECOMPUTATION=NEEDS_EVIDENCE
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTATION=NEEDS_EVIDENCE
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTATION=NEEDS_EVIDENCE
LOCAL_BUNDLE_PROVIDER_IDENTITY_RECONCILIATION=NEEDS_EVIDENCE
```

## 7. Final exact-head review gate

The initial evidence probe is historical and cannot qualify this hash-binding commit for canonical merge. This updated head requires a new independent exact-head review that recomputes or re-verifies the bound values and checks the source classification and authority boundary.

```text
INITIAL_HEAD_MERGE_ELIGIBLE=NO
INITIAL_PROBE_RESULT_REUSED_AS_FINAL_MERGE_QUALIFICATION=NO
HASH_BINDING_COMPLETE=YES
POST_HASH_BINDING_FRESH_EXACT_HEAD_REVIEW_REQUIRED=YES
CURRENT_HEAD_MERGE_ELIGIBILITY=PENDING_FRESH_EXACT_HEAD_REVIEW
```

The final review must verify at least:

```text
RECORD_ONLY_SCOPE=YES
SOURCE_CLASSIFICATION_MATCHES_PINNED_CONVERTER=YES
GRANITE_PROVIDER_RAW_HASH_SET_BOUND_CORRECTLY=YES
QWEN_PROVIDER_RAW_HASH_SET_BOUND_CORRECTLY=YES
QWEN_MODEL_INDEX_PROVIDER_RAW_SHA256_BOUND_CORRECTLY=YES
LOCAL_SOURCE_BUNDLE_MATERIALIZATION_NOT_CLAIMED=YES
CONVERSION_AUTHORITY_REMAINS_NONE=YES
RAW_ACTIONS_RUNS_ON_EXACT_HEAD=0
MATERIAL_BLOCKER=NO
```

## 8. Fail-closed boundaries

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

## 9. Current state

```text
DECISION_B_NON_WEIGHT_INPUT_SURFACE=HASH_BOUND_PENDING_FINAL_EXACT_HEAD_REVIEW
GRANITE_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
QWEN_PROVIDER_NON_WEIGHT_RAW_SHA256_SET=BOUND
QWEN_EXACT_MODEL_INDEX_PROVIDER_RAW_SHA256=BOUND
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=PROVIDER_BOUND_LOCAL_UNVERIFIED
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=PROVIDER_BOUND_LOCAL_UNVERIFIED
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO
E004_STATE=BLOCKED_PREFLIGHT
```

## Exclusions

This artifact performs no commandMed model/source-weight download, local source-bundle materialization, model loading, converter execution, model conversion, quantization, inference, benchmark/device execution, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, personnel engagement, payment, or spend. It creates no workflow and consumes no authorized workflow run.
