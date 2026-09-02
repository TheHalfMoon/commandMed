# Repository Independent Review Gate Amendment — 2026-09-02

**Decision class:** Founder constitutional amendment
**Decision ID:** `FD-007`
**Decision:** `REMOVE_MANDATORY_INDEPENDENT_REPOSITORY_REVIEW_GATE`
**Effective when:** this amendment and the aligned constitutional/operational edits are canonically merged
**Scope:** repository/PR qualification and merge governance only

## Current rule

The canonical constitution and operating guidance currently treat independent repository review as a mandatory assurance mechanism, and some active/historical specification records encode exact-head independent review or `MATERIAL_BLOCKER=NO` as a PR qualification or merge prerequisite.

## Replacement rule

Independent repository review, bot review, peer review, exact-head review, and a `MATERIAL_BLOCKER=NO` reviewer conclusion are **not mandatory repository qualification or merge gates** unless a later explicit bounded authority reintroduces such a gate for a specifically named task.

Repository changes remain subject to all applicable deterministic validation, evidence, scope, identity, CI, branch/ruleset, dependency-order, execution-authority, and fail-closed requirements.

This amendment does **not** remove or weaken domain-qualified human evidence that is itself a scientific or safety requirement. In particular, where a bounded spec requires clinical, statistical, privacy, rights, governance, or human-factor evidence to support a medical or safety claim, that evidence remains required unless separately amended through its own governing decision surface.

## Reason

The Founder explicitly directed on 2026-09-02 that no repository reviewer is needed and that the mandatory reviewer requirement should be removed. The project can preserve auditable deterministic validation and evidence gates without making an external/bot reviewer a universal prerequisite for repository progress.

## Affected governance

This amendment prospectively supersedes repository-review-only clauses in:

- `.specify/memory/constitution.md` Principle XIII;
- `AGENTS.md` Ponytail safety carve-out;
- active Spec 007 repository qualification/merge language;
- E004 current-state/reconciliation text that requires independent repository review, self-review prohibition, exact-head reviewer qualification, or `MATERIAL_BLOCKER=NO` solely as a repository merge gate;
- older authority/planning records only to the extent they are read prospectively as a repository-review prerequisite.

Historical review records, comments, PR evidence, closeouts, and previously collected reviewer conclusions remain historical evidence and are not rewritten or invalidated.

## Comparability and evidence preservation

Previously collected scientific, runtime, reproducibility, CI, review, and governance evidence remains comparable under its original identity and scope. Removing the repository reviewer gate does not convert any missing scientific or operational evidence into PASS and does not alter prior measured values.

```text
INDEPENDENT_REPOSITORY_REVIEW_REQUIRED_BY_DEFAULT=NO
EXACT_HEAD_REVIEW_REQUIRED_BY_DEFAULT=NO
MATERIAL_BLOCKER_NO_REVIEWER_SENTINEL_REQUIRED_BY_DEFAULT=NO
DETERMINISTIC_VALIDATION_AND_EVIDENCE_GATES=REMAIN_REQUIRED
SCIENTIFIC_DOMAIN_REVIEW_EVIDENCE=AFFECTED_ONLY_BY_SEPARATE_EXPLICIT_AMENDMENT
MODEL_CONVERSION_AUTHORITY=UNCHANGED
CONVERSION_EXECUTION_AUTHORITY=UNCHANGED
CONTAMINATION_ASSESSMENT_AUTHORITY=UNCHANGED
A15_ACTIVATION=UNCHANGED
TRAINING_AUTHORITY=UNCHANGED
CURRENT_AUTHORIZED_SPEND_USD=UNCHANGED
```

## Non-authority

This amendment grants no model/weight access, conversion, quantization, inference, benchmark execution, contamination assessment, A15 activation, training, credential use, protected-data access, paid compute, procurement/payment, or spend authority.
