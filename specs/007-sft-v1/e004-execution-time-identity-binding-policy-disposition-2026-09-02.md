# E004 Execution-Time Identity Binding Policy Disposition — 2026-09-02

**Spec:** 007 SFT V1  
**Canonical base:** `3da7d95b8dfc7ee1548cc8ece58c5cb55cbc82a6`  
**Artifact class:** non-executing bounded policy disposition  
**Depends on:** canonical rebuild-reproducibility diagnostic authority, implementation, terminal evidence, and result reconciliation  
**Authority effect before canonical merge:** NONE  
**Model conversion authority:** NONE  
**Conversion execution authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve only the policy question left open by the canonical E004 rebuild-reproducibility diagnostic: whether a future, separately authorized conversion execution may rely on a rigorously fail-closed **execution-time binary identity** even though the earlier repaired-runtime `llama-quantize` binary has not been reconstructed byte-for-byte.

This document performs no build, download, model access, conversion, inference, benchmark execution, contamination assessment, A15 activation, training, credential use, protected-data access, upload, procurement, payment, or spend.

Canonical merge of this document after fresh independent exact-head review would establish only the policy disposition below:

```text
POLICY_ID=E004-EXECUTION-TIME-IDENTITY-BINDING-V1
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_BINARY_RECONSTRUCTION_REQUIRED_AS_FUTURE_EXECUTION_PRECONDITION=NO
HISTORICAL_REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
REBUILD_BINARY_REPRODUCIBILITY_AGAINST_HISTORICAL_REPAIRED_HASH=NOT_PROVEN
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The accepted policy is not an equivalence claim between historical binaries and is not permission to execute a conversion.

## 2. Controlling retained evidence

The policy is bounded by the exact canonical observations already retained by commandMed.

### 2.1 Historical build-evidence identity

```text
HISTORICAL_BUILD_RUN_ID=33187438094
HISTORICAL_BUILD_JOB_ID=98903988417
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
HISTORICAL_SOURCE_DIR=/home/runner/work/_temp/e004-llama.cpp
HISTORICAL_BUILD_DIR=/home/runner/work/_temp/e004-llama.cpp-build
HISTORICAL_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
HISTORICAL_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
HISTORICAL_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
HISTORICAL_ELF_BUILD_ID=c3b1ffcb29aa0b069380b8aaf7aef6e4928f5738
```

### 2.2 Repaired runtime-evidence identity

```text
REPAIRED_RUNTIME_RUN_ID=33434874024
REPAIRED_RUNTIME_JOB_ID=99628745384
REPAIRED_SOURCE_DIR=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp
REPAIRED_BUILD_DIR=/home/runner/work/_temp/e004-runtime-evidence/llama.cpp-build
REPAIRED_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
REPAIRED_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
REPAIRED_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
RUNTIME_EVIDENCE_MANIFEST_SHA256=6f3e91fd162db6fd764a5915d34b50254cc91a07906eb602f833b02ff6dfb25d
```

### 2.3 One-shot diagnostic result

The canonical one-shot diagnostic was consumed exactly once:

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE
```

It produced:

```text
A1_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A2_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
B1_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B2_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
SHA_EQUAL_A1_A2=YES
SHA_EQUAL_B1_B2=YES
SHA_EQUAL_A1_B1=NO
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
DIAGNOSTIC_DISPOSITION=ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
```

The historical-layout cells reproduced the frozen historical build hash exactly. The repaired-layout cells were internally repeatable but produced a third hash, not the earlier repaired-runtime hash.

Therefore this policy preserves:

```text
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION=NOT_REPRODUCED
HISTORICAL_BINARY_EQUIVALENCE_CLAIM=PROHIBITED
```

## 3. Retained-evidence exhaustion does not justify a causal claim

The retained records prove that absolute source/build layout can change output bytes under the pinned build, while normalized effective executable-search PATH identity was equal across the historical and repaired PATH spellings.

