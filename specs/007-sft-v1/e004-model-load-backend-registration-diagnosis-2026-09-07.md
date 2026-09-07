# E004 Model-Load Backend Registration Diagnosis — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md`
**Canonical predecessor main:** `7e490d0c174e7c96854ee196a9e2ca401da5d2d9`
**Canonical predecessor tree:** `48b31bde037a81c82986ea82676b72dba1c5e08b`
**Artifact class:** repository-only diagnosis; no execution authority
**Model bytes acquired:** NO
**Model load performed:** NO
**Current authorized spend:** USD 0

## 1. Purpose

Diagnose the exact next runtime prerequisite exposed by the consumed corrective model-load compatibility run `34150708258` without rerunning or retrying any evidence workflow and without acquiring or loading model bytes.

This record is limited to canonical repository evidence, the completed GitHub Actions logs, and read-only inspection of the exact frozen llama.cpp source revision already bound by E004.

## 2. Canonical empirical input

V43 records that both exact frozen GGUF candidates reached the actual load-only call and failed with exit code `2` and the same runtime diagnostic:

```text
llama_model_load_from_file_impl: no backends are loaded. hint: use ggml_backend_load() or ggml_backend_load_all() to load a backend before calling this function
```

Canonical state remains:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_GGUF_EMPIRICAL_FAIL
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
```

## 3. Frozen runtime identity remains unchanged

This diagnosis does not propose or perform runtime substitution.

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
```

The upstream release tag `b10621` targets the same frozen source revision, and the published Ubuntu x64 archive digest matches the canonical archive SHA-256 above.

## 4. Exact frozen-source backend registration contract

Read-only inspection of exact frozen source `c1d0e7a004015f23bc0233470b747b596f29b264` establishes the required API surface.

### 4.1 Public backend API

Exact file:

```text
ggml/include/ggml-backend.h@c1d0e7a004015f23bc0233470b747b596f29b264
```

The frozen header declares:

```text
GGML_API size_t ggml_backend_reg_count(void);
GGML_API ggml_backend_reg_t ggml_backend_load(const char * path);
GGML_API void ggml_backend_load_all(void);
GGML_API void ggml_backend_load_all_from_path(const char * dir_path);
```

### 4.2 Frozen implementation search semantics

Exact file:

```text
ggml/src/ggml-backend-reg.cpp@c1d0e7a004015f23bc0233470b747b596f29b264
```

The frozen implementation establishes:

```text
BACKEND_SHARED_LIBRARY_PREFIX_LINUX=libggml-
BACKEND_SHARED_LIBRARY_EXTENSION_LINUX=.so
GGML_BACKEND_LOAD_ALL_WITH_NULL_PATH=SEARCH_EXECUTABLE_DIRECTORY_AND_CURRENT_DIRECTORY
GGML_BACKEND_LOAD_ALL_FROM_PATH=SEARCH_ONLY_CALLER_SUPPLIED_DIRECTORY
CPU_BACKEND_DISCOVERY=ATTEMPTED_BY_NAME_cpu
```

The frozen implementation defines `ggml_backend_load_all()` as a call to `ggml_backend_load_all_from_path(nullptr)` and explicitly attempts backend discovery including the CPU backend.

### 4.3 Frozen upstream simple example orders backend loading before model loading

Exact file:

```text
examples/simple/simple.cpp@c1d0e7a004015f23bc0233470b747b596f29b264
```

The frozen upstream example performs:

```text
ggml_backend_load_all();
llama_model_params model_params = llama_model_default_params();
llama_model * model = llama_model_load_from_file(model_path.c_str(), model_params);
```

This is direct frozen-source evidence that dynamic backend registration is an expected prerequisite before model loading in this runtime line.

## 5. Why the current reviewed helper reaches a no-backend state

The canonical load-only helper currently performs:

```text
llama_backend_init();
llama_model_params params = llama_model_default_params();
llama_model * model = llama_model_load_from_file(argv[1], params);
```

