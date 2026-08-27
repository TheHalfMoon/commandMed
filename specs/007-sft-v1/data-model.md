# Data Model — Spec 007 SFT V1

**Lifecycle:** `AUTHORIZED_TO_PLAN`  
**Execution authority:** NONE  
**Training authority:** NONE  
**Model selection:** FOUNDER + CHATGPT ONLY

This document defines the planning-level logical records required by Spec 007. It does not create real training data, model identities, runtime evidence, benchmark results, or execution authority.

## 1. Identity conventions

All canonical Spec 007 planning/runtime records use explicit versioned identities. Where SHA-256 is required, the content identity is computed over deterministic canonical serialization defined by implementation precedent.

General requirements:

- identifiers are explicit strings, never inferred from filenames;
- content identities are distinct from mutable human-readable labels;
- missing evidence is typed `NEEDS_EVIDENCE`, not replaced by placeholder values that look real;
- foreign identities must resolve to an expected record type;
- a changed semantically relevant field changes the content identity;
- schemas reject undeclared fields unless an inherited canonical contract explicitly allows them;
- authority state is never inferred from record existence.

## 2. CurriculumRecord

Purpose: represent one potential SFT training example without requiring a real medical payload in planning fixtures.

Required logical fields:

```text
schema_version
record_id
record_canonical_sha256
content_sha256
source_authority_id
source_license_id
source_verification_status
split_id
contamination_status
review_state
role_class
curriculum_strata[]
language_profile
conversation_structure_id
knowledge_placement
quarantine_disposition
```

Conditional/future fields once rendering is possible:

```text
rendering_policy_id
rendered_input_sha256
rendered_token_count
supervised_token_count
loss_mask_policy_id
```

These five rendered-state fields are an **all-or-none bundle**. An unrendered planning record may omit all five. If any one is present, all five are required. A conforming validator also enforces fail closed:

```text
supervised_token_count <= rendered_token_count
```

A partial rendered-state claim or token-accounting violation is invalid and cannot enter a rendered `DatasetSnapshot`.

`role_class` is closed to:

```text
PATIENT_CAREGIVER
CLINICAL_PROFESSIONAL
LEARNER_RESEARCHER
```

`knowledge_placement` is closed to:

```text
DURABLE_WEIGHT_ELIGIBLE
MUTABLE_RUNTIME_EVIDENCE_PREFERRED
DETERMINISTIC_TOOL_REQUIRED
REJECTED
```

A record not classified `DURABLE_WEIGHT_ELIGIBLE` cannot become gradient-bearing SFT input under Spec 007 without a later explicit policy change.

## 3. LanguageProfile

Required:

```text
primary_language
authored_language
translation_state
dialect_or_register
code_switch_state
transliteration_state
terminology_normalization_id|null
qualified_review_state
```

`terminology_normalization_id` is always present. Explicit `null` means no terminology-normalization identity applies; omission is invalid.

Closed `translation_state`:

```text
ORIGINAL
HUMAN_TRANSLATED
CLINICALLY_TRANSREATED
MACHINE_TRANSLATED_UNVERIFIED
NOT_APPLICABLE
```

`MACHINE_TRANSLATED_UNVERIFIED` cannot establish Arabic clinical-validity readiness.

Arabic-capable records may additionally identify:

```text
AR_MSA
AR_SAUDI_GULF_COLLOQUIAL
AR_OTHER
AR_EN_CODE_SWITCH
AR_TRANSLITERATED_MEDICAL
```

These are strata, not new training roles.

## 4. ConversationStructure

Represents semantic structure before tokenizer-specific rendering.

Fields:

```text
conversation_structure_id
message_sequence[]
tool_definitions_present
expected_outcome_state
required_context_policy
```

Canonical outcome states:

```text
ANSWER
ASK_MORE
USE_TOOL
RETRIEVE_EVIDENCE
ABSTAIN
ESCALATE
EMERGENCY
```

The structure may identify tool calls/results but must not grant tool execution authority.

## 5. PromptRenderingPolicy

Purpose: freeze semantic conversation → tokenizable representation.

