"""Non-executing E004 Transformers/PyTorch adapter control plane.

This module binds the frozen SAFETENSORS candidates to deterministic scoring and
resource-operation projections. It never imports Transformers or Torch, opens
model files, loads weights, invokes a process, accesses the network, selects a
winner, grants A15, or performs execution.
"""

from __future__ import annotations

import hashlib
from typing import Any, Mapping, Sequence

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.e004_execution_adapter import (
    FROZEN_EVALUATION_ASSETS,
    MULTIPLE_CHOICE_ASSET_KIND,
    MULTIPLE_CHOICE_SCORING_METHOD,
    RESOURCE_ASSET_KIND,
    RESOURCE_SCORING_METHOD,
)
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_candidate_bundle import (
    CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
    validate_candidate_artifact_bundle_set,
)
from src.commandmed.spec007.research_execution import (
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)
from src.commandmed.spec007.research_tournament_assets import (
    validate_research_component_evaluation_asset_set,
)

TRANSFORMERS_VERSION = "4.57.6"
TRANSFORMERS_SOURCE_REVISION = "753d61104116eefc8ffc977327b441ee0c8d599f"
TORCH_VERSION = "2.11.0+cpu"
PYTHON_RUNTIME_ENTRYPOINT = "python3.12"
PYTHON_RUNTIME_PATH = "/usr/bin/python3.12"
PYTHON_RUNTIME_VERSION = "3.12.3"
PYTHON_RUNTIME_SHA256 = (
    "a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223"
)
TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256 = (
    "bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05"
)
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256 = (
    "54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384"
)
TRANSFORMERS_MODULE_SHA256 = (
    "aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04"
)
TORCH_MODULE_SHA256 = (
    "0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001"
)

GRANITE_CANDIDATE = PRIMARY_CANDIDATES[2]
TRANSFORMERS_CANDIDATES = frozenset({GRANITE_CANDIDATE, CONTROL_CANDIDATE})

_CANDIDATE_RUNTIME_FACTS: dict[tuple[str, str], dict[str, Any]] = {
    GRANITE_CANDIDATE: {
        "candidate_role": "PRIMARY",
        "winner_eligible": True,
        "model_artifact_sha256": (
            "a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0"
        ),
        "model_artifact_bytes": 704786224,
        "complete_bundle_sha256": (
            "90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db"
        ),
        "complete_bundle_bytes": 714515562,
        "tokenizer_config_sha256": (
            "a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86"
        ),
        "architecture_config_module_sha256": (
            "535090da0bd3606c7be77517d2de4839f70b9658a40d4ec9ba98fb365397dc39"
        ),
        "architecture_modeling_module_sha256": (
            "920678d503bcb6795ba46c1b9579c28aad208a3ff0b73e7e02754e7cd9e3c19c"
        ),
    },
    CONTROL_CANDIDATE: {
        "candidate_role": "CONTROL",
        "winner_eligible": False,
        "model_artifact_sha256": (
            "d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397"
        ),
        "model_artifact_bytes": 8044982000,
        "complete_bundle_sha256": (
            "9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9"
        ),
        "complete_bundle_bytes": 8056508630,
        "tokenizer_config_sha256": (
            "3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5"
        ),
        "architecture_config_module_sha256": (
            "27863e9718fdbc899f2d0e567621e4d3d36d8dc500c1d54b49dba4242d08d2bd"
        ),
        "architecture_modeling_module_sha256": (
            "4b95c371fd26d40c69083dab36ac1eafd8cf82b415a0bb827275097c5ad2305b"
        ),
    },
}

LOADER_POLICY = {
    "model_api": "AutoModelForCausalLM.from_pretrained",
    "tokenizer_api": "AutoTokenizer.from_pretrained",
    "local_files_only": True,
    "trust_remote_code": False,
    "requested_device": "cpu",
    "requested_dtype": "auto",
    "network_allowed": False,
}

