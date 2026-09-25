# Repository Instructions

This repository is the long-lived source of truth for Penrix's AI-assisted coding cognition and curated coding-agent workflows.

When editing this repository:

- Read START-HERE.md first.
- Keep stable cognition separate from tool-specific implementation details.
- Do not vendor full third-party skill repositories unless there is a concrete need; prefer upstream references or marketplace entries.
- A new rule must solve an observed failure mode or a clearly defined workflow need. Do not accumulate generic best practices for their own sake.
- Avoid duplicate authorities. If Superpowers already owns TDD, debugging, worktrees, and review mechanics, route to it instead of copying it.
- Preserve the non-programmer-owner contract: product intent belongs to the user; technical judgment belongs to the coding agent.
- Any completion language must obey cognition/02-evidence-and-completion.md.
- When an upstream project changes materially, update upstreams/README.md and CHANGELOG.md.