The pinned upstream build-info mechanism was also inspected at the exact tool revision. `cmake/build-info.cmake` at blob `c7005950c5612d1d93ca728386b10806b0043106` derives build metadata from the Git commit count/hash, compiler, and target. That static inspection does not establish the missing historical repaired-runtime cause.

No retained evidence currently proves which additional execution-context difference produced `18ff27aa...` rather than diagnostic repaired-layout `1f5c96a6...`.

```text
BUILD_INFO_CAUSAL_ATTRIBUTION=NOT_ESTABLISHED
PATH_SEARCH_CAUSAL_ATTRIBUTION=PROHIBITED_EFFECTIVE_PATHS_EQUAL
UNOBSERVED_CAUSE_INVENTION=PROHIBITED
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
```

This policy chooses a future assurance mechanism without rewriting that scientific history.

## 4. Policy decision

For a future conversion subject that has obtained its own separate canonical execution authority, commandMed may accept an execution-time `llama-quantize` identity instead of requiring its SHA-256 to equal either historical binary hash **only if every requirement in this document is satisfied before model conversion begins**.

The accepted mechanism is:

```text
FUTURE_CONVERSION_TOOL_IDENTITY_MODE=SAME_SUBJECT_DOUBLE_BUILD_THEN_BIND
HISTORICAL_BINARY_HASH_AS_REQUIRED_TARGET=NO
EXECUTION_TIME_BINARY_IDENTITY_REQUIRED=YES
SAME_ABSOLUTE_PATH_DOUBLE_BUILD_REQUIRED=YES
FULL_FILE_SHA256_EQUALITY_BETWEEN_DOUBLE_BUILDS=REQUIRED
ELF_BUILD_ID_EQUALITY_BETWEEN_DOUBLE_BUILDS=REQUIRED_IF_PRESENT
INTEGER_BYTE_SIZE_EQUALITY_BETWEEN_DOUBLE_BUILDS=REQUIRED
BUILD_MANIFEST_EQUALITY_BETWEEN_DOUBLE_BUILDS=REQUIRED
FIRST_MODEL_BYTE_READ_BEFORE_TOOL_BINDING=PROHIBITED
CONVERSION_BEFORE_TOOL_BINDING=PROHIBITED
```

The execution-time identity is valid only for the exact separately authorized RunManifest and exact execution subject that produced it.

## 5. Pre-execution identities that must be frozen

A future conversion authority may not rely on an open-ended runtime discovery process. Before that execution begins, its exact RunManifest must freeze at least:

```text
run_manifest_id
run_manifest_sha256
policy_id=E004-EXECUTION-TIME-IDENTITY-BINDING-V1
tool_repository
tool_commit
tool_tree
converter_entrypoint_sha256
canonical_dependency_requirement_surface_sha256
source_manifest_sha256
dependency_set_manifest_sha256
python_runtime_path
python_runtime_sha256
resolver_identity
installed_environment_expected_identity_or_exact_derivation_contract
runner_class
runner_image_os
runner_image_version
cmake_path
cmake_sha256
ninja_path
ninja_sha256
c_compiler_path
c_compiler_sha256
cxx_compiler_path
cxx_compiler_sha256
exact_source_absolute_path
exact_build_absolute_path
exact_home_path
exact_tmp_path
exact_syntactic_path_value
exact_normalized_path_identity
exact_cmake_configure_argv
exact_build_argv
network_boundary_identity
credential_state_policy
exact_conversion_subject_identity
exact_conversion_source_directory
exact_conversion_output_directory
exact_conversion_argv
exact_quantize_argv
storage_boundary_identity
retention_enforcement_identity
compute_resource_identity
resource_authorization_basis
expected_cpu_ram_disk_envelope
expected_max_wallclock
zero_incremental_spend_disposition
```

Placeholder-bearing or runtime-selected alternatives are not conforming pre-execution identities.

If a field cannot truthfully be frozen until the concrete future environment exists, the future authority must remain unmerged/unexecuted until that field is concrete. This policy does not turn `NEEDS_EVIDENCE` into a wildcard.

## 6. Same-subject double-build protocol

