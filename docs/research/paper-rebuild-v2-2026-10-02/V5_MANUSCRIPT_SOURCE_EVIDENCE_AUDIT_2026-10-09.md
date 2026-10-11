# V5 immutable manuscript development-evidence source audit — 2026-10-09

Status: `DEVELOPMENT_ONLY_INTEGRITY_GATE; NOT_CONFIRMATORY_OR_PUBLICATION_AUTHORITY`.

## Purpose

An earlier manuscript addendum accurately distinguished completed development/calibration measurements from not-yet-executed confirmatory study results. A textual crosswalk alone is vulnerable to subsequent evidence edits or provenance drift. The read-only, model-free `scripts/v5_manuscript_development_evidence_audit.py` turns the crosswalk's fixed inputs and restrictions into a fail-closed check without modifying prospectively frozen manuscript, claim-ledger, red-team or data-generation files.

## Reproducibility

Run from the repository checkout:

```sh
python3 scripts/v5_manuscript_development_evidence_audit.py
PYTHONPATH=src python3 -m pytest -q tests/reliability_v5/test_manuscript_development_evidence_audit.py
```

The audit verifies SHA-256 of eight precisely named versioned inputs (independent R1/R2 verifier receipts, paired repeatability, prospectively frozen domain floors, computed benchmark margins, development source-task SD inventory, B1/C1/C2 seed synthesis, and the manuscript crosswalk) plus the original two R1/R2 Kaggle ZIPs. It rejects source drift, missing files, escaped paths, non-development scope, false clinical/publication approval, false power-family freeze, missing source-task cells, nonfinite SD, modified metric family, changed repeatability95 or post-hoc margin adjustment.

The model-free frozen-entry manifest is checked on each run: all **307** original hash-bound entry files, including the original manuscript/claim ledger, must stay unchanged. **The entry-file manifest itself is separately SHA-256 pinned** as `c33e603e531b5f3957a0fbe5fa63d45f070e21e2243b268af232516990dd428f`, because it is not one of the 307 self-described entries. Otherwise a coordinated rewrite of both the manifest and its referenced evidence could pass the entry loop. Duplicate manifest paths are rejected, too. The script also verifies that each original repeat has a distinct named Kaggle kernel, a valid independent archived export-verifier receipt, full 16,384-row coverage, and the exact pinned public RiskCalcs source identity.

## Scope and limitations

**PASS** means only that retained, independently verified development input files match this exact immutable report snapshot and satisfy the narrow admission checks. It is **not** a fresh independent Kaggle execution, an independent human or LLM peer review, proof of model performance, statistical power, scientific independence beyond the cited run provenance, clinical utility, medical safety, or permission to proceed to confirmatory/reserve materialization. A different source version requires a new reviewed evidence binding; the script is intentionally not a general-purpose permissive importer.

The four research-scale margins are study-defined nonclinical effect scales; the three trained seeds' within-source-task paired SDs are **descriptive** and do not substitute for a reviewed source-and-training-seed variance model. The primary hard-gate non-target hypothesis family and its count remain unfrozen, so the fixed 4,096-source-cluster design cannot be declared to meet 90% power. No V5-C01–V5-C07 empirical claim is promoted by this guard.

Repository branch/PR work is DCO-signed off only until GitHub independently verifies cryptographic signatures. Genuine zero-cost Alibaba OCR delegation eligibility and a host audit must not be represented as independent model or methodological review. No PHI, paid APIs/compute, new scientific inference or altered frozen source was used to build this offline qualification utility.

## 2026-10-10 calculator-ICC source-binding extension (development only)

The updated manuscript crosswalk references the new 72-cell source-bound calculator-effect ICC inventory from draft #323. The audit now requires the exact original artifact SHA-256 `37d64c0f6ac14d04cc6420a020e7bb7997fb333e50729f33798b2d403d292370`; it fails closed if that artifact is absent, overwritten, re-labeled, misses any expected intervention/seed/split/metric cell, erases its 12 negative finite-sample ICC values, loses the pre-existing paired-SD source hash, or escalates a scientific approval flag. This brings the total number of separately locked development text/JSON sources to nine plus two original Kaggle ZIP exports and the independently pinned 307-entry frozen manifest.

The source-based ICCs are descriptive only. No population correlation, confirmatory power, Holm-family review, clinical validation, external peer review, or paper/compute authority follows from this integrity extension. The originally frozen scientific files are unchanged.
