# CLAUDE.md — Working Rules for Claude in GhostPipesCodex

## What this repo is
GhostPipesCodex is the source-of-truth documentation for the Ghost Pipes project — a multi-station live performance and studio rig (hardware, DAW, MIDI, and software planning). This folder is simultaneously the Obsidian vault root and the git working directory; there is no separate copy of these notes anywhere else.

## Start here
At the start of any session working in this repo, read (in this order): this file, `README.md`, and `chapter-01/open-flags.md`. That's normally enough to pick up exactly where the last session left off without Jeremy having to re-explain anything.

## Ground Truth Directive
Physical hardware specifications and analog/digital I/O routing (defined in `chapter-01/`) are the "Ground Truth" for this project. They take priority over software logic, DAW configuration, or MIDI CC mapping whenever the two would conflict. Don't quietly resolve a contradiction in favor of a software assumption — flag it in `open-flags.md` instead.

## Source-of-truth hierarchy
1. **`chapter-01/*.md` (per-section files)** — the actively-edited source. Always edit here first.
2. **`GHOST_PIPES_CODEX_V{X.X}_CHAPTER_01.md` (compiled single-file edition)** — regenerated *from* the per-section files, for tools (GPT, Gemini, etc.) that work better with one document than with many. If the compiled file and the per-section files ever disagree, the per-section files win. After editing any `chapter-01/*.md` file, offer to regenerate the compiled file to match rather than letting it silently go stale.
3. **`exports/`** — generated, non-canonical reading copies (PDFs, etc.). Never hand-edit anything in here. Always regenerate from the `chapter-01/` source.

Future chapters (`chapter-02/`, etc.) follow this same three-tier pattern.

## Open flags
`chapter-01/open-flags.md` is the running list of unresolved decisions and unconfirmed assumptions. When asked "what are the flags" (or similar), read that file and summarize it directly rather than re-deriving the list from the section files.

Conventions for that file:
- A new unresolved item gets a 🚩 marker, a **bolded summary label**, and a `[[wikilink]]` back to the section it affects.
- When an item is resolved, don't delete it — strike it through (`~~like this~~`) and add a short note on how it was resolved. The history stays visible on purpose.
- Before editing a section that has an open flag against it, check whether the edit resolves, narrows, or is unrelated to that flag, and update `open-flags.md` in the same pass.

## Editing conventions
- Use Obsidian `[[wikilinks]]` to cross-reference between section files, not raw markdown links.
- Follow the existing versioning pattern: chapters are versioned (v1.9 → v2.0 → v2.1...); a version bump gets a revision note at the top of the compiled file summarizing what changed and which sections were untouched.
- Match the existing tone: precise and exhaustive on physical specs (connector types, signal paths, ownership status), and explicit about what's confirmed versus assumed. New gear or routing with unverified details gets logged as an open flag, not presented as settled fact.

## Git workflow
- This is a solo project right now, not a team repo — committing and pushing directly to `main` is fine for day-to-day edits. If this ever becomes collaborative, or the cost of a bad edit goes up, revisit this and add a branch/PR review step.
- Write commit messages that describe *what changed and why* in Codex terms (e.g. "Resolve flag #1: Martin X-Series DI routing" beats "update file").
- When working from a Cowork session, this folder should be connected via the device bridge so edits happen directly on these files — no copy/paste round-tripping.

## Cross-checking hardware/plugin inventory
Per `open-flags.md` item #12: when working from the machine that actually has the VST3/CLAP plugins installed ("The Commodore"), Claude can cross-check installed plugin files against the manifest in `chapter-01/01.7-workstation.md` if given access to the install folders. This is inference from filenames/folder contents, not a guaranteed source of truth — there's no visibility into license/activation status. Flag ambiguous results for Jeremy to confirm rather than asserting them as fact.
