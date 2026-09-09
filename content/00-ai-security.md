# AI Security

Version: 0.1 · 9 September 2026 · Status: Proposed narrative and overview architecture

This is the canonical entry point for the series: its definition, organizing story, relationships and overview visual. It connects the three component architectures in this series. It does not resolve their outstanding review findings or change their reviewed versions.

## The story

Organizations already protect important information, control access to systems, investigate attacks and recover services. AI changes how that work must be done.

AI can now be part of a business process. An assistant may read documents, recommend a decision or use tools to take action. Attackers can also use AI to help prepare and carry out attacks. Security teams can use AI to examine evidence and assist with their response.

**AI security protects the organization as AI becomes part of its work, attackers' methods, and its defenses.**

Our organizing idea is: **AI changes what we protect, how we are attacked, and how we defend.** These three questions lead to the three reference architectures below. They belong to one security program and often meet in the same business event.

This series takes a cybersecurity view of AI security. It connects to broader AI governance, privacy, safety and business-quality decisions; it does not claim to cover all of them. A technically authorized AI action can still be inaccurate, inappropriate or harmful. The business purpose and consequences must inform the controls.

## Three views of one security program

| View | Plain-language question | Familiar security work | What AI adds to the design |
|---|---|---|---|
| **01. Secure business AI** | What may our AI access and do? | Application security, data protection, access control and change management. | A workflow may interpret documents and generate tool requests. Untrusted content must not become permission. Limit access and actions, including permitted actions that could be misdirected. |
| **02. Defend against AI** | How do we stop attacks that AI helps attackers carry out? | Fraud prevention, exposure reduction, detection, incident response and recovery. | Reassess how attackers can use AI and attack AI systems themselves. Test the defenses against observable behavior without depending on proof that an attacker used AI. |
| **03. Defend with AI** | How can AI help security act effectively and within limits? | Security monitoring, investigation, playbooks and controlled automation. | AI can interpret evidence and propose actions. Permission, execution and verification need controls beyond the model's generated answer. |

The names remain consistent with the existing diagrams. “Secure business AI” describes the business-workflow view; its protection patterns also apply when the AI workflow belongs to the security team. “Defend against AI” is shorthand for defending against AI-enabled attacks, including attacks on AI workflows. AI is not treated as an adversary with intent of its own.

## How they connect

These relationships describe responsibilities and dependencies, not network traffic or a sequence of maturity stages.

| Relationship | Meaning | Practical interface to define in detailed design |
|---|---|---|
| **01 → 03: Protect the AI used by security.** | A security assistant needs access limits, protected data, secure tools, controlled changes and evidence just as a business assistant does. | Approved data access, distinct execution identities, tool permissions, approval records, and stop/recovery controls. Architecture 03 tailors these to security operations. |
| **03 → 01 + 02: Help operate and improve defenses.** | AI-assisted security can help investigate misuse of business AI and attacks across the enterprise. | Source-linked observations, action proposals, authorization decisions and verified outcomes. An AI recommendation does not authorize itself. |
| **02 → 01 + 03: Detect and contain attacks on AI.** | Both business AI and security AI can be attacked. The defensive program must be able to investigate and contain a compromised workflow. | Signals from resources and enforcement decisions, escalation paths, access revocation and recovery procedures. Response must retain a usable path when AI is unavailable or manipulated. |

The same event can appear in every view. That is expected: one view explains the workflow's safeguards, another explains the attack and response, and another explains how AI assists the defenders. Shared controls should have one implementation owner with explicit interfaces; repeating a box in another view does not create a second control service.

## A familiar example: a supplier payment change

A supplier asks the company to change bank details. A business assistant reads the request and prepares a proposed change.

In **Secure business AI**, the assistant may read the relevant records and prepare the change, but the destination and payment authority remain subject to the company's rules. Approval must refer to the actual proposed action, not just a persuasive summary.

In **Defend against AI**, the company treats an unexpected payment change as a fraud scenario. It verifies the request through a trusted business process and examines suspicious activity. It does not need to decide whether the email or voice was AI-generated before withholding payment.

In **Defend with AI**, a security assistant may bring together message, identity and application evidence to help an analyst investigate. Any account restriction or recovery action still needs the applicable authority, and its effect must be checked.

The business objective stays the same throughout: pay the right supplier and keep the business running. The three views explain different parts of protecting that objective. This is an illustrative design scenario, not a claim about any named company's systems or procedures.

## Shared foundation

All three views need **ownership, access rules, data protection, evidence and recovery**.

- **Ownership:** someone decides what the workflow is for, which consequences matter, and who can authorize changes or exceptions.
- **Access rules:** people, applications and AI workflows receive only the access and action permissions appropriate to the task.
- **Data protection:** information is handled according to its sensitivity, origin, permitted destinations and retention needs.
- **Evidence:** records from the systems involved let people reconstruct decisions and check what actually happened. An AI explanation alone is insufficient.
- **Recovery:** people can stop harmful activity, contain its effects and restore a usable service. Recovery actions have their own authority requirements.

