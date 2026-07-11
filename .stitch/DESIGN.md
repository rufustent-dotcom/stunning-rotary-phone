---
name: Greed Control Room
colors:
  surface: '#0b1020'
  surface-dim: '#121a2f'
  surface-bright: '#1a2540'
  surface-container-lowest: '#070b16'
  surface-container-low: '#10182b'
  surface-container: '#16213a'
  surface-container-high: '#1d2b49'
  surface-container-highest: '#243657'
  on-surface: '#eef3ff'
  on-surface-variant: '#a9b6d3'
  inverse-surface: '#eef3ff'
  inverse-on-surface: '#0b1020'
  outline: '#3a4d78'
  outline-variant: '#263658'
  surface-tint: '#59f0a7'
  primary: '#59f0a7'
  on-primary: '#08120e'
  primary-container: '#113528'
  on-primary-container: '#bfffe0'
  inverse-primary: '#0d6f47'
  secondary: '#52c7ff'
  on-secondary: '#06131c'
  secondary-container: '#102c3b'
  on-secondary-container: '#c2efff'
  tertiary: '#ffd166'
  on-tertiary: '#1a1405'
  tertiary-container: '#3a2b09'
  on-tertiary-container: '#ffedb8'
  error: '#ff6b7a'
  on-error: '#2d0710'
  error-container: '#4f1420'
  on-error-container: '#ffd9de'
  background: '#070b16'
  on-background: '#eef3ff'
  surface-variant: '#1a2540'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.03em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  body-bold:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: '0'
  label-caps:
    fontFamily: IBM Plex Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  stat-lg:
    fontFamily: IBM Plex Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
rounded:
  sm: 0.375rem
  DEFAULT: 0.75rem
  md: 1rem
  lg: 1.25rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 20px
  margin-mobile: 16px
  margin-desktop: 32px
---

# Design System: Greed Control Room
**Project ID:** 42045f1c-0fc6-4eb0-b7ae-37750da5b2e5

## Brand & Style

Greed should feel like a live operations cockpit for profitable automation:
focused, fast, and quietly confident. The visual language combines institutional
trading seriousness with a crisp systems-dashboard tone so users feel they are
watching a real signal pipeline rather than a playful simulation.

The atmosphere is dark, high-contrast, and data-forward. Surfaces stay deep and
cool, while profitable states glow in mint green, actionable system controls
lean electric blue, and warnings use a hot rose or amber accent. Motion and
highlighting should imply constant market activity without making the interface
feel noisy or frantic.

## Colors

The foundation is a layered midnight palette built from **Control Room Black**
(`#070b16`), **Slate Panel** (`#16213a`), and **Raised Console** (`#243657`).
These colors keep charts, tables, and deployment timelines readable while
supporting strong contrast for text.

**Profit Mint** (`#59f0a7`) is the signature accent and should be reserved for
positive market signals, primary calls to action, and selected states.
**Signal Blue** (`#52c7ff`) supports navigation, neutral interactivity, and
informational widgets. **Alert Gold** (`#ffd166`) is used for thresholds,
pending actions, and cautionary emphasis. **Failure Rose** (`#ff6b7a`) is
reserved for deployment errors, rejected actions, and unhealthy system status.

Primary text uses **Frost White** (`#eef3ff`) against dark surfaces. Secondary
labels and metadata use **Muted Telemetry** (`#a9b6d3`) to keep dense data
readable without flattening hierarchy.

## Typography

The system pairs **Space Grotesk** for display moments with **Inter** for core
interface text. Space Grotesk gives hero metrics and major section headings a
technical, modern presence. Inter handles tables, controls, and supporting copy
with strong legibility at small sizes.

**IBM Plex Mono** is used selectively for prices, tick values, event IDs, and
deployment counts so real-time data feels machine-generated and precise.
Display styles are tight and bold; body styles remain clean and restrained.
Labels can use uppercase mono tracking to echo terminal and trading-tool cues.

## Layout & Spacing

Layouts should follow a modular control-room grid with a persistent header,
primary workspace, and stacked analysis panels. Desktop views should prefer
two- and three-column arrangements for live signal summaries, action mappings,
and deployment history. Mobile layouts should collapse into a single prioritized
feed while preserving immediate access to the current profitable event.

Use a strict 4px spacing rhythm with 16px, 24px, and 32px intervals doing most
of the work. Panels need enough internal padding to let dense metrics breathe,
but the overall interface should still feel compact and efficient rather than
editorial or spacious.

## Elevation & Depth

Depth should come from panel layering, subtle borders, and restrained glow
rather than heavy shadows. Base surfaces are nearly black; elevated cards and
modals use slightly lighter slate containers with thin blue-gray outlines.

Positive states can introduce a soft mint halo, and selected controls can carry
a cool blue edge-light. Avoid broad blur or playful translucency; the product
should feel sharp, instrumented, and trustworthy.

## Shapes

The shape language is clean and slightly rounded. Cards and panels should use
12px to 20px radii so the interface feels modern without becoming soft. Inputs
and buttons should share the same mid-radius family to keep controls visually
cohesive.

Badges, chips, and status pills can become fully rounded when they communicate
state at a glance, especially for profit, threshold, queued, and failed states.

## Components

### Buttons

Primary buttons use **Profit Mint** fills with dark text for decisive actions
like deploy, acknowledge, or enable automation. Secondary buttons use outlined
or tonal **Signal Blue** treatments. Hover states should brighten slightly and
lift with a subtle edge glow rather than a large shadow.

### Cards & Panels

Cards act like operator consoles: dark layered surfaces, clear borders, strong
section titles, and compact metadata rows. High-priority panels such as current
signal, deployment status, and action mapping should support inline badges and
quick scan metrics without visual clutter.

### Charts & Timelines

Price movement, thresholds, and profitable peaks should be rendered with crisp
strokes on dark backgrounds. Use mint for profitable lines or markers, blue for
neutral trend context, gold for thresholds, and rose only for failure or loss
events. Gridlines should stay subdued.

### Inputs & Forms

Inputs should use dark inset fields with visible borders and strong focus rings.
Numeric fields, thresholds, and tick controls benefit from mono text. Validation
states must be immediate and high contrast.

### Status Chips & Deployment Records

Status chips should be small, dense, and unmistakable: mint for profitable or
successful, gold for pending, blue for informational, and rose for failed.
Deployment records should read like an audit trail with timestamp, package,
target count, and outcome aligned in clear columns.
