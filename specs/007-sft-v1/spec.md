# Spec 007 — SFT V1 (Minimal Multi-Role Supervised Fine-Tuning)

**Planning Branch**: `spec/007-specify`
**Created**: 2026-08-25
**Status**: Specification CANONICAL at PR #46 merge `645da20`; originally drafted under `AUTHORIZED_TO_SPECIFY` [**superseded 2026-08-26** — current stage is `AUTHORIZED_TO_CLARIFY` per the "Spec 007 clarification authorization record" in `specs/README.md`]
**Depends on**: Spec 003 `CLOSED_CANONICAL`, Spec 005 `CLOSED_CANONICAL`, Spec 006 `CLOSED_CANONICAL` (entry gate approved via the "Spec 007 specification authorization record" in `specs/README.md`)
**Lifecycle authority**: CURRENT=`AUTHORIZED_TO_CLARIFY` per `specs/README.md`; historical specification-artifact boundary=`SPECIFY ONLY`
**Execution authority**: NONE — no training run, model execution, weight access, benchmark payload access/execution, Private Gold/PHI access, device execution, provider generation, credential use, or spend is authorized by this specification.

> This specification defines the bounded problem for the minimal multi-role supervised fine-tuning candidate. It freezes what SFT V1 must prove, what it must not claim, and which inputs remain typed evidence prerequisites. It does NOT select a base model, a dataset, hyperparameters, or a budget, and it does not authorize any run.

## 1. Objective

Produce the first minimally adapted commandMed candidate: one compact base checkpoint — selected exclusively by the frozen tournament evidence from Specs 004–005 — supervised-fine-tuned on a small, verified, license-clean curriculum that adapts behavior across the three frozen role classes (`PATIENT_CAREGIVER`, `CLINICAL_PROFESSIONAL`, `LEARNER_RESEARCHER`) while preserving general capability, Arabic/English parity targets, tool/evidence grounding, and the Spec 006 behavioral-state safety boundary. Success is defined by the frozen evaluation protocol created before any run; no training result defines its own success.

## 2. Context and why this spec exists

Specs 001–005 froze evaluation, safety gates, data/license provenance, and the deterministic tournament control plane; Spec 006 made the interaction/tool safety boundary operable. The roadmap's next capability step is the first actually-trained candidate. Per D-001 (evaluation precedes training), T-001 (backbone winner decided only through the frozen tournament), D-003 (three training-role classes), FD-001 (permissive downstream release posture), and D-002/FD-002 (resource-based smallness on named devices), SFT V1 is deliberately **minimal**: fewer verified examples over large noisy synthetic corpora; no CPT (that is Spec 008's ablation); no distillation (Spec 009); no preference optimization; no RL. Every construction input passes the Spec 005 preconstruction control plane before any activation gate can open.

## User Scenarios & Testing

### User Story 1 — Role-adapted answering within the safety boundary (Priority: P1)

A frozen evaluation prompt drawn from the V1 metric catalog strata is answered by the SFT candidate in the role-appropriate register for its routed class, without violating any Spec 002 hard gate or Spec 006 behavioral-state rule.

**Why this priority**: role adaptation without safety regression is the core purpose of SFT V1.

**Independent Test**: offline fixture evaluation replays the candidate's recorded outputs through the canonical Spec 002 policy/scope **prequalification adapter first**, then delegates to `evaluate_hard_gates` within that path, with the Spec 006 scaffold precedence applied inside the same canonical qualification flow; any emergency/escalation miss, medication-critical error, state override, or skipped-prequalification shortcut fails the story regardless of quality metrics.

### User Story 2 — Capability preservation under specialization (Priority: P1)

General reasoning, instruction following, Arabic clinical strata, tool use, and safety checks are re-run after adaptation and compared to the base checkpoint's tournament-era baselines; regressions beyond pre-frozen tolerance fail.

**Why this priority**: invariant 6 requires regression checking after specialization; specialization gains cannot buy hidden losses.

**Independent Test**: paired per-stratum deltas between base checkpoint and SFT candidate on the frozen metric catalog with pre-registered non-inferiority margins; every delta outside margin is a hard failure, never averaged away.

### User Story 3 — Provenance-complete, quarantine-clean construction (Priority: P1)

Every SFT example carries provenance, license status, content identity/hash, split identity, contamination status, and verification state; Gold/holdout artifacts are provably excluded from all training, selection, and tuning surfaces.

**Why this priority**: invariants 3–4 and Spec 003 make lineage machine-verifiable; an unprovable dataset invalidates every downstream claim.

**Independent Test**: deterministic validators replay the construction snapshot: each record validates against the Spec 003 contract; contamination/quarantine cross-checks return zero violations; missing identity on any record fails the story.

### Edge Cases

