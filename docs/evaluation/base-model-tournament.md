# Spec 005 Base Model Tournament — Implementation Control Plane

**Status:** IMPLEMENTED_PENDING_EXACT_HEAD_REVIEW
**Scope:** Deterministic, offline, identity-bound validators only.
**Training authority:** NONE · **Model execution authority:** NONE · **Model-weight access authority:** NONE
**Benchmark-payload execution authority:** NONE · **Private Gold access authority:** NONE
**Provider generation authority:** NONE · **Device execution authority:** NONE
**A15 real construction activation authority:** NOT_AUTHORIZED · **Authorized spend:** $0

This document records the implemented Spec 005 control plane: what it validates, what it deliberately refuses to do, and which inherited canonical boundaries remain binding.

## 1. Implemented surface

```text
src/commandmed/spec005/
├── science.py          # US2: seven lanes, A2 thresholds, atomic A3+A4 design
├── preconstruction.py  # US3: A5/A6/A8/A9/A10/A11/A12 + snapshot readiness
├── personnel.py        # US4: opaque identity, eligibility, assignments, A7
├── access.py           # US5: three-zone firewall, A13 dispositions
├── finance.py          # US6: A14 requirement/authorization/lifecycle/PASS
├── device.py           # US7: frozen five-target qualification metadata
├── activation.py       # US7: A15 record validation (no real activation)
└── manifest.py         # US7: Spec 005 manifest + fail-closed projection gate

data/spec005/
├── selection_quality_contract.json    # seven noncompensable lanes, anchors
├── preconstruction_contract.json      # closed vocabularies + frozen DAG
└── device_qualification_contract.json # pinned protocol; unresolved = null

tests/spec005/                          # synthetic, non-medical fixture tests
```

## 2. Scientific selection layer (US2)

- Exactly seven quality lanes A–G are recognized; a failed or missing lane can never be compensated by other lanes (`LANES_ARE_NONCOMPENSABLE=YES`).
- Lane mappings bind metrics-v2 metric IDs with explicit `SELECTION_DEV`/`QUALIFICATION_ONLY` evidence roles; `PRIVATE_GOLD_FINAL_AUDIT` and `PUBLIC_EXTERNAL_EVAL` are prohibited as selection mapping roles.
- Arabic parity requires the five frozen coverage anchors and the `ar`/`en` language scope.
- A2 threshold/margin records require exact value-or-margin for any PASS decision; missing values are `INCOMPLETE`, never defaulted. Candidate-result-derived threshold selection is rejected; `pre_result_freeze=true` is mandatory.
- A3+A4 form one atomic statistical design identity: planned numeric N and coverage allocation must both exist, pairing/root-case dependency is required for Arabic parity (unpaired independent-two-sample shortcuts rejected), multiplicity structure must be declared, and `candidate_neutral=true` plus `pre_result_freeze=true` are enforced.
- `evaluate_scientific_selection_readiness()` returns deterministic sorted reason codes; caller-owned `PASS/powered/adequate` claims are ignored.

## 3. Preconstruction governance (US3)

- Closed source-route vocabulary; `MODEL_OR_PROVIDER_GENERATED` and `PROHIBITED_OR_BLOCKED_SOURCE` cannot serve selection development; derived routes need parent bindings; Private Gold can never be a parent/source.
- Root-task metadata is payload-free by construction: content identity is SHA-256 only, exactly one primary coverage anchor from the frozen taxonomy, unknown anchors fail closed.
- Pairs carry one Arabic and one English variant sharing root and pair identity with statistical unit count 1.
- Review bindings enforce author/reviewer/adjudicator separation and reject stale review identities.
- The contamination plan is identity-only (parent-aware, cross-lingual required, no mutable `latest` policy binding).
- `evaluate_preconstruction_snapshot()` consumes the frozen A1–A14 dependency DAG and yields only `NOT_READY_TO_CONSTRUCT` or `READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED`. US2 scientific readiness is a mandatory input that cannot be bypassed. `AUTHORIZED_TO_CONSTRUCT` is structurally excluded from snapshot states.

## 4. Personnel and access (US4/US5)

