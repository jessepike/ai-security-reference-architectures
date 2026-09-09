# AI Security Reference Architectures — presentation manuscript

Derived from the exported PPTX. Review draft. Edit the canonical architecture sources and deck builder before regenerating this review copy.

## Slide 1

AI Security and
Governance
A proposed series about how governance directs AI use, security protects it, and evidence informs the next decision.
Conceptual reference  |  Story v0.3  |  9 September 2026

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Open with the common story: governance directs AI use, security protects it, and evidence from real use informs the next decision. This is a teaching and architecture-discussion package. It does not select products or approve an implementation.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Series authoring standard: https://ai.jessepike.dev/authoring-standard; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 2

AI SECURITY REFERENCE ARCHITECTURES
How to use this deck
Situation
Start with a real use, consequence, owner and next decision.
Governance
Set the purpose, conditions, evidence and reassessment trigger.
Security
Shape safeguards early, implement protections and report results.
Evidence returns
Use real results to continue, restrict, redesign or stop.
Use the supplier-payment example to see governance set conditions, security carry them into protections, and evidence return for reassessment.
Proposed discussion draft  |  Conceptual reference architecture
02

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Use this sequence to avoid starting with products or unexplained AI terms. Governance and security exchange decisions and evidence throughout the use life; this is not a fixed approval sequence.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 3

AI SECURITY REFERENCE ARCHITECTURES
Scope and status
What this is
A proposed security and governance reference series for connected architecture discussion.
What this is not
A deployment blueprint, product selection, independent certification, or acceptance decision.
Status
Overview v0.3 and governance: bounded reviews. Deck and human review open.
Proposed discussion draft  |  Conceptual reference architecture
03

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Pause here to keep the authority boundary clear. Readers can use the package to prepare choices and tests, but a real enterprise still needs owners, systems, requirements and acceptance evidence. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself and human review remain open.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 4

AI SECURITY REFERENCE ARCHITECTURES
Start with the situation and next decision
Real situation
Name the AI use, affected people, data, actions and business consequence.
Purpose and owner
Identify who answers for the outcome and what use may be appropriate.
Security advice early
Assess threats, safeguards, constraints and evidence gaps before approval.
Decision and conditions
Proceed, add conditions, pause, narrow, redesign or stop.
Proposed discussion draft  |  Conceptual reference architecture
04

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Begin with a real situation, not a product category. Security advice helps authorized decision makers judge whether a use is appropriate and feasible before release. Ownership follows the decision and consequence.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 5

AI SECURITY REFERENCE ARCHITECTURES
Coordination and decision rights
Coordination
Security, GRC, an AI office or another function can bring the people and evidence together.
Decision rights
Business, security, privacy, legal, data and other specialists keep the decisions assigned to them.
Coordination makes the work visible. It does not grant every decision right or replace an existing incident authority.
Proposed discussion draft  |  Conceptual reference architecture
05

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The coordinator can route work and assemble evidence without becoming the owner of every business outcome or risk. A workstream selects the current decision; a security architecture view makes the related protections visible. The enterprise needs explicit allocation of release, exception, stop and incident decisions.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 6

AI SECURITY REFERENCE ARCHITECTURES
How AI arrives: four overlapping questions
Built
Was it developed or assembled by the organization?
Bought
Is it supplied as a service or purchased product?
Embedded
Does an existing product contain an AI feature?
Unmanaged
Has the use not entered normal oversight?
Ask every question. A bought product may have embedded AI, and any built, bought or embedded use may be unmanaged.
Proposed discussion draft  |  Conceptual reference architecture
06

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These are discovery prompts, not mutually exclusive inventory categories. The purpose is to find the real use and oversight gap before assigning a route or control response.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 7

AI SECURITY REFERENCE ARCHITECTURES
Permitted data use needs two decisions
Access
May this identity reach the data?
Security controls identity, resource, operation, destination and retention.
Appropriate use
May this data be used for this purpose, with adequate evidence and obligations to affected people?
Access alone does not establish appropriate use. Missing evidence can justify a pause, narrower conditions, redesign or stopping.
Proposed discussion draft  |  Conceptual reference architecture
07

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Security access enforcement remains necessary. Governance adds the purpose and suitability question: whether the proposed data use is allowed and appropriate for the context. Neither answer substitutes for the other.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 8

