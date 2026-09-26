# Experiment 002 — Prompt Shelf intent grounding and baseline authority

Date: 2026-09-26

Target: Penrix/Prompt-Shelf

Question:

> Can intent-contract turn a non-programmer owner's request such as “saving is unreliable, sorting is bad, sync it to Google Drive” into the correct next engineering action without asking the owner to make implementation decisions or rebuilding against a stale repository baseline?

## Repository Reality

main contains restored v0.3.0.

README explicitly records a newer runtime outside GitHub:

- both daily Chrome installations point at a local Prompt Shelf directory whose manifest is v0.4.0;
- local v0.4.0 already contains sorting, background-serialized saving, and Google Drive backup code;
- four local tests had passed;
- that source had not been reconciled back to GitHub;
- real cloud-backup behavior had not completed acceptance.

GitHub has only main and no v0.4 branch.

A Library search did not recover a v0.4.0 source archive.

Google Drive contains the 2026-09-19 recovery conversation for v0.3.0, but that recording ends at restoration of v0.3.0 and does not contain the later v0.4.0 source.

Therefore current source authority is split:

- GitHub v0.3.0 = recoverable historical source baseline;
- local installed v0.4.0 = newer runtime Reality;
- v0.4.0 source = currently unavailable through the accessible repositories/Library/Drive evidence in this experiment.

## Correct intent contract

### Goal

Prompt Shelf should reliably preserve prompt edits, support useful automatic/manual ordering, and keep a recoverable Google Drive backup without losing local data.

### Current Reality

Do not implement that goal on GitHub v0.3.0 yet.

The owner is already running a newer v0.4.0 that reportedly implements those areas. Reimplementing them on v0.3.0 risks discarding newer code and regressing the installed product.

### First success condition

Recover or otherwise reconcile the exact currently installed v0.4.0 source before feature work.

After recovery, establish which of these are:

- implemented and verified;
- implemented but live-unverified;
- still missing.

### Product decisions needed from owner

None at this stage.

The missing choice is technical/recovery work, not a product preference.

The coding agent should recover and inspect the newer source rather than ask the owner how to implement saving, ordering, or Drive sync.

## Code-level diagnosis from the older v0.3.0

The old code also explains why “saving is unreliable” is plausible.

shared.js exposes saveState(state), which writes the entire Penrix state object to one chrome.storage.local key.

manager.js, popup.js, and content.js each:

1. load their own full state snapshot;
2. mutate one part;
3. call saveState with the whole snapshot.

The manager's saving flag only serializes operations inside that one manager page. It does not serialize writes from popup/content/other tabs.

A deterministic stale-writer sequence is therefore possible:

1. manager and popup both load state A;
2. manager edits prompt text and saves state B;
3. popup still has stale state A, changes only autoAppend, and saves state C;
4. state C contains the popup's setting change but restores the old prompt text from A.

That is a whole-state lost-update hazard.

This experiment did not reproduce it inside Chrome, so it is CODE EVIDENCE, not LIVE VERIFIED.

The README statement that v0.4.0 introduced “background serialized saving” is technically consistent with this v0.3.0 hazard, but the v0.4.0 implementation itself was not available for inspection here.

## What intent-contract prevented

A naive execution path would be:

owner says saving/sorting/Drive are bad
→ inspect GitHub main
→ see v0.3.0 lacks sorting/Drive
→ implement sorting/Drive again
→ possibly overwrite or diverge from the newer local v0.4.0

The corrected path is:

owner states product outcome
→ inspect repository + deployed/runtime version evidence
→ detect deployed-newer-than-repo split
→ recover current source first
→ inspect/verify existing v0.4 behavior
→ only then modify remaining gaps

## New rule promoted from this experiment

Before planning implementation, establish source-baseline authority.

If a deployed/local/runtime version is known to be newer than the repository:

1. do not silently treat the repository as current source truth;
2. preserve the newer runtime/data;
3. recover or reconcile the newer source when possible;
4. use the old repository only as historical evidence or a recovery donor;
5. do not rebuild already-implemented features merely because the old repository lacks them;
6. ask the owner only if recovering the newer source would require a destructive/product choice, not for ordinary engineering strategy.

This rule is now part of intent-contract.
