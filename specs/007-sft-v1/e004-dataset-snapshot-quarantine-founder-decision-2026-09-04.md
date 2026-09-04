# E004 DatasetSnapshot and Quarantine Founder Decision — 2026-09-04

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Controlling request:** `e004-dataset-snapshot-quarantine-founder-decision-request-2026-09-04.md`
**Decision owner:** Founder
**Decision:** B
**Training authority:** NONE
**Spend authority:** NONE

The Founder supplied the exact post-canonical Decision B token required by the controlling request:

```text
FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B
```

The resulting bounded authorities are exactly those predeclared under Decision B in the controlling request:

```text
DATASET_SNAPSHOT_AUTHORITY=AUTHORIZED_CONDITIONAL_EXACT_AYA_43_RESEARCH_COMPONENT_ONLY
DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_AYA_43_PREDECLARED_METHOD_ONLY
QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_VERIFIED_SFT_CURRICULUM_DATA_TRAIN_BINDING_ONLY
SNAPSHOT_BUILDER_REPAIR_AUTHORITY=AUTHORIZED_NARROW_PROVENANCE_VS_QUARANTINE_SEMANTICS_REPAIR_ONLY
DATASET_SNAPSHOT_FREEZE_REQUIRES_DUPLICATE_REPORT_PASS=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_CONTAMINATION_EVIDENCE_MATCH=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_QUARANTINE_VERIFICATION_PASS=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_EXACT_AYA_43_IDENTITY_MATCH=YES
DATASET_SNAPSHOT_FREEZE_REQUIRES_VALIDATOR_PASS=YES
RAW_AYA_TEXT_REPOSITORY_PERSISTENCE=PROHIBITED
MODEL_INFERENCE_AUTHORITY_EXPANSION=NONE
MODEL_WINNER_SELECTION_AUTHORITY_EXPANSION=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

All exact subject identities, near-duplicate method semantics, transient-byte restrictions, quarantine binding semantics, narrow `snapshot.py` repair limits, authorized path families, and qualification gates are inherited unchanged from the controlling canonical request. Decision B authorizes construction but does not predetermine PASS.

No later boundary is opened by this record. E004 remains incomplete until the newly authorized supporting evidence and DatasetSnapshot dependency actually qualify; E005 remains not reached.