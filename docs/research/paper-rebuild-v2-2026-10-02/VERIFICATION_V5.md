# Verification record V5

Date: 2026-10-02. Scope: documentation/research packet only. No model inference, model download, training, clinical data access, paid compute, paid API, or empirical paper result occurred.

## Repository invariants

- Branch before publication: `research/commandmed-paper-first-principles`.
- Base/canonical main after fresh `git fetch origin --prune`: `51f73ec05750137e5bd94ffa0765f6383f475fee`.
- Local branch and `origin/main` divergence before staging: `0 / 0`.
- Historical tracked-file diff before staging: zero; all paper-rebuild work is additive under the named docs/spec directories.

## Static validation

- UTF-8 text normalized without BOM in the new packet.
- 9 JSON artifacts parsed successfully.
- 92 unique BibTeX keys across the packet bibliography files; zero duplicate keys.
- Manuscript V5 referenced 17 citation keys; zero missing bibliography keys.
- Required V5 protocol/manuscript files present; `Results.md` explicitly contains no empirical results.
- No ambiguous `Gamma[a,b,j]`, `I_ab(f)`, or scientific `off-diagonal` shorthand remains in V5 scientific files; ordered composition uses `Gamma[a|b,j]` and optional `Kappa`.
- Privacy/secret scan found no local user paths, email addresses, token patterns, PHI markers, or private-source payload markers in the publication packet.
## Test and review-tool evidence

- Existing repository test suite: `1052 passed in 30.36s` using `python -m pytest -q` on the unchanged codebase plus untracked documentation packet.
- Alibaba Open Code Review: local `open-code-review v1.12.11 (a758d9c)` verified. `ocr delegate preview` identified 9 reviewable JSON files out of 84 packet files; Markdown/BibTeX were explicitly excluded as unsupported extensions. `ocr delegate rule` resolved the JSON rule to check project-owned JSON-key spelling. A host-agent inspection of the 245 unique JSON keys found no clear project-owned spelling defect; upstream/external key names and path-identity keys were preserved rather than normalized.
- Jev: local wrapper `jev 0.3.2` verified from the local agent-skill installation. Its configured providers are remote TypeSafe/OpenRouter services; no Jev decision/review request was executed because the project forbids introducing paid API cost. No Jev review result is claimed.
- Scite MCP was not used for qualification after it reported that MCP access requires a paid plan or trial. Public/free literature sources were used instead.

## Scientific state after verification

V5 remains `PRIMARY_PAPER_SELECTED_CONDITIONALLY`, `NOVELTY_NOT_CLEARED_FOR_FIRST_CLAIMS`, `SCIENTIFIC_FREEZE_OPEN`, and `EXECUTION_NOT_AUTHORIZED`. Static verification does not promote any scientific claim.
## 2026-10-03 implementation and freeze-candidate update

