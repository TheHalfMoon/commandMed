# E004 Decision B Metadata Input Correction — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base at correction start:** `39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46`  
**Artifact class:** non-executing static correction / provider raw-byte binding  
**Authority effect:** NONE  
**Model/source-weight download by commandMed executor:** NO  
**Model load performed:** NO  
**Converter execution performed:** NO  
**Conversion/quantization performed:** NO  
**Spend:** USD 0

This record corrects the canonical Decision B non-weight input classification after exact pinned-source inspection found metadata inputs omitted from PR #106. An independent reviewer subsequently fetched the three missing small provider files at the exact frozen revisions, computed raw byte counts and SHA-256 values, and returned provider object identities. Those provider-side probes do **not** equal commandMed local source-bundle materialization or local-byte verification.

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

## 1. Pinned source identity and metadata call chain

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

The independent probe verified the selected local path:

```text
ModelBase.write()
 -> prepare_tensors()
 -> prepare_metadata(vocab_only=False)
 -> gguf.Metadata.load(...)
```

The pinned `Metadata.load()` conditionally reads:

```text
README.md
config.json
generation_config.json
```

The pinned metadata heuristic also consumes `model_path.name`, and `ModelBase.prepare_metadata()` may fall back to `self.dir_model.name`. Therefore the local source-directory basename is a semantic conversion input.

```text
METADATA_CALL_CHAIN_VERIFIED=YES
DIRECTORY_BASENAME_IS_SEMANTIC_INPUT=YES
ADDITIONAL_MISSING_SELECTED_METADATA_INPUT=NONE
```

## 2. Correction to PR #106 classifications

The following PR #106 classifications are incomplete and must not be treated as an execution-complete local input set:

```text
PR106_GRANITE_README_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT_FOR_GRANITE
PR106_GRANITE_GENERATION_CONFIG_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT
PR106_QWEN_GENERATION_CONFIG_CLASSIFICATION=NOT_SELECTED_CONVERSION_INPUT
```

Corrected classifications:

```text
GRANITE_README_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
GRANITE_GENERATION_CONFIG_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
QWEN_README_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
QWEN_GENERATION_CONFIG_CLASSIFICATION=OPTIONAL_READ_IF_PRESENT_METADATA_INPUT
```

`OPTIONAL_READ_IF_PRESENT_METADATA_INPUT` means absence is tolerated by pinned source, but when the file exists at the frozen provider revision its exact bytes belong to the deterministic conversion subject and must be identity-bound before execution authorization can be considered. Already-bound `config.json` rows remain required inputs and are not reopened here.

## 3. Bound missing provider-byte identities

Independent reviewer probe evidence was produced from exact `resolve/<frozen-revision>/<path>` bytes. The response header `X-Repo-Commit` matched the requested frozen revision for each row. Hugging Face exposed the 40-hex provider object identity through `ETag` / `X-Linked-Etag`; no Xet identity was exposed for these small files.

### Granite PRIMARY

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
```

| Path | Raw bytes | Raw SHA-256 | Provider OID |
|---|---:|---|---|
| `README.md` | `26418` | `e0786791023161d3f6dbc7e20a4efb278a1ef09a6a0abb9599bdba2e47a89378` | `9b8c0ebb687792889ff8cf9d862302138320cf08` |
| `generation_config.json` | `147` | `7c04cb9d2ba771f7528fba5a7104999cdaf7566d02b5fbd58472829f62716177` | `2eed7ca2d26ec1a753b8800e0bae20c824e8b015` |

### Qwen3-4B CONTROL

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
```

| Path | Raw bytes | Raw SHA-256 | Provider OID |
|---|---:|---|---|
| `generation_config.json` | `138` | `8c970692323e3ea0e9b8b0a4dca79388d31226e41f83c9fd6014804280ebf6e8` | `cbbb3133034e192527e5321b4c679154e4819ab8` |

`README.md` for Qwen was already provider-byte-bound by canonical PR #106 and is retained rather than duplicated here.

```text
THREE_MISSING_PROVIDER_ROWS_PROBED=YES
GRANITE_MISSING_METADATA_PROVIDER_RAW_SHA256_SET=BOUND_PROVIDER_SIDE
QWEN_MISSING_METADATA_PROVIDER_RAW_SHA256_SET=BOUND_PROVIDER_SIDE
PROVIDER_RAW_BYTE_BINDING_EQUALS_LOCAL_SOURCE_MATERIALIZATION=NO
```

## 4. Exact local-directory basename policy

The same frozen provider bytes under a different local directory basename can change converter-derived GGUF metadata. The subject therefore freezes the repository leaf names as semantic basenames:

