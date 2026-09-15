# Secure Business AI starter playbook

**Status:** Exploring | Review draft | Stage 0 Envision and handoff into Stage 1 only | 15 September 2026

This is a practical prototype for the CISO's first conversation with a team exploring business AI. It helps the team learn safely while choices are still flexible. The business leads the effort and owns the intended value. Security listens, helps make exposure visible, suggests safe ways to learn, operates protections assigned to security, and uses delegated authority where it exists.

This playbook starts from the existing [Applying Secure Business AI guide](../../content/guides/applying-secure-business-ai-guide.md), especially Stage 0 Envision and Stage 1 Discover and guardrail. It proposes a smaller working view of those stages. It does not revise the guide, replace its complete journey, inherit its external review, or establish approval for an AI use.

## The complete model behind the first conversation

The first conversation is deliberately small, but it connects to the full outcome approach:

**Intended business change -> credible consequences -> desired security conditions -> work and protections -> scoped evidence -> decision and reassessment**

Stage 0 does not need a final architecture, complete supplier assessment, or production control design. It needs enough understanding to identify a useful and reasonably safe next experiment. Controls deepen when exposure deepens. Sensitive data, wider reach, system actions, human effects, important dependencies, and difficult-to-reverse consequences call for more work earlier. A stage label alone does not make an experiment safe.

The same living record follows the effort. At first it may be one page. It grows as facts, evidence, decisions, conditions, and changes become important. Existing work systems can hold it. The playbook does not require a new set of documents.

## Stage 0 playbook for the CISO

### What the team brings

The team brings an idea, problem, opportunity, prototype, product option, or already-operating use. It should be ready to explain the business result it wants and the next thing it hopes to learn. A sketch, vendor page, sample output, or rough workflow is useful when available. Missing details are expected.

If a use is already operating, first establish its current exposure and make an intake and containment decision through existing authority. The conversation does not grant permission retroactively. Where needed, create a safer parallel experiment while the operating use is examined.

### What the CISO asks

Use the eight starter questions below. Listen for where the proposed experiment touches actual data, people, external services, business systems, or consequential decisions. Ask conditional follow-ups only when they fit the approach being considered.

### Guidance security gives now

Security gives a short initial risk view and practical experiment guidance. That guidance should make the next learning step possible within a broad safe boundary. It may suggest synthetic or de-identified data, a restricted workspace, draft-only output, a smaller user group, no external upload, no system connection, or human review before any consequence.

Security should distinguish advice from a binding requirement. If a law, contract, policy, safety duty, individual right, or delegated authority creates a binding condition, record its source, scope, decision owner, and consequence. The CISO does not become the sole approval owner by facilitating the conversation.

### What can wait

The team can usually defer final product selection, complete architecture, production identity design, full monitoring design, detailed incident procedures, enterprise-scale assurance, and long-term operating mechanics. Those subjects become specific as the experiment and exposure become specific.

They cannot wait when the contemplated experiment already depends on them. Before actual data goes to an external destination, the team needs to know the destination, permitted data, access conditions, and enough retention and provider behavior to make that transfer safe. Before an AI can read from or write to a business system, the relevant identity, permission, action, review, and recovery controls must be understood and checked.

### What security returns

Security returns three linked parts in the living record:

1. The team's answers to the starter questions, including visible unknowns.
2. An initial risk view describing the credible scenarios and the limits of current understanding.
3. Guidance for the next bounded experiment, including what can happen now, what waits, and what must be checked before exposure expands.

The initial risk view is a first-conversation judgment. It is revisited at the Stage 1 handoff. It is not a numeric score, a complete assessment, an approval, or evidence that controls work.

### What triggers the Stage 1 handoff

Move into Discover and guardrail when the team is ready to use actual or sensitive data, send information to an external service, add users beyond the initial group, connect an integration, allow read or write access, rely on output in a consequential decision, begin a formal pilot, select a provider, or resolve an unknown that prevents a safe experiment.

Stage 1 deepens only the specifics needed for the next bounded test. It maps the real workflow and boundary, assigns the relevant decision owners, defines guardrails and evidence, and checks applicable protections before actual data access or action. It does not require every enterprise production control at once.

