# E004 Execution-Time Identity Binding Policy Disposition — 2026-09-02

**Spec:** 007 SFT V1  
**Canonical base:** `3da7d95b8dfc7ee1548cc8ece58c5cb55cbc82a6`  
**Artifact class:** non-executing bounded policy disposition  
**Depends on:** canonical rebuild-reproducibility diagnostic authority, implementation, retained terminal evidence, and canonical result reconciliation  
**Authority effect before canonical merge:** NONE  
**Model conversion authority:** NONE  
**Conversion execution authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve only the policy question left open by the canonical E004 rebuild-reproducibility diagnostic: whether a future, separately authorized conversion execution may rely on a rigorously fail-closed execution-time `llama-quantize` identity even though the earlier repaired-runtime binary has not been reconstructed byte-for-byte.

This document performs no build, download, model/source-weight access, conversion, inference, benchmark execution, contamination assessment, A15 activation, training, credential use, protected-data access, upload, procurement, payment, or spend.

Canonical merge of this document after fresh independent exact-head review would establish only:

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

This is not a historical-binary equivalence claim and is not permission to execute a conversion.

## 2. Controlling retained evidence

The policy is bounded by the exact canonical evidence already retained by commandMed.

### 2.1 Historical build evidence

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
HISTORICAL_COMPILE_COMMANDS_SHA256=567ad70c6090af9fcce508c41eddba51681669f1079e52e6c285c5cc471d713e
```

### 2.2 Repaired runtime evidence

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

The repaired-runtime workflow did not retain a `compile_commands.json` SHA-256 in the canonical runtime manifest. This policy does not invent one retroactively.

### 2.3 One-shot diagnostic evidence

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE

A1_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A2_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
B1_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B2_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
A1_A2_BYTE_DIFFERENCE_COUNT=0
B1_B2_BYTE_DIFFERENCE_COUNT=0
A_B_BYTE_DIFFERENCE_COUNT=760129
A1_A2_BUILD_ID_EQUAL=YES
B1_B2_BUILD_ID_EQUAL=YES
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
DIAGNOSTIC_DISPOSITION=ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
```

The diagnostic reproduced the frozen historical build hash under the historical absolute layout. Its repaired-layout cells were internally repeatable but produced a third hash rather than the earlier repaired-runtime hash.

The diagnostic did not compute an ELF LOAD SHA-256 and this policy makes no such claim.

The retained evidence therefore continues to require:

```text
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION=NOT_REPRODUCED
HISTORICAL_BINARY_EQUIVALENCE_CLAIM=PROHIBITED
PATH_SEARCH_CAUSAL_ATTRIBUTION=PROHIBITED_EFFECTIVE_PATHS_EQUAL
UNOBSERVED_CAUSE_INVENTION=PROHIBITED
```

## 3. Policy decision

For a future conversion subject that has obtained its own separate canonical execution authority, commandMed may accept an execution-time `llama-quantize` identity instead of requiring its SHA-256 to equal either historical binary hash **only if every pre-conversion requirement in this document is satisfied before model conversion begins; post-use requirements must pass before the execution result is accepted**.

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

The execution-time identity is valid only for the exact separately authorized execution subject and exact RunManifest that anchor it.

## 4. Exact execution-subject bindings must be frozen

A future conversion authority may not rely on open-ended runtime discovery. Before execution begins, the exact execution-subject package anchored by the RunManifest — including the RunManifest itself and its directly referenced canonical component, environment, storage/resource, and authority records — must collectively freeze at least the following identities or exact derivation contracts:

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

These are required bindings for the exact execution subject; they are **not** all required to be direct JSON properties of `RunManifest`.

```text
RUN_MANIFEST_CLOSED_SCHEMA_WIDENED_BY_THIS_POLICY=NO
RUN_MANIFEST_VALIDATOR_WIDENED_BY_THIS_POLICY=NO
NEW_DIRECT_RUN_MANIFEST_FIELDS_AUTHORIZED_BY_THIS_POLICY=NO
```

The current closed RunManifest schema and `_RUN_FIELDS` remain unchanged. If a future execution design requires any listed identity as a new direct RunManifest property, that schema/validator change requires its own bounded implementation authority, tests, exact-head qualification, and independent review before use.

Placeholder-bearing or runtime-selected alternatives are not conforming pre-execution bindings. If an identity cannot truthfully be frozen until a concrete future environment exists, the future authority must remain unmerged and unexecuted until that binding is concrete. This policy does not turn `NEEDS_EVIDENCE` into a wildcard.

## 5. Same-subject double-build protocol

Any later execution authority adopting this policy must require exactly two pre-model builds under the same frozen execution subject.

For both builds:

