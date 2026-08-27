# E004 Frozen Artifact / Conversion Authority Decision Request — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `57e7a172ca888333255d4c12a441dbe9fd97c811`  
**Artifact class:** Founder decision request / authority proposal only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Model / GGUF payload access performed:** NO  
**Conversion performed:** NO  
**Model execution performed:** NO

This document converts the remaining frozen-artifact blocker into an exact decision surface. It does not infer authorization from repository progress, the existence of public GGUF files, or a generic instruction to continue.

```text
FOUNDER_ARTIFACT_DECISION=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
E002_PRECONVERTED_ALLOWLIST_COUNT=2
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling frozen candidate identities

The E001 candidate manifest remains unchanged.

```text
MANIFEST_VERSION=e001-mass-reach-v1
MANIFEST_CANONICAL_SHA256=98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28

PRIMARY_1=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
PRIMARY_2=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
PRIMARY_3=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
CONTROL_MASS_REACH_PACKAGE_GATE_REQUIRED_FOR_CONTROL_WINNING=NO
```

No candidate/revision substitution is in scope.

## 2. Existing E002 preconverted acquisition authority

E002 currently authorizes byte acquisition of exactly two preconverted artifacts and nothing else.

### Qwen3 0.6B PRIMARY

```text
REPOSITORY=Antigma/Qwen3-0.6B-Base-GGUF
REVISION=f457544766bcdc72afd3514439eb3d422d4434dc
FILENAME=qwen3-0.6b-base-q4_k_m.gguf
BYTES=396704512
SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
E001_LABEL=EXACT_BASE_DERIVATIVE_FEASIBILITY_ONLY_NOT_FINAL_RELEASE_BINDING
```

### Qwen3.5 0.8B PRIMARY

```text
REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
REVISION=1bd44f68963429437d08bc12f465716eb31ba6e5
FILENAME=Qwen3.5-0.8B-Base-Q4_0.gguf
BYTES=563035840
SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
E001_LABEL=DIRECT_DIGEST_PUBLIC_METADATA
```

```text
EXISTING_ALLOWLIST_ENTRY_AUTOMATICALLY_EQUALS_FINAL_TOURNAMENT_RUNTIME_BINDING=NO
PRECONVERTED_ARTIFACTS_NOT_EXPLICITLY_LISTED=UNAUTHORIZED
```

## 3. Unresolved Granite PRIMARY path

Frozen subject:

```text
CANDIDATE=ibm-granite/granite-4.0-350m-base
FROZEN_SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
```

Canonical public-artifact research recovered a first-party Q4_K_M identity, but not the complete E002 binding required to authorize its bytes:

```text
PUBLIC_GGUF_REPOSITORY=ibm-granite/granite-4.0-350m-base-GGUF
PUBLIC_GGUF_FILENAME=granite-4.0-350m-base-Q4_K_M.gguf
PUBLIC_GGUF_SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
PUBLIC_GGUF_XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
PUBLIC_DISPLAY_SIZE=237_MB
EXACT_INTEGER_BYTES=NEEDS_EVIDENCE
EXACT_FROZEN_SOURCE_REVISION_USED_TO_PRODUCE_BYTES=NEEDS_EVIDENCE
CURRENT_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
```

Fresh public verification on 2026-08-27 confirms that a public first-party Granite base GGUF repository and Q4_K_M artifact remain available. That observation does not establish the missing immutable source-to-output binding or exact integer-byte evidence required by E002.

## 4. Unresolved CONTROL path

Frozen subject:

```text
CANDIDATE=Qwen/Qwen3-4B-Base
FROZEN_SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

Canonical research recovered a public exact-base-labeled Q4_K_M artifact identity but not a complete frozen-source conversion attestation:

```text
PUBLIC_GGUF_REPOSITORY=Antigma/Qwen3-4B-Base-GGUF
PUBLIC_GGUF_FILENAME=qwen3-4b-base-q4_k_m.gguf
PUBLIC_GGUF_FILE_COMMIT=ab03cef12ef7fac77574d54a28331026c21257a0
PUBLIC_GGUF_SHA256=a91798f5f24b6ef5e9309fa97cb82be19c930f5b1e359e5d1af80d20e24b3f68
PUBLIC_REPORTED_SIZE_APPROX=2.5_GB
EXACT_INTEGER_BYTES=NEEDS_EVIDENCE
EXACT_FROZEN_SOURCE_REVISION_USED_TO_PRODUCE_BYTES=NEEDS_EVIDENCE
CURRENT_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
```

The CONTROL is not subject to the PRIMARY winning mass-reach package gate, but this fact does not itself define which device/runtime evidence the CONTROL must execute under E004. The artifact decision must not silently amend that obligation.

```text
CONTROL_DEVICE_RUNTIME_OBLIGATION=REQUIRES_EXACT_FROZEN_PROTOCOL_INTERPRETATION_OR_SEPARATE_GOVERNANCE_DECISION
CONTROL_ARTIFACT_SUBSTITUTION_BY_CONVENIENCE=PROHIBITED
```

## 5. Decision classes

The Founder should choose an explicit bounded class. Silence, repository merge, or code-review PASS is not a decision.

### `ARTIFACT_DECISION_A` — preserve current authority

