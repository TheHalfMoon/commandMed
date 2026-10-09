# V5 local pre-model host review

Review generation context: `338d0cb5fd3c9ee3131357af24333fd0e80ab4de` plus the implementation/evidence diff. A later post-commit attestation binds the reviewed final payload and file hashes.

Alibaba Open Code Review: installed `v1.12.11 (a758d9c)`, local `delegate preview` and `delegate rule`; no LLM backend or paid API used. Python rules classify correctness/security defects as blocking and style as nonblocking. JSON rules check project-owned key spelling. Test files excluded by preview were resolved explicitly. The reviewer is the host Codex agent; this is not independent peer review or a fabricated external verdict.

## Scope and findings

- Inspected the inherited oracle qualifier, fail-closed bound-rule AST/runtime, strengthened selector, task builder, and qualification/task tests before relying on them.
- Observed a real evidence-persistence defect: the frozen candidate-token checker stopped at label A before writing a failure artifact or checking B/length metadata. Repaired the diagnostic path to preserve both failed checks, exact tokenizer/package/implementation identities, and permitted development/calibration length checks. The invalid-token gate remains failed and returns exit 2. There is no fallback candidate, changed marker, truncation, model call, or silently removed example.
- Checked the regression tests against a retokenized prefix with a single divergent token, empty/multiple continuations, a valid preserved prefix, and main-path failure persistence. Their fixtures do not grant runtime authority.
- Reviewed regeneration of selection/case/quarantine/source-audit bindings and the added approved-authority overlay. The preparation manifest's `execution_authority=NO` states that this artifact cannot grant run authority; its separately bound Founder overlay records the approved development scope. Model execution and training are still unexecuted.
- Mechanically checked all bound path hashes, source/model hashes, ordered identities, deterministic rejection digest, all seven rerun artifacts, and preservation of the original failure. Selection changes are explained by the existing selector, not by performance or manual preference.
- Inspected the metadata-only PubMed audit and clinical review diff. Source screening remains distinct from clinical validity; abstracts are represented only by presence/hash.
- The proposed newline-marker amendment is explicitly unapproved and not applied. The original protocol and rule renderer remain unchanged.
- Empirical claims, training qualification, margins, power, and scientific freeze are not promoted by this work.

No remaining blocking correctness/security defect was identified in the reviewed evidence-persistence repair. A blocking scientific/interface gate remains: both frozen answer-prefix candidate checks fail. Model preflight/load must wait for prospective amendment and repeated pre-model qualification.

Jev: `DEFERRED_ZERO_COST_POLICY`. No compliant local decision backend was established; no remote or paid Jev request or verdict is claimed.


## Approved answer-interface amendment frontier - 2026-10-03

The Founder prospectively approved the sole terminal marker change from `ANSWER: ` to `ANSWER:\n`; authority is recorded in `V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md`. Protocol sections 1-12 are byte-preserved with an appended section 13. Renderer, preparation checker, and both existing model-facing runner markers now match. No other task, model, optimization or runtime design changed.

Amended preparation is `PASS_PRE_MODEL_INTERFACE`: 64 calculators; 8,192 development/calibration tasks; splits 256 / 3,840 / 256 / 3,840; 16,384 canonical/transformed prompt identities; 32,768 full-prompt A/B candidate checks with zero failures; tokens A=32/B=33; maximum length 593/768; no truncation or overlength. Two affected native regeneration pipelines are byte-identical for all five artifacts; all bound path hashes verify. Selected calculator records, rejection records, task IDs, target counts, partitions and tokenizer-file hashes are unchanged. Source-audit metadata is unchanged because source identities/metadata did not change; only renderer and dependent manifest hashes required regeneration.

The original SAH preparation failure remains byte-unchanged. The failed frozen-space-prefix preparation evidence is byte-preserved at `artifacts/v5/development/s1_task_preparation/frozen-space-prefix-failure-2026-10-03.json`. Earlier failed-interface regeneration/attestation records remain historical evidence of their exact payload; their old hashes are not current amended payload hashes.

Local precommit checks: 97 V5 tests passed; 1,149 full repository tests passed; compile validation and diff whitespace checks passed. Alibaba OCR v1.12.11 (a758d9c) local delegate preview/rules were applied to the exact pending implementation diff, including explicitly supplied tests. Host-agent review found no blocking amendment defect; this is zero-cost host review, not an external model or independent peer review. Jev execution remains `DEFERRED_ZERO_COST_POLICY`.

These are preparation results only. A clean reviewed/pushed head and fresh exact-run preflight are still required before model load. B1/C1/C2 learned qualification, calibration/selective-risk results, meaningful margins and power remain unexecuted at this frontier. Scientific freeze remains OPEN; confirmatory/reserve, paid resources, PHI/private data, replication, HCF/Qwen-Image, publication and merge remain prohibited. PR #320 remains OPEN / DRAFT / UNMERGED.
