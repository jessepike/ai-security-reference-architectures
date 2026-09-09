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

- **Status:** In progress
- **Trace:** RM-01 · O3, O4
- **Acceptance / evidence:** Preserve all workspace files and Git history while extracting the package from the misplaced client directory; retain an independent public repository under `ai-security/ref-architectures/publication/`; validate the new-path build, links, artifacts, GitHub CI, deployment and anonymous browser/download behavior. See [specification](docs/specs/2026-09-workspace-relocation.md), [layout](docs/workspace-layout.md) and [validation](docs/validation-2026-09-workspace-relocation.md).
- **Owner state:** Explicitly authorized relocation; no source import, architecture revision or repository merger.

## Open work

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
- **Acceptance / evidence:** A downstream author records the canonical source revision, audience/context adaptation, receiving owner, review status and feedback route in the downstream register before representing a specific AI Ignite or GTM artifact as ready.
- **Owner state:** Intended use only; it does not authorize ePlus adoption, an offer, pricing, delivery or enterprise approval.
