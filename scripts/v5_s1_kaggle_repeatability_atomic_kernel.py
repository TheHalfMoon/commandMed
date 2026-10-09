"""Private atomic unchanged-base repeatability kernel."""
import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(expected_head: str, admission: dict) -> int:
    repeat = admission.get("repeat")
    if not re.fullmatch("[0-9a-f]{40}", expected_head) or admission.get("private") is not True:
        raise ValueError("PRIVATE_EXACT_HEAD_REQUIRED")
    if (
        admission.get("intervention") != "BASELINE_V1"
        or admission.get("purpose") != "UNCHANGED_BASE_REPEATABILITY"
        or type(repeat) is not int
        or repeat not in (1, 2)
    ):
        raise ValueError("ATOMIC_FROZEN_REPEATABILITY_ONLY")
    if admission.get("resume") is not False:
        raise ValueError("ATOMIC_NO_RESUME_REQUIRED")

    output = Path("/kaggle/working")
    workspace = Path(tempfile.mkdtemp(prefix="commandmed-repeatability-"))
    repo = workspace / "repo"
    result = {
        "status": "ATOMIC_BOOTSTRAP_IN_PROGRESS",
        "expected_head": expected_head,
        "intervention": "BASELINE_V1",
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "repeat": repeat,
        "spend_usd": 0,
        "resume": False,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
    }
    try:
        import torch

        physical = {
            "python": sys.version,
            "torch": torch.__version__,
            "cuda": torch.version.cuda,
            "cuda_device_count": torch.cuda.device_count(),
            "visible_gpus": [
                {
                    "index": index,
                    "name": torch.cuda.get_device_name(index),
                    "total_memory_bytes": torch.cuda.get_device_properties(index).total_memory,
                    "scientific_use": index == 0,
                }
                for index in range(torch.cuda.device_count())
            ],
            "scientific_gpu_count": 1,
            "scientific_device": "cuda:0",
        }
        hardware = workspace / "physical-hardware.json"
        hardware.write_text(json.dumps(physical), encoding="utf-8")
        (output / "commandmed-physical-hardware.json").write_text(
            json.dumps(physical, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        subprocess.run(
            [
                "git",
                "clone",
                "--single-branch",
                "--branch",
                "research/commandmed-paper-first-principles",
                "https://github.com/TheHalfMoon/commandMed.git",
                str(repo),
            ],
            check=True,
        )
        actual = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
        ).strip()
        if actual != expected_head:
            raise RuntimeError("ATOMIC_LIVE_GIT_HEAD_MISMATCH")

        torch_before = importlib.metadata.version("torch")
        try:
            optional_torchao = importlib.metadata.version("torchao")
        except importlib.metadata.PackageNotFoundError:
            optional_torchao = None
        if optional_torchao is not None:
            subprocess.run(
                [sys.executable, "-m", "pip", "uninstall", "--yes", "torchao"],
                check=True,
            )
        result["runtime_repair"] = {
            "unused_optional_extension": "torchao",
            "before": optional_torchao,
            "after": None,
            "scope": "PREMODEL_ENVIRONMENT_ONLY; DIRECT_BF16_UNCHANGED",
        }
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "transformers==5.18.0",
                "tokenizers==0.23.2",
                "peft==0.21.2",
                "psutil==7.1.0",
                "safetensors==0.8.0",
                "huggingface-hub==1.33.0",
            ],
            check=True,
        )
        if importlib.metadata.version("torch") != torch_before:
            raise RuntimeError("ATOMIC_SUPPLIED_TORCH_CHANGED_DURING_SETUP")

        record = workspace / "admission.json"
        record.write_text(json.dumps(admission), encoding="utf-8")
        environment = dict(
            os.environ,
            CUDA_VISIBLE_DEVICES="0",
            HF_HUB_DISABLE_IMPLICIT_TOKEN="1",
        )
        command = [
            sys.executable,
            str(repo / "scripts/v5_s1_kaggle_repeatability.py"),
            "--expected-head",
            expected_head,
            "--admission",
            str(record),
            "--model-dir",
            str(workspace / "model"),
            "--source",
            str(workspace / "riskcalcs.json"),
        ]
        process = subprocess.run(command, env=environment)
        archive = (
            repo
            / "artifacts/v5/development/s1-kaggle-repeatability-runtime"
            / f"repeat-{repeat}.zip"
        )
        if archive.is_file():
            shutil.copyfile(
                archive,
                output / f"commandmed-base-repeatability-r{repeat}-evidence.zip",
            )
        result.update(
            status="ATOMIC_KERNEL_FINISHED",
            exit_code=process.returncode,
            exported_archive=archive.is_file(),
        )
    except Exception as exc:
        result.update(
            status="ATOMIC_BOOTSTRAP_BLOCKED",
            reason=str(exc),
            exception_type=type(exc).__name__,
        )
    finally:
        (output / "commandmed-atomic-kernel-result.json").write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(result, sort_keys=True), flush=True)
    return 0 if result.get("exit_code") == 0 else 2


if __name__ == "__main__":
    raise SystemExit(
        run(
            os.environ["COMMANDMED_EXPECTED_HEAD"],
            json.loads(os.environ["COMMANDMED_ADMISSION_JSON"]),
        )
    )
