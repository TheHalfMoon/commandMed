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
| `data/eval/benchmarks.json` | `7bb4f596f843450252b0d5eb18b85b713c7e3f33b41d9b3efb635b6b773e71f7` |
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
Ran 58 tests in 0.035s
OK
```

### Coverage Breakdown:
1. `tests/eval_contract/test_registry.py`: Validates canonical benchmark registry, 10 VERIFIED entries and 1 explicitly UNRESOLVED (`medqabstain`), schema validation, fail-closed handling on missing/duplicate/invalid fields, fail-closed rejection of VERIFIED status with UNRESOLVED licenses/sources, fail-closed rejection of DEVELOPMENT use on UNRESOLVED suites, zero payload markers, rejection of `COMPONENT_SPECIFIC` license with executable use, acceptance of `COMPONENT_SPECIFIC` with `REFERENCE_ONLY`, rejection of duplicate set-like metadata values, corrected canonical source identities (HealthBench bound to official Hugging Face datasets with immutable commits; HealthBench Professional bound to separate official dataset and arXiv:2604.27470; MedHELM bound to arXiv:2505.23802 v2.0.0 with `MIXED`/`COMPONENT_SPECIFIC`/`REFERENCE_ONLY` boundary), truthful HealthBench language/role representation (MULTILINGUAL sentinel; MULTI_ROLE for core/consensus/hard; paper-proven CLINICAL_PROFESSIONAL for Professional), controlled license vocabulary (fake license string fails; all canonical statuses within vocabulary), MedHELM versioned identity URI (v2.0.0, not `/latest/`), and legacy provenance truth (MedMCQA paper arXiv:2203.14371 + MIT + MIXED + non-executable UNBOUND boundary; MedQA variant label never masquerading as source revision + REFERENCE_ONLY; PubMedQA pinned to repository commit + PQA-L git blob as executable DEVELOPMENT; MedXpertQA pinned to official HF dataset revision with split artifacts and preserved quarantine boundary; MedAbstain family COMPONENT_SPECIFIC/MIXED/REFERENCE_ONLY boundary preserving both license facts; and SOURCE_VERIFIED does not imply DEVELOPMENT — every executable DEVELOPMENT asset must be artifact-identity-bound).
2. `tests/eval_contract/test_hard_gates.py`: Validates metrics catalog, presence of required hard gates, and proves hard-gate dominance (a run with 99.5% accuracy but failing 1 hard gate yields overall `FAIL`; unevaluated hard gates yield `INSUFFICIENT_EVIDENCE`).
3. `tests/eval_contract/test_gold_quarantine.py`: Validates 3 canonical Gold protocols, mandatory power analysis requirement, mandatory optimization prohibitions, rejection of candidate selection scoring stages, zero payload/PHI, quarantine rule validation, rejection of model selection on `PUBLIC_EXTERNAL_EVAL`, evidence-symmetry enforcement (all substantive contamination states `CHECKED_CLEAN`, `OVERLAP_FOUND`, `BLOCKED`, `ASSESSED_LOW_RISK`, `ASSESSED_HIGH_RISK` require resolved evidence identifiers), evidence-bound substantive assessments pass, and validation of baseline `NOT_ASSESSED`/`PENDING` records.
4. `tests/eval_contract/test_canonical.py`: Proves key-order independence, set-like list field reordering invariance, entity collection reordering invariance, SHA-256 digest stability, and semantic mutation sensitivity.

---

## 4. Acceptance Criteria Matrix (12/12 PASS)

| # | Spec 001 Acceptance Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Registry schema/contract exists and validates required metadata | `src/commandmed/eval_contract/validate.py`, `test_registry.py` | PASS |
| 2 | Initial named benchmark families are verified with source evidence or explicitly unresolved | `data/eval/benchmarks.json` (10 VERIFIED, 1 UNRESOLVED `medqabstain`). SOURCE/FAMILY VERIFICATION is distinct from EXECUTABLE ARTIFACT IDENTITY: every VERIFIED family has identity/existence/source/license boundary verified against a pinned immutable revision; executable DEVELOPMENT assets (HealthBench family, MedXpertQA, PubMedQA) additionally carry artifact identity inside the pinned revision (exact artifact file / dataset split files / git blob), while MedQA, MedMCQA, MedAbstain, and MedHELM remain VERIFIED + REFERENCE_ONLY until exact artifact/component identity is registered | PASS |
| 3 | Metrics catalog distinguishes optimization metrics from hard gates | `data/eval/metrics.json`, `docs/evaluation/metrics-and-gates.md` | PASS |
| 4 | Synthetic high-average/critical-failure fixture yields overall `FAIL` | `tests/eval_contract/test_hard_gates.py` | PASS |
| 5 | Three Gold protocol records exist without real case content | `data/eval/gold_protocols.json`, `test_gold_quarantine.py` | PASS |
| 6 | Gold quarantine/prohibited-use validation is enforced (including non-selection) | `validate_gold_protocol`, `validate_quarantine_rules` | PASS |
| 7 | Contamination metadata/interface is defined with evidence requirement | `data/eval/quarantine.json`, `test_gold_quarantine.py` (evidence symmetry across all substantive states) | PASS |
| 8 | Canonical serialization is semantic, deterministic, and SHA-256 identity is stable | `src/commandmed/eval_contract/canonical.py`, `test_canonical.py` | PASS |
| 9 | Fixture-only tests cover required failure modes and pass offline | 58 unit tests passing offline with stdlib runner | PASS |
| 10 | No unauthorized dependency or framework introduced | Python 3.11 standard library only; zero external packages | PASS |
| 11 | No model/data execution prohibited by this spec occurred | Zero model downloads, inference, training, PHI, Gold cases | PASS |
| 12 | Closeout evidence follows two-layer evidence protocol | In-tree artifact identities bound here; candidate HEAD recorded in PR/review metadata | PASS |

---

## 5. Unresolved External Facts & Risks

1. **MedQAbstain Licensing Boundary:** Licensing across derived upstream subsets in MedQAbstain remains unverified; classified as `UNRESOLVED` and restricted to `REFERENCE_ONLY`.
2. **MedMCQA Executable Artifact Boundary:** Family identity is VERIFIED (paper arXiv:2203.14371; MIT per LICENSE.md at pinned commit c59ef14ca1990266c4107c7864b45a20fd93e5e0), but the data is distributed separately via Google Drive and the official public test-set ground truth is withheld (submission-based evaluation). No executable MedMCQA component may be declared until its exact artifact/split identity is registered; Google Drive data is NOT downloaded in Spec 001.
3. **MedQA Executable Artifact Boundary:** Family identity is VERIFIED (arXiv:2009.13081; MIT at pinned commit 27b02f66aac217933c9648a06f82e9f720377925), but the QA/textbook dataset bytes are distributed externally via Google Drive and are not yet cryptographically/immutably bound by commandMed; the record stays `REFERENCE_ONLY` until artifact/split identity is registered.
4. **MedAbstain Component Rights Boundary:** Family identity is VERIFIED at pinned commit 091e5c22111fffeb51c0c2e69b65d0a21a1e4164 (paper arXiv:2601.12471, EACL 2026). MedAbstain's own released work/code is CC-BY-NC-4.0, but the benchmark is built over component datasets (MedQA-derived files present in the repository; amboss construction scripts). The family is `COMPONENT_SPECIFIC` + `REFERENCE_ONLY`; executable components retain their own upstream access/license/usage requirements and must be registered separately before execution. Components intentionally not registered in Spec 001 (Ponytail/YAGNI); MedAbstain not executed.
5. **MedHELM Component Registration:** The MedHELM family record is `REFERENCE_ONLY` with `license_status=COMPONENT_SPECIFIC`, pinned to the versioned identity URI `https://crfm.stanford.edu/helm/medhelm/v2.0.0/`. Its 35 component benchmarks (14 public, 7 gated, 14 private) are intentionally NOT individually registered in Spec 001 (Ponytail/YAGNI). Each executable component must be registered individually with exact component identity, access class, license/use rights, revision, and contamination status before commandMed may execute it.
6. **HealthBench Exact Language Inventory Not Enumerated:** The HealthBench family records use the `MULTILINGUAL` sentinel because the primary sources explicitly describe the benchmarks as multilingual without enumerating an exact language inventory (49/52 contributor-physician languages are a contributor fact, not a benchmark inventory). Deriving an exact inventory would require artifact case inspection under a recorded evidence method in a later authorized spec.
7. **Clinical Metric Thresholds:** Numerical threshold values are intentionally marked `DEFINED_NOT_YET_THRESHOLD_FROZEN` in Spec 001. They will be formally frozen in Spec 002 (Safety Gates) prior to candidate model runs.
8. **Contamination Assessment Pipelines:** Contamination records define the interface with state `NOT_ASSESSED` (evidence: `NONE`); automated token-overlap and embedding decontamination pipelines will be integrated in subsequent specs when candidate corpora exist. Evidence symmetry now requires resolved evidence identifiers for all substantive assessment states.
9. **HealthBench Professional External Implementation:** OpenAI does not release an official external evaluation implementation for HealthBench Professional (internal implementation only; `simple-evals` remains the reference for ordinary HealthBench). Execution harness identity must be resolved before any executable use.

---

## 6. Activity Attestations

```text
MODEL_DOWNLOADS=0
MODEL_WEIGHTS_LOADED=0
MODEL_INFERENCE_RUNS=0
BENCHMARK_PAYLOAD_DOWNLOADS=0
BENCHMARK_EXECUTION_RUNS=0
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