Any later execution authority adopting this policy must require exactly two pre-model builds under the same frozen execution subject.

For both builds:

1. use the same exact source tree and commit/tree identity;
2. use the same exact absolute source path;
3. clean and recreate the same exact absolute build path between builds;
4. use the same exact HOME, TMPDIR, syntactic PATH, normalized PATH identity, locale, and security boundary;
5. use the same exact compiler, CMake, Ninja, Python, and other bound executable identities;
6. use the exact same CMake configure argv and build argv;
7. prohibit model-weight access, conversion, inference, benchmark execution, contamination assessment, A15, training, credentials, uploads, and paid-resource escalation during both builds;
8. retain identity evidence for each build before deciding whether the execution may proceed.

The two builds must independently record at least:

```text
llama_quantize_sha256
llama_quantize_exact_integer_bytes
elf_build_id_if_present
cmake_cache_sha256
compile_commands_sha256
generated_build_info_sha256
build_environment_manifest_sha256
source_absolute_path_presence_disposition
build_absolute_path_presence_disposition
security_boundary_evidence_sha256
```

The following gate is noncompensable:

```text
DOUBLE_BUILD_FULL_FILE_SHA256_EQUAL=YES_REQUIRED
DOUBLE_BUILD_INTEGER_BYTES_EQUAL=YES_REQUIRED
DOUBLE_BUILD_ELF_BUILD_ID_EQUAL=YES_REQUIRED_IF_PRESENT
DOUBLE_BUILD_CMAKE_CACHE_EQUAL=YES_REQUIRED
DOUBLE_BUILD_COMPILE_COMMANDS_EQUAL=YES_REQUIRED
DOUBLE_BUILD_GENERATED_BUILD_INFO_EQUAL=YES_REQUIRED
DOUBLE_BUILD_SECURITY_BOUNDARY_EQUAL=YES_REQUIRED
```

Any failure is terminal for that exact execution attempt.

```text
DOUBLE_BUILD_MISMATCH_DISPOSITION=ABORT_BEFORE_MODEL_BYTES
AUTOMATIC_RETRY_AFTER_DOUBLE_BUILD_MISMATCH=PROHIBITED
ALTERNATE_TOOL_REVISION_AFTER_MISMATCH=PROHIBITED
PATH_SUBSTITUTION_AFTER_MISMATCH=PROHIBITED
BUILD_FLAG_SUBSTITUTION_AFTER_MISMATCH=PROHIBITED
```

A later retry or changed subject requires separately reviewed authority; this policy does not supply it.

## 7. Execution-time binding after a successful double build

Only after the double-build gate passes may the exact common binary identity be bound as the tool identity for that RunManifest.

```text
EXECUTION_TIME_LLAMA_QUANTIZE_SHA256=<EXACT_EQUAL_DOUBLE_BUILD_SHA256>
EXECUTION_TIME_LLAMA_QUANTIZE_INTEGER_BYTES=<EXACT_EQUAL_DOUBLE_BUILD_BYTES>
EXECUTION_TIME_ELF_BUILD_ID=<EXACT_EQUAL_DOUBLE_BUILD_BUILD_ID_IF_PRESENT>
EXECUTION_TIME_BUILD_MANIFEST_SHA256=<EXACT_BOUND_BUILD_MANIFEST>
EXECUTION_TIME_TOOL_BINDING_SCOPE=EXACT_RUN_MANIFEST_ONLY
```

The binding must be recorded before the first model/source-weight byte is opened by conversion logic.

The selected bound binary must then remain unchanged through the exact conversion/quantization stage. Immediately before use and immediately after the last permitted use, its SHA-256 and integer byte size must be recomputed and must equal the execution-time binding.

```text
PRE_USE_BINARY_REHASH=REQUIRED
POST_USE_BINARY_REHASH=REQUIRED
PRE_USE_SHA_MATCH=YES_REQUIRED
POST_USE_SHA_MATCH=YES_REQUIRED
BINARY_MUTATION_DURING_SUBJECT=FAIL_CLOSED
```