SCORING_CONTRACT = {
    "scoring_method": MULTIPLE_CHOICE_SCORING_METHOD,
    "sequence_construction": "PROMPT_PLUS_SINGLE_ASCII_SPACE_PLUS_CHOICE",
    "add_special_tokens": True,
    "common_prefix_semantics": "LONGEST_COMMON_TOKEN_ID_PREFIX_ACROSS_CHOICES",
    "scored_region": "CHOICE_DEPENDENT_CONTINUATION_FROM_COMMON_PREFIX",
    "token_score": "AUTOREGRESSIVE_LOG_SOFTMAX_NEXT_TOKEN",
    "normalization": "MEAN_LOG_PROBABILITY_PER_SCORED_TOKEN",
    "selection": "MAX_NORMALIZED_LOG_PROBABILITY",
    "tie_policy": "FIRST_IN_FROZEN_CHOICE_ORDER",
    "choice_order": ["A", "B", "C", "D"],
}

RESOURCE_GENERATION_CONTRACT = {
    "generation_mode": "GREEDY_CAUSAL_LM",
    "do_sample": False,
    "max_new_tokens": 8,
    "seed": 1,
    "network_allowed": False,
    "required_measurements": [
        "MODEL_ARTIFACT_BYTES",
        "PEAK_RSS_BYTES",
        "TIME_TO_FIRST_TOKEN_MS",
        "DECODE_TOKENS_PER_SECOND",
        "WALL_CLOCK_MS",
    ],
}

_MANIFEST_FIELDS = (
    "schema_version",
    "adapter_id",
    "adapter_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "candidate_bundle_set_sha256",
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "artifact_format",
    "model_artifact_sha256",
    "model_artifact_bytes",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "tokenizer_config_sha256",
    "backend_family",
    "transformers_version",
    "transformers_source_revision",
    "torch_version",
    "python_runtime_entrypoint",
    "python_runtime_path",
    "python_runtime_version",
    "python_runtime_sha256",
    "dependency_set_manifest_sha256",
    "installed_environment_manifest_sha256",
    "transformers_module_sha256",
    "torch_module_sha256",
    "architecture_config_module_sha256",
    "architecture_modeling_module_sha256",
    "loader_policy",
    "scoring_contract",
    "resource_generation_contract",
    "operations",
    "execution_performed",
    "runtime_format_compatibility_state",
    "authorized_spend_usd",
)
_OPERATION_FIELDS = (
    "operation_id",
    "operation_kind",
    "asset_id",
    "asset_sha256",
    "scoring_method",
    "input_identity",
    "expected_output_kind",
    "invocations",
)
_INVOCATION_FIELDS = (
    "invocation_id",
    "probe_id",
    "run_class",
    "run_index",
    "input_text_sha256",
    "max_new_tokens",
)


def _self_hash(record: Mapping[str, Any], field: str) -> str:
    projection = dict(record)
    projection.pop(field, None)
    return compute_canonical_sha256(projection)


def compute_e004_transformers_adapter_sha256(manifest: Mapping[str, Any]) -> str:
    """Compute one deterministic adapter-manifest identity."""
    return _self_hash(manifest, "adapter_sha256")


