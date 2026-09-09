# Governing intent: AI Security & Governance

## Control

- **Intent ID:** AISG-INTENT-001
- **Version:** 1.0
- **Lifecycle state:** Accepted owner direction
- **Created:** 9 September 2026
- **Owner:** Jesse Pike
- **Supersedes:** None. Formalizes the owner's vision and the existing project decisions.
- **Governing record:** This file. Git records its revisions; [decisions.md](decisions.md) records why direction changes.

## Owner-stated vision

> “this is our canonical AI Security & Governance package. Intended to set the stage, provide awareness and education, as well as a source for future evolution, exploration, and will provide a basis for ePlus AI Ignite and AI Security & Governance GTM.”

Jesse directed that this vision be captured and aligned with the project's status, roadmap, decisions, backlog and intent on 9 September 2026. **State: Decided.** This is the project's governing direction, including its intended downstream use. It is not evidence of adoption or endorsement by ePlus.

## Compressed governing intent

Maintain our canonical AI Security & Governance package so people can establish a shared understanding, learn how security and governance work together, and use a consistent foundation for further exploration and development. This package will provide a basis for ePlus AI Ignite and AI Security & Governance go-to-market work, with adaptations traceable to their source.

The package name describes the body of work. The existing repository name and public address remain `ai-security-reference-architectures` and [ai.jessepike.dev](https://ai.jessepike.dev).

## Purpose, outcomes and value

| Outcome ID | Intended change | Who receives value |
|---|---|---|
| O1 — Orientation and awareness | Readers can explain what AI security and governance mean, why they matter, and how the three security perspectives relate to governance. | People beginning the conversation, including business and security stakeholders. |
| O2 — Education and practical reference | Readers and architects can follow a familiar example, understand the reasons behind the reference designs, and identify the questions a real implementation must answer. | Learners, presenters, reviewers and architects. |
| O3 — Evolution and exploration | New questions, evidence and findings develop from an identifiable shared source and can improve it through recorded decisions. | Jesse, human contributors and agents extending the work. |
| O4 — Downstream foundation | Future ePlus AI Ignite and AI Security & Governance GTM materials can build on consistent definitions, explanations and design rationale, with explicit adaptations and review status. | Authors and reviewers preparing those downstream materials and their eventual readers. |

The value is a common starting point that people can understand, question and develop without rebuilding the explanation or losing its rationale each time.

## Recognizing success

The following are proposed evaluation criteria for the accepted outcomes; reader evidence has not yet established them:

- Readers can explain the distinction and continuing relationship in their own words, rather than merely locate a diagram.
- An architect can trace a visual element to its explanation, design decision, evidence and remaining limitations.
- A fresh contributor or agent can identify what governs, what is current, what is proposed and what needs review without replaying this conversation.
- A downstream author can identify the source revision used, explain what changed for the audience or context, and return useful findings to this package.

Completing an artifact or publishing a page alone does not establish those outcomes. The [roadmap](ROADMAP.md) organizes their development; the [backlog](BACKLOG.md) tracks work and evidence.

## Boundaries

- This repository is the canonical source for this package. Existing shared definitions and decisions guide its Markdown, PNGs, guides, presentation and website. Canonical status identifies the maintained source; it does not make each architecture approved, deployed or proven.
- Retain the three peer security views and their relationship to the wider governance companion. Use plain language, familiar examples and enough detail for architects to examine the designs.
- Preserve the authorized-source boundary. Use this conversation's approved inputs and cited public primary sources. Naming ePlus as a downstream use does not authorize importing unrelated workspaces, client information or non-public material.
- Keep the foundational package vendor-neutral. Audience, channel, service and product adaptations belong in identified downstream work with a recorded source and adaptation rationale.
- The intended ePlus uses do not establish approved offers, sponsorship, pricing, delivery commitments or enterprise authority. Such decisions belong to their relevant owners and evidence.
- Exploration may challenge the canon; it changes the canon through a reviewed source edit and a recorded decision, not by silently promoting a newer draft.
- Prefer clarity, consistency and useful learning over artifact volume, visual polish alone or unsubstantiated claims of completeness.

## Assumptions and unknowns

| Item | Current state | Does it block this alignment? | Resolution path |
|---|---|---|---|
| The common explanation helps intended readers | Hypothesis; reader testing remains open | No | Education/readability work in the roadmap and backlog. |
| Exact first downstream AI Ignite or GTM artifact, audience and receiving owner | Not selected in this project | No; required before authoring a specific adaptation | Record a scoped brief and a row in the downstream register. |
| Organization-specific adoption and commercial authority | Not established here | No; required for corresponding claims or commitments | Confirm within the authorized downstream work. |
| Original substantive architecture findings | Open | No for a labelled discussion package; may constrain an implementation or adaptation | Adjudicate findings and preserve their status. |
| Reuse license and external-writing cleanup | Pending | No for maintaining the existing authorized publication | Resolve the existing backlog items before making additional reuse claims. |

## Acceptance and readiness

**Human Acceptance: accepted for the owner-stated direction.** The direct statement above is the authority being recorded, not a retrospectively inferred approval of new architecture choices. Jesse explicitly requested capture and alignment. Proposed evaluation criteria, roadmap ordering and unselected downstream mechanisms retain their labelled states.

**AI Readiness: ready for this scope.** There is sufficient context to maintain and connect this canonical package and record its intended downstream role without inventing a specific ePlus offer or implementation. The unknowns above constrain later work and remain visible.

**Gate 1: passed for the stated project intent.** The current request also authorizes aligning the project records. It does not authorize every future roadmap item merely by listing it.

## Traceability and revision

Read [the project guide](content/project-guide.md), [purpose](PURPOSE.md), [decisions](decisions.md), [status](status.md), [roadmap](ROADMAP.md), [backlog](BACKLOG.md), [source map](content/source-map.md) and [downstream use contract](docs/downstream-use.md) together. DEC-010 records this intent. Intent changes require explicit owner direction, a new version and a decision identifying affected work. No reconciliation event is open.

| Version | State | Reason | Human direction | AI readiness |
|---|---|---|---|---|
| 1.0 | Accepted owner direction | Record the canonical package vision and intended educational, exploratory and downstream value. | Jesse's direct instruction, 9 September 2026 | Ready for package maintenance and record alignment. |
