# Spec 004 — Tournament Harness Analyze

**Canonical base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Analyze pass:** 2
**Final result:** PASS
**Open material findings:** 0
**Implementation authority after this file:** bounded Spec 004 fixture-only implementation only

## 1. Inputs analyzed

- canonical constitution / `AGENTS.md`;
- grand master plan;
- decision register;
- canonical Spec 001 evaluation contract/code/artifacts;
- canonical Spec 002 safety policy/evaluator;
- canonical Spec 003 lineage contract/evaluator;
- Spec 004 `spec.md`, `research.md`, `plan.md`, checklist, and tasks.

No model, benchmark payload, provider API, PHI, restricted data, private-Gold payload, or gated asset was accessed.

## 2. A004-01 — Caller-supplied internally consistent artifacts could masquerade as canonical

**Severity:** MATERIAL / PROTOCOL-INTEGRITY
**Initial state:** BLOCKING
**Resolution:** REPAIRED IN NORMATIVE IMPLEMENTATION REQUIREMENTS

### Problem

The draft plan required the harness to recompute artifact identities and compare them to the manifest. That proves internal consistency between:

```text
caller artifact bundle <-> manifest identity map
```

but does **not** prove that the bundle is the canonical commandMed protocol.

A caller could construct another semantically valid metrics/safety/quarantine artifact set, compute matching hashes, place those hashes in the manifest, and obtain a harness result under an unauthorized protocol.

That would defeat evaluation freeze and allow protocol drift without changing the harness schema.

### Repair

Spec 004 V1 implementation SHALL contain an exact immutable upstream identity map for the canonical baseline from which this harness is authorized:

```text
benchmarks_sha256=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
metrics_sha256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
gold_protocols_sha256=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
quarantine_sha256=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
safety_policy_sha256=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
lineage_contract_sha256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

The harness must require **both**:

1. recomputed supplied-artifact identities equal this exact canonical V1 map; and
2. manifest-declared identities equal this exact canonical V1 map.

Therefore an internally consistent but noncanonical policy bundle fails closed.

A future canonical policy revision requires an explicit reviewed harness schema/identity revision; it cannot be activated merely by changing manifest input.

This repair is normative and overrides any weaker reading of FR-004 / Plan §5.

## 3. A004-02 — Missing/incomplete candidate evidence could permit subset selection

**Severity:** MATERIAL / COMPARISON-INTEGRITY
**Initial state:** BLOCKING
**Resolution:** REPAIRED IN NORMATIVE STATE MODEL

### Problem

The draft plan said a missing declared candidate would be represented as non-qualifying, but it did not explicitly prevent the harness from selecting among the remaining candidates.

That creates a dangerous asymmetry: a candidate with incomplete evidence could effectively disappear, allowing a winner to be selected from a subset that is not the frozen tournament candidate set.

Likewise, `INSUFFICIENT_EVIDENCE` safety state is materially different from an observed hard-gate `FAIL`.

### Repair

Candidate state vocabulary becomes:

```text
QUALIFIED
DISQUALIFIED
INCOMPLETE
```

Mapping rules:

### `DISQUALIFIED`

Use only when complete enough evidence proves the candidate cannot qualify under frozen policy, including:

- lineage `PROHIBITED`;
- lineage `REFERENCE_ONLY` for the exact evaluation use;
- safety overall `FAIL`.

A tournament may select among remaining qualified candidates when other declared candidates are **proven** `DISQUALIFIED`.

### `INCOMPLETE`

Use when evidence is insufficient to make a fair frozen comparison, including:

- missing declared candidate result;
- malformed candidate result;
- wrong manifest digest;
- lineage `BLOCKED` / invalid or unresolved lineage;
- safety `INSUFFICIENT_EVIDENCE`, `BLOCKED`, or `NOT_EVALUATED`;
- missing/non-pass/non-finite comparison evidence;
- missing evidence artifact identity.

If **any** declared candidate is `INCOMPLETE`, tournament final state MUST be:

```text
NO_SELECTION
reason=CANDIDATE_EVIDENCE_INCOMPLETE
```

regardless of other candidates' scores.

Unknown extra candidate IDs or duplicate candidate result envelopes invalidate the result set and also force `NO_SELECTION`.

This repair is normative and overrides any weaker reading of FR-011 / Plan §11.

## 4. A004-03 — Hard-gate result vs optimization metric semantics

**Severity:** MATERIAL IF AMBIGUOUS
**State:** REPAIRED / CLARIFIED

A non-hard comparison metric result with status other than `PASS` is not treated as a hard policy disqualification because no tournament-specific threshold has been frozen for it in Spec 004.

Instead it is `INCOMPLETE` comparison evidence.

Hard-gate disqualification remains exclusively delegated to the canonical Spec 002/Spec 001 safety evaluation path.

This prevents the harness from inventing new pass/fail thresholds for optimization metrics.

## 5. A004-04 — Gold protocol binding could be misunderstood as Gold access

**Severity:** NON-BLOCKING CLARIFICATION
**State:** RESOLVED

Binding `gold_protocols_sha256` uses only the already-canonical metadata protocol. It neither loads nor authorizes any private-Gold case content.

No candidate result field may contain private-Gold payloads.

## 6. A004-05 — Heterogeneous canonical validator return shapes

**Severity:** IMPLEMENTATION DETAIL
**State:** RESOLVED

Existing validators have intentionally different APIs:

- registry/catalog/quarantine validators return `(bool, list[str])`;
- Spec 002 safety-policy/scope validators return `list[str]`;
- Spec 003 lineage-contract validator returns `list[str]`.

The harness may use a tiny private adapter/helper to collect their errors. It must not change those canonical APIs for convenience.

## 7. A004-06 — Safety evaluator import surface

**Severity:** IMPLEMENTATION DETAIL
**State:** RESOLVED

`evaluate_safety_qualification_hard_gates`, `validate_safety_policy`, and `validate_evaluation_scope` are imported directly from `src.commandmed.eval_contract.safety` because they are not all re-exported by `eval_contract.__init__`.

No export-layer change is required for Spec 004.

## 8. A004-07 — Candidate lineage class/use contract

**Severity:** REVIEWED
**State:** PASS

For tournament candidate results, requiring:

```text
asset_id == candidate_id
asset_class == MODEL_OR_CHECKPOINT
declared_use == DEVELOPMENT_EVALUATION
```

is a bounded structural requirement, not an inference that asset class is a universal trust boundary.

Spec 003 still owns the actual exact-use admission decision. Only `ELIGIBLE` can proceed.

## 9. A004-08 — Exact numeric comparison

**Severity:** NON-BLOCKING / V1 LIMITATION
**State:** ACCEPTED

V1 uses exact finite numeric comparison with no epsilon/tolerance.

This is acceptable for fixture-only mechanism validation and maximally explicit. A real Spec 005 experiment may require a pre-registered measurement uncertainty/tolerance rule before execution; Spec 004 does not invent one.

## 10. Final implementation requirements after Analyze

Implementation is authorized only if it obeys all of the following:

1. Pure/offline in-memory validation and aggregation only.
2. No subprocess/network/model/provider/benchmark execution surface.
3. Exact V1 top-level schemas with unknown-field rejection.
4. Recursive exact-key execution/payload denylist.
5. Canonical artifacts semantically validate first.
6. Supplied artifact identities must equal exact `CANONICAL_UPSTREAM_IDENTITIES_V1` above.
7. Manifest identity map must also equal that exact V1 map.
8. Candidate results bind exact manifest SHA.
9. Candidate lineage is exact `MODEL_OR_CHECKPOINT` / `DEVELOPMENT_EVALUATION` and delegated to Spec 003.
10. Safety qualification is delegated to Spec 002.
11. Candidate state distinguishes `QUALIFIED`, `DISQUALIFIED`, and `INCOMPLETE`.
12. Any `INCOMPLETE` declared candidate forces tournament `NO_SELECTION`.
13. Observed lineage prohibition/reference-only or safety `FAIL` may be `DISQUALIFIED` without making another complete candidate incomplete.
14. Comparison evidence must be non-hard-gate, predeclared, `PASS`, finite numeric, evidence-bound.
15. Lexicographic direction-aware comparison only.
16. Scientific ties never use candidate ID/input order as tie-breaker.
17. Reports/manifests are deterministically hashed without self-reference.
18. No real candidate/model/benchmark/Gold payload is used in Spec 004 tests.
19. No new third-party dependency.
20. Spec 005 remains blocked.

## 11. Analyze verdict

```text
SPEC_004_ANALYZE=PASS
OPEN_MATERIAL_FINDINGS=0
FOUNDER_DECISION_REQUIRED_NOW=NO
NEW_RUNTIME_DEPENDENCY_REQUIRED=NO
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
SPEC_005=BLOCKED
BOUNDED_FIXTURE_ONLY_IMPLEMENTATION=AUTHORIZED
```

Any implementation behavior that conflicts with this Analyze record is unauthorized and must fail review rather than silently broaden scope.