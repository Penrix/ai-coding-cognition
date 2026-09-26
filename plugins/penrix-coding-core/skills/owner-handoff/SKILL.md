---
name: owner-handoff
description: Use at the end of a non-trivial coding task to explain status to Penrix as a non-programmer owner: what changed, what now works, what was actually verified, what remains unverified, and whether any product decision or risk still needs him.
---

# Owner Handoff

Translate engineering evidence into owner-decision language. Do not remove technical stakes.

## Default output

### 结果

In plain Chinese: what changed from the owner's point of view.

### 现在你能做什么

Describe the observable behavior now available.

### 我拿什么证明

Use concrete evidence, not confidence:

- tests actually run;
- browser, device, or system flow actually exercised;
- independent review result;
- security scan result when applicable.

State the evidence class:

- LIVE VERIFIED
- CODE VERIFIED, LIVE UNVERIFIED
- NOT VERIFIED / BLOCKED

### 还没证明什么

Name any meaningful untested environment, path, or residual uncertainty.

### 需要你决定吗

Usually: no.

Only put something here when the owner truly must decide a product behavior, irreversible action, external side effect, permission, cost, or risk.

## Technical appendix

Add a short technical appendix only when it helps future work:

- files or areas changed;
- key engineering decision;
- PR, commit, or branch;
- important deferred finding.

Do not make the owner read code to know whether the task succeeded.
