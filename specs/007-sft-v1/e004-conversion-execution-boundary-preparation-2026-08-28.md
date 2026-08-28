# E004 Decision B Conversion Execution Boundary Preparation — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46`  
**Founder decision:** `ARTIFACT_DECISION_B` preparation-only  
**Artifact class:** non-executing exact-boundary preparation  
**Authority effect:** NONE beyond already-canonical Decision B preparation scope  
**Source/model byte acquisition performed:** NO  
**Package installation performed:** NO  
**Conversion/quantization performed:** NO  
**Model execution performed:** NO  
**Spend:** USD 0

This record prepares the conversion-specific network, credential, storage, retention, logging, and zero-incremental-spend boundaries required by the already-canonical Decision B preparation authority. It does not provision resources, grant byte access, create credentials, install packages, build tools, or authorize conversion execution.

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
PURPOSE=E004_FROZEN_TOURNAMENT_ARTIFACT_PREPARATION_ONLY
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling boundaries

Decision B explicitly permits preparation of required environment, network, credential, storage, retention, logging, and zero-spend boundaries while preserving execution authority at NONE.

This conversion-specific contract does not supersede A13/A14 or general E004 runtime governance. It narrows the later conversion subject only.

```text
A13_STORAGE_ACCESS_GOVERNANCE_REMAINS_CONTROLLING=YES
A14_SPEND_ENGAGEMENT_GOVERNANCE_REMAINS_CONTROLLING=YES
GENERAL_E004_RUNTIME_RESOURCE_INTAKE_REMAINS_CONTROLLING=YES
THIS_RECORD_CREATES_A13_OPERATIONAL_PASS=NO
THIS_RECORD_CREATES_A14_OPERATIONAL_PASS=NO
```

## 2. Network phase separation

Future conversion execution, if separately authorized, must be strictly local/offline with respect to model-provider and package/network access.

```text
NETWORK_PHASE_A=PREEXECUTION_INPUT_AND_ENVIRONMENT_PROVISIONING
NETWORK_PHASE_B=CONVERSION_AND_QUANTIZATION_EXECUTION
```

### Phase A — provisioning only

Any future network access for source bytes, dependency artifacts, or tool source is governed by separate then-current acquisition/provisioning authority. This record grants none.

```text
PHASE_A_AUTHORITY_FROM_THIS_RECORD=NONE
SOURCE_WEIGHT_DOWNLOAD_AUTHORITY_EXPANSION=NONE
DEPENDENCY_DOWNLOAD_AUTHORITY_FROM_THIS_RECORD=NONE
TOOL_SOURCE_DOWNLOAD_AUTHORITY_FROM_THIS_RECORD=NONE
```

If any later authority permits exact public byte acquisition, all fetched artifacts must be identity-bound before Phase B begins.

### Phase B — execution

```text
PHASE_B_NETWORK_POLICY=DEFAULT_DENY
MODEL_PROVIDER_NETWORK_ACCESS=PROHIBITED
HUGGING_FACE_API_OR_RAW_MODEL_FETCH_DURING_CONVERSION=PROHIBITED
PACKAGE_INDEX_ACCESS_DURING_CONVERSION=PROHIBITED
GIT_FETCH_OR_PULL_DURING_CONVERSION=PROHIBITED
REMOTE_HF_CONVERSION_MODE=PROHIBITED
PROVIDER_API_USE=PROHIBITED
TELEMETRY_OR_UNDECLARED_EXTERNAL_UPLOAD=PROHIBITED
```

The selected converter must operate only on the exact local source directory and exact local pinned converter/runtime environment after all required identities are already present.

```text
NETWORK_BOUNDARY=DESIGN_PREPARED_RUNTIME_ENFORCEMENT_NEEDS_EVIDENCE
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
NETWORK_BOUNDARY_PASS=NO
```

## 3. Credential state

The selected frozen Granite and Qwen source repositories are public/ungated identities in the Decision B preparation scope. Conversion does not require credentials.

