"""Fail when an image is too large for a web page.

Used by the ``image-size`` hook. Photographs and figures of several megabytes are the most common reason a page is
slow, so an image above the limit must be resized first (``scripts/optimize_images.py``).

Usage:
    python scripts/check_image_size.py images/profiles/photo.jpg
"""

from __future__ import annotations

import sys
from pathlib import Path

LIMIT_KB = {".png": 800}  # figures and diagrams compress less well than photographs
DEFAULT_KB = 400


def limit(path: str) -> int:
    """Return the size limit in KB for an image.

    Args:
        path: The image file.

    Returns:
        The limit for its type.
    """
    return LIMIT_KB.get(Path(path).suffix.lower(), DEFAULT_KB)


def main(paths: list[str]) -> int:
    """Report every image above the limit.

    Args:
        paths: Image files to check.

    Returns:
        1 when an image is too large, otherwise 0.
    """
    too_large = [(path, Path(path).stat().st_size / 1024) for path in paths if Path(path).is_file()]
    too_large = [(path, size) for path, size in too_large if size > limit(path)]
    for path, size in too_large:
        print(f"{path}: {size:,.0f} KB is above {limit(path)} KB; resize it with scripts/optimize_images.py")
    return 1 if too_large else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
