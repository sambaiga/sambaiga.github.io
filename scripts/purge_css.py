"""Remove the CSS rules and the icons that no page of the built site uses, and prove that nothing visible changed.

The two theme stylesheets of the site (light and dark) are about 660 KB each, because they carry all of Bootstrap and
of Quarto while a page uses a tenth of it, and the icon font is 176 KB for about thirty icons. This script keeps only
what matters, and decides it with a real browser instead of guessing from text:

* every built page is opened in Chrome in the light and in the dark scheme, so rules for ``body.quarto-dark`` count;
* a selector is kept when ``document.querySelector`` finds an element for it on any page, after the parts that depend
  on the state of the user (``:hover``, ``:focus``, ``::before`` and the like) are removed from the question;
* a selector is also kept when a script can add its class at run time: the whole class name is a word of a script, an
  icon (``bi-file-text``) is named in a script (``file-text``), or the class belongs to a widget that builds its names
  in code (the search box, tooltips);
* a selector the browser cannot parse is kept;
* the icon font is cut down to the icons of the rules that are kept.

Then the check: the computed style of every element is recorded on every page, in both schemes, before and after
the purge (elements that already differ between two loads of the same page are left out). If a single value
differs, the original files are put back and the script fails, so a purge can never change how the site looks, only
how much of it is downloaded.

It needs Playwright, Chrome, tinycss2 and fonttools with brotli, so it runs in CI and when asked, not on every local
preview.

Usage:
    uv run --with playwright --with tinycss2 --with fonttools --with brotli python scripts/purge_css.py _site
"""

from __future__ import annotations

import contextlib
import functools
import http.server
import io
import re
import sys
import threading
from collections.abc import Iterator
from pathlib import Path

import tinycss2
from fontTools import subset
from fontTools.ttLib import TTFont
from playwright.sync_api import sync_playwright

# Parts of a selector that depend on what the reader does or on how the browser draws, not on the page itself.
STATE = re.compile(
    r"::?(?:hover|focus|focus-within|focus-visible|active|visited|link|target|checked|disabled|enabled|read-only"
    r"|read-write|required|optional|valid|invalid|in-range|out-of-range|placeholder-shown|autofill|indeterminate"
    r"|default|fullscreen|before|after|first-line|first-letter|selection|placeholder|marker|backdrop|file-selector-button"
    r"|-webkit-[\w-]+|-moz-[\w-]+|-ms-[\w-]+|[\w-]+-thumb|[\w-]+-track)(?:\([^)]*\))?"
)
CLASS = re.compile(r"\.((?:[\w-]|\\.)+)")
WORD = re.compile(r"[A-Za-z_][\w-]*")
CODEPOINT = re.compile(r'content:\s*"(?:\\([0-9a-fA-F]+)|(.))"')
# Widgets that build their class names in code, so no script contains the whole name.
DYNAMIC_PREFIXES = ("aa-", "tippy", "algolia", "quarto-search", "headroom")
SKIP_FOLDERS = ("assets", "docs", "files", "images", "_extensions", "site_libs")
STUB_BYTES = 500
MATCH = (
    """(qs) => qs.filter((q) => { try { return document.querySelector(q) !== null; } catch (e) { return true; } })"""
)
# One number per element, from the properties that decide how it looks and where it sits.
SIGNATURE = """() => {
  const props = ["display", "position", "visibility", "opacity", "color", "backgroundColor", "backgroundImage",
    "fontFamily", "fontSize", "fontWeight", "fontStyle", "lineHeight", "letterSpacing", "textAlign",
    "textDecorationLine",
    "textTransform", "marginTop", "marginRight", "marginBottom", "marginLeft", "paddingTop", "paddingRight",
    "paddingBottom", "paddingLeft", "borderTopWidth", "borderTopColor", "borderBottomWidth", "borderBottomColor",
    "borderLeftWidth", "borderRightWidth", "borderRadius", "boxShadow", "width", "height", "flexDirection",
    "justifyContent", "alignItems", "gridTemplateColumns", "transform", "overflow", "zIndex", "cursor"];
  return Array.from(document.querySelectorAll("*")).map((el) => {
    const s = getComputedStyle(el); let h = 5381;
    for (const p of props) {
      const v = s[p];
      for (let i = 0; i < v.length; i++) h = ((h << 5) + h + v.charCodeAt(i)) | 0;
    }
    return el.tagName.toLowerCase() + "." + String(el.className).slice(0, 40) + "#" + h;
  });
}"""


def pages_of(root: Path) -> list[Path]:
    """List the built pages, without copied resources and without the stubs of draft pages.

    Args:
        root: The folder of the built site.

    Returns:
        The HTML files of the site.
    """
    return [
        p
        for p in sorted(root.rglob("*.html"))
        if p.relative_to(root).parts[0] not in SKIP_FOLDERS and p.stat().st_size > STUB_BYTES
    ]


