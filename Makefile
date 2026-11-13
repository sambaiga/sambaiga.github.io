.PHONY: hooks check render preview audit images purge

# Install the git hooks once: pre-commit and commit-msg run on every commit, pre-push renders the whole site.
hooks:
	uvx prek install --install-hooks -t pre-commit -t commit-msg -t pre-push

# Every hook on every file, including the full render of the pre-push stage.
check:
	uvx prek run --all-files
	uvx prek run --all-files --hook-stage pre-push

render:
	quarto render

preview:
	quarto preview

# Remove the unused CSS and icons of the built site (needs Chrome); fails, and undoes itself, if the site would look different.
purge:
	uv run --with playwright --with tinycss2 --with fonttools --with brotli python scripts/purge_css.py _site

# Render, purge, then audit the built site (metadata, accessibility, safe links).
audit: render purge
	python3 scripts/audit_site.py _site

# Resize and recompress images above their limit.
images:
	uv run --with pillow python scripts/optimize_images.py --over 400 images pages
