# V5 S1 final development-only cross-seed synthesis — 2026-10-09

Status: `COMPLETE_DEVELOPMENT_SYNTHESIS; NOT_CONFIRMATORY`

All three learned-intervention seeds 11, 29 and 47 are now durable for B1, C1 and C2. This synthesis reads only the already-reviewed development/calibration evidence and the narrow C2 SQuAD retention aggregates. It does not fit or select a model, threshold, calibration map, margin, or confirmatory identity.

## Learned-intervention summary

| Intervention | DEV canonical accuracy mean | DEV transformed accuracy mean | DEV canonical NLL mean | DEV transformed NLL mean | DEV semantic JS mean |
| --- | ---: | ---: | ---: | ---: | ---: |
| B1_TYPED_V1 | 0.4937500000000001 | 0.4937500000000001 | 104.83207465277776 | 105.0036892361111 | -4.647727942735951e-67 |
| C1_CRDI_V1 | 0.4875868055555556 | 0.4848958333333333 | 0.732595954195257 | 0.7275310719972197 | 0.001296562044407901 |
| C2_CRDI_RETAIN_V1 | 0.4848958333333333 | 0.4848958333333333 | 0.7415694349926284 | 0.7353233790562109 | 0.0013634747513634378 |

B1 is a strong negative development result: the typed heads remain near chance in accuracy while their NLL is extremely poor and unstable across seeds. C1 and C2 also remain near chance on rule-conformance accuracy. Their small semantic-JS values do not establish correct rule conformance, calibration, clinical validity, or broad reliability.

For C2's narrow SQuAD v1.1 retention control, baseline EM is 0.1953125 and candidate EM is 0.1953125 across all three seeds. Baseline token F1 is 0.31273046371355107; candidate token F1 mean is 0.3130283366275481. The paired token-F1 delta mean is 0.00029787291399702154, with seed values {'11': -0.0032335893273393035, '29': -0.003253404282499095, '47': 0.007380612351829463}. This narrow control is not evidence of general capability preservation.

## Training-randomness nuisance summary

The synthesis reports the sample standard deviation across the three trained seeds for each learned metric. For example, C2 DEV canonical accuracy between-seed SD is 0.007672354095133468, C2 DEV canonical NLL SD is 0.03165483254032418, and C2 retention token-F1 delta SD is 0.006133840282912676.

These between-training-seed SD values are descriptive nuisance quantities only. They are **not** unchanged-base `repeatability95_j`, meaningful-effect margins, confidence intervals, p-values, or confirmatory estimates.

## Scientific boundary

No V5-C01 through V5-C07 empirical claim is promoted by this development synthesis. The current evidence is sufficient to preserve negative and mixed development behavior and to motivate the remaining prospective gates, but not to support equivalence, noninferiority, calibration, selective-control, cross-property interaction, replication, or clinical-validity claims.

The next scientific gates remain:

- unchanged-base repeatability under an explicitly authorized and prospectively frozen repeatability method;
- explicit calibration and selective-control conventions;
- justified native-unit domain floors and final `m_j = max(domain_floor_j, 2 * repeatability95_j)`;
- final MDE/power planning at alpha 0.05 with Holm control and desired power 0.90;
- only after those gates, any future separately authorized confirmatory identity materialization/execution.

PR #320 remains OPEN / DRAFT / UNMERGED. Confirmatory/reserve execution, publication and merge remain unauthorized.
