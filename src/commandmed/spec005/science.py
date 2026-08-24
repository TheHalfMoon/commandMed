"""Spec 005 scientific selection quality, threshold and statistical design.

US2 validators for the seven noncompensable quality lanes, A2 threshold/margin
policies and the atomic A3+A4 statistical design record. Purely deterministic
metadata validation: no scientific values are invented, defaulted or fetched.
"""

from __future__ import annotations

from typing import Any

EXPECTED_LANES = (
    "A_MEDICAL_KNOWLEDGE_BIOMEDICAL_REASONING",
    "B_PATIENT_CAREGIVER_CLINICAL_SAFETY",
    "C_UNCERTAINTY_ABSTENTION_INFORMATION_SEEKING",
    "D_EVIDENCE_GROUNDED_CLINICAL",
    "E_ARABIC_ENGLISH_PAIRED_CLINICAL_PARITY",
    "F_CLINICAL_PROFESSIONAL_REASONING_WORKFLOW",
    "G_LAB_DOCUMENT_STRUCTURED_QUALIFICATION",
)
SELECTION_ALLOWED_LANE_ROLES = frozenset({"SELECTION_DEV", "QUALIFICATION_ONLY"})
PROHIBITED_LANE_ROLES = frozenset({"PRIVATE_GOLD_FINAL_AUDIT", "PUBLIC_EXTERNAL_EVAL"})
ALLOWED_DIRECTIONS = frozenset({"HIGHER_BETTER", "LOWER_BETTER"})

THRESHOLD_REQUIRED_FIELDS = (
    "threshold_policy_id",
    "threshold_policy_version",
    "metric_id",
    "metric_evidence_role",
    "lane_id",
    "required_stratum_or_scope",
    "estimand_id",
    "metric_direction",
    "decision_role",
    "threshold_kind",
    "unit_or_scale",
    "clinical_meaningfulness_evidence_ids",
    "statistical_justification_evidence_ids",
    "clinical_review_authority_reference",
    "statistical_review_authority_reference",
    "conflict_disposition_record_ids",
    "pre_result_freeze",
    "record_canonical_sha256",
)
THRESHOLD_VALUE_FIELD = "threshold_value_or_margin"

DESIGN_REQUIRED_FIELDS = (
    "statistical_design_id",
    "design_version",
    "quality_lane",
    "metric_id_or_metric_mapping_id",
    "required_stratum_or_scope",
    "estimand",
    "unit_of_analysis",
    "decision_role",
    "threshold_policy_id_or_explicit_not_applicable",
    "precision_or_power_objective",
    "confidence_or_error_rate_parameters",
    "anticipated_rate_variance_or_other_nuisance_inputs",
    "source_and_provenance_for_planning_inputs",
    "pairing_or_cluster_dependency_model",
    "multiplicity_structure",
    "planned_numeric_n",
    "coverage_allocation_design",
    "rounding_or_allocation_rule",
    "software_formula_or_method_identity",
    "sensitivity_analysis_identity_or_explicit_not_required",
    "candidate_neutral",
    "pre_result_freeze",
    "record_canonical_sha256",
)

UNPAIRED_SHORTCUT_MARKERS = ("INDEPENDENT_TWO_SAMPLE", "UNPAIRED")


def _require_fields(record: Any, fields, prefix: str, errors: list[str]) -> None:
    if not isinstance(record, dict):
        errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
        return
    for field in fields:
        value = record.get(field)
        if value is None or (isinstance(value, str) and not value.strip()):
            errors.append(f"{prefix}:{field}_MISSING")


def validate_selection_quality_contract(
    contract: Any, metrics_v2: Any
) -> list[str]:
    """Validate the frozen selection-quality policy against metrics-v2."""
    errors: list[str] = []
    if not isinstance(contract, dict):
        return ["QualityContract:MALFORMED_RECORD_NOT_OBJECT"]
    if not isinstance(metrics_v2, dict):
        errors.append("MetricsV2:MALFORMED_RECORD_NOT_OBJECT")

    lanes = contract.get("required_quality_lanes")
    if not isinstance(lanes, list):
        lanes = []
        errors.append("QualityContract:REQUIRED_QUALITY_LANES_MUST_BE_SEVEN")
    if len(lanes) != len(set(lanes)):
        errors.append("QualityContract:DUPLICATE_QUALITY_LANE_PROHIBITED")
    for lane in lanes:
        if lane not in EXPECTED_LANES:
            errors.append(f"QualityContract:UNKNOWN_LANE_{lane}")
    for lane in EXPECTED_LANES:
        if lane not in lanes:
            errors.append(f"QualityContract:MISSING_REQUIRED_LANE_{lane}")

    anchors = contract.get("required_arabic_coverage_anchors")
    if not isinstance(anchors, list) or len(anchors) != 5:
        errors.append("QualityContract:MISSING_REQUIRED_ARABIC_COVERAGE_ANCHOR")

    language_scope = contract.get("required_language_scope")
    if not isinstance(language_scope, list) or not {"ar", "en"}.issubset(
        set(language_scope)
    ):
        errors.append("QualityContract:ARABIC_ENGLISH_LANGUAGE_SCOPE_REQUIRED")

    mapping_req = contract.get("metric_mapping_requirements")
    if not isinstance(mapping_req, dict):
        errors.append("QualityContract:METRIC_MAPPING_REQUIREMENTS_MISSING")
    else:
        allowed_roles = mapping_req.get("allowed_evidence_roles_for_lane_mapping")
        if isinstance(allowed_roles, list) and PROHIBITED_LANE_ROLES.intersection(
            allowed_roles
        ):
            leaked = sorted(PROHIBITED_LANE_ROLES.intersection(allowed_roles))
            errors.append(
                "QualityContract:LANE_MAPPING_PROHIBITED_EVIDENCE_ROLE_"
                + "_".join(leaked)
            )
        if mapping_req.get("metrics_catalog_schema_id") != (
            "commandmed-metrics-catalog"
        ) or mapping_req.get("metrics_catalog_schema_version") != "2.0":
            errors.append("QualityContract:METRICS_V2_CATALOG_IDENTITY_REQUIRED")

    invariants = contract.get("invariants")
    if not isinstance(invariants, list) or (
        "LANES_ARE_NONCOMPENSABLE=YES" not in invariants
    ):
        errors.append("QualityContract:NONCOMPENSABLE_LANE_INVARIANT_REQUIRED")
    return errors