```text
E002_PRECONVERTED_ALLOWLIST_COUNT=2
MODEL_CONVERSION_AUTHORITY=NONE
FULL_E004_ARTIFACT_FRONTIER=BLOCKED
```

Scientific advantage: no authority expansion.  
Consequence: full frozen tournament remains blocked on artifact prerequisites.

### `ARTIFACT_DECISION_B` — authorize a bounded exact-source conversion path

This option would authorize conversion only after a separately reviewable conversion manifest binds every required field below. It would not itself authorize model inference, benchmark execution, device measurement, training, credentials, PHI, Private Gold, provider generation, or spend.

The proposed minimal conversion scope is:

```text
CONVERSION_SOURCE_SCOPE=EXACT_FROZEN_E001_SOURCE_REVISIONS_ONLY
PRIMARY_GRANITE_CONVERSION_ELIGIBLE_FOR_REQUEST=YES
CONTROL_CONVERSION_ELIGIBLE_FOR_REQUEST=ONLY_IF_CONTROL_RUNTIME_OBLIGATION_REQUIRES_GGUF_AND_IS_GOVERNANCE_BOUND
QWEN_0_6_OR_0_8_RECONVERSION_AUTO_AUTHORIZED=NO
OTHER_MODELS_OR_REVISIONS=PROHIBITED
```

Before any conversion execution, an exact `ConversionManifest`-equivalent evidence packet must bind:

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
no_credentials_assertion
no_model_inference_assertion
no_benchmark_access_assertion
```

After conversion, but before the output can become a tournament runtime artifact, evidence must bind:

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
CONVERSION_OUTPUT_AUTOMATICALLY_BECOMES_WINNER_OR_TRAINING_ASSET=NO
```

### `ARTIFACT_DECISION_C` — wait for a future fully bound preconverted artifact

No current public artifact may enter E002 by this option until a new evidence packet proves, at minimum:

```text
exact_repository
immutable_artifact_revision
exact_filename
exact_integer_bytes
sha256
exact_frozen_source_revision_binding
conversion_or_publisher_attestation_identity
license_and_rights_identity
```

A later explicit allowlist mutation would still be required.

### `ARTIFACT_DECISION_D` — amend frozen protocol/candidate obligations

This is a scientific/governance change, not an artifact shortcut. It requires its own explicit authority and rationale and cannot be inferred from package inconvenience or resource limits.

## 6. ChatGPT decision position for Founder review

```text
CHATGPT_ARTIFACT_POSITION=RECOMMEND_ARTIFACT_DECISION_B_FOR_GRANITE_PRIMARY_ONLY_AS_THE_NEXT_RESOLUTION_PATH
CHATGPT_REASON_1=EXACT_SOURCE_CONTROLLED_CONVERSION_CAN_CREATE_AUDITABLE_SOURCE_TO_OUTPUT_PROVENANCE_WITHOUT_TRUSTING_AMBIGUOUS_PRECONVERTED_LINEAGE
CHATGPT_REASON_2=GRANITE_IS_PRIMARY_AND_CURRENT_PRECONVERTED_BINDING_REMAINS_INCOMPLETE
CHATGPT_REASON_3=THE_PROPOSED_AUTHORITY_CAN_BE_STRICTLY_SEPARATED_FROM_INFERENCE_DEVICE_BENCHMARK_TRAINING_AND_SPEND
CHATGPT_CONTROL_POSITION=DO_NOT_AUTHORIZE_CONTROL_CONVERSION_UNTIL_ITS_EXACT_E004_RUNTIME_DEVICE_OBLIGATION_IS_GOVERNANCE_BOUND
```

This is a recommendation, not Founder authorization.

## 7. If `ARTIFACT_DECISION_B` is later authorized

The authority record should state an exact subject, not a generic conversion permission. At minimum:

```text
AUTHORIZED_CANDIDATE_IDS
AUTHORIZED_SOURCE_REVISIONS
AUTHORIZED_CONVERSION_TOOL_REVISION
AUTHORIZED_QUANTIZATION_FAMILY
AUTHORIZED_OUTPUT_CLASS
AUTHORIZED_PURPOSE=E004_FROZEN_TOURNAMENT_ARTIFACT_PREPARATION_ONLY
SPEND_AUTHORITY
CREDENTIAL_AUTHORITY
NETWORK_BOUNDARY
EXPIRY_OR_SUPERSESSION_RULE
```

Any unresolved field keeps conversion execution blocked.

## 8. Explicit non-decisions

This request does not authorize or decide:

```text
MODEL_WEIGHT_DOWNLOAD_BEYOND_EXISTING_E002=NO
NEW_PRECONVERTED_ARTIFACT_BYTE_ACCESS=NO
MODEL_CONVERSION=NO
MODEL_LOADING_OR_INFERENCE=NO
BENCHMARK_PAYLOAD_ACCESS_OR_EXECUTION=NO
DEVICE_EXECUTION=NO
CONTAMINATION_ASSESSMENT=NO
PRIVATE_GOLD_OR_PHI=NO
PROVIDER_GENERATION=NO
BACKBONE_WINNER=NO
TRAINING=NO
SPEND=NO
```

## 9. Decision capture requirement

A future Founder response may be recorded as authority only after the exact decision class and exact bounded scope are presented immediately before that response. A generic continuation instruction must not be retroactively expanded across unrelated authority gates.

Until then:

```text
FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=DECISION_NOT_TAKEN
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
```
