# Exercise 001 — selecting an AI investment discovery candidate
**Status: Work in Progress · Entirely hypothetical · No investment or pilot executed**

[Lab home](README.md) · [Synthetic CSV](data/synthetic-scores.csv) · [Decision template](template.md)

## Decision context and synthetic assumptions
Fictional Northstar ServiceCo wants to improve commercial responsiveness and operating capacity. Its committee can select one candidate for discovery, then decide separately whether to fund a pilot.
All numbers, constraints, roles, ratings and decision entries below are invented for this exercise. The scenario uses similar workflows to other portfolio examples but does not reuse their scoring models.

Assume a maximum pilot envelope of USD 60,000 and 12 weeks, including integration, evaluation, controls, training and contingency. Discovery has a separate assumed cap of USD 5,000 and two weeks. Each pilot estimate is a fictional point estimate, not a quote or validated cost. No expected revenues, savings or ROI are calculated.

| ID | Alternative | Synthetic operating context | Assumed pilot cost / weeks | Main uncertainty |
| --- | --- | --- | --- | --- |
| A | AI quotation drafting assistant, human approval | 200 quotations/month × 90 preparation minutes | USD 55,000 / 12 | Source consistency and commercial review burden |
| B | AI request triage suggestions, human routing | 1,500 requests/month × 8 handling minutes | USD 35,000 / 8 | Label quality, taxonomy and severe misrouting |
| C | Internal AI knowledge retrieval with citations | 600 lookups/month × 15 search minutes | USD 45,000 / 10 | Manual currency, permissions and retrieval reliability |
| D | Non-AI process standardization: templates, intake rules and curated catalog | Same broad improvement objective; narrower assumed upside | USD 15,000 / 6 | Whether process changes address the dominant bottleneck |

These volumes imply current task workloads, not savings; workloads overlap and must not be added as independent benefits. Each alternative represents a mutually exclusive first tranche for this exercise. Deferring investment remains available if gates or evidence are inadequate.

## Gates before scoring
A high total cannot compensate for failed gates:
- Approved data access and permitted use.
- Accountable process owner and available reviewers.
- Critical error controls, security review and escalation path.
- Pilot estimate within the assumed envelope and duration, with full costs.
- Evaluation plan against a manual or rules-based baseline.

All alternatives fit the invented cost/time limits on paper. Other gates remain **unknown**, including those for D. Therefore every ranking below is provisional for discovery; none is eligible for unconditional pilot funding.

## Criteria and anchors
Use favorable scores from 1 to 5. Scores 2 and 4 interpolate between the anchors. All judgments have low confidence.
| Criterion | Weight | 1 | 3 | 5 |
| --- | ---: | --- | --- | --- |
| Commercial contribution | 30% | Weak link to responsiveness or growth | Plausible indirect contribution | Direct link to a strategic commercial bottleneck |
| Productivity potential | 20% | Little addressable recurring work | Moderate recurring workload | Broad recurring workload plausibly addressable |
| Data / process readiness | 20% | Fragmented sources and unclear ownership | Usable inputs with material gaps | Curated inputs, clear workflow and owner |
| Control feasibility | 15% | Severe errors difficult to contain | Controls possible with material review | Bounded errors and straightforward review |
| Pilot affordability | 15% | Above USD 60k: fails cost gate | Above USD 35k to USD 45k | At or below USD 20k |

For affordability, score 4 is above USD 20k to USD 35k and score 2 is above USD 45k to USD 60k. This is an explicit cost rubric, not interpolation. Duration remains a separate gate. Readiness and controls use invented assumptions, not verified organizational conditions.

Commercial contribution excludes labor savings; productivity excludes revenue gains; readiness covers input/process preparation; controls cover error containment. Affordability covers total pilot cost. Some correlation remains: preparation and control work affect cost, so this model may penalize complexity more than once. Challenge weights before relying on the result.

## Scoring matrix and reproducible calculation
Weighted score = sum(weight as decimal × criterion score), on a 1–5 scale. Weights sum to 1.00. Higher is more favorable. No score is a probability or monetary return.

| ID | Commercial 30% | Productivity 20% | Readiness 20% | Controls 15% | Affordability 15% | Base total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 5 | 4 | 2 | 2 | 2 | **3.30** |
| B | 3 | 4 | 4 | 4 | 4 | **3.70** |
| C | 3 | 3 | 3 | 3 | 3 | **3.00** |
| D | 2 | 3 | 5 | 5 | 5 | **3.70** |

Example B = 0.30×3 + 0.20×4 + 0.20×4 + 0.15×4 + 0.15×4 = 3.70.

Rationale (also in the CSV):
- **A:** assumed direct commercial connection and recurring work; fragmented sources and scope/price errors complicate readiness and controls. USD 55k maps to affordability 2.
- **B:** indirect commercial contribution, repetitive handling and assumed stable labels. Human review and non-emergency scope make controls plausible. USD 35k maps to 4.
- **C:** plausible internal benefit but uncertain manual currency and evaluation demands; USD 45k maps to 3.
- **D:** smaller assumed commercial/productivity upside; simple inputs and visible rules support favorable readiness and controls. USD 15k maps to 5.

Even favorable readiness scores for B and D are assumptions. They do not establish that mandatory gates have passed.

