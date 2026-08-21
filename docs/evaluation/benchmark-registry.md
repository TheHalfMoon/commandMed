# commandMed Benchmark Registry

**Status:** SPEC_001_CLOSEOUT_CANDIDATE — BECOMES CANONICAL ONLY AFTER SPEC 001 CLOSURE
**Spec:** `specs/001-eval-charter`

## 1. Overview

The commandMed Benchmark Registry provides a deterministic, machine-readable inventory of external and public evaluation suites used during research and development. In accordance with Constitutional Principle I (*Evidence Before Training*) and Principle III (*Provenance, Licensing, and Data Lineage*), no benchmark may be used without explicit verification of its canonical source, access classification, license terms, and contamination sensitivity.

Public benchmark performance constitutes development evidence only; public benchmark wins cannot authorize clinical release claims.

## 2. Initial Benchmark Inventory & Verification Status

| Benchmark ID | Canonical Name | Primary Source Identifier | Access Class | License Status | Languages | Modalities | Roles | Contamination Sensitivity | Intended Use | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `healthbench_consensus` | HealthBench Consensus | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_core` | HealthBench Core | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_hard` | HealthBench Hard | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_professional` | HealthBench Professional | huggingface:datasets/openai/healthbench-professional @ 349962fd (arXiv:2604.27470) | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medabstain` | MedAbstain: Knowing When to Abstain | ACL-Anthology-2026.eacl-long.291 | `PUBLIC` | `CC-BY-NC-4.0` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL` | `MEDIUM` | `DEVELOPMENT` | `VERIFIED` |
| `medhelm` | MedHELM: Holistic Evaluation of LLMs for Medical Tasks | arXiv:2505.23802 (v2.0.0) | `MIXED` | `COMPONENT_SPECIFIC` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `REFERENCE_ONLY` | `VERIFIED` |
| `medmcqa` | MedMCQA Medical Entrance Exams | arXiv:2203.14381 | `PUBLIC` | `Apache-2.0` | `en` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqa_usmle` | MedQA (USMLE 4-Option) | arXiv:2009.13081 | `PUBLIC` | `MIT` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqabstain` | MedQAbstain: LLMs (Almost) Never Abstain | ACL-Anthology-2026.acl-long.1365 | `PUBLIC` | `UNRESOLVED` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `PATIENT_CAREGIVER` | `MEDIUM` | `REFERENCE_ONLY` | `UNRESOLVED` |
| `medxpertqa` | MedXpertQA Expert Medical QA | arXiv:2501.18362 | `PUBLIC` | `MIT` | `en` | `MULTIMODAL`, `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `pubmedqa` | PubMedQA Biomedical Research QA | arXiv:1909.06146 | `PUBLIC` | `MIT` | `en` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |

### 2.1 HealthBench Source Identity

The canonical current source for ordinary HealthBench (core/consensus/hard) is the official Hugging Face dataset `openai/healthbench` (MIT licensed), not the former GitHub repository reference. Each record is bound to an exact artifact file and the immutable upstream dataset commit `40ee1968852fc57f625934251ac22be47077a8fb`:

- `healthbench_core` → `2025-05-07-06-14-12_oss_eval.jsonl`
- `healthbench_consensus` → `consensus_2025-05-09-20-00-46.jsonl`
- `healthbench_hard` → `hard_2025-05-08-21-00-10.jsonl`

HealthBench Professional is a SEPARATE official dataset, `openai/healthbench-professional` (MIT licensed, 525 examples, artifact `healthbench_professional_eval.jsonl`), pinned to immutable dataset commit `349962fd46dd02343a0d8a606491baf59154ea1a`, with paper identity arXiv:2604.27470. It must not be conflated with ordinary HealthBench.

### 2.1.1 HealthBench Language and Role Truth

