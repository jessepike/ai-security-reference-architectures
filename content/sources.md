# Research basis

Checked 8–9 September 2026, America/Los_Angeles. This is a bounded review of current primary sources, not an exhaustive industry survey. Architecture names, component groupings, examples and acceptance checks are our proposed synthesis. No source endorses these diagrams or establishes their effectiveness.

## Sources and what they support

| ID | Primary source | Date / status observed | Use in this series |
|---|---|---|---|
| S1 | [NIST Cyber AI Profile project](https://www.nccoe.nist.gov/projects/cyber-ai-profile) and [IR 8596 initial preliminary draft](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8596.iprd.pdf) | December 2025 draft; project is reviewing comments | Three related perspectives: securing AI, countering AI-enabled attacks, and AI-enabled defense. Not a final compliance baseline. |
| S2 | [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and [linked document](https://genai.owasp.org/download/52117/?tmstv=1765059207) | Landing page dated 9 December 2025; linked PDF inspected | Threat review of agents, including goal manipulation, tool misuse, identity/privilege problems, supply-chain issues and memory/context poisoning. A risk taxonomy, not a full architecture. |
| S3 | [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) and [linked document](https://genai.owasp.org/download/56857/?tmstv=1785822482) | Landing page dated 3 August 2026; linked 2026 PDF inspected | Current LLM application guidance; prompt injection, output handling, context exposure and retrieval weaknesses inform threat selection. Avoid importing 2025 risk numbering. |
| S4 | [OWASP Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/) and [project repository](https://github.com/GenAI-Security-Project/agent-control-standard) | OWASP page dated 1 September 2026 | Emerging work on runtime hooks, policy enforcement and observability across agent frameworks. Availability does not establish interoperability, universal adoption or non-bypassability in a deployment. |
| S5 | [NCSC: Managing the cyber risk of agentic AI](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai) | 20 August 2026; explicitly interim practical advice | Proportionate autonomy, constraints outside prompts, restricted execution environments, oversight, monitoring and emergency shutdown. Formal guidance is still being developed. |
| S6 | [NCSC: Impact of AI on cyber threat from now to 2027](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027) | 7 May 2025; intelligence assessment | AI can improve attacker speed, scale and existing techniques. Its forward-looking judgments are forecasts, not proof of universal autonomous attacks. |
| S7 | [NCSC: Cyber Shield](https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence) | 7 July 2026; developing blueprint | Direction toward AI-assisted vulnerability work, detection and controlled mitigation. Broad autonomous defense remains an engineering and validation challenge. |
| S8 | [MITRE ATLAS](https://atlas.mitre.org/) | Living knowledge base, checked on research date | AI-specific adversary behavior and evidence levels. Supports scenario selection; does not imply every technique is observed in the wild. |
| S9 | [MITRE ATT&CK](https://attack.mitre.org/) | Living knowledge base, checked on research date | Enterprise attack behavior, applicable whether AI was involved or not. No static technique counts or unverified coverage claims are used. |
| S10 | [CISA: Implementing Phishing-Resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf) | Established guidance; official search excerpt reviewed | Phishing-resistant authentication as an identity baseline. Full document was not reviewed in this pass. |
| S11 | [NIST SP 800-63B-4: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) | Official publication checked during guide development on 8 September 2026 | Authentication context for the business-AI guide. Authentication does not by itself authorize a business transaction; no compliance claim is made. |
| S12 | [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Official AI Resource Center page checked 9 September 2026; page notes an AI RMF 1.0 revision is in progress | GOVERN as a cross-cutting lifecycle function; policies, roles, executive responsibility, inventories, monitoring, incident response and retirement. The six-box architecture is our synthesis, not the NIST diagram. |
| S13 | [NIST AI risks and trustworthiness](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) | Official AI Resource Center page checked 9 September 2026 | Security is one characteristic among validity and reliability, safety, resilience, accountability and transparency, explainability and interpretability, privacy enhancement and fairness with harmful bias managed. Used to show why governance extends beyond cybersecurity. |
| S14 | [ISO/IEC 42001:2023 overview](https://www.iso.org/standard/42001) | Published international standard; public ISO overview checked 9 September 2026 | Organization-wide AI management-system context and continual improvement. The public overview was used; this package is not a clause-by-clause interpretation or conformity assessment. |

## Interpretation

**Established foundations:** authenticated identities, least privilege, data access controls, secure delivery, segmentation, logging, incident handling and tested recovery remain necessary. AI-specific controls supplement these foundations.

**Evolving practice:** agent identities and delegation, protection of tool and memory boundaries, runtime interception, and evaluation of multi-step behavior need deployment-specific testing. A framework hook or model-based guardrail is not itself an enforcement guarantee.

**Our architectural proposals:** the exact boxes, cross-view connections, example policies and validation checks in this package. They are reviewable design recommendations, not claims that an external standard mandates the pictured arrangement.

**Governance scope:** NIST and ISO support continuous, organization-wide governance and management of AI risk. The responsibilities, arrows, authority language, arrival prompts and supplier-payment application in Architecture 04 are the authors' proposed synthesis. An earlier internal orientation was authorized only for conceptual comparison and adaptation; no non-public organizational claim is published as evidence.

**Design boundary:** this vendor-neutral series synthesizes the public sources above. No organization's deployed AI, licenses, products, data flows, controls or risk tolerance is represented.

## Research limitations

The official CISA ransomware-guide page returned HTTP 403; its full text was not used as reviewed evidence. Source dates above come from publisher pages or documents, not search-engine relative dates. The OWASP agentic document is identified by the publisher's linked artifact; no later point-version claim is made. Refresh this research before detailed product mapping or an implementation decision, especially if the NIST draft or agent-control guidance changes.
