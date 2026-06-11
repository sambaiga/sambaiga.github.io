# Design Tokens Reference

This document provides a comprehensive reference of all design tokens used throughout the site.

## Color Tokens

### Primary Colors

| Name | Value | Usage |
|------|-------|-------|
| `$primary` | #1E293B (Teal) | Primary brand color, primary buttons, links, headings |
| `$secondary` | #495057 (Dark Gray) | Secondary text, secondary buttons |
| `$success` | #059669 (Green) | Success messages, success buttons |
| `$info` | #0369A1 (Cyan) | Info messages, info buttons |
| `$warning` | #EA580C (Orange) | Warning messages, warning buttons |
| `$danger` | #DC2626 (Red) | Error messages, danger buttons |

### Accent Colors

| Name | Value | Usage |
|------|-------|-------|
| `$ai-accent` | #8B5CF6 (Purple) | AI-related projects, maintained status |
| `$energy-accent` | #10B981 (Green) | Energy-related projects, community status |

### Grayscale

| Name | Value | Usage |
|------|-------|-------|
| `$gray-100` | #F8F9FA | Background, light fills |
| `$gray-200` | #E9ECEF | Borders, dividers |
| `$gray-300` | #DEE2E6 | Subtle borders |
| `$gray-400` | #CED4DA | Disabled elements |
| `$gray-500` | #ADB5BD | Secondary text |
| `$gray-600` | #6B7280 | Body text alternative |
| `$gray-700` | #495057 | Body text (default) |
| `$gray-800` | #373A3C | Dark text |
| `$gray-900` | #212529 | Darkest text |

### State Colors

| Name | Value | Usage |
|------|-------|-------|
| `$color-hover-light` | rgba($primary, 0.1) | Hover background |
| `$color-hover-dark` | darken($primary, 10%) | Hover text |
| `$color-active` | darken($primary, 15%) | Active/pressed state |
| `$color-disabled` | #CED4DA | Disabled text |
| `$color-disabled-bg` | #F8F9FA | Disabled background |
| `$color-focus-ring` | rgba($primary, 0.3) | Focus ring outline |

## Typography

### Font Families

| Token | Font Stack | Usage |
|-------|-----------|-------|
| `$font-family-sans-serif` | Libre Franklin | Body text, paragraphs |
| `$headings-font-family` | Jost | Headings (h1-h6) |
| `$font-family-monospace` | SFMono, Menlo, Monaco | Code blocks, inline code |
| `$navbar-font-family` | Jost | Navigation text |
| `$footer-font-family` | Jost | Footer text |

### Font Sizes (Modular Scale - 1.25 ratio)

| Token | Size | Usage |
|-------|------|-------|
| `$font-size-xs` | ~0.775rem (12px) | Small labels, badges |
| `$font-size-sm` | ~0.875rem (14px) | Small text, captions |
| `$font-size-md` | ~1rem (16px) | Normal text |
| `$font-size-base` | ~1.05rem (16.8px) | Body text (default) |
| `$font-size-lg` | ~1.125rem (18px) | Large text, card titles |
| `$font-size-xl` | ~1.3rem (20.8px) | Larger text |
| `$font-size-xxl` | ~1.5rem (24px) | Subheadings |
| `$font-size-xxxl` | ~1.875rem (30px) | Large headings |
| `$font-size-display` | ~2.625rem (42px) | Extra large headings |

### Heading Sizes

| Token | Size | Element |
|-------|------|---------|
| `$h1-font-size` | $font-size-xxxl | `<h1>` |
| `$h2-font-size` | $font-size-xxl | `<h2>` |
| `$h3-font-size` | $font-size-xl | `<h3>` |
| `$h4-font-size` | $font-size-lg | `<h4>` |
| `$h5-font-size` | $font-size-base | `<h5>` |
| `$h6-font-size` | $font-size-sm | `<h6>` |

### Font Weights

| Token | Weight | Usage |
|-------|--------|-------|
| `$font-weight-thin` | 200 | Light headings |
| `$font-weight-light` | 300 | Light text |
| `$font-weight-normal` | 400 | Body text (default) |
| `$font-weight-medium` | 500 | Slightly bold |
| `$font-weight-semibold` | 600 | Headings, labels |
| `$font-weight-bold` | 700 | Bold text, strong |
| `$font-weight-extrabold` | 800 | Very bold |

### Line Heights

| Token | Value | Usage |
|-------|-------|-------|
| `$line-height-tight` | 1.2 | Compact headings |
| `$line-height-snug` | 1.3 | Headings |
| `$line-height-normal` | 1.5 | Normal text |
| `$line-height-relaxed` | 1.65 | Body text (default) |
| `$line-height-loose` | 1.8 | Easy to read |

## Spacing System

Base unit: `$spacer-base: 1rem (16px)`

All spacing uses an 8px grid:

| Token | Size | Usage |
|-------|------|-------|
| `$spacer-1` | 4px | Minimal spacing |
| `$spacer-2` | 8px | Small gaps |
| `$spacer-3` | 16px | Standard spacing |
| `$spacer-4` | 24px | Medium spacing |
| `$spacer-5` | 32px | Large spacing |
| `$spacer-6` | 48px | Extra large spacing |
| `$spacer-7` | 64px | Section spacing |
| `$spacer-8` | 80px | Large section spacing |

### Section Padding

| Token | Value | Usage |
|-------|-------|-------|
| `$section-padding-y` | 4rem (64px) | Section vertical padding |
| `$section-padding-y-sm` | 2rem (32px) | Small section padding |
| `$section-padding-y-lg` | 6rem (96px) | Large section padding |
| `$section-padding-x` | 1.5rem (24px) | Section horizontal padding |

