# Component Guide

Practical patterns and usage guidelines for site components.

## Cards

### Base Card
```html
<div class="card">
  <div class="card-body">
    Content goes here
  </div>
</div>
```

**Styling**: `$shadow-base` shadow, rounded corners, white background
**Hover**: Shadow elevates to `$shadow-hover`, slight lift effect

### Card with Header and Footer
```html
<div class="card">
  <div class="card-header">
    <h3>Card Title</h3>
  </div>
  <div class="card-body">
    Main content
  </div>
  <div class="card-footer">
    Footer content
  </div>
</div>
```

### Talk Card (with gradient border)
```html
<div class="talk-card">
  <div class="talk-date-badge">
    <span class="date-month">Apr</span>
    <span class="date-day">15</span>
    <span class="date-year">2026</span>
  </div>
  <div class="card-body">
    Talk details...
  </div>
</div>
```

**Features**: Gradient border on hover (pink → cyan → teal)

## Buttons

### Button Variants
```html
<!-- Primary -->
<button class="btn btn-primary">Primary</button>

<!-- Secondary -->
<button class="btn btn-secondary">Secondary</button>

<!-- Outline -->
<button class="btn btn-primary btn-outline">Outline</button>

<!-- Sizes -->
<button class="btn btn-sm">Small</button>
<button class="btn">Normal</button>
<button class="btn btn-lg">Large</button>

<!-- Disabled -->
<button class="btn btn-primary" disabled>Disabled</button>
```

**States**:
- Default: Styled color
- Hover: Darker background, elevated shadow
- Focus: Focus ring visible
- Active: Pressed appearance
- Disabled: Grayed out

### Button with Icon
```html
<button class="btn btn-primary">
  <i class="bi bi-arrow-right"></i>
  Click me
</button>
```

## Links

### Basic Links
```html
<!-- Primary link -->
<a href="#">Primary link</a>

<!-- Secondary link -->
<a href="#" class="link-secondary">Secondary</a>

<!-- Success link -->
<a href="#" class="link-success">Success</a>

<!-- Danger link -->
<a href="#" class="link-danger">Danger</a>
```

**Behavior**:
- Default: Primary color
- Hover: Darker color, underline appears
- Focus: Focus ring visible
- External links: automatic "↗" indicator

### Navigation Links
```html
<nav>
  <a href="/" class="nav-link active">Home</a>
  <a href="/about" class="nav-link">About</a>
  <a href="/blog" class="nav-link">Blog</a>
</nav>
```

## Forms

### Text Input
```html
<label for="name">Name</label>
<input type="text" id="name" required>
```

**Focus State**: Border color changes to primary, subtle shadow appears

### Select
```html
<label for="select">Choose one</label>
<select id="select">
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

### Textarea
```html
<label for="message">Message</label>
<textarea id="message"></textarea>
```

### Checkbox & Radio
```html
<label>
  <input type="checkbox">
  Agree to terms
</label>

<label>
  <input type="radio" name="choice">
  Option A
</label>
```

## Timeline Component (Projects Page)

### Structure
```html
<div class="timeline-event status-active">
  <div class="timeline-icon">
    <i class="bi bi-rocket"></i>
  </div>
  <div class="timeline-date">2024</div>
  <div class="timeline-content">
    <h3 class="timeline-title">Project Name</h3>
    <p class="timeline-description">...</p>
    <div class="timeline-meta">
      <span class="timeline-status">🚀 Active</span>
      <span>Updated: 2024-06</span>
    </div>
    <div class="timeline-links">
      <a href="#" class="timeline-link">
        <i class="bi bi-github"></i>GitHub
      </a>
    </div>
  </div>
</div>
```

### Status Variants
- `.status-active`: Teal color (#1E293B)
- `.status-maintained`: Purple color (#8B5CF6)
- `.status-community`: Green color (#10B981)

### Features
- Alternating left/right layout
- Connecting lines between projects
- Color-coded by status
- Animated entrance
- Hover elevation effect

## Navigation

### Navbar
```html
<nav class="navbar navbar-expand">
  <a href="/" class="navbar-brand">Anthony Faustine</a>
  <div class="navbar-nav">
    <a href="/pages/about" class="nav-link">About</a>
    <a href="/pages/blog" class="nav-link">Blog</a>
  </div>
