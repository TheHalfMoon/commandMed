# Spec 004 — Tournament Harness Clarification / Research

**Canonical base reviewed:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Status:** CLARIFIED
**External model/data execution performed:** NO

## Sources reviewed

Spec 004 derives its authority and mechanics from already-canonical repository sources rather than introducing a new external framework:

- `.specify/memory/constitution.md`
- `AGENTS.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- Spec 001 evaluation charter + canonical artifacts/code
- Spec 002 safety-gate contract + canonical safety evaluator
- Spec 003 lineage contract + canonical lineage evaluator

No external benchmark payload, model asset, provider API, or restricted data was inspected.

## Clarification C004-01 — What does “harness” mean here?

**Decision:** a deterministic validator/aggregator over **precomputed result envelopes**. It is not a model runner and not a benchmark runner.

The harness accepts metadata and numeric result evidence that some later authorized stage may produce. Spec 004 proves only that the comparison mechanism itself is frozen, auditable, identity-bound, and fail-closed.

This prevents implementation convenience from silently turning Spec 004 into Spec 005.

## Clarification C004-02 — Does Spec 004 select a real model?

**Decision:** NO.

Synthetic fixtures may exercise `SELECTED`/`NO_SELECTION` mechanics. Those results are mechanism tests only and must use neutral fixture IDs. No real candidate family is admitted or declared a winner in Spec 004.

Real baseline comparison remains Spec 005.

## Clarification C004-03 — Comparison strategy

**Decision:** V1 supports only `LEXICOGRAPHIC_PREDECLARED`.

Rationale:

- avoids an arbitrary weighted score that can hide tradeoffs;
- makes metric priority explicit before results exist;
- preserves canonical per-metric direction;
- is deterministic and simple to audit;
- can later be replaced only through an explicit manifest/schema revision.

The ordered comparison metric list is scientifically semantic and therefore its order is preserved in manifest identity.

## Clarification C004-04 — Tie behavior

**Decision:** V1 supports only `NO_SELECTION_ON_TIE`.

Candidate ID, alphabetical order, input iteration order, wall-clock time, or local runtime metadata may not break a scientific tie.

A later tournament may define an evidence-backed pre-registered tie rule, but V1 does not invent one.

## Clarification C004-05 — Candidate order vs metric order

**Decision:** candidate IDs are set-like; comparison metric IDs are ordered.

The manifest identity projection sorts candidate IDs so reordering candidate declarations does not create scientific drift. The comparison metric list remains in declared order because changing it changes tournament semantics.

## Clarification C004-06 — Which canonical artifacts are bound?

**Decision:** bind six identities:

```text
benchmarks_sha256
metrics_sha256
gold_protocols_sha256
quarantine_sha256
safety_policy_sha256
lineage_contract_sha256
```

Although private Gold payloads are never used by the tournament, binding the canonical Gold **protocol metadata** helps prove the tournament is operating under the same quarantine contract. It does not grant Gold access.

The first five JSON artifacts use existing semantic canonical hashing. The lineage contract uses Spec 003's dedicated `compute_lineage_contract_sha256()` projection.

## Clarification C004-07 — Validate canonical artifacts before trusting their hashes?

**Decision:** YES.

The harness must validate the supplied benchmark registry, metrics catalog, Gold protocol metadata, quarantine rules, safety policy, and lineage contract through the already-canonical validators before accepting their computed identities.

Hash equality alone is not semantic validity.

## Clarification C004-08 — Candidate lineage use

**Decision:** a tournament candidate lineage record must describe:

```text
asset_class=MODEL_OR_CHECKPOINT
declared_use=DEVELOPMENT_EVALUATION
```

Only Spec 003 admission state `ELIGIBLE` proceeds.

This is evaluation permission only. It grants no modification/training/redistribution authority.

Spec 004 fixtures use synthetic model/checkpoint metadata; no real weights are accessed.

## Clarification C004-09 — Parent lineage

**Decision:** if the candidate lineage record declares parents, the result envelope must supply the exact lineage registry needed by Spec 003. Parent resolution and restriction propagation are delegated to canonical Spec 003 logic.

Do not recreate parent policy inside the harness.

## Clarification C004-10 — Safety scope location

**Decision:** safety scope is frozen once in the tournament manifest.

Every candidate result binds the entire manifest by `tournament_manifest_sha256`; therefore a second candidate-level safety-scope digest would be redundant. The harness passes the manifest safety scope directly to canonical Spec 002 evaluation.

## Clarification C004-11 — Safety qualification

**Decision:** call canonical `evaluate_safety_qualification_hard_gates()`.

The harness does not reinterpret pending/frozen thresholds or hard-gate applicability. Overall safety state must be `PASS` before comparison.

A fixture may use a bounded component scope that has enough frozen sentinel evidence to demonstrate a positive path. This fixture scope does not freeze the future Spec 005 tournament scope.

## Clarification C004-12 — Comparison metric eligibility

**Decision:** V1 comparison metrics must be non-hard-gate metrics with canonical direction `HIGHER_BETTER` or `LOWER_BETTER`.

Hard gates remain qualification constraints and cannot simultaneously become optimization weights that offset another hard failure.

`TARGET_RANGE` is excluded until a distance-to-target rule is frozen before results.

## Clarification C004-13 — Result score types

**Decision:** comparison scores must be finite `int`/`float` values, excluding `bool`, NaN, and positive/negative infinity.

Every comparison result also requires `status=PASS` and a resolved `evidence_artifact_id`.

## Clarification C004-14 — Missing/incomplete candidate evidence

**Decision:** candidate-local evidence failure makes that candidate non-qualifying; canonical protocol identity failure blocks the entire tournament.

The report preserves why each candidate failed. The harness does not discard candidates silently.

If no candidate qualifies, final state is `NO_SELECTION`.

## Clarification C004-15 — Payload and execution-surface defense

**Decision:** add a small recursive exact-key denylist specific to tournament inputs in addition to canonical Gold/payload safeguards.

Examples of prohibited keys include runtime commands/hooks, prompts/messages, credentials/secrets/tokens, model/weights paths, benchmark/case payloads, model outputs/generated text, and provider endpoint configuration.

The denylist uses exact normalized key matches to avoid falsely rejecting legitimate identity metadata such as `generation_config_id` in Spec 003 lineage records.

The Python implementation itself must not import or invoke subprocess, socket/network clients, model runtimes, provider SDKs, or dynamic executable hooks.

## Clarification C004-16 — Candidate result manifest binding

**Decision:** every candidate result contains the exact `tournament_manifest_sha256` recomputed by the harness.

A result generated under another manifest cannot be mixed into the tournament even when candidate IDs and score fields look compatible.

## Clarification C004-17 — Report identity

**Decision:** report scientific identity excludes runtime/audit-only metadata and normalizes candidate report ordering by `candidate_id`.

The selected candidate ID, candidate qualification states/reasons, comparison vectors, manifest digest, and canonical artifact identities are scientific fields.

The harness does not need timestamps to produce a valid report.

## Clarification C004-18 — Founder decisions

**Decision:** no founder decision is needed now.

- FD-001 remains due when final candidate lineage/license posture requires it.
- FD-002 remains due before final tournament qualification thresholds.
- FD-006 remains due before tournament freeze if donor-origin restrictions are desired.

The fixture harness must not choose these values implicitly.

## Clarification C004-19 — Dependencies

**Decision:** no new third-party runtime dependency.

Python 3.11 standard library plus the existing commandMed modules are sufficient.

## Clarification C004-20 — Implementation placement

**Decision:** use one small module:

```text
src/commandmed/tournament.py
```

with one focused test module:

```text
tests/test_tournament.py
```

and one human-readable governance document:

```text
docs/evaluation/tournament-harness.md
```

Do not create a service, plugin system, adapter registry, queue, CLI, or runner framework in Spec 004.