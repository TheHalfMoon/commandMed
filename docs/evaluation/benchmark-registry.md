# commandMed Benchmark Registry

**Status:** CANONICAL EVALUATION GOVERNANCE
**Spec:** `specs/001-eval-charter`

## 1. Overview

The commandMed Benchmark Registry provides a deterministic, machine-readable inventory of external and public evaluation suites used during research and development. In accordance with Constitutional Principle I (*Evidence Before Training*) and Principle III (*Provenance, Licensing, and Data Lineage*), no benchmark may be used without explicit verification of its canonical source, access classification, license terms, and contamination sensitivity.

Public benchmark performance constitutes development evidence only; public benchmark wins cannot authorize clinical release claims.

## 2. Initial Verified Benchmark Families

| Benchmark ID | Canonical Name | Primary Source | Access Class | License Status | Modalities | Roles | Contamination Sensitivity | Intended Use | Status |
|---|---|---|---|---|---|---|---|---|---|
| `healthbench_consensus` | HealthBench Consensus | OpenAI / HealthBench Benchmark Suite | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_core` | HealthBench Core | OpenAI / HealthBench Benchmark Suite | `PUBLIC` | `MIT` | `TEXT` | `PATIENT_CAREGIVER`, `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_hard` | HealthBench Hard | OpenAI / HealthBench Benchmark Suite | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `healthbench_professional` | HealthBench Professional | OpenAI / HealthBench Benchmark Suite | `PUBLIC` | `MIT` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medabstain` | MedAbstain: Selective Classification | Clinical NLP Research Group 2024-2025 | `PUBLIC` | `CC-BY-4.0` | `TEXT` | `CLINICAL_PROFESSIONAL` | `MEDIUM` | `DEVELOPMENT` | `VERIFIED` |
| `medhelm` | MedHELM: Holistic Evaluation | Stanford CRFM / Nature Medicine / arXiv:2408.01242 | `PUBLIC` | `Apache-2.0 / CC-BY-4.0` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medmcqa` | MedMCQA Medical Entrance Exams | Pal et al., 2022 (CHIL 2022 / arXiv:2203.14381) | `PUBLIC` | `Apache-2.0` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqa_usmle` | MedQA (USMLE 4-option) | Jin et al., 2021 (Appl. Sci. / arXiv:2009.13081) | `PUBLIC` | `MIT` | `TEXT` | `LEARNER_RESEARCHER`, `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `medqabstain` | MedQAbstain: QA with Abstention | Medical NLP / arXiv / Uncertainty Benchmarks | `PUBLIC` | `CC-BY-4.0` | `TEXT` | `PATIENT_CAREGIVER`, `CLINICAL_PROFESSIONAL` | `MEDIUM` | `DEVELOPMENT` | `VERIFIED` |
| `medxpertqa` | MedXpertQA Expert Medical QA | arXiv:2501.18378 / Tsinghua / PKU Medical AI | `PUBLIC` | `CC-BY-NC-4.0` | `TEXT`, `DOCUMENT`, `LAB_REPORT`, `PHOTO`, `MULTIMODAL` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |
| `pubmedqa` | PubMedQA Biomedical Research QA | Jin et al., 2019 (EMNLP 2019 / arXiv:1909.06146) | `PUBLIC` | `MIT` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | `VERIFIED` |

## 3. Data Integrity and Privacy Rules

- **Zero Case Payloads:** The registry stores metadata, provenance, and verification records only. Question payloads, case texts, and answer keys are never stored in registry governance files.
- **Fail-Closed Validation:** Missing required fields, duplicate identifiers, or unverified states fail deterministic validation.
- **Offline Determinism:** Registry validation runs entirely offline without dynamic network dependencies.
