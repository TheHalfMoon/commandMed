# V5 repeatability verifier portability repair — 2026-10-09

Status: `VERIFICATION_MECHANICS_REPAIR_ONLY; NO_SCIENTIFIC_OUTPUT_CHANGED`

The first model-free verification attempt for unchanged-base repeatability R1 rejected the exported analysis with `REPEATABILITY_ANALYSIS_REPRODUCTION_MISMATCH`.

Investigation showed that every reproduced field matched except two mean semantic-JS floats, each differing by exactly `2.168404344971009e-19` between Kaggle JSON serialization/recomputation and the local verifier. All 16,384 exported logits, task identities, targets, prompt hashes, split/variant identities and stored scientific outputs were unchanged.

The original repeatability verifier required byte-identical canonical JSON for floating-point analysis values. That was stricter than the already-qualified C1/C2 model-free verifiers, which use an absolute `1e-12` analysis-reproduction tolerance.

This repair changes only the repeatability verifier's deterministic analysis comparison:

- exact dictionary/list structure remains required;
- non-float values remain exact;
- floats must be finite and agree within absolute tolerance `1e-12`;
- the verification receipt records `analysis_reproduced_absolute_tolerance=1e-12`;
- archive integrity, runtime identity, hardware binding, exact source identity, ordered 16,384-row identity, finite logits, model-free/no-weights boundary, zero spend and confirmatory/reserve prohibitions are unchanged.

The tolerance was not selected to make a scientific result pass. It matches the pre-existing C1/C2 verifier tolerance and is more than six orders of magnitude larger than the observed cross-platform drift while remaining far below reported scientific precision.

The failed first verification attempt is preserved as a negative verification-mechanics event. No R1 rerun is authorized or needed because the scientific export itself was complete and unchanged. R2 remains blocked until R1 passes the repaired verifier, is durably reviewed, committed and pushed, and the canonical predecessor gate passes.

PR #320 remains OPEN / DRAFT / UNMERGED. This repair grants no confirmatory, reserve, replication, publication, merge, paid-resource, PHI or gated-data authority.
