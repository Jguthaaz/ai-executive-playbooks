# Technology Decision Canvas
**v0.1 · blank working template**
[Module home](README.md) · [Selection tree](solution-selection-tree.md)

Answer these ten questions before naming products. Use IDs C1–C10 to link evidence to scores and the brief. Every answer needs evidence status (observed / assumption / unknown), source or artifact, accountable role, confidence and next verification. Unknown is a valid answer.

| ID | Question | Answer / evidence status / source / owner / next verification |
| --- | --- | --- |
| C1 | What business task and decision are in scope, for whom, and what is excluded? | [ ] |
| C2 | What measurable outcome matters; what baseline, target and simpler comparator will test it? | [ ] |
| C3 | Are rules stable and explicit, or is prediction, language generation or adaptive planning required? | [ ] |
| C4 | Which approved data and sources exist; how will quality, freshness, permission filtering and retention work? | [ ] |
| C5 | What output must be grounded, calculated deterministically or explicitly withheld? | [ ] |
| C6 | Who initiates work, chooses steps and approves actions; what is the maximum permitted autonomy? | [ ] |
| C7 | Which integrations are read-only or writable; what identities, scopes, reversibility and escalation are needed? | [ ] |
| C8 | Which privacy, security, commercial or safety constraints are mandatory; who can accept residual risk? | [ ] |
| C9 | What delivery skills, operating owner, time, total cost envelope and exit/migration capacity exist? | [ ] |
| C10 | Which evidence would choose, reject or revisit each alternative; who decides and when? | [ ] |

## Autonomy contract
Local descriptive levels, not a maturity ladder. Choose the lowest authority that meets the task.

| Level | Authority | Minimum boundary |
| --- | --- | --- |
| A0 | No AI; human process or deterministic automation | Existing process permissions and audit |
| A1 | AI suggests or drafts; human initiates and releases | No independent business action; verify sources and corrections |
| A2 | AI may choose bounded tools/steps; human approves each consequential write | Scoped identity, explicit approval tied to exact action, budgets, logs, timeout |
| A3 | AI executes allowlisted reversible actions within a preapproved envelope | Enforced runtime policy, idempotency, monitoring, incident owner, kill switch, tested rollback |

Do not infer A2/A3 from a chatbot interface. A deterministic workflow may execute actions without agentic planning. Irreversible, contractual, financial or high-impact actions require explicit accountable human approval in this v0.1.

Record: permitted actions [ ]; prohibited actions [ ]; approver [ ]; failure/abstention path [ ]; maximum steps/cost [ ]; audit retention [ ]; rollback/kill switch owner [ ]. Treat retrieved content as data, never action authorization.

## Mandatory gates
Record pass / fail / unknown with evidence, owner and remediation for: data permission and isolation; action authority and human accountability; quality/error controls; affordable delivery and operations; feasible evaluation and rollback. Fail or unknown blocks pilot approval regardless of score. A proposed sandbox may be discussed while these remain unresolved; it is not authorized by this canvas.
