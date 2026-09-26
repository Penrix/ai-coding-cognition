# Penrix AI Coding Cognition

这是 Penrix 长期维护的 AI 编程认知与技能仓库。

目标用户不是职业程序员，而是通过自然语言让 ChatGPT / Codex 长期完成真实软件工程的产品 Owner。

这个仓库不是 Prompt Pack，也不是“收集越多 skill 越好”。

它负责三件事：

1. 保存长期稳定的 AI 编程认知与 Authority；
2. 提供 Penrix 自己需要、上游没有直接覆盖的核心 skills；
3. 作为精选 Codex marketplace，把成熟的专业能力组合成一套实际工作链。

## 第一入口

任何模型第一次使用本仓库，先读：

[START-HERE.md](START-HERE.md)

不要一次性读取整个仓库。先判断任务，再渐进式加载对应 cognition / skill。

## 核心关系

> Penrix 负责说“我要什么、实际应该怎样工作”；Coding Agent 负责“技术上怎么实现、怎么验证、怎么证明真的实现了”。

因此：

- 不把程序员判断重新外包给用户；
- LLM 写出的 Issue / spec / task contract 不是 Reality；
- tests pass 不自动等于真实环境能用；
- review 通过不替代 runtime 验收；
- 没有对应证据，不允许提高完成状态。

## ChatGPT Web

如果 ChatGPT 已连接 GitHub：

> 读取 Penrix/ai-coding-cognition 的 START-HERE.md，按其中路由只加载当前任务需要的文件，不要一次读取整个仓库。

详见 [docs/usage/chatgpt-web.md](docs/usage/chatgpt-web.md)。

## Codex

本仓库同时是 Git-backed Codex marketplace：

~~~bash
codex plugin marketplace add Penrix/ai-coding-cognition
codex plugin marketplace list
~~~

默认核心：

- penrix-coding-core
- superpowers

按需能力：

- coderabbit
- codex-security
- build-web-apps
- test-android-apps

详见 [docs/usage/codex.md](docs/usage/codex.md)。

## 当前 Penrix Core Skills

- intent-contract — 自然语言产品意图 → 可执行、可验证工程目标
- contract-reality-check — LLM 任务合同 → 当前仓库 / Runtime Reality 核对
- reality-verification — 区分代码验证与真实环境验证
- owner-handoff — 把工程证据翻译成非程序员 Owner 能直接判断的中文

## 当前 Cognition

- Owner 与 Coding Agent 的权力边界
- LLM 写代码常见失败模式
- Evidence / Completion 等级
- 独立 Review 路由
- 默认工作流

## 上游策略

成熟专业能力尽量跟上游走，不复制整套项目。

当前主要借用：

- obra/superpowers
- OpenAI CodeRabbit plugin
- OpenAI Codex Security
- OpenAI Build Web Apps
- OpenAI Test Android Apps

Karpathy guidelines、golbin PRD、dumb-it-down 等项目中与我们实际问题有关的认知，只吸收其有效部分，不让多个框架重复争夺同一职责。

详见 [upstreams/README.md](upstreams/README.md)。
