# Evidence and Completion

Completion is a claim about evidence, not confidence.

## Evidence identity

Material evidence should be understood as:

```text
revision/package
× actual environment
× behavior exercised
× observation time
```

A missing dimension limits the claim.

A workflow name, target platform string, artifact name, or documentation title is not a substitute for the actual execution environment.

## LIVE VERIFIED

The target behavior was exercised in the real relevant environment or the closest authoritative runtime.

Examples:

- real rendered browser flow for browser-visible behavior;
- actual Windows path for Windows-specific integration when available;
- real Android or emulator path for Android behavior;
- actual extension interaction for extension behavior;
- actual remote service or account operation when authorized and required.

The original failure or target behavior must be directly checked after the change.

LIVE evidence may be historical. If the code revision is unchanged but the environment can drift, preserve the old evidence while stating its date/environment instead of calling it a fresh acceptance.

## CODE VERIFIED, LIVE UNVERIFIED

Code-level evidence is good:

- relevant tests pass;
- typecheck, build, or lint as applicable pass;
- regression behavior is covered;

but the target real environment was not exercised.

Cross-compiling or publishing an artifact for a platform is code/artifact evidence, not proof of runtime behavior on that platform.

This is not equivalent to fixed in production or works on the user's machine.

## NOT VERIFIED / BLOCKED

Evidence required to support the claim was not obtained, or the environment prevented a meaningful check.

A red CI badge is not automatically failure evidence. First confirm that a runner started and relevant steps executed.

A check that never executed proves neither pass nor fail.

## Evidence hierarchy

For a user-visible claim:

1. actual target-environment behavior;
2. close runtime reproduction;
3. integration or end-to-end tests;
4. unit tests;
5. typecheck, build, static analysis;
6. code inspection;
7. model confidence.

A lower level must not be described as a higher level.

## Freshness

Do not claim a check passes based only on an earlier run if relevant code changed afterward.

If code did not change but the environment is independently mutable, an older live run may remain relevant historical evidence but must retain its environment/date scope.

## Completion question

Before saying done, ask:

> What concrete observation would prove the exact user-facing claim I am about to make?

Then obtain that observation or lower the status.
