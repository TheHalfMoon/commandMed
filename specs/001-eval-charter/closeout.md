# Spec 001 — Evaluation Charter Closeout Evidence

**Closeout type:** governance / evaluation contract implementation
**Branch:** `spec/001-eval-charter`
**Canonical base commit:** `30283d7d45c1d257f6c448d3648b25034e8ee5d5`
**Spec Kit bootstrap commit:** `489a3d51d152fa160d88d86781a924e99c4af832` (specify v0.15.1)
**Status:** CLOSEOUT_CANDIDATE_PENDING_CANONICAL_REVIEW
**State transition rule:** Effective CLOSED_CANONICAL state occurs via dedicated closure PR after canonical merge of this implementation PR.

---

## 1. Summary

Spec 001 ("Evaluation Charter") establishes commandMed's evaluation governance, benchmark registry, metrics catalog, hard safety gate semantics, private Gold metadata protocols, quarantine rules, and deterministic canonical serialization.

All work strictly adhered to Ponytail discipline and the zero-model / zero-training invariants. No models were downloaded, loaded, or executed; no training or inference occurred; no PHI or real Gold cases were accessed or stored.

---

## 2. Canonical Artifact Identities (SHA-256)

| Artifact Path | Canonical JSON SHA-256 Digest |
|---|---|
| `data/eval/benchmarks.json` | `f1e97d772be6c6912a8009003bbd03d8243bdaf109787ae1f0b4dc26ac37edc6` |
| `data/eval/gold_protocols.json` | `33eaf46a6a1f275726758e65af68290fac72ccb59cc07273f4d0b0fce41c1ec4` |
| `data/eval/metrics.json` | `0c6acc6221c540a8ea610241e9549d50bda30ff205a3ef93df788c9b72c3dc3f` |
| `data/eval/quarantine.json` | `34b4aeb07d2b886882dca2d4e510d8ca4b3640f65e42a64aa708681d061f1b0e` |

---

## 3. Validation & Test Execution

**Command:**
```bash
python -m unittest discover -s tests -p "test_*.py"
```

**Result:**
```text
Ran 26 tests in 0.012s
OK
```

### Coverage Breakdown:
1. `tests/eval_contract/test_registry.py`: Validates canonical benchmark registry, all 11 required FR-002 families, schema validation, fail-closed handling on missing/duplicate/invalid fields, and zero payload markers.
2. `tests/eval_contract/test_hard_gates.py`: Validates metrics catalog, presence of required hard gates, and proves hard-gate dominance (a run with 99.5% accuracy but failing 1 hard gate yields overall `FAIL`; unevaluated hard gates yield `INSUFFICIENT_EVIDENCE`).
3. `tests/eval_contract/test_gold_quarantine.py`: Validates 3 canonical Gold protocols, mandatory power analysis requirement, mandatory optimization prohibitions, zero payload/PHI, quarantine rule validation, and contamination interface records.
4. `tests/eval_contract/test_canonical.py`: Proves key-order independence, byte-identical canonical JSON serialization, SHA-256 digest stability, and semantic mutation sensitivity.

---

## 4. Acceptance Criteria Matrix (12/12 PASS)

| # | Spec 001 Acceptance Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Registry schema/contract exists and validates required metadata | `src/commandmed/eval_contract/validate.py`, `test_registry.py` | PASS |
| 2 | Initial named benchmark families are verified with source evidence or explicitly unresolved | `data/eval/benchmarks.json` (11/11 verified with primary sources) | PASS |
| 3 | Metrics catalog distinguishes optimization metrics from hard gates | `data/eval/metrics.json`, `docs/evaluation/metrics-and-gates.md` | PASS |
| 4 | Synthetic high-average/critical-failure fixture yields overall `FAIL` | `tests/eval_contract/test_hard_gates.py` | PASS |
| 5 | Three Gold protocol records exist without real case content | `data/eval/gold_protocols.json`, `test_gold_quarantine.py` | PASS |
| 6 | Gold quarantine/prohibited-use validation is enforced | `validate_gold_protocol`, `validate_quarantine_rules` | PASS |
| 7 | Contamination metadata/interface is defined | `data/eval/quarantine.json`, `test_gold_quarantine.py` | PASS |
| 8 | Canonical serialization is deterministic and SHA-256 identity is stable | `src/commandmed/eval_contract/canonical.py`, `test_canonical.py` | PASS |
| 9 | Fixture-only tests cover required failure modes and pass offline | 26 unit tests passing offline with stdlib runner | PASS |
| 10 | No unauthorized dependency or framework introduced | Python 3.11 standard library only; zero external packages | PASS |
| 11 | No model/data execution prohibited by this spec occurred | Zero model downloads, inference, training, PHI, Gold cases | PASS |
| 12 | Closeout evidence binds results to exact HEAD and artifact identities | This closeout document | PASS |

---

## 5. Unresolved External Facts & Risks

1. **Benchmark Licensing Boundaries:** Certain public benchmark suites (e.g. MedXpertQA under CC-BY-NC-4.0) have non-commercial terms. These are classified as `DEVELOPMENT` only and cannot be used in commercial deployment pipelines without license clearance.
2. **Clinical Metric Thresholds:** Numerical threshold values are intentionally marked `DEFINED_NOT_YET_THRESHOLD_FROZEN` in Spec 001. They must be formally frozen in Spec 002 (Safety Gates) prior to candidate model tournament runs.
3. **Semantic Contamination Tooling:** Spec 001 establishes the contamination interface and exact-match checks; production semantic embedding overlap models remain to be integrated in later specs.

---

## 6. Activity Attestations

```text
MODEL_DOWNLOADS=0
MODEL_WEIGHTS_LOADED=0
MODEL_INFERENCE_RUNS=0
TRAINING_RUNS=0
CPT_RUNS=0
SFT_LORA_QLORA_RUNS=0
DISTILLATION_RUNS=0
DPO_GRPO_RL_RUNS=0
QAT_RUNS=0
PHI_ACCESSED=0
RESTRICTED_CLINICAL_DATA_ACCESSED=0
REAL_GOLD_CASES_CREATED_OR_ACCESSED=0
EXTERNAL_JUDGE_APIS_CALLED=0
SPEC_002_PLUS=NOT_STARTED
```
