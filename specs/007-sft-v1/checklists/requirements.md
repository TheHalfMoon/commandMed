# Requirements Checklist — Spec 007 SFT V1 Planning

Legend: `[x]` satisfied by the planning package; `[~]` deliberately unresolved typed prerequisite; `[ ]` not yet satisfied.

## Lifecycle and authority

- [x] Planning is canonically authorized by PR #50 / merge `981987390f60302d4c38ae6d54c101aa78c12f4e`.
- [x] Planning scope is non-executing only.
- [x] Model candidate and winner selection are reserved to Founder + ChatGPT.
- [x] Pi recommendation is forbidden by contract.
- [x] Model execution, weights, training, benchmark payload, Private Gold, PHI, device, credential and spend authorities remain NONE.
- [x] Any gradient-bearing pilot is classified as training and remains unauthorized.

## Scientific integrity

- [x] Evaluation-before-optimization is explicit.
- [x] Frozen evaluation protocol is a required precondition of training authorization.
- [x] Hard safety failures are non-compensable.
- [x] Complete purpose-aware quarantine governs all SFT tuning/selection surfaces.
- [x] Checkpoint selection defaults to fixed pre-registered step/token budget.
- [x] Protected final evidence cannot be recycled into optimization.
- [x] Record/SOTA claims require pre-registered record-class definitions and reproducible evidence.

## Data and curriculum

- [x] CurriculumRecord binds full Spec 003 identity fields.
- [x] Three role classes remain exactly D-003 classes.
- [x] Curriculum domains cover medical reasoning, active information acquisition, evidence, tools, abstention, Arabic/English, professional and patient communication, unsafe/adversarial behavior.
- [x] Dataset readiness is not reduced to row count.
- [x] Raw and post-render duplicate/contamination checks are required.
- [x] Mutable medical truth defaults to runtime evidence/tool placement.
- [x] Failure taxonomy distinguishes model, data, tool, safety, knowledge-placement and evaluation failures.
- [x] Protected final failures cannot authorize new training data.
- [~] Real curriculum content remains `DATA_AUTHORITY+PROVENANCE_REQUIRED`.

## Training mechanics

- [x] Tokenizer and chat-template identities are mandatory.
- [x] Prompt rendering is versioned.
- [x] Loss masking is explicit by token class.
- [x] Backend defaults are non-authoritative.
- [x] Packing is evidence-bound and cross-example attention is prohibited by default contract.
- [x] Silent truncation of required context is prohibited.
- [x] Resume identity includes optimizer/scheduler/RNG/data position.
- [x] Reproducibility distinguishes exact-environment replay from cross-environment equivalence.
- [~] Concrete tokenizer/template identities depend on winner evidence.
- [~] Concrete update strategy remains `NEEDS_EVIDENCE`.
- [~] Backend remains `NEEDS_EVIDENCE`.
- [~] Training numerics remain `NEEDS_EVIDENCE`.

## Safety and behavior

- [x] Seven canonical outcome states are preserved.
- [x] Multi-turn `ASK_MORE` / evidence / tool / abstention / escalation trajectories are first-class.
- [x] Deterministic tool authority cannot be replaced by generative text.
- [x] Optional SFT sentinel is quarantine-clean and abort/disqualify-only.
- [x] Sentinel cannot rank checkpoints, tune recipe, or change hyperparameters.
- [x] Capability-preservation binding includes general, medical, Arabic, tools, abstention and safety.

## Arabic

- [x] Arabic is first-class and not a translation-only pass.
- [x] Metadata supports MSA, Saudi/Gulf colloquial, code-switch and transliteration.
- [x] Machine translation alone cannot establish clinical validity.
- [x] Future candidate packet requires Arabic tokenizer-fragmentation evidence.
- [~] Real Arabic clinical review evidence remains later data/human evidence.

## Medical intelligence density

- [x] Additive strategy document exists.
- [x] Strict model-size accounting uses total parameters and real delivered resources, not marketing labels alone.
- [x] RecordClassDefinition contract exists.
- [x] ResourceAccountingRecord contract exists.
- [x] EfficiencyScorecard preserves raw metrics.
- [x] Safety failure disqualifies record claims.
- [x] Spec 007 is Core-only; Nano is a later gated hypothesis.
- [x] Downstream handoffs for CPT/data ablation, distillation, RL efficiency, calibration, compression/QAD, Arabic and release review are explicit and non-authorizing.
- [~] Real device/resource measurements require later device/runtime authority.
- [~] Any public record claim requires later independent evidence.

## Planning artifacts

- [x] `spec.md` canonical.
- [x] `clarification.md` canonical.
- [x] `research.md` canonical.
- [x] medical-intelligence-density strategy authored.
- [x] `plan.md` authored.
- [x] `data-model.md` authored.
- [x] `quickstart.md` authored.
- [x] strict JSON contract set authored.
- [x] requirements checklist authored.
- [x] dependency-ordered tasks authored in this planning package.
- [x] static analysis authored in this planning package.
- [ ] Exact-current-head independent review with no material blocker.
- [ ] Planning package merged canonically.

## Exit disposition

Planning is not canonical until the final two unchecked items are satisfied. Even after planning merge, implementation and every execution authority remain separately gated.
