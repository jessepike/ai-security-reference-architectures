# AI Security Reference Architectures

**Review draft · September 2026**

**Read the website: [ai.jessepike.dev](https://ai.jessepike.dev)**

![AI Security overview](public/images/00-ai-security.png)

AI changes what we protect, how we are attacked, and how we defend. This library explains three connected views:

1. **Secure business AI** — what may an AI workflow access and do?
2. **Defend against AI** — how do we interrupt AI-enabled attacks?
3. **Defend with AI** — how can AI help security act within limits?

Begin with the [AI Security overview](content/00-ai-security.md), then explore the [architect guides](content/guide-index.md). Images and presentation downloads accompany the browser-readable website.

## Review status

The three component architectures received model-assisted critique with material reservations. The overview and presentation are subsequent additions. These are conceptual proposals, not a deployed design or a certification. Read the [open design questions](content/review-status.md) before implementation.

## Feedback

Email **[jesse@jessepike.dev](mailto:jesse@jessepike.dev?subject=AI%20Security%20Reference%20Architectures%20feedback)** with the architecture or section and your comment. A GitHub account is not needed to read the website or send email. GitHub contributors may open an issue.

## Authoring and maintenance

The [source map](content/source-map.md), [authoring standard](content/authoring-standard.md) and [template](content/templates/reference-architecture.md) support consistent work by people and agents. The site renders from Markdown in `content/`. Presentation sources live in `presentation/`. Public images and downloadable artifacts live in `public/`.

Build the static site with `npm ci` followed by `npm run build`. Vercel publishes `dist/`. Local development and artifact builds use an isolated development environment.

No reuse license has been selected for this initial publication. Contact the author about redistribution or adaptation beyond the permissions provided by the hosting platform.
