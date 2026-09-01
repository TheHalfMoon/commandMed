# E004 Conversion Runtime Reconstruction Readiness Reconciliation — 2026-09-01

**Spec:** 007 SFT V1  
**Artifact class:** append-only runtime-reconstruction readiness reconciliation  
**Canonical base:** `836164f3b7ff9b50aac1a2b3ba9e7e950eef8e38`  
**Canonical repaired-runtime result:** `specs/007-sft-v1/e004-repaired-target-runtime-evidence-result-reconciliation-2026-09-01.md`  
**Repaired runtime run:** `33434874024`  
**Repaired runtime job:** `99628745384`  
**Authority effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the Decision B conversion-runtime evidence fields after the bounded repaired-target runtime-evidence run succeeded and its exact result became canonical through PR #163 / merge `836164f3b7ff9b50aac1a2b3ba9e7e950eef8e38`.

This record performs no execution and grants no authority. It distinguishes:

1. runtime/dependency identities that now have direct retained evidence;
2. a reproducibility mismatch between the earlier build-evidence binary and the later rebuilt binary; and
3. persistent conversion-subject, storage, resource, argv, scientific, governance, contamination, and activation fields that remain unresolved.

The controlling runtime-evidence request explicitly required an append-only current-state reconciliation after runtime evidence and explicitly stated that runtime-evidence PASS is not conversion authority.

```text
RUNTIME_EVIDENCE_RUN_RESULT=PASS
RUNTIME_RECONSTRUCTION_EVIDENCE_EXISTS=YES
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

## 2. Existing source-subject evidence remains separate

E002 run `33183096268` already established real commandMed-governed ephemeral local integrity evidence for the exact frozen Decision B source subjects:

```text
GRANITE_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
QWEN_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=PASS_ON_RUN_33183096268
```

Those bytes were intentionally not persisted.

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
PERSISTENT_EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_SOURCE_PATH=NEEDS_EVIDENCE
```

This reconciliation does not recreate or reinterpret that source-integrity evidence.

## 3. Runtime-specific fields now bound by direct evidence

The canonical runtime-evidence purpose was to resolve and bind the exact converter runtime, dependency closure, local GGUF selection, build, network-isolation, and credential-state evidence required for a later reconstruction-based conversion subject.

Run `33434874024` now provides direct retained evidence for the following runtime-specific fields.

### Python, resolver, and dependency closure

```text
PYTHON_RUNTIME_IDENTITY_FOR_CONVERSION_EVIDENCE=BOUND_EPHEMERAL_RUNTIME_RUN_33434874024
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=Python 3.12.3
PYTHON_RUNTIME_SHA256=1643dacd9feaedc58f3cc581e4d22577dfe25c09b10282936186ccf0f2e61118

RESOLVER_AND_VERSION=BOUND
RESOLVER_NAME=pip
RESOLVER_VERSION=24.0
RESOLVER_MODULE_PATH=/usr/lib/python3/dist-packages/pip/__init__.py
RESOLVER_MODULE_SHA256=a009359c5a4b994552e4b9fb371bcda06527e55927e851908cf68d0dff10f299

PACKAGE_INDEX_OR_OFFLINE_WHEELHOUSE_BOUNDARY=BOUND_FOR_RUNTIME_EVIDENCE_RUN
DEPENDENCY_ARTIFACT_COUNT=27
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
DEPENDENCY_PACKAGE_HASH_SET=BOUND_BY_RETAINED_DEPENDENCY_MANIFEST
DEPENDENCY_SET_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=694ff5fcf55413072218982371c350c1e37a21d034b498acc83a501a3d908a85
```

The exact artifact rows remain recoverable from the retained job log and are identity-bound by the manifest SHA-256 above. This does not claim a persistent wheelhouse exists after the runner was destroyed.

### Exact pinned tool and converter entrypoint

```text
LLAMA_CPP_REPOSITORY=ggml-org/llama.cpp
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
CONVERTER_ENTRYPOINT_SHA256=e38975e1c68d98ac1664dfd530616eb35c72294382a4dd873d4746b23f27779f
CANONICAL_DEPENDENCY_REQUIREMENT_SURFACE_SHA256=4e973aa513a628244ad686230a779896502d184d28bd4ce2769b70bcf502bd6d
SOURCE_MANIFEST_SHA256=015862c648877b86a9b2b7a420eefeb49e352267a03ccb3e22edcce51c413aad
```

### Local GGUF runtime selection

```text
LOCAL_GGUF_SOURCE_MODE=REQUIRED
GGUF_IMPORTED_FILE_PATH=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp/gguf-py/gguf/__init__.py
GGUF_IMPORTED_SOURCE_IDENTITY=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp/gguf-py
GGUF_IMPORTED_FILE_SHA256=3ccfc0104cd7ea88c6028743b7bf3f2c89b5f474425de03a217a6072320d7c2f
NO_LOCAL_GGUF_UNSET_ATTESTATION=PASS
GGUF_ATTESTATION_SHA256=250e591881b14560bb5de592ef77e649542ab4c6c70fc1c4de0ff541645168cf
```