## Copyable starter questionnaire

One answer may be a sentence. “Unknown” is acceptable. If an unknown prevents the contemplated exposure from being safe, record a safer experiment that avoids that exposure.

1. **Value and owner:** What business result are you trying to improve, how will you recognize useful progress, and who owns that result?
2. **Approach:** Are you buying, building, enabling AI already embedded in a product, combining those approaches, or still deciding?
3. **AI and architecture:** What tools, models, providers, and major components are known? What remains unknown? Add a rough sketch if one exists.
4. **Data:** What information might go in or come out, where does it come from, how sensitive might it be, where might it go, and what is known about reuse or retention?
5. **People and environment:** Who would use it, who could be affected, where would it run, and how would users get access?
6. **Connections and actions:** What could it read, recommend, create, send, or change? Which integrations are contemplated, and where would a person review the result?
7. **Consequences:** What could plausibly harm a person, customer, employee, business process, obligation, or important dependency if the AI is wrong, misused, manipulated, unavailable, or trusted too much?
8. **Next experiment:** What is the smallest useful thing you want to try next, and is any version already operating?

Conditional follow-ups:

- **If buying or enabling embedded AI:** Which provider and service are under consideration? What settings, data terms, retention, access controls, logs, change notices, and exit options are visible today?
- **If building or combining components:** Which model, retrieval source, tool, hosting environment, service identity, and evaluation method are contemplated? Which parts are still open choices?

These follow-ups are prompts, not mandatory fields. Ask only what affects the next experiment.

## Copyable initial risk view

Use this during the first conversation and revisit it at handoff.

> **Effort and date:**
>
> **Pending business decision and owner:**
>
> **Next experiment being considered:**
>
> **Credible scenarios:** What could go wrong through error, misuse, manipulation, weak access, excessive reliance, provider behavior, or failure?
>
> **Consequences:** Who or what could be affected, and how serious or reversible could the effect be?
>
> **Current exposure:** Which people, data, environments, providers, integrations, actions, and dependencies would the next experiment actually touch?
>
> **Important unknowns:** Which missing facts could change the experiment guidance? Which can remain open because the current boundary avoids them?
>
> **Initial security recommendation:** Proceed within a stated boundary, narrow the experiment, use a safer alternative, investigate a named unknown, or pause the affected activity.
>
> **Relevant decision and action owners:** Name only the roles needed for the current questions. One person may hold several roles.
>
> **Limits:** This is an initial qualitative view, not a score, approval, complete assessment, or proof that a protection works.

## Copyable experiment guidance

> **Purpose of the experiment:**
>
> **What may happen now:** Users, environment, data class, provider or local tool, allowed outputs, and allowed actions.
>
> **What must not happen in this experiment:** Prohibited data, destinations, integrations, actions, reliance, or expansion.
>
> **What can wait:** Questions and production work that the current boundary does not require.
>
> **What must be checked before exposure expands:** Facts, assigned decisions, protections, and evidence needed before actual data, external transfer, more users, system access, consequential reliance, or action.
>
> **How the team will learn:** What it will observe, test, or compare, including business value and unwanted behavior.
>
> **Stop and help route:** What causes the experiment to stop, who can stop it, and who the team contacts.
>
> **Owner and revisit date or trigger:**

The boundary should allow useful learning. “Use clean data” is not sufficient guidance. Name what data is allowed, where it may go, and what the experiment can do.

## Copyable Stage 1 handoff

> **Business purpose and next decision:**
>
> **Stage 0 experiment and learning:** What was tried, within which boundary, and what was learned about value and exposure?
>
> **Proposed next bounded test:**
>
> **Specific facts to deepen:** Only the workflow, data, identities, providers, integrations, human effects, consequences, and obligations needed for that test.
>
> **Controls to check before actual data or action:** Identify applicable access, data, action, human review, logging, stop, recovery, and provider controls. State how they will be tested.
>
> **Open decisions and assigned owners:** Include only the business, data, privacy, legal, safety, security, exception, or other decisions relevant now.
>
> **Evidence needed for the pilot decision:**
>
> **Interim boundary:** What remains restricted until the facts, controls, and decisions above are resolved?

