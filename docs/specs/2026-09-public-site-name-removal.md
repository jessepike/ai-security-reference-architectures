# Public-site organization-name removal

14 September 2026 · Owner-authorized scope

## Problem

The personal AI Security & Governance site and its public repository must not name or communicate a third-party organization. Earlier project records named a prospective downstream relationship. Those references are not part of the architecture explanation, but they are public source material and can be included in the site download package.

## Affected sources

The governing intent, decision log, purpose, roadmap, backlog, status, changelog, repository guidance, project guide, source map, downstream-use contract and downstream register contain the affected relationship. The generated site and portable ZIP must be rebuilt after the source edits. The architecture Markdown, PNGs, guides, PDFs and presentation have no matching organization-name references and do not need semantic or visual changes.

## Intended result

Retain the canonical package's ability to support future, traceable downstream adaptations while using neutral language throughout. Replace named prospective adaptations with general awareness, education and audience-specific adaptation descriptions. The change does not establish a new downstream program, offer, sponsorship, delivery commitment or external-use authority.

## Acceptance checks

1. A case-insensitive scan for the removed organization-name variants returns no matches outside Git history.
2. The source-bound project page and portable ZIP use the neutral downstream language.
3. The site build, source-to-site check and repository-link check pass.
4. The release manifest is regenerated after all tracked source changes.
