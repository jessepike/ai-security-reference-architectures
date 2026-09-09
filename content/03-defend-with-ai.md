# 3. Defend with AI

Version 0.1 · 8 September 2026 · Proposed logical reference architecture

**Outcome:** Improve the speed and quality of security work while keeping decisions accountable and actions bounded.

**Scope:** AI-assisted prevention, exposure assessment, detection engineering, investigation, response and recovery support. Includes statistical detection, copilots and tool-using agents. Broad unattended control of production systems is not assumed.

## Architecture

Security signals and business context support AI-assisted analysis. The analysis produces findings or proposed actions. A separate authorization step checks the evidence, scope and potential effect. Approved actions use controlled execution paths, and verification determines whether the intended change occurred. Analysts remain able to intervene and continue essential work without AI assistance.

| Component | Responsibility |
|---|---|
| Security ownership | Assign responsibility, define use cases, set action limits and maintain escalation and fallback procedures. |
| Security evidence | Ingest source-attributed telemetry, asset and identity context, threat information and relevant case records. Apply access controls, retention and freshness checks. |
| AI analysis and agents | Correlate events, summarize evidence, prioritize exposures, assist investigations, propose detections or remediation, and expose uncertainty. |
| Action authorization | Check identity, evidence, target, scope and policy. Require a human decision for cases outside a tested pre-authorized action envelope. |
| Controlled execution | Use constrained adapters to security and IT systems. Enforce rate, target and time limits, credential scope, and stop conditions. |
| Outcome verification | Check destination-system evidence and service health. Confirm effect, detect unintended consequences, and invoke rollback or recovery where available. |
| Evaluation and improvement | Test against representative cases and hostile inputs; investigate errors and retest changed models, data, tools and policies. |

NCSC's July 2026 Cyber Shield blueprint supports the direction toward AI-assisted vulnerability work, detection and controlled mitigation, while explicitly identifying unresolved engineering challenges. The component arrangement here is an enterprise-level proposal. [NCSC Cyber Shield](https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence).

## Decide autonomy by action

| Mode | Example | Required boundary |
|---|---|---|
| Assist | Summarize a case with links to its evidence. | Scoped read access; clearly separate observations from generated interpretation. |
| Recommend | Propose isolating a host or changing a detection rule. | Show supporting evidence, affected assets and expected consequences for review. |
| Act within limits | Execute a tested, narrowly scoped response allowed by policy. | Enforce the authorized target and action; record the result; support intervention. |

These are selectable operating modes, not maturity levels that every team must progress through. Isolation can itself interrupt critical work; reversibility alone does not make an action low risk. Consequential changes require explicit human approval unless they fall inside an authorized, tested emergency procedure.

## Boundaries that matter

1. **Telemetry to interpretation:** Logs, tickets and threat reports can contain attacker-controlled text. Treat that text as evidence to analyze, not instructions for the security agent.
2. **Inference to authority:** The same agent must not be able to change the policy that authorizes its work. Self-reported confidence or agreement from another model cannot replace relevant evidence.
3. **Authorization to production:** Bind permission to the real action and target. Keep credentials and enforcement outside model output, recheck current conditions and reject attempts to bypass controlled adapters.
4. **Execution to closure:** Verify results with source systems; keep the case open if evidence is missing or conflicting. Some actions cannot be undone, so plan recovery before permitting them.

The security AI platform is itself an AI system: apply architecture 1's identity, data, tool, runtime and supply-chain protections. Test it against both AI-specific and ordinary enterprise threats. [MITRE ATLAS](https://atlas.mitre.org/), [OWASP LLM guidance](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/).

## Walk through an example

An AI assistant correlates a suspicious login with an endpoint alert and identifies the affected user's access to a critical application. It proposes session revocation, citing those records and explaining uncertainty. Authorization checks whether that action and target fall inside a pre-approved response procedure; otherwise an analyst decides. A constrained adapter performs the revocation. Verification checks the identity platform and application sessions, and the analyst evaluates remaining exposure. A failed or uncertain revocation is escalated rather than reported as resolved.

## Validation to carry into detailed design

- Run historical and held-out cases; compare missed detections, incorrect conclusions and analyst effort with the current process.
- Insert malicious instructions into a ticket or log; confirm they cannot authorize a tool call.
- Test wrong-target and repeat-action prevention, policy-service failure and emergency stop.
- Verify action outcomes and service impact; rehearse recovery and operation during model or telemetry outages.

Track investigation quality, time to verified containment, false positives and negatives, unintended action rate and analyst overrides. Benchmark results and vendor demonstrations do not establish local effectiveness.

## Visual contract and accessible description

Image: [03-defend-with-ai.png](../public/images/03-defend-with-ai.png). Read the main flow left to right; the lower return path supports evaluated improvement.

| Region | Display text |
|---|---|
| Title | Defend with AI |
| Subtitle | Turn security evidence into controlled, verifiable action |
| Top band | Security ownership · Use cases · Action limits · Human oversight |
| Node 1 | Security evidence / Telemetry and context / Source and freshness |
| Node 2 | AI analysis & agents / Investigate and prioritize / Cite evidence and uncertainty |
| Node 3 | Action authorization / Policy and scope checks / Human approval when required |
| Node 4 | Controlled execution / Constrained tools / Limits and stop conditions |
| Node 5 | Outcome verification / Check actual effect / Recover or escalate |
| Boundary around node 2 | Analysis boundary |
| Branch below node 3 | Hold or reject / Missing evidence or authority |
| Lower band | Evaluation & improvement · Test cases · Measure errors · Retest changes |
| Foundation band | Secure the security AI · Identity · Data · Tools · Runtime · Audit |
| Principle | Permission comes from policy; success comes from evidence |
| Footer | 03 / 03 · Conceptual reference · v0.1 · 08 Sep 2026 |

Main connectors: node 1 → node 2, “evidence”; node 2 → node 3, “proposal”; node 3 → node 4, “authorized action”; node 4 → node 5, “result”. Node 3 → hold-or-reject branch, “exception”. Node 5 → evaluation band is a dashed arrow labeled “outcomes”; evaluation band → node 2 is a dashed return arrow labeled “tested updates”. This is controlled improvement, not automatic retraining on incident content. A dashed box surrounds node 2; the authorization service and execution controls sit outside the analysis boundary. The foundation band applies across the system.

## Next conversation

Choose a security task with adequate data and a measurable baseline. Start with the useful level of assistance for that task, then determine which specific actions can meet the evidence, authority and recovery requirements.
