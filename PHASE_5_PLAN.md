# Phase 5: Design System Consolidation & Polish
**Objective**: Achieve 100% branding consistency, improve UI/UX, and establish reusable patterns

---

## 📋 Phase Overview

**Duration**: 2-3 sprints (estimated 10 hours)  
**Priority**: Medium-High (improves maintainability and user experience)  
**Dependencies**: Phases 1-4 complete ✅

### Success Definition
- ✅ All pages use centralized SCSS variables (no local redefinitions)
- ✅ Consistent hover/focus/active states across all interactive elements
- ✅ Animation system unified with standard durations
- ✅ Design tokens documented for future reference
- ✅ Component patterns established and reusable
- ✅ WCAG AA accessibility compliance on all interactive elements

---

## 🔧 Work Breakdown

### Task 1: Refactor Projects Page SCSS (Priority: 🔴 CRITICAL)
**Effort**: 1.5 hours | **Impact**: HIGH

#### Current Issues:
```scss
// ❌ WRONG - Custom color redefinition
$color1: #1E293B;  // Duplicates $primary
$color2: #E0F2FE;  // Custom, should use rgba($primary, $opacity-10)
$color3: #8B5CF6;  // Duplicates $ai-accent
$color5: #10B981;  // Duplicates $energy-accent

// ❌ WRONG - Hard-coded values
background: #f6f9fc;
color: #525f7f;
padding: $spacing 1.2rem;  // Mixing custom + implicit
border-top: 1px solid #eee;  // Should be $border-color-light
```

#### Required Changes:
1. **Remove custom color variables**, replace with:
   ```scss
   // Replace $color1 with $primary
   // Replace $color2 with rgba($primary, $opacity-10)
   // Replace $color3 with $ai-accent
   // Replace $color5 with $energy-accent
   ```

2. **Replace hard-coded values**:
   ```scss
   background: #f6f9fc;           → background: $gray-100;
   color: #525f7f;                → color: $gray-700;
   padding: $spacing 1.2rem;      → padding: $spacer-3 $spacer-4;
   border-top: 1px solid #eee;    → border-top: $border-width-1 solid $border-color-light;
   font-size: 1.1rem;             → font-size: $font-size-lg;
   font-weight: 600;              → font-weight: $font-weight-semibold;
   margin-bottom: 0.5rem;         → margin-bottom: $spacer-2;
   ```

3. **Replace custom spacing values**:
   ```scss
   $spacing: 16px  → Remove variable, use $spacer-3 or $spacer-4
   margin: 1.5rem 0  → margin: $spacer-5 0;
   padding: 0 $spacing  → padding: 0 $spacer-3;
   ```

4. **Update animation timing**:
   ```scss
   // Replace hard-coded durations with new variables
   animation: fadeInUp 0.6s ease-out forwards;  → Use $animation-duration-base
   animation: fillTop 2s forwards 4s ease-in-out;  → Use $animation-duration-slow
   ```

5. **Use breakpoint variables**:
   ```scss
   @media (max-width: 786px)  → @media (max-width: $breakpoint-lg)
   @media (min-width: 1024px)  → @media (min-width: $breakpoint-lg)
   ```

#### Checklist:
- [ ] Remove `$color1-6` variable definitions
- [ ] Replace all `$color*` references with branding variables
- [ ] Replace hard-coded color hex values with system variables
- [ ] Replace hard-coded font sizes with typography scale
- [ ] Replace hard-coded spacing with $spacer system
- [ ] Replace custom breakpoint with `$breakpoint-lg`
- [ ] Test page at all breakpoints
- [ ] Verify no visual changes
- [ ] Commit with message: "Refactor: Consolidate Projects page to use branding SCSS variables"

---

### Task 2: Create Shared Animation System (Priority: 🟡 MEDIUM-HIGH)
**Effort**: 1 hour | **Impact**: MEDIUM

#### New File: `assets/scss/_animations.scss`

