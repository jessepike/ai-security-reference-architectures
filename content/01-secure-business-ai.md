# 1. Secure business AI

Version 0.1 · 8 September 2026 · Proposed logical reference architecture

**Outcome:** Business AI performs useful work within explicit limits on information access and action.

**Scope:** Employee use of AI, AI embedded in business applications, internally built assistants, and agents that use tools or coordinate automated business workflows. This includes the supporting data, models, connectors and runtime. Training a foundation model and securing a commercial AI product require deeper specialist views.

## Architecture

A business request enters through identity and intake controls. An AI application or agent interprets the request. Before it reaches data, a model service or a business tool, separate controls check the requested access or action. Returned content passes back through the appropriate checks; it does not acquire authority merely because a trusted connector delivered it.

| Component | Responsibility |
|---|---|
| Business ownership | Assign a workflow owner; define its purpose, acceptable outcomes, data use, autonomy and escalation rules. |
| Inventory and secure delivery | Discover sanctioned and unsanctioned AI use. Track applications, agents, models, tools and dependencies; review and test changes before release. |
| Business requests | People, scheduled events and application triggers initiate work within the workflow's stated purpose. |
| Identity and intake | Authenticate people and workloads, preserve the initiator's identity and delegated scope, and apply data-use rules to submitted content. |
| AI applications and agents | Interpret tasks and propose steps. Run with restricted compute, network access, memory and resource budgets. |
| Access and action checks | Enforce identity, purpose, resource and action permissions outside model reasoning. Validate tool arguments, retrieval scope, destinations and outputs. Deny or hold requests that lack authority. |
| Data, models and tools | Approved model services, permission-filtered retrieval, scoped memory, and business APIs or connectors, including MCP where used. Destination systems also enforce their own permissions. |
| Evidence and response | Preserve access decisions and action results; detect unexpected behavior, revoke access, stop workflows and verify recovery. |

This is a logical arrangement: enforcement may be distributed across identity services, model routing, retrieval services, API gateways, tool adapters and destination applications. It is not a claim that all SaaS traffic can traverse a single gateway. Where a provider does not expose the needed controls, restrict the use case, data or available actions.

## Boundaries that matter

1. **Initiator to workflow:** An agent receives task-specific authority, not every permission possessed by the user. Delegation to another agent cannot expand that authority.
2. **Content to instructions:** Documents, retrieved passages, tool output and memory are potentially hostile inputs. Label their origin and prevent them from granting permissions or changing governing policy.
3. **Proposal to effect:** Resource servers and execution controls enforce access at the point of use. A model's decision or safety classifier cannot grant access. Bind approval to the actual action, target and parameters, and recheck changed context.
4. **Execution to verification:** Use destination-system records to confirm what happened. An agent's completion message alone is insufficient.

Prompt injection and agent-specific threats motivate this separation of content, authority and action. The newer OWASP control work is relevant to implementing runtime interception; the architecture does not assume that any middleware can intercept every path. [OWASP agentic guidance](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [ACS](https://genai.owasp.org/resource/agent-control-standard-acs/).

## Walk through an example

An account-service agent reads a customer request, retrieves permitted account information and proposes a credit. Intake establishes the requester and account scope. Retrieval checks limit the records returned. The action control checks the credit amount and destination against policy. A credit requiring approval is held until a responsible person approves those exact details. The finance system records the action, and the workflow checks that record before reporting success. A malicious instruction in an attachment cannot raise the credit limit.

The credit thresholds and approval rules are illustrative; the business owner must define them. Secrets stay in a credential service, and the agent receives only the access needed for the current step. Retained traces require access controls and data minimization because they can contain sensitive information.

## Validation to carry into detailed design

- Attempt access to another customer's records and an unapproved destination; verify denial in the receiving system.
- Introduce hostile retrieved content; confirm it cannot change permissions or trigger an unauthorized write.
- Revoke a running agent's credentials; verify that subsequent calls stop and retries do not duplicate a completed action.
- Change the model, tool definition or retrieval corpus; rerun workflow evaluations before restoring the previous autonomy level.

NCSC's interim advice supports testing autonomy limits, restricting execution environments, operational monitoring and the ability to stop agents. These specific checks are proposed for this architecture. [NCSC, August 2026](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai).

## Visual contract and accessible description

Image: [01-secure-business-ai.png](../public/images/01-secure-business-ai.png). Read left to right. The following strings are the exact diagram copy; line breaks may change without changing wording.

| Region | Display text |
|---|---|
| Title | Secure business AI |
| Subtitle | Keep business workflows within approved access and action limits |
| Top band | Business ownership · Purpose · Data rules · Autonomy limits |
| Preparation band | Inventory & secure delivery · Discover AI use · Review dependencies · Test changes |
| Node 1 | Business requests / People · Events · Apps |
| Node 2 | Identity & intake / Who is asking? / What is permitted? |
| Node 3 | AI apps & agents / Plan and coordinate / Restricted runtime |
| Node 4 | Access & action checks / Enforce policy / Validate calls and results |
| Node 5 | Data, models & tools / Approved services / Scoped business access |
| Boundary around node 3 | Agent runtime |
| Branch below node 4 | Hold or deny / Approval required or outside policy |
| Evidence band | Evidence & response · Trace actions · Verify results · Revoke and stop |
| Principle | Model output cannot grant permission |
| Footer | 01 / 03 · Conceptual reference · v0.1 · 08 Sep 2026 |

Connectors: node 1 → node 2, “request”; node 2 → node 3, “scoped task”; node 3 ↔ node 4, “calls / results”; node 4 ↔ node 5, “permitted exchange”; node 4 → hold-or-deny branch, “exception”. The node 4–5 exchange includes permitted retrieval and inference calls, not only writes. Nodes 3, 4 and 5 feed the evidence band through a shared dashed line labeled “activity and outcomes”. The dashed box around node 3 marks its runtime boundary; access enforcement sits outside it. Bands describe cross-cutting responsibilities rather than a sequence.

## Next conversation

Choose one workflow. Identify its data and tools, the owner of its outcomes, the actions it may take alone, and the point where a person must decide. Then expand this view into actual trust zones and integration points.
