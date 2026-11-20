"""Check the site's copy against the writing standard borrowed from the umeme book.

The site follows the register of the author's thesis and books: formal, concise and specific. This check catches the
mechanical part of that standard in the text that visitors read:

- page prose in the top-level and ``pages/*/index.qmd`` files, and ``pages/books/mbuga.qmd``;
- the ``description``, ``subtitle`` and ``description-meta`` fields of those pages, of the data files and of every blog
  post, and the ``title`` of every blog post (talk and paper titles are quoted from the originals and are not checked).

Rules: no em- or en-dashes, no second person, no heading phrased as a question, no conversational phrase from
``BANNED``, no marketing phrase from ``MARKETING``. Blog post bodies are not checked.

Usage: ``python scripts/stylecheck.py [files...]`` (every copy file when none are given). Exits 1 and prints
``file:line: reason`` for each finding.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

#: Conversational or rhetorical phrases that do not belong in formal prose (shared with the umeme book).
BANNED = (
    "that gap", "by the end of", "the point is", "it turns out", "let's", "let us", "of course", "basically",
    "actually", "really", "pretty much", "a lot of", "huge", "clearly", "cheap", "obviously", "in other words",
    "why bother", "here's", "we'll", "don't", "doesn't", "isn't", "can't", "won't", "honest", "plainly",
    "lever", "levers", "recipe", "a handful", "behave badly", "holds up", "by accident", "culprit", "regime",
)  # fmt: skip

#: Marketing and generic phrases that read as machine-written or promotional.
MARKETING = (
    "learn how", "delve", "seamless", "cutting-edge", "state-of-the-art", "game-changing", "unlock", "empower",
    "journey", "in today's", "it is worth noting", "it's worth noting", "dive into", "deep dive", "genuinely",
    "satisfied", "majestic", "see the future", "sticks", "failing", "leverage", "best-in-class", "world-class",
)  # fmt: skip

RULES: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile("—|–|\\\\u2014|\\\\u2013"), "em- or en-dash; use a comma, colon or new sentence"),
    (re.compile(r"\b(you|your|yours|yourself)\b", re.IGNORECASE), "second person"),
    (re.compile(r"^#{1,6} .*\?\s*$"), "heading phrased as a question; use a descriptive noun phrase"),
    *(
        (re.compile(rf"(?<![\w-]){re.escape(p)}(?![\w-])", re.IGNORECASE), f'conversational phrase "{p}"')
        for p in BANNED
    ),
    *((re.compile(rf"(?<![\w-]){re.escape(p)}(?![\w-])", re.IGNORECASE), f'marketing phrase "{p}"') for p in MARKETING),
)

FIELD = re.compile(r'^\s*"?(description|description-meta|subtitle)"?\s*:\s*(.*)$')
TITLE = re.compile(r'^\s*"?title"?\s*:\s*(.*)$')
PAGES = ("pages/about", "pages/blog", "pages/books", "pages/now", "pages/publication", "pages/software", "pages/talks")


def targets() -> list[Path]:
    """Every file whose copy is checked.

    Returns:
        Sorted paths of pages, data files and blog posts.
    """
    files = [ROOT / "index.qmd", ROOT / "404.qmd"]
    files += [ROOT / d / "index.qmd" for d in PAGES]
    files += [ROOT / "pages/books/mbuga.qmd", ROOT / "pages/software/data.yml", ROOT / "pages/books/books.yaml"]
    files += sorted((ROOT / "pages/blog/posts").rglob("index.qmd"))
    files += sorted((ROOT / "pages/blog/posts").rglob("*.ipynb"))
    return [f for f in files if f.exists()]


def check(path: Path) -> list[str]:
    """Findings for one file.

    Args:
        path: A page, data file or blog post.

    Returns:
        One ``file:line: reason`` string per finding.
    """
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    post = "pages/blog/posts" in str(path)
    notebook = path.suffix == ".ipynb"
    lines = path.read_text(encoding="utf-8").splitlines()
    found: list[str] = []
    front = lines[:1] == ["---"]
    fenced = html = False
    for number, line in enumerate(lines, start=1):
        text = None
        match = FIELD.match(line.lstrip(' "')) if notebook else FIELD.match(line)
        title = TITLE.match(line.lstrip(' "')) if notebook else TITLE.match(line)
        if match:
            text = match.group(2)
        elif title and post:
            text = title.group(1)
        elif path.suffix == ".qmd" and not post:
            stripped = line.strip()
            if front:
                front = not (number > 1 and stripped == "---")
            elif stripped.startswith("```"):
                fenced = not fenced
                html = stripped.startswith("```{=html}") or html
            elif fenced and html:
                text = re.sub(r"<[^>]*>", " ", line) if not stripped.startswith(("<!--",)) else None
            elif not fenced:
                text = re.sub(r"\]\([^)]*\)|\{[^}]*\}|`[^`]*`", " ", line)
            if fenced and not stripped.startswith("```") and not html:
                text = None
        if not text:
            continue
        for pattern, reason in RULES:
            if pattern.search(text):
                found.append(f"{rel}:{number}: {reason}")
    return found


def main(argv: list[str]) -> int:
    """Check the given files, or every copy file, and report findings.

    Args:
        argv: File paths; all copy files when empty.

    Returns:
        Process exit code: 0 when clean, 1 otherwise.
    """
    wanted = {Path(a).resolve() for a in argv}
    files = [f for f in targets() if not wanted or f.resolve() in wanted]
    findings = [line for f in files for line in check(f)]
    print("\n".join(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
