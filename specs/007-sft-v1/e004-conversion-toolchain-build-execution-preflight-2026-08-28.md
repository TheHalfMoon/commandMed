# E004 Conversion Toolchain Build Execution Preflight — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical authority base:** `0a0d1768f496a8043acf8bfccc3f8b6f213d0ff5`  
**Authority record:** `e004-conversion-toolchain-build-authority-2026-08-28.md`  
**Authorized tool source:** `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`  
**Authorized build target:** `llama-quantize`  
**Artifact class:** execution-preflight evidence  
**Build result:** NOT EXECUTED — SOURCE MATERIALIZATION BLOCKED  
**Conversion result:** NOT EXECUTED  
**Spend:** USD 0

This record captures the first bounded build-evidence execution preflight after canonical build authority. It records real environment identities and real failed source-materialization attempts. It must not be interpreted as a successful build or as conversion authority.

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
BUILD_PREFLIGHT_EXECUTED=YES
EXACT_SOURCE_BYTES_MATERIALIZED=NO
BUILD_CONFIGURATION_EXECUTED=NO
LLAMA_QUANTIZE_BUILD_EXECUTED=NO
LLAMA_QUANTIZE_EXECUTABLE_PRODUCED=NO
MODEL_CONVERSION_EXECUTION_OCCURRED=NO
MODEL_INFERENCE_OCCURRED=NO
BENCHMARK_EXECUTION_OCCURRED=NO
DEVICE_EXECUTION_OCCURRED=NO
TRAINING_OCCURRED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Candidate build environment actually observed

The available isolated execution environment reported:

```text
HOST_OS=Debian GNU/Linux 13 (trixie)
HOST_ARCH=x86_64
KERNEL=6.18.35
PYTHON_VERSION=3.13.5
CMAKE_VERSION=3.31.6
GCC_VERSION=14.2.0
GXX_VERSION=14.2.0
NINJA_VERSION=1.12.1
GIT_VERSION=2.47.3
GLIBC_VERSION=2.41
```

Observed executable/file identities:

```text
PYTHON3_PATH=/opt/pyvenv/bin/python3
PYTHON3_SHA256=17b78e0a93175e86f9ac03141924fd7a7f0c0c52e66b34bfa0de20ffef989df1

CMAKE_PATH=/usr/bin/cmake
CMAKE_SHA256=9a2692f4d712265eb29c90c3366bfc40df400ea586b0477edabbcf3bae745dc1

GCC_PATH=/usr/bin/gcc
GCC_SHA256=a23ecab8ff08f09ad8c80602c2c5df7f49e09c25905cb8975902e101bf72635f

GXX_PATH=/usr/bin/g++
GXX_SHA256=6b3696e4dcb85e1c949c732a02befa50e3983ecf94ce7e8e58d9d503b954b79d

NINJA_PATH=/usr/bin/ninja
NINJA_SHA256=e8e646527e23aa7a66d0f04b86b89f1bb2f25edcc1c5e402a0989e5364c8779b

GIT_PATH=/usr/bin/git
GIT_SHA256=356db14e102d68a1a37d8a1ac577dfd678d45d46e92f468bef8b7154e7bfdc60

OS_RELEASE_SHA256=8b8c2f53770c96bf2996f8e9feb3705d4fec1a4579251eea8c996cb458257731
LIBC_PATH=/lib/x86_64-linux-gnu/libc.so.6
LIBC_SHA256=fa430b8f298f817a266046af84a77533185ad6fc4406c7d3787b5a0a0c207826
```

These identities describe the available candidate environment only. They are not yet a `BUILD_ENVIRONMENT_MANIFEST_SHA256`, because the exact source tree and resolved converter dependency artifacts were not materialized.

## 2. Network/source acquisition preflight

Direct resolver checks in the execution environment failed for the required public source hosts:

```text
DNS_GITHUB_COM=UNRESOLVED
DNS_API_GITHUB_COM=UNRESOLVED
DNS_CODELOAD_GITHUB_COM=UNRESOLVED
DNS_HUGGINGFACE_CO=UNRESOLVED
```

Observed direct failures included:

```text
curl https://github.com
-> curl: (6) Could not resolve host: github.com

curl https://huggingface.co
-> resolving timed out
```

A second test deliberately removed DNS as the explanatory variable. Public external DNS evidence identified a current `codeload.github.com` IPv4 address, and the acquisition attempt bound that hostname directly with curl `--resolve`. The connection still failed before any bytes were received:

```text
TARGET_HOST=codeload.github.com
TARGET_PORT=443
DNS_BYPASS_USED=YES
SOURCE_ARCHIVE_PATH=/ggml-org/llama.cpp/tar.gz/c1d0e7a004015f23bc0233470b747b596f29b264
RESULT=TCP_CONNECTION_FAILED
CURL_EXIT=7
SOURCE_ARCHIVE_BYTES_RECEIVED=0
```

Therefore the blocker is not safely reducible to repository DNS configuration. The available execution environment does not provide usable outbound source-materialization connectivity for this task.

## 3. Alternate local-source check

The execution workspace was searched for an already-materialized exact source tree or relevant converter/build artifacts under the available working/storage roots.

```text
LOCAL_LLAMA_CPP_TREE_FOUND=NO
LOCAL_CONVERT_HF_TO_GGUF_FOUND=NO
LOCAL_LLAMA_QUANTIZE_EXECUTABLE_FOUND=NO
```

No local fallback was used and no alternate source revision, fork, package-manager build, or prebuilt executable was substituted.

## 4. GitHub connector boundary

The connected GitHub interface can inspect immutable public source files and Git metadata, which is sufficient for the already-canonical static source-identity evidence. It does not expose an allowed binary source-archive materialization action for this upstream repository into the build workspace.

```text
STATIC_GITHUB_SOURCE_INSPECTION_AVAILABLE=YES
BUILD_WORKSPACE_SOURCE_ARCHIVE_MATERIALIZATION_AVAILABLE=NO
STATIC_SOURCE_METADATA_EQUALS_LOCAL_SOURCE_BYTES=NO
```

The build must not be reconstructed from a partial hand-selected subset of files because doing so would not establish that the built subject is the exact authorized source tree.

## 5. Fail-closed build disposition

Because exact source bytes are absent:

```text
SOURCE_REPOSITORY=ggml-org/llama.cpp
SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
SOURCE_TREE_OR_ARCHIVE_IDENTITY=NEEDS_EVIDENCE
SOURCE_FILE_IDENTITY_RECONCILIATION=INCOMPLETE_LOCAL_BYTES_ABSENT
RESOLVED_PYTHON_DEPENDENCY_SET=NEEDS_EVIDENCE
RESOLVED_PYTHON_DEPENDENCY_ARTIFACT_HASHES=NEEDS_EVIDENCE
CMAKE_CONFIGURATION_ARGV=NOT_EXECUTED
BUILD_ARGV=NOT_EXECUTED
BUILD_FLAGS=NOT_FROZEN_FROM_REAL_BUILD
LLAMA_QUANTIZE_OUTPUT_PATH=NOT_PRODUCED
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_LOG_IDENTITY=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
BUILD_PASS=NO
```

No CMake configure, compilation, dependency installation, or executable production was attempted after source-materialization failure.

## 6. Authority remains bounded

```text
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
CURRENT_AUTHORIZED_SPEND_USD=0
```

The failed build preflight does not consume, expand, revoke, or transform the underlying Founder authority. It simply proves this execution environment cannot currently satisfy the authorized build subject.

## 7. Next valid transition

The build-evidence lane can resume only in an execution environment that can materialize the exact authorized public source and exact resolved dependency artifacts while preserving:

```text
EXACT_TOOL_REVISION_ONLY=YES
CREDENTIALS=NONE
SPEND_USD=0
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_TRANSFORMATION=PROHIBITED
BENCHMARK_ACCESS=PROHIBITED
TRAINING=PROHIBITED
```

A new environment must re-run source integrity and environment identity collection. The identities in this record must not be copied forward as if they described a different environment.

External hosted execution must not be inferred from this build authority merely because it is zero-dollar; any materially different execution/provider boundary must be explicitly compatible with repository governance before use.

## 8. Current lifecycle effect

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_STARTABLE=NO
BUILD_EVIDENCE_LANE_STATE=BLOCKED_SOURCE_MATERIALIZATION_IN_CURRENT_ENVIRONMENT
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exit evidence for this record

This preflight record is complete only as evidence of a failed, fail-closed environment attempt after exact-head review confirms:

```text
REAL_ENVIRONMENT_IDENTITIES_RECORDED=YES
SOURCE_MATERIALIZATION_FAILURE_RECORDED_WITHOUT_PASS_INFERENCE=YES
NO_PARTIAL_SOURCE_BUILD_USED=YES
NO_BUILD_EXECUTED_WITHOUT_EXACT_SOURCE=YES
NO_MODEL_TRANSFORMATION_OCCURRED=YES
NO_DOWNSTREAM_AUTHORITY_CREATED=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Canonical merge would close only this execution-preflight evidence record. It would not close the build-evidence lane, E004, or any downstream gate.