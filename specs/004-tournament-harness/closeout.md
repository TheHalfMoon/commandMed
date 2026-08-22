# Spec 004 — Tournament Harness Canonical Closeout

**Closeout type:** dedicated post-implementation governance closure
**Status:** `CLOSED_CANONICAL` — effective only after this closure-only PR is merged and resulting canonical `main` is verified
**Implementation PR:** `#28`
**Canonical implementation merge:** `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`
**Canonical implementation tree:** `7e37fa626f825ee25271e0bf21a627a2e64e49da`
**Final reviewed implementation head:** `cf6158ea4193aa7db895607c6fac5a3a1442f708`
**Canonical implementation base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`

> This closeout is intentionally non-self-referential. It binds the already-canonical implementation evidence below but does not claim the closure merge SHA containing itself. `SPEC_004=CLOSED_CANONICAL` becomes effective only after this exact closure head is independently reviewed, guarded-merged unchanged, and the resulting canonical `main` plus lifecycle records are verified.

## 1. Canonical implementation binding

Spec 004 implementation was guarded squash-merged through [PR #28](https://github.com/TheHalfMoon/commandMed/pull/28) with expected implementation head:

```text
FINAL_REVIEWED_IMPLEMENTATION_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
CANONICAL_IMPLEMENTATION_MERGE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
CANONICAL_IMPLEMENTATION_TREE=7e37fa626f825ee25271e0bf21a627a2e64e49da
CANONICAL_IMPLEMENTATION_BASE=b13a8a823365f4ba800eab4e63c3169e27ed9dcb
```

Canonical `main` was verified at the implementation merge/tree before this closure branch was created. Temporary exact-head carrier PR #29 was then closed without merge.

## 2. Final exact-head implementation qualification

The final exact implementation head was qualified by:

- [GitHub Actions Run 32603944702](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702)
- [GitHub Actions Job 97106155513](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702/job/97106155513)

Recorded result:

```text
EXACT_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
CANONICAL_TOURNAMENT_IDENTITIES=PASS
EXECUTION_SURFACE_PREFLIGHT=PASS
FOCUSED_SPEC004_TESTS=48/48 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=276/276 PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

These links are the directly verifiable runtime qualification evidence; this document does not substitute an unlinked assertion for the underlying GitHub evidence.

## 3. Final independent implementation review

Fresh independent exact-head review evidence:

