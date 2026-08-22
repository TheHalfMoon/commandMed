# Spec 004 — Tournament Harness Implementation Plan

**Canonical base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Status:** `CLOSED_CANONICAL` — implementation plan completed; effective lifecycle closure only after the dedicated closure-only PR is merged and resulting canonical `main` is verified

## 1. Implementation objective

Add one small pure-Python tournament module that validates a frozen manifest and precomputed candidate result envelopes, delegates safety and lineage policy to canonical Specs 002/003, performs deterministic predeclared comparison, and produces an identity-bound report.

No runner, adapter, CLI, model loader, benchmark loader, provider client, network call, or training surface is added.

## 2. Reused canonical mechanisms

Reuse rather than reimplement:

- `compute_canonical_sha256()` — general semantic hashing;
- `validate_benchmark_registry()`;
- `validate_metrics_catalog()`;
- `validate_gold_protocols()`;
- `validate_quarantine_rules()`;
- `validate_contamination_records()`;
- `validate_safety_policy()`;
- `evaluate_safety_qualification_hard_gates()`;
- `validate_lineage_contract()`;
- `compute_lineage_contract_sha256()`;
- `evaluate_lineage_admission()`.

Spec 004 owns only tournament-specific validation, comparison, and report composition.

## 3. Planned files

### New source

```text
src/commandmed/tournament.py
```

### New tests

```text
tests/test_tournament.py
tests/test_tournament_contract_hardening.py
```

### New documentation

```text
docs/evaluation/tournament-harness.md
```

### Spec lifecycle

```text
specs/004-tournament-harness/spec.md
specs/004-tournament-harness/research.md
specs/004-tournament-harness/plan.md
specs/004-tournament-harness/checklists/requirements.md
specs/004-tournament-harness/tasks.md
specs/004-tournament-harness/analysis.md
specs/004-tournament-harness/review-reconciliation.md
```

No existing canonical evaluation/safety/lineage JSON or implementation file should require semantic modification.

## 4. Tournament module API

Public functions:

```python
compute_tournament_manifest_sha256(manifest) -> str
compute_tournament_report_sha256(report) -> str
compute_canonical_tournament_artifact_identities(artifacts) -> dict[str, str]
validate_tournament_manifest(manifest, artifacts) -> list[str]
validate_candidate_result(result, manifest, artifacts) -> list[str]
evaluate_tournament(manifest, candidate_results, artifacts) -> dict[str, Any]
```

Private helpers may normalize candidate IDs, validate execution-surface keys, resolve metrics, compare score vectors, and build deterministic candidate reports.

No class hierarchy is needed.

## 5. Canonical artifact input bundle

The harness accepts an in-memory mapping with exact required keys:

```text
benchmarks
metrics
gold_protocols
quarantine
safety_policy
lineage_contract
```

Before identity computation is trusted, each artifact is validated by its canonical validator. The canonical `quarantine` artifact is a container: `quarantine_rules` and `contamination_records` are validated separately, while the identity is computed over the full container.

Computed identities:

```text
benchmarks_sha256
metrics_sha256
gold_protocols_sha256
quarantine_sha256
safety_policy_sha256
lineage_contract_sha256
```

Both recomputed artifacts and manifest declarations must equal the exact immutable V1 identity map authorized by Spec 004; internal caller consistency is not sufficient.

## 6. Manifest V1 shape

Required fields:

```json
{
  "tournament_id": "fixture-tournament-001",
  "schema_version": "1.0",
  "execution_mode": "PRECOMPUTED_RESULTS_ONLY",
  "comparison_strategy": "LEXICOGRAPHIC_PREDECLARED",
  "comparison_metric_ids": ["metric-a", "metric-b"],
  "candidate_ids": ["fixture-model-a", "fixture-model-b"],
  "tie_policy": "NO_SELECTION_ON_TIE",
  "safety_scope": {"...": "canonical Spec 002 scope fields"},
  "canonical_artifact_identities": {"...": "six SHA-256 identities"}
}
```

Candidate IDs are normalized as set-like for manifest identity. Comparison metric order is preserved.

Unknown fields are rejected in V1 to prevent hidden execution/configuration channels.

## 7. Candidate result V1 shape

Required fields:

```json
{
  "candidate_id": "fixture-model-a",
  "tournament_manifest_sha256": "...",
  "candidate_lineage_record": {"...": "Spec 003 lineage record"},
  "lineage_registry": [{"...": "optional exact parent registry"}],
  "metric_results": {
    "metric-id": {
      "status": "PASS",
      "score": 0.0,
      "evidence_artifact_id": "fixture-evidence-001",
      "reason": "optional fixture-only explanation"
    }
  }
}
```

`lineage_registry` may be omitted when the candidate lineage record has no parents. Unknown top-level fields are rejected.

