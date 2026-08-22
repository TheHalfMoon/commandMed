# Spec 004 — Requirements Checklist

**Status:** READY_FOR_ANALYZE

## Authority and scope

- [x] Spec 003 is canonically closed before Spec 004 starts.
- [x] Spec 004 is explicitly `AUTHORIZED_TO_START` on canonical `main`.
- [x] Spec 005 remains blocked.
- [x] Model execution authority remains NONE.
- [x] Model-weight access authority remains NONE.
- [x] Benchmark-payload execution authority remains NONE.
- [x] Training/provider/PHI/private-Gold/gated-asset authority remains NONE.
- [x] Fixture/precomputed-results-only boundary is explicit.

## Manifest contract

- [x] Versioned schema is required.
- [x] Execution mode is frozen to `PRECOMPUTED_RESULTS_ONLY`.
- [x] Comparison strategy is frozen to `LEXICOGRAPHIC_PREDECLARED`.
- [x] Tie policy is frozen to `NO_SELECTION_ON_TIE`.
- [x] Candidate IDs are unique and set-like for identity.
- [x] Comparison metric order is scientifically semantic.
- [x] Unknown V1 top-level fields fail closed.
- [x] Recursive execution/payload surface rejection is required.

## Canonical contract binding

- [x] Benchmark registry identity is bound.
- [x] Metrics catalog identity is bound.
- [x] Gold protocol metadata identity is bound without Gold payload access.
- [x] Quarantine identity is bound.
- [x] Safety policy identity is bound.
- [x] Lineage contract identity is bound using Spec 003 projection.
- [x] Canonical artifacts are semantically validated before identities are trusted.
- [x] Caller-supplied identity mismatch blocks the tournament.

## Candidate qualification

- [x] Candidate result binds the exact manifest digest.
- [x] Candidate result ID must belong to the manifest.
- [x] Candidate lineage asset ID must equal candidate ID.
- [x] Candidate lineage asset class must be `MODEL_OR_CHECKPOINT`.
- [x] Candidate lineage declared use must be `DEVELOPMENT_EVALUATION`.
- [x] Spec 003 lineage evaluator is reused.
- [x] Only lineage `ELIGIBLE` may qualify.
- [x] Parent registry is delegated to Spec 003 when required.
- [x] Spec 002 safety evaluator is reused.
- [x] Only safety overall `PASS` may qualify.
- [x] Hard-gate failure cannot be averaged away.

## Comparison integrity

- [x] Comparison metric must exist in canonical metrics catalog.
- [x] Hard-gate metric cannot be used as optimization comparison metric.
- [x] Only `HIGHER_BETTER`/`LOWER_BETTER` are supported in V1.
- [x] `TARGET_RANGE` is rejected until a distance rule is pre-registered.
- [x] Comparison result status must be `PASS`.
- [x] Score must be finite numeric and not bool.
- [x] Evidence artifact ID is required.
- [x] No weighted aggregate exists in V1.
- [x] Candidate ID/input order cannot break scientific ties.
- [x] Tie produces `NO_SELECTION`.

## Determinism and reporting

- [x] Manifest SHA-256 is recomputed.
- [x] Report SHA-256 is recomputed.
- [x] Candidate report ordering is normalized.
- [x] Runtime/audit metadata is excluded from scientific identity.
- [x] Missing candidate results are explicit non-qualifying records.
- [x] Duplicate candidate result envelopes fail closed.
- [x] Zero qualified candidates produce `NO_SELECTION`.
- [x] Exactly one best candidate is required for `SELECTED`.

## Minimal mechanism

- [x] One source module is planned.
- [x] One focused test module is planned.
- [x] One human-readable governance doc is planned.
- [x] No service/database/plugin/queue/CLI/adapter framework is planned.
- [x] No new third-party runtime dependency is needed.
- [x] Existing Spec 001/002/003 policy code is reused.

## Testability

- [x] Positive fixture selection is testable without real model/data execution.
- [x] Hard-gate failure path is testable.
- [x] Lineage failure path is testable.
- [x] Identity mismatch path is testable.
- [x] Tie/no-selection path is testable.
- [x] Missing/non-finite comparison evidence is testable.
- [x] Input-order invariance is testable.
- [x] Canonical inherited semantic hashes can be rechecked.

## Founder decisions

- [x] No founder decision is required to implement this harness.
- [x] FD-001 remains deferred to lineage/release posture need.
- [x] FD-002 remains deferred to final tournament qualification thresholds.
- [x] FD-006 remains deferred to tournament freeze if donor restrictions are desired.
- [x] Spec 004 does not silently answer those decisions.