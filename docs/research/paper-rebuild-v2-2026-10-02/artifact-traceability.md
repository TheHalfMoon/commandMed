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


## Amended S1 exact-run resource stop - 2026-10-04

The amended pre-model gates passed at pushed clean head `47a49e311eff3b820a5bf5ed82aeea776deb83e3` (tree `1a31c41a1f8a176c013074ea8a3a900e42ce4bef`). Fresh exact-head checks passed: 97 V5 tests, 1,149 repository tests, compile and whitespace validation. The 12-file pinned bundle hash remained `b2b4de85ad1149ad987d01e5226c83389fa974fac8d2698bac0e4bdc7e682477`. Exact MODEL_LOAD preflight returned `PREFLIGHT_PASS`, environment hash `4291cc05b189b7b921d130f5810c614e1c033521c99bdf6d00f0e21b18639612`.

The authorized text causal-model path successfully loaded `Qwen3_5ForCausalLM` with 752,393,024 parameters, all bfloat16, on CPU. The unchanged load memory sampler then observed system available memory below the frozen 1.5 GiB limit and the canonical qualifier raised its resource stop. Pre-load available memory was 1,730,498,560 bytes on a 16,888,094,720-byte system; runtime-drive free space was 75,464,032,256 bytes. No inference, benchmark/backward step, optimizer step, B1/C1/C2 execution, calibration or selective-risk analysis occurred. Default post-load requires_grad flags do not mean training occurred or that the frozen adapter scope was qualified.

Evidence is under `artifacts/v5/development/s1-resource-qualification/`: artifact/environment manifests, fresh preflight, exact-run guard, model-load observation, actual failure, exact-run test logs/validation, observational harness source/hash, and `resource-blocker-evidence-2026-10-04.json`. Personal traceback paths alone were redacted from the publication payload; original raw evidence is retained locally with its hash. The existing exception path discarded the numeric load minimum/peak and load duration; only the measured below-threshold relation is supported. No missing memory/time measurements are invented and no reload was performed to reconstruct them.

Current gate: `RESOURCE_BLOCKED_MODEL_LOAD_MEMORY_HEADROOM`. Restore sufficient local free memory before an identical run with fresh exact-head artifact/environment/preflight gates. Existing authority permits that identical run after the external resource condition changes; it does not permit lower precision, alternate model/runtime, expanded limits, paid resources or relaxed stop thresholds. Full training feasibility remains unmeasured. Scientific freeze remains OPEN, empirical claims remain unsupported, and PR #320 remains OPEN / DRAFT / UNMERGED. Both earlier SAH and space-prefix negative results remain preserved. No confirmatory/reserve, PHI/gated/private data, replication, HCF/Qwen-Image, paid API/compute, publication or merge occurred.


## Prospective Colab runtime path - 2026-10-04

Authority sources: `V5_S1_COLAB_FREE_RUNTIME_AUTHORIZATION_SOURCE_2026-10-04.md`, `V5_S1_EXISTING_COLAB_PRO_AUTHORIZATION_2026-10-04.md`, and subsequent `V5_S1_FREE_COLAB_SELECTION_2026-10-04.md`; protocol sections 14-15 append the placement/cost change only. Prospective implementation: `scripts/v5_s1_colab_qualification.py`; notebook template: `notebooks/v5_s1_colab_resource_qualification.ipynb`. Preliminary metadata and primitive capability observations: `artifacts/v5/development/s1-colab-resource-qualification/pre-model-preparation-2026-10-04/`. This is not model execution or resource qualification evidence. Old CPU bindings are historical to their recorded code head and are never rewritten to match a later protocol.

## Measured Colab resources and prospective complete B1 stage - 2026-10-04

Measured run head: `3347cf564999cabc1b55bff49c8dfdfeba431106`. Original resource ZIP, console, environment, preflights, model/LoRA identities, full preparation, timing/projection and separate durability receipt: `artifacts/v5/development/s1-colab-resource-qualification/resource-measured-2026-10-04/`. Exact-run local tests passed 119 V5 / 1,171 repository tests, and deterministic task/binding reproduction and zero-cost OCR-rule host review passed. See `V5_S1_COLAB_RESOURCE_MEASUREMENTS_2026-10-04.md`; no medical training or scientific metric is claimed from that run.

New prospective bindings cover `scripts/v5_s1_b1_development.py`, `scripts/v5_s1_retention_preparation.py`, `src/commandmed/reliability_v5/retention_dataset.py`, and `V5_S1_MODEL_INTEGRATION_FREEZE_2026-10-04.md`. The exact pinned public validation file was acquired separately in Colab without model execution; source SHA is recorded in the metadata implementation. No SQuAD payload is committed. Full B1 and C1/C2 execution remain separately gated, and the medical interface/data/budgets are unchanged.


## Prospective atomic adapter integration - 2026-10-04

The complete baseline/B1 stage is executing normally at exact reviewed head `848692336c2b8537ee4d559338abed29da0c93d6`; no complete matrix or B1 seed is accepted at this record boundary. The predecessor resource evidence remains durable. Prospective `v5_s1_adapter_development.py` implements one complete C1/C2 seed under unchanged S1 identities, dtype, budgets and fresh preflight. Its companion freeze records canonical medical ordering, two ranked maintenance anchors per accumulation group (all 64 once over 32 updates), unchanged teacher-KL/greedy QA contract, resource-only C2 backward without updates, and atomic duration/export admission. No medical C1/C2 optimization or SQuAD model output preceded this implementation.

Model-free payload validation: 156 V5 tests and 1,208 repository tests pass; script/test compile, nbformat/cell compilation, whitespace and two byte-identical freeze-binding regenerations pass. Objective tests compare with the independently implemented frozen scalar JS/KL oracles, including zeros/extreme probabilities and semantic label permutation; resource tests ensure early EOS cannot underestimate the full 32-token cost. Local validation never loads weights. Actual GPU backward/full C2 execution remain separately gated. Prospective logs and payload hashes are in `artifacts/v5/development/s1-colab-resource-qualification/adapter-prospective-validation-2026-10-04/`. Exact committed-head review remains required before this adapter source executes. All prior negative results and original evidence bytes remain unchanged. No cost, holdout, publication or merge authority is expanded.


## Complete baseline/B1 durability and next-stage duration stop - 2026-10-04

Run source `848692336c2b8537ee4d559338abed29da0c93d6`: baseline plus B1 seeds 11/29/47 each have all 16,384 paired development/calibration prompts. Exact-byte original ZIP `7e6e21ed73d8b672b4cf6836cc199f3450a02fb5ad0ea1d3b157009a431ed913`, original console, raw records, model-free identity/metric reconstruction and separate durability receipt are preserved under `s1-colab-resource-qualification/b1-complete-2026-10-04/`. Original flags and historical negative evidence are unchanged. See `V5_S1_B1_DEVELOPMENT_RESULTS_2026-10-04.md`.

The next C1/C2 atomic-seed admission stopped prospectively at `COLAB_RUNTIME_DURATION_BLOCKER`, before any next-stage model load or SQuAD model call. No incremental spend or session-limit bypass occurred. The prospective adapter source `625bbe7cd4d162d2cd6e6157e3f52c8b0f8c72eb` passed 156 V5 / 1,208 repository tests and exact-head zero-cost host-agent OCR-rules review; no external verdict is claimed. PR #320 remains OPEN / DRAFT / UNMERGED.
