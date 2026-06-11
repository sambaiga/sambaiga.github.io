#!/bin/bash
# Validate Quarto YAML frontmatter in .qmd files
# Checks for required fields: title, date, description, draft

ERRORS=0

for file in "$@"; do
  if [[ ! "$file" =~ \.qmd$ ]]; then
    continue
  fi

  # Check if file starts with --- (frontmatter marker)
  if ! head -1 "$file" | grep -q "^---"; then
    echo "❌ $file: Missing YAML frontmatter (no opening ---)"
    ((ERRORS++))
    continue
  fi

  # Extract frontmatter section (lines between first and second ---)
  line_count=$(wc -l < "$file")
  frontmatter=$(awk '/^---$/{if(++count==2)exit; next} NR>1 && count==1' "$file")

  # Check for required fields in blog posts
  if [[ "$file" =~ /posts/ ]]; then
    for field in "title" "date" "description"; do
      if ! echo "$frontmatter" | grep -q "^$field:"; then
        echo "❌ $file: Missing required field '$field'"
        ((ERRORS++))
      fi
    done

    # Check for draft field
    if ! echo "$frontmatter" | grep -q "^draft:"; then
      echo "❌ $file: Missing 'draft' field"
      ((ERRORS++))
    fi
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "Quarto validation failed with $ERRORS error(s)"
  exit 1
fi

exit 0
