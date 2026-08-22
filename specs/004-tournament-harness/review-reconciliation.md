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

The canonical `data/eval/quarantine.json` artifact is a container with `quarantine_rules` and `contamination_records`. The initial adapter passed the entire container directly to `validate_quarantine_rules()`.

Repair:

- validate `quarantine_rules` with `validate_quarantine_rules()`;
- validate `contamination_records` with `validate_contamination_records()`;
- retain semantic SHA-256 over the complete canonical quarantine container.

## S004-01 — Caller-supplied alternate protocol bundle

**Discovered by:** Analyze self-audit
**Severity:** MATERIAL / PROTOCOL INTEGRITY
**Status:** REPAIRED

Internal consistency between caller artifacts and manifest declarations is insufficient canonical authority.

Repair:

- hard-pin the exact six Specs 001–003 identities in `CANONICAL_UPSTREAM_IDENTITIES_V1`;
- require recomputed supplied-artifact identities to equal that map;
- require manifest-declared identities to equal that same map.

A valid-but-noncanonical contract bundle therefore fails closed.

## S004-02 — Incomplete candidate subset-selection bypass

**Discovered by:** Analyze self-audit
**Severity:** MATERIAL / COMPARISON INTEGRITY
**Status:** REPAIRED

Candidate states are:

```text
QUALIFIED
DISQUALIFIED
INCOMPLETE
```

Only complete decisive evidence may produce `DISQUALIFIED`:

- lineage `PROHIBITED`;
- lineage `REFERENCE_ONLY` for the exact use;
- safety overall `FAIL`.

Missing/malformed/wrong-manifest/BLOCKED/insufficient/non-comparable evidence is `INCOMPLETE`.

Any declared `INCOMPLETE` candidate forces:

```text
NO_SELECTION
reason=CANDIDATE_EVIDENCE_INCOMPLETE
```

Unknown extra candidates or duplicate result envelopes invalidate the result set and force `NO_SELECTION`.

## R004-01 — FR-006 candidate schema conflict

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / CONTRACT CONSISTENCY
**Status:** REPAIRED

Original FR-006 wording appeared to require a candidate-level `safety_scope`, while the closed candidate schema rejected that duplicate field.

Canonical resolution:

- safety scope exists once in the frozen manifest;
- every candidate carries exact `tournament_manifest_sha256`;
- that digest binds the candidate to the manifest safety scope;
- a duplicate candidate-level safety scope is prohibited to avoid two sources of truth;
- manifest digest mismatch is `INCOMPLETE` and prevents ranking.

`spec.md` and `plan.md` now state this explicitly.

## R004-02 — Plan retained obsolete `NON_QUALIFYING` flow

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / COMPARISON INTEGRITY
**Status:** REPAIRED

Repair:

- remove `NON_QUALIFYING`;
- use `QUALIFIED / DISQUALIFIED / INCOMPLETE`;
- evaluate the incomplete-candidate gate before ranking;
- rank only when no declared candidate is incomplete.

## R004-03 — Report omitted canonical artifact identities

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / REPORT INTEGRITY
**Status:** REPAIRED

Repair:

- every report carries `canonical_artifact_identities` equal to `CANONICAL_UPSTREAM_IDENTITIES_V1`;
- the map participates in the non-self-referential report digest;
- regression proves identity-map mutation changes `report_sha256`.

## S004-03 — Invalid result-set report identity depended on input order

**Discovered by:** post-qualification self-audit
**Affected predecessor:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / DETERMINISTIC IDENTITY
**Status:** REPAIRED

Malformed/unknown result-set errors embedded caller list indexes, so equivalent permutations could change `report_sha256`.

Repair:

- result-set errors do not embed caller indexes;
- recursive denylist list paths use order-neutral `[]` notation;
- report error collections are sorted before hashing;
- regressions prove malformed and unknown-extra result permutations yield identical reports/identities.

## R004-04 — Large integer comparison overflow

**Independent review head:** `77ee65406d2e7bd0b05737622e45aee81a88ed74`
**Severity:** MATERIAL / STABILITY
**Status:** REPAIRED IN TWO LAYERS

