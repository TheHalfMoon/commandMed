# E004 Founder Artifact Decision B — 2026-08-28

**Spec:** 007 SFT V1  
**Branch base:** `87b8da870b75486db33adef715af6ffdb1c4f193`  
**Decision owner:** Founder  
**Decision class:** `ARTIFACT_DECISION_B`  
**Decision state:** RECORDED_FOR_REVIEW  
**Authority effect:** AUTHORIZE EXACT CONVERSION-SUBJECT PREPARATION ONLY  
**Conversion execution authority:** NONE  
**Model execution authority:** NONE  
**Benchmark execution authority:** NONE  
**Device execution authority expansion:** NONE  
**Training authority:** NONE  
**Spend authority:** USD 0

## 1. Decision capture

The immediately preceding decision surface presented this exact bounded proposal to the Founder:

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B

AUTHORIZED_CANDIDATE_SCOPE=
  ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
  Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539

PURPOSE=E004_FROZEN_TOURNAMENT_ARTIFACT_PREPARATION_ONLY

AUTHORITY_BOUNDARY=
  AUTHORIZE_PREPARATION_OF_EXACT_CONVERSION_SUBJECTS_ONLY_BEFORE_EXECUTION

MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_EXECUTION_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
SPEND_AUTHORITY_USD=0
```

The Founder then responded directly:

```text
FOUNDER_RESPONSE=go ahead
```

Because that response immediately followed the exact decision class, candidate scope, purpose, and exclusions, this record captures selection of `ARTIFACT_DECISION_B` for the bounded preparation scope above. It does not retroactively expand any earlier generic continuation instruction.

## 2. Exact candidate identities

```text
GRANITE_SUBJECT_SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
GRANITE_SUBJECT_SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
GRANITE_ROLE=PRIMARY

QWEN_CONTROL_SUBJECT_SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
QWEN_CONTROL_SUBJECT_SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
QWEN_CONTROL_ROLE=CONTROL
QWEN_CONTROL_WINNER_ELIGIBLE=NO
QWEN_CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

No other model, revision, candidate, role, or reconversion is authorized by this decision.

## 3. What this decision permits now

The repository may prepare reviewable conversion subjects for the two exact candidates above. Preparation may record already-public, immutable metadata and identify exact unresolved execution prerequisites.

Permitted repository-only work includes:

- bind exact frozen source repository and revision identities;
- bind public source-file SHA-256 metadata where independently observable;
- identify one exact proposed converter source revision and exact conversion/quantization entrypoints for review;
- define exact intended quantization family and output naming policy as a proposal;
- define required environment, network, credential, storage, retention, logging, and zero-spend boundaries;
- enumerate all fields that still require execution-derived evidence before conversion can be authorized;
- obtain exact-head review and repair documentation findings.

## 4. What this decision does not permit

```text
MODEL_OR_GGUF_DOWNLOAD_AUTHORITY_EXPANSION=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONVERTER_BUILD_EXECUTION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
DEVICE_MEASUREMENT_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY_USD=0
```

A prepared subject is not executable authority. Any conversion requires a later exact execution authorization bound to a fully populated subject with no required `NEEDS_EVIDENCE` fields.

## 5. Required exact-subject fields before any future conversion execution

For each candidate, the future execution-authoritative subject must bind at least:

```text
source_repository
source_revision
source_weight_file_identities_and_sha256
source_license_identity
conversion_tool_repository
conversion_tool_revision
conversion_runtime_executable_sha256
conversion_entrypoint
conversion_argv
quantization_method_and_parameters
output_format
output_filename
build_environment_manifest_sha256
normalization_or_metadata_policy_if_any
expected_zero_spend_resource_envelope
storage_and_retention_policy
network_access_boundary
credential_state
no_model_inference_assertion
no_benchmark_access_assertion
```

Any unresolved required field keeps conversion execution blocked.

## 6. Post-conversion evidence remains future-only

If conversion is later separately authorized and executed, no output may become a tournament runtime artifact until evidence binds:

```text
output_sha256
output_exact_integer_bytes
source_to_output_provenance_record
conversion_log_identity
conversion_environment_identity
license_and_rights_recheck
independent_integrity_review
runtime_compatibility_static_check
```

```text
CONVERSION_OUTPUT_AUTOMATICALLY_EQUALS_E004_RUNTIME_BINDING=NO
CONVERSION_OUTPUT_AUTOMATICALLY_PASSES_DEVICE_GATE=NO
CONVERSION_OUTPUT_AUTOMATICALLY_BECOMES_WINNER=NO
CONVERSION_OUTPUT_AUTOMATICALLY_BECOMES_TRAINING_ASSET=NO
```

## 7. Current lifecycle effect

```text
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
ARTIFACT_DECISION_B_SCOPE=GRANITE_PRIMARY_PLUS_QWEN3_4B_CONTROL
EXACT_CONVERSION_SUBJECT_PREPARATION_AUTHORIZED=YES
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This record does not:

- amend E001 candidate identities or roles;
- expand the E002 preconverted allowlist;
- authorize model/GGUF/source-weight byte acquisition beyond existing authority;
- authorize converter build or conversion execution;
- authorize inference, benchmark payload access/execution, device runs, contamination assessment, selection-suite construction, winner selection, training, credentials, PHI, Private Gold, provider generation, procurement, personnel engagement, or spend;
- convert public artifact metadata into source-to-output provenance;
- declare E004 or any downstream task complete.

## Exit Evidence

This decision-record artifact is repository-level complete only after fresh exact-head review confirms:

```text
FOUNDER_RESPONSE_BOUND_TO_IMMEDIATELY_PRECEDING_EXACT_DECISION_SURFACE=YES
DECISION_CLASS=ARTIFACT_DECISION_B
CANDIDATE_SCOPE_EXACTLY_TWO_FROZEN_IDENTITIES=YES
PREPARATION_AUTHORITY_ONLY=YES
CONVERSION_EXECUTION_AUTHORITY=NONE
NO_OTHER_AUTHORITY_EXPANSION=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Canonical merge of this record would capture the bounded Founder decision only. It would not itself authorize conversion execution.