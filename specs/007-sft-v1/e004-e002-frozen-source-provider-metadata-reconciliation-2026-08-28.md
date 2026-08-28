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

```text
PUBLIC_PROVIDER_METADATA=REMOTE_PROVIDER_REPORTED_EVIDENCE
PUBLIC_PROVIDER_LFS_POINTER=REMOTE_GIT_LFS_POINTER_EVIDENCE
PUBLIC_PROVIDER_XET_METADATA=REMOTE_XET_METADATA_EVIDENCE
PUBLIC_PROVIDER_RESOLVE_HEADER=REMOTE_EXACT_REVISION_HTTP_METADATA
LOCAL_BYTE_VERIFICATION=CRYPTOGRAPHIC_HASH_OVER_LOCALLY_MATERIALIZED_BYTES
```

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
PUBLIC_PROVIDER_SHA256_EQUALS_LOCALLY_RECOMPUTED_SHA256=NO
PUBLIC_PROVIDER_DISPLAY_SIZE_EQUALS_EXACT_INTEGER_BYTES=NO
PUBLIC_PROVIDER_RESOLVE_INTEGER_SIZE_EQUALS_LOCAL_FILE_STAT=NO
```

A provider-reported digest or integer size is provenance evidence. It does not become a locally recomputed digest or local file-size observation by transcription.

## 2. Granite PRIMARY — exact frozen-revision provider state

```text
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
SOURCE_LICENSE=Apache-2.0
SOURCE_WEIGHT_FILE=model.safetensors
```

Exact-revision public metadata surface:

```text
https://huggingface.co/api/models/ibm-granite/granite-4.0-350m-base/tree/a50b46cef21c8a86b15f0496cb794487a78a910b?recursive=true&expand=true
```

Exact-revision resolve surface used only for metadata/headers, not model download:

```text
https://huggingface.co/ibm-granite/granite-4.0-350m-base/resolve/a50b46cef21c8a86b15f0496cb794487a78a910b/model.safetensors
```

Independent exact-head review of the prior PR head queried those exact frozen-revision surfaces and reported:

```text
PUBLIC_PROVIDER_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
PUBLIC_PROVIDER_XET_HASH=ad623156f038ecd3f840ab101a5e3a7e465bce27b2201348c2d8e786d9c54043
PUBLIC_PROVIDER_INTEGER_WEIGHT_BYTES=704786224
INTEGER_SIZE_EVIDENCE_FIELD=X-Linked-Size
```

The exact SHA-256 and Xet values match the already-canonical Decision B conversion-subject preparation record. The exact integer byte count is newly bound provider evidence; it is not a local file observation.

A separate public Hugging Face mirror commit with the same SHA-256 independently exposes the corresponding Git-LFS pointer size `704786224`. That mirror is corroboration only and is not substituted for the IBM frozen-source identity:

```text
CORROBORATING_MIRROR=unsloth/granite-4.0-350m-base@b40bdaac3b7ddf381a937e92302522e55fd1ebfb
CORROBORATING_LFS_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
CORROBORATING_LFS_INTEGER_BYTES=704786224
CORROBORATING_MIRROR_IS_AUTHORIZED_SOURCE_SUBSTITUTE=NO
```

```text
GRANITE_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
GRANITE_PUBLIC_PROVIDER_INTEGER_WEIGHT_BYTES=BOUND
GRANITE_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED=NO
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=NO
```

The frozen-revision tree contains the source-model metadata/tokenizer assets needed for later subject completion, including `config.json`, `generation_config.json`, `merges.txt`, `model.safetensors`, `model.sig`, `special_tokens_map.json`, `tokenizer.json`, `tokenizer_config.json`, and `vocab.json`. This record does not claim an exact local hash set for those non-weight inputs.

## 3. Qwen3 4B CONTROL — exact frozen-revision provider state

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
SOURCE_LICENSE=Apache-2.0
```

Exact-revision provider metadata surface:

```text
https://huggingface.co/api/models/Qwen/Qwen3-4B-Base/tree/906bfd4b4dc7f14ee4320094d8b41684abff8539?recursive=true&expand=true
```

Exact-revision index source:

```text
https://huggingface.co/Qwen/Qwen3-4B-Base/raw/906bfd4b4dc7f14ee4320094d8b41684abff8539/model.safetensors.index.json
```

The frozen tree contains three source-weight shards plus `model.safetensors.index.json`, tokenizer/configuration assets, README, and LICENSE.

## 4. Qwen CONTROL exact provider weight evidence

### Shard 1

```text
FILE=model-00001-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=4c807e2503d68ae373d508689d00a41f4b33f33c2536da97ab81a20caddc1241
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=3957900840
PUBLIC_PROVIDER_XET_HASH=5ce2c21cd6643568258b5f339a1069bd27bc74f4e10db9732bd0795fd67f2c0e
```

### Shard 2

