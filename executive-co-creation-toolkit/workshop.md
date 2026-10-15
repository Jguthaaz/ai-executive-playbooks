# Worked exercise: improving quotation turnaround
**Status: Work in Progress · Hypothetical example · Not facilitated**

[Toolkit home](README.md) · [Blank template](template.md) · [Investment exercise](../decision-intelligence-lab/exercise.md)

## Problem and boundaries
Fictional company: Northstar ServiceCo, a B2B maintenance provider. The name and scenario are invented, with no intended reference to an actual business.

Assume 200 quotations a month and 90 minutes of preparation per quotation, inconsistent templates and fragmented approved service descriptions. These are invented discussion inputs, not observations. They imply 300 preparation hours a month, not 300 hours of possible savings.

**Problem hypothesis:** fragmented inputs and unclear handoffs may delay quotations and create rework. The actual bottleneck, customer impact and economic value are unknown.

**Workshop question:** what should we investigate first to shorten preparation and review while preserving price, scope and contractual controls?

Scope: one service line and internal quotation preparation. Exclude autonomous pricing, contractual commitments, customer-facing generation and production deployment. Do not assume AI is needed.

## Participants and decision rights
Six participants plus a facilitator; a participant may also keep time.
| Role | Contribution and accountability |
| --- | --- |
| Commercial sponsor | Owns the next discovery decision and its resource boundary |
| Sales lead | Explains commercial goals and customer friction |
| Quotation specialist | Represents day-to-day users and exceptions |
| Operations lead | Challenges delivery feasibility and handoffs |
| Data / technology lead | Checks source ownership, access and dependencies |
| Risk / finance representative | Challenges controls, cost assumptions and approval gates |
| Facilitator | Balances participation, separates assumptions from evidence and records dissent; does not decide for the sponsor |

## Preparation
Send the decision question and canvas in advance. For this exercise, use only the invented inputs above and synthetic quotation examples. In a real adaptation, request approved process maps, task-time distributions, rework reasons, source ownership and current controls; missing evidence remains a gap.
Prepare a shared board, timer and decision log. Ask each participant to bring one problem hypothesis and one reason their preferred solution could fail.

## 90-minute agenda
| Minutes | Activity | Facilitation move | Deliverable |
| --- | --- | --- | --- |
| 0–10 | Frame the decision and boundaries | Confirm sponsor, scope and what cannot be decided today | Agreed decision question |
| 10–25 | Map friction and perspectives | Silent notes first, then round-robin; label fact, assumption or question | Workflow and evidence gaps |
| 25–40 | Reframe and generate options | Ask for a process-only option before AI options; cluster duplicates | Three opportunity statements |
| 40–55 | Complete opportunity canvases | Small groups fill value, owner, evidence and failure modes | Three draft canvases |
| 55–70 | Prioritize | Score independently, reveal together and discuss divergent scores | Provisional matrix with dissent |
| 70–82 | Design the next discovery step | Define evidence, owner, scope, review date and stop condition | Discovery brief |
| 82–90 | Decide and close | Sponsor states decision; each participant names one unresolved concern | Decision log and follow-up commitments |

The intervals sum to 90 minutes. If evidence is inadequate, the valid output is an evidence-gathering decision rather than a forced winner.

## Questions to use
**Frame:** Who experiences the problem? Where does waiting occur versus active work? What would count as an improvement? Which constraints are non-negotiable?

**Explore:** Which explanation could contradict our hypothesis? Could clearer inputs or a template solve it? Whose perspective is missing? What happens in exceptions?

**Challenge:** What supports this score? What is still assumed? Where could an error cause harm? What human review would remain? Which option would we choose if AI were unavailable?

**Commit:** What evidence would change our minds? Who can provide it? What is the smallest reversible step? When do we stop, revisit or escalate?

