# V5 S1 answer-interface amendment request

Status: `PROPOSED_NOT_AUTHORIZED`; no model outputs observed.

## Observed gate failure

The repaired oracle gate qualifies 81 of 82 static candidates and deterministically selects 64. All 8,192 development/calibration examples materialize. The longest encoded canonical/transformed prompt is 593 tokens, below the unchanged 768-token limit. The frozen `ANSWER: ` prefix nevertheless fails the prefix-preserving single-token answer contract for both labels.

With the exact pinned local tokenizer, `ANSWER: ` encodes as `[11355, 38050, 25, 220]`. Appending `A` produces `[11355, 38050, 25, 357]`; appending `B` produces `[11355, 38050, 25, 417]`. The final space token is replaced. Merely observing a one-token divergent suffix does not satisfy the frozen contract. Removing the space also fails because the colon merges with the candidate.

Evidence: `artifacts/v5/development/s1_task_preparation/task-preparation-evidence.json` and `prospective-answer-prefix-metadata.json`. These are tokenizer metadata, not model behavior.

## Concrete prospective amendment for Founder review

Replace only the terminal answer-marker space with a newline: `ANSWER: ` becomes `ANSWER:\n`. Apply that identical marker in the medical prompt renderer, preparation checker, and any model-facing S1 candidate-token qualification. Preserve MATCH/MISMATCH semantics, source cases, proposal balancing, labels, code bodies, transformations, partitions, interventions, seeds, optimization budgets, dtype, CPU restrictions, and the 768-token/no-truncation gate.

Tokenizer-only inspection observes `ANSWER:\n` as `[11355, 38050, 25, 198]`; appending `A` preserves those four tokens and adds `[32]`, and appending `B` preserves them and adds `[33]`. This establishes a candidate interface repair only. No amended medical prompts have been adopted or executed. All full-prompt length and candidate-token checks must be repeated after an approved implementation; this metadata check is not a task-preparation PASS.

## Required prospective controls

1. Record explicit approval of this interface amendment before changing the frozen protocol or renderer.
2. Preserve both the original SAH execution failure and this tokenizer-prefix failure.
3. Update the S1 protocol append-only and bind the amended renderer/checker identities.
4. Regenerate and qualify development/calibration preparation evidence, all affected bindings, and any prompt-content identities. No truncation, length expansion, case exclusion, or tokenizer substitution is permitted.
5. Run relevant tests, compile validation, deterministic checks, exact-head review, and ordinary commit/push before any model preflight.
6. Require the exact run's preflight PASS before loading the existing pinned artifact. All current resource stop rules and confirmatory/reserve prohibitions continue to apply.

## Current boundary

The amendment is a reviewable proposal, not an authority grant. Under S1 section 6, the failed tokenizer interface stops execution and requires prospective amendment. Model load, inference, training, B1/C1/C2 empirical qualification, margin estimation, and power estimation remain blocked. Confirmatory/reserve execution, paid resources, PHI, publication, merge, and replication remain outside this request.
