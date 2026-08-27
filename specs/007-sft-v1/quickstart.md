# Quickstart — Spec 007 SFT V1 Planning and Future Offline Control Plane

**Current lifecycle:** `AUTHORIZED_TO_PLAN`
**Model execution:** NONE
**Training:** NONE

This quickstart describes how to inspect and later validate the Spec 007 planning/offline control plane without downloading weights, constructing real clinical datasets, executing benchmarks, training, using devices, credentials, or spending money.

## 1. Read canonical authority first

```bash
git fetch origin --prune
git checkout main
git pull --ff-only

git rev-parse HEAD
git rev-parse HEAD^{tree}
git status --short
```

Read in order:

```text
AGENTS.md
.specify/memory/constitution.md
docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md
docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md
docs/decision-register.md
specs/README.md
specs/007-sft-v1/spec.md
specs/007-sft-v1/clarification.md
specs/007-sft-v1/research.md
specs/007-sft-v1/plan.md
specs/007-sft-v1/data-model.md
```

Confirm current authority before doing anything else.

Expected planning-stage boundary:

```text
SPEC007=AUTHORIZED_TO_PLAN
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
```

If live repository truth differs, live truth wins.

## 2. What planning may do

Permitted under current planning authority:

- edit planning/specification documentation;
- define JSON schemas and logical data models;
- define synthetic/offline fixture requirements;
- define dependency-ordered implementation tasks;
- run static analysis of the planning package;
- run existing offline repository tests;
- request/repair exact-head code/document review;
- define future candidate/evidence packets without selecting a model.

Not permitted:

- model/weight download or load;
- inference;
- tournament execution;
- real benchmark payload execution;
- training or gradient probes;
- real restricted/PHI/Private Gold data access;
- device execution used as new evidence;
- credentials/provider calls;
- spend.

## 3. Planning validation

After planning changes:

```bash
python3 -m compileall -q src tests
pytest -q
git diff --check
git status --short
```

Do not claim an old test count as a current result. Record actual output from the current exact head.

## 4. Schema validation once implementation is authorized

Future offline implementation should provide a repository-native validation surface for synthetic records. The exact CLI/function is an implementation decision; planning does not invent a production CLI just to satisfy this document.

The minimum behavior to test is:

```text
VALID SYNTHETIC RECORD -> PASS
UNDECLARED FIELD -> FAIL
MISSING REQUIRED IDENTITY -> FAIL
INVALID ENUM -> FAIL
PROHIBITED QUARANTINE PURPOSE -> FAIL
MODEL/EXECUTION-DERIVED EVIDENCE BEFORE AUTHORITY -> FAIL
RECORD CLAIM WITHOUT PRE-REGISTERED CLASS -> FAIL
```

## 5. Synthetic CurriculumRecord example

Planning example only; no real medical content:

```json
{
  "schema_version": "1",
  "record_id": "fixture-record-001",
  "record_canonical_sha256": "<64-hex-fixture>",
  "content_sha256": "<64-hex-fixture>",
  "source_authority_id": "SYNTHETIC_FIXTURE_AUTHORITY",
  "source_license_id": "SYNTHETIC_TEST_ONLY",
  "source_verification_status": "VERIFIED_FIXTURE",
  "split_id": "SYNTHETIC_TRAIN_FIXTURE",
  "contamination_status": "CLEAR_FIXTURE",
  "review_state": "VERIFIED_FIXTURE",
  "role_class": "PATIENT_CAREGIVER",
  "curriculum_strata": ["ACTIVE_INFORMATION_ACQUISITION"],
  "knowledge_placement": "DURABLE_WEIGHT_ELIGIBLE",
  "quarantine_disposition": "ALLOWED_FIXTURE"
}
```

The placeholder hash notation above is documentation only. Executable fixtures must use valid deterministic fixture hashes, never human-looking placeholders accepted as real identities.

## 6. Protected-source negative example

Any synthetic fixture representing a protected source on a prohibited SFT purpose must fail, e.g. conceptually:

