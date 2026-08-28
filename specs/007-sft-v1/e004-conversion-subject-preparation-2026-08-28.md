# E004 Exact Conversion Subject Preparation — 2026-08-28

**Spec:** 007 SFT V1  
**Decision record:** `e004-founder-artifact-decision-b-2026-08-28.md`  
**Artifact class:** non-executing exact-subject preparation  
**Authority effect:** NONE beyond already-recorded preparation scope  
**Conversion execution performed:** NO  
**Converter build performed:** NO  
**Model/source-weight download performed:** NO  
**Model inference performed:** NO

This record prepares two independently reviewable conversion subjects under the bounded Founder `ARTIFACT_DECISION_B` response. It uses immutable public metadata and canonical repository research only. Required execution-derived fields remain `NEEDS_EVIDENCE`, therefore neither subject is executable.

```text
SUBJECT_COUNT=2
SUBJECT_1=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
SUBJECT_2=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
SUBJECTS_EXECUTABLE_NOW=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Shared proposed converter source identity

Canonical commandMed runtime research already established that exact upstream source commit `c1d0e7a004015f23bc0233470b747b596f29b264` contains the Qwen3 implementation mapping and the Granite `GraniteMoeHybridForCausalLM -> GraniteHybridModel -> GRANITE_HYBRID` converter mapping while preserving the product-topology distinction for the frozen dense Granite candidate.

```text
CONVERSION_TOOL_REPOSITORY=ggml-org/llama.cpp
PROPOSED_CONVERSION_TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
PROPOSED_CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
PROPOSED_QUANTIZATION_ENTRYPOINT=llama-quantize
PROPOSED_QUANTIZATION_METHOD=Q4_K_M
PROPOSED_INTERMEDIATE_FORMAT=GGUF_UNQUANTIZED
PROPOSED_FINAL_FORMAT=GGUF_Q4_K_M
```

This exact source commit is a review candidate for conversion tooling only. Selecting it here does not freeze it as the final commandMed inference runtime or device runtime.

```text
CONVERSION_TOOL_REVISION_EQUALS_FINAL_INFERENCE_RUNTIME_REVISION=NO
CONVERSION_TOOL_SOURCE_SUPPORT_PROVES_CONVERSION_SUCCESS=NO
CONVERSION_TOOL_SOURCE_SUPPORT_PROVES_DEVICE_PASS=NO
```

Before any conversion execution, the built/runtime identity must still be frozen:

```text
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
```

## 2. Subject 1 — Granite PRIMARY

```text
SUBJECT_ID=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
ROLE=PRIMARY
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
SOURCE_LICENSE=Apache-2.0
SOURCE_WEIGHT_FILE=model.safetensors
SOURCE_WEIGHT_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
SOURCE_WEIGHT_XET_HASH=ad623156f038ecd3f840ab101a5e3a7e465bce27b2201348c2d8e786d9c54043
SOURCE_WEIGHT_PUBLIC_SIZE=705_MB_DISPLAY_VALUE
```

Public Hugging Face metadata at the frozen repository revision identifies the model repository as Apache-2.0 and the source tree contains `model.safetensors` plus tokenizer/configuration assets. Public file metadata reports the SHA-256 above for the weight file.

The converter architecture naming remains deliberately separated from product topology:

```text
FROZEN_PRODUCT=granite-4.0-350m-base
FROZEN_PRODUCT_TOPOLOGY=DENSE_ALL_ATTENTION
HF_ARCHITECTURE_CLASS=GraniteMoeHybridForCausalLM
LLAMA_CPP_CONVERTER_ARCH=GRANITE_HYBRID
SCREENED_OUT_DISTINCT_PRODUCT=granite-4.0-h-350m-base
CONVERTER_ARCH_NAME_EQUALS_SCREENED_OUT_PRODUCT=NO
```

### Proposed conversion policy

```text
INTERMEDIATE_OUTPUT_FILENAME=granite-4.0-350m-base-a50b46c-f16.gguf
FINAL_OUTPUT_FILENAME=granite-4.0-350m-base-a50b46c-Q4_K_M.gguf
QUANTIZATION_METHOD=Q4_K_M
PRIMARY_PACKAGE_HARD_CAP_BYTES=734003200
PRIMARY_PACKAGE_TARGET_BYTES=629145600
PRIMARY_PACKAGE_STRETCH_BYTES=524288000
PRIMARY_PACKAGE_HARD_CAP_REMAINS_NONCOMPENSABLE=YES
```

The public first-party Granite Q4_K_M artifact previously observed by commandMed is evidence that a Q4_K_M product exists, but it is not lineage proof for this proposed exact-source conversion and is not reused as output evidence.

### Proposed argv shape — not executable authority

```text
CONVERT_ARGV_PROPOSAL=
  python3 convert_hf_to_gguf.py \
    --outfile granite-4.0-350m-base-a50b46c-f16.gguf \
    --outtype f16 \
    <EXACT_LOCAL_SOURCE_DIRECTORY>

