"""Prospective V5 intervention registry.

The registry separates mechanically implemented interventions from model/training
objective mechanics that remain non-executable until separately authorized.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InterventionSpec:
    intervention_id: str
    locus: str
    target_axes: tuple[str, ...]
    implementation_status: str
    changes_model_parameters: bool
    execution_authority: str = "NO"


IMPLEMENTED = "MECHANICAL_IMPLEMENTED"
OBJECTIVE_MECHANICS_IMPLEMENTED = "OBJECTIVE_MECHANICS_IMPLEMENTED"
CONTRACT_ONLY = "CONTRACT_ONLY"

INTERVENTIONS = {
    "A1_TS_V1": InterventionSpec(
        "A1_TS_V1", "POST_PROCESSING", ("CALIBRATION",), IMPLEMENTED, False
    ),
    "A2_SELBIAS_V1": InterventionSpec(
        "A2_SELBIAS_V1", "POST_PROCESSING", ("SEMANTIC_STABILITY",), IMPLEMENTED, False
    ),
    "B1_TYPED_V1": InterventionSpec(
        "B1_TYPED_V1", "DECISION_INTERFACE", ("DECISION_QUALITY",), OBJECTIVE_MECHANICS_IMPLEMENTED, True
    ),
    "C1_CRDI_V1": InterventionSpec(
        "C1_CRDI_V1", "MODEL_ADAPTATION", ("SEMANTIC_STABILITY",), OBJECTIVE_MECHANICS_IMPLEMENTED, True
    ),
    "C2_CRDI_RETAIN_V1": InterventionSpec(
        "C2_CRDI_RETAIN_V1",
        "MODEL_ADAPTATION",
        ("SEMANTIC_STABILITY", "CAPABILITY_RETENTION"),
        OBJECTIVE_MECHANICS_IMPLEMENTED,
        True,
    ),
    "D1_DEFER_V1": InterventionSpec(
        "D1_DEFER_V1", "DEPLOYMENT_POLICY", ("SELECTIVE_CONTROL",), IMPLEMENTED, False
    ),
    "D2_RULETOOL_V1": InterventionSpec(
        "D2_RULETOOL_V1", "DETERMINISTIC_TOOL_ROUTING", ("RULE_CONFORMANCE",), IMPLEMENTED, False
    ),
}

ORDERED_INTERACTION_CANDIDATES = (
    ("A1_TS_V1", "A2_SELBIAS_V1"),
    ("A2_SELBIAS_V1", "A1_TS_V1"),
    ("A1_TS_V1", "C1_CRDI_V1"),
    ("C1_CRDI_V1", "A1_TS_V1"),
)


def get_intervention(intervention_id: str) -> InterventionSpec:
    """Return an exact registry entry; unknown IDs fail closed."""
    try:
        return INTERVENTIONS[intervention_id]
    except KeyError as exc:
        raise KeyError(f"unknown V5 intervention id: {intervention_id}") from exc