AI SECURITY REFERENCE ARCHITECTURES
AI governance and AI security
AI governance
Direct AI use: set purpose, conditions, required evidence and when to reassess.
AI security
Protect the work: advise early, implement safeguards and return security evidence.
Governance directs AI use. Security protects it. Evidence from real use informs the next decision.
Proposed discussion draft  |  Conceptual reference architecture
08

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Governance and security exchange decisions and evidence throughout the AI use life. Governance connects to the three peer security views; it does not create a fourth security category. Governance extends beyond cybersecurity to purpose, privacy, reliability, safety, fairness, transparency, and effects on people and business.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 9

AI SECURITY REFERENCE ARCHITECTURES
AI governance: six connected responsibilities
Purpose and ownership
What is it for, who is affected, and who answers for it?
Risk and impact review
What could go wrong, and which obligations apply?
Decision and conditions
May it proceed, with what limits and evidence?
Implementation and release
Have conditions been implemented and tested?
Operation and reassessment
Do security and outcome evidence still support the conditions?
Change or retirement
What requires reapproval, restriction, redesign or stopping?
Proposed discussion draft  |  Conceptual reference architecture
09

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These responsibilities are connected and may be revisited. Security advice helps assess proposed use before approval, and operation returns security evidence alongside business and other impact evidence. Decision rights, policy and escalation apply throughout.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 10

ORIGINAL REFERENCE VISUAL
AI Governance
Proposed discussion draft  |  Conceptual reference architecture
10

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Read the top band, six responsibilities and their evidence handoffs, then the feedback loop, risk domains and security interface. Connector labels carry records or decisions; they do not transfer accountability automatically. The governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself and human review remain open.
Sources: AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1; 04-ai-governance.png

## Slide 11

AI SECURITY REFERENCE ARCHITECTURES
AI security
AI security protects the organization as AI becomes part of its work, attackers’ methods, and its defenses.
It helps shape conditions before approval, protects the work in operation and returns evidence for later decisions.
The three views below retain a cybersecurity scope. Governance uses their evidence but also considers purpose, privacy, reliability, safety and other impacts.
Proposed discussion draft  |  Conceptual reference architecture
11

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Security advice helps authorized decision makers judge whether a proposed AI use is feasible and what safeguards, constraints and evidence gaps matter. It does not decide every business or wider-risk question.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 12

AI SECURITY REFERENCE ARCHITECTURES
Three views of one security program
01  Secure business AI
What may our AI access and do?
Builds on application security, data protection and access control.
02  Defend against AI
How do we stop AI-enabled attacks?
Builds on fraud prevention, detection and incident response.
03  Defend with AI
How can AI help security act within limits?
Builds on investigation, playbooks and controlled automation.
Three peer security perspectives support governance conditions and return evidence. They do not form a maturity sequence.
Proposed discussion draft  |  Conceptual reference architecture
12

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These remain three peer security perspectives, not a joint governance-security diagram. Each answers a different security question about the same business event. Governance connects to them through conditions and evidence.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 13

AI SECURITY REFERENCE ARCHITECTURES
Shared foundation
Ownership
Purpose, consequence, exception and change decisions need accountable people.
Access rules
People, applications and AI workflows receive task-appropriate permissions.
Data protection
Sensitivity, origin, permitted destinations and retention shape use.
Evidence
Records from source systems reconstruct decisions and check outcomes.
Recovery
People can stop, contain and restore. Recovery actions have their own authority.
Proposed discussion draft  |  Conceptual reference architecture
13

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Call out that these are common concerns rather than a centrally prescribed platform. The detailed implementation must assign real owners, systems and measurable acceptance conditions.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 14

