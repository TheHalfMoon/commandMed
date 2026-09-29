# commandMed

**Universal Health & Medical Intelligence under hard evidence, safety, security, and resource constraints.**

commandMed is an open research program for building Health & Medical Intelligence for patients, caregivers, clinicians, nurses, pharmacists, students, and researchers.

The project optimizes for:

> **verified medical usefulness and safety per byte, joule, and second**

with hard requirements for evidence integrity, agent/tool security, software provenance, reproducibility, and honest scientific claims.

## Project status

commandMed is an active research repository. It is **not a released clinical product** and **no training is currently authorized**.

The existing canonical execution frontier remains **Spec 007 / E004**. Historical canonical evidence has established exact model-load compatibility for the previously frozen four-candidate set. The Founder selected the bounded no-model operational-preflight evidence lane, but that does not authorize training or imply a model winner.

Current historical execution state:

```text
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=PASS
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PASS_4_OF_4
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

For the exact pre-v2 dependency frontier, read:

- [`specs/007-sft-v1/e004-registry-current-state-reconciliation-v49-2026-09-08.md`](specs/007-sft-v1/e004-registry-current-state-reconciliation-v49-2026-09-08.md)
- [`specs/README.md`](specs/README.md)

Passing implementation tests never substitutes for missing scientific, authorization, access, resource, review, or evidence gates.

## CommandMed v2 research reset

The prospective research direction is now **CommandMed One**: investigate whether language/multimodal reasoning, one-pass calibrated typed decisions, and visual generation can be unified around one shared medical Qwen-family semantic backbone and one checkpoint.

The target is not an ensemble of three independently served foundation models. The research hypothesis is:

```text
                   shared medical Qwen backbone
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
       language head     decision head     visual bridge
       autoregressive    typed probability      |
          reasoning        distributions        v
                                             image DiT
                                                |
                                               VAE
                                                |
                                              image
```

The working method name is **Heterogeneous Capability Fusion (HCF)**. It combines only architecture-compatible weight-space merging with decision-head transplantation, cross-architecture representation alignment, image-encoder replacement, and joint stabilization. Simple averaging of incompatible language and diffusion tensors is explicitly not the research method.

Read first:

- [`docs/COMMANDMED-GRAND-MASTER-PLAN-v2.0.md`](docs/COMMANDMED-GRAND-MASTER-PLAN-v2.0.md)
- [`docs/research/COMMANDMED-V2-PAPER-AND-NOVELTY-PROGRAM.md`](docs/research/COMMANDMED-V2-PAPER-AND-NOVELTY-PROGRAM.md)

The older [`docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`](docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md) remains historical scientific/governance evidence and is superseded only for prospective architecture and roadmap planning. Closed historical specs and evidence are not rewritten.

## v2 scientific target

CommandMed v2 investigates one checkpoint with:

- a shared Qwen-family medical semantic backbone;
- autoregressive English/Arabic medical language and reasoning;
- native multimodal understanding;
- a non-autoregressive typed decision head returning probability distributions directly;
- a visual-generation path derived from Qwen-Image-family research;
- elimination of a duplicate image-model semantic encoder if experiments support it;
- evidence/FHIR/tool competence without surrendering deterministic truth boundaries;
- measurable parameter/storage/memory reuse;
- contamination-resistant medical evaluation;
- strong baselines against ordinary joint training and current model-merging methods.

The current preferred research backbone candidate is `Qwen/Qwen3.8-27B`; it is not a proven CommandMed winner. Qwen-Image-2.1 is a frontier research donor candidate with a distinct research license and therefore does not automatically satisfy the project’s permissive release posture.

## Paper-first research discipline

The paper is a primary project output, but publication pressure must not weaken evidence standards.

The strongest prospective paper thesis is not merely “medical understanding + image generation,” because recent work already studies unified medical understanding/generation. The intended research gap is the unification of three computational paradigms around one medical semantic backbone:

```text
autoregressive reasoning
        x
one-pass calibrated typed decisions
        x
flow/diffusion visual generation
        x
heterogeneous capability fusion
        x
