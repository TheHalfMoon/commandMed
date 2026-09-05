# E004 Selection-Dev Manifest Contract Implementation — 2026-09-05

**Spec:** 007 SFT V1 / inherited Spec 005 Q2  
**Depends on:** canonical FD-009 and the existing Session 9 Q1/Q2 population/design architecture  
**Implementation effect:** repository-only fail-closed manifest metadata validation  
**Benchmark/model payload access:** NO  
**Clinical case authoring:** NO  
**Model execution:** NO  
**Current authorized spend:** USD 0

## Purpose

Convert the already-frozen Q2 selection-dev manifest metadata requirements into executable validation without opening benchmark payloads, creating clinical cases, or weakening quarantine boundaries.

Canonical implementation:

```text
IMPLEMENTATION=src/commandmed/spec005/selection_dev.py
TESTS=tests/spec005/test_selection_dev.py
MANIFEST_SCHEMA_VERSION=1.0
METRICS_CONTRACT_SCHEMA_ID=commandmed-metrics-catalog
METRICS_CONTRACT_SCHEMA_VERSION=2.0
METRICS_CATALOG_PATH=data/eval/metrics-v2.json
METRICS_V2_SHA256=bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b
```

## Exact case metadata contract

Every case record binds exactly:

```text
case_id
root_case_id_or_explicit_none
quality_lane
role
language_or_explicit_not_applicable
use_context_or_task_stratum
source_component_id
quarantine_purpose
metric_id_or_metric_mapping_id
pair_id_or_explicit_none
fold_id_or_explicit_none
artifact_identity
source_revision
contamination_evidence_identity_or_unresolved_state
```

Payload-bearing or prompt/output fields are not part of the closed schema.

## Selection boundaries

```text
ALLOWED_QUARANTINE_PURPOSES=DEV,CHECKPOINT_SELECTION
TRAIN=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PUBLIC_EXTERNAL_EVAL=PROHIBITED
CANDIDATE_NEUTRAL=true_REQUIRED
PRE_RESULT_FREEZE=true_REQUIRED
```

An execution-ready validation additionally requires resolved contamination evidence for every case.

## Arabic paired invariant

For Lane E:

```text
PAIR_ID=REQUIRED
ROOT_CASE_ID=REQUIRED
LANGUAGES=EXACTLY_ONE_ar_AND_ONE_en_PER_PAIR
SHARED_ROOT_CASE_ID=REQUIRED
QUARANTINE_PURPOSE=CHECKPOINT_SELECTION
UNPAIRED_PRIMARY_PARITY_EVIDENCE=PROHIBITED
```

This implements pairing structure only. It does not author, translate, access, or validate any clinical case payload.

## Canonical identity

The manifest carries `manifest_canonical_sha256`. The digest excludes that self-reference and sorts case records by `case_id`, making identity invariant to serialization order while preserving case content metadata.

## Frontier effect

After qualified canonical merge, the following Q2 implementation blocker becomes closed:

```text
SELECTION_DEV_MANIFEST_SCHEMA_IMPLEMENTED=YES
CANDIDATE_NEUTRAL_METADATA_VALIDATION_IMPLEMENTED=YES
ARABIC_PAIR_COMPLETENESS_METADATA_VALIDATION_IMPLEMENTED=YES
EXECUTION_READY_CONTAMINATION_BINDING_VALIDATION_IMPLEMENTED=YES
```

The following remain unresolved and must not be claimed complete from this implementation:

```text
EXACT_SELECTION_DEV_CASE_IDENTITIES=UNRESOLVED
EXACT_SOURCE_COMPONENTS=UNRESOLVED
EXACT_CONTAMINATION_EVIDENCE=UNRESOLVED
T1_A2_NUMERIC_POLICY=NOT_FROZEN
D34_A3_A4=BLOCKED_BY_T1
A15_ACTIVATION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_ELIGIBLE_UNDER_GLOBAL_PREFLIGHT=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
