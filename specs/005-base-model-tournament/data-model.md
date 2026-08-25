# Spec 005 — Data Model

**Status:** `REPAIRED_COMPLETE`
**Scope:** Deterministic scientific/governance metadata and state model for preconstruction and tournament-manifest readiness. No clinical/model/benchmark/personnel payload is stored here.

## 1. Design rules

- Records are plain JSON-compatible mappings with closed vocabularies.
- Every material governance/scientific record has an explicit ID, version and canonical SHA-256.
- Caller-provided PASS/eligibility/authorization outcomes are never trusted when the outcome can be computed from bound evidence.
- Unknown enum/state values fail closed.
- Material changes create a new identity; historical records remain reproducible.
- Sensitive payloads remain outside repository metadata records.
- Exact threshold/margin/sample-size values are never guessed; a missing required value is a blocked evidence condition.

## 2. `MetricsV2Catalog`

**Purpose:** Additive Spec 001 evaluation catalog that can distinguish evidence roles/purposes without rewriting V1.

```text
schema_id
schema_version = "2.0"
supersedes_v1_sha256
metrics[]
canonical_sha256
```

Each V2 evidence-role entry binds at least:

```text
evidence_role
purpose
evidence_kind
binding_mode
source_policy
requirement
```

Rules:
- V1 `metrics.json` remains unchanged.
- V1 and V2 consumers reject version/path/SHA fall-forward or fallback.
- Arabic parity may carry separate `SELECTION_DEV` and `PRIVATE_GOLD_FINAL_AUDIT` evidence roles.

## 3. `SelectionQualityContract`

**Purpose:** Canonical Spec 005 scientific selection policy for seven noncompensable lanes and A2/A3+A4 record requirements.

```text
contract_id
contract_version
required_quality_lanes[]
required_role_ids[]
required_language_scope[]
required_arabic_coverage_anchors[]
metric_mapping_requirements[]
threshold_record_requirements[]
statistical_design_requirements[]
invariants[]
canonical_sha256
```

Required lanes:

```text
A_MEDICAL_KNOWLEDGE_BIOMEDICAL_REASONING
B_PATIENT_CAREGIVER_CLINICAL_SAFETY
C_UNCERTAINTY_ABSTENTION_INFORMATION_SEEKING
D_EVIDENCE_GROUNDED_CLINICAL
E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY
F_CLINICAL_PROFESSIONAL_REASONING_WORKFLOW
G_LAB_DOCUMENT_STRUCTURED_QUALIFICATION
```

A lane cannot compensate for a failed/missing required lane.

## 4. `ThresholdPolicyRecord` — A2

**Purpose:** Bind one metric/stratum decision threshold or margin to qualified evidence and review authority.

```text
threshold_policy_id
threshold_policy_version
metric_id
metric_evidence_role
lane_id
required_stratum_or_scope
estimand_id
metric_direction
decision_role
threshold_kind
threshold_value_or_margin
unit_or_scale
clinical_meaningfulness_evidence_ids[]
statistical_justification_evidence_ids[]
clinical_review_authority_reference
statistical_review_authority_reference
conflict_disposition_record_ids[]
pre_result_freeze = true
record_canonical_sha256
```

`threshold_value_or_margin` may be absent while the record is draft/incomplete, but a gate requiring it cannot PASS until exact evidence and review bindings exist. Candidate-result-derived threshold selection is prohibited.

## 5. `StatisticalDesignRecord` — atomic A3+A4

**Purpose:** Bind one estimand/decision rule to its sample-size and allocation design without allowing authoring capacity or candidate results to choose N.

```text
statistical_design_id
design_version
quality_lane
metric_id_or_metric_mapping_id
required_stratum_or_scope
estimand
unit_of_analysis
decision_role
threshold_policy_id_or_explicit_not_applicable
precision_or_power_objective
confidence_or_error_rate_parameters
anticipated_rate_variance_or_other_nuisance_inputs
source_and_provenance_for_planning_inputs
pairing_or_cluster_dependency_model
multiplicity_structure
planned_numeric_n
coverage_allocation_design
rounding_or_allocation_rule
software_formula_or_method_identity
sensitivity_analysis_identity_or_explicit_not_required
candidate_neutral = true
pre_result_freeze = true
record_canonical_sha256
```

A3 and A4 are one identity because `planned_numeric_n` and allocation across anchors/roles/strata are mutually dependent outputs of the same design. Missing required threshold, nuisance, dependency or review input blocks final design PASS.

## 6. `GateEvidenceRecord`

**Purpose:** Uniform reference to an evidence-bound prerequisite without embedding sensitive content.

```text
gate_id
record_id
record_version
record_canonical_sha256
state
reason_codes[]
source_record_ids[]
source_record_sha256s[]
stale = true|false
```

Typical states:

```text
PASS
BLOCKED
INCOMPLETE
NOT_APPLICABLE
STALE_REVALIDATION_REQUIRED
```

