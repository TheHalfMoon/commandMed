# E004 Post-Intake Frontier Reconciliation — 2026-08-27

**Spec:** 007 SFT V1  
**Canonical base at preparation:** `32006088b24b93973ce4624ff99971135d586e9e`  
**Artifact class:** append-only frontier reconciliation  
**Authority effect:** NONE  
**E004 execution performed:** NO

This record reconciles the E004 frontier after corrective maintenance, governance preparation, authority-request preparation, runtime/resource/personnel evidence-intake preparation, and bounded public runtime-candidate research. It distinguishes repository preparation from scientific or operational closure.

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Repository-preparation milestones already canonical

```text
CORRECTIVE_MAINTENANCE=CANONICAL
PR80_GOVERNANCE_FOUNDATION_CANDIDATES=CANONICAL
PR81_ARTIFACT_DECISION_AND_PROSPECTIVE_A11_REQUEST_SURFACES=CANONICAL
PR83_RUNTIME_RESOURCE_PERSONNEL_INTAKE=CANONICAL
```

These milestones prepare controls and intake surfaces only. They do not create real clinical/statistical thresholds, personnel evidence, storage enforcement, device measurements, contamination PASS, artifact conversion authority, winner evidence, or training authority.

### Corrective maintenance

```text
DEVICE_A15_STRUCTURAL_CYCLE=REPAIRED_CANONICALLY
PACKAGE_BOUNDARY_RECONCILIATION=REPAIRED_CANONICALLY
WARMUP_SEMANTICS_RECONCILIATION=REPAIRED_CANONICALLY
NON_EXECUTING_E004_REQUEST_ENVELOPE=PRESENT
CORRECTIVE_MAINTENANCE_EQUALS_E004_PASS=NO
```

### PR #80

```text
PR80_MERGE=57e7a172ca888333255d4c12a441dbe9fd97c811
PR80_EFFECT=GOVERNANCE_FOUNDATION_CANDIDATES_ONLY
A5_A6_A8_A12_OPERATIONAL_PASS_CREATED=NO
```

### PR #81

```text
PR81_MERGE=27faa40707f66302be56311357fd61792ea66835
FOUNDER_ARTIFACT_DECISION=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
A11_ACTIVE_REQUEST=ABSENT
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A15_CONSTRUCTION_AUTHORITY=ABSENT
```

### PR #83

```text
PR83_MERGE=32006088b24b93973ce4624ff99971135d586e9e
PR83_TREE=50959a6cfa03623fc3ebe6b2a4025f9eaa3530ca
RUNTIME_RESOURCE_PERSONNEL_INTAKE_TEMPLATE=PREPARED
REAL_RUNTIME_BINDINGS_CREATED=0
REAL_DEVICE_TARGET_BINDINGS_CREATED=0
REAL_PERSONNEL_ASSIGNMENTS_CREATED=0
REAL_A13_ACCESS_GRANTS_CREATED=0
REAL_A14_AUTHORIZATIONS_CREATED=0
REAL_MEASURED_DEVICE_RUNS_CREATED=0
```

The low-resource laptop target remains `Windows_11_x64_OR_EQUIVALENT_LINUX_x86_64`; the exact OS path and its applicable primary memory method must be bound before results.

## 2. Authority state remains fail-closed

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
LIVE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_E003_BOUNDED_CONDITIONAL
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

```text
AUTHORITY_EXISTS_EQUALS_EXECUTABLE_NOW=NO
DOCUMENT_MERGE_EQUALS_OPERATIONAL_PASS=NO
GENERIC_CONTINUE_INSTRUCTION_EQUALS_SEPARATE_FOUNDER_GATE_DECISION=NO
```

## 3. Scientific/statistical blocker remains real

```text
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO
```

Future closure requires qualified clinical/statistical review, exact metric/suite identities, numeric methods, sample-size/power/allocation rationale, and any still-required Founder false-positive/over-triage posture decision.

```text
NUMERIC_THRESHOLD_INFERENCE_FROM_LITERATURE_ALONE=PROHIBITED
NUMERIC_THRESHOLD_INFERENCE_FROM_MODEL_RESULTS=PROHIBITED
QUALIFIED_REVIEWER_IDENTITY_MAY_BE_FABRICATED=NO
```

## 4. Artifact/conversion blocker is decision-ready, not decided

```text
FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=DECISION_NOT_TAKEN
E002_PRECONVERTED_ALLOWLIST_COUNT=2
GRANITE_PRIMARY_FINAL_RUNTIME_ARTIFACT=NEEDS_EVIDENCE
QWEN3_4B_CONTROL_FINAL_RUNTIME_ARTIFACT=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
```

Public GGUF existence cannot substitute for exact frozen-source lineage, byte identity, or a Founder artifact decision.

