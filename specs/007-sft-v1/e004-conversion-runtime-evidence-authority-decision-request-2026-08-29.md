# E004 Conversion Runtime Evidence Authority Decision Request — 2026-08-29

**Spec:** 007 SFT V1  
**Canonical base:** `9ce75abedb329fe0bd3b618511eac48f722e538a`  
**Artifact class:** Founder decision request / authority proposal only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Model/source-weight acquisition performed:** NO  
**Model conversion or quantization performed:** NO  
**Model execution performed:** NO  
**Benchmark/device execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## Purpose

This document converts the current E004 conversion-runtime blocker into one exact bounded Founder decision surface without fabricating persistent bytes or reusing the exhausted build-evidence allowance.

The canonical repository already contains two real but intentionally ephemeral evidence lanes:

1. E002 run `33183096268` materialized and cryptographically verified the exact frozen Granite PRIMARY and Qwen3-4B CONTROL source bundles on GitHub-hosted runners, then destroyed those bytes with the runner because artifact upload was prohibited.
2. E004 build-evidence run `33187438094` materialized exact `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`, built `llama-quantize`, and recorded exact build/runtime identities on a GitHub-hosted runner, then destroyed those bytes with the runner because artifact upload was prohibited.

Those runs prove evidence existence, but they do not create a future conversion-time workspace. Canonical V4 therefore remains correct:

```text
PERSISTENT_LLAMA_QUANTIZE_EXECUTABLE_PRESENT=NO
PERSISTENT_BUILD_DIRECTORY_PRESENT=NO
PERSISTENT_EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_SOURCE_PATH=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_LLAMA_QUANTIZE_PATH=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

The narrow purpose of this request is to authorize, if the Founder explicitly selects it, one **runtime-evidence-only** execution that resolves the remaining converter runtime/dependency identities needed to prepare a later exact reconstruction-based conversion subject. It does not authorize model conversion.

## 1. Canonical inputs already established

### Frozen Decision B subjects

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
GRANITE_SUBJECT=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
GRANITE_SOURCE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
QWEN_CONTROL_SUBJECT=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
QWEN_CONTROL_SOURCE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
QWEN_CONTROL_WINNER_ELIGIBLE=NO
```

### Existing local source-integrity evidence

```text
E002_SOURCE_INTEGRITY_RUN=33183096268
GRANITE_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
QWEN_LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
```

No source-model bytes from that run remain available.

### Existing bounded build evidence

```text
E004_BUILD_EVIDENCE_RUN=33187438094
RUNNER_LABEL=ubuntu-24.04
RUNNER_IMAGE_VERSION=20260823.283.1
PYTHON_VERSION=3.12.3
PYTHON_PATH=/usr/bin/python3.12
PYTHON_SHA256=1643dacd9feaedc58f3cc581e4d22577dfe25c09b10282936186ccf0f2e61118
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_QUANTIZE_EPHEMERAL_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
LLAMA_QUANTIZE_EPHEMERAL_INTEGER_BYTES=6513680
BUILD_EVIDENCE_MANIFEST_SHA256=84f4915eee7b577feb71ea7daf57a6d16fdf86b1ac2771234599cf52ca6032c8
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
```

The executable hash above is historical evidence for run `33187438094`; it is not a claim that the binary remains present or that a later rebuild must silently be assumed identical.

## 2. Canonical converter dependency surface

The pinned runtime-dependency reconciliation already binds these exact source manifests at `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`:

```text
ROOT_PYPROJECT=pyproject.toml
ROOT_PYPROJECT_GIT_BLOB=46cf68ca1a398d40dc71f0eff043c03ceeaa73fe
ROOT_REQUIREMENTS=requirements.txt
ROOT_REQUIREMENTS_GIT_BLOB=f2a18d62879b4e37249b566d6d85fd9485fb20e2
HF_CONVERTER_REQUIREMENTS=requirements/requirements-convert_hf_to_gguf.txt
HF_CONVERTER_REQUIREMENTS_GIT_BLOB=b1f7c863e27e184e55408c9e5792158301c86547
LEGACY_CONVERTER_REQUIREMENTS=requirements/requirements-convert_legacy_llama.txt
LEGACY_CONVERTER_REQUIREMENTS_GIT_BLOB=28221fad0ce9790f91dc6adfbc893010454bdfe5
LOCAL_GGUF_PYPROJECT=gguf-py/pyproject.toml
LOCAL_GGUF_PYPROJECT_GIT_BLOB=d11c34a2186d7180345f0050c746df51043b5620
LOCAL_GGUF_VERSION=0.19.0
```

