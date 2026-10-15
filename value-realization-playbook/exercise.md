# Exercise — from quotation assistance to verified value
**Status: Work in Progress · Hypothetical design · Not executed**

[Playbook home](README.md) · [Benefits register template](template.md) · [Transformation plan](../business-transformation-blueprint/blueprint.md)

## 1. Business objective and value tree
Fictional Northstar ServiceCo wants timely, accurate quotations and sustainable commercial capacity. The invented company name does not refer to an actual organization.

Objective → operational change → evidence → possible value:
- Faster approved drafting → lower preparation plus review time → measured minutes per comparable quotation → capacity available for reassignment.
- Better first-pass quality → fewer material corrections → severity-coded correction rate → less rework, without counting it again as separate time savings.
- Faster customer response → shorter end-to-end turnaround → timestamped elapsed time → a commercial hypothesis, not proof of higher conversion.
- Higher adoption → more eligible tasks using the workflow correctly → completed eligible tasks using the workflow / all eligible tasks → a benefit realization dependency.

Do not add these branches as independent monetary benefits: they overlap and some are causal hypotheses.

## 2. Scope and alternatives
One service line, internal drafts from approved catalog content, mandatory human approval. No autonomous pricing, contractual commitments or customer-facing generation.

Compare current practice, a standard template with curated catalog, and AI-assisted drafting using that same curated content. Separate catalog cleanup benefits from the incremental contribution of AI. The [investment lab](../decision-intelligence-lab/exercise.md) does not select this option as an approved investment; this exercise explores how value would be evaluated if quotation assistance were considered later.

## 3. Synthetic baseline and assumptions
All figures below are invented. They are not measurements from a real team.
| Input | Assumption | Evidence required in a real evaluation |
| --- | ---: | --- |
| Eligible quotations per month | 200 | Workflow logs and eligibility rule |
| Current preparation time | 90 min / quotation | Comparable task observations |
| Current review time | 20 min / quotation | Reviewer time logs |
| Current total active time | 110 min / quotation | Preparation plus review; avoid overlap |
| Standard-template total active time | 95 min / quotation | Proposed comparator; untested |
| AI preparation time when adopted | 50 min / quotation | Proposed test hypothesis |
| AI review time when adopted | 30 min / quotation | Include source checks and corrections |
| Adoption among eligible quotations | 60% | Observed correct use, not account activation |
| Loaded labor value | USD 40 / hour | Finance-approved capacity valuation |
| Incremental AI operating cost | USD 1,200 / month | Tooling, support, monitoring and training refresh |
| Incremental AI setup investment | USD 18,000 | Integration, initial evaluation and training |

The USD 18k is an independent incremental-cost assumption for this scoped exercise, not the USD 55k total pilot estimate in the investment lab. The figures are not interchangeable. Catalog cleanup and template implementation costs are excluded as shared foundations; they must be included in a full investment case. Eligible volume is assumed unchanged.

## 4. Worked arithmetic: capacity, not cash
Adopted volume = 200 × 60% = 120 quotations/month. Remaining 80 use the template in the target scenario.

Current workload = 200 × 110 / 60 = **366.67 hours/month**.
Template-only workload = 200 × 95 / 60 = **316.67 hours/month**.
AI-plus-template workload = (120 × 80 + 80 × 95) / 60 = **286.67 hours/month**.

- Template improvement versus current practice: **50 hours/month**.
- Incremental AI capacity versus template-only: **30 hours/month**.
- Combined potential capacity versus current practice: **80 hours/month**, not 50 + 80.
- Incremental AI capacity equivalent = 30 × USD 40 = **USD 1,200/month**.
- Capacity equivalent less AI operating cost = **USD 0/month**, before setup cost.

There is **no demonstrated cash saving**. Redeployment requires demand, scheduling and manager action. Cash savings require an actual reduction in spending, such as verified avoided overtime, with finance validation. No conversion uplift or incremental revenue is assumed.

