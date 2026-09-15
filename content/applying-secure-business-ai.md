# Applying Secure Business AI

**Status: Proposed neutral application companion · Review draft · 14 September 2026**

Secure Business AI is how security supports useful AI development and business transformation while keeping access, action, and consequences within understood limits. This companion provides a reusable journey for an individual workflow, a shared platform, or a transformation program.

It applies the [Secure Business AI architecture](01-secure-business-ai.md) and the [AI Governance companion](04-ai-governance.md). The six stages below describe security's contribution to an AI effort. They do not replace the six governance responsibilities, create a security maturity scale, or add a fourth architecture. Governance responsibilities apply throughout every stage.

Security advises the business on its use of AI, operates protections assigned to security, and exercises delegated authority where the organization has granted it. Name only the roles relevant to the use and pending decision. These can include business, data, privacy, legal, safety, security, exception, release, recovery, and other decision owners; one person may hold several roles. Existing decision processes should carry the work when they can. If relevant authorities disagree, the affected activity stays within its existing approved boundary, or is held under the named authority, until the conflict is resolved and recorded.

## The outcome approach

Use one reasoning chain throughout the effort:

**Intended business change → credible consequences → desired security conditions → work and protections → scoped evidence → decision and reassessment.**

The business defines the intended change and how value will be recognized. The team maps the workflow, people affected, data, authority, dependencies, and credible consequences. Security helps define and operate conditions that keep access and action within understood limits. Evidence is tied to a claim, scope, configuration, date, source, limitations, and validity. The assigned decision owners use that evidence within their authority.

## The six progressive stages

| Stage | What must be understood | Security contribution | Useful deliverables | For the next decision |
|---|---|---|---|---|
| **0 Envision** | Intended change, accountable business owner, affected people, likely data, consequence before human review, and arrival path. | Join opportunity shaping, surface material feasibility and obligation signals, and separate facts from assumptions. | Security input to prioritization; preliminary data and authority view; open questions with owners. | Business owner selects, defers, or discards the candidate and names the next decision owners. |
| **1 Discover and guardrail** | Workflow boundary, data, identities, providers, tools, people affected, effective authority, misuse and failure scenarios, dependencies, and obligations. | Build the shared factual picture, involve specialists, agree a bounded use, define evidence needs, and implement applicable protections before data access or action. For bought or embedded AI, test platform fit before pilot commitment. | Living effort profile; initial threat and impact view; guardrails; decision-rights map; evidence plan; protection evidence. | Assigned business, data, privacy, legal, delegated security, and other owners proceed, reshape, hold, or stop within their authority. Conflicts hold the affected activity under the named authority. |
| **2 Pilot** | Actual data movement, user reliance, AI reach and action, provider behavior, control performance, events, stop and recovery behavior, and remaining unknowns. | Test the bounded protections, observe real behavior, exercise response routes, collect evidence, and identify what broader use requires. | Pilot boundary; tests and observations; event record; exercised stop route; updated profile; production needs; data disposition. | Assigned owners develop, pivot, extend within a revised boundary, or stop. Exception owners decide any requested departure; data and privacy owners decide live-data extensions. |
| **3 Develop** | Target workflow, integrations, identities, environments, suppliers, probabilistic and deterministic steps, authority points, failure handling, operating owners, and inherited controls. | Turn agreed conditions into traceable implementation needs; build or configure protections; verify supplier fit; test misuse, access, action, resilience, and recovery; expose exceptions. | Target outcomes and controls; architecture and flows; implementation trace; validation plan and results; supplier evidence; operating model; exception record. | Product and business owners decide whether to seek production validation; delegated security and other specialist owners decide within their authority; exception owners resolve departures. |
| **4 Production transition** | Deployed configuration, production users and data, permissions and autonomy, differences from the tested build, residual exposure, readiness, exceptions, and release and stop authority. | Validate the real boundary; test refusal, containment, recovery, monitoring, escalation, and incident routes; reconcile approved and deployed states. | Configuration record; validation and exercise evidence; transition record; response routes; exceptions; release decision and conditions. | Named release, business, data, privacy, legal, delegated security, recovery, and exception owners release, narrow, defer, or stop within their authority. |
| **5 Operate** | Current system and owners; model, data, tool, user, integration, supplier, authority, reliance, and purpose changes; signals, incidents, drift, value, and retirement dependencies. | Monitor and respond, assess material change, retest affected outcomes, exercise delegated hold or stop authority, and verify recovery and retirement. | Current profile; monitoring and incident evidence; change assessments; continuation or constraint decisions; retirement evidence. | Assigned owners continue, constrain, change, expand, stop, resume, or retire. A material change that invalidates evidence holds affected consequential actions or reduces autonomy through named authority until renewed evidence and a recorded resumption decision exist. |