The canonical declared dependency surface includes:

```text
PYTHON_DECLARED_RANGE=>=3.10,<3.15
TORCH_REQUIREMENT=torch==2.11.0
TORCH_CPU_INDEX=https://download.pytorch.org/whl/cpu
NUMPY_REQUIREMENT=~=1.26.4
SENTENCEPIECE_REQUIREMENT=>=0.1.98,<0.3.0
TRANSFORMERS_REQUIREMENT===4.57.6
GGUF_DISTRIBUTION_REQUIREMENT=>=0.1.0
PROTOBUF_REQUIREMENT=>=4.21.0,<5.0.0
LOCAL_GGUF_NUMPY=>=1.17
LOCAL_GGUF_TQDM=>=4.27
LOCAL_GGUF_PYYAML=>=5.1
LOCAL_GGUF_REQUESTS=>=2.25
```

These manifests are not an exact transitive lock:

```text
UPSTREAM_FULLY_RESOLVED_DEPENDENCY_LOCK_PRESENT=NO
UPSTREAM_MANIFESTS_EQUAL_EXACT_TRANSITIVE_RUNTIME=NO
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
PACKAGE_INDEX_SNAPSHOT_OR_WHEELHOUSE_IDENTITY=NEEDS_EVIDENCE
```

The runtime-evidence request therefore exists to resolve and bind the exact artifact set rather than treating compatible-version ranges as PASS evidence.

## 3. Local GGUF runtime rule is non-negotiable

Canonical Decision B runtime policy requires the local pinned `gguf-py` source tree to be the selected runtime code:

```text
LOCAL_GGUF_SOURCE_MODE=REQUIRED
LOCAL_GGUF_SOURCE_TREE=gguf-py@c1d0e7a004015f23bc0233470b747b596f29b264
LOCAL_GGUF_PROJECT_VERSION=0.19.0
NO_LOCAL_GGUF_ENVIRONMENT_VARIABLE=PROHIBITED
NO_LOCAL_GGUF_MUST_BE_UNSET=YES
EXTERNAL_GGUF_CODE_AS_SELECTED_RUNTIME=PROHIBITED
REMOTE_HF_CONVERSION_MODE=NOT_SELECTED
REMOTE_MODEL_NETWORK_USE=PROHIBITED
```

The upstream legacy requirement `gguf>=0.1.0` must not be interpreted as authority to execute arbitrary resolver-selected GGUF code. Resolver/package evidence may include the distribution requirement as part of upstream compatibility analysis, but runtime attestation must prove that the imported `gguf` module resolves under the exact pinned local source tree.

The selected Granite/Qwen paths do not create `mistral_common` authority:

```text
MISTRAL_COMMON_REQUIRED_FOR_SELECTED_DECISION_B_SUBJECTS=NO_EVIDENCE_OF_REQUIREMENT
MISTRAL_COMMON_SELECTED_RUNTIME_AUTHORITY=NONE
```

## 4. Remaining runtime-evidence gap

The Decision B conversion boundary requires exact runtime evidence before conversion execution authority can be created. The currently unresolved runtime-specific fields include:

```text
PYTHON_RUNTIME_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
RESOLVER_AND_VERSION=NEEDS_EVIDENCE
PACKAGE_INDEX_OR_OFFLINE_WHEELHOUSE_BOUNDARY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_OR_INTERPRETER_IDENTITY=NEEDS_EVIDENCE
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
GGUF_IMPORTED_FILE_PATH=NEEDS_EVIDENCE
GGUF_IMPORTED_SOURCE_IDENTITY=NEEDS_EVIDENCE
NO_LOCAL_GGUF_UNSET_ATTESTATION=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256_FOR_CONVERSION=NEEDS_EVIDENCE
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
```

