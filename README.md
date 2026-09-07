# commandMed

**Universal Health & Medical Intelligence under hard evidence, safety, security, and resource constraints.**

commandMed is an open research program for building compact, multilingual, tool-aware Health & Medical Intelligence systems for patients, caregivers, clinicians, nurses, pharmacists, students, and researchers.

The project optimizes for:

> **verified medical usefulness and safety per byte, joule, and second**

with additional hard requirements for evidence integrity, agent/tool security, software provenance, and reproducibility.

## Project status

commandMed is an active research repository with dependency-ordered governance. It is **not** a released clinical product and **no training is currently authorized**.

The current active frontier is **Spec 007 / E004**. Canonical evidence has established exact model-load compatibility for the frozen four-candidate set. The Founder has now selected the bounded no-model operational-preflight evidence lane, but that evidence has not yet been implemented, qualified, or executed; later prerequisite gates still remain.

Current high-level state:

```text
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=PASS
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PASS_4_OF_4
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

For the exact dependency frontier, read:

- [`specs/007-sft-v1/e004-registry-current-state-reconciliation-v49-2026-09-08.md`](specs/007-sft-v1/e004-registry-current-state-reconciliation-v49-2026-09-08.md)
- [`specs/README.md`](specs/README.md)

Passing implementation tests never substitutes for missing scientific, authorization, access, resource, review, or evidence gates.

## North star

commandMed aims to build a system that is simultaneously:

- medically useful;
- safety-capped;
- evidence-grounded;
- uncertainty-aware and willing to abstain;
- strong in English and Arabic;
- tool-aware without surrendering deterministic authority;
- reproducible and provenance-bound;
- secure across model, retrieval, tool, MCP, agent, runtime, and provider boundaries;
- efficient enough for meaningful on-device and bounded-resource deployment.

A benchmark score, model size, training completion, or marketing claim is never sufficient evidence by itself.

## Architecture

### Health & Medical Intelligence Core

The compact core targets durable capabilities such as medical reasoning, problem representation, active information acquisition, uncertainty detection, evidence use, role-conditioned communication, tool routing, and multilingual clinical language.

### Evidence & Tool Plane

Mutable or authoritative facts should remain external where practical: guidelines, formularies, drug interactions, literature, validated calculators, FHIR/schema validators, and institution-specific evidence packs.

### Patient Safety Shield

Safety-critical operations are composed with deterministic or authoritative checks. The system may force outcomes such as:

```text
ANSWER | ASK_MORE | USE_TOOL | RETRIEVE_EVIDENCE | ABSTAIN | ESCALATE | EMERGENCY
```

The model does not own safety-critical arithmetic, medication interaction logic, validated scoring rules, or schema validation when deterministic mechanisms exist.

### AI Security & Agent/Tool Trust

The master plan now includes first-class security architecture for prompt injection, authorization bypass, data/secret exfiltration, tool abuse, tool poisoning/shadowing, command injection, SSRF, agentic supply-chain risk, context over-sharing, provider/model substitution signals, and related AI-native threats.

The preferred security pattern is:

```text
DETERMINISTIC PRE-SCAN
-> VERSIONED RULE ENGINE
-> OPTIONAL AUTHORIZED MODEL-ASSISTED ANALYSIS
-> DETERMINISTIC FINDING NORMALIZATION
-> SECURITY HARD GATE
```

See [`docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md`](docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md).

### Profile-First Performance Engineering

Hardware-specific optimization is admitted only after profiling proves a material bottleneck. Microbenchmark gains do not count as system gains without end-to-end, correctness, medical/safety-equivalence, and resource evidence.

## Scientific and governance principles

commandMed uses dependency-ordered specifications and append-only evidence/reconciliation records.

Core rules include:

- evaluation before optimization;
- exact identities and reproducible manifests;
- no fabricated CI, review, runtime, qualification, or scientific evidence;
- fail closed when authority or evidence is absent;
- no PHI in repository artifacts;
- no Private Gold access without explicit authority;
- no model, benchmark, device, credential, or spend execution merely because code exists;
- no SOTA, winner, release, safety, or patient-facing claim wider than the evidence;
- one bounded active implementation frontier at a time.

Start with [`AGENTS.md`](AGENTS.md) and [`specs/README.md`](specs/README.md) before making changes.

## Repository map

```text
src/      deterministic implementation/control-plane code
scripts/  bounded evidence and repository utilities
specs/    dependency-ordered specifications, tasks, evidence, reconciliation
data/     repository-owned fixtures/manifests allowed by governance
tests/    focused and regression tests
docs/     master plans, research, governance, architecture
.github/  bounded CI/evidence workflows
```

## External source adoption

Founder-supplied external repositories may be studied and, where permitted, later copied or adapted. Source-use permission does not replace file-level provenance, license/NOTICE preservation, security qualification, dependency review, or canonical admission.

Every future adoption must classify itself as one of:

```text
REFERENCE_ONLY
PATTERN_REIMPLEMENTED
ADAPTED_DERIVATIVE
COPIED_SOURCE
VENDORED_COMPONENT
```

See [`docs/governance/external-code-adoption.md`](docs/governance/external-code-adoption.md).

Current qualified Tencent references include:

- `Tencent/AI-Infra-Guard` — AI/agent/MCP security assurance reference;
- `Tencent/AICGSecEval` — repository-level secure AI engineering evaluation reference;
- `Tencent/hpc-ops` — deferred GPU/server performance-engineering reference.

No donor code from those sources is made canonical merely by being referenced here.

## Software license

commandMed-owned software source is licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

Third-party and donor-origin code retains its applicable upstream terms. Every copied, adapted, or vendored component must preserve exact provenance, license/NOTICE obligations, security qualification, and admission evidence. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/governance/external-code-adoption.md`](docs/governance/external-code-adoption.md).

The license decision does not automatically admit any donor code, dependency, dataset, model artifact, benchmark, or other third-party material.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a change. Contributions must preserve the active-spec boundary, scientific evidence rules, provenance requirements, and security/safety hard gates.

## Security

Security issues affecting agent/tool authority, prompt injection, secret handling, command execution, network boundaries, provenance, release integrity, or other sensitive surfaces should follow [`SECURITY.md`](SECURITY.md).

Do not place credentials, PHI, Private Gold, exploit payloads, or sensitive operational details in public reports.

## Medical-use boundary

commandMed is research software. The repository does not currently authorize patient-facing clinical deployment or clinical claims. Nothing in this repository should be interpreted as medical advice or as evidence that a model can replace qualified clinicians.

## Core planning documents

- [`docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`](docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md)
- [`docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md`](docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md)
- [`docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md`](docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md)

The roadmap is planning. **Only canonical bounded authority may execute work.**
