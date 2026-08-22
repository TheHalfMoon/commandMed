# Spec 004 — Tournament Harness Implementation Plan

**Canonical base:** `b13a8a823365f4ba800eab4e63c3169e27ed9dcb`
**Status:** PLANNED — implementation still requires Analyze=PASS

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
```

No existing canonical evaluation/safety/lineage JSON or implementation file should require semantic modification.

## 4. Tournament module API

Planned public functions:

```python
compute_tournament_manifest_sha256(manifest) -> str
compute_tournament_report_sha256(report) -> str
compute_canonical_tournament_artifact_identities(artifacts) -> dict[str, str]
validate_tournament_manifest(manifest, artifacts) -> list[str]
validate_candidate_result(result, manifest, artifacts) -> list[str]
evaluate_tournament(manifest, candidate_results, artifacts) -> dict[str, Any]
```

Private helpers may normalize candidate IDs, validate execution-surface keys, resolve metrics, compare finite score vectors, and build deterministic candidate reports.

No class hierarchy is planned.

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

Before identity computation is trusted, each artifact is validated by its canonical validator.

Computed identities:

```text
benchmarks_sha256
metrics_sha256
gold_protocols_sha256
quarantine_sha256
safety_policy_sha256
lineage_contract_sha256
```

The manifest must exactly match all six values.

## 6. Manifest V1 shape

Planned required fields:

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

Planned required fields:

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

The candidate lineage record must satisfy:

```text
asset_id == candidate_id
asset_class == MODEL_OR_CHECKPOINT
declared_use == DEVELOPMENT_EVALUATION
admission == ELIGIBLE
```

This is evaluation-only lineage; no training/modification permission is inferred.

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
4. Recompute six artifact identities.
5. Require exact identity-map equality with the manifest.
6. Validate unique non-empty candidate IDs.
7. Validate unique ordered comparison metrics.
8. Resolve every comparison metric in canonical metrics catalog.
9. Reject hard-gate metrics as comparison metrics.
10. Reject unsupported direction/`TARGET_RANGE`.
11. Validate Spec 002 safety scope.
12. Recompute manifest SHA-256.

## 10. Candidate validation flow

1. Require exact V1 result fields/types.
2. Reject prohibited execution/payload keys recursively.
3. Require candidate ID in manifest candidate set.
4. Require exact manifest SHA match.
5. Reject duplicate candidate results at tournament level.
6. Require lineage record `asset_id == candidate_id`.
7. Require `MODEL_OR_CHECKPOINT` + `DEVELOPMENT_EVALUATION`.
8. Delegate lineage validation/admission to Spec 003.
9. Require lineage admission `ELIGIBLE` before qualification.
10. Delegate safety/hard-gate qualification to Spec 002.
11. Require overall safety `PASS` before comparison.
12. Require every comparison metric result to be `PASS`, finite numeric, and evidence-bound.

Candidate failures produce deterministic candidate state/reasons; they do not automatically invalidate another candidate.

## 11. Tournament evaluation flow

1. Validate manifest and canonical artifact identities.
2. If invalid, return tournament `NO_SELECTION / INVALID_MANIFEST_OR_PROTOCOL` without evaluating selection.
3. Validate candidate result set against exact manifest candidate IDs.
4. Missing result for a declared candidate is recorded as non-qualifying rather than silently omitted.
5. Build per-candidate qualification reports.
6. Build comparison vectors only for qualified candidates.
7. If zero qualified candidates -> `NO_SELECTION`.
8. Compare vectors lexicographically using canonical metric direction.
9. If multiple candidates share the exact best vector -> `NO_SELECTION / TOP_TIE`.
10. If exactly one best candidate -> `SELECTED` with that fixture candidate ID.
11. Sort candidate report records by candidate ID for deterministic report identity.
12. Compute report SHA-256 over scientific fields, excluding any caller audit-only metadata.

## 12. Fail-closed state vocabulary

Tournament final state:

```text
SELECTED
NO_SELECTION
```

Candidate qualification state:

```text
QUALIFIED
NON_QUALIFYING
```

Reason codes are deterministic tokens, expected to include where relevant:

```text
INVALID_MANIFEST_OR_PROTOCOL
MISSING_CANDIDATE_RESULT
DUPLICATE_CANDIDATE_RESULT
MANIFEST_IDENTITY_MISMATCH
LINEAGE_INVALID
LINEAGE_NOT_ELIGIBLE
SAFETY_NOT_PASS
COMPARISON_EVIDENCE_INVALID
NO_QUALIFIED_CANDIDATE
TOP_TIE
```

Underlying lineage/safety reasons are retained in nested detail rather than rewritten as parallel policy.

## 13. Comparison semantics

For each comparison metric in manifest order:

- `HIGHER_BETTER`: larger finite score wins;
- `LOWER_BETTER`: smaller finite score wins.

The first metric with unequal values decides the ordering.

If every frozen comparison metric is equal between the best candidates, V1 declares a tie. Candidate IDs do not resolve it.

No epsilon/tolerance is introduced in V1; fixture scores are compared exactly as supplied numeric values. A later spec may pre-register tolerance semantics if measurement uncertainty requires it.

## 14. Deterministic identity projections

### Manifest

Sort:

- `candidate_ids`.

Preserve:

- `comparison_metric_ids` order.

Canonical nested Spec 002 safety-scope set-like lists are already normalized by the existing canonicalizer.

### Report

Sort candidate report records by `candidate_id`.

Do not include runtime timestamp, local path, hostname, process ID, or iteration-order metadata in the scientific projection.

## 15. Test plan

Focused tests will cover:

### Manifest
- valid fixture manifest;
- stable hash under candidate order change;
- hash change under comparison-metric order change;
- duplicate candidate/metric rejection;
- unknown strategy/tie/execution mode rejection;
- unknown top-level field rejection;
- execution/payload key rejection;
- invalid canonical artifact bundle rejection;
- artifact digest mismatch rejection;
- hard-gate comparison metric rejection;
- `TARGET_RANGE` rejection if present.

### Candidate
- exact manifest binding;
- candidate ID membership and lineage asset ID binding;
- required `MODEL_OR_CHECKPOINT` / `DEVELOPMENT_EVALUATION`;
- blocked/prohibited/reference-only lineage non-qualification;
- parent-registry propagation;
- hard-gate failure dominates scores;
- insufficient/pending safety evidence non-qualification;
- missing/non-pass/non-finite comparison evidence rejection;
- evidence artifact ID required.

### Tournament
- unique best higher-better selection;
- lower-better direction;
- lexicographic priority;
- top tie -> `NO_SELECTION`;
- zero qualified -> `NO_SELECTION`;
- missing declared candidate -> non-qualifying entry;
- duplicate result -> fail closed;
- candidate input order invariant;
- report identity stable under input ordering;
- semantic mutation changes report identity.

### Regression
- existing full suite remains green;
- canonical benchmark/gold/metrics/quarantine/safety/lineage semantic hashes unchanged.

## 16. Verification strategy

Implementation qualification must include:

```text
python -m compileall -q src tests
python -m unittest tests.test_tournament -v
python -m unittest tests.eval_contract.test_hard_gates
python -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

A temporary GitHub exact-head carrier may be used if the repository still intentionally has no permanent workflow. The carrier must explicitly checkout the target PR head and remain separate from the implementation PR.

Independent review must inspect the exact implementation head after tests are green.

## 17. Closeout strategy

Use the established two-stage pattern:

1. implementation PR with non-self-referential closeout candidate and exact-head evidence;
2. after guarded implementation merge, a dedicated closure-only PR updates canonical lifecycle state and binds the implementation merge SHA/tree.

Spec 005 remains blocked until that dedicated Spec 004 closure is canonical and its separate founder prerequisites are resolved.