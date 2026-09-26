# Review Routing

Independent review is used to reduce correlated LLM error, not as ceremony.

## Review findings create a ledger

Any material independent review — contract review, plan review, code review, security review, or runtime review — creates findings that must be reconciled.

Every finding must end in one explicit disposition:

- ACCEPTED — implemented, with evidence;
- REJECTED — not applicable or technically wrong, with evidence;
- DEFERRED — deliberately postponed, with scope and consequence stated;
- UNRESOLVED — still open.

A later implementation or delivery must not silently omit earlier findings.

Do not mechanically obey a reviewer. Review is evidence and adversarial pressure, not a second owner.

The coding agent is responsible for deciding technical findings. Ask Penrix only when a finding changes product behavior, data effects, permissions, cost, irreversible action, or accepted risk.

If an unresolved finding materially affects the completion claim, that claim remains blocked.

## Ordinary small change

Use the main engineering workflow and fresh verification. Do not spawn multiple reviewers for a trivial mechanical edit unless risk warrants it.

## Non-trivial code change

Preferred:

- Superpowers engineering flow;
- fresh review before final acceptance when available.

## Diff-level independent review

If CodeRabbit is installed and the change is meaningful, use it to inspect the current diff.

Do not blindly obey findings. Each finding must receive one of the ledger dispositions above.

## Pre-implementation contract/plan review

When a task contract or implementation plan already has a read-only/adversarial review:

1. read the review before implementation;
2. reconcile it against current code and the task's authority boundaries;
3. carry accepted findings into the implementation/test plan;
4. record rejected/deferred findings with reasons;
5. do not let review findings disappear merely because they were not copied into the original contract text.

## Security-sensitive change

Use Codex Security when the change touches meaningful attack surface, including:

- credentials or secrets;
- authentication or authorization;
- browser-extension permissions;
- local file access;
- remote command execution;
- downloaded untrusted content;
- bridges between browser, local machine, and remote services;
- user data deletion or modification.

For a changed branch or PR, use diff-oriented security review where available. For a new or substantially changed system, use a broader repository scan when warranted.

## Reality review

Independent code review does not replace runtime proof. A reviewer can approve code that still fails in the actual browser, device, or environment.

Use reality-verification before final user-facing completion claims.
