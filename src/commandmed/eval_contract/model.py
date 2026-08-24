"""Data models and enums for commandMed evaluation governance."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AccessClass(str, Enum):
    """Access classification for benchmark/evaluation assets."""

    PUBLIC = "PUBLIC"
    GATED = "GATED"
    PRIVATE_EXTERNAL = "PRIVATE_EXTERNAL"
    REFERENCE_ONLY = "REFERENCE_ONLY"
    MIXED = "MIXED"


class VerificationStatus(str, Enum):
    """Status of source verification for benchmark records."""

    VERIFIED = "VERIFIED"
    UNRESOLVED = "UNRESOLVED"
    EXCLUDED = "EXCLUDED"


class LicenseStatus(str, Enum):
    """Controlled vocabulary for benchmark license status (fail-closed).

    Only statuses verified as present in the canonical registry are listed.
    Arbitrary license strings are rejected by validation.
    """

    MIT = "MIT"
    APACHE_2_0 = "Apache-2.0"
    CC_BY_NC_4_0 = "CC-BY-NC-4.0"
    COMPONENT_SPECIFIC = "COMPONENT_SPECIFIC"
    UNRESOLVED = "UNRESOLVED"


class IntendedUse(str, Enum):
    """Permitted commandMed research usage for an evaluation suite."""

    DEVELOPMENT = "DEVELOPMENT"
    REFERENCE_ONLY = "REFERENCE_ONLY"
    POSSIBLE_RELEASE_GATE = "POSSIBLE_RELEASE_GATE"
    PROHIBITED = "PROHIBITED"


class Role(str, Enum):
    """commandMed behavioral and evaluation roles."""

    PATIENT_CAREGIVER = "PATIENT_CAREGIVER"
    CLINICAL_PROFESSIONAL = "CLINICAL_PROFESSIONAL"
    LEARNER_RESEARCHER = "LEARNER_RESEARCHER"
    MULTI_ROLE = "MULTI_ROLE"


class Modality(str, Enum):
    """Evaluation input modalities."""

    TEXT = "TEXT"
    DOCUMENT = "DOCUMENT"
    LAB_REPORT = "LAB_REPORT"
    PHOTO = "PHOTO"
    MULTIMODAL = "MULTIMODAL"


class CapabilityDomain(str, Enum):
    """Core evaluated medical and reasoning domains."""

    KNOWLEDGE = "KNOWLEDGE"
    REASONING = "REASONING"
    SAFETY = "SAFETY"
    DIAGNOSTIC = "DIAGNOSTIC"
    EVIDENCE_USE = "EVIDENCE_USE"
    UNCERTAINTY_ABSTENTION = "UNCERTAINTY_ABSTENTION"
    COMMUNICATION = "COMMUNICATION"
    WORKFLOW = "WORKFLOW"
    EXTRACTION = "EXTRACTION"
    RESOURCE_EFFICIENCY = "RESOURCE_EFFICIENCY"


class ContaminationSensitivity(str, Enum):
    """Sensitivity to pretraining/training contamination."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"


class MetricDirection(str, Enum):
    """Optimization direction for a metric."""

    HIGHER_BETTER = "HIGHER_BETTER"
    LOWER_BETTER = "LOWER_BETTER"
    TARGET_RANGE = "TARGET_RANGE"


class ThresholdState(str, Enum):
    """State of metric threshold freezing."""

    DEFINED_NOT_YET_THRESHOLD_FROZEN = "DEFINED_NOT_YET_THRESHOLD_FROZEN"
    FROZEN = "FROZEN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class GateEvaluationState(str, Enum):
    """Outcome status for a gate or evaluation suite."""

    PASS = "PASS"
    FAIL = "FAIL"
    NOT_EVALUATED = "NOT_EVALUATED"
    BLOCKED = "BLOCKED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class Purpose(str, Enum):
    """Logical purposes for data and evaluation artifacts."""

    TRAIN = "TRAIN"
    DEV = "DEV"
    CALIBRATION = "CALIBRATION"
    CHECKPOINT_SELECTION = "CHECKPOINT_SELECTION"
    PUBLIC_EXTERNAL_EVAL = "PUBLIC_EXTERNAL_EVAL"
    PRIVATE_GOLD = "PRIVATE_GOLD"


class MetricEvidenceRole(str, Enum):
    """Lifecycle role of evidence attached to a V2 metric contract."""

    SELECTION_DEV = "SELECTION_DEV"
    PRIVATE_GOLD_FINAL_AUDIT = "PRIVATE_GOLD_FINAL_AUDIT"
    PUBLIC_EXTERNAL_EVAL = "PUBLIC_EXTERNAL_EVAL"
    QUALIFICATION_ONLY = "QUALIFICATION_ONLY"


class EvidenceBindingMode(str, Enum):
    """Identity-binding mode for a V2 metric evidence requirement."""

    MANIFEST_BOUND = "MANIFEST_BOUND"
    CANONICAL_FAMILY_BOUND = "CANONICAL_FAMILY_BOUND"