The same time improvement cannot be counted both as labor savings and as productive capacity generating revenue without a separate, non-overlapping attribution model.

## 5. Sensitivity and break-even
Hold volume, template baseline, labor valuation and cost fixed. Each row changes only adoption or AI review time.
| Scenario | Adoption | AI prep + review | Incremental hours vs template | Capacity equivalent | Less USD 1,200 monthly operating cost |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base | 60% | 50 + 30 = 80 min | 30 | USD 1,200 | USD 0 |
| Lower adoption | 30% | 80 min | 15 | USD 600 | −USD 600 |
| Higher adoption | 90% | 80 min | 45 | USD 1,800 | USD 600 |
| Higher review burden | 60% | 50 + 45 = 95 min | 0 | USD 0 | −USD 1,200 |
| Lower review burden | 60% | 50 + 15 = 65 min | 60 | USD 2,400 | USD 1,200 |

Formula: incremental hours = 200 × adoption × (95 − AI total minutes) / 60.
At 80 AI minutes, operating-cost break-even in capacity-equivalent terms occurs at **60% adoption**. This is not cash break-even and excludes setup investment.
At the higher-adoption scenario, a simple capacity-equivalent setup recovery calculation would be USD 18,000 / USD 600 = **30 months**, assuming stable benefits and costs. It is not a cash payback forecast; it excludes discounting, ramp-up, shared costs and opportunity costs. Base assumptions have no positive recurring surplus to recover setup cost.

## 6. Proposed evaluation — not run
1. Confirm approved sources, process owner, prohibited outputs and an error-severity rubric.
2. Establish current baseline and case mix; separate active work from waiting time.
3. Compare template-only and AI-assisted workflows on matched synthetic cases; counterbalance order and keep evaluation cases separate from tuning examples.
4. Record preparation, review, corrections, total active time, elapsed turnaround and tool/support costs. Have reviewers assess quality without knowing the drafting method where feasible.
5. If safety and access gates pass, seek authorization for a bounded real-world pilot with approved data and a predefined sample-size rationale. Synthetic tests alone do not establish adoption or commercial value.
6. Report sample counts, variability, exclusions and uncertainty, rather than just averages. Distinguish process cleanup effects from AI effects.

## 7. Proposed benefit register and gates
Role names are placeholders, not real assignments.
| Measure | Owner role | Proposed evidence / cadence | Illustrative gate |
| --- | --- | --- | --- |
| Total active time vs template | Process owner | Task logs; weekly pilot review | At least 15 min lower on comparable tasks |
| Material correction rate | Quality lead | Severity-coded review; each evaluated case | No increase versus template comparator |
| Critical pricing / scope error | Risk lead | Record before and after human review | Any critical error escaping review pauses pilot |
| Correct adoption | Team lead | Eligible completed tasks; weekly | At least 60%, then challenge economic case |
| Incremental operating cost | Finance / technology | Full cost ledger; monthly | Recalculate if above USD 1,200 |
| Actual capacity redeployment / cash impact | Business / finance | Task reassignment or spending evidence; monthly | No realized-benefit claim without evidence |

Thresholds are invented proposal values requiring approval before testing. Passing time and adoption thresholds alone is insufficient: the base economic case does not cover setup cost.

## 8. Illustrative decision
**Do not approve scale on these assumptions.** First investigate whether process standardization delivers sufficient value, whether AI provides reliable incremental improvement and whether a credible use for released capacity exists.

A pilot could be considered for learning only with an approved learning budget and safety gates. Scaling would require validated quality, adoption, incremental economics, operating ownership and a funded benefits realization plan. Stop or redesign if review burden eliminates time improvement, critical errors cannot be contained, or the template offers comparable outcomes with less total burden.

## 9. Limitations and evidence status
All calculations are deterministic illustrations. No task has been observed, no user adoption measured and no causal or financial effect established. The scenario simplifies demand, seasonality, learning curves and workflow variation. AI assistance was used to prepare the material. The artifact demonstrates an approach to questioning value claims; it does not document value delivered.
