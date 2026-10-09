# V5 repeatability: ordered distinct-repeat input integrity guard — 2026-10-09

Status: `SAFETY_CORRECTION_CANDIDATE; NO_R2_OUTPUT_CONSUMED`.

## Pre-correction negative test

At research commit `819cf1dda443937eec0360e6051a89062b545cb9`, the
model-free `compare(R1, R1)` input was accepted and reported all four primary
`repeatability95` quantities as zero. The same R1 decision-matrix artifact was
passed twice. This is an input-integrity defect, not evidence of perfect
repeatability or a valid two-run scientific estimate.

## Bounded correction

Reject the pair unless the JSON input metadata contains exact integer `repeat`
identities `1` and `2`, in the frozen R1-to-R2 order. Explicitly reject Boolean,
floating-point and string aliases. This correction changes no primary/secondary
metric, nearest-rank percentile rule, source-task clustering, split, numerical
precision or frozen analysis estimator.

The guard is necessary but insufficient to establish independent run provenance:
both inputs must still pass the independent full source-bound export verifier
and be linked to their genuine separately executed durable kernel records.

## Scope and scientific status

R2 was already running on Kaggle when this integrity defect was identified.
This safety correction is being prepared in a **separate branch**; the pinned
scientific R2 branch and frozen runtime are unchanged. No model call, R2 output,
confirmatory/reserve identity, clinical claim, publication, paid compute or
review/merge authority is introduced by this correction.

The exact negative case and all newly added tests must pass on the correction
branch. PR #320 remains draft and unmerged; separate gate review is required
before this correction may be incorporated into the scientific post-processing
pipeline. Historical outcomes are preserved.