It does not call any of:

```text
ggml_backend_load
ggml_backend_load_all
ggml_backend_load_all_from_path
```

The corrective workflow extracts the exact frozen runtime archive into a job-local runtime directory, locates the exact `libllama.so.0.3.0`, and derives its directory for linking the helper. The helper itself is emitted outside that extracted runtime library directory and is executed from the repository working directory.

Under the frozen backend loader semantics, an unqualified `ggml_backend_load_all()` would search the helper executable directory and current working directory by default, not necessarily the extracted frozen runtime library directory already identified by the workflow.

Therefore the narrowest deterministic successor design is path-bound backend discovery against the already-identified directory containing the exact frozen runtime libraries, rather than relying on ambient working-directory discovery.

## 6. Bounded prospective mechanism

The smallest exact mechanism supported by frozen source evidence is:

```text
1. Continue verifying the exact frozen runtime archive and runtime file manifest.
2. Derive the exact runtime library directory from the verified `libllama.so.0.3.0` path.
3. Before model loading, register dynamic backends only from that exact verified directory using `ggml_backend_load_all_from_path(<verified_runtime_library_directory>)`.
4. Fail closed if backend registration produces zero registered backends.
5. Only after backend registration succeeds, perform the existing load-only `llama_model_load_from_file` call.
6. Do not create a context, tokenize, decode, encode, sample, infer, generate, benchmark, evaluate, select a winner, activate A15, or train.
```

A future implementation must statically establish the exact backend-library files available in the frozen runtime archive and bind their identities before any new empirical model-load run is eligible. No backend file from another release, build, revision, route, package, system installation, or network source may be substituted.

## 7. Review-first static qualification requirement for any future implementation

If later exact authority is canonically granted, the future implementation must be review-first and must satisfy all of the following before any post-merge model-load evidence trigger exists:

```text
EXACT_FROZEN_RUNTIME_ARCHIVE_REVERIFICATION=PASS_REQUIRED
EXACT_RUNTIME_FILE_MANIFEST_REVERIFICATION=PASS_REQUIRED
EXACT_BACKEND_LIBRARY_DIRECTORY_BINDING=PASS_REQUIRED
EXACT_BACKEND_LIBRARY_FILE_IDENTITY_BINDING=PASS_REQUIRED
PATH_BOUND_BACKEND_DISCOVERY=PASS_REQUIRED
ZERO_REGISTERED_BACKENDS_FAIL_CLOSED=PASS_REQUIRED
LOAD_ONLY_HELPER_POLICY=PASS_REQUIRED
PULL_REQUEST_MODEL_BYTES=PROHIBITED
PULL_REQUEST_MODEL_LOAD=PROHIBITED
TRANSFORMERS_RERUN=PROHIBITED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=PASS_REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=PASS_REQUIRED
```

A no-model static backend-registration probe may be separately authorized by a future exact decision to prove that the frozen runtime can register its backend library before merge. It is not authorized by this diagnosis record itself.

## 8. Non-expansion

This diagnosis creates no execution authority.

```text
BACKEND_REGISTRATION_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
MODEL_LOAD_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 9. Disposition

```text
BACKEND_REGISTRATION_DIAGNOSIS=COMPLETE_REPOSITORY_ONLY
OBSERVED_FAILURE=NO_BACKENDS_LOADED_BEFORE_LLAMA_MODEL_LOAD
FROZEN_SOURCE_REQUIRED_PRELOAD_MECHANISM=DYNAMIC_BACKEND_REGISTRATION
NARROWEST_PATH_BOUND_API=ggml_backend_load_all_from_path
FURTHER_EMPIRICAL_MODEL_LOAD_AUTHORITY=NONE
NEXT_LAWFUL_TRANSITION=PREPARE_BOUNDED_FOUNDER_DECISION_SURFACE_ONLY
PROJECT_FINISHED=NO
```
