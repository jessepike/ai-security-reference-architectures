# Status

Updated 9 September 2026 · Review draft

## Current release

Public website: [ai.jessepike.dev](https://ai.jessepike.dev). GitHub `main` is connected to Vercel. The initial publication was commit `67b0e4cc839896fd019318575de5a018039483ee`; the current governance-and-orientation revision adds a governance companion to the three security views, for five PNGs, four detailed guides and a 44-slide presentation with speaker notes. Exact source/export hashes are in [the release manifest](docs/release-manifest.json).

## Governance and orientation revision

The owner accepted the orientation/governance recommendations and requested repository scaffolding. The revised introduction, governance canonical/PNG/guide, presentation, website fixes and project records implement [the scoped change specification](docs/specs/2026-09-governance-and-orientation.md). [The decision log](decisions.md) records the accepted direction. Sixteen website pages have complete canonical-article fidelity checks; direct repository links are checked separately. The governance guide is 11 pages, and a separate reviewing agent inspected every page without finding a blocking issue.

## Review boundary

The original three packages received model-assisted critique with material reservations. Mechanical corrections and publication do not close substantive findings. The revised overview and governance package received a separate bounded model-assisted review with no blocking findings; human review and reader testing remain open. The updated presentation does not inherit either review. See [review status](content/review-status.md) and [governance review](docs/reviews/governance-v0.1.md).

## Maintenance

The governance-and-orientation revision was pushed as `08ae83d78e99f97e15239742c7e8c39c92d201ef`. GitHub CI and the Vercel deployment completed successfully. Anonymous verification of all 46 published files passed: every response was HTTP 200, all HTML and non-ZIP bytes matched the inspected build, and all ZIP member contents matched. See [release validation](docs/validation-2026-09-governance.md).

`content/` is the maintained public source. Update source meaning before derived outputs, and follow [validation](docs/validation.md) and [release procedure](docs/releasing.md). Current work and open questions are in [BACKLOG.md](BACKLOG.md).
