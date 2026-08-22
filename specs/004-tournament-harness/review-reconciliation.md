# Spec 004 — Tournament Harness Review Reconciliation

**Status:** `CLOSED_CANONICAL` — effective only after the dedicated closure-only PR containing this record is merged and resulting canonical `main` is verified  
**Canonical implementation base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`  
**Canonical implementation merge:** `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`  
**Canonical implementation tree:** `7e37fa626f825ee25271e0bf21a627a2e64e49da`  
**Final reviewed implementation head:** `cf6158ea4193aa7db895607c6fac5a3a1442f708`  
**Scope:** fixture/precomputed-results-only harness  
**Authority:** no model, weight, benchmark-payload, provider/API, training, PHI/restricted-data, private-Gold payload, gated-asset, or Spec 005 execution authority

## Reconciliation rule

A green predecessor is never reusable as final qualification after a later material defect or semantic repair is discovered. Every repository-content repair creates a new candidate head requiring new exact-head validation and fresh independent review.

This file preserves the material implementation-review history and separately records the dedicated closure-review reconciliation. Earlier present-tense implementation gates are historical once the canonical implementation merge exists.

## Implementation findings — all repaired before canonical implementation merge

### V004-01 — Canonical quarantine container adapter

**Discovered by:** GitHub exact-head carrier Run `32600079522`  
**Affected predecessor:** `19cd7697b6f399af50f9006b7235b3421eb8cc0a`  
**Severity:** MATERIAL / INTEGRATION  
**Status:** REPAIRED

The canonical quarantine artifact is a container with `quarantine_rules` and `contamination_records`. The repair validates each collection with its canonical validator while retaining semantic SHA-256 over the complete canonical container.

### S004-01 — Caller-supplied alternate protocol bundle

**Discovered by:** analyze self-audit  
**Severity:** MATERIAL / PROTOCOL INTEGRITY  
**Status:** REPAIRED

Internal consistency was insufficient canonical authority. The harness now hard-pins the exact six Specs 001–003 identities; both recomputed supplied-artifact identities and manifest declarations must equal that immutable map.

### S004-02 — Incomplete candidate subset-selection bypass

**Discovered by:** analyze self-audit  
**Severity:** MATERIAL / COMPARISON INTEGRITY  
**Status:** REPAIRED

Candidate states are exactly `QUALIFIED`, `DISQUALIFIED`, and `INCOMPLETE`. Only complete decisive evidence may disqualify. Missing/malformed/wrong-manifest/blocked/insufficient/non-comparable evidence is incomplete. Any declared incomplete candidate forces `NO_SELECTION / CANDIDATE_EVIDENCE_INCOMPLETE` before ranking. Unknown or duplicate candidate envelopes invalidate the result set.

### R004-01 — FR-006 candidate schema conflict

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`  
**Severity:** MATERIAL / CONTRACT CONSISTENCY  
**Status:** REPAIRED

Safety scope exists once in the frozen manifest. Each candidate carries the exact manifest digest that binds it to that scope. Duplicate candidate-level safety scope is prohibited.

### R004-02 — Plan retained obsolete `NON_QUALIFYING` flow

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`  
**Severity:** MATERIAL / COMPARISON INTEGRITY  
**Status:** REPAIRED

The plan now uses `QUALIFIED / DISQUALIFIED / INCOMPLETE`; incomplete-candidate gating occurs before ranking.

### R004-03 — Report omitted canonical artifact identities

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`  
**Severity:** MATERIAL / REPORT INTEGRITY  
**Status:** REPAIRED

Every report carries `canonical_artifact_identities == CANONICAL_UPSTREAM_IDENTITIES_V1`, and the map participates in the non-self-referential report digest.

### S004-03 — Invalid result-set report identity depended on input order

**Discovered by:** post-qualification self-audit  
**Affected predecessor:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`  
**Severity:** MATERIAL / DETERMINISTIC IDENTITY  
**Status:** REPAIRED

Result-set errors no longer embed caller list indexes; recursive denylist list paths are order-neutral; report error collections are sorted before hashing; regressions prove permutation invariance.

### R004-04 — Large integer comparison overflow

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`  
**Severity:** MATERIAL / STABILITY  
**Status:** REPAIRED IN TWO LAYERS

`math.isfinite()` is applied only to floats; integers remain exact. A later exact-head run exposed Python 3.11's decimal integer-string limit during report hashing, leading to V004-02.

### V004-02 — Large integer report-hash decimal conversion limit

**Discovered by:** GitHub exact-head carrier Run `32600855451`  
**Affected predecessor:** `a8e3c197cd7320539b096821266bba7c36902c27`  
**Severity:** MATERIAL / STABILITY + DETERMINISTIC IDENTITY  
**Status:** REPAIRED

