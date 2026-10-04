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


## Amended S1 exact-run resource stop - 2026-10-04

The amended pre-model gates passed at pushed clean head `47a49e311eff3b820a5bf5ed82aeea776deb83e3` (tree `1a31c41a1f8a176c013074ea8a3a900e42ce4bef`). Fresh exact-head checks passed: 97 V5 tests, 1,149 repository tests, compile and whitespace validation. The 12-file pinned bundle hash remained `b2b4de85ad1149ad987d01e5226c83389fa974fac8d2698bac0e4bdc7e682477`. Exact MODEL_LOAD preflight returned `PREFLIGHT_PASS`, environment hash `4291cc05b189b7b921d130f5810c614e1c033521c99bdf6d00f0e21b18639612`.

The authorized text causal-model path successfully loaded `Qwen3_5ForCausalLM` with 752,393,024 parameters, all bfloat16, on CPU. The unchanged load memory sampler then observed system available memory below the frozen 1.5 GiB limit and the canonical qualifier raised its resource stop. Pre-load available memory was 1,730,498,560 bytes on a 16,888,094,720-byte system; runtime-drive free space was 75,464,032,256 bytes. No inference, benchmark/backward step, optimizer step, B1/C1/C2 execution, calibration or selective-risk analysis occurred. Default post-load requires_grad flags do not mean training occurred or that the frozen adapter scope was qualified.

Evidence is under `artifacts/v5/development/s1-resource-qualification/`: artifact/environment manifests, fresh preflight, exact-run guard, model-load observation, actual failure, exact-run test logs/validation, observational harness source/hash, and `resource-blocker-evidence-2026-10-04.json`. Personal traceback paths alone were redacted from the publication payload; original raw evidence is retained locally with its hash. The existing exception path discarded the numeric load minimum/peak and load duration; only the measured below-threshold relation is supported. No missing memory/time measurements are invented and no reload was performed to reconstruct them.

Current gate: `RESOURCE_BLOCKED_MODEL_LOAD_MEMORY_HEADROOM`. Restore sufficient local free memory before an identical run with fresh exact-head artifact/environment/preflight gates. Existing authority permits that identical run after the external resource condition changes; it does not permit lower precision, alternate model/runtime, expanded limits, paid resources or relaxed stop thresholds. Full training feasibility remains unmeasured. Scientific freeze remains OPEN, empirical claims remain unsupported, and PR #320 remains OPEN / DRAFT / UNMERGED. Both earlier SAH and space-prefix negative results remain preserved. No confirmatory/reserve, PHI/gated/private data, replication, HCF/Qwen-Image, paid API/compute, publication or merge occurred.

## Fresh C1 runtime assignment stop - 2026-10-04

The retained baseline/B1 completion record establishes full development matrices for baseline and B1 seeds 11/29/47, with a negative B1 reliability result; it does not support the confirmatory empirical claims above. See `V5_S1_B1_DEVELOPMENT_RESULTS_2026-10-04.md` for the original outcomes and evidence identities. No baseline/B1 rerun or retuning occurred in this continuation.

One normal fresh Colab connection request for C1 seed 11 failed at GPU assignment due to current usage limits. No fresh accelerator, duration projection or PREFLIGHT_PASS was obtained and no C1/C2 model call or optimization began. See `V5_S1_C1_FRESH_RUNTIME_GPU_BLOCKER_2026-10-04.md` and its durable UI evidence. The historical duration stop remains preserved separately. All claim statuses remain unchanged; no C1/C2 effect, retention preservation, clinical validity or V5 success is supported by this resource observation. Existing bounded authority and the frozen scientific design remain unchanged.

## Existing Google AI Pro entitlement observation - 2026-10-04

The current signed-in account visibly showed Google AI Pro membership, while Colab reported no recognized subscription and zero compute units. One additional ordinary fresh allocation request, in this distinct entitlement-check cycle, was rejected by the GPU usage-limit dialog. No account switching or purchase occurred, and no fresh runtime, preflight, duration admission or model call was reached. The discrepancy's cause and any reset time remain unknown. Help -> Send feedback was drafted but not submitted because the visible notice automatically included account metadata without a visible exclusion control. See `V5_S1_GOOGLE_AI_PRO_ENTITLEMENT_BLOCKER_2026-10-04.md` and its allowlisted durable evidence. All scientific claims, frozen settings, completed baseline/B1 results and prior failures remain unchanged. C1 seed 11 remains NOT_STARTED; scientific freeze remains OPEN.
