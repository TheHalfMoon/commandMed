# Claim ledger V5

Status: all scientific claims default to `UNPROVEN` until the frozen confirmatory protocol is executed.

| ID | Prospective claim | Evidence required | Current status |
|---|---|---|---|
| V5-C01 | Reliability properties cannot be safely substituted for one another in the studied medical decision setting. | Formal non-implication witnesses plus empirical cross-property contrasts. | PARTIAL_THEORY_ONLY |
| V5-C02 | At least one targeted reliability intervention materially changes a non-target assurance property. | Paired confirmatory effect with prespecified meaningful margin and multiplicity handling. | UNPROVEN |
| V5-C03 | At least one target-improving intervention harms a noncompensable assurance property. | Replicated harm classification on a hard-gate axis. | UNPROVEN |
| V5-C04 | Conventional compensatory scoring can reverse a deployment conclusion relative to non-compensatory assurance. | Same systems evaluated under both frozen rules with consequential failure traceability. | UNPROVEN |
| V5-C05 | At least one selected intervention pair has a non-additive cross-property interaction. | Preregistered factorial contrast ordered `Gamma[a|b,j]` (plus `Kappa` when both orders are meaningful) with independent-family replication. | UNPROVEN |
| V5-C06 | The main cross-property effect generalizes beyond one backbone family. | Directionally replicated effect on a second independently structured open-weight family. | UNPROVEN |
| V5-C07 | Deterministic rule routing improves exact rule conformance without implying that the underlying rule is clinically valid or that broader medical reliability improved. | Identity-bound rule oracle, same extraction inputs, tool/no-tool contrast, full assurance profile; clinical-validity wording requires separate qualified review. | UNPROVEN |
| V5-C08 | V5 is novel relative to prior medical multi-dimensional evaluation work. | Systematic prior-art search finding no substantially identical controlled intervention matrix design. | CONDITIONALLY_SUPPORTED |

## Pre-model development evidence update

The local execution-coverage repair qualifies 81/82 static calculators and selects exactly 64. This establishes bounded deterministic executability, not clinical validity or support for V5-C02 through V5-C07. All 8192 development/calibration tasks fit the sequence limit, but the frozen answer-token interface fails. No model logits, inference, training losses, calibration results, selective-risk results, margins, or power estimates have been observed. All empirical claim statuses above remain unchanged.


## Approved answer-interface amendment frontier - 2026-10-03

The Founder prospectively approved the sole terminal marker change from `ANSWER: ` to `ANSWER:\n`; authority is recorded in `V5_S1_ANSWER_INTERFACE_AMENDMENT_AUTHORIZATION_2026-10-03.md`. Protocol sections 1-12 are byte-preserved with an appended section 13. Renderer, preparation checker, and both existing model-facing runner markers now match. No other task, model, optimization or runtime design changed.

Amended preparation is `PASS_PRE_MODEL_INTERFACE`: 64 calculators; 8,192 development/calibration tasks; splits 256 / 3,840 / 256 / 3,840; 16,384 canonical/transformed prompt identities; 32,768 full-prompt A/B candidate checks with zero failures; tokens A=32/B=33; maximum length 593/768; no truncation or overlength. Two affected native regeneration pipelines are byte-identical for all five artifacts; all bound path hashes verify. Selected calculator records, rejection records, task IDs, target counts, partitions and tokenizer-file hashes are unchanged. Source-audit metadata is unchanged because source identities/metadata did not change; only renderer and dependent manifest hashes required regeneration.

The original SAH preparation failure remains byte-unchanged. The failed frozen-space-prefix preparation evidence is byte-preserved at `artifacts/v5/development/s1_task_preparation/frozen-space-prefix-failure-2026-10-03.json`. Earlier failed-interface regeneration/attestation records remain historical evidence of their exact payload; their old hashes are not current amended payload hashes.

Local precommit checks: 97 V5 tests passed; 1,149 full repository tests passed; compile validation and diff whitespace checks passed. Alibaba OCR v1.12.11 (a758d9c) local delegate preview/rules were applied to the exact pending implementation diff, including explicitly supplied tests. Host-agent review found no blocking amendment defect; this is zero-cost host review, not an external model or independent peer review. Jev execution remains `DEFERRED_ZERO_COST_POLICY`.

These are preparation results only. A clean reviewed/pushed head and fresh exact-run preflight are still required before model load. B1/C1/C2 learned qualification, calibration/selective-risk results, meaningful margins and power remain unexecuted at this frontier. Scientific freeze remains OPEN; confirmatory/reserve, paid resources, PHI/private data, replication, HCF/Qwen-Image, publication and merge remain prohibited. PR #320 remains OPEN / DRAFT / UNMERGED.
