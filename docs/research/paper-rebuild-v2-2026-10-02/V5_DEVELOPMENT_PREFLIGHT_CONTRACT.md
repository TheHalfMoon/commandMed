# V5 development execution preflight contract

Status: `MECHANICALLY_IMPLEMENTED`; `EXECUTION_AUTHORITY=NO`.

This contract implements the fail-closed boundary requested in `V5_DEVELOPMENT_EXECUTION_AUTHORITY_REQUEST.md`. It validates a proposed development run but does not approve authority, acquire weights, load a model, run inference, or train.

## Exact model boundary

Only `Qwen/Qwen3.5-0.8B-Base` at revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68` can pass the V5 development preflight. A model artifact SHA-256 and exact 40-hex code SHA are mandatory before model execution.

## Allowed roles

The only admissible run roles are `RULE_ORACLE_DEVELOPMENT`, `RULE_ORACLE_CALIBRATION`, `SQUAD_RETENTION`, and `SYNTHETIC_MECHANICAL`. `SQUAD_RETENTION` is restricted to `C2_CRDI_RETAIN_V1`. Confirmatory and reserve materialization are rejected.

## Training boundary

Only `BASELINE_V1` and the seven frozen V5 intervention IDs are admissible; unknown or `latest` IDs fail closed. Training can pass only for `B1_TYPED_V1`, `C1_CRDI_V1`, or `C2_CRDI_RETAIN_V1`. Mechanical interventions do not become trainable merely because their code exists.

## Cost and data boundary

Both the authority object and the run manifest must declare zero paid compute/API usage and zero expected spend. PHI, gated data, confirmatory access, and reserve access are rejected. The environment identity must be a SHA-256 binding and output must remain below `artifacts/v5/development/` without parent traversal.

## Authority boundary

The default authority object is denied. A synthetic test object can demonstrate the shape of a passing contract, but it is not founder approval. Until the founder explicitly approves the bounded request, real execution remains blocked even though the validator is implemented.

## Evidence

Implementation: `src/commandmed/reliability_v5/preflight.py`. Regression tests: `tests/reliability_v5/test_preflight.py`. The tests include default-deny, exact model/revision, artifact identity, zero-cost, holdout quarantine, PHI/gated-data, trainable-intervention, SQuAD-role, and code/data-role failure cases.