The returned scientific report retains the original integer. The report-hash projection maps integers to an exact tagged hexadecimal representation before canonical JSON serialization. Booleans remain booleans; no process-global integer-digit setting is modified.

### R004-05 — Recursive denylist separator/whitespace bypass

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`  
**Reviewer:** Qodo  
**Severity:** MATERIAL / SECURITY  
**Status:** REPAIRED

Key names are normalized through Unicode NFKC + casefold; non-ASCII-alphanumeric separator sequences collapse to `_`; both normalized and underscore-free compact forms are compared against the prohibited vocabulary. Regressions reject `api\tkey`, `api\u200bkey`, and `provider.endpoint`.

### R004-06 — Report digest did not bind comparison-vector order

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`  
**Reviewer:** Qodo  
**Severity:** MATERIAL / SCIENTIFIC IDENTITY  
**Status:** REPAIRED

The public report remains unchanged. In the report-hash projection each comparison-vector record becomes the ordered positional sequence `[metric_id, direction, score, evidence_artifact_id]`, preventing inherited set-like dictionary-list normalization from erasing lexicographic order.

### R004-07 — Bounded spec lacked explicit template exit headings

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`  
**Reviewer:** Qodo  
**Severity:** GOVERNANCE / AUDITABILITY  
**Status:** REPAIRED

The bounded spec now has explicit `## Exclusions` and `## Exit Evidence` sections while preserving the rule that implementation merge alone does not close Spec 004.

### R004-08 — Mixed object-key types could abort fail-closed evaluation

**Independent review head:** `6c1a359f969222dd7868248d1ba12fc114f413d9`  
**Reviewer:** Qodo  
**Severity:** MATERIAL / RELIABILITY + FAIL-CLOSED INPUT HANDLING  
**Status:** REPAIRED

`_exact_keys()` isolates string keys before set arithmetic/sorting and deterministically reports non-string object keys. `_base_report()` avoids hashing malformed mixed-key manifests before validation. Regressions drive mixed-key manifests and candidate envelopes through `evaluate_tournament()` and require deterministic no-selection/incomplete outcomes rather than exceptions.

### G004-01 — Closeout task bookkeeping stale on implementation closeout head

**Independent review head:** `6c1a359f969222dd7868248d1ba12fc114f413d9`  
**Reviewers:** CodeRabbit and Qodo  
**Severity:** GOVERNANCE / MAINTAINABILITY  
**Status:** REPAIRED

The implementation closeout already existed but T004-10 still listed its creation as remaining. Task bookkeeping was reconciled before the next qualification.

### R004-09 — Invalid non-object manifests received a misleading manifest digest

**Independent review head:** `bf57ccd47791ef0cd25ebc478e154a9f28c14be4`  
**Reviewer:** Qodo  
**Severity:** MATERIAL / CORRECTNESS + REPORT IDENTITY  
**Status:** REPAIRED

`_base_report()` computes `tournament_manifest_sha256` only when the manifest is a dictionary and all top-level keys are strings. String/list/`None` manifests and mixed-key dictionaries retain a null manifest identity and fail closed as `NO_SELECTION / INVALID_MANIFEST_OR_PROTOCOL`.

## Qualification invalidation history

```text
19cd7697b6f399af50f9006b7235b3421eb8cc0a
  -> Run 32600079522 failed V004-01

77ee65406d2e7bd0b05737622e45aee81a88ed74
  -> Run 32600227184 green (35 focused / 9 hard / 263 full)
  -> invalidated by R004-01/R004-02/R004-03/S004-03/R004-04

66ed1bfc6a80c249f7e78e68a6abf6252afe722b
  -> Run 32600571207 green (39 focused / 9 hard / 267 full)
  -> invalidated by later reconciliation mutations

a8e3c197cd7320539b096821266bba7c36902c27
  -> Run 32600855451 failed V004-02 during oversized-int final report hashing

8da820fde8974ec382afde7009cd201ee8f59bdf
  -> Run 32600976193 green (40 focused / 9 hard / 268 full)
  -> invalidated by R004-05/R004-06/R004-07

f21d500dd172b1cbe1c9d23a86b9880e4104e64a
  -> Run 32601489770 green (42 focused / 9 hard / 270 full)
  -> invalidated by test-only malformed-result coverage mutation

7a04d40030a2aa28b4c2f0d5db6e4d387388c756
  -> Run 32601812794 green (45 focused / 9 hard / 273 full)
  -> clean/minimal-risk review
  -> invalidated by implementation closeout/task-state mutation

6c1a359f969222dd7868248d1ba12fc114f413d9
  -> Run 32602120618 green (45 focused / 9 hard / 273 full)
  -> invalidated by R004-08/G004-01

bf57ccd47791ef0cd25ebc478e154a9f28c14be4
  -> Run 32603238663 green (47 focused / 9 hard / 275 full)
  -> invalidated by R004-09

cf6158ea4193aa7db895607c6fac5a3a1442f708
  -> Run 32603944702 green (48 focused / 9 hard / 276 full)
  -> fresh independent exact-head review: no material blocker
  -> guarded squash implementation merge accepted this exact expected head
```

