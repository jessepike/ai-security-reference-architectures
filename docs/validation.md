# Validation

Use four separate kinds of evidence. Do not report a check in one category as proof of another.

| Check | What it establishes | What it does not establish |
|---|---|---|
| Source-to-output fidelity | Canonical text, tables, labels and links survive rendering. | That the source claims are correct or complete. |
| Browser and document presentation | Tested pages, images, PDFs and slides are readable and usable. | Full accessibility conformance or architectural effectiveness. |
| Architecture and source review | A reviewer assessed specified claims, boundaries, responsibilities and failure cases against named evidence. | Owner acceptance or effectiveness in a deployed environment. |
| Deployment verification | Public pages and downloads are reachable and match inspected artifacts. | Completion of substantive review findings. |

## Website

Build in an isolated environment with `npm ci` and `npm run build`. Run `python3 scripts/check-site.py`. Check every public page's complete canonical article body, including lists/tables and links. Preserve source heading fragment targets when rendering a heading in the page hero. Check navigation, local fragments, downloads and unexpected private markers.

Use a real browser for desktop and mobile checks. Record exact routes and viewport sizes. Check the overview, each new/changed document, image expansion, menu interaction, readable tables and complete introductory sentences. State sampling limits; an HTTP request is not a browser inspection.

Run `python3 scripts/check-repo-links.py` too. Website link rewriting can hide incorrect Markdown paths that fail when the source is read directly on GitHub or from the ZIP.

## Artifacts

- PNG: inspect every visible label, grouping, connector direction and authority implication against the canonical visual contract. Save the prompt and output hash.
- PDF: compare text coverage, links and numbering; render and inspect every affected page. Text extraction alone cannot assess image-only pages or layout.
- PPTX: run package/layout checks and render the final saved file. Inspect every changed slide and the full final deck; verify notes and final file hash. State if PowerPoint-native inspection was not performed.

## Architecture review

Check purpose/scope, ownership, trust boundaries, data and authority, failure behavior, recovery, third-party limitations and verification evidence. Use the guide's stated acceptance scenarios. Challenge unjustified claims of completeness, autonomy or effectiveness. Record findings and their disposition rather than silently rewriting source authority.

## Public deployment

Check the custom domain without authentication. Verify all routes and downloads. Compare asset hashes and ZIP member bytes with the inspected local build; archive timestamps may differ across builds. Retain a compact public validation receipt with exact scope, results, versions and limitations. Keep operational logs and credentials outside the repository.
