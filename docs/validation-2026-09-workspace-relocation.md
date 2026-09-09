# Workspace relocation validation

9 September 2026 · AISG-013 · Repository and deployment continuity

## Preservation

The complete local workspace moved into `ai-security/ref-architectures/`. Its independent public Git repository remains at `publication/`. The before/after inventories match for all 3,145 regular files and five symlinks, including file modes and hashes. The 478-directory inventory differs only in the expected root path label; child directories and modes match. Comparisons were completed before subsequent documentation edits and rebuilds.

The public repository retained HEAD `529515cfe7a4daffd8594fb6a01604b43637690a`, its `main` branch, remote and working state at the move boundary. `git fsck --full` passed from the new location. The surrounding exploratory repository's HEAD and existing work state are unchanged. A local ignore entry prevents accidental staging of this package into that repository.

The old workspace address is a compatibility symlink; the files physically reside at the destination. The wrapper's local agent instructions and README identify `publication/` as the independent Git/build root. Historical records remain intact and are not imported into the public source tree.

## Public continuity

The existing public GitHub repository and Vercel project remain in place. GitHub's default branch is `main`; the homepage remains `https://ai.jessepike.dev`. Vercel reports the same project and custom domain. No repository rename, DNS change, protection change or new public exposure is required for the disk move.

## Validation scope

A clean dependency install and build from the new location passed: all 17 source-bound pages/articles, 196 repository-relative links and archive link checks. All 45 release-manifest entries match their declared hashes and the 64-member portable ZIP. Active public scripts/configuration contain no old client-path references. The presentation scratch dependency symlink resolves in its intended development VM; its VM path is not meaningful on the host. Final independent-checkout and deployment checks follow the [relocation specification](specs/2026-09-workspace-relocation.md). Architecture sources and PNG/PDF/PPTX exports are unchanged by the relocation and documentation work. The [workspace layout](workspace-layout.md) describes the maintained arrangement.

Detailed inventories and operational receipts remain local outside the public repository. This work establishes relocation and publication continuity; it does not close architecture-review findings, establish external-writing cleanup, or assess implementation effectiveness.
