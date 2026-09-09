# AI Security and Governance

Version: 0.3 · 9 September 2026 · Status: Proposed narrative and overview architecture

This is the canonical entry point for the series: the shared story of AI security and governance, their relationship, and the three security perspectives. The governance companion explains the wider decision and oversight responsibilities in detail. Outstanding component review findings retain their recorded status.

The narrative is v0.3. The existing PNG and visual contract remain v0.1 and depict the three security views. Read that security diagram together with the governance companion and the relationship explained here.

## The story

Organizations need to decide where AI belongs in their work and protect the work that depends on it. AI governance and AI security help them do both, with evidence from real use informing whether that use should continue or change.

Consider a familiar supplier-payment process. Someone decides who may change bank details, what checks apply and who answers if a payment goes wrong. Others implement those checks, investigate suspicious requests and use what they learn to improve the process. Adding an AI assistant changes how some tasks happen. The company still needs people with authority to make decisions and practical safeguards that carry those decisions into the work.

**AI governance directs and oversees AI use: who may decide, what uses and risks are acceptable, what evidence is required, and when decisions must be revisited.**

**AI security protects the organization as AI becomes part of its work, attackers' methods, and its defenses.**

**Governance directs AI use. Security protects it. Evidence from real use informs the next decision.**

That is the shared story of this library. Decisions set the purpose and conditions for AI use. Security specialists help assess what is feasible and what could go wrong, work with other teams to implement protections, and report what those protections achieve or miss. Responsible decision makers use that evidence, alongside business results and other impacts, to continue, restrict, redesign or stop a use.

Governance covers a wider set of questions than cybersecurity, including whether AI is suitable for its purpose and how it affects people. Privacy, reliability, safety, fairness and other concerns need their own expertise. A secure system can still produce an unsuitable decision. The relationship described here organizes the conversation; it does not make this library a complete treatment of every AI risk.

Within that shared story, **AI changes what we protect, how we are attacked, and how we defend.** Those three questions lead to the security architectures below. An assistant may read business records or use tools, an attacker may use AI to help carry out an attack, and a security team may use AI to examine evidence. The three security views often meet in the same event and connect to the same decisions about purpose, authority and acceptable consequences.

## How governance and security work together

Governance and security exchange decisions and evidence throughout an AI use's life. Security advice helps shape the initial decision, and operating results can change an earlier decision. The following are recurring exchanges, not a fixed approval sequence.

| Exchange | What people share | What it enables |
|---|---|---|
| **Assess the proposed use together** | The business owner explains the purpose, affected people, data and intended actions. Security identifies threats, possible safeguards, constraints and evidence gaps. Other specialists assess their concerns. | The authorized decision makers can decide whether the use is appropriate and feasible, including whether to narrow it or pause. |
| **Turn conditions into protections** | Decision makers record permitted uses, limits, required checks and who may approve exceptions. Security and delivery teams translate relevant conditions into access rules, protected tools, monitoring and recovery arrangements. | Release evidence can show which conditions have been implemented and tested, and which remain unresolved. |
| **Return evidence from operation** | Security supplies control results, incidents and limits of detection. Business and other teams supply outcome, quality and impact evidence. | Responsible decision makers can judge continued use with a fuller view of what actually happens. A quiet alert feed alone does not establish acceptable use. |
| **Respond and reconsider** | An incident, failed check or material change reaches the people authorized to restrict, change or stop the use. Their decision updates the conditions and implementation. | The organization can contain immediate harm and decide what must change before continued use or restoration. |

Existing incident procedures should give named responders authority to take urgent protective action within agreed limits. A routine governance review need not precede every containment action. The incident and its consequences still feed subsequent reassessment, and recovery needs its own appropriate authority.

The relationship takes a different form in each security view. Governance of the organization's AI uses applies to business AI and AI used by defenders, including limits on investigation data and automated response. Defense against AI-enabled attacks uses established security and business decision rights even when the organization uses no AI itself. The attacker's AI does not become an enterprise AI use to approve. When an attack affects the organization's AI, the resulting evidence also informs decisions about that use.

## Who coordinates and who decides

Security, GRC, an AI office or another function may coordinate the work. The useful starting question is which role holds each decision. The coordinator can bring the right people and evidence together without becoming the owner of every business outcome or risk.

For example, the business process owner answers for the intended outcome; security holds the security decisions assigned to it; privacy, legal, data and other specialists hold their relevant responsibilities. The organization must make that allocation explicit. Reuse existing product, procurement, risk, change and incident processes where they can perform the work. A reporting line alone does not explain who may release, accept an exception or stop an AI workflow.

