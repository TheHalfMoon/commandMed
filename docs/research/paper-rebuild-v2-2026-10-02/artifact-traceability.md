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