No historical hash equality is inferred from this binding.

## 8. No cross-run promotion or binary reuse

An execution-time binary identity is not a reusable release artifact merely because it passed one exact RunManifest.

```text
EXECUTION_TIME_BINARY_PERSISTENT_REUSE=PROHIBITED_BY_THIS_POLICY
EXECUTION_TIME_BINARY_CROSS_RUN_REUSE=PROHIBITED_BY_THIS_POLICY
EXECUTION_TIME_BINARY_RELEASE_ARTIFACT_STATUS=NO
EXECUTION_TIME_BINARY_PROVES_HISTORICAL_EQUIVALENCE=NO
EXECUTION_TIME_BINARY_PROVES_GENERAL_BUILD_REPRODUCIBILITY=NO
```

A later run must perform its own separately authorized same-subject binding unless a future canonical policy explicitly creates a persistent reproducible tool artifact with its own provenance and qualification evidence.

## 9. Historical hashes remain evidence, not acceptance targets

The three observed binary identities retain their exact meanings:

```text
E1D88_HASH_ROLE=HISTORICAL_BUILD_EVIDENCE_AND_DIAGNOSTIC_A_LAYOUT_REPRODUCTION
18FF27_HASH_ROLE=HISTORICAL_REPAIRED_RUNTIME_EVIDENCE_ONLY
1F5C96_HASH_ROLE=DIAGNOSTIC_B_LAYOUT_REPEATABLE_OBSERVATION_ONLY
```

This policy does not declare any pair equivalent and does not declare any one of them the future conversion binary.

```text
E1D88_EQUALS_18FF27=NO
E1D88_EQUALS_1F5C96=NO
18FF27_EQUALS_1F5C96=NO
HISTORICAL_REPAIRED_RUNTIME_CAUSE=NEEDS_EVIDENCE
```

The unresolved causal question remains a valid evidence defect. It is no longer proposed as a mandatory historical-hash reconstruction target for a future separately authorized conversion because the future assurance boundary is the exact double-built execution subject itself.

## 10. Composition with existing conversion policy

This policy does not supersede the canonical Decision B normalization/metadata policy. Any future conversion must still preserve its source-byte, directory-basename, converter-mode, metadata, tokenizer, config, and post-conversion attestation requirements.

```text
NORMALIZATION_METADATA_POLICY=E004-DECISION-B-CONVERSION-NORMALIZATION-METADATA-V1
SOURCE_BYTE_MUTATION=PROHIBITED
SOURCE_DIRECTORY_BASENAME_DRIFT=PROHIBITED
REMOTE_HF_MODE=PROHIBITED_FOR_PREPARED_DECISION_B_SUBJECT
TRUST_REMOTE_CODE=FALSE_REQUIRED
POST_CONVERSION_METADATA_ATTESTATION=REQUIRED_IF_CONVERSION_LATER_AUTHORIZED
```

Execution-time tool identity binding cannot compensate for a source, metadata, lineage, storage, contamination, governance, or scientific-policy failure.

## 11. What this policy resolves and what it does not

After canonical merge, this policy would resolve only the narrow policy disposition requested by the rebuild-reproducibility authority:

```text
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION_AS_MANDATORY_PRECONDITION=REMOVED_BY_POLICY
```

It would not produce operational execution readiness by itself:

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO_UNCHANGED
EXACT_FUTURE_CONVERSION_SOURCE_DIRECTORY=NEEDS_EVIDENCE
EXACT_FUTURE_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
EXACT_FUTURE_CONVERSION_ARGV=NEEDS_EVIDENCE
EXACT_FUTURE_QUANTIZE_ARGV=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
CONVERSION_PHASE_NETWORK_BOUNDARY=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
CONVERSION_PHASE_CREDENTIAL_ATTESTATION=NEEDS_EXACT_FUTURE_SUBJECT_BINDING
```

Nor does it resolve independent E004 prerequisites:

```text
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 12. Authority and claims boundary

