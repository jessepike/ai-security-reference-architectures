# Backlog

Status terms: **In progress** is authorized work being executed; **Complete** has stated evidence; **Open** is a tracked need awaiting completion; **Not commissioned** records intended future work whose specific scope has not been selected. Status alone does not authorize execution. Outcome IDs refer to [AISG-INTENT-001](intent.md#purpose-outcomes-and-value); roadmap IDs refer to [ROADMAP.md](ROADMAP.md). Each item's owner state records its current limits.

## Completed foundation

### AISG-001 — Canonical package foundation

- **Status:** Complete
- **Trace:** RM-01 · O1, O2
- **Acceptance / evidence:** The public vendor-neutral package maintains the three security views, governance companion, canonical sources, five PNGs, four guides, 44-slide presentation and website. DEC-001 through DEC-008 and [the release manifest](docs/release-manifest.json) provide the decision and artifact record.
- **Owner state:** Established project foundation; does not establish deployed effectiveness or enterprise authority.

### AISG-002 — Integrated governance story

- **Status:** Complete
- **Trace:** RM-01 · O1, O2
- **Acceptance / evidence:** DEC-009, overview v0.3 and its website/presentation alignment were published in release `54a2036ff85a89a0684cd834e7d77a849a3b5376`; [integrated-story validation](docs/validation-2026-09-integrated-story.md) records the checks and final presentation hash.
- **Owner state:** Established project direction and released narrative. Original substantive findings, human review and reader testing remain open.

### AISG-003 — Project-record alignment

- **Status:** Complete
- **Trace:** RM-01 · O1, O2, O3, O4
- **Acceptance / evidence:** [AISG-INTENT-001](intent.md), [alignment specification](docs/specs/2026-09-project-alignment.md), [ROADMAP.md](ROADMAP.md), this backlog, status and DEC-010 connect governing direction, outcomes, work and downstream boundaries without changing the five PNGs, four guides or 44-slide presentation.
- **Owner state:** Accepted owner direction governs the alignment; proposed roadmap ordering and downstream mechanisms remain labelled as such.

### AISG-013 — Workspace relocation and repository separation

- **Status:** Complete
- **Trace:** RM-01 · O3, O4
- **Acceptance / evidence:** Preserve all workspace files and Git history while extracting the package from the misplaced client directory; retain an independent public repository under `ai-security/ref-architectures/publication/`; validate the new-path build, links, artifacts, GitHub CI, deployment and anonymous browser/download behavior. See [specification](docs/specs/2026-09-workspace-relocation.md), [layout](docs/workspace-layout.md) and [validation](docs/validation-2026-09-workspace-relocation.md).
- **Owner state:** Explicitly authorized relocation; no source import, architecture revision or repository merger.

## Open work

### AISG-014 — Applying Secure Business AI preview

- **Status:** Complete; published
- **Trace:** RM-05 · O1, O2, O3
- **Acceptance / evidence:** Commit `bc74095c3fe9c3aa7a5765a90be1bebb4a77c022` maintains the neutral source and detailed guide, derived map and PDFs, separate site routes, and related links. Three model-assisted review passes verified the original eight High corrections and the map correction; the final source-attribution wording was corrected and locally verified after the panel. Source-fidelity, link, archive, manifest, rendered-page, binary-preservation, local browser, CI, Vercel, and live preview checks passed. See [validation](docs/validation-2026-09-applying-secure-business-ai-preview.md).
- **Owner state:** Published under DEC-015 in release `1f8970f046d4019ee25f26e52595c130fd74fae8`. Human review, field validation, control effectiveness, compliance, and organization-specific adoption remain unassessed.

### AISG-015 — Stage 0 CISO starter-playbook prototype

- **Status:** Complete; prototype selected for walkthrough
- **Trace:** RM-05 · O2, O3
- **Acceptance / evidence:** Prototype one compact, reusable Stage 0 Envision playbook and targeted handoff into Discover and guardrail. Include an eight-question starter conversation, qualitative initial risk view, bounded experiment guidance, Stage 1 handoff, customer-service credit-assistant example, and proportional-path checks for bought and built AI. Map the outputs to the existing guide without changing it.
- **Owner state:** Completed exploration for Stage 0 and its handoff. Selected material is published through AISG-016; later-stage playbooks, field validity, and organization-specific use remain unassessed.

### AISG-016 — CISO walkthrough preview

- **Status:** Complete; published
- **Trace:** RM-05 · O1, O2, O3
- **Acceptance / evidence:** Present the selected Stage 0 playbook and Stage 1 handoff as six meeting-friendly conversation stops at `/ciso-walkthrough`; preserve one canonical Markdown source, source-fidelity checks, no-JavaScript access, direct-hash and browser-history navigation, accessible template disclosures and copy actions, and derived Markdown downloads. Link it from the home and application pages without changing the established architectures, application guide, map, PDFs, or presentation.
- **Owner state:** Published under DEC-015 in release `1f8970f046d4019ee25f26e52595c130fd74fae8`. Source-fidelity, link, archive, derived-template, internal implementation review, local browser, CI, protected-preview, and anonymous production checks pass. Human architectural review, reader testing, field validation, control effectiveness, compliance, and organization-specific adoption remain unassessed. See [validation](docs/validation-2026-09-ciso-walkthrough.md).

### AISG-017 — Primary navigation layout

- **Status:** Complete for local preview
- **Trace:** RM-01 · O1, O2
- **Acceptance / evidence:** Group the three architecture views, Secure Business AI application material, and project resources into accessible navigation menus while preserving direct Overview and Governance links and every prior destination. Validate keyboard, Escape, outside-click, current-page, no-JavaScript, responsive, overflow, source-fidelity, link, and archive behavior.
- **Owner state:** Local build, source-fidelity, link, archive, responsive, keyboard, no-JavaScript, and independent browser checks pass. Authorized site-usability change awaiting preview deployment; canonical content meaning, review status, and publication authority remain unchanged. See [validation](docs/validation-2026-09-navigation-layout.md).

### AISG-018 — Neutral public introduction

- **Status:** Complete
- **Trace:** RM-01 · O1, O2
- **Acceptance / evidence:** Replace personal ownership framing in the README, purpose, and project-guide introductions with a direct description of the public, vendor-neutral resource. Preserve functional addresses and historical project records; verify current public and downloadable surfaces for unintended personal or organizational branding.
- **Owner state:** The README, purpose, and project-guide introductions now describe the resource directly. Current Markdown/source scans and extracted PDF/PowerPoint text contain no unintended personal or ePlus branding; remaining name strings are functional addresses or retained historical records. Site, source-fidelity, archive, and repository-link checks pass. Architecture meaning, accepted intent, authorship history, review state, and publication authority are unchanged.

### AISG-019 — Foundation editorial clarity

- **Status:** Complete
- **Trace:** RM-02 · O1, O2
- **Acceptance / evidence:** Apply the ten owner-approved wording changes from the 15 September foundation editorial review to canonical sources, matching guide passages, the generated site, and maintained presentation outputs. Preserve architecture meaning, authority, exposure conditions, evidence requirements, and review state; validate source synchronization and regenerated artifacts.
- **Owner state:** Complete under DEC-017. Canonical source regression review, site source-fidelity and link checks, 44-slide package/layout checks, and full-size/contact-sheet inspection of affected presentation and Guide 03 output pass. This scoped edit does not complete the broader external-writing cleanup in AISG-008 or establish reader comprehension. See [validation](docs/validation-2026-09-editorial-clarity.md).

### AISG-004 — Adjudicate original architecture-review findings

- **Status:** Open
- **Trace:** RM-02 · O1, O2
- **Acceptance / evidence:** Record a disposition for all 30 original findings, including the two reviewer-labelled High findings on recovery authorization and execution identity in *Defend with AI*; identify any resulting canonical source revision and preserve rejected or unresolved findings. Source: [review status](content/review-status.md).
- **Owner state:** Tracked review work; no finding is closed until its disposition and evidence are recorded.

### AISG-005 — Obtain human architectural review

- **Status:** Open
- **Trace:** RM-02 · O1, O2
- **Acceptance / evidence:** A human reviewer assesses the current overview, governance companion and relevant component contracts, with observations and disposition recorded against the exact reviewed sources.
- **Owner state:** Needed evidence; no human acceptance is inferred from model review or publication.

### AISG-006 — Test intended-reader comprehension

- **Status:** Open
- **Trace:** RM-02 · O1, O2
- **Acceptance / evidence:** Record reader feedback on the security/governance relationship, ownership language and key limits; revise only through identified source changes and decisions where warranted.
- **Owner state:** Proposed evaluation work; reader evidence is currently not assessed.

### AISG-007 — Tailor to a selected environment

- **Status:** Open
- **Trace:** RM-03 · O3
- **Acceptance / evidence:** Select a real workflow and environment before creating deployment-specific architecture or product mappings; document the specific authority, evidence and implementation context.
- **Owner state:** No environment, product or implementation is selected here; establish the specific scope before implementation.

### AISG-008 — Complete external-writing cleanup

- **Status:** Open
- **Trace:** RM-02 · O1, O2
- **Acceptance / evidence:** Apply the separate supported external-writing cleanup and record the affected sources and result. Do not claim this pass has run until it is evidenced.
- **Owner state:** Pending workflow availability.

### AISG-009 — Decide reuse licensing

- **Status:** Open
- **Trace:** RM-02 · O2
- **Acceptance / evidence:** Record an owner decision and applicable license before representing the library as openly licensed.
- **Owner state:** Reuse terms are undecided.

### AISG-010 — Project-guide website exposure check

- **Status:** Complete
- **Trace:** RM-01 · O1, O2, O3
- **Acceptance / evidence:** The [published project guide](https://ai.jessepike.dev/project) and all 47 published files match the local build. Local desktop/mobile browser and navigation checks passed. Results are recorded in [alignment validation](docs/validation-2026-09-project-alignment.md).
- **Owner state:** Completed within the authorized project alignment.

## Not commissioned

### AISG-011 — Exploration intake and canon-improvement loop

- **Status:** Not commissioned
- **Trace:** RM-03 · O3
- **Acceptance / evidence:** Select and complete a scoped exploration with a question, authorized evidence, findings and recorded disposition under the [exploration guidance](docs/exploration/README.md). A draft cannot change the canon without a reviewed source edit and recorded decision.
- **Owner state:** The method is documented; no specific exploration has been selected or commissioned.

### AISG-012 — Downstream adaptation intake

- **Status:** Not commissioned
- **Trace:** RM-04 · O4
- **Acceptance / evidence:** A downstream author records the canonical source revision, audience/context adaptation, receiving owner, review status and feedback route in the downstream register before representing a specific adaptation as ready.
- **Owner state:** Intended use only; it does not authorize adoption, an offer, pricing, delivery or organizational approval.
