# Artifact and evidence traceability


Every empirical table cell must be reconstructible from immutable inputs.

## Required experiment manifest

Each run records: repository commit SHA, dirty-tree status, model repository and revision, tokenizer/processor revision, dataset source and admitted content hash, split/group assignment hash, environment lock, hardware identity, random seed, hyperparameters, command/config, start/end timestamps, raw prediction artifact, metric-script SHA and protocol version.

## Result path

`claim -> table/figure -> analysis artifact -> raw predictions -> run manifest -> code/model/data identities`.

No manually transcribed headline number is accepted without this path.

## Paper linkage

Each manuscript quantitative sentence must reference a result ID. Each result ID lists the affected claim-ledger entries. Development and confirmatory evidence must remain distinguishable in filenames and metadata.

## Literature linkage

Each related-work statement must resolve to a bibliography key and a recorded evidence depth. Abstract-only sources cannot support detailed implementation claims. Preprints must not be silently described as conference publications.

## Privacy and publication

Private Obsidian notes, raw retrieval caches, credentials, local paths and excluded/restricted data are not publication artifacts. Public packets contain only reviewed derived notes, public-source identities/hashes and intended reproducibility materials.

## Local S1 pre-model continuation artifacts

`artifacts/v5/development/s1_task_preparation/` preserves the original `preparation-failure-2026-10-03.json` unchanged and adds:

- `oracle-selection-transition.json`: old/new ordered PMID identities, the single rejection, and deterministic selection changes.
- `model-artifact-reverification.json`: all 12 public model-file hashes, exact revision, full bundle verification, and explicit no-load/no-inference/no-training state; no personal local artifact path is published.
- `task-preparation-evidence.json`: exact generation-context HEAD plus implementation hash, tokenizer hashes/packages, all split counts, prompt lengths, and both failed frozen candidate-token checks.
- `prospective-answer-prefix-metadata.json`: tokenizer-only checks for the frozen marker and proposed alternatives; no proposed interface is admitted by this artifact.

The task-preparation HEAD is generation context. Its implementation hash binds the tested working-tree repair; a later post-commit attestation binds the final payload without circularly hashing itself. The failed task-preparation status is retained in the regenerated scientific-freeze bindings.
