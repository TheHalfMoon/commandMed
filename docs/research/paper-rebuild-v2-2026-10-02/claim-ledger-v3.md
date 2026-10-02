# Claim ledger v3 — CommandMed Contract

All scientific claims begin `UNPROVEN`.

| ID | Candidate claim | Status | Required evidence | Reject / narrow if |
|---|---|---|---|---|
| C3-001 | Decision distributions are materially unstable under semantics-preserving interface transformations in the studied medical tasks. | UNPROVEN | preregistered E-family transforms, CED/CAFR, paired CIs | instability is negligible under frozen meaningful threshold |
| C3-002 | Distribution-level contract metrics reveal failures not captured by top-1 accuracy alone. | UNPROVEN | paired examples where argmax is stable but distribution/action threshold changes | metrics are redundant with ordinary accuracy/order sensitivity |
| C3-003 | CRDI improves contract equivariance over matched LM-logit, typed-head and permutation-aware baselines. | UNPROVEN | budget-matched confirmatory comparison | gain disappears after capacity/tuning controls |
| C3-004 | CRDI preserves semantic responsiveness to evidence-changing interventions rather than becoming indiscriminately invariant. | UNPROVEN | C-family intervention strata, proper scores, RR/CTG/SRT | invariance regularization suppresses legitimate evidence response |
| C3-005 | Contract improvement does not require unacceptable loss of decision quality or retained autoregressive competence. | UNPROVEN | noncompensable decision/retention gates | robustness gain is purchased by material capability loss |
| C3-006 | The central effect replicates across at least two backbone families. | UNPROVEN | independent-family replication | effect is Qwen-specific or directionally inconsistent |
| C3-007 | The contract framework adds scientific value beyond prior MCQ selection-bias and metamorphic-testing work. | UNPROVEN | final novelty refresh + reviewer-attack matrix | closest prior work already covers same joint contract |
| C3-008 | CommandMed is clinically safe/effective. | FORBIDDEN_WITH_CURRENT_DESIGN | prospective clinical validation outside this bounded study | always with current evidence |

Promotion: `HYPOTHESIS -> DESIGN -> DEVELOPMENT_RESULT -> CONFIRMATORY_RESULT -> REPLICATED_RESULT -> PAPER_CLAIM`.