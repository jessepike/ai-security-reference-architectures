# Review status and open design questions

Updated 9 September 2026 · Review draft

These are vendor-neutral reference architectures for discussion and detailed design. They do not describe a deployed environment or establish that a particular control is effective.

## What was reviewed

Claude Fable 5.1 reviewed each of the three component architectures together with its canonical Markdown, PNG, detailed guide and rendered guide PDF. All three received the disposition **“Suitable for architect discussion, with material reservations.”** The review covered the actual images and all 34 PDF pages. This is model-assisted critique, not independent certification or an assessment of a deployed system.

The overview and subsequent presentation and website were created after that review. They are not covered by the original reviewer disposition. The public package preserves the design's discussion status and identifies the questions that still need resolution.

## Questions to resolve before implementation

| View | Principal open questions |
|---|---|
| Secure business AI | How is misuse within granted permission constrained? What happens when enforcement is unavailable? Where are hold/deny decisions recorded? Does the approver see the exact action that will execute? |
| Defend against AI | Which component owns the interface with business-AI safeguards? Do enforcement decisions reach detection? How is a manipulated security-AI recommendation prevented from causing harmful containment? |
| Defend with AI | What authorizes recovery or rollback? Which identity executes an action, and who is accountable? How does approval bind to the exact action? Can the improvement loop alter production capabilities outside its authority? |

The review raised 30 findings in total, including clarification requests and formatting issues. The two High findings concern recovery authorization and execution identity in **Defend with AI**. Severity labels are reviewer judgments and have not been converted into an aggregate readiness score.

## How to use the material

Use the overview to establish shared understanding. Use the detailed guides to identify interfaces, responsibilities and acceptance evidence. Resolve the questions above against a specific workflow before translating the conceptual boxes into deployed services or granting automated action authority.

Treat a recommendation, an authorization, an attempted action and a verified outcome as separate states. A permitted action can still be the wrong action for the business. Recovery actions require appropriate authority too.

The public edition may include mechanical layout or spelling corrections. Such corrections do not close substantive review findings. A future design revision should state which findings it accepts, rejects or resolves and identify the resulting source version.

## Give feedback

Email [jesse@jessepike.dev](mailto:jesse@jessepike.dev?subject=AI%20Security%20Reference%20Architectures%20feedback) with the architecture or section and what is unclear, missing or incorrect. No GitHub account is required. Technical contributors can also use [GitHub Issues](https://github.com/jessepike/ai-security-reference-architectures/issues).