Even after a qualified canonical merge:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_AUTHORITY=UNCHANGED_BY_THIS_POLICY
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
SAFE_FOR_PATIENT_USE=NO
CLINICALLY_VALIDATED=NO
RELEASE_READY=NO
```

No execution may be inferred from policy acceptance.

## 13. Failure semantics for any future adopter

A future authority that adopts this policy must fail closed if any of the following occurs:

- a frozen source/tool/dependency/runtime identity does not match;
- actual absolute source/build paths differ from the RunManifest;
- syntactic or normalized PATH identity differs from the RunManifest;
- the two pre-model builds differ in required identity evidence;
- the generated build-info evidence differs between the two builds;
- the binary changes between binding, pre-use, and post-use;
- model bytes are opened before the tool-binding gate passes;
- a retry, path change, tool revision change, compiler change, flag change, or dependency change is attempted without separate authority;
- a storage, retention, resource, network, credential, provenance, contamination, safety, or scientific prerequisite is absent or non-PASS;
- the future execution would exceed its exact spend/resource authority.

No average metric or later successful conversion can compensate for one of these identity failures.

## 14. Required independent review and merge-exit gate

This policy has no canonical effect until a fresh independent exact-head repository/governance review verifies the complete diff and concludes that no material correctness, evidence-integrity, reproducibility, security, or authority-boundary blocker remains.

The reviewer must verify at least:

```text
EXACT_CANONICAL_BASE_MATCHES_MAIN=YES
HISTORICAL_BUILD_IDENTITY_RETAINED_EXACTLY=YES
REPAIRED_RUNTIME_IDENTITY_RETAINED_EXACTLY=YES
DIAGNOSTIC_A1_A2_AND_B1_B2_IDENTITIES_RETAINED_EXACTLY=YES
HISTORICAL_TWO_HASH_SPLIT_REMAINS_NOT_REPRODUCED=YES
REBUILD_MISMATCH_CAUSE_REMAINS_NEEDS_EVIDENCE=YES
NO_FALSE_HISTORICAL_BINARY_EQUIVALENCE=YES
NO_UNSUPPORTED_BUILD_INFO_CAUSAL_CLAIM=YES
EXECUTION_TIME_BINDING_IS_EXACT_RUN_MANIFEST_ONLY=YES
SAME_SUBJECT_DOUBLE_BUILD_REQUIRED_BEFORE_MODEL_BYTES=YES
DOUBLE_BUILD_MISMATCH_FAILS_CLOSED=YES
AUTOMATIC_RETRY_AUTHORITY_CREATED=NO
CROSS_RUN_BINARY_REUSE_CREATED=NO
NORMALIZATION_METADATA_POLICY_PRESERVED=YES
PERSISTENT_CONVERSION_SUBJECT_FIELDS_REMAIN_UNRESOLVED=YES
CONVERSION_EXECUTION_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_INCOMPLETE=YES
E005_REMAINS_NOT_REACHED=YES
PROJECT_FINISHED_REMAINS_NO=YES
MATERIAL_BLOCKER=NO
```

Any `MATERIAL_BLOCKER=YES` finding must be resolved on a new exact head and independently re-reviewed before merge. Self-review is not sufficient.

## 15. Explicit exclusions

This artifact does not authorize or perform:

- a rerun of run `33507754943` or any job from it;
- a second rebuild-reproducibility diagnostic;
- binary-difference localization execution;
- normalization experiments;
- model/source-weight download, loading, conversion, quantization, or inference;
- benchmark or device execution;
- contamination assessment;
- A15 activation;
- training or gradient updates;
- Private Gold, PHI, restricted, or gated asset access;
- credentials or provider generation;
- artifact upload or persistent binary promotion;
- external clinical/statistical reviewer outreach;
- paid or larger runner use;
- procurement, payment, or spend;
- clinical, deployment, release, superiority, SOTA, or safety claims.

The next dependency-safe unit after a qualified canonical merge must be selected only by rereading live canonical E004 governance and identifying the next prerequisite that can be truthfully completed without inventing absent operational or scientific evidence.
