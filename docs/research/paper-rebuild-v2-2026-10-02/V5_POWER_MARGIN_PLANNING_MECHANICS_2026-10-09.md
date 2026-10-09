# V5 power/margin planning mechanics qualification — 2026-10-09

Status: `MECHANICS_ONLY; NO_NUMERIC_MARGIN_FROZEN`

This record qualifies fail-closed development-only mechanics for the final V5 margin/power gate. It does not choose a domain floor, meaningful margin, nuisance estimate, primary non-target family size, or confirmatory identity.

Implementation: `scripts/v5_power_margin_plan.py`.

## Frozen mechanics implemented

Given an explicit prospective input contract, the utility:

- requires `scope=DEVELOPMENT_ONLY_POWER_PLANNING`;
- requires confirmatory and reserve flags to remain false;
- enforces the existing V5 margin rule `m_j = max(domain_floor_j, 2 * repeatability95_j)`;
- requires a positive domain floor and frozen justification hash per metric;
- requires durable repeatability and paired-SD evidence hashes per metric;
- requires `HOLM` multiplicity, family-wise alpha, primary non-target family size, desired power and planned source-cluster count as explicit inputs;
- uses the conservative Holm first-step threshold `alpha / family_size` for per-cell normal-approximation power planning;
- computes the normal-approximation MDE at the planned cluster count and the corresponding required cluster count at the frozen margin;
- preserves zero paired SD as zero planning noise rather than inventing positive variance;
- fails closed on missing, malformed, nonfinite, negative or unfrozen inputs.

The conservative `alpha / family_size` planning threshold is a sufficient worst-case planning rule for the first Holm step. It does not replace the final Holm procedure on confirmatory p-values and does not assert independence across endpoint tests.

## Explicit non-decisions

This qualification does not select or infer:

- any numeric `domain_floor_j`;
- any numeric `m_j`;
- any `repeatability95_j` value before the two frozen repeats are durable;
- any paired SD or variance estimate;
- the primary non-target family size if that family has not yet been frozen;
- any confirmatory sample identity;
- any effect classification, equivalence/noninferiority conclusion, p-value or confidence interval.

Observed development intervention effects are not inputs to selecting domain floors. A later final power plan must bind every numeric input to a durable evidence/justification SHA-256.

## Boundary

The utility is planning-only. It never reads model weights, calls a model, materializes confirmatory/reserve identities, uses PHI/private/gated clinical data, or authorizes paid compute/API use. PR #320 remains OPEN / DRAFT / UNMERGED. Publication, independent-family replication, confirmatory/reserve execution and merge remain outside current authority.
