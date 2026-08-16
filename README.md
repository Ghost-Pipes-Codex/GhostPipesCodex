# GhostPipesCodex

Ongoing Ghost Pipes Source of Truth — hardware, DAW, MIDI, and software planning. This folder is both the Obsidian vault root and the Git working directory: there is no separate "notes" copy anywhere else once this is set up.

## Structure
- `chapter-01/` — Chapter 01: The Manifest (physical hardware "Ground Truth"). Start at `chapter-01/00-README.md`. Open decisions live in `chapter-01/open-flags.md`.
- `exports/` — generated, non-canonical reading copies (PDFs, etc.) compiled from the markdown source. Never hand-edit anything in here — regenerate from `chapter-01/` instead.
- Future chapters get their own top-level folder (`chapter-02/`, etc.) following the same pattern.

## Editing workflow
1. Edit markdown directly in Obsidian (or any editor) inside this folder.
2. Commit and push via GitHub Desktop, or the Obsidian Git community plugin for one-click sync from inside Obsidian.
3. When working with Claude in a Cowork session, keep this folder connected via the device bridge — Claude reads and writes these same files directly, no copy/paste.

## Status
Chapter 01 is at v2.0 (revised from the original v1.9 draft). See `chapter-01/open-flags.md` for unresolved items — the Martin X-Series acoustic DI routing is the highest-priority open decision.