```text
CONVERSION_CREDENTIAL_POLICY=NONE
HF_TOKEN=PROHIBITED_IN_CONVERSION_ENVIRONMENT
HUGGING_FACE_HUB_TOKEN=PROHIBITED_IN_CONVERSION_ENVIRONMENT
GITHUB_TOKEN=PROHIBITED_IN_CONVERSION_ENVIRONMENT
CLOUD_PROVIDER_CREDENTIALS=PROHIBITED_IN_CONVERSION_ENVIRONMENT
MODEL_PROVIDER_API_KEYS=PROHIBITED_IN_CONVERSION_ENVIRONMENT
PRIVATE_GOLD_CREDENTIALS=PROHIBITED
PHI_OR_CLINICAL_SYSTEM_CREDENTIALS=PROHIBITED
```

A future environment attestation must prove no credential-bearing variables/files/agents are exposed to the conversion process. Exact enforcement evidence remains future-only.

```text
CREDENTIAL_STATE=DESIGN_PREPARED_RUNTIME_ATTESTATION_NEEDS_EVIDENCE
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_IDENTITY=NEEDS_EVIDENCE
CREDENTIAL_STATE_PASS=NO
```

## 4. Storage zones for conversion only

A future execution subject must bind one exact local storage boundary. Directory names alone are not accepted as a security boundary.

```text
CONVERSION_ZONE_INPUT=READ_ONLY_FROZEN_SOURCE_AND_PINNED_TOOL_RUNTIME
CONVERSION_ZONE_WORK=EPHEMERAL_INTERMEDIATE_OUTPUT_AND_LOG_WORKSPACE
CONVERSION_ZONE_CANDIDATE_OUTPUT=POST_CONVERSION_UNACCEPTED_ARTIFACT_STAGING
```

These conversion zones are not A13 selection-payload/result zones and must not be confused with them.

```text
CONVERSION_STORAGE_EQUALS_A13_OPERATIONAL_STORAGE=NO
PRIVATE_GOLD_PRESENT_IN_CONVERSION_STORAGE=PROHIBITED
SELECTION_SUITE_CONTENT_PRESENT_IN_CONVERSION_STORAGE=PROHIBITED
BENCHMARK_PAYLOAD_PRESENT_IN_CONVERSION_STORAGE=PROHIBITED
```

Future exact evidence must bind:

```text
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
FILESYSTEM_OR_VOLUME_IDENTITY=NEEDS_EVIDENCE
ACCESS_CONTROL_OR_PROCESS_ISOLATION_IDENTITY=NEEDS_EVIDENCE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
```

## 5. Source input immutability

Before conversion execution can be authorized:

```text
SOURCE_INPUT_DIRECTORY_MODE=READ_ONLY_TO_CONVERSION_PROCESS_WHERE_PLATFORM_SUPPORTS_ENFORCEMENT
SOURCE_FILE_MUTATION_BY_COMMANDMED=PROHIBITED
SOURCE_METADATA_REWRITE=PROHIBITED
TOKENIZER_NORMALIZATION_BY_COMMANDMED=PROHIBITED
SOURCE_DIRECTORY_BASENAME_MUTATION=PROHIBITED_AFTER_FREEZE
```

The pinned converter may perform only its own converter-defined in-memory parsing/transformation behavior. The repository may not pre-edit source bytes to make conversion succeed.

Runtime enforcement evidence for read-only source treatment remains required.

```text
SOURCE_INPUT_IMMUTABILITY_ENFORCEMENT=NEEDS_EVIDENCE
```

## 6. Intermediate and candidate-output handling

The unquantized GGUF intermediate and Q4_K_M candidate output are execution-derived bytes and do not become canonical tournament artifacts automatically.

```text
INTERMEDIATE_GGUF_STATUS=EPHEMERAL_EXECUTION_DERIVATIVE
Q4_K_M_OUTPUT_STATUS=UNACCEPTED_CANDIDATE_DERIVATIVE_UNTIL_POST_CONVERSION_GATES_PASS
AUTO_PUBLISH_TO_HUGGING_FACE=PROHIBITED
AUTO_GITHUB_ARTIFACT_UPLOAD=PROHIBITED
AUTO_RELEASE_ATTACHMENT=PROHIBITED
AUTO_PACKAGE_REGISTRY_UPLOAD=PROHIBITED
AUTO_MODEL_REGISTRY_UPLOAD=PROHIBITED
```