This is runtime-selection evidence only. The path is ephemeral and is not a future conversion-time path.

### Rebuilt tool and build-environment evidence

```text
CONVERSION_RUNTIME_EXECUTABLE_OR_INTERPRETER_IDENTITY=BOUND_EPHEMERAL_RUNTIME_RUN_33434874024
LLAMA_QUANTIZE_EPHEMERAL_PATH=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp-build/bin/llama-quantize
LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
LLAMA_QUANTIZE_INTEGER_BYTES=6513680
BUILD_ENVIRONMENT_MANIFEST_SHA256_FOR_CONVERSION_EVIDENCE=dd7a23f7ccc4aa03365caa1bfafe0713cd1f37c9da50e45a30ed2ae6a60a8122
CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
CMAKE_CONFIG=Release_Ninja_static_llama_quantize_only
BUILD_ARGV=cmake --build <build_dir> --target llama-quantize --parallel 2 --verbose
```

The rebuilt executable no longer exists after the ephemeral runner was destroyed.

```text
PERSISTENT_LLAMA_QUANTIZE_EXECUTABLE_PRESENT=NO
FUTURE_CONVERSION_TIME_LLAMA_QUANTIZE_PATH=NEEDS_EVIDENCE
```

## 4. Network and credential runtime evidence now exists

The isolated Phase B runtime emitted:

```text
PHASE_B_NETWORK_POLICY=DEFAULT_DENY_NETWORK_NAMESPACE
PHASE_B_UID=1001
CapInh=0000000000000000
CapPrm=0000000000000000
CapEff=0000000000000000
CapBnd=0000000000000000
CapAmb=0000000000000000
NoNewPrivs=1
SENSITIVE_PLATFORM_ENV_PRESENT=NO
NO_LOCAL_GGUF_STATE=UNSET
SECURITY_EVIDENCE_SHA256=e957873641db7e2bd2b9a140daee530d8fa7fcdd52293b228427bf1f48391dfe
```

Therefore the earlier generic current-state interpretation that no runtime network/credential evidence existed is superseded for **evidence existence on run `33434874024`**:

```text
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_EVIDENCE=PASS_ON_RUN_33434874024
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_EVIDENCE=PASS_ON_RUN_33434874024
```

This does not bind a future conversion process to that destroyed runner or create an operational conversion storage/resource identity.

## 5. Rebuild comparison result is a real mismatch

The runtime-evidence request required comparison against the earlier canonical build-evidence binary.

Earlier build-evidence run `33187438094` recorded:

```text
PRIOR_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
PRIOR_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
PRIOR_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
```

Repaired runtime-evidence run `33434874024` recorded:

```text
REBUILT_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
REBUILT_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
REBUILT_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
```

The direct comparison is therefore:

```text
REBUILT_SHA_EQUALS_PRIOR_SHA=NO
REBUILT_INTEGER_BYTES_EQUALS_PRIOR_INTEGER_BYTES=YES
REBUILD_BINARY_REPRODUCIBILITY=NOT_PROVEN
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
```

No mismatch cause is fabricated.

## 6. Static comparison narrows but does not explain the mismatch

The two runs used the same exact:

