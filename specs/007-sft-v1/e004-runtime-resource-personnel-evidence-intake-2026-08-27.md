# E004 Runtime / Resource / Personnel Evidence Intake — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base:** `27faa40707f66302be56311357fd61792ea66835`  
**Artifact class:** non-executing evidence-intake checklist only  
**Authority effect:** NONE  
**Validator input:** NO  
**Runtime/device execution performed:** NO  
**Personnel assigned or engaged:** NO  
**Storage/access provisioned:** NO  
**Spend committed or paid:** NO

This document converts the remaining E004 runtime/resource/personnel/access/finance evidence surface into exact intake questions using the already-frozen Spec 005 control plane. It creates no new schema or framework and does not mutate closed Spec 005 code, contracts, device targets, personnel governance, access rules, spend architecture, or the canonical request surfaces merged through PR #81.

```text
RUNTIME_RESOURCE_PERSONNEL_INTAKE_TEMPLATE=PREPARED
REAL_RUNTIME_BINDINGS_CREATED=0
REAL_DEVICE_TARGET_BINDINGS_CREATED=0
REAL_PERSONNEL_ASSIGNMENTS_CREATED=0
REAL_A13_ACCESS_GRANTS_CREATED=0
REAL_A14_AUTHORIZATIONS_CREATED=0
REAL_MEASURED_DEVICE_RUNS_CREATED=0
DEVICE_EXECUTION_AUTHORITY_EXISTS_UNDER_E003=YES_BOUNDED
DEVICE_EXECUTION_CURRENTLY_STARTABLE=NO_E004_PREEXECUTION_INCOMPLETE
FOUNDER_ARTIFACT_DECISION=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A7_OPERATIONAL_PASS=NO
A13_OPERATIONAL_PASS=NO
A14_OPERATIONAL_PASS=NO
CURRENT_AUTHORIZED_SPEND_USD=0
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
TRAINING_AUTHORITY=NONE
```

## 1. Controlling sources

```text
DEVICE_RUNTIME_CONTROL=src/commandmed/spec005/device.py
DEVICE_CONTRACT=data/spec005/device_qualification_contract.json
A7_PERSONNEL_ROOT=specs/005-base-model-tournament/session-13-q1-personnel-qualification-gold-nonexposure-role-transition-registry.md
A7_OPERATIONAL_PASS_ROOT=specs/005-base-model-tournament/session-13-q5-a7-bootstrap-root-of-trust-operational-pass-manifest.md
A13_STORAGE_ACCESS_ROOT=specs/005-base-model-tournament/session-12-q5-payload-storage-access-candidate-feedback-firewall.md
A14_SPEND_ROOT=specs/005-base-model-tournament/session-14-q1-a14-spend-engagement-authorization-architecture.md
ARTIFACT_DECISION_REQUEST=specs/007-sft-v1/e004-artifact-conversion-authority-decision-request-2026-08-27.md
A11_AUTHORITY_REQUEST_TEMPLATE=specs/007-sft-v1/e004-a11-contamination-assessment-authority-request-template-2026-08-27.md
CURRENT_FRONTIER=specs/007-sft-v1/e004-current-frontier-reconciliation-2026-08-27.md
```

If any controlling source changes materially before evidence adoption, affected bindings must be re-read and requalified; mutable `latest` references are not evidence.

## 2. Frozen device target set

All five target identities remain required for pre-execution readiness for both `PRIMARY` and `CONTROL` candidate roles.

| Target ID | Frozen representative identity | Current real target binding |
|---|---|---|
| `FLAGSHIP_REPRESENTATIVE` | `Apple_iPhone_17_Pro_12GB` | `NEEDS_EVIDENCE` |
| `APPLE_LOW_RESOURCE_REPRESENTATIVE` | `Apple_iPhone_13_4GB` | `NEEDS_EVIDENCE` |
| `MODERN_MIDRANGE_ANDROID_REPRESENTATIVE` | `Samsung_Galaxy_A56_5G_8GB` | `NEEDS_EVIDENCE` |
| `LOW_RESOURCE_ANDROID_REPRESENTATIVE` | `Samsung_Galaxy_A16_5G_4GB` | `NEEDS_EVIDENCE` |
| `LOW_RESOURCE_LAPTOP_ENVELOPE` | `Intel_N100_8GB_x86_64` | `NEEDS_EVIDENCE` |

```text
ALL_FIVE_TARGETS_REQUIRED=YES
PHYSICAL_DEVICE_SUBSTITUTION_AFTER_RESULTS=PROHIBITED
PRE_RESULT_SUBSTITUTION_REQUIRES_SEPARATE_REVIEWED_EQUAL_OR_STRICTER_CLARIFICATION=YES
```

