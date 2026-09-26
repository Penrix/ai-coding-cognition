# Experiment 006 — Lightrans Direct preservation envelope

Date: 2026-09-26

Target: Penrix/lightrans-direct

Question:

> Can the coding workflow prevent a locally correct fix from regressing already-valued product behavior outside the requested change?

## Historical pair

PR #6:

- title: Fix auto source-language handling and simplify glossary behavior
- head: 9bf84696a2fabb5a13defc0a6500cecf0dd07215
- based on main
- CI: PASS
- not merged

PR #7:

- title: Preserve compact selection UI and fix source-language routing
- head: a9adf9fcbffb4aaf7e283538ba9c479432403396
- explicitly superseded PR #6
- merged
- CI: PASS

The final main merge is 54d4809a16b094a57ef03fb6a175d6939c3a2d32 and its push CI also passed.

## Why PR #6 was still wrong despite green CI

The requested technical correction was about:

- resolving auto source language locally when possible;
- respecting configured page source language;
- simplifying glossary semantics.

PR #6 implemented that work and its build workflow passed.

But it was based on main instead of the already-established compact-selection branch.

Its task/CI did not encode one important product invariant:

> selection translation must remain the compact translation-only bubble rather than reverting to the inherited large result panel.

Therefore a green CI run proved the checks it contained, but those checks did not cover an already-valued behavior that the new work was not authorized to change.

## PR #7 correction

PR #7 made preservation explicit:

- keep compact selection bubble;
- keep translation-only selection result;
- keep English → Simplified Chinese one-way controls;
- preserve page display modes;
- apply the source-language/glossary fix.

It also added CI guards that assert the compact selection implementation remains wired:

- CompactPanel remains the selection display;
- translated text remains the displayed result.

This is not merely a larger test suite. It is an explicit statement of the preservation boundary.

## Lesson

“Surgical change” is not measured only by line count or changed-file count.

A change is surgical when:

1. the intended behavior delta is explicit;
2. existing behavior outside that delta is treated as preserved by default;
3. known user-valued or recently established surfaces are named as protected;
4. the verification plan covers both the new behavior and high-value preservation constraints.

A perfectly green test suite can still approve the wrong product if the preservation envelope is missing from the suite.

## New rule promoted from this experiment

For non-trivial changes, intent-contract should include a **Preservation Envelope** when relevant.

It contains only behaviors that are both:

- already established/relied upon; and
- plausibly endangered by the current change or baseline selection.

Do not turn it into a catalog of the entire product.

Examples:

- “fix source-language routing, but keep compact selection bubble and English-only mode”;
- “fix M2 acceptance harness, but do not modify production provider”;
- “repair rate-limit handling, but do not auto-retry Send or weaken outcome uncertainty”.

The coding agent must derive this from repository history, current code, task constraints, recent accepted behavior, and relevant review evidence. The non-programmer owner should not have to enumerate implementation-level regression surfaces.
