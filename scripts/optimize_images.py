"""Resize and recompress web images in place.

Photographs and figures are scaled down to a width a page can use and saved again with a lighter encoding. A file is
only replaced when the result is smaller. The originals stay in the git history.

Usage:
    uv run --with pillow python scripts/optimize_images.py images/profiles/photo.jpg --max-width 900
    uv run --with pillow python scripts/optimize_images.py --over 400 images pages
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

SUFFIXES = {".jpg", ".jpeg", ".png"}


def optimise(path: Path, max_width: int, quality: int) -> tuple[int, int]:
    """Resize and recompress one image, replacing it only when the result is smaller.

    Args:
        path: A JPEG or PNG file.
        max_width: The widest the image may be, in pixels.
        quality: JPEG quality from 1 to 95.

    Returns:
        The size in bytes before and after.
    """
    before = path.stat().st_size
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source)
        if image.width > max_width:
            image = image.resize((max_width, round(image.height * max_width / image.width)), Image.LANCZOS)
        temporary = path.with_name(path.name + ".tmp")
        if path.suffix.lower() == ".png":
            image.save(temporary, format="PNG", optimize=True)
        else:
            image.convert("RGB").save(temporary, format="JPEG", quality=quality, optimize=True, progressive=True)
    after = temporary.stat().st_size
    if after < before:
        temporary.replace(path)
        return before, after
    temporary.unlink()
    return before, before


def main() -> None:
    """Optimise the given files, or every image above ``--over`` KB in the given folders."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", type=Path, help="Image files or folders")
    parser.add_argument("--max-width", type=int, default=1600)
    parser.add_argument("--quality", type=int, default=82)
    parser.add_argument("--over", type=int, default=0, help="Only touch files above this size in KB")
    args = parser.parse_args()
    files = [
        f for p in args.paths for f in ([p] if p.is_file() else sorted(p.rglob("*"))) if f.suffix.lower() in SUFFIXES
    ]
    for file in files:
        if file.stat().st_size / 1024 <= args.over:
            continue
        before, after = optimise(file, args.max_width, args.quality)
        print(f"{file}: {before / 1024:,.0f} KB -> {after / 1024:,.0f} KB")


if __name__ == "__main__":
    main()
