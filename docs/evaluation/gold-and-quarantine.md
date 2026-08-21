# commandMed Private Gold Protocols & Quarantine Governance

**Status:** CANONICAL EVALUATION GOVERNANCE
**Spec:** `specs/001-eval-charter`

## 1. The Three Canonical Gold Families

To prevent evaluation degradation and benchmark gaming, commandMed maintains three protected private Gold evaluation families (Constitutional Principle VIII *Holdout Quarantine and Anti-Contamination*):

1. **`COMMANDMED_CLINICAL_GOLD`**: Comprehensive clinical reasoning, medication safety, emergency recognition, and ethical abstention cases.
2. **`COMMANDMED_ARABIC_GOLD`**: Modern Standard Arabic, Saudi/Gulf colloquial patient expressions, medical code-switching, and regional medication nomenclature.
3. **`COMMANDMED_MULTIMODAL_GOLD`**: Diagnostic lab report extraction, clinical photograph triage, and multimodal document synthesis.

## 2. Air-Gapped Governance & Zero Repository Payloads

- **No Payloads in Repository:** Spec 001 establishes governance protocols, metadata contracts, and access policies only. No real Gold cases, patient records, or answer keys are stored in the codebase.
- **Mandatory Power Analysis:** Every Gold protocol strictly requires statistical power analysis before any claim evaluation is conducted.
- **Double-Blind Clinical Adjudication:** Gold cases require independent clinician consensus review.

## 3. Strict Optimization Prohibition

Private Gold assets are under strict cryptographic and operational quarantine. Private Gold content is strictly prohibited from entering:

- Continued Pretraining (CPT)
- Supervised Fine-Tuning (SFT)
- Teacher model generation
- Distillation pipelines
- Direct Preference Optimization (DPO) / Reinforcement Learning (RL/RLVR/GRPO)
- Prompt optimization / prompt tuning
- Hyperparameter tuning
- Checkpoint selection
- Backbone model selection

## 4. Purpose and Quarantine Transition Matrix

| Purpose | Can Train? | Can Select Model? | Allowed Ingestion Sources | Prohibited Ingestion Sources |
|---|---|---|---|---|
| `TRAIN` | `true` | `false` | Permissive pretraining, SFT curriculum, verified synthetic examples | `PRIVATE_GOLD`, `PUBLIC_EXTERNAL_EVAL` |
| `DEV` | `false` | `true` | Verified dev splits, held-out synthetic pilot cases | `PRIVATE_GOLD` |
| `CALIBRATION` | `false` | `true` | Calibration hold-out splits | `PRIVATE_GOLD` |
| `CHECKPOINT_SELECTION` | `false` | `true` | Model selection dev sets, public benchmark dev splits | `PRIVATE_GOLD` |
| `PUBLIC_EXTERNAL_EVAL` | `false` | `true` | Public benchmark canonical test splits | `PRIVATE_GOLD` |
| `PRIVATE_GOLD` | `false` | `false` | Curated air-gapped clinical gold cases | All training/dev/public splits |

## 5. Contamination Interface

The contamination contract establishes interfaces for tracking both:
1. **Exact-Match Contamination:** 13-gram hashing and n-gram overlap checks against candidate training streams.
2. **Semantic Overlap:** High-level contamination risk classifications (`PENDING_DECONTAMINATION_INTERFACE`, `ASSESSED_LOW_RISK`, `ASSESSED_HIGH_RISK`).