```scss
/*-- scss:animations --*/

// =====================================================
// ANIMATION & TRANSITION SYSTEM
// =====================================================

// Duration Variables
$animation-duration-fast: 0.15s !default;
$animation-duration-base: 0.3s !default;
$animation-duration-slow: 0.6s !default;
$animation-duration-very-slow: 1s !default;

// Timing Functions
$animation-timing-linear: linear !default;
$animation-timing-ease: ease !default;
$animation-timing-ease-in: ease-in !default;
$animation-timing-ease-out: ease-out !default;
$animation-timing-ease-in-out: ease-in-out !default;

// Entrance Animations
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

// Timeline-specific Animations (moved from _projects.scss)
@keyframes fillLeft {
  100% { right: 100%; }
}

@keyframes fillTop {
  100% { top: 100%; }
}

@keyframes fillLeftOdd {
  100% { left: 100%; }
}

// Scale Animations
@keyframes scaleUp {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

// Rotate Animations
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

// Pulse Animation
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

// Bounce Animation
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

// =====================================================
// TRANSITION MIXINS
// =====================================================

@mixin transition-smooth($property: all) {
  transition: $property $animation-duration-base $animation-timing-ease-in-out;
}

@mixin transition-fast($property: all) {
  transition: $property $animation-duration-fast $animation-timing-ease-in-out;
}

@mixin transition-slow($property: all) {
  transition: $property $animation-duration-slow $animation-timing-ease-in-out;
}
```

#### Update `assets/twiga.scss`:
Add near the top:
```scss
/*-- scss:animations --*/
@import 'scss/animations';
```

#### Update `_projects.scss`:
```scss
// Remove @keyframes definitions (now in _animations.scss)
// Update animation references:
animation: fadeInUp $animation-duration-base $animation-timing-ease-out forwards;
```

#### Checklist:
- [ ] Create `_animations.scss` with all animations
- [ ] Add duration and timing variables
- [ ] Create transition mixins
- [ ] Update `twiga.scss` import
- [ ] Update `_projects.scss` to remove duplicate animations
- [ ] Test all animations on homepage and projects page
- [ ] Verify smooth 60fps animations
- [ ] Commit: "feat: Create centralized animation system with reusable animations and timing"

---

### Task 3: Create State Color & Shadow Tokens (Priority: 🟡 MEDIUM)
**Effort**: 1.5 hours | **Impact**: MEDIUM

#### Update `assets/scss/_defaults.scss`

Add after opacity levels section:
```scss
// =====================================================
// STATE COLOR SYSTEM
// =====================================================

// Hover States
$color-hover-light: rgba($primary, $opacity-10) !default;
$color-hover-dark: darken($primary, 10%) !default;

// Active States
$color-active: darken($primary, 15%) !default;

// Disabled States
$color-disabled: $gray-400 !default;
$color-disabled-bg: $gray-100 !default;

// Focus/Ring States
$color-focus-ring: rgba($primary, $opacity-30) !default;
$focus-ring-width: 2px !default;
$focus-ring-style: 2px solid $color-focus-ring !default;

// =====================================================
// SHADOW SYSTEM
// =====================================================

// Base Shadows (for depth/elevation)
$shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.05) !default;
$shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06) !default;
$shadow-base: 0 4px 6px rgba(0, 0, 0, 0.1), 0 2px 4px rgba(0, 0, 0, 0.06) !default;
$shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !default;
$shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !default;
$shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25) !default;

// Hover Shadows (elevate on hover)
$shadow-hover: $shadow-md !default;
$shadow-hover-lg: $shadow-lg !default;

// Interactive Shadow Transitions
$shadow-transition: box-shadow $animation-duration-base $animation-timing-ease-in-out !default;

// =====================================================
// TRANSFORM SYSTEM
// =====================================================

$transform-hover-lift: translateY(-2px) !default;
$transform-active-press: translateY(0) !default;
$transform-disabled: scale(1) !default;
```

