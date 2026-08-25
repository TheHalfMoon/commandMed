# Spec 005 — Session 8 Q2 Canonical Metric-Repair Governance

**Lifecycle:** CLARIFY ONLY  
**Accepted question:** Session 8 — Q2  
**Exact predecessor head:** `2cf690fe9a638a4ee7dd1555bd75f83b68383307`  
**Canonical metadata base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`  
**Purpose:** freeze how the Session 8 Q1 canonical metric-identity gap may be repaired without allowing Spec 005 or PR #34 to mutate closed upstream contracts implicitly, without erasing historical Spec 004 identity semantics, and without granting any execution or payload authority.

> This artifact is documentation/governance only. It does not perform or authorize the corrective-maintenance repair itself. It does not modify `data/eval/metrics.json`, Spec 001 source/tests, Spec 004 source/tests, any canonical identity constant, benchmark metadata, safety semantics, quarantine semantics, lineage semantics, model/weight assets, or benchmark payloads. It does not authorize `PLAN`, Ready, merge, model access, benchmark access, contamination-assessment access, model execution, device execution, provider generation, training, or tournament execution.

## 1. Canonical basis

Session 8 Q1 established a real dependency gap:

- MedXpertQA `Text/dev.jsonl` is currently the only exact slice whose canonical split semantics support `CHECKPOINT_SELECTION`;
- the official upstream MedXpertQA evaluator reports **accuracy**;
- canonical Spec 001 has no MedXpertQA-compatible or generic medical-MCQ accuracy metric identity;
- the existing `medqa_usmle_accuracy` identity is explicitly MedQA USMLE specific and cannot be widened to MedXpertQA;
- therefore the exact primary-selection manifest remains blocked.

Canonical Spec 001 is `CLOSED_CANONICAL`, but its authority boundary explicitly preserves one post-close exception: **separately reviewed corrective maintenance**.

Canonical Spec 004 is also `CLOSED_CANONICAL`. It explicitly prohibits changing canonical evaluation contracts merely to make a fixture pass, while allowing a separately justified defect to require corrective maintenance. Spec 004 also binds the metric catalog by exact semantic SHA-256 through `CANONICAL_UPSTREAM_IDENTITIES_V1` and requires supplied canonical artifacts to match the authorized identity map.

Therefore a canonical metric repair cannot be smuggled into PR #34 and cannot land as an isolated `metrics.json` edit that leaves the tournament harness bound to an incompatible historical identity.

## 2. Accepted policy

`SEPARATE_VERSIONED_ATOMIC_CORRECTIVE_MAINTENANCE_BEFORE_SPEC005_CONSUMPTION` is frozen:

```text
METRIC_REPAIR_GOVERNANCE_POLICY=
SEPARATE_VERSIONED_ATOMIC_CORRECTIVE_MAINTENANCE_BEFORE_SPEC005_CONSUMPTION

DISCOVERED_GAP=
NO_CANONICAL_COMPATIBLE_MEDXPERTQA_ACCURACY_METRIC_ID
DISCOVERED_GAP_CLASS=CORRECTIVE_MAINTENANCE_CANDIDATE
Q2_DECLARES_CORRECTIVE_MAINTENANCE_IMPLEMENTED=NO
Q2_AUTHORIZES_CORRECTIVE_MAINTENANCE_MUTATION=NO

PR34_MAY_EDIT_SPEC001_METRIC_CATALOG=NO
PR34_MAY_EDIT_SPEC004_CANONICAL_IDENTITY_BINDING=NO
PR34_MAY_REDEFINE_EXISTING_METRIC_SEMANTICS=NO

