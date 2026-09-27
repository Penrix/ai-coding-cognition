# LLM Coding Failure Modes

This file records failure modes we actively constrain.

## Silent assumption drift

The model picks one interpretation without checking project evidence and builds on it.

Countermeasure: inspect current code and runtime; distinguish verified facts from assumptions.

## Symptom patching

The model sees an error near X and modifies X without tracing the cause.

Countermeasure: root-cause investigation before fix; prefer Superpowers systematic debugging when applicable.

## Drive-by edits

The model improves nearby code, formatting, comments, or architecture unrelated to the request.

Countermeasure: surgical scope. Every changed line should be explainable by the task or by cleanup caused by the task.

## Overengineering

The model adds abstractions, options, configuration, error branches, or frameworks not required by the product goal or current Reality.

Countermeasure: smallest sufficient design, no speculative flexibility.

## Defensive fantasy

The model converts uncertainty into fallback branches, hidden defaults, broad catches, retries, compatibility code, or "just in case" safety machinery instead of establishing whether the scenario is real.

Countermeasure: use complexity-gate. A recovery path needs current evidence and an intended recovery contract; otherwise expose the violated assumption.

## Duplicate authority

The model reimplements a concern that another layer already owns: retry, submission state, rate limiting, lifecycle, cache truth, compatibility, or safety state.

Countermeasure: identify the authoritative owner and delegate to it. Do not create a second independent state machine without evidence that composition is required.

## Action bias

The model assumes a coding task must end with a code patch even when the reported problem is stale, already fixed, or not reproducible.

Countermeasure: establish current Reality first. "No code change required" is a valid successful outcome.

## Test self-certification

The model writes or alters tests after seeing its own implementation, mocks the broken integration, weakens expectations to match produced output, or treats a fake surface as proof of the real runtime.

Countermeasure: derive expectations from product intent, prior failure, independent invariants, or real protocols. Prefer tests that distinguish the old/broken baseline. Keep CODE VERIFIED and LIVE VERIFIED separate.

## Wrapper proliferation

The model adds one-off helpers, aliases, wrappers, factories, interfaces, or extra configuration because they look architecturally tidy rather than because a real boundary requires them.

Countermeasure: use complexity-gate. Search existing call sites and modify the current owner directly unless the new boundary has evidence-backed independent policy or consumers.

## Self-certifying completion

The model changes code, sees one green command, and says fixed.

Countermeasure: use cognition/02-evidence-and-completion.md.

## Contract worship

One LLM writes a technical task contract; another follows it as if every technical statement were fact.

Countermeasure: contract-reality-check.

## Unit-test tunnel vision

Tests pass while the real browser, device, or system behavior is still broken.

Countermeasure: Reality verification in the actual surface whenever the claim is user-visible or environment-dependent.

## Non-expert overload

The model returns code internals instead of telling the owner what changed and what remains uncertain.

Countermeasure: owner-handoff.