Fields:

```text
policy_id
policy_sha256
base_checkpoint_binding_id
tokenizer_identity
chat_template_identity
normalization_policy
system_message_policy
tool_schema_rendering_policy
bos_policy
eos_policy
special_token_map_identity
target_turn_policy
multi_turn_continuation_policy
```

Changing any model-visible rendering behavior creates a new policy identity.

## 6. LossMaskPolicy

Purpose: make the supervised objective explicit.

Fields:

```text
policy_id
policy_sha256
rendering_policy_id
token_class_rules
unknown_token_class_behavior
padding_behavior
validation_fixture_set_id
```

Required token classes:

```text
SYSTEM
USER
ASSISTANT_NATURAL_LANGUAGE
ASSISTANT_TOOL_CALL
TOOL_RESULT
SAFETY_CONTROL
SEPARATOR_OR_SPECIAL
PADDING
```

Every class must explicitly state `SUPERVISED` or `MASKED`. An absent class is invalid.

## 7. PackingTruncationPolicy

Fields:

```text
policy_id
packing_mode
cross_example_attention_allowed
truncation_mode
safe_segmentation_mode
required_context_classes[]
reason_code_vocabulary_id
```

Planning default:

```text
PACKING=NEEDS_EVIDENCE
SILENT_REQUIRED_CONTEXT_TRUNCATION=PROHIBITED
```

Required context classes include safety context, tool schema needed by the target, supervised target, and material conversation facts.

## 8. BaseCheckpointBinding

Future record only; current values remain unresolved.

Fields:

```text
binding_id
winner_decision_record_id
model_repository_id
model_revision
checkpoint_identity
weight_content_identity
total_parameter_count
active_parameter_semantics|null
reference_precision_bytes
tokenizer_identity
chat_template_identity
special_token_map_identity
license_evidence_id
lineage_evidence_id
tournament_evidence_pack_id
resource_evidence_id|null
```

Current state:

```text
BASE_CHECKPOINT_BINDING=NEEDS_EVIDENCE
BACKBONE_WINNER=NEEDS_EVIDENCE
DECISION_OWNER=FOUNDER+CHATGPT
```

## 9. CandidateEvidenceRecord

Neutral future tournament input/output record. Pi may construct/validate this evidence but cannot assign a recommendation.

Fields:

```text
candidate_id
checkpoint_identity
license_evidence_id
parameter_accounting
package_accounting
medical_quality_evidence
patient_conversation_evidence
abstention_evidence
arabic_english_evidence
tool_use_evidence
general_capability_evidence
training_tooling_evidence
resource_evidence
runtime_compatibility_evidence
known_limitations[]
qualification_reason_codes[]
pi_recommendation
```

Invariant:

```text
pi_recommendation = NONE
```

## 10. DatasetSnapshot

Fields:

```text
snapshot_id
snapshot_sha256
record_ids[]
canonical_order_identity
record_count
rendered_token_count|null
supervised_token_count|null
source_summary
license_summary
role_coverage
curriculum_coverage
language_coverage
duplicate_report_id
contamination_report_id
quarantine_verification_id
knowledge_placement_summary
```

Mandatory fail-closed invariants:

```text
record_count == len(record_ids)
record_ids are unique
if rendered_token_count != null and supervised_token_count != null:
    supervised_token_count <= rendered_token_count
```

A snapshot identity changes when admitted records, order, rendering, or semantically material metadata changes. A snapshot with inconsistent count or token accounting is invalid.

## 11. DuplicateContaminationReport

Fields:

```text
report_id
input_snapshot_candidate_id
exact_duplicate_groups
near_duplicate_groups
benchmark_overlap_findings
quarantine_overlap_findings
source_concentration_findings
post_render_overlap_findings|null
disposition
```

`disposition` is `PASS` only when no prohibited overlap remains.

## 12. CurriculumCoverageReport

Raw counts are reported but are not readiness by themselves.

Fields:

