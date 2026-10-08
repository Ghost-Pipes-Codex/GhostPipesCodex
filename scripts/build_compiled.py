#!/usr/bin/env python3
"""Rebuild the compiled single-file edition of chapter-01.

The per-section files in chapter-01/ are the source of truth. This script
concatenates them (behind scripts/compiled-header.md) into
GHOST_PIPES_CODEX_V{version}_CHAPTER_01.md at the repo root, for tools (GPT,
Gemini, etc.) that work better with one document than with many.

- Version comes from the title line of chapter-01/00-README.md, e.g. "(v2.2)".
- Older GHOST_PIPES_CODEX_V*_CHAPTER_01.md files are removed (git history keeps them).
- The revision notes in scripts/compiled-header.md are hand-written: when you bump
  the version, add a new revision note there. "{{VERSION}}" is filled in automatically.

Usage:
    python3 scripts/build_compiled.py          # rebuild
    python3 scripts/build_compiled.py --check  # exit 1 if the compiled file is out of date
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTER = ROOT / "chapter-01"
HEADER = ROOT / "scripts" / "compiled-header.md"
SEPARATOR = "\n\n\n---\n\n\n"


def read_version() -> str:
    first_line = (CHAPTER / "00-README.md").read_text(encoding="utf-8").splitlines()[0]
    match = re.search(r"\(v(\d+\.\d+)\)", first_line)
    if not match:
        sys.exit(f"Could not find a '(vX.Y)' version in the title of chapter-01/00-README.md: {first_line!r}")
    return match.group(1)


def section_files() -> list[Path]:
    sections = sorted(
        p for p in CHAPTER.glob("*.md") if p.name not in ("00-README.md", "open-flags.md")
    )
    return sections + [CHAPTER / "open-flags.md"]


def build(version: str) -> str:
    header = HEADER.read_text(encoding="utf-8").replace("{{VERSION}}", version)
    body = SEPARATOR.join(p.read_text(encoding="utf-8").strip() for p in section_files())
    return header + body + "\n"


def main() -> int:
    version = read_version()
    target = ROOT / f"GHOST_PIPES_CODEX_V{version}_CHAPTER_01.md"
    content = build(version)
    stale = [p for p in ROOT.glob("GHOST_PIPES_CODEX_V*_CHAPTER_01.md") if p != target]

    if "--check" in sys.argv:
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != content or stale:
            print(f"OUT OF DATE: {target.name} does not match chapter-01 (or stale versions exist).")
            return 1
        print(f"{target.name} is up to date.")
        return 0

    target.write_text(content, encoding="utf-8")
    for p in stale:
        p.unlink()
        print(f"Removed superseded {p.name}")
    print(f"Wrote {target.name} ({len(content)} chars, {len(section_files())} sections)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
