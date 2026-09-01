# E004 Rebuild Reproducibility Diagnostic Authority — 2026-09-01

**Spec:** 007 SFT V1  
**Decision owner:** Founder  
**Artifact class:** bounded diagnostic authority  
**Canonical base:** `6dfde8e4a73459fe460cd528461a0a2139f23621`  
**Canonical runtime-readiness reconciliation:** `specs/007-sft-v1/e004-conversion-runtime-reconstruction-readiness-reconciliation-2026-09-01.md`  
**Authority effect before canonical merge:** NONE  
**Model/source-weight access authority:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation authority:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Authorize the smallest execution required to diagnose the unresolved `llama-quantize` rebuild reproducibility mismatch recorded canonically after the repaired E004 runtime-evidence run.

Canonical evidence currently records:

```text
PRIOR_BUILD_RUN=33187438094
PRIOR_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
PRIOR_LLAMA_QUANTIZE_INTEGER_BYTES=6513680

REPAIRED_RUNTIME_RUN=33434874024
REPAIRED_RUNTIME_JOB=99628745384
REBUILT_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
REBUILT_LLAMA_QUANTIZE_INTEGER_BYTES=6513680

REBUILT_SHA_EQUALS_PRIOR_SHA=NO
REBUILD_BINARY_REPRODUCIBILITY=NOT_PROVEN
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
RUNTIME_RECONSTRUCTION_READINESS=INCOMPLETE_PENDING_MISMATCH_REVIEW_OR_SEPARATE_RESOLUTION
```

The controlling runtime-evidence contract states that a mismatch must not be silently accepted, is not automatically a source-integrity failure, and leaves later conversion authority blocked pending review.

This authority therefore permits one toolchain-only diagnostic execution. It does not authorize acceptance of the mismatch in advance, does not authorize model conversion, and does not weaken any later exact-subject requirement.

## 2. Founder directive and narrow interpretation

The Founder has repeatedly directed:

```text
FOUNDER_DIRECTIVE=go ahead do not stop until finish the project , you have all approvals fro me . DO NOT STOP
FOUNDER_DIRECTIVE_SHA256=7037b7f98e65b324fd478d65c88d49c34483ff37a1a5eb9f380987df0b22d82a
FOUNDER_DIRECTIVE_DATE=2026-09-01
FOUNDER_DIRECTIVE_ORDERING=AFTER_PR165_CANONICAL_RUNTIME_READINESS_RECONCILIATION
```

This directive is interpreted only at the exact live dependency frontier. It authorizes the bounded diagnostic lifecycle defined here after independent review and canonical merge. It does not waive evidence, exact-head review, one-shot cardinality, historical-evidence preservation, or any scientific/execution gate outside this diagnostic.

## 3. Diagnostic question

The one authorized run may answer only:

> Under a single exact GitHub-hosted runner environment, with the exact pinned `llama.cpp` source and the previously frozen build configuration, are `llama-quantize` output bytes repeatable at the same absolute source/build paths, and does changing only the historically observed source/build path and PATH context reproduce or materially explain the previously observed SHA-256 difference?

Permitted dispositions after the run are limited to:

```text
DIAGNOSTIC_DISPOSITION=PATH_CONTEXT_REPRODUCES_OBSERVED_HASH_SPLIT
DIAGNOSTIC_DISPOSITION=PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
DIAGNOSTIC_DISPOSITION=SAME_PATH_BUILD_NOT_BYTE_REPRODUCIBLE
DIAGNOSTIC_DISPOSITION=NO_PATH_EFFECT_OBSERVED_CAUSE_NEEDS_EVIDENCE
DIAGNOSTIC_DISPOSITION=INCONCLUSIVE_ENVIRONMENT_MISMATCH_OR_EXECUTION_FAILURE
```

No other causal claim may be invented from the diagnostic.

## 4. Exact source and historical environment identities

The diagnostic source is fixed to:

```text
TOOL_REPOSITORY=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
TARGET=llama-quantize
CMAKE_BUILD_TYPE=Release
GENERATOR=Ninja
```

Historical and repaired runs both recorded:

```text
ImageOS=ubuntu24
ImageVersion=20260823.283.1
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_SHA256=1643dacd9feaedc58f3cc581e4d22577dfe25c09b10282936186ccf0f2e61118
CMAKE_PATH=/usr/local/bin/cmake
CMAKE_SHA256=c4b3b237dc7a013590db9e90f70fca2dfdedde09521e920d3339569ea364230a
NINJA_PATH=/usr/local/bin/ninja
NINJA_SHA256=607e668f90dd6cd82e1a42ae572647ad1b1fd43063964295b9547836d8c15d99
C_COMPILER_PATH=/usr/bin/x86_64-linux-gnu-gcc-13
C_COMPILER_SHA256=1b99826121ae6682a634e5efe09bd3e3df58ce58e0b28f849114ab5b89139c26
CXX_COMPILER_PATH=/usr/bin/x86_64-linux-gnu-g++-13
CXX_COMPILER_SHA256=1353e9bdd29a7295c7226bf6c63abccce056d8cac31f112e5cdbecc3f28c2769
```

