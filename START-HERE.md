# START HERE

这是 Penrix 的 AI 编程认知与技能仓库。

第一次进入本仓库时，不要一次性加载所有内容。先建立总规则，再按当前任务渐进式加载。

## 0. 总入口

如果 Penrix Coding Core 已安装，先使用：

- plugins/penrix-coding-core/skills/using-penrix-coding-core/SKILL.md

它负责权力关系和路由，不替代专业工程 skill。

### 0.1 先判定：是不是已经解决、只剩机械执行

如果答案、patch、结论、目标文件或执行决定已经存在，而当前只是在：

- 把已经讨论清楚的结论写进 GitHub；
- 应用现成 patch / exact edit；
- 把已有结果同步到 Issue / PR / 文档；
- 重命名、搬运、记录已知 artifact；
- 或 Penrix 明确说“不要重新研究，只执行”；

先读取：

- plugins/penrix-coding-core/skills/mechanical-execution-fastpath/SKILL.md

进入 Fast Path 后，不重新研究问题本身，不重新规划已经明确的执行路径，只发现完成下一动作所必需的最小未知量；显式成功条件满足后立即 STOP。

> **Verification scope must not exceed execution scope unless a concrete failure requires expansion.**

同时记住：

- Penrix 是产品 Owner，不是程序员；
- Coding Agent 承担普通技术判断；
- Superpowers 负责工程纪律，不负责把技术选择重新丢给 Owner；
- LLM 写出来的任务合同不是 Reality；
- 写代码前不能只靠模型记忆和仓库内部推断；
- 写完后的自检也不能只拿自己的代码和自己的测试自证；
- 完成状态由证据决定。

## A. Penrix 用自然语言说“我要做什么 / 改什么”

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/intent-contract/SKILL.md

目标：从真实项目出发，把产品意图变成可观察、可验证工程目标。技术选择由 Coding Agent 承担。若已知本机/部署版本比仓库更新，同时读取 cognition/07-source-baseline-authority.md，先恢复真实代码基线。非简单改动同时建立最小 Preservation Envelope，见 cognition/08-preservation-envelope.md。

## B. 已经有 Issue / 任务合同 / 另一个 LLM 写出的技术方案

读取：

1. cognition/00-owner-and-agent.md
2. plugins/penrix-coding-core/skills/contract-reality-check/SKILL.md

目标：把用户真正授权的目标与边界，和 LLM 自己推断出的技术事实拆开。后者必须对当前仓库和实际行为重新验证。

## C. 每次准备写生产代码：先做 Reality Reconnaissance PRE

读取：

1. plugins/penrix-coding-core/skills/reality-reconnaissance/SKILL.md
2. cognition/09-reality-reconnaissance.md

先确认当前仓库真正 owner，再按任务需要收集当前官方资料、上游源码/测试/Issue、版本信息、真实用户分享和目标环境事实。

重点不是“搜索过”，而是弄清楚：

- 现实里到底怎么安装、配置、启动、授权和运行；
- 当前版本到底支持什么；
- 哪个组件真正拥有这个职责；
- 真实用户在哪些地方会失败、怎么成功；
- 这些事实具体淘汰了哪些实现方向；
- 最后要在什么真实环境观察什么，才能证明能用。

纯内部机械改动可以只做项目内 reconnaissance；不要为了仪式随机浏览。

## D. 正在修 bug / 做较大实现

如果已安装 Superpowers，优先使用其对应工程流程，不在本仓库复制另一套 TDD、systematic debugging、worktree、review。

同时读取：

- cognition/02-evidence-and-completion.md
- cognition/05-superpowers-coordination.md

## D2. 代码开始长出额外机制

当实现准备新增以下任一机制时：

- fallback / hidden default；
- retry / debounce / rate limit / cooldown；
- wrapper / adapter / factory / interface / generalized helper；
- compatibility / legacy path；
- cache / shadow state / second source of truth；
- 新的 safety state / lifecycle state；
- mock / fake integration seam；
- “以后可能用到”的配置或扩展点；

读取：

- plugins/penrix-coding-core/skills/complexity-gate/SKILL.md

目标：让每一层新增复杂度都拿出当前 Reality 的入场证据；避免重复另一组件已经拥有的职责；避免把测试约束偷渡进生产；实现后做一次删除优先的 complexity pass。

这不是“代码越少越好”。真实产品要求、已观察故障和明确外部协议需要多少复杂度，就保留多少。

## E. 写完代码准备自检：再做 Reality Reconnaissance POST

重新读取：

- plugins/penrix-coding-core/skills/reality-reconnaissance/SKILL.md

这一次以**实际 diff**为输入，不是把 PRE 搜索结果再看一遍。

逐项列出最终代码已经押注的外部事实：API、版本、权限、路径、组件所有权、安装步骤、fallback/retry 语义、平台行为等；再用当前官方/上游/用户现场资料去攻击这些押注。

结论至少分：

- MATCH；
- MISMATCH；
- UNVERIFIED。

MISMATCH 先修。重大 UNVERIFIED 不能被自己的单测或自信抹掉。

## F. 任务声称完成，需要判断“到底能不能用”

读取：

1. plugins/penrix-coding-core/skills/reality-verification/SKILL.md
2. cognition/02-evidence-and-completion.md
3. cognition/06-environment-routing.md

网页/UI：优先真实浏览器验证。

Chrome 扩展：必须实际加载扩展并走受影响路径，build 通过不等于 Live 通过。

Windows / DSH / WebCodex / 本地桥接：Windows 特有结论尽量在 Windows 真环境验收。

Android：官方 Test Android Apps 当前主要覆盖 emulator；MIUI、root、AutoJs6、K20 真机行为需要真机证据。

## G. 需要独立反证

读取 cognition/03-review-routing.md。

代码 diff：可使用 CodeRabbit。
安全面：使用 Codex Security。
重大工程任务：Superpowers 的 reviewer / subagent 流程可作为主工程审查。

## H. 最后给 Penrix 汇报

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
4. 当前代码、运行结果、当前官方/上游事实、真实用户现场证据、真实浏览器/设备/系统行为：技术事实来源；不同来源回答不同问题，不能互相冒充。
5. 没有证据，禁止把“应该工作”写成“已经工作”。
