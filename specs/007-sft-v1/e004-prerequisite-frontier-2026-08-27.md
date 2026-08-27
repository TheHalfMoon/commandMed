# E004 Prerequisite Frontier — 2026-08-27

**Spec:** 007 SFT V1
**Task:** E004
**Assessment type:** post-blocker dependency / authority audit
**Canonical audit base:** `222d63f3f52f6998a377b435972ee3c58f1893f6`
**Canonical audit base tree:** `167e181f7456add142a5dfed7aa30ff96b3a92ec`
**E004 state:** `BLOCKED_PREFLIGHT`
**Execution performed by this audit:** `NO`

## Purpose

PR #63 canonically established that E004 is blocked before execution. This follow-up audit identifies the earliest blockers that can and cannot be resolved under current authority. It does not convert any missing scientific, provenance, contamination, personnel, finance, runtime, artifact, or device evidence into PASS.

The controlling rule remains:

```text
E003_AUTHORITY=EXISTS
E004_AUTHORITY=AUTHORIZED_BY_E003_SUBJECT_TO_PREFLIGHT
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Audit conclusion

E004 is not blocked merely by missing record files. The current dependency frontier contains four different blocker classes:

1. real external scientific/governance evidence that cannot be fabricated;
2. separate access/authority decisions not granted by E003;
3. closed-Spec control-plane inconsistencies that require separately authorized corrective maintenance;
4. frozen artifact/runtime constraints that make the current full tournament impossible under the existing artifact allowlist.

No current repository-only action can make A15 PASS without first resolving these classes.

## 1. Scientific threshold and statistical-design frontier

The canonical Spec 005 Session 9 Q5 matrix remains authoritative for readiness:

```text
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO
```

The six hard-gate population thresholds remain dependent on exact identity-bound evaluation suites, clinical review authority, statistical review authority, metric-specific numeric methods/inputs, uncertainty/confidence choices where applicable, and sample-size/power derivations. Architecture and validators are not evidence for those values.

`FD-004` remains `FOUNDER_REQUIRED` for the benign-case over-triage product/ethics posture. It must not be inferred from candidate results or another project.

```text
SCIENTIFIC_THRESHOLD_FRONTIER=EXTERNAL_EVIDENCE_REQUIRED
STATISTICAL_DESIGN_FRONTIER=EXTERNAL_EVIDENCE_REQUIRED
FD004_FRONTIER=FOUNDER_DECISION_REQUIRED
REPOSITORY_MAY_INVENT_VALUES=NO
```

## 2. Selection-source contamination authority sequencing gap

Current canonical selection evidence is contamination-incomplete. In particular, the MedXpertQA text development slice retains:

```text
MEDXPERTQA_TEXT_DEV_PURPOSE=CHECKPOINT_SELECTION
MEDXPERTQA_TEXT_DEV_CONTAMINATION_GATE=INCOMPLETE
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=NO_WHILE_CONTAMINATION_GATE_INCOMPLETE
```

The current E003 benchmark boundary permits payload access only after the exact public/ungated input is provenance-, license-, purpose-, and contamination-qualified for selection use. However the frozen A11 contamination design states that actual contamination assessment itself requires separate assessment payload-access and execution authority bound to the exact suite/candidate/candidate-corpus/method identities.

No separate current A11 contamination-assessment payload-access/execution authorization was found in the canonical current-state authority summary.

Therefore E003 alone cannot be used to open an unresolved selection payload merely in order to create the contamination evidence that E003 requires before opening that payload.

```text
SELECTION_CONTAMINATION_STATE=UNRESOLVED
E003_SELECTION_PAYLOAD_ACCESS_BEFORE_CONTAMINATION_PASS=UNAUTHORIZED
A11_ASSESSMENT_AUTHORITY_CURRENTLY_BOUND=NO
CONTAMINATION_ASSESSMENT_FRONTIER=SEPARATE_AUTHORITY_REQUIRED
```

This is an authority-sequencing blocker, not a contamination PASS or FAIL finding.

## 3. Device preflight circular dependency

Canonical E003 requires the A15/pre-execution state to PASS before the first device-qualification run.

The canonical Spec 005 manifest validator, however, requires:

```text
manifest.device_protocol_identity.preflight_state=PREFLIGHT_PASS
```

and `src/commandmed/spec005/device.py` can return `PREFLIGHT_PASS` only when all five target evidence records exist with the required measured-run evidence. The validator requires exactly five measured runs per target and treats missing target/run/runtime evidence as incomplete.

This creates a closed loop under the current contracts:

```text
A15/PREFLIGHT PASS
  requires DEVICE PREFLIGHT PASS

DEVICE PREFLIGHT PASS
  requires measured device qualification runs

E003
  forbids first device qualification run before A15/PREFLIGHT PASS