This checklist does not procure, reserve, borrow, enroll, substitute, or authorize any physical device.

## 3. Candidate-level runtime/artifact binding intake

For every executable candidate role under the frozen device control plane, future evidence must bind the exact candidate/runtime artifact identity before device execution.

Required shared evidence slots:

```text
candidate_id=NEEDS_EVIDENCE
candidate_role=NEEDS_EVIDENCE
frozen_e001_source_revision=NEEDS_EVIDENCE
model_artifact_sha256=NEEDS_EVIDENCE
complete_bundle_sha256=NEEDS_EVIDENCE
complete_bundle_bytes=NEEDS_EVIDENCE
gguf_quantization=NEEDS_EVIDENCE
llama_cpp_core_revision=NEEDS_EVIDENCE
```

The current candidate universe remains exactly the frozen E001 PRIMARY set plus CONTROL; no candidate substitution is permitted by this intake document.

```text
PRIMARY_PACKAGE_HARD_CAP_BYTES=734003200
PRIMARY_PACKAGE_TARGET_BYTES=629145600
PRIMARY_PACKAGE_STRETCH_BYTES=524288000
PRIMARY_PACKAGE_HARD_CAP_NONCOMPENSABLE=YES
CONTROL_PRIMARY_PACKAGE_HARD_CAP_APPLIES=NO
CONTROL_OTHER_DEVICE_PREEXECUTION_IDENTITY_REQUIREMENTS_APPLY=YES
```

Existing public/E002 metadata does not automatically populate final E004 runtime bindings. Exact accepted artifact identity and provenance must be established separately under the applicable authority path. The PR #81 artifact decision request is a decision surface only and creates no artifact binding by itself.

## 4. Per-target pre-execution identity intake

For each candidate × each of the five targets, future pre-execution evidence must bind:

```text
build_toolchain_identity=NEEDS_EVIDENCE
runtime_artifact_sha256=NEEDS_EVIDENCE
wrapper_identity=NEEDS_EVIDENCE
memory_measurement_identity=NEEDS_EVIDENCE
thermal_signal_identity=NEEDS_EVIDENCE
energy_signal_identity=NEEDS_EVIDENCE
execution_plan_sha256=NEEDS_EVIDENCE
```

The target identity record must also bind the shared candidate fields in Section 3. A record with a stale/different model artifact, GGUF identity, or llama.cpp core revision is not equivalent evidence.

```text
SHARED_GGUF_MODEL_IDENTITY_ACROSS_TARGETS_REQUIRED=YES
SHARED_LLAMA_CPP_CORE_REVISION_REQUIRED=YES
PLATFORM_WRAPPERS_MAY_DIFFER_ONLY_AS_EXACT_BOUND_IDENTITIES=YES
MUTABLE_TAG_LATEST_BRANCH_OR_FAMILY_NAME_SUFFICIENT=NO
RUNTIME_DRIFT_REQUIRES_NEW_EXACT_IDENTITY=YES
```

## 5. Frozen protocol and unresolved pre-execution bindings

The common protocol already binds:

```text
CORE_CONTEXT_TOKENS=8192
STRESS_CONTEXT_TOKENS=16384
PROMPT_BUDGET_CORE=7168
GENERATION_BUDGET=1024
PROMPT_BUDGET_STRESS=15360
KV_K_TYPE=Q8_0
KV_V_TYPE=Q8_0
BATCH=512
UBATCH=128
CACHE_REUSE=false
MEASURED_RUNS=5
AGGREGATION=MEDIAN_WITH_WORST_CASE
NON_MEASURED_WARMUP_REQUESTS=0
FRESH_PROCESS_PER_MEASURED_RUN_REQUIRED=YES
```

The following real pre-execution evidence remains unresolved:

```text
PERFORMANCE_THRESHOLD_POLICY_STATE=UNRESOLVED_PRE_EXECUTION
PERFORMANCE_THRESHOLD_POLICY_RECORD_ID=NEEDS_EVIDENCE
PERFORMANCE_THRESHOLD_POLICY_SHA256=NEEDS_EVIDENCE
WINDOWS_PRIMARY_MEMORY_MEASUREMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_BUILD_TOOLCHAINS=NEEDS_EVIDENCE
EXACT_RUNTIME_EXECUTABLES=NEEDS_EVIDENCE
EXACT_WRAPPER_IDENTITIES=NEEDS_EVIDENCE
EXACT_THERMAL_SIGNAL_METHODS=NEEDS_EVIDENCE
EXACT_ENERGY_SIGNAL_METHODS=NEEDS_EVIDENCE
EXACT_EXECUTION_PLAN_IDENTITIES=NEEDS_EVIDENCE
```

