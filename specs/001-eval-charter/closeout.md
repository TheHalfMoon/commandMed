# Spec 001 — Evaluation Charter Candidate Evidence

**Closeout type:** governance / evaluation contract implementation
**Status:** CLOSEOUT_CANDIDATE_PENDING_CANONICAL_REVIEW
**Branch:** `spec/001-eval-charter`
**Canonical base commit:** `30283d7d45c1d257f6c448d3648b25034e8ee5d5`
**Spec Kit bootstrap commit:** `489a3d51d152fa160d88d86781a924e99c4af832` (specify v0.15.1)
**State transition rule:** Effective `CLOSED_CANONICAL` state occurs via dedicated closure PR after canonical merge of this implementation PR.

---

## 1. Summary

Spec 001 ("Evaluation Charter") establishes commandMed's evaluation governance, benchmark registry, metrics catalog, hard safety gate semantics, private Gold metadata protocols, quarantine rules, and semantic canonical serialization.

All work strictly adhered to Ponytail discipline and the zero-model / zero-training invariants. No models were downloaded, loaded, or executed; no training or inference occurred; no PHI or real Gold cases were accessed or stored.

---

## 2. Canonical Artifact Identities (SHA-256)

Computed via semantic canonical JSON serialization:

| Artifact Path | Canonical Semantic SHA-256 Digest |
|---|---|
| `data/eval/benchmarks.json` | `9c47b9096ab84d4679c5c0b8fa34d2c0bbd73c76ac77b9f1a7336db4a1f9f9de` |
| `data/eval/gold_protocols.json` | `8e7c8a71e664996e8722adc4a6b32dc712ed59e81fff31053556bf52b465a592` |
| `data/eval/metrics.json` | `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a` |
| `data/eval/quarantine.json` | `b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080` |

---

## 3. Validation & Test Execution

**Command:**
```bash
python -m unittest discover -s tests -p "test_*.py"
```

**Result:**
```text
Ran 46 tests in 0.018s
OK
```

### Coverage Breakdown:
1. `tests/eval_contract/test_registry.py`: Validates canonical benchmark registry, 10 VERIFIED entries and 1 explicitly UNRESOLVED (`medqabstain`), schema validation, fail-closed handling on missing/duplicate/invalid fields, fail-closed rejection of VERIFIED status with UNRESOLVED licenses/sources, fail-closed rejection of DEVELOPMENT use on UNRESOLVED suites, zero payload markers, rejection of `COMPONENT_SPECIFIC` license with executable use, acceptance of `COMPONENT_SPECIFIC` with `REFERENCE_ONLY`, rejection of duplicate set-like metadata values, and corrected canonical source identities (HealthBench bound to official Hugging Face datasets with immutable commits; HealthBench Professional bound to separate official dataset and arXiv:2604.27470; MedHELM bound to arXiv:2505.23802 v2.0.0 with `MIXED`/`COMPONENT_SPECIFIC`/`REFERENCE_ONLY` boundary).
2. `tests/eval_contract/test_hard_gates.py`: Validates metrics catalog, presence of required hard gates, and proves hard-gate dominance (a run with 99.5% accuracy but failing 1 hard gate yields overall `FAIL`; unevaluated hard gates yield `INSUFFICIENT_EVIDENCE`).
3. `tests/eval_contract/test_gold_quarantine.py`: Validates 3 canonical Gold protocols, mandatory power analysis requirement, mandatory optimization prohibitions, rejection of candidate selection scoring stages, zero payload/PHI, quarantine rule validation, rejection of model selection on `PUBLIC_EXTERNAL_EVAL`, evidence-symmetry enforcement (all substantive contamination states `CHECKED_CLEAN`, `OVERLAP_FOUND`, `BLOCKED`, `ASSESSED_LOW_RISK`, `ASSESSED_HIGH_RISK` require resolved evidence identifiers), evidence-bound substantive assessments pass, and validation of baseline `NOT_ASSESSED`/`PENDING` records.
4. `tests/eval_contract/test_canonical.py`: Proves key-order independence, set-like list field reordering invariance, entity collection reordering invariance, SHA-256 digest stability, and semantic mutation sensitivity.

