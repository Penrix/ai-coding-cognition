# Codex Usage

This repository is both an external cognition source and a Git-backed Codex plugin marketplace.

## Add the marketplace

~~~bash
codex plugin marketplace add Penrix/ai-coding-cognition
codex plugin marketplace list
~~~

Codex CLI currently accepts owner/repo as a marketplace source.

## Default

Install:

- penrix-coding-core
- superpowers

If Superpowers is already installed from OpenAI's official marketplace, keep that installation and do not install a duplicate copy from this marketplace.

## Install when useful

- coderabbit — independent diff review
- codex-security — security-sensitive work and security scans
- build-web-apps — rendered browser and frontend Reality verification
- test-android-apps — Android emulator, ADB, UI, log, and performance evidence

The upstream entries here are a curated convenience. They remain namespaced by marketplace. Do not deliberately install the same plugin from multiple marketplaces unless testing source differences.

## Session entry

When using the repository as cognition rather than only as installed plugins:

> Read START-HERE.md first and load only the path relevant to this task.

## Current environment gaps

No current selected plugin fully substitutes for:

- real Chrome-extension acceptance;
- native Windows acceptance for DSH/WebCodex/local bridges;
- rooted K20/MIUI/AutoJs6 physical-device acceptance.

Follow cognition/06-environment-routing.md for these cases.

## Principle

Do not install every possible coding skill pack.

Add a capability only when it owns a distinct job not already covered by the current stack.
