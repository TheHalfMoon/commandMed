# Static Analyze — Spec 007 SFT V1 Planning Package

**Date:** 2026-08-27  
**Lifecycle:** `AUTHORIZED_TO_PLAN`  
**Scope:** planning/static consistency only; no model/data/device/training execution

## 1. Inputs analyzed

- `AGENTS.md`
- `.specify/memory/constitution.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- canonical Spec 007 `spec.md`, `clarification.md`, `research.md`
- current `plan.md`
- current `data-model.md`
- current `quickstart.md`
- current JSON contracts
- current requirements checklist
- current tasks

## 2. Planning authority analysis

Result: PASS.

The package performs non-executing planning only. It does not introduce runtime source, model weights, benchmark payloads, dataset payloads, device execution, provider calls, credentials, spend, or training.

Model authority remains:

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 3. Spec alignment

### FR-001 curriculum

Covered by CurriculumRecord, coverage dimensions, three fixed roles, domain taxonomy, Arabic/English metadata, multi-turn/tool/abstention structures.

### FR-002 base checkpoint

Covered as typed future BaseCheckpointBinding. No model is named or selected. Winner remains external evidence/Founder+ChatGPT decision.

### FR-003 quarantine

Covered by purpose-aware canonical matrix binding across training, monitoring, early stopping, recipe, checkpoint and model-selection surfaces. Static copied names are explicitly non-authoritative relative to the canonical matrix identity.

### FR-004 provenance

Curriculum and future evaluation/run assets require explicit source/license/content/split/contamination/verification identities. Missing identity fails closed.

### FR-005 frozen evaluation

`FrozenEvaluationProtocolBinding` requires immutable protocol identity before training authorization.

### FR-006 training configuration

TrainingConfigurationRecord exists with unresolved numerics/update/backend permitted only as typed `NEEDS_EVIDENCE`.

### FR-007 safety behavior

Seven canonical outcome states, deterministic tool authority, hard-gate composition, abstention, escalation and abort-only monitoring remain preserved.

### FR-008 compute/spend

No budget is fabricated. Spend remains NONE and future finance evidence is a RunManifest/activation prerequisite.

## 4. Strategy alignment

The additive medical-intelligence-density strategy does not replace the frozen Grand Master Plan. It operationalizes its existing per-byte/joule/second objective.

The package adds planning contracts for:

- strict resource accounting;
- record-class pre-registration;
- raw+normalized efficiency scorecards;
- Core-vs-Nano boundary;
- failure taxonomy;
- maximum-information-per-gradient curriculum policy;
- downstream ablation/distillation/RL/compression/Arabic/release handoffs.

None are executed or claimed as achieved.

## 5. Safety analysis

No material safety weakening found in planning scope.

Hard protections:

- final/protected evidence cannot enter tuning;
- sentinel is abort/disqualify-only;
- checkpoint selection is fixed/pre-registered by default;
- deterministic medical tools retain authority;
- safety failure disqualifies record claims;
- mutable medical truth defaults to runtime evidence/tool placement;
- a schema-valid RunManifest does not imply execution authority.

## 6. Data leakage / contamination analysis

No planned path permits a protected evaluation source to influence gradient-bearing input or optimization-affecting selection.

`FailureTaxonomyRecord` explicitly separates protected final evidence from optimization-admissible development evidence. Protected final failure cannot authorize training-data admission.

## 7. Record-chasing analysis

No public record is claimed.

Future record claims require:

- pre-registered class;
- strict resource accounting;
- safety PASS;
- comparable baselines;
- uncertainty policy;
- contamination/quarantine pass;
- reproducible or independently auditable evidence.

This prevents a leaderboard objective from becoming a hidden optimization leak.

## 8. Overengineering analysis

Potential risk: many schemas/modules.

Mitigation: plan explicitly permits consolidation into existing repository modules during implementation and prohibits empty abstraction layers. Schemas exist to freeze cross-stage contracts, not to require one runtime class/module per schema.

No database, service, queue, plugin framework, trainer abstraction, cloud service, or new dependency is planned by default.

## 9. Training-mechanics analysis

P0 gaps identified in earlier research are addressed:

- tokenizer/template identity — COVERED;
- deterministic rendering — COVERED;
- explicit token-level loss masking — COVERED;
- packing/truncation safety — COVERED;
- multi-turn/tool trajectories — COVERED;
- checkpoint-selection firewall — COVERED;
- safety/capability preservation — COVERED;
- realistic GPU reproducibility — COVERED;
- resume integrity — COVERED;
- backend/update-strategy neutrality — COVERED;
- no unauthorized pilot — COVERED.

## 10. Arabic analysis

Arabic is not treated as a translation-only slice. Required metadata and future tokenizer-efficiency evidence are explicit. Real clinical Arabic validity remains external data/human evidence, not fabricated planning completion.

## 11. Downstream-scope analysis

The plan references later research without absorbing it:

- CPT/data ablation remains Spec 008;
- distillation remains Spec 009;
- RL/reasoning efficiency remains Spec 010;
- calibration remains Spec 011;
- compression/QAD remains Spec 012;
- Arabic deepening remains Spec 013;
- human eval remains Spec 015;
- public record/HF/paper claims remain Spec 017.

This preserves bounded Spec 007 scope.

## 12. Contradiction inventory

```text
CRITICAL=0
HIGH=0
MEDIUM=0
LOW=2
```

LOW-001: The contract surface is intentionally broad. Implementation should consolidate validators/modules where repository-native mechanisms already exist rather than mirror every schema with a new abstraction.

LOW-002: Real record-class comparisons may require future benchmark/device methodology refinement. The planning schemas intentionally freeze the evidence shape, not future numerical thresholds.

Neither LOW item blocks planning qualification.

## 13. Typed unresolved evidence

The following are intentionally unresolved and do not make planning inconsistent:

```text
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CANDIDATE_MANIFEST=FOUNDER+CHATGPT_DECISION_REQUIRED
LIVE_TOURNAMENT_EXECUTION=SEPARATE_AUTHORIZATION_REQUIRED
MODEL_WEIGHT_ACCESS=SEPARATE_AUTHORIZATION_REQUIRED
TOKENIZER_TEMPLATE_CONCRETE_IDENTITIES=DEPEND_ON_WINNER
TRAINING_BACKEND=NEEDS_EVIDENCE
UPDATE_STRATEGY=NEEDS_EVIDENCE
TRAINING_NUMERICS=NEEDS_EVIDENCE
REAL_CURRICULUM_CONTENT=DATA_AUTHORITY+PROVENANCE_REQUIRED
REAL_DEVICE_RESOURCE_EVIDENCE=SEPARATE_AUTHORITY_REQUIRED
COMPUTE_BUDGET=NEEDS_EVIDENCE+FOUNDER_SPEND_AUTHORITY
TRAINING_RUN=SEPARATE_TRAINING_AUTHORIZATION_REQUIRED
PUBLIC_RECORD_CLAIM=INDEPENDENT_EVIDENCE_REQUIRED
```

## 14. Static analyze disposition

```text
RESULT=PASS_PLANNING_STATIC
CRITICAL=0
HIGH=0
MEDIUM=0
LOW=2
UNRESOLVED_HARD_CONTRADICTIONS=0
IMPLEMENTATION_AUTHORIZED=NO
TRAINING_AUTHORIZED=NO
MODEL_SELECTED=NO
```

This result is an internal planning consistency analysis, not independent exact-head review. Planning still requires repository checks and fresh independent review before canonical merge.
