"""Check that the brand colours of _brand.yml agree with the SCSS tokens and the logo script.

Usage:
    python scripts/check_brand.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def palette() -> dict[str, str]:
    """Read the palette of ``_brand.yml`` without a YAML dependency.

    Returns:
        Colour name to upper-case hex value.
    """
    text = (ROOT / "_brand.yml").read_text()
    block = text.split("palette:")[1].split("foreground:")[0]
    return {k: v.upper() for k, v in re.findall(r'^\s+(\w+): "(#[0-9A-Fa-f]{6})"', block, re.M)}


def scss(path: str, name: str) -> str:
    """Return the value of one SCSS variable.

    Args:
        path: File relative to the repository root.
        name: Variable name without the dollar sign.

    Returns:
        The upper-case hex value, or an empty string when the variable is absent.
    """
    match = re.search(rf"^\${name}:\s*(#[0-9A-Fa-f]{{6}})", (ROOT / path).read_text(), re.M)
    return match.group(1).upper() if match else ""


def main() -> int:
    """Compare the values and print every mismatch.

    Returns:
        Zero when everything agrees, one otherwise.
    """
    colours = palette()
    logo = (ROOT / "scripts/branding/make_logo.py").read_text()
    checks = [
        ("blue", scss("assets/scss/_defaults.scss", "blue")),
        ("orange", scss("assets/scss/_defaults.scss", "orange")),
        ("green", scss("assets/scss/_defaults.scss", "green")),
        ("red", scss("assets/scss/_defaults.scss", "red")),
        ("slate", scss("assets/scss/_defaults.scss", "teal")),
        ("sky", scss("assets/twiga-dark.scss", "teal")),
        ("night", scss("assets/twiga-dark.scss", "body-bg")),
    ]
    failures = [f"{n}: _brand.yml {colours.get(n)} vs scss {v}" for n, v in checks if colours.get(n) != v]
    for name in ("slate", "orange", "night"):
        if colours[name] not in logo.upper():
            failures.append(f"{name}: {colours[name]} not found in make_logo.py")
    print("\n".join(failures) or "brand tokens agree")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