class EvidenceSourcePolicy(str, Enum):
    """Permitted source policy for a V2 metric evidence requirement."""

    SELECTION_SAFE_NON_GOLD = "SELECTION_SAFE_NON_GOLD"
    PRIVATE_GOLD_FAMILY = "PRIVATE_GOLD_FAMILY"
    PUBLIC_EXTERNAL_TEST_ONLY = "PUBLIC_EXTERNAL_TEST_ONLY"
    IDENTITY_BOUND_QUALIFICATION_ASSET = "IDENTITY_BOUND_QUALIFICATION_ASSET"


class GoldFamilyId(str, Enum):
    """The three canonical private Gold families."""

    COMMANDMED_CLINICAL_GOLD = "COMMANDMED_CLINICAL_GOLD"
    COMMANDMED_ARABIC_GOLD = "COMMANDMED_ARABIC_GOLD"
    COMMANDMED_MULTIMODAL_GOLD = "COMMANDMED_MULTIMODAL_GOLD"


class ExactMatchStatus(str, Enum):
    """Status of exact-match contamination evaluation."""

    NOT_ASSESSED = "NOT_ASSESSED"
    PENDING = "PENDING"
    CHECKED_CLEAN = "CHECKED_CLEAN"
    OVERLAP_FOUND = "OVERLAP_FOUND"
    BLOCKED = "BLOCKED"


class SemanticOverlapStatus(str, Enum):
    """Status of semantic-overlap contamination evaluation."""

    NOT_ASSESSED = "NOT_ASSESSED"
    PENDING = "PENDING"
    ASSESSED_LOW_RISK = "ASSESSED_LOW_RISK"
    ASSESSED_HIGH_RISK = "ASSESSED_HIGH_RISK"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class BenchmarkRecord:
    """Metadata record for a registered benchmark family."""

    benchmark_id: str
    canonical_name: str
    primary_source: str
    source_uri: str
    source_identifier: str
    source_revision: str
    verification_date: str
    artifact_version: str
    access_class: str
    license_status: str
    license_source_uri: str
    languages: tuple[str, ...]
    roles: tuple[str, ...]
    modalities: tuple[str, ...]
    capability_domains: tuple[str, ...]
    contamination_sensitivity: str
    intended_use: str
    verification_status: str
    notes: str


@dataclass(frozen=True)
class MetricRecord:
    """Metadata record for an evaluation metric or hard safety gate."""

    metric_id: str
    name: str
    category: str
    description: str
    direction: str
    unit: str
    is_hard_gate: bool
    threshold_state: str
    applicable_roles: tuple[str, ...]
    applicable_modalities: tuple[str, ...]
    applicable_languages: tuple[str, ...]
    required_evidence: str


@dataclass(frozen=True)
class MetricEvidenceRequirement:
    """Machine-readable evidence-role requirement for a V2 metric record."""

    evidence_role: str
    purpose: str
    evidence_kind: str
    binding_mode: str
    source_policy: str
    requirement: str


@dataclass(frozen=True)
class MetricRecordV2:
    """Version 2 metric record with explicit lifecycle evidence roles."""

    metric_id: str
    name: str
    category: str
    description: str
    direction: str
    unit: str
    is_hard_gate: bool
    threshold_state: str
    applicable_roles: tuple[str, ...]
    applicable_modalities: tuple[str, ...]
    applicable_languages: tuple[str, ...]
    evidence_requirements: tuple[MetricEvidenceRequirement, ...]


@dataclass(frozen=True)
class MetricsV2Catalog:
    """Versioned additive metrics catalog envelope."""

    schema_id: str
    schema_version: str
    supersedes_metrics_v1_sha256: str
    metrics: tuple[MetricRecordV2, ...]


@dataclass(frozen=True)
class GoldProtocolRecord:
    """Governance protocol for a private Gold evaluation family (metadata only)."""

    family_id: str
    display_name: str
    purpose: str
    intended_strata: tuple[str, ...]
    content_location_policy: str
    allowed_access_roles: tuple[str, ...]
    adjudication_policy: str
    power_analysis_required: bool
    prohibited_optimization_uses: tuple[str, ...]
    permitted_scoring_stages: tuple[str, ...]
    release_claim_scope: str
    audit_requirements: str


@dataclass(frozen=True)
class QuarantineRule:
    """Rule defining permitted and prohibited data purpose transitions."""

    purpose: str
    allowed_sources: tuple[str, ...]
    prohibited_sources: tuple[str, ...]
    can_train: bool
    can_select_model: bool


@dataclass(frozen=True)
class ContaminationRecord:
    """Interface and evidence record for benchmark contamination assessment."""

    asset_id: str
    exact_match_status: str
    semantic_overlap_status: str
    evidence_artifact_id: str
    methodology_interface: str
    notes: str