```text
FILE=model-00002-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=f4707585548b2fc75a6b1d732e8465c62040a8699903c32850781beeb9b27826
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=3987450520
PUBLIC_PROVIDER_XET_HASH=06334f44342b0ca51d6a936fd4ddc69b6bef1a52aef8e2887531207afd724ca7
```

### Shard 3

```text
FILE=model-00003-of-00003.safetensors
PUBLIC_PROVIDER_LFS_SHA256=c7b1aa8fb672de2e00423c99876926022e50b18d4f0d140670788510a27f9965
PUBLIC_PROVIDER_LFS_INTEGER_BYTES=99630640
PUBLIC_PROVIDER_XET_HASH=91ccda833766cc1b12e03e1126e75fe5a968f51ae0854c7e90335ab9b0491217
```

The exact provider remote-container byte sum is:

```text
PUBLIC_PROVIDER_LFS_WEIGHT_CONTAINER_BYTES_SUM=8044982000
```

This is only the arithmetic sum of the three exact provider file sizes. It is not a local directory size, tensor-size statement, or runtime-memory estimate.

## 5. Qwen index metadata is a distinct quantity

The exact frozen-revision `model.safetensors.index.json` reports:

```text
PUBLIC_PROVIDER_INDEX_METADATA_TOTAL_SIZE=8045591552
```

```text
INDEX_METADATA_TOTAL_SIZE_EQUALS_REMOTE_CONTAINER_BYTE_SUM=NO_ASSUMPTION
INDEX_METADATA_TOTAL_SIZE_SEMANTICS_INDEPENDENTLY_VALIDATED_BY_THIS_RECORD=NO
```

The provider's index `metadata.total_size` and the remote container-file byte sum differ. Downstream contracts must select the exact intended quantity rather than substitute one for the other. This record infers no defect merely from the difference.

## 6. Decision B subject-field effect

The prior conversion-subject record correctly left local/execution-authoritative integrity fields fail closed. This provider reconciliation narrows only remote-provider metadata:

```text
GRANITE_PUBLIC_PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
GRANITE_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
GRANITE_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256=NEEDS_EVIDENCE
GRANITE_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE

QWEN_PUBLIC_PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=BOUND
QWEN_PUBLIC_PROVIDER_WEIGHT_SHA256_PER_SHARD=BOUND
QWEN_PUBLIC_PROVIDER_XET_HASH_PER_SHARD=BOUND
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=NEEDS_EVIDENCE
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=NEEDS_EVIDENCE
QWEN_EXACT_MODEL_INDEX_SHA256=NEEDS_EVIDENCE
QWEN_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
```

A future execution-authoritative conversion subject still requires the local/integrity fields required by then-current governance. Provider metadata alone does not make either subject executable.

## 7. Prior-head review provenance

The first exact head of this record was:

```text
PR=104
PRIOR_HEAD=37c222b482352e11c6cc8f7e37204375ac549f32
PRIOR_HEAD_RAW_ACTIONS_RUNS=0
```

CodeRabbit independently re-read canonical E001/E002/Decision B records, queried exact frozen-revision Hugging Face API/resolve surfaces, verified every Qwen shard field and arithmetic, verified the Granite SHA-256/Xet identity, obtained the direct Granite `X-Linked-Size: 704786224`, confirmed no local-byte verification claim, and reported no material blocker on that prior head.

This commit changes the record to bind the new Granite exact integer provider evidence. Therefore the prior-head review is historical and a fresh exact-head review is required before merge.

## 8. No authority expansion

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

## 9. Fresh review requirements

Fresh exact-head review must independently verify:

1. the repository/revision identities exactly match canonical E001/E002/Decision B scope;
2. Granite exact frozen-revision metadata reports SHA-256 `a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0`, Xet `ad623156f038ecd3f840ab101a5e3a7e465bce27b2201348c2d8e786d9c54043`, and integer bytes `704786224`;
3. all three Qwen CONTROL SHA-256, Xet, and exact integer byte values are correct at revision `906bfd4b...`;
4. `PUBLIC_PROVIDER_LFS_WEIGHT_CONTAINER_BYTES_SUM=8044982000` is arithmetically correct;
5. Qwen index `metadata.total_size=8045591552` remains distinct from the container-byte sum;
6. provider evidence is not described as locally recomputed evidence;
7. no model bytes were loaded, converted, quantized, inferred, benchmarked, or trained;
8. no workflow-run allowance, conversion authority, training authority, credential authority, procurement, or spend is expanded;
9. raw Actions on the new exact head remain zero.

## 10. Current lifecycle effect

```text
E002_FROZEN_SOURCE_PROVIDER_METADATA_RECONCILIATION=PREPARED_FOR_FINAL_EXACT_HEAD_REVIEW
GRANITE_PROVIDER_INTEGER_WEIGHT_BYTES=BOUND_FOR_REVIEW
QWEN_CONTROL_PROVIDER_SHARD_INTEGER_BYTES=BOUND_FOR_REVIEW
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