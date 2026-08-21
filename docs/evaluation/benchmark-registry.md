# commandMed Benchmark Registry

**Status:** CANONICAL EVALUATION GOVERNANCE
**Spec:** `specs/001-eval-charter`

## 1. Overview

The commandMed Benchmark Registry provides a deterministic, machine-readable inventory of external and public evaluation suites used during research and development. In accordance with Constitutional Principle I (*Evidence Before Training*) and Principle III (*Provenance, Licensing, and Data Lineage*), no benchmark may be used without explicit verification of its canonical source, access classification, license terms, and contamination sensitivity.

Public benchmark performance constitutes development evidence only; public benchmark wins cannot authorize clinical release claims.

## 2. Initial Benchmark Inventory & Verification Status

| Benchmark ID | Canonical Name | Primary Source Identifier | Access Class | License Status | Modalities | Roles | Contamination Sensitivity | Intended Use | Status |
|---|---|---|---|---|---|---|---|---|---|
| `healthbench_consensus` | HealthBench Consensus | OpenAI-HealthBench-2025.1 | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_core` | HealthBench Core | OpenAI-HealthBench-2025.1 | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL`, `PATIENT_CAREGIVER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_hard` | HealthBench Hard | OpenAI-HealthBench-2025.1 | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_professional` | HealthBench Professional | OpenAI-HealthBench-Professional-2026.1 | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medabstain` | MedAbstain: Knowing When to Abstain | ACL-Anthology-2026.eacl-long.291 | `PUBLIC` | `CC-BY-NC-4.0` | `TEXT` | `CLINICAL_PROFESSIONAL` | `MEDIUM` | `DEVELOPMENT` | `VERIFIED` |
| `medhelm` | MedHELM: Holistic Evaluation | arXiv:2408.01242 | `MIXED` | `Apache-2.0` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medmcqa` | MedMCQA Medical Entrance Exams | arXiv:2203.14381 | `PUBLIC` | `Apache-2.0` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqa_usmle` | MedQA (USMLE 4-Option) | arXiv:2009.13081 | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqabstain` | MedQAbstain: LLMs (Almost) Never Abstain | ACL-Anthology-2026.acl-long.1365 | `PUBLIC` | `UNRESOLVED` | `TEXT` | `CLINICAL_PROFESSIONAL`, `PATIENT_CAREGIVER` | `MEDIUM` | `REFERENCE_ONLY` | `UNRESOLVED` |
| `medxpertqa` | MedXpertQA Expert Medical QA | arXiv:2501.18362 | `PUBLIC` | `MIT` | `MULTIMODAL`, `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `pubmedqa` | PubMedQA Biomedical Research QA | arXiv:1909.06146 | `PUBLIC` | `MIT` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |

## 3. Evidence-Bound Governance Rules

- **Fail-Closed Verification Invariant:** A benchmark record may be marked `VERIFIED` only if its primary source URI, identifier, verification date, access class, and license status are fully resolved.
- **Unresolved Asset Boundary:** Any suite with unresolved licensing or source boundaries (such as `medqabstain`) is restricted to `intended_use="REFERENCE_ONLY"` or `PROHIBITED` and cannot be used as an executable development or release gate.
- **Zero Case Payloads:** The registry stores metadata, provenance, and verification records only. Question payloads, case texts, and answer keys are strictly forbidden.
- **Offline Determinism:** Registry validation runs entirely offline using semantic canonical normalization.
