# Spec 002 — Safety Gates Candidate Closeout Evidence

**Closeout type:** fixture-only safety-governance implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION`
**Canonical starting base:** `cc02b0d99d67e5a720502953c99307c8b991720d`
**Implementation branch:** `spec/002-safety-gates`
**State transition rule:** implementation merge does not make Spec 002 `CLOSED_CANONICAL`; a dedicated post-merge closure-only PR remains required.

## 1. Purpose

Record the implementation-candidate evidence for the bounded Spec 002 Safety Gates contract without claiming model, benchmark, patient, or real-world clinical performance.

Spec 002 implements declarative/offline mechanics for:

- canonical behavioral-state and forced-state precedence;
- deterministic/authoritative truth-boundary governance;
- system-vs-component applicability rules;
- policy/sentinel zero-violation semantics;
- pending population clinical-threshold provenance requirements;
- deterministic semantic policy identity;
- fail-closed handling of malformed policy, scope, and synthetic-fixture inputs.

It does not implement a clinical red-flag catalogue, medication database, dose engine, clinical calculator, retrieval service, patient advice runtime, model evaluator, or training system.

## 2. Latest implementation-proven exact-head evidence

GitHub Actions carrier PR #14 validated exact implementation predecessor head:

```text
VALIDATED_IMPLEMENTATION_HEAD=19e409112ee512367eb675a3150d5ebb1242a752
RUN_ID=32590890965
JOB_ID=97074442747
WORKFLOW=Spec 002 Final Exact-Head Validation
CONCLUSION=SUCCESS
```

The workflow explicitly checked out detached HEAD `19e409112ee512367eb675a3150d5ebb1242a752` rather than the carrier head.

Observed evidence:

```text
EXACT_HEAD=19e409112ee512367eb675a3150d5ebb1242a752
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
SAFETY_POLICY_VALIDATION=PASS
FOCUSED_SPEC_002_TESTS=49/49_PASS
FULL_OFFLINE_TESTS=151/151_PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

This run includes the fail-closed malformed-scope and malformed scalar-token repairs added during independent self-review. It supersedes the earlier 41/143 and 43/145 predecessor runs as implementation evidence.

Because this closeout evidence file itself creates a newer branch head, the SHA above is intentionally an **implementation predecessor**, not the final PR-head qualification. The final PR head must be rerun after this file's last content mutation.

## 3. Final-head evidence binding without self-reference

This closeout file MUST NOT be mutated merely to embed the SHA produced by its own mutation. That would create an endless self-reference cycle.

Therefore final exact-head qualification is bound through immutable GitHub evidence external to this file:

1. a GitHub-hosted validation workflow explicitly checks out the final PR head SHA;
2. the run/job IDs and exact outputs are recorded in PR #10 metadata;
3. an exact-head review is anchored to the same final SHA;
4. any head mutation invalidates that qualification and requires a new run/review.

After this document's final mutation, no further repository-content change is permitted before qualification unless a material defect is discovered.

## 4. Semantic policy identity

The latest implementation-proven run computed:

```text
data/eval/safety_policy.json=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
```

The same run re-confirmed the four inherited Spec 001 semantic identities with no drift:

```text
data/eval/benchmarks.json=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
data/eval/gold_protocols.json=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
data/eval/metrics.json=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
data/eval/quarantine.json=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
SEMANTIC_IDENTITIES=PASS
```

The final external exact-head run must re-confirm these identities after this evidence-only mutation.

## 5. Planning/analyze evidence

Spec 002 planning used the repository Spec Kit lifecycle and recorded `analysis.md` before implementation.

The analysis found and repaired two material planning contradictions before code was added:

1. `NOT_APPLICABLE` was initially described as a gate-result state even though canonical Spec 001 `GateEvaluationState` does not contain it. The repair keeps N/A as applicability metadata resolved before hard-gate aggregation.
2. generic N/A semantics could have allowed component scope narrowing to suppress required system safety obligations. The repair separates `SYSTEM_QUALIFICATION` from `COMPONENT_QUALIFICATION`, prevents component PASS promotion to system PASS, and prevents Arabic/patient safety obligations from being waived by scope relabeling.

Independent implementation review then found and repaired malformed-input crash surfaces in scope collections and scalar-vocabulary membership, extending fail-closed coverage without changing the canonical safety-policy semantic identity.

Analyze verdict:

```text
SPEC_002_ANALYZE=PASS_TO_IMPLEMENT
```

## 6. Acceptance matrix

