# E004 Runtime Candidate Metadata Research — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `32006088b24b93973ce4624ff99971135d586e9e`  
**Artifact class:** read-only public-source runtime candidate research  
**Authority effect:** NONE  
**Runtime selection performed:** NO  
**Runtime/build download performed:** NO  
**Build performed:** NO  
**Model/GGUF download performed:** NO  
**Model/device execution performed:** NO

This record narrows the E004 runtime-identity research surface by binding current immutable upstream `llama.cpp` metadata that is relevant to the frozen E001 candidate families and target-platform planning. It is compatibility and provenance research only. It does **not** freeze a commandMed runtime revision, wrapper, build toolchain, binary, device plan, or execution manifest.

```text
RUNTIME_CANDIDATE_RESEARCH_ONLY=YES
FINAL_LLAMA_CPP_CORE_REVISION=NEEDS_EVIDENCE
FINAL_RUNTIME_ARTIFACT_SHA256=NEEDS_EVIDENCE
FINAL_BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
FINAL_WRAPPER_IDENTITIES=NEEDS_EVIDENCE
DEVICE_QUALIFICATION=NOT_STARTED
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Upstream stable source candidate

On 2026-08-27 the latest stable `ggml-org/llama.cpp` release observed through the GitHub release API is:

```text
UPSTREAM_REPOSITORY=ggml-org/llama.cpp
STABLE_RELEASE_TAG=v0.3.0
STABLE_RELEASE_PUBLISHED_AT=2026-08-25T10:22:58Z
STABLE_SOURCE_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
STABLE_SOURCE_COMMIT_IS_COMMANDMED_RUNTIME_FREEZE=NO
```

Primary public evidence:

- `https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0`
- `https://github.com/ggml-org/llama.cpp/commit/c1d0e7a004015f23bc0233470b747b596f29b264`

The stable release provides a useful immutable **source candidate identity**. Current availability or recency alone does not make it the commandMed execution revision.

```text
LATEST_STABLE_EQUALS_AUTOMATIC_RUNTIME_SELECTION=NO
SOURCE_COMMIT_SUPPORT_EQUALS_DEVICE_PASS=NO
SOURCE_COMMIT_SUPPORT_EQUALS_FINAL_BUILD_IDENTITY=NO
```

## 2. Frozen candidate architecture coverage at the exact stable commit

At exact source commit `c1d0e7a004015f23bc0233470b747b596f29b264`, `src/llama-model.cpp` contains explicit model mappings for the architecture families needed by the current frozen E001 candidates:

```text
QWEN3_ARCH_MAPPING=LLM_ARCH_QWEN3 -> llama_model_qwen3
QWEN35_ARCH_MAPPING=LLM_ARCH_QWEN35 -> llama_model_qwen35
GRANITE_HYBRID_ARCH_MAPPING=LLM_ARCH_GRANITE_HYBRID -> llama_model_granite_hybrid
```

Primary public evidence:

`https://github.com/ggml-org/llama.cpp/blob/c1d0e7a004015f23bc0233470b747b596f29b264/src/llama-model.cpp`

This supplies architecture-level feasibility evidence for:

```text
Qwen/Qwen3-0.6B-Base
Qwen/Qwen3-4B-Base
Qwen/Qwen3.5-0.8B-Base
ibm-granite/granite-4.0-350m-base
```

It does not prove that a particular GGUF artifact, quantization, wrapper, build, OS/backend, or physical device path is correct or performant.

## 3. Qwen3.5 direct upstream usage evidence

The exact stable README at `c1d0e7a...` uses Qwen3.5 directly in its Quick Start examples:

```text
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF
```

Primary public evidence:

`https://github.com/ggml-org/llama.cpp/blob/c1d0e7a004015f23bc0233470b747b596f29b264/README.md`

This is strong current ecosystem-compatibility evidence for the Qwen3.5 architecture family. It is not evidence that the commandMed frozen exact-base artifact is the same repository/file, and it grants no artifact-access or execution authority.

## 4. Platform-family support metadata

The exact stable README describes upstream support or build documentation relevant to the frozen commandMed platform classes, including:

```text
APPLE_SILICON=FIRST_CLASS_CITIZEN_WITH_ARM_NEON_ACCELERATE_METAL
X86_ARCHITECTURE=AVX_AVX2_AVX512_AMX_SUPPORT_DECLARED
ANDROID_BUILD_DOCUMENTATION=PRESENT
METAL_BACKEND=PRESENT
VULKAN_BACKEND=PRESENT
OPENCL_BACKEND=PRESENT
SYCL_BACKEND=PRESENT
```

These statements establish upstream capability families, not exact commandMed platform wrappers or measurement identities.

```text
UPSTREAM_PLATFORM_SUPPORT_EQUALS_FROZEN_TARGET_BINDING=NO
UPSTREAM_BACKEND_SUPPORT_EQUALS_PERFORMANCE_THRESHOLD_PASS=NO
UPSTREAM_BACKEND_SUPPORT_EQUALS_MEMORY_GATE_PASS=NO
```

## 5. Build/release identity candidate sharing the stable source commit

The upstream prerelease/nightly tag `b10621` points to the same exact source commit as `v0.3.0`:

```text
UPSTREAM_BUILD_TAG=b10621
UPSTREAM_BUILD_PRERELEASE=YES
UPSTREAM_BUILD_TARGET_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
UPSTREAM_BUILD_PUBLISHED_AT=2026-08-25T10:17:02Z
```

The release publishes immutable asset digests. Representative assets relevant to commandMed platform research include:

