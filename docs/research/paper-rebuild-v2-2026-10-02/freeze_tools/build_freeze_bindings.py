#!/usr/bin/env python3
"""Build the prospective CommandMed V5 scientific-freeze binding manifest."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PACKET = Path(__file__).resolve().parents[1]
OUT = PACKET / "scientific-freeze-bindings-v5.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def bind(path: str) -> dict[str, str]:
    target = ROOT / path
    return {"path": path.replace("\\", "/"), "sha256": sha256_file(target)}

IMPLEMENTATIONS = {
    "A1_TS_V1": "src/commandmed/reliability_v5/probability.py",
    "A2_SELBIAS_V1": "src/commandmed/reliability_v5/selection_bias.py",
    "D1_DEFER_V1": "src/commandmed/reliability_v5/policy.py",
    "D2_RULETOOL_V1": "src/commandmed/reliability_v5/rule_tool.py",
}

OBJECTIVE_MECHANICS = {
    "B1_TYPED_V1": "DECISION_INTERFACE",
    "C1_CRDI_V1": "MODEL_ADAPTATION",
    "C2_CRDI_RETAIN_V1": "MODEL_ADAPTATION",
}

MODELS = {
    "development": {
        "repo": "Qwen/Qwen3.5-0.8B-Base",
        "revision": "dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68",
    },
    "independent_replication": {
        "repo": "HuggingFaceTB/SmolLM2-1.7B",
        "revision": "effd688a12921b4cc83e3312b6feb579f70f9c71",
    },
}


def main() -> int:
    status = git("status", "--porcelain")
    payload = {
        "schema": "commandmed-v5-scientific-freeze-bindings",
        "schema_version": "1.4",
        "confirmatory_frozen": False,
        "execution_authority": "NO",
        "model_execution": "NO",
        "training": "NO",
        "paid_compute": "NO",
    }
    # This manifest records preparation evidence; it never grants run authority.
    payload["development_authority"] = {
        "state": "APPROVED_SUBJECT_TO_EXACT_RUN_PREFLIGHT",
        "request": bind("docs/research/paper-rebuild-v2-2026-10-02/V5_DEVELOPMENT_EXECUTION_AUTHORITY_REQUEST.md"),
        "authorization": bind("docs/research/paper-rebuild-v2-2026-10-02/V5_DEVELOPMENT_EXECUTION_AUTHORIZATION_2026-10-03.md"),
        "s1_protocol": bind("docs/research/paper-rebuild-v2-2026-10-02/V5_S1_DEVELOPMENT_EXECUTION_PROTOCOL_2026-10-03.md"),
        "oracle_amendment": bind("docs/research/paper-rebuild-v2-2026-10-02/V5_S1_RULE_ORACLE_EXECUTION_COVERAGE_AMENDMENT_2026-10-03.md"),
        "answer_interface_authorization": bind("docs/research/paper-rebuild-v2-2026-10-02/V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md"),
    }
    payload["repository_context"] = {
        "branch": git("branch", "--show-current"),
        "generated_from_head": git("rev-parse", "HEAD"),
        "worktree_dirty_at_build": bool(status),
        "binding_semantics": "INFORMATIONAL_GENERATION_CONTEXT_NOT_FINAL_COMMIT_ATTESTATION",
    }
    payload["models"] = MODELS
    payload["retention_control"] = {
        "dataset": "rajpurkar/squad",
        "revision": "7b6d24c440a36b6815f21b70d25016731768db1f",
        "split": "validation",
        "license": "cc-by-sa-4.0",
        "claim_scope": "paired extractive-QA retention only",
        "dataset_inventory": bind("docs/research/paper-rebuild-v2-2026-10-02/dataset-inventory.json"),
        "admission": bind("docs/research/paper-rebuild-v2-2026-10-02/RETENTION_TASK_ADMISSION_V5.md"),
    }
    rule_manifest = json.loads(
        (PACKET / "riskcalcs-rule-oracle-final-candidate-v5.json").read_text(encoding="utf-8")
    )
    quarantine_commitments = json.loads(
        (PACKET / "quarantine-commitments-v5.json").read_text(encoding="utf-8")
    )
    selected_spaces = [int(row["prospective_case_space"]) for row in rule_manifest["selected"]]
    payload["rule_oracle"] = {
        "manifest": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/"
            "riskcalcs-rule-oracle-final-candidate-v5.json"
        ),
        "case_identities": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/rule-oracle-case-index-v5.json"
        ),
        "quarantine_commitments": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/quarantine-commitments-v5.json"
        ),
        "case_generator": bind("src/commandmed/reliability_v5/case_generator.py"),
        "quarantine_mechanics": bind("src/commandmed/reliability_v5/quarantine.py"),
        "clinical_source_audit": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/clinical-source-audit-v5.json"
        ),
        "clinical_source_review": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/clinical-source-review-v5.md"
        ),
        "static_eligible_count": int(rule_manifest["static_eligible_count"]),
        "execution_qualified_count": int(rule_manifest["execution_qualified_count"]),
        "execution_rejected_count": int(rule_manifest["execution_rejected_count"]),
        "execution_rejection_digest_sha256": rule_manifest["execution_rejection_digest_sha256"],
        "execution_gate": bind("src/commandmed/reliability_v5/oracle_qualification.py"),
        "bound_rule_runtime": bind("src/commandmed/reliability_v5/rule_dataset.py"),
        "eligible_selection_stratum_count": int(rule_manifest["eligible_selection_stratum_count"]),
        "calculator_count": int(rule_manifest["selected_count"]),
        "minimum_candidate_state_space": int(quarantine_commitments["minimum_candidate_state_space"]),
        "selected_candidate_state_space_min": min(selected_spaces),
        "selected_candidate_state_space_total": sum(selected_spaces),
        "development_cases_per_calculator": 64,
        "calibration_cases_per_calculator": 64,
        "planned_confirmatory_cases_per_calculator": 64,
        "planned_reserve_cases_per_calculator": 64,
        "prefreeze_committed_cluster_count": 8192,
        "planned_confirmatory_cluster_count": 4096,
        "confirmatory_assignment_materialized": False,
        "reserve_assignment_materialized": False,
    }
    payload["implementations"] = {
        intervention_id: {**bind(path), "status": "MECHANICAL_IMPLEMENTED"}
        for intervention_id, path in IMPLEMENTATIONS.items()
    }
    payload["objective_mechanics"] = {
        intervention_id: {
            **bind("src/commandmed/reliability_v5/objectives.py"),
            "locus": locus,
            "status": "OBJECTIVE_MECHANICS_IMPLEMENTED",
            "execution_authority": "NO",
        }
        for intervention_id, locus in OBJECTIVE_MECHANICS.items()
    }
    payload["shared_mechanics"] = {
        "contracts": bind("src/commandmed/reliability_v5/contracts.py"),
        "registry": bind("src/commandmed/reliability_v5/registry.py"),
        "quarantine": bind("src/commandmed/reliability_v5/quarantine.py"),
    }
    payload["protocols"] = {
        "evaluation": bind("docs/research/paper-rebuild-v2-2026-10-02/evaluation-protocol-v5.md"),
        "statistics": bind("docs/research/paper-rebuild-v2-2026-10-02/statistics-protocol-v5.md"),
        "preregistration": bind("docs/research/paper-rebuild-v2-2026-10-02/preregistration-v5.md"),
        "power_margin_gate": bind("docs/research/paper-rebuild-v2-2026-10-02/POWER_AND_MARGIN_GATE_V5.md"),
        "rights_source_admission": bind("docs/research/paper-rebuild-v2-2026-10-02/RIGHTS_AND_SOURCE_ADMISSION_V5.md"),
        "confirmatory_quarantine": bind("docs/research/paper-rebuild-v2-2026-10-02/CONFIRMATORY_QUARANTINE_V5.md"),
        "retention_task_admission": bind("docs/research/paper-rebuild-v2-2026-10-02/RETENTION_TASK_ADMISSION_V5.md"),
    }
    payload["remaining_blockers"] = [
        "B1/C1/C2 model-integration and learned-execution qualification",
        "property-specific meaningful numeric margins",
        "power verification at frozen margins",
        "future confirmatory state selection after clean freeze event and future beacon pulse",
        "post-commit attestation binding the reviewed freeze commit",
    ]
    preparation_path = "artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json"
    if (ROOT / preparation_path).is_file():
        preparation = json.loads((ROOT / preparation_path).read_text(encoding="utf-8"))
        payload["s1_task_preparation"] = {
            **bind(preparation_path),
            "status": preparation["status"],
            "implementation": bind("docs/research/paper-rebuild-v2-2026-10-02/execution_tools/prepare_s1_tasks.py"),
            "renderer": bind("src/commandmed/reliability_v5/rule_dataset.py"),
            "resource_runner": bind("scripts/v5_s1_resource_qualification.py"),
            "smoke_runner": bind("docs/research/paper-rebuild-v2-2026-10-02/execution_tools/run_s1_smoke.py"),
            "answer_prefix": preparation["answer_prefix"],
            "prompt_content_sequence_sha256": preparation["prompt_content_sequence_sha256"],
            "prior_negative_interface_evidence": bind("artifacts/v5/development/s1_task_preparation/frozen-space-prefix-failure-2026-10-03.json"),
        }
        if preparation["status"] != "PASS_PRE_MODEL_INTERFACE":
            payload["remaining_blockers"].insert(0, "S1 task-preparation interface qualification failed before model load")
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"OUT={OUT}")
    print(f"OUT_SHA256={sha256_file(OUT)}")
    print(f"WORKTREE_DIRTY_AT_BUILD={payload['repository_context']['worktree_dirty_at_build']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
