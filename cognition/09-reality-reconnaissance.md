# Reality Reconnaissance

## Problem

LLM coding can be internally coherent and still miss the world outside the repository.

A model can:

- use an API that existed in an older version;
- design around a library that already owns the needed behavior;
- assume an install path that real users cannot reproduce;
- miss permissions, OEM/runtime constraints or service drift;
- pass its own tests against a fake boundary;
- review its finished diff only against the assumptions that produced it.

Repository inspection, TDD, code review and runtime verification each solve part of this problem, but none of them automatically forces current external research and real-user operational evidence into the implementation loop.

## Ruling

Every production-code task gets a Reality Reconnaissance gate before implementation and again before final self-review.

The first pass constrains what is allowed to be built.

The second pass attacks the concrete assumptions the finished diff now makes.

The depth is proportional to the task. Purely internal mechanical changes may remain project-local. Non-trivial external integrations must include current official/upstream evidence and a search for real user field reports.

## Evidence roles

Different sources answer different questions.

### Current project/runtime

Best source for what this product currently does and what must be preserved.

### Official docs/specs/releases

Best source for normative, versioned contracts when current and precise.

### Upstream source/tests

Best source when documentation is shallow or when ownership/edge behavior matters.

### Upstream issues and user reports

Best source for discovering real failure modes, installation friction, platform quirks and workarounds that formal docs may omit.

They are sensors, not automatic truth; corroborate important claims.

### Target-environment execution

Highest authority for whether the desired behavior actually works in the user's real environment.

Research cannot substitute for this final evidence.

## Required distinction

```text
PRE:
What does current Reality allow us to build?

IMPLEMENT:
Build the smallest evidence-backed path.

POST:
What assumptions did the actual diff introduce,
and does current Reality still support them?

LIVE:
Does the target environment actually do it?
```

This separates four failure classes that LLM coding often collapses:

- wrong goal;
- wrong external assumptions;
- wrong implementation;
- unverified runtime.

## Operational focus

"Research" is not collecting articles.

The useful output is concrete constraint gain:

- exact supported version;
- actual install/bootstrap path;
- permissions and runtime prerequisites;
- current API/CLI/configuration names;
- component ownership;
- known real failure modes;
- field-proven workarounds;
- target acceptance path.

If the search does not change or constrain implementation decisions, it was probably too generic.

## Relation to other Penrix Core skills

- `intent-contract` owns product intent.
- `contract-reality-check` checks LLM-written technical claims.
- `reality-reconnaissance` checks current project/external/field facts before and after code.
- `complexity-gate` prevents unsupported machinery from entering.
- `reality-verification` classifies actual runtime proof.
- `owner-handoff` reports what is and is not established.

Superpowers continues to own engineering mechanics such as brainstorming, systematic debugging, TDD, planning and review.

## No ritual research

This rule does not authorize random browsing on every typo.

The gate always runs; the evidence lanes are selected by what can materially make the code wrong.

When external reality is material, skipping it is not simplification. It is guessing.
