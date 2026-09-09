# Governance-and-orientation validation

9 September 2026 · Review draft

## Content and source fidelity

The revision implements the scoped orientation/governance recommendations and repository scaffold. Sixteen website pages have exactly one source-bound canonical article. Checks compare source hashes and independently parsed paragraph, table-cell, list-item and heading text with the rendered article, preserve heading targets, and detect an intentionally changed article body. Local routes, fragments and downloads pass. Direct Markdown file links are checked separately for GitHub/ZIP portability.

A separate reviewing agent assessed the revised overview and governance canonical source, guide, PNG and all 11 PDF pages. No blocking content or visual defect was identified. Its scope and reader-testing advisory are in [the governance review](reviews/governance-v0.1.md). This result does not close the original security findings or constitute human acceptance.

## PNG and PDF

The governance PNG is 1672 × 941 pixels. Its six boxes, questions, handoffs, feedback, shared bands, security interface and labels were inspected against the visual contract. One correction added the missing Operation and reassessment feedback connection. See [visual provenance](governance-visual-provenance.md).

The governance PDF has 11 pages. Text coverage was 100% under the source-text comparison. Page numbering, public link destinations and absence of private paths passed. Every page was visually reviewed. After the review-status paragraph was updated, the PDF was regenerated and the affected final page inspected again. Existing three security PDFs retain their previously inspected content and valid public link destinations.

## Presentation

The expanded deck has 44 slides and speaker-note parts. Package, layout, font/import and overflow checks pass; final rendered slides and the contact sheet were inspected. Five architecture PNGs remain raster images inside the otherwise editable teaching presentation. PowerPoint-native inspection was not performed. The release manifest records the final saved PPTX hash.

## Browser and deployment scope

Before publication, the governance page and guide were inspected in Chromium desktop and a 390 × 844 mobile viewport. The homepage summary is a complete paragraph, document titles are rendered once, and the governance image appears once. Root screenshot review identified inline image overflow; the image selector was corrected to include nested Markdown images and an accessible full-size image button was added. All 16 routes passed full-document and body width checks at both 1440 × 1000 and 390 × 844 (32 route/viewport combinations, zero overflow failures). Clicking the governance image opened its full-size dialog. The corrected screenshots were inspected. Desktop Chromium emulation does not establish native iOS Safari behavior.

GitHub CI runs isolated site and repository link checks. Public release verification must check the custom domain anonymously and compare page/article content and download bytes with the inspected build. ZIP member contents are compared separately from archive timestamps. Browser/source-fidelity checks do not establish completeness of every architecture claim, accessibility conformance, control effectiveness or compliance.

Current source and artifact hashes: [release manifest](release-manifest.json). Original review scope and unresolved questions: [review status](../content/review-status.md).

## Published revision

Content revision `08ae83d78e99f97e15239742c7e8c39c92d201ef` was pushed to public GitHub `main`. [GitHub CI](https://github.com/jessepike/ai-security-reference-architectures/actions/runs/34393563920) and [Vercel deployment](https://vercel.com/pikeholdings/ai-security-reference-architectures/EKXp81s2vnebvCiZf8VbBbf2d4gw) completed successfully on 9 September 2026. Anonymous HTTPS checks against `ai.jessepike.dev` verified all 46 published files: HTTP 200 throughout, every HTML and non-ZIP file byte-identical to the inspected local build, and all 27 ZIP member contents identical. Archive timestamps were deliberately excluded from ZIP equivalence. These checks include the final 44-slide presentation and governance PNG/Markdown/guide/PDF.

A fresh unauthenticated Chromium context then checked the live home, governance, governance-guide and decisions routes at 1440 × 1000 and 390 × 844. All eight route/viewport combinations returned HTTP 200, had one H1 and a source-bound canonical article, and had no horizontal overflow. The governance image opened its full-size dialog. No defect was found within this live browser scope.
