#!/bin/bash
# Validate that image assets referenced in .qmd files exist
# Checks for cover images and banner images in blog posts

ERRORS=0

for file in "$@"; do
  if [[ ! "$file" =~ \.qmd$ ]]; then
    continue
  fi

  # Only check files in posts directory
  if [[ ! "$file" =~ /posts/ ]]; then
    continue
  fi

  dir=$(dirname "$file")

  # Extract image field from frontmatter
  image=$(awk '/^---$/{if(++count==2)exit; next} NR>1 && count==1 && /^image:/{gsub(/^image:[[:space:]]*/, ""); gsub(/["\x27]/, ""); print; exit}' "$file")

  if [[ -n "$image" ]]; then
    if [[ ! -f "$dir/$image" ]]; then
      echo "❌ $file: Missing image file: $image"
      ((ERRORS++))
    fi
  fi

  # Extract title-block-banner field from frontmatter
  banner=$(awk '/^---$/{if(++count==2)exit; next} NR>1 && count==1 && /^title-block-banner:/{gsub(/^title-block-banner:[[:space:]]*/, ""); gsub(/["\x27]/, ""); print; exit}' "$file")

  if [[ -n "$banner" ]]; then
    if [[ ! -f "$dir/$banner" ]]; then
      echo "❌ $file: Missing banner file: $banner"
      ((ERRORS++))
    fi
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "Image validation failed with $ERRORS error(s)"
  exit 1
fi

exit 0
