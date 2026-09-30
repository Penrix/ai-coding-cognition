# Reality Reconnaissance skill — formation note

Date: 2026-09-30

## Trigger

Penrix required a missing step to become structural rather than optional:

- before writing code, collect the relevant current information;
- include real user reports / operational sharing where external reality matters;
- understand how the thing is actually installed, configured and used;
- after implementation, collect/re-check the relevant reality again before self-reviewing the code.

The question was whether an upstream skill already owns this responsibility.

## Upstream audit

### obra/superpowers v6.4.2

Reviewed head:

`8ca22dba9a94f28898bbce59f2537ff4d87c747d`

Relevant current skills:

- brainstorming
- systematic-debugging
- writing-plans
- requesting-code-review
- verification-before-completion

Current `brainstorming` explores project files/docs/recent commits and user intent, but released main does not contain an external/prior-art research step.

Current `systematic-debugging` requires evidence and root-cause investigation for bugs, and says to research more when the cause is not understood. It does not define a general pre-implementation and post-implementation external-reality pass.

Current `verification-before-completion` requires fresh execution evidence for completion claims. It does not require current docs/upstream/user-field research before reviewing the final mechanism.

Current `requesting-code-review` reviews the diff against requirements. It does not independently establish current external operational facts.

### Upstream community evidence

Superpowers Issue #983 raised essentially the pre-design half of the same gap:

https://github.com/obra/superpowers/issues/983

The report warns that an agent can propose a library/API path that is already obsolete and asks for prior-art search, dependency verification and pattern research.

A community comment on that issue specifically reports using research cycles before/during/after proposals and finding plans improve when grounded in both official and community sources.

Issue #983 was later closed in favor of tracker #2129:

https://github.com/obra/superpowers/issues/2129

As of this review, #2129 is open and explicitly states that current brainstorming performs local orientation only, not external/prior-art research.

Active PR #2116:

https://github.com/obra/superpowers/pull/2116

adds a conditional, read-only research subagent before architectural design. It is still open and not part of the reviewed v6.4.2 release.

Even if #2116 lands, its current scope is narrower than Penrix's requirement:

- it is a pre-design prior-art pass;
- it is conditional on external/current uncertainty;
- it does not define a POST pass against the final diff;
- it does not require real-user operational evidence as a distinct lane;
- it does not connect research findings to final target-environment acceptance.

### multica-ai/andrej-karpathy-skills

Reviewed head:

`2c606141936f1eeef17fa3043a72095b4765b9c2`

`karpathy-guidelines` says "Think Before Coding", surface assumptions, prefer simplicity, make surgical changes and define verifiable goals.

It does not define how to collect current external evidence, user field reports, installation reality or a post-implementation research audit.

## Decision

Do not wait for upstream.

Create a Penrix Core skill with a distinct responsibility:

`reality-reconnaissance`

Its scope is not "do more research." Its scope is:

```text
PRE  -> current local + official/upstream + field reality constrains implementation
POST -> actual diff assumptions are re-checked against current reality
LIVE -> target environment proves or disproves the result
```

This does not fork Superpowers' debugging/TDD/review/verification mechanics.

If upstream later ships its prior-art research step, keep the useful upstream design-phase behavior there and reduce any duplicated PRE wording if appropriate. The Penrix-specific POST audit, user-field lane and real-landing questions remain separate responsibilities unless upstream grows to cover them.
