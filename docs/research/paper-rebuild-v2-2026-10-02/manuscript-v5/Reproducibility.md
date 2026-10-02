# 10. Reproducibility

The final artifact package will record exact repository/model revisions, environment locks, dataset identities and licenses, transformation-generator versions, source-item cluster IDs, prompt templates, decoding settings, calibration splits, training/tuning budgets, random seeds and hardware/resource usage.

Every intervention receives a machine-readable manifest describing its locus, target property, prerequisites, additional parameters, calibration/training access and inference overhead. Every assurance axis receives a metric manifest with direction, unit, threshold, meaningful margin, missing-data rule and code identity.

Confirmatory data are quarantined from development. Accidental exposure is recorded and affected items lose confirmatory status. Repeated access cannot be relabeled as a fresh test.

The publication package should include deterministic fixture tests for all transformation mappings and clinical-rule oracles, plus raw per-source-item evaluation records sufficient to recompute every reported table without rerunning the model where licensing permits.

Negative, null and failed interventions remain in the artifact package. The exact paper tables are generated from versioned analysis code rather than manually transcribed values.
