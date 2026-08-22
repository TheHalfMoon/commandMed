# Spec 002 Requirements Quality Checklist

**Spec:** `002-safety-gates`
**Purpose:** verify the specification is bounded, testable, evidence-aware and non-contradictory before implementation.

## Authority and scope

- [x] Canonical starting base is explicit.
- [x] Dependency on Spec 001 `CLOSED_CANONICAL` is explicit.
- [x] Spec 003 implementation remains unauthorized.
- [x] Model execution authority remains NONE.
- [x] Training authority remains NONE.
- [x] Benchmark execution authority remains NONE.
- [x] Explicit exclusions prohibit model/data/runtime scope creep.

## Safety semantics

- [x] All seven required behavioral states are enumerated.
- [x] Forced emergency/escalation behavior is non-overridable.
- [x] Missing safety-critical information blocks unsupported ordinary answer.
- [x] Required deterministic/authoritative tools cannot be substituted by generative prose.
- [x] Valid deterministic safety-critical outputs cannot be silently changed by prose.
- [x] Required evidence cannot be fabricated or treated as present when unresolved.
- [x] Malformed/contradictory safety state fails closed.

## Threshold governance

- [x] Policy/sentinel zero-violation invariants are distinguished from population clinical rates.
- [x] Sentinel success is explicitly prohibited from being promoted into a real-world zero-error claim.
- [x] Pending clinical thresholds cannot pass until evidence prerequisites are bound.
- [x] Frozen statistical thresholds require value/operator/unit/intended use/evidence/rationale/reviewer identity/revision.
- [x] FD-004 is referenced only for benign over-triage and is not prematurely resolved.
- [x] No universal clinical numeric threshold is invented from general regulatory/ethics guidance.

## Gate applicability and claims

- [x] Gate result states include controlled `NOT_APPLICABLE`.
- [x] `NOT_APPLICABLE` requires an explicit out-of-scope capability declaration.
- [x] A capability claim cannot coexist with its required gate being N/A.
- [x] Existing Spec 001 hard-gate identities are preserved rather than weakened/relabelled for convenience.

## Deterministic truth boundary

- [x] Required task classes are closed and reviewable.
- [x] Spec defines mechanism classes without implementing clinical tools.
- [x] No drug database, calculator library, red-flag catalogue, FHIR engine or retrieval system is authorized.
- [x] Unavailable required mechanism cannot silently fall back to ordinary `ANSWER`.
- [x] Result identity requirements are explicit.

## Testability

- [x] Each P1 safety requirement has a fixture-only independent test path.
- [x] Tests require no model or benchmark execution.
- [x] Tests require no PHI, restricted data or real Gold content.
- [x] Fail-closed malformed-input cases are enumerated.
- [x] Full existing Spec 001 regression suite remains required.
- [x] Canonical identity reorder/sensitivity tests are required.

## Evidence and research integrity

- [x] WHO/FDA/NIST sources are recorded as design evidence, not regulatory compliance claims.
- [x] Current FDA final/draft status is distinguished.
- [x] Source limitations are explicit.
- [x] Regulatory product classification remains out of scope.
- [x] Claims are narrower than the evidence.

## Minimal implementation

- [x] Standard library/offline implementation is the default.
- [x] Existing `eval_contract` mechanisms are reused.
- [x] A second policy/evaluation/canonicalization framework is prohibited.
- [x] Proposed artifact layout is small and directly tied to requirements.
- [x] No speculative service, database, plugin system, DSL or UI is introduced.

## Exit evidence

- [x] Exact-head validation/review is required.
- [x] Semantic SHA-256 of the safety-policy artifact is required.
- [x] Acceptance matrix is required.
- [x] Pending clinical/founder thresholds must be listed at closeout.
- [x] Dedicated post-implementation closure-only PR is required before `CLOSED_CANONICAL`.
- [x] Closing Spec 002 does not authorize model execution or training.

## Checklist verdict

```text
SPEC_002_REQUIREMENTS_CHECKLIST=PASS_FOR_ANALYZE
IMPLEMENTATION_AUTHORITY=PENDING_ANALYSIS
MODEL_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
