# Spec 004 — Tournament Harness

**State:** `CLOSED_CANONICAL` — effective only after the dedicated closure-only PR is merged and resulting canonical `main` is verified
**Canonical starting base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Dependencies:** Spec 001, Spec 002, Spec 003 — all `CLOSED_CANONICAL`
**Training authority:** NONE
**Model execution authority:** NONE
**Model-weight access authority:** NONE
**Benchmark-payload execution authority:** NONE
**Provider/API generation authority:** NONE

## Problem

commandMed now has canonical evaluation, safety, and lineage contracts, but it does not yet have a deterministic mechanism that binds those contracts into one pre-registered model-comparison envelope.

Without a harness contract, Spec 005 could accidentally introduce post-hoc metric selection, incomparable candidate evidence, safety-gate averaging, lineage bypass, mutable protocol identity, or hidden execution behavior while attempting to run a tournament.

Spec 004 must establish the smallest reusable tournament mechanism **before any candidate model or benchmark payload is executed**.

## Goal

Implement an offline, deterministic, fixture-only tournament harness that:

1. validates a frozen tournament manifest;
2. binds the manifest to exact canonical evaluation/safety/lineage identities;
3. validates precomputed candidate result envelopes without producing them;
4. requires exact-use candidate lineage admission before qualification;
5. reuses canonical Spec 001/002 hard-gate semantics;
6. compares only pre-registered, comparable numeric metrics;
7. refuses winner/selection output when evidence is missing, blocked, unsafe, non-comparable, or tied without a pre-registered resolution rule;
8. produces deterministic identity-bound tournament reports;
9. is fully testable with synthetic/non-medical fixtures and no external execution.

## Scope boundary

Spec 004 implements **tournament governance and deterministic aggregation only**.

It does not execute the tournament against real model candidates. That remains Spec 005 and remains blocked until Spec 004 closes plus required founder license/device decisions are resolved.

### Allowed in Spec 004

- Python 3.11 standard-library validation and deterministic aggregation;
- synthetic/non-medical fixture candidates;
- synthetic precomputed metric-result envelopes;
- canonical repository metadata from Specs 001–003;
- deterministic manifest/report hashing;
- fail-closed tests for unsafe, incomplete, incomparable, or mutable evidence;
- fixture-only ranking/selection semantics that prove the mechanism, not a real backbone decision.

### Prohibited in Spec 004

- downloading, loading, opening, or executing model weights/checkpoints;
- inference/generation against any candidate model;
- benchmark dataset/case payload loading or execution;
- external model/provider/API calls;
- real private-Gold payload access;
- PHI/restricted clinical-data access;
- gated asset access or terms acceptance;
- training, CPT, SFT, LoRA/QLoRA, distillation, DPO, RL/GRPO, QAT, or compression;
- device benchmarking against candidate models;
- selecting or declaring a real backbone winner;
- modifying canonical Spec 001/002/003 contracts merely to make a fixture pass;
- starting Spec 005.

## Canonical inputs to bind

A tournament manifest must bind the exact semantic identities of the canonical contracts it relies on, including:

- benchmark registry;
- metric catalog;
- Gold protocol metadata;
- quarantine/contamination contract;
- safety policy;
- lineage contract.

The harness must compare the declared identities against identities computed from the supplied canonical artifacts and against the exact V1 identity map authorized by this spec. A caller cannot self-assert a protocol identity or substitute another internally consistent contract bundle.

## User stories

### US1 — Researcher freezes a tournament before execution

As a researcher, I can define a tournament manifest containing candidate IDs, exact comparison metrics, ordered comparison rules, safety scope, and canonical contract identities before any model is run.

**Independent test:** semantic mutation of the manifest changes its SHA-256 identity; representation-only ordering of set-like fields does not.

### US2 — Reviewer proves candidates are comparable

As an independent reviewer, I can see that every candidate result references the same frozen tournament manifest and supplies the same required comparison metrics under the same declared scope.

**Independent test:** a candidate missing a required metric, using another manifest digest, or using a non-numeric/invalid score fails closed and cannot be ranked.

### US3 — Safety owner prevents leaderboard averaging over hard failures

