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


## Approved answer-interface amendment frontier - 2026-10-03

The Founder prospectively approved the sole terminal marker change from `ANSWER: ` to `ANSWER:\n`; authority is recorded in `V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md`. Protocol sections 1-12 are byte-preserved with an appended section 13. Renderer, preparation checker, and both existing model-facing runner markers now match. No other task, model, optimization or runtime design changed.

Amended preparation is `PASS_PRE_MODEL_INTERFACE`: 64 calculators; 8,192 development/calibration tasks; splits 256 / 3,840 / 256 / 3,840; 16,384 canonical/transformed prompt identities; 32,768 full-prompt A/B candidate checks with zero failures; tokens A=32/B=33; maximum length 593/768; no truncation or overlength. Two affected native regeneration pipelines are byte-identical for all five artifacts; all bound path hashes verify. Selected calculator records, rejection records, task IDs, target counts, partitions and tokenizer-file hashes are unchanged. Source-audit metadata is unchanged because source identities/metadata did not change; only renderer and dependent manifest hashes required regeneration.

The original SAH preparation failure remains byte-unchanged. The failed frozen-space-prefix preparation evidence is byte-preserved at `artifacts/v5/development/s1_task_preparation/frozen-space-prefix-failure-2026-10-03.json`. Earlier failed-interface regeneration/attestation records remain historical evidence of their exact payload; their old hashes are not current amended payload hashes.

Local precommit checks: 97 V5 tests passed; 1,149 full repository tests passed; compile validation and diff whitespace checks passed. Alibaba OCR v1.12.11 (a758d9c) local delegate preview/rules were applied to the exact pending implementation diff, including explicitly supplied tests. Host-agent review found no blocking amendment defect; this is zero-cost host review, not an external model or independent peer review. Jev execution remains `DEFERRED_ZERO_COST_POLICY`.

These are preparation results only. A clean reviewed/pushed head and fresh exact-run preflight are still required before model load. B1/C1/C2 learned qualification, calibration/selective-risk results, meaningful margins and power remain unexecuted at this frontier. Scientific freeze remains OPEN; confirmatory/reserve, paid resources, PHI/private data, replication, HCF/Qwen-Image, publication and merge remain prohibited. PR #320 remains OPEN / DRAFT / UNMERGED.