```text
report_id
snapshot_id
coverage_by_role
coverage_by_domain
coverage_by_language
coverage_by_risk
coverage_by_outcome_state
coverage_by_tool_requirement
coverage_by_reasoning_type
multi_turn_coverage
abstention_coverage
supervised_token_distribution
source_concentration
verification_state_distribution
knowledge_placement_distribution
uncovered_required_strata[]
```

## 13. TrainingConfigurationRecord

Fields remain versioned even when values are `NEEDS_EVIDENCE`:

```text
config_id
base_checkpoint_binding_id
dataset_snapshot_id
rendering_policy_id
loss_mask_policy_id
packing_truncation_policy_id
update_strategy
precision_policy
sequence_length
role_mix_policy
optimizer_class
scheduler_class
learning_rate_record
effective_batch_semantics
token_budget
epoch_or_step_budget
gradient_accumulation
clipping_policy
checkpoint_schedule
seed
data_seed
deterministic_mode
backend_id
environment_manifest_id
```

No placeholder numeric is treated as canonical evidence.

## 14. BackendCandidateEvidence

Purpose: assess trainer/backend compatibility without selecting a backend during planning.

Fields:

```text
backend_candidate_id
software_identity
architecture_support_evidence
rendering_fidelity_evidence
loss_mask_support_evidence
packing_truncation_support_evidence
resume_support_evidence
reproducibility_support_evidence
precision_update_strategy_support
network_telemetry_behavior
maintenance_dependency_cost
non_executing_evidence_only
status
```

Before execution authority:

```text
non_executing_evidence_only = true
```

No backend is selected by this schema.

## 15. NonExecutingRecipeEvidence

Allowed classes:

```text
SCHEMA_COMPLETENESS
DOCUMENTED_COMPATIBILITY
STATIC_RESOURCE_ESTIMATE
RENDERING_CONFORMANCE_DEFINITION
LOSS_MASK_CONFORMANCE_DEFINITION
PACKING_TRUNCATION_CONFORMANCE_DEFINITION
PROVENANCE_QUARANTINE_BINDING
ENVIRONMENT_IDENTITY
ARTIFACT_EXPORT_REQUIREMENT
LICENSE_POSTURE
```

Forbidden before execution/training authority:

```text
LOSS_CURVE
GRADIENT_BEHAVIOR
CONVERGENCE
MODEL_OUTPUT
CHECKPOINT_COMPARISON
BENCHMARK_EXECUTION
EMPIRICAL_TRAINING_RESULT
```

## 16. CheckpointSelectionPolicy

Fields:

```text
policy_id
selection_mode
checkpoint_rule
selection_source_ids[]
selection_source_purpose_authorization|null
evaluation_asset_ranking_allowed
abort_sentinel_can_rank
recipe_tuning_allowed
hyperparameter_tuning_allowed
frozen_before_run
```

For `FIXED_PRE_REGISTERED_CHECKPOINT`:

```text
selection_source_ids = []
selection_source_purpose_authorization = null
evaluation_asset_ranking_allowed = false
abort_sentinel_can_rank = false
recipe_tuning_allowed = false
hyperparameter_tuning_allowed = false
```

For `SEPARATELY_AUTHORIZED_NON_QUARANTINED_SELECTION`, `selection_source_purpose_authorization` is a structured record requiring:

```text
authorization_id
authority_record_id
exact_purpose = SFT_CHECKPOINT_SELECTION
authorized_source_ids[]
quarantine_disposition = VERIFIED_NON_QUARANTINED_FOR_SFT_CHECKPOINT_SELECTION
provenance_validation_status = PASS
frozen_before_run = true
```

Mandatory fail-closed invariant:

```text
selection_source_ids == selection_source_purpose_authorization.authorized_source_ids
```

An arbitrary authorization identifier, wrong purpose, provenance failure, quarantine mismatch, or source-set mismatch is invalid. This record does not itself grant the separate authority it references.

## 17. AbortSentinelPolicy

Optional future record.

Fields:

```text
policy_id
sentinel_set_id
source_purpose_verification_id
threshold_record_id
allowed_effects[]
can_rank_checkpoints
can_tune_recipe
can_change_hyperparameters
frozen_before_run
```

Required:

