# Presentation sources

The PowerPoint is an editable teaching sequence built from the architecture and guide Markdown in `../content/`. `slide-plan.md` maps that sequence to its sources. `build-deck.mjs` contains the slide copy and editable layout instructions; `finalize-deck.mjs` validates the exported package. `generate-manuscript.py` regenerates the human-readable `manuscript.md` from the candidate PPTX.

Make architecture changes in the canonical sources first, then reconcile the presentation copy. The manuscript is a derived review artifact, not a second authoring source. Preserve source references in speaker notes and the distinction between proposed design, review findings and deployment evidence.

## Build environment

The deck renderer requires an available `@oai/artifact-tool` runtime and the associated presentation-skill finalization helpers. It is separate from the website's npm dependencies. Use an isolated build environment with native dependencies compatible with that environment; keep generated previews and validation receipts outside public downloads.

The authoring scripts accept absolute environment paths for `RUNTIME_NODE_MODULES`, `SKILL_DIR` and `WORKSPACE_DIR`. The finalizer also requires `RUNTIME_PYTHON`. `PUBLICATION_DIR` may identify this repository explicitly when supported by the builder. See each script for its current invocation contract. Those paths are environment configuration and are not stored in the presentation or published source.

The five PNG architecture views are source images, so their internal text is not editable in PowerPoint. The other teaching diagrams, headings and body text use native editable presentation elements. Each PNG also has an accessible Markdown visual contract. The governance view is a companion architecture that connects to, rather than extends, the three peer AI-security views.

The rendered deck is a review draft. Its creation and structural validation do not imply independent review, PowerPoint-native testing or deployment approval.
