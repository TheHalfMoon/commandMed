# E004 / E002 Frozen Source Provider Metadata Reconciliation — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `3576e9a02d1b65752967bb676759c1092ed26a08`  
**Authority basis:** canonical E002 public, ungated, frozen-source access authority  
**Artifact class:** static public provider metadata / provenance evidence only  
**Model/source-weight download performed by this record:** NO  
**Model loading performed:** NO  
**Model conversion performed:** NO  
**Model inference performed:** NO  
**Benchmark/device execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

This record advances the source-bundle evidence needed by the already-canonical `ARTIFACT_DECISION_B` conversion subjects without treating provider metadata as local byte verification. It is deliberately limited to the two Decision B source identities:

```text
GRANITE_PRIMARY=
  ibm-granite/granite-4.0-350m-base@
  a50b46cef21c8a86b15f0496cb794487a78a910b

QWEN_CONTROL=
  Qwen/Qwen3-4B-Base@
  906bfd4b4dc7f14ee4320094d8b41684abff8539
```

No other model, revision, artifact family, preconverted GGUF, credentialed source, or fallback is authorized or examined as a Decision B source subject by this record.

## 1. Evidence semantics

The following distinctions are mandatory:

```text
PUBLIC_PROVIDER_METADATA=REMOTE_PROVIDER_REPORTED_EVIDENCE
PUBLIC_PROVIDER_LFS_POINTER=REMOTE_GIT_LFS_POINTER_EVIDENCE
PUBLIC_PROVIDER_XET_METADATA=REMOTE_XET_METADATA_EVIDENCE
LOCAL_BYTE_VERIFICATION=CRYPTOGRAPHIC_HASH_OVER_LOCALLY_MATERIALIZED_BYTES
```

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
PUBLIC_PROVIDER_SHA256_EQUALS_LOCALLY_RECOMPUTED_SHA256=NO
PUBLIC_PROVIDER_DISPLAY_SIZE_EQUALS_EXACT_INTEGER_BYTES=NO
CURRENT_PROVIDER_TREE_HEAD_EQUALS_FROZEN_REVISION_ONLY_WHEN_EXACT_IDENTITY_IS_PROVEN=NO
```

A provider-reported digest is useful provenance evidence but does not become a locally recomputed digest by transcription.

## 2. Granite PRIMARY provider state

Frozen identity:

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
SOURCE_LICENSE=Apache-2.0
```

Current public Hugging Face tree metadata reports the verified repository head prefix `a50b46c`, matching the frozen revision prefix, and exposes this file inventory:

```text
.gitattributes
README.md
config.json
generation_config.json
merges.txt
model.safetensors
model.sig
special_tokens_map.json
tokenizer.json
tokenizer_config.json
vocab.json
```

Provider tree source:

```text
https://huggingface.co/ibm-granite/granite-4.0-350m-base/tree/main
```

The current public weight-file page reports:

```text
SOURCE_WEIGHT_FILE=model.safetensors
PUBLIC_PROVIDER_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
PUBLIC_PROVIDER_XET_HASH=ad623156f038ecd3f840ab101a5e3a7e465bce27b2201348c2d8e786d9c54043
PUBLIC_PROVIDER_DISPLAY_SIZE=705_MB
```

Provider weight source:

```text
https://huggingface.co/ibm-granite/granite-4.0-350m-base/blob/main/model.safetensors
```

The digest/Xet identity matches the already-canonical Decision B preparation record. This reconciliation does not upgrade it to a local-byte digest.

```text
GRANITE_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_DISPLAY_SIZE=BOUND
GRANITE_PUBLIC_PROVIDER_INTEGER_WEIGHT_BYTES=NEEDS_EVIDENCE
GRANITE_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED=NO
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=NO
```

The public tree also reports the following display sizes for relevant non-weight repository files:

```text
config.json=1.76_kB_DISPLAY
merges.txt=917_kB_DISPLAY
model.sig=9.67_kB_DISPLAY
special_tokens_map.json=579_BYTES_DISPLAY
tokenizer.json=7.15_MB_DISPLAY
tokenizer_config.json=17.7_kB_DISPLAY
vocab.json=1.61_MB_DISPLAY
```

Those display values are inventory evidence only, not exact integer byte bindings unless an exact integer value is separately obtained.

## 3. Qwen3 4B CONTROL provider state

Frozen identity:

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
SOURCE_LICENSE=Apache-2.0
```

The exact frozen-revision `config.json` is publicly readable at:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/blob/906bfd4b4dc7f14ee4320094d8b41684abff8539/config.json
```

Current public tree metadata reports verified repository head prefix `906bfd4`, matching the frozen revision prefix, and exposes this inventory:

```text
.gitattributes
LICENSE
README.md
config.json
generation_config.json
merges.txt
model-00001-of-00003.safetensors
model-00002-of-00003.safetensors
model-00003-of-00003.safetensors
model.safetensors.index.json
tokenizer.json
tokenizer_config.json
vocab.json
```

Provider tree source:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/tree/main
```

## 4. Qwen exact public LFS pointer evidence

Hugging Face public Git-LFS blame/pointer surfaces expose exact integer byte sizes for all three frozen CONTROL weight shards.

### Shard 1

```text
FILE=model-00001-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=4c807e2503d68ae373d508689d00a41f4b33f33c2536da97ab81a20caddc1241
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=3957900840
PUBLIC_PROVIDER_XET_HASH=5ce2c21cd6643568258b5f339a1069bd27bc74f4e10db9732bd0795fd67f2c0e
```

Sources:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/blame/main/model-00001-of-00003.safetensors
https://huggingface.co/Qwen/Qwen3-4B-Base/blob/main/model-00001-of-00003.safetensors
```

