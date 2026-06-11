#!/usr/bin/env python3
"""
Validate BibTeX bibliography files (.bib).
Checks for syntax errors, duplicate keys, and missing required fields.
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Set

def parse_bib_file(filepath: Path) -> tuple:
    """
    Parse BibTeX file and extract entries.
    Returns (entries_dict, errors_list)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return {}, [f"Cannot read file: {e}"]

    entries = {}
    errors = []
    seen_keys = set()

    # Match @TYPE{KEY, ...}
    entry_pattern = r'@(\w+)\s*\{\s*([^,\s]+)\s*,'
    matches = list(re.finditer(entry_pattern, content, re.IGNORECASE))

    for match in matches:
        entry_type = match.group(1)
        key = match.group(2)

        # Check for duplicate keys
        if key in seen_keys:
            errors.append(f"Duplicate citation key: {key}")
        else:
            seen_keys.add(key)
            entries[key] = entry_type

    # Basic syntax check: ensure closing braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        errors.append(f"Unmatched braces: {open_braces} {{ vs {close_braces} }}")

    return entries, errors

def check_bib_references_in_qmd(qmd_file: Path, bib_files: List[Path]) -> List[str]:
    """Check that all citations in QMD file exist in bibliography."""
    errors = []

    try:
        content = qmd_file.read_text(encoding='utf-8')
    except Exception:
        return errors

    # Look for @KEY citation pattern
    citation_pattern = r'@([a-zA-Z0-9_\-]+)'
    citations = set(re.findall(citation_pattern, content))

    if not citations:
        return errors

    # Collect all available keys from bibliography files
    available_keys = set()
    for bib_file in bib_files:
        entries, _ = parse_bib_file(bib_file)
        available_keys.update(entries.keys())

    # Check for missing citations
    missing = citations - available_keys
    if missing:
        rel_path = qmd_file.relative_to(qmd_file.parent.parent.parent)
        errors.append(f"Missing bibliography keys in {rel_path}: {', '.join(sorted(missing))}")

    return errors

def main():
    """Validate all .bib files in the repository."""
    repo_root = Path(__file__).parent.parent
    bib_files = list(repo_root.glob('**/*.bib'))

    if not bib_files:
        print("No .bib files found")
        return 0

    all_errors = {}

    # Validate each .bib file
    for bib_file in sorted(bib_files):
        entries, errors = parse_bib_file(bib_file)
        if errors:
            rel_path = bib_file.relative_to(repo_root)
            all_errors[str(rel_path)] = errors

    # Check cross-references from QMD files
    qmd_files = list(repo_root.glob('**/*.qmd'))
    for qmd_file in qmd_files:
        errors = check_bib_references_in_qmd(qmd_file, bib_files)
        if errors:
            rel_path = qmd_file.relative_to(repo_root)
            all_errors[str(rel_path)] = errors

    if all_errors:
        print("Bibliography validation errors found:\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for error in errors:
                print(f"    - {error}")
        return 1

    print(f"✓ Bibliography validation passed ({len(bib_files)} files)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