```

Therefore the first real device qualification run cannot occur without violating one side of the current canonical protocol.

A safe repair would need to distinguish a **pre-execution device readiness** state (exact artifact/runtime/build/tool/signal/protocol identities, no measured result claim) from the **post-execution device qualification result** (five measured runs and numeric/hard-failure evidence). That is a corrective-maintenance design candidate only; this audit does not implement or authorize it.

```text
DEVICE_GATE_GRAPH=CIRCULAR
DEVICE_EXECUTION_NOW=PROHIBITED
SILENTLY_TREAT_MISSING_RUNS_AS_PREFLIGHT_PASS=PROHIBITED
CORRECTIVE_MAINTENANCE_REQUIRED=YES
```

## 4. Frozen artifact authority blocks full GGUF device qualification

E001 freezes three PRIMARY candidates plus one CONTROL. E002 permits source-weight access for all four but permits byte acquisition of only two exact preconverted GGUF artifacts:

```text
PRECONVERTED_ARTIFACT_ALLOWLIST_COUNT=2
```

The two allowlisted artifacts are the Qwen3 0.6B and Qwen3.5 0.8B entries. E002 explicitly records the Granite GGUF feasibility artifact as unauthorized for byte acquisition and records no preconverted CONTROL binding. E002 also prohibits expanding the allowlist, while current authority keeps:

```text
MODEL_CONVERSION_AUTHORITY=NONE
```

The frozen device protocol requires one shared GGUF model identity across all five targets for a candidate. Granite is a frozen PRIMARY candidate and therefore cannot currently complete that GGUF device path under the existing allowlist. The CONTROL also has no preconverted binding; whether the CONTROL requires the same device evidence for its opportunity-cost role must remain governed by the frozen protocol rather than assumed here.

The two allowlisted Qwen artifacts are not automatically final tournament runtime bindings merely because acquisition is authorized: E002 explicitly preserves their E001 feasibility/direct-metadata labels and requires a later exact runtime-artifact binding before execution.

```text
GRANITE_DEVICE_GGUF_ACQUISITION_AUTHORITY=NONE
CONTROL_PRECONVERTED_BINDING=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
ARTIFACT_SUBSTITUTION=PROHIBITED
FULL_FROZEN_PRIMARY_DEVICE_QUALIFICATION_UNDER_CURRENT_ARTIFACT_AUTHORITY=BLOCKED
```

Resolving this requires a new explicit artifact/conversion authority decision; E004 must not expand E002 by implication.

## 5. Closed-Spec device contract inconsistencies

Two repository-actionable inconsistencies were found between frozen Spec 005 decisions and the canonical device contract:

### 5.1 Package envelope

The Spec 005 clarification freezes the mass-reach envelope as:

```text
HARD_CAP=700 MiB
ENGINEERING_TARGET=600 MiB
STRETCH_TARGET=500 MiB
```

but `data/spec005/device_qualification_contract.json` currently stores:

```text
package_hard_cap_bytes=null
package_target_bytes=null
package_stretch_bytes=null
```

The exact semantic scope (complete minimum Core bundle versus model artifact component) must be reconciled rather than filling fields mechanically.

### 5.2 Warm-up semantics

The frozen Spec 005 decision `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` states that each measured run starts from a fresh process, includes a fresh model load, contains exactly one measured request after load, and uses **no non-measured warm-up requests**.

The canonical device JSON currently states:

```text
warmup_runs_required_before_measurement=true
```

That is not safe to reinterpret at execution time. The contract and tests must be reconciled under separately authorized corrective maintenance before device execution.

```text
DEVICE_CONTRACT_RECONCILIATION_REQUIRED=YES
E004_MAY_PATCH_CLOSED_SPEC005_WITHOUT_AUTHORITY=NO
```

## 6. No canonical live execution surface is currently bound

Spec 004 is intentionally fixture-only and fixes:

```text
EXECUTION_MODE=PRECOMPUTED_RESULTS_ONLY
```

Its implementation explicitly exposes no model, benchmark, network, subprocess, credential, or provider execution surface.

Spec 005 is also canonically closed as an offline deterministic **preparation/control plane**, not a real model runner. Its Spec 004 projection emitted by `src/commandmed/spec005/manifest.py` is still:

```text
execution_mode=PRECOMPUTED_RESULTS_ONLY
```

Repository search at this audit base found no canonical E004 runner, llama.cpp command manifest, model-inference execution module, or equivalent identity-bound runtime surface that converts an A15 PASS into reproducible raw candidate outputs.

E003 grants bounded authority to execute the frozen tournament, but authority alone does not define a reproducible execution mechanism. An ad hoc shell command, mutable runtime invocation, or unrecorded manual process would bypass the repository's exact-identity and audit requirements.

```text
LIVE_E004_EXECUTION_AUTHORITY=CONDITIONAL_E003
LIVE_E004_CANONICAL_EXECUTION_SURFACE=NOT_FOUND
AD_HOC_UNBOUND_EXECUTION=PROHIBITED
EXECUTION_SURFACE_FRONTIER=REPOSITORY_DESIGN_OR_IMPLEMENTATION_REQUIRED
```

Whether that surface belongs in a narrowly amended Spec 005 execution adapter or an E004-specific bounded execution spec/task must be decided and canonically authorized before implementation.

## 7. Runtime/build/device evidence remains real evidence

Even after the structural issues above are repaired, real device readiness still requires exact immutable runtime/build/tool identities and physical evidence where the protocol requires it. Current unresolved examples include the exact llama.cpp core revision, concrete platform build manifests/toolchains/wrappers, thermal and energy signal/tool identities, and target-specific device evidence.

The Windows memory method is unresolved in the current contract, but the low-resource laptop target allows a Windows 11 x64 **or equivalent Linux x86-64** path. Therefore the Windows-specific method is a blocker only if the Windows execution path is selected; it must not be overstated as an unconditional blocker if a qualified Linux N100 path is canonically bound instead.

No physical-device availability, exact build identity, or measurement PASS is inferred by this audit.

## 8. A7/A13/A14 and real-world resource evidence

The canonical control plane rejects assumptions that `$0`, a free tier, or presumed volunteer capacity establish an A14 PASS. Personnel eligibility/independence and access state also require real bound evidence where applicable.

Current E003 permits no spend and no credential/gated-asset access. Therefore a real preconstruction snapshot must prove that the exact tournament can be completed with existing authorized zero-spend resources and with any required personnel/access evidence; otherwise it remains blocked.

```text
A14_ASSUMED_ZERO_COST_EQUALS_PASS=NO
PERSONNEL_IDENTITY_MAY_BE_FABRICATED=NO
ACCESS_GRANT_MAY_BE_INFERRED=NO
```

## 9. Corrective-maintenance authority boundary

Spec 005 is `CLOSED_CANONICAL`. `AGENTS.md` states that the active bounded spec is the execution authority and adjacent roadmap/spec work is not implicitly authorized.

The current active frontier is Spec 007 E004. No current canonical record found by this audit grants a bounded corrective-maintenance implementation authority to mutate the closed Spec 005 device/manifest control plane or to add a live execution surface there.

Therefore this audit may identify and specify defects, but it must not silently repair closed-Spec implementation under E004 authority.

```text
SPEC005_CORRECTIVE_MAINTENANCE_AUTHORITY=NOT_FOUND
CURRENT_E004_AUTHORITY_IMPLIES_SPEC005_CODE_MUTATION=NO
```

A separate bounded authorization is required before code/contract repair.

## 10. Dependency-safe remediation order

The earliest safe order is:

1. **Corrective-maintenance decision** — separately authorize a bounded repository repair for the closed Spec 005/E004 interface, limited to pre-execution-vs-post-execution device semantics, exact device-contract reconciliation, and a reproducible live-E004 execution surface if governance assigns it there. No model/device/benchmark execution is part of the repair.
2. **Artifact authority decision** — separately bind an exact executable GGUF path for every frozen candidate that requires device qualification, or separately authorize a bounded conversion path. Do not expand E002 or conversion authority implicitly.
3. **Contamination-assessment authority** — separately authorize only the exact public/ungated assessment inputs/methods needed to create candidate-bound contamination evidence; this is not selection execution authority.
4. **Scientific/governance evidence** — bind exact evaluation-suite identities, clinical/statistical authorities, threshold/margin values, uncertainty methods, N/power/allocation identities, and FD-004 where applicable.
5. **Runtime/resource preconstruction** — freeze exact runtime/build/tool/signal identities, physical target bindings, personnel/access/finance evidence, and zero-spend resource availability.
6. **Construct real A1–A14 snapshot** — only from complete, current, identity-bound prerequisite records.
7. **Separate A15 activation** — bind the exact ready snapshot and current canonical commit.
8. **Construct exact E004 tournament manifest/admission records** — no substitution or membership drift.
9. **Run final pre-execution validation** — any `BLOCKED`, `INCOMPLETE`, `NEEDS_EVIDENCE`, stale, mismatched, or unauthorized state fails closed.
10. **Execute E004** only after PASS. E004 produces evidence only; E005 remains Founder+ChatGPT.

## 11. Current STOP state

The repository has reached the furthest state possible without new authority or real external evidence on the blockers above.

This is not project completion and not E004 completion.

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
A15_REAL_ACTIVATION=ABSENT
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E005_REACHABLE=NO
BACKBONE_WINNER=NEEDS_EVIDENCE

NEXT_REPOSITORY_DECISION_1=SPEC005_E004_CORRECTIVE_MAINTENANCE_AUTHORIZATION
NEXT_REPOSITORY_DECISION_2=FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION
NEXT_REPOSITORY_DECISION_3=CONTAMINATION_ASSESSMENT_ACCESS_EXECUTION_AUTHORIZATION
NEXT_EXTERNAL_EVIDENCE=CLINICAL_STATISTICAL_RUNTIME_DEVICE_PERSONNEL_RESOURCE_BINDINGS
```

No model, benchmark payload, device, conversion, training, credential, gated asset, Private Gold, PHI, provider generation, or spend execution occurred in producing this audit.
