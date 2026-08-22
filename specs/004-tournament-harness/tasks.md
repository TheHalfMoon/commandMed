# Spec 004 — Tournament Harness Tasks

**Status:** IMPLEMENTATION_COMPLETE_AWAITING_FINAL_CLOSEOUT_QUALIFICATION

## T004-01 — Freeze manifest and result contracts — COMPLETE

Tournament-specific closed vocabularies and fail-closed structural validation are implemented in `src/commandmed/tournament.py`.

Exit evidence:

- exact V1 manifest fields enforced;
- exact V1 candidate-result fields enforced;
- execution/payload surface denylist enforced recursively, including separator/whitespace hardening;
- candidate IDs unique;
- ordered comparison metric IDs unique;
- unknown execution mode/strategy/tie policy rejected.

## T004-02 — Bind canonical Specs 001–003 identities — COMPLETE

Canonical artifact bundle validation and exact six-identity pinning are implemented:

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
- supplied artifacts and manifest declaration must both equal the exact V1 canonical identity map;
- inherited canonical artifact hashes remain unchanged.

## T004-03 — Freeze comparison metric semantics — COMPLETE

Exit evidence:

- unknown/duplicate metrics rejected;
- hard-gate metrics rejected as comparison metrics;
- only `HIGHER_BETTER`/`LOWER_BETTER` accepted;
- metric order affects manifest identity;
- candidate order does not affect manifest identity.

## T004-04 — Qualify candidate lineage and safety — COMPLETE

Exit evidence:

- exact manifest SHA binding;
- candidate ID membership;
- lineage `asset_id == candidate_id`;
- lineage `MODEL_OR_CHECKPOINT` + `DEVELOPMENT_EVALUATION`;
- canonical Spec 003 admission reused;
- only `ELIGIBLE` continues;
- canonical Spec 002 safety hard-gate evaluation reused;
- observed safety `FAIL` is decisively disqualified while insufficient/blocked/not-evaluated evidence remains incomplete;
- parent registry flows through Spec 003.

## T004-05 — Validate comparison evidence — COMPLETE

Exit evidence:

- comparison result status `PASS`;
- score finite numeric, bool excluded;
- arbitrarily large integers handled exactly without float or decimal-string overflow;
- evidence artifact ID resolved;
- missing/non-pass/NaN/infinity/malformed result is `INCOMPLETE` and cannot be ranked.

## T004-06 — Deterministic tournament comparison/report — COMPLETE

Exit evidence:

- canonical metric direction respected;
- no weighted average;
- exactly one best qualified fixture candidate -> `SELECTED`;
- best-vector tie -> `NO_SELECTION / TOP_TIE`;
- zero qualified -> `NO_SELECTION / NO_QUALIFIED_CANDIDATE`;
- any declared incomplete candidate -> `NO_SELECTION / CANDIDATE_EVIDENCE_INCOMPLETE` before ranking;
- missing declared candidate represented explicitly;
- duplicate or undeclared candidate envelope fails closed;
- input candidate order does not alter result/report identity;
- report carries exact canonical artifact identities;
- report digest binds lexicographic comparison-vector order.

## T004-07 — Focused fixture tests — COMPLETE

Focused synthetic/non-medical regression coverage exists in:

```text
tests/test_tournament.py
tests/test_tournament_contract_hardening.py
tests/test_tournament_review_hardening.py
```

Latest predecessor exact-head qualification at `7a04d40030a2aa28b4c2f0d5db6e4d387388c756`:

```text
RUN=32601812794
JOB=97101112661
FOCUSED_SPEC004_TESTS=45/45 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=273/273 PASS
```

No real benchmark/model/Gold payload, network, subprocess, provider, or runtime dependency is used.

## T004-08 — Governance documentation — COMPLETE

`docs/evaluation/tournament-harness.md` and the bounded Spec 004 lifecycle documents record:

- precomputed-results-only boundary;
- manifest/result contracts;
- safety and lineage delegation;
- comparison semantics;
- no-selection semantics;
- deterministic identity rules;
- material review reconciliation;
- Spec 005 boundary and deferred founder decisions.

## T004-09 — Regression and semantic-identity verification — COMPLETE FOR PRE-CLOSEOUT HEAD

Pre-closeout exact-head evidence at `7a04d40030a2aa28b4c2f0d5db6e4d387388c756`:

```text
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004=45/45 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=273/273 PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

A final closeout content mutation still requires a new exact-head run and may not reuse this predecessor PASS as final merge evidence.

## T004-10 — Independent exact-head review and closeout candidate — IN PROGRESS

Completed before closeout mutation:

- all material implementation/review findings reconciled;
- predecessor qualification invalidated after every semantic repair;
- exact predecessor `7a04d40030a2aa28b4c2f0d5db6e4d387388c756` received CodeRabbit review Run `5effe806-c304-44a6-a910-95a604c56933` with no actionable comments and Minimal merge risk;
- malformed candidate-result coverage requested by the prior review is now direct and exact-head green.

Remaining:

- add non-self-referential implementation closeout candidate;
- requalify exact final closeout head;
- fresh independent review of exact final head;
- guarded squash merge only if the head remains unchanged.

## T004-11 — Dedicated canonical closure — BLOCKED ON IMPLEMENTATION MERGE

After qualified implementation merge only:

- verify canonical implementation merge SHA/tree;
- create closure-only branch from exact canonical main;
- bind implementation merge SHA/tree in Spec 004 closeout;
- update lifecycle registry only as required;
- independently review exact closure head;
- guarded squash merge closure PR;
- verify resulting canonical main before marking Spec 004 `CLOSED_CANONICAL`.

Spec 005 remains blocked unless its separate founder prerequisites and explicit start authorization are satisfied.
