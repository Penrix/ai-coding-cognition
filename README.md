# Penrix AI Coding Cognition

面向“不会也不打算亲自审代码，但希望长期用 ChatGPT / Codex 完成真实软件工程”的个人认知与技能仓库。

这个仓库不是 Prompt Pack，也不是把很多第三方 skill 复制进来。

它做三件事：

1. **保存长期稳定的工作原则**：用户负责产品意图；Coding Agent 负责技术判断、实现、验证和证据。
2. **提供可加载的 Penrix 核心 skills**：把自然语言目标变成可验证任务，核对 LLM 任务合同与真实仓库，执行 Reality 验收，并把最终状态翻译成非程序员能判断的中文。
3. **作为一个精选插件 Marketplace**：集中暴露我们实际需要的成熟上游能力，而不是安装几十个互相抢流程的 skill pack。

## 第一入口

任何模型第一次使用本仓库时，先读：

- [`START-HERE.md`](START-HERE.md)

不要一上来读取整个仓库。这里采用渐进式加载：先确认当前任务属于哪一类，再读取对应 skill / cognition 文档。

## 面向 Codex

本仓库设计为 Git-backed Codex plugin marketplace。

```bash
codex plugin marketplace add Penrix/ai-coding-cognition
codex plugin marketplace list
```

推荐默认安装：

- `penrix-coding-core`
- `superpowers`

推荐按需安装：

- `coderabbit`
- `codex-security`
- `build-web-apps`
- `test-android-apps`

## 面向 ChatGPT 网页端

ChatGPT 网页端若已连接 GitHub，可以直接读取本仓库。

建议指令：

> 读取 `Penrix/ai-coding-cognition` 的 `START-HERE.md`，按它的路由规则只加载当前任务需要的文件。不要一次性读取整个仓库。

## 核心原则

> **Penrix 负责说“我要什么、实际应该怎样工作”；Coding Agent 负责回答“技术上怎么实现、怎么证明真的实现了”。**

不要把程序员判断重新外包给用户。
