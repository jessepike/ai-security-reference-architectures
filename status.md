# Status

Updated 9 September 2026 · Current project snapshot

## Direction and release

The governing direction is [AISG-INTENT-001](intent.md): maintain the canonical AI Security & Governance package for orientation, education, future evolution and explicitly traced downstream adaptations. This is accepted owner direction. It records intended ePlus AI Ignite and AI Security & Governance GTM use without establishing adoption, an offer, sponsorship or enterprise approval.

The current integrated-story content release is [`54a2036ff85a89a0684cd834e7d77a849a3b5376`](https://github.com/jessepike/ai-security-reference-architectures/commit/54a2036ff85a89a0684cd834e7d77a849a3b5376). It is published at [ai.jessepike.dev](https://ai.jessepike.dev); CI, deployment and anonymous content verification passed. Exact source and export hashes are in [the release manifest](docs/release-manifest.json).

This release has five PNGs, four detailed guides and a 44-slide presentation with speaker notes. They are immutable for this project-record revision; the alignment work changes control records and navigation material, not those artifacts.

## Current work

The package workspace has moved under `ai-security/ref-architectures/`, with its independent Git and deployment root retained at `publication/`. [AISG-013](BACKLOG.md#aisg-013--workspace-relocation-and-repository-separation) is complete: file preservation, independent Git-only build, links, GitHub CI, Vercel deployment and anonymous live checks passed. [Relocation validation](docs/validation-2026-09-workspace-relocation.md) records the results. [Workspace layout](docs/workspace-layout.md) documents the repository boundary and temporary compatibility link. Architectural content and exported artifact bytes are unchanged by this relocation.

The project-record alignment is complete in [AISG-003](BACKLOG.md#aisg-003--project-record-alignment), published in [`e183ccc`](https://github.com/jessepike/ai-security-reference-architectures/commit/e183ccc634b7ede9d0105fc0342676c3e7490cd6). The new [project guide](https://ai.jessepike.dev/project) passes local source and desktop/mobile browser checks. Anonymous verification of all 47 published files passed, including the portable ZIP contents. [AISG-010](BACKLOG.md#aisg-010--project-guide-website-exposure-check) records the completed exposure check. [Alignment validation](docs/validation-2026-09-project-alignment.md) records the trace audit, independent consistency review and publication checks.

Next proposed work is confidence and reader education: adjudicate the original review findings, obtain human architectural review, test the explanation with intended readers, and complete the separately supported writing cleanup. Future exploration and downstream adaptation remain uncommissioned directional work in the [roadmap](ROADMAP.md).

## Material limits

The original component review has 30 findings, including two reviewer-labelled High findings on recovery authorization and execution identity in *Defend with AI*. These findings remain open. The bounded model-assisted review of the revised overview and governance companion did not close them; the presentation and website do not inherit that review. Human architectural review and reader testing are not assessed. See [review status](content/review-status.md).

The package is vendor-neutral and conceptual. It does not establish implementation effectiveness, compliance, organization-specific authority, product selection, service readiness or downstream adoption. The [intent](intent.md), [downstream-use contract](docs/downstream-use.md), [roadmap](ROADMAP.md) and [backlog](BACKLOG.md) are the current control map.

`content/` remains the maintained public source. Update source meaning before derived outputs, following [validation](docs/validation.md) and [release procedure](docs/releasing.md).
