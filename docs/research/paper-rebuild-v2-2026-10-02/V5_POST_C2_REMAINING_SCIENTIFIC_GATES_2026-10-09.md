# V5 post-C2 remaining scientific gates — 2026-10-09

Status: `AUDIT_ONLY; NO_NEW_SCIENTIFIC_AUTHORITY`

This record audits the adopted V5 protocol against the current implementation/evidence frontier. It does not change the protocol, select a scientific convention, authorize a new model run, or promote any empirical claim.

## Already mechanically available

- development/calibration-only B1, C1 and C2 learned-intervention paths;
- frozen C1/C2 model/revision/dtype/objective/seed contracts;
- paired source-cluster statistics, Holm adjustment and normal-approximation MDE/planning helpers;
- parameter-explicit calibration-bin and selective-risk/coverage mechanics that do not choose their scientific parameters;
- development-only cross-seed synthesis mechanics that fail closed until all three C2 seeds are durable.

## Remaining gates after C2 seed 47 becomes durable

### 1. Unchanged-base repeatability

The V5 evaluation protocol requires unchanged-base repeated runs. The power/margin gate defines `repeatability95_j` as the 95th percentile absolute unchanged-base paired difference on development-only repeated runs.

The current durable evidence contains one complete scientific baseline decision matrix from the B1 stage. Resource-timing probes in later C1/C2 runs are not complete scientific matrices and do not export the raw repeated logits needed to compute property-level `repeatability95_j`.

The 2026-10-08 Kaggle runtime amendment explicitly states `Do not rerun baseline/B1`. Therefore a new Kaggle unchanged-base repeat cannot be inferred from the existing runtime authority. If Kaggle is used to obtain repeatability evidence, a narrow prospective runtime amendment is required before any such model call.

### 2. Calibration diagnostic definition

V5 requires probability calibration diagnostics, but the repository explicitly states that multiclass calibration requires an explicitly chosen definition and that ECE is not a universal substitute.

The following remain scientifically unfrozen:

- top-label versus classwise versus another declared calibration definition;
- fixed versus adaptive reliability binning;
- exact bin count/edges if a binned diagnostic is used;
- any calibration-map fitting/temperature-selection rule.

The project-owned diagnostics implementation intentionally requires these choices as explicit inputs and does not select them after seeing results.

### 3. Selective-control definition

V5 requires selective risk together with coverage. The mechanics can evaluate explicit masks/thresholds, but the protocol has not yet bound:

- the per-item loss used for selective risk;
- the confidence/selection score;
- the fixed threshold or target-risk/target-coverage rule;
- the AURC integration convention, if AURC is retained as a reported diagnostic.

These must be frozen prospectively before corresponding development results are interpreted for confirmatory planning.

### 4. A1/A2/D1 development application rules

The mechanical implementations exist, but the current V5 records do not yet bind all application/tuning choices needed for a complete development matrix:

- A1 scalar temperature fitting/selection rule;
- A2 prior-estimation/fitting split and exact application composition where needed;
- D1 threshold/target rule;
- ordered A1/A2 composition where both orders are operationally admitted.

No current artifact should silently infer these choices from observed development rankings.

### 5. Meaningful native-unit margins

The fixed rule remains:

`m_j = max(domain_floor_j, 2 * repeatability95_j)`.

No numeric `domain_floor_j` values are currently frozen. A domain floor requires written justification from measurement meaning, literature, or operational consequence. It may not be reverse-engineered from confirmatory effects or weakened to rescue power.

### 6. Final power gate

The planned primary RULE_ORACLE confirmatory size is 4096 source clusters, desired power is 0.90, alpha is 0.05, and the primary non-target family uses Holm control. Final MDE/required-cluster planning cannot close until the native-unit margins and development-only nuisance/repeatability quantities are frozen.

### 7. Confirmatory and replication authority

Confirmatory/reserve identities remain unmaterialized and execution remains unauthorized. Independent-family SmolLM2 replication also remains outside the current bounded execution authority.

## Current fail-closed conclusion

C2 completion is necessary but not sufficient to close V5 development. After C2 seed 47, the executor may complete the frozen cross-seed synthesis and all analysis that uses already-bound definitions. It must stop rather than invent a repeatability runtime exception, calibration convention, selective threshold, domain floor, or confirmatory authority.

This audit creates no blocker by itself; it makes the remaining prospective decisions explicit so the project can close them without post-hoc ambiguity.