- What if the tournament has not produced a qualified winner? → SFT V1 remains unexecutable; base-checkpoint binding stays a typed `NEEDS_EVIDENCE` prerequisite.
- What if Arabic curriculum coverage cannot meet parity strata? → scope narrows to English-first with explicit Arabic gap reporting; Arabic claims are dropped rather than simulated.
- What if license compatibility of any curriculum source conflicts with FD-001? → the source is rejected outright; substitution follows the same verification path.
- What happens on partial hard-gate failure? → FD-005 policy applies at release review; no hidden downgrade inside SFT V1 itself.

## Requirements

### Functional Requirements

- **FR-001**: System MUST define the SFT V1 curriculum as a versioned, identity-bound set of examples spanning medical fundamentals/factual accuracy, clinical problem representation, differential reasoning, active information acquisition, patient explanation, professional workflow, evidence use, uncertainty/abstention, tools/structured outputs, Arabic/English clinical language, and adversarial/unsafe cases — with per-class (`PATIENT_CAREGIVER` / `CLINICAL_PROFESSIONAL` / `LEARNER_RESEARCHER`) routing recorded per example.
- **FR-002**: System MUST bind the base checkpoint exclusively to tournament evidence: exact checkpoint identity, license compatibility with FD-001, and qualification manifest from the frozen Specs 004–005 protocol. [CLARIFIED as typed prerequisite: the winning checkpoint remains `NEEDS_EVIDENCE` until the authorized tournament execution produces it — this specification MUST NOT name a candidate family as selected]
- **FR-003**: System MUST enforce Gold/holdout quarantine over the canonical quarantine source set defined by `eval_contract.validate` (`COMMANDMED_CLINICAL_GOLD`, `COMMANDMED_ARABIC_GOLD`, `COMMANDMED_MULTIMODAL_GOLD`, `CALIBRATION_HOLD_OUT_SPLIT`, `MODEL_SELECTION_DEV_SET`, `PUBLIC_BENCHMARK_DEV_SPLITS`, `HELD_OUT_SYNTHETIC_PILOT_CASES`, `VERIFIED_DEV_SPLIT`, and the other members of that frozen set), governed by its purpose→allowed-sources policy — including the rule that `CALIBRATION_HOLD_OUT_SPLIT` may be used only for calibration. These artifacts are structurally excluded from curriculum construction, SFT training, hyperparameter and recipe selection, checkpoint selection, and every other selection or tuning surface, with machine-verifiable exclusion evidence for each surface.
- **FR-004**: System MUST require every curriculum record AND every evaluation asset consumed by the frozen protocol replay (metric inputs, replay fixtures, threshold records) to satisfy the Spec 003 provenance contract (source authority, license, content SHA-256, split identity, contamination status, `source_verification_status`, review/adjudication state) before admission, failing closed otherwise.
- **FR-005**: System MUST freeze the evaluation protocol BEFORE any run: the V1 metric catalog, hard gates, statistical metrics, stratification (including Arabic strata per master plan §13), sample-size rationale, and review-threshold margins from Specs 001–002 apply unchanged; SFT-specific acceptance thresholds are frozen as versioned records prior to activation.
- **FR-006**: System MUST represent the training configuration (role mix ratios, sequence budget, adapter/full-update decision, optimizer class, seeds) as a versioned preconstruction record validated by the Spec 005 control plane, with every unresolved numeric left as `NEEDS_EVIDENCE` rather than placeholder fiction. [CLARIFIED boundaries resolved here; exact values are later-stage evidence]
- **FR-007**: System MUST keep Spec 006's behavioral states intact: the SFT candidate is evaluated through the same fixture protocol, and generative adaptation MUST NOT weaken emergency/escalation precedence, abstention, or tool-routing determinism.
- **FR-008**: System MUST treat spend/compute as gated: any run requires the Spec 005 finance/engagement authorization records bound to a real budget estimate, and CURRENT_AUTHORIZED_SPEND_USD=0 until separately authorized. [typed `NEEDS_EVIDENCE`: budget determination workload]

*Non-compensable invariants*: hard safety gates are zero-tolerance; averages never compensate critical failures; quarantine violations are absolute failures.

### Key Entities

- **Curriculum Example**: identity-bound training record with role class, stratum tags, language tags, provenance bundle, license, contamination status, review state.
- **Base Checkpoint Binding**: tournament-evidence-bound model identity + license posture + device-tier fit note.
- **Training Configuration Record**: versioned preconstruction artifact (mix ratios, budgets, seeds, adapter decision) passing Spec 005 validators.
- **Evaluation Binding**: pointer into the frozen V1 metric catalog + SFT acceptance thresholds frozen pre-run.
- **Run Manifest**: (later stage) activation-gated record tying checkpoint + config + data snapshot + eval protocol into one reproducible unit, and carrying the identity-bound Spec 005 **A14 finance authorization reference** (requirement-manifest identity, budget estimate, and `CURRENT_AUTHORIZED_SPEND_USD` snapshot) so activation validates A14 against the exact run — or A14 is validated independently against the run by the activation gate before any execution.

