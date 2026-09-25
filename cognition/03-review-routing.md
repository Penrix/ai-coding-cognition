# Review Routing

Independent review is used to reduce correlated LLM error, not as ceremony.

## Ordinary small change

Use the main engineering workflow and fresh verification. Do not spawn multiple reviewers for a trivial mechanical edit unless risk warrants it.

## Non-trivial code change

Preferred:

- Superpowers engineering flow;
- fresh review before final acceptance when available.

## Diff-level independent review

If CodeRabbit is installed and the change is meaningful, use it to inspect the current diff.

Do not blindly obey findings. Each finding must be:

- confirmed and fixed;
- rejected with evidence;
- or recorded as unresolved.

## Security-sensitive change

Use Codex Security when the change touches meaningful attack surface, including:

- credentials or secrets;
- authentication or authorization;
- browser-extension permissions;
- local file access;
- remote command execution;
- downloaded untrusted content;
- bridges between browser, local machine, and remote services;
- user data deletion or modification.

For a changed branch or PR, use diff-oriented security review where available. For a new or substantially changed system, use a broader repository scan when warranted.

## Reality review

Independent code review does not replace runtime proof. A reviewer can approve code that still fails in the actual browser, device, or environment.

Use reality-verification before final user-facing completion claims.
