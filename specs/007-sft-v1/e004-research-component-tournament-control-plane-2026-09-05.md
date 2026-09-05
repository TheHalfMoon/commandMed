# E004 Research-Component Tournament Control Plane — 2026-09-05

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Artifact class:** deterministic non-executing tournament control plane
**Authority effect:** NONE
**Execution effect:** NONE
**Winner-selection effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Implement the missing static contract for the already-authorized `SP007-RO-001` non-clinical backbone tournament without reviving the full clinical T1/A2 path or external human review.

The canonical successor execution decision already provides:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

This implementation supplies the deterministic protocol/evidence-pack validator required to make that authority auditable. It does not claim that an executable protocol instance or evaluation asset bundle already exists.

## 2. Exact frozen candidate boundary

The control plane admits exactly the existing E001 candidate set.

### PRIMARY

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
```

### CONTROL

```text
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

The validator rejects candidate additions, substitutions, revision drift, duplicate identities, a winner-eligible control, and a non-winner-eligible primary.

## 3. Ranking scope

Only the following non-clinical research-component metric families are eligible for ranking evidence:

```text
GENERAL_INSTRUCTION_FOLLOWING
GENERAL_ENGLISH_LANGUAGE
GENERAL_ARABIC_LANGUAGE_NON_CLINICAL
UNCERTAINTY_AND_ABSTENTION
SYNTHETIC_NON_CLINICAL_TOOL_ROUTING
GENERAL_CAPABILITY_PRESERVATION
RESOURCE_EFFICIENCY
```

The protocol requires exactly one identity-bound selection asset per ranking family.

The full clinical/population metric path is excluded from this successor tournament:

```text
emergency_miss_rate=PROHIBITED_FOR_COMPONENT_RANKING
medication_critical_error_rate=PROHIBITED_FOR_COMPONENT_RANKING
selective_risk_at_target_coverage=PROHIBITED_FOR_COMPONENT_RANKING
citation_entailment_fidelity=PROHIBITED_FOR_COMPONENT_RANKING
arabic_clinical_parity_gap=PROHIBITED_FOR_COMPONENT_RANKING
lab_report_field_extraction_accuracy=PROHIBITED_FOR_COMPONENT_RANKING
benign_case_over_triage_rate=PROHIBITED_FOR_COMPONENT_RANKING
```

This does not mark those metrics PASS. They remain outside the declared positive capability scope of `SP007-RO-001`.

## 4. Evaluation-asset fail-closed boundary

An evaluation asset cannot enter the frozen protocol unless its exact manifest records:

```text
asset_id
metric_family
source_class
source_authority_id
source_license_id
license_validation_status=PASS
content_sha256
split_id
provenance_validation_status=PASS
source_verification_status=PASS
contamination_status=PASS
quarantine_can_select_model=true
purpose=COMPONENT_TOURNAMENT_SELECTION
```

Allowed source classes are closed to:

```text
PUBLIC_UNGATED_NONCLINICAL
REPOSITORY_FROZEN_NONCLINICAL
SYNTHETIC_NONCLINICAL_EVALUATION
```

The class name alone creates no admission. Every exact asset still requires its own authority, license, hash, split, provenance, verification, contamination, and quarantine evidence.

The following source classes are explicitly rejected for component ranking:

```text
PRIVATE_GOLD
PRIVATE_GOLD_FINAL_AUDIT
PROTECTED_EVALUATION
ABORT_SENTINEL
HUMAN_REVIEW_DISPOSITION
CLINICAL_REVIEW_DISPOSITION
STATISTICAL_REVIEW_DISPOSITION
```

## 5. Sentinel boundary

The control plane binds the exact already-frozen seven-fixture subject:

```text
SENTINEL_FIXTURE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
SENTINEL_CAN_RANK=false
```

Evidence-pack validation requires the exact seven canonical guard IDs and exact fixture SHA-256 values. Any positive violation count must be `FAIL`; zero violations must be `PASS`.

Sentinels remain abort/disqualify-only. They are not optimization, recipe-tuning, hyperparameter-tuning, or ranking evidence.

## 6. Pre-result and zero-spend invariants

A valid protocol requires:

```text
candidate_result_visibility_before_freeze=false
winner_selection_performed_by_protocol=false
pre_result_freeze=true
private_gold_allowed=false
clinical_metric_ids_allowed=[]
authorized_spend_usd=0
```

An evidence pack requires:

```text
execution_authority_id=E004_SUCCESSOR_EXECUTION_DECISION_B
spend_usd=0
winner_selected=false
recommendation=NONE
```

The evidence pack therefore cannot perform E005 by construction.

## 7. Winner boundary

This control plane produces only identity-bound evidence.

```text
TOURNAMENT_PROTOCOL_SELECTS_WINNER=NO
TOURNAMENT_EVIDENCE_PACK_SELECTS_WINNER=NO
TOURNAMENT_EVIDENCE_PACK_RECOMMENDS_WINNER=NO
CONTROL_WINNER_ELIGIBLE=NO
E005_WINNER_SELECTION_REMAINS_SEPARATE=YES
```

A later E005 decision must use the then-canonical evidence and governance. No primary candidate is selected or recommended here.

## 8. Implementation

New deterministic implementation:

```text
src/commandmed/spec007/research_tournament.py
tests/spec007/test_research_tournament.py
```

The implementation composes repository canonical hashing and closed-object validation and remains offline/static.

```text
MODEL_WEIGHTS_LOADED_BY_IMPLEMENTATION=NO
MODEL_INFERENCE_EXECUTED_BY_IMPLEMENTATION=NO
BENCHMARK_PAYLOAD_EXECUTED_BY_IMPLEMENTATION=NO
DEVICE_OPENED_BY_IMPLEMENTATION=NO
NETWORK_CALLED_BY_IMPLEMENTATION=NO
TRAINING_STARTED_BY_IMPLEMENTATION=NO
WINNER_SELECTED_BY_IMPLEMENTATION=NO
```

## 9. Current live protocol state

This PR intentionally does not fabricate evaluation payload identities.

```text
LIVE_SP007_TOURNAMENT_PROTOCOL_INSTANCE=ABSENT_PENDING_EXACT_EVALUATION_ASSET_ADMISSION
LIVE_SP007_TOURNAMENT_EVALUATION_ASSET_SET=ABSENT
LIVE_SP007_TOURNAMENT_EVIDENCE_PACK=ABSENT
LIVE_SP007_TOURNAMENT_EXECUTION=NOT_PERFORMED
MODEL_WINNER_SELECTED=NO
BASE_CHECKPOINT_BINDING=ABSENT
```

The next evidence-producing repository transition after this control plane becomes canonical is to identify and admit exact non-clinical ranking assets that satisfy every manifest condition above, then freeze a real protocol instance before any candidate result is observed.

## 10. Preserved boundaries

```text
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
SAFE_FOR_PATIENT_USE=NO
CLINICALLY_VALIDATED=NO
RELEASE_READY=NO
PROJECT_FINISHED=NO
```

## 11. Qualification

Before merge, require exact-head repository verification appropriate to the changed code surface, including applicable CI/status checks, unresolved review-thread reconciliation, mergeability, branch/ruleset state, and an expected-head guarded merge.

Under FD-007, external independent repository review is optional by default unless a later exact task reintroduces it. Bot silence or service unavailability is never represented as a substantive review PASS.
