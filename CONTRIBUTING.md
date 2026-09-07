# Contributing to commandMed

commandMed is a medically sensitive, evidence-first research repository. Contributions are welcome, but repository quality is measured by correctness, safety, reproducibility, provenance, and scope discipline rather than change volume.

## Start here

Before changing code or documentation, read:

1. [`AGENTS.md`](AGENTS.md)
2. [`specs/README.md`](specs/README.md)
3. the current active-spec reconciliation / task ledger
4. relevant governance documents under [`docs/governance/`](docs/governance/)

The roadmap is not execution authority. A future feature being desirable does not make it lawful to implement under the current active spec.

## Contribution principles

### Preserve the active boundary

Do not silently expand an active spec, introduce model/data/runtime/provider execution, or open a blocked downstream spec merely because an implementation is convenient.

If a change needs new authority, evidence, credentials, budget, protected data, model weights, device access, or a Founder decision, fail closed and document the prerequisite.

### No fabricated evidence

Never claim tests, CI, review, benchmark results, runtime measurements, model behavior, qualification, mergeability, scientific outcomes, or authority that did not actually occur.

Static reasoning is not empirical evidence. Passing code tests are not a medical, scientific, security, or release qualification unless the governing spec explicitly defines them that way.

### Medical and privacy safety

Do not commit:

- PHI;
- real patient records;
- Private Gold payloads;
- credentials/secrets;
- restricted datasets without explicit admission authority;
- patient-facing clinical claims unsupported by qualified evidence.

Use synthetic or repository-approved fixtures for ordinary development.

### Deterministic authority first

When a deterministic or authoritative mechanism exists for a safety-critical operation, prefer it over model judgment. Examples include arithmetic, unit conversion, schema validation, validated scores, medication-interaction logic, access control, and execution policy.

### Security is non-compensable

A critical security failure is not offset by a high aggregate score. Changes touching tools, MCP, agents, network access, credentials, execution, provenance, release pipelines, or safety boundaries require explicit security reasoning and negative tests appropriate to their risk.

## External source and donor code

External repositories may be used only under [`docs/governance/external-code-adoption.md`](docs/governance/external-code-adoption.md).

Every adoption must declare one mode:

```text
REFERENCE_ONLY
PATTERN_REIMPLEMENTED
ADAPTED_DERIVATIVE
COPIED_SOURCE
VENDORED_COMPONENT
```

For copied/adapted/vendored code, preserve exact donor repository/revision/path/blob identity, license/NOTICE obligations, third-party component state, modification notices, attribution, security review, and test evidence.

Do not assume Founder source-use permission eliminates upstream license, patent, copyright, NOTICE, or third-party obligations.

At present, canonical redistribution of copied donor code remains blocked until the repository's root software-license posture is explicitly selected and implemented.

## Pull request scope

Prefer one bounded concern per PR.

A strong PR should state:

- problem and scope;
- exact files/surfaces affected;
- governing spec or planning/governance basis;
- authority effect (`NONE` when appropriate);
- security/safety implications;
- provenance or external-source impact;
- tests or validation actually performed;
- explicit non-actions when execution boundaries matter.

Do not bundle unrelated cleanup with scientific or authority-sensitive changes.

## Tests and qualification

Use the narrowest focused tests first, then the governing regression suite required by the affected spec or workflow.

For implementation changes, expected evidence may include:

- syntax/compile checks;
- focused unit/policy tests;
- spec-level regression;
- full repository regression where required;
- whitespace/diff checks;
- exact-head CI;
- independent review when governance requires it.

Do not weaken tests or path filters simply to make CI green.

Docs-only PRs may legitimately have no Actions run if current workflow filters exclude them; report that state rather than inventing a CI result.

## Commit and repository-facing language

Repository/GitHub technical content should be concise, explicit, and evidence-based. Prefer commit messages such as:

```text
docs(governance): add bounded source-adoption policy
test(e004): harden prerequisite snapshot validation
fix(e004): fail closed on runtime identity mismatch
```

Avoid promotional claims that are broader than the evidence.

## Scientific claims

Terms such as `SOTA`, `best`, `safe`, `clinically validated`, `winner`, `release-ready`, or similar claims require the exact comparison class, frozen protocol, relevant hard gates, and evidence required by governance.

Negative and NO-GO results are valid research outcomes.

## Questions and proposals

For substantial ideas, start from the current dependency frontier. A useful proposal explains what measured gap it addresses, why existing mechanisms are insufficient, what evidence would justify adoption, and what kill criteria would reject it.

Do not create detailed implementation plans for blocked future specs solely to make the roadmap appear complete.
