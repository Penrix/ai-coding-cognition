---
name: mechanical-execution-fastpath
description: Use when the answer, patch, content, or execution decision already exists and the remaining task is mechanical execution such as writing settled conclusions to GitHub, applying an existing patch, syncing an existing result to an Issue, renaming/moving/recording artifacts, or when Penrix explicitly says not to research and only execute. Prevent execution ceremony, repeated discovery, scope expansion, and post-success wandering.
---

# Mechanical Execution Fast Path

Use this skill when the problem has already been solved and the remaining work is execution.

The goal is not to make every task fast. The goal is to distinguish work that still requires cognition from work whose cognition is already complete.

## Task-type gate

Before starting, classify the current task:

```text
research?
implementation?
debugging?
or already-solved mechanical execution?
```

If the answer, patch, content, destination, or decision already exists, and the user is asking to apply, record, sync, move, rename, or write it, enter this Fast Path.

Typical triggers:

- write already-settled conclusions into GitHub;
- apply an already-defined patch or exact edit;
- sync an existing result to an Issue / PR / document;
- rename, move, copy, or record known artifacts;
- perform a known repository writeback;
- Penrix explicitly says “不要重新研究，只执行” or equivalent.

Do not use this Fast Path when a real unresolved engineering, product, or factual question still determines what should be done.

## Hard Fast Path

1. **Does the answer already exist?**
   - YES -> do not research the problem again.

2. **Has the user already given the execution path or boundary?**
   - YES -> do not redesign the workflow.

3. **What still needs discovery?**
   - Discover only the minimum unknown information required to execute the next action.

4. **Are the tool, path, rule, or target already known?**
   - YES -> do not rediscover them.

5. **Before every extra search / read / check, ask:**
   > Which pending execution action can this result change?
   - If there is no concrete answer -> do not perform it.

6. **When the explicit success condition is satisfied:**
   - STOP immediately.

7. **No scope expansion:**
   - no “顺手检查”;
   - no “既然来了再看看”;
   - no extra audit merely to appear careful;
   - no new theory, architecture, cleanup, index maintenance, or adjacent repair unless the requested execution fails without it.

## Verification boundary

> **Verification scope must not exceed execution scope unless a concrete failure requires expansion.**

Examples:

- If the task is to write three documents, read back those three documents.
- Do not inspect `CURRENT.md` merely because the three documents were written.
- Do not inspect `ENTRY-MAP.md` because `CURRENT.md` happened to be inspected.
- If a required repository rule explicitly says an index must change, update that index; otherwise do not invent index work.

Verification proves the requested execution. It is not permission to open a new investigation.

## Extra-step burden of proof

Every additional execution step has the burden of proof.

“Safer”, “more complete”, “while we are here”, “best practice”, “I should double-check”, and “it may also need updating” are not sufficient reasons.

For any proposed extra step, name:

```text
required action:
concrete uncertainty:
how this check can change that action:
```

If those fields cannot be filled concretely, skip the step.

## Tool discovery

Tool discovery is part of execution overhead, not the task itself.

- Reuse an already-known action when available.
- Discover a missing action once, then execute.
- Do not repeatedly search for equivalent tools.
- Do not turn tool-schema exploration into a substitute for doing the requested work.
- A failure to find a tool is a blocker only after a bounded direct attempt, not after wandering discovery loops.

## STOP conditions

Define the smallest observable success condition before execution.

Examples:

```text
GitHub writeback:
target files created/updated
+ returned write success
+ exact written files read back
= STOP

Issue sync:
comment created
+ comment read/confirmed if needed
= STOP

Known patch:
patch applied
+ affected verification passes
= STOP
```

Once STOP is reached, report the result. Do not search for more work.

## Relationship to other skills

This is the execution-layer sibling of `complexity-gate`.

`complexity-gate` says:

> New code complexity has the burden of proof.

This skill says:

> **New execution complexity has the burden of proof.**

It does not cancel required engineering workflows when implementation/debugging is genuinely still underway. It prevents those workflows from being re-run after the problem is already solved and only mechanical execution remains.

If Penrix explicitly narrows the task to mechanical execution, that explicit instruction wins over generic ceremony.
