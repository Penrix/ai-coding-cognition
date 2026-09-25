---
name: intent-contract
description: Use when Penrix describes a coding goal, bug, feature, or desired behavior in natural language and the agent must turn it into an executable, verifiable engineering target without outsourcing technical decisions back to the user.
---

# Intent Contract

The owner supplies product intent, not implementation design.

## Recover the real target

Inspect the current repository and project state before inventing a design.

Establish:

- current observed behavior;
- desired observable behavior;
- explicit constraints from the owner;
- what would count as success in Reality;
- any genuinely missing product decision.

Do not ask the owner to choose ordinary implementation mechanisms.

## Separate product unknowns from engineering unknowns

Engineering unknowns are yours to investigate.

Examples:

- which file owns the behavior;
- which concurrency primitive to use;
- which existing abstraction to extend;
- which test layer best reproduces the bug.

Product unknowns may require the owner only when alternatives create meaningfully different visible behavior, data effects, cost, permissions, or irreversible consequences.

## Compact execution contract

For a non-trivial task, keep only:

- Goal — one sentence in user-visible terms.
- Current reality — what the project actually does now, with evidence.
- Success evidence — what observation will prove the goal.
- Constraints — explicit owner boundaries and relevant project constraints.
- Engineering plan — shortest viable technical route.
- Open product decisions — only if truly needed.

Do not inflate this into a document when a few lines are enough.

## Continue

If the owner already asked for implementation, the contract is not a stopping point. Proceed into the appropriate engineering workflow unless a real approval boundary exists.
