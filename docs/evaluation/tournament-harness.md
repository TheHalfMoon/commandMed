# commandMed Spec 004 — Fixture-Only Tournament Harness

## Status and authority

This document describes the Spec 004 V1 tournament harness. The harness is an offline deterministic evaluator over canonical governance metadata and precomputed/synthetic result envelopes.

It does **not** authorize or implement model execution, model-weight access, benchmark payload execution, candidate-model tournament execution, provider/API generation, training, PHI/restricted-data access, private-Gold payload access, or gated-asset access.

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

## Purpose

Spec 004 proves the tournament **mechanism** before any real model tournament is separately authorized. It answers a narrow question:

> Given an exact frozen commandMed protocol and complete precomputed evidence for a declared set of synthetic candidates, can the repository deterministically validate qualification, preserve hard-gate/lineage restrictions, compare only predeclared optimization metrics, refuse incomplete evidence, and produce an identity-bound selection report?

The V1 implementation lives in:

```text
src/commandmed/tournament.py
```

Focused synthetic tests live in:

```text
tests/test_tournament.py
```

## Canonical upstream binding

The harness does not trust a caller merely because a supplied artifact bundle is internally self-consistent. Spec 004 V1 pins the exact canonical upstream semantic identities inherited from Specs 001–003:

```text
benchmarks_sha256=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
metrics_sha256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
gold_protocols_sha256=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
quarantine_sha256=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
safety_policy_sha256=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
lineage_contract_sha256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

A manifest is valid only when both:

1. the supplied artifacts validate under their canonical validators and recompute to this exact map; and
2. the manifest declares this exact map.

A future canonical policy revision therefore requires a reviewed code/schema revision. It cannot be activated by changing caller input alone.

Gold binding above concerns only canonical Gold **protocol metadata**. No private-Gold cases or payloads are accessed by Spec 004.

## Manifest contract

V1 accepts only this top-level shape:

```json
{
  "tournament_id": "fixture-tournament-001",
  "schema_version": "1.0",
  "execution_mode": "PRECOMPUTED_RESULTS_ONLY",
  "comparison_strategy": "LEXICOGRAPHIC_PREDECLARED",
  "comparison_metric_ids": ["metric-a", "metric-b"],
  "candidate_ids": ["fixture-model-a", "fixture-model-b"],
  "tie_policy": "NO_SELECTION_ON_TIE",
  "safety_scope": {
    "scope_id": "fixture-scope",
    "scope_kind": "COMPONENT_QUALIFICATION",
    "claimed_capabilities": [],
    "out_of_scope_capabilities": []
  },
  "canonical_artifact_identities": {
    "benchmarks_sha256": "...",
    "metrics_sha256": "...",
    "gold_protocols_sha256": "...",
    "quarantine_sha256": "...",
    "safety_policy_sha256": "...",
    "lineage_contract_sha256": "..."
  }
}
```

The actual safety scope must validate under canonical Spec 002 rules; the abbreviated example above is illustrative rather than an authorization to omit required capabilities.

V1 invariants:

- unknown top-level fields fail closed;
- candidate IDs are a set for manifest identity and therefore sort canonically;
- comparison metric order is scientific and remains ordered;
- duplicate candidate IDs or comparison metric IDs fail;
- comparison metrics must exist in the canonical metrics catalog;
- hard-gate metrics cannot be used as ranking metrics;
- only `HIGHER_BETTER` and `LOWER_BETTER` ranking directions are accepted;
- `TARGET_RANGE` is not invented or interpreted by Spec 004;
- tie policy is exactly `NO_SELECTION_ON_TIE`.

## Candidate result contract

Each result is a precomputed evidence envelope:

```json
{
  "candidate_id": "fixture-model-a",
  "tournament_manifest_sha256": "...",
  "candidate_lineage_record": {},
  "lineage_registry": [],
  "metric_results": {
    "metric-id": {
      "status": "PASS",
      "score": 0.0,
      "evidence_artifact_id": "fixture:evidence:001",
      "reason": "optional fixture-only explanation"
    }
  }
}
```

`lineage_registry` is optional when no parents are referenced.

The candidate lineage record must bind:

```text
asset_id == candidate_id
asset_class == MODEL_OR_CHECKPOINT
declared_use == DEVELOPMENT_EVALUATION
```

Actual admission is then delegated to Spec 003. The harness does not infer broader training, modification, redistribution, or commercial rights from evaluation eligibility.

## Safety delegation

Spec 004 does not implement a second hard-gate engine. It delegates candidate safety qualification to:

```text
evaluate_safety_qualification_hard_gates()
```

which applies Spec 002 policy/scope semantics and ultimately reuses Spec 001 hard-gate aggregation.

Consequences:

- observed safety `FAIL` is a proven disqualification;
- `INSUFFICIENT_EVIDENCE`, `BLOCKED`, or `NOT_EVALUATED` are not treated as failures that conveniently remove a candidate — they make the tournament incomplete;
- pending `NO_PASS_UNTIL_FROZEN` policy gates remain non-passable;
- Spec 004 cannot manufacture clinical thresholds merely to obtain a tournament winner.

## Candidate state model

Candidate states are intentionally distinct:

```text
QUALIFIED
DISQUALIFIED
INCOMPLETE
```

### QUALIFIED

A candidate is `QUALIFIED` only when:

- its envelope is structurally valid;
- it binds the exact tournament manifest;
- lineage admission is `ELIGIBLE`;
- canonical safety qualification is `PASS`;
- every predeclared comparison metric has `PASS`, finite numeric score, and resolved evidence identity.

### DISQUALIFIED

Use only when complete evidence proves the candidate cannot qualify, including:

- lineage `PROHIBITED`;
- lineage `REFERENCE_ONLY` for the exact evaluation use;
- safety overall `FAIL`.

A proven disqualified candidate may be excluded from ranking without making another complete candidate unfairly incomplete.

### INCOMPLETE

Use when a fair frozen comparison cannot be made, including:

- missing or malformed declared result;
- wrong manifest digest;
- lineage `BLOCKED`/invalid/unresolved;
- safety `INSUFFICIENT_EVIDENCE`, `BLOCKED`, or `NOT_EVALUATED`;
- missing/non-pass/non-finite comparison evidence;
- missing comparison evidence identity.

If **any** declared candidate is `INCOMPLETE`, final tournament state is always:

```text
NO_SELECTION
reason=CANDIDATE_EVIDENCE_INCOMPLETE
```

This prevents subset selection caused by conveniently missing evidence.

Unknown extra candidate IDs and duplicate result envelopes invalidate the candidate result set and also force `NO_SELECTION`.

## Comparison semantics

Only qualified candidates receive comparison vectors. Comparison is lexicographic in the exact manifest metric order:

- `HIGHER_BETTER`: larger finite score ranks higher;
- `LOWER_BETTER`: smaller finite score ranks higher.

No weighted average is permitted. The first unequal frozen comparison metric decides ranking.

Spec 004 V1 uses exact numeric equality because its purpose is fixture-only mechanism validation. It does not invent measurement uncertainty or tolerance rules for a real experiment.

If the best comparison vector is shared by multiple candidates:

```text
NO_SELECTION
reason=TOP_TIE
```

Candidate ID and input order are never scientific tie-breakers.

## Deterministic identities

`tournament_manifest_sha256` is computed over semantic manifest content with candidate IDs normalized as a set while comparison metric order remains preserved.

`report_sha256` is computed without self-reference. Candidate reports are sorted by candidate ID before hashing. Runtime timestamp, local path, hostname, PID, and iteration order are not scientific identity fields and are not part of the report schema.

## Execution/payload denylist

Manifest and candidate envelopes are recursively checked for exact normalized keys that would turn the harness into an execution or secret/payload carrier, including command/shell/argv/hooks, prompts/messages, credentials/tokens/secrets, provider endpoints, model/weights/checkpoint paths, benchmark/private-Gold/case/question payloads, and model-generated output fields.

This is defense in depth; canonical Specs 001–003 retain their own payload and authority checks.

## Spec 005 boundary

Spec 004 proves only the fixture/precomputed-result tournament mechanism. It does not run the Base Model Tournament.

Spec 005 remains blocked until:

1. Spec 004 is independently qualified, merged, and closed canonically through its dedicated closure transition; and
2. the separate founder/license/device prerequisites declared for Spec 005 are resolved and Spec 005 receives explicit bounded authorization.

No model execution authority is inherited merely because the harness exists.

## Additive metrics V2 corrective maintenance

A1 corrective maintenance adds a **separate** metrics contract for future explicitly bound consumers. It does not reinterpret or replace the historical Spec 004 V1 metrics contract.

Historical V1 remains immutable:

```text
V1_METRICS_PATH=data/eval/metrics.json
V1_METRICS_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V1_TOURNAMENT_IDENTITY_MAP=CANONICAL_UPSTREAM_IDENTITIES_V1
V1_FALL_FORWARD_TO_V2=PROHIBITED
```

The additive V2 identity is explicit:

```text
V2_METRICS_PATH=data/eval/metrics-v2.json
V2_SCHEMA_ID=commandmed-metrics-catalog
V2_SCHEMA_VERSION=2.0
V2_SUPERSEDES_V1_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
V2_METRICS_SHA256=ebfdaecebd924c3ec3b897bb6c26a9860635f8cfb6757e8167b20bc488b0adaf
V2_FALL_BACK_TO_V1=PROHIBITED
MUTABLE_LATEST_METRICS_CONTRACT=PROHIBITED
```

V2 replaces the ambiguous V1 `required_evidence` string **only inside the V2 schema** with machine-readable `evidence_requirements`. Each requirement binds a lifecycle `evidence_role`, canonical `purpose`, evidence kind, binding mode, source policy, and requirement text. Unknown values or incompatible role/purpose/source-policy combinations fail closed.

For `arabic_clinical_parity_gap`, V2 represents two distinct lifecycle roles without granting access to either evidence source:

```text
SELECTION_DEV -> CHECKPOINT_SELECTION -> SELECTION_SAFE_NON_GOLD
PRIVATE_GOLD_FINAL_AUDIT -> PRIVATE_GOLD -> PRIVATE_GOLD_FAMILY
```

The Private Gold role remains non-selection evidence. The schema and binding do not authorize payload access, model execution, benchmark execution, threshold selection, candidate selection, or real tournament execution.

All non-Arabic V1 metric evidence text remains traceable through non-selection `QUALIFICATION_ONLY` V2 requirements; the migration does not automatically create selection, Private Gold, or public-external authority for those metrics.

V2 consumers must bind all four fields exactly:

```text
metrics_contract_schema_id
metrics_contract_schema_version
metrics_catalog_path
metrics_catalog_sha256
```

The repository validator recomputes the supplied V2 catalog semantic SHA-256 and validates the V2 schema before accepting a binding. Caller-supplied path/version/SHA cannot broaden the contract, and no consumer may infer a mutable "latest" metrics version.