The Windows memory method and performance-threshold policy must be separately bound before execution; this checklist selects neither.

## 6. Hard-gate facts this intake may not weaken

```text
CORE_8K_PEAK_MEMORY_HARD_CEILING_BYTES=2147483648
MEMORY_HARD_GATE_APPLIES_TO_ALL_FIVE_TARGETS=YES
ABSOLUTE_PLATFORM_NATIVE_PEAK_IS_HARD_GATE_INPUT=YES
PEAK_DELTA_FROM_BASELINE_IS_DIAGNOSTIC_ONLY=YES
HELPER_AND_CHILD_PROCESSES_INCLUDED=YES
MEMORY_CEILING_EXCEEDED=HARD_FAIL
OS_MEMORY_TERMINATION_DURING_QUALIFICATION=HARD_FAIL
RUNTIME_CRASH_DURING_MEASURED_RUN=HARD_FAIL
WRONG_MODEL_ARTIFACT_IDENTITY=HARD_FAIL
RUNTIME_IDENTITY_DRIFT=HARD_FAIL
```

Performance thresholds must be frozen before real device execution. No observed candidate result may set, loosen, or reinterpret them.

## 7. Pre-execution evidence versus measured qualification

```text
PRE_EXECUTION_READINESS_REQUIRES_MEASURED_RUNS=NO
POST_EXECUTION_QUALIFICATION_REQUIRES_FIVE_COMPLETE_MEASURED_RUNS=YES
REAL_MEASURED_RUNS_CURRENTLY_PRESENT=0
```

This intake is pre-execution only. It must not contain fabricated timing, memory, thermal, energy, package, crash, or throughput measurements.

Future measured evidence, only after all separate authorities and preflight PASS, must preserve the frozen record families including:

```text
TTFT_MS
PREFILL_TOKENS_PER_SECOND
DECODE_TOKENS_PER_SECOND
SUSTAINED_THROUGHPUT_TOKENS_PER_SECOND
THERMAL_STATE_BEFORE_RUN
THERMAL_STATE_AFTER_RUN
THROTTLING_OBSERVED
BATTERY_DELTA_OR_ENERGY_PROXY_PER_RUN
```

No observed numeric values are recorded here.

## 8. Runtime environment / E004 execution-subject intake

Before E004 execution can start, the future exact execution subject must bind the applicable runtime/evaluation identities, including:

```text
canonical_repository_commit=NEEDS_EVIDENCE
model_artifact_sha256=NEEDS_EVIDENCE
complete_bundle_sha256=NEEDS_EVIDENCE
evaluation_artifact_ids_and_sha256=NEEDS_EVIDENCE
lineage_and_license_evidence_ids=NEEDS_EVIDENCE
contamination_disposition=NEEDS_EVIDENCE_EXPECTED_ASSESSED_CLEAN_WHERE_REQUIRED
runtime_entrypoint=NEEDS_EVIDENCE
runtime_executable_sha256=NEEDS_EVIDENCE
llama_cpp_core_revision=NEEDS_EVIDENCE
tokenizer_or_rendering_config_sha256=NEEDS_EVIDENCE
environment_manifest_sha256=NEEDS_EVIDENCE
exact_argv=NEEDS_EVIDENCE
network_boundary=NEEDS_EVIDENCE
credential_state=NEEDS_EVIDENCE
spend_state=NEEDS_EVIDENCE_CURRENT_BOUNDARY_USD_0
```

This section is an intake surface only; it does not construct an E004 execution manifest or imply admission. The canonical A11 request template remains non-activatable until its full upstream sequence is complete.

## 9. A7 personnel-governance intake

Personnel qualification, assignment, and payload access are distinct states.

```text
QUALIFIED_PERSON != ASSIGNED_PERSON
ASSIGNED_PERSON != PAYLOAD_ACCESS_GRANTED
FOUNDER_STATUS_ALONE_PROVES_QUALIFICATION=NO
PERSONNEL_IDENTITY_OR_CREDENTIALS_MAY_BE_INVENTED=NO
PUBLIC_REPO_RAW_PERSONNEL_EVIDENCE=PROHIBITED
PUBLIC_REPO_PERSONNEL_REFERENCES=OPAQUE_ONLY
```

For each function that future E004/preconstruction work actually requires, intake must classify the need without inventing a person:

```text
FUNCTION_REQUIRED=NEEDS_EVIDENCE_OR_NOT_REQUIRED_WITH_CANONICAL_JUSTIFICATION
ROLE_CLASS=NEEDS_EVIDENCE
OPAQUE_PERSONNEL_REFERENCE=NEEDS_EVIDENCE_IF_REQUIRED
QUALIFICATION_DISPOSITION=NEEDS_EVIDENCE_IF_REQUIRED
CONFLICT_DISPOSITION=NEEDS_EVIDENCE_IF_REQUIRED
PRIVATE_GOLD_EXPOSURE_DISPOSITION=NEEDS_EVIDENCE_IF_REQUIRED
INDEPENDENCE_VALIDATION=NEEDS_EVIDENCE_IF_REQUIRED
ASSIGNMENT_AUTHORITY_REFERENCE=NEEDS_EVIDENCE_IF_REQUIRED
```

Potential role classes are governed by A7/A13 and may include `PAYLOAD_CUSTODIAN`, `CONTAMINATION_ASSESSOR`, `EVALUATION_EXECUTOR`, and other author/reviewer/adjudicator roles. This intake does not assert that a human must fill a function the frozen protocol can validly satisfy without new personnel.

A7 `OPERATIONAL_PASS` cannot be inferred from design documents. Session 13 Q5 requires exact policy binding, protected personnel-evidence storage controls, opaque/public index integrity, state machines, independent evidence validation, steady-state handoff evidence, and bootstrap privilege revocation before operational PASS may be declared.

## 10. A13 storage/access intake

A13 remains a three-zone least-privilege boundary:

```text
ZONE_1=METADATA_AND_GOVERNANCE
ZONE_2=SELECTION_CONTENT_PAYLOAD
ZONE_3=CANDIDATE_OUTPUT_AND_RESULT
PRIVATE_GOLD=SEPARATE_TRUST_DOMAIN
```

Future A13 operational evidence must bind at least:

```text
exact_storage_boundary_identity=NEEDS_EVIDENCE
zone_separation_enforcement_identity=NEEDS_EVIDENCE
acl_policy_identity=NEEDS_EVIDENCE
acl_policy_sha256=NEEDS_EVIDENCE
audit_logging_identity=NEEDS_EVIDENCE
role_to_capability_bindings=NEEDS_EVIDENCE
personnel_assignment_bindings=NEEDS_EVIDENCE_IF_REQUIRED
protected_payload_retention_policy=NEEDS_EVIDENCE
candidate_feedback_firewall_evidence=NEEDS_EVIDENCE
private_gold_namespace_separation_evidence=NEEDS_EVIDENCE
```

```text
DIRECTORY_NAME_ONLY_COUNTS_AS_SECURITY_BOUNDARY=NO
POLICY_WITHOUT_ENFORCEABLE_ACCESS_CONTROL=INSUFFICIENT
ZONE_2_SELECTION_PAYLOAD_MAY_BE_CREATED_NOW=NO
ZONE_3_RESULT_PAYLOAD_MAY_BE_CREATED_NOW=NO
A13_PASS_EQUALS_A15_CONSTRUCTION_AUTHORITY=NO
A13_PASS_EQUALS_MODEL_EXECUTION_AUTHORITY=NO
```

Actual Zone 2 payload creation remains downstream of separate A15 construction authority. Candidate-result access cannot flow backward into active authoring/review for the same suite identity.

## 11. A14 spend / engagement intake

Current hard boundary:

```text
CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_OPERATIONAL_PASS=NO
```

A14 final requirement determination is downstream of exact D34, A8, and A7 evidence:

```text
D34_FINAL_REQUIRED_BEFORE_A14_FINAL_REQUIREMENT=YES
A8_FINAL_REQUIRED_BEFORE_A14_FINAL_REQUIREMENT=YES
A7_FINAL_REQUIRED_BEFORE_A14_FINAL_REQUIREMENT=YES
```

Therefore this intake may only record evidence needed to later determine whether a new commitment exists. It may not set `A14_NOT_REQUIRED_PASS` by assumption, silence, convenience, lack of invoice, or a zero-dollar label.

```text
AVAILABLE_PERSONAL_DEVICE_IMPLIES_NO_NEW_RESOURCE_COMMITMENT=NEEDS_EVIDENCE
ALREADY_OWNED_INTERNAL_RESOURCE_IMPLIES_A14_NOT_REQUIRED=NO_BY_ITSELF
ZERO_DOLLAR_EXTERNAL_SERVICE_IMPLIES_AUTHORITY=NO
UNPAID_EXTERNAL_WORK_IMPLIES_AUTHORITY=NO
QUOTE_OR_ESTIMATE_EQUALS_SPEND_AUTHORITY=NO
AVAILABLE_FUNDS_EQUALS_SPEND_AUTHORITY=NO
```