```text
source = COMMANDMED_CLINICAL_GOLD
purpose = SFT_TRAINING
expected = REJECT
```

The implementation must consult the canonical purpose→source policy identity, not a hand-copied list only.

## 7. Checkpoint-selection default

Until a separately canonicalized, non-quarantined SFT selection source exists:

```text
SELECTION_MODE=FIXED_PRE_REGISTERED_CHECKPOINT
CHECKPOINT_RULE=PREDECLARED_FINAL_STEP_OR_TOKEN_BUDGET
EVALUATION_ASSET_RANKING=PROHIBITED
ABORT_SENTINEL_CAN_RANK=NO
```

A validator must reject any configuration that tries to use protected evaluation results, human preference inspection, LLM-judge scores, or abort-sentinel results to rank checkpoints.

## 8. Abort-only sentinel

A future sentinel policy is valid only if:

```text
allowed_effects ⊆ {CONTINUE, ABORT_RUN, DISQUALIFY_RUN}
can_rank_checkpoints = false
can_tune_recipe = false
can_change_hyperparameters = false
```

If its source/purpose is not proven outside prohibited quarantine for the monitoring purpose, fail closed.

## 9. Non-executing recipe evidence

Before training authority, accept only static/control-plane evidence.

Examples that remain invalid:

```text
"we tried one training step"
"loss looked stable"
"QLoRA converged faster"
"checkpoint 400 looked best"
"the model answered this benchmark better"
```

Every example above is execution-derived evidence and requires the applicable execution/training authorities before it can exist.

## 10. Model-selection packet

Future Pi output may contain evidence rows but must terminate with:

```text
PI_RECOMMENDATION=NONE
DECISION_OWNER=FOUNDER+CHATGPT
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Pi must not rank or select candidates.

## 11. Record-class validation

A future public record claim must trace to a frozen `RecordClassDefinition` created before comparison evaluation.

Planning example:

```text
claim = "best medical quality per shipped GB"
record_class_definition = REQUIRED
hard_safety_disposition = PASS REQUIRED
comparable_baselines = REQUIRED
resource_measurement = REQUIRED
uncertainty_policy = REQUIRED
independent/reproducible evidence = REQUIRED
```

Without all required evidence, result is `NOT_CLAIMABLE`.

## 12. Resource measurements

Do not place fabricated performance values into fixtures that could be mistaken for evidence.

Planning fixtures may validate shape only. Real values such as:

- peak VRAM;
- TTFT;
- decode throughput;
- energy;
- thermal behavior;

remain `NEEDS_EVIDENCE` until the relevant device/runtime execution is separately authorized.

## 13. Failure taxonomy

Future non-protected development failures may be classified without implying a training response.

Examples:

```text
ARABIC_OR_CODE_SWITCH -> possible Arabic data/eval investigation
TOOL_SELECTION_OR_ARGUMENTS -> possible tool curriculum/validator investigation
MUTABLE_KNOWLEDGE_PLACEMENT -> prefer retrieval/tool correction
EVALUATION_AMBIGUITY -> repair evaluation, not model
```

Protected final/Gold failures may inform release disposition but cannot be fed back into optimization while preserving protected status.

## 14. Future training activation

When a later authority exists, training activation must still verify all bindings:

```text
Founder+ChatGPT winner decision
BaseCheckpointBinding
DatasetSnapshot
PromptRenderingPolicy
LossMaskPolicy
PackingTruncationPolicy
TrainingConfigurationRecord
CheckpointSelectionPolicy
CapabilityPreservationBinding
EnvironmentManifest
FrozenEvaluationProtocolBinding
NonExecutingRecipeEvidence
access authorization
finance authorization
training authorization
```

Any missing/stale/mismatched prerequisite -> fail closed.

## 15. Stop condition

Under current planning authority, stop before:

```text
src/commandmed/spec007 implementation
model access
model execution
tournament execution
training
data acquisition requiring new authority
device evidence execution
spend
```

The complete planning package may be qualified and merged, but implementation requires a separate founder authorization.