## Shadow System

### Base Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `$shadow-xs` | 0 1px 2px rgba(0,0,0,0.05) | Minimal elevation |
| `$shadow-base` | 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06) | Cards at rest |
| `$shadow-hover` | 0 10px 15px -3px rgba(0,0,0,0.1), ... | Cards on hover |
| `$shadow-hover-lg` | 0 20px 25px -5px rgba(0,0,0,0.1), ... | Modals, dropdowns |
| `$shadow-sm` | Bootstrap variable | Small shadows |
| `$shadow-md` | Bootstrap variable | Medium shadows |
| `$shadow-lg` | Bootstrap variable | Large shadows |
| `$shadow-xl` | Bootstrap variable | Extra large shadows |

### Shadow Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `$shadow-transition` | box-shadow 0.3s ease-in-out | Smooth shadow changes |

## Animation System

### Durations

| Token | Duration | Usage |
|-------|----------|-------|
| `$animation-duration-fast` | 0.15s | Quick transitions (focus, hover) |
| `$animation-duration-base` | 0.3s | Standard transitions |
| `$animation-duration-slow` | 0.6s | Entrance animations |
| `$animation-duration-very-slow` | 1s | Slow, emphasized animations |

### Timing Functions

| Token | Value | Usage |
|-------|-------|-------|
| `$animation-timing-linear` | linear | Constant speed (spinners) |
| `$animation-timing-ease` | ease | Smooth, natural feel |
| `$animation-timing-ease-in` | ease-in | Accelerating motion |
| `$animation-timing-ease-out` | ease-out | Decelerating motion (entrances) |
| `$animation-timing-ease-in-out` | ease-in-out | Smooth both directions (default) |

### Common Animations

| Name | Duration | Used For |
|------|----------|----------|
| `fadeIn` | 0.3s | Opacity change |
| `fadeInUp` | 0.6s | Slide up while fading |
| `slideInLeft` | 0.6s | Slide from left |
| `slideInRight` | 0.6s | Slide from right |
| `scaleUp` | 0.3s | Grow while appearing |
| `spin` | 1s (infinite) | Loading spinners |
| `pulse` | 1s (infinite) | Attention grabber |
| `bounce` | 0.6s (infinite) | Playful emphasis |

### Transform Tokens

| Token | Value | Usage |
|-------|-------|-------|
| `$transform-hover-lift` | translateY(-2px) | Card/button hover lift |
| `$transform-active-press` | translateY(0) | Button press |
| `$transform-disabled` | scale(1) | No transform for disabled |

## Border Radius

| Token | Size | Usage |
|-------|------|-------|
| `$border-radius-xs` | 0.125rem (2px) | Subtle rounding |
| `$border-radius-sm` | 0.25rem (4px) | Small rounding |
| `$border-radius` | 0.375rem (6px) | Standard rounding |
| `$border-radius-lg` | 0.5rem (8px) | Larger rounding |
| `$border-radius-xl` | 0.75rem (12px) | Extra large rounding |
| `$border-radius-2xl` | 1rem (16px) | Very large rounding |
| `$border-radius-3xl` | 1.5rem (24px) | Huge rounding |
| `$border-radius-full` | 9999px | Perfect circles |

## Border & Stroke

| Token | Value | Usage |
|-------|-------|-------|
| `$border-width-1` | 1px | Standard border |
| `$border-width-2` | 2px | Thicker border |
| `$border-width-3` | 3px | Accent border |
| `$border-width-4` | 4px | Strong border |
| `$border-color-light` | #DEE2E6 | Light borders |
| `$border-color` | #CED4DA | Standard borders |
| `$border-color-dark` | #ADB5BD | Dark borders |

## Opacity

Standard opacity levels (0.05 to 0.95):

| Token | Value | Usage |
|-------|-------|-------|
| `$opacity-05` | 0.05 | Very subtle |
| `$opacity-10` | 0.1 | Subtle backgrounds |
| `$opacity-20` | 0.2 | Light overlays |
| `$opacity-30` | 0.3 | Medium overlays |
| `$opacity-50` | 0.5 | Disabled elements |
| `$opacity-75` | 0.75 | Semi-transparent |

## Responsive Breakpoints

| Token | Size | Device |
|-------|------|--------|
| `$breakpoint-xs` | 0 | Extra small |
| `$breakpoint-sm` | 576px | Small (phones) |
| `$breakpoint-md` | 768px | Medium (tablets) |
| `$breakpoint-lg` | 992px | Large (desktops) |
| `$breakpoint-xl` | 1200px | Extra large |
| `$breakpoint-xxl` | 1400px | Ultra large |

## Usage Guidelines

### Color Palette Consistency
- Always use color tokens, never hard-code hex values
- Use semantic colors ($primary, $danger) not numbered grays
- State colors ($color-hover-dark) for interactive states

### Typography Patterns
- Headings: Jost font family, semibold weight minimum
- Body: Libre Franklin, normal weight, relaxed line height
- Code: Monospace family, smaller size

### Spacing Rules
- Use spacer tokens (multiples of 8px)
- Section padding: `$section-padding-y` vertical, `$section-padding-x` horizontal
- Component padding: `$spacer-3` or `$spacer-4` for cards

### Animation Best Practices
- Entrance animations: use `$animation-duration-slow`
- Hover/focus transitions: use `$animation-duration-fast`
- Always include `@media (prefers-reduced-motion: reduce)`

### Accessibility
- Color contrast: minimum 4.5:1 for text
- Focus indicators: always visible with `$focus-ring-style`
- Disabled elements: use `$color-disabled` and lower opacity
- Motion: respect `prefers-reduced-motion` setting
