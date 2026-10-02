# Preregistration skeleton V5

Status: `PARTIALLY_BOUND_NOT_FROZEN`; confirmatory access remains prohibited.

## Research question

Do targeted reliability interventions for medical foundation-model decisions transfer across assurance properties, remain modular, or interfere with other reliability requirements?

## Primary hypotheses

- H1: at least one admitted intervention has a non-negligible non-target effect on another assurance property.
- H2: at least one target-improving intervention materially harms a declared noncompensable property.
- H3: the frozen compensatory aggregate and the non-compensatory assurance rule disagree on at least one system conclusion for a consequential reason.
- H4: at least one nominated cross-property effect replicates directionally on a second backbone family.
- H5: at least one preregistered ordered intervention pair exhibits a non-additive interaction on a nominated assurance property.

## Bound fields

- primary backbone: `Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`
- replication backbone: `HuggingFaceTB/SmolLM2-1.7B@effd688a12921b4cc83e3312b6feb579f70f9c71`
- primary source family: public-domain RiskCalcs lineage at `ncbi-nlp/Clinical-Tool-Learning@d474a95128e128623933c9be0d389ff7d82ef782`
- primary planned cluster count: `4096` (`64 calculators x 64 cases`) if final static admission succeeds
- secondary external family: RiskQA blob `2a2372ddd705efab4194f2ff7a3bf21c74dc1c7e`, reported `N=350`
- primary family-wise alpha: `0.05`; multiplicity: Holm
- desired primary power: `0.90`
- learned-intervention development seeds: `11`, `29`, `47`

## Bound intervention specification IDs

`A1_TS_V1`, `A2_SELBIAS_V1`, `B1_TYPED_V1`, `C1_CRDI_V1`, `C2_CRDI_RETAIN_V1`, `D1_DEFER_V1`, and `D2_RULETOOL_V1` are the only current confirmatory candidates. Implementation commit/blob hashes remain unbound until the code exists and passes review.

Ordered interaction candidates are `A1 -> A2`, `A2 -> A1`, `A1 -> C1`, and `C1 -> A1` where technically meaningful.

## Still frozen-before-run

- final admitted 64-calculator manifest after static domain/interpretation audit: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- synthetic generator implementation and exact hash: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- intervention implementation hashes: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- meaningful native-unit margins `m_j`: `TBD_AFTER_DEVELOPMENT_ONLY_PILOT_BEFORE_CONFIRMATORY_ACCESS`
- final power calculation at frozen `m_j`: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- lawful capability-retention task identity: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- exact confirmatory source identities and transformation seeds: `TBD_BEFORE_CONFIRMATORY_ACCESS`
- nominated effects for independent-family replication: `TBD_BEFORE_REPLICATION_ACCESS`

Hard-gate protection is relative noninferiority: every declared hard-gate non-target property must satisfy `Delta[i,j] >= -m_j` under the frozen confidence procedure. No compensatory aggregate can override a failed hard gate.