# Editorial clarity pass

Date: 15 September 2026  
Status: Approved implementation scope

## Purpose

Apply the owner-approved wording changes from the 15 September foundation editorial review. The changes make the public explanation more direct while preserving the architecture, authority model, risk constraints, evidence requirements, and recorded review status.

## Scope

- Revise the overview introduction, shared governance and security statement, starting guidance, and shared-control explanation.
- Simplify introductory scope language in Defend Against AI, Defend With AI, and AI Governance, including matching guide wording.
- Clarify three abstract passages in the CISO walkthrough without changing its progressive safeguards.
- Keep the homepage, authoring standard, source checks, and generated guide labels aligned with the canonical Markdown.
- Regenerate only affected public images, PDFs, and presentation files from their maintained sources.

## Constraints

- Do not change the three-view architecture, add claims, alter decision authority, or weaken conditions on data access, actions, or expansion.
- Preserve the distinction between editorial review, architecture review, field validation, and publication authority.
- Keep generated artifacts synchronized with their canonical sources and verify the published wording after rendering.

## Validation

- Run the publication checks and repository-link checks in the OrbStack dev VM.
- Scan tracked source and generated text for superseded phrases.
- Inspect each regenerated visual page or slide and record the exact files and hashes.
