from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"expected text not found in {path}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def apply_repairs() -> None:
    replace_once(
        ".specify/scripts/powershell/common.ps1",
        '                foreach ($pid in $sortedPresets) {\n                    $mf = Join-Path $presetsDir "$pid/preset.yml"',
        '                foreach ($presetCandidateId in $sortedPresets) {\n                    $mf = Join-Path $presetsDir "$presetCandidateId/preset.yml"',
    )
    replace_once(
        ".specify/scripts/powershell/common.ps1",
        "    if ($FeatureDirectory.StartsWith($prefix, $cmp)) {\n        $FeatureDirectory = $FeatureDirectory.Substring($prefix.Length)\n    }\n\n    $fjPath =",
        "    if ($FeatureDirectory.StartsWith($prefix, $cmp)) {\n        $FeatureDirectory = $FeatureDirectory.Substring($prefix.Length)\n    }\n    # Persist repository-relative paths portably across Windows/Linux consumers.\n    $FeatureDirectory = $FeatureDirectory.Replace('\\\\', '/')\n\n    $fjPath =",
    )

    replace_once(
        ".specify/scripts/powershell/setup-plan.ps1",
        '}\n\n# Load common functions\n. "$PSScriptRoot/common.ps1"',
        '}\n\nif ($RemainingArgs -and $RemainingArgs.Count -gt 0) {\n    [Console]::Error.WriteLine("ERROR: Unknown option \'$($RemainingArgs[0])\'")\n    exit 1\n}\n\n# Load common functions\n. "$PSScriptRoot/common.ps1"',
    )
    replace_once(
        ".specify/scripts/powershell/setup-plan.ps1",
        "        # Create a basic plan file if template doesn't exist\n        New-Item -ItemType File -Path $paths.IMPL_PLAN -Force | Out-Null",
        "        # Missing templates are a hard prerequisite failure; never create an empty plan.\n        exit 1",
    )
    replace_once(
        ".specify/scripts/python/setup_plan.py",
        '            print("Warning: Plan template not found", file=status_stream)\n            paths.impl_plan.touch()',
        '            print("Warning: Plan template not found", file=status_stream)\n            return 1',
    )

    replace_once(
        ".specify/scripts/python/check_prerequisites.py",
        '        return 1\n\n    if not paths.impl_plan.is_file():',
        '        return 1\n\n    if not paths.feature_spec.is_file():\n        print(f"ERROR: spec.md not found in {paths.feature_dir}", file=sys.stderr)\n        print(\n            f"Run {format_speckit_command(\'specify\', paths.repo_root)} first to create the feature structure.",\n            file=sys.stderr,\n        )\n        return 1\n\n    if not paths.impl_plan.is_file():',
    )

    ps_path = Path(".specify/scripts/powershell/check-prerequisites.ps1")
    ps = ps_path.read_text(encoding="utf-8")
    if "ERROR: spec.md not found" not in ps:
        old = '''if (-not (Test-Path $paths.IMPL_PLAN -PathType Leaf)) {
    [Console]::Error.WriteLine("ERROR: plan.md not found in $($paths.FEATURE_DIR)")
    $planCommand = '/speckit-plan'
'''
        new = '''if (-not (Test-Path $paths.FEATURE_SPEC -PathType Leaf)) {
    [Console]::Error.WriteLine("ERROR: spec.md not found in $($paths.FEATURE_DIR)")
    $specifyCommand = Format-SpecKitCommand -CommandName 'specify' -RepoRoot $paths.REPO_ROOT
    [Console]::Error.WriteLine("Run $specifyCommand first to create the feature structure.")
    exit 1
}

if (-not (Test-Path $paths.IMPL_PLAN -PathType Leaf)) {
    [Console]::Error.WriteLine("ERROR: plan.md not found in $($paths.FEATURE_DIR)")
    $planCommand = Format-SpecKitCommand -CommandName 'plan' -RepoRoot $paths.REPO_ROOT
'''
        if old not in ps:
            raise SystemExit("expected PowerShell prerequisite block not found")
        ps = ps.replace(old, new, 1)
    ps = ps.replace(
        "    $specifyCommand = '/speckit-specify'",
        "    $specifyCommand = Format-SpecKitCommand -CommandName 'specify' -RepoRoot $paths.REPO_ROOT",
    )
    ps = ps.replace(
        "    $planCommand = '/speckit-plan'",
        "    $planCommand = Format-SpecKitCommand -CommandName 'plan' -RepoRoot $paths.REPO_ROOT",
    )
    ps = ps.replace(
        "    $tasksCommand = '/speckit-tasks'",
        "    $tasksCommand = Format-SpecKitCommand -CommandName 'tasks' -RepoRoot $paths.REPO_ROOT",
    )
    ps_path.write_text(ps, encoding="utf-8")

    benchmark_path = Path("data/eval/benchmarks.json")
    benchmarks = json.loads(benchmark_path.read_text(encoding="utf-8"))
    medhelm = next(item for item in benchmarks if item.get("benchmark_id") == "medhelm")
    medhelm["license_source_uri"] = (
        "https://github.com/stanford-crfm/helm/blob/"
        "63754d05db6f874e41a395880fb573890a13e791/LICENSE"
    )
    convenience = (
        " Convenience license branch reference (non-identity-bearing): "
        "https://github.com/stanford-crfm/helm/blob/main/LICENSE."
    )
    if convenience.strip() not in medhelm["notes"]:
        medhelm["notes"] += convenience
    benchmark_path.write_text(
        json.dumps(benchmarks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    gold_path = Path("data/eval/gold_protocols.json")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    replacements = {
        "FINAL_PRE_RELEASE_SAFETY_AUDIT": "PRE_RELEASE_SAFETY_AUDIT",
        "FINAL_ARABIC_PRE_RELEASE_SAFETY_AUDIT": "ARABIC_PRE_RELEASE_SAFETY_AUDIT",
    }
    for record in gold:
        record["permitted_scoring_stages"] = [
            replacements.get(stage, stage)
            for stage in record["permitted_scoring_stages"]
        ]
    gold_path.write_text(
        json.dumps(gold, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    validate_path = Path("src/commandmed/eval_contract/validate.py")
    validate = validate_path.read_text(encoding="utf-8")
    if "VALID_GOLD_SCORING_STAGES" not in validate:
        anchor = '''PROHIBITED_GOLD_STAGE_SUBSTRINGS = {
    "SELECTION", "ADAPTER_GATE", "BACKBONE_GATE", "CHECKPOINT_GATE",
}
'''
        addition = anchor + '''
VALID_GOLD_SCORING_STAGES = {
    "ARABIC_PRE_RELEASE_SAFETY_AUDIT",
    "MULTIMODAL_PRE_RELEASE_SAFETY_AUDIT",
    "POST_QUANTIZATION_REGRESSION_AUDIT",
    "PRE_RELEASE_SAFETY_AUDIT",
}
'''
        if anchor not in validate:
            raise SystemExit("Gold scoring-stage constant anchor not found")
        validate = validate.replace(anchor, addition, 1)

    old_loop = '''        for stage in scoring_stages:
            if isinstance(stage, str):
                for prohibited_sub in PROHIBITED_GOLD_STAGE_SUBSTRINGS:
                    if prohibited_sub in stage.upper():
                        errors.append(
                            f"{prefix}: Contradiction in permitted_scoring_stages: '{stage}' contains prohibited keyword '{prohibited_sub}'. Private Gold cannot perform candidate selection."
                        )
'''
    new_loop = '''        for stage in scoring_stages:
            if not isinstance(stage, str):
                continue
            for prohibited_sub in PROHIBITED_GOLD_STAGE_SUBSTRINGS:
                if prohibited_sub in stage.upper():
                    errors.append(
                        f"{prefix}: Contradiction in permitted_scoring_stages: '{stage}' contains prohibited keyword '{prohibited_sub}'. Private Gold cannot perform candidate selection."
                    )
            if stage not in VALID_GOLD_SCORING_STAGES:
                errors.append(
                    f"{prefix}: Unknown permitted_scoring_stage '{stage}'. Allowed: {sorted(VALID_GOLD_SCORING_STAGES)}"
                )
'''
    if new_loop not in validate:
        if old_loop not in validate:
            raise SystemExit("Gold scoring-stage validation loop not found")
        validate = validate.replace(old_loop, new_loop, 1)

    old_gate = '''        if metric.get("is_hard_gate") is True:
            metric_id = metric.get("metric_id")
            if isinstance(metric_id, str) and metric_id:
                hard_gate_metrics[metric_id] = metric
            else:
                malformed_catalog = True
'''
    new_gate = '''        if metric.get("is_hard_gate") is True:
            metric_id = metric.get("metric_id")
            if not isinstance(metric_id, str) or not metric_id:
                malformed_catalog = True
                continue
            if validate_metric(metric):
                malformed_catalog = True
                continue
            hard_gate_metrics[metric_id] = metric
'''
    if new_gate not in validate:
        if old_gate not in validate:
            raise SystemExit("hard-gate validation loop not found")
        validate = validate.replace(old_gate, new_gate, 1)
    validate_path.write_text(validate, encoding="utf-8")

    fail_path = Path("tests/eval_contract/test_fail_closed.py")
    fail_text = fail_path.read_text(encoding="utf-8")
    if "test_29_malformed_hard_gate_record_is_insufficient" not in fail_text:
        marker = '\n\nif __name__ == "__main__":\n'
        test = '''
    def test_29_malformed_hard_gate_record_is_insufficient(self):
        state, _ = evaluate_hard_gates(
            [{"metric_id": "gate", "is_hard_gate": True}],
            {"gate": {"status": "PASS"}},
        )
        self.assertEqual(
            state,
            GateEvaluationState.INSUFFICIENT_EVIDENCE.value,
        )
'''
        if marker not in fail_text:
            raise SystemExit("test_fail_closed insertion marker not found")
        fail_text = fail_text.replace(marker, "\n" + test + marker, 1)
    fail_text = fail_text.replace(
        '"prohibited_sources": gold,',
        '"prohibited_sources": list(gold),',
    )
    fail_path.write_text(fail_text, encoding="utf-8")

    gold_test_path = Path("tests/eval_contract/test_gold_quarantine.py")
    gold_test = gold_test_path.read_text(encoding="utf-8")
    if "test_unknown_gold_scoring_stage_fails" not in gold_test:
        anchor = "    def test_gold_protocol_requires_power_analysis(self) -> None:\n"
        test = '''    def test_unknown_gold_scoring_stage_fails(self) -> None:
        """Unknown private-Gold scoring stages must fail closed."""
        bad_gold = dict(self.gold_data[0])
        bad_gold["permitted_scoring_stages"] = ["UNREGISTERED_SAFETY_AUDIT"]
        errors = validate_gold_protocol(bad_gold)
        self.assertTrue(
            any("Unknown permitted_scoring_stage" in e for e in errors)
        )

'''
        if anchor not in gold_test:
            raise SystemExit("gold test insertion anchor not found")
        gold_test = gold_test.replace(anchor, test + anchor, 1)
    gold_test_path.write_text(gold_test, encoding="utf-8")


def update_evidence(log_path: str) -> None:
    from src.commandmed.eval_contract.canonical import compute_file_canonical_sha256

    log = Path(log_path).read_text(encoding="utf-8")
    match = re.search(r"Ran (\d+) tests in ([0-9.]+)s", log)
    if not match:
        raise SystemExit("could not parse unittest result")
    count = int(match.group(1))

    closeout = Path("specs/001-eval-charter/closeout.md")
    text = closeout.read_text(encoding="utf-8")
    text = re.sub(
        r"Ran \d+ tests(?: in [0-9.]+s)?",
        f"Ran {count} tests",
        text,
        count=1,
    )
    text = re.sub(
        r"\b\d+ unit tests passing offline\b",
        f"{count} unit tests passing offline",
        text,
    )
    if "5. `tests/eval_contract/test_fail_closed.py`" not in text:
        anchor = (
            "4. `tests/eval_contract/test_canonical.py`: Proves key-order independence, "
            "set-like list field reordering invariance, entity collection reordering "
            "invariance, SHA-256 digest stability, and semantic mutation sensitivity.\n"
        )
        addition = anchor + (
            "5. `tests/eval_contract/test_fail_closed.py`: Exercises fail-closed "
            "governance boundaries for absent/malformed hard gates, quarantine matrix "
            "violations, impossible dates, and malformed parsed JSON.\n"
        )
        if anchor not in text:
            raise SystemExit("closeout coverage anchor not found")
        text = text.replace(anchor, addition, 1)

    old_hashes = {
        "benchmarks.json": "7bb4f596f843450252b0d5eb18b85b713c7e3f33b41d9b3efb635b6b773e71f7",
        "gold_protocols.json": "8e7c8a71e664996e8722adc4a6b32dc712ed59e81fff31053556bf52b465a592",
        "metrics.json": "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a",
        "quarantine.json": "b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080",
    }
    for name, old_hash in old_hashes.items():
        digest = compute_file_canonical_sha256(Path("data/eval") / name)
        print(f"{name}={digest}")
        text = text.replace(old_hash, digest)
    closeout.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-log")
    args = parser.parse_args()
    if args.evidence_log:
        update_evidence(args.evidence_log)
    else:
        apply_repairs()
