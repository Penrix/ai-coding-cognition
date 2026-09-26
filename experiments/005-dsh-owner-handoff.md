# Experiment 005 — dsh-chatgpt-web owner handoff

Date: 2026-09-26

Target: Penrix/dsh-chatgpt-web, WEB-M1-WIN-LIVE-017 rev 1

Question:

> Can a technically dense delivery be reduced to what a non-programmer owner actually needs to know without hiding uncertainty or making the owner decide engineering details?

## Raw engineering state

The delivery receipt contains:

- two Draft PR heads;
- seven changed files;
- source blob identities;
- pacing constants;
- limiter selectors/phrases;
- Send-boundary details;
- targeted harness validation;
- missing repository-level validation;
- no browser live run.

A subsequent cognition experiment also found that the earlier independent contract review had at least one material unresolved concern:

- multiple pages observing one account-wide conversation-history limiter can each call noteHistoryRateLimit();
- current code increments strikes on every observation;
- same-episode deduplication/semantics are not defined or tested.

This is useful engineering detail, but it is not the format Penrix should have to interpret.

## Owner handoff that the system should produce

### 结果

M1-017 已经把两个最重要的安全动作写进代码：

1. 新开 ChatGPT Temporary Chat 页面会被全局节流，不再允许短时间疯狂开新页；
2. 在真正点击 Send 之前，会再次检查“对话历史限流”弹窗；如果弹窗存在，就直接停止，不会强行关闭弹窗，也不会自动重发。

### 现在能确认什么

从当前源码可以确认：

- 限流检查确实放在不可逆 Send 边界之前；
- 检测到已知 history limiter 时不会点击 Send；
- 旧的自动点 Got it 路径已经移除；
- page creation 前会先占用 fresh-page 配额，因此创建失败不会自动把那次配额退回，避免失败循环无成本狂开页。

### 还不能说什么

现在还不能说“M1-017 已经安全可用了”。

原因：

- 当前交付 head 没有跑过完整仓库 typecheck/tests/build；
- 当前交付 head 没有跑真实 Windows + ChatGPT Web live；
- 独立 review 里有一个并发冷却问题还没有明确闭环：同一个 account-wide history limiter 如果被多个页面同时看到，当前实现可能把一次事件累计成多次 strike，快速把 cooldown 推到 600 秒。

### 证据状态

Overall:

**NOT VERIFIED / BLOCKED**

Specific code properties above are supported by source inspection, but the overall behavior is not yet current-head live accepted.

### 需要 Penrix 决定吗

**不需要。**

这不是产品选择，而是工程问题。

Coding Agent 应该自己：

1. 给 review finding 做明确 disposition；
2. 如果同一 limiter episode 不该重复记 strike，就修并加并发测试；
3. 跑当前 head 的完整测试；
4. 再交给 Windows/ChatGPT live 验收。

Penrix 只需要在“是否允许自动重试、是否允许强制关闭弹窗、是否接受更激进节流”等真正改变产品行为时决定。

## What owner-handoff did

The raw delivery asks the owner to mentally combine:

- contract;
- reviewer comments;
- implementation;
- test evidence;
- live boundary.

The handoff turns those into:

- what changed;
- what is actually proven;
- what is not proven;
- whether the owner must decide anything;
- who owns the next action.

## New rule promoted from this experiment

When work is incomplete but no owner decision is required, owner-handoff should not stop at “unverified”.

It should include:

### 下一步

State the next engineering action and make clear that it belongs to the coding agent.

Do not convert unfinished technical work into a request for the non-programmer owner to choose an implementation.
