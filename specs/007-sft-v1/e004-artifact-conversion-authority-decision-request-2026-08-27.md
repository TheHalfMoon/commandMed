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

This document converts the remaining frozen-artifact blocker into an exact decision surface. It does not infer authorization from repository progress, public artifact availability, code-review status, or a generic instruction to continue.

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

## 1. Controlling frozen candidate identities and device-role semantics

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

The current corrected device control plane is explicit: both `PRIMARY` and `CONTROL` are executable roles for static pre-execution readiness and require all five target identity records. The package hard cap is PRIMARY-only.

```text
DEVICE_EXECUTABLE_CANDIDATE_ROLES=PRIMARY,CONTROL
CONTROL_DEVICE_PREEXECUTION_READINESS_REQUIRED=YES
CONTROL_ALL_FIVE_TARGET_IDENTITY_RECORDS_REQUIRED=YES
CONTROL_MODEL_ARTIFACT_SHA256_REQUIRED=YES
CONTROL_GGUF_QUANTIZATION_IDENTITY_REQUIRED=YES
CONTROL_LLAMA_CPP_CORE_REVISION_REQUIRED=YES
CONTROL_PRIMARY_PACKAGE_HARD_CAP_APPLIES=NO
```

No candidate/revision substitution and no silent CONTROL scope reduction are in scope.

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

Current public availability does not establish immutable frozen-source-to-output binding or exact integer-byte evidence.

## 4. Unresolved CONTROL path

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

The CONTROL is exempt from the PRIMARY package hard cap but not from current device pre-execution identity requirements.

```text
CONTROL_DEVICE_RUNTIME_OBLIGATION=BOUND_BY_CURRENT_DEVICE_CONTROL_PLANE
CONTROL_PREEXECUTION_DEVICE_IDENTITY_REQUIRED=YES
CONTROL_PRIMARY_PACKAGE_HARD_CAP_APPLIES=NO
CONTROL_ARTIFACT_SUBSTITUTION_BY_CONVENIENCE=PROHIBITED
```

If governance intentionally narrows that obligation, that is a protocol amendment under `ARTIFACT_DECISION_D`, not an artifact-resolution inference.

## 5. Decision classes

Silence, repository merge, or code-review PASS is not a Founder decision.

### `ARTIFACT_DECISION_A` — preserve current authority

```text
E002_PRECONVERTED_ALLOWLIST_COUNT=2
MODEL_CONVERSION_AUTHORITY=NONE
FULL_E004_ARTIFACT_FRONTIER=BLOCKED
```

### `ARTIFACT_DECISION_B` — authorize a bounded exact-source conversion path

This class would authorize conversion only after a separately reviewable exact conversion subject is bound. It would not itself authorize inference, benchmark execution, device measurement, training, credentials, PHI, Private Gold, provider generation, or spend.

Proposed bounded candidate scope:

```text
CONVERSION_SOURCE_SCOPE=EXACT_FROZEN_E001_SOURCE_REVISIONS_ONLY
PRIMARY_GRANITE_CONVERSION_ELIGIBLE_FOR_REQUEST=YES
CONTROL_QWEN3_4B_CONVERSION_ELIGIBLE_FOR_REQUEST=YES
CONTROL_CONVERSION_PURPOSE=SATISFY_CURRENT_FROZEN_CONTROL_RUNTIME_ARTIFACT_IDENTITY_REQUIREMENT
QWEN_0_6_OR_0_8_RECONVERSION_AUTO_AUTHORIZED=NO
OTHER_MODELS_OR_REVISIONS=PROHIBITED
```

Before any conversion execution, the exact subject must bind:

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

