# Prospective statistical protocol


Status: DRAFT; numeric margins and sample sizes remain intentionally UNFROZEN until lawful development evidence and qualified review exist.

## Estimands

The primary estimand is the paired difference in decision NLL between matched readout/adaptation cells on a quarantined confirmatory set. Co-primary interpretation includes retained-capability change so a decision improvement cannot be presented without its competence cost.

## Pairing and uncertainty

Use paired item-level analysis whenever predictions are produced on the same items. Report effect sizes with confidence intervals. For binary correctness, use paired methods such as McNemar where assumptions fit; for continuous/proper scores, use paired bootstrap intervals or an explicitly justified alternative. Bootstrap design must preserve grouping when examples share source documents or cases [@arxiv170604599].

## Multiplicity

Freeze one primary contrast before confirmatory evaluation. Secondary contrasts are labeled and controlled with a declared family-wise or false-discovery procedure. Exploratory analyses remain exploratory.

## Calibration

NLL and Brier are proper scoring-rule endpoints; reliability diagrams and calibration error summaries are diagnostics, not substitutes [@arxiv170604599]. Risk-coverage/AURC is evaluated independently from calibration [@arxiv190109192]. Distribution-shift conclusions require explicit shift strata [@arxiv190602530].

## Equivalence and noninferiority

No equivalence or noninferiority margin is invented from literature. Any margin must be clinically/scientifically justified before confirmatory access, with direction, scale and consequence documented. Failing to reject a difference is not evidence of equivalence.

## Seeds and tuning budget

Seed count, development budget and baseline tuning budget must be identical or explicitly resource-matched. Report all preregistered seeds, not only the best run.

## Confirmatory quarantine

The final test set is accessed only after architecture, metrics, hyperparameter-selection rule and analysis code are frozen. Repeated access converts the set to development evidence and must be recorded.
