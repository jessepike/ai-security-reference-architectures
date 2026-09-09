# Workspace and repository layout

The canonical AI Security & Governance package has its own Git history, governing intent, public repository and deployment. Its local workspace sits within `ai-security/ref-architectures/`; the surrounding exploratory repository remains independent.

```text
ai-security/                         surrounding exploratory repository
└── ref-architectures/                local package workspace
    ├── README.md, AGENTS.md          navigation to the maintained source
    ├── publication/                 independent Git repository; run Git/builds here
    │   ├── .git/                    existing public repository history
    │   ├── intent.md, ROADMAP.md, BACKLOG.md, status.md, decisions.md
    │   ├── content/, presentation/, public/
    │   └── scripts/, docs/
    ├── review/                      retained original review evidence
    └── output/, tmp/, original files  local artifacts and historical receipts
```

## Working in the correct repository

Open `ref-architectures/publication/` for Git and build work. Running Git from the wrapper directory can discover the surrounding exploratory repository instead. Confirm `git rev-parse --show-toplevel` before staging; its result must end in `ref-architectures/publication` for this package.

The surrounding repository locally excludes `/ref-architectures/` through its `.git/info/exclude`. It neither tracks this package nor imports its public authority. That local exclusion is not part of either repository's published content; maintain the same separation when arranging another checkout.

Read this package's [intent](../intent.md), [project instructions](../AGENTS.md) and [project guide](../content/project-guide.md). The directory move does not authorize importing surrounding research or changing the source boundary. Historical originals stay intact; they are not a competing maintained canon.

## GitHub and Vercel

The remote remains [jessepike/ai-security-reference-architectures](https://github.com/jessepike/ai-security-reference-architectures). Vercel builds that repository's `main` branch and publishes `dist/` at [ai.jessepike.dev](https://ai.jessepike.dev). It does not build the surrounding exploratory repository or use the local wrapper as a deployment root. A fresh clone of the public repository is itself the build root and does not need a `publication/` subdirectory.

Scripts resolve their paths from their own source locations. Run `npm ci`, `npm run check` and `python3 scripts/check-repo-links.py` in an isolated development environment from the public Git root. PDF and presentation production retain their existing source-relative paths and documented dependencies.

## Compatibility and recovery

The old local workspace address is temporarily a symlink to the new physical workspace, preserving this open task and historical local references. It holds no second data copy. New work should use the new location. Remove the compatibility link only after affected open tasks, bookmarks and external local consumers have moved; do not confuse removing the link with deleting its target.

Detailed before/after inventories and relocation receipts remain outside the public repository. The [relocation validation](validation-2026-09-workspace-relocation.md) records the public verification scope. [DEC-011](../decisions.md) records the rationale, and AISG-013 in the [backlog](../BACKLOG.md) tracks completion.
