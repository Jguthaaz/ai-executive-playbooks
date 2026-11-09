# Worked case — B2B quotation architecture decision
**v0.1 · fictional, AI-assisted extension · not a model run, pilot or client validation**
[Module home](README.md) · [Existing case](../examples/quotation-assistant.md) · [Reproducible inputs](case-scorecard.json)

This applies the new layer to the existing maintenance-services quotation case. It preserves its one-service-line scope, fictional catalog, human commercial approval and exclusions. It does not replace the existing pilot design or change the earlier portfolio priority.

## Completed canvas
All numeric business inputs and scores below are assumptions. “Pass” for authority means only that the proposed design includes a human boundary, not that enforcement was tested.

| ID | Scenario answer | Evidence status / source | Accountable role and verification |
| --- | --- | --- | --- |
| C1 | Draft scope, exclusions and clarification questions for one service line; no pricing, sending or contracts | Assumption; existing quotation case | Commercial owner: confirm task scope |
| C2 | Existing illustration assumes 200 quotations/month and 90 preparation minutes; total review-inclusive baseline unknown | Assumption, not observed; existing case | Evaluator: measure preparation, review and correction for manual and improved-template workflows |
| C3 | Language drafting from varied requests; service rules/prices remain deterministic | Qualitative scenario judgment | Process owner: test if templates alone suffice |
| C4 | Fictional catalog v1, service S1; no actual customer data; permission enforcement/freshness untested | Constructed source in existing case | Catalog/security owners: approve versions, access filtering and retention |
| C5 | Every scope claim needs a catalog reference; missing coverage leads to abstention; prices withheld | Proposed acceptance rule | Commercial evaluator: inspect unsupported claims |
| C6 | Human initiates, edits and releases; A1 maximum | Proposed design boundary | Commercial approver: approve exact content before release |
| C7 | Sandbox reads catalog, produces local draft; no writable CRM/email/pricing tools | Proposed architecture, no integration built | Technical owner: demonstrate scopes and blocked writes |
| C8 | No unapproved data access, unsupported commitments or release without human review | Mandatory constraints, untested | Security/commercial owners: verify controls |
| C9 | Four-week discovery/test window; proposed cap USD 6,000; skills, costs and owner availability unconfirmed | Illustrative budget/window, not authorization or quote | Sponsor/technical owner: validate full cost and capacity |
| C10 | Compare templates, fixed RAG copilot and bounded agent; investigate before funding deployment | Proposed decision/evidence plan | Sponsor: review at end of week 4 after any separately authorized test |

## Selection trace
Tree 1: baseline unknown → investigation, not pilot approval. For architecture exploration only, assume the task hypothesis is worth testing.
Tree 2: improved templates may suffice; retain them. Tree 3: prediction is not the primary need, so ML is deferred. Tree 4: drafting needs approved catalog grounding; propose RAG with citations and abstention. Tree 5: human initiates and releases, so A1 copilot experience. Tree 6: known retrieve → draft → review sequence; adaptive tool selection is unnecessary. Tree 7: gates remain unknown; hold pilot approval.

Proposed configuration: human copilot experience + RAG + fixed deterministic orchestration, without business-action tools. Compare approved configured SaaS/low-code and custom builds later against identity, data boundary, export, skills and full cost; no product is selected in v0.1.

## Architecture comparison
Order: task fit / simplicity / cost / delivery capability / control fit / time. Each score is an authored qualitative judgment, not test evidence. Default weights: 30/20/15/10/15/10.

| Alternative | Scores | Provisional total | Rationale and limitation |
| --- | --- | --- | --- |
| Improved template + curated catalog (A0) | 2/5/5/5/5/5 | 4.10 | Assumed limited flexible drafting, easiest delivery and strongest direct control; adequacy unknown |
| Fixed RAG copilot (A1) | 5/3/3/3/4/3 | 3.75 | Assumed flexible grounded drafting; added retrieval, source maintenance and review; fit/control unproven |
| Bounded adaptive agent (A2 proposal) | 5/1/1/1/2/1 | 2.35 | No additional task benefit assumed; extra tool selection, permissions and operation; exceeds permitted A1 authority |

