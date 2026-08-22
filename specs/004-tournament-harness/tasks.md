# Spec 004 — Tournament Harness Tasks

**Status:** `CLOSED_CANONICAL` — effective only after the dedicated closure-only PR containing this record is merged and the resulting canonical `main` is verified

> This file records the completed Spec 004 task lifecycle. Implementation qualification/review evidence is external and directly linked below. The closure state is intentionally non-self-referential: it becomes effective only after the unchanged closure PR is independently reviewed, guarded-merged, and canonical `main` is verified.

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
- material implementation-review reconciliation through R004-09;
- closure-review reconciliation through C004-03;
- Spec 005 boundary and deferred founder decisions.

## T004-09 — Regression and semantic-identity verification — COMPLETE

Final implementation exact-head evidence is complete on:

```text
EXACT_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
RUN=32603944702
JOB=97106155513
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004_TESTS=48/48 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=276/276 PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

Direct evidence:

- [GitHub Actions Run 32603944702](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702)
- [GitHub Actions Job 97106155513](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702/job/97106155513)

## T004-10 — Independent exact-head review and implementation merge — COMPLETE

Final exact implementation head:

```text
cf6158ea4193aa7db895607c6fac5a3a1442f708
```

Fresh independent review reported no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker on that exact head. Direct evidence:

- [PR #28 fresh exact-head Qodo review](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440)
- [Qodo review updated through exact `cf6158ea...`](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920)
- [Implementation PR #28](https://github.com/TheHalfMoon/commandMed/pull/28)

The guarded squash merge used the exact expected head and produced:

```text
CANONICAL_IMPLEMENTATION_MERGE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
CANONICAL_IMPLEMENTATION_TREE=7e37fa626f825ee25271e0bf21a627a2e64e49da
```

Canonical `main` was verified at that merge/tree before closure work began. Temporary carrier PR #29 was closed without merge.

## T004-11 — Dedicated canonical closure — COMPLETE ON CLOSURE MERGE

This dedicated closure-only transition records completion of the final governance task. Its `CLOSED_CANONICAL` state is effective only after this closure PR is independently reviewed, guarded-merged unchanged, and the resulting canonical `main` plus lifecycle files are verified.

Closure transition requirements:

- closure branch starts from exact canonical implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`;
- canonical implementation tree remains `7e37fa626f825ee25271e0bf21a627a2e64e49da`;
- lifecycle/governance documentation only is changed;
- final implementation evidence remains linked and unchanged;
- exact closure head receives fresh independent review with no material lifecycle/governance/authorization/integrity blocker;
- closure PR is guarded squash-merged without head drift;
- resulting canonical `main` and lifecycle files are verified.

Spec 005 remains `BLOCKED`. Spec 004 closure does not satisfy Spec 005's separate founder license/device prerequisites and does not grant explicit Spec 005 start authorization.
