"""Write one page for every talk that has slides.

The talks are listed in ``pages/talks/talks.yaml``. A talk with a ``slug`` and ``slides`` gets the page
``pages/talks/<slug>/index.qmd``, which holds the slide viewer, the details of the talk, a citation and links to the
neighbouring talks. The pages are generated: a change to a talk is made in the data file, and the pages are made again.

Usage:
    uv run --with pyyaml python scripts/make_talk_pages.py
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "pages" / "talks" / "talks.yaml"
OUT = ROOT / "pages" / "talks"
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
TYPES = {
    "conference": ("people", "Conference"),
    "invited": ("mic", "Invited"),
    "teaching": ("mortarboard", "Teaching"),
    "poster": ("file-earmark-richtext", "Poster"),
}
AUTHOR = "Anthony Faustine"


def when(talk: dict) -> str:
    """Return the date of a talk, with the month only when it is known.

    Args:
        talk: One entry of the data file.

    Returns:
        For example ``September 2024`` or ``2021``.
    """
    month = talk.get("month")
    return f"{MONTHS[month - 1]} {talk['year']}" if month else str(talk["year"])


def authors(talk: dict) -> str:
    """Return the author list of a talk for the citation.

    Args:
        talk: One entry of the data file.

    Returns:
        The author and the co-authors, for example ``Anthony Faustine and Lucas Pereira``.
    """
    others = str(talk.get("coauthors", "")).removeprefix("with ").strip()
    return f"{AUTHOR}, {others}" if others else AUTHOR


def citation(talk: dict) -> str:
    """Return a plain-text citation of the slides.

    Args:
        talk: One entry of the data file.

    Returns:
        The citation as one line.
    """
    place = f", {talk['place']}" if talk.get("place") else ""
    return f"{authors(talk)} ({talk['year']}). {talk['title']}. {talk['venue']}{place}. Slides."


def meta_line(icon: str, text: str) -> str:
    """Return one detail of the header of a page.

    Args:
        icon: The name of a Bootstrap icon.
        text: The text of the detail.

    Returns:
        The markup of the detail.
    """
    return f'<span><i class="bi bi-{icon}"></i>{escape(text)}</span>'


def header(talk: dict) -> str:
    """Return the markup above the viewer.

    Args:
        talk: One entry of the data file.

    Returns:
        The breadcrumb, the label, the title and the details.
    """
    icon, label = TYPES.get(talk.get("type"), ("easel2", ""))
    details = [meta_line("building", talk["venue"])]
    if talk.get("place"):
        details.append(meta_line("geo-alt", talk["place"]))
    details.append(meta_line("calendar3", when(talk)))
    if talk.get("coauthors"):
        details.append(meta_line("people", talk["coauthors"]))
    crumb = (
        '<nav class="tp-crumb" aria-label="Breadcrumb">'
        '<a href="../index.html"><i class="bi bi-arrow-left"></i>Talks</a>'
        f'<i class="bi bi-chevron-right" aria-hidden="true"></i><span>{talk["year"]}</span></nav>'
    )
    name = f"<b>{label}</b>" if label else ""
    kind = f'<p class="tk-kind"><i class="bi bi-{icon}"></i>{name}<span>{escape(talk["topic"])}</span></p>'
    title = f'<h1 class="tp-title no-anchor">{escape(talk["title"])}</h1>'
    return "\n".join([crumb, kind, title, f'<p class="tk-meta">{"".join(details)}</p>'])


def viewer(talk: dict) -> str:
    """Return the markup of the slide viewer.

    Args:
        talk: One entry of the data file.

    Returns:
        The viewer, which a script fills with the slides of the PDF file.
    """
    pdf = f"../../../files/slides/{Path(talk['slides']).name}"
    return f"""<section class="tp-viewer" data-viewer data-pdf="{pdf}" data-lib="../../../assets/vendor/pdfjs/"
  aria-label="Slides">
  <div class="tp-stage" data-stage>
    <button class="tp-nav tp-nav--prev" type="button" data-prev aria-label="Previous slide">
      <i class="bi bi-chevron-left"></i></button>
    <canvas data-canvas role="img" aria-label="Slide"></canvas>
    <button class="tp-nav tp-nav--next" type="button" data-next aria-label="Next slide">
      <i class="bi bi-chevron-right"></i></button>
    <p class="tp-fallback" data-fallback>The slides need JavaScript. <a href="{pdf}">Open the PDF file</a>.</p>
  </div>
  <div class="tp-progress"><i data-progress></i></div>
  <div class="tp-bar">
    <span data-position aria-live="polite"></span>
    <span class="tp-keys"><kbd>&larr;</kbd> <kbd>&rarr;</kbd> to move</span>
    <button class="tp-tool" type="button" data-full><i class="bi bi-arrows-fullscreen"></i>Full screen</button>
    <a class="tp-tool tp-tool--main" href="{pdf}" download>
      <i class="bi bi-download"></i>Download PDF</a>
  </div>
  <div class="tp-strip" data-strip role="group" aria-label="Slide thumbnails"></div>
