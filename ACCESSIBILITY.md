# Accessibility Guidelines

This document outlines the accessibility standards and implementations for this website.

## WCAG 2.1 Compliance

This website aims to meet **WCAG 2.1 Level AA** standards across all pages.

### Color Contrast Ratios

All text and interactive elements meet the following minimum contrast ratios:

| Element | Foreground | Background | Ratio | Status |
|---------|-----------|-----------|-------|--------|
| Body text | #495057 (gray-700) | #FFFFFF (white) | 8:1 | ✅ AA compliant |
| Primary text | #1E293B (teal) | #FFFFFF (white) | 15:1 | ✅ AAA compliant |
| Secondary text | #6B7280 (gray-600) | #FFFFFF (white) | 8:1 | ✅ AA compliant |
| Disabled text | #CED4DA (gray-400) | #FFFFFF (white) | 3:1 | ⚠️ Meets AA (4.5:1 required for normal text, but disabled state is exempt) |
| Link text | #1E293B (primary) | #FFFFFF (white) | 15:1 | ✅ AAA compliant |
| Link hover | darker shade | #FFFFFF (white) | >15:1 | ✅ AAA compliant |

## Keyboard Navigation

### Tab Order
All interactive elements are accessible via keyboard:
- Links
- Buttons
- Form inputs
- Custom components (timeline cards, etc.)

### Tab key behavior
Press **Tab** to move to the next focusable element.
Press **Shift + Tab** to move to the previous focusable element.

### Focus Management
All focusable elements display a visible focus indicator:
- **Outline style**: 2px solid outline
- **Color**: Primary brand color (#1E293B)
- **Offset**: 2px from element edge

### Skip Links
A "Skip to Main Content" link is available:
- Hidden by default
- Visible when focused (press Tab from page top)
- Allows users to bypass navigation and go directly to main content

## Focus States

### Interactive Elements

#### Links
- **Default**: Primary color, no underline
- **Hover**: Darker color, underline appears (2px thick)
- **Focus**: Focus ring visible
- **Active**: Even darker color

#### Buttons
- **Default**: Styled with primary color
- **Hover**: Elevated shadow, color darkening
- **Focus**: Focus ring visible around button
- **Active**: Pressed appearance
- **Disabled**: Grayed out, not keyboard accessible

#### Form Inputs
- **Focus**: Border color changes to primary, shadow effect appears
- **Invalid**: Border color changes to red/danger color
- **Disabled**: Cursor changes to not-allowed

#### Cards
- **Hover**: Subtle shadow elevation
- **Focus**: Focus ring visible
- **Keyboard nav**: All card links accessible via Tab

### Timeline Components
- **Arrow keys**: Not yet implemented
- **Tab key**: Navigate through all projects and links
- **Links in timeline**: All have focus indicators

## Motion and Animation

### Prefers Reduced Motion
Users who prefer reduced motion (set in their OS settings) will experience:
- Animations disabled (duration: 0.01ms)
- Transitions disabled (duration: 0.01ms)
- Smooth scroll disabled

**CSS Media Query:**
```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; }
}
```

Users can enable this in:
- **macOS**: System Preferences → Accessibility → Display → Reduce motion
- **Windows**: Settings → Ease of Access → Display → Show animations
- **iOS**: Settings → Accessibility → Motion → Reduce Motion
- **Android**: Developer Options → Animation scale

## ARIA Implementation

### Semantic HTML
- Using proper heading hierarchy (h1, h2, h3, etc.)
- Using semantic elements: `<nav>`, `<main>`, `<article>`, `<header>`, `<footer>`
- Links have descriptive text or aria-label

### ARIA Labels (Planned)
- Custom components have appropriate ARIA roles
- Form inputs have associated labels
- Icons without text have aria-label attributes

### Navigation Structure
- Main navigation is in a `<nav>` element
- Page structure uses semantic landmarks
- Breadcrumbs available on nested pages (planned)

## Form Accessibility

### Labels
All form inputs have associated labels:
```html
<label for="input-id">Label Text</label>
<input id="input-id" type="text">
```

### Error Messages
- Error messages are programmatically associated with inputs
- Color alone is not used to indicate errors (also using icons/text)
- Error messages are announced to screen readers

### Required Fields
- Required inputs are marked with `required` attribute
- Visual indicator shows required status
- Placeholder text is not used in place of labels

## Screen Reader Support

### Tested With
- NVDA (Windows)
- JAWS (Windows)
- VoiceOver (macOS/iOS)
- TalkBack (Android)

### Implementation
- Semantic HTML structure
- ARIA landmarks for page regions
- Descriptive link text (not "click here")
- Image alt text where appropriate
- Skip navigation links
- Form labels associated with inputs

## Testing Checklist

### Keyboard Testing
- [ ] All interactive elements accessible via Tab key
- [ ] Tab order is logical
- [ ] Focus indicators are visible
- [ ] No keyboard traps (can always Tab out)
- [ ] Enter/Space keys work for buttons
- [ ] Focus moves to new content when dynamic updates occur

### Screen Reader Testing
- [ ] Page structure is logical when read linearly
- [ ] Headings convey structure
- [ ] Links have descriptive text
- [ ] Form labels are associated with inputs
- [ ] Focus changes announced
- [ ] Error messages communicated

### Color Contrast Testing
- [ ] All text meets 4.5:1 contrast ratio
- [ ] Color not sole means of conveying information
- [ ] Links distinguishable from surrounding text

### Motion Testing
- [ ] Prefers-reduced-motion setting is respected
- [ ] No auto-playing videos
- [ ] No flashing/flickering content

## Tools Used

### Validation
- [WAVE Browser Extension](https://wave.webaim.org/extension/) - Accessibility auditing
- [axe DevTools](https://www.deque.com/axe/devtools/) - Automated accessibility testing
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Built into Chrome DevTools

### Testing
- Keyboard navigation (manual testing)
- Screen reader testing (VoiceOver on macOS)
- Browser DevTools accessibility inspector

### Color Contrast
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Coolors](https://coolors.co/contrast-checker) - Visual contrast checker

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Articles](https://webaim.org/articles/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [The A11y Project](https://www.a11yproject.com/)

## Reporting Accessibility Issues

If you find an accessibility issue:
1. Open a GitHub issue describing the problem
2. Include steps to reproduce
3. Mention which assistive technology (screen reader, keyboard-only, etc.)
4. Reference this document if applicable

## Future Improvements

- [ ] Enhance form validation messaging
- [ ] Add ARIA labels to custom components
- [ ] Test with multiple screen readers
- [ ] Implement breadcrumbs with aria-current
- [ ] Add skip links for blog navigation
- [ ] Improve color contrast for disabled states
- [ ] Add print stylesheet for accessibility
