#!/usr/bin/env python3
"""
Validate Quarto YAML frontmatter in .qmd files.
Checks for required fields and valid YAML syntax.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple
import yaml

REQUIRED_FIELDS = {'title', 'date', 'description'}
OPTIONAL_FIELDS = {'subtitle', 'author', 'categories', 'draft', 'bibliography', 'image'}

def extract_frontmatter(content: str) -> Tuple[dict, int]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, 0

    lines = content.split('\n')
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}, 0

    frontmatter_text = '\n'.join(lines[1:end_idx])
    try:
        data = yaml.safe_load(frontmatter_text)
        return data or {}, end_idx
    except yaml.YAMLError as e:
        return {'_yaml_error': str(e)}, end_idx

def validate_qmd_file(filepath: Path) -> List[str]:
    """Validate a single .qmd file. Returns list of errors."""
    errors = []

    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"Cannot read file: {e}"]

    frontmatter, _ = extract_frontmatter(content)

    if '_yaml_error' in frontmatter:
        errors.append(f"YAML syntax error: {frontmatter['_yaml_error']}")
        return errors

    # Check required fields for blog posts
    if 'blog' in str(filepath):
        missing = REQUIRED_FIELDS - set(frontmatter.keys())
        if missing:
            errors.append(f"Missing required fields: {', '.join(sorted(missing))}")

        # Check draft status
        if 'draft' not in frontmatter:
            errors.append("Missing 'draft' field (should be 'true' or 'false')")

    return errors

def main():
    """Validate all .qmd files in the repository."""
    repo_root = Path(__file__).parent.parent
    qmd_files = list(repo_root.glob('**/*.qmd'))

    if not qmd_files:
        print("No .qmd files found")
        return 0

    all_errors = {}
    for qmd_file in sorted(qmd_files):
        errors = validate_qmd_file(qmd_file)
        if errors:
            rel_path = qmd_file.relative_to(repo_root)
            all_errors[str(rel_path)] = errors

    if all_errors:
        print("Quarto validation errors found:\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for error in errors:
                print(f"    - {error}")
        return 1

    print(f"✓ Quarto validation passed ({len(qmd_files)} files)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