Future evidence must distinguish separately:

```text
financial_commitment_requirement
payment_execution_requirement
new_personnel_engagement_requirement
resource_provisioning_requirement
payload_access_requirement
technical_execution_authority
```

These are not interchangeable booleans.

## 12. Current blocker matrix

| Evidence family | Current state | Can this intake close it? |
|---|---|---|
| exact accepted runtime artifacts | `NEEDS_EVIDENCE` | NO — separate artifact authority/provenance path |
| exact llama.cpp/runtime/build identities | `NEEDS_EVIDENCE` | NO — real identity binding required |
| five-target device instances/identities | `NEEDS_EVIDENCE` | NO — real resource evidence required |
| performance threshold policy | `UNRESOLVED_PRE_EXECUTION` | NO — scientific/governance freeze required |
| Windows primary memory method | `NEEDS_EVIDENCE` | NO — exact method binding required |
| A7 operational personnel governance | `BLOCKED` | NO — real protected evidence/verification required |
| A13 operational storage/ACL | `BLOCKED` | NO — real enforceable implementation/audit required |
| A14 requirement/pass | `BLOCKED` | NO — upstream D34/A8/A7 and exact requirement evidence required |
| measured device qualification | `NOT_STARTED` | NO — execution-only after preflight PASS |

## 13. Fail-closed intake rules

```text
MISSING_EVIDENCE_MAY_BE_INFERRED_FROM_CONVENIENCE=NO
PUBLIC_MARKETING_SPEC_COUNTS_AS_PHYSICAL_TARGET_EVIDENCE=NO
CODE_REVIEW_PASS_COUNTS_AS_DEVICE_QUALIFICATION=NO
DOCUMENT_MERGE_COUNTS_AS_PERSONNEL_ASSIGNMENT=NO
DOCUMENT_MERGE_COUNTS_AS_A13_ACCESS_GRANT=NO
DOCUMENT_MERGE_COUNTS_AS_A14_PASS=NO
NO_NEW_INVOICE_COUNTS_AS_A14_NOT_REQUIRED=NO
NO_MEASURED_RUN_COUNTS_AS_FAVORABLE_RESULT=NO
```

## Exclusions

This bounded intake explicitly excludes:

- model/GGUF download, conversion, loading, inference, benchmark payload access/execution, contamination assessment, selection-suite construction, device execution, measured qualification, winner selection, training, or provider generation;
- procurement, device reservation, account creation, credential use, storage provisioning, ACL changes, personnel recruitment/assignment/engagement, contracting, payment, reimbursement, or spend;
- PHI, restricted clinical data, Private Gold, raw personnel evidence, names, emails, phone numbers, license numbers, identity documents, or signed credential/attestation artifacts in the public repository;
- selecting performance thresholds, Windows memory methods, runtime wrappers, thermal/energy methods, personnel, vendors, or services by convenience;
- changing Spec 005 contracts, device target identities, package/memory gates, personnel separation rules, A13 firewall semantics, A14 ordering, PR #81 authority states, or any candidate identity.

## Exit Evidence

This **intake-template artifact** is eligible for repository-level closure only when one exact head demonstrates:

```text
INTAKE_REUSES_CANONICAL_DEVICE_CONTRACT_WITHOUT_NEW_SCHEMA=YES
INTAKE_LISTS_ALL_FIVE_FROZEN_TARGETS=YES
INTAKE_PRESERVES_PRIMARY_AND_CONTROL_DEVICE_ROLE_REQUIREMENTS=YES
INTAKE_PRESERVES_PRIMARY_ONLY_PACKAGE_HARD_CAP=YES
INTAKE_PRESERVES_ALL_TARGET_MEMORY_HARD_GATE=YES
INTAKE_DISTINGUISHES_PREEXECUTION_IDENTITY_FROM_MEASURED_QUALIFICATION=YES
INTAKE_PRESERVES_A7_QUALIFICATION_ASSIGNMENT_ACCESS_SEPARATION=YES
INTAKE_PRESERVES_A13_THREE_ZONE_AND_CANDIDATE_FEEDBACK_FIREWALL=YES
INTAKE_PRESERVES_A14_D34_A8_A7_DEPENDENCY_AND_ZERO_SPEND_BOUNDARY=YES
INTAKE_CREATES_REAL_EVIDENCE_OR_AUTHORITY=NO
```

Repository closure additionally requires fresh exact-head review with no unresolved material findings, no active review threads, bounded documentation-only diff verification, guarded canonical merge, and post-merge main verification. These checks close this checklist only; every real evidence slot remains `NEEDS_EVIDENCE` until separately produced and verified under its governing authority.