Per the HealthBench paper (arXiv:2505.08775), the 5,000 conversations "span a wide range of geographies, languages, and healthcare personas" between "an individual user or healthcare professional"; contributing physicians contributed data in 49 languages, and the official artifacts contain non-English conversations. The primary source does NOT enumerate an exact language inventory. Accordingly:

- `healthbench_core`, `healthbench_consensus`, `healthbench_hard`, and `healthbench_professional` record `languages=["MULTILINGUAL"]`.
- **`MULTILINGUAL` sentinel semantics:** it asserts only that the primary source explicitly describes the benchmark as multilingual. It does NOT enumerate an exact language inventory and does NOT mean all contributor languages (49 for HealthBench, 52 for HealthBench Professional) are necessarily represented. No individual language codes are invented.
- HealthBench Consensus is the criteria-filtered subset retaining 3,671 examples with at least one positive consensus criterion; HealthBench Hard is the difficulty-selected subset of 1,000 examples. Neither filter is language-based, so no English-only restriction is recorded.
- Because Consensus and Hard are defined by criteria/difficulty filtering rather than role filtering, and their exact role composition is not established without case inspection, `healthbench_core`, `healthbench_consensus`, and `healthbench_hard` record the broad `MULTI_ROLE` representation rather than clinician-only or guessed patient-role claims. `healthbench_professional` retains `CLINICAL_PROFESSIONAL` because its primary source independently proves it: every example is a physician-authored conversation with ChatGPT for Clinicians.

### 2.2 MedHELM Mixed-Family License Boundary

MedHELM (arXiv:2505.23802, release v2.0.0: 35 benchmarks = 14 public + 7 gated + 14 private) is a mixed-access evaluation framework. Its family record uses `access_class=MIXED`, `license_status=COMPONENT_SPECIFIC`, `intended_use=REFERENCE_ONLY`, and is pinned to the versioned official identity URI `https://crfm.stanford.edu/helm/medhelm/v2.0.0/` (the `/latest/` leaderboard URL is a convenience reference only and is not identity-bearing). The HELM Apache-2.0 code license does NOT license MedHELM benchmark data. The family record is not an executable benchmark asset. Any executable MedHELM component must first be registered individually with exact component identity, access class, license/use rights, revision, and contamination status.

## 3. Evidence-Bound Governance Rules

- **Fail-Closed Verification Invariant:** A benchmark record may be marked `VERIFIED` only if its primary source URI, identifier, verification date, access class, and license status are fully resolved. A non-empty URI string alone does not establish verification; the source must exist, be canonical, and its revision/artifact must exist.
- **Controlled License Vocabulary:** `license_status` must be one of the controlled vocabulary `MIT`, `Apache-2.0`, `CC-BY-NC-4.0`, `COMPONENT_SPECIFIC`, `UNRESOLVED`. Arbitrary license strings (e.g. `NOT_A_REAL_LICENSE`) fail validation; new statuses may be added only when legitimately verified in the canonical registry.
- **Truthful Language/Role Metadata:** Language and role claims must come from the primary source. Where the primary source describes a benchmark as multilingual without enumerating an inventory, the `MULTILINGUAL` sentinel is used; where subset role composition is not established without case inspection, the broad `MULTI_ROLE` representation is used. Unsupported English-only or clinician-only claims are prohibited.
- **Unresolved Asset Boundary:** Any suite with unresolved licensing or source boundaries (such as `medqabstain`) is restricted to `intended_use="REFERENCE_ONLY"` or `PROHIBITED` and cannot be used as an executable development or release gate.
- **Component-Specific License Boundary:** A mixed-access family record (such as `medhelm`) with `license_status="COMPONENT_SPECIFIC"` may only carry `intended_use="REFERENCE_ONLY"` or `PROHIBITED`. A framework code license never silently authorizes gated, private, or differently licensed component data.
- **Zero Case Payloads:** The registry stores metadata, provenance, and verification records only. Question payloads, case texts, and answer keys are strictly forbidden.
- **Offline Determinism:** Registry validation runs entirely offline using semantic canonical normalization.