#### Use in Components

Update `_cards.scss`:
```scss
.card {
  box-shadow: $shadow-base;  // Was $card-box-shadow
  
  &:hover {
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
  
  &:focus-visible {
    outline: $focus-ring-style;
  }
  
  &:disabled {
    opacity: 0.6;
    color: $color-disabled;
  }
}
```

#### Checklist:
- [ ] Add state color variables to `_defaults.scss`
- [ ] Add shadow system variables
- [ ] Add transform variables
- [ ] Update `_cards.scss` to use new variables
- [ ] Update `_buttons.scss` to use state colors
- [ ] Update `_projects.scss` shadow references
- [ ] Test hover/focus/active states on all interactive elements
- [ ] Commit: "feat: Add state color and shadow token system for consistency"

---

### Task 4: Standardize Interaction Patterns (Priority: 🟡 MEDIUM)
**Effort**: 2 hours | **Impact**: MEDIUM-HIGH

#### Button Consistency

Update `assets/scss/components/_buttons.scss`:
```scss
.btn {
  transition: $shadow-transition, 
              color $animation-duration-base $animation-timing-ease-in-out;
  
  &:hover {
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
  
  &:active {
    box-shadow: $shadow-sm;
    transform: $transform-active-press;
  }
  
  &:focus-visible {
    outline: $focus-ring-style;
    outline-offset: 2px;
  }
  
  &:disabled {
    background-color: $color-disabled-bg;
    color: $color-disabled;
    cursor: not-allowed;
  }
}
```

#### Link Consistency

Create `assets/scss/components/_links.scss`:
```scss
/*-- scss:components/links --*/

a {
  transition: color $animation-duration-fast $animation-timing-ease;
  
  &:hover {
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 4px;
  }
  
  &:focus-visible {
    outline: $focus-ring-style;
    outline-offset: 2px;
  }
}

.link-primary {
  color: $primary;
  
  &:hover {
    color: $color-hover-dark;
  }
}

.link-secondary {
  color: $secondary;
  
  &:hover {
    color: darken($secondary, 10%);
  }
}
```

#### Card Consistency (Update existing)

All cards should follow:
```scss
.card {
  box-shadow: $shadow-base;
  transition: $shadow-transition, transform $animation-duration-base $animation-timing-ease-in-out;
  
  &:hover {
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
}
```

#### Projects Page Cards

Update timeline-content:
```scss
.timeline-content {
  box-shadow: $shadow-base;  // Not hard-coded
  transition: $shadow-transition, transform $animation-duration-base $animation-timing-ease-in-out;
  
  &:hover {
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
}
```

#### Checklist:
- [ ] Standardize all button hover/focus/active states
- [ ] Create `_links.scss` component
- [ ] Update all card hover states
- [ ] Test keyboard navigation (Tab through all interactive elements)
- [ ] Verify focus rings visible on all inputs
- [ ] Test disabled states
- [ ] Commit: "refactor: Standardize interaction patterns (hover, focus, active states)"

---

### Task 5: Add Accessibility Improvements (Priority: 🟡 MEDIUM)
**Effort**: 1.5 hours | **Impact**: MEDIUM

#### Update `assets/scss/base.scss`

Add focus styles:
```scss
// Keyboard Navigation
:focus-visible {
  outline: $focus-ring-style;
  outline-offset: 2px;
}

// Skip to main content link (hide but accessible)
.skip-to-main {
  position: absolute;
  top: -40px;
  left: 0;
  background: $primary;
  color: $white;
  padding: $spacer-3 $spacer-4;
  text-decoration: none;
  z-index: 100;
  
  &:focus {
    top: 0;
  }
}
```

#### Add ARIA-label support

Update `_buttons.scss`:
```scss
.btn[aria-busy="true"] {
  opacity: 0.7;
  pointer-events: none;
}
```

#### Color Contrast Verification