1. use the same exact source commit and tree;
2. use the same exact absolute source path;
3. clean and recreate the same exact absolute build path between builds;
4. use the same exact HOME, TMPDIR, syntactic PATH, normalized PATH identity, locale, and security boundary;
5. use the same exact compiler, CMake, Ninja, Python, and other bound executable identities;
6. use the same exact CMake configure argv and build argv;
7. prohibit model/source-weight access, conversion, inference, benchmark execution, contamination assessment, A15 activation, training, credentials, uploads, and paid-resource escalation during both builds;
8. retain identity evidence for each build before deciding whether the execution may proceed.

Each build must independently record at least:

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

A future implementation may define a canonical build manifest that contains these bound observations, but any such implementation is outside this policy-only PR.

The double-build gate is noncompensable:

```text
DOUBLE_BUILD_FULL_FILE_SHA256_EQUAL=YES_REQUIRED
DOUBLE_BUILD_INTEGER_BYTES_EQUAL=YES_REQUIRED
DOUBLE_BUILD_ELF_BUILD_ID_EQUAL=YES_REQUIRED_IF_PRESENT
DOUBLE_BUILD_CMAKE_CACHE_EQUAL=YES_REQUIRED
DOUBLE_BUILD_COMPILE_COMMANDS_EQUAL=YES_REQUIRED
DOUBLE_BUILD_GENERATED_BUILD_INFO_EQUAL=YES_REQUIRED
DOUBLE_BUILD_SECURITY_BOUNDARY_EQUAL=YES_REQUIRED
DOUBLE_BUILD_BUILD_MANIFEST_EQUAL=YES_REQUIRED
```

Any failure is terminal for that exact execution attempt:

```text
DOUBLE_BUILD_MISMATCH_DISPOSITION=ABORT_BEFORE_MODEL_BYTES
AUTOMATIC_RETRY_AFTER_DOUBLE_BUILD_MISMATCH=PROHIBITED
ALTERNATE_TOOL_REVISION_AFTER_MISMATCH=PROHIBITED
PATH_SUBSTITUTION_AFTER_MISMATCH=PROHIBITED
BUILD_FLAG_SUBSTITUTION_AFTER_MISMATCH=PROHIBITED
```

A later retry or changed execution subject requires separately reviewed authority; this policy does not supply it.

## 6. Execution-time binding and completion attestation

Only after every pre-conversion binding and the complete double-build gate pass may the exact common binary identity be bound to the exact execution subject.

```text
EXECUTION_TIME_LLAMA_QUANTIZE_SHA256=<EXACT_EQUAL_DOUBLE_BUILD_SHA256>
EXECUTION_TIME_LLAMA_QUANTIZE_INTEGER_BYTES=<EXACT_EQUAL_DOUBLE_BUILD_BYTES>
EXECUTION_TIME_ELF_BUILD_ID=<EXACT_EQUAL_DOUBLE_BUILD_BUILD_ID_IF_PRESENT>
EXECUTION_TIME_BUILD_MANIFEST_SHA256=<EXACT_EQUAL_DOUBLE_BUILD_MANIFEST_SHA256>
EXECUTION_TIME_TOOL_BINDING_SCOPE=EXACT_RUN_MANIFEST_AND_EXECUTION_SUBJECT_ONLY
```

The binding must be recorded before the first model/source-weight byte is opened by conversion logic.

Immediately before first permitted use, the binary SHA-256 and integer byte size must be recomputed and match the binding. The selected bound binary must remain unchanged through the exact conversion/quantization stage. Immediately after its last permitted use, its SHA-256 and integer byte size must be recomputed again.

```text
PRE_USE_BINARY_REHASH=REQUIRED
PRE_USE_SHA_MATCH=YES_REQUIRED
POST_USE_BINARY_REHASH=REQUIRED
POST_USE_SHA_MATCH=YES_REQUIRED
BINARY_MUTATION_DURING_SUBJECT=FAIL_CLOSED
POST_USE_ATTESTATION_IS_EXECUTION_RESULT_ACCEPTANCE_GATE=YES
```

A post-use mismatch invalidates acceptance of the execution result even if conversion code otherwise completed successfully. It does not authorize retry.

No historical hash equality is inferred from execution-time binding.

## 7. No cross-run promotion or binary reuse

```text
EXECUTION_TIME_BINARY_PERSISTENT_REUSE=PROHIBITED_BY_THIS_POLICY
EXECUTION_TIME_BINARY_CROSS_RUN_REUSE=PROHIBITED_BY_THIS_POLICY
EXECUTION_TIME_BINARY_RELEASE_ARTIFACT_STATUS=NO
EXECUTION_TIME_BINARY_PROVES_HISTORICAL_EQUIVALENCE=NO
EXECUTION_TIME_BINARY_PROVES_GENERAL_BUILD_REPRODUCIBILITY=NO
```

