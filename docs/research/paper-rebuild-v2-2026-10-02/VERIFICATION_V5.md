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