Create checklist for WCAG AA (4.5:1 for text, 3:1 for UI):
- [ ] Primary text on white: $gray-900 or $gray-800 ✅ (15:1)
- [ ] Primary text on $primary: $white ✅ (10:1)
- [ ] Secondary text: $gray-700 ✅ (8:1)
- [ ] Disabled text: $gray-400 ⚠️ (Check: 2.3:1 - below target, needs review)

#### Checklist:
- [ ] Add focus-visible styles to all interactive elements
- [ ] Test keyboard navigation (no mouse)
- [ ] Verify color contrasts with accessibility checker
- [ ] Add ARIA labels to interactive components
- [ ] Test with screen reader (NVDA/JAWS)
- [ ] Document accessible patterns
- [ ] Commit: "a11y: Add keyboard navigation and focus state improvements"

---

### Task 6: Create Design System Documentation (Priority: 🟢 MEDIUM-LOW)
**Effort**: 2 hours | **Impact**: HIGH (long-term)

#### File 1: `DESIGN_TOKENS.md`

```markdown
# Design Tokens Reference

## Colors
### Primary
- Teal (#1E293B) - Primary brand color
- Light Teal (rgba) - Hover states
- Dark Teal - Active states

### Semantic
- Success: $green (#059669)
- Warning: $orange (#EA580C)
- Danger: $red (#DC2626)
- Info: $cyan (#0369A1)

### Accent
- Energy: #10B981 (Community projects)
- AI: #8B5CF6 (Maintained projects)

## Typography Scale
- Display: 2.625rem
- H1: 1.875rem
- H2: 1.5rem
- H3: 1.3rem
- ...etc

## Spacing System
- Base: 1rem (16px)
- Spacer-1: 4px
- Spacer-2: 8px
- Spacer-3: 16px
- ...up to Spacer-8: 80px

## Shadows
- xs: Small elevation
- base: Default cards
- hover: Hover state
- lg: Modal/overlay

## Animations
- Duration: 0.15s (fast), 0.3s (base), 0.6s (slow)
- Timing: ease, ease-in-out, ease-out
```

#### File 2: `COMPONENT_GUIDE.md`

Document patterns for:
- Card types (basic, elevated, outlined)
- Button variations
- Link behaviors
- Form inputs
- Navigation patterns
- Timeline component (Projects page)
- Blog listing
- Publication grid

#### Checklist:
- [ ] Create `DESIGN_TOKENS.md`
- [ ] Create `COMPONENT_GUIDE.md`
- [ ] Document all color variables
- [ ] Document typography scale
- [ ] Document spacing system
- [ ] Document shadow system
- [ ] Document animation system
- [ ] Commit: "docs: Add design system and component documentation"

---

### Task 7: Create Reusable Component Mixins (Priority: 🟢 LOW)
**Effort**: 1 hour | **Impact**: MEDIUM (future use)

#### New File: `assets/scss/_component-mixins.scss`

```scss
/*-- scss:mixins/components --*/

// Card with consistent styling
@mixin card-base {
  background: $white;
  border-radius: $border-radius-lg;
  box-shadow: $shadow-base;
  transition: $shadow-transition, transform $animation-duration-base $animation-timing-ease-in-out;
  
  &:hover {
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
}

// Button with consistent interactive states
@mixin button-interactive($bg-color: $primary, $text-color: $white) {
  background: $bg-color;
  color: $text-color;
  transition: all $animation-duration-base $animation-timing-ease-in-out;
  cursor: pointer;
  
  &:hover {
    background: darken($bg-color, 5%);
    box-shadow: $shadow-hover;
    transform: $transform-hover-lift;
  }
  
  &:active {
    box-shadow: $shadow-sm;
    transform: $transform-active-press;
  }
  
  &:focus-visible {
    outline: $focus-ring-style;
    outline-offset: 2px;
  }
  
  &:disabled {
    background: $color-disabled-bg;
    color: $color-disabled;
    cursor: not-allowed;
    box-shadow: none;
    transform: none;
  }
}

// Text input focus state
@mixin input-focus {
  border-color: $primary;
  box-shadow: 0 0 0 3px rgba($primary, $opacity-10);
  outline: none;
}

// Badge/label styling
@mixin badge($bg-color: $primary) {
  display: inline-block;
  padding: $spacer-1 $spacer-2;
  background: rgba($bg-color, $opacity-10);
  color: $bg-color;
  border-radius: $border-radius-full;
  font-size: $font-size-xs;
  font-weight: $font-weight-semibold;
  text-transform: uppercase;
  letter-spacing: $letter-spacing-wider;
}
```

