# V5 calibration/selective diagnostic mechanics — 2026-10-09

Status: `MECHANICS_ONLY; NO_NUMERIC_DIAGNOSTIC_CONVENTION_FROZEN`

This record qualifies project-owned mechanics needed for later development-only calibration and selective-control analysis without choosing a scientific convention that is not already frozen.

The implementation is `src/commandmed/reliability_v5/diagnostics.py`.

## Qualified mechanics

The module can:

- bin caller-defined confidence/event pairs using caller-supplied explicit bin edges;
- retain empty bins without silently dropping the frozen layout;
- compute a count-weighted absolute calibration gap from an already specified reliability table;
- compute selective risk and coverage from an explicit acceptance mask;
- evaluate an explicit ordered set of thresholds under an explicit score orientation.

The module fails closed on malformed lengths, nonfinite values, invalid probabilities, invalid binary outcomes, malformed bin edges, duplicate thresholds, and undefined zero-coverage selective risk.

## Explicit non-decisions

This implementation does **not** choose:

- top-label versus classwise versus marginal calibration;
- bin count or bin edges;
- adaptive versus fixed-width binning;
- confidence score definition;
- abstention threshold;
- target coverage or target risk;
- AURC integration convention;
- calibration-map fitting rule;
- temperature-selection rule;
- selection-bias prior-fitting split;
- any meaningful-effect margin or domain floor.

Those choices remain scientific protocol gates and must be frozen prospectively before their corresponding development result is interpreted for later confirmatory planning. Mechanics tests cannot be used as evidence that any one convention is scientifically preferred.

## Scientific boundary

No model output is read by this qualification. No model call, intervention fit, confirmatory/reserve identity, PHI, gated/private clinical data, paid API, or paid compute is involved.

The functions accept explicit inputs so later analysis code cannot silently optimize a threshold or binning rule after seeing outcomes. A caller that needs a not-yet-frozen convention must stop and record a scientific/governance blocker rather than select one implicitly.

This record does not close the V5 scientific freeze and does not promote any empirical claim. PR #320 remains OPEN / DRAFT / UNMERGED.