- The V5 deterministic/mechanical intervention layer is implemented for `A1_TS_V1`, `A2_SELBIAS_V1`, `D1_DEFER_V1`, and `D2_RULETOOL_V1`. `B1_TYPED_V1`, `C1_CRDI_V1`, and `C2_CRDI_RETAIN_V1` now have project-owned pure-math objective mechanics marked `OBJECTIVE_MECHANICS_IMPLEMENTED`; model integration, optimization, training, inference, and execution authority remain `NO`.
- The hardened RiskCalcs selector admits only statically parsed Boolean/numeric-threshold rules with no string domains, input arithmetic/calls/subscripts/attributes, at most eight inputs, and prospective generated input space of at least `1024` states.
- `82` calculators pass that hardened static gate across `15` first-listed source specialty strata; `64` are selected by deterministic domain-balanced round-robin before model outputs. All `64/64` selected PMIDs resolve in PubMed, all expose abstracts in the current audit, and `0` carry a retraction/withdrawal publication-type flag. This is source/provenance screening, not current-care clinical qualification.
- RULE_ORACLE no longer pre-materializes a 256-case universe. Each selected calculator has at least `1024` candidate states; only `64` development and `64` calibration states are fixed before model work.
- Before model work, `4,096` development and `4,096` calibration case identities are committed. No confirmatory or reserve identity is materialized; after the clean freeze event the future beacon selects `4,096` confirmatory and `4,096` reserve states from the still-unselected candidate spaces.
- The frozen quarantine procedure uses the first valid future NIST Beacon 2.0 pulse after the clean freeze event to select confirmatory/reserve states; it does not merely relabel a pre-known holdout pool.
- `rajpurkar/squad@7b6d24c440a36b6815f21b70d25016731768db1f` is admitted only as a narrow paired nonmedical extractive-QA retention control; source payload is not vendored and broad capability-preservation claims remain forbidden.
- `rule-oracle-case-index-v5.json` binds development/calibration identities only; future confirmatory and reserve identities are deliberately absent until the public-randomness event.
- V5-focused tests on the final reviewed worktree after quarantine/contract hardening: `60 passed in 0.49s`.
- Full repository tests on the final reviewed worktree after quarantine/contract hardening: `1112 passed in 24.27s`.
- `python -m compileall` passed for the V5 implementation, freeze tools, and tests.
- The rule-oracle/source-audit/freeze-binding generation pipeline was executed twice after the final schema changes; all five generated artifacts were byte-identical across reruns and `git diff --check` reported zero lines.
- For the selected-calculator source audit, fetched PubMed abstract text is used only transiently to record presence and SHA-256 identity; no fetched abstract body or upstream RiskCalcs interpretation narrative is persisted in `clinical-source-audit-v5.json` or `clinical-source-review-v5.md`.
- The specialty balancing field is explicitly an internal **first-listed source specialty stratum**; it does not claim that the upstream source declares a primary clinical specialty or that the strata estimate prevalence.
- Ruff is not installed on this host; no Ruff result is claimed and no package was installed merely to obtain one.
- Alibaba Open Code Review `v1.12.11 (a758d9c)` was run in zero-cost delegation mode. `ocr delegate preview` and `ocr delegate rule` resolved the Python review policy for the V5 code/freeze tools/tests. Host-agent review under those rules identified a fail-closed contract inconsistency for malformed exclusion/state-index inputs; the code was repaired to raise `ReliabilityContractError` consistently, regression tests were added, and the final reviewed state has no known blocking correctness/security defect. OCR's own default-path policy excluded test files from preview, so tests were supplied explicitly to `ocr delegate rule` and inspected with the same Python rule.
- Jev remains `DEFERRED_ZERO_COST_POLICY`; no paid Jev call is claimed.

## Literature refresh

A new bounded adversarial refresh is recorded in `literature-refresh-v5-2026-10-03.md`. MedHELM, CSEDB, the EMNLP trustworthy-medical-QA survey, Gu et al. on probabilistic medical predictions, Boie et al. on medical confidence calibration, Matta et al. on calibration versus probabilistic validity, CURA, and CALIN further narrow the paper. The refresh does not clear a `first` claim. The surviving candidate gap is the matched intervention-to-assurance causal effect matrix with preregistered ordered interactions, exact rule-oracle cases, noncompensatory decision logic, and independent-family replication.

## 2026-10-03 default-deny development preflight update

- Added `src/commandmed/reliability_v5/preflight.py` and dedicated regression tests.
- The validator requires the exact pinned Qwen3.5-0.8B repository/revision, a model-artifact SHA-256, a 40-hex code SHA, admitted development/calibration roles, zero paid resource/spend declarations, and nonempty environment/output identities.
- Training is restricted mechanically to B1/C1/C2; SQuAD retention is restricted to C2. Confirmatory/reserve materialization, PHI, gated data, and paid resources fail closed.
- The default authority object remains denied. Passing synthetic fixtures test contract mechanics only and do not grant founder authority or permit a real model call.
- Final V5-focused suite after preflight hardening: `71 passed in 0.65s`; full repository suite: `1123 passed in 23.29s`; V5 compileall and `git diff --check` passed.
- Alibaba Open Code Review `v1.12.11` delegation rules were applied to the changed Python files. Host-agent review found an inference-path scope weakness (unknown intervention IDs were not rejected) and weak environment/output identity validation; both were repaired before the final test run. The final validator now rejects unknown intervention IDs, non-hash environment identities, and output traversal/out-of-scope destinations.
- Jev remains `DEFERRED_ZERO_COST_POLICY`; no Jev API call was made.

## 2026-10-03 statistical-mechanics update