## Begin with the situation and the next decision

Start with a real use of AI or a decision someone needs to make. State what the AI is meant to do, who is affected, who answers for the business outcome, what data and actions are involved, and what decision is pending. That intake may route work to one primary security motion while several architecture views still apply. A **motion** is the workstream selected for the current decision. An **architecture view** is a perspective used to design the protections.

AI can arrive through software the organization builds, a service it buys, a feature embedded in an existing product, or use that has not yet entered normal oversight. These are overlapping discovery prompts. A purchased product may contain embedded AI, and built, bought or embedded AI may also be unmanaged. Ask all four questions instead of assigning each use to one exclusive bucket.

Ownership follows the decision and the consequence. A business process owner usually answers for a business use and its outcome. Security owns security decisions within its assigned authority and leads the design and operation of cybersecurity protections. Data, technology, privacy, legal, safety, finance, fraud, identity, recovery and other functions may hold decisions that belong to them. The detailed design must name the people or roles that decide, implement, check and accept risk; saying “governance” or “the business” is not an authority assignment.

Before permitting data use, establish both access and appropriateness. Access control asks whether an identity may reach the data. Governance must also ask whether the proposed use is allowed, suitable for the purpose, supported by adequate evidence and consistent with obligations to affected people. Missing evidence can lead to a pause, narrower conditions, redesign or stopping.

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

Through **AI governance**, the company names the payment-process owner and decides what help is appropriate. In this example, the assistant may prepare a change using specified records, while a designated person verifies the request through a trusted route and approves the actual change. The decision also states the evidence needed before release, who can stop the assistant and what changes require reassessment. Security helps shape these conditions by assessing fraud, access and workflow risks before use begins.

In **Secure business AI**, the assistant may read the relevant records and prepare the change, but the destination and payment authority remain subject to the company's rules. Approval must refer to the actual proposed action, not just a persuasive summary.

In **Defend against AI**, the company treats an unexpected payment change as a fraud scenario. It verifies the request through a trusted business process and examines suspicious activity. It does not need to decide whether the email or voice was AI-generated before withholding payment.

In **Defend with AI**, a security assistant may bring together message, identity and application evidence to help an analyst investigate. Any account restriction or recovery action still needs the applicable authority, and its effect must be checked.

The results return to the decision makers. If records show that the assistant repeatedly proposes the wrong account, the payment owner may restrict or pause it even if nobody attacked the system. If a new tool would let it update bank details directly, that proposed capability requires assessment of changed permissions and consequences. Security evidence contributes to those decisions alongside payment accuracy and other business evidence.

The business objective stays the same throughout: pay the right supplier and keep the business running. Governance establishes and revisits the conditions for using AI; the three security views explain the protections and response that support those conditions. This is an illustrative design scenario, not a claim about any named company's systems or procedures.

## Shared foundation

All three views need **ownership, access rules, data protection, evidence and recovery**.

- **Ownership:** someone decides what the workflow is for, which consequences matter, and who can authorize changes or exceptions.
- **Access rules:** people, applications and AI workflows receive only the access and action permissions appropriate to the task.
- **Data protection:** information is handled according to its sensitivity, origin, permitted destinations and retention needs.
- **Evidence:** records from the systems involved let people reconstruct decisions and check what actually happened. An AI explanation alone is insufficient.
- **Recovery:** people can stop harmful activity, contain its effects and restore a usable service. Recovery actions have their own authority requirements.

These are shared concerns, not a product layer or a prescribed organizational structure. A detailed implementation assigns owners, systems and measurable acceptance conditions.

## Connection to AI governance

Use the [AI Governance companion](04-ai-governance.md) and its [detailed guide](guides/04-ai-governance-guide.md) to examine the decisions and evidence behind this story. Its six responsibilities cover purpose and ownership, risk and impact review, decisions and conditions, implementation and release, operation and reassessment, and change or retirement. The three security views provide the corresponding cybersecurity detail. The governance companion remains distinct from those three peer security perspectives.

## Proposed design decisions