No option is approved. Data, quality, budget and evaluation gates are unknown for all three. Human-release authority is a design pass for template and fixed RAG; the A2 agent fails the A1 scope boundary. All totals are provisional scenario arithmetic only.

Default preference is the improved template, not AI. If task-fit weight rises to 50% and other weights become 10% each, totals are 3.50 / 4.10 / 3.10. If RAG task fit then falls from 5 to 3, totals become 3.50 / 3.10 / 3.10 and templates lead again. Thus a recommendation to investigate RAG is conditional on proving an advantage over templates. For a task-fit weight w, with all other weights equal, template = 5 − 3w and RAG = 3.2 + 1.8w; they tie at w = 37.5%. This is preference sensitivity, not empirical confidence.

## Economics handed to the value register
Illustrative planning estimates, USD, first 12 months; not market pricing or measured labor:
| Alternative | Setup | Monthly operations excluding review | Exit reserve | 12-month subtotal excluding review |
| --- | --- | --- | --- | --- |
| Template | 1,000 | 100 | 200 | 2,400 |
| Fixed RAG copilot | 4,000 | 400 | 1,000 | 9,800 |
| Agent | 8,000 | 900 | 2,000 | 20,800 |

Subtotal = setup + 12 × monthly operations + exit reserve. Monthly operations conceptually include licensing/inference, storage, source upkeep and monitoring; allocations and taxes remain unknown. Human review, training, integration contingencies and opportunity costs must be added before financial approval. These rough estimates motivate favorable cost scores 5/3/1; scores remain judgment rather than calibrated price bands.

The USD 6,000 cap concerns a proposed four-week investigation/test only, not annual operations. Confirm a scoped quote within that cap before any authorization. Transfer measured total time, eligible volume, adoption and complete costs to the [value register](../value-realization-playbook/template.md). The assumed 300 preparation hours/month are activity, not savings. No ROI or cash savings are claimed.

## Executive Decision Brief — completed
**Decision:** hold pilot approval; recommend a costed comparison of improved templates and fixed RAG drafting. Sponsor/authority: roles to assign, not actual approvals. Review: end of week 4 after a separately authorized test; no calendar commitment.

**Why:** default scoring favors templates (4.10 vs 3.75). RAG becomes preferable only under stronger task-fit preference and verified drafting quality. An agent adds no required capability and its A2 proposal violates the A1 scope.

**Autonomy:** A1, user-initiated local drafts, approved catalog read only, mandatory human commercial release; no sending, pricing, discounts or commitments. Retrieved instructions cannot change permissions. On missing/contradictory evidence, abstain and escalate. Technical owner must demonstrate a stop control and deletion of sandbox artifacts; no production rollback is claimed.

**Evidence tranche proposed:** four weeks, USD 6,000 maximum subject to a scoped quote and owner approval. Before starting, commercial evaluator defines a rubric and freezes 30 held-out synthetic requests: 10 complete, 8 incomplete, 6 contradictory/out-of-scope and 6 malicious/unauthorized requests. Keep development examples separate. Test templates and RAG on identical tasks, blind/randomize order where practical, record source versions and preparation/review/correction time. Agent implementation is excluded.

**Illustrative preregistration proposal:** no unauthorized actions or unsupported price/contract claims; every material scope claim supported by approved sources; at least 27/30 cases acceptable after review; median total task time at least 20% below improved templates. Sponsor must accept or revise these targets and sample rationale before execution. Thirty synthetic cases are a learning exercise, not statistical proof of production performance.

**Stop/revise:** stop on an unauthorized action or uncontrolled critical error; revise source handling on citation/permission failures; choose templates if RAG lacks the agreed incremental advantage. Passing synthetic thresholds permits consideration of a separately approved representative pilot only. Scaling requires real workflow, security, adoption and complete financial evidence.

**Missing evidence / owners:** baseline and rubric (commercial evaluator), source permissions and action blocks (security/technical owners), delivery skills and cost (technical owner/sponsor). Fail or unknown gates block approval.

**Observed results:** none. Only documentation checks and arithmetic have been executed; see [validation](VALIDATION.md).
