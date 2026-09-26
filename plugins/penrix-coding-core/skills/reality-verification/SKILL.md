---
name: reality-verification
description: Use before claiming a coding task is fixed, complete, or usable when the claim depends on browser UI, Windows or local integration, Android or device behavior, extensions, external services, or other runtime reality beyond static code checks.
---

# Reality Verification

Code evidence and Reality evidence are different.

## Define the exact claim

State the user-facing behavior being claimed.

Then identify the highest-authority environment that can prove it.

## Exercise the target behavior

Examples:

- browser or UI: render the actual app, perform the interaction, inspect resulting state, relevant console and network evidence, and screenshots when useful;
- Chrome extension: load and use the extension path and exercise the affected behavior;
- Windows integration: run the actual Windows or live path when accessible;
- Android: emulator or device plus ADB, UI, and log evidence;
- external service: perform the authorized real operation or use the closest authoritative sandbox.

For a bugfix, reproduce the original failing path before or otherwise establish it, then exercise that same path after the change.

## Classify status

Return exactly one evidence class:

- LIVE VERIFIED
- CODE VERIFIED, LIVE UNVERIFIED
- NOT VERIFIED / BLOCKED

Never promote a lower class because the code looks right.

## Record

Keep concise evidence:

- environment;
- exact flow exercised;
- expected result;
- observed result;
- commands, tools, or checks actually run;
- remaining untested surfaces.

Do not create bulky artifacts unless they help prove the claim.
