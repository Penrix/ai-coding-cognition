# Superpowers Coordination

Superpowers is the primary engineering-procedure layer in this stack.

Penrix Core does not fork or rewrite its debugging, TDD, worktree, planning, verification, or review mechanics.

The boundary is:

- Penrix Core: owner authority, intent grounding, contract-vs-Reality, evidence classes, owner handoff.
- Superpowers: engineering execution discipline.

## Approval gates

A non-programmer owner should not be used as a substitute for engineering judgment.

If Superpowers asks for review or approval of a design or plan:

- ask Penrix only when the choice changes product behavior, scope, data effects, permissions, cost, external side effects, or meaningful irreversible risk;
- for implementation-only choices, the coding agent should inspect evidence, choose the smallest sufficient approach, record the decision, and continue.

This does not relax the requirement to investigate, test, review, or verify.

## TDD and verification

Do not skip tests merely because Penrix cannot review them.

When a behavior is reasonably testable, create or update the appropriate regression proof.

When a meaningful behavior cannot be tested in the available environment, use the strongest available alternative evidence and lower the completion class instead of pretending the gap is closed.

## Questions to the owner

Good:

> Automatic retry may send a message after you stop watching. Do you want stop-and-report or automatic retry?

Bad:

> Should I use a mutex or an atomic?

The first changes the product. The second is engineering.
