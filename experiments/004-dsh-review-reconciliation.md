# Experiment 004 — dsh-chatgpt-web review reconciliation

Date: 2026-09-26

Target: Penrix/dsh-chatgpt-web Issue #1, WEB-M1-WIN-LIVE-017 rev 1

Question:

> When a detailed LLM task contract already has an independent technical review, does the coding workflow reconcile each review finding, or can implementation proceed while material findings silently disappear?

## Inputs

- Issue #1 WEB-M1-WIN-LIVE-017 rev 1 contract
- independent read-only contract review in Issue #1
- delivery receipt for Draft PR #14 head 7251fdf8565efaa55847f2c7d3be50c203c188ea
- actual source at that head:
  - src/chatgpt/fresh-page-safety.ts
  - src/chatgpt/browser.ts
  - src/chatgpt/guards.ts
  - src/chatgpt/turn.ts
  - tests/fresh-page-safety.test.ts

## Review findings vs implementation

The independent review raised six main runtime/test concerns plus Apache handling.

### 1. Atomic fresh-start reservation

Review concern:

- concurrent newTurnPage calls must not all see one free slot.

Implementation observation:

- FreshPageSafetyGate.waitForSlot() performs the check and the state mutation synchronously between await points;
- when a slot is available it pushes the start timestamp and advances nextStartAt before returning;
- callers share one provider-instance gate.

In JavaScript's single-thread event loop this is materially different from an unsynchronized multi-thread check/wait/record sequence.

Disposition:

- **not proven broken**;
- review concern is technically weaker than it first appears;
- a concurrent fake-clock regression test would still be valuable because the contract reviewer explicitly raised it.

The correct workflow should record that disposition rather than either blindly adding a lock or silently ignoring the review.

### 2. Failed page creation must remain charged

Review concern:

- reserve before context.newPage();
- if page creation throws, keep the start charged.

Actual code:

createFreshPageAfterGate():

1. awaits gate.waitForSlot();
2. gate.waitForSlot records starts.push(now) and nextStartAt;
3. only then createPage() is invoked.

If createPage throws, no rollback occurs.

Disposition:

- **implemented by current code**;
- focused test requested by review is absent.

### 3. Final limiter check inside irreversible Send helper

Actual code:

dispatchTemporarySendFailClosed():

- assertTemporaryChatPage(page)
- await preSendGuard()
- dispatchSendFailClosed()
  - mark delivery possible
  - click

runFreshTurn passes throwIfRateLimitDialog as preSendGuard.

Disposition:

- **implemented**.

### 4. Limiter detection must be side-effect free

Actual guards.ts:

- detection reads visible modal/alert/dialog/toast/live regions;
- throwIfRateLimitDialog throws;
- the previous Got-it acknowledgement path is absent.

Disposition:

- **implemented**.

### 5. Concurrent observations of one account-wide limiter episode

Review concern:

- multiple open pages may observe the same history limiter;
- one real episode must not accidentally become strikes 1→2→3→4 unless that escalation is explicitly intended.

Actual code:

noteHistoryRateLimit():

- every call executes strikes += 1;
- lastHistoryLimitAt = now;
- cooldown indexes directly from strike count.

No episode identity or deduplication exists.

Therefore several pages observing the same account-wide modal at the same time can escalate the shared gate through 120 / 240 / 480 / 600 seconds.

The tests call noteHistoryRateLimit sequentially to prove the escalation schedule, but do not define or test same-episode concurrency semantics.

Disposition:

- **material review finding remains unresolved / behavior undefined**.

This experiment does not decide which product behavior is correct; it establishes that the review concern did not receive an explicit evidence-backed disposition before delivery.

### 6. Bounded/cancelled waiter state

Implementation observation:

- there is no explicit waiter queue;
- each wait is an async caller using a bounded sleep loop;
- defaultSleep cleans its abort listener and timer;
- the existing test proves a pacing abort creates no page.

The review-requested concurrent-abort scenario is not covered.

Disposition:

- **mechanism reduces the original queue-leak concern, but concurrent behavior remains untested**.

## Apache provenance

The implementation includes a provenance comment naming:

- MoonTzai/folderbridge-mcp
- adapter v0.3.2
- Apache-2.0
- independent TypeScript reimplementation
- no copied source

The delivery receipt explicitly claims behavior/architecture adaptation rather than copied expression.

Disposition:

- consistent with the clean-reimplementation path described by the review;
- this experiment did not perform a copyright-expression similarity audit.

## Workflow failure discovered

The contract had an independent review before implementation, but the later delivery receipt does not maintain a finding ledger.

As a result:

- some review points were implemented;
- some were effectively answered by code architecture;
- at least one material point remains unresolved;
- the reader has to reconstruct all of this manually after the fact.

That is exactly the kind of technical bookkeeping a non-programmer owner cannot reasonably be expected to perform.

## New rule promoted from this experiment

Any material independent review — of a contract, plan, code diff, or security surface — creates a review ledger.

Every finding must end in exactly one state:

- ACCEPTED — implemented, with evidence;
- REJECTED — not applicable/wrong, with technical evidence;
- DEFERRED — intentionally not fixed now, with scope/risk stated;
- UNRESOLVED — still open and therefore blocks any claim that depends on it.

A later implementation or delivery must not silently omit earlier review findings.

The owner should only be asked when the disposition requires a product/risk decision. Technical review reconciliation belongs to the coding agent.
