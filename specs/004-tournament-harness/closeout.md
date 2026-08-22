# Spec 004 — Tournament Harness Implementation Closeout Candidate

**Closeout type:** pre-merge implementation closeout candidate
**Status:** `REPAIRED_AWAITING_FINAL_EXACT_HEAD_QUALIFICATION_AND_REVIEW`
**Implementation PR:** `#28`
**Canonical starting base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Historical reviewed predecessor:** `7a04d40030a2aa28b4c2f0d5db6e4d387388c756`

> This document is intentionally non-self-referential. It does not claim the commit SHA that contains itself. The final repair and reconciliation content containing this document must receive fresh exact-head GitHub qualification and independent review before merge. No predecessor run or review is final merge evidence after a later material finding.

## 1. Bounded implementation completed

Spec 004 establishes the minimum deterministic **fixture/precomputed-results-only** tournament harness required before any later real tournament execution can be authorized separately.

It implements:

- exact V1 tournament manifest validation;
- exact canonical Specs 001–003 artifact identity pinning;
- fail-closed canonical artifact validation before identity trust;
- exact candidate-to-manifest SHA binding;
- canonical Spec 003 exact-use lineage admission;
- canonical Spec 002/001 safety hard-gate qualification;
- explicit `QUALIFIED / DISQUALIFIED / INCOMPLETE` candidate states;
- tournament-wide no-selection when any declared candidate evidence is incomplete;
- deterministic predeclared lexicographic comparison of non-hard-gate metrics;
- no weighted aggregate and no candidate-ID/input-order scientific tie-break;
- deterministic identity-bound reports that include the exact canonical contract identity map;
- report hashing that binds lexicographic comparison-vector order;
- fail-closed recursive execution/payload/credential key rejection;
- fail-closed mixed-type object-key handling without heterogeneous-key sort exceptions;
- exact large-integer comparison and report identity without float or decimal-string overflow;
- synthetic/non-medical fixture regression coverage only.

## 2. Exact canonical identities bound by V1

```text
benchmarks_sha256=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
metrics_sha256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
gold_protocols_sha256=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
quarantine_sha256=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
safety_policy_sha256=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
lineage_contract_sha256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

The harness requires both the recomputed supplied-artifact identities and the manifest-declared identities to equal this exact map. Caller-provided internally consistent alternate policy bundles cannot become canonical by self-assertion.

## 3. Material reconciliation completed

`specs/004-tournament-harness/review-reconciliation.md` records the full predecessor invalidation chain. Material issues repaired during implementation include:

- canonical quarantine container validation across both rules and contamination records;
- alternate-policy self-assertion prevention through immutable V1 identity pinning;
- incomplete-candidate subset-selection prevention;
- candidate safety-scope schema reconciliation through exact manifest binding;
- obsolete `NON_QUALIFYING` plan semantics removal;
- canonical identity map inclusion in reports;
- input-order-independent invalid-result-set report identity;
- large-integer `math.isfinite()` overflow avoidance;
- Python 3.11 large-integer report-hash decimal conversion avoidance via exact tagged-hex hash projection;
- recursive prohibited-key separator/whitespace normalization hardening;
- scientific binding of comparison-vector order in report hashes;
- explicit bounded-spec `Exclusions` and `Exit Evidence` governance sections;
- mixed string/non-string object-key fail-closed validation and invalid-manifest report-shell hardening.

Final-review governance bookkeeping was also reconciled so T004-10 no longer lists creation of an already-present closeout candidate as remaining work.

Every material semantic repair invalidated earlier qualification rather than reusing stale green evidence.

## 4. Historical qualification evidence — not final merge evidence

Temporary GitHub carrier PR #29 previously checked out the historical test-complete predecessor:

```text
RUN=32601812794
JOB=97101112661
EXACT_HEAD=7a04d40030a2aa28b4c2f0d5db6e4d387388c756
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004_TESTS=45/45 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=273/273 PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

After closeout/task content was added, carrier Run `32602120618` also passed 45 focused / 9 inherited hard-gate / 273 full tests on predecessor `6c1a359f969222dd7868248d1ba12fc114f413d9`, together with exact identity, execution-surface, diff, and bounded-path gates.

That later predecessor qualification was invalidated before merge when final independent review identified R004-08, the mixed-type object-key fail-closed defect. Neither historical run is merge evidence for the repaired final head.

## 5. Historical independent review and final-review repair

CodeRabbit reviewed the test-complete predecessor delta through review Run:

