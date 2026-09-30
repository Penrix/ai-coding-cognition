# Load Instruction

For ChatGPT Web or Codex when this repository is used as external cognition:

> Read START-HERE.md first. Route from there and load only the files needed for the current task. Treat this repository as the current coding-workflow authority unless the user's current instruction overrides it. Do not bulk-load the repository.

For an existing LLM-generated Issue or task contract:

> Preserve the user's product goal and explicit constraints, but re-verify technical claims against the current repository and actual runtime before implementing.

For any task that will write production code:

> Run reality-reconnaissance before the first production edit. If external/platform/dependency/operational facts can change correctness, inspect current official/upstream evidence and real user field reports, and recover the concrete install/config/run path. After the implementation exists, run the POST pass against the actual diff before final verification.
