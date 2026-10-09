# V5 native-unit domain-floor freeze — 2026-10-09

Status: `FROZEN_PROSPECTIVELY_BEFORE_REPEATABILITY_OUTPUT`

Authority: the Founder-authorized development program explicitly permits freezing property-specific meaningful margins and power assumptions from development-only evidence. At this freeze point, unchanged-base repeatability R1 is still RUNNING and no R1 output has been retrieved or inspected.

Machine-readable binding: `artifacts/v5/development/domain-floor-freeze-2026-10-09/domain-floors.json`.

## Decision

For the four primary metrics already bound by the unchanged-base repeatability method, adopt a transparent **non-clinical research-scale minimum effect**. These values are study-defined benchmark-scale floors, not claims of universal clinical importance.

| Metric | Frozen domain floor | Interpretation |
| --- | ---: | --- |
| canonical accuracy | `0.01` | one absolute percentage point; about 41 of 4,096 planned source clusters |
| canonical NLL | `0.009950330853168092` nats | `ln(1.01)`, about a one-percent multiplicative change in geometric-mean target probability |
| canonical two-class Brier | `0.02` | one percent of the implemented `[0,2]` mathematical range |
| semantic JS | `0.006931471805599453` nats | `ln(2)/100`, one percent of the binary Jensen-Shannon mathematical maximum |

The final meaningful margin remains exactly:

`m_j = max(domain_floor_j, 2 * repeatability95_j)`.

No final `m_j` is known until both frozen unchanged-base repeats are durable and the prospectively frozen repeatability estimator is applied.

## Why this route is adopted

The preceding evidence review found no defensible universal clinical cutoff that could simply be imported for NLL, Brier, calibration or Jensen-Shannon divergence. Calibration measurement depends on the chosen construct; Brier score does not encode clinical utility by itself; and noninferiority margins require prespecified statistical plus substantive reasoning.

The primary V5 RULE_ORACLE construct is methodological rule conformance rather than current-care clinical validity. A benchmark-scale floor is therefore appropriate only if it is labeled as such. The one-percent scale convention is simple, metric-interpretable, independent of the observed intervention ranking, and fixed before repeatability output is seen.

This choice deliberately does **not** imply that a one-percent metric change is clinically important. Any future current-care clinical-validity claim would require separate qualified clinical review and could require different margins.

## Anti-contamination statement

These values were not selected to make B1, C1, C2, A1, A2, D1 or any ordered composition pass or fail. The observed development effect sizes were not used to tune the floors. The domain floors will not be weakened if the planned 4,096-cluster design later fails the power gate.

## Scope

This freeze covers only the four primary repeatability metrics:

- `canonical_accuracy`;
- `canonical_nll`;
- `canonical_brier`;
- `semantic_js`.

It does not silently create margins for selective-risk/coverage, SQuAD retention, coherence, evidence responsiveness, clinical utility or any currently undefined/not-applicable S1 property. Those constructs require their own already-frozen target/threshold or a separate prospective decision if they enter a future confirmatory primary family.

## Preserved boundaries

No confirmatory/reserve identity is materialized. No confirmatory/replication execution, paid API/compute, PHI, gated/private clinical data, publication or PR merge is authorized. PR #320 remains OPEN / DRAFT / UNMERGED.