```text
allowed_effects ⊆ {CONTINUE, ABORT_RUN, DISQUALIFY_RUN}
can_rank_checkpoints = false
can_tune_recipe = false
can_change_hyperparameters = false
```

## 18. CapabilityPreservationBinding

Fields:

```text
binding_id
base_checkpoint_binding_id
candidate_checkpoint_id
frozen_evaluation_protocol_id
required_slices[]
pre_registered_margins_id
quarantine_verification_id
```

Required logical slices include general reasoning, instruction following, medical core, Arabic, tools, abstention/selective risk, and safety.

## 19. EnvironmentManifest

Fields:

```text
environment_id
os_or_container_identity
python_identity
framework_identity
training_backend_identity
device_runtime_identity
device_identity
driver_identity
attention_kernel_identity
precision_identity
compiler_flags_identity|null
dependency_lock_identity
seed_policy
deterministic_mode
known_nondeterminism[]
```

This record is necessary but does not authorize device use.

## 20. TrainingCheckpointManifest

Fields:

```text
checkpoint_manifest_id
model_or_adapter_state_identity
optimizer_state_identity
scheduler_state_identity
scaler_state_identity|null
rng_state_identity
data_position_identity
global_step
training_config_id
base_checkpoint_binding_id
dataset_snapshot_id
rendering_policy_id
environment_manifest_id
```

Missing optimizer/scheduler/RNG/data-position state means the artifact is an export, not a resumable training checkpoint.

## 21. FrozenEvaluationProtocolBinding

Fields:

```text
binding_id
metric_catalog_identity
hard_gate_identity
statistical_protocol_identity
stratification_identity
sample_size_rationale_identity
acceptance_threshold_identity
quarantine_matrix_identity
evaluation_asset_manifests[]
frozen_before_training_authorization
```

`evaluation_asset_manifests` is non-empty and binds every asset consumed by the frozen protocol. Each manifest requires:

```text
asset_id
asset_role
source_authority_id
source_license_id
content_sha256
split_id
contamination_status
source_verification_status
review_state
provenance_validation_status = PASS
```

Allowed `asset_role` values are:

```text
METRIC_INPUT
REPLAY_FIXTURE
THRESHOLD_ASSET
STRATIFICATION_ASSET
SAMPLE_SIZE_EVIDENCE
OTHER_PROTOCOL_ASSET
```

The binding cannot be treated as frozen unless every consumed evaluation asset has the complete inherited Spec 003 provenance/admission bundle and `provenance_validation_status=PASS`.

Required:

```text
frozen_before_training_authorization = true
```

## 22. RunManifest

Future activation root:

```text
run_manifest_id
base_checkpoint_binding_id
dataset_snapshot_id
prompt_rendering_policy_id
loss_mask_policy_id
packing_truncation_policy_id
training_config_id
checkpoint_selection_policy_id
capability_preservation_binding_id
environment_manifest_id
frozen_evaluation_protocol_binding_id
non_executing_recipe_evidence_id
software_commit
software_tree
access_authorization_ids[]
finance_requirement_id
finance_authorization_id
training_authorization_id
```

Manifest validation is not execution authority.

## 23. ResourceAccountingRecord

Raw future resource accounting:

```text
resource_record_id
artifact_identity
total_parameter_count
active_parameters_per_token|null
reference_precision_bytes
shipped_model_bytes
required_tokenizer_config_bytes
required_adapter_bytes
peak_memory_bytes
context_length_tested
kv_cache_bytes
hardware_identity
runtime_identity
ttft_ms
prefill_tokens_per_second
decode_tokens_per_second
sustained_tokens_per_second
energy_joules_per_case|null
thermal_condition|null
```

Real measurements require device/runtime authority; planning fixtures use typed synthetic values only.

## 24. RecordClassDefinition

Fields:

```text
record_class_id
version
name
inclusion_rules
exclusion_rules
parameter_accounting_rule
shipped_byte_accounting_rule
peak_memory_accounting_rule
required_medical_slices[]
required_safety_disposition
required_resource_evidence[]
uncertainty_policy
tie_break_policy
contamination_prerequisites
allowed_claim_templates[]
prohibited_claim_templates[]
pre_registered
```