#### Checklist:
- [ ] Create `_component-mixins.scss`
- [ ] Add to `twiga.scss` imports
- [ ] Document mixin usage
- [ ] Update components to use mixins
- [ ] Commit: "refactor: Add reusable component mixins for consistency"

---

## 📊 Phase 5 Summary Table

| Task | Duration | Priority | Files Changed | Impact |
|------|----------|----------|----------------|--------|
| 1. Refactor Projects Page | 1.5h | 🔴 CRITICAL | _projects.scss | HIGH |
| 2. Animation System | 1h | 🟡 MEDIUM | _animations.scss, twiga.scss | MEDIUM |
| 3. State Tokens | 1.5h | 🟡 MEDIUM | _defaults.scss, _cards.scss, _buttons.scss | MEDIUM |
| 4. Interaction Patterns | 2h | 🟡 MEDIUM | _buttons.scss, _cards.scss, _projects.scss | MEDIUM-HIGH |
| 5. Accessibility | 1.5h | 🟡 MEDIUM | base.scss | MEDIUM |
| 6. Documentation | 2h | 🟢 LOW | DESIGN_TOKENS.md, COMPONENT_GUIDE.md | HIGH |
| 7. Component Mixins | 1h | 🟢 LOW | _component-mixins.scss | MEDIUM |
| **TOTAL** | **10h** | — | **10 files** | **TRANSFORMATIVE** |

---

## 🚀 Implementation Strategy

### Phase 5A: Foundation (Hours 1-3)
Priority: Complete Task 1 & 2 first
1. Refactor Projects page (1.5h)
2. Create animation system (1.5h)
- **Result**: Consolidation of custom variables, reusable animations

### Phase 5B: Enhancement (Hours 4-7)
Priority: Add state system & patterns
3. State color tokens (1.5h)
4. Interaction patterns (2h)
5. Accessibility (1.5h)
- **Result**: Consistent hover/focus/active states, WCAG compliance

### Phase 5C: Documentation (Hours 8-10)
Priority: Codify knowledge for team
6. Design system docs (2h)
7. Component mixins (1h)
- **Result**: Reference guide for future development

---

## ✅ Merge Strategy

- **Create branch**: `feature/design-system-consolidation`
- **Commit frequency**: After each task completes
- **Testing**: Manual visual regression testing at each step
- **Review**: Check all pages at multiple breakpoints
- **Final**: Comprehensive comparison: Before Phase 5 vs. After Phase 5

---

## 🎯 Phase 5 Success Indicators

By end of Phase 5:
- ✅ Zero custom color variables (all use branding system)
- ✅ Zero hard-coded dimensions (all use spacing system)
- ✅ Consistent hover states across all interactive elements
- ✅ Visible focus states for keyboard navigation
- ✅ Animation system unified
- ✅ Design tokens documented
- ✅ Component patterns established
- ✅ WCAG AA compliance verified
- ✅ Site feels more cohesive and professional
- ✅ Future changes easier to implement

---

## 📝 Notes

- Changes are **non-breaking** - visual output should remain identical
- All changes are **maintainability improvements**
- Can be merged directly to main (no QA blocker)
- Recommended to preview in browser to verify no regressions
- Provides foundation for future features (dark mode, themes, etc.)

