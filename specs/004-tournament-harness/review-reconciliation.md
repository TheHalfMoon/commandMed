# Spec 004 — Tournament Harness Review Reconciliation

**Canonical base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Scope:** fixture/precomputed-results-only harness
**Authority:** no model, weight, benchmark-payload, provider/API, training, PHI/restricted-data, private-Gold payload, gated-asset, or Spec 005 execution authority

## Reconciliation rule

A green predecessor is not reusable as final qualification after a later material defect or semantic repair is discovered. Every repository-content repair creates a new candidate head that requires new exact-head validation and fresh independent review.

## V004-01 — Canonical quarantine container adapter

**Discovered by:** GitHub exact-head carrier Run `32600079522`
**Affected predecessor:** `19cd7697b6f399af50f9006b7235b3421eb8cc0a`
**Severity:** MATERIAL / INTEGRATION
**Status:** REPAIRED

The canonical `data/eval/quarantine.json` artifact is a container with:

```text
quarantine_rules
contamination_records
```

The initial adapter passed the entire container directly to `validate_quarantine_rules()`, causing focused validation to fail.

Repair:

- validate `quarantine_rules` with `validate_quarantine_rules()`;
- validate `contamination_records` with `validate_contamination_records()`;
- retain the semantic SHA-256 over the complete canonical quarantine container.

`19cd7697...` is invalidated as a qualification candidate.

## S004-01 — Caller-supplied alternate protocol bundle

**Discovered by:** Analyze self-audit
**Severity:** MATERIAL / PROTOCOL INTEGRITY
**Status:** REPAIRED

Internal consistency between caller artifacts and manifest declarations is insufficient to establish canonical authority.

Repair:

- hard-pin the exact six canonical Specs 001–003 semantic identities in `CANONICAL_UPSTREAM_IDENTITIES_V1`;
- require recomputed supplied-artifact identities to equal that map;
- require manifest-declared identities to equal that same map.

A semantically valid but noncanonical policy bundle therefore fails closed.

## S004-02 — Incomplete candidate subset-selection bypass

**Discovered by:** Analyze self-audit
**Severity:** MATERIAL / COMPARISON INTEGRITY
**Status:** REPAIRED

A missing or unresolved candidate must not disappear from the frozen candidate set and allow selection among a convenient subset.

Repair:

```text
QUALIFIED
DISQUALIFIED
INCOMPLETE
```

Only complete decisive evidence may produce `DISQUALIFIED`, currently:

- lineage `PROHIBITED`;
- lineage `REFERENCE_ONLY` for the exact use;
- safety overall `FAIL`.

Missing/malformed/wrong-manifest/BLOCKED/insufficient/non-comparable evidence is `INCOMPLETE`.

Any declared `INCOMPLETE` candidate forces:

```text
NO_SELECTION
reason=CANDIDATE_EVIDENCE_INCOMPLETE
```

Unknown extra candidates or duplicate result envelopes invalidate the result set and also force `NO_SELECTION`.

## R004-01 — Candidate schema conflicted with FR-006 safety-scope wording

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / CONTRACT CONSISTENCY
**Status:** REPAIRED

The closed candidate schema rejected an extra candidate-level `safety_scope`, while the original FR-006 wording appeared to require one.

Canonical resolution:

- safety scope exists once in the frozen tournament manifest;
- every candidate result carries exact `tournament_manifest_sha256`;
- that digest binds the candidate to the manifest safety scope;
- candidate-level duplicate safety scope is intentionally prohibited to avoid two sources of truth;
- manifest digest mismatch is `INCOMPLETE` evidence and prevents selection.

`spec.md` and `plan.md` now state this explicitly.

## R004-02 — Plan retained obsolete `NON_QUALIFYING` flow

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / COMPARISON INTEGRITY
**Status:** REPAIRED

The implementation and Analyze contract already used `QUALIFIED / DISQUALIFIED / INCOMPLETE`, but the implementation plan still described missing candidates as generic non-qualifying evidence and permitted ranking too early.

Repair:

- remove `NON_QUALIFYING` from the plan;
- require explicit `INCOMPLETE` candidate records;
- evaluate the incomplete-candidate gate before ranking;
- rank only when no declared candidate is incomplete.

## R004-03 — Selection report omitted canonical artifact identities

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / REPORT INTEGRITY
**Status:** REPAIRED

FR-012 requires the report itself to expose the canonical identity map. The predecessor report contained only `tournament_manifest_sha256`.

Repair:

- every report carries `canonical_artifact_identities` equal to `CANONICAL_UPSTREAM_IDENTITIES_V1`;
- the identity map is included in the non-self-referential scientific report digest;
- regression proves identity-map mutation changes `report_sha256`.

## S004-03 — Invalid result-set reports were input-order sensitive

**Discovered by:** post-qualification self-audit
**Affected predecessor:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / DETERMINISTIC IDENTITY
**Status:** REPAIRED

Valid candidate reports were order-normalized, but malformed/unknown result-set error strings included caller list indexes. Reordering semantically equivalent invalid envelopes could therefore change `report_sha256`.

Repair:

- result-set errors no longer embed caller iteration indexes;
- recursive denylist paths use order-neutral `[]` list notation;
- report error collections are sorted before hashing;
- regressions prove malformed and unknown-extra result permutations yield identical reports and report identities.

## R004-04 — Arbitrarily large integer scores could raise `OverflowError`

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / STABILITY
**Status:** REPAIRED

Python/JSON arbitrary-precision integers passed the numeric type check, but the predecessor then called `math.isfinite(score)`, which converts large integers through floating point and may raise `OverflowError`.

Repair:

- booleans and non-numeric values remain rejected;
- `math.isfinite()` is applied only to `float` values;
- integers remain exact finite integer values without float coercion;
- regression uses `10 ** 10000` and proves evaluation completes deterministically and can compare the value.

## Qualification invalidation history

```text
19cd7697b6f399af50f9006b7235b3421eb8cc0a
  -> invalidated by V004-01 carrier failure

77ee65406d2e7bd0b05737622e45aee81a88ed74
  -> Run 32600227184 was green (35 focused / 9 hard / 263 full)
  -> invalidated by R004-01, R004-02, R004-03, S004-03, R004-04

66ed1bfc6a80c249f7e78e68a6abf6252afe722b
  -> Run 32600571207 was green (39 focused / 9 hard / 267 full)
  -> invalidated by subsequent FR-006/plan/large-integer reconciliation mutations
```

No predecessor PASS is merge evidence for the current implementation head.

## Current required qualification

The next implementation candidate must independently prove on one unchanged exact head:

```text
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004_TESTS=PASS
INHERITED_HARD_GATES=PASS
FULL_OFFLINE_SUITE=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
INDEPENDENT_EXACT_HEAD_REVIEW=NO_MATERIAL_BLOCKER
```

Only after that implementation review is clean may a non-self-referential closeout candidate be added. Adding closeout changes the head and requires another final exact-head qualification/review before guarded merge.

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
