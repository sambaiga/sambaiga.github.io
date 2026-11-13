"""Audit the rendered site for the basics of a well-made web page.

Every page is read once. A page fails the audit when it lacks something a browser, a search engine or a screen
reader depends on: the language, a title, a description, a canonical address, a share image, the viewport, a single
heading of level one, a text alternative for each image, a safe ``rel`` on links that open a new tab, or when it loads a
script or style from a third party. Softer
findings (skipped heading levels, links without a name) are reported as warnings.

Usage:
    python3 scripts/audit_site.py _site
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

# Folders of the output that hold copied resources, not pages of the site.
SKIP = ("assets", "docs", "files", "images", "_extensions", "site_libs")
# Hosts that pages may load scripts and styles from: the site itself only, so a page never depends on a third party.
ALLOWED_HOSTS: set[str] = set()
# Quarto writes a file of about 90 bytes for a draft page.
STUB_BYTES = 500


class Page(HTMLParser):
    """Collect what the audit needs from one HTML page."""

    def __init__(self) -> None:
        """Start with an empty record."""
        super().__init__()
        self.lang = None
        self.title = ""
        self.in_title = False
        self.meta: dict[str, str] = {}
        self.canonical = None
        self.h1 = 0
        self.levels: list[int] = []
        self.images: list[dict[str, str | None]] = []
        self.links: list[dict[str, str | None]] = []
        self.hosts: set[str] = set()
        self.ids: Counter[str] = Counter()
        self.nameless_links = 0
        self._link: dict[str, str | None] | None = None
        self._text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Record one opening tag.

        Args:
            tag: The tag name.
            attrs: Its attributes.
        """
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content") or ""
        elif tag == "link":
            if a.get("rel") == "canonical":
                self.canonical = a.get("href")
            if (a.get("href") or "").startswith("http"):
                self.hosts.add((a["href"] or "").split("/")[2])
        elif tag == "script" and (a.get("src") or "").startswith("http"):
            self.hosts.add((a["src"] or "").split("/")[2])
        elif tag == "img":
            self.images.append(a)
        elif tag == "a":
            self.links.append(a)
            self._link, self._text = a, ""
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.levels.append(int(tag[1]))
            self.h1 += tag == "h1"
        if a.get("id"):
            self.ids[a["id"] or ""] += 1

    def handle_endtag(self, tag: str) -> None:
        """Close the title or a link.

        Args:
            tag: The tag name.
        """
        if tag == "title":
            self.in_title = False
        elif tag == "a" and self._link is not None:
            named = self._text.strip() or self._link.get("aria-label") or self._link.get("title")
            hidden = self._link.get("aria-hidden") == "true"
            self.nameless_links += not (named or hidden)
            self._link = None

    def handle_data(self, data: str) -> None:
        """Collect text for the title and for link names.

        Args:
            data: A run of text.
        """
        if self.in_title:
            self.title += data
        if self._link is not None:
            self._text += data


def audit(path: Path) -> tuple[list[str], list[str]]:
    """Audit one page.

    Args:
        path: The HTML file.

    Returns:
        The errors and the warnings found on the page.
    """
    page = Page()
    page.feed(path.read_text(encoding="utf-8", errors="ignore"))
    errors, warnings = [], []
    checks = {
        "no lang attribute on <html>": bool(page.lang),
        "empty <title>": bool(page.title.strip()),
        "no meta description": bool(page.meta.get("description", "").strip()),
        "no canonical link": bool(page.canonical),
        "no og:image": bool(page.meta.get("og:image", "").strip()),
        "no viewport meta": "viewport" in page.meta,
    }
    errors += [message for message, ok in checks.items() if not ok]
    if page.h1 != 1:
        errors.append(f"{page.h1} headings of level one (expected 1)")
    missing_alt = sum(1 for image in page.images if "alt" not in image)
    if missing_alt:
        errors.append(f"{missing_alt} image(s) without an alt attribute")
    unsafe = sum(
        1
        for link in page.links
        if link.get("target") == "_blank" and not {"noopener", "noreferrer"} & set((link.get("rel") or "").split())
    )
    if unsafe:
        errors.append(f"{unsafe} link(s) open a new tab without rel=noopener")
    insecure = [link["href"] for link in page.links if (link.get("href") or "").startswith("http://")]
    if insecure:
        warnings.append(f"{len(insecure)} link(s) use http, e.g. {insecure[0]}")
    if any(b - a > 1 for a, b in zip(page.levels, page.levels[1:], strict=False)):
        warnings.append("a heading level is skipped")
    if page.nameless_links:
        warnings.append(f"{page.nameless_links} link(s) without text or a label")
    duplicates = [i for i, n in page.ids.items() if n > 1 and not i.startswith("quarto-")]
    if duplicates:
        warnings.append(f"duplicate ids: {duplicates[:3]}")
    foreign = sorted(page.hosts - ALLOWED_HOSTS - {"sambaiga.github.io"})
    if foreign:
        errors.append(f"third-party hosts: {foreign}")
    return errors, warnings


def audit_styles(base: Path) -> list[str]:
    """Find stylesheets that import from a third party.

    Args:
        base: The folder of the rendered site.

    Returns:
        One message per stylesheet with an ``@import`` of an outside address.
    """
    found = []
    for sheet in sorted(base.rglob("*.css")):
        text = sheet.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"@import\s*(?:url\()?\s*[\"']?https?://", text):
            found.append(f"{sheet.relative_to(base)}: imports from a third party")
    return found


def main(root: str) -> int:
    """Audit every page below ``root``.

    Args:
        root: The folder of the rendered site.

    Returns:
        1 when any page has an error, otherwise 0.
    """
    base = Path(root)
    # A draft page is an empty stub (draft-mode: gone), not a page of the site.
    pages = [
        p
        for p in sorted(base.rglob("*.html"))
        if p.relative_to(base).parts[0] not in SKIP and p.stat().st_size > STUB_BYTES
    ]
    failed = 0
    for path in pages:
        errors, warnings = audit(path)
        name = path.relative_to(base)
        for message in errors:
            print(f"ERROR   {name}: {message}")
        for message in warnings:
            print(f"warning {name}: {message}")
        failed += bool(errors)
    styles = audit_styles(base)
    for message in styles:
        print(f"ERROR   {message}")
    print(f"\n{len(pages)} pages audited, {failed} with errors")
    return 1 if failed or styles else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "_site"))
