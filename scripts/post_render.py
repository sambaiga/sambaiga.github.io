"""Clean up the rendered site after Quarto has written it.

Two things, both about what a page asks of the reader's browser:

* Quarto writes a few small icons (such as the licence icon of the footer) as inline ``data:`` images without an
  ``alt`` attribute. A screen reader then announces the file name, so each one gets an empty ``alt``. Images that
  point to a file are never touched: they need real text, and the audit fails when it is missing.
* The Bootswatch themes (cosmo and darkly) start their CSS with an ``@import`` of a Google font. The site serves its
  own fonts (``assets/fonts``), so the import is removed and no page contacts a font service.

Quarto runs this after every render (``post-render`` in ``_quarto.yml``).
"""

from __future__ import annotations

import os
import re
from pathlib import Path

IMAGE = re.compile(r"<img\b(?![^>]*\balt=)([^>]*\bsrc=\"data:[^>]*)>")
FONT_IMPORT = re.compile(r"@import\s*(?:url\()?\s*[\"']https://fonts\.googleapis\.com[^\"')]*[\"']?\)?\s*;?")


def main() -> None:
    """Mark decorative inline images and remove third-party font imports."""
    root = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
    pages = styles = 0
    for page in root.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        patched = IMAGE.sub(r'<img alt=""\1>', text)
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
