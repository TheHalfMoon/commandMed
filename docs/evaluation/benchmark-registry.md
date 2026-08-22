# commandMed Benchmark Registry

**Status:** SPEC_001_CLOSEOUT_CANDIDATE — BECOMES CANONICAL ONLY AFTER SPEC 001 CLOSURE
**Spec:** `specs/001-eval-charter`

## 1. Overview

The commandMed Benchmark Registry provides a deterministic, machine-readable inventory of external and public evaluation suites used during research and development. In accordance with Constitutional Principle I (*Evidence Before Training*) and Principle III (*Provenance, Licensing, and Data Lineage*), no benchmark may be used without explicit verification of its canonical source, access classification, license terms, and contamination sensitivity.

Public benchmark performance constitutes development evidence only; public benchmark wins cannot authorize clinical release claims.

## 2. Initial Benchmark Inventory & Verification Status

| Benchmark ID | Canonical Name | Primary Source Identifier | Access Class | License Status | Languages | Modalities | Roles | Contamination Sensitivity | Intended Use | Artifact Identity | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `healthbench_consensus` | HealthBench Consensus | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | BOUND: consensus_2025-05-09-20-00-46.jsonl @ dataset commit | `VERIFIED` |
| `healthbench_core` | HealthBench Core | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | BOUND: 2025-05-07-06-14-12_oss_eval.jsonl @ dataset commit | `VERIFIED` |
| `healthbench_hard` | HealthBench Hard | huggingface:datasets/openai/healthbench @ 40ee1968 | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `MULTI_ROLE` | `HIGH` | `DEVELOPMENT` | BOUND: hard_2025-05-08-21-00-10.jsonl @ dataset commit | `VERIFIED` |
| `healthbench_professional` | HealthBench Professional | huggingface:datasets/openai/healthbench-professional @ 349962fd (arXiv:2604.27470) | `PUBLIC` | `MIT` | `MULTILINGUAL` | `TEXT` | `CLINICAL_PROFESSIONAL` | `HIGH` | `DEVELOPMENT` | BOUND: healthbench_professional_eval.jsonl @ dataset commit | `VERIFIED` |
| `medabstain` | MedAbstain: Knowing When to Abstain | arXiv:2601.12471 / github.com/sravanthi6m/MedAbstain @ 091e5c2 | `MIXED` | `COMPONENT_SPECIFIC` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL` | `MEDIUM` | `REFERENCE_ONLY` | UNBOUND (family record; components unregistered) | `VERIFIED` |
| `medhelm` | MedHELM: Holistic Evaluation of LLMs for Medical Tasks | arXiv:2505.23802 (v2.0.0) | `MIXED` | `COMPONENT_SPECIFIC` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `REFERENCE_ONLY` | UNBOUND (family record; components unregistered) | `VERIFIED` |
| `medmcqa` | MedMCQA Medical Entrance Exams | arXiv:2203.14371 / github.com/medmcqa/medmcqa @ c59ef14 | `MIXED` | `MIT` | `en` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `REFERENCE_ONLY` | UNBOUND (Google Drive data; official test ground truth withheld) | `VERIFIED` |
| `medqa_usmle` | MedQA (USMLE 4-Option) | arXiv:2009.13081 / github.com/jind11/MedQA @ 27b02f6 | `PUBLIC` | `MIT` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `REFERENCE_ONLY` | UNBOUND (Google Drive data; variant label only) | `VERIFIED` |
| `medqabstain` | MedQAbstain: LLMs (Almost) Never Abstain | ACL-Anthology-2026.acl-long.1365 | `PUBLIC` | `UNRESOLVED` | `en` | `TEXT` | `CLINICAL_PROFESSIONAL`, `PATIENT_CAREGIVER` | `MEDIUM` | `REFERENCE_ONLY` | UNBOUND | `UNRESOLVED` |
| `medxpertqa` | MedXpertQA Expert Medical QA | huggingface:datasets/TsinghuaC3I/MedXpertQA @ 7e7c465 (arXiv:2501.18362) | `PUBLIC` | `MIT` | `en` | `MULTIMODAL`, `TEXT` | `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | BOUND: Text/MM dev+test .jsonl @ dataset revision | `VERIFIED` |
| `pubmedqa` | PubMedQA Biomedical Research QA | arXiv:1909.06146 / github.com/pubmedqa/pubmedqa @ 1cbae8e | `PUBLIC` | `MIT` | `en` | `TEXT` | `LEARNER_RESEARCHER` | `HIGH` | `DEVELOPMENT` | BOUND: data/ori_pqal.json (git blob 38db7750) | `VERIFIED` |

*Artifact Identity column is documentation/reporting terminology: BOUND means the exact executable artifact file is identified inside an immutable pinned revision (repository commit or dataset revision); UNBOUND means the executable payload is not yet identity-bound by commandMed (external Google Drive distribution, or family record whose components are intentionally unregistered).*

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

### 2.3 Legacy Benchmark Provenance (Final Reconciliation)