### Shard 2

```text
FILE=model-00002-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=f4707585548b2fc75a6b1d732e8465c62040a8699903c32850781beeb9b27826
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=3987450520
PUBLIC_PROVIDER_XET_HASH=06334f44342b0ca51d6a936fd4ddc69b6bef1a52aef8e2887531207afd724ca7
```

Sources:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/blame/main/model-00002-of-00003.safetensors
https://huggingface.co/Qwen/Qwen3-4B-Base/blob/main/model-00002-of-00003.safetensors
```

### Shard 3

```text
FILE=model-00003-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=c7b1aa8fb672de2e00423c99876926022e50b18d4f0d140670788510a27f9965
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=99630640
PUBLIC_PROVIDER_XET_HASH=91ccda833766cc1b12e03e1126e75fe5a968f51ae0854c7e90335ab9b0491217
```

Sources:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/blame/main/model-00003-of-00003.safetensors
https://huggingface.co/Qwen/Qwen3-4B-Base/blob/main/model-00003-of-00003.safetensors
```

The exact sum of the three provider LFS remote-file byte counts is:

```text
PUBLIC_PROVIDER_LFS_WEIGHT_CONTAINER_BYTES_SUM=8044982000
```

This is a mathematical sum of the three provider pointer sizes only. It is not a locally observed directory size and is not a model-runtime memory estimate.

## 5. Qwen index metadata is a distinct quantity

The public `model.safetensors.index.json` blame surface reports:

```text
INDEX_FILE=model.safetensors.index.json
PUBLIC_PROVIDER_INDEX_FILE_DISPLAY_BYTES=32819
PUBLIC_PROVIDER_INDEX_METADATA_TOTAL_SIZE=8045591552
```

Source:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/blame/main/model.safetensors.index.json
```

The index `metadata.total_size` value is not silently interpreted as the same semantic quantity as the sum of remote safetensors container-file byte counts.

```text
INDEX_METADATA_TOTAL_SIZE_EQUALS_REMOTE_CONTAINER_BYTE_SUM=NOT_ASSUMED
INDEX_METADATA_TOTAL_SIZE_SEMANTICS_INDEPENDENTLY_VALIDATED_BY_THIS_RECORD=NO
```

Because the two provider-reported quantities differ, downstream code or governance must use the exact field required by the relevant contract rather than substituting one for the other.

No defect is inferred from the difference by this record.

## 6. Decision B subject-field effect

The prior conversion-subject record used fail-closed fields such as:

```text
EXACT_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=NEEDS_EVIDENCE
EXACT_MODEL_INDEX_SHA256=NEEDS_EVIDENCE
EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
```

This provider reconciliation narrows those fields without overstating closure:

```text
QWEN_PUBLIC_PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=BOUND
QWEN_PUBLIC_PROVIDER_WEIGHT_SHA256_PER_SHARD=BOUND
QWEN_PUBLIC_PROVIDER_XET_HASH_PER_SHARD=BOUND
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=NEEDS_EVIDENCE
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=NEEDS_EVIDENCE
QWEN_EXACT_MODEL_INDEX_SHA256=NEEDS_EVIDENCE
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE

GRANITE_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
GRANITE_PUBLIC_PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256=NEEDS_EVIDENCE
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
```

A future execution-authoritative conversion subject still requires the local/integrity fields required by then-current governance. Provider transcription alone does not satisfy those requirements.

## 7. No authority expansion

```text
E002_AUTHORITY=AUTHORIZED_EXISTING_FROZEN_PUBLIC_CANDIDATES_ONLY
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
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This record does not modify or consume the separate one-run GitHub Actions build-evidence allowance.

```text
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 8. Review requirements

Fresh exact-head review must independently verify at least:

1. the repository/revision identities exactly match the canonical E001/E002/Decision B scope;
2. current Hugging Face provider tree prefixes match the frozen revision prefixes but are not misrepresented as a full exact-revision proof;
3. the Granite provider SHA-256/Xet metadata matches the previously canonical preparation record;
4. all three Qwen CONTROL LFS pointer SHA-256 values and exact integer byte counts are correct;
5. all three Qwen Xet hashes are correct;
6. `PUBLIC_PROVIDER_LFS_WEIGHT_CONTAINER_BYTES_SUM=8044982000` is arithmetically correct;
7. the index `metadata.total_size=8045591552` is recorded as a distinct provider field and is not silently equated to remote container bytes;
8. no provider digest or display size is described as a locally recomputed value;
9. no model bytes were loaded, converted, quantized, inferred, benchmarked, or trained;
10. no build workflow allowance, conversion authority, training authority, credential authority, procurement, or spend is expanded.

If an independent reviewer can obtain a trustworthy exact integer provider size for Granite `model.safetensors`, it should report the value and source as a concrete finding. That value must not be inserted by assumption.

## 9. Current lifecycle effect

```text
E002_FROZEN_SOURCE_PROVIDER_METADATA_RECONCILIATION=PREPARED_FOR_REVIEW
QWEN_CONTROL_PROVIDER_SHARD_INTEGER_BYTES=BOUND_FOR_REVIEW
GRANITE_PROVIDER_INTEGER_WEIGHT_BYTES=NEEDS_EVIDENCE
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Canonical merge of this record would close only this provider-metadata reconciliation. It would not close E004, establish a local source bundle, authorize model transformation, or make either conversion subject executable.