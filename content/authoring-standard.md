# Architecture authoring standard

Version: 0.3 · 9 September 2026 · Status: Proposed series standard

Audience: human authors, architects, editors, reviewers and AI agents. This document records the shared writing, visual and production conventions for this series.

## Start with the reader

The introductory reader understands ordinary business activity and basic security concerns but may be unfamiliar with AI terminology. The architect guide serves a more technical reader. Keep those two levels connected without requiring introductory readers to learn implementation details first.

Use the sequence: **familiar situation → governance and security responsibilities → their exchange of decisions and evidence → relevant architecture views → worked example → detailed decisions and evidence**. Begin with the purpose of the architecture and the decision it helps someone make.

The overview's shared story is “Governance directs AI use. Security protects it. Evidence from real use informs the next decision.” Within that story, “AI changes what we protect, how we are attacked, and how we defend” introduces the three security views. Retrieve the exact definitions, labels and relationships from [00-ai-security.md](00-ai-security.md); do not paraphrase them into competing definitions in each artifact.

The governance companion answers who decides whether and how AI may be used, what evidence is required, and when the decision must be revisited. Do not present governance as a fourth security view or force it into three categories. Connect it to the three security views through decisions, conditions, controls, incidents and evidence.

Explain the exchange before introducing the component architectures. Security helps assess and shape proposed uses before approval, and governance continues during operation. Show evidence changing a decision in the recurring example. Identify both a security concern and a business-quality or impact concern so readers do not equate secure access with acceptable use. Preserve existing authority for urgent response and avoid implying that every protective action waits for a review meeting.

## Source order and responsibilities

Read [source map](source-map.md), then the relevant canonical architecture and this standard before authoring. Human and agent authors use the same sources and template.

1. The user's current direction sets scope and constraints.
2. The overview defines the series narrative and relationships.
3. Each canonical architecture defines its own meaning, design decisions and visual contract.
4. Its detailed guide explains the contract and labels implementation elaboration or unresolved decisions.
5. PNG and PDF outputs depict or render those sources.
6. Research records support claims; reviews challenge them. Neither silently changes the design.

If sources conflict, name the conflict and propose a source edit before changing a render. A newer file is not automatically more authoritative. Canonical means the designated editable source; it does not mean accepted, deployed or proven effective.

## Language and teaching rules

- Use familiar words and concrete verbs. Say who checks, permits, records or stops something.
- Introduce an unfamiliar term with its ordinary meaning and a short example before using shorthand. Define an agent as an AI-based workflow that can use tools to carry out parts of a task; do not imply independent business authority.
- Connect a new concept to familiar practice and state where the analogy stops. An AI assistant can be compared to a worker with access permissions, but it has no human judgment, accountability or right to approve its own actions.
- Distinguish analysis, permission, execution and verified outcome. “Suggested,” “allowed,” “attempted” and “confirmed” describe different states.
- Explain what a control can and cannot establish. Access checks cannot establish that every permitted action is a good business decision.
- Use a recurring example to connect views. Keep facts and characters consistent; label examples as illustrative.
- Avoid unexplained acronyms, product lists, promotional language and claims that a control “ensures” security without conditions.
- Prefer short connected paragraphs. Use tables for genuine comparisons, interface definitions and decisions. Use lists for steps or parallel checks.
- Keep the image sparse. Put rationale, alternatives, exceptions and source nuance in the guide.
- Name the human or assigned role that holds a decision right. A coordinating governance function does not silently acquire accountability for every business, security, privacy, safety or operational outcome.
- Treat built, bought and embedded as overlapping origin or delivery questions, and unmanaged as an oversight condition that can apply to any of them.
- Reuse existing business, risk, privacy, security, release, incident and assurance processes where they can perform the stated responsibility. Add a new process only when a required decision or evidence path is missing.

Preferred translations:

| Technical term | Introduce it as |
|---|---|
| Authorization | Deciding whether this identity may perform this action on this target. |
| Non-human identity | An identity assigned to an application or automated workflow. |
| Prompt injection | Untrusted content that tries to redirect an AI workflow. Explain both attempts to exceed permission and misuse within permission. |
| Provenance | Where information came from and how it was obtained. |
| Telemetry | Records and signals from systems about what happened. |
| Autonomy limit | The actions a workflow may take without a new human decision. |
| Trust boundary | A point where access, information or actions cross into a different set of security rules. |

