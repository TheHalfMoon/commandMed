# V5 S1 Colab optional dependency failure - 2026-10-04

Status: `COLAB_OPTIONAL_DEPENDENCY_BLOCKER_PRESERVED`.

At exact reviewed/pushed head `3236304f59d6715916a5886b9965b0a1bd908f4d`, Colab reproduced all 8,192 tasks, 32,768 candidate checks and every frozen preparation field except the generation-head annotation. The exact 12-file artifact, A=32/B=33, 593/768-token maximum, no truncation and unchanged task/prompt identities passed. Fresh `MODEL_LOAD` and `INFERENCE` preflights passed.

The native `Qwen3_5ForCausalLM` text path loaded with 752,393,024 bfloat16 parameters on the assigned Tesla T4. The completed mechanical smoke inference produced finite bfloat16 logits in 1.2567172439999013 seconds. After that, the required PEFT import failed because Colab preloaded `torchao` 0.10.0 whereas the pinned PEFT version requires a newer optional torchao integration. No adapter, backward benchmark, optimizer step, medical training, calibration analysis, margin or power result occurred. This is environment compatibility evidence, not a scientific failure or V5 support.

The original exported ZIP and console, load/memory observations, exact preflights, environment/model/tokenizer records, reproduced preparation and completed smoke output are preserved under `artifacts/v5/development/s1-colab-resource-qualification/torchao-import-failure-2026-10-04/`. Their exact bytes were verified outside ephemeral storage. Original flags remain unchanged; a separate export receipt records durability.

The prospective runtime repair removes the unused preinstalled optional quantization extension from this pure bfloat16 environment and verifies required PEFT imports before model load. The reusable notebook records the same setup. No quantization, kernel optimization, precision fallback, new model, altered task/interface, changed optimization budget or scientific-design change is admitted. Rebind the actual packages and obtain fresh complete preparation and preflight at a clean candidate boundary. Prior failures remain preserved, and PR #320 remains OPEN / DRAFT / UNMERGED.

The repair-only cell completed without loading a model: removal exit code 0 and a fresh-process required-import probe exit code 0. The exact `dependency-repair.json` SHA-256 `67344a8052b881fcfe5c0a5adccfafc4e501184860add413544ad797eb723d5b` was verified after export outside Colab. Required versions remain torch 2.11.0+cu130, transformers 5.18.0, tokenizers 0.23.2, PEFT 0.21.2 and NumPy 2.4.6. This is dependency evidence only; a new model run still requires complete fresh admission.
