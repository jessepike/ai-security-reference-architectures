# Status

Updated 15 September 2026 · Current project snapshot

## Direction and release

The governing direction is [AISG-INTENT-001](intent.md): maintain the canonical AI Security & Governance package for orientation, education, future evolution and explicitly traced downstream adaptations. This is accepted owner direction. Version 1.1 and DEC-012 remove organization-specific downstream language from the personal site and public repository without establishing adoption, an offer, sponsorship or organizational approval.

The current production release is [`1f8970f046d4019ee25f26e52595c130fd74fae8`](https://github.com/jessepike/ai-security-reference-architectures/commit/1f8970f046d4019ee25f26e52595c130fd74fae8). It publishes the Applying Secure Business AI companion and [CISO walkthrough](https://ai.jessepike.dev/ciso-walkthrough) at [ai.jessepike.dev](https://ai.jessepike.dev). Repository CI, Vercel production deployment, and anonymous production browser and download checks passed. Exact source and export hashes are in [the release manifest](docs/release-manifest.json).

The five original PNGs, four original guide PDFs, and 44-slide presentation remain byte-identical to the prior release. The application companion adds its own map, guide exports, and walkthrough source and site views without adding a fourth architecture or changing the presentation.

## Current work

[AISG-018](BACKLOG.md#aisg-018--neutral-public-introduction) is complete under DEC-016. The README, purpose, and project guide now introduce the public, vendor-neutral resource directly. Scans found no unintended personal or ePlus branding in current public Markdown, SVG, PDF, or PowerPoint content; functional addresses and historical records remain. Architecture meaning and review state are unchanged.

[AISG-017](BACKLOG.md#aisg-017--primary-navigation-layout) is complete for local preview. The header now groups the three architecture views, Secure Business AI material, and project resources while retaining direct Overview and Governance links. Native disclosures keep every destination available without JavaScript. Build, source-fidelity, links, current states, keyboard behavior, outside-click closure, five responsive widths, overflow, and console checks pass. Preview deployment is pending; canonical content and review state are unchanged.

[AISG-016](BACKLOG.md#aisg-016--ciso-walkthrough-preview) is complete and published through release `1f8970f046d4019ee25f26e52595c130fd74fae8`. The walkthrough adds six meeting-friendly stops for the Stage 0 starter conversation and Stage 1 handoff, derived from one Markdown source with no answer collection. Source-fidelity, build, links, derived templates, internal implementation review, local browser, CI, protected-preview checks, and anonymous production checks pass. The walkthrough does not inherit the application companion's earlier external review. Human architectural review, reader testing, and field validation remain unassessed.

[AISG-015](BACKLOG.md#aisg-015--stage-0-ciso-starter-playbook-prototype) is a completed exploration prototype. Its selected Stage 0 and handoff material is published through the CISO walkthrough; later-stage playbooks remain future work, and publication is not field evidence.

[AISG-014](BACKLOG.md#aisg-014--applying-secure-business-ai-preview) is complete and published through release `1f8970f046d4019ee25f26e52595c130fd74fae8`. It adds the neutral application companion, map, detailed guide, and separate site routes. Its recorded review scope and remaining limits are unchanged.

PR 1 merged to `main` at `1f8970f046d4019ee25f26e52595c130fd74fae8` under DEC-015. Production verification passed for the application and walkthrough routes and downloads. The earlier protected-preview records remain evidence of the review path; they no longer describe the current publication state.

The package workspace has moved under `ai-security/ref-architectures/`, with its independent Git and deployment root retained at `publication/`. [AISG-013](BACKLOG.md#aisg-013--workspace-relocation-and-repository-separation) is complete: file preservation, independent Git-only build, links, GitHub CI, Vercel deployment and anonymous live checks passed. [Relocation validation](docs/validation-2026-09-workspace-relocation.md) records the results. [Workspace layout](docs/workspace-layout.md) documents the repository boundary and temporary compatibility link. Architectural content and exported artifact bytes are unchanged by this relocation.

The project-record alignment is complete in [AISG-003](BACKLOG.md#aisg-003--project-record-alignment), published in [`e183ccc`](https://github.com/jessepike/ai-security-reference-architectures/commit/e183ccc634b7ede9d0105fc0342676c3e7490cd6). The new [project guide](https://ai.jessepike.dev/project) passes local source and desktop/mobile browser checks. Anonymous verification of all 47 published files passed, including the portable ZIP contents. [AISG-010](BACKLOG.md#aisg-010--project-guide-website-exposure-check) records the completed exposure check. [Alignment validation](docs/validation-2026-09-project-alignment.md) records the trace audit, independent consistency review and publication checks.

The next proposed work is confidence and reader education: adjudicate the original review findings, obtain human architectural review, test the explanation with intended readers, field-test the walkthrough, and complete the separately supported writing cleanup.

The dated [development-roadmap snapshot](docs/roadmap/2026-09-15/development-roadmap.md) shows the established foundation, published application material, recommended confidence work, and later scoped use. It is a proposed visual interpretation of ROADMAP.md and does not commission the optional stage-specific playbooks it depicts.

## Material limits

The original component review has 30 findings, including two reviewer-labelled High findings on recovery authorization and execution identity in *Defend with AI*. These findings remain open. The bounded model-assisted review of the revised overview and governance companion did not close them; the presentation and website do not inherit that review. Human architectural review and reader testing are not assessed. See [review status](content/review-status.md).

The package is vendor-neutral and conceptual. It does not establish implementation effectiveness, compliance, organization-specific authority, product selection, service readiness or downstream adoption. The [intent](intent.md), [downstream-use contract](docs/downstream-use.md), [roadmap](ROADMAP.md) and [backlog](BACKLOG.md) are the current control map.

`content/` remains the maintained public source. Update source meaning before derived outputs, following [validation](docs/validation.md) and [release procedure](docs/releasing.md).
