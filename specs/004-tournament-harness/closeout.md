# Spec 004 — Tournament Harness Canonical Closeout

**Closeout type:** dedicated post-implementation closure-only transition  
**Status:** `CLOSURE_CANDIDATE_REVIEW_AND_MERGE_REQUIRED`  
**Implementation PR:** `#28`  
**Canonical implementation merge:** `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`  
**Canonical implementation tree:** `7e37fa626f825ee25271e0bf21a627a2e64e49da`  
**Final reviewed implementation head:** `cf6158ea4193aa7db895607c6fac5a3a1442f708`  
**Canonical implementation base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`

> This closure record is intentionally non-self-referential. It binds the already-canonical implementation evidence below, but it does not claim the closure commit or closure merge SHA that contains it. `SPEC_004=CLOSED_CANONICAL` becomes effective only if this dedicated closure-only PR is independently reviewed, guarded-merged unchanged, and the resulting canonical `main` plus these lifecycle files are verified.

## 1. Canonical implementation binding

The qualified Spec 004 implementation was squash-merged through PR #28 with an expected-head guard requiring exact implementation head:

```text
cf6158ea4193aa7db895607c6fac5a3a1442f708
```

GitHub produced canonical implementation merge:

```text
9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
```

with canonical tree:

```text
7e37fa626f825ee25271e0bf21a627a2e64e49da
```

The merge commit has canonical parent:

```text
b13a8a823365f4ba800eab4e63c3169e27ed9dcb
```

After merge, canonical `main` was independently fetched and matched `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d` with tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`.

Temporary exact-head carrier PR #29 was then closed **without merge**.

## 2. Final exact-head qualification evidence

Temporary carrier PR #29 explicitly checked out the final reviewed implementation head and produced the final successful exact-head validation:

```text
RUN=32603944702
JOB=97106155513
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

GitHub confirmed Run `32603944702` and Job `97106155513` completed successfully. Every job step, including exact checkout, syntax, identity pins, execution-surface preflight, focused tests, inherited hard gates, full offline suite, and diff/bounded-path checks, completed successfully.

## 3. Final independent implementation review

Fresh independent review was completed against exact head:

```text
cf6158ea4193aa7db895607c6fac5a3a1442f708
```

relative to canonical base:

```text
b13a8a823365f4ba800eab4e63c3169e27ed9dcb
```

The final review result reported:

```text
NO_MATERIAL_CORRECTNESS_BLOCKER
NO_MATERIAL_SECURITY_BLOCKER
NO_MATERIAL_SCIENTIFIC_INTEGRITY_BLOCKER
NO_MATERIAL_LIFECYCLE_BLOCKER
NO_MATERIAL_AUTHORIZATION_BLOCKER
NO_MATERIAL_DETERMINISTIC_REPORTING_BLOCKER
NO_MATERIAL_EXECUTION_SURFACE_BLOCKER
```

The final review explicitly re-verified the material predecessor repairs, including:

- R004-08 mixed string/non-string object-key fail-closed behavior;
- R004-09 suppression of manifest identity for invalid non-object and mixed-key manifests;
- malformed result-set no-selection behavior;
- canonical upstream identity pinning;
- ordered comparison-vector report-hash binding;
- large-integer exact report identity;
- recursive execution/payload/credential denylist hardening;
- fixture/precomputed-results-only authority boundaries; and
- continued `SPEC_005=BLOCKED` state.

All inline material review threads on PR #28 were resolved before merge.

## 4. Bounded implementation completed

Spec 004 establishes the minimum deterministic **fixture/precomputed-results-only** tournament harness required before any later real tournament execution can be separately authorized.

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
- deterministic identity-bound reports including the exact canonical contract identity map;
- report hashing that binds lexicographic comparison-vector order;
- fail-closed recursive execution/payload/credential key rejection;
- fail-closed mixed-type object-key handling without heterogeneous-key sort exceptions;
- invalid non-object manifests without misleading tournament-manifest digests;
- exact large-integer comparison and report identity without float or decimal-string overflow; and
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

The harness requires both the recomputed supplied-artifact identities and the manifest-declared identities to equal this exact map. Caller-provided internally consistent alternate policy bundles cannot become canonical by self-assertion.

## 6. Material reconciliation completed

`specs/004-tournament-harness/review-reconciliation.md` records the predecessor invalidation chain. Material issues repaired during implementation include:

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
- mixed string/non-string object-key fail-closed validation and invalid-manifest report-shell hardening; and
- non-object manifest identity suppression so invalid manifest types cannot carry a valid-looking tournament-manifest digest.

Every material semantic repair invalidated earlier qualification rather than reusing stale green evidence.

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

## 8. Canonical closure transition

The implementation merge alone did not close Spec 004. This dedicated closure-only transition binds the canonical implementation merge, tree, final reviewed implementation head, exact-head validation, independent review, and immutable authority boundary.

This closure PR must itself remain docs/lifecycle-only. It must introduce no source, test, data, dependency, workflow, runtime, execution, model, provider, credential, or authorization changes.

Before merge, the exact closure head must prove:

```text
BASE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
CHANGED_PATHS=specs/004-tournament-harness/closeout.md,specs/README.md
GIT_DIFF_CHECK=PASS
RUNTIME_SOURCE_TEST_DATA_DEPENDENCY_WORKFLOW_CHANGES=NONE
FRESH_INDEPENDENT_CLOSURE_HEAD_REVIEW=NO_MATERIAL_BLOCKER
SPEC_005=BLOCKED
```

Only after the unchanged closure head is independently reviewed, guarded-merged, and the resulting canonical `main` plus lifecycle files are verified may the effective repository state become:

```text
SPEC_004=CLOSED_CANONICAL
SPEC_005=BLOCKED
```

No Spec 005 implementation or execution is authorized by this closure transition.
