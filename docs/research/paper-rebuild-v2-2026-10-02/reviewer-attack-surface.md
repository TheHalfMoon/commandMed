# Reviewer attack surface


This document converts predictable reviewer objections into experimental requirements.

1. **Why not use LM logits?** Use LM candidate-logit, structured-generation and post-hoc-probe controls.
2. **Is the head receiving extra supervision?** Match data, optimization and parameter/tuning budgets; report deviations.
3. **Is this just Visual Jev in medicine?** Require a replicated readout-by-objective interaction or a strong equivalence/negative result that changes architecture choice [@arxiv260925845].
4. **Does medical QA imply clinical utility?** No. State construct limits and avoid patient-benefit language.
5. **Are probabilities trustworthy?** Report proper scores, calibration diagnostics and selective risk separately; test shift.
6. **Did you tune CommandMed more than baselines?** Freeze and disclose per-method tuning budgets.
7. **Why Qwen?** Treat Qwen as one backbone factor; require an independent-family replication for general claims.
8. **Could gains be contamination?** Bind source identities, deduplicate where possible, quarantine tests, and report residual pretrained-model contamination risk.
9. **Why not a decision-only specialist?** Include a specialist/resource control if lawfully runnable; retain-generation claims require a shared-backbone comparison.
10. **What would change practice?** The paper passes the major-contribution gate only if results justify an architectural decision under reliability and retention constraints, not merely a new model name.