A future post-conversion acceptance path must independently bind output SHA-256, exact integer bytes, provenance, log/environment identity, rights/license recheck, independent integrity review, and static runtime compatibility.

## 7. Retention policy

The intended fail-closed retention semantics are:

```text
SOURCE_INPUT_RETENTION=NO_NEW_POLICY_AUTHORITY_FROM_THIS_RECORD
INTERMEDIATE_UNQUANTIZED_GGUF_RETENTION=DELETE_AFTER_OUTPUT_INTEGRITY_AND_PROVENANCE_CAPTURE_UNLESS_SEPARATELY_REQUIRED_FOR_REVIEW
FAILED_OR_PARTIAL_OUTPUT_RETENTION=DELETE_AFTER_FAILURE_EVIDENCE_CAPTURE_UNLESS_SEPARATELY_REQUIRED_FOR_INCIDENT_REVIEW
UNACCEPTED_Q4_K_M_OUTPUT_RETENTION=STAGED_ONLY_UNTIL_ACCEPT_OR_REJECT_DISPOSITION
ACCEPTED_OUTPUT_RETENTION=REQUIRES_SEPARATE_RUNTIME_ARTIFACT_BINDING_AND_STORAGE_AUTHORITY
```

This record does not choose an exact retention duration because no operational storage identity or conversion execution authority exists yet.

```text
EXACT_RETENTION_DURATION=NEEDS_EVIDENCE_OR_SEPARATE_POLICY_BINDING
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
STORAGE_AND_RETENTION_POLICY=DESIGN_PREPARED_OPERATIONAL_BINDING_INCOMPLETE
```

## 8. Logging/evidence policy

Future conversion logs are evidence, not authority. The intended evidence set is:

```text
CONVERSION_STDOUT_STDERR_CAPTURE=REQUIRED
CONVERSION_LOG_SHA256=REQUIRED_AFTER_EXECUTION
EXACT_ARGV_CAPTURE=REQUIRED
START_END_TIMESTAMP_CAPTURE=REQUIRED
EXIT_STATUS_CAPTURE=REQUIRED
PYTHON_RUNTIME_IDENTITY_CAPTURE=REQUIRED
DEPENDENCY_ENVIRONMENT_IDENTITY_CAPTURE=REQUIRED
PINNED_CONVERTER_SOURCE_IDENTITY_CAPTURE=REQUIRED
SOURCE_INPUT_IDENTITY_SET_CAPTURE=REQUIRED
OUTPUT_SHA256_AND_INTEGER_BYTES_CAPTURE=REQUIRED
```

Logs must not intentionally include raw tensor values, model payload bytes, credentials, Private Gold, PHI, or benchmark payloads.

```text
RAW_MODEL_TENSOR_VALUES_IN_LOGS=PROHIBITED
CREDENTIALS_IN_LOGS=PROHIBITED
PRIVATE_GOLD_IN_LOGS=PROHIBITED
PHI_IN_LOGS=PROHIBITED
BENCHMARK_PAYLOAD_IN_LOGS=PROHIBITED
```

Exact logging implementation and log-storage identity remain future evidence.

## 9. Zero-incremental-spend resource envelope

The Decision B preparation scope is bounded to current authorized spend of USD 0. A later conversion execution authorization must therefore prove a zero-incremental-spend resource path or obtain separate spend authority before execution.

```text
EXPECTED_INCREMENTAL_SPEND_USD=0
PAID_CLOUD_COMPUTE=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
PAID_STORAGE=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
PAID_BANDWIDTH_OR_EGRESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
PAID_EXTERNAL_SERVICE=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
PROCUREMENT=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
NEW_PAID_PERSONNEL_ENGAGEMENT=PROHIBITED_WITHOUT_SEPARATE_AUTHORITY
```

