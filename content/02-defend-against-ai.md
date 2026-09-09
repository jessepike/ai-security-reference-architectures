# 2. Defend against AI

Version 0.1 · 8 September 2026 · Proposed logical reference architecture

**Outcome:** Reduce fraud, compromise, data loss and disruption when attackers use AI to improve their operations.

**Scope:** Enterprise people, identities, applications, endpoints, networks, cloud services, data and AI systems. Protection is needed even where the business has not adopted AI. Wider societal influence operations are outside this view.

## Architecture

This view organizes controls around three representative attack paths. They are parallel examples, not an exhaustive threat taxonomy or three stages of an attack. An incident may cross all three. Detection, response and recovery serve the whole protected environment.

| Attack path | Where to intervene | Protected assets |
|---|---|---|
| Impersonation and fraud | Authenticate people with phishing-resistant methods; independently verify sensitive business requests; protect account recovery and help-desk changes. | People and business processes, including payment, supplier and privileged-access changes. |
| Automated intrusion | Find exposed assets, prioritize reachable weaknesses, patch, protect endpoints and workloads, constrain privileges and segment access. | Identities, applications, infrastructure and connected services. |
| Attacks on AI workflows | Check content and tool boundaries; restrict agent permissions, retrieval, memory writes and outbound destinations. | Business AI, security AI, and the data and systems they can reach. |

AI's practical effect is often to accelerate or scale familiar attacker behavior. NCSC's threat assessment supports this emphasis; it is not evidence that every incident is AI-driven or fully autonomous. [NCSC threat assessment](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027).

## Shared defensive services

- **Business priorities:** Identify essential services, unacceptable losses and recovery needs. Give control changes and incident decisions accountable owners.
- **Exposure management:** Connect internet exposure, software and configuration weaknesses, identities, third parties and business criticality. Track remediation through verification, rather than treating a ticket as proof of closure.
- **Detection and investigation:** Correlate identity, endpoint, cloud, application, network and AI activity with business events. Detect harmful behavior regardless of whether its author was a person or a model.
- **Containment and recovery:** Revoke sessions, isolate affected systems, block harmful transfers and stop compromised workflows under pre-agreed authority. Restore from protected copies and verify the recovered business service.

Use ATT&CK to select enterprise attack scenarios and ATLAS for threats involving AI systems. Preserve the distinction between a possible technique, a demonstration and an observed incident. [MITRE ATT&CK](https://attack.mitre.org/), [MITRE ATLAS](https://atlas.mitre.org/).

## Boundaries that matter

1. **Communication to business authorization:** A convincing voice, video, email or chat message is not sufficient to authorize a sensitive change. Confirm it through an independently established route and business approval process.
2. **Initial access to wider compromise:** A breached endpoint, identity or application should not provide unrestricted access to critical services. Limit privileges and lateral paths; monitor session misuse as well as login attempts.
3. **AI content to connected systems:** Route threats to an AI workflow through architecture 1's protections. Content analysis alone cannot ensure that the workflow will stay inside its authority.
4. **Incident to recovery:** Protect response access and recovery material from the compromised environment. Test the actual service and data after restoration.

Phishing-resistant authentication helps protect sign-in; transaction verification and recovery-process controls address separate paths. CISA's official guidance supports the authentication baseline. [CISA MFA guidance](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf).

## Walk through an example

An attacker uses a convincing executive voice message to request a supplier bank-account change. The employee follows a known callback route and the supplier-change approval process. A related compromised session attempts the change directly; session monitoring and application authorization provide another intervention point. Security staff correlate the request and account events, revoke access if needed, and reconcile any affected transactions. A deepfake detector may contribute a signal, but the control decision does not depend on identifying synthetic media.

This example and its control arrangement are proposed design choices. Exact verification steps, separation of duties and containment authority must match the business process.

## Validation to carry into detailed design

- Exercise a synthetic impersonation attempt against both the employee process and the help desk.
- Test a representative exposed-application-to-sensitive-data path and verify where it is interrupted.
- Simulate hostile content reaching a connected AI workflow; verify blocked unauthorized actions and usable alerts.
- Exercise response while AI assistance is unavailable, then restore a business service and reconcile its data.

Measure successful intervention and business recovery, including missed detections and response delays. A rising count of blocked messages does not by itself demonstrate lower business risk.

## Visual contract and accessible description

Image: [02-defend-against-ai.png](02-defend-against-ai.png). Read across each of three aligned rows. The right-hand column describes protected assets, not confirmed compromise.

| Region | Display text |
|---|---|
| Title | Defend against AI |
| Subtitle | Interrupt AI-enabled attacks before they become business loss |
| Top band | Business priorities · Critical services · Loss limits · Recovery needs |
| Column headings | Attack paths / Control boundaries / Protected assets |
| Row 1 left | Impersonation & fraud / Convincing messages and identities |
| Row 1 center | Verify people & requests / Strong sign-in · Independent checks |
| Row 1 right | People & business processes |
| Row 2 left | Automated intrusion / Faster discovery and exploitation |
| Row 2 center | Reduce exposure & contain / Patch · Limit privilege · Segment |
| Row 2 right | Identity, apps & infrastructure |
| Row 3 left | Attacks on AI workflows / Hostile content and tool abuse |
| Row 3 center | Protect AI boundaries / Scope data · Restrict tools and actions |
| Row 3 right | Business AI & security AI |
| Lower band | Detect & investigate · Identity · Endpoint · Cloud · Network · AI signals |
| Recovery band | Contain & recover · Revoke access · Isolate · Restore · Verify |
| Principle | Defend against harmful behavior, whether AI use is visible or not |
| Footer | 02 / 03 · Conceptual reference · v0.1 · 08 Sep 2026 |

Each attack-path node → its matching control node uses a solid amber arrow labeled “attempt”. Each control node → its protected asset uses a blue line **without an arrowhead**, labeled “protects”; this is a protective relationship, not an allowed attack path. A gray dashed outline encloses the protected-assets column. The column feeds the detection band through a dashed arrow labeled “telemetry”. Detection → recovery uses a solid navy arrow labeled “response”. Recovery → the protected-assets boundary uses a dashed teal return arrow labeled “restore service”. The top band applies to the entire view.

## Next conversation

Choose the most consequential attack path for the business. Identify the real control points, evidence sources, response authority and recovery dependency. Architecture 3 can then show where AI assistance might improve that defense.
