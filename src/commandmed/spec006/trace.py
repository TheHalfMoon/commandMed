"""Spec 006 InteractionTrace hash chains, seals, manifests, trusted-tree sets.

Implements the frozen ``contracts/{interaction-trace,trace-seal,
fixture-manifest}.schema.json`` semantics:

- strict ``interaction_id`` identity across manifest, seal, and every trace;
- contiguous monotonic ``trace_sequence`` starting at 0 with unique keys;
- ``GENESIS`` predecessor rule and hash chaining
  (``predecessor_sha256 == sha256(canonical_json(predecessor))``);
- ``state_before`` continuity (0 => null; >0 => predecessor.state_after);
- closed nested objects (undeclared fields rejected everywhere);
- determinism proof equalities enforced by the semantic validator;
- TraceSeal terminal anchor (expected_final_sequence + terminal_record_sha256);
- FixtureManifest projection identity (``manifest_identity_sha256``);
- trusted-tree verification where the trusted git commit OID is an
  OUT-OF-BAND verifier input. The OID is never stored inside the manifest it
  authenticates; verification resolves commit -> tree and reads manifest,
  seal, and trace bytes exclusively from that trusted tree at manifest-bound
  paths confined to ``specs/006-patient-safety-scaffold/fixtures/``.

All mismatches fail closed as ``INSUFFICIENT_EVIDENCE``.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec006.policy import BEHAVIORAL_STATES

ROLES = frozenset({"PATIENT_CAREGIVER", "CLINICAL_PROFESSIONAL", "LEARNER_RESEARCHER"})
LANGUAGES = frozenset({"ar", "en", "ar-en"})
TOOL_AVAILABILITY = frozenset({"AVAILABLE", "UNAVAILABLE", "TIMEOUT"})

UUID_PATTERN = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
SHA256_HEX = re.compile(r"^[0-9a-f]{64}$")

GENESIS = "GENESIS"
FIXTURE_ROOT_PREFIX = "specs/006-patient-safety-scaffold/fixtures/"
SEAL_PATH_PATTERN = re.compile(
    r"^specs/006-patient-safety-scaffold/fixtures/[^/]+/trace_seal\.json$"
)
TRACE_SET_PATH_PATTERN = re.compile(
    r"^specs/006-patient-safety-scaffold/fixtures/[^/]+/traces\.json$"
)

TRACE_REQUIRED_FIELDS = (
    "interaction_id",
    "trace_version",
    "trace_sequence",
    "predecessor_sha256",
    "input_identity_sha256",
    "context_identity_sha256",
    "policy_identity_sha256",
    "tool_registry_identity_sha256",
    "state_before",
    "state_after",
    "trigger_record_ids",
    "tool_call_record_ids",
    "output_identity_sha256",
    "failure_reason_codes",
    "safety_context",
    "tool_calls",
    "determinism_proof",
)


def _is_sha256(value: Any) -> bool:
    return isinstance(value, str) and SHA256_HEX.match(value) is not None


def _is_uuid(value: Any) -> bool:
    return isinstance(value, str) and UUID_PATTERN.match(value) is not None


def _string_list(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        errors.append(f"{field}: expected array of strings")


def _validate_safety_context(context: Any, errors: list[str], field: str = "safety_context") -> None:
    if not isinstance(context, dict):
        errors.append(f"{field}: expected object")
        return
    required = {"role", "language", "available_evidence_ids", "tool_availability"}
    missing = required - set(context)
    if missing:
        errors.append(f"{field}: required fields missing {sorted(missing)}")
    undeclared = set(context) - (required | {"locale_hint", "jurisdiction"})
    if undeclared:
        errors.append(f"{field}: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return
    if context["role"] not in ROLES:
        errors.append(f"{field}.role: unsupported value '{context['role']}'")
    if context["language"] not in LANGUAGES:
        errors.append(f"{field}.language: unsupported value '{context['language']}'")
    if not isinstance(context["available_evidence_ids"], list) or not all(
        isinstance(item, str) for item in context["available_evidence_ids"]
    ):
        errors.append(f"{field}.available_evidence_ids: expected array of strings")
    availability = context["tool_availability"]
    if not isinstance(availability, dict):
        errors.append(f"{field}.tool_availability: expected object")
    else:
        for tool_id, state in availability.items():
            if state not in TOOL_AVAILABILITY:
                errors.append(f"{field}.tool_availability.{tool_id}: unsupported '{state}'")
            if not isinstance(tool_id, str) or not tool_id:
                errors.append(f"{field}.tool_availability: invalid tool key")
    for optional in ("locale_hint", "jurisdiction"):
        if optional in context and context[optional] is not None and not isinstance(
            context[optional], str
        ):
            errors.append(f"{field}.{optional}: expected string or null")


def _validate_tool_call(call: Any, errors: list[str], field: str) -> None:
    if not isinstance(call, dict):
        errors.append(f"{field}: expected object")
        return
    required = {
        "tool_call_id",
        "tool_id",
        "tool_version",
        "input_identity_sha256",
        "output_identity_sha256",
        "provenance",
        "failure",
    }
    missing = required - set(call)
    if missing:
        errors.append(f"{field}: required fields missing {sorted(missing)}")
    undeclared = set(call) - required
    if undeclared:
        errors.append(f"{field}: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return
    for text_key in ("tool_call_id", "tool_id", "tool_version"):
        if not isinstance(call[text_key], str) or not call[text_key].strip():
            errors.append(f"{field}.{text_key}: expected non-empty string")
    if not _is_sha256(call["input_identity_sha256"]):
        errors.append(f"{field}.input_identity_sha256: expected lowercase sha256 hex")
    if not _is_sha256(call["output_identity_sha256"]):
        errors.append(f"{field}.output_identity_sha256: expected lowercase sha256 hex")

    provenance = call["provenance"]
    if not isinstance(provenance, dict):
        errors.append(f"{field}.provenance: expected object")
    else:
        p_required = {"tool_content_identity", "source_authority", "result_sha256"}
        p_missing = p_required - set(provenance)
        if p_missing:
            errors.append(f"{field}.provenance: required fields missing {sorted(p_missing)}")
        elif set(provenance) - p_required:
            errors.append(f"{field}.provenance: undeclared fields {sorted(set(provenance) - p_required)}")
        else:
            if not _is_sha256(provenance["tool_content_identity"]):
                errors.append(f"{field}.provenance.tool_content_identity: expected sha256 hex")
            if not isinstance(provenance["source_authority"], str) or not provenance[
                "source_authority"
            ].strip():
                errors.append(f"{field}.provenance.source_authority: expected non-empty string")
            if not _is_sha256(provenance["result_sha256"]):
                errors.append(f"{field}.provenance.result_sha256: expected sha256 hex")

    failure = call["failure"]
    if not isinstance(failure, dict):
        errors.append(f"{field}.failure: expected object")
    else:
        f_required = {"is_failure", "reason_code"}
        f_missing = f_required - set(failure)
        if f_missing:
            errors.append(f"{field}.failure: required fields missing {sorted(f_missing)}")
        elif set(failure) - f_required:
            errors.append(f"{field}.failure: undeclared fields {sorted(set(failure) - f_required)}")
        else:
            if not isinstance(failure["is_failure"], bool):
                errors.append(f"{field}.failure.is_failure: expected boolean")
            reason = failure["reason_code"]
            if reason is not None and (not isinstance(reason, str) or not reason.strip()):
                errors.append(f"{field}.failure.reason_code: expected non-empty string or null")


def _validate_determinism_proof(proof: Any, trace: Any, errors: list[str], field: str) -> None:
    if not isinstance(proof, dict):
        errors.append(f"{field}: expected object")
        return
    required = {
        "replayed",
        "replay_input_sha256",
        "replay_context_identity_sha256",
        "replay_policy_identity_sha256",
        "replay_tool_registry_identity_sha256",
        "replay_output_state",
    }
    missing = required - set(proof)
    if missing:
        errors.append(f"{field}: required fields missing {sorted(missing)}")
    undeclared = set(proof) - required
    if undeclared:
        errors.append(f"{field}: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return
    # JSON Schema enforces const true; the semantic validator rejects false too.
    if proof["replayed"] is not True:
        errors.append(f"{field}.replayed: must be true")
    equalities = (
        ("replay_input_sha256", "input_identity_sha256"),
        ("replay_context_identity_sha256", "context_identity_sha256"),
        ("replay_policy_identity_sha256", "policy_identity_sha256"),
        ("replay_tool_registry_identity_sha256", "tool_registry_identity_sha256"),
    )
    for replay_key, identity_key in equalities:
        if not _is_sha256(proof[replay_key]):
            errors.append(f"{field}.{replay_key}: expected lowercase sha256 hex")
        elif proof[replay_key] != trace[identity_key]:
            errors.append(f"{field}.{replay_key}: must equal {identity_key}")
    if proof["replay_output_state"] not in BEHAVIORAL_STATES:
        errors.append(f"{field}.replay_output_state: unsupported behavioral state")
    elif proof["replay_output_state"] != trace["state_after"]:
        errors.append(f"{field}.replay_output_state: must equal state_after")


def validate_trace(record: Any) -> list[str]:
    """Validate one InteractionTrace record against the frozen contract."""
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["trace: expected an object record"]

    missing = [key for key in TRACE_REQUIRED_FIELDS if key not in record]
    if missing:
        errors.append(f"trace: required fields missing {missing}")
    undeclared = set(record) - set(TRACE_REQUIRED_FIELDS)
    if undeclared:
        errors.append(f"trace: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return errors

    if not _is_uuid(record["interaction_id"]):
        errors.append("trace.interaction_id: expected UUID format")
    if not isinstance(record["trace_version"], str) or not record["trace_version"].strip():
        errors.append("trace.trace_version: expected non-empty string")

    sequence = record["trace_sequence"]
    if not isinstance(sequence, int) or isinstance(sequence, bool) or sequence < 0:
        errors.append("trace.trace_sequence: expected integer >= 0")

    # Genesis contract (data-model §1.4): trace_sequence 0 has no prior state.
    if sequence == 0 and not isinstance(sequence, bool):
        if record["state_before"] is not None:
            errors.append("trace.state_before: genesis record must use null")
    elif sequence > 0 and record["state_before"] is None:
        errors.append("trace.state_before: non-genesis record requires a prior state")

    predecessor = record["predecessor_sha256"]
    if sequence == 0 and not isinstance(sequence, bool):
        if predecessor != GENESIS:
            errors.append("trace.predecessor_sha256: genesis record must use 'GENESIS'")
    else:
        if not _is_sha256(predecessor):
            errors.append("trace.predecessor_sha256: expected lowercase sha256 hex")

    for hash_key in (
        "input_identity_sha256",
        "context_identity_sha256",
        "policy_identity_sha256",
        "tool_registry_identity_sha256",
        "output_identity_sha256",
    ):
        if not _is_sha256(record[hash_key]):
            errors.append(f"trace.{hash_key}: expected lowercase sha256 hex")

    if record["state_before"] is not None and record["state_before"] not in BEHAVIORAL_STATES:
        errors.append("trace.state_before: unsupported behavioral state")
    if record["state_after"] not in BEHAVIORAL_STATES:
        errors.append("trace.state_after: unsupported behavioral state")

    _string_list(record["trigger_record_ids"], "trace.trigger_record_ids", errors)
    _string_list(record["tool_call_record_ids"], "trace.tool_call_record_ids", errors)
    _string_list(record["failure_reason_codes"], "trace.failure_reason_codes", errors)

    _validate_safety_context(record["safety_context"], errors)

    tool_calls = record["tool_calls"]
    if not isinstance(tool_calls, list):
        errors.append("trace.tool_calls: expected array")
    else:
        for index, call in enumerate(tool_calls):
            _validate_tool_call(call, errors, f"trace.tool_calls[{index}]")

    _validate_determinism_proof(record["determinism_proof"], record, errors, "trace.determinism_proof")

    return errors


def record_hash(trace: Any) -> str:
    """Canonical SHA-256 over one InteractionTrace record."""
    return compute_canonical_sha256(trace)


def append_trace(previous: dict[str, Any] | None, partial: dict[str, Any]) -> dict[str, Any]:
    """Build the next chained trace record.

    Computes ``trace_sequence`` from the previous record (genesis when absent)
    and binds ``predecessor_sha256`` to ``GENESIS`` or the previous record's
    canonical hash. Append-only: callers add new records, never mutate prior ones.
    """
    if previous is None:
        sequence = 0
        predecessor = GENESIS
    else:
        sequence = int(previous["trace_sequence"]) + 1
        predecessor = record_hash(previous)
    record = dict(partial)
    record["trace_sequence"] = sequence
    record["predecessor_sha256"] = predecessor
    return record


def validate_seal(seal: Any) -> list[str]:
    """Validate one TraceSeal terminal completeness anchor."""
    errors: list[str] = []
    if not isinstance(seal, dict):
        return ["seal: expected an object record"]
    required = {"interaction_id", "seal_version", "expected_final_sequence", "terminal_record_sha256"}
    missing = required - set(seal)
    if missing:
        errors.append(f"seal: required fields missing {sorted(missing)}")
    undeclared = set(seal) - required
    if undeclared:
        errors.append(f"seal: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return errors
    if not _is_uuid(seal["interaction_id"]):
        errors.append("seal.interaction_id: expected UUID format")
    if not isinstance(seal["seal_version"], str) or not seal["seal_version"].strip():
        errors.append("seal.seal_version: expected non-empty string")
    final_sequence = seal["expected_final_sequence"]
    if not isinstance(final_sequence, int) or isinstance(final_sequence, bool) or final_sequence < 0:
        errors.append("seal.expected_final_sequence: expected integer >= 0")
    if not _is_sha256(seal["terminal_record_sha256"]):
        errors.append("seal.terminal_record_sha256: expected lowercase sha256 hex")
    return errors


def validate_trace_set(traces: Any, seal: Any, interaction_id: Any) -> list[str]:
    """Semantic validation of a sealed ordered trace set.

    Enforces cross-artifact interaction equality, contiguity 0..final,
    unique sequence keys, predecessor chain, state continuity, and the
    terminal seal hash.
    """
    errors: list[str] = []
    errors.extend(validate_seal(seal))
    if not _is_uuid(interaction_id):
        errors.append("requested interaction_id: expected UUID format")
    if not isinstance(traces, list) or not traces:
        return errors + ["trace_set: expected non-empty ordered array"]

    seen_sequences: set[int] = set()
    previous: dict[str, Any] | None = None
    for index, trace in enumerate(traces):
        field = f"trace_set[{index}]"
        trace_errors = validate_trace(trace)
        errors.extend(trace_errors)
        if trace_errors or not isinstance(trace, dict):
            previous = None
            continue
        if trace["interaction_id"] != interaction_id:
            errors.append(
                f"{field}.interaction_id: mismatch against requested interaction_id"
            )
        sequence = trace["trace_sequence"]
        if sequence in seen_sequences:
            errors.append(f"{field}.trace_sequence: duplicate sequence {sequence}")
        seen_sequences.add(sequence)
        if previous is not None:
            if sequence != previous["trace_sequence"] + 1:
                errors.append(
                    f"{field}.trace_sequence: gap detected (expected"
                    f" {previous['trace_sequence'] + 1}, got {sequence})"
                )
            if trace["predecessor_sha256"] != record_hash(previous):
                errors.append(f"{field}.predecessor_sha256: chain mismatch")
            if trace["state_before"] != previous["state_after"]:
                errors.append(f"{field}.state_before: continuity violation")
        elif sequence != 0:
            errors.append(f"{field}: first record must be genesis (trace_sequence 0)")
        previous = trace

    if seal is not None and isinstance(seal, dict):
        if seal.get("interaction_id") != interaction_id:
            errors.append("seal.interaction_id: mismatch against requested interaction_id")
        final_expected = seal.get("expected_final_sequence")
        if previous is not None and isinstance(final_expected, int):
            if previous["trace_sequence"] != final_expected:
                errors.append(
                    "seal.expected_final_sequence: terminal sequence mismatch"
                    f" (sealed {final_expected}, got {previous['trace_sequence']})"
                )
            if seal.get("terminal_record_sha256") == record_hash(previous):
                pass
            elif _is_sha256(seal.get("terminal_record_sha256")):
                errors.append("seal.terminal_record_sha256: terminal record hash mismatch")
    return errors


def validate_manifest(manifest: Any) -> list[str]:
    """Validate a FixtureManifest bundle.

    Checks structure, entry shape, path confinement patterns, unique
    interaction ids, unique manifest-bound paths, duplicate-entry rejection,
    and recomputation of the ``manifest_identity_sha256`` projection.
    """
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["manifest: expected object bundle"]
    required = {"manifest_version", "manifest_identity_sha256", "entries"}
    missing = required - set(manifest)
    if missing:
        errors.append(f"manifest: required fields missing {sorted(missing)}")
    undeclared = set(manifest) - required
    if undeclared:
        errors.append(f"manifest: undeclared fields {sorted(undeclared)}")
    if missing or undeclared:
        return errors

    if not isinstance(manifest["manifest_version"], str) or not manifest["manifest_version"].strip():
        errors.append("manifest.manifest_version: expected non-empty string")
    if not _is_sha256(manifest["manifest_identity_sha256"]):
        errors.append("manifest.manifest_identity_sha256: expected lowercase sha256 hex")
    else:
        projection = {
            "manifest_version": manifest["manifest_version"],
            "entries": manifest["entries"],
        }
        expected = compute_canonical_sha256(projection)
        if manifest["manifest_identity_sha256"] != expected:
            errors.append(
                f"manifest.manifest_identity_sha256: mismatch against projection (expected {expected})"
            )

    entries = manifest["entries"]
    if not isinstance(entries, list) or len(entries) < 1:
        return errors + ["manifest.entries: expected array with minItems 1"]

    seen_interaction: set[str] = set()
    seen_paths: set[str] = set()
    entry_required = {
        "interaction_id",
        "seal_path",
        "trace_set_path",
        "seal_canonical_sha256",
        "expected_final_sequence",
        "terminal_record_sha256",
    }
    for index, entry in enumerate(entries):
        field = f"manifest.entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{field}: expected object")
            continue
        missing = entry_required - set(entry)
        if missing:
            errors.append(f"{field}: required fields missing {sorted(missing)}")
        undeclared = set(entry) - entry_required
        if undeclared:
            errors.append(f"{field}: undeclared fields {sorted(undeclared)}")
        if missing or undeclared:
            continue
        if not _is_uuid(entry["interaction_id"]):
            errors.append(f"{field}.interaction_id: expected UUID format")
        if entry["interaction_id"] in seen_interaction:
            errors.append(
                f"{field}.interaction_id: duplicate interaction_id '{entry['interaction_id']}'"
            )
        seen_interaction.add(entry["interaction_id"])

        for path_key in ("seal_path", "trace_set_path"):
            path_value = entry[path_key]
            if not isinstance(path_value, str):
                errors.append(f"{field}.{path_key}: expected string path")
                continue
            if ".." in Path(path_value).parts or not path_value.startswith(FIXTURE_ROOT_PREFIX):
                errors.append(f"{field}.{path_key}: path escapes fixture root or traverses upward")
            if path_key == "seal_path" and SEAL_PATH_PATTERN.match(path_value) is None:
                errors.append(f"{field}.seal_path: does not match canonical seal path pattern")
            if path_key == "trace_set_path" and TRACE_SET_PATH_PATTERN.match(path_value) is None:
                errors.append(f"{field}.trace_set_path: does not match canonical traces path pattern")
            if path_value in seen_paths:
                errors.append(f"{field}.{path_key}: duplicate manifest-bound path")
            seen_paths.add(path_value)

        if not _is_sha256(entry["seal_canonical_sha256"]):
            errors.append(f"{field}.seal_canonical_sha256: expected lowercase sha256 hex")
        if not _is_sha256(entry["terminal_record_sha256"]):
            errors.append(f"{field}.terminal_record_sha256: expected lowercase sha256 hex")
        final_sequence = entry["expected_final_sequence"]
        if not isinstance(final_sequence, int) or isinstance(final_sequence, bool) or final_sequence < 0:
            errors.append(f"{field}.expected_final_sequence: expected integer >= 0")

    return errors


class TrustedTreeReader:
    """Read blobs exclusively from one resolved git tree via local git plumbing.

    Standard-library only (subprocess to the git binary). No network access.
    Blob reads are strictly binary: bytes returned from ``read_blob`` are the
    exact object-store contents, so byte-identity checks in
    ``validate_trace_set_trusted`` compare true object bytes.
    """

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self._env_workdir = str(repo_root)

    def _run(self, args: list[str]) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", *args],
            cwd=self._env_workdir,
            capture_output=True,
            check=False,
        )

    def resolve_object_type(self, oid: str) -> str | None:
        result = self._run(["cat-file", "-t", oid])
        if result.returncode != 0:
            return None
        return result.stdout.decode("utf-8", errors="replace").strip()

    def resolve_tree(self, commit_oid: str) -> str | None:
        result = self._run(["rev-parse", "--verify", "--quiet", f"{commit_oid}^{{tree}}"])
        if result.returncode != 0 or result.stdout.strip() == b"":
            return None
        return result.stdout.decode("utf-8").strip()

    def read_blob(self, tree_oid: str, path: str) -> bytes | None:
        result = self._run(["cat-file", "blob", f"{tree_oid}:{path}"])
        if result.returncode != 0:
            return None
        return result.stdout


def validate_trace_set_trusted(
    trusted_commit_oid: Any,
    interaction_id: Any,
    caller_manifest_bytes: Any,
    repo_root: Path | None = None,
    reader: TrustedTreeReader | None = None,
) -> dict[str, Any]:
    """Full trusted-tree verification of a sealed trace fixture set.

    Procedure (all steps fail closed to INSUFFICIENT_EVIDENCE):

    1. trusted commit OID format (40-hex sha1 or 64-hex sha256);
    2. trusted commit resolves in the repository;
    3. trusted tree resolves from the commit;
    4. ``fixture-manifest.json`` bytes are read from that exact trusted tree
       and must be byte-identical to the caller-supplied manifest bytes;
    5. referenced TraceSeal is read from the trusted tree via the
       manifest-bound ``seal_path``;
    6. referenced ordered trace records are read from the trusted tree via
       the manifest-bound ``trace_set_path``;
    7. manifest identity projection validates;
    8. manifest entry interaction matches the requested interaction;
    9. TraceSeal interaction matches;
    10. every InteractionTrace interaction matches;
    11. sequence is contiguous from 0;
    12. sequence keys are unique;
    13. predecessor chain validates;
    14. state continuity validates;
    15. terminal sequence matches the seal;
    16. terminal record hash matches the seal;
    17. determinism proof identities match (via per-record validation);
    18. any mismatch fails closed.
    """
    reasons: list[str] = []

    def insufficient() -> dict[str, Any]:
        return {"status": "INSUFFICIENT_EVIDENCE", "reason_codes": reasons}

    if not isinstance(trusted_commit_oid, str) or re.fullmatch(
        r"(?:[0-9a-f]{40}|[0-9a-f]{64})", trusted_commit_oid
    ) is None:
        return insufficient() | {"reason_codes": ["UNTRUSTED_COMMIT_OID_FORMAT"]}

    root = repo_root if repo_root is not None else Path.cwd()
    reader = reader if reader is not None else TrustedTreeReader(root)

    if reader.resolve_object_type(trusted_commit_oid) != "commit":
        return insufficient() | {"reason_codes": ["UNTRUSTED_COMMIT_UNRESOLVED"]}
    tree_oid = reader.resolve_tree(trusted_commit_oid)
    if tree_oid is None:
        return insufficient() | {"reason_codes": ["UNTRUSTED_TREE_UNRESOLVED"]}

    if not isinstance(caller_manifest_bytes, bytes):
        return insufficient() | {"reason_codes": ["MANIFEST_BYTES_NOT_SUPPLIED"]}
    trusted_manifest_bytes = reader.read_blob(
        tree_oid, FIXTURE_ROOT_PREFIX + "fixture-manifest.json"
    )
    if trusted_manifest_bytes is None:
        return insufficient() | {"reason_codes": ["MANIFEST_MISSING_FROM_TRUSTED_TREE"]}
    if trusted_manifest_bytes != caller_manifest_bytes:
        return insufficient() | {"reason_codes": ["MANIFEST_MISMATCH_AGAINST_TRUSTED_TREE"]}

    try:
        import json

        manifest = json.loads(caller_manifest_bytes.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return insufficient() | {"reason_codes": ["MANIFEST_BYTES_NOT_JSON"]}
    manifest_errors = validate_manifest(manifest)
    if manifest_errors:
        return insufficient() | {"reason_codes": ["MANIFEST_INVALID", *manifest_errors[:3]]}

    entry = next(
        (
            candidate
            for candidate in manifest["entries"]
            if candidate.get("interaction_id") == interaction_id
        ),
        None,
    )
    if entry is None:
        return insufficient() | {"reason_codes": ["MANIFEST_ENTRY_MISSING_FOR_INTERACTION"]}

    seal_bytes = reader.read_blob(tree_oid, entry["seal_path"])
    if seal_bytes is None:
        return insufficient() | {"reason_codes": ["SEAL_MISSING_FROM_TRUSTED_TREE"]}
    try:
        seal = json.loads(seal_bytes.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return insufficient() | {"reason_codes": ["SEAL_BYTES_NOT_JSON"]}

    traces_bytes = reader.read_blob(tree_oid, entry["trace_set_path"])
    if traces_bytes is None:
        return insufficient() | {"reason_codes": ["TRACE_SET_MISSING_FROM_TRUSTED_TREE"]}
    try:
        traces = json.loads(traces_bytes.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return insufficient() | {"reason_codes": ["TRACE_SET_BYTES_NOT_JSON"]}

    from src.commandmed.eval_contract.canonical import compute_canonical_sha256 as _sha

    if _sha(seal) != entry["seal_canonical_sha256"]:
        reasons.append("MANIFEST_SEAL_HASH_MISMATCH")

    set_errors = validate_trace_set(traces, seal, interaction_id)
    if set_errors:
        reasons.append("TRACE_SET_INVALID")
        reasons.extend(set_errors[:5])

    if seal is not None and isinstance(seal, dict):
        if seal.get("expected_final_sequence") != entry.get("expected_final_sequence"):
            reasons.append("MANIFEST_FINAL_SEQUENCE_MISMATCH")
        if seal.get("terminal_record_sha256") != entry.get("terminal_record_sha256"):
            reasons.append("MANIFEST_TERMINAL_HASH_MISMATCH")

    if reasons:
        return {"status": "INSUFFICIENT_EVIDENCE", "reason_codes": reasons}
    return {"status": "VERIFIED", "reason_codes": []}