## 5. Proposed next Founder decision

The exact proposed authority class is:

```text
PROPOSED_NEXT_FOUNDER_DECISION=E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY
DECISION_OPTION=AUTHORIZE_BOUNDED_RUNTIME_EVIDENCE_RUN
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
PURPOSE=RESOLVE_AND_BIND_EXACT_CONVERSION_RUNTIME_DEPENDENCY_AND_REBUILD_EVIDENCE_ONLY
CURRENT_AUTHORIZED_SPEND_USD=0
```

If selected, this authority would be a **new, separately bounded runtime-evidence authority**. It would not reopen, extend, reset, or rerun the exhausted build-evidence allowance from run `33187438094`.

```text
PRIOR_BUILD_EVIDENCE_ALLOWANCE_REMAINING=0
PRIOR_BUILD_EVIDENCE_WORKFLOW_RERUN_AUTHORIZED=NO
NEW_RUNTIME_EVIDENCE_AUTHORITY_EQUALS_PRIOR_BUILD_RERUN=NO
```

## 6. Exact actions proposed for the one runtime-evidence run

Only the following actions would be permitted:

```text
ACQUIRE_EXACT_LLAMA_CPP_SOURCE=YES
VERIFY_TOOL_COMMIT_AND_TREE=YES
VERIFY_CANONICAL_DEPENDENCY_MANIFEST_GIT_BLOBS=YES
RESOLVE_CONVERTER_PYTHON_DEPENDENCIES=YES
DOWNLOAD_RESOLVED_DEPENDENCY_ARTIFACTS_TO_EPHEMERAL_STAGING=YES
HASH_EVERY_RESOLVED_DEPENDENCY_ARTIFACT_BEFORE_INSTALL=YES
CAPTURE_RESOLVER_IDENTITY_AND_VERSION=YES
CREATE_EPHEMERAL_ISOLATED_PYTHON_ENVIRONMENT=YES
INSTALL_ONLY_FROM_LOCALLY_STAGED_HASHED_DEPENDENCY_ARTIFACTS=YES
BUILD_LLAMA_QUANTIZE_FROM_EXACT_AUTHORIZED_TOOL_SOURCE=YES
HASH_REBUILT_LLAMA_QUANTIZE=YES
IMPORT_LOCAL_GGUF_FOR_PATH_AND_SOURCE_ATTESTATION=YES
IMPORT_CONVERTER_MODEL_OR_ARCHITECTURE_MODULES=NO
LOAD_MODEL_WEIGHTS=NO
CAPTURE_EXACT_RUNTIME_AND_BUILD_MANIFESTS=YES
CAPTURE_EXACT_COMMAND_ARGV=YES
EMIT_EVIDENCE_TO_JOB_LOGS_ONLY=YES
```

Dependency resolution may use only the canonical dependency surface required by the pinned `convert_hf_to_gguf.py` path and pinned local `gguf-py` source selection. No optional inference stack, benchmark stack, training stack, telemetry package, Mistral-only dependency, or undeclared helper dependency may be added for convenience.

A resolved dependency artifact may be installed only after its exact package name, version, artifact filename, integer byte count, and SHA-256 are captured. Installation must then occur from the local ephemeral staging directory with network-disabled package installation semantics.

The runtime attestation must execute with `NO_LOCAL_GGUF` unset and must fail closed unless `gguf.__file__` resolves under the exact pinned `gguf-py` source tree. Presence of an external `gguf` distribution in resolver metadata does not authorize selection of external GGUF runtime code.

## 7. Explicitly prohibited actions

This proposed authority would preserve all of the following prohibitions:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_WEIGHT_QUANTIZATION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
REMOTE_HF_CONVERSION_MODE=PROHIBITED
REMOTE_MODEL_NETWORK_USE=PROHIBITED
EXTERNAL_GGUF_CODE_AS_SELECTED_RUNTIME=PROHIBITED
MISTRAL_COMMON_SELECTED_RUNTIME=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
SELECTION_SUITE_CONSTRUCTION=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PHI=PROHIBITED
GATED_ASSETS=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
TRAINING=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
CACHE_UPLOAD=PROHIBITED
WORKFLOW_ARTIFACT_UPLOAD=PROHIBITED
RELEASE_ASSET_UPLOAD=PROHIBITED
PACKAGE_REGISTRY_UPLOAD=PROHIBITED
REPOSITORY_BINARY_COMMIT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