def _validate_lane_mappings(records: dict, quality: dict, metrics_v2: dict) -> list[str]:
    """Every required lane needs exactly one explicit selection-eligible mapping."""
    errors: list[str] = []
    known_metric_ids = {
        m.get("metric_id") for m in metrics_v2.get("metrics", []) if isinstance(m, dict)
    }
    seen_lanes: set[str] = set()
    mappings = records.get("lane_metric_mappings")
    if not isinstance(mappings, list) or not mappings:
        return ["LaneMapping:NO_LANE_METRIC_MAPPINGS"]
    for index, mapping in enumerate(mappings):
        prefix = f"LaneMapping[{index}]"
        if not isinstance(mapping, dict):
            errors.append(f"{prefix}:MALFORMED_RECORD_NOT_OBJECT")
            continue
        lane = mapping.get("lane_id")
        metric_id = mapping.get("metric_id")
        role = mapping.get("metric_evidence_role")
        direction = mapping.get("metric_direction")
        if lane not in quality.get("required_quality_lanes", []):
            errors.append(f"{prefix}:UNKNOWN_LANE_{lane}")
        elif lane in seen_lanes:
            errors.append(f"{prefix}:DUPLICATE_LANE_MAPPING_{lane}")
        else:
            seen_lanes.add(lane)
        if metric_id not in known_metric_ids:
            errors.append(f"{prefix}:UNKNOWN_METRIC_{metric_id}")
        if role not in SELECTION_ALLOWED_LANE_ROLES:
            errors.append(f"{prefix}:EVIDENCE_ROLE_NOT_SELECTION_ELIGIBLE_{role}")
        if direction not in ALLOWED_DIRECTIONS:
            errors.append(f"{prefix}:METRIC_DIRECTION_NOT_EXPLICIT")
    for lane in quality.get("required_quality_lanes", []):
        if lane not in seen_lanes:
            errors.append(f"LaneMapping:MISSING_LANE_MAPPING_{lane}")
    return errors


def validate_threshold_policy(
    record: Any, quality_contract: Any, metrics_v2: Any
) -> list[str]:
    """Validate one A2 threshold/margin policy against lane and metric identity."""
    errors: list[str] = []
    _require_fields(record, THRESHOLD_REQUIRED_FIELDS, "ThresholdPolicy", errors)
    if not isinstance(record, dict):
        return errors

    known_metric_ids = {
        m.get("metric_id") for m in metrics_v2.get("metrics", []) if isinstance(m, dict)
    } if isinstance(metrics_v2, dict) else set()
    required_lanes = (
        quality_contract.get("required_quality_lanes", [])
        if isinstance(quality_contract, dict)
        else []
    )

    metric_id = record.get("metric_id")
    if metric_id not in known_metric_ids:
        errors.append(f"ThresholdPolicy:UNKNOWN_METRIC_{metric_id}")
    lane_id = record.get("lane_id")
    if lane_id not in required_lanes:
        errors.append(f"ThresholdPolicy:UNKNOWN_LANE_{lane_id}")
    role = record.get("metric_evidence_role")
    if role not in SELECTION_ALLOWED_LANE_ROLES:
        errors.append(f"ThresholdPolicy:EVIDENCE_ROLE_NOT_SELECTION_ELIGIBLE_{role}")
    direction = record.get("metric_direction")
    if direction not in ALLOWED_DIRECTIONS:
        errors.append(f"ThresholdPolicy:METRIC_DIRECTION_NOT_EXPLICIT_{direction}")

    # The exact threshold/margin value is conditionally required: absent while
    # draft is representable, but it blocks any PASS decision.
    if THRESHOLD_VALUE_FIELD not in record or record.get(THRESHOLD_VALUE_FIELD) is None:
        errors.append("ThresholdPolicy:INCOMPLETE_MISSING_THRESHOLD_VALUE_OR_MARGIN")

    if record.get("pre_result_freeze") is not True:
        errors.append("ThresholdPolicy:pre_result_freeze_MUST_BE_TRUE")
    return errors

