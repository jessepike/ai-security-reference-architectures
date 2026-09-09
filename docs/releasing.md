# Releasing

The public site is hosted on Vercel at [ai.jessepike.dev](https://ai.jessepike.dev). Its GitHub integration builds the production `main` branch from this repository. Treat a push to `main` as publication.

1. Confirm the authorized scope against [intent](../intent.md), the relevant [roadmap](../ROADMAP.md) area and [backlog](../BACKLOG.md) item, and read the latest decisions/status. Use a branch for work that is not yet ready to publish.
2. Update canonical text before dependent artifacts. Retain historical review scope; do not overwrite critique receipts or claim new content inherited an older review.
3. Complete [validation](validation.md), update `CHANGELOG.md`, `status.md`, `BACKLOG.md` and any affected decision entries. Record artifact hashes and review limits. Update roadmap state only when supported by the evidence. Use the [downstream register](downstream-register.md) to identify adaptations needing review after a source change.
4. Inspect the staged file list. Exclude `.env*`, `.vercel/`, operational receipts, temporary files and unrelated material. Check the generated public ZIP separately.
5. Commit coherent units and publish within the owner's current authorization. GitHub CI builds/checks the site; Vercel deploys `main`. Inspect the actual deployment result rather than assuming a push succeeded.
6. Verify the public custom domain and downloads anonymously. Record the released commit and artifact hashes in the handoff. Confirm the working tree is clean.

Run `python3 scripts/release-manifest.py` after the final source and project-record updates, including a documentation-only release-record commit. The manifest includes intent, roadmap, backlog and status as well as content and exported artifacts, so an updated status file needs a refreshed manifest too. The manifest does not hash itself.

## Recovery

If a release breaks the site, inspect the cause and use Vercel's previous known-good deployment or a reviewed revert commit as appropriate. Avoid rewriting shared Git history. Restoring the site does not settle content-review findings.

## Artifact sources

`content/` holds public canonical meaning and guides. `public/images/` and `public/downloads/` hold inspected exports. `presentation/` holds the editable deck source and manuscript. `scripts/` holds site/PDF production and validation. `dist/` is generated and ignored. Build presentation/PDF artifacts in an isolated environment using their documented dependencies.

For PDF generation, install `requirements-render.txt` inside the isolated environment and provide the DejaVu Sans fonts expected by `scripts/render-guides.py`. Run `python3 scripts/render-guides.py --all`, or use `--guide` to regenerate only an affected guide. The website build consumes the inspected PDF/PPTX exports; it does not silently rebuild them. Presentation-specific dependencies and commands are documented in `presentation/README.md`.