The result does not duplicate `safety_scope`. Exact `tournament_manifest_sha256` binds every candidate to the one manifest safety scope; mismatched manifest identity is `INCOMPLETE` evidence and prevents selection.

The candidate lineage record must satisfy:

```text
asset_id == candidate_id
asset_class == MODEL_OR_CHECKPOINT
declared_use == DEVELOPMENT_EVALUATION
```

Actual admission is delegated to Spec 003; only `ELIGIBLE` can become `QUALIFIED`. No training/modification permission is inferred.

## 8. Execution-surface denylist

Recursively reject exact normalized keys such as:

```text
command
commands
shell
argv
executable
hook
hooks
prompt
prompts
messages
api_key
access_token
token
credential
credentials
secret
secrets
provider_endpoint
endpoint
model_path
weights_path
checkpoint_path
benchmark_payload
case_payload
question_text
private_gold_payload
model_output
generated_text
```

Canonical payload-marker checks remain in the underlying contracts. This additional list prevents Spec 004 from becoming an execution/configuration carrier.

## 9. Manifest validation flow

1. Require exact V1 top-level fields and types.
2. Reject prohibited execution/payload keys recursively.
3. Validate canonical artifact bundle through Specs 001–003.
4. Validate both quarantine container members canonically.
5. Recompute six artifact identities.
6. Require supplied-artifact identities to equal the exact V1 map.
7. Require manifest identity map to equal the same exact V1 map.
8. Validate unique non-empty candidate IDs.
9. Validate unique ordered comparison metrics.
10. Resolve every comparison metric in canonical metrics catalog.
11. Reject hard-gate metrics as comparison metrics.
12. Reject unsupported direction/`TARGET_RANGE`.
13. Validate Spec 002 safety scope.
14. Recompute manifest SHA-256.

## 10. Candidate validation flow

1. Require exact V1 result fields/types.
2. Reject prohibited execution/payload keys recursively.
3. Require candidate ID in manifest candidate set.
4. Require exact manifest SHA match, which also binds safety scope.
5. Reject duplicate candidate results at tournament level.
6. Require lineage record `asset_id == candidate_id`.
7. Require `MODEL_OR_CHECKPOINT` + `DEVELOPMENT_EVALUATION`.
8. Delegate lineage validation/admission to Spec 003.
9. Classify lineage `PROHIBITED`/`REFERENCE_ONLY` as decisive `DISQUALIFIED`; blocked/invalid/unresolved lineage is `INCOMPLETE`.
10. Delegate safety/hard-gate qualification to Spec 002.
11. Classify overall safety `FAIL` as decisive `DISQUALIFIED`; non-pass incomplete states are `INCOMPLETE`.
12. For candidates otherwise `QUALIFIED`, require every comparison metric result to be `PASS`, finite numeric, and evidence-bound.
13. Boolean/non-numeric/NaN/infinite scores are invalid; arbitrarily large integer scores remain finite integers and must not be coerced through float finiteness checks.

Candidate state is evidence-sensitive: a decisive proven failure is not the same as missing evidence.

## 11. Tournament evaluation flow

1. Validate manifest and canonical artifact identities.
2. If invalid, return `NO_SELECTION / INVALID_MANIFEST_OR_PROTOCOL` without ranking.
3. Validate the candidate result set against the exact manifest candidate set.
4. Unknown extra candidates or duplicate result envelopes invalidate the result set and force `NO_SELECTION / CANDIDATE_RESULT_SET_INVALID`.
5. Represent every missing declared candidate explicitly as `INCOMPLETE / MISSING_CANDIDATE_RESULT`.
6. Build per-candidate reports using `QUALIFIED`, `DISQUALIFIED`, or `INCOMPLETE`.
7. If **any** declared candidate is `INCOMPLETE`, return `NO_SELECTION / CANDIDATE_EVIDENCE_INCOMPLETE` before ranking.
8. Build comparison vectors only for `QUALIFIED` candidates; proven `DISQUALIFIED` candidates are excluded from ranking.
9. If zero candidates are `QUALIFIED`, return `NO_SELECTION / NO_QUALIFIED_CANDIDATE`.
10. Compare vectors lexicographically using canonical metric direction.
11. If multiple qualified candidates share the exact best vector, return `NO_SELECTION / TOP_TIE`.
12. If exactly one best qualified candidate exists, return `SELECTED / UNIQUE_BEST_QUALIFIED_CANDIDATE`.
13. Sort candidate report records by candidate ID for deterministic report identity.
14. Make invalid-result-set errors independent of caller input iteration indexes/order.
15. Include the exact canonical artifact identity map in the report.
16. Compute report SHA-256 over scientific fields, excluding self-reference/runtime metadata.

## 12. Fail-closed state vocabulary

Tournament final state:

```text
SELECTED
NO_SELECTION
```