```text
GRANITE_REQUIRED_DIRECTORY_BASENAME=granite-4.0-350m-base
QWEN_REQUIRED_DIRECTORY_BASENAME=Qwen3-4B-Base
DIRECTORY_BASENAME_NORMALIZATION=PROHIBITED
HASH_OR_RANDOM_BASENAME_SUBSTITUTION=PROHIBITED
EXACT_LOCAL_SOURCE_DIRECTORY_PARENT=NEEDS_EVIDENCE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
```

This basename binding does not grant source acquisition, storage provisioning, model loading, or conversion authority.

## 5. Metadata / normalization policy implication

The pinned converter parses source metadata and applies converter-defined mappings and heuristics; it does not byte-copy all source metadata into GGUF.

```text
SOURCE_BYTES=IMMUTABLE_EXACT_FROZEN_REVISION_PROVIDER_IDENTITIES
SOURCE_DIRECTORY_BASENAME=IMMUTABLE_SEMANTIC_INPUT
CONVERTER_DEFINED_METADATA_MAPPING=PINNED_SOURCE_BEHAVIOR_ONLY
COMMANDMED_MANUAL_METADATA_MUTATION=PROHIBITED
METADATA_OVERRIDE_FILE=NOT_SELECTED
MODEL_NAME_OVERRIDE=NOT_SELECTED
REMOTE_HF_MODEL_ID=NOT_SELECTED
SOURCE_FILE_PREPROCESSING_BY_COMMANDMED=PROHIBITED
CONVERTER_INTERNAL_PARSE_NORMALIZATION=PERMITTED_ONLY_AS_IMPLEMENTED_BY_PINNED_SOURCE
METADATA_HEURISTIC_BYPASS=PROHIBITED
```

The pinned model-card parser includes internal parse normalization before YAML decoding. That implementation behavior is not authority for commandMed to alter source bytes before conversion.

This correction closes the missing **provider-side metadata-input identity** gap only. It does not by itself establish the final `NORMALIZATION_OR_METADATA_POLICY`, because exact installed runtime/dependency identity, local source materialization, exact local directory identity, and any execution-authoritative environment remain unresolved.

## 6. Probe provenance and review lifecycle

Historical probe heads remain non-merge evidence:

```text
INITIAL_PROBE_HEAD=2a146fae2222588880d86d4cb434a683696db3d1
SECOND_PROBE_HEAD=5d9514e5a1e49ea775780730fd54b9efcb4c0c72
SECOND_PROBE_RAW_ACTIONS_RUNS=0
SECOND_PROBE_CURRENT_HEAD_ELIGIBLE_FOR_MERGE=NO
```

The independent probe on `5d9514e5a1e49ea775780730fd54b9efcb4c0c72` returned:

```text
METADATA_CALL_CHAIN_VERIFIED=YES
THREE_MISSING_PROVIDER_ROWS_PROBED=YES
DIRECTORY_BASENAME_IS_SEMANTIC_INPUT=YES
ADDITIONAL_MISSING_SELECTED_METADATA_INPUT=NONE
RAW_ACTIONS_RUNS_ON_EXACT_HEAD=0
```

This hash-bound update creates a new head and therefore **must receive a fresh exact-head review**. The probe verdict cannot qualify this new head.

```text
REVIEWER_HASH_PROBE_REQUIRED=NO_COMPLETED
POST_HASH_BINDING_FRESH_EXACT_HEAD_REVIEW_REQUIRED=YES
CURRENT_HASH_BOUND_HEAD_REVIEW_STATE=PENDING
REVIEW_SERVICE_UNAVAILABLE_EQUALS_REVIEW_PASS=NO
```

## 7. Fail-closed boundaries

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
REVIEWER_RAW_DOWNLOAD_EQUALS_COMMANDMED_LOCAL_SOURCE_BUNDLE_MATERIALIZATION=NO
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
MODEL_SOURCE_WEIGHT_LOCAL_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
NORMALIZATION_OR_METADATA_POLICY=INCOMPLETE_PENDING_RUNTIME_AND_LOCAL_BINDINGS
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
DECISION_B_METADATA_INPUT_CORRECTION=HASH_BOUND_PENDING_FRESH_EXACT_HEAD_REVIEW
GRANITE_METADATA_PROVIDER_RAW_SHA256_SET=BOUND_PROVIDER_SIDE
QWEN_METADATA_PROVIDER_RAW_SHA256_SET=BOUND_PROVIDER_SIDE
DIRECTORY_BASENAME_SEMANTIC_INPUT=BOUND_STATIC_POLICY
PR106_PROVIDER_BINDINGS_OTHERWISE_RETAINED=YES
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004_STATE=BLOCKED_PREFLIGHT
```

## Exclusions

This artifact performs no commandMed model/source-weight download, model loading, converter execution, model conversion, quantization, inference, benchmark/device execution, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, personnel engagement, payment, or spend. It creates no workflow and consumes no authorized workflow run.
