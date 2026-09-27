# LLM Coding Complexity Failure Patterns — 2026-09-27

This note records why Penrix Coding Core gained the `complexity-gate` skill.

It is not a generic list of coding best practices. The retained patterns meet two conditions:

1. they recur in public developer reports or empirical research; and
2. they match failures observed in Penrix's actual AI-assisted coding work.

Community reports are anecdotal evidence. Empirical papers are stronger evidence about population-level behavior. Neither replaces repository/runtime evidence for a specific patch.

## Repeated external patterns

### 1. Fallback and defensive-code addiction

A widely discussed complaint is that coding models add fallback branches, hidden defaults, broad try/catch blocks, fake values, legacy paths, debounce/rate-limit logic, or alternate implementations instead of exposing and fixing the actual violated assumption.

Representative discussion:

- Reddit, "Please turn off Claude Code's insatiable need for fallback code"  
  https://www.reddit.com/r/ClaudeAI/comments/1jgtgc2/please_turn_off_claude_codes_insatiable_need_for/
- Hacker News, discussion around LLMs being overly defensive and hiding impossible-state failures  
  https://news.ycombinator.com/item?id=45530486
- Hacker News, "My Agent Skill for Test-Driven Development" discussion calling this "speculative coding"  
  https://news.ycombinator.com/item?id=48398925

The important distinction is not "never handle errors". It is:

```text
known recoverable failure
→ handle it deliberately

violated assumption / unknown state
→ expose it

imagined future failure
→ do not pre-code it
```

### 2. Wrapper onion and abstraction proliferation

Developers report agents creating one-off helpers, aliases, wrappers around wrappers, unnecessary classes, factories, interfaces, and duplicated public/private layers instead of changing an existing boundary directly.

Representative discussion:

- Reddit, "I am so so sick of certain AI coding patterns"  
  https://www.reddit.com/r/CursorAI/comments/1v7qsby/i_am_so_so_sick_of_certain_ai_coding_patterns/

This matches the already-reviewed Karpathy guidance absorbed by this repository: minimum code, no speculative flexibility, no single-use abstraction merely for neatness.

Upstream reference:

- https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md

### 3. Action bias: coding even when no change is required

The 2026 paper *Coding Agents Don't Know When to Act* tested 200 human-verified tasks where no code change was needed. Across five recent models and four harnesses, agents still proposed undesirable code changes in 35%–65% of cases.

Source:

- https://arxiv.org/abs/2605.07769

This supports treating "no code change" as a legitimate successful outcome and requiring current Reality before patching stale bug reports or LLM-authored contracts.

### 4. Test self-certification and over-mocking

Developers repeatedly report agents writing tests that merely match the implementation, weakening expectations when tests fail, or mocking the exact integration that is broken.

Representative discussion:

- Reddit, "Why does AI write tests that don't actually test anything, and how can I fix it?"  
  https://www.reddit.com/r/Agentic_Coding/comments/1wce8p7/why_does_ai_write_tests_that_dont_actually_test/
- Reddit, "When a test fails, coding agents fix the test. The suite goes green and the bug ships"  
  https://www.reddit.com/r/ChatGPTCoding/comments/1wldasi/when_a_test_fails_coding_agents_fix_the_test_the/

Empirical support:

- *Are Coding Agents Generating Over-Mocked Tests? An Empirical Study* analyzed 1.2M+ commits and found coding-agent commits added mocks more often than non-agent commits (36% vs 26% among the studied commits).  
  https://arxiv.org/abs/2602.00409

The rule derived here is not "never mock". It is: do not use a mock of the boundary under test as evidence that the real boundary works.

### 5. Complexity feels cheap when code generation is cheap

Public discussion around AI coding repeatedly notes that low generation cost encourages speculative structure that remains expensive to understand and debug.

Representative discussions:

- Reddit, "How do you keep complexity out?"  
  https://www.reddit.com/r/ClaudeCode/comments/1wm15qm/how_do_you_keep_complexity_out/
- O'Reilly / Addy Osmani, "Comprehension Debt: The Hidden Cost of AI-Generated Code"  
  https://www.oreilly.com/radar/comprehension-debt-the-hidden-cost-of-ai-generated-code/

This repository does not adopt a blanket "less code is always better" rule. The goal is to keep code proportional to current product reality.

## Existing upstream overlap

Superpowers already treats complexity reduction and YAGNI as core engineering principles, and its brainstorming guidance explicitly says to remove unnecessary features and avoid unrelated refactoring.

Reference:

- https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md

Karpathy guidelines already provide the generic simplicity rule.

Therefore Penrix Core should not duplicate another complete simplicity methodology.

The missing responsibility is narrower:

> Gate each new mechanism by current evidence, ownership, and layer placement.

That is the responsibility of `complexity-gate`.

## Penrix-local collision that triggered the skill

During the 2026-09-27 M1A relay work in `Penrix/dsh-chatgpt-web`, the coding agent initially added:

- a second production `SendSafetyLease`;
- a GET-426 preflight before every relay inference;
- a new relay-safety abstraction/test seam;
- duplicate interpretation of post-Send ambiguity;
- redundant transport identity fields.

This was layered around `codex-chatgpt-web`, which already owned browser submission state, ambiguity, and retry semantics.

The same pass also showed a different failure: the agent had verified the public Responses schema but had not followed the real browser-execution path far enough to discover its native `thread_id/turn_id` requirement.

The correction was:

```text
remove duplicate transport ownership
+
add the actually required runtime contract
+
keep test pacing in the acceptance harness
```

This is the key lesson:

> Over-defending guessed failures can coexist with under-verifying the one real contract that matters.

## Derived rules

The resulting stable rules are:

1. New complexity has the burden of proof.
2. "Safer" and "future-proof" are motivations, not evidence.
3. One cross-layer concern should have one authoritative owner.
4. Verification-only constraints stay out of production unless the product actually needs them.
5. Fallbacks require a real recovery contract; otherwise expose the failure.
6. "No change" is a valid outcome when Reality already satisfies the goal.
7. Tests must discriminate behavior, not certify the implementation that wrote them.
8. Mocking is not evidence for the real integration boundary being changed.
9. A schema/type check is not the same as the deeper runtime contract.
10. After implementation, run a removal pass: if a new mechanism has no concrete failure or requirement that returns when removed, remove or defer it.