---

## 4. Acceptance Criteria Matrix (12/12 PASS)

| # | Spec 001 Acceptance Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Registry schema/contract exists and validates required metadata | `src/commandmed/eval_contract/validate.py`, `test_registry.py` | PASS |
| 2 | Initial named benchmark families are verified with source evidence or explicitly unresolved | `data/eval/benchmarks.json` (10 VERIFIED with primary/canonical sources bound to immutable revisions, 1 UNRESOLVED `medqabstain` with reference-only restriction; MedHELM family record `REFERENCE_ONLY` with `COMPONENT_SPECIFIC` license boundary) | PASS |
| 3 | Metrics catalog distinguishes optimization metrics from hard gates | `data/eval/metrics.json`, `docs/evaluation/metrics-and-gates.md` | PASS |
| 4 | Synthetic high-average/critical-failure fixture yields overall `FAIL` | `tests/eval_contract/test_hard_gates.py` | PASS |
| 5 | Three Gold protocol records exist without real case content | `data/eval/gold_protocols.json`, `test_gold_quarantine.py` | PASS |
| 6 | Gold quarantine/prohibited-use validation is enforced (including non-selection) | `validate_gold_protocol`, `validate_quarantine_rules` | PASS |
| 7 | Contamination metadata/interface is defined with evidence requirement | `data/eval/quarantine.json`, `test_gold_quarantine.py` (evidence symmetry across all substantive states) | PASS |
| 8 | Canonical serialization is semantic, deterministic, and SHA-256 identity is stable | `src/commandmed/eval_contract/canonical.py`, `test_canonical.py` | PASS |
| 9 | Fixture-only tests cover required failure modes and pass offline | 46 unit tests passing offline with stdlib runner | PASS |
| 10 | No unauthorized dependency or framework introduced | Python 3.11 standard library only; zero external packages | PASS |
| 11 | No model/data execution prohibited by this spec occurred | Zero model downloads, inference, training, PHI, Gold cases | PASS |
| 12 | Closeout evidence follows two-layer evidence protocol | In-tree artifact identities bound here; candidate HEAD recorded in PR/review metadata | PASS |

---

## 5. Unresolved External Facts & Risks

1. **MedQAbstain Licensing Boundary:** Licensing across derived upstream subsets in MedQAbstain remains unverified; classified as `UNRESOLVED` and restricted to `REFERENCE_ONLY`.
2. **MedAbstain Non-Commercial Terms:** MedAbstain is licensed under CC-BY-NC-4.0; classified as `DEVELOPMENT` only.
3. **MedHELM Component Registration:** The MedHELM family record is `REFERENCE_ONLY` with `license_status=COMPONENT_SPECIFIC`. Its 35 component benchmarks (14 public, 7 gated, 14 private) are intentionally NOT individually registered in Spec 001 (Ponytail/YAGNI). Each executable component must be registered individually with exact component identity, access class, license/use rights, revision, and contamination status before commandMed may execute it.
4. **Clinical Metric Thresholds:** Numerical threshold values are intentionally marked `DEFINED_NOT_YET_THRESHOLD_FROZEN` in Spec 001. They will be formally frozen in Spec 002 (Safety Gates) prior to candidate model runs.
5. **Contamination Assessment Pipelines:** Contamination records define the interface with state `NOT_ASSESSED` (evidence: `NONE`); automated token-overlap and embedding decontamination pipelines will be integrated in subsequent specs when candidate corpora exist. Evidence symmetry now requires resolved evidence identifiers for all substantive assessment states.
6. **HealthBench Professional External Implementation:** OpenAI does not release an official external evaluation implementation for HealthBench Professional (internal implementation only; `simple-evals` remains the reference for ordinary HealthBench). Execution harness identity must be resolved before any executable use.

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
