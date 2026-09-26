# Upstream Review Lock

This is a review snapshot, not a dependency lockfile.

It records what versions and repository heads were examined when this cognition was last self-audited. Marketplace git-subdir entries may move as upstream repositories move.

Last reviewed: 2026-09-26.

| Source | Reviewed state | Decision |
|---|---|---|
| openai/plugins | commit 1dc195897af4161d039b80d8471ec0a10c9bbc89 | Primary Codex compatibility source for curated plugins |
| obra/superpowers | v6.4.2, commit 8ca22dba9a94f28898bbce59f2537ff4d87c747d | Semantic upstream; currently newer than OpenAI curated mirror |
| OpenAI curated Superpowers | v6.3.0 at reviewed openai/plugins head | Used by this marketplace for Codex compatibility/stability |
| CodeRabbit | v1.1.4 at reviewed openai/plugins head | Independent diff review |
| Codex Security | v0.1.24 at reviewed openai/plugins head | Security workflow |
| Build Web Apps | v0.1.2 at reviewed openai/plugins head | Browser/frontend verification |
| Test Android Apps | v0.1.2 at reviewed openai/plugins head | Emulator-focused Android verification |
| multica-ai/andrej-karpathy-skills | commit 2c606141936f1eeef17fa3043a72095b4765b9c2 | Principles absorbed, not installed |
| golbin/agent-skills | commit 30f04e4e138abf56313ddfef700c0182796ae3ac | PRD/intention behavior absorbed, not installed |
| breadoncee/dumb-it-down | commit 941b3a8706eaeba838eb3699defdf916cdf18ac9 | Non-expert handoff behavior absorbed, not installed |

## Superpowers version policy

Prefer the OpenAI curated mirror in Codex unless a specific upstream fix or capability is needed and verified to work with the current Codex plugin format.

Freshest is not automatically best.

When the official mirror materially lags a needed upstream fix, review the delta and deliberately switch source rather than silently changing it.
