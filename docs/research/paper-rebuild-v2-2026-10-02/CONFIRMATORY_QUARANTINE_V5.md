# V5 confirmatory quarantine protocol

Status: `PROCEDURE_FROZEN_CONFIRMATORY_IDENTITIES_NOT_MATERIALIZED`.

Purpose: prevent case-specific development feedback from selecting or tuning against the final RULE_ORACLE confirmatory sample while keeping development and calibration reproducible.

## Admitted case spaces

Each selected calculator must expose at least `1024` statically generated Boolean/numeric-threshold states. The case identity is intrinsic to calculator identity, state index and canonical inputs; changing the selection salt cannot rename the same case.

The public rule definition is not secret. This quarantine protects **future case selection**, not rule secrecy. Developers can know the rule and the candidate state space; they cannot know which still-unselected states will become the confirmatory sample before the future-randomness event.

## Stage 1 — fixed development and calibration

Before model execution, `prefreeze_state_partition()` deterministically selects per calculator:
- `64` development states;
- `64` disjoint calibration states.

The repository commits their identities/hashes and the exact generator/mechanics. It does **not** create a fixed 128-case holdout pool, and it does not commit future confirmatory/reserve identities.

With a minimum 1024-state calculator, at least `896` candidate states remain unselected before the final random sample.
## Stage 2 — implementation freeze event

After prompts, intervention code, hyperparameters, calibration rules, model revisions, statistical code and tuning budgets are fixed, create a dedicated GitHub `FREEZE_EVENT` record identifying the clean commit and its GitHub server `created_at` timestamp.

The event must remain unedited. If timestamp or body provenance is ambiguous, the event is invalid and a new freeze event is required before confirmatory selection.

Any model-facing implementation change after the valid freeze event invalidates the pending confirmatory selection.

## Stage 3 — future public randomness

Use the first valid NIST Randomness Beacon 2.0 pulse strictly after the freeze-event timestamp. Record chain/index, time, 512-bit output value, certificate identity when available and the exact response hash.

Official NIST source: `https://csrc.nist.gov/projects/interoperable-randomness-beacons/beacon-20`.

NIST labels Beacon 2.0 as beta. NIST also describes future-beacon randomness as a mechanism for publicly auditable randomized selection. If the required pulse cannot be retrieved or verified, do not silently substitute another source; the confirmatory selection remains blocked until a replacement procedure is explicitly reviewed and frozen.

`derive_partition_seed()` hashes the fixed namespace, clean freeze commit and 512-bit beacon output. The beacon value is public randomness, not a secret key.

## Stage 4 — future confirmatory/reserve selection

For each calculator, `confirmatory_reserve_state_partition()` HMAC-ranks every candidate state index that was not used for development or calibration. Using the future seed, it selects:
- `64` states -> confirmatory;
- next `64` states -> reserve.

This yields `4096` confirmatory source clusters and `4096` reserve clusters across 64 calculators, while drawing from a substantially larger still-unselected state space.
## Access and invalidation rules

- Confirmatory and reserve identities are not materialized before the clean freeze event and future beacon pulse.
- Reserve cases are not a second fishing set; any use requires a prespecified replacement or replication rule and explicit reporting.
- Any accidental confirmatory access before the planned run is logged; affected analyses lose confirmatory status.
- Repeated confirmatory access converts the affected analysis to development/regression evidence.
- No threshold, prompt, checkpoint, training schedule, metric definition, intervention or model-selection choice may be changed from confirmatory outputs.
- The final paper releases the beacon record, seed derivation inputs, split assignments and audit hashes after confirmatory completion.

## Known limitation

Because the underlying calculator rules and candidate state construction are public, this design cannot create secret labels. Its purpose is narrower and auditable: prevent the research team from knowing the exact future confirmatory sample during model/intervention development. Claims must describe it as future-sample quarantine, not as an externally hidden clinical test set.

This protocol fixes quarantine mechanics only. It does not authorize model execution and does not establish the clinical validity of the underlying rules.
