# ChatGPT Web Usage

This repository is designed to be read through the GitHub connection as an external cognition source.

## Important limitation

The repository is not automatically injected into every new ChatGPT conversation.

A new conversation must explicitly ask ChatGPT to read it, or a future plugin/workflow must automate that loading step.

## Normal entry

Tell ChatGPT:

> 读取 Penrix/ai-coding-cognition 的 START-HERE.md。按其中路由只加载当前任务需要的文件，不要一次读取整个仓库。

## Existing coding task

If the current task is already in another repository or Issue, also provide that repository or Issue.

The model should:

1. read START-HERE.md;
2. load only the relevant cognition and skill files;
3. inspect the actual target repository;
4. preserve the owner's stated product goal;
5. verify technical claims instead of trusting prior LLM wording.

## Purpose

ChatGPT Web uses this repository primarily as persistent external cognition.

It does not need every Codex plugin installed in order to understand and apply the repository's authority model, evidence rules, or workflow routing.