```text
REVIEW_RUN=5effe806-c304-44a6-a910-95a604c56933
REVIEWED_DELTA=f21d500dd172b1cbe1c9d23a86b9880e4104e64a..7a04d40030a2aa28b4c2f0d5db6e4d387388c756
RESULT=NO_ACTIONABLE_COMMENTS
MERGE_RISK=MINIMAL
```

The immediately preceding implementation repair head `f21d500dd172b1cbe1c9d23a86b9880e4104e64a` had also received independent review Run `a3febb8c-5520-43a1-a34e-664152eee42c` with no actionable comments. The only residual Moderate risk reported there was missing dedicated regression coverage for malformed candidate result sets; `7a04d400...` added that coverage and the follow-up review reduced merge risk to Minimal.

A later final review of predecessor `6c1a359f969222dd7868248d1ba12fc114f413d9` identified:

- **R004-08 / MATERIAL:** heterogeneous object keys could raise before fail-closed evaluation completed;
- **G004-01 / GOVERNANCE:** T004-10 still listed closeout creation as remaining although `closeout.md` already existed.

Both are repaired in the current candidate content. The current final repair head therefore requires a new independent review; predecessor reviews remain historical context only.

## 6. Acceptance status before final repair qualification

| Area | Current implementation status |
|---|---|
| Closed manifest/result schemas | REPAIRED / final exact-head proof pending |
| Exact six canonical upstream identities | unchanged / final exact-head proof pending |
| Alternate-protocol self-assertion prevention | implemented |
| Candidate lineage delegation | implemented |
| Safety hard-gate delegation | implemented |
| Incomplete-candidate no-selection semantics | implemented |
| Decisive disqualification semantics | implemented |
| Evidence-bound finite comparison metrics | implemented |
| Large integer stability | implemented |
| Lexicographic direction-aware ranking | implemented |
| Scientific tie handling | implemented |
| Deterministic report identity | implemented |
| Comparison-vector order binding | implemented |
| Recursive execution/payload-key hardening | implemented |
| Malformed result-set fail-closed coverage | implemented |
| Mixed-type object-key fail-closed coverage | implemented / final exact-head proof pending |
| Final focused fixture tests | PENDING fresh exact-head run |
| Final inherited hard gates | PENDING fresh exact-head run |
| Final full offline suite | PENDING fresh exact-head run |
| Final independent review | PENDING fresh exact-head review |
| Model/provider/benchmark execution | NONE |

## 7. Explicit authority boundary

Spec 004 does **not** authorize or perform:

- model downloads, model-weight/checkpoint access, loading, or execution;
- inference or generation;
- benchmark dataset/case payload loading or execution;
- tournament execution against real candidate models;
- provider/API generation;
- training, CPT, SFT, LoRA/QLoRA, distillation, DPO, RL/GRPO, QAT, or compression;
- PHI or restricted clinical-data access;
- private-Gold payload access;
- gated asset access or terms acceptance;
- real backbone selection;
- Spec 005 start.

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

## 8. Final implementation merge gate

This closeout candidate does not authorize merge by itself. The exact final repaired PR head containing this file must independently prove:

```text
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004_TESTS=PASS
INHERITED_HARD_GATES=PASS
FULL_OFFLINE_SUITE=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
FRESH_INDEPENDENT_EXACT_HEAD_REVIEW=NO_MATERIAL_BLOCKER
```

Only an unchanged head satisfying all of those gates may be guarded squash-merged through PR #28. No repository-content mutation may occur between final qualification/review and merge.

## 9. Post-merge canonical closure requirement

Implementation merge alone will **not** make Spec 004 `CLOSED_CANONICAL`.

After the qualified implementation merge:

1. verify the canonical implementation merge SHA and tree on `main`;
2. close temporary carrier PR #29 without merge;
3. create a dedicated closure-only branch from that exact canonical main;
4. update this closeout record to bind the canonical implementation merge SHA/tree;
5. update `specs/README.md` to mark Spec 004 closed only through that dedicated transition;
6. keep Spec 005 `BLOCKED` because its separate founder license/device decisions and explicit start authorization remain unsatisfied;
7. independently review the exact closure-only head;
8. guarded squash-merge the closure PR; and
9. verify resulting canonical `main` SHA/tree and lifecycle files.

Only after those steps may the repository state become:

```text
SPEC_004=CLOSED_CANONICAL
SPEC_005=BLOCKED
```