CORRECTIVE_MAINTENANCE_REQUIRES_SEPARATE_EXPLICIT_AUTHORIZATION=YES
CORRECTIVE_MAINTENANCE_REQUIRES_SEPARATE_BRANCH=YES
CORRECTIVE_MAINTENANCE_REQUIRES_SEPARATE_PR=YES
CORRECTIVE_MAINTENANCE_BASE_MUST_BE_LIVE_CANONICAL_MAIN=YES
CORRECTIVE_MAINTENANCE_SCOPE_MUST_BE_PREDECLARED=YES
CORRECTIVE_MAINTENANCE_MUST_BE_INDEPENDENTLY_EXACT_HEAD_REVIEWED=YES
CORRECTIVE_MAINTENANCE_MUST_BE_EXACT_HEAD_QUALIFIED=YES
CORRECTIVE_MAINTENANCE_MUST_BE_GUARDED_MERGED=YES
CANONICAL_MAIN_MUST_BE_REVERIFIED_AFTER_REPAIR_MERGE=YES

EXISTING_MEDQA_USMLE_ACCURACY_IDENTITY_PRESERVED=YES
EXISTING_MEDQA_USMLE_ACCURACY_RENAME=PROHIBITED
EXISTING_MEDQA_USMLE_ACCURACY_WIDEN_TO_MEDXPERTQA=PROHIBITED

NEW_COMPATIBLE_METRIC_ID=UNRESOLVED_UNTIL_SEPARATE_MAINTENANCE
NEW_COMPATIBLE_METRIC_SCOPE=UNRESOLVED_UNTIL_SEPARATE_MAINTENANCE
NEW_COMPATIBLE_METRIC_MUST_PRESERVE_UPSTREAM_ACCURACY_SEMANTICS=YES
BENCHMARK_SPECIFIC_VS_GENERIC_METRIC_SCOPE_MUST_BE_EXPLICIT=YES
METRIC_DIRECTION_AND_UNIT_MUST_BE_EXPLICIT=YES
METRIC_REQUIRED_EVIDENCE_MUST_BE_EXPLICIT=YES
METRIC_HARD_GATE_ROLE_MUST_BE_EXPLICIT=YES
Q2_RECLASSIFIES_ANY_EXISTING_SAFETY_HARD_GATE=NO
Q2_CHANGES_ANY_EXISTING_SAFETY_THRESHOLD=NO

CURRENT_CANONICAL_METRICS_SHA256=
304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
REPAIRED_CANONICAL_METRICS_SHA256=UNRESOLVED_UNTIL_REPAIR

HISTORICAL_SPEC004_V1_IDENTITY_SEMANTICS_MUST_REMAIN_REPRODUCIBLE=YES
IN_PLACE_REINTERPRETATION_OF_HISTORICAL_V1_IDENTITY=PROHIBITED
HISTORICAL_CLOSEOUT_EVIDENCE_REWRITE=PROHIBITED

REPAIR_MUST_RECONCILE_ALL_PINNED_CURRENT_CONSUMERS_ATOMICALLY=YES
CANONICAL_MAIN_WITH_NEW_METRICS_AND_INCOMPATIBLE_CURRENT_HARNESS_BINDING=PROHIBITED
VERSIONED_CURRENT_IDENTITY_BINDING_REQUIRED_IF_METRIC_IDENTITY_CHANGES=YES
EXACT_VERSIONING_MECHANISM=UNRESOLVED_UNTIL_SEPARATE_MAINTENANCE

NON_METRICS_CANONICAL_IDENTITY_CHANGES_REQUIRE_SEPARATE_JUSTIFICATION=YES
UNRELATED_CANONICAL_CONTRACT_CHANGES=PROHIBITED

PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
PRIMARY_SELECTION_METRIC_MAPPING=UNRESOLVED_CANONICAL_METRIC_IDENTITY_GAP
```

## 3. Why the repair must be separate from PR #34

PR #34 is a Spec 005 clarification carrier. It is not the canonical authority that originally defined the metric catalog.

Allowing PR #34 to add or reinterpret a metric would create several governance failures:

1. a downstream consumer would silently rewrite its upstream evaluation contract;
2. the new metric could be selected because it helps the current tournament design rather than because its semantics were independently reviewed;
3. the canonical metric digest would change without a dedicated repair record;
4. Spec 004's exact protocol identity binding could become stale or be rewritten without explicit review;
5. historical V1 tournament evidence could lose reproducibility if the meaning of the V1 identity map were changed in place.

The metric gap is therefore a dependency repair, not an ordinary Spec 005 clarification edit.

## 4. Atomic cross-spec reconciliation requirement

A future separately authorized corrective-maintenance PR must leave canonical `main` internally coherent at the merge commit.

At minimum, if the metric catalog semantic identity changes, the repair must account for every current canonical consumer that requires the old metric identity. The known critical consumer is the Spec 004 tournament harness, whose current source contains:

```text
CANONICAL_UPSTREAM_IDENTITIES_V1.metrics_sha256=
304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

and whose validation fails closed when supplied canonical artifacts do not match its authorized identity map.

Q2 does **not** prescribe the exact implementation of the version transition. The repair may require a new versioned identity map, manifest/protocol version semantics, or another independently reviewed mechanism. What is frozen is the invariant:

```text
OLD_V1_EVIDENCE_REMAINS_INTERPRETABLE_UNDER_OLD_V1_IDENTITY=YES
NEW_CANONICAL_METRIC_CATALOG_HAS_AN_EXPLICIT_CURRENT_IDENTITY_BINDING=YES
NO_CANONICAL_COMMIT_MAY_SILENTLY_MAP_OLD_V1_NAME_TO_NEW_SEMANTICS=YES
```

A repair that merely replaces the old V1 `metrics_sha256` literal with a new value without preserving historical identity semantics is not sufficient under this Q2 policy.

## 5. Minimum corrective-maintenance evidence

The exact changed-file set is not frozen by Q2 because the versioning mechanism remains unresolved. Before mutation, the future repair must predeclare its bounded path set and justify every path.

Its evidence package must establish at least:

```text
LIVE_CANONICAL_BASE=VERIFIED
METRIC_GAP_JUSTIFICATION=DOCUMENTED
NEW_OR_REPAIRED_METRIC_SEMANTICS=EXACTLY_DEFINED
UPSTREAM_SCORE_SEMANTICS_BINDING=DOCUMENTED
EXISTING_MEDQA_METRIC_SEMANTICS=UNCHANGED
EXISTING_SAFETY_HARD_GATE_SEMANTICS=UNCHANGED
NEW_METRICS_SHA256=RECORDED
OTHER_CANONICAL_SHA256_IDENTITIES=RECORDED_AND_EXPLAINED
SPEC004_CURRENT_IDENTITY_BINDING=RECONCILED
HISTORICAL_V1_REPRODUCIBILITY=PROVEN
METRICS_CATALOG_VALIDATION=PASS
FOCUSED_SPEC001_EVALUATION_TESTS=PASS
FOCUSED_SPEC004_IDENTITY_AND_MANIFEST_TESTS=PASS
INHERITED_HARD_GATE_TESTS=PASS
FULL_OFFLINE_SUITE=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
INDEPENDENT_EXACT_HEAD_REVIEW=NO_MATERIAL_BLOCKER
```

This is a governance requirement for a future repair; Q2 does not claim any of these tests have run for a repair that does not yet exist.

## 6. Historical evidence rule

Existing Spec 001 and Spec 004 implementation/closure records are historical evidence and must not be rewritten to pretend the repaired metric existed at their original reviewed heads.

A future maintenance change must create new, additive maintenance evidence that binds:

- the pre-repair canonical main SHA;
- the exact repair head;
- old metric semantic identity;
- new metric semantic identity;
- the version transition mechanism;
- validation/review evidence;
- resulting canonical repair merge SHA/tree after merge.

Historical closeout SHAs, historical run results, and historical V1 semantic identities remain historical facts.

