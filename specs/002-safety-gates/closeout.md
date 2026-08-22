# Spec 002 — Safety Gates Candidate Closeout Evidence

**Closeout type:** fixture-only safety-governance implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_FINAL_EXACT_HEAD_RERUN`
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
- deterministic semantic policy identity.

It does not implement a clinical red-flag catalogue, medication database, dose engine, clinical calculator, retrieval service, patient advice runtime, model evaluator, or training system.

## 2. Pre-closeout exact-head validation evidence

GitHub Actions carrier PR #11 validated exact implementation predecessor head:

```text
VALIDATED_PRE_CLOSEOUT_HEAD=a58b4a7788d74d8edc6179e4adb4e603d8e78a98
RUN_ID=32552922513
JOB_ID=96982457564
WORKFLOW=Spec 002 Exact-Head Validation
CONCLUSION=SUCCESS
```

The workflow explicitly checked out detached HEAD `a58b4a7788d74d8edc6179e4adb4e603d8e78a98` rather than the carrier head.

Observed evidence:

```text
EXACT_HEAD=a58b4a7788d74d8edc6179e4adb4e603d8e78a98
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
SAFETY_POLICY_VALIDATION=PASS
FOCUSED_SPEC_002_TESTS=41/41_PASS
FULL_OFFLINE_TESTS=143/143_PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

This is real exact-head predecessor evidence. Because this closeout document and status reconciliation create a newer branch head, this predecessor run is **not** the final candidate-head qualification. A final exact-head rerun is required before Ready/merge.

## 3. Semantic policy identity

The pre-closeout exact-head workflow computed:

```text
data/eval/safety_policy.json=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
```

The same run re-confirmed the four inherited Spec 001 semantic identities with no drift:

```text
data/eval/benchmarks.json=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
data/eval/gold_protocols.json=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
data/eval/metrics.json=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
data/eval/quarantine.json=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
INHERITED_SEMANTIC_IDENTITIES=PASS
```

The final exact-head rerun must re-confirm these identities after this evidence-only mutation.

## 4. Planning/analyze evidence

Spec 002 planning used the repository Spec Kit lifecycle and recorded `analysis.md` before implementation.

The analysis found and repaired two material planning contradictions before code was added:

1. `NOT_APPLICABLE` was initially described as a gate-result state even though canonical Spec 001 `GateEvaluationState` does not contain it. The repair keeps N/A as applicability metadata resolved before hard-gate aggregation.
2. generic N/A semantics could have allowed component scope narrowing to suppress required system safety obligations. The repair separates `SYSTEM_QUALIFICATION` from `COMPONENT_QUALIFICATION`, prevents component PASS promotion to system PASS, and prevents Arabic/patient safety obligations from being waived by scope relabeling.

Analyze verdict:

```text
SPEC_002_ANALYZE=PASS_TO_IMPLEMENT
```

## 5. Acceptance matrix

| # | Spec 002 acceptance criterion | Candidate evidence | Status |
|---|---|---|---|
| 1 | Machine-readable safety-policy contract with stable IDs/closed vocabularies | `data/eval/safety_policy.json` + validator | CANDIDATE_PASS |
| 2 | Unknown/malformed/duplicate policy objects fail cleanly | focused malformed/completeness tests | CANDIDATE_PASS |
| 3 | Required `EMERGENCY`/`ESCALATE` cannot be overridden in sentinels | forced-state tests | CANDIDATE_PASS |
| 4 | Required deterministic/authoritative mechanisms cannot be replaced by guessed prose | truth-boundary validator/evaluator tests | CANDIDATE_PASS |
| 5 | Valid deterministic safety-critical results cannot be altered silently | exact typed-result comparison tests | CANDIDATE_PASS |
| 6 | Missing required information/evidence blocks unsupported answer/pass | precedence + unresolved-evidence tests | CANDIDATE_PASS |
| 7 | Existing gate-result semantics reused; applicability scope cannot hide claimed capability or promote component PASS to system PASS | scope validator/applicability tests | CANDIDATE_PASS |
| 8 | Sentinel zero violations explicitly separated from population zero-error claim | policy classes + documentation + tests | CANDIDATE_PASS |
| 9 | Unsupported statistical thresholds remain pending/non-passable; FD-004 over-triage remains pending | threshold requirement validator/tests | CANDIDATE_PASS |
| 10 | Existing Spec 001 hard-gate identities mapped without weakening | exact metric→capability/class completeness validation | CANDIDATE_PASS |
| 11 | Offline fixture-only tests pass and Spec 001 regression suite remains green | 41 focused + 143 full tests on predecessor exact head | PENDING_FINAL_HEAD |
| 12 | Canonical policy identity and exact-head closeout evidence recorded with no prohibited activity | semantic hash + this two-layer evidence protocol | PENDING_FINAL_HEAD |

Spec 002 MUST NOT be described as `12/12 PASS` until rows 11 and 12 are re-proven on the final exact PR head.

## 6. Pending clinical/founder thresholds

The following population/statistical thresholds remain intentionally unresolved and non-passable until the required evidence is bound:

1. `emergency_miss_rate` — `PENDING_CLINICAL_EVIDENCE`;
2. `medication_critical_error_rate` — `PENDING_CLINICAL_EVIDENCE`;
3. `selective_risk_at_target_coverage` — `PENDING_CLINICAL_EVIDENCE`;
4. `citation_entailment_fidelity` — `PENDING_CLINICAL_EVIDENCE`;
5. `arabic_clinical_parity_gap` — `PENDING_CLINICAL_EVIDENCE`;
6. `lab_report_field_extraction_accuracy` — `PENDING_CLINICAL_EVIDENCE`;
7. `benign_case_over_triage_rate` — `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE`, bound to `FD-004`.

Spec 002 does not manufacture numeric values for these metrics. Zero-violation policy/sentinel mechanics do not imply zero population clinical error.

## 7. External design-evidence boundary

`research.md` records current WHO, FDA and NIST primary guidance used to inform general safety-governance principles. That research is explicitly not a regulatory-compliance determination and is not used to derive unsupported commandMed clinical thresholds.

## 8. Repository-scope activity/authority attestation

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

## 9. Final qualification gate

Before PR #10 may leave Draft, all of the following must be true on one final exact head:

1. Spec 002 status wording is reconciled to closeout-candidate state;
2. `validate_safety_policy` passes on the exact remote artifact;
3. focused Spec 002 tests pass;
4. the complete repository test suite passes;
5. inherited Spec 001 semantic identities remain unchanged;
6. safety-policy semantic SHA-256 is re-confirmed;
7. diff hygiene/scope checks pass;
8. PR body records the exact final candidate head and evidence;
9. fresh exact-head review finds no material blocker.

Until then:

```text
SPEC_002=CLOSEOUT_CANDIDATE_PENDING_FINAL_EXACT_HEAD_RERUN
PR_10=DRAFT
MERGE_AUTHORITY=NO
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