The predecessor accepted arbitrary Python integers, but `math.isfinite(10 ** 10000)` can raise `OverflowError` due to float conversion.

Layer 1 repair:

- booleans/non-numeric values remain rejected;
- `math.isfinite()` applies only to `float` values;
- integer ranking remains exact without float coercion.

## V004-02 — Large integer report-hash decimal conversion limit

**Discovered by:** GitHub exact-head carrier Run `32600855451`
**Affected predecessor:** `a8e3c197cd7320539b096821266bba7c36902c27`
**Severity:** MATERIAL / STABILITY + DETERMINISTIC IDENTITY
**Status:** REPAIRED

Run #4 proved Layer 1 was insufficient. The `10 ** 10000` comparison completed, but final report hashing reached Python 3.11's default 4300-digit decimal integer-string conversion limit inside `json.dumps()` and raised `ValueError`.

The project does not change process-global `sys.set_int_max_str_digits()` merely to make the fixture pass.

Layer 2 repair:

- the returned scientific report keeps the original Python integer value;
- report-hash projection recursively maps integers to an exact tagged hexadecimal representation before canonical JSON serialization;
- booleans remain booleans and are not treated as integers;
- metric envelope validation rejects non-finite floats globally;
- integer comparison/ranking remains exact;
- the oversized-integer regression passes through comparison and final report hashing.

The tagged hexadecimal form is an internal scientific-hash projection only; it is not a mutation of the reported score or any inherited canonical Specs 001–003 artifact.

## R004-05 — Recursive denylist separator/whitespace bypass

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`
**Reviewer:** Qodo
**Severity:** MATERIAL / SECURITY
**Status:** REPAIRED

The predecessor normalized only literal spaces and hyphens. A nested field such as `api\tkey` could therefore avoid matching `api_key` in objects whose canonical validators permit additional metadata.

Repair:

- normalize key names through Unicode NFKC compatibility normalization plus case folding;
- collapse every non-ASCII-alphanumeric separator sequence to `_`;
- compare both normalized and underscore-free compact forms against the prohibited vocabulary, preventing separator and camel-style variants from creating a hidden channel;
- use normalized path labels in deterministic errors rather than raw control-character-bearing keys;
- regression rejects `api\tkey`, `api\u200bkey`, and `provider.endpoint` inside manifest safety scope.

No new execution surface or dependency is introduced; `unicodedata` and `re` are Python standard library.

## R004-06 — Report digest did not bind comparison-vector order

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`
**Reviewer:** Qodo
**Severity:** MATERIAL / SCIENTIFIC IDENTITY
**Status:** REPAIRED

The inherited semantic canonicalizer sorts lists of dictionary records that carry recognized IDs such as `metric_id`. That behavior is correct for set-like catalog records but would erase the scientific order of a lexicographic `comparison_vector` if the vector remained a list of dictionaries in the hash projection.

Repair:

- keep the public report unchanged;
- in the report-hash projection only, map each comparison-vector record to an ordered positional sequence `[metric_id, direction, score, evidence_artifact_id]`;
- positional sequence order is preserved by the inherited canonicalizer;
- exact-integer tagged hashing remains applied after this projection;
- regression proves reversing a candidate's comparison vector changes `report_sha256`.

The implementation does not modify the inherited Spec 001 canonicalizer or any canonical artifact identity.

## R004-07 — Bounded spec lacked explicit template exit headings

**Independent review head:** `8da820fde8974ec382afde7009cd201ee8f59bdf`
**Reviewer:** Qodo
**Severity:** GOVERNANCE / AUDITABILITY
**Status:** REPAIRED

The spec already contained explicit prohibited scope and acceptance/exit semantics, but the headings were not the exact review-template labels.

Repair:

- rename the section to the explicit `## Exclusions` heading;
- add a non-empty `## Exit Evidence` section enumerating exact-head CI, independent review, closeout, guarded implementation merge, and dedicated closure-only requirements;
- preserve the rule that Spec 004 is not `CLOSED_CANONICAL` until the separate closure PR is merged and canonical main is verified.

## R004-08 — Mixed object-key types could abort fail-closed evaluation

