# AI Security Reference Architectures — presentation source

**Status:** Proposed discussion draft, 9 September 2026. This deck teaches a logical reference series. It is not a deployment design, product recommendation, independent certification, or owner acceptance.

| # | Slide | Purpose | Upstream source |
|---|---|---|---|
| 1 | AI Security Reference Architectures | Introduce the series and its proposed status. | ../content/00-ai-security.md |
| 2 | How to use this deck | Explain reader path from familiar situation to design questions. | AUTHORING-STANDARD.md |
| 3 | Scope and status | State limits and discussion-draft conditions. | ../content/00-ai-security.md; ../content/source-map.md |
| 4 | AI security | Define the organizing idea. | 00-ai-security.md |
| 5 | Three views of one security program | Establish the peer views. | 00-ai-security.md |
| 6 | Shared foundation | Make ownership, access, data, evidence and recovery visible. | 00-ai-security.md |
| 7 | Series overview | Show the original overview visual once. | ../public/images/00-ai-security.png; ../content/00-ai-security.md |
| 8 | Supplier payment change | Establish the recurring illustrative example. | 00-ai-security.md |
| 9–13 | Secure business AI | Explain the question, visual, runtime limits, action controls and evidence. | ../content/01-secure-business-ai.md; guide 01 |
| 14–18 | Defend against AI | Explain the question, visual, attack paths, supplier fraud and recovery. | ../content/02-defend-against-ai.md; guide 02 |
| 19–23 | Defend with AI | Explain the question, visual, controlled action, operating modes and verification. | ../content/03-defend-with-ai.md; guide 03 |
| 24–28 | Shared interfaces | Show the contracts joining the three views and apply them to the recurring example. | 00-ai-security.md; guides 01–03 |
| 29–31 | Implementation questions | Turn logical architecture into deployment questions and testable checks. | guides 01–03 |
| 32–34 | Review findings, design questions and limits | Keep material reservations, unresolved questions and scope limits visible. | ../content/review-status.md |
| 35–37 | Appendix | Define terms, list sources and close with a discussion guide. | AUTHORING-STANDARD.md; canonical sources |

## Review note carried in every slide

This presentation is a proposed discussion draft. The original three architecture packages received a discussion-level review with material reservations; the review raised 30 findings, and substantive design questions remain open. The overview has not received independent review. Slides that describe a control or interface identify a proposed logical design, never a verified deployed capability. The detailed notes cite the governing canonical Markdown and relevant guide section.

## Source citations used in speaker notes

- `../content/00-ai-security.md`, 9 September 2026: narrative, peer views, connections, supplier-payment example, shared foundation.
- `../content/01-secure-business-ai.md` and `../content/guides/01-secure-business-ai-guide.md`, 8 September 2026: workflow controls, evidence and failure questions.
- `../content/02-defend-against-ai.md` and `../content/guides/02-defend-against-ai-guide.md`, 8 September 2026: attack paths, business verification, detection and recovery.
- `../content/03-defend-with-ai.md` and `../content/guides/03-defend-with-ai-guide.md`, 8 September 2026: analysis, authorization, execution, verification and operating modes.
- `../content/review-status.md`: open review findings and reviewer disposition.
- Source links in the canonical Markdown: NIST Cyber AI Profile, MITRE ATT&CK and ATLAS, NCSC agentic-AI guidance and Cyber Shield, OWASP GenAI LLM Top 10 and Agentic Applications Top 10, CISA phishing-resistant MFA guidance.
