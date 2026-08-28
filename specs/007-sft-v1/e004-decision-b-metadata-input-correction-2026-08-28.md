# E004 Decision B Metadata Input Correction — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46`  
**Artifact class:** non-executing static correction / raw-hash probe candidate  
**Authority effect:** NONE  
**Model/source-weight download performed:** NO  
**Model load performed:** NO  
**Converter execution performed:** NO  
**Conversion/quantization performed:** NO  
**Spend:** USD 0

This record corrects the canonical Decision B non-weight input classification after a deeper exact-source inspection found additional metadata inputs consumed by the pinned local conversion path. It does not authorize conversion and does not claim raw-file SHA-256 values that have not yet been independently recomputed from exact frozen-revision bytes.

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

## 1. Why this correction is required

PR #106 / canonical merge `39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46` correctly bound the tokenizer/config/index provider-byte surface identified through `conversion/base.py`, architecture-specific converter code, and `gguf-py/gguf/vocab.py`. A subsequent pinned-source inspection identified an additional always-invoked metadata path that was not included in that review scope.

Pinned source identities:

```text
CONVERSION_ENTRYPOINT_GIT_BLOB=78ad26c6563062e2a801c9f76f77a7ce196dd195
MODEL_BASE_SOURCE=conversion/base.py
MODEL_BASE_GIT_BLOB=56547ace009fd4d719a641f910e3f0890587d9b9
GGUF_METADATA_SOURCE=gguf-py/gguf/metadata.py
GGUF_METADATA_GIT_BLOB=d5836cc68d7a96cd267e70800994bb3cc7bfcad0
GRANITE_CONVERTER_SOURCE=conversion/granite.py
GRANITE_CONVERTER_GIT_BLOB=796d37cca269a71e014759cb0f6c5c1342c7615b
QWEN_CONVERTER_SOURCE=conversion/qwen.py
QWEN_CONVERTER_GIT_BLOB=cdba8a63e9c919232e2ec80e88b01afec7967dc4
MAMBA_CONVERTER_SOURCE=conversion/mamba.py
MAMBA_CONVERTER_GIT_BLOB=8a2a4637529a4f8140836ab089654684f85f96c9
SPECIAL_VOCAB_SOURCE=gguf-py/gguf/vocab.py
SPECIAL_VOCAB_GIT_BLOB=d93b94f2d792147276be21db004dbd8d4edef82c
```

The pinned `ModelBase.write()` path executes:

```text
prepare_tensors()
prepare_metadata(vocab_only=False)
write_header_to_file(...)
write_kv_data_to_file()
write_tensors_to_file(...)
```

`ModelBase.prepare_metadata()` calls `gguf.Metadata.load(...)` using the local model directory as the model-card directory. The pinned `Metadata.load()` implementation in `gguf-py/gguf/metadata.py` calls all three of:

```text
Metadata.load_model_card(model_path)          -> README.md when present
Metadata.load_hf_parameters(model_path)       -> config.json when present
Metadata.load_generation_config(model_path)  -> generation_config.json when present
```

Therefore the local conversion path reads model-card and generation metadata in addition to the tokenizer/config/index surface previously bound.

## 2. Canonical #106 finding and correction semantics

The following prior classifications are incomplete and must not be used as an execution-complete local input set:

```text
PR106_GRANITE_README_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT_FOR_GRANITE
PR106_GRANITE_GENERATION_CONFIG_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT
PR106_QWEN_GENERATION_CONFIG_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT
```

Corrected classification:

```text
GRANITE_README_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
GRANITE_GENERATION_CONFIG_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
QWEN_README_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
QWEN_GENERATION_CONFIG_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
```

`OPTIONAL_READ_IF_PRESENT_METADATA_INPUT` means the pinned converter reads the file when it exists in the exact local source directory; absence is tolerated by the source code, but when the file is present at the frozen provider revision its exact bytes belong to the deterministic local conversion subject and must be identity-bound before execution authorization can be considered.

The already-bound `config.json` rows remain hard converter/metadata inputs and are not reopened by this correction.

## 3. Non-file metadata input: local directory basename

The pinned `Metadata.apply_metadata_heuristic(...)` also uses `model_path.name` as a directory-name fallback when source metadata does not already establish all naming fields. Therefore the exact same file bytes placed under a different local directory basename can produce different GGUF metadata.

This makes the source-directory basename a semantic conversion input, not an operationally irrelevant path detail.

