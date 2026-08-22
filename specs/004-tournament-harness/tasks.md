# Spec 004 — Tournament Harness Tasks

**Status:** READY_FOR_ANALYZE

## T004-01 — Freeze manifest and result contracts

Implement tournament-specific closed vocabularies and fail-closed structural validation in `src/commandmed/tournament.py`.

Exit evidence:

- exact V1 manifest fields enforced;
- exact V1 candidate-result fields enforced;
- execution/payload surface denylist enforced recursively;
- candidate IDs unique;
- ordered comparison metric IDs unique;
- unknown execution mode/strategy/tie policy rejected.

## T004-02 — Bind canonical Specs 001–003 identities

Validate canonical artifact bundle and compute six identities:

```text
benchmarks_sha256
metrics_sha256
gold_protocols_sha256
quarantine_sha256
safety_policy_sha256
lineage_contract_sha256
```

Exit evidence:

- canonical validators invoked;
- identity mismatch blocks manifest;
- inherited canonical artifact hashes remain unchanged.

## T004-03 — Freeze comparison metric semantics

Resolve ordered comparison metrics against canonical metrics catalog.

Exit evidence:

- unknown/duplicate metrics rejected;
- hard-gate metrics rejected as comparison metrics;
- only `HIGHER_BETTER`/`LOWER_BETTER` accepted;
- metric order affects manifest identity;
- candidate order does not affect manifest identity.

## T004-04 — Qualify candidate lineage and safety

Validate each precomputed candidate envelope.

Exit evidence:

- exact manifest SHA binding;
- candidate ID membership;
- lineage `asset_id == candidate_id`;
- lineage `MODEL_OR_CHECKPOINT` + `DEVELOPMENT_EVALUATION`;
- canonical Spec 003 admission reused;
- only `ELIGIBLE` continues;
- canonical Spec 002 safety hard-gate evaluation reused;
- only overall `PASS` continues;
- parent registry flows through Spec 003.

## T004-05 — Validate comparison evidence

Require every frozen comparison metric to have valid comparable evidence.

Exit evidence:

- result status `PASS`;
- score finite numeric, bool excluded;
- evidence artifact ID resolved;
- missing/non-pass/NaN/infinity/malformed result is non-qualifying.

## T004-06 — Deterministic tournament comparison/report

Implement lexicographic comparison and deterministic report generation.

Exit evidence:

- canonical direction respected;
- no weighted average;
- exactly one best qualified fixture candidate -> `SELECTED`;
- best-vector tie -> `NO_SELECTION / TOP_TIE`;
- zero qualified -> `NO_SELECTION / NO_QUALIFIED_CANDIDATE`;
- missing declared candidate represented explicitly;
- duplicate candidate envelope fails closed;
- input candidate order does not alter result/report identity.

## T004-07 — Focused fixture tests

Add `tests/test_tournament.py` using synthetic/non-medical metadata only.

Exit evidence:

- all Spec 004 positive/negative requirements covered;
- no real benchmark/model/Gold payload in fixtures;
- no network/subprocess/provider/runtime dependency.

## T004-08 — Governance documentation

Add `docs/evaluation/tournament-harness.md` documenting:

- precomputed-results-only boundary;
- manifest/result contracts;
- safety and lineage delegation;
- comparison semantics;
- no-selection semantics;
- Spec 005 boundary and deferred founder decisions.

## T004-09 — Regression and semantic-identity verification

Run focused, inherited hard-gate, and full offline tests; confirm inherited canonical identities unchanged.

Exit evidence:

```text
PYTHON_SYNTAX=PASS
FOCUSED_SPEC004=PASS
INHERITED_HARD_GATES=PASS
FULL_OFFLINE_SUITE=PASS
INHERITED_SEMANTIC_IDENTITIES=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

## T004-10 — Independent exact-head review and closeout candidate

After implementation qualification:

- request fresh independent review of exact current PR head;
- reconcile every material authorization/comparison-integrity finding;
- invalidate predecessor qualification after every semantic repair;
- add a non-self-referential closeout candidate;
- requalify/review final closeout head;
- guarded merge only on unchanged exact head.

## T004-11 — Dedicated canonical closure

After qualified implementation merge:

- verify canonical merge SHA/tree;
- create closure-only branch from exact canonical main;
- update only Spec 004 closeout/lifecycle registry as required;
- independently review exact closure head;
- guarded merge;
- verify resulting canonical main before marking Spec 004 `CLOSED_CANONICAL`.

Spec 005 remains blocked unless its separate founder prerequisites and explicit start authorization are satisfied.