# E004 Conversion Toolchain Static Identity — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `e7c83db3c305cc0f98bf04e182249cbd261e5da0`  
**Founder decision:** `ARTIFACT_DECISION_B` canonical via PR #85  
**Artifact class:** static public-source evidence only  
**Authority effect:** NONE  
**Converter build performed:** NO  
**Conversion performed:** NO  
**Model/source-weight acquisition performed by this record:** NO  
**Model execution performed:** NO

This record reduces the remaining conversion-subject ambiguity by binding the exact public source identities for the proposed conversion and quantization toolchain at the already-reviewed `llama.cpp` candidate revision. It does not build the toolchain, freeze an executable, authorize conversion, or claim that source support proves successful conversion or runtime/device qualification.

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
EXACT_CONVERSION_SUBJECT_PREPARATION_AUTHORIZED=YES
CONVERSION_EXECUTION_AUTHORITY=NONE
CONVERTER_BUILD_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Exact proposed upstream source revision

```text
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
REVISION_ROLE=CONVERSION_TOOLCHAIN_SOURCE_CANDIDATE
FINAL_COMMANDMED_INFERENCE_RUNTIME_REVISION=NEEDS_EVIDENCE
```

This revision was already recorded by canonical E004 runtime research as containing the relevant Qwen3 and Granite conversion/runtime source mappings. This record narrows only the conversion-tool source surface.

```text
TOOL_REVISION_EQUALS_BUILT_EXECUTABLE_IDENTITY=NO
TOOL_REVISION_EQUALS_FINAL_INFERENCE_RUNTIME_IDENTITY=NO
SOURCE_SUPPORT_EQUALS_CONVERSION_SUCCESS=NO
SOURCE_SUPPORT_EQUALS_DEVICE_QUALIFICATION=NO
```

## 2. Hugging Face -> GGUF conversion entrypoint

At the exact revision above:

```text
CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
CONVERSION_ENTRYPOINT_GIT_BLOB=78ad26c6563062e2a801c9f76f77a7ce196dd195
CONVERSION_ENTRYPOINT_BYTES=12798
```

Static source inspection establishes that this entrypoint:

- accepts a local model directory as its model argument;
- exposes `--outfile`;
- exposes `--outtype` including `f16`, `bf16`, `q8_0`, and `auto`;
- resolves the model architecture from local Hugging Face configuration;
- writes a GGUF output when executed.

For the Decision B subjects, commandMed proposes the local-directory path only. The script's `--remote` mode is not part of the prepared conversion subject because source acquisition and conversion execution are separate authority/evidence steps.

```text
PREPARED_SUBJECT_SOURCE_MODE=EXACT_LOCAL_DIRECTORY_AFTER_SEPARATE_E002_ACQUISITION_AND_INTEGRITY_VERIFICATION
REMOTE_CONVERSION_MODE_SELECTED=NO
```

No invocation occurred while preparing this evidence.

## 3. Python conversion dependency surface

The exact revision contains:

```text
CONVERSION_REQUIREMENTS_FILE=requirements/requirements-convert_hf_to_gguf.txt
CONVERSION_REQUIREMENTS_GIT_BLOB=b1f7c863e27e184e55408c9e5792158301c86547
CONVERSION_REQUIREMENTS_BYTES=200

LEGACY_REQUIREMENTS_FILE=requirements/requirements-convert_legacy_llama.txt
LEGACY_REQUIREMENTS_GIT_BLOB=28221fad0ce9790f91dc6adfbc893010454bdfe5
LEGACY_REQUIREMENTS_BYTES=102
```

The recorded dependency constraints are:

```text
PYTORCH=torch==2.11.0
NUMPY=numpy~=1.26.4
SENTENCEPIECE=>=0.1.98,<0.3.0
TRANSFORMERS=4.57.6
GGUF=>=0.1.0
PROTOBUF=>=4.21.0,<5.0.0
PYTORCH_INDEX=https://download.pytorch.org/whl/cpu
```

