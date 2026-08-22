"""Static regressions for bounded Spec Kit bootstrap repairs in Spec 001."""

from pathlib import Path
import unittest


class TestSpecKitExternalReview(unittest.TestCase):
    """Prevent reintroduction of reviewed cross-platform/fail-closed defects."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[2]
        cls.ps_dir = cls.repo_root / ".specify" / "scripts" / "powershell"
        cls.py_dir = cls.repo_root / ".specify" / "scripts" / "python"

    def _read(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def test_common_ps1_does_not_assign_pid_automatic_variable(self) -> None:
        text = self._read(self.ps_dir / "common.ps1")
        self.assertNotIn("foreach ($pid in $sortedPresets)", text)
        self.assertIn("foreach ($presetCandidateId in $sortedPresets)", text)

    def test_create_feature_persists_posix_repo_relative_path(self) -> None:
        text = self._read(self.ps_dir / "create-new-feature.ps1")
        self.assertIn(
            'Save-FeatureJson -RepoRoot $repoRoot -FeatureDirectory "specs/$branchName"',
            text,
        )
        self.assertNotIn(
            "Save-FeatureJson -RepoRoot $repoRoot -FeatureDirectory $featureDir",
            text,
        )

    def test_powershell_setup_plan_rejects_unknown_arguments(self) -> None:
        text = self._read(self.ps_dir / "setup-plan.ps1")
        self.assertIn("$RemainingArgs.Count -gt 0", text)
        self.assertIn("ERROR: Unknown option", text)

    def test_setup_plan_twins_fail_closed_on_missing_template(self) -> None:
        ps_text = self._read(self.ps_dir / "setup-plan.ps1")
        py_text = self._read(self.py_dir / "setup_plan.py")
        self.assertNotIn("New-Item -ItemType File -Path $paths.IMPL_PLAN", ps_text)
        self.assertNotIn("paths.impl_plan.touch()", py_text)
        self.assertIn("Warning: Plan template not found", ps_text)
        self.assertIn("Warning: Plan template not found", py_text)
        self.assertIn("return 1", py_text)

    def test_python_setup_plan_rejects_unknown_arguments(self) -> None:
        text = self._read(self.py_dir / "setup_plan.py")
        self.assertIn("ERROR: Unknown option", text)
        self.assertIn("return 1", text)

    def test_python_prerequisites_require_spec_before_plan(self) -> None:
        text = self._read(self.py_dir / "check_prerequisites.py")
        spec_check = "if not paths.feature_spec.is_file():"
        plan_check = "if not paths.impl_plan.is_file():"
        self.assertIn(spec_check, text)
        self.assertLess(text.index(spec_check), text.index(plan_check))
        self.assertIn("format_speckit_command('specify', paths.repo_root)", text)

    def test_powershell_prerequisites_require_spec_before_plan(self) -> None:
        text = self._read(self.ps_dir / "check-prerequisites.ps1")
        spec_check = "Test-Path $paths.FEATURE_SPEC -PathType Leaf"
        plan_check = "Test-Path $paths.IMPL_PLAN -PathType Leaf"
        self.assertIn(spec_check, text)
        self.assertLess(text.index(spec_check), text.index(plan_check))

    def test_powershell_prerequisite_help_uses_configured_command_formatter(self) -> None:
        text = self._read(self.ps_dir / "check-prerequisites.ps1")
        self.assertIn("Format-SpecKitCommand -CommandName 'specify'", text)
        self.assertIn("Format-SpecKitCommand -CommandName 'plan'", text)
        self.assertIn("Format-SpecKitCommand -CommandName 'tasks'", text)
        self.assertNotIn("$planCommand = '/speckit-plan'", text)
        self.assertNotIn("$tasksCommand = '/speckit-tasks'", text)


if __name__ == "__main__":
    unittest.main()
