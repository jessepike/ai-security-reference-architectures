# Applying Secure Business AI preview adaptation

## Scope

Add a proposed, vendor-neutral application companion that helps a CISO support an AI effort from early shaping through operation. The companion applies the existing Secure Business AI architecture and AI Governance companion; it does not add a fourth architecture, alter either source, or extend the existing presentation.

This work is authorized for a Vercel preview only. It does not establish owner acceptance of the content, production publication, implementation effectiveness, compliance, or organizational authority.

## Sources and outputs

Canonical meaning lives in `content/applying-secure-business-ai.md` and `content/guides/applying-secure-business-ai-guide.md`. Derived outputs are the overview SVG and PNG, standalone overview PDF, and ten-page detailed guide PDF. Guide pages 1, 2, 9, and 10 are landscape; the six stage pages 3 through 8 are portrait. The site exposes `/applying-secure-business-ai` and `/guides/applying-secure-business-ai-guide`, with related links from the home, Secure Business AI, governance, and guide-index pages.

The adaptation incorporates the eight High corrections from the 14 September 2026 external panel review. Four Low observations are also addressed within the adaptation. Shared vocabulary remains partly aligned, while specialist scope boundaries and the frozen private guide's specification accuracy remain outside this adaptation. Their dispositions are recorded in the public review summary.

## Acceptance checks

- The six stages are clearly an application journey, distinct from the six governance responsibilities and from maturity.
- Each stage states what must be understood, the desired outcome, useful deliverables, evidence, and the next decision.
- Decision roles include business, data, privacy, legal, delegated security, exception, release, recovery, and other specialist authorities as applicable.
- Conflict, missing provider controls, unmanaged entry, and material change have explicit bounded responses under named authority.
- Human effects remain in the coverage map.
- Public files contain no private paths, raw prompts, private decision IDs, or internal reviewer metadata.
- The original five PNGs, four guides, and presentation remain byte-identical.
- The overview PNG and every guide PDF page render without clipping, overlap, broken glyphs, or shrink-to-fit.
- Site build, link, fidelity, archive, and release-manifest checks pass in the development VM.

## Render prerequisites

Run `scripts/render-application-guide.py` in the OrbStack `dev` VM. It requires Python with ReportLab and the `rsvg-convert` command from librsvg. The renderer reads the canonical Markdown directly; it does not require a maintained JSON content source.
