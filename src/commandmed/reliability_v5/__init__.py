"""Mechanical reliability-intervention primitives for CommandMed paper V5."""

from .contracts import (
    EffectInterval,
    classify_effect,
    hard_gate_noninferiority_pass,
    order_gap,
    ordered_interaction,
)
from .policy import SelectiveDecision, fixed_defer_policy
from .probability import (
    ProbabilityContractError,
    multiclass_brier,
    negative_log_likelihood,
    normalize_probabilities,
    softmax,
    temperature_scale_logits,
)
from .registry import INTERVENTIONS, ORDERED_INTERACTION_CANDIDATES, get_intervention
from .selection_bias import (
    align_display_to_semantic,
    debias_and_align,
    debias_display_distribution,
    estimate_display_slot_prior,
    mean_semantic_distribution,
)
from .case_generator import case_space_size, deterministic_cases, expanded_domains

from .rule_tool import RuleToolResult, execute_rule_tool