These are shared concerns, not a product layer or a prescribed organizational structure. A detailed implementation assigns owners, systems and measurable acceptance conditions.

## Proposed design decisions

| ID | Decision and reason | Alternative and tradeoff | Revisit when |
|---|---|---|---|
| AISEC-D01 | Start with an organization-wide definition and three familiar questions. Readers need a reason for the categories before studying controls. | Start with threats or products; more concrete for specialists but narrows the introductory story. | The audience already shares the definition and needs a specific implementation answer. |
| AISEC-D02 | Keep the three views as peer perspectives. Their work overlaps in real events. | Draw a sequence or maturity ladder; easy to follow but implies prerequisites that do not apply universally. | A later artifact describes a particular adoption sequence, explicitly labeled as such. |
| AISEC-D03 | Show relationships and a shared foundation. This makes the overview an architecture of responsibilities, not just a category list. | Show only three headings; simpler but leaves the reader to infer dependencies. | Testing with readers shows a relationship is unclear or an important dependency is missing. |
| AISEC-D04 | Teach with one supplier-payment example and familiar security practices. It introduces AI-specific questions without requiring a new vocabulary first. | Use a model-training or multi-agent example; technically richer but harder for a first conversation. | The intended audience or use case requires another entry point. |
| AISEC-D05 | Keep the scope focused on cybersecurity and identify adjacent AI governance concerns. | Claim to cover all AI risk; creates misleading completeness without the necessary disciplines and evidence. | The owner explicitly expands the scope and provides the corresponding sources and expertise. |

## Visual contract and accessible description

PNG: `00-ai-security.png`. White background, landscape 16:9 target. The overview is read top to bottom. It shows scope and dependencies; it is not a deployment or transaction-flow diagram.

| Element ID | Exact visible copy | Meaning |
|---|---|---|
| O-TITLE | AI Security | Umbrella topic. |
| O-STORY | AI changes what we protect, how we are attacked, and how we defend. | The introductory mental model. |
| O-SCOPE | One security program | Grouping heading applying to all three cards. |
| O-01 | 01 / Secure business AI / What may our AI access and do? / Builds on application security, data protection and access control. | Protecting the organization's use of AI. |
| O-02 | 02 / Defend against AI / How do we stop AI-enabled attacks? / Builds on fraud prevention, detection and incident response. | Defending against attacker behavior, including attacks on AI. |
| O-03 | 03 / Defend with AI / How can AI help security act within limits? / Builds on investigation, playbooks and controlled automation. | Using AI in security work. |
| O-LINKS | How the views connect | Heading for the three dependency rows below. |
| O-R13 | 01 → 03 / Protect the AI used by security. | Protection dependency. |
| O-R312 | 03 → 01 + 02 / Help operate and improve defenses. | Operational support dependency. |
| O-R213 | 02 → 01 + 03 / Detect and contain attacks on AI. | Defense of both kinds of AI workflow. |
| O-BASE | Shared foundation / Ownership · Access rules · Data protection · Evidence · Recovery | Common concerns across the three views. |
| O-FOOT | Overview · Proposed · v0.1 · 09 Sep 2026 | Version and proposal status. |

The three cards are peers. Do not put flow arrows between adjacent cards. The arrows in the relationship rows mean “provides the named responsibility to”; they do not imply execution, unrestricted access, central ownership, or automatically authorized response. The shared foundation applies to all cards without prescribing a central platform. Navy indicates framing, blue indicates the peer views, teal indicates shared protective concerns, and gray provides structure; color is secondary to labels. Amber is unnecessary here because this overview does not depict a specific untrusted input or held action.

## Walkthrough and comprehension check

Read the organizing sentence, introduce the three questions, then use the supplier example to connect the views. Only then open the detailed diagrams and guides.

A reader should be able to explain what each view is for, why the security team's AI needs protection, and why using AI for defense does not remove the need for controlled access and response. If the reader interprets the cards as three purchases, three teams or three maturity stages, revise the explanation or visual.

## Sources and relationship to the series

NIST's [Cyber AI Profile project](https://www.nccoe.nist.gov/projects/cyber-ai-profile) describes corresponding areas covering protection of AI systems, AI-assisted attacks and AI-assisted defense. Checked 9 September 2026: the page reports that comments are under review and links the draft profile. This supports the three-part framing; the exact definition, teaching sentence, example, relationships and layout here are our proposed synthesis, not a NIST reference architecture or endorsement.

Continue with [01](01-secure-business-ai.md), [02](02-defend-against-ai.md), [03](03-defend-with-ai.md), their [architect guides](guide-index.md) and the [review findings](review-status.md). The overview has not yet received independent review or owner acceptance. This material is a review draft; see the review status before using it in detailed design.