## Success Criteria

### Measurable Outcomes

- **SC-001**: 100% of admitted curriculum records AND evaluation assets carry complete Spec 003 provenance bundles; zero records or assets admitted fail-closed.
- **SC-002**: Zero Gold/holdout artifacts present in ANY FR-003 surface — curriculum construction, SFT training input assembly, hyperparameter/recipe selection, checkpoint selection, and every other selection or tuning surface enumerated there — proven by replayable per-surface exclusion evidence; 'construction surface' in this specification means exactly that full FR-003 surface set, never a subset.
- **SC-003**: All hard safety gates evaluate **PASS** on the candidate's frozen evaluation replay through the canonical qualification path. Any gate returning `INSUFFICIENT_EVIDENCE` is surfaced explicitly as **non-qualification** of the candidate (fail-closed per Spec 002), never accepted as success; zero silent or averaged failures.
- **SC-004**: Base-vs-SFT paired deltas are computed on the full frozen stratification with pre-registered margins; out-of-margin regressions are surfaced as failures, never averaged.
- **SC-005**: The entire specify→construction→evaluation pipeline runs offline-deterministically at the validator level (`pytest -q`) AND passes one composed fail-closed validator check spanning the full path — covering model weights access, PHI, credentials, provider APIs, network access, and spend — such that any prohibited-surface touch fails closed; none of these surfaces is required or permitted until separately authorized gates open.

## Assumptions

- The three role classes from D-003 are sufficient granularity for V1; finer slices are evaluation-only.
- A qualified tournament winner will eventually exist; until then SFT V1 stays in preconstruction-only mode without blocking repository work.
- Arabic depth beyond measured-parity reporting belongs to Spec 013; SFT V1 carries the strata, not the deepening program.
- Compute policy constraints (free/low-cost tiers) shape budgets but do not appear as fabricated numbers here.

## Exclusions

- Continued pretraining (Spec 008 ablation), distillation (Spec 009), RLVR (Spec 010), DPO/preference optimization, quantization/device work (Spec 012).
- Selecting or announcing a backbone winner; executing the live tournament; downloading or loading weights.
- Constructing Private Gold; accessing PHI or restricted clinical datasets; sending data to third-party APIs.
- Any training run, provider generation, or spend — each requires its own founder authorization plus Spec 005 finance gates.
- Multimodal adaptation (Spec 014), human evaluation programs (FD-003 / Spec 015).

## Exit Evidence

Exit from the specification stage requires ALL of the following, merged canonically:

1. This `spec.md` passing static analyze with CRITICAL=0 / HIGH=0 / MEDIUM=0 and no constitution violation.
2. Independent exact-head review of the specification head reporting MATERIAL_BLOCKER=NO.
3. Every hard FR above is classified clause-completely with no silent gaps:
   - **FR-001** — frozen: role-class routing from decision-register D-003; curriculum domains from the canonical master-plan post-training list (§10); Arabic/English scope from §13 strata; adversarial/unsafe cases from AGENTS.md safety invariants.
   - **FR-002** — mixed: qualification-manifest *schema* frozen from Specs 004–005; winner checkpoint identity `NEEDS_EVIDENCE` (kind: authorized tournament execution result; owner: tournament lifecycle); `FD-001` license compatibility of that checkpoint `NEEDS_EVIDENCE` (kind: per-checkpoint lineage/license verification under FD-001 posture; owner: planning-stage license review).
   - **FR-003** — frozen from AGENTS.md invariants 3–4 + the canonical quarantine source matrix in `eval_contract.validate`.
   - **FR-004** — frozen from the Spec 003 contract.
   - **FR-005** — frozen from Specs 001–002 metric/gate contracts.
   - **FR-006** — boundaries frozen here; exact numerics `NEEDS_EVIDENCE` (kind: preconstruction determination records; owner: planning stage).
   - **FR-007** — frozen from the Spec 006 boundary + scaffold validators.
   - **FR-008** — `NEEDS_EVIDENCE` (kind: Spec 005 A14 budget-determination workload; owner: finance workload + founder spend gate).
4. Baseline suite unchanged (`pytest -q` 627+128 PASS, `compileall` PASS, `git diff --check` PASS) — specifications add no runtime code.
5. Registry updated to the next lifecycle stage only via the separate founder authorization record.

## Lifecycle note

[Historical snapshot at specification merge: this spec was `AUTHORIZED_TO_SPECIFY`. **Superseded 2026-08-26** — the founder approved the clarify stage per the "Spec 007 clarification authorization record" in `specs/README.md`, which is the authoritative current authority. Clarification advances only to a separately authorized planning step. Implementation start and any run require further explicit founder authorization recorded there. Model selection remains reserved to FOUNDER+CHATGPT with `BACKBONE_WINNER=NEEDS_EVIDENCE`.]
