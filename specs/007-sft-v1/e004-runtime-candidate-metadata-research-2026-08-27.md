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

This record narrows the E004 runtime-identity research surface using exact public metadata. It does not freeze a commandMed runtime revision, binary, wrapper, toolchain, backend, device plan, or execution manifest.

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

## 1. Exact upstream source candidate

On 2026-08-27, GitHub release metadata for `ggml-org/llama.cpp` identified stable release `v0.3.0` at exact source commit:

```text
UPSTREAM_REPOSITORY=ggml-org/llama.cpp
OBSERVED_STABLE_RELEASE_TAG=v0.3.0
OBSERVED_STABLE_RELEASE_PUBLISHED_AT=2026-08-25T10:22:58Z
EXACT_SOURCE_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
RELEASE_TAG_IS_COMMANDMED_IDENTITY_AUTHORITY=NO
EXACT_SOURCE_COMMIT_IS_COMMANDMED_RUNTIME_FREEZE=NO
```

The commit SHA is the exact source identity used by this research. Release/tag labels remain descriptive discovery handles only.

## 2. Qwen architecture implementation presence

At exact source commit `c1d0e7a004015f23bc0233470b747b596f29b264`, `src/llama-model.cpp` contains:

```text
QWEN3_ARCH_MAPPING=LLM_ARCH_QWEN3 -> llama_model_qwen3
QWEN35_ARCH_MAPPING=LLM_ARCH_QWEN35 -> llama_model_qwen35
```

These mappings are relevant to the frozen candidates:

```text
Qwen/Qwen3-0.6B-Base
Qwen/Qwen3-4B-Base
Qwen/Qwen3.5-0.8B-Base
```

They prove only that the exact upstream source contains the corresponding architecture implementations. They do not prove exact GGUF loading, tokenizer/rendering correctness, backend stability, device compatibility, or any commandMed hard-gate PASS.

## 3. Granite naming ambiguity resolved explicitly

The frozen candidate is:

```text
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
```

Canonical E001 research classifies this product variant as the **350M dense** PRIMARY and separately identifies `granite-4.0-h-350m-base` as the screened-out hybrid Mamba2 product variant.

The frozen/public IBM configuration for `granite-4.0-350m-base` nevertheless uses the Transformers implementation class and model type:

```text
HF_ARCHITECTURES=[GraniteMoeHybridForCausalLM]
HF_MODEL_TYPE=granitemoehybrid
HF_LAYER_TYPES=ALL_ATTENTION
HF_NUM_LOCAL_EXPERTS=0
HF_NUM_EXPERTS_PER_TOK=0
```

The all-attention / zero-expert fields are consistent with IBM's model-card description of this product as a dense transformer. Therefore the word `Hybrid` in the Transformers class name must not be used as a product-topology classification by commandMed.

At exact llama.cpp source commit `c1d0e7a...`, `conversion/granite.py` registers:

```text
TRANSFORMERS_CLASS=GraniteMoeHybridForCausalLM
LLAMA_CPP_CONVERTER_CLASS=GraniteHybridModel
GGUF_MODEL_ARCH=GRANITE_HYBRID
```

And `src/llama-model.cpp` contains:

```text
LLM_ARCH_GRANITE_HYBRID -> llama_model_granite_hybrid
```

Accordingly, the bounded claim is:

```text
FROZEN_GRANITE_PRODUCT_TOPOLOGY=DENSE_ALL_ATTENTION
LLAMA_CPP_CONVERTER_ARCH_NAME_FOR_FROZEN_HF_CLASS=GRANITE_HYBRID
DISTINCT_H_PRODUCT_VARIANT_ADMITTED=NO
CONVERTER_ARCH_NAME_EQUALS_PRODUCT_H_VARIANT=NO
EXACT_GGUF_LOAD_SUCCESS_PROVEN=NO
```

This resolves the naming ambiguity without claiming that the admitted dense PRIMARY is the screened-out `-h-` model.

## 4. Qwen3.5 direct upstream usage evidence

The exact upstream README at `c1d0e7a...` includes Qwen3.5 quick-start examples using `ggml-org/Qwen3.5-0.8B-GGUF`. This is ecosystem-usage evidence for the architecture family only. It does not prove identity equivalence with the commandMed frozen exact-base artifact and grants no artifact or execution authority.

## 5. Platform-family metadata

The exact upstream README documents capability/build families relevant to commandMed planning, including Apple Silicon, x86, Android, Metal, Vulkan, OpenCL, and SYCL.

