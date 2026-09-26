# START HERE

这是 Penrix 的 AI 编程认知与技能仓库。

第一次进入本仓库时，不要一次性加载所有内容。先建立总规则，再按当前任务渐进式加载。

## 0. 总入口

如果 Penrix Coding Core 已安装，先使用：

- plugins/penrix-coding-core/skills/using-penrix-coding-core/SKILL.md

它负责权力关系和路由，不替代专业工程 skill。

同时记住：

- Penrix 是产品 Owner，不是程序员；
- Coding Agent 承担普通技术判断；
- Superpowers 负责工程纪律，不负责把技术选择重新丢给 Owner；
- LLM 写出来的任务合同不是 Reality；
- 完成状态由证据决定。

## A. Penrix 用自然语言说“我要做什么 / 改什么”

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/intent-contract/SKILL.md

目标：从真实项目出发，把产品意图变成可观察、可验证的工程目标。技术选择由 Coding Agent 承担。若已知本机/部署版本比仓库更新，同时读取 cognition/07-source-baseline-authority.md，先恢复真实代码基线。非简单改动同时建立最小 Preservation Envelope，见 cognition/08-preservation-envelope.md。

## B. 已经有 Issue / 任务合同 / 另一个 LLM 写出的技术方案

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/contract-reality-check/SKILL.md

目标：把用户真正授权的目标与边界，和 LLM 自己推断出的技术事实拆开。后者必须对当前仓库和实际行为重新验证。

## C. 正在修 bug / 做较大实现

如果已安装 Superpowers，优先使用其对应工程流程，不在本仓库复制另一套 TDD、systematic debugging、worktree、review。

同时读取：

- cognition/02-evidence-and-completion.md
- cognition/05-superpowers-coordination.md

## D. 任务声称完成，需要判断“到底能不能用”

读取：

1. plugins/penrix-coding-core/skills/reality-verification/SKILL.md
2. cognition/02-evidence-and-completion.md
3. cognition/06-environment-routing.md

网页/UI：优先真实浏览器验证。

Chrome 扩展：必须实际加载扩展并走受影响路径，build 通过不等于 Live 通过。

Windows / DSH / WebCodex / 本地桥接：Windows 特有结论尽量在 Windows 真环境验收。

Android：官方 Test Android Apps 当前主要覆盖 emulator；MIUI、root、AutoJs6、K20 真机行为需要真机证据。

## E. 需要独立反证

读取 cognition/03-review-routing.md。

代码 diff：可使用 CodeRabbit。
安全面：使用 Codex Security。
重大工程任务：Superpowers 的 reviewer / subagent 流程可作为主工程审查。

## F. 最后给 Penrix 汇报

读取 plugins/penrix-coding-core/skills/owner-handoff/SKILL.md。

必须回答：

- 实际改变了什么；
- 现在用户能做什么；
- 哪些是真实验证过的；
- 哪些仍未验证；
- 是否还有真正需要用户决定的产品行为、风险或不可逆操作。

## 权力关系

1. 用户自然语言中的产品目标、可见行为、风险许可、不可逆选择：用户 Authority。
2. 技术实现、代码组织、测试方式、调试方法：Coding Agent 的责任。
3. LLM 生成的 Issue / spec / task contract：工作材料，不是 Reality。
4. 当前代码、运行结果、真实浏览器/设备/系统行为：技术事实来源。
5. 没有证据，禁止把“应该工作”写成“已经工作”。