```text
EXACT_LOCAL_SOURCE_DIRECTORY_PARENT=CONTENT_OR_STORAGE_LOCATION_MAY_VARY_ONLY_IF_OTHER_BOUNDARIES_ALLOW
EXACT_LOCAL_SOURCE_DIRECTORY_BASENAME=REQUIRES_PREEXECUTION_FREEZE
GRANITE_REQUIRED_DIRECTORY_BASENAME=granite-4.0-350m-base
QWEN_REQUIRED_DIRECTORY_BASENAME=Qwen3-4B-Base
DIRECTORY_BASENAME_NORMALIZATION=PROHIBITED
HASH_OR_RANDOM_BASENAME_SUBSTITUTION=PROHIBITED
```

The required basename values above preserve the frozen provider repository leaf names. They do not grant source materialization or conversion authority. A future exact local content address may bind the parent/location independently while preserving this basename.

Because the prepared argv currently contains `<EXACT_LOCAL_SOURCE_DIRECTORY>`, this finding also means an execution-authoritative argv cannot be frozen until both the exact location/content identity and basename semantics are bound.

```text
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
EXACT_LOCAL_SOURCE_DIRECTORY_BASENAME_POLICY=STATICALLY_IDENTIFIED_PENDING_FINAL_POLICY_REVIEW
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
```

## 4. Missing frozen-provider byte identities

### Granite PRIMARY

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
MISSING_METADATA_HASH_PROBE_PATHS=
  README.md
  generation_config.json
```

Required independent raw-byte probe:

| Path | Raw bytes | Raw SHA-256 | Provider OID |
|---|---:|---|---|
| `README.md` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_PROVIDER_IDENTITY` |
| `generation_config.json` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_PROVIDER_IDENTITY` |

Public Hugging Face page evidence currently corroborates, but does not replace the raw-byte probe:

```text
GRANITE_PUBLIC_TREE_CURRENT_COMMIT_PREFIX=a50b46c
GRANITE_PUBLIC_TREE_CURRENT_COMMIT_MATCHES_FROZEN_REVISION_PREFIX=YES
GRANITE_PUBLIC_README_DISPLAY_SIZE=26.4_kB_NON_INTEGER_DISPLAY_ONLY
GRANITE_PUBLIC_GENERATION_CONFIG_DISPLAY_BYTES=147
GRANITE_PUBLIC_PAGE_EVIDENCE_EQUALS_RAW_SHA256_PROBE=NO
```

No SHA-256 is inferred from rendered HTML, parsed page text, or reconstructed JSON formatting.

### Qwen3-4B CONTROL

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
MISSING_METADATA_HASH_PROBE_PATHS=
  generation_config.json
```

`README.md` for Qwen was already included and provider-byte-bound by #106 because the Qwen converter also has optional reranker-detection behavior. It does not need a second binding here.

Required independent raw-byte probe:

| Path | Raw bytes | Raw SHA-256 | Provider OID |
|---|---:|---|---|
| `generation_config.json` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_RAW_BYTE_PROBE` | `NEEDS_INDEPENDENT_PROVIDER_IDENTITY` |

Exact frozen-revision Hugging Face page evidence corroborates:

```text
QWEN_PUBLIC_PAGE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
QWEN_PUBLIC_GENERATION_CONFIG_DISPLAY_BYTES=138
QWEN_PUBLIC_GENERATION_CONFIG_FILE_COMMIT_PREFIX=2fcc0a0
QWEN_PUBLIC_PAGE_EVIDENCE_EQUALS_RAW_SHA256_PROBE=NO
```

Again, no raw SHA-256 is inferred from the rendered/blame page.

## 5. Metadata/normalization policy implication

The pinned converter does not merely copy all source metadata bytes into GGUF. It parses model-card YAML frontmatter, config JSON, and generation configuration, applies converter-defined heuristics/field mapping, and writes GGUF key/value metadata. The source itself also contains narrowly defined parsing normalization, including model-card YAML handling and model/directory-name heuristics.

A future exact Decision B metadata policy must therefore distinguish:

```text
SOURCE_BYTES=
  immutable exact frozen-revision input bytes whose identities are bound before execution

SOURCE_DIRECTORY_BASENAME=
  immutable semantic input because pinned metadata heuristics consume model_path.name

CONVERTER_DEFINED_METADATA_MAPPING=
  deterministic behavior of the exact pinned converter source and exact dependency/runtime set

