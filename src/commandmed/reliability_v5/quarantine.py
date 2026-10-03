"""Publicly auditable quarantine mechanics for the V5 rule-oracle study.

Development and calibration state indices are fixed before model execution.
Confirmatory and reserve state indices are not selected until after an
implementation freeze and a future public-randomness pulse.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import string
from collections.abc import Mapping, Sequence

from .case_generator import deterministic_state_indices
from .contracts import ReliabilityContractError

DEVELOPMENT_COUNT = 64
CALIBRATION_COUNT = 64
CONFIRMATORY_COUNT = 64
RESERVE_COUNT = 64
MIN_FUTURE_CANDIDATE_SPACE = 1024
DEV_NAMESPACE = "CommandMed-V5-DEV-v2"
CAL_NAMESPACE = "CommandMed-V5-CAL-v2"
QUARANTINE_NAMESPACE = "CommandMed-V5-QUARANTINE-NIST-BEACON-2-v2"


def prefreeze_state_partition(calculator_id: str, total: int) -> dict[str, tuple[int, ...]]:
    """Select fixed development/calibration states while leaving the rest unselected."""
    if not isinstance(total, int) or isinstance(total, bool) or total < MIN_FUTURE_CANDIDATE_SPACE:
        raise ReliabilityContractError(
            f"total: expected at least {MIN_FUTURE_CANDIDATE_SPACE} candidate states"
        )
    development = deterministic_state_indices(
        calculator_id,
        total,
        count=DEVELOPMENT_COUNT,
        salt=DEV_NAMESPACE,
    )
    calibration = deterministic_state_indices(
        calculator_id,
        total,
        count=CALIBRATION_COUNT,
        salt=CAL_NAMESPACE,
        exclude_state_indices=development,
    )
    return {"development": development, "calibration": calibration}


def derive_partition_seed(*, freeze_commit: str, beacon_output_hex: str) -> bytes:
    """Derive a public final-test seed from the frozen commit and future beacon output."""
    if (
        not isinstance(freeze_commit, str)
        or len(freeze_commit) != 40
        or any(ch not in string.hexdigits for ch in freeze_commit)
    ):
        raise ReliabilityContractError("freeze_commit: expected a 40-character hexadecimal Git SHA-1")
    try:
        beacon_bytes = bytes.fromhex(beacon_output_hex)
    except (TypeError, ValueError) as exc:
        raise ReliabilityContractError("beacon_output_hex: expected hexadecimal text") from exc
    if len(beacon_bytes) != 64:
        raise ReliabilityContractError("beacon_output_hex: expected a 512-bit beacon value")
    payload = b"|".join(
        (
            QUARANTINE_NAMESPACE.encode("ascii"),
            freeze_commit.lower().encode("ascii"),
            beacon_bytes,
        )
    )
    return hashlib.sha256(payload).digest()


def confirmatory_reserve_state_partition(
    calculator_id: str,
    total: int,
    excluded_state_indices: Sequence[int],
    seed: bytes,
) -> dict[str, tuple[int, ...]]:
    """Select future confirmatory/reserve states from the still-unselected space."""
    if not isinstance(total, int) or isinstance(total, bool) or total < MIN_FUTURE_CANDIDATE_SPACE:
        raise ReliabilityContractError(
            f"total: expected at least {MIN_FUTURE_CANDIDATE_SPACE} candidate states"
        )
    raw_excluded = tuple(excluded_state_indices)
    if any(not isinstance(index, int) or isinstance(index, bool) for index in raw_excluded):
        raise ReliabilityContractError("excluded_state_indices: expected integers")
    if len(set(raw_excluded)) != len(raw_excluded):
        raise ReliabilityContractError("excluded_state_indices: duplicates are not allowed")
    excluded = set(raw_excluded)
    if any(index < 0 or index >= total for index in excluded):
        raise ReliabilityContractError("excluded_state_indices: index outside case space")
    if not isinstance(seed, bytes) or len(seed) < 32:
        raise ReliabilityContractError("seed: expected at least 256 bits")
    remaining = total - len(excluded)
    required = CONFIRMATORY_COUNT + RESERVE_COUNT
    if remaining < required:
        raise ReliabilityContractError("unselected case space is smaller than confirmatory+reserve demand")

    def rank_key(state_index: int) -> tuple[bytes, int]:
        message = f"{calculator_id}|{state_index}".encode("utf-8")
        return (hmac.new(seed, message, hashlib.sha256).digest(), state_index)

    ranked = sorted((index for index in range(total) if index not in excluded), key=rank_key)
    chosen = ranked[:required]
    return {
        "confirmatory": tuple(chosen[:CONFIRMATORY_COUNT]),
        "reserve": tuple(chosen[CONFIRMATORY_COUNT:]),
    }


def assignment_commitment(partition: Mapping[str, Sequence[object]]) -> str:
    """Return a canonical SHA-256 commitment for a named assignment."""
    normalized = {name: list(partition[name]) for name in sorted(partition)}
    payload = json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
