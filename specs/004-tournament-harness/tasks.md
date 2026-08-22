# Spec 004 — Tournament Harness Tasks

**Status:** IMPLEMENTATION_COMPLETE_EXTERNAL_FINAL_GATES_REQUIRED

> Exact-head qualification and independent review are external evidence produced only after repository content freezes. This file intentionally does not self-attest the final head/run/review that contains it; doing so would mutate the head and invalidate that evidence.

## T004-01 — Freeze manifest and result contracts — COMPLETE

Tournament-specific closed vocabularies and fail-closed structural validation are implemented in `src/commandmed/tournament.py`.

Exit evidence:

- exact V1 manifest fields enforced;
- exact V1 candidate-result fields enforced;
- execution/payload surface denylist enforced recursively, including separator/whitespace hardening;
- mixed string/non-string object keys fail closed instead of raising during closed-shape validation;
- non-object manifests are invalid and do not receive a tournament-manifest identity;
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
- report digest binds lexicographic comparison-vector order;
- invalid manifest shapes cannot carry a misleading tournament-manifest digest.

## T004-07 — Focused fixture tests — COMPLETE

Focused synthetic/non-medical regression coverage exists in:

```text
tests/test_tournament.py
tests/test_tournament_contract_hardening.py
tests/test_tournament_review_hardening.py
```

Coverage includes the final-review boundaries for:

- malformed/non-list candidate-result sets;
- mixed-type manifest and candidate object keys;
- wholly non-object string/list/`None` manifests producing `INVALID_MANIFEST_OR_PROTOCOL` with `tournament_manifest_sha256=None`;
- prohibited-key separator normalization;
- comparison-vector hash-order binding;
- arbitrarily large integer comparison and final report hashing.

No real benchmark/model/Gold payload, network, subprocess, provider, or runtime dependency is used.

## T004-08 — Governance documentation — COMPLETE

`docs/evaluation/tournament-harness.md` and the bounded Spec 004 lifecycle documents record:

- precomputed-results-only boundary;
- manifest/result contracts;
- safety and lineage delegation;
- comparison semantics;
- no-selection semantics;
- deterministic identity rules;
- material review reconciliation through R004-09;
- Spec 005 boundary and deferred founder decisions.

## T004-09 — Regression and semantic-identity verification — EXTERNAL EXACT-HEAD GATE

Repository implementation work is complete. After this content is frozen, one unchanged exact head must externally prove:

```text
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004=PASS
INHERITED_HARD_GATES=PASS
FULL_OFFLINE_SUITE=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

The authoritative run/job/head belongs in PR/carrier evidence, not by mutating this file after the run.

## T004-10 — Independent exact-head review and closeout candidate — EXTERNAL GATES IN PROGRESS

Completed in repository content:

- material implementation/review findings through R004-09 reconciled;
- predecessor qualification invalidated after every semantic repair;
- non-self-referential implementation closeout candidate exists at `specs/004-tournament-harness/closeout.md`;
- stale task bookkeeping identified during prior final review reconciled;
- predecessor independent reviews retained only as historical context.

External gates remaining after this content freezes:

- exact-head qualification required by T004-09;
- fresh independent review of that exact unchanged head with no material blocker;
- guarded squash merge PR #28 only if canonical `main`, exact PR head, qualification, and review remain unchanged.

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
