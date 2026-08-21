# Spec 001 Requirements Checklist

**Purpose:** pre-implementation and closeout checklist for the Evaluation Charter.

## A. Scope integrity

- [ ] Spec Kit bootstrap has been reconciled without silently replacing commandMed canonical planning files.
- [ ] Work is limited to Spec 001.
- [ ] No model weights were downloaded, loaded, or executed.
- [ ] No inference was run.
- [ ] No training/CPT/SFT/LoRA/QLoRA/distillation/DPO/GRPO/RL/QAT was run.
- [ ] No PHI or restricted clinical dataset content was accessed or committed.
- [ ] No real private Gold cases were created or committed.
- [ ] No external model/judge API was called.
- [ ] No backbone/model selection was performed.

## B. Benchmark registry

- [ ] Registry has stable IDs and required metadata.
- [ ] Every `VERIFIED` entry has a primary/current source reference and verification date.
- [ ] Unknown license/version/access facts can be represented explicitly.
- [ ] Duplicate benchmark IDs fail validation.
- [ ] Missing required fields fail validation.
- [ ] Invalid enum/state values fail validation.
- [ ] Initial scope accounts for MedHELM.
- [ ] Initial scope accounts for HealthBench.
- [ ] Initial scope accounts for HealthBench Hard.
- [ ] Initial scope accounts for HealthBench Consensus.
- [ ] Initial scope accounts for HealthBench Professional.
- [ ] Initial scope accounts for MedXpertQA text/multimodal.
- [ ] Initial scope accounts for MedQA.
- [ ] Initial scope accounts for MedMCQA.
- [ ] Initial scope accounts for PubMedQA.
- [ ] Initial scope accounts for MedQAbstain.
- [ ] Initial scope accounts for MedAbstain.
- [ ] No benchmark question/case payload is copied merely to populate metadata.

## C. Metrics and hard gates

- [ ] Metric records distinguish optimization metrics from hard gates.
- [ ] Critical-error/safety metrics are represented.
- [ ] Emergency sensitivity is represented.
- [ ] Benign-case over-triage is represented.
- [ ] Abstention/selective-risk metrics are represented.
- [ ] Calibration is represented.
- [ ] Evidence/citation fidelity is represented.
- [ ] Active information acquisition is represented.
- [ ] Patient comprehension/actionability is represented.
- [ ] Professional workflow correctness is represented.
- [ ] Arabic/English gap is represented.
- [ ] Longitudinal robustness is represented.
- [ ] Multimodal metrics are represented.
- [ ] Device/resource metrics are represented.
- [ ] A failed evaluated hard gate forces overall `FAIL` regardless of aggregate score.
- [ ] A required unevaluated hard gate cannot silently produce `PASS`.
- [ ] Spec 001 does not invent unsupported final clinical thresholds.

## D. Gold and quarantine

- [ ] `COMMANDMED_CLINICAL_GOLD` metadata/protocol exists.
- [ ] `COMMANDMED_ARABIC_GOLD` metadata/protocol exists.
- [ ] `COMMANDMED_MULTIMODAL_GOLD` metadata/protocol exists.
- [ ] Each Gold protocol requires power analysis before claim use.
- [ ] Reviewer/adjudication expectations are explicit.
- [ ] Gold payload is not stored in normal repository fixtures.
- [ ] Gold is prohibited from training.
- [ ] Gold is prohibited from teacher generation/distillation.
- [ ] Gold is prohibited from DPO/RL.
- [ ] Gold is prohibited from prompt/hyperparameter optimization.
- [ ] Gold is prohibited from checkpoint/backbone selection.
- [ ] Invalid Gold-purpose combinations fail validation.

## E. Contamination

- [ ] Exact-content identity/overlap state can be recorded.
- [ ] Semantic-overlap/contamination assessment state can be recorded without pretending Spec 001 implements semantic search.
- [ ] Contamination uncertainty can be explicit.
- [ ] Public benchmark/development use is distinguished from private final evaluation.

## F. Determinism and identity

- [ ] Canonical serialization algorithm is documented.
- [ ] Canonical output is UTF-8 and deterministic.
- [ ] Equivalent key ordering produces byte-identical canonical output.
- [ ] Equivalent key ordering produces the same SHA-256 digest.
- [ ] Semantic mutation changes the digest.
- [ ] Invalid artifacts cannot be promoted with a canonical digest.
- [ ] Machine/path/runtime noise does not alter scientific identity unless explicitly semantic.

## G. Ponytail / dependency discipline

- [ ] Python 3.11 standard library was preferred.
- [ ] Every new third-party dependency, if any, has a written necessity.
- [ ] No database was introduced without requirement.
- [ ] No vector store/RAG system was introduced.
- [ ] No web service/UI was introduced.
- [ ] No plugin/framework architecture was introduced for speculative future needs.
- [ ] Safety/provenance/validation was not removed in the name of minimalism.

## H. Tests

- [ ] Tests run offline.
- [ ] Valid fixture acceptance is tested.
- [ ] Missing required field rejection is tested.
- [ ] Duplicate identity rejection is tested.
- [ ] Invalid state rejection is tested.
- [ ] Hard-gate dominance is tested.
- [ ] Gold quarantine violation is tested.
- [ ] Canonical serialization determinism is tested.
- [ ] Semantic mutation/digest change is tested.
- [ ] Fixtures contain no PHI/restricted/Gold case content.

## I. Closeout evidence

- [ ] Exact HEAD is recorded.
- [ ] Exact changed paths are recorded.
- [ ] Validation/test commands and results are recorded.
- [ ] Canonical artifact SHA-256 identities are recorded.
- [ ] Every Spec 001 acceptance criterion has PASS/FAIL evidence.
- [ ] Unresolved benchmark/license/access facts are listed explicitly.
- [ ] Zero-model/inference/training attestation is present.
- [ ] Zero-PHI/real-Gold-content attestation is present.
- [ ] `SPEC_002_PLUS=NOT_STARTED` is explicit.

## Final gate

- [ ] No unchecked hard item above is being silently waived.
- [ ] Spec 001 is eligible to be proposed `CLOSED_CANONICAL`.
