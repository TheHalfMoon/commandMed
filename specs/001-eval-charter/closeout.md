# Spec 001 — Evaluation Charter Candidate Evidence

**Closeout type:** governance / evaluation contract implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_FINAL_EXACT_HEAD_RERUN`
**Branch:** `spec/001-eval-charter`
**Canonical base commit:** `30283d7d45c1d257f6c448d3648b25034e8ee5d5`
**Spec Kit bootstrap commit:** `489a3d51d152fa160d88d86781a924e99c4af832` (`specify` v0.15.1)
**State transition rule:** `CLOSED_CANONICAL` occurs only through a dedicated closure PR after canonical merge of this implementation PR.

---

## 1. Summary

Spec 001 ("Evaluation Charter") establishes commandMed's evaluation governance, benchmark registry, metrics catalog, hard-safety-gate semantics, private Gold metadata protocols, quarantine rules, contamination-evidence interface, and semantic canonical serialization.

The implementation is metadata/governance and fixture-test scoped. It introduces no model runtime, training loop, benchmark downloader, benchmark executor, PHI ingestion path, or real-Gold case payload. Repository-scope activity attestations are recorded in Section 6; they are not claims about activity outside the authorized commandMed Spec 001 workflow.

---

## 2. Canonical Artifact Identities

GitHub Actions run `32551171859`, job `96978051918`, explicitly checked out candidate commit `031c22964a2733c9dce75b0b9895a666aa7212f9` and computed these semantic SHA-256 values with `src.commandmed.eval_contract.canonical.compute_file_canonical_sha256`:

| Artifact Path | Semantic SHA-256 |
|---|---|
| `data/eval/benchmarks.json` | `7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7` |
| `data/eval/gold_protocols.json` | `40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666` |
| `data/eval/metrics.json` | `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a` |
| `data/eval/quarantine.json` | `b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080` |

The only source mutation after that run is this closeout evidence update; no canonical JSON artifact is modified by this evidence-only commit. A final exact-head rerun is still required because exact-head qualification binds to the final PR head, not merely to content-equivalent predecessor evidence.

---

## 3. Validation & Test Execution

Required command:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

GitHub Actions validation carrier PR #7 ran workflow `Spec 001 Final Exact-Head Validation` on exact detached HEAD `031c22964a2733c9dce75b0b9895a666aa7212f9`.

Observed result:

```text
Ran 102 tests in 0.013s
OK
```

The same job also proved:

```text
PYTHON_SYNTAX=PASS
POWERSHELL_PARSE=PASS
SETUP_PLAN_UNKNOWN_ARG_EXIT=1
GIT_DIFF_CHECK=PASS
```

Run identity:

```text
RUN_ID=32551171859
JOB_ID=96978051918
VALIDATED_HEAD=031c22964a2733c9dce75b0b9895a666aa7212f9
```

Because this document update creates a new commit, the final PR head still requires one final rerun of the same gates. The 102-test result above is real predecessor evidence and MUST NOT be silently treated as final-head evidence.

### Required coverage before qualification

1. `test_registry.py`: benchmark registry schema, license vocabulary, source truth, executable/reference-only boundaries, and contamination-sensitive metadata.
2. `test_hard_gates.py`: hard-gate dominance, missing-gate failure, malformed metric rejection, and evidence-bearing PASS semantics.
3. `test_gold_quarantine.py`: three Gold protocols, non-selection, power analysis, quarantine matrix, and contamination evidence symmetry.
4. `test_canonical.py`: deterministic semantic serialization and digest invariance/sensitivity.
5. `test_fail_closed.py`: malformed JSON, impossible dates, empty gates, and quarantine fail-closed behavior.
6. `test_external_review_reconciliation.py`: executable artifact identity boundary, whitespace-normalized unresolved sentinel rejection, Gold scoring-stage allowlist, and immutable MedHELM license evidence.
7. `test_speckit_external_review.py`: PowerShell `$PID` collision regression, portable feature path persistence, setup-plan fail-closed behavior, and spec-before-plan prerequisite ordering.

---

## 4. Acceptance Criteria Matrix

| # | Spec 001 Acceptance Criterion | Current evidence | Status |
|---|---|---|---|
| 1 | Registry schema/contract exists and validates required metadata | validator + registry tests | CANDIDATE_PASS |
| 2 | Named benchmark families verified or explicitly unresolved with executable boundary enforced | registry + executable-use fail-closed validation | CANDIDATE_PASS |
| 3 | Metrics catalog distinguishes optimization metrics from hard gates | metrics catalog + governance docs | CANDIDATE_PASS |
| 4 | Critical hard-gate failure dominates aggregate performance | hard-gate tests; PASS requires score + evidence identifier | CANDIDATE_PASS |
| 5 | Three Gold protocol records exist without real case content | Gold protocol metadata | CANDIDATE_PASS |
| 6 | Gold quarantine/prohibited-use validation is enforced | stage allowlist + quarantine validators/tests | CANDIDATE_PASS |
| 7 | Contamination interface is defined with evidence symmetry | quarantine metadata + validator/tests | CANDIDATE_PASS |
| 8 | Canonical serialization is semantic/deterministic | canonical serializer + tests | CANDIDATE_PASS |
| 9 | Fixture-only full suite passes offline | 102/102 PASS on immediate predecessor `031c229...`; final-head rerun required | PENDING_FINAL_HEAD |
| 10 | No unauthorized runtime dependency introduced | Python 3.11 stdlib-only implementation; syntax gate passed | CANDIDATE_PASS |
| 11 | Spec 001 repository scope contains no model/training/benchmark execution path | source/diff inspection + Section 6 bounded attestation | CANDIDATE_PASS |
| 12 | Closeout follows two-layer exact-head evidence protocol | in-tree evidence recorded; final exact-head external evidence still required | PENDING_FINAL_HEAD |

Spec 001 MUST NOT be described as `12/12 PASS` until rows 9 and 12 are proven on the final exact PR head.

---

## 5. Unresolved External Facts & Risks

1. **MedQAbstain licensing:** remains `UNRESOLVED` and `REFERENCE_ONLY`.
2. **MedMCQA executable artifact:** family identity is verified, but externally distributed bytes and withheld official test ground truth are not identity-bound; the record stays `REFERENCE_ONLY`.
3. **MedQA executable artifact:** family identity is verified, but externally distributed dataset bytes are not identity-bound; the record stays `REFERENCE_ONLY`.
4. **MedAbstain component rights:** family is `COMPONENT_SPECIFIC + REFERENCE_ONLY`; each executable component requires separate upstream access/license registration.
5. **MedHELM components:** family is `REFERENCE_ONLY`; its 35 components (14 public, 7 gated, 14 private) require individual registration before execution. HELM framework license evidence is pinned independently and does not license component data.
6. **HealthBench language inventory:** `MULTILINGUAL` is a sentinel because primary sources do not enumerate a complete benchmark-language inventory.
7. **Clinical metric thresholds:** remain `DEFINED_NOT_YET_THRESHOLD_FROZEN`; threshold freezing belongs to later authorized safety-gate work, not this implementation candidate.
8. **Contamination pipelines:** interface exists, but substantive assessments require separately produced evidence artifacts in later authorized work.
9. **HealthBench Professional external harness:** executable harness identity remains unresolved before use.

---

## 6. Repository-Scope Activity Attestation

For the bounded Spec 001 repository workflow represented by this PR and the actions explicitly authorized in its review history:

```text
MODEL_RUNTIME_OR_DOWNLOADER_ADDED=NO
TRAINING_LOOP_ADDED=NO
BENCHMARK_PAYLOAD_DOWNLOADER_ADDED=NO
BENCHMARK_EXECUTOR_ADDED=NO
PHI_INGESTION_PATH_ADDED=NO
REAL_GOLD_CASE_PAYLOAD_ADDED=NO
MODEL_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEC_002_PLUS=NOT_STARTED
```

The project record additionally reports no model downloads, weight loading, inference, benchmark payload execution, training, PHI access, restricted clinical-data access, real-Gold case access, or external judge calls during the authorized Spec 001 workflow. Those are workflow attestations, not independently observable claims about activity outside this repository/process.

---

## 7. Final Qualification Gate

Before PR #3 may return to Ready-for-review status, all of the following must be true on one exact head:

1. every material external-review thread is resolved or explicitly reconciled with evidence;
2. `python -m unittest discover -s tests -p "test_*.py"` passes on that exact head;
3. PowerShell/Python Spec Kit repairs pass syntax/behavior validation;
4. all four semantic JSON digests are recomputed or re-confirmed on that exact head;
5. `git diff --check` passes;
6. PR body exact-head identity matches the repository head;
7. fresh exact-head external review finds no material blocker.

Until then:

```text
SPEC_001=CLOSEOUT_CANDIDATE_PENDING_FINAL_EXACT_HEAD_RERUN
MERGE_AUTHORITY=NO
SPEC_002_PLUS=NOT_STARTED
```
