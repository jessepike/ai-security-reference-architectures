# Contributing

Start with the [website](https://ai.jessepike.dev), [source map](content/source-map.md) and [authoring standard](content/authoring-standard.md). For a content question, name the architecture, heading or diagram box and explain what is unclear, missing or incorrect. Include a primary source or a concrete failure scenario where useful.

Email [jesse@jessepike.dev](mailto:jesse@jessepike.dev?subject=AI%20Security%20Reference%20Architectures%20feedback) for account-free feedback. GitHub users can open an issue or pull request. Do not include credentials or confidential customer information.

## Content changes

Edit the canonical Markdown first. Explain the proposed decision, rationale and limits. Update affected guide, image and presentation outputs together. A source citation should support the associated claim; a framework name alone is not evidence. Preserve the distinction between established source statements and this project's proposed synthesis.

## Website changes

Use an isolated development environment with Node.js 22 and Python 3. Run `npm ci`, `npm run build`, then `python3 scripts/check-site.py`. Follow [validation](docs/validation.md) for content and visual checks. Do not add telemetry, external services or dependencies without a task requirement.

## Reviews and releases

Report the exact artifacts and versions reviewed. Separate technical findings from presentation defects, and record unresolved issues. See [release procedure](docs/releasing.md). No reuse license has been selected; contact the maintainer about redistribution or adaptation beyond hosting-platform permissions.
