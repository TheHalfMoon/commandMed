# E004 Conversion Toolchain Build Authority — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `e50f6ca65c23039613318153429030cbdc578c56`  
**Decision owner:** Founder  
**Decision state:** RECORDED_FOR_REVIEW  
**Authority class:** `E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY`  
**Authority effect:** BOUNDED BUILD-EVIDENCE EXECUTION ONLY  
**Model conversion authority:** NONE  
**Model execution authority:** NONE  
**Benchmark/device execution authority expansion:** NONE  
**Training authority:** NONE  
**Spend authority:** USD 0

## 1. Decision capture

Immediately before the Founder response, the following exact bounded decision surface was presented:

```text
PROPOSED_NEXT_FOUNDER_DECISION=E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY

AUTHORIZED_PURPOSE=
  PRODUCE_EXACT_BUILD_AND_EXECUTABLE_IDENTITY_EVIDENCE
  FOR_ARTIFACT_DECISION_B_SUBJECTS_ONLY

TOOL_SOURCE=
  ggml-org/llama.cpp@
  c1d0e7a004015f23bc0233470b747b596f29b264

AUTHORIZED_ACTIONS=
  ACQUIRE_EXACT_TOOL_SOURCE
  RESOLVE_AND_HASH_EXACT_CONVERTER_DEPENDENCIES
  CREATE_ISOLATED_BUILD_ENVIRONMENT
  BUILD_LLAMA_QUANTIZE_ONLY
  HASH_BUILT_EXECUTABLES
  CAPTURE_COMPILER_CMAKE_PYTHON_DEPENDENCY_AND_BUILD_MANIFESTS

MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_INFERENCE=PROHIBITED
MODEL_CONVERSION=PROHIBITED
QUANTIZATION_OF_MODEL_WEIGHTS=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PHI=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
CREDENTIALS=NONE
SPEND_USD=0

OUTPUT_AUTHORITY=BUILD_EVIDENCE_ONLY
OUTPUT_MUST_NOT_BECOME_CONVERSION_AUTHORITY=YES
```

The Founder then responded directly:

```text
FOUNDER_RESPONSE=go ahead
```

Because the response immediately followed the exact authority class, source revision, permitted actions, purpose, and exclusions above, this record captures the bounded build-evidence authority only. It does not reinterpret unrelated historical `go ahead` instructions.

## 2. Exact authorized source scope

```text
BUILD_TOOL_REPOSITORY=ggml-org/llama.cpp
BUILD_TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
BUILD_TARGET=llama-quantize
CONVERTER_ENTRYPOINT=convert_hf_to_gguf.py
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
```

No alternate `llama.cpp` revision, fork, binary release, package-manager build, prebuilt converter, or model artifact is authorized by this record.

## 3. Permitted actions

The build-evidence lane may:

- acquire the exact public `llama.cpp` source revision above into an isolated evidence workspace;
- verify the acquired source revision and source-file identities against the already-canonical static source evidence;
- resolve the exact Python dependency set needed by `convert_hf_to_gguf.py` from the already-bound requirements surface;
- calculate hashes for every resolved converter dependency artifact used by the build/runtime environment;
- create an isolated zero-spend build/runtime environment;
- configure and build `llama-quantize` from the exact authorized source revision;
- hash the resulting `llama-quantize` executable;
- hash the exact Python runtime used for the converter entrypoint;
- capture compiler, CMake, Ninja/build-system, libc/platform, dependency, source-tree, command-line, and environment-manifest identities;
- record failed acquisition/build attempts as evidence when they fail closed before any prohibited operation.

This authority is intentionally sufficient to produce future exact build identities. It is not sufficient to transform any model bytes.

## 4. Explicit prohibitions

```text
SOURCE_MODEL_WEIGHT_ACQUISITION_AUTHORITY_EXPANSION=NONE
MODEL_WEIGHT_LOADING_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_QUALIFICATION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
SELECTION_SUITE_CONSTRUCTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY_USD=0
```

Existing E002 authority for the exact frozen public candidate source artifacts remains separate and unchanged. This build record neither revokes nor widens E002.

## 5. Required build-evidence outputs

A successful build-evidence execution must bind at least:

```text
source_repository
source_revision
source_tree_or_archive_identity
source_file_identity_reconciliation
host_os_identity
host_architecture
kernel_identity
libc_identity
python_runtime_path_and_sha256
python_runtime_version
resolved_python_dependency_set
resolved_python_dependency_artifact_hashes
cmake_path_version_and_sha256
compiler_paths_versions_and_sha256
build_system_path_version_and_sha256
cmake_configuration_argv
build_argv
build_flags
network_access_boundary
credential_state
spend_usd
llama_quantize_output_path
llama_quantize_executable_sha256
build_log_identity
build_environment_manifest_sha256
```

If the exact source or dependency bytes cannot be materialized, the build must not be simulated and no executable identity may be inferred from source metadata.

## 6. Conversion remains separately gated

Even after a successful build:

```text
BUILD_PASS_EQUALS_CONVERSION_EXECUTION_AUTHORITY=NO
BUILT_LLAMA_QUANTIZE_EQUALS_AUTHORIZED_MODEL_TRANSFORMATION=NO
CONVERTER_ENVIRONMENT_READY_EQUALS_MODEL_LOAD_AUTHORITY=NO
CONVERTER_ENVIRONMENT_READY_EQUALS_BENCHMARK_AUTHORITY=NO
```

A later conversion-execution decision must be separately requested against fully populated exact conversion subjects. No conversion request may rely on placeholders or unverified source-model bytes.

## 7. Current lifecycle effect

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Review requirements

Exact-head review must verify:

1. The Founder response is bound only to the immediately preceding exact build-authority proposal.
2. The only build source is `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`.
3. The authority permits source/dependency acquisition and build evidence but no model transformation.
4. `MODEL_CONVERSION_AUTHORITY=NONE` remains explicit.
5. Model loading, inference, benchmark/device execution, contamination assessment, selection-suite construction, training, credentials, procurement, and spend remain prohibited.
6. Any failed materialization/build attempt must fail closed and may not be promoted to PASS evidence.
7. E004 remains `BLOCKED_PREFLIGHT`.

Canonical merge of this record authorizes only the bounded build-evidence lane above.