| Upstream asset | Exact bytes | Published SHA-256 | Research implication |
|---|---:|---|---|
| `llama-b10621-bin-android-arm64.tar.gz` | 72431960 | `050b7bc2ba0bcc66be790be6741bce1e75247a635469093c6328ebc90a95762e` | Android arm64 binary provenance candidate only |
| `llama-b10621-bin-macos-arm64.tar.gz` | 10954823 | `429c8270608600188035e5e92f7d78dffb7900904fe7dd7e6a84f48068cd13cf` | macOS arm64 binary provenance candidate only |
| `llama-b10621-bin-ubuntu-x64.tar.gz` | 16291771 | `91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583` | Linux x64 binary provenance candidate only |
| `llama-b10621-bin-win-cpu-x64.zip` | 18068018 | `0e8b65e650e369f70f8307d890508886f171ef4fb00facccddd4a1b7ffdaca51` | Windows x64 CPU binary provenance candidate only |
| `llama-b10621-xcframework.zip` | 80871640 | `ea50671b3dfe86136be16448763f94642c53443df96964777b4e1c3d51f06e20` | Apple/XCFramework packaging candidate only |

Primary public evidence:

`https://github.com/ggml-org/llama.cpp/releases/tag/b10621`

No listed asset was downloaded or executed while creating this record.

The published assets are **not** automatically suitable commandMed runtime artifacts because final qualification still requires exact wrapper/toolchain/backend/build configuration, runtime executable identity, platform/device mapping, and reproducible commandMed execution-plan evidence.

## 6. Source revision versus runtime artifact identity

The canonical device contract requires both the shared llama.cpp core revision and target-specific runtime/build identities. Therefore this research distinguishes:

```text
SOURCE_CANDIDATE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
SOURCE_CANDIDATE_EVIDENCE_STATE=PUBLIC_IMMUTABLE_METADATA_BOUND
FINAL_LLAMA_CPP_CORE_REVISION=NEEDS_EVIDENCE
FINAL_BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
FINAL_RUNTIME_ARTIFACT_SHA256=NEEDS_EVIDENCE
FINAL_PLATFORM_WRAPPER_IDENTITIES=NEEDS_EVIDENCE
FINAL_BACKEND_CONFIGURATION=NEEDS_EVIDENCE
```

A future exact runtime-binding decision may adopt this source commit, a later commit, or another justified exact revision only under the frozen pre-result protocol and review requirements. The decision must not be based on observed candidate scores or device results.

## 7. Backend/regression caveat

Architecture support is necessary but insufficient. The commandMed repository already treats immutable runtime identity and device execution as hard evidence because backend/model combinations can regress between builds.

This record therefore adopts the following conservative interpretation:

```text
ARCHITECTURE_MAPPING_PROVES_LOAD_PATH_EXISTS_IN_SOURCE=BOUNDED_YES
ARCHITECTURE_MAPPING_PROVES_EXACT_GGUF_LOAD_SUCCESS=NO
ARCHITECTURE_MAPPING_PROVES_TARGET_DEVICE_STABILITY=NO
ARCHITECTURE_MAPPING_PROVES_MEMORY_LATENCY_THERMAL_ENERGY_PASS=NO
UPSTREAM_PREBUILT_ASSET_PROVES_COMMANDMED_WRAPPER_IDENTITY=NO
```

Only real, separately authorized exact-artifact/device evidence can close those fields.

## 8. Current runtime evidence reduction

Before this research, the runtime family was known but an immediately reviewable immutable current candidate was not bound in one E004 record. This document safely reduces that ambiguity to:

```text
CURRENT_UPSTREAM_STABLE_SOURCE_CANDIDATE=c1d0e7a004015f23bc0233470b747b596f29b264
CURRENT_MATCHING_UPSTREAM_BUILD_TAG=b10621
ALL_FROZEN_MODEL_ARCH_FAMILIES_HAVE_SOURCE_MAPPINGS_AT_CANDIDATE=YES
MULTIPLE_RELEVANT_PLATFORM_BUILD_ARTIFACTS_HAVE_PUBLISHED_SHA256=YES
COMMANDMED_FINAL_RUNTIME_SELECTION_MADE=NO
COMMANDMED_RUNTIME_EXECUTION_READY=NO
```

Remaining runtime evidence cannot be completed by read-only public metadata alone. It requires a separately reviewed exact commandMed runtime/build/wrapper/target binding before execution.

## Exclusions

This bounded research explicitly excludes:

- selecting or freezing `c1d0e7a...`, `b10621`, or any other source/build as the commandMed final runtime;
- downloading or executing upstream binaries, source builds, models, GGUF files, benchmarks, or device workloads;
- selecting Metal/Vulkan/OpenCL/SYCL/CPU or any other backend for a frozen target;
- constructing target wrappers, resolving toolchains, choosing measurement methods, or setting performance thresholds;
- changing E001 candidates, E002 artifact authority, E003 execution authority, the PR #81 artifact/A11 authority state, the PR #83 evidence-intake state, A7/A13/A14 state, A15 state, E004 completion, E005 winner selection, training authority, or spend;
- treating public upstream support statements as device qualification.

## Exit Evidence

This **research artifact** is eligible for repository-level closure when one exact head proves:

```text
IMMUTABLE_STABLE_SOURCE_CANDIDATE_RECORDED=YES
EXACT_SOURCE_ARCHITECTURE_MAPPINGS_RECORDED=YES
MATCHING_BUILD_TAG_AND_SELECTED_PUBLIC_ASSET_DIGESTS_RECORDED=YES
NO_RUNTIME_SELECTION_OR_EXECUTION_CLAIMED=YES
FINAL_RUNTIME_AND_BUILD_FIELDS_REMAIN_NEEDS_EVIDENCE=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Repository closure of this research record does not close any runtime/device gate. It closes only the bounded public-metadata research step.