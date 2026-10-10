"""Pure synthetic guardrails; the original-matrix receipt is independently replayed."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_development_calculator_icc_inventory as calc


def _balanced(rule):
    return [(f"calc-{c:02}", float(rule(c, i))) for c in range(64) for i in range(60)]


def test_same_effect_per_calculator_has_one_icc() -> None:
    x = calc.calculator_anova_components(_balanced(lambda c, _: c % 2))
    assert math.isclose(x["anovamom_rho_unclipped"], 1.0)
    assert x["illustrative_effective_cases"] == 64.0


def test_same_effect_across_calculators_has_negative_finite_sample_icc() -> None:
    x = calc.calculator_anova_components(_balanced(lambda _, i: i % 2))
    assert x["anovamom_rho_unclipped"] < 0
    assert x["illustrative_effective_cases"] is None


def test_identical_effects_are_undefined_not_zero() -> None:
    x = calc.calculator_anova_components(_balanced(lambda _c, _i: 0.5))
    assert x["rho_status"] == "UNDEFINED_ZERO_TOTAL_VARIANCE"
    assert x["anovamom_rho_unclipped"] is None


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), -float("inf"), False, "0"])
def test_non_numeric_or_nonfinite_paired_deltas_are_rejected(bad) -> None:
    pairs = _balanced(lambda c, i: c % 2)
    pairs[0] = ("calc-00", bad)
    with pytest.raises(calc.CalculatorICCContractError, match="INVALID_FINITE_PAIRED_DELTA"):
        calc.calculator_anova_components(pairs)


def test_unbalanced_calculator_source_cases_rejected() -> None:
    with pytest.raises(calc.CalculatorICCContractError, match="UNBALANCED_OR_MISSING"):
        calc.calculator_anova_components(_balanced(lambda c, i: i)[:-1])


def test_empty_calculator_identifier_rejected() -> None:
    pairs = _balanced(lambda c, i: i)
    pairs[0] = ("", 0.0)
    with pytest.raises(calc.CalculatorICCContractError, match="INVALID_CALCULATOR_ID"):
        calc.calculator_anova_components(pairs)


def test_existing_development_receipt_is_nonclinical_and_source_bound() -> None:
    path = Path(__file__).resolve().parents[2] / (
        "artifacts/v5/development/s1-calculator-icc-inventory-2026-10-10/"
        "development-calculator-icc.json"
    )
    x = json.loads(path.read_text(encoding="utf-8"))
    assert x["rows"] == 72
    assert len(x["all_development_cells"]) == 72
    assert x["reference_sd_cells_reproduced"] == 72
    assert x["n_negative_icc"] + x["n_nonnegative_icc"] + x["n_missing_icc"] == 72
    assert all(value is False for key, value in x["boundaries"].items()
               if key.endswith(("_qualified", "_reviewed", "_authorized")))
    assert x["reference_sd_sha256"] == calc.FROZEN_REFERENCE_SHA256
    assert x["input_hashes"] == calc.EXPECTED_INPUT_SHA256
