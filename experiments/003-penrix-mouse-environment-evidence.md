# Experiment 003 — Penrix Mouse environment evidence

Date: 2026-09-26

Target: Penrix/Penrix-Mouse

Question:

> Can reality-verification distinguish a Windows-target build from actual Windows desktop behavior, and can it preserve useful historical live evidence without pretending that it is a fresh current-environment acceptance?

## Current source

main head:

- cc8b7f8ea2c77f1cdcf4a23a8ad4de68087e82c8
- fix: stabilize taskbar cycling and fast Chrome tab close
- committed 2026-09-19

README.md, docs/CURRENT-INTERACTION-MAP.md, and docs/TESTING.md were all updated by that same commit.

Therefore the current interaction documentation is not stale relative to main.

## The misleading workflow name

The workflow is named:

- build-windows

But its runner is:

- ubuntu-latest

It:

- runs Core self-tests;
- restores/builds the Windows project;
- publishes a self-contained win-x64 executable;
- verifies the artifact shape.

It does not run:

- a Windows desktop session;
- a low-level mouse hook against real input;
- Chrome tab interaction;
- Windows taskbar hit testing;
- physical monitor brightness;
- system volume interaction;
- real multi-monitor boundary behavior.

Therefore a green run would be CODE/ARTIFACT evidence for a Windows target, not Windows LIVE evidence.

Rule:

> Workflow name, target RID, artifact filename, or job title do not establish the runtime environment. Inspect the actual runner and exercised surface.

## Current CI state

The latest three workflow runs were red.

Inspection showed all three ended before steps:

- runner_id = 0
- steps = []
- duration only a few seconds

A fresh rerun of the latest run was triggered on 2026-09-26 without source changes.

The rerun again ended with:

- runner_id = 0
- steps = []

Therefore:

- current CI is not fresh test evidence;
- the red status is not evidence that the code or self-tests failed;
- the workflow is currently not obtaining a runner.

No deeper cause is claimed here.

## Historical real-machine evidence

docs/TESTING.md records real Windows-machine observations for the current main commit, including:

- Core self-test 23/23 at the time;
- Chrome tab-bar wheel cycling;
- taskbar wheel cycling;
- actual target-tab closure rather than merely SendInput success;
- Shift + right-click retaining the native Chrome menu;
- right-click on tab-bar blank space retaining native behavior.

Because docs/TESTING.md was updated in the same commit as current main, this evidence corresponds to the present code revision.

However it is historical environment evidence from 2026-09-19, not a fresh 2026-09-26 run.

The environment can drift independently of code:

- Chrome/Chromium updates;
- Windows updates;
- display topology;
- monitor DDC/CI behavior;
- foreground-window behavior;
- local settings.

Therefore the precise status is:

> Current commit has historical LIVE evidence on the user's Windows environment from 2026-09-19, but no fresh current-environment acceptance was performed in this experiment.

## What reality-verification prevented

Naive interpretation A:

build-windows is green
→ Windows behavior works

Wrong because runner identity and target behavior are different.

Naive interpretation B:

build-windows is red
→ Windows code is broken

Wrong because the job never executed.

Naive interpretation C:

TESTING.md says machine verified
→ current environment is verified forever

Wrong because live evidence has environment and time scope even when the code commit is unchanged.

## New rule promoted from this experiment

Every material verification claim should bind at least:

- code revision;
- actual execution environment;
- behavior exercised;
- observation time.

For environment-sensitive products, unchanged code does not guarantee unchanged Reality.

Historical live evidence remains valuable and should not be discarded, but it must be labeled as historical when environment drift can matter.
