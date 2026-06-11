# Website Enhancement Implementation Plan

**Status:** Ready to Start  
**Date Created:** 2026-06-11  
**Project:** sambaiga.github.io Website Improvements  
**Lead:** Claude Code  

---

## Table of Contents
1. [Overview](#overview)
2. [Phase Breakdown](#phase-breakdown)
3. [Merge Order](#merge-order)
4. [Decision Points](#decision-points)
5. [Testing & Review Checklist](#testing--review-checklist)
6. [Timeline](#timeline)

---

## Overview

### Approach
- **Strategy:** Parallel preparation with sequential merging (3-5 feature branches running in parallel)
- **Review Cadence:** After each branch is ready, you test locally, review, then merge to main
- **Estimated Total Time:** 3-4 hours work (30-45 min per phase after parallelization)
- **Branches Strategy:** Independent feature branches to avoid conflicts

### Key Requirements
✅ Create feature branch from main  
✅ Replace CV with new one (from June 2026 PDF)  
✅ Update current role to reflect "Principal AI Engineer" at Analog Devices  
✅ Add pre-commit hooks for quality gates (YAML, bib, links, images)  
✅ Create open-source projects page with all 5 projects  
✅ Set up GitHub Actions for PR validation  
✅ Design consistency with existing branding (twiga.scss)  
✅ Test locally before merging each phase  

---

## Phase Breakdown

### Phase 1: Foundation & CV Update ⏱️ ~45 min
**Branch:** `feature/cv-and-site-updates`  
**Status:** Foundation - no conflicts with other branches

**Tasks:**
1. Replace CV file (`files/CV_Anthony_2025.pdf` with new June 2026 version)
2. Update homepage (`index.qmd`):
   - Update hero section: "Leading Applied AI for Strategic Impact"
   - Update stats (years of experience, projects, impact)
   - Verify company/role alignment with CV
3. Update about page (`pages/about/index.qmd`):
   - Refresh bio to reflect current Principal AI Engineer role at Analog Devices
   - Update current employer and location details
   - Highlight strategic AI leadership and MLOps expertise
4. Update current role info across site
5. Add reading-time estimates to all blog posts (2024, 2025, 2026)
6. Mark Part 3 draft (`pages/blog/posts/2026/05/index.qmd`) as `draft: true` and commit safely

**Review Checklist:**
- [ ] CV loads correctly from `/files/`
- [ ] Homepage accurately reflects your current role (Principal AI Engineer)
- [ ] About page bio is current and compelling
- [ ] Reading time estimates appear on blog listing
- [ ] Site builds without errors: `quarto preview`
- [ ] Homepage visually accurate on mobile and desktop

**Merge Decision:** Approve before moving to Phase 2

---

### Phase 2: Pre-commit Hooks & Quality Gates ⏱️ ~40 min
**Branch:** `feature/pre-commit-hooks`  
**Dependencies:** None (can run in parallel, but best merged before Phase 4)

**Tasks:**
1. Add Quarto-specific pre-commit validation:
   - Validate YAML frontmatter in all `.qmd` files
   - Check for required fields: `title`, `date`, `description`, `draft`
2. Add bibliography validation for `.bib` files:
   - Ensure all citation keys are defined
   - Check for duplicate keys
3. Create shell script for internal link validation:
   - Verify relative links like `../03/` point to existing files
   - Check cross-post references are valid
4. Create image asset validation script:
   - Verify `cover.png` exists for each blog post with `image:` in frontmatter
   - Verify `banner.jpg` exists when `title-block-banner:` is set
   - Report missing images before commit
5. Update `.pre-commit-config.yaml` with all new hooks
6. Test with `pre-commit run --all-files` on existing posts

**Pre-commit Config Structure:**
```yaml
# Quarto YAML validation
- repo: custom
  hooks:
    - id: quarto-yaml-validate
      
# Bibliography validation
- repo: custom
  hooks:
    - id: bib-validate

# Link validation
- repo: custom
  hooks:
    - id: internal-link-check

# Image validation
- repo: custom
  hooks:
    - id: image-asset-check
```

**Review Checklist:**
- [ ] `pre-commit run --all-files` passes with no false positives
- [ ] Existing posts pass all validations
- [ ] Draft post detection works correctly
- [ ] No legitimate links flagged as broken
- [ ] Image validation catches missing assets
- [ ] Pre-commit runs quickly (<5 sec) on typical commit

**Merge Decision:** Approve before Phase 4 (GitHub Actions)

---

### Phase 3A: Projects Page - Card Grid Design ⏱️ ~1 hour
**Branch:** `feature/projects-page-cards`  
**Status:** Design Option A (choose between 3A or 3B)

**Tasks:**
1. Create `pages/projects/index.qmd` (card grid layout):
   - Page title: "Open Source Projects & Libraries"
   - Introduction: Brief statement about your OSS contributions
   - Responsive card grid (4 columns desktop, 2 tablet, 1 mobile)

2. Create `pages/projects/data.yml` with project metadata:
   ```yaml
   projects:
     - name: Twiga
       description: "Production forecasting library built on transformer and seq2seq architectures"
       status: Active
       year: 2024
       links:
         - label: "PyPI"
           url: "https://pypi.org/project/twiga/"
         - label: "Docs"
           url: "https://sambaiga.github.io/twiga-docs/"
         - label: "GitHub"
           url: "https://github.com/sambaiga/twiga"
       stars: 250
       icon: "package"
       
     - name: MLPForecast
       description: "MLP-based net-load forecasting with uncertainty estimates"
       status: Active
       year: 2023
       links:
         - label: "GitHub"
           url: "https://github.com/sambaiga/mlpforecast"
       icon: "chart-line"
       
     - name: MLCFCD
       description: "Machine Learning-based Conformal Forecasting for Demand"
       status: Maintained
       year: 2023
       links:
         - label: "GitHub"
           url: "https://github.com/sambaiga/MLCFCD"
       icon: "brain"
       
     - name: AWRGNILM
       description: "Adaptive Weighted Recurrence Graphs for Non-Intrusive Load Monitoring"
       status: Maintained
       year: 2021
       links:
         - label: "GitHub"
           url: "https://github.com/sambaiga/AWRGNILM"
       icon: "bolt"
       
     - name: Deep-NILMtk
       description: "Deep Learning Toolkit for Non-Intrusive Load Monitoring"
       status: Community
       year: 2020
       links:
         - label: "GitHub"
           url: "https://github.com/BHafsa/Deep-NILMtk"
       icon: "zap"
   ```

3. Design card component with:
   - Icon/status badge (color-coded: green=Active, blue=Maintained, gray=Community)
   - Project name and description
   - Year started (bottom left)
   - Links (PyPI, Docs, GitHub) with icons
   - Optional: Star count from GitHub API (if available)
   - Hover effects (lift effect, link highlight)

4. Style using twiga.scss color scheme:
   - Active: `#4CAF50` (green)
   - Maintained: `#2196F3` (blue)
   - Community: `#9E9E9E` (gray)

5. Add to navbar in `_quarto.yml`:
   ```yaml
   - text: "Projects"
     file: "pages/projects/index.qmd"
   ```

6. Add breadcrumb navigation (optional)

**Review Checklist:**
- [ ] Cards display correctly in 4-column grid on desktop
- [ ] Cards stack properly on tablet (2 columns) and mobile (1 column)
- [ ] All 5 projects listed with complete information
- [ ] Status badges color-coded correctly
- [ ] Links work (test each project's GitHub/PyPI/Docs)
- [ ] Styling matches twiga.scss color scheme
- [ ] Hover effects smooth and visible
- [ ] Page loads quickly
- [ ] Site builds without errors: `quarto preview`

**Visual Reference:**
```
┌──────────────────────────────────────────┐
│  📦 Twiga                    Active ✓     │
│  Production forecasting library           │
│  Built on transformers & seq2seq          │
│  ⭐ 250 · 2024                           │
│  [PyPI] [Docs] [GitHub]                  │
└──────────────────────────────────────────┘
[Card repeats 4 across on desktop]
```

**Merge Decision:** Choose this OR Phase 3B, not both

---

### Phase 3B: Projects Page - Timeline Design ⏱️ ~1 hour
**Branch:** `feature/projects-page-timeline`  
**Status:** Design Option B (choose between 3A or 3B)

**Tasks:**
1. Create `pages/projects/index.qmd` (timeline layout):
   - Page title: "Open Source Projects & Libraries"
   - Grouped by status (Active → Maintained → Community)
   - Vertical timeline with visual flow

2. Reuse `pages/projects/data.yml` from Phase 3A (same data, different layout)

3. Design timeline component:
   - Left/right alternating entries on desktop (single column on mobile)
   - Status group headers (Active, Maintained, Community)
   - Visual timeline connector (vertical line with dots)
   - Each project entry shows:
     - Project name
     - Year started
     - Description
     - Status badge
     - Links
     - Icon

4. Add filtering/toggling by status (optional: collapse maintained/community sections)

5. Style matching twiga.scss (same status colors)

6. Add to navbar in `_quarto.yml`

**Review Checklist:**
- [ ] Timeline displays correctly on desktop and mobile
- [ ] Status groups clearly separated and labeled
- [ ] All 5 projects visible with complete information
- [ ] Timeline connectors visually clear
- [ ] Filtering/toggling works (if implemented)
- [ ] Links functional
- [ ] Color scheme matches site
- [ ] Site builds: `quarto preview`

**Visual Reference:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ACTIVE (3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ●─── 2024: 🔷 Twiga
     │    Production forecasting library
     │    [PyPI] [Docs] [GitHub]
     │
     ●─── 2023: 🟦 MLPForecast
     │    MLP-based forecasting
     │    [GitHub]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MAINTAINED (2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ●─── 2023: MLCFCD
     │    ...
```

**Merge Decision:** Choose this OR Phase 3A, not both. After both are ready, you decide which design wins.

---

### Phase 4: GitHub Actions CI/CD ⏱️ ~30 min
**Branch:** `feature/github-actions`  
**Dependencies:** Phase 2 (pre-commit hooks should be merged first for consistency)

**Tasks:**
1. Create `.github/workflows/pr-validation.yml`:
   ```yaml
   name: PR Validation
   on:
     pull_request:
     push:
       branches: [main]
   
   jobs:
     quarto-validate:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Quarto YAML Validation
           run: |
             # Validate all .qmd files for proper YAML frontmatter
             # Check required fields: title, date, description, draft
         
     bibliography-validate:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Bibliography Validation
           run: |
             # Check all .bib files for valid keys
             # Ensure no duplicate citations
         
     link-check:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Internal Link Validation
           run: |
             # Check all relative links exist
             # Verify ../XX/ cross-references
         
     image-validate:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Image Asset Validation
           run: |
             # Verify cover.png for posts with image: field
             # Verify banner.jpg for posts with title-block-banner:
   ```

2. Configure validation rules:
   - **Quarto YAML:** Check all `.qmd` files in `pages/blog/posts/**`
   - **Bibliography:** Validate all `.bib` files
   - **Links:** Check internal references in `.qmd` files
   - **Images:** Verify assets exist before commit

3. Set up GitHub branch protection:
   - Require all checks to pass before merging to main
   - Require at least 1 review (optional, for future enforcement)

4. Create documentation in PR template (`.github/pull_request_template.md`):
   - Explain validation checks
   - Guide for fixing common issues
   - Checklist for blog post PRs

5. Test workflow with a test PR (to be done after merge)

**GitHub Actions Workflow Details:**

```yaml
# .github/workflows/pr-validation.yml
name: Validate Blog Posts and Content

on:
  pull_request:
    paths:
      - 'pages/blog/**'
      - '.github/workflows/**'
      - '.qmd'
      - '.bib'
  push:
    branches: [main]
    paths:
      - 'pages/blog/**'

jobs:
  quarto-validate:
    name: Quarto YAML Validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: |
          python -m pip install pyyaml
      - name: Validate Quarto files
        run: |
          python scripts/validate_quarto.py

  bib-validate:
    name: Bibliography Validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate BibTeX files
        run: |
          python scripts/validate_bib.py

  link-validate:
    name: Internal Link Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check internal links
        run: |
          python scripts/validate_links.py

  image-validate:
    name: Image Asset Validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check image assets
        run: |
          python scripts/validate_images.py
```

**Review Checklist:**
- [ ] Workflow file has valid YAML syntax
- [ ] All four checks configured (YAML, bib, links, images)
- [ ] Tests run on both PR and main branch push
- [ ] Validation scripts created in `scripts/` directory
- [ ] Branch protection rule created
- [ ] Test PR created to verify workflow executes
- [ ] All checks pass on a valid post
- [ ] Checks fail appropriately on invalid input

**Merge Decision:** Approve and merge

---

### Phase 5: Design Refinement & Polish ⏱️ ~20 min
**Branch:** `feature/design-polish`  
**Dependencies:** Phase 3 (projects page should be merged)

**Tasks:**
1. Add breadcrumb navigation:
   - Homepage > Projects > [Project Name]
   - Helps with site navigation and SEO

2. Ensure consistent spacing:
   - Match padding/margins across all pages
   - Verify card/timeline spacing consistent with other sections

3. Add meta descriptions:
   - Projects page: "Open-source libraries for AI forecasting, load monitoring, and intelligent power systems"
   - Review pages for completeness

4. Test social card previews:
   - Verify Open Graph tags render correctly
   - Twitter card display correct

5. Mobile responsiveness check:
   - Test all new pages on iPhone/iPad screen sizes
   - Verify touch targets are adequate

6. Performance check:
   - Run Quarto build and check output size
   - Verify site loads quickly with new assets

7. Accessibility check:
   - Verify color contrast on status badges
   - Check link underlines/focus states
   - Test with screen reader (ARIA labels)

**Review Checklist:**
- [ ] Breadcrumbs display correctly
- [ ] Spacing consistent across pages
- [ ] Meta descriptions accurate and present
- [ ] Social cards preview correctly
- [ ] Mobile layout responsive and usable
- [ ] Site builds quickly
- [ ] Accessibility features working
- [ ] No visual regressions in existing pages

**Merge Decision:** Final approval, ready to push to live

---

## Merge Order

This is the recommended sequence. **Each phase must be reviewed and approved before merging:**

```
1. feature/cv-and-site-updates
   └─ Status: Foundation - no conflicts
   └─ Review: CV, homepage, about page
   └─ Merge: ✓ Required before next phases

2. feature/pre-commit-hooks
   └─ Status: Independent but should merge before Phase 4
   └─ Review: Run pre-commit, verify validations
   └─ Merge: ✓ Required before Phase 4

3. feature/projects-page-{cards OR timeline}
   └─ Status: YOU CHOOSE ONE
   └─ Options: 
      - Card Grid (Phase 3A): Visual, scrollable, modern
      - Timeline (Phase 3B): Narrative, status-grouped, evolutionary
   └─ Review: Layout, links, responsive design
   └─ Merge: ✓ Pick winner, delete loser

4. feature/github-actions
   └─ Status: Quality gates
   └─ Review: Workflow syntax, validation logic
   └─ Merge: ✓ Final quality protection

5. feature/design-polish
   └─ Status: Final touches
   └─ Review: Full site polish
   └─ Merge: ✓ Ready for live
```

---

## Decision Points

### Decision 1: Projects Page Design (Phase 3)
**When:** After both 3A and 3B branches are ready  
**Options:**
- **Card Grid (3A):** 4 columns, modern, visual-first, scrollable
- **Timeline (3B):** Vertical narrative, status-grouped, evolutionary story

**How to Decide:**
1. Preview both locally: `quarto preview`
2. Check on mobile: responsive test
3. Which feels more "you"? Which better tells your OSS story?
4. Tell me which wins, I merge that and delete the other

**Recommendation:** Timeline better shows the **evolution** of your work (2020→2024) and **maturity levels** (Active/Maintained/Community). Card grid is more conventional but less narrative. Your choice!

---

## Testing & Review Checklist

### Before Each Phase Merge

- [ ] Code builds without errors: `quarto preview`
- [ ] No TypeScript/ESLint errors (if applicable)
- [ ] No broken internal links
- [ ] Responsive design tested on mobile/tablet/desktop
- [ ] All links (GitHub, PyPI, Docs) verified working
- [ ] No spelling/grammar errors
- [ ] Metadata complete (title, date, description, image)
- [ ] Color contrast meets accessibility standards (WCAG AA)
- [ ] Page loads reasonably fast

### Local Testing Commands
```bash
# Build and preview
quarto preview

# Check for errors
quarto check

# Validate markdown/yaml
pre-commit run --all-files

# Check links (when implemented)
python scripts/validate_links.py

# Build static output
quarto render
```

### Review Deliverables
Each phase PR should include:
- Summary of changes
- Link to preview (or "run `quarto preview` locally")
- Checklist of tested items
- Screenshot (for visual changes)
- Any breaking changes or deprecations

---

## Timeline

### Estimated Schedule
- **Phase 1:** 45 min (CV update, homepage, about page)
- **Phase 2:** 40 min (pre-commit hooks)
- **Phases 3A + 3B:** 1 hour each (parallel: both ready in ~1.5 hours wall time, but your choice picks one)
- **Phase 4:** 30 min (GitHub Actions)
- **Phase 5:** 20 min (design polish)

**Total active development:** ~3-4 hours  
**Your review time:** ~15-30 min per phase × 5 phases = ~2-2.5 hours total

### Realistic Project Timeline
- **Now → Next 2 hours:** Phases 1-2 complete and merged
- **Next 2-3 hours:** Phase 3 (design decision point)
- **Next 1 hour:** Phase 4-5 (final polish & protection)
- **Total project duration:** 3-4 hours, 1 day to completion

---

## Success Criteria

✅ **Phase 1:** CV updated, homepage/about reflect current role  
✅ **Phase 2:** Pre-commit hooks prevent invalid posts  
✅ **Phase 3:** Projects page showcases all 5 OSS projects beautifully  
✅ **Phase 4:** GitHub Actions validates every PR automatically  
✅ **Phase 5:** Site is polished, responsive, accessible  

**Final Outcome:**
- Website reflects your current role as Principal AI Engineer
- Open-source contributions are prominently featured
- Quality gates prevent deployment of invalid content
- Site is performant, accessible, and maintainable
- You can confidently push new blog posts knowing they're validated

---

## Notes & Assumptions

- All work is on **feature branches**, not main
- Each phase is **independent** — you approve before merge
- Pre-commit hooks assume **Python 3.8+** is available
- GitHub Actions requires **.github/** directory exists (create if needed)
- Projects page data can be **extended later** (add more projects easily)
- Timeline filter is **optional** (can be added if needed)

---

## Questions Before We Start?

1. **Projects page preference:** Card grid vs. Timeline? (Can decide after seeing both)
2. **Navigation:** Should Projects link from navbar or just footer?
3. **Blog reading time:** Should it show minutes or be hidden?
4. **Status badges:** Color-coded OK or prefer text labels?
5. **Accessibility:** Any specific requirements beyond WCAG AA?

---

**Ready to start?** 🚀

Next step: Create `feature/cv-and-site-updates` branch and update CV + homepage.