## 7. Spec 005 consumption gate after a future repair

Even after a corrective-maintenance PR is independently reviewed and merged, Spec 005 may not automatically consume the new metric.

Required sequence:

```text
1. SEPARATE_REPAIR_AUTHORIZED
2. REPAIR_IMPLEMENTED_ON_LIVE_CANONICAL_BASE
3. REPAIR_EXACT_HEAD_QUALIFIED
4. REPAIR_INDEPENDENTLY_EXACT_HEAD_REVIEWED
5. REPAIR_GUARDED_MERGED
6. RESULTING_CANONICAL_MAIN_REVERIFIED
7. PR34_RECONCILED_TO_NEW_CANONICAL_MAIN_WITHOUT_REBASE_OR_FORCE_PUSH_IF_NEEDED
8. FRESH_SPEC005_CLARIFICATION_BINDS_THE_NEW_CANONICAL_METRIC_ID
9. FRESH_EXACT_HEAD_QUALIFICATION
```

Q2 does not authorize steps 1–9 beyond recording this dependency order.

PR #34 must not duplicate the repair changes. If canonical `main` advances because of a future repair, PR #34 must preserve history; force-push and rebase remain prohibited. Any necessary branch reconciliation must be non-destructive and followed by fresh exact-head qualification.

## 8. What metric repair does not solve

A future canonical metric repair would resolve only the metric-identity dependency if all its gates pass. It would **not** by itself resolve:

- whether MedXpertQA `Text/dev.jsonl` is statistically adequate as the sole primary quality-floor evidence;
- the minimum medical-quality threshold;
- MedXpertQA's current `NOT_ASSESSED` contamination evidence;
- contamination-assessment payload access authority;
- benchmark payload access or execution authority;
- HealthBench purpose mapping;
- PubMedQA purpose mapping;
- candidate admission/rights/license completeness;
- model-weight access;
- model execution;
- tournament execution;
- final primary-selection manifest freeze.

Therefore:

```text
METRIC_REPAIR_CAN_UNBLOCK_METRIC_IDENTITY_DEPENDENCY_ONLY=YES
METRIC_REPAIR_ALONE_FREEZES_PRIMARY_MANIFEST=NO
METRIC_REPAIR_ALONE_GRANTS_SELECTION_ELIGIBILITY=NO
METRIC_REPAIR_ALONE_GRANTS_PAYLOAD_ACCESS=NO
METRIC_REPAIR_ALONE_GRANTS_EXECUTION=NO
```

## 9. Authority boundary

```text
CURRENT_AUTHORIZED_SPEND_USD=0

PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CORRECTIVE_MAINTENANCE_IMPLEMENTATION_AUTHORITY=NONE
```

## 10. Session 8 progress

Acceptance of Q2 advances only bounded Session 8:

```text
CLARIFICATION_SESSION_8=2_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_8_STATUS=IN_PROGRESS

METRIC_REPAIR_GOVERNANCE_POLICY=
SEPARATE_VERSIONED_ATOMIC_CORRECTIVE_MAINTENANCE_BEFORE_SPEC005_CONSUMPTION

PRIMARY_SELECTION_MANIFEST_FREEZE_STATUS=BLOCKED
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN

CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
```

This Q2 does not complete Session 8, does not complete the overall CLARIFY lifecycle, and does not authorize transition to `PLAN`.

## Remaining clarification scope

Remaining work includes whether/when to separately authorize the corrective-maintenance implementation; exact new metric identity and version-transition mechanism; statistical adequacy and minimum medical-quality threshold; any contamination-assessment-only payload access route; actual candidate-specific contamination evidence; HealthBench/PubMedQA purpose binding if supportable; exact component rights/privacy/license evidence; exact llama.cpp/build/tokenizer/instrumentation identities; numeric performance values; thermal/energy/failure-signal details; secondary ranking order; exact-head independent review; and final clarification lifecycle closure.
