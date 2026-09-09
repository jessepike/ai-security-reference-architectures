# Workspace relocation validation

9 September 2026 · AISG-013 · Repository and deployment continuity

## Preservation

The complete local workspace moved into `ai-security/ref-architectures/`. Its independent public Git repository remains at `publication/`. The before/after inventories match for all 3,145 regular files and five symlinks, including file modes and hashes. The 478-directory inventory differs only in the expected root path label; child directories and modes match. Comparisons were completed before subsequent documentation edits and rebuilds.

The public repository retained HEAD `529515cfe7a4daffd8594fb6a01604b43637690a`, its `main` branch, remote and working state at the move boundary. `git fsck --full` passed from the new location. The surrounding exploratory repository's HEAD and existing work state are unchanged. A local ignore entry prevents accidental staging of this package into that repository.

The old workspace address is a compatibility symlink; the files physically reside at the destination. The wrapper's local agent instructions and README identify `publication/` as the independent Git/build root. Historical records remain intact and are not imported into the public source tree.

## Public continuity

The existing public GitHub repository and Vercel project remain in place. GitHub's default branch is `main`; the homepage remains `https://ai.jessepike.dev`. Vercel reports the same project and custom domain. No repository rename, DNS change, protection change or new public exposure is required for the disk move.

## Validation scope

A clean dependency install and build from the new location passed: all 17 source-bound pages/articles, 196 repository-relative links and archive link checks. All 45 release-manifest entries match their declared hashes and the 64-member portable ZIP. Active public scripts/configuration contain no old client-path references. The presentation scratch dependency symlink resolves in its intended development VM; its VM path is not meaningful on the host. The [relocation specification](specs/2026-09-workspace-relocation.md) defines the checked scope. Architecture sources and PNG/PDF/PPTX exports are unchanged by the relocation and documentation work. The [workspace layout](workspace-layout.md) describes the maintained arrangement.

Detailed inventories and operational receipts remain local outside the public repository. This work establishes relocation and publication continuity; it does not close architecture-review findings, establish external-writing cleanup, or assess implementation effectiveness.

## Independent build and published verification

A Git-only export of relocation commit [`ad019e7715b94676e2dc5d331a2913115ecba3ed`](https://github.com/jessepike/ai-security-reference-architectures/commit/ad019e7715b94676e2dc5d331a2913115ecba3ed) built successfully in a separate VM directory with a fresh dependency installation. All 47 built files match the new-location build; ZIP comparison uses the member names and uncompressed bytes because archive ordering and timestamps can differ. No original workspace, review folder or surrounding exploratory source was supplied to that build.

[GitHub CI run 34399119882](https://github.com/jessepike/ai-security-reference-architectures/actions/runs/34399119882) passed and Vercel reported deployment complete. All 47 anonymous public routes/files returned HTTP 200 and matched the local build, including all 64 ZIP members. GitHub, the Vercel project and the custom domain retain their existing identities.

Live browser checks covered the project guide and decision page at desktop 1440 × 1000 and mobile 390 × 844. The new DEC-011 row renders and its workspace-layout link points to the correct public GitHub document. No horizontal document overflow was observed; mobile navigation opens. Screenshots were inspected for mobile presentation. These are scoped browser checks alongside complete automated page and download fidelity checks, not a new architectural or accessibility certification.

The temporary compatibility link also keeps the current application task's old address usable. Its configured sandbox root predates the move; continued file operations in this task required authorized escalated execution at the new physical path. Future work should open the new `publication/` Git root directly. No global application or agent configuration was rewritten.