Candidate qualification state:

```text
QUALIFIED
DISQUALIFIED
INCOMPLETE
```

Representative deterministic reason codes include:

```text
INVALID_MANIFEST_OR_PROTOCOL
CANDIDATE_RESULT_SET_INVALID
CANDIDATE_EVIDENCE_INCOMPLETE
MISSING_CANDIDATE_RESULT
DUPLICATE_CANDIDATE_RESULT
MANIFEST_IDENTITY_MISMATCH
LINEAGE_NOT_ELIGIBLE
LINEAGE_INCOMPLETE
SAFETY_FAIL
SAFETY_EVIDENCE_INCOMPLETE
COMPARISON_EVIDENCE_INVALID
NO_QUALIFIED_CANDIDATE
TOP_TIE
UNIQUE_BEST_QUALIFIED_CANDIDATE
```

Underlying lineage/safety reasons are retained in nested detail rather than rewritten as parallel policy.

## 13. Comparison semantics

For each comparison metric in manifest order:

- `HIGHER_BETTER`: larger finite score wins;
- `LOWER_BETTER`: smaller finite score wins.

The first metric with unequal values decides the ordering.

If every frozen comparison metric is equal between the best qualified candidates, V1 declares a tie. Candidate IDs do not resolve it.

No epsilon/tolerance is introduced in V1; fixture scores are compared exactly as supplied numeric values. Python/JSON integers are compared as integers, including arbitrarily large integers. Float values must satisfy `math.isfinite()`.

## 14. Deterministic identity projections

### Manifest

Sort:

- `candidate_ids`.

Preserve:

- `comparison_metric_ids` order.

Canonical nested Spec 002 safety-scope set-like lists are normalized by the existing canonicalizer.

### Report

The scientific report contains:

- tournament/manifest identity;
- exact canonical artifact identity map;
- deterministic candidate states/reasons;
- comparison vectors for qualified candidates;
- final selection/no-selection state and reason.

Sort candidate report records by `candidate_id`. Normalize set-like reason/error collections. Do not include runtime timestamp, local path, hostname, process ID, or caller iteration index metadata in the scientific projection.

## 15. Test plan

Focused tests cover:

### Manifest
- valid fixture manifest;
- stable hash under candidate order change;
- hash change under comparison-metric order change;
- duplicate candidate/metric rejection;
- unknown strategy/tie/execution mode rejection;
- unknown top-level field rejection;
- execution/payload key rejection;
- invalid canonical artifact bundle rejection;
- alternate internally consistent artifact bundle rejection;
- hard-gate comparison metric rejection;
- `TARGET_RANGE` rejection if present.

### Candidate
- exact manifest/safety-scope binding;
- candidate ID membership and lineage asset ID binding;
- required `MODEL_OR_CHECKPOINT` / `DEVELOPMENT_EVALUATION`;
- `PROHIBITED`/`REFERENCE_ONLY` decisive disqualification;
- blocked/unresolved lineage incomplete handling;
- parent-registry propagation;
- hard-gate failure disqualification;
- insufficient/pending safety evidence incomplete handling;
- missing/non-pass/non-finite comparison evidence rejection;
- evidence artifact ID required;
- oversized integer score does not raise/abort.

### Tournament/report
- unique best higher-better selection;
- lower-better direction;
- lexicographic priority;
- top tie -> `NO_SELECTION`;
- zero qualified -> `NO_SELECTION`;
- any incomplete declared candidate -> `NO_SELECTION` before ranking;
- missing declared candidate -> explicit incomplete entry;
- duplicate/unknown result -> result-set invalid;
- candidate input order invariant;
- malformed/extra result input permutation invariant;
- report carries exact canonical identity map;
- report identity stable under representation/input ordering;
- semantic mutation changes report identity.

### Regression
- existing full suite remains green;
- canonical benchmark/gold/metrics/quarantine/safety/lineage semantic hashes unchanged.

## 16. Verification strategy

Implementation qualification includes:

```text
python -m compileall -q src tests
python -m unittest tests.test_tournament tests.test_tournament_contract_hardening -v
python -m unittest tests.eval_contract.test_hard_gates
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

A temporary GitHub exact-head carrier may be used because the repository intentionally has no permanent Spec 004 workflow. The carrier explicitly checks out the target PR head and remains separate from the implementation PR.

Independent review must inspect the exact implementation head after tests are green. Any semantic repair invalidates predecessor qualification/review.

## 17. Closeout strategy

Use the established two-stage pattern:

1. implementation PR with a non-self-referential closeout candidate and exact-head evidence;
2. after guarded implementation merge, a dedicated closure-only PR updates canonical lifecycle state and binds the implementation merge SHA/tree.

Spec 005 remains blocked until that dedicated Spec 004 closure is canonical and its separate founder prerequisites are resolved.