`NOT_APPLICABLE` is allowed only where the governing contract explicitly permits it.

## 7. `PreconstructionSnapshot`

**Purpose:** Bind A1–A14 prerequisite identities at one point in governance time.

```text
snapshot_id
snapshot_version
metrics_v2_catalog_id
selection_quality_contract_id
threshold_policy_record_ids[]
statistical_design_record_ids[]
requirements[]
gate_evidence_by_id{}
dependency_edges[]
computed_readiness
reason_codes[]
canonical_sha256
```

Readiness states:

```text
NOT_READY_TO_CONSTRUCT
READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED
```

A real `AUTHORIZED_TO_CONSTRUCT` state belongs to `ConstructionActivationRecord`, not this snapshot.

## 8. `SelectionSourceRouteRecord`

```text
source_route_record_id
route_class
origin_type
lineage_record_id
lineage_record_sha256
parent_asset_ids[]
rights_evidence_id
privacy_evidence_id
declared_use = DEVELOPMENT_EVALUATION
purpose = CHECKPOINT_SELECTION
record_canonical_sha256
```

Allowed route classes include:

```text
ORIGINAL_HUMAN_AUTHORED_NON_PHI
PUBLIC_DEV_DIRECT
PUBLIC_DEV_DERIVED
AUTHORIZED_INTERNAL_DERIVED
MODEL_OR_PROVIDER_GENERATED
PROHIBITED_OR_BLOCKED_SOURCE
```

`MODEL_OR_PROVIDER_GENERATED` is representable but currently unauthorized for execution.

## 9. `RootTaskMetadata`

**Purpose:** Metadata-only identity for a future selection case. Validators may use synthetic fixture records but MUST NOT create real case content before A15.

```text
root_task_id
root_task_record_version
root_task_state
root_content_artifact_sha256
source_route_record_id
source_route_record_sha256
lineage_record_id
lineage_record_sha256
primary_coverage_anchor_id
secondary_coverage_tags[]
role_id
use_context_id
statistical_stratum_id
statistical_slot_id
rights_instrument_evidence_id
privacy_attestation_evidence_id
gold_nonexposure_attestation_reference
content_authoring_record_id
record_canonical_sha256
```

No clinical text, answer or rubric appears in this record.

## 10. `LanguageVariantMetadata`

```text
variant_id
root_task_id
pair_id
language
content_artifact_sha256
source_route_record_id
parent_variant_ids[]
privacy_attestation_evidence_id
record_canonical_sha256
```

Arabic and English variants share one root and one pair ID. Translation/adaptation relationships are explicit parent/derivation inputs.

## 11. `PairMetadata`

```text
pair_id
root_task_id
arabic_variant_id
english_variant_id
pair_creation_method
clinical_semantic_equivalence_review_identity
statistical_unit_count = 1
record_canonical_sha256
```

Exactly one Arabic and one English variant are required for the paired unit. Variants are not independent N.

## 12. `ReviewBindingRecord`

```text
review_binding_id
pair_id
review_protocol_id
review_protocol_version
review_protocol_canonical_sha256
review_record_ids[]
adjudication_record_id_or_none
final_review_disposition
reviewed_pair_content_identity_sha256
record_canonical_sha256
```

Accepted pair evidence requires the current A8 protocol and fresh review for the exact content identity.

## 13. `ContaminationPlanRecord`

```text
contamination_plan_id
selection_content_universe_policy
exact_method_id
exact_method_version
semantic_method_id
semantic_method_version
semantic_threshold_policy_id
candidate_corpus_binding_policy
parent_aware = true
cross_lingual_semantic_assessment_required = true
record_canonical_sha256
```

This is a preconstruction plan identity, not an assessment result.

## 14. `PersonnelIdentityRecord`

```text
personnel_reference
identity_state
record_version
protected_evidence_reference
record_canonical_sha256
```

Identity states:

```text
REGISTERED_UNVERIFIED
VERIFIED
SUSPENDED
RETIRED
```

No name/email/phone/license document is required in the public record.

## 15. `PersonnelEligibilityRecord`

```text
eligibility_record_id
personnel_reference
role_class
suite_or_scope_id
identity_record_id
qualification_evidence_ids[]
conflict_disposition_record_id
gold_exposure_disposition_record_id
result_exposure_state
eligibility_state
reason_codes[]
record_canonical_sha256
```

Eligibility states:

```text
NOT_COMPUTED
ELIGIBLE
ELIGIBLE_WITH_SCOPE_LIMIT
BLOCKED_PENDING_EVIDENCE
INELIGIBLE
STALE_RECOMPUTE_REQUIRED
```

Eligibility is role/scope-specific, never global.

## 16. `RoleAssignmentRecord`

```text
assignment_id
personnel_reference
role_class
suite_or_scope_id
eligibility_record_id
assignment_state
record_canonical_sha256
```

Assignment states:

