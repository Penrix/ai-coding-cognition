# Experiment 001 — chatgpt-continuity contract vs Reality

Date: 2026-09-26

Target: Penrix/chatgpt-continuity

Question:

> Can the cognition stack correctly determine the current software truth and whether the recorder is ready to merge/use without trusting whichever status document looks most authoritative?

## Inputs inspected

- main: CURRENT.md
- main: working/CURRENT.md
- main: README.md
- Draft PR #1
- PR #1 branch manifest.json
- PR #1 browser acceptance contract
- GitHub Actions run 35191355781, original attempt and fresh rerun

## Finding 1 — “CURRENT” is scoped and time-sensitive

main/CURRENT.md was last updated on 2026-09-20.

It states:

- main remains the older v0.1 baseline;
- active implementation is Draft PR #1;
- branch feat/recorder-v0.2-poc is v0.2.4;
- installed real-machine copies are still v0.2.0;
- v0.2.4 still requires real-browser acceptance.

working/CURRENT.md was last updated on 2026-09-15 and describes the older capture/finality implementation.

Therefore the two documents are not equal conflicting authorities. The older working document is a historical checkpoint relative to the newer root CURRENT.md.

Lesson:

> A filename such as CURRENT.md does not create authority by itself. Reconcile branch, commit time, intended scope, and current code before using status prose as technical truth.

## Finding 2 — branch Reality supports the v0.2.4 identity

Draft PR #1 is still open and draft.

PR head:

- 0a510478525d83865a67e609864d87d19d67cb1e

The branch manifest directly confirms:

- version 0.2.4;
- MAIN scripts: page-boundary.js then page-recorder-minimal.js;
- isolated scripts: canonical-rate-gate-content.js then recorder-content.js;
- Google OAuth client ID remains a placeholder.

This supports the newer CURRENT.md description of the active development line.

## Finding 3 — historical CI failure was not a code-test failure

The original PR workflow run 35191355781 failed with:

- steps = [];
- runner_id = 0;
- runtime of only a few seconds.

That supports the PR note that the workflow failed before executing its test steps.

As part of this experiment, the same failed workflow was rerun without changing source.

Fresh attempt on 2026-09-26 again failed before steps executed:

- steps = [];
- no runner execution.

Therefore the CI limitation is still current, not merely stale prose.

But it proves only:

> CI did not execute.

It does not prove either that the code passes or that the code fails.

## Finding 4 — merge/readiness remains Reality-blocked

PR #1 explicitly requires real-browser acceptance before merge.

The acceptance gate includes:

- zero extension-owned ChatGPT requests while idle;
- globally shared request gate;
- at most one singular canonical GET after a permitted accepted send;
- no plural fallback or immediate retry;
- cross-tab suppression;
- 429 circuit-breaker persistence;
- no composer/send automation;
- branch preservation;
- stable tape and Drive identity.

This experiment did not run the branch in the user's actual Chrome/Windows session.

Therefore the overall readiness claim is:

**NOT VERIFIED / BLOCKED**

Not because the code is known bad, but because:

1. current CI still cannot execute;
2. the required real-browser acceptance has not been freshly performed here.

## What the cognition stack changed

Without contract-reality-check, an agent could have:

- trusted the stale working/CURRENT.md;
- treated old test prose as fresh proof;
- interpreted the red CI badge as test failure;
- or interpreted static code inspection as real-browser safety.

With the stack:

- owner/product intent was kept separate from technical status;
- status documents were reconciled by scope and freshness;
- branch code was checked directly;
- CI failure semantics were verified instead of guessed;
- completion was limited to the evidence actually available.

## New rule promoted from this experiment

When multiple status/handoff/current-state documents exist:

1. identify the branch or runtime each document describes;
2. record its last relevant update;
3. compare it with current code/PR/runtime state;
4. treat older scoped documents as historical checkpoints unless newer evidence says otherwise;
5. never use a filename such as CURRENT.md as authority by name alone.

This rule is now part of contract-reality-check.
