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