QUANTIZE_ARGV_PROPOSAL=
  ./llama-quantize \
    granite-4.0-350m-base-a50b46c-f16.gguf \
    granite-4.0-350m-base-a50b46c-Q4_K_M.gguf \
    Q4_K_M
```

`<EXACT_LOCAL_SOURCE_DIRECTORY>` is deliberately unresolved because no source-weight acquisition or storage location is authorized by this preparation record.

### Granite blockers before execution authorization

```text
EXACT_SOURCE_DIRECTORY_OR_CONTENT_ADDRESS=NEEDS_EVIDENCE
EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
EXACT_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
NETWORK_BOUNDARY=NEEDS_EVIDENCE
CREDENTIAL_STATE=NEEDS_EVIDENCE_EXPECTED_NONE
STORAGE_AND_RETENTION_POLICY=NEEDS_EVIDENCE
EXPECTED_ZERO_SPEND_RESOURCE_ENVELOPE=NEEDS_EVIDENCE
NORMALIZATION_OR_METADATA_POLICY=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 3. Subject 2 — Qwen3 4B CONTROL

```text
SUBJECT_ID=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
SOURCE_LICENSE=Apache-2.0
```

Frozen-source weight identities prepared from public Hugging Face metadata:

| Source weight file | SHA-256 | Xet hash | Public size display |
|---|---|---|---|
| `model-00001-of-00003.safetensors` | `4c807e2503d68ae373d508689d00a41f4b33f33c2536da97ab81a20caddc1241` | `5ce2c21cd6643568258b5f339a1069bd27bc74f4e10db9732bd0795fd67f2c0e` | `3.96 GB` |
| `model-00002-of-00003.safetensors` | `f4707585548b2fc75a6b1d732e8465c62040a8699903c32850781beeb9b27826` | `06334f44342b0ca51d6a936fd4ddc69b6bef1a52aef8e2887531207afd724ca7` | `3.99 GB` |
| `model-00003-of-00003.safetensors` | `c7b1aa8fb672de2e00423c99876926022e50b18d4f0d140670788510a27f9965` | `91ccda833766cc1b12e03e1126e75fe5a968f51ae0854c7e90335ab9b0491217` | `99.6 MB` |

The frozen revision tree also includes `model.safetensors.index.json`, tokenizer, merges, vocab, config, and generation metadata. Their exact content hashes remain to be bound before execution; this record does not infer them from filenames.

### Proposed conversion policy

```text
INTERMEDIATE_OUTPUT_FILENAME=qwen3-4b-base-906bfd4-f16.gguf
FINAL_OUTPUT_FILENAME=qwen3-4b-base-906bfd4-Q4_K_M.gguf
QUANTIZATION_METHOD=Q4_K_M
CONTROL_PRIMARY_PACKAGE_HARD_CAP_APPLIES=NO
CONTROL_OTHER_DEVICE_PREEXECUTION_IDENTITY_REQUIREMENTS_APPLY=YES
```