**Independent review head:** `6c1a359f969222dd7868248d1ba12fc114f413d9`
**Reviewer:** Qodo
**Severity:** MATERIAL / RELIABILITY + FAIL-CLOSED INPUT HANDLING
**Status:** REPAIRED

The closed-shape helper previously constructed one heterogeneous key set and then sorted unknown keys. A malformed object containing both string and non-string keys could therefore raise `TypeError` rather than produce deterministic invalid-input evidence. In addition, `evaluate_tournament()` constructed its report shell by hashing the manifest before validation, so a mixed-key manifest could reach the inherited canonicalizer and abort before the fail-closed validation result was returned.

Repair:

- `_exact_keys()` now isolates only string keys before missing/extra set arithmetic and sorting;
- any non-string object key adds a deterministic `object keys must be strings` validation error;
- recursive prohibited-key scanning retains its independent non-string-key rejection;
- `_base_report()` does not attempt tournament-manifest canonical hashing when top-level manifest keys are non-string, and uses `None` for that invalid manifest identity instead;
- the inherited Specs 001–003 canonicalizer is not modified;
- regressions drive mixed-key manifest and candidate envelopes through `evaluate_tournament()` and require deterministic `NO_SELECTION` / invalid-or-incomplete outcomes rather than exceptions.

## G004-01 — Closeout task bookkeeping stale on closeout head

**Independent review head:** `6c1a359f969222dd7868248d1ba12fc114f413d9`
**Reviewers:** CodeRabbit and Qodo
**Severity:** GOVERNANCE / MAINTAINABILITY
**Status:** REPAIRED

The implementation closeout file already existed, but T004-10 still listed creation of that same closeout candidate as remaining work.

Repair:

- remove closeout creation from the remaining list;
- record the closeout candidate as completed;
- leave only exact-head requalification, fresh review, and guarded implementation merge as remaining T004-10 work.

## Qualification invalidation history

```text
19cd7697b6f399af50f9006b7235b3421eb8cc0a
  -> Run 32600079522 failed V004-01

77ee65406d2e7bd0b05737622e45aee81a88ed74
  -> Run 32600227184 green (35 focused / 9 hard / 263 full)
  -> invalidated by R004-01/R004-02/R004-03/S004-03/R004-04

66ed1bfc6a80c249f7e78e68a6abf6252afe722b
  -> Run 32600571207 green (39 focused / 9 hard / 267 full)
  -> invalidated by later FR-006/plan/large-integer reconciliation mutations

a8e3c197cd7320539b096821266bba7c36902c27
  -> Run 32600855451 failed focused test V004-02 after 39 tests passed and oversized-int final report hashing raised ValueError

8da820fde8974ec382afde7009cd201ee8f59bdf
  -> Run 32600976193 green (40 focused / 9 hard / 268 full)
  -> invalidated by second independent review findings R004-05/R004-06/R004-07

f21d500dd172b1cbe1c9d23a86b9880e4104e64a
  -> Run 32601489770 green (42 focused / 9 hard / 270 full)
  -> independent review had no actionable comments but requested direct malformed-result regression coverage before merge-risk reduction
  -> invalidated by test-only coverage mutation

7a04d40030a2aa28b4c2f0d5db6e4d387388c756
  -> Run 32601812794 green (45 focused / 9 hard / 273 full)
  -> CodeRabbit review Run 5effe806-c304-44a6-a910-95a604c56933: no actionable comments / Minimal risk
  -> invalidated by implementation closeout/task-state content mutation

6c1a359f969222dd7868248d1ba12fc114f413d9
  -> Run 32602120618 green (45 focused / 9 hard / 273 full)
  -> final independent review discovered R004-08 mixed-key fail-closed defect and G004-01 stale task state
  -> qualification invalidated before merge
```

No predecessor PASS is merge evidence for the current implementation head.

## Current required qualification

The non-self-referential implementation closeout candidate already exists. After R004-08/G004-01 repair, the resulting exact final repair head must independently prove on one unchanged head:

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

No further repository-content mutation may occur between that final qualification/review and guarded PR #28 merge. Implementation merge still does not establish `CLOSED_CANONICAL`; the separate closure-only transition remains required.

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
