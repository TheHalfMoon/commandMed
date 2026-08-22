# Spec 003 — Independent Review Reconciliation

**Spec:** `003-data-license-provenance`
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Review source:** independent CodeRabbit review on PR #25
**Status:** REPAIRED_PENDING_EXACT_HEAD_REQUALIFICATION

## 1. Predecessor evidence invalidation

The prior implementation candidate:

```text
ab594ad2756b33813d7b69166079849474a290aa
```

had successful exact-head validation evidence, but that evidence is **predecessor-only** and does not qualify the repaired candidate.

Independent review found two material authorization defects. Because the defects affect admission semantics, the prior candidate is not merge-qualified even though its tests and exact-head carrier were green.

## 2. Finding R003-01 — Purpose-to-use authorization bypass

**Review thread:** `PRRT_kwDOT_FyzM6bbCBU`
**Original review comment:** `PRRC_kwDOT_FyzM7kso7_`
**Severity:** MATERIAL / SECURITY

### Finding

The evaluator special-cased `PRIVATE_GOLD` but did not enforce the canonical Spec 001 `Purpose` policy before `ELIGIBLE`.

A fully resolved record could therefore present a purpose such as:

```text
PUBLIC_EXTERNAL_EVAL
CHECKPOINT_SELECTION
DEV
CALIBRATION
```

while requesting `TRAINING_OR_ADAPTATION` and avoid a purpose-level authorization denial.

### Repair

The repaired V1 contract now contains and fail-closed validates the exact canonical purpose/use allowlist:

```text
TRAIN -> TRAINING_OR_ADAPTATION | TEACHER_OR_SYNTHETIC_GENERATION | MODIFICATION_OR_DERIVATION
DEV -> DEVELOPMENT_EVALUATION
CALIBRATION -> DEVELOPMENT_EVALUATION
CHECKPOINT_SELECTION -> DEVELOPMENT_EVALUATION
PUBLIC_EXTERNAL_EVAL -> DEVELOPMENT_EVALUATION | PRIVATE_RELEASE_EVALUATION
PRIVATE_GOLD -> PRIVATE_RELEASE_EVALUATION
```

For a record carrying canonical `Purpose`, every non-`REFERENCE` declared use must be present in that exact allowlist or admission is `PROHIBITED` with `PURPOSE_USE_INCOMPATIBLE`.

The contract cannot silently weaken this matrix because `validate_lineage_contract()` compares it to the V1 canonical matrix and requires invariant `PURPOSE_USE_COMPATIBILITY_ENFORCED`.

Tests cover at least:

- public external evaluation cannot train;
- checkpoint-selection cannot train;
- dev cannot train;
- TRAIN cannot masquerade as development evaluation;
- public external evaluation remains eligible for development evaluation;
- private Gold remains eligible only for bounded private release evaluation;
- public external evaluation cannot silently gain redistribution authority.

## 3. Finding R003-02 — Parent restrictions not propagated

**Review thread:** `PRRT_kwDOT_FyzM6bbCBW`
**Original review comment:** `PRRC_kwDOT_FyzM7kso8C`
**Severity:** MATERIAL / SECURITY

### Finding

`parent_asset_ids` were previously validated only as local strings. The registry did not prove that every parent existed, and admission did not evaluate or propagate parent restrictions.

A synthetic/derived child could therefore name arbitrary parents or a restrictive parent and still be evaluated only on the child fields.

### Repair

The repaired implementation now:

1. requires every referenced parent to resolve in a supplied lineage registry;
2. rejects duplicate IDs, self-parent references, unresolved parents, and parent cycles;
3. requires parent evidence to be scoped to the same exact `declared_use` as the child before it can authorize that use;
4. recursively evaluates parent records;
5. propagates parent admission fail-closed:
   - parent `PROHIBITED` -> child `PROHIBITED` / `PARENT_PROHIBITED`;
   - parent `REFERENCE_ONLY` -> child `BLOCKED` / `PARENT_REFERENCE_ONLY`;
   - parent `BLOCKED` -> child `BLOCKED` / `PARENT_BLOCKED`;
   - missing resolver/registry -> `PARENT_REGISTRY_REQUIRED`;
   - invalid registry -> `PARENT_REGISTRY_INVALID`;
   - mismatched exact-use evidence -> `PARENT_USE_EVIDENCE_MISMATCH`.

The V1 contract requires invariant `PARENT_RESTRICTIONS_PROPAGATE`, so this authorization boundary cannot be removed without invalidating the contract.

Tests cover missing registry, unresolved parent, self-parent, cycle, exact-use evidence mismatch, prohibited public-evaluation parent, unresolved-rights parent, reference-only parent, and clean eligible training parent.

## 4. Review-driven hardening beyond the literal findings

The repair also made these adjacent fail-closed rules explicit:

- `PRIVATE_GOLD` purpose and `PRIVATE_GOLD` quarantine state must agree in both directions;
- generic `QUARANTINED` state prohibits non-reference admission;
- purpose/use policy is an exact allowlist for every non-reference declared use, not only training-related uses;
- scientific identity and admission remain evaluator-owned rather than caller-asserted.

## 5. Authority boundary

Nothing in this repair authorizes execution or data access.

```text
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
TEACHER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEC_004=BLOCKED
```

All repair tests are metadata/fixture-only.

## 6. Qualification status

```text
PREDECESSOR_QUALIFIED_HEAD=ab594ad2756b33813d7b69166079849474a290aa
PREDECESSOR_QUALIFICATION=INVALIDATED_BY_MATERIAL_REVIEW_FINDINGS
REPAIR_IMPLEMENTED=YES
FOCUSED_REVIEW_REGRESSION_TESTS=ADDED
CURRENT_EXACT_HEAD_QUALIFICATION=PENDING
FRESH_INDEPENDENT_EXACT_HEAD_REVIEW=PENDING
MERGE_AUTHORIZED=NO
```

The repaired candidate must pass a new exact-head GitHub validation carrier, inherited semantic-identity checks, full offline regression suite, diff hygiene, and a fresh independent exact-head review before PR #25 may be considered merge-qualified.