ORIGINAL REFERENCE VISUAL
Three security views
Proposed discussion draft  |  Conceptual reference architecture
14

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
This unchanged visual orients the reader to the three security views. It does not depict the governance-security relationship. Its relationship arrows mean responsibility dependencies, not network traffic, access rights, central ownership or automatic response. Overview v0.3 received a separate bounded narrative review; this deck itself and human review remain open.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1; 00-ai-security.png

## Slide 15

AI SECURITY REFERENCE ARCHITECTURES
A familiar example: supplier payment change
Supplier request
A supplier asks to change bank details.
AI proposal
The assistant reads specified records and prepares a proposed change.
Conditions and checks
The owner sets permitted use; security advises; a trusted route verifies.
Outcome and evidence
Payment evidence informs whether conditions should continue or change.
The recurring example is illustrative. It names no company, system or approved procedure.
Proposed discussion draft  |  Conceptual reference architecture
15

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Governance names the payment-process owner, appropriate assistance, evidence before release, stop authority and reassessment triggers. Security helps shape conditions by assessing fraud, access and workflow risks before use begins. The three security views then protect the same objective: pay the right supplier and keep the business running.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 16

AI SECURITY REFERENCE ARCHITECTURES
01. Secure business AI
Question: What may our AI access and do?
An AI workflow can interpret documents and generate tool requests. It must not turn untrusted content or its own output into permission.
Design focus
Limit data access and actions. Bind authority to the initiator, task and current policy.
Proposed discussion draft  |  Conceptual reference architecture
16

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The familiar anchor is application security and access control. The AI-specific concern is that a workflow can reason over untrusted content and propose actions, so its output needs separate enforcement.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 17

ORIGINAL REFERENCE VISUAL
Secure business AI
Proposed discussion draft  |  Conceptual reference architecture
17

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Read from request through scoped task, restricted runtime, enforcement and resources. The bands are cross-cutting responsibilities, not a sequence. The dashed box marks the agent runtime boundary; enforcement remains outside it.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; 01-secure-business-ai.png

## Slide 18

AI SECURITY REFERENCE ARCHITECTURES
Secure business AI: a controlled workflow
Request and identity
Capture requester, purpose and account scope.
Restricted runtime
The agent coordinates permitted steps inside set limits.
Action check
Independent policy checks caller, target and operation.
Destination evidence
The receiving system records the result.
Teaching diagram: the proposed action passes through an independent check. Model output cannot grant permission.
Proposed discussion draft  |  Conceptual reference architecture
18

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
This native teaching diagram elaborates the logical view. The real design must determine which calls can be intercepted, where final enforcement lives, how alternate paths are denied, and how controls reduce misuse within granted permissions.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 19

AI SECURITY REFERENCE ARCHITECTURES
Access and action checks
Inputs to evaluate
Caller and represented identity
Resource and operation
Target, parameters and destination
Task context and policy version
Possible dispositions
Allow a scoped operation
Hold for a valid decision
Deny with a reason
Check returned results before reuse
A human approval must bind to the exact action. A changed target, amount or destination requires a new decision.
Proposed discussion draft  |  Conceptual reference architecture
19

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The action check may represent several services. A content classifier can flag risk, but it cannot expand permissions. The receiving resource still needs a final access check.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 20

AI SECURITY REFERENCE ARCHITECTURES
Evidence, holds and recovery
Trace
Link task, authorization, resource and result records.
Verify
Use business-system evidence, not agent narration.
Stop or revoke
Prevent future work and reconcile in-flight effects.
Recover
Verify business process and data after restoration.
Open questions: who decides a hold, what if policy or audit delivery is unavailable, how do rights changes affect queued work, and how is within-permission misuse limited?
Proposed discussion draft  |  Conceptual reference architecture
20

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
A hold and a denial have different operating meanings. Hold preserves a request for a valid decision or missing prerequisite. Denial terminates a prohibited attempt. Both need evidence and a defined disposition.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 21