A later run must perform its own separately authorized same-subject binding unless a future canonical policy explicitly establishes a persistent reproducible tool artifact with its own provenance and qualification evidence.

The historical identities remain evidence, not future acceptance targets:

```text
E1D88_HASH_ROLE=HISTORICAL_BUILD_EVIDENCE_AND_DIAGNOSTIC_A_LAYOUT_REPRODUCTION
18FF27_HASH_ROLE=HISTORICAL_REPAIRED_RUNTIME_EVIDENCE_ONLY
1F5C96_HASH_ROLE=DIAGNOSTIC_B_LAYOUT_REPEATABLE_OBSERVATION_ONLY
HISTORICAL_REPAIRED_RUNTIME_CAUSE=NEEDS_EVIDENCE
```

## 8. Composition with existing conversion policy

This policy does not supersede the canonical Decision B normalization/metadata policy. Any future separately authorized conversion must still satisfy its source-byte, directory-basename, converter-mode, metadata, tokenizer, configuration, and post-conversion attestation requirements.

```text
NORMALIZATION_METADATA_POLICY=E004-DECISION-B-CONVERSION-NORMALIZATION-METADATA-V1
SOURCE_BYTE_MUTATION=PROHIBITED
SOURCE_DIRECTORY_BASENAME_DRIFT=PROHIBITED
REMOTE_HF_MODE=PROHIBITED_FOR_PREPARED_DECISION_B_SUBJECT
TRUST_REMOTE_CODE=FALSE_REQUIRED
POST_CONVERSION_METADATA_ATTESTATION=REQUIRED_IF_CONVERSION_LATER_AUTHORIZED
```

Execution-time tool identity binding cannot compensate for a source, metadata, lineage, storage, contamination, governance, safety, or scientific-policy failure.

## 9. What this policy resolves and what remains blocked

After a qualified canonical merge, this policy would resolve only:

```text
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=ACCEPTED_FAIL_CLOSED_FOR_FUTURE_SEPARATELY_AUTHORIZED_CONVERSION
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION_AS_MANDATORY_PRECONDITION=REMOVED_BY_POLICY
```

It would not establish operational conversion readiness:

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

Nor would it resolve independent E004 prerequisites:

```text
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 10. Authority and claims boundary

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

## 11. Failure semantics for any future adopter

A future authority that adopts this policy must fail closed if any of the following occurs:

- a frozen source/tool/dependency/runtime identity does not match;
- the execution-subject package does not resolve all required bindings before execution;
- actual absolute source/build paths differ from the frozen execution-subject bindings;
- syntactic or normalized PATH identity differs from the frozen execution-subject bindings;
- the two pre-model builds differ in any required equality evidence;
- the generated build-info evidence differs between the two builds;
- the build manifests differ between the two builds;
- the binary changes between binding, pre-use, and post-use;
- model/source-weight bytes are opened before the tool-binding gate passes;
- a retry, path change, tool revision change, compiler change, flag change, or dependency change is attempted without separate authority;
- a storage, retention, resource, network, credential, provenance, contamination, safety, or scientific prerequisite is absent or non-PASS;
- the future execution would exceed its exact spend/resource authority.

No average metric or later successful conversion can compensate for one of these identity failures.

## 12. Required independent review and merge-exit gate

This policy has no canonical effect until a fresh independent exact-head repository/governance review verifies the complete diff and concludes that no material correctness, evidence-integrity, reproducibility, security, integration, or authority-boundary blocker remains.

The reviewer must verify at least:

```text
EXACT_CANONICAL_BASE_MATCHES_MAIN=YES
HISTORICAL_BUILD_IDENTITY_RETAINED_EXACTLY=YES
REPAIRED_RUNTIME_IDENTITY_RETAINED_EXACTLY=YES
DIAGNOSTIC_A1_A2_AND_B1_B2_IDENTITIES_RETAINED_EXACTLY=YES
HISTORICAL_TWO_HASH_SPLIT_REMAINS_NOT_REPRODUCED=YES
REBUILD_MISMATCH_CAUSE_REMAINS_NEEDS_EVIDENCE=YES
NO_FALSE_HISTORICAL_BINARY_EQUIVALENCE=YES
NO_UNSUPPORTED_ELF_LOAD_CLAIM=YES
PRE_CONVERSION_AND_POST_USE_GATES_SEPARATED=YES
EXECUTION_SUBJECT_BINDINGS_DO_NOT_WIDEN_RUN_MANIFEST_SCHEMA=YES
SAME_SUBJECT_DOUBLE_BUILD_REQUIRED_BEFORE_MODEL_BYTES=YES
DOUBLE_BUILD_BUILD_MANIFEST_EQUALITY_EXPLICIT=YES
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

## 13. Explicit exclusions

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