No model repository or Hugging Face model payload endpoint is required or authorized for this runtime-evidence run.

## 8. Proposed network and credential boundary

Network is permitted only during explicit Phase A provisioning for the exact public tool source and exact converter dependency artifacts.

The proposed allowed public destination families are bounded to:

```text
PHASE_A_ALLOWED_TOOL_SOURCE_HOST=github.com
PHASE_A_ALLOWED_PYPI_INDEX_HOST=pypi.org
PHASE_A_ALLOWED_PYPI_ARTIFACT_HOST=files.pythonhosted.org
PHASE_A_ALLOWED_TORCH_CPU_INDEX_HOST=download.pytorch.org
OTHER_PACKAGE_INDEX_OR_MIRROR=PROHIBITED
HUGGING_FACE_MODEL_ENDPOINT=PROHIBITED
MODEL_PROVIDER_ENDPOINT=PROHIBITED
```

Any exact future workflow subject must bind concrete URLs/commands and fail closed if resolution redirects to or requires an undeclared host. This decision request does not authorize arbitrary internet access.

After all source/dependency artifacts are staged and hashed, package installation, local GGUF attestation, tool build, and runtime inspection must execute with outbound network disabled using the already-reviewed unprivileged network-namespace pattern where the runner supports it.

```text
NETWORK_PHASE_A=PUBLIC_TOOL_AND_DEPENDENCY_PROVISIONING_ONLY
NETWORK_PHASE_B=LOCAL_INSTALL_BUILD_AND_RUNTIME_ATTESTATION_ONLY
PHASE_B_NETWORK_POLICY=DEFAULT_DENY
MODEL_PROVIDER_NETWORK_ACCESS=PROHIBITED
HUGGING_FACE_MODEL_ENDPOINT_ACCESS=PROHIBITED
PACKAGE_INDEX_ACCESS_DURING_PHASE_B=PROHIBITED
GIT_FETCH_OR_PULL_DURING_PHASE_B=PROHIBITED
PROVIDER_API_USE=PROHIBITED
TELEMETRY_OR_EXTERNAL_UPLOAD=PROHIBITED
```

Credential policy remains none:

```text
WORKFLOW_PERMISSIONS={}
HF_TOKEN_USE=PROHIBITED
HUGGING_FACE_HUB_TOKEN_USE=PROHIBITED
GITHUB_TOKEN_USE_BY_WORKFLOW_STEPS=PROHIBITED
GH_TOKEN_USE=PROHIBITED
CLOUD_CREDENTIAL_USE=PROHIBITED
PACKAGE_REGISTRY_CREDENTIAL_USE=PROHIBITED
PRIVATE_OR_GATED_PACKAGE_ACCESS=PROHIBITED
OTHER_SECRET_ACCESS=PROHIBITED
```

GitHub platform bootstrap token presence, if created by the platform, does not create token-use authority and must not be exposed to the isolated install/build/runtime-attestation phase.

## 9. Mandatory evidence outputs

A successful runtime-evidence run must bind at least:

```text
run_id
run_head_sha
runner_label
runner_image_version
host_os_identity
host_architecture
kernel_identity
libc_identity
python_implementation
python_runtime_path
python_runtime_version
python_runtime_sha256
resolver_name
resolver_version
llama_cpp_repository
llama_cpp_commit
llama_cpp_tree
converter_entrypoint_sha256
canonical_dependency_manifest_git_blob_set
canonical_dependency_requirement_surface_sha256
package_index_or_wheelhouse_boundary
resolved_dependency_name_version_set
resolved_dependency_artifact_filename_set
resolved_dependency_artifact_integer_byte_set
resolved_dependency_artifact_sha256_set
dependency_set_manifest_sha256
ephemeral_environment_path
installed_environment_manifest_sha256
gguf_imported_file_path
gguf_imported_source_identity
no_local_gguf_unset_attestation
cmake_path_version_sha256
compiler_paths_versions_sha256
build_system_path_version_sha256
cmake_configuration_argv
build_argv
build_flags
rebuilt_llama_quantize_path
rebuilt_llama_quantize_sha256
rebuilt_llama_quantize_integer_bytes
prior_build_sha256_comparison_result
network_phase_boundary_evidence_sha256
credential_state_evidence_sha256
runtime_evidence_manifest_sha256
spend_usd_observed_or_provider_billing_visibility_disposition
```

