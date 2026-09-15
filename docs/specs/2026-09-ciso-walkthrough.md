# CISO walkthrough preview specification

**Status:** Authorized implementation for protected preview; content acceptance and production publication remain pending  
**Work:** AISG-016 · RM-05 · O1, O2, O3  
**Date:** 15 September 2026

## Problem

The application map and detailed guide show the complete Secure Business AI journey, while the Stage 0 starter playbook gives a CISO a practical first conversation. A meeting needs a lighter interface that connects those pieces without turning the questionnaire into an application or presenting the six conversation stops as a replacement lifecycle.

## Scope

Build a separate `/ciso-walkthrough` route from `content/ciso-walkthrough.md`. The route guides a presenter through six conversation stops: the approach, the full journey, the starter conversation, the initial risk view, bounded experiment guidance, and the Stage 1 handoff with the later journey. Add a prominent home entry and relevant links from the application companion and its guide.

The walkthrough is a proposed Stage 0 and handoff display. The existing six-stage application guide remains the complete journey reference. The three security architectures and governance companion remain unchanged. The route does not collect, store, or transmit answers.

## Source and rendering contract

- `content/ciso-walkthrough.md` is the only maintained source for the walkthrough's meaning.
- Its six H2 sections are the six presentation stops. Existing H2, H3, paragraph, list, and table text must remain in one source-bound article so the fidelity check can compare the page with the canonical Markdown.
- Presenter controls sit outside the source-bound article and do not repeat source claims.
- Copy actions read the visible canonical template text from the page. Derived Markdown downloads are generated during the build from the same source sections and are not maintained copies.
- Without JavaScript, all six sections remain visible in source order. JavaScript may progressively present one stop at a time, preserve direct hashes and browser history, and expose every stop when printing.

## Design plan

The page uses the site's existing identity and typography. The compact token set is ink `#092a43`, deep ink `#061d30`, teal `#007c73`, pale teal `#e6f5f1`, mist `#f4f8fa`, line `#cedae0`, Manrope for interface text, Source Serif 4 for explanatory prose, and DM Mono only for small sequence markers.

The layout is a meeting canvas: a narrow six-stop rail on the left and one large conversation surface on the right. The memorable element is a vertical teal journey line that makes the presenter's position clear while keeping the content quiet and readable.

```text
desktop                              mobile
┌────────────┬───────────────────┐   ┌─────────────────────┐
│ 1 2 3 4 5 6│ current stop      │   │ progress + stop menu│
│ journey    │ main conversation │   ├─────────────────────┤
│ position   │ optional details  │   │ current conversation│
│            │ back / next       │   │ details + back/next │
└────────────┴───────────────────┘   └─────────────────────┘
```

Content stays left aligned, with short line lengths and a clear presenter hierarchy. Native disclosure controls hold supporting examples and detail. The design avoids a dashboard grid because this is a guided conversation, and it avoids adding the walkthrough to the already dense global navigation; the home entry is its primary front door.

## Interaction and accessibility

- Provide labelled previous and next controls, a six-stop navigator, and visible progress.
- On direct hash navigation, show and focus the requested stop. Browser back and forward follow hash history.
- Keep focus rings strong, targets large enough for meeting use, and status updates available to assistive technology.
- Respect `prefers-reduced-motion`; do not autoplay or advance on a timer.
- Keep native disclosures keyboard operable and expose all content for no-JavaScript and print use.
- Copy controls report success or failure without sending content elsewhere.

## Acceptance checks

- The route renders all six canonical sections, has exactly one source-bound article, and appears in `dist/fidelity-manifest.json`.
- No-JavaScript output contains the complete source. Enhanced navigation, direct hashes, back/forward behavior, copy actions, keyboard focus, reduced motion, mobile layout, and print behavior work.
- Home, application companion, and detailed guide links resolve; existing guide, map, PDFs, architectures, governance, and presentation remain unchanged.
- `npm run check`, repository-link validation, release-manifest refresh, and local desktop/mobile browser checks pass in the OrbStack development VM.
- Records state preview-only authority and do not imply inherited external review, content acceptance, production publication, or an intent change.