```text
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
RUNNER_IMAGE_OS=ubuntu24
RUNNER_IMAGE_VERSION=20260823.283.1
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

The configured CMake feature flags and requested build target are also the same.

Known static execution-context deltas include at least:

```text
PRIOR_SOURCE_DIR=/home/runner/work/_temp/e004-llama.cpp
REBUILT_SOURCE_DIR=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp
PRIOR_BUILD_DIR=/home/runner/work/_temp/e004-llama.cpp-build
REBUILT_BUILD_DIR=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp-build
PRIOR_BUILD_PATH=/usr/local/bin:/usr/bin
REBUILT_BUILD_PATH=/usr/local/bin:/usr/bin:/bin
PRIOR_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
REBUILT_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
```

These are observed/static deltas, not proof that any one of them caused the binary SHA difference.

The earlier runtime-evidence authority explicitly states that a SHA mismatch must not be silently accepted and leaves later conversion authority blocked pending review. This reconciliation therefore classifies the mismatch as a live readiness blocker rather than treating equal file size as reproducibility.

## 7. Runtime evidence readiness classification

The runtime-evidence run successfully resolves the prior **evidence-existence** gaps for the exact dependency closure, interpreter/runtime identity, local GGUF selection, build manifest, rebuilt tool identity, network isolation, and credential-state attestation.

It does not prove byte-for-byte reproducibility against the prior build-evidence executable.

```text
RUNTIME_DEPENDENCY_CLOSURE_EVIDENCE=BOUND
PYTHON_RUNTIME_EVIDENCE=BOUND
RESOLVER_EVIDENCE=BOUND
INSTALLED_ENVIRONMENT_EVIDENCE=BOUND
LOCAL_GGUF_RUNTIME_EVIDENCE=BOUND
BUILD_ENVIRONMENT_EVIDENCE=BOUND
NETWORK_ISOLATION_EVIDENCE=BOUND
CREDENTIAL_STATE_EVIDENCE=BOUND
REBUILT_TOOL_IDENTITY_EVIDENCE=BOUND
REBUILT_TOOL_BYTE_REPRODUCIBILITY_AGAINST_PRIOR_BUILD=FAIL_MISMATCH_OBSERVED
RUNTIME_RECONSTRUCTION_READINESS=INCOMPLETE_PENDING_MISMATCH_REVIEW_OR_SEPARATE_RESOLUTION
```

No additional runtime attempt is authorized by this state.

```text
REPAIRED_TARGET_RUNTIME_EVIDENCE_ATTEMPT_ALLOWANCE_REMAINING=0
AUTOMATIC_TARGET_RETRY_AUTHORITY=NONE
FAILED_TARGET_JOB_RERUN_AUTHORITY=NONE
SECOND_NEW_TARGET_ATTEMPT_AUTHORITY=NONE
```

## 8. Persistent exact conversion-subject fields still unresolved

The canonical runtime-evidence request itself states that runtime PASS cannot create a conversion execution subject. The following remain unresolved for an actual later conversion:

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
EXACT_LOCAL_SOURCE_DIRECTORY_AT_EXECUTION=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY_AT_EXECUTION=NEEDS_EVIDENCE
EXACT_CONVERT_ARGV=NEEDS_EVIDENCE
EXACT_QUANTIZE_ARGV=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
FILESYSTEM_OR_VOLUME_IDENTITY=NEEDS_EVIDENCE
ACCESS_CONTROL_OR_PROCESS_ISOLATION_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
CONVERSION_PHASE_NETWORK_DISABLEMENT=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
CONVERSION_PHASE_CREDENTIAL_ATTESTATION=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
```

The canonical normalization/metadata policy remains statically defined and unchanged:

```text
NORMALIZATION_OR_METADATA_POLICY=CANONICAL_STATIC_POLICY_DEFINED
```

No placeholder-bearing argv is promoted.

## 9. Scientific, governance, contamination, resource, and activation blockers remain independent

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Repository automation, AI review, or the runtime evidence above cannot substitute for these real external/governance evidence classes.

## 10. E004 / E005 consequence

```text
COMPONENT_RUNTIME_EVIDENCE=PASS_REPAIRED_TARGET_RUN_33434874024
COMPONENT_RUNTIME_RECONSTRUCTION_READINESS=INCOMPLETE_BINARY_REPRODUCIBILITY_MISMATCH
COMPONENT_PERSISTENT_CONVERSION_SUBJECT=INCOMPLETE
COMPONENT_MODEL_CONVERSION_AUTHORITY=NONE
COMPONENT_CONTAMINATION_AUTHORITY=NONE
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

## 11. Next dependency-safe frontier

No model conversion may be prepared as executable authority while the binary-reproducibility mismatch remains unresolved and the persistent conversion subject/resource fields remain incomplete.

The smallest next dependency-safe work after this record is one of:

1. exact review/reconciliation of whether the observed rebuild mismatch is acceptable under the frozen reconstruction contract or requires a separately authorized reproducibility diagnostic/repair;
2. separately authorized creation of a persistent exact conversion subject/workspace that binds the model source, output/storage, retention, compute/resource, and zero-spend identities without performing model conversion; or
3. independent real scientific/governance evidence through a separately permitted path.

This record itself authorizes none of those later actions.

## 12. Required review gate

Before canonical merge, a fresh independent exact-head reviewer must verify at least:

- the canonical repaired-runtime result merge `836164f3b7ff9b50aac1a2b3ba9e7e950eef8e38` is the exact base;
- E002 source-integrity evidence remains ephemeral and is not represented as a persistent source workspace;
- runtime/dependency fields marked `BOUND` are directly supported by run `33434874024`, job `99628745384`, and retained logs;
- dependency and build manifest hashes are copied exactly;
- network and credential evidence is scoped to the repaired runtime-evidence run only;
- prior build SHA `e1d88ef6...` and rebuilt SHA `18ff27aa...` are recorded exactly and are unequal;
- equal binary size is not represented as binary reproducibility;
- static workflow/environment deltas are observations only and no causal mechanism is invented;
- the mismatch remains a readiness blocker pending separate resolution;
- no rerun, second attempt, model conversion, contamination assessment, A15, training, credential expansion, paid runner, procurement/payment, or spend authority is created;
- persistent source/storage/resource/argv fields remain `NEEDS_EVIDENCE`;
- E004 remains incomplete and E005 remains `NOT_REACHED`.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only guarded canonical merge of the exact independently reviewed head may make this reconciliation canonical.