As a safety owner, I can prove that Spec 001/002 hard-gate failure or insufficient safety evidence prevents candidate qualification regardless of comparison scores.

**Independent test:** a synthetic candidate with excellent comparison scores but one applicable hard-gate failure cannot become selectable.

### US4 — Lineage owner prevents unauthorized candidate admission

As a lineage owner, I can require a candidate's exact-use lineage record to be `ELIGIBLE` before its results can qualify for tournament comparison.

**Independent test:** blocked/prohibited/reference-only/unbound lineage prevents selectability even when metric scores are excellent.

### US5 — Researcher gets deterministic, non-post-hoc comparison

As a researcher, I can compare qualified fixture candidates using an ordered metric vector frozen in the manifest rather than an ad-hoc weighted average invented after results are known.

**Independent test:** lexicographic comparison uses only the pre-registered metric order and canonical direction; changing metric order changes the manifest identity.

### US6 — Reviewer sees honest no-selection outcomes

As a reviewer, I can distinguish `SELECTED`, `NO_SELECTION`, and blocked/insufficient states without forcing a winner.

**Independent test:** ties without an explicit frozen tie-resolution rule, incomplete evidence, or zero qualified candidates produce `NO_SELECTION` with deterministic reason codes.

## Functional requirements

### FR-001 — Tournament manifest contract

The harness SHALL validate one versioned tournament manifest with at least:

- `tournament_id`;
- `schema_version`;
- `comparison_strategy`;
- ordered `comparison_metric_ids`;
- candidate IDs;
- safety evaluation scope;
- canonical artifact identities;
- tie policy;
- declared execution mode fixed to `PRECOMPUTED_RESULTS_ONLY`.

V1 SHALL support only one comparison strategy: `LEXICOGRAPHIC_PREDECLARED`.

V1 SHALL support only one tie policy: `NO_SELECTION_ON_TIE`.

Unknown strategies or tie policies fail closed.

### FR-002 — No execution surface

The manifest/result contracts SHALL NOT accept runtime commands, shell fragments, provider credentials, model prompts, model loader configuration, generation parameters, benchmark payloads, private-Gold payloads, or arbitrary executable hooks.

The implementation SHALL not import subprocess/network/model-runtime/provider libraries and SHALL perform no file/network execution of candidate assets.

### FR-003 — Candidate identity set

Candidate IDs SHALL be non-empty, unique, and treated as set-like for manifest identity, while comparison metric order remains semantically ordered.

Spec 004 fixture IDs are synthetic/neutral. Real candidate admission belongs to Spec 005.

### FR-004 — Canonical contract identity binding

The harness SHALL recompute and verify required artifact identities from supplied canonical artifacts rather than trusting the manifest alone.

V1 SHALL bind exactly:

```text
benchmarks_sha256
metrics_sha256
gold_protocols_sha256
quarantine_sha256
safety_policy_sha256
lineage_contract_sha256
```

Both the recomputed supplied-artifact map and the manifest-declared map SHALL equal the exact canonical V1 identity map frozen by Spec 004. Identity mismatch yields a blocked tournament and no selection.

### FR-005 — Comparison metric freeze

Every comparison metric ID SHALL:

- exist exactly once in the canonical metric catalog;
- not be a hard-gate metric used as an optimization substitute;
- have canonical direction `HIGHER_BETTER` or `LOWER_BETTER` in V1;
- appear exactly once in the ordered comparison list.

`TARGET_RANGE` comparison is excluded from V1 ranking until a separate pre-registered distance rule exists.

### FR-006 — Candidate result envelope

Each precomputed candidate result SHALL contain at least:

- `candidate_id`;
- `tournament_manifest_sha256`;
- candidate lineage evidence record;
- optional lineage registry required by that record's parents;
- metric results keyed by metric ID;
- exact evidence artifact IDs for reported metrics.

The candidate result SHALL **not** duplicate `safety_scope`. The exact `tournament_manifest_sha256` binds the result to the manifest, and the manifest contains the one canonical safety scope used for all candidate qualification. A digest mismatch is `INCOMPLETE` evidence and cannot be ranked.

The result envelope SHALL not contain model output text, benchmark cases, private Gold, prompts, or executable runtime configuration.

