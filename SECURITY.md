# Security Policy

commandMed treats AI-system security, medical safety, provenance, and deterministic authority as connected hard-gated concerns.

This repository is research software and is not currently authorized for patient-facing clinical deployment.

## Security scope

Security-relevant reports include, but are not limited to:

- direct or indirect prompt injection that crosses a protected boundary;
- authorization bypass;
- tool abuse, tool poisoning, tool shadowing, or tool-name confusion;
- secret, credential, data, or context exfiltration;
- unsafe command or code execution;
- SSRF, unsafe redirects, or unintended network access;
- privilege escalation or filesystem-scope escape;
- MCP / agent / skill / plugin supply-chain issues;
- model/runtime/provider substitution or integrity failures;
- provenance, artifact-hash, or release-integrity bypasses;
- sandbox escapes or unsafe dynamic-test behavior;
- deterministic medical-tool authority bypass;
- vulnerabilities that could expose PHI, protected evaluation material, or other sensitive data;
- security controls that fail open when evidence or authority is missing.

## Reporting

Do not publish exploit details, credentials, PHI, Private Gold content, protected benchmark payloads, or other sensitive operational material in a public issue.

Use GitHub private vulnerability reporting / Security Advisories when that feature is available for this repository.

If a private reporting channel is not available, open a minimal public issue that requests a private security contact **without** including exploit payloads, credentials, sensitive data, or step-by-step abuse instructions.

For non-sensitive security hardening proposals that do not expose a live vulnerability, a normal issue or pull request is appropriate.

## What to include

A useful report should provide the minimum information necessary to reproduce and triage safely:

- affected commit/revision;
- affected path/component;
- vulnerability class;
- preconditions;
- expected security boundary;
- observed boundary failure;
- minimal safe reproduction description;
- potential impact;
- whether network, credentials, model/runtime execution, PHI, or protected data are involved.

Do not attach real patient data or production credentials as proof.

## Safe reproduction rules

Unless a separately authorized security spec explicitly permits otherwise:

```text
PHI=PROHIBITED
PRIVATE_GOLD=PROHIBITED
REAL_CREDENTIALS=PROHIBITED
UNBOUNDED_NETWORK=PROHIBITED
DESTRUCTIVE_SIDE_EFFECTS=PROHIBITED
UNSANDBOXED_POC_EXECUTION=PROHIBITED
UNAUTHORIZED_MODEL_OR_PROVIDER_EXECUTION=PROHIBITED
```

Prefer synthetic fixtures, local deterministic tests, disposable sandboxes, least privilege, strict timeouts, explicit resource limits, and network-off execution.

Do not run vulnerability PoCs merely because an upstream donor project contains them.

## Security design principles

commandMed's preferred AI-security architecture is:

```text
DETERMINISTIC PRE-SCAN
-> VERSIONED RULE ENGINE
-> OPTIONAL AUTHORIZED MODEL-ASSISTED ANALYSIS
-> DETERMINISTIC FINDING NORMALIZATION
-> SECURITY HARD GATE
```

Critical findings are non-compensable. An aggregate score cannot erase credential exfiltration, unauthorized execution, patient-data exposure, deterministic medical-tool bypass, or release-provenance failure.

Network, credential, tool, and agent integrations should be deny-by-default and least-privilege unless a bounded spec proves a narrower requirement.

## Dependency and donor security

External source use is governed by [`docs/governance/external-code-adoption.md`](docs/governance/external-code-adoption.md).

Copied, adapted, or vendored code must retain exact source provenance and applicable license/NOTICE obligations and must receive commandMed-native security qualification before canonical admission.

Source qualification or Founder permission to use code is not itself a security result.

## Disclosure and remediation

Security fixes should preserve evidence and avoid history rewriting when possible. Use a bounded fix, focused regression tests, exact-head qualification, and append-only reconciliation when governance requires it.

Do not suppress or downgrade a real security finding merely to satisfy CI or release criteria.

## Medical-safety interaction

Some security defects are also medical-safety defects. For example, a tool-poisoning vulnerability that can alter a validated medication calculation is both a security failure and a clinical-safety failure. In such cases, all applicable hard gates must pass independently before the affected capability can be considered qualified.
