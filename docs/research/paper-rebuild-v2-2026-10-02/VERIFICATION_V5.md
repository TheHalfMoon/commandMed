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
- The strict RiskCalcs selector admits only statically parsed Boolean/numeric-threshold rules with no string domains, input arithmetic/calls/subscripts/attributes, at most eight inputs, and prospective generated input space of at least 64 states.
- `413` calculators passed that strict static gate across `24` first-listed source specialty strata; `64` are selected by deterministic domain-balanced round-robin before model outputs. All `64/64` selected PMIDs resolve in PubMed, all expose abstracts in the current audit, and `0` carry a retraction/withdrawal publication-type flag. This is source/provenance screening, not current-care clinical qualification.
- The prospective primary RULE_ORACLE design is now `4096` source clusters (`64 calculators x 64 cases`). No clinical calculator function was executed to create these identities.
- Compact case binding: ordered 4096 case IDs SHA-256 = `4973506f7700fcb655a1e1ccd129eaecd1af012e532cb5534e1c643093845c39`.
- `rule-oracle-case-index-v5.json` replaces the large generated case payload; exact cases remain deterministically regenerable from the bound source manifest and generator.
- V5-focused tests on the final reviewed worktree: `46 passed in 0.26s`.
- Full repository tests on the final reviewed worktree: `1098 passed in 25.52s`.
- `python -m compileall` passed for the V5 implementation, freeze tools, and tests.
- The rule-oracle/source-audit/freeze-binding generation pipeline was executed twice after the final schema changes; all five generated artifacts were byte-identical across reruns and `git diff --check` reported zero lines.
- For the selected-calculator source audit, fetched PubMed abstract text is used only transiently to record presence and SHA-256 identity; no fetched abstract body or upstream RiskCalcs interpretation narrative is persisted in `clinical-source-audit-v5.json` or `clinical-source-review-v5.md`.
- The specialty balancing field is explicitly an internal **first-listed source specialty stratum**; it does not claim that the upstream source declares a primary clinical specialty or that the strata estimate prevalence.
- Ruff is not installed on this host; no Ruff result is claimed and no package was installed merely to obtain one.
- Alibaba Open Code Review `v1.12.11 (a758d9c)` was run in zero-cost delegation mode. `ocr delegate preview` and `ocr delegate rule` resolved the Python review policy for the V5 code/freeze tools/tests. Host-agent review under those rules plus targeted security/error-pattern scanning found no blocking correctness/security defect. OCR's own default-path policy excluded test files from preview, so tests were supplied explicitly to `ocr delegate rule` and inspected with the same Python rule.
- Jev remains `DEFERRED_ZERO_COST_POLICY`; no paid Jev call is claimed.

## Literature refresh

A new bounded adversarial refresh is recorded in `literature-refresh-v5-2026-10-03.md`. MedHELM, CSEDB, the EMNLP trustworthy-medical-QA survey, Gu et al. on probabilistic medical predictions, Boie et al. on medical confidence calibration, Matta et al. on calibration versus probabilistic validity, CURA, and CALIN further narrow the paper. The refresh does not clear a `first` claim. The surviving candidate gap is the matched intervention-to-assurance causal effect matrix with preregistered ordered interactions, exact rule-oracle cases, noncompensatory decision logic, and independent-family replication.
