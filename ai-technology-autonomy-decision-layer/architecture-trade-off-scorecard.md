# Architecture Trade-off Scorecard
**v0.1 · architecture worksheet; illustrative preferences**
[Canvas](technology-decision-canvas.md) · [Worked case](case-quotation-decision.md)

Reuse the [investment decision discipline](../decision-intelligence-lab/template.md): agree weights before scoring, keep unknowns unscored, preserve non-AI comparators, and apply mandatory gates first. This worksheet compares configurations for one task; it does not add a portfolio priority index.

## Favorable anchors
Intermediate 2 and 4 mean between adjacent anchors. Scores are ordinal judgments, not probabilities or measured performance. Local default weights sum to 100%; change them with the decision owner and explain overlap.

| Criterion | Weight | 1 | 3 | 5 | Evidence |
| --- | --- | --- | --- | --- | --- |
| Task fit | 30% | Cannot meet key task | Partial coverage; substantial review | Meets defined task with bounded review | Equivalent-task evaluation, C1–C5 |
| Simplicity | 20% | Adaptive multi-system orchestration | Retrieval plus fixed integrations | Existing process or one simple component | Component/dependency map, C3/C7 |
| Total cost affordability | 15% | Exceeds envelope | Within envelope with little reserve | Within envelope with substantial reserve | Setup + operation + review + exit estimate, C9 |
| Delivery capability | 10% | Critical skills/owner absent | Gaps with credible plan | Skills and operating owner available | Role/capacity evidence, C9 |
| Control fit | 15% | Required controls unavailable | Controls feasible but unproven | Required controls demonstrated | Permissions/action/evaluation evidence, C4/C6/C8 |
| Time to bounded test | 10% | Beyond decision window | Fits with dependency risk | Fits with buffer | Critical path estimate, C9 |

Control fit grades implementation burden/strength only after eligibility; it cannot compensate a failed gate. Costs must cover setup, licenses/inference, retrieval/storage, integration, monitoring, human review, source maintenance, training and migration; record currency, horizon, uncertainty and exclusions. No vendor price is implied.

## Calculation and uncertainty
Total on a 1–5 scale = sum(weight percent × score) / 100. Never normalize away a missing score; show total as unknown. Compare eligible alternatives only. A held alternative can have a provisional scenario total for discussion, labeled as such.

| Configuration / build style | Gate status and evidence | Six scores | Total | Rationale / confidence |
| --- | --- | --- | --- | --- |
| Process / no AI | [ ] | [ ] | [ ] | [ ] |
| Deterministic automation | [ ] | [ ] | [ ] | [ ] |
| ML or grounded assistant as relevant | [ ] | [ ] | [ ] | [ ] |
| Bounded agent if justified | [ ] | [ ] | [ ] | [ ] |

Test alternative weights and uncertain scores. State when the preference reverses or becomes a tie. Keep a cheaper adequate alternative; do not read a narrow score lead as evidence of superiority. Return cost/benefit estimates to the existing [value register](../value-realization-playbook/template.md).

The [case JSON](case-scorecard.json) and [validation script](validate.py) reproduce arithmetic, eligibility and the case's sensitivity. The script does not choose a technology for real users.
