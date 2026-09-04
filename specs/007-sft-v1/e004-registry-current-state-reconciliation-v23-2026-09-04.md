# E004 Registry Current-State Reconciliation V23 — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Reconciliation class:** append-only current-state overlay  
**Supersedes as current view:** `e004-registry-current-state-reconciliation-v22-2026-09-04.md`  
**Canonical base:** `2d4b51c8e076284902e178b0fb1fb46ba4e93d37`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Purpose

Reconcile the E004 current view after canonical merge of the exact Aya-43 curriculum and content-scope persistence evidence in PR #234.

This artifact records what is now evidenced. It does not manufacture DatasetSnapshot, sentinel, model, conversion, activation, execution, training, resource, credential, procurement, payment, or spend authority.

## 2. Canonical change since V22

V22 ended at the corrected Spec 003 exact 43-record eligible set and correctly recorded that final curriculum admission authority was then absent.

A later canonical Founder decision supplied the exact bounded authority:

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
FINAL_CURRICULUM_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_SP007_RESEARCH_COMPONENT_ONLY
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
CURRICULUM_RECORD_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_HASH_BOUND_METADATA_ONLY
CONTENT_SCOPE_VERIFICATION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_ONLY
DATASET_SNAPSHOT_AUTHORITY=NONE
```

The authorized deterministic construction was subsequently implemented and persisted without expanding that authority.

## 3. Exact Aya-43 evidence now canonical

PR #234 merged as `2d4b51c8e076284902e178b0fb1fb46ba4e93d37` from exact head `8611c90bed7283338e9286b7751e1117421b8bed`.

Exact-head Actions run `33864457065`, job `100996009504`, completed successfully and reconstructed and validated the exact persisted subject:

```text
AYA_43_CURRICULUM_RECORD_COUNT=43
AYA_43_CONTENT_SCOPE_VERIFICATION_COUNT=43
AYA_43_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
AYA_43_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
PERSISTED_RAW_AYA_TEXT=ABSENT
PERSISTED_USER_ID=ABSENT
VALIDATION=PASS
```

The canonical evidence record is:

`specs/007-sft-v1/e004-aya-43-curriculum-construction-evidence-v1-2026-09-04.md`

## 4. Dependency-order reconciliation

The controlling component blocker packet defines the following first dependencies:

1. freeze exact admitted gradient-bearing content with provenance, rights/license, privacy, split, verification, and contamination state;
2. freeze exact content-scope verification identities for every gradient-bearing record;
3. freeze the exact seven required sentinel fixture identities and expected actions without optimization feedback;
4. freeze an exact DatasetSnapshot and quarantine verification identity;
5. continue through model/checkpoint, RunManifest, scope-binding, guard, access/resource, activation, and execution prerequisites in order.

For the exact Aya-43 component subject, the current evidence state is now:

```text
DEPENDENCY_1_EXACT_ADMITTED_GRADIENT_CONTENT=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_2_CONTENT_SCOPE_VERIFICATION_IDENTITIES=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_3_EXACT_SEVEN_SENTINEL_FIXTURE_IDENTITIES=NOT_YET_FROZEN_AS_LIVE_COMPONENT_SUBJECT
DEPENDENCY_4_DATASET_SNAPSHOT_AND_QUARANTINE_IDENTITY=BLOCKED_BY_MISSING_DATASET_SNAPSHOT_AUTHORITY
```

No dependency after item 2 is promoted to PASS by this reconciliation.

## 5. Successor execution authority remains conditional

The previously canonical Founder decision remains effective:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

This authority is necessary but not sufficient. It does not convert any absent/stale/mismatched preflight input into PASS and cannot be used before the exact subject satisfies every applicable preflight requirement.

## 6. Current component evidence map

```text
LIVE_COMPONENT_ADMITTED_CURRICULUM=EXACT_AYA_43_HASH_BOUND_METADATA_PERSISTED
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=EXACT_43_PERSISTED_VALIDATED
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_QUARANTINE_PASS_BINDING=ABSENT_FOR_DATASET_SNAPSHOT
LIVE_COMPONENT_BASE_CHECKPOINT_BINDING=ABSENT
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
LIVE_COMPONENT_RESOURCE_FINANCE_BINDINGS=INCOMPLETE
LIVE_COMPONENT_ACCESS_BINDINGS=INCOMPLETE
LIVE_COMPONENT_PREFLIGHT_ALLOWED_TRUE=NO
REAL_COMPONENT_MODEL_EXECUTION_PERFORMED=NO
REAL_COMPONENT_TOURNAMENT_EXECUTION_PERFORMED=NO
```

## 7. Data and privacy boundary

The exact Aya-43 authority is consumed only for the already-evidenced bounded construction. It does not authorize source expansion or DatasetSnapshot creation.

```text
AYA_BLOCKED_RECORD_COUNT=92
AYA_BLOCKED_RECORD_DOWNSTREAM_ADMISSION=PROHIBITED
OASST1_ADMISSION_AUTHORITY=NONE
DOLLY_15K_ADMISSION_AUTHORITY=NONE
OTHER_DATASET_ADMISSION_AUTHORITY=NONE
SOURCE_EXPANSION_AUTHORITY=NONE
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
AYA_USER_ID_READ_OR_PERSISTENCE=PROHIBITED
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
```

## 8. Model, activation, training, and spend boundary

```text
MODEL_WINNER_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 9. E004 / E005 state

The Aya-43 curriculum-construction substep is complete, but the tournament evidence pack is not.

```text
CURRENT_AYA_DATA_FRONTIER=AYA_43_COMPONENT_CURRICULUM_AND_SCOPE_EVIDENCE_PERSISTED_VALIDATED
AYA_43_CURRICULUM_CONSTRUCTION_SUBSTEP=COMPLETE
AYA_43_CONTENT_SCOPE_VERIFICATION_SUBSTEP=COMPLETE
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

The Phase E task order remains controlling. This component work does not silently complete E008 or E009 and does not make E005 reachable.

## 10. Immediate frontier

The first unevidenced item in the component dependency list is the exact seven sentinel-fixture identity freeze. Before mutating that live component subject, repository governance and existing authority must be checked for an explicit applicable construction/freeze authority. If no such authority exists, the next safe repository action is a bounded Founder decision surface for that exact item; generic continuation approval cannot manufacture it.

DatasetSnapshot is not the immediate mutation because its canonical authority is explicitly `NONE` and the Founder curriculum decision states that it is not reachable pending separate authority.

## 11. Review boundary

Under FD-007 / constitutional amendment 0.1.1, independent repository review is optional by default for bounded repository reconciliation. No review PASS may be inferred from bot silence or service unavailability.

## 12. Merge qualification

Before merging this reconciliation, verify:

- exact current `main` base;
- exact PR head and bounded changed-file scope;
- all applicable exact-head CI/status checks;
- unresolved review-thread state;
- mergeability;
- branch protection and repository rulesets;
- absence of later canonical invalidation; and
- expected-head guarded merge.

This reconciliation must remain descriptive and fail closed.