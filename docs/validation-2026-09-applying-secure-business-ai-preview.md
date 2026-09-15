# Applying Secure Business AI preview validation

## Scope

This record covers the proposed neutral application companion on `codex/applying-secure-business-ai-preview`. It validates source-to-site fidelity, local publication integrity, new PNG/PDF rendering, and preservation of previously released binary artifacts. It does not establish content acceptance, human review, reader comprehension, field validity, control effectiveness, compliance, production publication, or authority for a particular use.

## Source and artifact checks

- The site builder binds `/applying-secure-business-ai` to `content/applying-secure-business-ai.md` and `/guides/applying-secure-business-ai-guide` to its canonical guide Markdown.
- The renderer consumes those Markdown sources and produced a 1920 × 1080 overview PNG, a one-page overview PDF, and a ten-page detailed guide PDF.
- Every guide page and the overview PDF were rendered to PNG. An initial contact-sheet pass missed an incomplete outcome-chain banner and a final-page overflow; both were corrected. All ten corrected pages were then inspected at full size, with focused reinspection of pages 1 and 10. No clipping, overlap, broken glyph, or unreadable matrix text remained. The matrix uses 9-point body text.
- The five previously released PNGs, four guide PDFs, and 44-slide presentation were checked against the prior release manifest. All ten binary files remain byte-identical.
- Text scans of the new public sources, renderer, site output, and extracted PDF text found no private machine path, raw prompt, internal review identifier, credential marker, or private-source status wording.

## Local publication checks

`npm run check` passed in the OrbStack `dev` VM after the source and artifacts were integrated:

- 19 HTML pages found;
- 19 pages bound to canonical Markdown in the fidelity manifest;
- no missing local links or fragments;
- no source-to-render semantic mismatch;
- no public archive error;
- no private marker found by the site validator.

The release manifest was refreshed after the final review and project-record updates and records 51 source and artifact hashes. Temporary render and QA files remain under ignored `tmp/` paths and are excluded from the public archive.

## Browser checks

Read-only browser QA passed against the built `dist/` site at desktop and mobile sizes. The home, application companion, detailed application guide, Secure Business AI, and governance routes loaded without horizontal overflow or console errors. The image modal opened and closed by pointer and keyboard. The overview PNG, both PDFs, and both Markdown downloads returned HTTP 200 and contained their expected markers. Raw screenshots and browser receipts remain in the private wrapper outside this repository.

## Review and publication state

Across three external model-assisted review passes, the original eight High corrections and the second-pass map identity and interpretation correction were verified. The third pass found one High source-attribution ambiguity; its factual label was corrected and locally verified in the source and rendered page after the panel, without a fourth external pass. The final local browser recheck passes.

## Preview deployment

Commit `bc74095c3fe9c3aa7a5765a90be1bebb4a77c022` deployed successfully to the protected [Vercel preview](https://ai-security-reference-architectures-16anezt5g-pikeholdings.vercel.app). GitHub CI validation and the Vercel deployment passed. The [draft pull request](https://github.com/jessepike/ai-security-reference-architectures/pull/1) remains open for review.

Live browser QA returned HTTP 200 for five key routes at desktop and mobile sizes, with no document overflow or console errors. Image-modal pointer and keyboard behavior passed. The overview PNG, overview PDF, detailed-guide PDF, application Markdown, and detailed-guide Markdown matched the corresponding local SHA-256 hashes. Raw browser receipts remain in the private wrapper outside this repository.

The preview retains Vercel sign-in protection. No bypass or share token is recorded here. Production remains unchanged on `main` at `d01d962517ab79458e8627456973071c40aa0954`. Content acceptance, merger to `main`, and production publication remain pending.
