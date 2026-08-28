# E004 GitHub-Hosted Runner Static Evidence — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Record class:** append-only read-only public-environment evidence  
**Canonical repository base:** `6b0ca9d654b5302d95695ca46f4c669164543434`  
**Controlling environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority effect:** NONE  
**Workflow dispatch performed:** NO  
**Runner job executed:** NO  
**Build executed:** NO  
**Model/device/benchmark operation:** NO  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

The current E004 frontier explicitly permits read-only runtime/tool metadata research without model or device execution. This record binds current public GitHub evidence for the already-selected standard GitHub-hosted `ubuntu-24.04` runner class.

It is intentionally **not** runtime qualification. GitHub-hosted runner images are rolling provider-managed images, and the exact image assigned to a future authorized run is not known until that run starts. Therefore this record may reduce uncertainty but cannot satisfy runtime-only preflight assertions.

```text
STATIC_ENVIRONMENT_RESEARCH_ONLY=YES
RUNTIME_PREFLIGHT_EXECUTED=NO
RUNTIME_PREFLIGHT_PASS=NOT_CLAIMED
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 2. Primary public sources

### 2.1 GitHub-hosted runner reference

Primary documentation:

```text
https://docs.github.com/en/actions/reference/runners/github-hosted-runners
```

Observed on 2026-08-28, the public-repository standard-runner table documents `ubuntu-24.04` as an x64 Linux virtual machine with:

```text
PUBLIC_STANDARD_RUNNER_LABEL=ubuntu-24.04
PUBLIC_STANDARD_RUNNER_CPU=4
PUBLIC_STANDARD_RUNNER_MEMORY_GB=16
PUBLIC_STANDARD_RUNNER_STORAGE_GB=14
PUBLIC_STANDARD_RUNNER_ARCHITECTURE=x64
PUBLIC_STANDARD_RUNNER_PRICING=FREE_AND_UNLIMITED_FOR_PUBLIC_REPOSITORIES
```

The same GitHub documentation states that Linux GitHub-hosted virtual machines run with passwordless `sudo`.

```text
GITHUB_DOCUMENTED_PASSWORDLESS_SUDO=YES
```

This evidence applies to the standard GitHub-hosted runner class already selected by canonical Decision B. It does not authorize larger runners, private-runner billing, self-hosted runners, installation, procurement, or spend.

### 2.2 GitHub runner-image inventory

Primary repository:

```text
https://github.com/actions/runner-images
```

Exact current source commit observed for `images/ubuntu/Ubuntu2404-Readme.md`:

```text
RUNNER_IMAGES_REPOSITORY=actions/runner-images
RUNNER_IMAGE_README_PATH=images/ubuntu/Ubuntu2404-Readme.md
RUNNER_IMAGE_README_COMMIT=cbb8df97e1dd32af7cb23a90590f12734ec11d0b
RUNNER_IMAGE_README_COMMIT_DATE=2026-08-28T08:11:17Z
RUNNER_IMAGE_README_UPDATE_SUBJECT=Updating readme file for ubuntu24 version 20260823.283.1 (#14615)
```

At that exact source commit, the published Ubuntu 24.04 image inventory reports:

```text
PUBLISHED_OS_VERSION=24.04.4_LTS
PUBLISHED_KERNEL_VERSION=6.17.0-1022-azure
PUBLISHED_IMAGE_VERSION=20260823.283.1
PUBLISHED_SYSTEMD_VERSION=255.4-1ubuntu8.17
```

## 3. Published tool evidence relevant to the qualified workflow

The exact current runner-image inventory explicitly publishes the following relevant tools or packages:

```text
BASH_PUBLISHED=YES
BASH_PUBLISHED_VERSION=5.2.21(1)-release

GIT_PUBLISHED=YES
GIT_PUBLISHED_VERSION=2.55.0

CMAKE_PUBLISHED=YES
CMAKE_PUBLISHED_VERSION=3.31.6

NINJA_PUBLISHED=YES
NINJA_PUBLISHED_VERSION=1.13.2

GNU_CPP_PUBLISHED=YES
GNU_CPP_PUBLISHED_VERSIONS=12.4.0,13.3.0,14.2.0

GCC_APT_PACKAGE_PUBLISHED=YES
GCC_APT_PACKAGE_VERSION=4:13.2.0-7ubuntu1

GPP_APT_PACKAGE_PUBLISHED=YES
GPP_APT_PACKAGE_VERSION=4:13.2.0-7ubuntu1

PYTHON_PUBLISHED=YES
BASE_PYTHON_PUBLISHED_VERSION=3.12.3

COREUTILS_APT_PACKAGE_PUBLISHED=YES
COREUTILS_APT_PACKAGE_VERSION=9.4-3ubuntu6.2

FILE_APT_PACKAGE_PUBLISHED=YES
FILE_APT_PACKAGE_VERSION=1:5.45-3build1

SUDO_APT_PACKAGE_PUBLISHED=YES
```

The published inventory therefore provides useful current evidence for many of the workflow's fail-closed required tools, including Bash, Git, CMake, Ninja, C/C++ toolchains, Python, coreutils-family commands, `file`, and `sudo`.

This remains inventory evidence only. The exact executable selected by `command -v`, its fully resolved path, file SHA-256, and any provider-side update between this snapshot and a future run remain runtime evidence.

## 4. What public inventory does not prove

The published `Ubuntu2404-Readme.md` inventory does not explicitly enumerate `unshare` or `setpriv`, and repository code search under `actions/runner-images/images/ubuntu` does not produce an explicit `util-linux` inventory binding.

Therefore this record deliberately does **not** claim either command is available on the eventual runner:

```text
UNSHARE_STATIC_INVENTORY_EVIDENCE=NOT_EXPLICITLY_BOUND
SETPRIV_STATIC_INVENTORY_EVIDENCE=NOT_EXPLICITLY_BOUND
UNSHARE_RUNTIME_AVAILABILITY=NEEDS_RUNTIME_EVIDENCE
SETPRIV_RUNTIME_AVAILABILITY=NEEDS_RUNTIME_EVIDENCE
```

The qualified live workflow already fails closed before configure/build if either command is missing.

Similarly, GitHub's passwordless-`sudo` documentation does not prove that the exact future job can successfully create the required network namespace. The exact operation remains runtime-only evidence:

```text
PASSWORDLESS_SUDO_CLASS_DOCUMENTED=YES
SUDO_N_UNSHARE_NET_RUNTIME_SUCCESS=NEEDS_RUNTIME_EVIDENCE
NETWORK_NAMESPACE_CREATION=NEEDS_RUNTIME_EVIDENCE
SETUID_SETGID_DROP=NEEDS_RUNTIME_EVIDENCE
CAPABILITY_DROP=NEEDS_RUNTIME_EVIDENCE
NO_NEW_PRIVS=NEEDS_RUNTIME_EVIDENCE
POST_RESET_TOOL_IDENTITY=NEEDS_RUNTIME_EVIDENCE
```

No static documentation result may substitute for these fail-closed checks.

## 5. Rolling-image identity boundary

The label `ubuntu-24.04` identifies a provider-managed image class, not an immutable image digest selected by this repository. The current published image version is evidence about the provider's current image inventory only.

```text
RUNNER_LABEL=ubuntu-24.04
RUNNER_LABEL_IMMUTABLE_IMAGE_ID=NO
CURRENT_PUBLISHED_IMAGE_VERSION=20260823.283.1
FUTURE_ASSIGNED_IMAGE_VERSION=NEEDS_RUNTIME_EVIDENCE
FUTURE_KERNEL_VERSION=NEEDS_RUNTIME_EVIDENCE
FUTURE_TOOL_PATHS=NEEDS_RUNTIME_EVIDENCE
FUTURE_TOOL_SHA256=NEEDS_RUNTIME_EVIDENCE
```

This is why the qualified workflow records `ImageOS`, `ImageVersion`, kernel/OS identity, tool versions, resolved executable paths, and executable SHA-256 values during the authorized job rather than pre-binding mutable provider versions.

## 6. Resource and zero-spend interpretation

GitHub currently documents the standard public-repository `ubuntu-24.04` runner as free and unlimited. This is consistent with the existing Decision B requirement to use only a standard GitHub-hosted public-repository runner and with the repository's current USD 0 spend boundary.

It does not create spending authority and does not permit switching runner classes:

```text
STANDARD_PUBLIC_RUNNER_CURRENT_PROVIDER_PRICE_EVIDENCE=ZERO
PAID_OR_LARGER_RUNNER_AUTHORITY=NONE
SELF_HOSTED_RUNNER_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Actual future provider policy and the exact repository visibility/state must still be re-read immediately before any authorized dispatch. If the standard public runner is no longer zero-cost under then-current provider policy, execution must fail closed pending separate finance authority.

## 7. Platform network versus workflow-command network

GitHub documents that a GitHub-hosted runner must communicate with GitHub-owned endpoints for essential runner operations. This provider control-plane communication is distinct from network access performed by workflow commands.

The canonical E004 subject already permits only the exact unauthenticated public source fetch by workflow commands before configure/build and places configure/build in a separate network namespace. This static record does not claim the provider control plane itself is offline.

```text
PROVIDER_CONTROL_PLANE_NETWORK_EXISTS=YES_BY_GITHUB_DOCUMENTATION
WORKFLOW_COMMAND_PUBLIC_SOURCE_FETCH_BOUNDARY=UNCHANGED
CONFIGURE_BUILD_NETWORK_ISOLATION=NEEDS_RUNTIME_EVIDENCE
```

## 8. Current disposition

This research reduces uncertainty about the selected runner class but does not convert any runtime gate to PASS.

```text
RUNNER_CLASS_PUBLIC_DOCUMENTATION_FOUND=YES
CURRENT_IMAGE_INVENTORY_EXACT_SOURCE_COMMIT_BOUND=YES
CURRENT_PUBLISHED_BUILD_TOOLS_SUBSTANTIALLY_PRESENT=YES
PASSWORDLESS_SUDO_CLASS_DOCUMENTED=YES
UNSHARE_SETPRIV_EXACT_AVAILABILITY=NEEDS_RUNTIME_EVIDENCE
NETWORK_NAMESPACE_OPERATION=NEEDS_RUNTIME_EVIDENCE
FUTURE_ASSIGNED_IMAGE_IDENTITY=NEEDS_RUNTIME_EVIDENCE
RUNTIME_PREFLIGHT_EXECUTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
EXECUTION_TOOLING_BLOCKER=ACTIVE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

No workflow file, task checkbox, authority record, model artifact, dataset, benchmark, device state, conversion state, or training state is modified by this evidence record.