</section>"""


def details(talk: dict) -> str:
    """Return the boxes below the viewer.

    Args:
        talk: One entry of the data file.

    Returns:
        A box with the links of the talk and a box with the citation.
    """
    pdf = f"../../../files/slides/{Path(talk['slides']).name}"
    new = ' target="_blank" rel="noopener"'
    links = [f'<a href="{pdf}" download><i class="bi bi-file-earmark-pdf"></i>Slides as a PDF file</a>']
    if talk.get("video"):
        links.append(f'<a href="{talk["video"]}"{new}><i class="bi bi-play-circle"></i>Video of the talk</a>')
    if talk.get("link"):
        links.append(f'<a href="{talk["link"]}"{new}><i class="bi bi-box-arrow-up-right"></i>Event or paper page</a>')
    pages = f"<p>{escape(talk['pages'])}</p>" if talk.get("pages") else ""
    items = "".join(f"<li>{link}</li>" for link in links)
    cite = escape(citation(talk))
    return f"""<div class="tp-boxes">
  <section class="tp-box">
    <h2 class="no-anchor"><i class="bi bi-link-45deg"></i>Links</h2>{pages}<ul>{items}</ul>
  </section>
  <section class="tp-box">
    <h2 class="no-anchor"><i class="bi bi-quote"></i>Cite these slides</h2>
    <p class="tp-cite" data-cite>{cite}</p>
    <button class="tp-tool" type="button" data-copy><i class="bi bi-clipboard"></i><span>Copy citation</span></button>
  </section>
</div>"""


def neighbours(talks: list[dict], index: int) -> str:
    """Return the links to the earlier and the later talk with a page.

    Args:
        talks: The talks that have a page, newest first.
        index: The position of the current talk in the list.

    Returns:
        The navigation at the end of a page.
    """
    later = talks[index - 1] if index > 0 else None
    earlier = talks[index + 1] if index + 1 < len(talks) else None

    def link(talk: dict | None, label: str, icon: str, side: str) -> str:
        if talk is None:
            return '<span class="tp-step tp-step--none"></span>'
        arrow = f'<i class="bi bi-{icon}"></i>'
        text = f"<span><small>{label}</small>{escape(talk['title'])}</span>"
        inner = arrow + text if side == "prev" else text + arrow
        return f'<a class="tp-step tp-step--{side}" href="../{talk["slug"]}/index.html">{inner}</a>'

    before = link(earlier, "Earlier", "arrow-left", "prev")
    after = link(later, "Later", "arrow-right", "next")
    return f'<nav class="tp-steps" aria-label="Other talks">{before}{after}</nav>'


def page(talks: list[dict], index: int) -> str:
    """Return the source of the page of one talk.

    Args:
        talks: The talks that have a page, newest first.
        index: The position of the current talk in the list.

    Returns:
        The text of the ``index.qmd`` file.
    """
    talk = talks[index]
    title = talk["title"].replace('"', '\\"')
    description = f"Slides of the talk {title} at {talk['venue']}, {when(talk)}."
    body = "\n\n".join([header(talk), viewer(talk), details(talk), neighbours(talks, index)])
    return f"""---
title: ""
pagetitle: "{title} | Talks | Anthony Faustine"
description-meta: "{description.replace('"', "'")}"

format:
  html:
    page-layout: full
    body-classes: "talks-page talk-page"
    include-after-body:
      - text: |
          <script src="../../../assets/js/talk-viewer.js" defer></script>

toc: false
---

```{{=html}}
<div class="tp">

{body}

</div>
```
"""


def main() -> None:
    """Write the page of every talk that has slides, and remove the page of a talk that lost them."""
    talks = [t for t in yaml.safe_load(DATA.read_text()) if t.get("slug") and t.get("slides")]
    talks.sort(key=lambda t: t["year"] * 100 + (t.get("month") or 0), reverse=True)
    keep = set()
    for index, talk in enumerate(talks):
        folder = OUT / talk["slug"]
        folder.mkdir(exist_ok=True)
        (folder / "index.qmd").write_text(page(talks, index))
        keep.add(folder)
    for folder in OUT.iterdir():
        if folder.is_dir() and folder not in keep and (folder / "index.qmd").exists():
            (folder / "index.qmd").unlink()
            folder.rmdir()
    print(f"{len(talks)} talk pages written")


if __name__ == "__main__":
    main()
