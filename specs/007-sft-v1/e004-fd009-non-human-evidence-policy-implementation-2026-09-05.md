# E004 FD-009 Non-Human T1/A2 Evidence-Policy Implementation — 2026-09-05

**Spec:** 007 SFT V1  
**Depends on:** `docs/t1-a2-human-review-gate-amendment-2026-09-05.md`  
**Policy ID:** `FD009_T1_A2_NON_HUMAN_EVIDENCE_POLICY_V1`  
**Implementation effect:** repository-only validation control plane  
**Numeric threshold freeze created:** NO  
**T1/A2 PASS created:** NO  
**External reviewer outreach:** NO  
**Current authorized spend:** USD 0

## Purpose

Implement the minimum fail-closed compatibility layer required by FD-009 without rewriting historical Spec 005 records or weakening the existing scientific readiness validator.

The existing structural fields named `clinical_review_authority_reference` and `statistical_review_authority_reference` remain in the legacy `ThresholdPolicy` shape for backward structural compatibility. Under the FD-009 entrypoint they are no longer interpreted as human reviewer identities. They must equal exact non-human policy authority identities.

```text
FD009_POLICY_ID=FD009_T1_A2_NON_HUMAN_EVIDENCE_POLICY_V1
FD009_CLINICAL_POLICY_AUTHORITY=FD009_T1_A2_CLINICAL_MEANINGFULNESS_EVIDENCE_POLICY_V1
FD009_STATISTICAL_POLICY_AUTHORITY=FD009_T1_A2_STATISTICAL_EVIDENCE_POLICY_V1
EXTERNAL_HUMAN_REVIEWER_IDENTITY_REQUIRED=NO
ARBITRARY_REVIEWER_LIKE_STRING_ACCEPTED_BY_FD009_ENTRYPOINT=NO
```

## Canonical implementation surface

```text
IMPLEMENTATION=src/commandmed/spec005/fd009.py
THRESHOLD_VALIDATOR=validate_fd009_threshold_policy
READINESS_EVALUATOR=evaluate_fd009_scientific_selection_readiness
TESTS=tests/spec005/test_fd009_science.py
```

The FD-009 threshold validator composes the existing `validate_threshold_policy()` rather than replacing it. Therefore all existing structural gates remain active, including metric/lane/role validity, exact threshold/margin presence, pre-result freeze, and canonical SHA validation.

FD-009 adds the following mandatory gates:

```text
CLINICAL_MEANINGFULNESS_EVIDENCE_IDS=NONEMPTY_STRING_LIST_REQUIRED
STATISTICAL_JUSTIFICATION_EVIDENCE_IDS=NONEMPTY_STRING_LIST_REQUIRED
CLINICAL_POLICY_AUTHORITY=EXACT_FD009_ID_REQUIRED
STATISTICAL_POLICY_AUTHORITY=EXACT_FD009_ID_REQUIRED
```

The global FD-009 readiness evaluator composes `evaluate_scientific_selection_readiness()` and adds the exact policy checks for every threshold record. Existing noncompensable lane coverage, A3+A4 design, candidate-neutrality, pairing, allocation, N, threshold-design binding, and other readiness gates remain unchanged.

## Fail-closed properties

```text
MISSING_THRESHOLD_VALUE_OR_MARGIN=BLOCK
EMPTY_CLINICAL_EVIDENCE_IDS=BLOCK
EMPTY_STATISTICAL_EVIDENCE_IDS=BLOCK
LEGACY_REVIEWER_PLACEHOLDER_AS_POLICY_AUTHORITY=BLOCK
POST_RESULT_FREEZE_FALSE=BLOCK
BASE_SCIENTIFIC_READINESS_FAILURE=BLOCK
FD009_POLICY_FAILURE=BLOCK
```

No test fixture value is a commandMed scientific recommendation. Synthetic values exercise only validator structure.

## Current frontier after implementation

Even after this implementation is qualified and merged:

```text
T1_A2_HUMAN_REVIEW_BLOCKER=REMOVED_BY_FD009
T1_A2_NON_HUMAN_EVIDENCE_POLICY_IMPLEMENTATION=CANONICAL_AFTER_QUALIFIED_MERGE
T1_A2_NUMERIC_THRESHOLD_MARGIN_POLICY=NOT_YET_FROZEN
T1_A2=INCOMPLETE_PENDING_EXACT_EVIDENCE_BOUND_NUMERIC_POLICY
D34_A3_A4=BLOCKED_BY_T1
A15_ACTIVATION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_ELIGIBLE_UNDER_GLOBAL_PREFLIGHT=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next scientific task is to construct exact metric-specific evidence-bound threshold/margin policy records using source evidence and deterministic derivation rules. No numeric value may be invented merely to make readiness pass.
