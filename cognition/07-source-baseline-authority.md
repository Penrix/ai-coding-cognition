# Source Baseline Authority

Repository source is usually important evidence, but it is not automatically the newest product Reality.

A common AI-assisted-development split is:

```text
GitHub source      = vN
local installed   = vN+1
user data/runtime = already using vN+1
```

If the coding agent starts from vN simply because it is easier to access, it can faithfully produce a regression.

## Authority check

Before meaningful implementation, ask technically:

> Which source tree actually corresponds to the newest behavior the owner is relying on?

Check branch, package, release, installed manifest, recorded machine evidence, and current status artifacts.

## Deployed-newer-than-repo rule

When deployed/local is known newer than repository source:

- preserve the deployed copy and its data;
- do not overwrite it with the older repo;
- recover or reconcile the newer source first when practical;
- avoid reimplementing features already known to exist in the newer runtime;
- classify the older repo as historical/recovery evidence until reconciliation.

## Recovery does not require owner programming judgment

The coding agent should choose how to compare manifests, hashes, local directories, packages, backups, branches, or recovered artifacts.

Escalate only when recovery requires destructive replacement, data loss, external side effects, or a product decision.

## Evidence language

Knowing that a newer runtime exists does not prove its implementation is correct.

Keep separate:

- SOURCE EXISTS / VERSION VERIFIED;
- CODE VERIFIED;
- LIVE VERIFIED.

A README statement that a local build passed tests is useful evidence, but it does not replace inspection or fresh validation when those become available.