## Conditions that change the path

An effort may enter at its current stage, but stage entry is not acceptance of earlier decisions or evidence. An unmanaged use first receives an intake and containment decision: identify the current exposure, preserve evidence, restrict urgent harm through existing authority, and name who decides what happens next.

When a provider cannot expose or enforce needed controls outside the model, record the limitation and restrict the use case, permitted data, or available actions. Do not treat a provider assertion or model instruction as equivalent to an enforceable boundary.

A material model, provider, tool, retrieval, data, integration, purpose, population, or autonomy change invalidates only the evidence it affects. Until renewed evidence supports a decision, named authority holds affected consequential actions or reduces autonomy. The resumption decision records the evidence, remaining limits, and conditions.

## Coverage map

Each effort considers these subjects at a depth proportional to its consequences and uncertainty:

| Subject | Questions that remain in view |
|---|---|
| Purpose and ownership | What change is sought, who is affected, who owns the result, and who holds each decision right? |
| Workflow and boundary | Where does AI enter the work, what happens before and after, and which people, systems, organizations, and environments are included? |
| Data and knowledge | What enters prompts, retrieval, memory, logs, outputs, derived stores, and tuning? Who owns it, where does it move, and when is it deleted? |
| Identity, access, and authority | Who and what can reach the AI and connected resources? What may it see, recommend, create, send, change, approve, or delete? |
| Models, tools, platforms, and suppliers | What is relied on? What can be configured, verified, changed, revoked, or replaced? |
| Threat, misuse, failure, and impact | How could the use be attacked, misused, fail, or cause harm? Which specialist decisions apply? |
| Protection and resilience | Which access, action, isolation, oversight, validation, detection, containment, recovery, and continuity outcomes are needed? |
| Evidence and assurance | What demonstrates each claim, for which scope and configuration, for how long, with what limits, and with what independence? |
| Operation and change | What is monitored, who responds, what reopens a decision, and how are expansion, exception, stopping, resuming, and retirement handled? |
| Business value and human effects | Is intended value appearing? How do people rely on the output? Which privacy, legal, safety, reliability, fairness, transparency, workforce, or other judgments apply? |

## A common living record

One linked record should follow the effort through retirement. It preserves purpose, owners, affected people, workflow, data, identities, suppliers, effective authority, facts, assumptions, unknowns, scenarios, conditions, obligations, decisions, dissent, evidence, changes, incidents, restrictions, resumptions, and retirement evidence. Existing systems can hold these parts; the framework does not require a new register.

At every stage, record whether each applicable question is **understood**, **evidenced**, **open**, or **not applicable with a reason**. Also record the basis, assigned owner, next action, and current decision. A check mark or completed deliverable is not proof that a protection works.

## Limits and review status

This is a proposed neutral application companion. It has received a model-assisted external review and incorporates the panel's eight High corrections. The panel's Low observations remain historically recorded; some related wording changed while creating this adaptation, but no Low finding is claimed closed until the rendered preview is reviewed. The present companion does not close or reclassify the 30 findings on the existing architectures.

It does not define an organization's risk tolerance, obligations, role assignments, thresholds, products, or approval bodies. Human review, reader testing, field use, control effectiveness, compliance, production publication, and owner content acceptance remain unassessed.
