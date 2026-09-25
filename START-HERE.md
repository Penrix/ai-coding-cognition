# START HERE

这是 Penrix 的 AI 编程认知与技能仓库。

第一次进入本仓库时，不要一次性加载所有内容。先判断当前任务属于哪一类，再读取对应文件。

## A. Penrix 用自然语言说“我要做什么 / 改什么”

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/intent-contract/SKILL.md

目标：从真实项目出发，把产品意图变成可观察、可验证的工程目标。技术选择由 Coding Agent 承担，不把程序员判断甩回给用户。

## B. 已经有 Issue / 任务合同 / 另一个 LLM 写出的技术方案

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/contract-reality-check/SKILL.md

目标：把用户真正授权的目标与边界，和 LLM 自己推断出的技术事实拆开。后者必须对当前仓库和实际行为重新验证。

## C. 正在修 bug / 做较大实现

如果已安装 Superpowers，优先使用其对应工程流程，不在本仓库重复维护另一套 TDD、systematic debugging、worktree、review。

同时读取 cognition/02-evidence-and-completion.md。

## D. 任务声称完成，需要判断“到底能不能用”

读取：

1. plugins/penrix-coding-core/skills/reality-verification/SKILL.md
2. cognition/02-evidence-and-completion.md

网页/UI：优先真实浏览器验证。
Android：优先 emulator / ADB / UI / log 证据。
Windows / Chrome 扩展 / 本地桥接：优先实际目标环境；没有实机证据时，不得把代码验证冒充 Live 验证。

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