</nav>
```

### Mobile Menu (planned)
- Hamburger icon for mobile
- Slide-out menu
- Touch-friendly size

## Status Indicators

### Badges
```html
<span class="badge">New</span>
<span class="badge badge-success">Published</span>
<span class="badge badge-danger">Urgent</span>
```

### Status Labels (Timeline)
```html
<span class="timeline-status">🚀 Active</span>
<span class="timeline-status">⚙️ Maintained</span>
<span class="timeline-status">👥 Community</span>
```

## Spacing Examples

### Component Padding
- Cards: `$spacer-3` (16px)
- Headings: `$spacer-3` bottom margin
- Section padding: `$section-padding-y` / `$section-padding-x`

### Element Gaps
- Between sections: `$spacer-5` (32px) or larger
- Between items in list: `$spacer-2` (8px)
- Between cards: `$spacer-3` (16px)

## Animation Guidelines

### When to Use Animations
- **Entrance**: Page load, new content appears → use `fadeInUp` 0.6s
- **Interaction**: Hover, click → use `shadow-transition` 0.3s
- **Focus**: Keyboard navigation → use fast transition 0.15s
- **Loading**: Long operations → use `spin` infinite

### Motion Preferences
Always respect user's motion preferences:
```scss
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; }
}
```

## Accessibility Checklist

For each component:
- [ ] Focus states visible (focus ring)
- [ ] Keyboard navigable (Tab key works)
- [ ] Color contrast: 4.5:1 minimum
- [ ] Labels associated with inputs
- [ ] Disabled state clear
- [ ] Icons have aria-label or title
- [ ] Links have descriptive text

## Color Usage Guidelines

### Primary Color ($primary - Teal)
- Main buttons
- Primary links
- Active states
- Focus indicators
- Headings
- Important UI elements

### Secondary Color ($secondary - Gray)
- Body text (default)
- Secondary buttons
- Less important information
- Form labels

### Semantic Colors
- `$success` (Green): Success messages, confirmations
- `$danger` (Red): Errors, destructive actions
- `$warning` (Orange): Cautions, warnings
- `$info` (Cyan): Information, notices

### Accent Colors
- `$ai-accent` (Purple): AI, Maintained projects
- `$energy-accent` (Green): Energy, Community projects

## Typography Hierarchy

| Level | Font | Weight | Size | Color | Usage |
|-------|------|--------|------|-------|-------|
| h1 | Jost | Semibold | 1.875rem | Gray-900 | Page title |
| h2 | Jost | Semibold | 1.5rem | Gray-900 | Section title |
| h3 | Jost | Semibold | 1.3rem | Primary | Subsection |
| h4 | Jost | Semibold | 1.125rem | Primary | Card title |
| body | Libre Franklin | Normal | 1.05rem | Gray-700 | Main text |
| small | Libre Franklin | Normal | 0.875rem | Gray-600 | Secondary |
| code | Monospace | Normal | 0.85rem | Primary | Code blocks |

## Best Practices

1. **Consistency**: Use tokens, not custom values
2. **Accessibility**: Always include focus states and labels
3. **Spacing**: Use 8px grid for predictable layouts
4. **Motion**: Respect prefers-reduced-motion
5. **Color**: Ensure sufficient contrast
6. **Typography**: Follow hierarchy guidelines
7. **Responsive**: Test on multiple breakpoints
8. **Performance**: Use CSS transitions, not animations when possible

## Future Component Patterns

- [ ] Tabs component
- [ ] Accordion component
- [ ] Modals/Dialogs
- [ ] Dropdown menus
- [ ] Breadcrumbs
- [ ] Tooltips
- [ ] Popups/Popovers