## Opportunity canvas: constructed example
| Field | Illustrative entry |
| --- | --- |
| Opportunity ID / title | O2 — internal quotation drafting assistant |
| User and workflow | Quotation specialist drafts scope from approved service descriptions; manager reviews |
| Problem hypothesis | Repeated assembly work may consume time; no actual measurement |
| Desired change | Lower preparation plus review time without more material corrections |
| Proposed approach | Generate a draft from approved sources, flag missing information and retain human approval |
| Simpler alternative | Standard template with curated service descriptions (O1) |
| Value hypothesis | More capacity or faster response; conversion and margin effects unknown |
| Required sources / owner | Versioned service catalog and templates; operations owner to be confirmed |
| Dependencies | Consistent sources, approved access, evaluation set and user availability |
| Risks / controls | Incorrect scope or price: exclude generated pricing, require source checks and approval |
| Evidence gap | Time by step, correction rate, source currency and review burden |
| Smallest next step | Map ten synthetic quotations against source fields; compare template and assisted draft designs |
| Accountability | Sales lead proposes; sponsor authorizes discovery after owner and controls are confirmed |
| Disconfirming signal | Review burden offsets preparation reduction, or template addresses the same friction |

## Prioritization matrix
Use 1–5, with higher always more favorable. **Value:** 1 = local convenience, 3 = relevant process improvement, 5 = direct strategic contribution. **Feasibility:** 1 = major unresolved dependencies, 3 = manageable dependencies, 5 = ready inputs and owner. **Learning:** 1 = little new evidence, 3 = resolves one material question, 5 = tests a decision-critical assumption quickly. Values 2 and 4 interpolate.

Provisional score = 0.40 × value + 0.35 × feasibility + 0.25 × learning.
Weights express preferences, not facts. All scores and rationale below are invented and low confidence.
| ID | Opportunity | Value | Feasibility | Learning | Total | Rationale |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| O1 | Standard template and curated catalog | 3 | 5 | 4 | 3.95 | Assumed simple to explore; establishes a non-AI baseline |
| O2 | AI-assisted draft with review | 5 | 2 | 4 | 3.70 | Greater assumed upside; source and review dependencies |
| O3 | Intake and approval workflow redesign | 4 | 3 | 3 | 3.40 | May reduce handoff delays; ownership unclear |

Mandatory gates sit outside scoring: permitted data use, accountable owner and acceptable critical-error controls. Unknown or failed gates prevent pilot approval regardless of total. At this workshop, gates are unverified; the ranking only guides discovery.

Illustrative disagreement: sales rates O2 feasibility as 4; technology rates it 2. Retain the range and ask what source evidence would resolve it. Do not average away an unresolved blocker.
If O2 feasibility moves from 2 to 3, its total becomes 4.05 and overtakes O1. The ranking is therefore sensitive to a single assumption.

## Constructed deliverables and decision
These are sample outputs, not the results of a real meeting:
1. Shared problem hypothesis and scoped workflow.
2. Three canvases, matrix, assumptions and dissent.
3. **Illustrative sponsor decision:** investigate O1 first and assess O2 source readiness in parallel; do not fund a pilot yet.
4. **Discovery brief:** sales lead maps a synthetic workflow; technology lead inventories required source types; risk representative specifies prohibited outputs. Resource cap: two person-days, assumed for this exercise.
5. **Review:** ten working days after a future kickoff; no actual calendar event or assignment exists.
6. **Stop / revisit:** stop if no owner can be confirmed; revisit if handoff delays dominate active preparation or O2 source readiness changes.
7. **Evidence for next decision:** proposed time-measurement plan, source gaps, estimated review burden and explicit comparison with process-only options.

## Limitations
Ninety minutes creates a shared starting point, not validated consensus or an investment case. Participants are role placeholders, not real attendees. Ordinal scoring assumes comparable intervals and may hide power dynamics. Independent scoring and dissent help but do not remove bias. No savings, customer impact or workshop effectiveness has been demonstrated.
