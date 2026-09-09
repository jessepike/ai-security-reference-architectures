# AI Security Reference Architectures — presentation manuscript

Derived from the exported PPTX. Review draft. Edit the canonical architecture sources and the deck builder before regenerating this review copy.

## Slide 1

AI Security
Reference Architectures
A proposed series for discussing how AI changes what we protect, how we are attacked, and how we defend
Conceptual reference  |  Version 0.1  |  9 September 2026

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Open by framing this as a teaching and architecture-discussion package. The deck makes proposed responsibilities and questions visible. It does not select products or approve an implementation.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Series authoring standard: https://ai.jessepike.dev/authoring-standard

## Slide 2

AI SECURITY REFERENCE ARCHITECTURES
How to use this deck
Familiar situation
Start with a business process, sensitive decision or security event.
What AI changes
AI may interpret content, use tools, or help an attacker or defender.
Architecture view
Use a peer view to ask the right security question.
Design evidence
Define authority, interfaces, tests and recovery before deployment.
Use the supplier-payment example to see the same event through all three views. Open the detailed guides when a box, connector or decision needs a more technical explanation.
Proposed discussion draft  |  Conceptual reference architecture
02

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Use this sequence to avoid starting with products or unexplained AI terms. The deck keeps the introductory reader and architect reader connected.

Sources: Series authoring standard: https://ai.jessepike.dev/authoring-standard

## Slide 3

AI SECURITY REFERENCE ARCHITECTURES
Scope and status
What this is
A proposed logical reference series for cybersecurity architecture discussion.
What this is not
A deployment blueprint, product selection, independent certification, or acceptance decision.
Status
The overview is proposed. The three original packages have discussion-level review with material reservations.
Proposed discussion draft  |  Conceptual reference architecture
03

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Pause here to keep the authority boundary clear. Readers can use the package to prepare choices and tests, but a real enterprise still needs owners, systems, requirements and acceptance evidence.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; CANONICAL-SOURCES.md; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 4

AI SECURITY REFERENCE ARCHITECTURES
AI security
AI security protects the organization as AI becomes part of its work, attackers’ methods, and its defenses.
The organizing idea: AI changes what we protect, how we are attacked, and how we defend.
The series takes a cybersecurity view. Business quality, privacy, safety and wider AI governance still matter, but they are not claimed as covered here.
Proposed discussion draft  |  Conceptual reference architecture
04

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Introduce an AI agent in ordinary terms: an AI-based workflow that can use tools to carry out parts of a task. It has no independent business authority or human accountability.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 5

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
These are peer perspectives. They overlap during real business events and do not form a maturity sequence.
Proposed discussion draft  |  Conceptual reference architecture
05

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Each architecture answers a different question about the same security program. Repeated capabilities across views require explicit interfaces and ownership; they are not duplicate products or teams.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 6

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
06

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Call out that these are common concerns rather than a centrally prescribed platform. The detailed implementation must assign real owners, systems and measurable acceptance conditions.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 7

ORIGINAL REFERENCE VISUAL
Series overview
Proposed discussion draft  |  Conceptual reference architecture
07

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Use this visual as an orientation map. Its relationship arrows mean responsibility dependencies, not network traffic, access rights, central ownership or automatic response.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; 00-ai-security.png

## Slide 8

AI SECURITY REFERENCE ARCHITECTURES
A familiar example: supplier payment change
Supplier request
A supplier asks to change bank details.
Business assistant
Reads the request and prepares a proposed change.
Decision point
A person or rule checks the actual target, scope and authority.
Payment outcome
The company pays the right supplier and records what occurred.
The recurring example is illustrative. It names no company, system or approved procedure.
Proposed discussion draft  |  Conceptual reference architecture
08

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Keep the business outcome fixed across all three views: pay the right supplier and keep the business running. The views reveal different protections and decisions around that goal.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 9