The previous `llama-quantize` SHA-256 is a comparison target only:

```text
PRIOR_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
REBUILT_SHA_EQUALS_PRIOR_SHA=NEEDS_RUNTIME_EVIDENCE
```

A mismatch is not silently accepted and is not automatically a failure of source integrity. It must be recorded with the exact runner/toolchain delta and leaves later conversion authority blocked pending review.

## 10. Why this does not create conversion authority

The proposed run resolves runtime reconstruction evidence only. It still does not create or prove the future conversion-time model source path, output path, model-specific exact argv, storage boundary, retention enforcement, compute-capacity sufficiency, contamination authority, scientific gates, governance gates, A1-A14 activation snapshot, or A15 activation.

After a successful runtime-evidence run, a later exact conversion subject would still have to bind, without placeholders:

```text
EXACT_MODEL_SOURCE_REPOSITORY_AND_REVISION
EXACT_MODEL_SOURCE_FILE_HASH_SET
EXACT_RUNTIME_RECONSTRUCTION_INPUT_HASH_SET
EXACT_LOCAL_SOURCE_DIRECTORY_AT_EXECUTION
EXACT_LOCAL_OUTPUT_DIRECTORY_AT_EXECUTION
EXACT_CONVERT_ARGV
EXACT_QUANTIZE_ARGV
EXACT_STORAGE_BOUNDARY_IDENTITY
RETENTION_ENFORCEMENT_IDENTITY
EXACT_COMPUTE_RESOURCE_IDENTITY
RESOURCE_AUTHORIZATION_BASIS
EXPECTED_CPU_RAM_DISK_ENVELOPE
EXPECTED_MAX_WALLCLOCK
ZERO_INCREMENTAL_SPEND_DISPOSITION
CONVERSION_PHASE_NETWORK_DISABLEMENT
CONVERSION_PHASE_CREDENTIAL_ATTESTATION
```

Only after all required fields are exact may a separate Founder conversion-execution authority surface be presented.

```text
RUNTIME_EVIDENCE_PASS_EQUALS_CONVERSION_EXECUTION_AUTHORITY=NO
RUNTIME_EVIDENCE_PASS_EQUALS_E004_TOURNAMENT_START=NO
RUNTIME_EVIDENCE_PASS_EQUALS_A15_ACTIVATION=NO
RUNTIME_EVIDENCE_PASS_EQUALS_TRAINING_AUTHORITY=NO
```

## 11. Scientific and governance blockers remain independent

This proposed authority does not alter:

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_G2_G3_G4=REAL_GOVERNANCE_OPERATIONAL_EVIDENCE_INCOMPLETE
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

Repository automation or AI review cannot substitute for the required qualified clinical/statistical review or real governance/personnel/resource evidence.

## 12. ChatGPT recommendation

```text
CHATGPT_POSITION=RECOMMEND_AUTHORIZE_BOUNDED_RUNTIME_EVIDENCE_RUN
RATIONALE_1=IT_TARGETS_A_REAL_CONVERSION_SUBJECT_GAP_NOT_A_DECORATIVE_RERUN
RATIONALE_2=IT_DOES_NOT_REUSE_OR_RESET_THE_EXHAUSTED_BUILD_EVIDENCE_ALLOWANCE
RATIONALE_3=IT_CREATES_THE_EXACT_DEPENDENCY_AND_RUNTIME_HASH_SET_NEEDED_FOR_A_LATER_RECONSTRUCTION_BASED_CONVERSION_SUBJECT
RATIONALE_4=IT_PRESERVES_LOCAL_GGUF_SOURCE_SELECTION_AND_NO_REMOTE_MODEL_MODE
RATIONALE_5=IT_PRESERVES_MODEL_CONVERSION_INFERENCE_BENCHMARK_DEVICE_CONTAMINATION_TRAINING_AND_SPEND_AT_NONE
RATIONALE_6=IT_FAILS_CLOSED_IF_THE_CURRENT_RUNNER_CANNOT_REPRODUCE_THE_REQUIRED_RUNTIME_BOUNDARY
```