### FR-007 — Candidate lineage qualification

Before comparison, the harness SHALL call the canonical Spec 003 lineage evaluator for the candidate's exact declared use.

Only lineage state `ELIGIBLE` may proceed to tournament qualification.

`BLOCKED`, `PROHIBITED`, or `REFERENCE_ONLY` must remain non-selectable and expose deterministic reason codes. `PROHIBITED` or `REFERENCE_ONLY` may be decisively `DISQUALIFIED`; blocked/invalid/unresolved evidence is `INCOMPLETE`.

### FR-008 — Safety/hard-gate qualification

The harness SHALL reuse canonical Spec 002 `evaluate_safety_qualification_hard_gates()` over the supplied canonical safety policy, manifest-bound safety scope, canonical metric catalog, and candidate precomputed metric results.

Only overall `PASS` may proceed to comparison.

Observed overall `FAIL` is a decisive `DISQUALIFIED` result. `INSUFFICIENT_EVIDENCE`, `BLOCKED`, or `NOT_EVALUATED` remain `INCOMPLETE` and SHALL not be converted into pass or used to remove a candidate from the frozen comparison set.

### FR-009 — Required comparison evidence

For every comparison metric, each otherwise-qualified candidate SHALL provide:

- canonical metric ID;
- `PASS` result status;
- finite numeric score (boolean is not numeric for this purpose);
- resolved non-empty `evidence_artifact_id`.

Missing, NaN, positive/negative infinity, malformed, or non-pass comparison evidence fails closed. Arbitrarily large Python/JSON integer values are finite numeric values and SHALL be handled deterministically without float conversion overflow.

### FR-010 — Deterministic lexicographic comparison

V1 SHALL compare qualified candidates lexicographically using the exact ordered metric list frozen in the manifest and each metric's canonical direction.

No weighted aggregate, normalization, or post-hoc metric insertion is allowed.

Candidate IDs may be used only for deterministic report ordering, never as a scientific tie-breaker.

### FR-011 — No-selection semantics

The harness SHALL return `NO_SELECTION` when:

- no candidate qualifies;
- any declared candidate is `INCOMPLETE`;
- the best comparison vector is tied under all frozen comparison metrics;
- canonical identity binding fails;
- the manifest is invalid;
- the candidate result set is malformed, contains duplicate envelopes, or contains undeclared extra candidate IDs;
- required comparison evidence is incomplete/non-comparable.

A candidate proven `DISQUALIFIED` by complete decisive evidence does not itself force the other complete candidates to become incomplete.

The harness SHALL never silently choose alphabetically, by input order, or from a subset created by missing evidence.

### FR-012 — Deterministic tournament report

The report SHALL include at minimum:

- tournament manifest SHA-256;
- exact canonical contract identity map;
- per-candidate qualification state/reason codes;
- frozen comparison vector for qualified candidates;
- selected candidate ID only when exactly one best candidate exists;
- final state `SELECTED` or `NO_SELECTION`;
- deterministic report SHA-256 computed over scientific fields.

Runtime timestamps, local paths, machine names, and input iteration order SHALL NOT alter scientific identity, including invalid-result-set reports. The report digest SHALL preserve the manifest-declared lexicographic order of each `comparison_vector`; reordering that vector is a scientific mutation and must change `report_sha256`.

### FR-013 — Fixture-only validation

Tests SHALL prove at least:

- valid manifest acceptance;
- duplicate candidate/metric rejection;
- protocol identity mismatch rejection;
- payload/execution-surface rejection, including internal-whitespace/separator variants of prohibited key names;
- lineage blocked/prohibited/reference-only candidate cannot qualify;
- safety hard-gate failure dominates excellent scores;
- pending/insufficient safety evidence cannot qualify;
- missing/non-finite/non-pass comparison score fails closed;
- arbitrarily large integer comparison scores do not abort evaluation;
- direction-aware lexicographic ordering;
- tied best candidates produce `NO_SELECTION`;
- candidate input order does not change report identity/result, including malformed/undeclared-result permutations;
- report carries the exact canonical identity map and semantic mutation changes report identity;
- reordering a candidate comparison vector changes report identity;
- manifest semantic mutation changes identity;
- canonical Spec 001/002/003 identities remain unchanged.