## 5. A11 contamination remains downstream of construction

```text
A11_PLAN_PREDECLARED
-> ALL_OTHER_PRECONSTRUCTION_GATES_COMPLETE
-> SEPARATE_A15_CONSTRUCTION_AUTHORITY
-> AUTHORIZED_CONSTRUCTION_AND_EXACT_SUITE_FREEZE
-> SEPARATE_A11_PAYLOAD_ACCESS_AND_EXECUTION_AUTHORITY
-> EXACT_AND_SEMANTIC_CONTAMINATION_ASSESSMENT
-> EVIDENCE_BOUND_DISPOSITION
```

Current state:

```text
A15_CONSTRUCTION_AUTHORITY=ABSENT
EXACT_SELECTION_SUITE_CONSTRUCTED=NO
A11_ACTIVE_REQUEST=ABSENT
CONTAMINATION_ASSESSMENT_EXECUTION_OCCURRED=NO
CONTAMINATION_PASS_CREATED=NO
```

## 6. Public runtime research reduced ambiguity but did not bind execution

The companion runtime research records exact public source/build metadata at llama.cpp commit:

```text
CURRENT_UPSTREAM_SOURCE_CANDIDATE=c1d0e7a004015f23bc0233470b747b596f29b264
OBSERVED_MATCHING_BUILD_TAG=b10621
QWEN3_IMPLEMENTATION_MAPPING_OBSERVED=YES
QWEN35_IMPLEMENTATION_MAPPING_OBSERVED=YES
FROZEN_GRANITE_HF_CLASS_TO_LLAMA_CPP_CONVERTER_MAPPING_OBSERVED=YES
```

Granite naming is deliberately disambiguated:

```text
FROZEN_GRANITE_PRODUCT=granite-4.0-350m-base
FROZEN_GRANITE_PRODUCT_TOPOLOGY=DENSE_ALL_ATTENTION
FROZEN_GRANITE_HF_ARCHITECTURE_CLASS=GraniteMoeHybridForCausalLM
LLAMA_CPP_CONVERTER_ARCH_NAME_FOR_THAT_CLASS=GRANITE_HYBRID
SCREENED_OUT_DISTINCT_PRODUCT=granite-4.0-h-350m-base
CONVERTER_ARCH_NAME_EQUALS_SCREENED_OUT_PRODUCT=NO
```

This is source/converter metadata only. It does not prove exact GGUF load success or device qualification.

```text
FINAL_LLAMA_CPP_CORE_REVISION=NEEDS_EVIDENCE
FINAL_RUNTIME_ARTIFACT_SHA256=NEEDS_EVIDENCE
FINAL_BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
FINAL_WRAPPER_IDENTITIES=NEEDS_EVIDENCE
FINAL_BACKEND_CONFIGURATION=NEEDS_EVIDENCE
```

## 7. Device/resource evidence remains external

Frozen targets remain:

```text
Apple_iPhone_17_Pro_12GB
Apple_iPhone_13_4GB
Samsung_Galaxy_A56_5G_8GB
Samsung_Galaxy_A16_5G_4GB
Intel_N100_8GB_x86_64
```

Current evidence:

```text
REAL_FIVE_TARGET_BINDINGS=0
REAL_MEASURED_DEVICE_RUNS=0
PERFORMANCE_THRESHOLD_POLICY=UNRESOLVED_PRE_EXECUTION
EXACT_BUILD_TOOLCHAINS=NEEDS_EVIDENCE
EXACT_MEMORY_MEASUREMENT_IDENTITIES=NEEDS_EVIDENCE_PER_BOUND_PLATFORM
EXACT_THERMAL_SIGNAL_METHODS=NEEDS_EVIDENCE
EXACT_ENERGY_SIGNAL_METHODS=NEEDS_EVIDENCE
EXACT_EXECUTION_PLAN_IDENTITIES=NEEDS_EVIDENCE
```

Public hardware specifications or upstream binaries do not prove commandMed device qualification.

## 8. A7 personnel remains protected and unproduced

```text
A7_OPERATIONAL_PASS=NO
EXACT_PERSONNEL_ROSTER=ABSENT
REAL_QUALIFICATION_ATTESTATIONS=ABSENT
REAL_CONFLICT_DISPOSITIONS=ABSENT
REAL_PRIVATE_GOLD_NONEXPOSURE_DISPOSITIONS=ABSENT
REAL_INDEPENDENCE_VALIDATIONS=ABSENT
```

The public repository must not invent or expose protected personnel evidence.

## 9. A13 storage/access remains operationally blocked

