# Spec 004 — Requirements Checklist

**Status:** `CLOSED_CANONICAL` — effective only after the dedicated closure-only PR containing this record is merged and resulting canonical `main` is verified

## Authority and scope

- [x] Spec 003 was canonically closed before Spec 004 started.
- [x] Spec 004 had explicit `AUTHORIZED_TO_START` authority before implementation began.
- [x] Spec 004 implementation is canonically merged and qualified; closure becomes effective only after the dedicated closure-only PR is reviewed, merged, and canonical `main` is verified.
- [x] Spec 005 remains `BLOCKED` and is not authorized to start by Spec 004 closure.
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
- [x] Missing candidate results are explicit incomplete records that prevent ranking.
- [x] Duplicate candidate result envelopes fail closed.
- [x] Zero qualified candidates produce `NO_SELECTION`.
- [x] Exactly one best candidate is required for `SELECTED`.
- [x] Report hash binds ordered lexicographic comparison vectors.
- [x] Mixed-type object keys fail closed without heterogeneous-sort exceptions.
- [x] Invalid non-object manifests retain `tournament_manifest_sha256=None`.
- [x] Arbitrarily large integer scores preserve exact ranking/report identity without float or decimal-string overflow.

## Minimal mechanism

- [x] One source module implements the bounded harness.
- [x] Focused fixture tests cover the contract and review-hardening boundaries.
- [x] Human-readable governance documentation records the contract and closure evidence.
- [x] No service/database/plugin/queue/CLI/adapter framework was introduced.
- [x] No new third-party runtime dependency was introduced.
- [x] Existing Spec 001/002/003 policy code is reused.

## Testability

- [x] Positive fixture selection is tested without real model/data execution.
- [x] Hard-gate failure path is tested.
- [x] Lineage failure path is tested.
- [x] Identity mismatch path is tested.
- [x] Tie/no-selection path is tested.
- [x] Missing/non-finite comparison evidence is tested.
- [x] Input-order invariance is tested.
- [x] Canonical inherited semantic hashes are rechecked.
- [x] Malformed result-set and invalid-manifest fail-closed behavior is tested.

## Final implementation evidence

- [x] Final reviewed implementation head is `cf6158ea4193aa7db895607c6fac5a3a1442f708`.
- [x] [GitHub Actions Run 32603944702](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702) completed successfully.
- [x] [GitHub Actions Job 97106155513](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702/job/97106155513) completed successfully.
- [x] Focused Spec 004 tests: `48/48 PASS`.
- [x] Inherited hard gates: `9/9 PASS`.
- [x] Full offline suite: `276/276 PASS`.
- [x] [Fresh exact-head Qodo review on PR #28](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440) reported no material blocker.
- [x] [Qodo review update marker](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920) binds that review to exact `cf6158ea...`.
- [x] Guarded implementation merge is `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d` with tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`.
- [x] Temporary carrier PR #29 was closed without merge after canonical implementation evidence was captured.

## Closure requirements

- [x] Dedicated closure branch starts from exact canonical implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`.
- [x] Closure changes are governance/documentation-only and preserve runtime/source/test/data/dependency/workflow semantics.
- [x] First closure review findings C004-01 through C004-03 are reconciled before final closure qualification.
- [x] Fresh independent review of the exact final closure head remains required before merge and must report no material lifecycle/governance/authorization/integrity blocker.
- [x] Guarded merge of the unchanged reviewed closure head remains required.
- [x] Resulting canonical `main` and lifecycle-file verification remain required before `CLOSED_CANONICAL` becomes effective.

The checked closure items above define mandatory closure requirements; they do not self-attest that this file's own future merge or resulting-main verification has already occurred. Effectiveness remains controlled by the status qualifier and external GitHub evidence.

## Founder decisions

- [x] No founder decision was required to implement or close this fixture-only harness.
- [x] FD-001 remains deferred to lineage/release posture need.
- [x] FD-002 remains deferred to final real-tournament qualification thresholds.
- [x] FD-006 remains deferred to tournament freeze if donor restrictions are desired.
- [x] Spec 004 does not silently answer those decisions.
- [x] Spec 005 still requires its separate founder license/device prerequisites and explicit start authorization.
