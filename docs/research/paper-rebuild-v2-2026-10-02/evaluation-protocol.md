# Prospective evaluation protocol


Status: DRAFT FOR SCIENTIFIC FREEZE. No model execution is authorized.

## Primary question

Does a native typed decision readout provide a measurable benefit after decision supervision, maintenance supervision, backbone state and tuning budget are matched, and what capability interference is introduced by each adaptation strategy?

## Factorial design

Primary factors: readout = LM candidate logits vs typed head; adaptation = frozen vs decision-only vs decision-plus-language-maintenance; backbone family = Qwen-family small model vs an independently structured second family when lawfully runnable. The primary inference concerns readout-by-adaptation interaction, not a single best checkpoint.

## Decision scorecard

Primary metrics: negative log-likelihood and Brier score. Secondary metrics: accuracy, class-conditional reliability, adaptive calibration diagnostics, invalid-output rate, risk-coverage curve and AURC. ECE is reported only with binning sensitivity; it is not the sole calibration endpoint [@arxiv170604599; @arxiv190109192].

## Capability-retention scorecard

Evaluate medical/biomedical QA, nonmedical retained competence, and bounded generation quality separately. PubMedQA, MedQA and MedMCQA are candidate task families only after rights admission; examination accuracy is not a clinical-outcome claim [@arxiv190906146; @arxiv200913081; @arxiv220314371].

## Comparator discipline

Every readout comparison uses the same underlying representation and the same eligible examples. Post-hoc probes on frozen adapted backbones separate representational change from head-fitting benefit. Structured autoregressive answer generation remains a baseline. Visual Jev and Dyad are direct neighboring controls [@arxiv260925845; @arxiv260936116].

## Noncompensable gates

A mean capability gain cannot compensate for a prespecified safety or calibration failure. No clinical-safety conclusion follows from benchmark success. Medical image generation is prospectively excluded from this primary study.