```text
PROPOSED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
```

`ACTIVE` assignment does not itself grant resource access.

## 17. `AccessHandshakeRecord`

```text
handshake_id
assignment_id
eligibility_record_id
signal
resource_zone
scope_id
record_canonical_sha256
```

Signals:

```text
ALLOW_GRANT_CONSIDERATION
DENY_GRANT
REVOKE_REQUIRED
REVALIDATION_REQUIRED
```

`ALLOW_GRANT_CONSIDERATION` is not an actual payload-access grant.

## 18. `AccessGrantMetadata`

```text
access_grant_id
personnel_reference
assignment_id
eligibility_record_id
resource_zone
scope_id
purpose
grant_state
authorization_reference
record_canonical_sha256
```

Real storage ACL provisioning is out of scope.

## 19. `A14RequirementManifest`

```text
requirement_manifest_id
exact_d34_design_id
exact_a8_protocol_id
exact_a7_roster_snapshot_id
work_packages[]
resource_capability_requirements[]
existing_authorized_capacity_records[]
capacity_gap_records[]
new_engagement_requirement_records[]
new_financial_commitment_requirement_records[]
requirement_disposition
record_canonical_sha256
```

Requirement disposition:

```text
NOT_REQUIRED
REQUIRED
BLOCKED_UNKNOWN_OR_INCOMPLETE
```

`REQUIRED` grants no spend authority.

## 20. `A14AuthorizationRecord`

```text
a14_authorization_id
authorization_version
requirement_manifest_id
requirement_manifest_sha256
bounded_scope
spend_categories[]
engagement_classes[]
payee_vendor_or_personnel_references[]
currency
max_committed_amount
max_payable_amount
authorized_period_or_expiry
stop_conditions[]
approval_decision_id
approval_decision_sha256
record_canonical_sha256
```

Lifecycle state is separate from immutable authorization identity:

```text
DRAFT_PROPOSED
PENDING_APPROVAL
APPROVED_NOT_ACTIVE
ACTIVE
SUSPENDED
EXHAUSTED
EXPIRED
REVOKED
SUPERSEDED
REJECTED
```

Only `ACTIVE` may cover a prospective new commitment.

## 21. `DeviceQualificationProtocol`

```text
protocol_id
protocol_version
targets[]
core_context_tokens = 8192
stress_context_tokens = 16384
prompt_budget_core = 7168
generation_budget = 1024
prompt_budget_stress = 15360
kv_k_type = Q8_0
kv_v_type = Q8_0
batch = 512
ubatch = 128
cache_reuse = false
measured_runs = 5
aggregation = MEDIAN_WITH_WORST_CASE
core_peak_memory_cap_bytes = 2147483648
package_hard_cap_bytes
package_target_bytes
package_stretch_bytes
runtime_identity_policy
memory_measurement_policy
timing_policy
thermal_policy
energy_policy
failure_semantics
record_canonical_sha256
```

Exact runtime/tool/build identities remain evidence fields and may be unresolved until execution preparation.

## 22. `ConstructionActivationRecord`

```text
activation_id
activation_version
preconstruction_snapshot_id
preconstruction_snapshot_sha256
required_gate_identities{}
authorization_decision_id
authorized_construction_scope[]
explicit_exclusions[]
activation_state
record_canonical_sha256
```

Synthetic fixtures may test validation. This implementation MUST NOT create a canonical real activation without separate authority.

## 23. `Spec005TournamentManifest`

```text
manifest_id
manifest_version
metrics_v2_identity
selection_quality_contract_identity
threshold_policy_identities[]
statistical_design_identities[]
preconstruction_snapshot_identity
construction_activation_identity_or_none
candidate_admission_records[]
device_protocol_identity
comparison_policy
spec004_manifest_projection
preflight_state
reason_codes[]
record_canonical_sha256
```

Preflight is fail closed. Only complete, exact, authorized evidence may yield a projection eligible for later Spec 004 comparison processing.

## 24. Relationship graph

```text
MetricsV2Catalog ───────────────┐
SelectionQualityContract ───────┤
ThresholdPolicyRecord ──────────┤
StatisticalDesignRecord ────────┤
SelectionSource/Pair/Review ────┼─> PreconstructionSnapshot
PersonnelEligibility/A13 ───────┤
A14Requirement/Authorization ───┘
                                  │
DeviceQualificationProtocol ──────┼─> Spec005TournamentManifest
                                  │
PreconstructionSnapshot ─────────> ConstructionActivationRecord
                                  │
ConstructionActivationRecord ─────┘

Spec005TournamentManifest -> validated projection -> existing Spec 004 tournament harness
```

## 25. Material-change rule

A material change to metric/evidence-role mapping, threshold/margin identity, statistical design/allocation, content/source route, scoring mapping, personnel eligibility, access binding, finance authorization, device protocol or activation prerequisite creates a new record identity and invalidates dependent cached PASS evidence until revalidated.