def _require_asset_set(asset_set: Any) -> dict[str, Mapping[str, Any]]:
    errors = validate_research_component_evaluation_asset_set(asset_set)
    if errors or not isinstance(asset_set, dict):
        raise ValueError("evaluation asset set is not canonically valid")
    if asset_set.get("asset_set_sha256") != RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256:
        raise ValueError("evaluation asset set identity mismatch")
    records = asset_set.get("asset_records")
    if not isinstance(records, list) or len(records) != 7:
        raise ValueError("frozen asset set must contain exactly seven records")
    by_id: dict[str, Mapping[str, Any]] = {}
    for asset in records:
        if not isinstance(asset, dict):
            raise ValueError("evaluation asset records must be objects")
        asset_id = str(asset.get("asset_id"))
        frozen = FROZEN_EVALUATION_ASSETS.get(asset_id)
        if frozen is None:
            raise ValueError("evaluation asset is outside frozen set")
        expected_sha, expected_kind, expected_scoring = frozen
        if asset.get("asset_sha256") != expected_sha:
            raise ValueError("evaluation asset sha256 mismatch")
        if asset.get("asset_kind") != expected_kind:
            raise ValueError("evaluation asset kind mismatch")
        if asset.get("scoring_method") != expected_scoring:
            raise ValueError("evaluation asset scoring method mismatch")
        if asset_id in by_id:
            raise ValueError("duplicate evaluation asset")
        by_id[asset_id] = asset
    if set(by_id) != set(FROZEN_EVALUATION_ASSETS):
        raise ValueError("frozen evaluation asset coverage mismatch")
    return by_id


def _require_candidate_bundle(
    bundle_set: Any, candidate_id: str, upstream_revision: str
) -> Mapping[str, Any]:
    errors = validate_candidate_artifact_bundle_set(bundle_set)
    if errors or not isinstance(bundle_set, dict):
        raise ValueError("candidate artifact bundle set is not canonically valid")
    if bundle_set.get("bundle_set_sha256") != CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256:
        raise ValueError("candidate artifact bundle set identity mismatch")
    pair = (candidate_id, upstream_revision)
    if pair not in TRANSFORMERS_CANDIDATES:
        raise ValueError("candidate is not assigned to the Transformers/PyTorch route")
    bundles = bundle_set.get("candidate_bundles")
    if not isinstance(bundles, list):
        raise ValueError("candidate bundle records are missing")
    for bundle in bundles:
        if not isinstance(bundle, dict):
            continue
        if (bundle.get("candidate_id"), bundle.get("upstream_revision")) == pair:
            if bundle.get("artifact_format") != "SAFETENSORS":
                raise ValueError("Transformers candidate must use frozen SAFETENSORS bundle")
            return bundle
    raise ValueError("candidate bundle is missing")


def normalized_log_likelihood_argmax(
    log_probability_sums: Sequence[float], scored_token_counts: Sequence[int]
) -> int:
    """Select the first maximum mean continuation log-probability.

    This pure helper mirrors the frozen normalization/tie policy and performs no
    tokenization, model call, or runtime import.
    """
    if len(log_probability_sums) != 4 or len(scored_token_counts) != 4:
        raise ValueError("exactly four frozen choices are required")
    means: list[float] = []
    for total, count in zip(log_probability_sums, scored_token_counts, strict=True):
        if not isinstance(total, (int, float)) or isinstance(total, bool):
            raise ValueError("log probability sums must be numeric")
        if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            raise ValueError("scored token counts must be positive integers")
        means.append(float(total) / count)
    winner = 0
    for index in range(1, len(means)):
        if means[index] > means[winner]:
            winner = index
    return winner


def _build_resource_invocations(asset: Mapping[str, Any]) -> list[dict[str, Any]]:
    probes = asset.get("probes")
    if not isinstance(probes, list) or len(probes) != 8:
        raise ValueError("frozen resource asset must contain exactly eight probes")
    invocations: list[dict[str, Any]] = []
    for probe in probes:
        if not isinstance(probe, dict):
            raise ValueError("resource probes must be object records")
        if probe.get("warmup_runs") != 1 or probe.get("measured_runs") != 3:
            raise ValueError("resource run counts mismatch")
        if probe.get("max_new_tokens") != 8:
            raise ValueError("resource max_new_tokens mismatch")
        required = probe.get("required_measurements")
        if required != RESOURCE_GENERATION_CONTRACT["required_measurements"]:
            raise ValueError("resource required_measurements mismatch")
        probe_id = str(probe.get("probe_id"))
        text = probe.get("input_text")
        if not isinstance(text, str) or not text:
            raise ValueError("resource input_text must be non-empty")
        input_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        invocations.append(
            {
                "invocation_id": f"{probe_id}-WARMUP-01",
                "probe_id": probe_id,
                "run_class": "WARMUP",
                "run_index": 1,
                "input_text_sha256": input_sha,
                "max_new_tokens": 8,
            }
        )
        for run_index in range(1, 4):
            invocations.append(
                {
                    "invocation_id": f"{probe_id}-MEASURED-{run_index:02d}",
                    "probe_id": probe_id,
                    "run_class": "MEASURED",
                    "run_index": run_index,
                    "input_text_sha256": input_sha,
                    "max_new_tokens": 8,
                }
            )
    return invocations


