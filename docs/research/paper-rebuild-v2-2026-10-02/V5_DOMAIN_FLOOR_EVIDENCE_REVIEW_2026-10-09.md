# V5 native-unit domain-floor evidence review — 2026-10-09

Status: `EVIDENCE_REVIEW_COMPLETE; NUMERIC_DOMAIN_FLOORS_NOT_FROZEN`

This review narrows the remaining V5 meaningful-margin decision without using confirmatory/reserve outputs. It does not select a numeric domain floor.

## Evidence reviewed

1. Huang et al., *Journal of the American Medical Informatics Association* 2020, DOI `10.1093/jamia/ocz228`, describe multiple calibration measurements and emphasize that calibration assessment has no single universally best measurement; calibration diagnostics answer different questions and must be interpreted with their construction and use case.
2. Assel, Sjoberg and Vickers, *Diagnostic and Prognostic Research* 2017, DOI `10.1186/s41512-017-0020-3`, show that the Brier score is a proper scoring rule but does not itself encode clinical utility; a raw Brier difference therefore cannot be assigned a universal clinical-importance cutoff.
3. Althunian et al., *British Journal of Clinical Pharmacology* 2017, DOI `10.1111/bcp.13280`, review noninferiority-margin selection and emphasize that a margin requires prespecified statistical reasoning together with context-specific substantive judgment rather than being inferred from a nonsignificant result.
4. The existing V5 protocol already separates proper scores, calibration diagnostics, rule conformance, semantic stability, selective risk/coverage and clinical utility. Current-care clinical-validity interpretation is explicitly outside the primary RULE_ORACLE construct.

Together these sources support the existing fail-closed rule: no universal published cutoff can be imported as a clinically meaningful NLL, Brier, calibration-gap or Jensen-Shannon threshold for this benchmark.

## Measurement-scale facts that are safe to use

The following are mathematical scale facts, not meaningful-effect decisions:

- canonical accuracy is in `[0,1]`;
- the implemented two-class multiclass Brier score is in `[0,2]`;
- semantic Jensen-Shannon divergence using natural logarithms is in `[0, ln(2)]`;
- NLL is in `[0, +infinity)` and an additive NLL difference `d` corresponds to a multiplicative factor `exp(d)` in geometric-mean target probability;
- the planned RULE_ORACLE confirmatory sample contains 4,096 source clusters, so one absolute percentage point in accuracy corresponds to about 41 source-cluster decisions.

These facts can explain a study-defined benchmark-scale floor, but they do not prove that any particular percentage is substantively meaningful.

## Candidate research-scale convention — NOT FROZEN

A transparent non-clinical candidate, if the Founder and methodological reviewer decide that a benchmark-scale rather than clinical margin is appropriate, is:

- canonical accuracy: `0.01` absolute;
- canonical NLL: `ln(1.01) = 0.009950330853168092` nats, representing about a one-percent multiplicative change in geometric-mean target probability;
- canonical two-class Brier: `0.02`, equal to one percent of its implemented `[0,2]` range;
- semantic JS: `ln(2)/100 = 0.006931471805599453`, equal to one percent of its mathematical range.

This candidate is deliberately derived from measurement scale and not from observed intervention rankings. It is **not** claimed to be a clinical tolerance, a literature-standard cutoff, or an approved V5 margin. It must not enter `m_j` until a prospective decision explicitly freezes it (or replaces it) before confirmatory identity materialization.

## Why automatic freezing is not justified

The development results already show that calibration-like scores can improve while rule-conformance accuracy remains near chance, and D1 can satisfy its tiny tuning subset while failing to transport. Choosing floors to make those observed effects look important, negligible or equivalent would be post-hoc contamination.

The remaining choice is therefore substantive:

- **benchmark-scale route:** explicitly adopt a transparent research-scale convention such as the candidate above, stating that it is methodological and not clinical; or
- **qualified-judgment route:** obtain a statistician/clinical-methodology panel decision for property-specific floors, especially if the paper intends stronger applied/clinical language.

No value should be selected merely because it makes the planned 4,096-cluster design pass power.

## Gate state

```text
DOMAIN_FLOOR_EVIDENCE_REVIEW=COMPLETE
UNIVERSAL_LITERATURE_CUTOFF_FOUND=NO
CANDIDATE_RESEARCH_SCALE_CONVENTION=DOCUMENTED_NOT_FROZEN
NUMERIC_DOMAIN_FLOORS_FROZEN=NO
NUMERIC_MEANINGFUL_MARGINS_FROZEN=NO
CONFIRMATORY_IDENTITY_MATERIALIZATION=NO
CONFIRMATORY_EXECUTION=NO
```

The final margin gate remains `m_j = max(domain_floor_j, 2 * repeatability95_j)`. Repeatability R1/R2 remains independently frozen and must complete before final margins/power can be computed.
