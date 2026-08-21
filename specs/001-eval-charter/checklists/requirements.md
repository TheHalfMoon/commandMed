# Spec 001 Requirements Checklist

**Purpose:** pre-implementation and closeout checklist for the Evaluation Charter.

## A. Scope integrity

- [x] Spec Kit bootstrap has been reconciled without silently replacing commandMed canonical planning files.
- [x] Work is limited to Spec 001.
- [x] No model weights were downloaded, loaded, or executed.
- [x] No inference was run.
- [x] No training/CPT/SFT/LoRA/QLoRA/distillation/DPO/GRPO/RL/QAT was run.
- [x] No PHI or restricted clinical dataset content was accessed or committed.
- [x] No real private Gold cases were created or committed.
- [x] No external model/judge API was called.
- [x] No backbone/model selection was performed.

## B. Benchmark registry

- [x] Registry has stable IDs and required metadata.
- [x] Every `VERIFIED` entry has a primary/current source reference and verification date.
- [x] Unknown license/version/access facts can be represented explicitly.
- [x] Duplicate benchmark IDs fail validation.
- [x] Missing required fields fail validation.
- [x] Invalid enum/state values fail validation.
- [x] Initial scope accounts for MedHELM.
- [x] Initial scope accounts for HealthBench.
- [x] Initial scope accounts for HealthBench Hard.
- [x] Initial scope accounts for HealthBench Consensus.
- [x] Initial scope accounts for HealthBench Professional.
- [x] Initial scope accounts for MedXpertQA text/multimodal.
- [x] Initial scope accounts for MedQA.
- [x] Initial scope accounts for MedMCQA.
- [x] Initial scope accounts for PubMedQA.
- [x] Initial scope accounts for MedQAbstain.
- [x] Initial scope accounts for MedAbstain.
- [x] No benchmark question/case payload is copied merely to populate metadata.

## C. Metrics and hard gates

- [x] Metric records distinguish optimization metrics from hard gates.
- [x] Critical-error/safety metrics are represented.
- [x] Emergency sensitivity is represented.
- [x] Benign-case over-triage is represented.
- [x] Abstention/selective-risk metrics are represented.
- [x] Calibration is represented.
- [x] Evidence/citation fidelity is represented.
- [x] Active information acquisition is represented.
- [x] Patient comprehension/actionability is represented.
- [x] Professional workflow correctness is represented.
- [x] Arabic/English gap is represented.
- [x] Longitudinal robustness is represented.
- [x] Multimodal metrics are represented.
- [x] Device/resource metrics are represented.
- [x] A failed evaluated hard gate forces overall `FAIL` regardless of aggregate score.
- [x] A required unevaluated hard gate cannot silently produce `PASS`.
- [x] Spec 001 does not invent unsupported final clinical thresholds.

## D. Gold and quarantine

- [x] `COMMANDMED_CLINICAL_GOLD` metadata/protocol exists.
- [x] `COMMANDMED_ARABIC_GOLD` metadata/protocol exists.
- [x] `COMMANDMED_MULTIMODAL_GOLD` metadata/protocol exists.
- [x] Each Gold protocol requires power analysis before claim use.
- [x] Reviewer/adjudication expectations are explicit.
- [x] Gold payload is not stored in normal repository fixtures.
- [x] Gold is prohibited from training.
- [x] Gold is prohibited from teacher generation/distillation.
- [x] Gold is prohibited from DPO/RL.
- [x] Gold is prohibited from prompt/hyperparameter optimization.
- [x] Gold is prohibited from checkpoint/backbone selection.
- [x] Invalid Gold-purpose combinations fail validation.

## E. Contamination

- [x] Exact-content identity/overlap state can be recorded.
- [x] Semantic-overlap/contamination assessment state can be recorded without pretending Spec 001 implements semantic search.
- [x] Contamination uncertainty can be explicit.
- [x] Public benchmark/development use is distinguished from private final evaluation.

## F. Determinism and identity

- [x] Canonical serialization algorithm is documented.
- [x] Canonical output is UTF-8 and deterministic.
- [x] Equivalent key ordering produces byte-identical canonical output.
- [x] Equivalent key ordering produces the same SHA-256 digest.
- [x] Semantic mutation changes the digest.
- [x] Invalid artifacts cannot be promoted with a canonical digest.
- [x] Machine/path/runtime noise does not alter scientific identity unless explicitly semantic.

## G. Ponytail / dependency discipline

- [x] Python 3.11 standard library was preferred.
- [x] Every new third-party dependency, if any, has a written necessity.
- [x] No database was introduced without requirement.
- [x] No vector store/RAG system was introduced.
- [x] No web service/UI was introduced.
- [x] No plugin/framework architecture was introduced for speculative future needs.
- [x] Safety/provenance/validation was not removed in the name of minimalism.

## H. Tests

- [x] Tests run offline.
- [x] Valid fixture acceptance is tested.
- [x] Missing required field rejection is tested.
- [x] Duplicate identity rejection is tested.
- [x] Invalid state rejection is tested.
- [x] Hard-gate dominance is tested.
- [x] Gold quarantine violation is tested.
- [x] Canonical serialization determinism is tested.
- [x] Semantic mutation/digest change is tested.
- [x] Fixtures contain no PHI/restricted/Gold case content.

## I. Closeout evidence

- [x] Exact HEAD is recorded.
- [x] Exact changed paths are recorded.
- [x] Validation/test commands and results are recorded.
- [x] Canonical artifact SHA-256 identities are recorded.
- [x] Every Spec 001 acceptance criterion has PASS/FAIL evidence.
- [x] Unresolved benchmark/license/access facts are listed explicitly.
- [x] Zero-model/inference/training attestation is present.
- [x] Zero-PHI/real-Gold-content attestation is present.
- [x] `SPEC_002_PLUS=NOT_STARTED` is explicit.

## Final gate

- [x] No unchecked hard item above is being silently waived.
- [x] Spec 001 is eligible to be proposed `CLOSED_CANONICAL`.
