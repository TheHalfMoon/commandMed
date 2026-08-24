# Spec 001 Corrective Maintenance — Metrics V2 Evidence Roles

## Status

```text
CORRECTIVE_MAINTENANCE=A1_METRICS_V2
IMPLEMENTATION_STATE=T010_QUALIFIED_PENDING_EXACT_HEAD_REVIEW_AND_SEPARATELY_AUTHORIZED_MERGE
REAL_TOURNAMENT_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This additive maintenance record does not rewrite the historical Spec 001 closeout or reinterpret the V1 metrics catalog. It records the bounded A1 repair that introduces a separately versioned metrics V2 evidence-role contract for future explicitly bound consumers.

## Pre-repair canonical base

```text
PRE_REPAIR_CANONICAL_MAIN_SHA=19aa95bbd122f3e01421ba2618dc1efe2f088289
PRE_REPAIR_CANONICAL_MAIN_TREE=078dad59343e74169a777dd01181c8201c41645a
EXACT_REPAIR_BRANCH=fix/a1-metrics-v2
IMPLEMENTATION_HEAD_BEFORE_EVIDENCE_RECORD=d617e5077c2ed5f3dc55d5bfb05f815a36cc8a26
EXACT_REPAIR_HEAD_SHA=d617e5077c2ed5f3dc55d5bfb05f815a36cc8a26
EVIDENCE_RECORD_COMMIT=THIS_DOCUMENT_COMMIT_FOLLOWING_THE_QUALIFICATION_HEAD
```

All A1 code, data, and test files are present and verified at the exact qualification head `d617e5077c2ed5f3dc55d5bfb05f815a36cc8a26`. This evidence-record document was updated afterwards in a follow-up documentation-only commit; the full verification sequence was rerun on that resulting head and produced identical PASS results, because the only delta between the two heads is this markdown file.

## Exact authorized changed-path set

```text
data/eval/metrics-v2.json
src/commandmed/eval_contract/model.py
src/commandmed/eval_contract/validate.py
src/commandmed/eval_contract/canonical.py
src/commandmed/eval_contract/__init__.py
src/commandmed/tournament.py
tests/eval_contract/test_metrics_v2.py
tests/test_tournament_metrics_v2_identity.py
docs/evaluation/tournament-harness.md
specs/001-eval-charter/corrective-maintenance-metrics-v2.md
```

No workflow, dependency, model-runtime, benchmark-payload, Private-Gold payload, credential, PHI, or Spec 005 planning path is part of A1.

## Immutable V1 identity guarantee

```text
V1_METRICS_PATH=data/eval/metrics.json
V1_METRICS_SHA256_BEFORE=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V1_METRICS_FILE_MUTATION=PROHIBITED
CANONICAL_UPSTREAM_IDENTITIES_V1_MUTATION=PROHIBITED
V1_TOURNAMENT_SCHEMA_VERSION_1_0_BEHAVIOR_MUTATION=PROHIBITED
V1_METRICS_SHA256_AFTER_EXPECTED=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V1_METRICS_SHA256_AFTER_QUALIFICATION=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

The canonicalizer change is additive: V2 evidence-role records sort by `evidence_role`; V1 has no such record field and must retain the exact historical digest.

## Additive V2 identity

```text
V2_SCHEMA_ID=commandmed-metrics-catalog
V2_SCHEMA_VERSION=2.0
V2_CATALOG_PATH=data/eval/metrics-v2.json
V2_SUPERSEDES_V1_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V2_METRICS_SHA256=ebfdaecebd924c3ec3b897bb6c26a9860635f8cfb6757e8167b20bc488b0adaf
V2_CONSUMER_BINDING_IDENTITY=commandmed-metrics-catalog|2.0|data/eval/metrics-v2.json|ebfdaecebd924c3ec3b897bb6c26a9860635f8cfb6757e8167b20bc488b0adaf
```

V2 preserves the V1 metric ID set and non-evidence scientific fields. It replaces the V1 single `required_evidence` representation only in the V2 contract with explicit evidence-role records.

For `arabic_clinical_parity_gap`, the V2 contract requires exactly:

```text
SELECTION_DEV -> purpose=CHECKPOINT_SELECTION -> source_policy=SELECTION_SAFE_NON_GOLD
PRIVATE_GOLD_FINAL_AUDIT -> purpose=PRIVATE_GOLD -> source_policy=PRIVATE_GOLD_FAMILY
```

