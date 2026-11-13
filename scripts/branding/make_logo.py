"""Draw the sambaiga logo: one letter S and the five tools built around it.

The mark is the lowercase s of the wordmark font in a slate tile. Five dots rise from it, one for each tool of
the family (kobe, milia, twiga, popo and umeme), so the badge reads as one author and one stack. Every colour
is from the site and book palette: slate, blue and orange, with their tints. The wordmark
is Jost SemiBold converted to outlines, with the dot of the i in orange, so no font is needed to view the files.
The favicon keeps only the s and a single orange dot, because five dots do not survive at 16 pixels.

The script writes the badge, the favicon, the wordmark and the lockup (badge plus wordmark) on light and dark
backgrounds and in one colour, as SVG with PNG copies when ``rsvg-convert`` is installed, and ``favicon.ico``
when Pillow is installed.

Usage:
    uv run --with fonttools --with pillow python scripts/branding/make_logo.py \
        --fonts ~/Documents/projects/umeme --out images/brand
"""

from __future__ import annotations

import argparse
import math
import shutil
import subprocess
from functools import lru_cache
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

SLATE, ORANGE = "#1E293B", "#E26029"
PAPER, NIGHT = "#F8FAFC", "#0F172A"
WORD = "sambaiga"
SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box}" fill="none">'

# One dot per tool, from the slate, blue and orange families of the site and book palette, so the badge adds no
# colour the site does not use. The order runs from the foundation (slate) to the book (orange).
FAMILY = (
    ("kobe", "#94A3B8"),
    ("milia", "#81B4D0"),
    ("twiga", "#38BDF8"),
    ("popo", "#F0B094"),
    ("umeme", ORANGE),
)

THEMES = {
    "light": {"ink": SLATE, "dot": ORANGE, "bg": PAPER},
    "dark": {"ink": "#F1F5F9", "dot": ORANGE, "bg": NIGHT},
    "mono": {"ink": SLATE, "dot": SLATE, "bg": "#FFFFFF"},
}

Bounds = tuple[float, float, float, float]


@lru_cache(maxsize=4)
def load(font_file: Path) -> TTFont:
    """Open a font once.

    Args:
        font_file: A TrueType font file.

    Returns:
        The opened font.
    """
    return TTFont(font_file)


def contours(
    font_file: Path, char: str, x: float, baseline: float, size: float
) -> tuple[list[tuple[str, Bounds]], float]:
    """Convert one character to SVG path data, one entry per contour.

    Args:
        font_file: A TrueType font file.
        char: The character to set.
        x: Left edge of the glyph.
        baseline: Vertical position of the baseline.
        size: Font size in canvas units.

    Returns:
        The path data and bounds of every contour, and the advance width of the character.
    """
    font = load(font_file)
    glyphs = font.getGlyphSet()
    name = font.getBestCmap()[ord(char)]
    scale = size / font["head"].unitsPerEm
    matrix = (scale, 0, 0, -scale, x, baseline)
    recording = DecomposingRecordingPen(glyphs)
    glyphs[name].draw(recording)
    pieces: list[list[tuple[str, tuple]]] = []
    for op, args in recording.value:
        if op == "moveTo":
            pieces.append([])
        pieces[-1].append((op, args))
    out = []
    for piece in pieces:
        path, box = SVGPathPen(glyphs), BoundsPen(glyphs)
        for op, args in piece:
            getattr(TransformPen(path, matrix), op)(*args)
            getattr(TransformPen(box, matrix), op)(*args)
        out.append((path.getCommands(), box.bounds))
    return out, font["hmtx"][name][0] * scale


def wordmark(font_file: Path, x: float, baseline: float, size: float, ink: str, dot: str) -> tuple[str, float]:
    """Set the wordmark with the dot of the i in its own colour.

    Args:
        font_file: The wordmark font.
        x: Left edge of the first letter.
        baseline: Vertical position of the baseline.
        size: Font size in canvas units.
        ink: Colour of the letters.
        dot: Colour of the dot of the i.

    Returns:
        SVG elements and the width of the wordmark.
    """
    parts, cursor = [], x
    for char in WORD:
        shapes, advance = contours(font_file, char, cursor, baseline, size)
        if char == "i":
            top = min(shapes, key=lambda shape: shape[1][1])
            parts.extend(f'<path d="{shape[0]}" fill="{dot if shape is top else ink}"/>' for shape in shapes)
        else:
            # One path per glyph keeps the counters of b, a and g open.
            parts.append(f'<path d="{" ".join(d for d, _ in shapes)}" fill="{ink}"/>')
        cursor += advance
    return "".join(parts), cursor - x