These requirement files are **not an exact dependency lock**. Multiple dependencies permit ranges, and an index URL is mutable. Therefore they cannot satisfy the future reproducible build/environment identity by themselves.

```text
DEPENDENCY_REQUIREMENT_SOURCE_IDENTITY=BOUND_STATICALLY
EXACT_RESOLVED_DEPENDENCY_SET=NEEDS_EVIDENCE
DEPENDENCY_WHEEL_OR_PACKAGE_HASH_SET=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
```

No package installation is authorized or performed by this record.

## 4. Quantization executable source surface

The exact revision defines the `llama-quantize` executable under `tools/quantize/`.

```text
QUANTIZE_CMAKE_FILE=tools/quantize/CMakeLists.txt
QUANTIZE_CMAKE_GIT_BLOB=eead4c859513a6dbb201a71a403d4233f57bbfef
QUANTIZE_CMAKE_BYTES=710

QUANTIZE_MAIN_FILE=tools/quantize/main.cpp
QUANTIZE_MAIN_GIT_BLOB=fc247190c83654544ca68bd6c30181a2aaba7e0a
QUANTIZE_MAIN_BYTES=121

QUANTIZE_IMPLEMENTATION_FILE=tools/quantize/quantize.cpp
QUANTIZE_IMPLEMENTATION_GIT_BLOB=8d03c8fcd4279fd9c70a265b3dafcb95d1a6e43e
QUANTIZE_IMPLEMENTATION_BYTES=27259

QUANTIZE_README_FILE=tools/quantize/README.md
QUANTIZE_README_GIT_BLOB=27384bebf697fec4e22df899fdbc345da4e89e91
QUANTIZE_README_BYTES=12406
```

The exact `CMakeLists.txt` creates the executable target:

```text
CMAKE_EXECUTABLE_TARGET=llama-quantize
CXX_STANDARD=cxx_std_17
LINKS_TO=llama-quantize-impl
```

The source identity is now bounded, but the future executable is not.

```text
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
COMPILER_IDENTITY=NEEDS_EVIDENCE
CMAKE_IDENTITY=NEEDS_EVIDENCE
BUILD_FLAGS=NEEDS_EVIDENCE
BUILD_OUTPUT_PATH=NEEDS_EVIDENCE
```

## 5. Q4_K_M method support at the exact source revision

The exact-revision quantization documentation describes the two-phase path:

```text
SOURCE_MODEL -> HIGH_PRECISION_GGUF -> QUANTIZED_GGUF
```

and explicitly documents `llama-quantize` use with `Q4_K_M` as the quantization type. This supports keeping the prepared Decision B subject policy:

```text
PROPOSED_QUANTIZATION_METHOD=Q4_K_M
PROPOSED_INTERMEDIATE_OUTPUT=HIGH_PRECISION_GGUF
PROPOSED_FINAL_OUTPUT=GGUF_Q4_K_M
```

This is method/CLI support evidence only.

```text
Q4_K_M_SOURCE_SUPPORT_OBSERVED=YES
Q4_K_M_CONVERSION_EXECUTED=NO
Q4_K_M_OUTPUT_BYTES=NEEDS_EVIDENCE
Q4_K_M_OUTPUT_SHA256=NEEDS_EVIDENCE
Q4_K_M_MEDICAL_EQUIVALENCE=NEEDS_EVIDENCE
Q4_K_M_DEVICE_PASS=NEEDS_EVIDENCE
```

The upstream documentation itself notes that quantization may reduce model quality. Therefore commandMed must not infer medical equivalence from successful quantization even after a future conversion succeeds.

## 6. Prepared argv semantics after static source verification

The already-canonical Decision B preparation may retain the following **non-executable** command shapes:

```text
CONVERT_ARGV_SHAPE=
  python3 convert_hf_to_gguf.py \
    --outfile <EXACT_INTERMEDIATE_OUTPUT> \
    --outtype f16 \
    <EXACT_LOCAL_SOURCE_DIRECTORY>

QUANTIZE_ARGV_SHAPE=
  <EXACT_LLAMA_QUANTIZE_EXECUTABLE> \
    <EXACT_INTERMEDIATE_OUTPUT> \
    <EXACT_Q4_K_M_OUTPUT> \
    Q4_K_M
```

