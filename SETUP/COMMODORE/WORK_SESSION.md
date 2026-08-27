# Commodore Setup — Work Session Log

Running record of setup state for "The Commodore" (Dell Precision 7550).
Read this first before starting a new setup session — it should be enough to
pick up where the last one left off without re-deriving context.

## Current state

*Scaffold only — no setup actions have been taken yet.*

- Local clone / vault root: `C:\Users\jerem\OneDrive\Documents\GitHub\GhostPipesCodex`
- Drive layout, environment variables, plugin install paths: not yet inventoried here.

## Pending

- [ ] Confirm drive layout and any additional storage paths in use.
- [ ] Inventory environment variables / tool paths relevant to the rig.
- [ ] Cross-check installed VST3/CLAP plugins against the manifest in
      `chapter-01/01.7-workstation.md` (see `open-flags.md` #12) — flag any
      mismatches there rather than resolving them here.

## Session log

| Date | Who | What changed |
|------|-----|---------------|
| 2026-08-27 | Claude | Created SETUP/COMMODORE scaffold (README, this file, scripts/, logs/). No machine changes made. |

## Decisions

- Routine logs stay local only (`logs/` gitignored except `.gitkeep`) —
  committed history should be scripts and durable state, not raw output.
- This file tracks *setup* state only. Hardware/plugin *manifest* facts still
  live in `chapter-01/01.7-workstation.md`; discrepancies get flagged in
  `chapter-01/open-flags.md`, not recorded here as if they were resolved.