- Added project-owned paired source-cluster mean effects, deterministic paired bootstrap intervals, Holm-adjusted p-values, and normal-approximation MDE/required-cluster planning helpers.
- The bootstrap preserves source-item pairing and uses a fixed seed; its percentile interval is conservatively widened only when necessary to satisfy the shared `EffectInterval` requirement that the observed estimate lie inside the interval.
- Power helpers are explicitly planning approximations. They do not choose `m_j`, prove endpoint-specific power, or replace the post-pilot frozen power calculation.
- Alibaba Open Code Review delegation rules were applied to the statistics implementation/tests. Host-agent review identified the finite-sample percentile/point-estimate contract edge case before publication; it was repaired and documented.
- Final V5-focused suite after statistics hardening: `80 passed in 0.71s`; full repository suite: `1132 passed in 24.20s`; compileall and `git diff --check` passed.
- No model execution, dataset payload access, confirmatory access, paid API, or paid compute occurred.

## Local pre-model continuation verification

Generation-context HEAD: `338d0cb5fd3c9ee3131357af24333fd0e80ab4de`. This section describes the reviewed working-tree repair; the successor post-commit attestation binds its final payload SHA/tree. Earlier counts and authority-denied statements above remain historical.

- Fetched live origin and safely fast-forwarded the clean existing clone by 19 remote-only commits; no local-only commits, stashes, or additional research worktrees were present. Canonical main remains `51f73ec05750137e5bd94ffa0765f6383f475fee`; PR #320 was verified open/draft.
- Initial current-HEAD V5 suite: `90 passed in 1.32s`.
- Strengthened selector: `82` static candidates, `81` execution-qualified, `1` execution-rejected, exactly `64` selected. Rejection digest: `470e039d9a9f1362f93c7eafd56a32c0cac4e612c8b9e765a440ee0d37a8a83d`.
- The prospective loop rejects SAH PMID 24103667 at development state 248 on unbound `age_score`; the historical preparation failure on unbound `gcs_score` remains byte-unchanged. No upstream code or generated state was repaired, skipped, clamped, or deleted.
- Regenerated the selection-dependent case index, quarantine commitments, live PubMed source audit/review, and freeze bindings. A transitional suite correctly detected the not-yet-regenerated state-space binding (`1 failed, 93 passed`); completing native binding regeneration resolved that mismatch without changing the test or gate.
- Current source audit: `64/64` identities resolve and expose abstracts; `0` publication-type retraction/withdrawal flags. Abstract bodies were not persisted. No broader no-retraction or clinical-validity claim is made.
- All `8192` S1 tasks materialize with exact split counts `256/3840/256/3840`. Maximum prompt length is `593`; no overlength or truncation. Task preparation deliberately returns failure because both frozen answer-prefix candidate-token checks fail.
- Enhanced preparation now persists both failed token checks and completes permitted metadata checks before returning failure. It does not adopt another answer marker, substitute token IDs, or call a model. Regression checks cover prefix retokenization, zero/multiple continuation tokens, valid continuation tokens, and failure evidence persistence.
- Final V5 suite after the evidence repair: `95 passed in 0.65s`; full repository suite: `1147 passed in 18.05s`.
- Two complete repository-native regeneration pipelines produce `PASS_7_OF_7_BYTE_IDENTICAL`; all bound path hashes verify. Expected task-preparation exit `2` occurs on both reruns and remains a failed gate.
- Recomputed all `12` local artifact-file hashes without download. Full model bundle matches `b2b4de85ad1149ad987d01e5226c83389fa974fac8d2698bac0e4bdc7e682477`; RiskCalcs source matches `00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9`.
- Existing D-drive execution runtime lacks pytest. Pytest `8.4.2` was installed in a separate local validation directory outside the clone and injected only for test runs; the model environment was not modified.
- Alibaba Open Code Review `v1.12.11 (a758d9c)` preview and resolved Python/JSON rules were used locally at zero cost. Test files excluded by preview were supplied explicitly to rule resolution and host review. This is host-agent review under OCR rules, not independent peer review or an OCR LLM verdict. See `V5_LOCAL_PREMODEL_REVIEW_2026-10-03.md`.
- Jev remains `DEFERRED_ZERO_COST_POLICY`; no paid Jev execution or qualification is claimed.

Current scientific state: `SCIENTIFIC_FREEZE_OPEN`; `MODEL_LOAD=NO`; `INFERENCE=NO`; `TRAINING=NO`; `CONFIRMATORY_MATERIALIZED=NO`; `RESERVE_MATERIALIZED=NO`. Existing bounded development authority is approved, but the frozen interface requires a prospective amendment. The concrete request is `V5_S1_ANSWER_INTERFACE_AMENDMENT_REQUEST_2026-10-03.md`; its proposed newline marker has not been adopted.


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