The placeholders remain deliberate blockers. They must not be converted to an executable request until each exact identity is bound to verified evidence and separate execution authority exists.

## 7. Remaining exact toolchain blockers

Static public-source research can reduce no further than:

```text
TOOL_REPOSITORY=BOUND
TOOL_REVISION=BOUND
CONVERSION_ENTRYPOINT_SOURCE=BOUND
CONVERSION_REQUIREMENTS_SOURCE=BOUND
QUANTIZE_TARGET_SOURCE=BOUND
Q4_K_M_METHOD_SUPPORT=BOUND

CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
COMPILER_IDENTITY=NEEDS_EVIDENCE
CMAKE_IDENTITY=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
EXACT_RESOLVED_DEPENDENCY_SET=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
BUILD_FLAGS=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
```

Those remaining fields require an exact build/runtime environment and evidence collection. PR #85 explicitly did not grant converter-build or conversion-execution authority, so this record does not attempt either.

## 8. Source-model acquisition boundary remains separate

Canonical E002 authorizes non-executing acquisition and integrity verification of the exact frozen public source-model revisions. Decision B does not replace or widen E002.

```text
SOURCE_MODEL_ACQUISITION_AUTHORITY=E002_FROZEN_PUBLIC_CANDIDATES_ONLY
SOURCE_MODEL_LOCAL_INTEGRITY_EVIDENCE_REQUIRED_BEFORE_CONVERSION=YES
PRECONVERTED_GGUF_ALLOWLIST_EXPANDED_BY_DECISION_B=NO
```

Public Hugging Face metadata recorded in the Decision B preparation is not equivalent to locally materialized byte verification.

```text
PUBLIC_METADATA_SHA256_EQUALS_LOCAL_BYTE_VERIFICATION=NO
LOCAL_SOURCE_BUNDLE_IDENTITY_FOR_GRANITE=NEEDS_EVIDENCE
LOCAL_SOURCE_BUNDLE_IDENTITY_FOR_QWEN_CONTROL=NEEDS_EVIDENCE
```

## 9. Current lifecycle effect

```text
CONVERSION_TOOLCHAIN_STATIC_IDENTITY=PREPARED_FOR_REVIEW
CONVERSION_TOOLCHAIN_EXECUTABLE_IDENTITY=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONVERTER_BUILD_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This record excludes:

- installing converter dependencies;
- cloning/building `llama.cpp` for execution;
- producing or hashing built executables;
- downloading source-model weights as part of this artifact;
- running `convert_hf_to_gguf.py` or `llama-quantize`;
- conversion, quantization, requantization, model loading, inference, benchmark access/execution, device execution, contamination assessment, selection-suite construction, winner selection, training, PHI, Private Gold, gated assets, credentials, provider generation, personnel engagement, procurement, or spend;
- treating Git blob IDs as executable SHA-256 identities;
- treating static support as conversion success or medical equivalence.

## Exit Evidence

This static-evidence artifact is repository-level complete only after exact-head independent review confirms:

```text
EXACT_LLAMA_CPP_SOURCE_REVISION_BOUND=YES
CONVERTER_ENTRYPOINT_SOURCE_IDENTITY_BOUND=YES
CONVERTER_REQUIREMENTS_SOURCE_IDENTITIES_BOUND=YES
DEPENDENCY_RANGES_NOT_MISREPRESENTED_AS_LOCK=YES
LLAMA_QUANTIZE_SOURCE_IDENTITIES_BOUND=YES
Q4_K_M_METHOD_SUPPORT_BOUND=YES
SOURCE_IDENTITIES_NOT_MISREPRESENTED_AS_EXECUTABLE_IDENTITIES=YES
CONVERTER_BUILD_EXECUTION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Canonical merge would close this static source-identity research only. It would not authorize building or executing the converter toolchain.