AI SECURITY REFERENCE ARCHITECTURES
01. Secure business AI
Question: What may our AI access and do?
An AI workflow can interpret documents and generate tool requests. It must not turn untrusted content or its own output into permission.
Design focus
Limit data access and actions. Bind authority to the initiator, task and current policy.
Proposed discussion draft  |  Conceptual reference architecture
09

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The familiar anchor is application security and access control. The AI-specific concern is that a workflow can reason over untrusted content and propose actions, so its output needs separate enforcement.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 10

ORIGINAL REFERENCE VISUAL
Secure business AI
Proposed discussion draft  |  Conceptual reference architecture
10

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Read from request through scoped task, restricted runtime, enforcement and resources. The bands are cross-cutting responsibilities, not a sequence. The dashed box marks the agent runtime boundary; enforcement remains outside it.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; 01-secure-business-ai.png

## Slide 11

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
11

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

This native teaching diagram elaborates the logical view. The real design must determine which calls can be intercepted, where final enforcement lives, how alternate paths are denied, and how controls reduce misuse within granted permissions.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 12

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
12

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The action check may represent several services. A content classifier can flag risk, but it cannot expand permissions. The receiving resource still needs a final access check.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 13

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
13

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

A hold and a denial have different operating meanings. Hold preserves a request for a valid decision or missing prerequisite. Denial terminates a prohibited attempt. Both need evidence and a defined disposition.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai

## Slide 14

AI SECURITY REFERENCE ARCHITECTURES
02. Defend against AI
Question: How do we stop attacks that AI helps attackers carry out?
AI can make familiar attacker behavior faster or more convincing. Defenses should respond to harmful behavior and business consequence without waiting for proof that AI was involved.
Design focus
Interrupt fraud, compromise, data loss and disruption through control boundaries, evidence and recovery.
Proposed discussion draft  |  Conceptual reference architecture
14

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The architecture does not treat AI as an adversary with intent. It focuses on observable attempts, defensive intervention and verified business recovery.

Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf

## Slide 15

ORIGINAL REFERENCE VISUAL
Defend against AI
Proposed discussion draft  |  Conceptual reference architecture
15

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Read each row across. Amber represents an attack attempt, teal represents an interrupting boundary, and blue represents a protected asset class. The rows are parallel examples, not a full taxonomy or incident sequence.

Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; 02-defend-against-ai.png

## Slide 16

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
16

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Use MITRE ATT&CK and ATLAS to select scenarios for detailed design. They help name possible behavior; they do not prove local occurrence or control effectiveness.

Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf

## Slide 17

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
17

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The decision does not depend on whether a detector labels a message synthetic. Phishing-resistant sign-in helps protect login but does not substitute for transaction authority and independent business verification.

Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf

## Slide 18

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
18

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The review calls for explicit interfaces between Architecture 02 and Architecture 01 enforcement decisions, including decision telemetry. Recovery must preserve access to response capabilities and recovery material where feasible.

Sources: Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 19

AI SECURITY REFERENCE ARCHITECTURES
03. Defend with AI
Question: How can AI help security act effectively and within limits?
AI can help correlate evidence, prioritize work and propose action. Permission, execution and verification require controls beyond a generated answer.
Design focus
Use AI assistance to improve security work while keeping decisions accountable and actions bounded.
Proposed discussion draft  |  Conceptual reference architecture
19

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Security AI itself needs the protections described in Architecture 01: identity, data, tools, runtime, audit and controlled changes. Architecture 03 adds the flow from evidence through verified outcome.

Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 20

ORIGINAL REFERENCE VISUAL
Defend with AI
Proposed discussion draft  |  Conceptual reference architecture
20

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Read the main flow left to right. The lower path returns tested updates to analysis only; it does not change authorization or execution controls. The dashed analysis boundary is a separation of responsibility, not an enforcement mechanism by itself.

Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; 03-defend-with-ai.png

