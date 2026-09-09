# Workspace relocation

9 September 2026 · AISG-013 · RM-01 · O3, O4

## Owner request

Extract the canonical AI Security & Governance package from its misplaced client directory, place it within the existing `ai-security` working area, preserve GitHub and website operation, and validate the move.

## Layout and boundary

Use the existing empty `ai-security/ref-architectures/` directory for this package's complete local workspace. Retain `publication/` as its independent Git repository and public deployment root. The surrounding `ai-security` repository remains a separate exploratory body of work. Directory proximity does not merge histories, import sources, or change the package's governing intent.

Preserve the complete workspace, including historical reviews, exported artifacts and local receipts. Only `publication/` is publishable. Keep its remote, branch, Git history and Vercel project association unchanged. Locally exclude the nested workspace from the surrounding repository to prevent accidental staging. A temporary compatibility symlink may retain old application and historical paths while all physical files live at the new location.

## Acceptance checks

- Capture a pre-move file/symlink inventory and hashes, Git HEAD/status/remotes, and the parent repository's existing state. Verify preservation immediately after the move, before subsequent documentation edits or builds.
- Verify that the original data directory is gone, the destination contains all files, Git resolves to the independent publication repository, and the parent repository's tracked and existing untracked work is unchanged.
- Audit active scripts/configuration for old absolute paths and check symlinks. Preserve frozen historical records; do not rewrite review evidence solely to change a path.
- Add local navigation instructions identifying the independent Git root. Record the layout and rationale in maintained project documentation, decisions, backlog, roadmap and status without changing architectural meaning or intent.
- Build and check from the new location in the isolated development VM. Validate source fidelity, relative links, release hashes and clean ZIP contents. Confirm architecture sources and exported PNG/PDF/PPTX bytes remain unchanged.
- Push the documentation/relocation record to the existing GitHub repository. Verify CI and Vercel deployment, anonymous route/download fidelity, and desktop/mobile browser behavior.

## Evidence and recovery

Keep detailed inventories and operational receipts outside the public repository. Publish a compact validation record without client paths or private runtime data. Preserve both repositories' histories and unrelated changes. A failed move must leave a recoverable complete tree; do not delete source data based only on a successful copy command.