def build_e004_transformers_adapter_manifest(
    asset_set: Any,
    bundle_set: Any,
    *,
    candidate_id: str,
    upstream_revision: str,
) -> dict[str, Any]:
    """Build one deterministic non-executing SAFETENSORS adapter manifest."""
    by_id = _require_asset_set(asset_set)
    bundle = _require_candidate_bundle(bundle_set, candidate_id, upstream_revision)
    pair = (candidate_id, upstream_revision)
    facts = _CANDIDATE_RUNTIME_FACTS[pair]

    for field in (
        "candidate_role",
        "winner_eligible",
        "model_artifact_sha256",
        "model_artifact_bytes",
        "complete_bundle_sha256",
        "complete_bundle_bytes",
        "tokenizer_config_sha256",
    ):
        if bundle.get(field) != facts[field]:
            raise ValueError(f"candidate bundle {field} does not match frozen route fact")

    operations: list[dict[str, Any]] = []
    for asset_id in sorted(by_id):
        asset = by_id[asset_id]
        if asset.get("asset_kind") == MULTIPLE_CHOICE_ASSET_KIND:
            cases = asset.get("cases")
            if not isinstance(cases, list) or len(cases) != 12:
                raise ValueError("frozen multiple-choice asset must contain exactly 12 cases")
            operations.append(
                {
                    "operation_id": f"{asset_id}-MC-SCORE",
                    "operation_kind": "MULTIPLE_CHOICE_SCORE",
                    "asset_id": asset_id,
                    "asset_sha256": asset.get("asset_sha256"),
                    "scoring_method": MULTIPLE_CHOICE_SCORING_METHOD,
                    "input_identity": asset.get("asset_sha256"),
                    "expected_output_kind": "ASSET_ACCURACY_RECORD_V1",
                    "invocations": [
                        {
                            "invocation_id": f"{asset_id}-MC-SCORE-01",
                            "probe_id": None,
                            "run_class": "SCORING",
                            "run_index": 1,
                            "input_text_sha256": asset.get("asset_sha256"),
                            "max_new_tokens": 0,
                        }
                    ],
                }
            )
        elif asset.get("asset_kind") == RESOURCE_ASSET_KIND:
            operations.append(
                {
                    "operation_id": f"{asset_id}-RESOURCE",
                    "operation_kind": "RESOURCE_MEASUREMENT",
                    "asset_id": asset_id,
                    "asset_sha256": asset.get("asset_sha256"),
                    "scoring_method": RESOURCE_SCORING_METHOD,
                    "input_identity": asset.get("asset_sha256"),
                    "expected_output_kind": "RESOURCE_MEASUREMENT_RECORD_V1",
                    "invocations": _build_resource_invocations(asset),
                }
            )
        else:
            raise ValueError("unsupported frozen evaluation asset kind")

    manifest: dict[str, Any] = {
        "schema_version": "1",
        "adapter_id": f"SP007-RO-001-TRANSFORMERS-ADAPTER::{candidate_id}@{upstream_revision}",
        "adapter_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_bundle_set_sha256": CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "candidate_id": candidate_id,
        "upstream_revision": upstream_revision,
        "candidate_role": facts["candidate_role"],
        "winner_eligible": facts["winner_eligible"],
        "artifact_format": "SAFETENSORS",
        "model_artifact_sha256": facts["model_artifact_sha256"],
        "model_artifact_bytes": facts["model_artifact_bytes"],
        "complete_bundle_sha256": facts["complete_bundle_sha256"],
        "complete_bundle_bytes": facts["complete_bundle_bytes"],
        "tokenizer_config_sha256": facts["tokenizer_config_sha256"],
        "backend_family": "TRANSFORMERS_TORCH_CPU",
        "transformers_version": TRANSFORMERS_VERSION,
        "transformers_source_revision": TRANSFORMERS_SOURCE_REVISION,
        "torch_version": TORCH_VERSION,
        "python_runtime_entrypoint": PYTHON_RUNTIME_ENTRYPOINT,
        "python_runtime_path": PYTHON_RUNTIME_PATH,
        "python_runtime_version": PYTHON_RUNTIME_VERSION,
        "python_runtime_sha256": PYTHON_RUNTIME_SHA256,
        "dependency_set_manifest_sha256": TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256,
        "installed_environment_manifest_sha256": TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
        "transformers_module_sha256": TRANSFORMERS_MODULE_SHA256,
        "torch_module_sha256": TORCH_MODULE_SHA256,
        "architecture_config_module_sha256": facts["architecture_config_module_sha256"],
        "architecture_modeling_module_sha256": facts["architecture_modeling_module_sha256"],
        "loader_policy": dict(LOADER_POLICY),
        "scoring_contract": dict(SCORING_CONTRACT),
        "resource_generation_contract": dict(RESOURCE_GENERATION_CONTRACT),
        "operations": operations,
        "execution_performed": False,
        "runtime_format_compatibility_state": "NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE",
        "authorized_spend_usd": 0,
    }
    manifest["adapter_sha256"] = compute_e004_transformers_adapter_sha256(manifest)
    return manifest