single-checkpoint efficiency
```

Any `first`, `best`, `SOTA`, `safe`, or `clinical-grade` claim remains prohibited until the corresponding evidence and related-work claim ledger support it.

## Probability, calibration, and safety

v2 does **not** require a separate uncertainty model. Probability quality is a native property of the decision head and is measured directly using calibration and selective-prediction metrics.

The research goal is calibrated decisiveness, not unsupported certainty. Safety-critical failures remain noncompensable.

The model may support outcomes such as:

```text
ANSWER | ASK_MORE | USE_TOOL | RETRIEVE_EVIDENCE | ABSTAIN | ESCALATE | EMERGENCY
```

when required by the frozen policy. Deterministic or authoritative mechanisms continue to own safety-critical arithmetic, validated clinical scores, drug/interaction lookups, schema validation, and hard escalation rules where such mechanisms exist.

## Generated-image truth boundary

Generated or edited pixels are not clinical evidence for the source case.

Research artifacts must distinguish observed source images from model interpretations and generated visual content. Image generation may be studied for education, simulation, augmentation, counterfactual research, annotation, reconstruction, and representation analysis, but diagnostic claims require modality-specific evidence.

## North star

commandMed aims to build a model/system that is simultaneously:

- medically useful;
- safety-capped;
- evidence-grounded;
- calibrated and capable of requesting more information or abstaining when required;
- strong in English and Arabic;
- tool-aware without surrendering deterministic authority;
- reproducible and provenance-bound;
- secure across model, retrieval, tool, MCP, agent, runtime, and provider boundaries;
- efficient enough to justify a single-checkpoint design under measured resource constraints.

A benchmark score, model size, training completion, or attractive demo is never sufficient evidence by itself.

## Scientific and governance principles

commandMed uses dependency-ordered specifications and append-only evidence/reconciliation records.

Core rules include:

- evaluation before optimization;
- exact identities and reproducible manifests;
- no fabricated CI, review, runtime, qualification, or scientific evidence;
- fail closed when authority or evidence is absent;
- no PHI in repository artifacts;
- no Private Gold access without explicit authority;
- no model, benchmark, device, credential, or spend execution merely because code or a roadmap exists;
- no SOTA, winner, release, safety, or patient-facing claim wider than the evidence;
- one bounded active implementation frontier at a time;
- negative results are preserved rather than hidden;
- repeated access converts confirmatory tests into development/regression evidence.

Start with [`AGENTS.md`](AGENTS.md), the v2 master plan, and [`specs/README.md`](specs/README.md) before making changes.

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

## Software license

commandMed-owned software source is licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

Third-party and donor-origin code/weights retain their applicable upstream terms. Every copied, adapted, merged, distilled, transplanted, or vendored component must preserve exact provenance and satisfy the intended use. The project’s license does not relicense third-party model material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/governance/external-code-adoption.md`](docs/governance/external-code-adoption.md).

## Security

Security issues affecting agent/tool authority, prompt injection, secret handling, command execution, network boundaries, provenance, release integrity, or other sensitive surfaces should follow [`SECURITY.md`](SECURITY.md).

Do not place credentials, PHI, Private Gold, exploit payloads, or sensitive operational details in public reports.

## Medical-use boundary

commandMed is research software. The repository does not currently authorize patient-facing clinical deployment or clinical claims. Nothing in this repository should be interpreted as medical advice or as evidence that a model can replace qualified clinicians.

## Core planning documents

Prospective v2:

- [`docs/COMMANDMED-GRAND-MASTER-PLAN-v2.0.md`](docs/COMMANDMED-GRAND-MASTER-PLAN-v2.0.md)
- [`docs/research/COMMANDMED-V2-PAPER-AND-NOVELTY-PROGRAM.md`](docs/research/COMMANDMED-V2-PAPER-AND-NOVELTY-PROGRAM.md)

Historical/current assurance references:

- [`docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`](docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md)
- [`docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md`](docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md)
- [`docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md`](docs/COMMANDMED-SECURITY-ASSURANCE-AND-PERFORMANCE-PLAN-v0.1.md)

The roadmap is planning. **Only canonical bounded authority may execute work.**