Availability of an owned machine, free tier, trial, donated service, volunteer labor, or zero-dollar quote does not by itself prove A14 or execution authority.

```text
OWNED_RESOURCE_EQUALS_AUTHORITY=NO
FREE_TIER_EQUALS_AUTHORITY=NO
TRIAL_EQUALS_AUTHORITY=NO
DONATED_RESOURCE_EQUALS_AUTHORITY=NO
UNPAID_EXTERNAL_LABOR_EQUALS_AUTHORITY=NO
```

Future exact evidence must bind the actual resource identity, ownership/control or authorization basis, expected runtime envelope, and a zero-incremental-cost disposition before execution.

```text
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
EXPECTED_ZERO_SPEND_RESOURCE_ENVELOPE=DESIGN_PREPARED_OPERATIONAL_BINDING_INCOMPLETE
```

## 10. Isolation from model execution and evaluation

Conversion and quantization authority, if later granted, remains distinct from inference or evaluation authority.

```text
MODEL_INFERENCE_DURING_CONVERSION=PROHIBITED
TOKEN_GENERATION_DURING_CONVERSION=PROHIBITED
BENCHMARK_ACCESS_DURING_CONVERSION=PROHIBITED
BENCHMARK_EXECUTION_DURING_CONVERSION=PROHIBITED
DEVICE_QUALIFICATION_DURING_CONVERSION=PROHIBITED
CONTAMINATION_ASSESSMENT_DURING_CONVERSION=PROHIBITED
TRAINING_OR_ADAPTATION_DURING_CONVERSION=PROHIBITED
```

Static parser/import/runtime-attestation checks that do not load model weights require their own exact then-current authority if they execute code; this preparation record grants none.

## 11. Pre-execution fail-closed checklist

A future exact conversion authorization must not be created while any required field remains unresolved, including:

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY
EXACT_LOCAL_SOURCE_DIRECTORY
EXACT_LOCAL_SOURCE_DIRECTORY_BASENAME
NORMALIZATION_OR_METADATA_POLICY
PYTHON_RUNTIME_IDENTITY
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256
CONVERSION_RUNTIME_EXECUTABLE_SHA256
BUILD_ENVIRONMENT_MANIFEST_SHA256
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS
NETWORK_BOUNDARY_RUNTIME_ENFORCEMENT
CREDENTIAL_STATE_RUNTIME_ATTESTATION
EXACT_STORAGE_BOUNDARY_IDENTITY
RETENTION_ENFORCEMENT_IDENTITY
EXACT_COMPUTE_RESOURCE_IDENTITY
ZERO_INCREMENTAL_SPEND_DISPOSITION
```

```text
ANY_REQUIRED_FIELD_NEEDS_EVIDENCE=CONVERSION_EXECUTION_BLOCKED
```

## 12. Current state

```text
CONVERSION_NETWORK_POLICY=DESIGN_PREPARED
CONVERSION_CREDENTIAL_POLICY=DESIGN_PREPARED
CONVERSION_STORAGE_ZONE_POLICY=DESIGN_PREPARED
CONVERSION_RETENTION_POLICY=DESIGN_PREPARED_WITH_EXACT_DURATION_UNRESOLVED
CONVERSION_LOGGING_POLICY=DESIGN_PREPARED
EXPECTED_ZERO_SPEND_RESOURCE_ENVELOPE=DESIGN_PREPARED_OPERATIONAL_BINDING_INCOMPLETE
NETWORK_BOUNDARY=NEEDS_OPERATIONAL_EVIDENCE
CREDENTIAL_STATE=NEEDS_OPERATIONAL_EVIDENCE
STORAGE_AND_RETENTION_POLICY=NEEDS_OPERATIONAL_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## Exclusions

This artifact performs no network provisioning, source/model byte acquisition, package installation, converter build, Python import execution, model loading, conversion, quantization, inference, benchmark/device execution, contamination assessment, storage provisioning, ACL mutation, credential access, personnel engagement, procurement, payment, upload, publication, training, or spend. It creates no workflow and consumes no authorized workflow run.
