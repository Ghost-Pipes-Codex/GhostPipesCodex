# SETUP/COMMODORE

Local machine setup for **"The Commodore"** — the Dell Precision 7550 primary
workstation documented in [[01.7-workstation]] (`chapter-01/01.7-workstation.md`).

## What this is (and isn't)

This folder holds the *operational* side of the Commodore: drive layout,
environment paths, installer/config scripts, and a running log of setup
decisions. It is **not** Ground Truth — it doesn't describe what's true about
the rig's hardware or signal path; `chapter-01/` still owns that. This is how
the machine got configured to match what `chapter-01/01.7-workstation.md`
says it should be.

Because of that split, changes here don't trigger the "update the source of
truth?" checkpoint used for `chapter-01/`. If a setup task here reveals that
the Commodore's actual hardware or plugin manifest differs from what
`chapter-01/01.7-workstation.md` claims, that discrepancy gets flagged in
`chapter-01/open-flags.md`, not silently fixed here.

This folder also stays out of the compiled single-file edition
(`GHOST_PIPES_CODEX_V{X.X}_CHAPTER_01.md`) and out of the public
`ghostpipes-source-of-truth` repo used for GPT/Gemini — those are chapter-01
content only, not machine setup scripts.

## Structure

- `README.md` — this file.
- `WORK_SESSION.md` — current/last known setup state. Read this first at the
  start of any Commodore setup session to pick up where the last one left off.
- `scripts/` — reproducible setup and validation scripts (PowerShell `.ps1`).
  Committed — these are meant to be re-run, not one-off commands.
- `logs/` — raw machine-generated output (command output, inventories, scan
  dumps). Gitignored except for `.gitkeep`; kept locally only unless a log is
  specifically decided to be worth keeping as a record.

## Status

Scaffold created 2026-08-27. No setup scripts or session logs yet — this
folder is ready for the first Commodore setup session (drives, environment,
plugin path confirmation, etc.).
