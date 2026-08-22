# Spec 001 — Evaluation Charter Candidate Evidence

**Closeout type:** governance / evaluation contract implementation
**Status:** `CLOSEOUT_CANDIDATE_PENDING_EXACT_HEAD_VALIDATION`
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

The previous exact-head validation on `fa20facab6f8ef29386809acbbf2522839174856` established these semantic SHA-256 values:

| Artifact Path | Historical digest on `fa20faca...` | Current-head state |
|---|---|---|
| `data/eval/benchmarks.json` | `7bb4f596f843450252b0d5eb18b85b713c7e3f33b41d9b3efb635b6b773e71f7` | **CHANGED — PENDING fresh semantic digest** |
| `data/eval/gold_protocols.json` | `8e7c8a71e664996e8722adc4a6b32dc712ed59e81fff31053556bf52b465a592` | **CHANGED — PENDING fresh semantic digest** |
| `data/eval/metrics.json` | `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a` | unchanged content; digest must still be re-verified at final exact head |
| `data/eval/quarantine.json` | `b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080` | unchanged content; digest must still be re-verified at final exact head |

Do not reuse historical digests as current-head evidence after semantic JSON mutation. Final values must be recomputed with `src.commandmed.eval_contract.canonical.compute_file_canonical_sha256` on the exact candidate head.

---

## 3. Validation & Test Execution

Required exact-head command:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

**Current repaired-head result:** `PENDING_EXACT_HEAD_RERUN`

The prior GitHub-hosted run on `fa20facab6f8ef29386809acbbf2522839174856` reported `86 tests / OK`, but that evidence is historical only. The current head adds external-review reconciliation changes and additional regression tests, so the old count/result MUST NOT be represented as current-head evidence.

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
| 1 | Registry schema/contract exists and validates required metadata | `src/commandmed/eval_contract/validate.py`, registry tests | CANDIDATE_PASS |
| 2 | Named benchmark families verified or explicitly unresolved with executable boundary enforced | `data/eval/benchmarks.json`; executable uses reject `UNBOUND`/`UNRESOLVED` artifact identity | CANDIDATE_PASS |
| 3 | Metrics catalog distinguishes optimization metrics from hard gates | `data/eval/metrics.json`, `docs/evaluation/metrics-and-gates.md` | CANDIDATE_PASS |
| 4 | Critical hard-gate failure dominates aggregate performance | `test_hard_gates.py`; PASS additionally requires score + evidence identifier | CANDIDATE_PASS |
| 5 | Three Gold protocol records exist without real case content | `data/eval/gold_protocols.json` | CANDIDATE_PASS |
| 6 | Gold quarantine/prohibited-use validation is enforced | Gold stage allowlist + quarantine validators/tests | CANDIDATE_PASS |
| 7 | Contamination interface is defined with evidence symmetry | `data/eval/quarantine.json`, validator/tests | CANDIDATE_PASS |
| 8 | Canonical serialization is semantic/deterministic | `canonical.py`, `test_canonical.py` | CANDIDATE_PASS |
| 9 | Fixture-only full suite passes offline on exact candidate head | Fresh run required after current mutations | **PENDING** |
| 10 | No unauthorized runtime dependency introduced | implementation remains Python stdlib-only; exact-head suite still required | CANDIDATE_PASS |
| 11 | Spec 001 repository scope contains no model/training/benchmark execution path | source/diff inspection + Section 6 bounded attestation | CANDIDATE_PASS |
| 12 | Closeout follows two-layer exact-head evidence protocol | in-tree evidence updated; final PR-head + fresh tests/hashes still required | **PENDING** |

Spec 001 MUST NOT be described as `12/12 PASS` until rows 9 and 12 are proven on the final exact head.

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
3. PowerShell/Python Spec Kit repairs receive syntax/behavior validation appropriate to the available runners;
4. all four semantic JSON digests are recomputed and recorded from that exact head;
5. PR body exact-head identity matches the repository head;
6. a fresh independent exact-head review finds no material blocker.

Until then:

```text
SPEC_001=CLOSEOUT_CANDIDATE_PENDING_EXACT_HEAD_VALIDATION
MERGE_AUTHORITY=NO
SPEC_002_PLUS=NOT_STARTED
```
