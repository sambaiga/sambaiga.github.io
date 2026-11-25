"""Clean up the rendered site after Quarto has written it.

Five things, all about what a page asks of the reader's browser:

* Quarto writes a few small icons (such as the licence icon of the footer) as inline ``data:`` images without an
  ``alt`` attribute. A screen reader then announces the file name, so each one gets an empty ``alt``. Images that
  point to a file are never touched: they need real text, and the audit fails when it is missing.
* Quarto puts ``role="menu"`` on the button that opens the navbar on a phone. A button already has a role, and the
  extra one is announced wrongly, so it is removed.
* The Bootswatch themes (cosmo and darkly) start their CSS with an ``@import`` of a Google font. The site serves its
  own fonts (``assets/fonts``), so the import is removed and no page contacts a font service.
* A notebook page with an HTML output gets jQuery and require.js from a content delivery network. The figures of the
  posts are inline SVG and need neither, so the two script tags are removed and no page contacts that host.

* A footnote entry gets its number as a label, so that the hover preview shows it (see ``number_footnotes``).

Quarto runs this after every render (``post-render`` in ``_quarto.yml``).
"""

from __future__ import annotations

import os
import re
from pathlib import Path

IMAGE = re.compile(r"<img\b(?![^>]*\balt=)([^>]*\bsrc=\"data:[^>]*)>")
TOGGLER = re.compile(r'(<button class="navbar-toggler[^>]*?) role="menu"')
FONT_IMPORT = re.compile(r"@import\s*(?:url\()?\s*[\"']https://fonts\.googleapis\.com[^\"')]*[\"']?\)?\s*;?")


# Quarto adds jQuery and require.js, from a content delivery network, to a page that has an HTML output of a notebook,
# and a one-line script that registers jQuery with require.js. The figures of the posts are inline SVG and need none of
# them, and the site requests nothing from a third party, so all three are removed together.
NOTEBOOK_SCRIPT = re.compile(
    r'<script[^>]+src="https://cdn\.jsdelivr\.net/npm/(?:requirejs|jquery)@[^"]+"[^>]*></script>\s*'
    r"|<script[^>]*>\s*define\('jquery',\s*\[\],\s*function\(\)\s*\{return window\.jQuery;\}\)\s*;?\s*</script>\s*"
)


# A footnote of a post is a numbered reference. The list at the end shows its number as a marker, but the preview that
# opens on hover (footnotes-hover) carries only the text, so the number is written into the entry as a label that the
# list hides and the preview shows.
FOOTNOTE = re.compile(r'(<li id="fn(\d+)"[^>]*>\s*<p>)(?!<span class="fn-label">)')


def number_footnotes(text: str) -> str:
    """Write the number of each footnote into its entry, so that the hover preview shows it."""
    return FOOTNOTE.sub(lambda m: f'{m.group(1)}<span class="fn-label">[{m.group(2)}]</span> ', text)


def main() -> None:
    """Mark decorative images, remove third-party font imports and the scripts that Quarto adds for notebook output."""
    root = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
    pages = styles = 0
    for page in root.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        patched = number_footnotes(NOTEBOOK_SCRIPT.sub("", TOGGLER.sub(r"\1", IMAGE.sub(r'<img alt=""\1>', text))))
        if patched != text:
            page.write_text(patched, encoding="utf-8")
            pages += 1
    for sheet in root.rglob("*.css"):
        text = sheet.read_text(encoding="utf-8")
        patched = FONT_IMPORT.sub("", text)
        if patched != text:
            sheet.write_text(patched, encoding="utf-8")
            styles += 1
    print(f"post_render: decorative images marked in {pages} pages, font imports removed from {styles} stylesheets")


if __name__ == "__main__":
    main()
