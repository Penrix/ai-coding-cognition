# ADR-0001: One cognition repository, not a pile of copied skill packs

## Decision

Use one Penrix-owned repository as:

1. long-lived semantic source;
2. progressive-loading entrypoint for ChatGPT;
3. Git-backed Codex plugin marketplace;
4. home for a small number of Penrix-specific glue skills.

Do not copy whole upstream skill packs when a marketplace reference can keep the upstream independently updateable.

## Why

The problem is not lack of coding prompts. It is coordination:

- the user is a non-programmer product owner;
- LLM-generated technical contracts may be wrong;
- coding agents can overclaim completion;
- code review and runtime verification are different jobs;
- overlapping skill packs can fight for control and bloat context.

The repository therefore owns routing and authority, while mature upstreams own specialist engineering procedures.