AI SECURITY REFERENCE ARCHITECTURES
02. Defend against AI
Question: How do we stop attacks that AI helps attackers carry out?
AI can make familiar attacker behavior faster or more convincing. Defenses should respond to harmful behavior and business consequence without waiting for proof that AI was involved.
Design focus
Interrupt fraud, compromise, data loss and disruption through control boundaries, evidence and recovery.
Proposed discussion draft  |  Conceptual reference architecture
21

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The architecture does not treat AI as an adversary with intent. It focuses on observable attempts, defensive intervention and verified business recovery. Attackers' AI use does not create an enterprise AI use for governance to approve. Existing security and business authority applies. If an attack affects the enterprise's AI use, evidence informs its governance reassessment.
Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 22

ORIGINAL REFERENCE VISUAL
Defend against AI
Proposed discussion draft  |  Conceptual reference architecture
22

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Read each row across. Amber represents an attack attempt, teal represents an interrupting boundary, and blue represents a protected asset class. The rows are parallel examples, not a full taxonomy or incident sequence.
Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; 02-defend-against-ai.png

## Slide 23

AI SECURITY REFERENCE ARCHITECTURES
Three representative attack paths
Impersonation and fraud
Convincing messages and identities can seek a sensitive business change.
Automated intrusion
Faster discovery and exploitation can expand a compromise path.
Attacks on AI workflows
Hostile content and tool abuse can redirect a connected workflow.
Each path needs a real interruption point. The middle control boundary must produce evidence for investigation and recovery.
Proposed discussion draft  |  Conceptual reference architecture
23

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Use MITRE ATT&CK and ATLAS to select scenarios for detailed design. They help name possible behavior; they do not prove local occurrence or control effectiveness.
Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf

## Slide 24

AI SECURITY REFERENCE ARCHITECTURES
Supplier-change impersonation
Convincing request
A message, voice or compromised account asks for bank-detail change.
Independent verification
Use a known contact route and the actual supplier-change approval process.
Investigate
Correlate request, verification, account, approval and transaction events.
Contain and reconcile
Revoke access, pause or reconcile a transaction, then verify the supplier record.
Proposed discussion draft  |  Conceptual reference architecture
24

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The decision does not depend on whether a detector labels a message synthetic. Phishing-resistant sign-in helps protect login but does not substitute for transaction authority and independent business verification.
Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf

## Slide 25

AI SECURITY REFERENCE ARCHITECTURES
Recovery means a usable business service
Containment
Revoke sessions, isolate systems or block harmful transfers under pre-agreed authority.
Restoration
Restore from protected material and bring the service back through the intended recovery procedure.
Verification
Check service, data, access state and reconciliation evidence. A rebuilt component is not enough.
Open design question: which response and recovery actions have authority, and how do their decisions feed security telemetry?
Proposed discussion draft  |  Conceptual reference architecture
25

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The review calls for explicit interfaces between Architecture 02 and Architecture 01 enforcement decisions, including decision telemetry. Recovery must preserve access to response capabilities and recovery material where feasible.
Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 26

AI SECURITY REFERENCE ARCHITECTURES
03. Defend with AI
Question: How can AI help security act effectively and within limits?
AI can help correlate evidence, prioritize work and propose action. Permission, execution and verification require controls beyond a generated answer.
Design focus
Use AI assistance to improve security work while keeping decisions accountable and actions bounded.
Proposed discussion draft  |  Conceptual reference architecture
26

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Security AI itself needs the protections described in Architecture 01: identity, data, tools, runtime, audit and controlled changes. Architecture 03 adds the flow from evidence through verified outcome.
Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 27

ORIGINAL REFERENCE VISUAL
Defend with AI
Proposed discussion draft  |  Conceptual reference architecture
27

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Read the main flow left to right. The lower path returns tested updates to analysis only; it does not change authorization or execution controls. The dashed analysis boundary is a separation of responsibility, not an enforcement mechanism by itself.
Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; 03-defend-with-ai.png

## Slide 28