## Slide 21

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
21

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The output of analysis is a proposal, not an executable command. Authorization is bound to an operation, target, scope, identity, validity and limits. Verification checks the destination system and service condition.

Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 22

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
22

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Mode selection belongs in the use-case record. A useful analytical result does not authorize later autonomous action.

Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 23

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
23

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Two High findings in the independent review concern recovery/rollback authorization and execution identity/delegation. This deck preserves them as open design questions; it does not claim they are resolved by the logical architecture.

Sources: Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 24

AI SECURITY REFERENCE ARCHITECTURES
Shared interfaces across the three views
Authority
Who may permit a specific action, exception or recovery step?
Identity
Which human, workload or delegated identity acts, and within what scope?
Evidence
Which source records show a decision, attempt, effect and recovery outcome?
Recovery
Who can stop, contain and restore when normal controls fail?
The same event can appear in every view. One implementation owner and clear interfaces avoid duplicated or conflicting controls.
Proposed discussion draft  |  Conceptual reference architecture
24

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The overview identifies shared responsibilities. The reviewer asks for a series-level reconciliation of delegated authority, approval records, enforcement telemetry and controlled recovery.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 25

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
25

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

An architect should model the approval as a record tied to the actual action rather than a narrative summary. Holds and denials also need records that support later investigation and operational disposition.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 26

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
26

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Avoid shared unrestricted service identities. A detailed design needs correlation between the initiator, workflow, delegation, authorization artifact and destination execution identity.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 27

AI SECURITY REFERENCE ARCHITECTURES
Evidence and telemetry contract
Source event
Preserve source identity, event time, collection status, classification and retention rule.
Enforcement decision
Record allow, hold or deny with policy version and reason.
Execution and outcome
Link destination response, verification evidence, ambiguity and reconciliation status.
Security response
Use the record for investigation, containment, recovery and evidence review.
Proposed discussion draft  |  Conceptual reference architecture
27

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Telemetry should include control-boundary decisions as well as assets and detections. The detailed design must decide availability, access, provenance, buffering and loss behavior for evidence.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 28

AI SECURITY REFERENCE ARCHITECTURES
Supplier payment change through three views
01. Secure business AI
The assistant can read permitted records and prepare the request. It cannot change the payment destination or authority.
02. Defend against AI
The company verifies the change through a trusted route and investigates suspicious account or transaction activity.
03. Defend with AI
A security assistant can correlate request, identity and application evidence. Any restriction or recovery action needs authority and verification.
Proposed discussion draft  |  Conceptual reference architecture
28

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Use this slide to show why one business event needs several architecture perspectives. It is illustrative, and the exact approval, separation-of-duties and recovery process depend on the enterprise.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 29

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
29

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

These questions turn a logical reference into detailed architecture work. The architecture does not supply universal thresholds, assigned owners or product selections.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 30

AI SECURITY REFERENCE ARCHITECTURES
From logical view to deployment design
Choose one use case
Name the business or security task, outcome, affected systems and prohibited actions.
Map real interfaces
Identify data, identity, policies, tools, destinations, evidence and recovery dependencies.
Define operating envelope
Select assistance mode, action limits, approval points, stops and fallback.
Test and decide
Run representative and hostile cases, verify outcomes, then seek accountable acceptance.
Proposed discussion draft  |  Conceptual reference architecture
30

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

This is a design sequence, not an adoption timeline. A real deployment needs its own security, business, privacy, continuity and change decisions.

Sources: Series authoring standard: https://ai.jessepike.dev/authoring-standard; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 31

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
31

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

These are example acceptance checks to adapt to business consequence and technical behavior. Passing a test does not create general assurance outside the tested scope. Within-permission misuse remains a design question for task constraints and review.

Sources: Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 32

AI SECURITY REFERENCE ARCHITECTURES
Model-assisted review: open findings
What the review observed
Fable 5.1 found useful authority separation and discussion-level architect use. It also noted a spelling error in the original 03 PNG.
What remains open
The review raised 30 findings. Mechanical public corrections were made; substantive design questions remain open. The overview has not had independent review.
The next revision should triage findings, decide which changes need canonical source updates, and preserve the frozen reviewed packages.
Proposed discussion draft  |  Conceptual reference architecture
32

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