The diagnostic must record all corresponding live identities before interpretation. If `ImageVersion` or any required tool identity differs from the historical identities above, the run may still retain observations but MUST classify the causal diagnostic as `INCONCLUSIVE_ENVIRONMENT_MISMATCH_OR_EXECUTION_FAILURE` unless the evidence itself independently supports a narrower non-causal statement.

## 5. Exact build configuration

Every diagnostic build must use the same frozen configuration:

```text
cmake -S <source_dir> -B <build_dir> -G Ninja -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=OFF -DLLAMA_BUILD_COMMON=ON -DLLAMA_BUILD_TESTS=OFF \
  -DLLAMA_BUILD_TOOLS=ON -DLLAMA_BUILD_EXAMPLES=OFF -DLLAMA_BUILD_SERVER=OFF \
  -DLLAMA_BUILD_APP=OFF -DLLAMA_BUILD_UI=OFF -DLLAMA_USE_PREBUILT_UI=OFF \
  -DLLAMA_TOOLS_INSTALL=OFF -DLLAMA_TESTS_INSTALL=OFF -DLLAMA_OPENSSL=OFF \
  -DLLAMA_SUBPROCESS=OFF -DLLAMA_LLGUIDANCE=OFF -DGGML_NATIVE=OFF \
  -DGGML_CCACHE=OFF -DGGML_OPENMP=OFF
cmake --build <build_dir> --target llama-quantize --parallel 2 --verbose
```

No source patch, compiler flag repair, prefix-map flag, linker flag, dependency mutation, or normalization attempt is permitted in the diagnostic run.

## 6. Diagnostic matrix

The implementation must create one exact source fetch and then local exact-source copies/worktrees sufficient to execute these cells without additional network access after staging:

```text
CELL_A1=HISTORICAL_PATHS_HISTORICAL_PATH_ENV_FIRST_BUILD
CELL_A2=HISTORICAL_PATHS_HISTORICAL_PATH_ENV_REPEAT_AFTER_CLEAN_BUILD_DIR
CELL_B1=REPAIRED_PATHS_REPAIRED_PATH_ENV_FIRST_BUILD
CELL_B2=REPAIRED_PATHS_REPAIRED_PATH_ENV_REPEAT_AFTER_CLEAN_BUILD_DIR
CELL_C=HISTORICAL_PATHS_REPAIRED_PATH_ENV
CELL_D=REPAIRED_PATHS_HISTORICAL_PATH_ENV
```

Path/environment bindings:

```text
HISTORICAL_SOURCE_DIR=$RUNNER_TEMP/e004-llama.cpp
HISTORICAL_BUILD_DIR=$RUNNER_TEMP/e004-llama.cpp-build
HISTORICAL_BUILD_PATH=/usr/local/bin:/usr/bin

REPAIRED_SOURCE_DIR=$RUNNER_TEMP/e004-runtime-evidence/llama.cpp
REPAIRED_BUILD_DIR=$RUNNER_TEMP/e004-runtime-evidence/llama.cpp-build
REPAIRED_BUILD_PATH=/usr/local/bin:/usr/bin:/bin
```

A1/A2 and B1/B2 test same-path repeatability. C/D separate the observed PATH delta from the absolute source/build path delta.

## 7. Mandatory evidence per cell

For every cell the job must emit at least:

```text
CELL_ID
SOURCE_DIR
BUILD_DIR
PATH_VALUE
SOURCE_COMMIT
SOURCE_TREE
CMAKE_CACHE_SHA256
LLAMA_QUANTIZE_SHA256
LLAMA_QUANTIZE_INTEGER_BYTES
LLAMA_QUANTIZE_FILE_TYPE
ELF_BUILD_ID_IF_PRESENT
```

The job must also emit:

- exact resolved paths and SHA-256 identities for `cmake`, `ninja`, `cc`, `c++`, and relevant ELF inspection tools;
- `uname -a`, `/etc/os-release`, `ImageOS`, and `ImageVersion`;
- same-path equality results for A1/A2 and B1/B2;
- cross-cell SHA equality matrix;
- equality against both historical hashes;
- `cmp` difference count or an equivalent bounded byte-difference summary for non-identical cells;
- ELF note/build-ID comparison where available;
- bounded string/path inspection sufficient to report whether exact historical or repaired absolute paths are present in the resulting binary bytes;
- a final deterministic disposition selected only from Section 3.

Large binary dumps are prohibited. Evidence is logs-only.

## 8. Network, credential, persistence, runner, and spend boundary

The diagnostic may use network only to fetch exact public `llama.cpp` source from `github.com` before local build cells begin.

```text
NETWORK_SOURCE_STAGING_HOST=github.com
OTHER_NETWORK_DESTINATION=PROHIBITED
MODEL_REPOSITORY_ACCESS=PROHIBITED
PACKAGE_INDEX_ACCESS=PROHIBITED
MODEL_PROVIDER_ACCESS=PROHIBITED
TELEMETRY_OR_UPLOAD=PROHIBITED
```

After exact source staging, the diagnostic build/inspection phase must run without any need for external network access. It must clear model/provider/package credentials and must not use them.

