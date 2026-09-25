---
name: contract-reality-check
description: Use when the task arrives as an Issue, spec, plan, acceptance contract, or technical instructions produced partly or wholly by another LLM. Verify technical claims against the current repository and runtime before implementation while preserving the owner's actual goal and explicit boundaries.
---

# Contract Reality Check

A task contract is evidence of prior reasoning, not proof of current technical reality.

## Split the contract

Classify important statements as either owner authority or technical claims.

### Owner authority

Preserve unless the owner changes them:

- desired user-visible behavior;
- explicit scope;
- actions that must not happen;
- irreversible or security boundaries;
- named delivery requirements.

### Technical claims

Re-verify:

- file and function names;
- current branch and head;
- claimed root cause;
- current runtime behavior;
- referenced upstream behavior;
- test and acceptance coverage;
- assumptions about timing, APIs, environment, browser state, or dependencies.

## Preflight

Before modifying code:

1. confirm the referenced code and state exist;
2. reproduce or otherwise establish the current behavior when practical;
3. check whether the proposed acceptance really exercises the original failure;
4. identify contract statements that are stale, ambiguous, or contradicted by Reality.

## Conflict rule

If technical contract text conflicts with current evidence:

- preserve the owner's product goal and explicit safety boundaries;
- correct the technical route;
- record the correction concisely;
- do not faithfully implement a stale technical assertion.

If the conflict changes the product outcome rather than only the implementation, surface it to the owner.

## Continue

After the preflight, execute the task. Do not turn this skill into a second planning bureaucracy.