```text
UPSTREAM_PLATFORM_SUPPORT_EQUALS_FROZEN_TARGET_BINDING=NO
UPSTREAM_BACKEND_SUPPORT_EQUALS_MEMORY_PASS=NO
UPSTREAM_BACKEND_SUPPORT_EQUALS_PERFORMANCE_PASS=NO
```

## 6. Observed build metadata sharing the source commit

GitHub release metadata for prerelease/nightly tag `b10621` was observed pointing to the same exact source commit `c1d0e7a...`.

```text
OBSERVED_BUILD_TAG=b10621
OBSERVED_BUILD_PRERELEASE=YES
OBSERVED_BUILD_TARGET_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
BUILD_TAG_IS_COMMANDMED_RUNTIME_IDENTITY=NO
```

Representative observed release-asset metadata:

| Upstream asset | Bytes observed | SHA-256 reported by GitHub | Scope |
|---|---:|---|---|
| `llama-b10621-bin-android-arm64.tar.gz` | 72431960 | `050b7bc2ba0bcc66be790be6741bce1e75247a635469093c6328ebc90a95762e` | provenance candidate only |
| `llama-b10621-bin-macos-arm64.tar.gz` | 10954823 | `429c8270608600188035e5e92f7d78dffb7900904fe7dd7e6a84f48068cd13cf` | provenance candidate only |
| `llama-b10621-bin-ubuntu-x64.tar.gz` | 16291771 | `91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583` | provenance candidate only |
| `llama-b10621-bin-win-cpu-x64.zip` | 18068018 | `0e8b65e650e369f70f8307d890508886f171ef4fb00facccddd4a1b7ffdaca51` | provenance candidate only |
| `llama-b10621-xcframework.zip` | 80871640 | `ea50671b3dfe86136be16448763f94642c53443df96964777b4e1c3d51f06e20` | provenance candidate only |

No listed asset was downloaded or executed. Asset digests are observed public metadata, not accepted commandMed runtime bindings.

## 7. Conservative interpretation

```text
EXACT_SOURCE_ARCHITECTURE_IMPLEMENTATIONS_OBSERVED=YES
FROZEN_GRANITE_HF_CLASS_TO_LLAMA_CPP_CONVERTER_MAPPING_OBSERVED=YES
ALL_FROZEN_CANDIDATES_HAVE_FINAL_ACCEPTED_RUNTIME_BINDINGS=NO
ARCHITECTURE_IMPLEMENTATION_PROVES_EXACT_GGUF_LOAD_SUCCESS=NO
ARCHITECTURE_IMPLEMENTATION_PROVES_TOKENIZER_RENDERING_CORRECTNESS=NO
ARCHITECTURE_IMPLEMENTATION_PROVES_TARGET_DEVICE_STABILITY=NO
ARCHITECTURE_IMPLEMENTATION_PROVES_MEMORY_LATENCY_THERMAL_ENERGY_PASS=NO
UPSTREAM_PREBUILT_ASSET_PROVES_COMMANDMED_WRAPPER_IDENTITY=NO
```

Final commandMed binding still requires a separately reviewed exact runtime/build/wrapper/backend/target subject before device execution.

## Exclusions

This bounded research explicitly excludes:

- selecting or freezing `c1d0e7a...`, `b10621`, or any other runtime/build;
- treating release/tag labels as immutable authority;
- downloading, converting, building, or executing upstream binaries, models, GGUF files, benchmarks, or device workloads;
- treating `GraniteMoeHybridForCausalLM` or `GRANITE_HYBRID` naming as proof that the admitted product is the screened-out `granite-4.0-h-350m-base` variant;
- choosing backends, wrappers, toolchains, measurement methods, or performance thresholds;
- changing E001/E002/E003 authority, PR #81 decision state, PR #83 intake state, A7/A13/A14/A15 state, E004 completion, E005 winner selection, training authority, or spend.

## Exit Evidence

This research artifact is repository-level complete only when one exact reviewed head proves:

```text
EXACT_SOURCE_COMMIT_CANDIDATE_RECORDED=YES
RELEASE_TAGS_TREATED_AS_DESCRIPTIVE_ONLY=YES
QWEN_IMPLEMENTATION_MAPPINGS_RECORDED=YES
GRANITE_PRODUCT_VS_CONVERTER_NAMING_DISAMBIGUATED=YES
OBSERVED_BUILD_ASSET_METADATA_RECORDED=YES
NO_RUNTIME_SELECTION_OR_EXECUTION_CLAIMED=YES
FINAL_RUNTIME_AND_BUILD_FIELDS_REMAIN_NEEDS_EVIDENCE=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Repository closure of this record closes only the bounded public-metadata research step.