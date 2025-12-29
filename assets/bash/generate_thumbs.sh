#!/bin/bash

# Configuration
PDF_DIR="files/papers"
IMG_DIR="images/publications"

mkdir -p "$IMG_DIR"

for pdf in "$PDF_DIR"/*.pdf; do
    filename=$(basename "$pdf" .pdf)
    output_svg="$IMG_DIR/${filename}.svg"

    echo "Converting: $filename to Square SVG"

    # 1. Convert 1st page of PDF to SVG
    # -svg: output format
    # -f 1 -l 1: only first page
    pdftocairo "$pdf" -svg -f 1 -l 1 "$output_svg"

    # 2. Force Square Aspect Ratio (1:1)
    # This uses Python to adjust the viewBox so the top part of the page 
    # (usually the title/authors) is perfectly centered in a square.
    python3 - <<EOF
import re
path = "$output_svg"
with open(path, 'r') as f:
    content = f.read()

# Find original width/height
dims = re.search(r'width="([\d\.]+)pt" height="([\d\.]+)pt"', content)
if dims:
    w, h = float(dims.group(1)), float(dims.group(2))
    side = min(w, h)
    # Create a centered square viewBox (x, y, width, height)
    # Shifts y-offset slightly to capture the title better
    new_viewbox = f'viewBox="0 0 {side} {side}"'
    
    # Update the SVG tag with the new viewBox and fixed square dimensions
    content = re.sub(r'width="[\d\.]+pt"', f'width="600"', content)
    content = re.sub(r'height="[\d\.]+pt"', f'height="600"', content)
    if 'viewBox' in content:
        content = re.sub(r'viewBox="[^"]+"', new_viewbox, content)
    else:
        content = content.replace('<svg ', f'<svg {new_viewbox} ')

with open(path, 'w') as f:
    f.write(content)
EOF

    echo "  + Created: $output_svg"
done