## Non-functional requirements

### NFR-001 — Determinism

Equivalent semantic inputs produce identical canonical manifest/report identities and comparison outcomes.

### NFR-002 — Offline operation

All Spec 004 source/tests must run without network access.

### NFR-003 — Standard library first

No new third-party runtime dependency without an explicit necessity finding and separate approval.

### NFR-004 — Fail closed

Malformed, incomplete, contradictory, unknown, non-finite, incomparable, or identity-mismatched input cannot become selectable.

### NFR-005 — Minimal mechanism

Use existing Spec 001 canonicalization/hard-gate code, Spec 002 safety qualification, and Spec 003 lineage admission. Do not duplicate these policies in a second framework.

### NFR-006 — No hidden execution

The implementation is a pure validation/aggregation mechanism over in-memory metadata/results. It does not discover or execute model/benchmark tooling.

## Exclusions

Spec 004 SHALL NOT:

- implement model adapters/runtimes;
- define candidate model families beyond synthetic fixtures;
- resolve FD-001/FD-002/FD-006;
- freeze final device thresholds;
- execute or score real benchmarks;
- access or construct private Gold cases;
- calculate clinical thresholds from synthetic fixtures;
- declare a real tournament winner;
- start Spec 005;
- change canonical safety/lineage/evaluation contracts unless a separately justified defect requires corrective maintenance.

## Founder-decision status

No founder decision is required to implement or close this fixture-only harness.

The following remain deferred to the dependency point that actually needs them:

- FD-001 release/licensing posture;
- FD-002 target device tier — needed before final tournament qualification thresholds;
- FD-006 donor-origin restrictions — needed before tournament freeze if restrictions are desired.

Spec 004 must expose a clean boundary for those later decisions rather than choosing them implicitly.

## Acceptance criteria

1. Versioned manifest validation exists and rejects execution surfaces.
2. Manifest identity is deterministic and binds the exact canonical Specs 001–003 artifact map.
3. Candidate result validation requires the exact manifest identity; that digest binds every candidate to the single manifest safety scope without duplicating scope fields.
4. Candidate lineage uses the canonical Spec 003 evaluator and only `ELIGIBLE` can qualify.
5. Safety qualification uses the canonical Spec 002 evaluator; observed hard-gate failure disqualifies while insufficient evidence forces no selection.
6. Comparison metrics are pre-registered, canonical, direction-aware, finite, evidence-bound, and handle large integers without overflow.
7. Lexicographic comparison is deterministic and has no hidden/alphabetic tie-break selection.
8. Ties and incomplete/blocked evidence produce `NO_SELECTION`; proven `DISQUALIFIED` candidates remain distinct from incomplete evidence.
9. Deterministic report identity is stable under semantic input reordering, carries canonical contract identities, binds comparison-vector order, and changes on scientific mutation.
10. Synthetic fixture tests cover positive and negative cases without model/benchmark payload execution.
11. Canonical Spec 001/002/003 semantic identities remain unchanged.
12. No new dependency/runtime/provider/model/data execution surface is introduced.
13. Independent review reports no unresolved material authorization, comparison-integrity, security, or governance blocker.
14. Exact-head GitHub validation passes before guarded merge.

## Exit Evidence

Spec 004 is eligible for implementation merge only when one unchanged exact PR head proves all of the following:

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

The final implementation head must also contain a non-self-referential closeout record that cites predecessor validation/review evidence without claiming its own commit SHA. Adding that closeout changes the head and therefore requires a fresh exact-head validation and independent review before guarded merge.

After implementation merge, a separate closure-only PR must bind the canonical implementation merge SHA/tree and update lifecycle state. Only the verified merge of that closure-only PR may establish `SPEC_004=CLOSED_CANONICAL`.

## Exit state

Spec 004 becomes `CLOSED_CANONICAL` only after its bounded implementation is independently reviewed, exact-head qualified, merged, and followed by a dedicated closure-only transition.

Closing Spec 004 may unblock Spec 005 **only** subject to its separate required founder license/device decisions and its own explicit authorization. It never grants model execution automatically.
