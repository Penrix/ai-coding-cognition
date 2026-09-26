# Preservation Envelope

A requested change authorizes a behavior delta. It does not authorize unrelated product drift.

## Shape

For a non-trivial change:

```text
Current accepted product
        |
        | authorized delta
        v
Desired product

Everything outside the authorized delta
is preserved by default.
```

The useful engineering artifact is not a list of every existing feature.

It is a small **Preservation Envelope** containing existing behaviors that are:

1. already accepted, relied upon, or explicitly constrained; and
2. plausibly at risk from the current change, chosen baseline, refactor, or dependency update.

## Sources

The coding agent derives the envelope from:

- explicit user do-not-change constraints;
- current accepted UI/behavior;
- recent PRs and fixes;
- product/current-state documents;
- tests that protect important behavior;
- independent review findings;
- incident boundaries.

Do not ask the non-programmer owner to reverse-engineer regression surfaces from code.

## Verification

Success means both:

- the intended new behavior is demonstrated;
- the relevant preservation envelope remains true.

A green suite proves only what the suite actually covers.

If a user-valued invariant is missing from verification, add the smallest useful regression proof rather than assuming unrelated green checks cover it.

## Surgical change

Surgical does not mean few files at any cost.

It means:

- every behavior change traces to the authorized delta;
- supporting edits are necessary for that delta;
- protected existing behavior does not silently change;
- unrelated cleanup/refactoring is excluded.
