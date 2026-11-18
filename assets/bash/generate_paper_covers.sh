#!/bin/bash
# For every paper PDF: a cover (the top of the first page, 4:3) for the Research list, and the whole first page for the
# preview that opens on a click. An image that exists is kept, so a render does not change tracked files. Delete an image,
# or run with FORCE=1, to make it again.

PDF_DIR="files/papers"
COVER_DIR="images/publications/cover"
PREVIEW_DIR="images/publications/preview"

mkdir -p "$COVER_DIR" "$PREVIEW_DIR"

for pdf in "$PDF_DIR"/*.pdf; do
    name=$(basename "$pdf" .pdf)
    # PDFs that no paper of the list uses: the example, a second copy of the ICASSP 2023 paper, and a copy of the multi-label paper
    case "$name" in example_pdf | FTNILM | nilmsurvey2017) continue ;; esac
    if [ ! -f "$COVER_DIR/$name.jpg" ] || [ -n "$FORCE" ]; then
        pdftoppm -f 1 -l 1 -jpeg -jpegopt quality=76 -scale-to-x 640 -scale-to-y -1 -x 0 -y 0 -W 640 -H 480 -singlefile "$pdf" "$COVER_DIR/$name"
    fi
    if [ ! -f "$PREVIEW_DIR/$name.jpg" ] || [ -n "$FORCE" ]; then
        pdftoppm -f 1 -l 1 -jpeg -jpegopt quality=72 -scale-to-x 760 -scale-to-y -1 -singlefile "$pdf" "$PREVIEW_DIR/$name"
    fi
done
