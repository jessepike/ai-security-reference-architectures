# AI Governance

Version: 0.1 · 9 September 2026 · Status: Review draft

This is the canonical source for the AI Governance reference architecture. It is a companion to the three AI security views. It does not add a fourth security category or assign authority in a particular organization.

## Purpose and scope

**AI governance directs and oversees AI use: who may decide, what uses and risks are acceptable, what evidence is required, and when decisions must be revisited.**

AI security protects AI systems and the resources they reach, withstands attacks involving AI, and supports safe use of AI in security work. Governance includes security requirements and also considers appropriate purpose, reliability, safety, privacy, fairness, transparency, and effects on people and business. A system can satisfy access rules and still be inaccurate, unsuitable or harmful.

This logical architecture helps leaders, business owners, risk specialists, architects and operators connect decisions across an AI use's lifecycle. It does not prescribe a new committee or duplicate every existing process. Existing product, procurement, privacy, security, change, incident, legal, safety, quality and assurance processes should perform these responsibilities where they can.

## Begin with what arrived and the decision at hand

Ask whether the AI is built by the organization, bought as a service, embedded in an existing product, or unmanaged outside normal oversight. These descriptions overlap. A bought product may contain embedded AI, and any built, bought or embedded use may be unmanaged.

Then record the real situation: what the AI is for, who is affected, what data and actions it uses, who answers for the outcome, and which decision is pending. Valid outcomes include proceeding, proceeding with conditions, pausing for evidence, narrowing the use, redesigning it or stopping it.

## The architecture

![AI Governance reference architecture](../public/images/04-ai-governance.png)

The architecture contains six connected responsibilities. They often inform one another and may be revisited; they are not a universal sequence of approval meetings.

| ID | Responsibility | Question | Representative output |
|---|---|---|---|
| G-01 | **Purpose and ownership** | What is it for, who is affected, and who answers for it? | Use-case record, affected parties, accountable owner and intended outcome. |
| G-02 | **Risk and impact review** | What could go wrong, and which obligations apply? | Risk and impact assessment, review participants, evidence gaps and applicable obligations. |
| G-03 | **Decision and conditions** | May it proceed, with what limits and evidence? | Recorded decision, conditions, exception authority and reassessment triggers. |
| G-04 | **Implementation and release** | Have conditions been implemented and tested? | Implemented controls, evaluation results, unresolved limitations and release decision. |
| G-05 | **Operation and reassessment** | Are performance, impacts and conditions still acceptable? | Monitoring, feedback, incidents, assurance results and continued-use decision. |
| G-06 | **Change or retirement** | What requires reapproval, restriction, redesign or stopping? | Change decision, restriction, rollback or retirement plan, and retained records. |

Three responsibilities apply throughout:

- **Decision rights:** name the human or assigned role permitted to decide, accept risk, approve an exception, release, restrict or stop the use.
- **Policy:** translate organizational principles and obligations into rules, thresholds, required evidence and prohibited uses.
- **Escalation:** define where uncertainty, conflict, missing evidence, incidents and urgent exceptions go, including who can impose a temporary hold.

The forward connectors carry purpose records, review findings, decisions, conditions and evidence. They do not transfer accountability automatically. Feedback, incidents and material changes return to the responsible decision makers for reassessment. A monitoring system can trigger review; it cannot grant itself authority to accept a changed risk.

## Risk and impact domains

Each use needs a proportionate review across **security, privacy, safety, reliability, fairness, transparency, and effects on people and business**. The relevant specialists and depth depend on context. Independent assurance should remain distinguishable from implementation when the consequence warrants it.

These domains interact. A reliable system may still be unfair. A secure system may still be unsuitable for its stated purpose. A transparent explanation may still rest on weak evidence. The assessment should identify both each concern and the accountable decision owner.

## Organizational placement and authority

Security, GRC, a data or AI office, legal, technology, or another group may coordinate governance. Coordination maintains the process, records and interfaces; it does not silently transfer every business decision to that group. Business owners remain accountable for business outcomes under the organization's authority. Security makes security decisions within delegated authority. Privacy, legal, safety, data, finance, fraud, identity, recovery and other functions retain decisions assigned to them.

Map the responsibilities to the actual organization only after naming each decision, input, output and escalation path. Record when one person holds several roles and where independent review is required.

## Interface with the three AI security views

The accountable business, security, data, privacy, legal and other decision owners set purpose, conditions, authority and evidence requirements within their assigned roles. The security architectures implement and operate protections, identify threats and incidents, and return evidence for review.

| Security view | Governance provides | Security provides back |
|---|---|---|
| [01. Secure business AI](01-secure-business-ai.md) | Permitted purpose, data-use conditions, autonomy limits, release criteria and exception authority. | Access and action control evidence, workflow incidents, verified outcomes, control limitations and change signals. |
| [02. Defend against AI](02-defend-against-ai.md) | Risk priorities, tolerance, response authority, notification obligations and recovery conditions. | Threat scenarios, exposure evidence, detections, incidents, containment results and residual risk. |
| [03. Defend with AI](03-defend-with-ai.md) | Approved security purpose, evidence rules, action limits, human authority and improvement boundaries. | Source-linked findings, action records, execution outcomes, errors, misuse signals and evaluation results. |