@contextlib.contextmanager
def serving(root: Path) -> Iterator[int]:
    """Serve a folder on a free local port.

    Args:
        root: The folder to serve.

    Yields:
        The port number.
    """
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    handler.log_message = lambda *args, **kwargs: None  # type: ignore[method-assign]
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        yield server.server_address[1]
    finally:
        server.shutdown()


def visit(root: Path, action) -> None:  # noqa: ANN001
    """Open every page in both colour schemes and call ``action`` with the scheme, the path and the page.

    Args:
        root: The folder of the built site.
        action: A function of ``(scheme, path, page)``.
    """
    with serving(root) as port, sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for scheme in ("light", "dark"):
            page = browser.new_context(color_scheme=scheme, viewport={"width": 1300, "height": 900}).new_page()
            for path in pages_of(root):
                try:
                    page.goto(f"http://127.0.0.1:{port}/{path.relative_to(root)}", wait_until="load", timeout=60000)
                except Exception as error:  # a page that does not load must not stop the others
                    print(f"purge_css: could not load {path.relative_to(root)}: {error}")
                    continue
                page.add_style_tag(content="*{animation:none!important;transition:none!important}")
                page.wait_for_timeout(700)
                action(scheme, str(path.relative_to(root)), page)
        browser.close()


def script_words(root: Path) -> set[str]:
    """Collect every word of the scripts of the site, which is where run-time classes come from.

    Args:
        root: The folder of the built site.

    Returns:
        The set of words found in the scripts.
    """
    words: set[str] = set()
    for script in root.rglob("*.js"):
        words.update(WORD.findall(script.read_text(encoding="utf-8", errors="ignore")))
    return words


def named_in_script(name: str, words: set[str]) -> bool:
    """Tell whether a class can be added by a script.

    Args:
        name: A class name of a selector.
        words: The words of the scripts of the site.

    Returns:
        True when the whole name, or the icon name behind ``bi-``, is a word of a script, or the name begins with a
        prefix of a widget that builds its names in code.
    """
    icon = name[3:] if name.startswith("bi-") else ""
    return name in words or name.startswith(DYNAMIC_PREFIXES) or bool(icon and icon in words)


def split(prelude: str) -> list[str]:
    """Split a selector list on the commas that are not inside brackets.

    Args:
        prelude: The text before the block of a rule.

    Returns:
        The selectors of the list.
    """
    parts, depth, start = [], 0, 0
    for i, char in enumerate(prelude):
        if char in "([":
            depth += 1
        elif char in ")]":
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(prelude[start:i].strip())
            start = i + 1
    parts.append(prelude[start:].strip())
    return [p for p in parts if p]


def collect(rules: list, found: set[str]) -> None:
    """Gather every selector of a list of rules, also inside media rules.

    Args:
        rules: Parsed rules.
        found: The set the selectors are added to.
    """
    for rule in rules:
        if rule.type == "qualified-rule":
            found.update(split(tinycss2.serialize(rule.prelude)))
        elif rule.type == "at-rule" and rule.content is not None and rule.lower_at_keyword in {"media", "supports"}:
            collect(tinycss2.parse_rule_list(rule.content, skip_whitespace=True, skip_comments=True), found)


def prune(rules: list, keep: set[str]) -> str:
    """Write the rules back, keeping only the selectors in ``keep`` and dropping what becomes empty.

    Args:
        rules: Parsed rules.
        keep: The selectors to keep.

    Returns:
        The minified CSS text.
    """
    out = []
    for rule in rules:
        if rule.type == "qualified-rule":
            kept = [s for s in split(tinycss2.serialize(rule.prelude)) if s in keep]
            if kept:
                out.append(",".join(kept) + "{" + tinycss2.serialize(rule.content) + "}")
        elif rule.type == "at-rule" and rule.content is not None and rule.lower_at_keyword in {"media", "supports"}:
            inner = prune(tinycss2.parse_rule_list(rule.content, skip_whitespace=True, skip_comments=True), keep)
            if inner:
                out.append(f"@{rule.at_keyword} {tinycss2.serialize(rule.prelude).strip()}{{{inner}}}")
        else:
            out.append(tinycss2.serialize([rule]))
    return "".join(out)


def used_selectors(root: Path, selectors: set[str]) -> set[str]:
    """Ask Chrome which selectors have an element on any page, in both colour schemes.

    Args:
        root: The folder of the built site.
        selectors: The selectors to test.

    Returns:
        The selectors that match, plus those that cannot be asked about.
    """
    questions = {s: STATE.sub("", s).strip() for s in selectors}
    open_questions = {q for q in questions.values() if q}
    answered: set[str] = set()

    def ask(_scheme: str, _path: str, page) -> None:  # noqa: ANN001
        hits = set(page.evaluate(MATCH, sorted(open_questions)))
        answered.update(hits)
        open_questions.difference_update(hits)

    visit(root, ask)
    return {s for s, q in questions.items() if not q or q in answered}