No predecessor PASS is substituted for the final implementation evidence.

## Final implementation qualification — COMPLETE

Final exact implementation head:

```text
cf6158ea4193aa7db895607c6fac5a3a1442f708
```

Final GitHub qualification:

```text
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
- [PR #28 fresh exact-head Qodo review](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440)
- [Qodo review update marker binding review through exact `cf6158ea...`](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920)
- [Implementation PR #28](https://github.com/TheHalfMoon/commandMed/pull/28)

The final review reported no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker. The guarded squash merge produced canonical implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`, tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`, directly from canonical base `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`.

## Dedicated closure-review reconciliation

The first dedicated closure candidate head `45037b988bd716adc1750199df6c6069ff15f5ac` was independently reviewed before merge and rejected as closure authority. That review is historical evidence only.

Direct review evidence:

- [Qodo closure review on PR #30](https://github.com/TheHalfMoon/commandMed/pull/30#issuecomment-5383104852)

### C004-01 — Noncanonical closeout status

**Affected closure head:** `45037b988bd716adc1750199df6c6069ff15f5ac`  
**Severity:** HIGH / LIFECYCLE CORRECTNESS  
**Status:** REPAIRED

The closeout header used the nonstandard token `CLOSURE_CANDIDATE_REVIEW_AND_MERGE_REQUIRED` while the registry used `CLOSED_CANONICAL`. The repair follows the established Spec 003 pattern: `CLOSED_CANONICAL` with an explicit qualifier that effectiveness begins only after this closure-only PR is merged and resulting canonical `main` is verified.

### C004-02 — Spec 004 lifecycle artifacts remained pre-closeout

**Affected closure head:** `45037b988bd716adc1750199df6c6069ff15f5ac`  
**Severity:** HIGH / LIFECYCLE CONSISTENCY  
**Status:** REPAIRED

`tasks.md`, `review-reconciliation.md`, and the requirements checklist retained present-tense implementation/pre-closeout states after the implementation merge. The closure transition now reconciles the complete lifecycle document set:

- `closeout.md` — canonical closure state with post-merge effectiveness qualifier;
- `tasks.md` — T004-09 and T004-10 complete; T004-11 recorded as complete on closure merge;
- `review-reconciliation.md` — final implementation qualification recorded complete and closure-review history separated;
- `checklists/requirements.md` — lifecycle status reconciled to canonical closure while external closure merge/verification remain non-self-attested;
- `specs/README.md` — Spec 004 `CLOSED_CANONICAL`, Spec 005 `BLOCKED`.

### C004-03 — CI/review claims lacked direct evidence links

**Affected closure head:** `45037b988bd716adc1750199df6c6069ff15f5ac`  
**Severity:** MEDIUM / EVIDENCE QUALITY  
**Status:** REPAIRED

Strong implementation qualification/review claims are now accompanied by directly verifiable GitHub links to the exact Run, Job, implementation PR, fresh exact-head Qodo review, and review update marker.

Any repository-content mutation made to repair C004-01 through C004-03 invalidates the first closure review. The repaired closure head must receive a new fresh independent review before merge.

## Final closure gate

The closure branch originates from exact canonical implementation merge:

```text
9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
```

The repaired final closure head must independently prove, without subsequent content mutation:

```text
BASE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
LIFECYCLE_DOCS_ONLY=PASS
RUNTIME_SOURCE_TEST_DATA_DEPENDENCY_WORKFLOW_CHANGES=NONE
GIT_DIFF_CHECK=PASS
FRESH_INDEPENDENT_CLOSURE_HEAD_REVIEW=NO_MATERIAL_BLOCKER
SPEC_005=BLOCKED
```

Only the guarded merge of that unchanged closure head plus resulting canonical-main verification makes `SPEC_004=CLOSED_CANONICAL` effective.

## Authority boundary

```text
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AGAINST_MODELS=NONE
TRAINING_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEC_005=BLOCKED
```

Spec 004 closure does not authorize Spec 005 start. Spec 005 retains its separate founder license/device prerequisites and explicit start-authorization requirement.