- Personnel references are opaque; no names, emails, or credential material exist in public records.
- Eligibility is role/scope-specific and computed from bound evidence: Private Gold exposure blocks selection-content roles; same-suite result exposure is incompatible with result-blind content roles; stale or missing evidence blocks rather than degrades silently.
- Assignments never grant resource access; ACTIVE assignment state requires computed eligibility.
- Independence collisions across author/reviewer/adjudicator roles fail closed.
- The A13 firewall is default-deny across the three zones; `ALLOW_GRANT_CONSIDERATION` is not a grant; A7 deny/revoke/revalidation signals cannot be overridden by caller claims.

## 5. Finance governance (US6)

- Workload silence, `$0` labels, free tiers, and assumed volunteers never establish `NOT_REQUIRED`.
- Authorization approval is segregated from payee/beneficiary roles; self-approval is rejected; bounded scope and exact amounts are required.
- Only current `ACTIVE`, non-stale authorizations bound to the matching manifest identity may cover prospective commitments (`A14_AUTHORIZED_PASS`); genuine full-capacity manifests yield `A14_NOT_REQUIRED_PASS`.
- No payment execution, contract creation, vendor selection, or reconciliation action exists in the module.

## 6. Device, activation and manifest (US7)

- The five frozen targets (iPhone 17 Pro 12GB, iPhone 13 4GB, Galaxy A56 8GB, Galaxy A16 4GB, Intel N100 8GB envelope) share one GGUF artifact identity and one llama.cpp core revision per the frozen policy.
- The common protocol pins 8192/16384 context tokens, Q8_0 KV cache, batch 512 / ubatch 128, no cache reuse, five measured runs aggregated median-with-worst-case.
- The platform-native absolute 2 GiB (`2147483648` bytes) Core peak-memory hard ceiling applies to all targets; OS memory termination remains a hard failure below the ceiling.
- Package-byte thresholds and exact runtime build identities are intentionally unresolved (`null` / evidence fields): they are fail-closed prerequisites frozen before execution, never defaults chosen after results.
- Preflight distinguishes `HARD_FAIL` (ceiling exceeded, OS termination, crash) from `INCOMPLETE` (missing runs/targets/identity fields); incomplete is never silently favorable.
- A15 activation validation binds an exact prerequisite snapshot including the scientific T1/D34 records; blocked/stale/mismatched prerequisites block; caller-owned authorized claims are not trusted. Synthetic fixtures test semantics only.
- The Spec 005 manifest binds exact metrics-v2 catalog SHA, selection-quality contract identity, threshold/statistical design identities, device preflight PASS, and base-only candidate admission (Private Gold evidence prohibited). No Spec 004 projection exists without an explicitly authorized `AUTHORIZED_TO_CONSTRUCT` activation; even then it is `PRECOMPUTED_RESULTS_ONLY`.

## 7. Inherited canonical boundaries preserved

| Boundary | Disposition |
|---|---|
| Metrics V1 identity | `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a` unchanged |
| Metrics V2 identity | `bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b` (evidence-role-primary canonicalization) |
| Spec 002 safety gates | Hard gates remain noncompensable; no module alters them |
| Spec 003 lineage | Private Gold never parent/source; rights/privacy evidence required |
| Spec 004 harness | Comparison strategy/tie policy inherited verbatim; projection reuses existing tournament semantics |

## 8. Explicit non-execution scope

Nothing in this implementation downloads weights, loads models, runs inference, accesses benchmark payloads or Private Gold payloads, touches PHI, calls providers, provisions storage, spends money, engages contributors, selects vendors, executes devices, or activates real construction. Validators operate exclusively on repository JSON contracts and synthetic in-test fixtures.

## 9. Verification commands

```bash
python -m compileall -q src tests
python -m unittest tests.spec005.test_science tests.spec005.test_preconstruction -v
python -m unittest tests.spec005.test_personnel tests.spec005.test_access -v
python -m unittest tests.spec005.test_finance tests.spec005.test_device -v
python -m unittest tests.spec005.test_activation tests.spec005.test_manifest -v
python -m unittest discover -s tests -p "test_*.py"   # full offline regression
```

No network access, model runtime, benchmark payload, Private Gold payload, provider call, device runtime, or payment instrument is used by any command above.

## Implementation Evidence

*(appended only with actual verified evidence after independent exact-head review — see T049)*
