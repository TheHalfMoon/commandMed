"""Mechanical reliability-intervention primitives for CommandMed paper V5."""

from .case_generator import (
    case_space_size,
    cases_from_state_indices,
    deterministic_cases,
    deterministic_state_indices,
    expanded_domains,
)
from .contracts import (
    EffectInterval,
    classify_effect,
    hard_gate_noninferiority_pass,
    order_gap,
    ordered_interaction,
)
from .objectives import (
    capability_retention_penalty,
    contract_consistency_penalty,
    contract_regularized_objective,
    negative_log_likelihood_for_target,
    retention_regularized_objective,
    typed_readout_logits,
    typed_readout_probabilities,
)
from .policy import SelectiveDecision, fixed_defer_policy
from .preflight import (
    APPROVED_MODEL_REPO,
    APPROVED_MODEL_REVISION,
    DevelopmentAuthority,
    DevelopmentRunManifest,
    PreflightDecision,
    evaluate_development_preflight,
)
from .probability import (
    ProbabilityContractError,
    multiclass_brier,    negative_log_likelihood,
    normalize_probabilities,
    softmax,
    temperature_scale_logits,
)
from .quarantine import (
    assignment_commitment,
    confirmatory_reserve_state_partition,
    derive_partition_seed,
    prefreeze_state_partition,
)
from .registry import INTERVENTIONS, ORDERED_INTERACTION_CANDIDATES, get_intervention
from .rule_tool import RuleToolResult, execute_rule_tool
from .selection_bias import (
    align_display_to_semantic,
    debias_and_align,
    debias_display_distribution,
    estimate_display_slot_prior,
    mean_semantic_distribution,
)
