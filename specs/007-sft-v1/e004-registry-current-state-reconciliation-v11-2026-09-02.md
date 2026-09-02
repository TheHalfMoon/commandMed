# E004 Registry Current-State Reconciliation V11 — 2026-09-02

**Spec:** 007 SFT V1
**Task:** E004
**Artifact class:** append-only current-state reconciliation
**Canonical base:** `10f6ee4cdbbc418462d1c9d1e8a1e015f61bc35b`
**Authority effect:** repository-review governance only
**Execution effect:** NONE

## Purpose

Reconcile the E004 current view after Founder decision `FD-007`, which removes mandatory independent repository/PR review as a default qualification or merge gate.

This record supersedes only the prospective repository-review-gate language in V10 and earlier E004 records. It does not rewrite historical review evidence and does not alter any scientific, safety, identity, reproducibility, resource, rights, privacy, personnel, model, data, execution, contamination, A15, training, or spend prerequisite.

## Repository review policy

Effective after canonical merge of the governing amendment:

```text
INDEPENDENT_REPOSITORY_REVIEW_REQUIRED_BY_DEFAULT=NO
EXACT_HEAD_REVIEW_REQUIRED_BY_DEFAULT=NO
MATERIAL_BLOCKER_NO_REVIEWER_SENTINEL_REQUIRED_BY_DEFAULT=NO
SELF_REVIEW_PROHIBITION_AS_REPOSITORY_MERGE_GATE=REMOVED
```

A later bounded authority may explicitly require a repository reviewer for a specifically named task, but no such requirement is inferred from historical E004 records after this amendment.

Deterministic verification remains mandatory where applicable:

```text
LIVE_BASE_HEAD_VERIFICATION=REQUIRED
BOUNDED_DIFF_VERIFICATION=REQUIRED
CI_AND_STATUS_CHECKS=REQUIRED_WHEN_APPLICABLE
UNRESOLVED_REVIEW_THREADS=REQUIRED_ZERO_WHEN_THREADS_EXIST
EVIDENCE_DEPENDENT_GATES=REMAIN_REQUIRED
EXECUTION_AUTHORITY_GATES=REMAIN_REQUIRED
```

## Scientific and domain evidence boundary

This amendment does not remove domain-qualified human evidence requirements that are part of a scientific or safety claim. Clinical/statistical review evidence, privacy/rights/governance evidence, human-factor evidence, and patient-facing human evaluation remain governed by their own canonical requirements unless separately amended.

Repository bots, LLMs, or Founder self-attestation still do not substitute for a domain-qualified human evidence requirement when such evidence is independently required by the scientific contract.

## Current E004 state

No repository-review gate blocks further repository work after this amendment. All non-review blockers remain exactly as established by V10 and later canonical evidence.

```text
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Supersession boundary

V11 supersedes any V10 or earlier E004 sentence that requires independent repository review, exact-head reviewer qualification, or an explicit reviewer `MATERIAL_BLOCKER=NO` solely as a repository PR/merge gate.

All historical review outcomes remain valid historical evidence. All non-review authority and evidence constraints remain unchanged.