## Worked example: customer-service credit assistant

This entire example is invented. The Stage 0 learning and Stage 1 handoff below illustrate what the records could look like; they do not report an actual test or verified result.

The customer-service team wants an assistant that drafts account-credit recommendations. The first experiment has no autonomous credit authority and no connection to a finance or customer-account system.

### Starter questionnaire

1. **Value and owner:** The service leader wants faster, more consistent draft recommendations and owns the result. The team will compare usefulness, corrections, and handling time.
2. **Approach:** The team will use an existing approved AI tool in a restricted workspace with a small prompt and evaluation workflow. Any future provider selection remains open.
3. **AI and architecture:** Known pieces are the approved tool, restricted test workspace, invented cases, and a human reviewer. Production architecture is unknown. The sketch is: invented case -> approved tool -> draft recommendation -> supervisor review.
4. **Data:** The first experiment uses invented cases only. No transformed historical record, live customer data, or other real-derived data may be uploaded.
5. **People and environment:** Two service designers use the restricted test workspace. Supervisors may review samples. Customers are affected only in a future use because experiment output cannot reach an account.
6. **Connections and actions:** The assistant can read only the test case entered by the designer and return a draft. It has no integrations and cannot create or apply a credit. A supervisor reviews selected drafts.
7. **Consequences:** Weak drafts could teach staff a poor approach or reveal sensitive patterns if real cases are introduced. Future system access could create an incorrect or duplicate credit. Provider handling and over-reliance are important unknowns.
8. **Next experiment:** Compare draft usefulness on 30 invented cases and test several misleading case descriptions. Nothing is operating today.

### Initial risk view

> **Effort and date:** Customer-service credit assistant, initial conversation.
>
> **Pending business decision and owner:** The service leader decides whether the draft-only experiment is worth running.
>
> **Next experiment being considered:** Generate draft credit recommendations for 30 invented cases in an existing approved tool and restricted workspace.
>
> **Credible scenarios:** The model produces inconsistent or inappropriate drafts, follows misleading case text, or encourages excessive supervisor reliance. Actual customer data could be exposed if the boundary is ignored.
>
> **Consequences:** The current experiment could waste staff time or create misleading learning. Customer or financial effects are avoided because output cannot reach a live case, account, or credit system.
>
> **Current exposure:** Two designers, invented cases, one restricted workspace, an existing approved AI tool, draft output, and no integration or action.
>
> **Important unknowns:** Future provider selection, provider retention and reuse for any real-derived data, production identity, live-data handling, and any future credit-system design. Those can remain open while the experiment uses invented data in the approved tool and has no connection.
>
> **Initial security recommendation:** Proceed with the draft-only experiment inside the stated boundary using the existing approved tool and invented cases. Do not introduce another provider or real-derived data through this guidance.
>
> **Relevant decision and action owners:** The service leader owns value and use of the experiment. Security operates workspace access and confirms the approved-tool boundary. Data and privacy owners join before any transformed historical record is proposed.
>
> **Limits:** This view does not approve live data, system connection, credit execution, a provider, or production use.

### Experiment guidance

> **Purpose of the experiment:** Learn whether the assistant can produce useful draft recommendations and how it behaves when case text is incomplete or misleading.
>
> **What may happen now:** Two named designers may use invented cases in the approved tool and restricted workspace. The assistant may return text drafts for review.
>
> **What must not happen in this experiment:** No live customer data, customer contact, finance or account-system connection, credit creation, automated decision, or use of output as a final customer decision.
>
> **What can wait:** Production architecture, service identity, API permissions, production monitoring, recovery design, and enterprise rollout planning.
>
> **What must be checked before exposure expands:** Data and privacy review before using transformed historical records; destination, provider terms, access, retention, and deletion before any real-derived data transfer; identity and permissions before any connection; exact approval and action limits before any credit-system write.
>
> **How the team will learn:** Record useful, corrected, rejected, and manipulated-case results separately. Ask supervisors why they changed or rejected a draft.
>
> **Stop and help route:** Stop if real-derived data appears, a user attempts a connection or new provider, the approved-tool boundary changes, or outputs reveal sensitive information. The service lead and security contact decide the immediate response within their roles.
>
> **Owner and revisit trigger:** Service leader. Revisit when the 30-case test ends or before any transformed historical record, new user group, provider change, or integration.

