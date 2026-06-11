#!/bin/bash
# Validate BibTeX bibliography files (.bib)
# Checks for syntax errors and duplicate keys

ERRORS=0

for file in "$@"; do
  if [[ ! "$file" =~ \.bib$ ]]; then
    continue
  fi

  # Check for unmatched braces
  open_braces=$(grep -o '{' "$file" | wc -l)
  close_braces=$(grep -o '}' "$file" | wc -l)

  if [[ $open_braces -ne $close_braces ]]; then
    echo "❌ $file: Unmatched braces ($open_braces { vs $close_braces })"
    ((ERRORS++))
  fi

  # Check for duplicate citation keys
  keys=$(grep -o '@[A-Za-z0-9]*{[^,]*' "$file" | sed 's/@[^{]*{\([^,]*\).*/\1/' | sort)
  duplicates=$(echo "$keys" | uniq -d)

  if [[ -n "$duplicates" ]]; then
    echo "❌ $file: Duplicate citation keys:"
    echo "$duplicates" | sed 's/^/   - /'
    ((ERRORS++))
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "Bibliography validation failed with $ERRORS error(s)"
  exit 1
fi

exit 0
