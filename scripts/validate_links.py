#!/usr/bin/env python3
"""
Validate internal links in .qmd files.
Checks that relative links point to existing files.
"""

import sys
import re
from pathlib import Path
from typing import List
from urllib.parse import urlparse

def extract_links(content: str, file_path: Path) -> List[tuple]:
    """
    Extract all links from markdown content.
    Returns list of (link, line_number) tuples.
    """
    links = []

    # Markdown link pattern: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(link_pattern, content):
        url = match.group(2)
        # Count line number
        line_num = content[:match.start()].count('\n') + 1
        links.append((url, line_num))

    # HTML href pattern: href="url"
    href_pattern = r'href=["\']([^"\']+)["\']'
    for match in re.finditer(href_pattern, content):
        url = match.group(1)
        line_num = content[:match.start()].count('\n') + 1
        links.append((url, line_num))

    return links

def is_relative_link(url: str) -> bool:
    """Check if URL is relative (not external)."""
    if url.startswith(('http://', 'https://', 'mailto:', '#')):
        return False
    return True

def validate_relative_link(link: str, file_path: Path, repo_root: Path) -> str:
    """
    Validate that a relative link points to an existing file.
    Returns error message or empty string if valid.
    """
    # Remove anchor
    link_without_anchor = link.split('#')[0]
    if not link_without_anchor:
        return ""

    # Resolve relative path
    target_path = (file_path.parent / link_without_anchor).resolve()

    # Check if target exists
    if not target_path.exists():
        rel_path = target_path.relative_to(repo_root) if repo_root in target_path.parents else target_path
        return f"Link points to non-existent file: {link} -> {rel_path}"

    return ""

def validate_qmd_file(filepath: Path, repo_root: Path) -> List[str]:
    """Validate all links in a .qmd file."""
    errors = []

    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"Cannot read file: {e}"]

    links = extract_links(content, filepath)

    for url, line_num in links:
        if is_relative_link(url):
            error = validate_relative_link(url, filepath, repo_root)
            if error:
                errors.append(f"Line {line_num}: {error}")

    return errors

def main():
    """Validate internal links in all .qmd files."""
    repo_root = Path(__file__).parent.parent
    qmd_files = list(repo_root.glob('**/*.qmd'))

    if not qmd_files:
        print("No .qmd files found")
        return 0

    all_errors = {}
    for qmd_file in sorted(qmd_files):
        errors = validate_qmd_file(qmd_file, repo_root)
        if errors:
            rel_path = qmd_file.relative_to(repo_root)
            all_errors[str(rel_path)] = errors

    if all_errors:
        print("Link validation errors found:\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for error in errors:
                print(f"    - {error}")
        return 1

    print(f"✓ Link validation passed ({len(qmd_files)} files)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
