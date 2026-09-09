# Canonical package alignment validation

9 September 2026 · Project-record and navigation revision

## Scope

The revision records the owner's vision in AISG-INTENT-001 v1.0 and DEC-010 and connects it to purpose, roadmap, backlog, status, decisions, source mapping, authoring and downstream use. The [specification](specs/2026-09-project-alignment.md) defines the work. The existing architecture Markdown, five PNGs, four detailed guide Markdown/PDFs and 44-slide presentation are unchanged, confirmed against Git.

## Traceability

The backlog has 12 stable work IDs mapped to four roadmap areas and intent outcomes O1–O4. Each work ID appears once in the roadmap and has a valid roadmap/outcome trace. Fifteen relative heading links among the project records resolve to their target headings. The original unresolved work remains present, including the 30 original findings and two High findings, human review, reader testing, environment selection, external-writing cleanup and licensing.

The intended ePlus AI Ignite and GTM uses have register entries with unselected receiving owners, source versions and artifact scopes explicitly marked. The downstream-use contract records how source versions inform adaptations and how learning returns through exploration, backlog and decisions. No adoption, commercial offer or enterprise authority is claimed.

## Independent consistency review

A separate reviewing agent read the project records as a continuation packet. It found no consequential gap in identifying purpose, outcomes, authority, current state, proposed future work, source versions or the exploration/adaptation feedback path. It confirmed that owner-stated direction is distinct from proposed evaluation criteria and roadmap ordering, and that the intended ePlus relationship does not assert adoption or commercial authority. This was a bounded model-assisted review of record coherence, not review of a future adaptation or human architectural acceptance.

## Website and publication checks

The project guide renders as a source-bound seventeenth page at `/project`, reached through the footer. Its canonical links point to the maintained records; it does not duplicate their state lists. The website review callout now defers version-specific coverage to the canonical review record.

Local site checks passed for 17 pages/articles. Chromium checks of the home and project pages at desktop 1440 × 1000 and mobile 390 × 844 found no document/body overflow. The footer project link, decision-log route and source-map route resolved, and the guide contains links to the public GitHub project records. The final desktop and mobile project screenshots and record table were visually inspected.

The portable ZIP now includes the explicitly selected public root project records, public Markdown/JSON/TXT documentation and presentation source files alongside the existing canonical text and exported artifacts. A relative-link check inside the archive passes. This keeps the intent, roadmap, status, backlog and decision links usable together offline without adding credentials, local runtime receipts or unrelated material. The release manifest records the current project-record hashes alongside content and artifact hashes.

Final local checks passed for 180 repository-relative file links and all 17 source-bound website articles. The archive contains 61 unique members. All 44 manifest entries are present in the archive and match their local source bytes and declared SHA-256 hashes. The presentation retains SHA-256 `e7e490f7c0362733244cc7e0c98b856c380b5aa5944d19f9c579cf5ff3543af3`.

## Published release

Project-record release [`e183ccc634b7ede9d0105fc0342676c3e7490cd6`](https://github.com/jessepike/ai-security-reference-architectures/commit/e183ccc634b7ede9d0105fc0342676c3e7490cd6) was pushed to GitHub. [CI run 34397618574](https://github.com/jessepike/ai-security-reference-architectures/actions/runs/34397618574) passed and Vercel reported deployment complete. Anonymous verification at `https://ai.jessepike.dev` returned HTTP 200 for all 47 built files with matching contents, comparing the ZIP by its uncompressed members. This includes `/project` and the published project records in the ZIP. AISG-010 is complete.

Live anonymous Chromium checks also passed at desktop 1440px and mobile 390px: `/project` has the canonical source binding, one main title and no horizontal overflow. The home footer reaches the guide, the decision log resolves its intent/roadmap links, and public GitHub intent, roadmap, backlog and status pages return HTTP 200 without a login form. Live desktop/mobile screenshots were retained in the local validation receipts.

## Limits

This is a check of project coherence, traceability and observed publication behavior. It is not new review of the architecture designs or exported presentation. The proposed evaluation criteria and roadmap ordering are distinguishable from the accepted owner direction. Human review and outcome evidence retain their documented status.
