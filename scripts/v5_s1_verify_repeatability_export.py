"""Model-free verifier for private Kaggle unchanged-base repeatability exports."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import tempfile
import zipfile
from pathlib import Path

import v5_s1_b1_development as b1
import v5_s1_colab_qualification as existing

base = existing.base
RISKCALCS_SHA256 = "00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_members(archive: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    infos = archive.infolist()
    seen = set()
    for info in infos:
        name = info.filename
        member = Path(name)
        if (
            not name
            or member.is_absolute()
            or ".." in member.parts
            or "\\" in name
            or ":" in name
            or name in seen
        ):
            raise RuntimeError("UNSAFE_OR_DUPLICATE_ZIP_MEMBER")
        seen.add(name)
    bad = archive.testzip()
    if bad is not None:
        raise RuntimeError("ZIP_CRC_FAILURE:" + bad)
    return infos


def verify(args) -> dict:
    if _sha(args.source) != RISKCALCS_SHA256:
        raise RuntimeError("RISKCALCS_SOURCE_HASH_MISMATCH")
    runtime = json.loads(args.runtime.read_text(encoding="utf-8"))
    hardware = json.loads(args.hardware.read_text(encoding="utf-8"))
    required_runtime = {
        "status": "ATOMIC_KERNEL_FINISHED",
        "exit_code": 0,
        "expected_head": args.expected_head,
        "intervention": "BASELINE_V1",
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "repeat": args.repeat,
        "spend_usd": 0,
        "resume": False,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
        "exported_archive": True,
    }
    if any(runtime.get(key) != value for key, value in required_runtime.items()):
        raise RuntimeError("ALLOWLISTED_RUNTIME_MISMATCH")
    if (
        hardware.get("scientific_gpu_count") != 1
        or hardware.get("scientific_device") != "cuda:0"
        or not isinstance(hardware.get("visible_gpus"), list)
        or not hardware["visible_gpus"]
        or hardware["visible_gpus"][0].get("scientific_use") is not True
        or any(row.get("scientific_use") is True for row in hardware["visible_gpus"][1:])
    ):
        raise RuntimeError("PHYSICAL_HARDWARE_SCIENTIFIC_BINDING_MISMATCH")

    archive_sha = _sha(args.archive)
    with zipfile.ZipFile(args.archive) as zf:
        infos = _safe_members(zf)
        with tempfile.TemporaryDirectory(prefix="commandmed-repeatability-verify-") as temp:
            root = Path(temp)
            zf.extractall(root)
            required = {
                "repeatability-result.json",
                "repeatability-decision-matrix.json",
                "repeatability-analysis.json",
                "environment-manifest.json",
                "frozen-bindings.json",
                "hardware-manifest.json",
                "duration-admission.json",
            }
            names = {info.filename for info in infos if not info.is_dir()}
            if not required.issubset(names):
                raise RuntimeError("REPEATABILITY_REQUIRED_EVIDENCE_MISSING")

            result = json.loads((root / "repeatability-result.json").read_text(encoding="utf-8"))
            if (
                result.get("status") != "BASELINE_REPEAT_COMPLETE_DEVELOPMENT"
                or result.get("code_sha") != args.expected_head
                or result.get("intervention") != "BASELINE_V1"
                or result.get("purpose") != "UNCHANGED_BASE_REPEATABILITY"
                or result.get("repeat") != args.repeat
                or result.get("complete_matrix") is not True
                or result.get("prompt_count") != 16384
                or result.get("training") is not False
                or result.get("optimizer_steps") != 0
                or result.get("spend_usd") != 0
                or result.get("confirmatory_materialized") is not False
                or result.get("reserve_materialized") is not False
            ):
                raise RuntimeError("REPEATABILITY_RESULT_CONTRACT_MISMATCH")

            matrix = json.loads((root / "repeatability-decision-matrix.json").read_text(encoding="utf-8"))
            rows = matrix.get("rows")
            if (
                matrix.get("complete") is not True
                or matrix.get("intervention") != "BASELINE_V1"
                or matrix.get("repeat") != args.repeat
                or not isinstance(rows, list)
                or len(rows) != 16384
            ):
                raise RuntimeError("REPEATABILITY_MATRIX_CONTRACT_MISMATCH")

            rules = base.bind_selected_rules(
                source_bytes=args.source.read_bytes(),
                selection_manifest=json.loads(base.SELECTION_MANIFEST.read_text(encoding="utf-8")),
            )
            examples = base.materialize_development_examples(rules)
            if len(examples) != 8192:
                raise RuntimeError("EXPECTED_8192_DEVELOPMENT_EXAMPLES")
            position = 0
            for example in examples:
                for variant, prompt in (
                    ("canonical", example.canonical_prompt),
                    ("transformed", example.transformed_prompt),
                ):
                    row = rows[position]
                    expected = {
                        "task_id": example.task_id,
                        "calculator_id": example.calculator_id,
                        "split": example.split,
                        "variant": variant,
                        "target_index": 0 if example.target_label == "A" else 1,
                        "option_a_semantic": example.option_a_semantic,
                        "prompt_sha256": base.sha256_bytes(prompt.encode()),
                    }
                    if any(row.get(key) != value for key, value in expected.items()):
                        raise RuntimeError(f"ORDERED_ROW_IDENTITY_MISMATCH:{position}")
                    logits = row.get("logits")
                    if (
                        not isinstance(logits, list)
                        or len(logits) != 2
                        or any(
                            not isinstance(value, (int, float))
                            or isinstance(value, bool)
                            or not math.isfinite(value)
                            for value in logits
                        )
                    ):
                        raise RuntimeError(f"NONFINITE_OR_INVALID_LOGITS:{position}")
                    position += 1

            stored_analysis = json.loads((root / "repeatability-analysis.json").read_text(encoding="utf-8"))
            reproduced = b1.analyze_rows(rows)
            if base.canonical_json(stored_analysis) != base.canonical_json(reproduced):
                raise RuntimeError("REPEATABILITY_ANALYSIS_REPRODUCTION_MISMATCH")

            file_rows = []
            for info in infos:
                if info.is_dir():
                    continue
                path = root / info.filename
                file_rows.append(
                    {
                        "path": info.filename,
                        "bytes": path.stat().st_size,
                        "sha256": _sha(path),
                    }
                )
            file_rows.sort(key=lambda row: row["path"])

    receipt = {
        "schema": "commandmed.v5.repeatability-export-verification.v1",
        "status": "PASS_MODEL_FREE_REPEATABILITY_EXPORT_VERIFICATION",
        "kernel": args.kernel,
        "kernel_version": args.version,
        "expected_head": args.expected_head,
        "repeat": args.repeat,
        "intervention": "BASELINE_V1",
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "durable_export_verified": True,
        "ordered_rows_verified": 16384,
        "source_task_count_verified": 8192,
        "model_weights_loaded": False,
        "scientific_replication": False,
        "clinical_validity": False,
        "confirmatory": False,
        "reserve": False,
        "spend_usd": 0,
        "riskcalcs_sha256": RISKCALCS_SHA256,
        "archive_sha256": archive_sha,
        "allowlisted_runtime_sha256": _sha(args.runtime),
        "physical_hardware_sha256": _sha(args.hardware),
        "files": file_rows,
    }
    args.receipt.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--hardware", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repeat", type=int, choices=(1, 2), required=True)
    parser.add_argument("--kernel", required=True)
    parser.add_argument("--version", type=int, required=True)
    args = parser.parse_args()
    receipt = verify(args)
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "rows": receipt["ordered_rows_verified"],
                "archive_sha256": receipt["archive_sha256"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