- [Qodo exact-head review result on PR #28](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440)
- [Qodo review update marker through exact `cf6158ea...`](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920)

The review reported no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker on exact `cf6158ea4193aa7db895607c6fac5a3a1442f708` relative to canonical base `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`.

It re-verified the material final boundaries, including mixed/non-string key fail-closed behavior, invalid non-object manifest identity suppression, malformed result-set no-selection behavior, canonical identity pinning, ordered comparison-vector report hashing, exact large-integer identity, recursive execution/payload/credential denylist hardening, fixture/precomputed-results-only scope, and `SPEC_005=BLOCKED`.

## 4. Bounded implementation completed

Spec 004 establishes the minimum deterministic **fixture/precomputed-results-only** tournament harness required before any later real tournament execution could be separately authorized.

It provides:

- exact V1 tournament manifest validation;
- exact canonical Specs 001–003 artifact identity pinning;
- fail-closed semantic artifact validation before identity trust;
- exact candidate-to-manifest SHA binding;
- canonical Spec 003 exact-use lineage admission;
- canonical Spec 002/001 safety hard-gate qualification;
- explicit `QUALIFIED / DISQUALIFIED / INCOMPLETE` candidate states;
- tournament-wide no-selection when any declared candidate evidence is incomplete;
- deterministic predeclared lexicographic comparison of non-hard-gate metrics;
- no weighted aggregate and no candidate-ID/input-order scientific tie-break;
- deterministic identity-bound reports containing the canonical contract identity map;
- report hashing that binds lexicographic comparison-vector order;
- fail-closed recursive execution/payload/credential key rejection;
- fail-closed mixed-type object-key handling without heterogeneous-key sorting exceptions;
- invalid non-object manifests without misleading tournament-manifest digests;
- exact large-integer comparison/report identity without float or decimal-string overflow; and
- synthetic/non-medical fixture regression coverage only.

## 5. Exact canonical identities bound by V1

```text
benchmarks_sha256=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
metrics_sha256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
gold_protocols_sha256=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
quarantine_sha256=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
safety_policy_sha256=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
lineage_contract_sha256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

Both recomputed supplied-artifact identities and manifest-declared identities must equal this exact map. A caller-provided internally consistent alternate policy bundle cannot become canonical by self-assertion.

## 6. Implementation-review reconciliation

`specs/004-tournament-harness/review-reconciliation.md` preserves the full implementation invalidation chain. Material repairs completed before the canonical implementation merge include:

- quarantine container validation across both rules and contamination records;
- immutable V1 upstream identity pinning;
- incomplete-candidate subset-selection prevention;
- candidate safety-scope schema reconciliation through manifest digest binding;
- obsolete `NON_QUALIFYING` plan semantics removal;
- canonical identity inclusion in reports;
- input-order-independent invalid-result-set report identity;
- large-integer comparison and report-hash overflow repairs;
- recursive prohibited-key separator/whitespace normalization hardening;
- comparison-vector order binding in report hashes;
- explicit bounded-spec `Exclusions` and `Exit Evidence` sections;
- mixed string/non-string object-key fail-closed handling; and
- non-object manifest identity suppression.

Every material implementation mutation invalidated predecessor qualification rather than reusing stale green evidence.

## 7. Dedicated closure-review reconciliation

The first closure candidate head `45037b988bd716adc1750199df6c6069ff15f5ac` was independently reviewed and rejected as closure authority before merge. Evidence:

- [Qodo closure review on PR #30](https://github.com/TheHalfMoon/commandMed/pull/30#issuecomment-5383104852)

That review found and this repaired closure set reconciles:

```text
C004-01 NONCANONICAL_CLOSEOUT_STATUS=REPAIRED
C004-02 STALE_SPEC004_LIFECYCLE_ARTIFACTS=REPAIRED
C004-03 UNLINKED_CI_REVIEW_EVIDENCE=REPAIRED
```

C004-01 is repaired by following the established canonical-closeout pattern: `CLOSED_CANONICAL` with an explicit post-merge effectiveness qualifier.

C004-02 is repaired by reconciling the complete Spec 004 lifecycle set in this closure transition:

- `specs/004-tournament-harness/closeout.md`
- `specs/004-tournament-harness/tasks.md`
- `specs/004-tournament-harness/review-reconciliation.md`
- `specs/004-tournament-harness/checklists/requirements.md`
- `specs/README.md`

C004-03 is repaired by linking the exact GitHub Actions Run/Job, implementation PR, exact-head Qodo review result, review-update marker, and first closure review directly from the lifecycle records.

Because these repairs changed repository content, the first closure review on `45037b...` is historical only. The repaired closure head requires a new fresh independent review before merge.

## 8. Explicit authority boundary

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
- real backbone selection; or
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

## 9. Canonical closure transition

The implementation merge alone did not close Spec 004. This dedicated closure-only transition binds the canonical implementation merge/tree, final reviewed implementation head, directly linked exact-head qualification, directly linked independent review, closure-review reconciliation, and immutable authority boundary.

This closure branch starts from exact canonical implementation merge:

```text
BASE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
```

The closure delta must remain exactly lifecycle/governance documentation. Expected changed paths:

```text
specs/004-tournament-harness/closeout.md
specs/004-tournament-harness/tasks.md
specs/004-tournament-harness/review-reconciliation.md
specs/004-tournament-harness/checklists/requirements.md
specs/README.md
```

Before merge, the exact repaired closure head must prove:

```text
LIFECYCLE_DOCS_ONLY=PASS
RUNTIME_SOURCE_TEST_DATA_DEPENDENCY_WORKFLOW_CHANGES=NONE
GIT_DIFF_CHECK=PASS
FRESH_INDEPENDENT_CLOSURE_HEAD_REVIEW=NO_MATERIAL_BLOCKER
SPEC_005=BLOCKED
```

Only after that unchanged closure head is independently reviewed, guarded-merged, and resulting canonical `main` plus lifecycle files are verified does the effective repository state become:

```text
SPEC_004=CLOSED_CANONICAL
SPEC_005=BLOCKED
```

No Spec 005 implementation or execution is authorized by this closure transition.
