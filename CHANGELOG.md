# Changelog

## 0.3.0 - 2026-09-27 complexity gate

- Added `complexity-gate`, a Penrix-specific admission gate for fallbacks, retries, wrappers, abstractions, compatibility paths, duplicated safety state, mocks, and other speculative mechanisms.
- Added an implementation-removal pass: every new mechanism must identify the observed failure, explicit requirement, or runtime contract that returns if it is removed.
- Added explicit protection against duplicate cross-layer authority, test-only constraints leaking into production, fallback masking, action bias, and test self-certification.
- Expanded the LLM coding failure-mode cognition with community-reported and empirically studied patterns.
- Added a research note preserving the external evidence and the 2026-09-27 M1A formation case that produced this skill.
- Routed Penrix Core to invoke the gate when a change begins accumulating generalized defensive machinery.

## 0.2.0 - 2026-09-26 self-audit

- Added using-penrix-coding-core as the plugin-wide authority and routing entry.
- Defined explicit coordination with Superpowers so engineering rigor remains strong without outsourcing implementation choices to a non-programmer owner.
- Added environment routing for Chrome extensions, Windows-local integrations, emulator Android, and rooted physical Android.
- Added repository validator and GitHub Actions validation.
- Added upstream review lock with reviewed versions and commits.
- Documented ChatGPT Web's explicit-load limitation.
- Documented duplicate-marketplace behavior and advised against duplicate installs.
- Clarified that OpenAI's curated Superpowers mirror is currently preferred for Codex compatibility even when obra upstream is newer.

## 0.1.0

- Established the repository as long-lived AI coding cognition plus a curated Codex marketplace.
- Added the non-programmer-owner authority model.
- Added evidence and completion vocabulary.
- Added Penrix core skills:
  - intent-contract
  - contract-reality-check
  - reality-verification
  - owner-handoff
- Added curated entries for:
  - Superpowers
  - CodeRabbit
  - Codex Security
  - Build Web Apps
  - Test Android Apps
- Added upstream registry.
