#!/usr/bin/env python3
"""
Validate that image assets referenced in .qmd files exist.
Checks for cover.png, banner.jpg, and other image fields.
"""

import sys
import re
from pathlib import Path
from typing import List, Dict
import yaml

def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}

    lines = content.split('\n')
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}

    frontmatter_text = '\n'.join(lines[1:end_idx])
    try:
        data = yaml.safe_load(frontmatter_text)
        return data or {}
    except yaml.YAMLError:
        return {}

def validate_qmd_file(filepath: Path) -> List[str]:
    """Validate image assets for a single .qmd file."""
    errors = []
    post_dir = filepath.parent

    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"Cannot read file: {e}"]

    frontmatter = extract_frontmatter(content)

    # Check 'image' field (usually cover.png)
    if 'image' in frontmatter:
        image_name = frontmatter['image']
        image_path = post_dir / image_name
        if not image_path.exists():
            errors.append(f"Missing image: {image_name}")

    # Check 'title-block-banner' field (usually banner.jpg)
    if 'title-block-banner' in frontmatter:
        banner_name = frontmatter['title-block-banner']
        banner_path = post_dir / banner_name
        if not banner_path.exists():
            errors.append(f"Missing banner: {banner_name}")

    # Check for ![alt](image) references in body
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    for match in re.finditer(img_pattern, content):
        img_path = match.group(2)
        if not img_path.startswith(('http://', 'https://')):
            full_path = post_dir / img_path
            if not full_path.exists():
                line_num = content[:match.start()].count('\n') + 1
                errors.append(f"Line {line_num}: Missing image: {img_path}")

    return errors

def main():
    """Validate all image assets in blog posts."""
    repo_root = Path(__file__).parent.parent
    qmd_files = list(repo_root.glob('**/posts/**/*.qmd'))

    if not qmd_files:
        print("No blog post files found")
        return 0

    all_errors = {}
    for qmd_file in sorted(qmd_files):
        errors = validate_qmd_file(qmd_file)
        if errors:
            rel_path = qmd_file.relative_to(repo_root)
            all_errors[str(rel_path)] = errors

    if all_errors:
        print("Image validation errors found:\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for error in errors:
                print(f"    - {error}")
        return 1

    print(f"✓ Image validation passed ({len(qmd_files)} posts)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
