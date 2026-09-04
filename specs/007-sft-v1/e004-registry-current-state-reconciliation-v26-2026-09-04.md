# E004 Registry Current-State Reconciliation V26 — 2026-09-04

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Reconciliation class:** append-only current-state overlay
**Supersedes as current view:** `e004-registry-current-state-reconciliation-v25-2026-09-04.md`
**Canonical base before this reconciliation:** `b7b4c9aaae8e76bdcef2c3def0cd856038e25558`
**Authority effect:** NONE
**Execution effect:** NONE
**Training authority:** NONE
**Spend authority:** NONE

## 1. Purpose

Reconcile E004 after post-PR-#240 verification of the DatasetSnapshot dependency boundary.

V25 correctly identified DatasetSnapshot/quarantine as dependency item 4 and recorded `DATASET_SNAPSHOT_AUTHORITY=NONE`. This reconciliation preserves that result, records the exact supporting-evidence gap, records a repository implementation incompatibility discovered by reading the canonical DatasetSnapshot/quarantine code against the frozen Aya-43 records, and points to the bounded Founder decision-request surface prepared for the next authority decision.

This record creates no DatasetSnapshot, supporting PASS, repair authority, model execution, winner selection, conversion, A15 activation, or training authority.

## 2. Canonical dependencies 1–3 remain satisfied

```text
DEPENDENCY_1_EXACT_ADMITTED_GRADIENT_CONTENT=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_2_CONTENT_SCOPE_VERIFICATION_IDENTITIES=EVIDENCED_EXACT_AYA_43_ONLY
DEPENDENCY_3_EXACT_SEVEN_SENTINEL_FIXTURE_IDENTITIES=CONSTRUCTED_FROZEN_VALIDATED_EXACT_SUBJECT
CURRENT_AYA_DATA_FRONTIER=AYA_43_COMPONENT_CURRICULUM_AND_SCOPE_EVIDENCE_PERSISTED_VALIDATED
CURRENT_COMPONENT_SENTINEL_FRONTIER=EXACT_SENTINEL_7_FROZEN_VALIDATED
```

No later evidence invalidating those exact subjects was found during this reread.

## 3. DatasetSnapshot authority search result

The current canonical repository was searched for an applicable DatasetSnapshot construction/freeze authority after PR #240.

```text
APPLICABLE_CANONICAL_DATASET_SNAPSHOT_AUTHORITY_FOUND=NO
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
```

Existing records that mention DatasetSnapshot preserve `NONE`; none creates an exact authority for the current Aya-43 component subject.

## 4. Existing supporting evidence and remaining duplicate gap

Existing canonical evidence establishes:

```text
AYA_CANDIDATE_EXACT_CONTENT_DEDUPLICATION_PERFORMED=YES
AYA_SOURCE_ROWS_EXCLUDED_AS_EXACT_DUPLICATE_CONTENT=3
AYA_135_EXTERNAL_CONTAMINATION_METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
AYA_135_CONTAMINATION_RESULTS_SHA256=f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857
AYA_135_CONTAMINATION_ASSESSED_CLEAN_COUNT=135
AYA_135_CONTAMINATION_OVERLAP_OR_HIGH_RISK_COUNT=0
```

Those facts are relevant but do not establish the complete `DuplicateContaminationReport` PASS required by the Spec 007 logical contract. The current repository contains no independent near-duplicate PASS for the exact Aya-43 subject.

```text
AYA_43_NEAR_DUPLICATE_ASSESSMENT=ABSENT
AYA_43_DUPLICATE_CONTAMINATION_REPORT_PASS=ABSENT
```

No empty near-duplicate finding set may be fabricated from exact-content deduplication or external benchmark contamination evidence.

## 5. Quarantine binding semantics

The canonical TRAIN quarantine rule currently permits:

```text
VERIFIED_PERMISSIVE_PRETRAINING_CORPUS
VERIFIED_SFT_CURRICULUM_DATA
VERIFIED_SYNTHETIC_DERIVED_EXAMPLES
```

with `can_train=true`.

The exact Aya-43 CurriculumRecords are frozen with distinct provenance and split identities:

```text
source_authority_id=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
split_id=VERIFIED_SFT_CURRICULUM_DATA
```

The first field is the Founder provenance/authority identity. The second is the canonical training split/source identity represented by the quarantine matrix.

## 6. DatasetSnapshot builder incompatibility

Current `src/commandmed/spec007/snapshot.py` `_validated_records()` evaluates both `source_authority_id` and `split_id` with `evaluate_quarantine_source(..., "TRAIN")` and requires both to be allowed and trainable.

That behavior is incompatible with the frozen Aya-43 records because `E004_FINAL_CURRICULUM_ADMISSION_DECISION_B` is not a quarantine source ID and must not be added to the quarantine source allowlist merely to make the builder pass.

```text
SNAPSHOT_BUILDER_AYA_43_CURRENT_RESULT=FAIL_CLOSED_ON_SOURCE_AUTHORITY_AS_QUARANTINE_SOURCE
FROZEN_AYA_43_RECORD_MUTATION_ALLOWED=NO
QUARANTINE_ALLOWLIST_WIDENING_ALLOWED=NO
EXISTING_E004_CORRECTIVE_MAINTENANCE_AUTHORITY_COVERS_SNAPSHOT_PY=NO
```

The earlier E004 corrective-maintenance authority is path- and objective-bounded and does not authorize changing `src/commandmed/spec007/snapshot.py`. Therefore no repair is performed by this reconciliation.

## 7. Activation preflight requires a real quarantine PASS identity

The canonical activation preflight resolves `dataset_snapshot.quarantine_verification_id` through the component-store `quarantine_verifications` collection and requires the resolved record to have matching identity and `status=PASS`.

```text
QUARANTINE_VERIFICATION_IDENTITY_FOR_DATASET_SNAPSHOT=ABSENT
QUARANTINE_VERIFICATION_PASS_FOR_DATASET_SNAPSHOT=ABSENT
```

A non-empty string in DatasetSnapshot is insufficient by itself.

## 8. Bounded next decision surface

The dependency-safe next repository action is the decision-request artifact:

`specs/007-sft-v1/e004-dataset-snapshot-quarantine-founder-decision-request-2026-09-04.md`

That surface predeclares the exact Aya-43-only subject, deterministic record order, supporting duplicate/near-duplicate method class, exact existing contamination evidence boundary, exact TRAIN quarantine source/split identity, and a narrow corrective repair scope for the provenance-vs-quarantine-source incompatibility.

The request itself has no authority effect.

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=ABSENT
DATASET_SNAPSHOT_AUTHORITY=NONE
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=NONE
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=NONE
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=NONE
```

## 9. Ledger drift identified

At this base, `specs/007-sft-v1/tasks.md` still describes V24 as the current E004 state and still says the sentinel Founder decision is absent. That text is stale after PR #240/V25.

The ledger must be reconciled descriptively to the current sentinel-frozen state and DatasetSnapshot decision frontier. Such reconciliation creates no authority and does not mark E004 complete.

## 10. Later boundaries remain closed

```text
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
SENTINEL_GUARD_PASS_CREATED=NO
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Current project state

```text
NEXT_DEPENDENCY=DATASET_SNAPSHOT_AND_QUARANTINE_IDENTITY
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

No generic continuation instruction may substitute for an exact decision where the canonical decision surface explicitly requires an exact post-canonical Founder token.

## 12. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded reconciliation. Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, DatasetSnapshot/quarantine code semantics, current Aya-43/sentinel identities, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