| # | Spec 002 acceptance criterion | Candidate evidence | Status |
|---|---|---|---|
| 1 | Machine-readable safety-policy contract with stable IDs/closed vocabularies | `data/eval/safety_policy.json` + validator | CANDIDATE_PASS |
| 2 | Unknown/malformed/duplicate policy objects fail cleanly | malformed scalar/collection/completeness regression matrix | CANDIDATE_PASS |
| 3 | Required `EMERGENCY`/`ESCALATE` cannot be overridden in sentinels | forced-state tests | CANDIDATE_PASS |
| 4 | Required deterministic/authoritative mechanisms cannot be replaced by guessed prose | truth-boundary validator/evaluator tests | CANDIDATE_PASS |
| 5 | Valid deterministic safety-critical results cannot be altered silently | exact typed-result comparison tests | CANDIDATE_PASS |
| 6 | Missing required information/evidence blocks unsupported answer/pass | precedence + unresolved-evidence tests | CANDIDATE_PASS |
| 7 | Existing gate-result semantics reused; applicability scope cannot hide claimed capability or promote component PASS to system PASS | scope validator/applicability tests | CANDIDATE_PASS |
| 8 | Sentinel zero violations explicitly separated from population zero-error claim | policy classes + documentation + tests | CANDIDATE_PASS |
| 9 | Unsupported statistical thresholds remain pending/non-passable; FD-004 over-triage remains pending | threshold requirement validator/tests | CANDIDATE_PASS |
| 10 | Existing Spec 001 hard-gate identities mapped without weakening | exact metric→capability/class/evidence-kind completeness validation | CANDIDATE_PASS |
| 11 | Offline fixture-only tests pass and Spec 001 regression suite remains green | 49 focused + 151 full tests on latest implementation predecessor | PENDING_FINAL_PR_HEAD |
| 12 | Canonical policy identity and exact-head closeout evidence recorded with no prohibited activity | semantic hashes + external final-head binding protocol | PENDING_FINAL_PR_HEAD |

Spec 002 MUST NOT be described as `12/12 PASS` until rows 11 and 12 are re-proven on the final exact PR head after this file's last mutation.

## 7. Pending clinical/founder thresholds

The following population/statistical thresholds remain intentionally unresolved and non-passable until required evidence is bound:

1. `emergency_miss_rate` — `PENDING_CLINICAL_EVIDENCE`;
2. `medication_critical_error_rate` — `PENDING_CLINICAL_EVIDENCE`;
3. `selective_risk_at_target_coverage` — `PENDING_CLINICAL_EVIDENCE`;
4. `citation_entailment_fidelity` — `PENDING_CLINICAL_EVIDENCE`;
5. `arabic_clinical_parity_gap` — `PENDING_CLINICAL_EVIDENCE`;
6. `lab_report_field_extraction_accuracy` — `PENDING_CLINICAL_EVIDENCE`;
7. `benign_case_over_triage_rate` — `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE`, bound to `FD-004`.

Spec 002 does not manufacture numeric values for these metrics. Zero-violation policy/sentinel mechanics do not imply zero population clinical error.

## 8. External design-evidence boundary

`research.md` records current WHO, FDA and NIST primary guidance used to inform general safety-governance principles. That research is explicitly not a regulatory-compliance determination and is not used to derive unsupported commandMed clinical thresholds.

## 9. Repository-scope activity/authority attestation

For the bounded Spec 002 workflow represented by this branch and its authorized review/validation actions:

```text
MODEL_RUNTIME_OR_DOWNLOADER_ADDED=NO
BENCHMARK_RUNNER_ADDED=NO
TRAINING_LOOP_ADDED=NO
CLINICAL_RED_FLAG_CATALOGUE_ADDED=NO
DRUG_OR_DOSE_DATABASE_ADDED=NO
PATIENT_ADVICE_RUNTIME_ADDED=NO
NETWORK_RUNTIME_ADDED=NO
NEW_THIRD_PARTY_DEPENDENCY=NO
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
```

The project record additionally reports no model downloads/weight loading/inference, benchmark payload execution, training, PHI access, restricted clinical-data access, real-Gold access, or external judge/model calls during the authorized Spec 002 workflow. These are bounded workflow attestations, not claims about activity outside this repository/process.

## 10. Final qualification gate

Before PR #10 may leave Draft, all of the following must be true on one final exact head created by this document's last mutation:

1. `validate_safety_policy` passes on the exact remote artifact;
2. focused Spec 002 tests pass;
3. the complete repository test suite passes;
4. inherited Spec 001 semantic identities remain unchanged;
5. safety-policy semantic SHA-256 remains `79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f`;
6. diff hygiene/scope checks pass;
7. PR body records the exact final candidate head and run/job evidence;
8. fresh exact-head review finds no material blocker.

Until then:

```text
SPEC_002=CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION
PR_10=DRAFT
MERGE_AUTHORITY=NO
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
