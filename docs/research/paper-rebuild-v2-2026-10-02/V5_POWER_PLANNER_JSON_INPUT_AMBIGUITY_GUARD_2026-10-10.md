# V5 mechanical power-planner input ambiguity guard — 2026-10-10

Status: `DEVELOPMENT_ONLY_INPUT_INTEGRITY; UNREVIEWED_HYPOTHESES; NOT_FINAL_POWER`.

## Reproduced flaw

The unqualified development-only `scripts/v5_power_margin_plan.py` previously used the default Python `json.loads` behavior on caller-supplied power-planning specifications. When an object supplied the same key multiple times, **the last occurrence silently won**. A synthetic JSON specification based on the existing regression fixture was augmented with contradictory `primary_non_target_family_size` entries (`1`, then `4`). The command succeeded with `PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT` using `4`, despite the conflicting source text. Nested hypothesis identity or per-hypothesis nuisance keys had the same ambiguity. At no point did this bug prove that final power, hypothesis-family completeness, or clinical utility were qualified; all scientific/confirmatory authority flags were already `false`.

Standard Python's non-strict JSON decoder also accepts `NaN`, `Infinity`, and `-Infinity`, which are **not** JSON numbers under RFC 8259. The downstream numeric contract rejected these if routed through its numeric fields, but rejecting them at source is a clearer, uniform trust boundary.

## Narrow source-bound correction

The CLI now loads all caller-supplied planning specifications with a strict JSON object-pairs hook that **rejects duplicate keys at every object depth**, after JSON unescaping (including `\\u` escapes). There is no silent last-wins canonicalization; a failed input produces no new plan output. It also rejects nonstandard `NaN`/`Infinity` literals, invalid UTF-8, malformed JSON and non-object JSON roots with controlled input-contract errors. A valid unambiguous input still emits `PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT` and `final_90_percent_power_qualified=false`, without a review or confirmatory grant.

Real CLI subprocess negative tests (from an unrelated working directory with no `PYTHONPATH`) cover conflicting top-level Holm-family sizes, nested descriptive paired SD, nested hypothesis ID, Unicode-escaped equivalent duplicate names, `NaN`, `Infinity`, non-object roots and malformed JSON. The existing exact-head GitHub Actions V5 input-contract workflow includes the expanded focused test suite.

## Non-overwrite protection for existing scientific evidence

A separate Mac-only synthetic regression demonstrated that the original direct CLI allowed `--spec` and `--output` to reference the **same existing path**: it exited with `PASS_DEVELOPMENT_ONLY_INPUT_CONTRACT` while destroying its own input bytes. Any previously written development planning receipt or original evidence file could have been similarly overwritten by an unintended output path.

The CLI now serializes its *unqualified* development-only result first, then creates its destination with exclusive file mode `x` rather than truncating an existing path. An already existing file, the input source itself, a symlink to evidence, or a second attempt to write the same output filename is rejected with `OUTPUT_ALREADY_EXISTS` and no success receipt. This is a **destination no-clobber guarantee**, not an atomic full-file transaction guarantee if the filesystem fails partway through a fresh write. Direct-subprocess regressions use temp files to verify preserved bytes, symlink preservation and repeat invocation, without touching any actual frozen evidence.

## Explicit boundaries

- Strict JSON syntax **cannot** establish that a user-supplied hypothesis list is prospectively complete, that declared coupling tags are valid, or that an SHA-shaped evidence identifier identifies genuine qualified research evidence.
- The descriptive paired SD values still do **not** qualify the crossed source-case and stochastic training-seed nuisance model or 90% power.
- Scientific `main`, the frozen case generator/evidence/307 bound files, benchmark margins, study endpoints, actual observations and prior negative results are unchanged.
- No inference, model weights, GPU, paid cloud, PHI, confirmatory/reserve case identity access, independent review or founder authority is implied.
- The fix is isolated in a stacked draft successor to PR #327 because the existing local PR #327 worktree has separately owned uncommitted edits and must not be overwritten or committed by another session. No history rewrite or merge is performed.

Reference: statistical and founder authorization gate [#326](https://github.com/TheHalfMoon/commandMed/issues/326), original defect report [PR #327 issuecomment-6094934938](https://github.com/TheHalfMoon/commandMed/pull/327#issuecomment-6094934938).
