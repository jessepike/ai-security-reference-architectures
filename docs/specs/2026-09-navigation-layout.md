# Primary navigation layout specification

**Status:** Authorized implementation for preview  
**Work:** AISG-017 · RM-01 · O1, O2  
**Date:** 15 September 2026

## Problem

The production header presents eight peer links in one row. Labels crowd each other at laptop widths, and application material is split across unrelated positions. Readers need a calmer navigation hierarchy that keeps every existing destination easy to reach.

## Design

Keep the compact two-line wordmark at left. At right, show Overview and Governance as direct links, with three native disclosure groups:

- Architectures: the three peer security views.
- Secure Business AI: application overview, CISO walkthrough, and detailed guide.
- Resources: project guide, architect guides, sources, review status, authoring standard, and decisions when present.

Native `details` and `summary` elements keep grouped links available without JavaScript. JavaScript closes an open group when another opens, on Escape, or on an outside click. At mobile widths, the existing menu button progressively enhances a roomy vertical menu; without JavaScript, the complete navigation remains visible.

Use the existing navy, teal, white, pale blue, Manrope, and focus-ring tokens. Keep labels on one line, use generous 44-pixel minimum targets, and move to the mobile layout before labels need to shrink. Dropdown structure encodes hierarchy; decoration remains restrained.

## Acceptance checks

- All prior destinations remain reachable, with the application routes grouped together.
- Parent groups indicate the current architecture, application, or resource area; exact child links identify the current page.
- Keyboard navigation, Escape, outside click, native disclosure, mobile expansion, and no-JavaScript access work.
- The header and open panels have no horizontal overflow at 320, 375, 768, 1024, and 1440 pixels.
- Source-fidelity, site-link, archive, and repository-link checks pass without canonical content changes.
