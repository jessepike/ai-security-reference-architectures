# Review status and open design questions

Updated 9 September 2026 · Review draft

These are vendor-neutral reference architectures for discussion and detailed design. They do not describe a deployed environment or establish that a particular control is effective.

## What was reviewed

Claude Fable 5.1 reviewed each of the three component architectures together with its canonical Markdown, PNG, detailed guide and rendered guide PDF. All three received the disposition **“Suitable for architect discussion, with material reservations.”** The review covered the actual images and all 34 PDF pages. This is model-assisted critique, not independent certification or an assessment of a deployed system.

The overview and subsequent presentation and website were created after that review. Overview v0.2 and AI Governance v0.1 were also created after it. They are not covered by the original reviewer disposition. Do not describe Fable's earlier work as review of these changes. The public package preserves the design's discussion status and identifies the questions that still need resolution.

On 9 September 2026, a separate model-assisted review examined the revised overview and governance canonical source, guide, PNG and all 11 PDF pages. It found no blocking architectural or visual defect within that scope. Its advisory recommendation is to test whether readers understand the two-way governance/security interface without treating it as a hierarchy. This was not the original Fable review, a comprehensive standards audit, human acceptance or an assessment of deployed controls. [Review scope and result](https://github.com/jessepike/ai-security-reference-architectures/blob/main/docs/reviews/governance-v0.1.md).

The integrated opening story in overview v0.3 received a separate bounded model-assisted narrative review against the unchanged governance canonical source and guide. It found no blocking contradiction. An advisory scope clarification distinguished governance of the organization's AI from response to an attacker's AI; the author applied it and the reviewer confirmed its resolution. This review does not cover the resulting presentation or website. [Narrative review scope and result](https://github.com/jessepike/ai-security-reference-architectures/blob/main/docs/reviews/integrated-story-v0.3.md). Human architectural review and reader testing remain open.

On 14 September 2026, a three-reviewer model-assisted panel examined the frozen working material proposed for Applying Secure Business AI. Across three passes, the panel verified the original eight High corrections and the second-pass map identity correction. The third pass found one remaining High source-attribution ambiguity; it was corrected and locally verified after the panel and was not externally reviewed again. [Preview review scope and disposition](https://github.com/jessepike/ai-security-reference-architectures/blob/main/docs/reviews/applying-secure-business-ai-preview.md). This work does not close or reclassify the 30 findings below.

## Questions to resolve before implementation

| View | Principal open questions |
|---|---|
| Secure business AI | How is misuse within granted permission constrained? What happens when enforcement is unavailable? Where are hold/deny decisions recorded? Does the approver see the exact action that will execute? |
| Defend against AI | Which component owns the interface with business-AI safeguards? Do enforcement decisions reach detection? How is a manipulated security-AI recommendation prevented from causing harmful containment? |
| Defend with AI | What authorizes recovery or rollback? Which identity executes an action, and who is accountable? How does approval bind to the exact action? Can the improvement loop alter production capabilities outside its authority? |
| AI Governance | Which named role holds each decision right in the actual organization? Which existing processes can perform the six responsibilities? What makes a change material enough for reassessment? How are conflicting obligations and emergency exceptions resolved? What evidence is sufficient for release, continued operation and retirement? |
| Applying Secure Business AI | Do the six stages remain distinct from governance responsibilities? Are relevant decision owners and interim constraints clear without creating a mandatory committee? Does the map remain usable across built, bought, embedded, unmanaged, and agentic efforts? |

The review raised 30 findings in total, including clarification requests and formatting issues. The two High findings concern recovery authorization and execution identity in **Defend with AI**. Severity labels are reviewer judgments and have not been converted into an aggregate readiness score.

## How to use the material

Use the overview to establish shared understanding. Use the detailed guides to identify interfaces, responsibilities and acceptance evidence. Resolve the questions above against a specific workflow before translating the conceptual boxes into deployed services or granting automated action authority.

Treat a recommendation, an authorization, an attempted action and a verified outcome as separate states. A permitted action can still be the wrong action for the business. Recovery actions require appropriate authority too.

The public edition may include mechanical layout or spelling corrections. Such corrections do not close substantive review findings. The governance companion has the bounded model-assisted review described above; human review remains open. A future design revision should state which findings it accepts, rejects or resolves and identify the resulting source version.

## Give feedback

Email [jesse@jessepike.dev](mailto:jesse@jessepike.dev?subject=AI%20Security%20Reference%20Architectures%20feedback) with the architecture or section and what is unclear, missing or incorrect. No GitHub account is required. Technical contributors can also use [GitHub Issues](https://github.com/jessepike/ai-security-reference-architectures/issues).
