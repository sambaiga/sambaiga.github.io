#!/usr/bin/env python3
"""Check the structure of notebook posts, so that a post renders as written.

Quarto reads the front matter of a notebook from its first non-empty cell. These checks catch the three mistakes
that broke posts before:

- the first cell does not hold the front matter;
- the source of a cell is one string and not a list of lines, which makes Quarto print the front matter as text;
- the front matter names a ``bibliography``, which stops Quarto from resolving the ``@fig-`` and ``@tbl-`` references
  of a notebook. References are footnotes, written as IEEE entries, and are listed at the end of the post;
- a heading breaks the heading standard of the site: two to eight words, not a question, and not opening with How,
  Why or What. The heading standard is in ``.claude/skills/site-writing`` and comes from the umeme book.

Usage: ``python scripts/check_notebook_posts.py [notebooks...]``. Exits non-zero and prints one line per finding.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

POSTS = Path("pages/blog/posts")
EXEMPT = {"References", "Citation"}
QUESTION_WORDS = {"how", "why", "what", "when", "which"}


def heading_findings(path: Path, cells: list[dict]) -> list[str]:
    """Findings for the headings of the markdown cells of a notebook post."""
    findings = []
    for cell in cells:
        if cell.get("cell_type") != "markdown":
            continue
        for line in "".join(cell["source"]).splitlines():
            if not line.startswith("#"):
                continue
            title = line.lstrip("#").strip()
            words = title.split()
            if title in EXEMPT or not words:
                continue
            if len(words) < 2 or len(words) > 8:
                findings.append(f"{path}: heading '{title}' must have two to eight words")
            elif title.endswith("?") or words[0].lower() in QUESTION_WORDS:
                findings.append(f"{path}: heading '{title}' must be a noun phrase, not a question")
    return findings


def check(path: Path) -> list[str]:
    """Return the findings for one notebook post, as ``path: reason`` lines."""
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = [cell for cell in notebook.get("cells", []) if "".join(cell["source"]).strip()]
    findings = []
    if not cells or cells[0].get("cell_type") not in {"raw", "markdown"}:
        return [f"{path}: the first cell must hold the front matter"]
    front = cells[0]["source"]
    front_text = front if isinstance(front, str) else "".join(front)
    if not front_text.startswith("---"):
        findings.append(f"{path}: the first cell must start with the front matter delimiter ---")
    if any(isinstance(cell.get("source"), str) for cell in cells):
        findings.append(f"{path}: cell sources must be lists of lines (nbformat), not single strings")
    if "\nbibliography:" in front_text:
        findings.append(f"{path}: remove 'bibliography:'; it breaks @fig- references. Use footnotes as IEEE entries")
    return findings + heading_findings(path, cells)


def main(argv: list[str]) -> int:
    """Check the given notebooks, or every notebook post when none are given."""
    paths = [Path(name) for name in argv] or sorted(POSTS.rglob("*.ipynb"))
    findings = [line for path in paths for line in check(path)]
    print("\n".join(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
