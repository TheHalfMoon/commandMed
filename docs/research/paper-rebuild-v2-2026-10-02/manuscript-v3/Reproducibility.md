# 10. Reproducibility

Every empirical run must be reconstructible from an immutable manifest containing repository commit/tree, model and tokenizer/processor revisions, dataset/content hashes, split and transformation-manifest hashes, environment lock, hardware, seeds, hyperparameters, command/configuration, timestamps, raw outputs and analysis-code identity.

Transformation generators are versioned research artifacts. For each generated case, retain source item ID, transformation family, canonical-to-transformed candidate mapping, generator revision, validation status and exclusion reason where applicable.

The final paper package will include:

- `main.tex` and section sources;
- `bibliography.bib`;
- preregistered protocol and statistical-analysis plan;
- claim ledger;
- experiment index;
- transformation manifest;
- run manifests;
- raw or lawfully shareable predictions;
- analysis scripts;
- figure/table generation scripts;
- environment lock;
- artifact manifest with cryptographic hashes.

If data or model licenses prevent redistribution, the manifest will identify exact upstream resources and document what cannot be shared. Reproducibility claims will be narrowed accordingly.