```text
HF_TOKEN_USE=PROHIBITED
HUGGING_FACE_HUB_TOKEN_USE=PROHIBITED
GH_TOKEN_USE_BY_DIAGNOSTIC_STEPS=PROHIBITED
CLOUD_CREDENTIAL_USE=PROHIBITED
PRIVATE_OR_GATED_ASSET_ACCESS=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
RELEASE_UPLOAD=PROHIBITED
REPOSITORY_BINARY_COMMIT=PROHIBITED
```

Execution is limited to:

```text
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_DIAGNOSTIC_RUNS=1
MAX_AUTHORIZED_RUN_ATTEMPTS=1
CURRENT_AUTHORIZED_SPEND_USD=0
PAID_OR_LARGER_RUNNER=PROHIBITED
```

The allowance is consumed when the one diagnostic run is created, regardless of conclusion.

## 9. Trigger and implementation lifecycle

Because the connected executor does not expose a native fresh `workflow_dispatch` creator, this new diagnostic may use one merge-triggered, path-scoped workflow rather than creating another transport bootstrap.

The implementation path must be exactly:

```text
.github/workflows/e004-rebuild-reproducibility-diagnostic-v1.yml
```

The only authorized trigger is:

```text
push to main
AND changed path == .github/workflows/e004-rebuild-reproducibility-diagnostic-v1.yml
AND github.run_attempt == 1
```

The workflow must use `permissions: {}` and a unique concurrency group with `cancel-in-progress: false`.

Required lifecycle:

```text
THIS_AUTHORITY_EXACT_HEAD_REVIEW
-> GUARDED_CANONICAL_AUTHORITY_MERGE
-> REREAD_CANONICAL_GOVERNANCE
-> FRESH_IMPLEMENTATION_BRANCH_FROM_EXACT_AUTHORITY_MAIN
-> ONE_WORKFLOW_PATH_ONLY
-> FRESH_EXACT_HEAD_IMPLEMENTATION_REVIEW
-> GUARDED_CANONICAL_IMPLEMENTATION_MERGE
-> EXACTLY_ONE_MERGE_TRIGGERED_DIAGNOSTIC_RUN
-> RETAIN_TERMINAL_RUN_JOB_LOG_EVIDENCE
-> CANONICAL_DIAGNOSTIC_RESULT_RECONCILIATION
```

No retry, failed-job rerun, second diagnostic run, alternate trigger, local substitute, or widened repair is authorized by this record.

## 10. Explicit exclusions

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_WEIGHT_QUANTIZATION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS=PROHIBITED
CONTAMINATION_ASSESSMENT_EXECUTION=PROHIBITED
SELECTION_SUITE_CONSTRUCTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
TRAINING=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PERSISTENT_BINARY_STORAGE=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

This diagnostic cannot create or imply `MODEL_CONVERSION_AUTHORITY`, `CONVERSION_EXECUTION_AUTHORITY`, contamination authority, A15 activation, training authority, E005 transition, or a backbone winner.

## 11. Result interpretation

A diagnostic PASS means only that the one bounded diagnostic completed and its evidence is retained. It does not mean the mismatch is acceptable.

If same-path builds are not byte-identical, runtime reconstruction remains blocked and any repair/normalization experiment requires separate authority.

If same-path builds are byte-identical and the historical/repaired path contexts reproduce the historical two-hash split, a later reconciliation may attribute the observed split to the reproduced path/build-context dependency only to the extent directly demonstrated by retained evidence. It still must not reinterpret unrelated historical failures.

If the historical split is not reproduced, the cause remains `NEEDS_EVIDENCE` and later conversion authority remains blocked unless a separately reviewed policy disposition explicitly accepts execution-time identity binding without byte-for-byte reconstruction.

## 12. E004 / E005 effect

Canonical merge of this authority changes only diagnostic authority state:

```text
E004_REBUILD_REPRO_DIAGNOSTIC_AUTHORITY=AUTHORIZED_EXACTLY_ONE_AFTER_IMPLEMENTATION_QUALIFICATION
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

## 13. Required independent review

Before canonical merge, an independent reviewer must verify at least:

- canonical base `6dfde8e4a73459fe460cd528461a0a2139f23621` and PR #165 readiness reconciliation are correctly bound;
- both historical binary SHA-256 values and equal byte counts are copied exactly;
- mismatch cause remains `NEEDS_EVIDENCE`;
- the diagnostic question is narrow and does not pre-accept the mismatch;
- exact source commit/tree and build flags remain unchanged;
- A1/A2, B1/B2, C, and D cells isolate repeatability/path/PATH effects without model execution;
- one standard public `ubuntu-24.04` runner and zero-spend boundary are preserved;
- the merge-triggered path-scoped mechanism cannot execute more than the single newly authorized diagnostic run absent a later workflow mutation and separate authority;
- no retry, failed-job rerun, second run, alternate trigger, model/weight access, conversion, inference, benchmark, contamination, A15, training, credential, upload, paid-runner, procurement/payment, or spend authority is created;
- E004 remains incomplete and E005 remains `NOT_REACHED`.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only guarded canonical merge of the exact reviewed authority head activates the diagnostic implementation lifecycle.