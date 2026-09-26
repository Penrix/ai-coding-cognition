# Environment Routing

Use the most authoritative environment available for the actual claim.

## Web apps and rendered frontend

Primary helper: Build Web Apps / frontend testing and debugging.

Prefer a real rendered browser flow with interaction, console and network checks when relevant.

A successful build alone does not establish user-visible correctness.

## Chrome extensions

The current curated stack does not include a dedicated Chrome-extension acceptance plugin.

For extension work, Reality means exercising the affected extension behavior in a browser environment that actually loads the extension:

- extension installation or load-unpacked path;
- manifest and permission behavior;
- background or service-worker behavior;
- content-script injection;
- popup, options, or page UI as applicable;
- the real target site's interaction when the bug depends on it.

Unit tests, bundling, and extension build success are CODE evidence, not LIVE evidence.

## Windows-local integrations

The current curated stack does not include a dedicated Windows-live plugin.

For DSH, WebCodex, local bridges, browser-to-local tooling, shell integration, or Windows-specific behavior, LIVE VERIFIED requires exercising the relevant path on Windows.

Linux or container tests can support the implementation but cannot silently substitute for a Windows-specific acceptance claim.

## Android emulator

Primary helper: Test Android Apps.

Its current official description is emulator-focused. It is useful for reproduction, screenshots, UI inspection, logcat, and performance evidence.

## Physical Android / rooted K20

A physical rooted-device claim requires the actual device path when the behavior depends on:

- OEM or MIUI behavior;
- root;
- AutoJs6 or accessibility automation;
- app-specific timing;
- screen coordinates or OCR;
- watchdog interaction between multiple apps;
- real network or power conditions.

Emulator success is not enough for those claims.

When the real device is unavailable, report CODE VERIFIED, LIVE UNVERIFIED or NOT VERIFIED / BLOCKED as appropriate.

## Rule

Choose the evidence class from what was actually exercised, not from how confident the coding agent feels.
