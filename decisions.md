# Project decision log

Decisions record the owner's accepted direction for this project. They do not certify an architecture, assign authority in another organization or close review findings. Proposed technical design decisions remain in the corresponding canonical architecture until explicitly adopted.

Entries are dated and retained. Supersede an entry with a new entry rather than rewriting its historical rationale.

| ID | Date | State | Decision and reason | Origin and scope | Revisit when |
|---|---|---|---|---|---|
| DEC-001 | 2026-09-08 | Accepted | Develop the original security architectures from the owner's brief and public primary sources; exclude unrelated workspace material. A folder's contents do not define the design basis. | Explicit owner instruction during initial creation. | The owner authorizes a specific additional source. |
| DEC-002 | 2026-09-09 | Accepted | Keep secure business AI, defend against AI-enabled attacks and defend with AI as three connected security perspectives. The same event may need all three. | Owner's requested series and overarching narrative. | Evidence shows an important security responsibility cannot be explained within the views and their interfaces. |
| DEC-003 | 2026-09-09 | Accepted | Maintain canonical Markdown and PNG visuals, detailed guides, a presentation and a public website. Capture common language and authoring rules for people and agents. | Owner's artifact and repeatability requests. | Reader testing identifies a format that adds maintenance burden without helping comprehension. |
| DEC-004 | 2026-09-09 | Accepted | Publish the selected public edition in `jessepike/ai-security-reference-architectures` and at `ai.jessepike.dev`, with feedback to `jesse@jessepike.dev`. Keep raw operational review material outside public packages. | Explicit publication, domain and public-email selections. | The owner changes the public identity, host or sharing scope. |
| DEC-005 | 2026-09-09 | Accepted | Improve the introduction with situation, next decision, accountable owner and permitted data use. Present built, bought, embedded and unmanaged as overlapping discovery prompts. | Owner accepted the comparison recommendations on 9 September. Only the approved concepts transfer; the prior internal document is not published. | Reader testing shows these prompts confuse rather than clarify the starting conversation. |
| DEC-006 | 2026-09-09 | Accepted | Add one governance companion with canonical Markdown, PNG and a detailed guide. Explain decision rights and lifecycle oversight across the three security perspectives, including risks beyond cybersecurity. | Owner accepted the governance recommendation on 9 September. | An existing governance model can meet the need through a smaller interface guide, or the owner explicitly changes scope. |
| DEC-007 | 2026-09-09 | Accepted | Distinguish coordination from accountability. Identify the relevant decisions and evidence before mapping them to security, GRC, an AI office or other teams. Reuse existing governance processes where possible. | Accepted governance/ownership recommendation; no organization-specific roles are assigned. | A specific implementation supplies its actual authority and operating model. |
| DEC-008 | 2026-09-09 | Accepted | Scaffold this repository with a purpose, shared agent instructions, decisions, work state, contribution guidance and validation/release procedures. Public canonical sources live in `content/`. | Explicit owner request to scaffold the project and capture decisions. | The structure becomes insufficient or creates unnecessary duplicate records. |

## Review boundary

The original three component packages received model-assisted critique with material reservations. New content and successful browser/build checks do not inherit that review. Keep current coverage and open questions in [review status](content/review-status.md).