| ID | Decision and reason | Alternative and tradeoff | Revisit when |
|---|---|---|---|
| AISEC-D01 | Start with an organization-wide definition and three familiar questions. Readers need a reason for the categories before studying controls. | Start with threats or products; more concrete for specialists but narrows the introductory story. | The audience already shares the definition and needs a specific implementation answer. |
| AISEC-D02 | Keep the three views as peer perspectives. Their work overlaps in real events. | Draw a sequence or maturity ladder; easy to follow but implies prerequisites that do not apply universally. | A later artifact describes a particular adoption sequence, explicitly labeled as such. |
| AISEC-D03 | Show relationships and a shared foundation. This makes the overview an architecture of responsibilities, not just a category list. | Show only three headings; simpler but leaves the reader to infer dependencies. | Testing with readers shows a relationship is unclear or an important dependency is missing. |
| AISEC-D04 | Teach with one supplier-payment example and familiar security practices. It introduces AI-specific questions without requiring a new vocabulary first. | Use a model-training or multi-agent example; technically richer but harder for a first conversation. | The intended audience or use case requires another entry point. |
| AISEC-D05 | Superseded for the introductory story by AISEC-D08. The original v0.1/v0.2 framing led with cybersecurity and identified governance as adjacent scope. The three security views retain their cybersecurity focus. | That framing kept the entry point narrow but left readers to connect governance themselves. | Retained as historical rationale; use AISEC-D08 for the current story. |
| AISEC-D06 | Begin intake with the situation, pending decision, accountable owner, affected people, data and actions. This lets readers route work before choosing a technical view. | Start with a category or product; faster classification but can obscure the actual outcome and authority. | Reader testing shows another intake sequence produces clearer accountable decisions. |
| AISEC-D07 | Treat built, bought, embedded and unmanaged as overlapping discovery prompts, and connect the security series to a separate governance companion. | Use exclusive arrival buckets or add governance as a fourth security view; visually simpler but misstates common combinations and scope. | A local taxonomy preserves overlap, or the series owner explicitly changes the architecture. |
| AISEC-D08 | Introduce security and governance together through decisions, protections and returning evidence. Carry the relationship through one example, while preserving the three security views and the wider governance remit. | Add only a governance paragraph at the end; less introductory text but leaves the main story incomplete. | Reader testing shows the relationship is unclear or a real implementation needs a more specific decision model. |

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
| O-FOOT | Overview · Proposed · v0.1 · 09 Sep 2026 | Version and proposal status visible in the existing security PNG. The canonical narrative is v0.3; the PNG continues to depict the three security views, with the governance relationship explained in the surrounding story and companion. |

The three cards are peers. Do not put flow arrows between adjacent cards. The arrows in the relationship rows mean “provides the named responsibility to”; they do not imply execution, unrestricted access, central ownership, or automatically authorized response. The shared foundation applies to all cards without prescribing a central platform. Navy indicates framing, blue indicates the peer views, teal indicates shared protective concerns, and gray provides structure; color is secondary to labels. Amber is unnecessary here because this overview does not depict a specific untrusted input or held action.

## Walkthrough and comprehension check

Begin with the shared business situation. Explain who decides the conditions for AI use, how security helps shape and protect that use, and how evidence changes subsequent decisions. Introduce the three security questions and walk through the supplier example, including its governance conditions and reassessment. Then open the detailed diagrams and guides.

A reader should be able to explain what governance decides, what security contributes before and after release, and what evidence could cause a decision to change. They should also understand why the security team's AI needs protection and why permitted use can still produce an unacceptable business result. If readers interpret governance as a one-time approval, assign every decision to the coordinating team, or treat the three security cards as purchases or maturity stages, revise the explanation.

## Sources and relationship to the series

NIST's [Cyber AI Profile project](https://www.nccoe.nist.gov/projects/cyber-ai-profile) describes corresponding areas covering protection of AI systems, AI-assisted attacks and AI-assisted defense. Checked 9 September 2026: the page reports that comments are under review and links the draft profile. This supports the three-part framing; the exact definition, teaching sentence, example, relationships and layout here are our proposed synthesis, not a NIST reference architecture or endorsement.

NIST's [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) describes governance as a continuing responsibility throughout risk management and calls for clear roles, monitoring and review. Its [AI Risks and Trustworthiness](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) explains why security must be considered alongside reliability, safety, privacy and other characteristics. Checked 9 September 2026: both pages describe AI RMF 1.0 and note that a revision is in progress. These sources support the broader scope and continuing relationship. The definitions, exchange table and supplier example here are this series' teaching synthesis.

Continue with [AI Governance](04-ai-governance.md), security views [01](01-secure-business-ai.md), [02](02-defend-against-ai.md), [03](03-defend-with-ai.md), their [architect guides](guide-index.md) and the [review findings](review-status.md). Overview v0.3 received a separate bounded model-assisted narrative review. One advisory scope clarification was applied and the reviewer confirmed its resolution. The review does not cover the resulting presentation or website, and human architectural review and reader testing remain open.