def validate_statistical_design(
    record: Any, threshold_records: Any, quality_contract: Any
) -> list[str]:
    """Validate the atomic A3+A4 statistical design/allocation record."""
    errors: list[str] = []
    _require_fields(record, DESIGN_REQUIRED_FIELDS, "StatisticalDesign", errors)
    if not isinstance(record, dict):
        return errors

    required_lanes = (
        quality_contract.get("required_quality_lanes", [])
        if isinstance(quality_contract, dict)
        else []
    )
    lane = record.get("quality_lane")
    if lane not in required_lanes:
        errors.append(f"StatisticalDesign:UNKNOWN_LANE_{lane}")

    # Arabic parity lanes are paired/root-case aware; an unpaired independent
    # two-sample shortcut is contractually prohibited.
    dependency_model = record.get("pairing_or_cluster_dependency_model")
    if isinstance(dependency_model, str) and any(
        marker in dependency_model for marker in UNPAIRED_SHORTCUT_MARKERS
    ):
        errors.append(
            "StatisticalDesign:UNPAIRED_ARABIC_PARITY_SHORTCUT_PROHIBITED"
        )

    multiplicity = record.get("multiplicity_structure")
    if not isinstance(multiplicity, dict) or not multiplicity:
        errors.append("StatisticalDesign:multiplicity_structure_MISSING")

    if record.get("candidate_neutral") is not True:
        errors.append("StatisticalDesign:candidate_neutral_MUST_BE_TRUE")
    if record.get("pre_result_freeze") is not True:
        errors.append("StatisticalDesign:pre_result_freeze_MUST_BE_TRUE")

    n_value = record.get("planned_numeric_n")
    if not isinstance(n_value, int) or isinstance(n_value, bool) or n_value <= 0:
        errors.append("StatisticalDesign:planned_numeric_n_MISSING_OR_INVALID")
    allocation = record.get("coverage_allocation_design")
    if not isinstance(allocation, dict) or not allocation:
        errors.append("StatisticalDesign:coverage_allocation_design_MISSING")

    # Caller-owned outcome claims are never authoritative evidence.
    return errors


def evaluate_scientific_selection_readiness(
    records: Any, quality_contract: Any, metrics_v2: Any
) -> dict[str, object]:
    """Compute US2 readiness from bound records; fail closed on anything less."""
    reason_codes: list[str] = []
    contract_errors = validate_selection_quality_contract(
        quality_contract, metrics_v2
    )
    reason_codes.extend(contract_errors)

    if not isinstance(records, dict):
        reason_codes.append("ScientificReadiness:MALFORMED_RECORDS_NOT_OBJECT")
    elif not isinstance(quality_contract, dict):
        reason_codes.append("QualityContract:MALFORMED_RECORD_NOT_OBJECT")
    elif not isinstance(metrics_v2, dict):
        reason_codes.append("MetricsV2:MALFORMED_RECORD_NOT_OBJECT")
    else:
        reason_codes.extend(
            _validate_lane_mappings(records, quality_contract, metrics_v2)
        )

        thresholds = records.get("threshold_policies")
        if not isinstance(thresholds, list):
            thresholds = []
        for index, threshold in enumerate(thresholds):
            prefix = f"ThresholdPolicy[{index}]"
            errors = validate_threshold_policy(threshold, quality_contract, metrics_v2)
            reason_codes.extend(f"{prefix}:{e}" for e in errors)

        designs = records.get("statistical_designs")
        if not isinstance(designs, list):
            designs = []
        for index, design in enumerate(designs):
            prefix = f"StatisticalDesign[{index}]"
            errors = validate_statistical_design(
                design, thresholds, quality_contract
            )
            reason_codes.extend(f"{prefix}:{e}" for e in errors)

        if not thresholds:
            reason_codes.append("ScientificReadiness:NO_THRESHOLD_POLICIES")
        if not designs:
            reason_codes.append("ScientificReadiness:NO_STATISTICAL_DESIGNS")

        # Noncompensable lanes require decision-criteria coverage in both the
        # A2 threshold layer and the atomic A3+A4 design layer.
        required_lanes = set(quality_contract.get("required_quality_lanes", []))
        threshold_lanes = {
            t.get("lane_id")
            for t in thresholds
            if isinstance(t, dict)
        }
        design_lanes = {
            d.get("quality_lane")
            for d in designs
            if isinstance(d, dict)
        }
        for lane in sorted(required_lanes - threshold_lanes):
            reason_codes.append(f"ScientificReadiness:LANE_{lane}_THRESHOLD_COVERAGE_MISSING")
        for lane in sorted(required_lanes - design_lanes):
            reason_codes.append(f"ScientificReadiness:LANE_{lane}_DESIGN_COVERAGE_MISSING")

    unique_sorted = sorted(set(reason_codes))
    state = "READY_FOR_PRECONSTRUCTION" if not unique_sorted else "INCOMPLETE"
    return {"state": state, "reason_codes": unique_sorted}