def _expected_resource_invocations(asset_id: str) -> set[tuple[str, str, int, str]]:
    expected: set[tuple[str, str, int, str]] = set()
    for probe_index in range(1, 9):
        probe_id = f"{asset_id}-PROBE-{probe_index:02d}"
        expected.add((probe_id, "WARMUP", 1, f"{probe_id}-WARMUP-01"))
        for run_index in range(1, 4):
            expected.add(
                (probe_id, "MEASURED", run_index, f"{probe_id}-MEASURED-{run_index:02d}")
            )
    return expected


def validate_e004_transformers_adapter_manifest(
    manifest: Any, asset_set: Any, bundle_set: Any
) -> list[str]:
    """Validate one deterministic Transformers adapter manifest fail closed."""
    prefix = "E004TransformersAdapterManifest"
    errors = validate_closed_object(manifest, required_fields=_MANIFEST_FIELDS, field=prefix)
    if errors or not isinstance(manifest, dict):
        return errors
    try:
        by_id = _require_asset_set(asset_set)
        bundle = _require_candidate_bundle(
            bundle_set,
            str(manifest.get("candidate_id")),
            str(manifest.get("upstream_revision")),
        )
    except ValueError as exc:
        return [f"{prefix}: {exc}"]

    pair = (manifest.get("candidate_id"), manifest.get("upstream_revision"))
    facts = _CANDIDATE_RUNTIME_FACTS.get(pair)
    if facts is None:
        return [f"{prefix}: candidate route mismatch"]

    expected = {
        "schema_version": "1",
        "adapter_id": (
            f"SP007-RO-001-TRANSFORMERS-ADAPTER::{manifest.get('candidate_id')}@"
            f"{manifest.get('upstream_revision')}"
        ),
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_bundle_set_sha256": CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "candidate_role": facts["candidate_role"],
        "winner_eligible": facts["winner_eligible"],
        "artifact_format": "SAFETENSORS",
        "model_artifact_sha256": facts["model_artifact_sha256"],
        "model_artifact_bytes": facts["model_artifact_bytes"],
        "complete_bundle_sha256": facts["complete_bundle_sha256"],
        "complete_bundle_bytes": facts["complete_bundle_bytes"],
        "tokenizer_config_sha256": facts["tokenizer_config_sha256"],
        "backend_family": "TRANSFORMERS_TORCH_CPU",
        "transformers_version": TRANSFORMERS_VERSION,
        "transformers_source_revision": TRANSFORMERS_SOURCE_REVISION,
        "torch_version": TORCH_VERSION,
        "python_runtime_entrypoint": PYTHON_RUNTIME_ENTRYPOINT,
        "python_runtime_path": PYTHON_RUNTIME_PATH,
        "python_runtime_version": PYTHON_RUNTIME_VERSION,
        "python_runtime_sha256": PYTHON_RUNTIME_SHA256,
        "dependency_set_manifest_sha256": TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256,
        "installed_environment_manifest_sha256": TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
        "transformers_module_sha256": TRANSFORMERS_MODULE_SHA256,
        "torch_module_sha256": TORCH_MODULE_SHA256,
        "architecture_config_module_sha256": facts["architecture_config_module_sha256"],
        "architecture_modeling_module_sha256": facts["architecture_modeling_module_sha256"],
        "loader_policy": LOADER_POLICY,
        "scoring_contract": SCORING_CONTRACT,
        "resource_generation_contract": RESOURCE_GENERATION_CONTRACT,
        "execution_performed": False,
        "runtime_format_compatibility_state": "NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE",
        "authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if manifest.get(field) != value:
            errors.append(f"{prefix}: {field} mismatch")
    for field in (
        "model_artifact_sha256",
        "complete_bundle_sha256",
        "tokenizer_config_sha256",
        "python_runtime_sha256",
        "dependency_set_manifest_sha256",
        "installed_environment_manifest_sha256",
        "transformers_module_sha256",
        "torch_module_sha256",
        "architecture_config_module_sha256",
        "architecture_modeling_module_sha256",
    ):
        if not is_canonical_sha256(manifest.get(field)):
            errors.append(f"{prefix}: {field} must be canonical sha256")
    if not is_canonical_sha256(manifest.get("adapter_sha256")):
        errors.append(f"{prefix}: adapter_sha256 must be canonical")
    elif manifest.get("adapter_sha256") != compute_e004_transformers_adapter_sha256(manifest):
        errors.append(f"{prefix}: adapter_sha256 mismatch")

    for field in (
        "candidate_role",
        "winner_eligible",
        "model_artifact_sha256",
        "model_artifact_bytes",
        "complete_bundle_sha256",
        "complete_bundle_bytes",
        "tokenizer_config_sha256",
    ):
        if manifest.get(field) != bundle.get(field):
            errors.append(f"{prefix}: {field} mismatch with candidate bundle")

    operations = manifest.get("operations")
    if not isinstance(operations, list) or len(operations) != 7:
        errors.append(f"{prefix}: exactly seven operations required")
        return sorted(set(errors))
    observed_assets = [item.get("asset_id") for item in operations if isinstance(item, dict)]
    if len(observed_assets) != 7 or set(observed_assets) != set(FROZEN_EVALUATION_ASSETS):
        errors.append(f"{prefix}: exact frozen asset coverage required")

    for index, operation in enumerate(operations):
        item_prefix = f"{prefix}.operations[{index}]"
        item_errors = validate_closed_object(
            operation, required_fields=_OPERATION_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(operation, dict):
            continue
        asset_id = str(operation.get("asset_id"))
        asset = by_id.get(asset_id)
        frozen = FROZEN_EVALUATION_ASSETS.get(asset_id)
        if asset is None or frozen is None:
            errors.append(f"{item_prefix}: asset outside frozen set")
            continue
        asset_sha, asset_kind, scoring_method = frozen
        expected_common = {
            "asset_sha256": asset_sha,
            "scoring_method": scoring_method,
            "input_identity": asset_sha,
        }
        for field, value in expected_common.items():
            if operation.get(field) != value:
                errors.append(f"{item_prefix}: {field} mismatch")

        invocations = operation.get("invocations")
        if asset_kind == MULTIPLE_CHOICE_ASSET_KIND:
            expected_mc = {
                "operation_id": f"{asset_id}-MC-SCORE",
                "operation_kind": "MULTIPLE_CHOICE_SCORE",
                "expected_output_kind": "ASSET_ACCURACY_RECORD_V1",
            }
            for field, value in expected_mc.items():
                if operation.get(field) != value:
                    errors.append(f"{item_prefix}: {field} mismatch")
            if not isinstance(invocations, list) or len(invocations) != 1:
                errors.append(f"{item_prefix}: exactly one scoring invocation required")
                continue
            invocation = invocations[0]
            inv_errors = validate_closed_object(
                invocation, required_fields=_INVOCATION_FIELDS, field=f"{item_prefix}.invocations[0]"
            )
            errors.extend(inv_errors)
            if inv_errors or not isinstance(invocation, dict):
                continue
            expected_invocation = {
                "invocation_id": f"{asset_id}-MC-SCORE-01",
                "probe_id": None,
                "run_class": "SCORING",
                "run_index": 1,
                "input_text_sha256": asset_sha,
                "max_new_tokens": 0,
            }
            for field, value in expected_invocation.items():
                if invocation.get(field) != value:
                    errors.append(f"{item_prefix}: scoring invocation {field} mismatch")
        elif asset_kind == RESOURCE_ASSET_KIND:
            expected_resource = {
                "operation_id": f"{asset_id}-RESOURCE",
                "operation_kind": "RESOURCE_MEASUREMENT",
                "expected_output_kind": "RESOURCE_MEASUREMENT_RECORD_V1",
            }
            for field, value in expected_resource.items():
                if operation.get(field) != value:
                    errors.append(f"{item_prefix}: {field} mismatch")
            if not isinstance(invocations, list) or len(invocations) != 32:
                errors.append(f"{item_prefix}: exactly 32 resource invocations required")
                continue
            probes = asset.get("probes")
            probe_map = {
                str(probe.get("probe_id")): probe
                for probe in probes
                if isinstance(probes, list) and isinstance(probe, dict)
            }
            observed: set[tuple[str, str, int, str]] = set()
            for inv_index, invocation in enumerate(invocations):
                inv_prefix = f"{item_prefix}.invocations[{inv_index}]"
                inv_errors = validate_closed_object(
                    invocation, required_fields=_INVOCATION_FIELDS, field=inv_prefix
                )
                errors.extend(inv_errors)
                if inv_errors or not isinstance(invocation, dict):
                    continue
                probe_id = str(invocation.get("probe_id"))
                probe = probe_map.get(probe_id)
                if probe is None:
                    errors.append(f"{inv_prefix}: frozen probe_id required")
                    continue
                run_class = str(invocation.get("run_class"))
                run_index = invocation.get("run_index")
                invocation_id = str(invocation.get("invocation_id"))
                if not isinstance(run_index, int) or isinstance(run_index, bool):
                    errors.append(f"{inv_prefix}: run_index must be integer")
                    continue
                observed.add((probe_id, run_class, run_index, invocation_id))
                expected_text_sha = hashlib.sha256(
                    str(probe.get("input_text")).encode("utf-8")
                ).hexdigest()
                if invocation.get("input_text_sha256") != expected_text_sha:
                    errors.append(f"{inv_prefix}: input_text_sha256 mismatch")
                if invocation.get("max_new_tokens") != 8:
                    errors.append(f"{inv_prefix}: max_new_tokens mismatch")
            if observed != _expected_resource_invocations(asset_id):
                errors.append(f"{item_prefix}: exact warmup/measured invocation set required")
    return sorted(set(errors))
