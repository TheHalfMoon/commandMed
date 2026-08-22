# Spec 002 — Safety Gates Candidate Closeout Evidence

**Closeout type:** fixture-only safety-governance implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION`
**Canonical starting base:** `cc02b0d99d67e5a720502953c99307c8b991720d`
**Implementation branch:** `spec/002-safety-gates`
**State transition rule:** implementation merge does not make Spec 002 `CLOSED_CANONICAL`; a dedicated post-merge closure-only PR remains required.

## 1. Purpose

Record implementation-candidate evidence for the bounded Spec 002 Safety Gates contract without claiming model, benchmark, patient, or real-world clinical performance.

Spec 002 implements declarative/offline mechanics for:

- canonical behavioral-state and forced-state precedence;
- deterministic/authoritative truth-boundary governance;
- system-vs-component applicability rules;
- policy/sentinel zero-violation semantics;
- pending population clinical-threshold provenance requirements;
- deterministic semantic policy identity;
- fail-closed malformed policy, scope, and synthetic-fixture handling;
- policy-aware qualification preconditioning followed by canonical Spec 001 `evaluate_hard_gates()` aggregation.

It does not implement a clinical red-flag catalogue, medication database, dose engine, clinical calculator, retrieval service, patient advice runtime, model evaluator, or training system.

## 2. Latest implementation-proven exact-head evidence

GitHub Actions carrier PR #21 independently validated the pending-gate-repaired implementation predecessor head:

```text
VALIDATED_IMPLEMENTATION_HEAD=3f728586fb76de623db069c883cff51ed78daf99
RUN_ID=32592762187
JOB_ID=97079017593
WORKFLOW=Spec 002 P1 Exact-Head Validation
CONCLUSION=SUCCESS
```

The workflow explicitly checked out detached HEAD `3f728586fb76de623db069c883cff51ed78daf99` rather than the carrier head.

Observed evidence:

```text
EXACT_HEAD=3f728586fb76de623db069c883cff51ed78daf99
PYTHON_VERSION=3.11.16
PYTHON_SYNTAX=PASS
SAFETY_POLICY_VALIDATION=PASS
FOCUSED_SPEC_002_TESTS=54/54_PASS
HARD_GATE_INTEGRATION_TESTS=9/9_PASS
FULL_OFFLINE_TESTS=157/157_PASS
SEMANTIC_IDENTITIES=PASS
GIT_DIFF_CHECK=PASS
BOUNDED_PATH_PREFLIGHT=PASS
```

This run includes malformed-input hardening, exact-state and aggregation reconciliation, truth-boundary fixture identity, and pending statistical-gate qualification preconditioning. It supersedes earlier predecessor runs as implementation evidence.

Because this closeout evidence file itself creates a newer branch head, the SHA above is intentionally an **implementation predecessor**, not the final PR-head qualification. The final PR head must be rerun after this file's last content mutation.

## 3. External review reconciliation

Material external-review findings were verified against live code and repaired before this closeout candidate:

1. **Canonical hard-gate aggregation reuse** — qualification-level safety result records ultimately flow through the existing Spec 001 `evaluate_hard_gates()` implementation; no second aggregator is authorized.
2. **Forced-state exact equality** — identity-bound forced `EMERGENCY` or `ESCALATE` sentinels pass only when the observed state exactly equals the required state.
3. **Mixed required-gate precedence** — any observed hard-gate `FAIL` dominates missing/incomplete evidence; regression coverage preserves this precedence.
4. **Truth-boundary fixture identity** — promoted synthetic truth-boundary results require resolved `fixture_id`, `boundary_id`, `evidence_artifact_id`, and configured result identity fields; missing/unresolved identity is insufficient evidence.
5. **Dynamic PR lifecycle state** — Draft/Ready is external GitHub metadata and is not frozen as a current-state assertion inside this artifact. Ready never grants merge authority by itself.
6. **Pending statistical gates must not qualify** — an all-`PASS` numeric/evidenced result set cannot qualify while any applicable safety-policy gate remains `NO_PASS_UNTIL_FROZEN`. `evaluate_safety_qualification_hard_gates()` validates policy/scope, removes known gates proven not applicable to the declared scope, converts applicable pending gates to `INSUFFICIENT_EVIDENCE` unless a stronger fail-closed result already applies, and then delegates final precedence/overall state to `evaluate_hard_gates()`.

Regression coverage additionally proves that the pending-gate adapter never weakens an observed `FAIL` and that component qualification excludes known not-applicable gates before canonical aggregation.

Temporary repair carrier PR #20 and validation carrier PR #21 were closed without merge.

## 4. Final-head evidence binding without self-reference

This closeout file MUST NOT be mutated merely to embed the SHA produced by its own mutation. That would create an endless self-reference cycle.

Final exact-head qualification is therefore bound through immutable GitHub evidence external to this file:

1. a GitHub-hosted validation workflow explicitly checks out the final PR head SHA;
2. run/job IDs and exact outputs are recorded in PR #10 metadata;
3. an exact-head review is anchored to the same final SHA;
4. any repository-content head mutation invalidates qualification and requires a new run/review.

PR #10 Draft/Ready state is also external GitHub metadata. The durable invariant frozen here is that Ready state alone never grants merge authority: `MERGE_AUTHORITY=NO` remains true until external exact-head validation/review gates are satisfied on an unchanged head and guarded merge is explicitly performed.

After this document's final mutation, no further repository-content change is permitted before qualification unless a material defect is discovered.

## 5. Semantic policy identity

The latest implementation-proven run re-confirmed:

```text
data/eval/benchmarks.json=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
data/eval/gold_protocols.json=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
data/eval/metrics.json=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
data/eval/quarantine.json=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
data/eval/safety_policy.json=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
SEMANTIC_IDENTITIES=PASS
```

The final external exact-head run must re-confirm these identities after this evidence-only mutation.

## 6. Planning/analyze evidence

Spec 002 planning used the repository Spec Kit lifecycle and recorded `analysis.md` before implementation.

Planning repaired two material contradictions before code was added:

1. `NOT_APPLICABLE` remains applicability metadata, not a new Spec 001 gate-result state.
2. component scope narrowing cannot suppress required system safety obligations or promote component PASS to system PASS.

Independent implementation review then repaired malformed-input crash surfaces and later exact-head review tightened policy-aware qualification without changing the canonical safety-policy semantic identity.

Analyze verdict:

```text
SPEC_002_ANALYZE=PASS_TO_IMPLEMENT
```

## 7. Acceptance matrix

| # | Spec 002 acceptance criterion | Candidate evidence | Status |
|---|---|---|---|
| 1 | Machine-readable safety-policy contract with stable IDs/closed vocabularies | `data/eval/safety_policy.json` + validator | CANDIDATE_PASS |
| 2 | Unknown/malformed/duplicate policy objects fail cleanly | malformed scalar/collection/completeness regression matrix | CANDIDATE_PASS |
| 3 | Required `EMERGENCY`/`ESCALATE` exact sentinel states cannot be overridden | exact forced-state tests + repaired SP-001 contract | CANDIDATE_PASS |
| 4 | Required deterministic/authoritative mechanisms cannot be replaced by guessed prose | truth-boundary validator/evaluator tests | CANDIDATE_PASS |
| 5 | Valid deterministic safety-critical results cannot be altered silently | exact typed-result comparison tests | CANDIDATE_PASS |
| 6 | Missing required information/evidence/fixture identity blocks unsupported answer/pass | precedence + unresolved-evidence/fixture tests | CANDIDATE_PASS |
| 7 | Applicability scope cannot hide claimed capability or promote component PASS to system PASS | scope validation + scoped prequalification tests | CANDIDATE_PASS |
| 8 | Sentinel zero violations explicitly separated from population zero-error claim | policy classes + documentation + tests | CANDIDATE_PASS |
| 9 | Applicable `NO_PASS_UNTIL_FROZEN` statistical gates cannot become qualification PASS | policy-aware prequalification + all-PASS regression | CANDIDATE_PASS |
| 10 | Existing Spec 001 hard-gate identities/precedence remain canonical | adapter delegates final aggregation to `evaluate_hard_gates()` + FAIL-preservation regression | CANDIDATE_PASS |
| 11 | Offline fixture-only tests pass and Spec 001 regression suite remains green | 54 focused + 9 hard-gate + 157 full tests on exact implementation predecessor | PENDING_FINAL_PR_HEAD |
| 12 | Canonical policy identity and exact-head closeout evidence recorded with no prohibited activity | semantic hashes + external final-head binding protocol | PENDING_FINAL_PR_HEAD |

Spec 002 MUST NOT be described as `12/12 PASS` until rows 11 and 12 are re-proven on the final exact PR head after this file's last mutation.

## 8. Pending clinical/founder thresholds

Population/statistical thresholds remain intentionally unresolved and non-passable until required evidence is bound. `NO_PASS_UNTIL_FROZEN` applies to the corresponding qualification gates; frozen zero-violation sentinel mechanics remain distinct from population performance claims.

Pending families include:

1. `emergency_miss_rate` — population threshold `PENDING_CLINICAL_EVIDENCE`;
2. `medication_critical_error_rate` — population threshold `PENDING_CLINICAL_EVIDENCE`;
3. `selective_risk_at_target_coverage` — qualification gate `NO_PASS_UNTIL_FROZEN`;
4. `citation_entailment_fidelity` — population threshold `PENDING_CLINICAL_EVIDENCE` while its unsupported-evidence sentinel remains a frozen mechanic;
5. `arabic_clinical_parity_gap` — qualification gate `NO_PASS_UNTIL_FROZEN`;
6. `lab_report_field_extraction_accuracy` — qualification gate `NO_PASS_UNTIL_FROZEN` when applicable;
7. `benign_case_over_triage_rate` — `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE`, bound to `FD-004`.

Spec 002 does not manufacture numeric population thresholds. Zero-violation policy/sentinel mechanics do not imply zero population clinical error.

## 9. External design-evidence boundary

`research.md` records WHO, FDA and NIST primary guidance used to inform general safety-governance principles. That research is not a regulatory-compliance determination and is not used to derive unsupported commandMed clinical thresholds.

## 10. Repository-scope activity/authority attestation

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

The bounded Spec 002 workflow did not authorize model downloads/weight loading/inference, benchmark payload execution, training, PHI access, restricted clinical-data access, real-Gold access, or external judge/model calls.

## 11. Final qualification gate

Before guarded merge of PR #10, all of the following must be true on one unchanged final exact head created by this document's last repository-content mutation:

1. `validate_safety_policy` passes on the exact remote artifact;
2. focused Spec 002 and hard-gate integration tests pass;
3. pending `NO_PASS_UNTIL_FROZEN` qualification regressions pass;
4. the complete repository test suite passes;
5. inherited Spec 001 semantic identities remain unchanged;
6. safety-policy semantic SHA-256 remains `79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f`;
7. diff hygiene/scope checks pass;
8. PR body records the exact final candidate head and run/job evidence;
9. all material external-review findings are reconciled;
10. fresh exact-head independent review finds no material blocker;
11. GitHub PR metadata shows PR #10 Ready on the same exact head immediately before merge.

Until all merge gates are satisfied:

```text
SPEC_002=CLOSEOUT_CANDIDATE_PENDING_EXTERNAL_EXACT_HEAD_QUALIFICATION
PR_10_LIFECYCLE_STATE=EXTERNAL_GITHUB_METADATA
MERGE_AUTHORITY=NO
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
