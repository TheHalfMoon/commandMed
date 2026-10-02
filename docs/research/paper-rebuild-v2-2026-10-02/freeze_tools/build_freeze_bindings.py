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

CONTRACT_ONLY = {
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
        "schema_version": "1.0",
        "confirmatory_frozen": False,
        "execution_authority": "NO",
        "model_execution": "NO",
        "training": "NO",
        "paid_compute": "NO",
    }
    payload["repository"] = {
        "branch": git("branch", "--show-current"),
        "head": git("rev-parse", "HEAD"),
        "dirty": bool(status),
    }
    payload["models"] = MODELS
    payload["rule_oracle"] = {
        "manifest": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/"
            "riskcalcs-rule-oracle-final-candidate-v5.json"
        ),
        "case_identities": bind(
            "docs/research/paper-rebuild-v2-2026-10-02/rule-oracle-case-index-v5.json"
        ),
        "case_generator": bind("src/commandmed/reliability_v5/case_generator.py"),
        "calculator_count": 64,
        "cases_per_calculator": 64,
        "source_cluster_count": 4096,
    }
    payload["implementations"] = {
        intervention_id: {**bind(path), "status": "MECHANICAL_IMPLEMENTED"}
        for intervention_id, path in IMPLEMENTATIONS.items()
    }
    payload["contract_only"] = {
        intervention_id: {"locus": locus, "status": "CONTRACT_ONLY"}
        for intervention_id, locus in CONTRACT_ONLY.items()
    }
    payload["shared_mechanics"] = {
        "contracts": bind("src/commandmed/reliability_v5/contracts.py"),
        "registry": bind("src/commandmed/reliability_v5/registry.py"),
    }
    payload["protocols"] = {
        "evaluation": bind("docs/research/paper-rebuild-v2-2026-10-02/evaluation-protocol-v5.md"),
        "statistics": bind("docs/research/paper-rebuild-v2-2026-10-02/statistics-protocol-v5.md"),
        "preregistration": bind("docs/research/paper-rebuild-v2-2026-10-02/preregistration-v5.md"),
        "power_margin_gate": bind("docs/research/paper-rebuild-v2-2026-10-02/POWER_AND_MARGIN_GATE_V5.md"),
        "rights_source_admission": bind("docs/research/paper-rebuild-v2-2026-10-02/RIGHTS_AND_SOURCE_ADMISSION_V5.md"),
    }
    payload["remaining_blockers"] = [
        "B1_TYPED_V1 exact implementation and review",
        "C1_CRDI_V1 exact implementation and review",
        "C2_CRDI_RETAIN_V1 exact implementation and review",
        "property-specific meaningful numeric margins",
        "power verification at frozen margins",
        "final capability-retention task rights and identity",
        "final quarantine procedure and confirmatory source identity binding",
        "final clean commit binding after review",
    ]
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUT={OUT}")
    print(f"OUT_SHA256={sha256_file(OUT)}")
    print(f"DIRTY={payload['repository']['dirty']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