The same supplier-payment event can use all three security views while finance remains accountable for the payment outcome. The assigned finance and risk owners decide whether an assistant may recommend or execute payment changes, who accepts the associated risk, what verification is required and what causes reconsideration. Security owners enforce access and action limits within their authority, investigate manipulation and supply evidence.

## Proposed design decisions

| ID | Decision and reason | Alternative and tradeoff | Revisit when |
|---|---|---|---|
| GOV-D01 | Organize around six connected responsibilities. They expose required decisions without prescribing a particular committee structure. | Organize by departments; familiar locally but difficult to reuse and can hide gaps between teams. | A deployment maps the responsibilities to named organizational processes. |
| GOV-D02 | Apply decision rights, policy and escalation across the lifecycle. A one-time approval cannot govern later changes and incidents. | Put governance only at intake; simpler but loses operational authority and reassessment. | A use is demonstrably static and a documented process still covers change and incidents. |
| GOV-D03 | Make feedback and material change return to decision makers. Evidence must be capable of changing conditions or stopping use. | Monitor only for reporting; creates records without a decision path. | Evidence shows another feedback destination has explicit authority. |
| GOV-D04 | Show security as a three-view interface. This preserves the security architecture while connecting it to broader governance. | Add governance as a fourth security view; visually tidy but conceptually misleading. | The series scope is explicitly redefined by its owner. |
| GOV-D05 | Review several risk and impact domains. Security is necessary but does not establish suitability, fairness, safety or business value. | Use a cybersecurity-only review; narrower and insufficient for AI governance. | The artifact is explicitly scoped to one technical control decision. |
| GOV-D06 | Treat built, bought, embedded and unmanaged as overlapping discovery prompts. | Use exclusive inventory categories; easier counting but misclassifies common combinations. | A local taxonomy preserves overlap through multiple attributes. |
| GOV-D07 | Reuse existing processes when they can perform the responsibility and produce required evidence. | Create a parallel AI approval system; consistent in appearance but likely to duplicate authority and records. | Existing processes leave a material decision, evidence or escalation gap. |

## Visual contract and accessible description

PNG: `04-ai-governance.png`. White background, landscape 16:9. Read the top band, then the six responsibility boxes, their evidence handoffs and feedback loop, followed by the risk domains and security interface. Navy indicates framing; blue indicates lifecycle responsibilities; teal indicates evidence, feedback and protective interfaces; gray provides scope and structure. Labels carry the meaning without color.

| Element ID | Exact visible copy | Meaning |
|---|---|---|
| G-TITLE | AI Governance | Architecture topic. |
| G-SUB | Direct and oversee AI use through named decisions, evidence and reassessment. | Purpose. |
| G-TOP | Decision rights · Policy · Escalation | Responsibilities that apply throughout. |
| G-01 | 1 / Purpose and ownership / What is it for, who is affected, and who answers for it? | Establish intent, affected parties and accountability. |
| G-02 | 2 / Risk and impact review / What could go wrong, and which obligations apply? | Identify concerns, participants and evidence gaps. |
| G-03 | 3 / Decision and conditions / May it proceed, with what limits and evidence? | Record authority, outcome, limits and triggers. |
| G-04 | 4 / Implementation and release / Have conditions been implemented and tested? | Translate conditions into controls and release evidence. |
| G-05 | 5 / Operation and reassessment / Are performance, impacts and conditions still acceptable? | Evaluate actual operation and continued suitability. |
| G-06 | 6 / Change or retirement / What requires reapproval, restriction, redesign or stopping? | Govern material change and end of use. |
| G-FEEDBACK | Feedback, incidents and material change return for reassessment | Explicit return from G-05 and G-06 to the responsible decision makers in G-01 through G-03. |
| G-RISK | Risk and impact domains / Security · Privacy · Safety · Reliability · Fairness · Transparency · Effects on people and business | Domains considered according to context. |
| G-SEC | AI security views / 01 Secure business AI / 02 Defend against AI / 03 Defend with AI | Peer security perspectives connected to governance. |
| G-IFACE | Decisions and conditions → protections; evidence → review | Two-way interface between the lifecycle responsibilities and the three security views. |
| G-NOTE | Connected responsibilities, not a universal approval sequence. | Reading rule. |
| G-FOOT | Reference architecture · Review draft · v0.1 · 09 Sep 2026 | Status and version. |

Connector labels are: `purpose + evidence`, `review findings`, `decision + conditions`, `release evidence`, and `operating evidence`. Each connector carries a record or decision to the next responsibility. It does not mean that a receiving team inherits the sender's authority or that every use must move left to right without iteration.

## Limits and review status

This architecture does not define an organization's risk tolerance, legal obligations, control thresholds, roles, products or approval bodies. A separate model-assisted review found no blocking content or visual defects in the governance package and revised overview. Human architectural review and reader comprehension testing remain open. Source-fidelity and visual checks establish artifact quality within their stated scope, not deployed effectiveness. See the [review status](review-status.md) and [detailed guide](guides/04-ai-governance-guide.md).

## Sources

NIST's [AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) informs the continuous governance, lifecycle, roles, inventory, monitoring and retirement concepts. NIST's [trustworthiness characteristics](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) support treating security as one of several related concerns. The [ISO/IEC 42001 overview](https://www.iso.org/standard/42001) supports an organization-wide management-system and continual-improvement context. Checked 9 September 2026. The six responsibilities, exact arrows, wording, worked example and layout are our proposed synthesis, not standard-defined diagrams or a conformity claim.
