# sambaiga.github.io

The personal site of Anthony Faustine, built with [Quarto](https://quarto.org) and published with GitHub Pages.

## Work on the site

```bash
quarto preview            # live preview of the whole site
make hooks                # install the git hooks once (pre-commit, commit-msg, pre-push)
make check                # every hook on every file, then a full render
make audit                # render, then audit the built site
make images               # resize images above their size limit
```

Changes reach `main` through a pull request. Look at the preview in the light and the dark theme, at desktop and phone
width, before a pull request is merged.

## What is checked

- **On every commit** (hooks): conventional commit messages with no AI co-author trailer, secrets, large files, build
  output, web-sized images, front matter, spelling, Python scripts (ruff) and the workflows (zizmor).
- **Before a push**: the whole site renders.
- **On every pull request**: the hooks on the changed files, a full render, `scripts/audit_site.py` (language, title,
  description, canonical link, share image, one h1, alt text, safe links, no outside imports) and a link check.
- **Weekly**: the workflows and the repository are scanned for security problems.

## Layout

| Folder | Content |
|---|---|
| `pages/` | Pages and posts (`blog`, `publication`, `projects`, `books`, `about`) |
| `assets/` | Styles (`scss`), templates (`ejs`), scripts (`js`) and self-hosted fonts |
| `images/figures/` | Concept diagrams of the book for use in posts, with a catalogue |
| `images/brand/` | The logo set, drawn by `scripts/branding/make_logo.py` |
| `scripts/` | Validators, the site audit, image tools and the logo generator |

The site is deployed by `.github/workflows/build-and-deploy.yml` when `main` changes. The actions are pinned to commit
SHAs and kept current by Dependabot.