After conversion, before an output can become a tournament runtime artifact, evidence must bind:

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
CONTROL_CONVERSION_OUTPUT_EXEMPT_FROM_PRIMARY_PACKAGE_HARD_CAP=YES
CONTROL_CONVERSION_OUTPUT_EXEMPT_FROM_OTHER_FROZEN_DEVICE_READINESS_FIELDS=NO
```

### `ARTIFACT_DECISION_C` — wait for future fully bound preconverted artifacts

No current public Granite/CONTROL artifact may enter E002 under this option until a new evidence packet proves:

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

This is a scientific/governance change, not an artifact shortcut. It requires separate explicit authority and rationale. It is the only decision class here that may intentionally narrow the current CONTROL device/runtime obligation.

## 6. ChatGPT position for Founder review

```text
CHATGPT_ARTIFACT_POSITION=RECOMMEND_ARTIFACT_DECISION_B_FOR_BOTH_CURRENTLY_UNRESOLVED_FROZEN_RUNTIME_ARTIFACT_PATHS
CHATGPT_GRANITE_SCOPE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CHATGPT_CONTROL_SCOPE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CHATGPT_REASON_1=EXACT_SOURCE_CONTROLLED_CONVERSION_CAN_CREATE_AUDITABLE_SOURCE_TO_OUTPUT_PROVENANCE_WITHOUT_TRUSTING_AMBIGUOUS_PRECONVERTED_LINEAGE
CHATGPT_REASON_2=GRANITE_PRIMARY_AND_CONTROL_BOTH_REQUIRE_EXACT_RUNTIME_ARTIFACT_IDENTITIES_UNDER_THE_CURRENT_FROZEN_CONTROL_PLANE
CHATGPT_REASON_3=CONTROL_IS_EXEMPT_FROM_THE_PRIMARY_PACKAGE_HARD_CAP_BUT_NOT_FROM_DEVICE_PREEXECUTION_IDENTITY_REQUIREMENTS
CHATGPT_REASON_4=THE_PROPOSED_CONVERSION_AUTHORITY_CAN_BE_STRICTLY_SEPARATED_FROM_INFERENCE_DEVICE_BENCHMARK_TRAINING_AND_SPEND
```

This is recommendation-only. If the Founder does not want CONTROL conversion under the current frozen role, the safe path is an explicit `ARTIFACT_DECISION_D`, not silent omission.

## 7. Exact future authority record for Decision B

If B is later chosen, the authorization must bind an exact subject rather than generic conversion permission:

```text
AUTHORIZED_CANDIDATE_IDS
AUTHORIZED_SOURCE_REVISIONS
AUTHORIZED_SOURCE_WEIGHT_IDENTITIES_AND_SHA256
AUTHORIZED_CONVERSION_TOOL_REPOSITORY
AUTHORIZED_CONVERSION_TOOL_REVISION
AUTHORIZED_CONVERSION_RUNTIME_SHA256
AUTHORIZED_QUANTIZATION_FAMILY
AUTHORIZED_OUTPUT_CLASS
AUTHORIZED_PURPOSE=E004_FROZEN_TOURNAMENT_ARTIFACT_PREPARATION_ONLY
SPEND_AUTHORITY
CREDENTIAL_AUTHORITY
NETWORK_BOUNDARY
EXPIRY_OR_SUPERSESSION_RULE
```

Any unresolved field keeps conversion execution blocked.

## 8. Decision capture requirement

A future Founder response may be recorded as authority only after the exact decision class and exact bounded scope are presented immediately before that response. A generic continuation instruction must not be retroactively expanded across unrelated authority gates.

Until then:

```text
FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=DECISION_NOT_TAKEN
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
```

## Exclusions

This bounded decision request explicitly excludes:

- any current Founder authorization or inference of authorization;
- expansion of the existing two-entry E002 preconverted allowlist;
- downloading Granite, CONTROL, or any other newly unlisted model/GGUF bytes;
- conversion execution, model loading, inference, benchmark payload access/execution, device execution, or measured device evidence;
- contamination assessment, selection-suite construction, Private Gold, PHI, restricted/gated assets, credentials, provider generation, winner selection, training, payment, procurement, or spend;
- candidate/revision substitution or silent narrowing of CONTROL obligations;
- treating public artifact availability, public SHA metadata, code-review status, or this document's merge as evidence of source-to-output provenance.

## Exit Evidence

This **decision-request artifact** is eligible for repository-level closure only when one exact head demonstrates:

```text
REQUEST_BINDS_FROZEN_E001_CANDIDATE_IDENTITIES=YES
REQUEST_PRESERVES_EXISTING_E002_TWO_ENTRY_ALLOWLIST=YES
REQUEST_DISTINGUISHES_PUBLIC_ARTIFACT_EXISTENCE_FROM_E002_ELIGIBILITY=YES
REQUEST_PRESERVES_PRIMARY_AND_CONTROL_DEVICE_ROLE_SEMANTICS=YES
REQUEST_PRESERVES_PRIMARY_ONLY_PACKAGE_HARD_CAP=YES
REQUEST_PRESENTS_BOUNDED_DECISION_CLASSES_WITHOUT_GRANTING_AUTHORITY=YES
REQUEST_BINDS_DECISION_B_TO_EXACT_SOURCE_CONVERSION_EVIDENCE=YES
REQUEST_GRANTS_CURRENT_CONVERSION_AUTHORITY=NO
REQUEST_DOWNLOADS_OR_EXECUTES_MODEL_BYTES=NO
```

Repository closure additionally requires fresh exact-head review with no unresolved material findings, no active review threads, bounded documentation-only diff verification, guarded canonical merge, and post-merge main verification. Those checks close this **decision-request document only**. They do not constitute Founder selection of A/B/C/D, do not mutate E002, and do not authorize conversion or E004 execution.
