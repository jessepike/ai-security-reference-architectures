# Development roadmap visual brief

## Purpose

Show the development path for the AI Security Reference Architectures publication as of 15 September 2026. The visual must help a reader see what is live, what should happen next, and what remains future work.

## Story and status

1. The reference foundation is established and live.
2. The Applying Secure Business AI companion and CISO walkthrough are live.
3. Confidence and reader learning are the recommended next workstream.
4. A scoped real-workflow exploration and authorized downstream adaptations follow later.

An optional strip may show additional stage-specific playbooks as a proposal from discussion. It must not imply that these playbooks are commissioned or part of the maintained backlog.

## Visual contract

- Canvas: 1920 × 1080, 16:9.
- Format: editable SVG plus PNG derived from the SVG.
- Style: publication navy, teal, white and pale blue-gray.
- Main flow: four left-to-right workstream cards. Arrows show recommended order, not technical dependency.
- Status must be visible in words. Dates appear only in the snapshot line.
- Copy must remain sparse and readable at presentation size.
- A visible note must distinguish roadmap workstreams from the six project stages in the application companion.
- Source references belong in a small footer.

## Reproduction

Run `python3 render.py` from this directory inside the repository's OrbStack `dev` VM. The script writes `development-roadmap.svg` beside itself. Rasterize that SVG to the dated PNG in the same isolated environment; do not install a Python runtime or rendering package on the host.