def signatures(root: Path) -> dict[tuple[str, str], list[str]]:
    """Record the computed style of every element of every page, in both colour schemes.

    Args:
        root: The folder of the built site.

    Returns:
        For each scheme and page, one entry per element.
    """
    recorded: dict[tuple[str, str], list[str]] = {}
    visit(root, lambda scheme, path, page: recorded.__setitem__((scheme, path), page.evaluate(SIGNATURE)))
    return recorded


def subset_icons(root: Path, css: Path, kept_css: str) -> Path | None:
    """Cut the icon font down to the icons of the rules that are kept, as a woff2 file.

    Args:
        root: The folder of the built site.
        css: The icon stylesheet, which names the font file.
        kept_css: The text of the icon stylesheet after the purge.

    Returns:
        The original icon font, which nothing refers to any more, or None when there was nothing to cut.
    """
    codepoints = sorted({int(code, 16) if code else ord(char) for code, char in CODEPOINT.findall(kept_css)})
    source = next(root.glob("site_libs/bootstrap/bootstrap-icons.woff"), None)
    if not codepoints or source is None:
        return None
    font = TTFont(source)
    options = subset.Options(flavor="woff2", layout_features=[], notdef_outline=False, name_IDs=[], hinting=False)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=codepoints)
    subsetter.subset(font)
    font.flavor = "woff2"
    target = source.with_name("bootstrap-icons-subset.woff2")
    buffer = io.BytesIO()
    font.save(buffer)
    target.write_bytes(buffer.getvalue())
    face = re.sub(r"src:[^;}]*", 'src:url("./bootstrap-icons-subset.woff2") format("woff2")', kept_css, count=1)
    css.write_text(face, encoding="utf-8")
    print(
        f"purge_css: icon font {source.stat().st_size // 1024} KB -> {target.stat().st_size // 1024} KB, "
        f"{len(codepoints)} icons"
    )
    return source


def purge(root: Path) -> int:
    """Purge every Bootstrap stylesheet of the site in place, and undo it if anything visible changes.

    Args:
        root: The folder of the built site.

    Returns:
        0 when the purge is kept, 1 when it was undone because the site would look different.
    """
    sheets = sorted(root.glob("site_libs/bootstrap/*.css"))
    original = {sheet: sheet.read_text(encoding="utf-8") for sheet in sheets}
    parsed = {
        sheet: tinycss2.parse_stylesheet(text, skip_whitespace=True, skip_comments=True)
        for sheet, text in original.items()
    }
    selectors: set[str] = set()
    for rules in parsed.values():
        collect(rules, selectors)
    kept = used_selectors(root, selectors)
    words = script_words(root)
    for selector in selectors - kept:
        classes = [c.replace("\\", "") for c in CLASS.findall(selector)]
        if classes and any(named_in_script(c, words) for c in classes):
            kept.add(selector)
    before = signatures(root)
    spare_fonts: list[Path] = []
    # Elements that look different between two loads of the same page (a carousel, an image still loading) cannot
    # prove or disprove anything, so they are left out of the comparison.
    again = signatures(root)
    unstable = {
        (key, i)
        for key in before
        for i, (a, b) in enumerate(zip(before[key], again.get(key, []), strict=False))
        if a != b
    }
    for sheet, rules in parsed.items():
        text = prune(rules, kept)
        sheet.write_text(text, encoding="utf-8")
        if sheet.name == "bootstrap-icons.css":
            spare = subset_icons(root, sheet, text)
            if spare is not None:
                spare_fonts.append(spare)
        print(f"purge_css: {sheet.name[:28]} {len(original[sheet]) // 1024} KB -> {sheet.stat().st_size // 1024} KB")
    after = signatures(root)
    differences = [
        (key, i, a, b)
        for key in before
        for i, (a, b) in enumerate(zip(before[key], after.get(key, []), strict=False))
        if a != b and (key, i) not in unstable
    ]
    differences += [(key, -1, "length", "length") for key in before if len(before[key]) != len(after.get(key, []))]
    if differences:
        for sheet, text in original.items():
            sheet.write_text(text, encoding="utf-8")
        for key, i, a, b in differences[:8]:
            print(f"purge_css: DIFFERENT {key} element {i}: {a} -> {b}")
        for font in root.glob("site_libs/bootstrap/bootstrap-icons-subset.woff2"):
            font.unlink()
        print(f"purge_css: {len(differences)} elements look different, the original stylesheets are back")
        return 1
    for font in spare_fonts:
        font.unlink()
    checked = sum(len(v) for v in before.values()) - len(unstable)
    print(
        f"purge_css: {checked} elements on {len(before)} page views look exactly the same "
        f"({len(unstable)} unstable ones skipped)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(purge(Path(sys.argv[1] if len(sys.argv) > 1 else "_site")))