def tile(font_file: Path, family: bool) -> str:
    """Draw the slate tile with the s, on a 100 x 100 canvas.

    Args:
        font_file: The wordmark font.
        family: Draw the five tool dots when true, a single orange dot when false.

    Returns:
        SVG elements.
    """
    shapes, _ = contours(font_file, "s", 0, 0, 78)
    left, top = min(s[1][0] for s in shapes), min(s[1][1] for s in shapes)
    right, bottom = max(s[1][2] for s in shapes), max(s[1][3] for s in shapes)
    dx, dy = 47 - (left + right) / 2, 56 - (top + bottom) / 2
    glyph = f'<path d="{" ".join(d for d, _ in shapes)}" fill="#F1F5F9"/>'
    out = [
        f'<rect width="100" height="100" rx="22" fill="{SLATE}"/>',
        f'<g transform="translate({dx:.1f} {dy:.1f})">{glyph}</g>',
    ]
    if family:
        for i, (_, colour) in enumerate(FAMILY):
            angle = math.radians(-84 + 15 * i)
            cx, cy = 50 + 40 * math.cos(angle), 50 + 40 * math.sin(angle)
            out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{3.6 + 0.5 * i:.1f}" fill="{colour}"/>')
    else:
        out.append(f'<circle cx="76" cy="26" r="9" fill="{ORANGE}"/>')
    return "".join(out)


def badge(font_file: Path, family: bool = True) -> str:
    """Build the square badge, used as avatar and, without the family dots, as favicon.

    Args:
        font_file: The wordmark font.
        family: Draw the five tool dots.

    Returns:
        A complete SVG document.
    """
    return f"{SVG.format(box='0 0 100 100')}{tile(font_file, family)}</svg>"


def lockup(font_file: Path, theme: str, with_badge: bool, transparent: bool = True) -> str:
    """Build the wordmark, with or without the badge, for one background.

    Args:
        font_file: The wordmark font.
        theme: ``light``, ``dark`` or ``mono``.
        with_badge: Put the badge before the wordmark.
        transparent: Leave the background out, for use on a page.

    Returns:
        A complete SVG document.
    """
    c = THEMES[theme]
    left = 124 if with_badge else 14
    text, width = wordmark(font_file, left, 80, 68, c["ink"], c["dot"])
    total = left + width + 14
    back = "" if transparent else f'<rect width="{total:.0f}" height="120" rx="12" fill="{c["bg"]}"/>'
    mark = f'<g transform="translate(10 10)">{tile(font_file, family=theme != "mono")}</g>' if with_badge else ""
    return f"{SVG.format(box=f'0 0 {total:.0f} 120')}{back}{mark}{text}</svg>"


def png(svg: Path, width: int) -> None:
    """Render an SVG to a PNG next to it, if ``rsvg-convert`` is installed.

    Args:
        svg: The SVG file.
        width: Output width in pixels.
    """
    tool = shutil.which("rsvg-convert")
    if tool:
        target = svg.with_name(f"{svg.stem}-{width}.png")
        subprocess.run([tool, "-w", str(width), str(svg), "-o", str(target)], check=True)


def ico(source: Path, target: Path) -> None:
    """Write a multi-size ``favicon.ico`` from a large PNG, if Pillow is installed.

    Args:
        source: The 512 pixel favicon PNG.
        target: The ``.ico`` file to write.
    """
    try:
        from PIL import Image
    except ImportError:
        return
    Image.open(source).save(target, sizes=[(16, 16), (32, 32), (48, 48)])


def main() -> None:
    """Write every file."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fonts", type=Path, required=True, help="Directory holding Jost-SemiBold.ttf")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    args = parser.parse_args()
    font_file = args.fonts / "Jost-SemiBold.ttf"
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "badge.svg").write_text(badge(font_file))
    (args.out / "favicon.svg").write_text(badge(font_file, family=False))
    for size in (32, 180, 512):
        png(args.out / "badge.svg", size)
    for size in (32, 512):
        png(args.out / "favicon.svg", size)
    for theme in THEMES:
        (args.out / f"wordmark-{theme}.svg").write_text(lockup(font_file, theme, with_badge=False))
        (args.out / f"lockup-{theme}.svg").write_text(lockup(font_file, theme, with_badge=True))
        png(args.out / f"wordmark-{theme}.svg", 1000)
        png(args.out / f"lockup-{theme}.svg", 1200)
    if (args.out / "favicon-512.png").exists():
        ico(args.out / "favicon-512.png", args.out / "favicon.ico")


if __name__ == "__main__":
    main()