## Sensitivity to executive priorities
Keep scores fixed and change weights; each row sums to 100%. All scenarios are preferences to discuss, not forecasts.
| Scenario | Commercial | Productivity | Readiness | Controls | Affordability | A | B | C | D | Leader |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Base | 30% | 20% | 20% | 15% | 15% | 3.30 | 3.70 | 3.00 | 3.70 | B / D tie |
| Commercial emphasis | 50% | 20% | 10% | 10% | 10% | 3.90 | 3.50 | 3.00 | 3.10 | A |
| Control / affordability emphasis | 15% | 15% | 20% | 30% | 20% | 2.75 | 3.85 | 3.00 | 4.25 | D |

The winner changes with priorities. A committee must agree on the decision objective rather than selecting weights to endorse a favorite.

### Sensitivity to uncertain inputs
Hold base weights fixed; change one assumption at a time:
| Change | Recalculation | Implication |
| --- | --- | --- |
| B readiness falls 4 → 3 | 3.70 − 0.20 = **3.50** | D leads at 3.70 |
| B pilot estimate rises USD 35k → USD 40k; affordability 4 → 3 | 3.70 − 0.15 = **3.55** | D leads |
| A readiness rises 2 → 4 | 3.30 + 0.40 = **3.70** | A ties B and D; controls still unresolved |
| D commercial contribution rises 2 → 3 | 3.70 + 0.30 = **4.00** | D leads |

A cost increase might also affect readiness or duration; one-at-a-time analysis does not model those dependencies.

**Break-even:** transfer weight x from readiness to commercial contribution, keeping all other weights fixed. B minus D starts at zero; the commercial difference is +1 and readiness difference is −1. Thus the new gap is 2x. The break-even is the base weighting itself. Moving 2.5 percentage points from commercial to readiness (27.5% / 22.5%) gives D a 0.05-point advantage; moving the same amount in the other direction favors B by 0.05.

**Decision implication:** the base case has no unique winner. Two decimal places reflect arithmetic, not empirical precision or evidence of superiority.

## Risk and evidence register
| Risk / assumption | Evidence needed before pilot | Proposed accountable role | Decision trigger |
| --- | --- | --- | --- |
| B taxonomy or labels are unstable | Approved sample audit; clear category definitions and exception policy | Operations / data owner | If inconsistent, compare rules or defer B |
| Misrouting a critical request | Severity taxonomy; synthetic critical and ambiguous cases; escalation design | Risk / operations | Any uncontrolled critical path blocks scope approval |
| A invents scope or pricing | Source traceability, prohibited outputs and reviewer protocol | Sales / risk | No autonomous pricing; unresolved scope errors block pilot |
| C uses outdated or restricted manuals | Version inventory and permission checks | Content / security owner | Missing provenance blocks affected content |
| Costs omit integration or review | Full estimate including evaluation, change and contingency | Finance / technology | Above envelope requires redesign or separate approval |
| Adoption or review time erodes value | User walkthrough; plan to measure end-to-end time and correction burden | Process owner | No credible evaluation or owner: defer |
| Weighting hides disagreement or double counting | Independent scoring, criterion review and recorded dissent | Committee chair | Revisit model before releasing funds |

Owner roles are placeholders; nobody has actually been assigned. No controls or evidence checks have been performed.

## Illustrative decision record — not an actual authorization
**Decision:** nominate B for a bounded discovery step, benchmarked against rules and D's process improvements. Do not release the pilot budget on the basis of this matrix.

**Why:** B and D share the highest base total, and D leads under a control-focused preference set. B is nominated only as a learning candidate because its assumed recurring taxonomy offers a specific hypothesis to test; the matrix alone does not distinguish B from D. The next useful investment is evidence to discriminate them, not a commitment to AI.

**Proposed discovery tranche:** up to the assumed USD 5k and two weeks, subject to sponsor approval, an owner and permitted inputs. Use synthetic cases initially. Inventory taxonomy and source requirements, obtain a full cost estimate and define comparative evaluation. No discovery has occurred.

**Pilot release conditions:** gate evidence recorded; baseline and held-out evaluation cases defined; error-severity thresholds and acceptable review burden approved before testing; cost and duration confirmed. The matrix supplies no universal numerical thresholds.

**Stop / defer:** no owner, impermissible data use, uncontained critical errors, or evidence that simpler rules offer comparable value with lower total burden. Re-score if costs, readiness or priorities change.

**Deferred:** A until source and control assumptions improve; C until provenance and user demand are clarified. D remains the active comparator and may become the preferred first investment.

**Review:** ten working days after a future discovery kickoff; sponsor and finance review evidence and record dissent. No real date, expenditure or business result is implied.

## Assumptions and limitations
- Weights and ratings were constructed with AI assistance, not elicited from an actual committee.
- Ordinal ratings are treated as interval values in an additive model; this is a simplifying assumption.
- Scores can compensate for each other only after mandatory gates pass; thresholds should be agreed in context.
- Synthetic data cannot establish demand, feasibility, error rates, savings or ROI.
- This is a first-tranche choice, not portfolio optimization: dependencies, sequencing, opportunity costs and interactions are simplified.
- No uncertainty distributions, confidence intervals, causal estimates or financial valuation are provided.
- The current model supports a structured discussion. Real investment requires verified evidence, governance and accountable judgment.
