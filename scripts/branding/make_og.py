"""Draw the default social preview image (1200 by 630 pixels) with the umeme illustration style.

The picture follows the standard of ``umeme.style.diagrams``: a heavy blue forecast curve, one pale prediction band,
hollow slate observations and symbolic axes. The text is the name, three formal lines of positioning and the four
tools. Colours and fonts come from the book's tokens, so the site and the book share one identity.

Usage:
    uv run --project ~/Documents/projects/umeme python scripts/branding/make_og.py --out images/og/default.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

from umeme.style.diagrams import HEADING, STRONG, TEXT, _canvas, profile
from umeme.style.tokens import BAND, INFO, NETWORK, SLATE_50, SLATE_300, SLATE_500, WHITE

WIDTH_PX, HEIGHT_PX, DPI = 1200, 630, 100
WIDTH_MM, HEIGHT_MM = WIDTH_PX / DPI * 25.4, HEIGHT_PX / DPI * 25.4
TOOLS = ("milia", "twiga", "popo", "umeme")


def forecast_panel(ax, left: float, bottom: float, width: float, height: float) -> None:
    """Draw the forecast illustration: observations, band and the forecast curve on symbolic axes."""
    hours = np.linspace(0, 24, 241)
    scale = height * 0.62 / 1.5
    curve = profile(hours)
    spread = 0.07 + 0.12 * curve
    xs = left + width * hours / 24
    base = bottom + 0.12 * height

    ax.fill_between(xs, base + scale * (curve - spread), base + scale * (curve + spread), color=BAND, lw=0, zorder=2)
    ax.plot(xs, base + scale * curve, color=INFO, lw=3.2, solid_capstyle="round", zorder=4)

    rng = np.random.default_rng(7)
    seen = np.arange(0.5, 24, 1.0)
    noise = rng.normal(0, 0.06, seen.size) * (0.6 + curve[(seen * 10).astype(int)])
    ax.scatter(
        left + width * seen / 24,
        base + scale * (profile(seen) + noise),
        s=26,
        facecolor=WHITE,
        edgecolor=NETWORK,
        linewidth=0.9,
        zorder=5,
    )

    axis_bottom = base - 4
    ax.plot([left, left], [axis_bottom, bottom + height * 0.9], color=NETWORK, lw=1.0, zorder=3)
    ax.plot([left, left + width], [axis_bottom, axis_bottom], color=NETWORK, lw=1.0, zorder=3)
    ax.text(left + width / 2, axis_bottom - 7, "Time", fontproperties=TEXT, fontsize=11, color=SLATE_500, ha="center")
    ax.text(left - 5, bottom + height * 0.5, "Demand", fontproperties=TEXT, fontsize=11, color=SLATE_500, rotation=90, ha="center", va="center")


def draw() -> object:
    """Compose the whole image and return the figure."""
    fig, ax = _canvas(HEIGHT_MM, WIDTH_MM)
    fig.patch.set_facecolor(SLATE_50)
    ax.add_patch(Rectangle((0, 0), WIDTH_MM, HEIGHT_MM, facecolor=SLATE_50, edgecolor="none", zorder=0))

    card = FancyBboxPatch(
        (158, 18), 130, HEIGHT_MM - 36, boxstyle="round,pad=0,rounding_size=3", facecolor=WHITE, edgecolor=SLATE_300, lw=0.8, zorder=1
    )
    ax.add_patch(card)
    ax.text(166, HEIGHT_MM - 30, "Forecast with a prediction interval", fontproperties=HEADING, fontsize=13, color=NETWORK, zorder=6)
    forecast_panel(ax, 178, 28, 98, HEIGHT_MM - 70)

    ax.add_patch(Rectangle((20, HEIGHT_MM - 36), 16, 1.8, facecolor=INFO, edgecolor="none", zorder=2))
    ax.text(20, HEIGHT_MM - 62, "Anthony Faustine", fontproperties=HEADING, fontsize=40, color=NETWORK, zorder=6)
    lines = (
        "Machine learning system architecture and design,",
        "time series algorithm development and",
        "strategic management of technology",
    )
    for row, line in enumerate(lines):
        ax.text(20, HEIGHT_MM - 78 - 8.5 * row, line, fontproperties=TEXT, fontsize=16, color=SLATE_500, zorder=6)

    ax.text(20, 46, "Open-source software and a book", fontproperties=STRONG, fontsize=11, color=NETWORK, zorder=6)
    for i, name in enumerate(TOOLS):
        x = 20 + 29 * i
        ax.add_patch(
            FancyBboxPatch((x, 28), 26, 11, boxstyle="round,pad=0,rounding_size=2", facecolor=WHITE, edgecolor=SLATE_300, lw=0.8, zorder=2)
        )
        ax.text(x + 13, 33.5, name, fontproperties=STRONG, fontsize=12, color=INFO, ha="center", va="center", zorder=6)
    ax.text(20, 18, "sambaiga.github.io", fontproperties=TEXT, fontsize=11, color=SLATE_500, zorder=6)
    return fig


def main() -> None:
    """Write the image to the path given on the command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    draw().savefig(args.out, dpi=DPI, facecolor=SLATE_50)


if __name__ == "__main__":
    main()
