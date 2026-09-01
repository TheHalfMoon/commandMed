# Temporary E004 Exact-Head Evidence Review Carrier

**DO NOT MERGE THIS CARRIER.**

This file exists only to create a fresh review-carrier commit whose parent is the exact canonical merge candidate under review.

```text
REVIEW_SUBJECT_HEAD=2417ec96fd551b102a0115913d0ccf1748fcf172
REVIEW_SUBJECT_PARENT_OF_CARRIER=YES
CANONICAL_BASE=bc3ea6830fc0aaa674df2b439b74a98cda34bd20
SOURCE_PR=168
CARRIER_MERGE_AUTHORITY=NONE
CARRIER_EXECUTION_AUTHORITY=NONE
```

The required independent review is of `REVIEW_SUBJECT_HEAD`, not of this carrier file.

The reviewer must independently inspect:

1. `git diff bc3ea6830fc0aaa674df2b439b74a98cda34bd20...2417ec96fd551b102a0115913d0ccf1748fcf172` and confirm it changes exactly one reconciliation document.
2. `specs/007-sft-v1/e004-rebuild-reproducibility-diagnostic-authority-2026-09-01.md` at canonical base/main.
3. `.github/workflows/e004-rebuild-reproducibility-diagnostic-v1.yml` at canonical base/main.
4. Retained GitHub Actions run `33507754943`, attempt `1`, job `99855785119`, without triggering, retrying, rerunning, or substituting execution.
5. The retained terminal log directly, preferably with:

```bash
gh run view 33507754943 --repo TheHalfMoon/commandMed --log > /tmp/e004-run-33507754943.log
```

The terminal evidence must be compared with exact subject file:

`specs/007-sft-v1/e004-rebuild-reproducibility-diagnostic-result-reconciliation-2026-09-01.md`

at exact commit `2417ec96fd551b102a0115913d0ccf1748fcf172`.

The review must verify hashes, byte counts, GNU Build-IDs, CMake-cache identities, same-layout equality, cross-layout inequality, byte-difference counts, normalized PATH identities, final diagnostic disposition, one-shot history, canonical reproducibility sentinels, and authority boundaries.

If no material correctness, evidence-integrity, governance, reproducibility, or authority-boundary blocker remains on the exact subject head, the reviewer should conclude explicitly:

```text
MATERIAL_BLOCKER=NO
```

This carrier adds no model, weight, conversion, inference, benchmark, contamination, A15, training, credential, protected-data, upload, paid-compute, procurement/payment, spend, workflow-execution, retry, rerun, or successor authority. Close the carrier without merge after review evidence is captured.