These explanations aid comprehension; preserve a precise technical term when an architect needs it.

## Visual rules

Use a white background and landscape 16:9 target, clear sans-serif text, generous whitespace and a consistent title position. Record actual pixel dimensions instead of claiming the requested size was delivered. Never squeeze more text into a box by making it unreadable at its intended display size.

| Visual role | Treatment |
|---|---|
| Framing and governing rules | Navy |
| Operational components or peer architecture views | Blue / pale blue |
| Enforcement, verification and protective concerns | Teal / pale teal |
| Untrusted inputs, attack paths or held actions | Amber, when relevant |
| Scope and supporting structure | Gray |

Use color consistently within a diagram and explain exceptions. Labels and line styles must carry meaning without reliance on color alone. Do not introduce a color merely to use the whole palette.

Every box has a stable element ID, exact label, purpose and guide reference. Every meaningful connector has a source, destination, label, direction and interpretation. Explain whether an arrow carries a request, evidence, authority, results or a responsibility. A grouping line is not an execution path. A feedback loop must state what can change and who authorizes it. Explain important omitted paths in the guide; do not let their absence imply that logging, approval or recovery is unnecessary.

A PNG is a visual companion. Keep its accessible text description in Markdown. When a generated PNG is used, preserve the exact prompt and inspect spelling and connectors against the contract; prompt compliance cannot be assumed.

## Required package

Use [the template](templates/reference-architecture.md) for each new architecture. An overview may combine its narrative and guide explanation in one canonical document; component architectures retain a separate detailed guide.

- Canonical Markdown: purpose, scope, intended reader, familiar anchor, architecture, relationships, decisions, worked example, limitations, visual contract and dated sources.
- PNG: exact semantic match to the contract, with version and status visible.
- Guide Markdown: every visual element and connection, responsibilities, inputs/outputs, enforcement, failure behavior, alternatives, tradeoffs and questions requiring deployment context.
- PDF when requested: diagram opener followed by the guide; preserve headings, numbering, table meaning and links. Define any extra cover/footer wording explicitly in production metadata.
- Production record: source version, render method, exact prompt or renderer, actual dimensions/page counts, inspection results and known defects.
- Review record: exact reviewed versions, critique and reviewer limitations. Record actual model and actual image inspection when model review is requested.

## Human and agent workflow

1. Read the source map and user brief. State the intended reader, altitude and question.
2. Draft the narrative and decisions in Markdown. Mark new choices as proposals. Use primary sources for current claims, with dates and publication status.
3. Define the visual contract before generating the image. Populate each element and connector in the guide. Cross-reference related architectures instead of inventing duplicate control ownership.
4. Render from the declared source. Do not update reviewed snapshots in place. Preserve a versioned record when making revisions.
5. Check the image and every PDF page. Compare labels, spelling, direction, status, omissions, page numbers, aspect ratio, link targets, tables and text coverage. Automated coverage is only one check.
6. Conduct a reader check: can someone explain the purpose, the main relationship and one important limit without the author narrating? Record “not assessed” if no reader check occurred.
7. If independent review is requested, send the actual visual and complete sources. Separate observations, recommendations and accepted changes. Record open findings at handoff.
8. Update the source map and status. A human can accept or redirect design choices. Agents may prepare and verify drafts within their authorized scope; generation and review do not imply acceptance.

Before publication, review the language for clarity and confirm that architectural limits, source status and unresolved findings remain visible.

## Acceptance questions

Can the intended reader explain the architecture in their own words? Does every visual element have one meaning and a place in the guide? Are shared responsibilities and authority paths explicit? Does the worked example demonstrate both the useful behavior and its limits? Are source claims distinguished from our design choices? Can another human or agent reproduce the package from the declared sources without relying on this chat?

This standard supports repeatable meaning and review. Image generation does not guarantee identical pixels on repeated runs. Exact visual reproducibility would require an editable deterministic diagram source and renderer; that has not been established for the existing PNGs.