## 13. Exact Founder decision capture requirement

This document itself grants no new authority.

A Founder response may be recorded as `E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED` only when the exact authority class, provider, runner class, maximum run count, purpose, permitted actions, dependency source boundary, local-GGUF selection rule, prohibitions, credential boundary, network boundary, and USD 0 spend boundary are presented immediately before that response.

Historical or generic instructions such as `go ahead`, `continue`, or `you have all approvals` must not be retroactively expanded across this separately gated decision.

Until a valid exact response is captured:

```text
E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY=NONE
NEW_RUNTIME_EVIDENCE_WORKFLOW_PROMOTION_AUTHORITY=NONE
NEW_RUNTIME_EVIDENCE_WORKFLOW_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
```

## 14. Mandatory sequence if the decision is later authorized

```text
EXACT_FOUNDER_DECISION_CAPTURED
-> PREPARE_NON_EXECUTABLE_WORKFLOW_SUBJECT_FROM_THEN_CURRENT_CANONICAL_MAIN
-> BIND_WORKFLOW_PATH_AND_SHA256
-> FRESH_EXACT_HEAD_REVIEW
-> CANONICAL_MERGE_OF_DECISION_RECORD_AND_REVIEWED_WORKFLOW_ONLY_IF_AUTHORIZED
-> POST_MERGE_BYTE_IDENTITY_VERIFICATION
-> AT_MOST_ONE_WORKFLOW_DISPATCH_ONLY_IF_ALL_PRE_RUN_CONDITIONS_PASS
-> CAPTURE_REAL_RUNTIME_EVIDENCE_OR_FAIL_CLOSED
-> APPEND_ONLY_CURRENT_STATE_RECONCILIATION
-> PREPARE_LATER_EXACT_CONVERSION_EXECUTION_SUBJECT_ONLY_IF_RUNTIME_EVIDENCE_IS_SUFFICIENT
```

No arrow may be skipped. Merge of this decision-request document does not satisfy the first arrow.

## Exclusions

This request performs no GitHub Actions workflow promotion or dispatch, source-model/GGUF acquisition, model loading, conversion, quantization, inference, benchmark/device execution, contamination assessment, A15 activation, Private Gold/PHI/gated access, credential use, external reviewer outreach, provider generation, training, procurement, payment, or spend. It creates no runtime PASS and changes no task checkbox.

## Exit Evidence

Repository-level closure of this **decision-request artifact only** requires fresh exact-head review confirming:

```text
REQUEST_TARGETS_REAL_RUNTIME_EVIDENCE_GAP=YES
REQUEST_BINDS_CANONICAL_DEPENDENCY_MANIFEST_SURFACE=YES
REQUEST_PRESERVES_LOCAL_GGUF_SOURCE_SELECTION=YES
REQUEST_PROHIBITS_REMOTE_MODEL_MODE=YES
REQUEST_DOES_NOT_RESET_PRIOR_BUILD_ALLOWANCE=YES
REQUEST_GRANTS_CURRENT_RUNTIME_EXECUTION_AUTHORITY=NO
REQUEST_GRANTS_CURRENT_MODEL_CONVERSION_AUTHORITY=NO
REQUEST_PRESERVES_NO_OUTREACH_BOUNDARY=YES
REQUEST_PRESERVES_SCIENTIFIC_GOVERNANCE_A15_BLOCKERS=YES
REQUEST_PRESERVES_USD_ZERO_BOUNDARY=YES
REQUEST_PRESERVES_E004_BLOCKED_PREFLIGHT=YES
REQUEST_PRESERVES_E005_NOT_REACHED=YES
```

Canonical merge would close this request document only and present a truthful next exact Founder decision surface. It would not authorize or execute the proposed runtime-evidence run.