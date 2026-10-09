# V5 S1 Colab artifact ordering failure - 2026-10-04

Status: `PRE_MODEL_ARTIFACT_BINDING_FAILURE_PRESERVED`.

The first Colab resource candidate at reviewed/pushed head `1b2571dc457cb4d2cd40e8b0cb25d16e34b5783e` stopped on `EXACT_12_FILE_BUNDLE_MISMATCH`, before task qualification, model-load preflight, model load, inference or optimization. Its original ZIP, JSON records and exact export checksum are preserved under `artifacts/v5/development/s1-colab-resource-qualification/artifact-order-failure-2026-10-04/`.

Metadata-only diagnosis verified that all 12 filenames, sizes and individual SHA-256 digests match the frozen artifact exactly. POSIX `Path` sorting placed uppercase `LICENSE`/`README.md` earlier than Windows sorting. The POSIX-order aggregate was `64911e5a2bfd62ad10d43f50c0f8fbfa4acfed3b85071f949f27abf70058f99f`; reproducing the already-bound file order exactly restores the unchanged frozen bundle `b2b4de85ad1149ad987d01e5226c83389fa974fac8d2698bac0e4bdc7e682477`.

The prospective Colab binder now first requires exact equality of every file record against the frozen manifest, then hashes records in that manifest's order. Missing, extra, duplicated, renamed, resized or content-changed files still stop. The historical CPU binder and evidence remain untouched. This is a platform-independent reproduction repair; no model/tokenizer artifact, dtype, prompt, task, source, intervention, optimizer, budget or scientific design is amended.

Repeat tests, compile, deterministic regeneration and exact-head/OCR review, commit/push, then start a new candidate boundary with fresh complete Colab preparation and exact-run preflight. The preserved failure remains valid operational evidence. It is not a model or scientific result. All prior negative evidence and prohibitions remain binding; PR #320 remains OPEN / DRAFT / UNMERGED.
