# V5 S1 cross-property development completion results — 2026-10-09

Status: `COMPLETE_DEVELOPMENT_CROSS_PROPERTY_DIAGNOSTICS; NOT_CONFIRMATORY`

Run source: `65f62778388abc8f20b5d139018a4a743a538079`, tree `4c778e1334365a6b06af3572c8f9df11f81c19a7`.

Canonical output: `artifacts/v5/development/s1-cross-property-completion-2026-10-09/development-cross-property.json`.

Output SHA-256: `e2c73a8f86049ec7d3f4a13d1fa4bafe38583b3e9e09a846dcc0b37c033f7df2`.

The analysis uses only already-durable development/calibration matrices and parameters prospectively frozen in `V5_S1_CROSS_PROPERTY_DEVELOPMENT_COMPLETION_FREEZE_2026-10-09.md`. It performs no model call, training, threshold refit, temperature refit, bin selection, confirmatory/reserve access or claim promotion.

## Fixed D1 policy transport

The baseline D1 threshold remains exactly `0.8933094060543488`, selected previously from baseline canonical `S1_CAL_TUNE` under the frozen 5% methodological tuning-risk target. This completion analysis applies that threshold unchanged to every admitted condition.

| Condition | Seed | DEV canonical coverage | DEV canonical risk | CAL canonical coverage | CAL canonical risk |
| --- | ---: | ---: | ---: | ---: | ---: |
| BASELINE_V1 | — | 0.006510416666666667 | 0.48 | 0.00546875 | 0.47619047619047616 |
| A1_TS_V1 | — | 0.0 | null | 0.0 | null |
| A2_SELBIAS_V1 | — | 0.0 | null | 0.0 | null |
| A1_THEN_A2 | — | 0.0 | null | 0.0 | null |
| A2_THEN_A1 | — | 0.0 | null | 0.0 | null |
| B1_TYPED_V1 | 11 | 1.0 | 0.51875 | 1.0 | 0.5067708333333333 |
| B1_TYPED_V1 | 29 | 1.0 | 0.48125 | 1.0 | 0.49322916666666666 |
| B1_TYPED_V1 | 47 | 1.0 | 0.51875 | 1.0 | 0.5067708333333333 |
| C1_CRDI_V1 | 11 | 0.0 | null | 0.0 | null |
| C1_CRDI_V1 | 29 | 0.0 | null | 0.0 | null |
| C1_CRDI_V1 | 47 | 0.0 | null | 0.0 | null |
| C2_CRDI_RETAIN_V1 | 11 | 0.0018229166666666667 | 0.0 | 0.0013020833333333333 | 0.0 |
| C2_CRDI_RETAIN_V1 | 29 | 0.0 | null | 0.0 | null |
| C2_CRDI_RETAIN_V1 | 47 | 0.0 | null | 0.0 | null |
| C1_THEN_A1 | 11 | 0.0 | null | 0.0 | null |
| C1_THEN_A1 | 29 | 0.0 | null | 0.0 | null |
| C1_THEN_A1 | 47 | 0.0 | null | 0.0 | null |

Transformed-form results are preserved in the machine-readable artifact. They are similarly unstable: for example C1 seed 11 transformed DEV coverage is `0.0078125` with risk `0.5666666666666667`, while C2 seed 47 transformed DEV coverage is `0.0005208333333333333` with risk `1.0`.

These results show that the baseline-tuned selective threshold is not portable across intervention-induced score distributions. A1 and its ordered compositions collapse accepted coverage to zero at the fixed operational threshold; B1 accepts all items while retaining near-chance error; most C1/C2 conditions accept none or almost none. This is a development-only cross-property failure mode, not an effect classification or clinical safety result.

## Probability-quality and semantic diagnostics

Raw B1, C1 and C2 seed matrices now have the same seed-specific development calibration tables and 10/15/20-bin semantic-MATCH reliability summaries used for the already-admitted post-processing conditions, together with canonical/transformed NLL, Brier, accuracy and paired semantic JS. No learned seed is pooled before its seed-specific result is preserved.

The result does not change the earlier interpretation: proper-score or calibration-like improvement can coexist with chance-level rule conformance, and low semantic JS can coexist with poor correctness. The full numeric tables are preserved in the canonical JSON rather than compressed into a new headline score.

## Assurance-axis completion status

- P1 canonical decision quality: `MEASURED_DEVELOPMENT`.
- P2 probability calibration: `MEASURED_DEVELOPMENT_DIAGNOSTIC`.
- P3 coherence: `NOT_APPLICABLE_OR_NOT_INSTANTIATED_IN_S1_RULE_ORACLE`.
- P4 semantic stability: `MEASURED_DEVELOPMENT`.
- P5 evidence responsiveness: `NOT_APPLICABLE_OR_NOT_INSTANTIATED_IN_S1_RULE_ORACLE`.
- P6 rule conformance: `MEASURED_DEVELOPMENT_MATCH_MISMATCH_ACCURACY`.
- P7 selective control: `MEASURED_DEVELOPMENT_FIXED_D1_POLICY`.
- P8 capability retention: B1 base backbone unchanged without an empirical retention claim; C2 has the narrow paired SQuAD v1.1 control; C1 remains `NOT_MEASURED_DEVELOPMENT`.

The C1 retention gap is not filled by inference from C2. This result creates no authority to rerun C1 or add a retention model call.

## Scientific boundary

No V5-C01 through V5-C07 empirical claim is promoted. No improve/harm/equivalent label is assigned because native-unit meaningful margins and the frozen confidence procedure are not complete. The result is not clinical validation, broad capability preservation, confirmatory interaction evidence or independent-family replication.

Unchanged-base repeatability R1/R2, final domain floors, meaningful margins, final power, future confirmatory/reserve authority, independent-family replication, publication and merge remain separate gates. PR #320 remains OPEN / DRAFT / UNMERGED.