### Proposed argv shape — not executable authority

```text
CONVERT_ARGV_PROPOSAL=
  python3 convert_hf_to_gguf.py \
    --outfile qwen3-4b-base-906bfd4-f16.gguf \
    --outtype f16 \
    <EXACT_LOCAL_SOURCE_DIRECTORY>

QUANTIZE_ARGV_PROPOSAL=
  ./llama-quantize \
    qwen3-4b-base-906bfd4-f16.gguf \
    qwen3-4b-base-906bfd4-Q4_K_M.gguf \
    Q4_K_M
```

### Qwen CONTROL blockers before execution authorization

```text
EXACT_SOURCE_DIRECTORY_OR_CONTENT_ADDRESS=NEEDS_EVIDENCE
EXACT_MODEL_INDEX_SHA256=NEEDS_EVIDENCE
EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
EXACT_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
NETWORK_BOUNDARY=NEEDS_EVIDENCE
CREDENTIAL_STATE=NEEDS_EVIDENCE_EXPECTED_NONE
STORAGE_AND_RETENTION_POLICY=NEEDS_EVIDENCE
EXPECTED_ZERO_SPEND_RESOURCE_ENVELOPE=NEEDS_EVIDENCE
NORMALIZATION_OR_METADATA_POLICY=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 4. Proposed common execution boundary

The following boundary is proposed for later exact authorization, not granted here:

```text
PURPOSE=E004_FROZEN_TOURNAMENT_ARTIFACT_PREPARATION_ONLY
NETWORK_POLICY=DEFAULT_DENY_AFTER_EXACT_INPUT_ACQUISITION
CREDENTIALS=NONE_EXPECTED_FOR_PUBLIC_UNGATED_INPUTS
PROVIDER_API_USE=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED_DURING_CONVERSION
TRAINING_OR_ADAPTATION=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PHI=PROHIBITED
SPEND_USD=0
```

Any actual source-weight acquisition remains governed by then-current E002/Founder authority and exact storage/access boundaries; this preparation record does not expand byte-access authority.

## 5. Review questions

Exact-head review should verify:

1. The Founder decision is represented as preparation-only, not conversion execution authority.
2. Both source revisions exactly match the frozen E001 manifest.
3. Public weight SHA-256 metadata is recorded without claiming local verification.
4. `c1d0e7a...` is treated as a proposed conversion-tool revision, not the final commandMed inference runtime.
5. Granite product topology is not confused with llama.cpp converter architecture naming.
6. Q4_K_M is a proposed exact conversion policy and does not claim post-conversion package/device PASS.
7. Placeholder-bearing argv remains non-executable and cannot be mistaken for an active execution manifest.
8. Every execution-derived identity remains `NEEDS_EVIDENCE`.
9. No source-weight download, build, conversion, inference, benchmark, device run, training, credential use, personnel action, or spend is authorized or claimed.

## 6. Current state

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
EXACT_CONVERSION_SUBJECT_PREPARATION_AUTHORIZED=YES
GRANITE_SUBJECT=PREPARED_INCOMPLETE_NOT_EXECUTABLE
QWEN_CONTROL_SUBJECT=PREPARED_INCOMPLETE_NOT_EXECUTABLE
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This artifact excludes model/source-weight/GGUF downloads, converter builds, conversion execution, model loading, inference, benchmark access/execution, device execution, contamination assessment, selection-suite construction, winner selection, training, PHI, Private Gold, gated assets, credentials, provider generation, procurement, personnel engagement, and spend.

## Exit Evidence

Repository-level completion of this preparation artifact requires exact-head review with no unresolved material finding, bounded documentation-only diff verification, and canonical merge. Such closure means only that two exact conversion subjects have been prepared as far as public/repository evidence permits. It does not make either subject executable and does not grant conversion authority.