```text
A13_OPERATIONAL_PASS=NO
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
EXACT_ACL_POLICY_IDENTITY=NEEDS_EVIDENCE
AUDIT_LOGGING_IDENTITY=NEEDS_EVIDENCE
ROLE_TO_CAPABILITY_BINDINGS=NEEDS_EVIDENCE
CANDIDATE_FEEDBACK_FIREWALL_OPERATIONAL_EVIDENCE=NEEDS_EVIDENCE
```

A policy document or folder structure is not an enforceable storage/access PASS.

## 10. A14 finance/engagement remains operationally blocked

```text
A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_OPERATIONAL_PASS=NO
CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
```

A14 remains downstream of exact D34, A8, and A7 evidence. Free service, owned hardware, volunteer labor, or absent invoices cannot create `A14_NOT_REQUIRED_PASS`.

## 11. Real A1–A14 snapshot and A15 activation remain absent

```text
REAL_A1_A14_PASS_SNAPSHOT=ABSENT
A15_REAL_ACTIVATION=ABSENT
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E004_EXECUTION_STARTABLE=NO
```

A15 may not be synthesized from design documents or repository progress.

## 12. Dependency-safe next transitions

1. Obtain an explicit Founder artifact decision from the canonical PR #81 decision surface; if conversion is selected, create and review an exact conversion subject before conversion.
2. Resolve scientific/statistical thresholds through qualified identity-bound evidence and required Founder posture decisions.
3. Produce real A7 personnel-governance evidence in protected storage and complete independent verification.
4. Implement and verify the exact A13 storage/ACL/audit boundary without prematurely creating protected selection payload.
5. Determine A14 requirements only after its upstream dependencies while preserving `$0` until separate authorization.
6. Bind exact runtime/build/wrapper/device/measurement identities before real device execution.
7. Assemble and independently verify a real A1–A14 snapshot.
8. Request and receive separate exact A15 construction/activation authority as required by the frozen sequence.
9. Only after applicable construction, contamination, artifact, runtime/resource, and activation gates are satisfied may E004 execution become startable.

## 13. Downstream tasks remain unreachable

```text
E005_REACHABLE=NO
E006_REACHABLE=NO
E007_REACHABLE=NO
E008_REAL_DATA_CONSTRUCTION_REACHABLE=NO_UNTIL_ITS_AUTHORITY_AND_DEPENDENCIES
E009_REACHABLE=NO
E010_REACHABLE=NO
E011_TRAINING_AUTHORITY_REACHABLE=NO
E012_FIRST_SFT_RUN_REACHABLE=NO
```

No winner, tokenizer/checkpoint binding, backend selection, real curriculum, training numerics, training RunManifest authority, or SFT run may be fabricated.

## 14. Furthest genuinely completable repository-only state

Once this reconciliation and the companion runtime research are exact-head reviewed and canonically merged, the repository-only E004 blocker-reduction frontier is exhausted **under current authority and available evidence**.

Remaining progress requires one or more of:

```text
FOUNDER_DECISION
REAL_QUALIFIED_CLINICAL_OR_STATISTICAL_EVIDENCE
REAL_PROTECTED_PERSONNEL_EVIDENCE
REAL_STORAGE_ACCESS_IMPLEMENTATION_EVIDENCE
REAL_RESOURCE_DEVICE_RUNTIME_BINDINGS
SEPARATE_A15_OR_A11_AUTHORITY
SEPARATE_ARTIFACT_CONVERSION_AUTHORITY_IF_SELECTED
```

Manufacturing placeholders, self-approving gates, downloading/converting unauthorized artifacts, or simulating measurements would violate the canonical plan rather than finish it.

## Exclusions

This reconciliation excludes:

- declaring E004/E005 or downstream tasks complete;
- granting Founder decisions or interpreting generic continuation as a distinct Founder gate decision;
- downloading/converting/loading models or GGUF artifacts beyond existing authority;
- benchmark payload access/execution, selection-suite construction, contamination assessment, device runs, model inference, training, provider generation, PHI, Private Gold, gated assets, credentials, procurement, personnel engagement, or spend;
- inventing thresholds, sample sizes, reviewer qualifications, personnel attestations, access grants, runtime/device measurements, or A1–A15 PASS states;
- selecting the companion runtime source candidate as final commandMed runtime by documentation merge.

## Exit Evidence

This reconciliation is repository-level complete only if its exact head is independently reviewed with no unresolved material findings, the diff remains documentation-only and bounded, the head is merged under an exact-head guard, and post-merge `main` is verified.

That closure means only:

```text
POST_PR83_FRONTIER_RECONCILED=YES
PUBLIC_RUNTIME_CANDIDATE_METADATA_RESEARCH_RECORDED=YES
CURRENT_AUTHORITY_AND_EVIDENCE_WALL_EXPLICIT=YES
E004_REMAINS_INCOMPLETE=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

It does not convert absent real evidence or authority into PASS.