COMMANDMED_MANUAL_METADATA_MUTATION=
  PROHIBITED unless separately frozen and reviewed before execution

METADATA_OVERRIDE_FILE=
  NOT_SELECTED; no --metadata override is present in the prepared argv

MODEL_NAME_OVERRIDE=
  NOT_SELECTED; no --model-name override is present in the prepared argv

REMOTE_HF_MODEL_ID=
  NOT_SELECTED
```

The pinned model-card parser itself performs defined parsing normalization before YAML decoding, including quoting an exact `- no` sequence and replacing tabs with two spaces in the YAML frontmatter buffer. These are converter-defined parse semantics; they are not permission for commandMed to modify the source file before conversion.

```text
SOURCE_FILE_PREPROCESSING_BY_COMMANDMED=PROHIBITED
CONVERTER_INTERNAL_PARSE_NORMALIZATION=PERMITTED_ONLY_AS_IMPLEMENTED_BY_PINNED_SOURCE
METADATA_HEURISTIC_BYPASS=PROHIBITED
```

This correction does not yet close `NORMALIZATION_OR_METADATA_POLICY`; it removes false assumptions about the complete source input surface so that a later policy can be exact.

## 6. Reviewer raw-hash probe requirements

A fresh independent review of this exact head is requested to query Hugging Face at the exact frozen revisions and calculate SHA-256 over the raw bytes returned for exactly these three missing files:

```text
ibm-granite/granite-4.0-350m-base|a50b46cef21c8a86b15f0496cb794487a78a910b|README.md
ibm-granite/granite-4.0-350m-base|a50b46cef21c8a86b15f0496cb794487a78a910b|generation_config.json
Qwen/Qwen3-4B-Base|906bfd4b4dc7f14ee4320094d8b41684abff8539|generation_config.json
```

For each path return:

```text
repository
revision
path
raw_integer_bytes
raw_sha256
provider_oid_or_xet_identity_if_exposed
```

The reviewer must independently verify:

1. the pinned `ModelBase.write() -> prepare_metadata() -> Metadata.load()` call chain;
2. `metadata.py` Git blob identity;
3. that `Metadata.apply_metadata_heuristic(...)` consumes `model_path.name` as a fallback;
4. whether any other file or path-derived value on the exact selected local conversion path remains unbound by #106 plus this correction.

The first CodeRabbit request on the prior probe head could not execute because the service reported an hourly chat-message rate limit. Qodo was billing-blocked and Cubic reported its monthly review-line quota exhausted. Those service states are not review PASS evidence and do not relax this gate.

The initial and current correction heads remain evidence-probe material, not final qualification. After reviewer raw hashes are returned, this branch must be updated to bind those exact values and receive a new exact-head review before merge.

```text
INITIAL_HEAD_ELIGIBLE_FOR_CANONICAL_MERGE=NO
REVIEWER_HASH_PROBE_REQUIRED=YES
POST_HASH_BINDING_FRESH_EXACT_HEAD_REVIEW_REQUIRED=YES
REVIEW_SERVICE_UNAVAILABLE_EQUALS_REVIEW_PASS=NO
```

## 7. Fail-closed boundaries

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
REVIEWER_RAW_DOWNLOAD_EQUALS_COMMANDMED_LOCAL_SOURCE_BUNDLE_MATERIALIZATION=NO
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
MODEL_SOURCE_WEIGHT_LOCAL_INTEGRITY=INCOMPLETE
NORMALIZATION_OR_METADATA_POLICY=INCOMPLETE_PENDING_CORRECTED_INPUT_BINDING
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 8. Current state

```text
DECISION_B_METADATA_INPUT_CORRECTION=IDENTIFIED_PENDING_RAW_HASH_BINDING
GRANITE_MISSING_METADATA_PROVIDER_RAW_SHA256_SET=INCOMPLETE_PENDING_RAW_HASH_PROBE
QWEN_MISSING_METADATA_PROVIDER_RAW_SHA256_SET=INCOMPLETE_PENDING_RAW_HASH_PROBE
DIRECTORY_BASENAME_SEMANTIC_INPUT=IDENTIFIED
PR106_PROVIDER_BINDINGS_OTHERWISE_RETAINED=YES
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004_STATE=BLOCKED_PREFLIGHT
```

## Exclusions

This artifact performs no model/source-weight download, model loading, converter execution, model conversion, quantization, inference, benchmark/device execution, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, personnel engagement, payment, or spend. It creates no workflow and consumes no authorized workflow run.