A record claim is invalid if this definition did not exist before the comparison evidence was evaluated.

## 25. EfficiencyScorecard

Fields:

```text
scorecard_id
artifact_identity
record_class_id|null
raw_medical_metrics
hard_safety_disposition
selective_risk_metrics
arabic_metrics
tool_reliability_metrics
general_capability_delta
resource_accounting_id
reasoning_token_metrics|null
derived_efficiency_metrics
qualification_state
```

A hard safety failure forces `qualification_state=DISQUALIFIED` regardless of derived efficiency. `INSUFFICIENT_EVIDENCE` is also non-qualifying; `qualification_state=QUALIFIED` requires `hard_safety_disposition=PASS`.

## 26. FailureTaxonomyRecord

Fields:

```text
failure_id
evidence_source_id
source_is_protected_final_evidence
failure_category
subtype
severity
language_stratum
role_stratum
root_cause_confidence
recommended_remediation_surface
training_data_admission_allowed
reason_codes[]
```

Closed top-level categories:

```text
FACTUAL_KNOWLEDGE
CLINICAL_REASONING
ACTIVE_INFORMATION_ACQUISITION
EVIDENCE_USE
TOOL_SELECTION_OR_ARGUMENTS
TOOL_RESULT_TRUST
ABSTENTION_OR_OVERANSWERING
ESCALATION_OR_EMERGENCY
PATIENT_COMMUNICATION
PROFESSIONAL_WORKFLOW
ARABIC_OR_CODE_SWITCH
STRUCTURED_OUTPUT
PROVENANCE_OR_DATA
EVALUATION_AMBIGUITY
MUTABLE_KNOWLEDGE_PLACEMENT
GENERAL_CAPABILITY_REGRESSION
OTHER_REVIEW_REQUIRED
```

If `source_is_protected_final_evidence=true`, the record requires `training_data_admission_allowed=false` and cannot authorize optimization/training-data creation.

## 27. Record relationships

Future run relationship:

```text
Founder+ChatGPT WinnerDecision
        |
        v
BaseCheckpointBinding
        |
        +---------------------------+
        |                           |
        v                           v
PromptRenderingPolicy       DatasetSnapshot
        |                           |
        v                           |
LossMaskPolicy                     |
        |                           |
        +------------+--------------+
                     v
          TrainingConfigurationRecord
                     |
        +------------+-------------+
        |                          |
        v                          v
EnvironmentManifest      CheckpointSelectionPolicy
        |                          |
        +------------+-------------+
                     v
                  RunManifest
                     |
              [AUTHORITY GATES]
                     |
              future training run
                     |
          TrainingCheckpointManifest
                     |
         Frozen qualification evidence
                     |
              EfficiencyScorecard
```

`RecordClassDefinition`, `ResourceAccountingRecord`, and `EfficiencyScorecard` are measurement/claim records; they do not control gradient optimization.

## 28. Planning invariants

1. No concrete backbone identity is valid until Founder+ChatGPT select it from authorized tournament evidence.
2. No dataset snapshot can be valid with incomplete Spec 003 identities or inconsistent record/token accounting.
3. No protected quarantine source can silently enter any prohibited SFT optimization surface.
4. No backend default determines rendering or loss masking.
5. No evaluation result may create execution authority.
6. No record-class score can compensate for a hard safety failure or insufficient required safety evidence.
7. No real resource value may be fabricated before measurement authority exists.
8. No protected final failure becomes optimization data through `FailureTaxonomyRecord`.
9. No model-only export may be represented as a resumable checkpoint.
10. No planning record authorizes training.
11. No partial rendered-state bundle is valid, and supervised tokens cannot exceed rendered tokens.
12. No separately authorized checkpoint-selection policy is valid without a provenance-clean, non-quarantined, purpose-exact authority binding whose authorized source set exactly matches the policy source set.
13. No frozen evaluation protocol is valid unless every consumed evaluation asset carries complete provenance and a PASS admission status.
