# Upstream Registry

Prefer links and marketplace references over copying entire upstream repositories.

| Upstream | Role here | Integration |
|---|---|---|
| obra/superpowers | Engineering discipline: debugging, TDD, planning, worktrees, verification, review, subagents | Codex currently follows the OpenAI curated mirror for compatibility; semantic upstream is tracked separately |
| multica-ai/andrej-karpathy-skills | Source inspiration for think-first, simplicity, surgical changes, goal-driven verification | Principles absorbed into cognition; do not install separately |
| golbin/agent-skills | Source inspiration for turning user outcome into concise success conditions | Relevant behavior absorbed into intent-contract |
| breadoncee/dumb-it-down | Source inspiration for non-expert decision handoff | Relevant behavior absorbed into owner-handoff |
| OpenAI CodeRabbit plugin | Independent diff review | Curated marketplace entry |
| OpenAI Codex Security plugin | Security audit and diff scan | Curated marketplace entry |
| OpenAI Build Web Apps plugin | Browser and rendered frontend validation | Curated marketplace entry |
| OpenAI Test Android Apps plugin | Emulator-focused Android evidence | Curated marketplace entry; not a substitute for rooted physical-device acceptance |

See LOCK.md for the exact states reviewed during the latest self-audit.

## Rule for adding upstreams

Do not add an upstream because it is popular.

Add it only when it owns a distinct responsibility that the current stack does not already cover, or demonstrably improves a weak layer.

If two projects own the same responsibility, choose one primary authority and document why.

## Mirror vs semantic upstream

When OpenAI's curated Codex mirror differs from a project's newest upstream release, prefer the curated mirror by default for Codex compatibility.

Switch to a newer direct upstream only when a needed delta is understood and deliberately accepted.