This was a model-assisted review by Fable 5.1. Treat it as input to a subsequent series-level reconciliation. It is not an acceptance decision or deployment-ready certification.

Sources: Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 33

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
33

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

These questions include the two High Architecture 03 review findings and the cross-architecture interface work named in the review summary. They remain open for detailed design and owner decision.

Sources: Review status: https://ai.jessepike.dev/review-status | Model-assisted review summary: Fable 5.1

## Slide 34

AI SECURITY REFERENCE ARCHITECTURES
Limits of the reference series
Logical, not physical
A box may map to several services. The diagrams do not prescribe topology, product or network placement.
Cybersecurity scope
The series connects to privacy, safety and business-quality issues without claiming to cover them.
Evidence before confidence
A model explanation, tool acknowledgement or favorable demonstration does not establish local effectiveness.
Proposed discussion draft  |  Conceptual reference architecture
34

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Restate the practical boundary: technical authorization can still lead to an inaccurate, inappropriate or harmful business action. Business purpose and consequences inform the controls.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile

## Slide 35

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
35

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Use plain language first. These definitions help readers connect ordinary security practice to the architecture vocabulary.

Sources: Series authoring standard: https://ai.jessepike.dev/authoring-standard

## Slide 36

AI SECURITY REFERENCE ARCHITECTURES
Appendix: source basis
This series synthesizes proposed architecture patterns from its canonical Markdown and guides. The primary sources below inform risk selection and questions; they do not approve the design.
NIST Cyber AI Profile project
MITRE ATT&CK and ATLAS
NCSC guidance on agentic AI and Cyber Shield
OWASP GenAI LLM Top 10 and Agentic Applications Top 10
CISA guidance on phishing-resistant MFA
Complete links and source-status notes appear in the canonical Markdown and detailed guides.
Proposed discussion draft  |  Conceptual reference architecture
36

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

The canonical sources identify the date and status of each source. Examples and component arrangements in this deck are a proposed synthesis rather than a NIST, MITRE, NCSC, OWASP or CISA reference architecture.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Architecture 01: https://ai.jessepike.dev/architectures/01-secure-business-ai | Guide: https://ai.jessepike.dev/guides/01-secure-business-ai-guide | OWASP Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | NCSC agentic AI guidance: https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai; Architecture 02: https://ai.jessepike.dev/architectures/02-defend-against-ai | Guide: https://ai.jessepike.dev/guides/02-defend-against-ai-guide | MITRE ATT&CK: https://attack.mitre.org/ | MITRE ATLAS: https://atlas.mitre.org/ | CISA phishing-resistant MFA: https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf; Architecture 03: https://ai.jessepike.dev/architectures/03-defend-with-ai | Guide: https://ai.jessepike.dev/guides/03-defend-with-ai-guide | NCSC Cyber Shield: https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence | OWASP GenAI LLM Top 10: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

## Slide 37

AI SECURITY REFERENCE ARCHITECTURES
Discussion guide
A useful next conversation starts with one workflow or security task.
1
What outcome must the workflow or response protect?
2
What may the AI read, propose or do, and where does a person decide?
3
What source evidence verifies the action and supports recovery if it goes wrong?
Use the detailed guides to prepare the architecture, evidence and owner decisions for that single use case.
Proposed discussion draft  |  Conceptual reference architecture
37

### Speaker notes

Presentation-wide status: Proposed discussion draft. The three original packages received discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. No slide asserts deployment approval, certification, or demonstrated effectiveness.

Close by moving from the reference series to a bounded, accountable design conversation. No deployment decision follows from this deck alone.

Sources: Series source: https://ai.jessepike.dev/ | NIST Cyber AI Profile: https://www.nccoe.nist.gov/projects/cyber-ai-profile; Series authoring standard: https://ai.jessepike.dev/authoring-standard

