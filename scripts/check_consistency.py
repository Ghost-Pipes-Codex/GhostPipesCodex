#!/usr/bin/env python3
"""Simple consistency checks for chapter-01. Warnings only — never fails the build.

1. Items listed under "### Not Confirmed Owned" in 01.7-workstation.md should not be
   referenced elsewhere in chapter-01 as if they were owned or committed. Any other
   mention is reported unless the line says it is not owned / not confirmed /
   previously / struck through (~~). open-flags.md is exempt (flags discuss these).
2. The version in chapter-01/00-README.md and chapter-01/open-flags.md should match.

Output uses GitHub Actions annotation syntax (::warning file=...,line=...::), which
is also readable in a plain terminal.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTER = ROOT / "chapter-01"
WORKSTATION = CHAPTER / "01.7-workstation.md"
SECTION_HEADING = "### Not Confirmed Owned"
ALLOWED = re.compile(r"not owned|not confirmed|previously|removed from|before purchasing|~~", re.IGNORECASE)
# Sections in 01.7 whose job is to list not-owned items (wishlist = candidates by definition).
EXEMPT_HEADINGS = ("### Not Confirmed Owned", "### Master Wishlist")


def section_range(lines: list[str], heading: str) -> range:
    """1-based line numbers covered by the '### ...' section starting with `heading`."""
    start = next((i for i, l in enumerate(lines) if l.startswith(heading)), None)
    if start is None:
        return range(0)
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("### ")), len(lines))
    return range(start + 1, end + 1)


def not_owned_items() -> list[str]:
    lines = WORKSTATION.read_text(encoding="utf-8").splitlines()
    names = []
    for num in section_range(lines, SECTION_HEADING):
        line = lines[num - 1]
        if line.startswith("* "):
            names += re.findall(r"\*\*(.+?)\*\*", line)
    return names


def check_not_owned() -> int:
    names = not_owned_items()
    if not names:
        print("::warning::No 'Not Confirmed Owned' section found in 01.7-workstation.md; skipped that check.")
        return 0
    ws_lines = WORKSTATION.read_text(encoding="utf-8").splitlines()
    exempt = [n for h in EXEMPT_HEADINGS for n in section_range(ws_lines, h)]
    count = 0
    for path in sorted(CHAPTER.glob("*.md")):
        if path.name == "open-flags.md":
            continue
        for num, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if path == WORKSTATION and num in exempt:
                continue
            for name in names:
                if name in line and not ALLOWED.search(line):
                    rel = path.relative_to(ROOT)
                    print(f"::warning file={rel},line={num}::'{name}' is listed as NOT owned in 01.7 but is referenced here without saying so.")
                    count += 1
    return count


def title_version(path: Path) -> str | None:
    match = re.search(r"\(v(\d+\.\d+)\)", path.read_text(encoding="utf-8").splitlines()[0])
    return match.group(1) if match else None


def check_versions() -> int:
    readme, flags = title_version(CHAPTER / "00-README.md"), title_version(CHAPTER / "open-flags.md")
    if readme != flags:
        print(f"::warning file=chapter-01/open-flags.md,line=1::Version mismatch: 00-README says v{readme}, open-flags says v{flags}.")
        return 1
    return 0


if __name__ == "__main__":
    total = check_not_owned() + check_versions()
    print(f"Consistency check finished: {total} warning(s).")
    sys.exit(0)