### Stage 1 handoff

> **Business purpose and next decision:** Decide whether a bounded pilot with transformed real cases would provide enough learning to justify deeper development.
>
> **Stage 0 experiment and learning:** In this invented example, the team tested drafts on invented cases in the approved tool with two designers, no integrations, and supervisor review. The illustrative record captures usefulness, corrections, rejections, and manipulation behavior.
>
> **Proposed next bounded test:** A time-limited pilot using a reviewed set of transformed historical cases. Output remains draft-only and disconnected from customer and finance systems.
>
> **Specific facts to deepen:** The transformation method, residual customer identifiers, provider destination and retention, workspace identities, reviewers, logs, deletion, misleading-input scenarios, and how supervisors may rely on drafts.
>
> **Controls to check before actual data or action:** Data-owner review of the transformed set; tested workspace access; provider data controls; logging without unnecessary case content; deletion test; supervisor rejection route; immediate pilot shutdown. Credit-execution controls can wait; verify that the test has no business-system connection or write permission.
>
> **Open decisions and assigned owners:** The service leader decides pilot value and operating boundary. The data and privacy owners decide whether transformed cases may be used and sent to the provider. Security checks access, provider conditions, logging, and shutdown. Legal joins only if the identified data use or provider terms require its decision.
>
> **Evidence needed for the pilot decision:** Data review, provider terms, access test, deletion test, stop exercise, sample evaluation plan, and a recorded boundary with owners.
>
> **Interim boundary:** Invented cases only until an explicit new decision permits the bounded use of transformed historical records; named users; draft output; no customer contact, live-case retrieval, finance connection, account write, or autonomous credit.

## Two proportional-path checks

### Bought AI with an unknown provider

A team can discuss the idea, compare product claims, sketch a workflow, and use public or invented examples while the provider is unknown. Unknown provider identity does not block that safe exploration. Before the team uploads internal or personal data, it must identify the destination and understand enough about access, retention, reuse, and contractual conditions to make the transfer safe. If that cannot be established, the next experiment uses a local or approved alternative, invented data, or a provider whose boundary is known.

### Built prototype using synthetic data

A team can test a locally contained prompt, simple model interaction, or user experience with synthetic data and no integrations while production architecture remains unknown. Stage 1 becomes necessary when the next test adds actual data, external hosting, more users, retrieval, tools, business-system access, or consequential reliance. The handoff deepens those changes instead of demanding a full production design for the synthetic experiment.

## Relationship to the existing stage guide

| Prototype output | Existing Stage 0 or Stage 1 field |
|---|---|
| Starter questionnaire | Stage 0 intended change, owner, users, affected people, likely data, platform, actions, consequences, and early obligation signals |
| Initial risk view | Stage 0 preliminary data and action view, assumptions, open questions, initial security outcomes, and receiving owners |
| Experiment guidance | Stage 0 next bounded step and security input; Stage 1 pilot boundary, guardrails, stop route, and evidence plan |
| Stage 1 handoff | Stage 1 workflow and boundary, data, identities, providers, effective authority, scenarios, obligations, decision owners, controls, and pilot evidence |
| One living record | The guide's living use-case profile and continuing evidence record |

The prototype is a proposed revision to how readers could apply the existing Stage 0 and Stage 1 material. Promotion would require review, owner direction, a canonical source decision, and updates to any dependent site or rendered formats. Until then, the existing guide remains unchanged and authoritative for the published application companion.

## Evidence, counterevidence, and test

The existing guide supports a light Stage 0 conversation followed by deeper Stage 1 work, and the owner has directed that security listen and enable broad safe experimentation while controls follow actual exposure. The counter-risk is that even a short playbook becomes a mandatory form or lets an unsafe unknown pass without a narrower alternative. This prototype has not been tested with readers. If a business team or CISO cannot use it to choose a clear, bounded next step after one conversation, revise the prompts and guidance before considering promotion.