AI SECURITY REFERENCE ARCHITECTURES
Evidence to verified outcome
Security evidence
Source records with provenance, freshness and access limits.
AI analysis
Correlate evidence. Show sources and uncertainty.
Authorization
Check target, scope, policy and current conditions.
Controlled execution
A constrained adapter enforces the operation.
Outcome verification
Destination evidence confirms effect or keeps the case open.
Proposed discussion draft  |  Conceptual reference architecture
28

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The output of analysis is a proposal, not an executable command. Authorization is bound to an operation, target, scope, identity, validity and limits. Verification checks the destination system and service condition.
Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 29

AI SECURITY REFERENCE ARCHITECTURES
Selectable operating modes
Assist
Summarize a case or correlate evidence.
Scoped read access. Evidence remains visible. No production action.
Recommend
Propose a containment or remediation step.
Show evidence, affected assets, consequence and uncertainty for review.
Act within limits
Execute a tested response inside an authorized procedure.
Enforce target, scope and limits; verify result; allow intervention.
These are operating choices for a use case. They are not a maturity ladder.
Proposed discussion draft  |  Conceptual reference architecture
29

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Mode selection belongs in the use-case record. A useful analytical result does not authorize later autonomous action.
Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 30

AI SECURITY REFERENCE ARCHITECTURES
Verification, recovery and uncertainty
Execution response
The adapter reports what it attempted and received.
Destination evidence
The receiving system and service health show actual state.
Uncertain outcome
Conflicting or missing evidence keeps the case open for escalation.
Recovery decision
An authorized path determines containment, rollback or service recovery.
Open review finding: recovery and rollback need an explicit authorization path. Execution also needs an accountable identity and delegation model.
Proposed discussion draft  |  Conceptual reference architecture
30

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Two High findings in the independent review concern recovery/rollback authorization and execution identity/delegation. This deck preserves them as open design questions; it does not claim they are resolved by the logical architecture.
Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 31

AI SECURITY REFERENCE ARCHITECTURES
How governance and security work together
Assess together
Purpose, affected people, actions, threats, safeguards and evidence gaps.
Conditions to protections
Security and delivery teams implement relevant limits, checks and recovery arrangements.
Evidence from operation
Security, business and other evidence shows what actually happens.
Respond and reconsider
Authorized responders contain harm; decision makers update conditions.
Decisions and conditions travel to security. Evidence and changes return for reassessment. Coordination does not grant every decision right.
Proposed discussion draft  |  Conceptual reference architecture
31

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These are recurring exchanges, not a fixed approval sequence. Existing incident procedures should give named responders authority for urgent protective action within agreed limits. Incident and recovery evidence then feed subsequent reassessment, which has its own appropriate authority.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 32

AI SECURITY REFERENCE ARCHITECTURES
Action and approval contract
Action request
Which operation, target, material parameters, intended effect, task and evidence support this request?
Decision
Which policy version, decision owner, validity conditions and disposition apply?
Approval binding
Can a changed target, amount or destination reuse the approval? It should not.
Execution result
Which destination identifier and reconciliation status show what happened?
Proposed discussion draft  |  Conceptual reference architecture
32

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
An architect should model the approval as a record tied to the actual action rather than a narrative summary. Holds and denials also need records that support later investigation and operational disposition.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 33

AI SECURITY REFERENCE ARCHITECTURES
Execution identity and delegation contract
Initiating identity
Who started the task, and what business purpose and account scope apply?
Workflow identity
Which non-human identity coordinates the permitted work, and what rights expire?
Destination identity
Which controlled identity executes the bounded call, and how does the destination verify it?
Open question: how does a delegated child workflow retain task attribution without exceeding the original authority?
Proposed discussion draft  |  Conceptual reference architecture
33

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Avoid shared unrestricted service identities. A detailed design needs correlation between the initiator, workflow, delegation, authorization artifact and destination execution identity.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 34