- **MedMCQA:** paper identity corrected to arXiv:2203.14371 (the previously recorded arXiv:2203.14381 was wrong); license corrected to MIT (LICENSE.md at pinned commit c59ef14ca1990266c4107c7864b45a20fd93e5e0; Apache-2.0 was wrong). The invented `source_revision="v1.0"` is removed. `access_class=MIXED` represents public train/dev data (182,822 / 6,150 questions) distributed separately via Google Drive plus NON-public official test ground truth (4,183 questions; predictions evaluated via author submission). The family is `VERIFIED` + `REFERENCE_ONLY`: no executable component until exact artifact/split identity is registered. Google Drive data is NOT downloaded in Spec 001.
- **MedQA (USMLE 4-Option):** source/documentation provenance bound to repository commit 27b02f66aac217933c9648a06f82e9f720377925 (the commit that introduced the MIT LICENSE). The `4-option-usmle` value is a SUBSET/VARIANT LABEL preserved as artifact metadata, never presented as a source revision. Dataset bytes are distributed externally via Google Drive and are NOT yet cryptographically/immutably bound by commandMed, so the record is `VERIFIED` + `REFERENCE_ONLY`.
- **PubMedQA:** remains an executable `DEVELOPMENT` asset because the PQA-L artifact lives inside the official repository: pinned to commit 1cbae8e92f72f20c8d3747cbb3bf5bc53554d997 with artifact `data/ori_pqal.json` at git blob 38db7750761c78950ed32303e7545bdaa513390c. Revision-pinned source/license URIs are used instead of mutable `master` links.
- **MedXpertQA:** bound to the ACTUAL dataset source, the official Hugging Face dataset `TsinghuaC3I/MedXpertQA` at dataset revision 7e7c465a68eb2b866926bfa59c8c9d17a8daba65 (4,460 examples; Text + MM, each with dev/test splits: `Text/dev.jsonl`, `Text/test.jsonl`, `MM/dev.jsonl`, `MM/test.jsonl`, plus `images.zip`), not merely the GitHub evaluation-code repository; the unevidenced `source_revision="v1.0"` is removed. Remains executable `DEVELOPMENT` with the quarantine boundary preserved: `PUBLIC_EXTERNAL_EVAL.can_select_model=false`; test splits are evaluation-only; any dev-split use for selection must enter the DEV/CHECKPOINT_SELECTION purpose and must never make the canonical test split selectable.
- **MedAbstain:** family-level fail-closed boundary. Bound to official repository github.com/sravanthi6m/MedAbstain at commit 091e5c22111fffeb51c0c2e69b65d0a21a1e4164; paper arXiv:2601.12471 (EACL 2026). `access_class=MIXED`, `license_status=COMPONENT_SPECIFIC`, `intended_use=REFERENCE_ONLY`, `verification_status=VERIFIED`. Both facts preserved: (1) MedAbstain's own released work/code is CC-BY-NC-4.0 (top-level LICENSE at the pinned commit); (2) the repository contains MedQA-derived benchmark files and amboss/medqa component-construction scripts, so executable component datasets retain their own upstream access/license/usage requirements and MUST be registered separately before execution. Components are intentionally NOT registered in Spec 001 (Ponytail/YAGNI); MedAbstain is NOT executed.

## 3. Evidence-Bound Governance Rules

- **Source Verification ≠ Executable Artifact Binding:** `verification_status=VERIFIED` asserts only that a benchmark family's identity/existence/source/license boundary is verified (SOURCE/FAMILY VERIFICATION). It does NOT assert that the exact executable bytes/split/revision are immutably identified (EXECUTABLE ARTIFACT IDENTITY). Only assets whose executable artifact identity is bound inside an immutable pinned revision may be executable `DEVELOPMENT` assets. `REFERENCE_ONLY` is a valid `VERIFIED` source/family state. Documented invariant: REFERENCE_ONLY records may use a documentation/source revision without an executable data hash.
- **Immutable Evidence URIs:** Where an exact reviewed commit is known, identity-bearing evidence fields use revision-pinned URLs. Mutable `main`/`master`/`latest` links may remain only as convenience/discovery references in notes.
- **Fail-Closed Verification Invariant:** A benchmark record may be marked `VERIFIED` only if its primary source URI, identifier, verification date, access class, and license status are fully resolved. A non-empty URI string alone does not establish verification; the source must exist, be canonical, and its revision/artifact must exist.
- **Controlled License Vocabulary:** `license_status` must be one of the controlled vocabulary `MIT`, `Apache-2.0`, `CC-BY-NC-4.0`, `COMPONENT_SPECIFIC`, `UNRESOLVED`. Arbitrary license strings (e.g. `NOT_A_REAL_LICENSE`) fail validation; new statuses may be added only when legitimately verified in the canonical registry.
- **Truthful Language/Role Metadata:** Language and role claims must come from the primary source. Where the primary source describes a benchmark as multilingual without enumerating an inventory, the `MULTILINGUAL` sentinel is used; where subset role composition is not established without case inspection, the broad `MULTI_ROLE` representation is used. Unsupported English-only or clinician-only claims are prohibited.
- **Unresolved Asset Boundary:** Any suite with unresolved licensing or source boundaries (such as `medqabstain`) is restricted to `intended_use="REFERENCE_ONLY"` or `PROHIBITED` and cannot be used as an executable development or release gate.
- **Component-Specific License Boundary:** A mixed-access family record (such as `medhelm` or `medabstain`) with `license_status="COMPONENT_SPECIFIC"` may only carry `intended_use="REFERENCE_ONLY"` or `PROHIBITED`. A top-level or framework code license never silently authorizes gated, private, or differently licensed component data.
- **Zero Case Payloads:** The registry stores metadata, provenance, and verification records only. Question payloads, case texts, and answer keys are strictly forbidden.
- **Offline Determinism:** Registry validation runs entirely offline using semantic canonical normalization.