This representation does not bind a real selection-safe Arabic suite and does not authorize access to `COMMANDMED_ARABIC_GOLD`.

For non-Arabic metrics, A1 preserves the historical V1 evidence requirement text through a non-selection `QUALIFICATION_ONLY` role and does not automatically grant selection, Private-Gold, or public-external lifecycle authority.

## Versioned consumer behavior

```text
V1_CONSUMER_FALL_FORWARD_TO_V2=PROHIBITED
V2_CONSUMER_FALL_BACK_TO_V1=PROHIBITED
MUTABLE_LATEST_METRICS_CONTRACT=PROHIBITED
V2_SCHEMA_VERSION_MISMATCH=FAIL_CLOSED
V2_PATH_MISMATCH=FAIL_CLOSED
V2_SHA_MISMATCH=FAIL_CLOSED
CALLER_SUPPLIED_RECOMPUTED_SHA_OVERRIDES_CANONICAL_BINDING=NO
```

`src/commandmed/tournament.py` retains `CANONICAL_UPSTREAM_IDENTITIES_V1` unchanged and adds a separate `CANONICAL_METRICS_V2_BINDING` for future explicit V2 consumers.

## Qualification evidence

These fields were verified by T010 on the exact qualification head and rerun identically on the evidence-record head:

```text
FOCUSED_TEST_RESULTS=PASS (tests.eval_contract.test_metrics_v2: 11 tests OK; tests.test_tournament_metrics_v2_identity: 8 tests OK)
FOCUSED_V1_REGRESSION_RESULTS=PASS (test_canonical + test_hard_gates + test_fail_closed + test_tournament + test_tournament_contract_hardening: 82 tests OK)
FULL_OFFLINE_SUITE_RESULT=PASS (unittest discover -s tests -p "test_*.py": 295 tests OK, 0 failures, offline)
PYTHON_COMPILE_RESULT=PASS (py_compile over all A1-touched modules and tests)
V1_IDENTITY_REVERIFICATION=PASS (semantic SHA-256 of data/eval/metrics.json == 304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a; CANONICAL_UPSTREAM_IDENTITIES_V1["metrics_sha256"] unchanged)
V2_IDENTITY_REVERIFICATION=PASS (schema_id/schema_version/supersedes exact; semantic SHA-256 of data/eval/metrics-v2.json == ebfdaecebd924c3ec3b897bb6c26a9860635f8cfb6757e8167b20bc488b0adaf; CANONICAL_METRICS_V2_BINDING matches exactly)
EXACT_CHANGED_PATH_GATE=PASS (git diff --name-status against authorized base shows exactly the ten authorized paths; UNAUTHORIZED_PATH_COUNT=0)
NEGATIVE_CASE_COVERAGE=PASS (V1 fall-forward rejected; V2 fallback rejected; V2 SHA/path/schema-version mismatch rejected; unknown role/purpose/binding/source-policy rejected; duplicate role rejected; missing Arabic role rejected; role reordering digest-stable; role semantic mutation changes digest — covered by focused V2 suites)
GITHUB_ACTIONS_RUN=NO_GITHUB_ACTIONS_WORKFLOW_PRESENT_ON_BRANCH
STATUS_CHECK_DISPOSITION=NO_CI_RUN_EXISTS_NO_PASS_CLAIMED
INDEPENDENT_EXACT_HEAD_REVIEW_DISPOSITION=PENDING_EXTERNAL_INDEPENDENT_REVIEW
DRAFT_TO_READY_GATE=PENDING_SEPARATE_AUTHORITY
GUARDED_MERGE_RESULT=NOT_PERFORMED
POST_MERGE_CANONICAL_MAIN_SHA=PENDING_IF_MERGE_AUTHORIZED_AND_COMPLETED
POST_MERGE_CANONICAL_MAIN_TREE=PENDING_IF_MERGE_AUTHORIZED_AND_COMPLETED
```

No `PASS`, independent-review success, CI success, or merge success is claimed by this record before the corresponding evidence exists.

## T010 stop rule

A1 is not canonical merely because these files exist on a branch. Before Spec 005 T011 may start, T010 must prove focused and full offline regression, exact V1/V2 identities, exact authorized path scope, exact-head independent review with no material blocker, an authorized guarded merge, and post-merge canonical `main` SHA/tree plus V1/V2 identity reverification.

If any of those gates is unavailable or fails, implementation stops before T011 rather than using an unmerged local A1 substitute.