AI SECURITY REFERENCE ARCHITECTURES
Evidence from security to decisions
Source event
Preserve source identity, event time, collection status, classification and retention rule.
Enforcement decision
Record allow, hold or deny with policy version and reason.
Execution and outcome
Link destination response, verification evidence, ambiguity and reconciliation status.
Decision evidence
Use security results for response and governance reassessment.
Proposed discussion draft  |  Conceptual reference architecture
34

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Telemetry should include control-boundary decisions as well as assets and detections. Security results are one input to reassessment alongside business outcome, quality and other impact evidence. The detailed design must decide availability, access, provenance, buffering and loss behavior for evidence.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 35

AI SECURITY REFERENCE ARCHITECTURES
Supplier payment: governance and security
Governance
Names permitted assistance, release evidence, stop authority and reassessment triggers.
01. Secure business AI
Limits the assistant to permitted records and proposed changes.
02. Defend against AI
Verifies through a trusted route and investigates suspicious activity.
03. Defend with AI
Correlates evidence. Restriction and recovery still need authority and verification.
Proposed discussion draft  |  Conceptual reference architecture
35

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
If records show repeated wrong bank proposals, the payment owner may restrict or pause the assistant even without an attack. If a new tool would let it update bank details directly, the changed permissions and consequences need assessment. An AI-enabled attack still uses the normal security and business response authority.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 36

AI SECURITY REFERENCE ARCHITECTURES
Implementation questions
Business consequence
What loss or service impact is unacceptable, and who owns that decision?
Scope
What smallest data access, target and action remain useful for the task?
Authority
Which cases require a human decision, and what binds that decision to the action?
Evidence
Which system can independently show the intended effect and any unintended consequence?
Continuity
What happens when policy, identity, telemetry, model, tool adapter or destination system is unavailable?
Proposed discussion draft  |  Conceptual reference architecture
36

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These questions turn a logical reference into detailed architecture work. The architecture does not supply universal thresholds, assigned owners or product selections.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 37

AI SECURITY REFERENCE ARCHITECTURES
From logical view to deployment design
Assess together
Name purpose, affected people, actions, threats, safeguards and evidence gaps.
Set conditions
Record permitted use, limits, checks, exceptions and recovery authority.
Implement and operate
Test protections, use them in work and preserve security and outcome evidence.
Respond and reassess
Contain harm within authority; update conditions before continued use.
Proposed discussion draft  |  Conceptual reference architecture
37

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These recurring exchanges are not a fixed approval sequence. A real deployment needs its own security, business, privacy, continuity and change decisions. Existing incident responders can take urgent protective action within agreed limits, then feed the incident and recovery evidence into reassessment.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Series authoring standard: https://ai.jessepike.dev/authoring-standard

## Slide 38

AI SECURITY REFERENCE ARCHITECTURES
Testable acceptance checks
Hostile-content resistance
Insert a malicious instruction in test evidence. Confirm it cannot change policy, expand scope or trigger an unauthorized action.
Independent authorization
Attempt an altered or model-generated action directly. Confirm controlled execution rejects it without a bounded authorization.
Verification and continuity
Simulate ambiguous result, policy failure and AI outage. Confirm the case stays open and people can follow the non-AI procedure.
Acceptance evidence should trace source evidence, proposal, authorization, execution, verification and disposition.
Proposed discussion draft  |  Conceptual reference architecture
38

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These are example acceptance checks to adapt to business consequence and technical behavior. Passing a test does not create general assurance outside the tested scope. Within-permission misuse remains a design question for task constraints and review.
Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 39

AI SECURITY REFERENCE ARCHITECTURES
Model-assisted review: open findings
What the review observed
Fable 5.1 found useful authority separation and discussion-level architect use. It also noted a spelling error in the original 03 PNG.
What remains open
The review raised 30 findings. Mechanical public corrections were made; substantive design questions remain open. Human review remains open.
The next revision should triage findings, decide which changes need canonical source updates, and preserve the frozen reviewed packages.
Proposed discussion draft  |  Conceptual reference architecture
39

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
This slide summarizes the Fable 5.1 review of the original packages. The governance companion had an earlier bounded package review. Overview v0.3 had a separate bounded narrative review. None is an acceptance decision or human review, and the deck itself has not received review.
Sources: Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 40

