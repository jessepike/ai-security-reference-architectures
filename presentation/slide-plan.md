# AI Security Reference Architectures — presentation source

**Status:** Proposed discussion draft, Story v0.3, 9 September 2026. This deck teaches a logical AI-security reference series with a connected AI Governance companion. It is not a deployment design, product recommendation, independent certification, or owner acceptance.

| # | Slide | Purpose | Upstream source |
|---|---|---|---|
| 1 | AI Security and Governance | Introduce the shared story and its proposed status. | ../content/00-ai-security.md |
| 2 | How to use this deck | Explain reader path from familiar situation to design questions. | ../content/authoring-standard.md |
| 3 | Scope and status | State limits and discussion-draft conditions. | ../content/00-ai-security.md; ../content/source-map.md |
| 4–7 | Situation, coordination, AI arrival and data use | Start with a real decision, preserve workstream-versus-view distinction, discover overlap and assess appropriate data use. | ../content/00-ai-security.md; ../content/04-ai-governance.md |
| 8–10 | AI Governance companion | Teach how governance directs AI use, security protects it and evidence informs reassessment; show the governance visual once. | ../content/04-ai-governance.md; ../content/guides/04-ai-governance-guide.md; ../public/images/04-ai-governance.png |
| 11 | AI security | Show security advice before approval, protection in operation and evidence for later decisions. | ../content/00-ai-security.md |
| 12 | Three views of one security program | Establish the peer security views. | ../content/00-ai-security.md |
| 13 | Shared foundation | Make ownership, access, data, evidence and recovery visible. | ../content/00-ai-security.md |
| 14 | Three security views | Show the unchanged security overview visual once; it is not a joint governance-security diagram. | ../public/images/00-ai-security.png; ../content/00-ai-security.md |
| 15 | Supplier payment change | Establish the recurring illustrative example and its conditions/evidence loop. | ../content/00-ai-security.md |
| 16–20 | Secure business AI | Explain the question, visual, runtime limits, action controls and evidence. | ../content/01-secure-business-ai.md; guide 01 |
| 21–25 | Defend against AI | Explain the question, visual, attack paths, supplier fraud and recovery. | ../content/02-defend-against-ai.md; guide 02 |
| 26–30 | Defend with AI | Explain the question, visual, controlled action, operating modes and verification. | ../content/03-defend-with-ai.md; guide 03 |
| 31–35 | Governance-security exchanges | Show decisions/conditions moving to security and evidence/changes returning for reassessment; apply it to the example. | ../content/00-ai-security.md; guides 01–03 |
| 36–38 | Implementation questions | Turn recurring exchanges into deployment questions and testable checks. | guides 01–03 |
| 39–41 | Review findings, design questions and limits | Keep material reservations, unresolved questions and scope limits visible. | ../content/review-status.md |
| 42–44 | Appendix | Define terms, list sources and close with a discussion guide. | ../content/authoring-standard.md; canonical sources |

## Review note carried in every slide

This presentation is a proposed discussion draft. The original three architecture packages received a discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The AI Governance companion received an earlier bounded package review. Overview v0.3 received a separate bounded narrative review with no blockers. This deck itself has not received review, and human review remains open. Slides that describe a control or interface identify a proposed logical design, never a verified deployed capability. The detailed notes cite the governing canonical Markdown and relevant guide section.

## Source citations used in speaker notes

- `../content/00-ai-security.md`, 9 September 2026: narrative, peer views, connections, supplier-payment example, shared foundation.
- `../content/01-secure-business-ai.md` and `../content/guides/01-secure-business-ai-guide.md`, 8 September 2026: workflow controls, evidence and failure questions.
- `../content/02-defend-against-ai.md` and `../content/guides/02-defend-against-ai-guide.md`, 8 September 2026: attack paths, business verification, detection and recovery.
- `../content/03-defend-with-ai.md` and `../content/guides/03-defend-with-ai-guide.md`, 8 September 2026: analysis, authorization, execution, verification and operating modes.
- `../content/04-ai-governance.md` and `../content/guides/04-ai-governance-guide.md`, 9 September 2026: decision rights, lifecycle responsibilities, data-use conditions and security interfaces.
- `../content/review-status.md`: open review findings and reviewer disposition.
- Source links in the canonical Markdown: NIST Cyber AI Profile, MITRE ATT&CK and ATLAS, NCSC agentic-AI guidance and Cyber Shield, OWASP GenAI LLM Top 10 and Agentic Applications Top 10, CISA phishing-resistant MFA guidance.