AI SECURITY REFERENCE ARCHITECTURES
Material design questions to resolve
Recovery authorization
Who may invoke rollback, containment or restoration, under which bounded conditions?
Execution identity
Which accountable identity acts at the destination, and how is delegation traceable?
Approval binding
How does a human view and approve the exact target, scope and material parameters?
Enforcement telemetry
How do allow, hold and deny decisions enter the evidence and investigation path?
AI unavailable or manipulated
How do people continue essential work and retain authority when AI assistance cannot be trusted?
Proposed discussion draft  |  Conceptual reference architecture
40

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
These questions include the two High Architecture 03 review findings and the cross-architecture interface work named in the review summary. They remain open for detailed design and owner decision.
Sources: Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 41

AI SECURITY REFERENCE ARCHITECTURES
Limits of the reference series
Logical, not physical
A box may map to several services. The diagrams do not prescribe topology, product or network placement.
Cybersecurity scope
Governance is broader than cyber. Privacy, safety, reliability and other expertise retain their own decisions.
Evidence before confidence
A model explanation, tool acknowledgement or favorable demonstration does not establish local effectiveness.
Proposed discussion draft  |  Conceptual reference architecture
41

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Technical authorization can still lead to an inaccurate, inappropriate or harmful business action. Security evidence is relevant to reassessment but does not create a complete treatment of wider AI risks or centralize all decision rights.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001

## Slide 42

AI SECURITY REFERENCE ARCHITECTURES
Appendix: terms used in this deck
Authorization
Deciding whether an identity may perform an action on a target in the current context.
Non-human identity
An identity assigned to an application or automated workflow.
Prompt injection
Untrusted content that tries to redirect an AI workflow or misuse its permitted access.
Provenance
Where information came from and how it was obtained.
Autonomy limit
Actions a workflow may take without a new human decision.
Proposed discussion draft  |  Conceptual reference architecture
42

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Use plain language first. These definitions help readers connect ordinary security practice to the architecture vocabulary.
Sources: Series authoring standard: https://ai.jessepike.dev/authoring-standard

## Slide 43

AI SECURITY REFERENCE ARCHITECTURES
Source basis
This series synthesizes proposed architecture patterns from its canonical Markdown and guides. The primary sources below inform risk selection and questions; they do not approve the design.
NIST Cyber AI Profile project
NIST AI RMF and ISO/IEC 42001
MITRE ATT&CK and ATLAS
NCSC guidance on agentic AI and Cyber Shield
OWASP GenAI LLM Top 10 and Agentic Applications Top 10
CISA guidance on phishing-resistant MFA
Complete links and source-status notes appear in the canonical Markdown and detailed guides.
Proposed discussion draft  |  Conceptual reference architecture
43

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
The canonical sources identify the date and status of each source. Examples and component arrangements in this deck are a proposed synthesis rather than a NIST, ISO, MITRE, NCSC, OWASP or CISA reference architecture.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 44

AI SECURITY REFERENCE ARCHITECTURES
Discussion guide
A useful next conversation starts with one workflow or security task.
1
What outcome, purpose and accountable owner define this use?
2
What conditions and security safeguards must apply before release?
3
What evidence, change or incident should trigger reassessment?
Use the detailed guides to prepare the architecture, evidence and owner decisions for that single use case.
Proposed discussion draft  |  Conceptual reference architecture
44

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review. This deck itself has not received review, and human review remains open. No slide asserts deployment approval, certification, or demonstrated effectiveness.
Close by moving from the reference series to a bounded, accountable design conversation. Security and other specialists supply evidence; the people who hold decision rights decide whether to continue, restrict, redesign or stop. No deployment decision follows from this deck alone.
Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; AI Governance: https://ai.jessepike.dev/architectures/04-ai-governance | Guide: https://ai.jessepike.dev/guides/04-ai-governance-guide | NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | NIST trustworthiness characteristics: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ | ISO/IEC 42001 overview: https://www.iso.org/standard/42001; Series authoring standard: https://ai.jessepike.dev/authoring-standard
