# AI Opportunity Prioritization: Impact and Effort

**Status:** published illustrative case · v0.2. AI-assisted; no real-world validation.
**Date:** October 12, 2026. Entirely hypothetical; no pilot or measured outcomes.

## Decision and scenario

A fictional B2B maintenance company seeks growth and profitability and can investigate one pilot. Each option covers one team and a limited workflow with human approval.

| Option | Invented scenario inputs | Bounded approach | Non-AI alternative |
| --- | --- | --- | --- |
| A. Quotation assistant | 200 quotations/month, 90 minutes each; inconsistent catalog and proposal formats | Draft sections for one service line; no autonomous pricing | Standard templates and curated catalog |
| B. Request triage | 1,500 requests/month, 8 minutes each; stable taxonomy and labeled history assumed | Suggest category and routing for one queue; no automated emergency decisions | Intake forms and routing rules |
| C. Technical knowledge | 600 lookups/month, 15 minutes each; some manuals lack verified versions | Retrieve approved guidance for one equipment family with source references | Current manuals and improved search |

All numbers and conditions are invented. Permissions, owners and real baselines remain unverified. Initial tests would use synthetic inputs. Assumed current workload is 300, 200 and 150 hours/month respectively: these are NOT savings. Review overhead, attainable reduction and adoption are unknown.

## Method

The portfolio owner proposed **business impact** and **implementation effort**, with subdimensions. The assistant proposed the case, weights and illustrative scores. Weights sum to 100% within each dimension.

Score 1–5: impact 1 = limited, 3 = moderate, 5 = substantial; effort 1 = limited preparation/change, 3 = moderate, 5 = extensive. Intermediate values are 2 and 4. Real application requires business-specific anchors and evidence. Unknowns should remain unscored until investigated.

Weighted dimension score = sum(score × weight). Keep impact and effort separate; do not turn them into an unsupported single ratio. Every score below has LOW confidence and illustrates the method only.

## Illustrative impact

| Variable | Assessment | Weight | A | B | C |
| --- | --- | --- | --- | --- | --- |
| Revenue and margin | Commercial capacity, conversion or profitability | 25% | 5 | 2 | 2 |
| Productivity and cost | Addressable work and rework | 30% | 4 | 4 | 3 |
| Customer experience and quality | Response, resolution and consistency | 20% | 4 | 4 | 4 |
| Risk reduction | Potential reduction of operational errors | 10% | 2 | 3 | 4 |
| Strategic alignment | Contribution to growth and profitability priorities | 15% | 5 | 4 | 3 |
| **Weighted impact** | | **100%** | **4.20** | **3.40** | **3.05** |

## Illustrative effort

| Variable | Assessment | Weight | A | B | C |
| --- | --- | --- | --- | --- | --- |
| Data preparation | Quality, currency and approved access | 25% | 4 | 2 | 5 |
| Technology and integration | Implementation and operational complexity | 25% | 4 | 2 | 3 |
| Process change and adoption | Workflow changes and training | 20% | 3 | 2 | 3 |
| Security and controls | Work to manage errors and protect information | 15% | 4 | 3 | 5 |
| Resources and time | Residual coordination and specialist capacity | 15% | 4 | 2 | 4 |
| **Weighted effort** | | **100%** | **3.80** | **2.15** | **3.95** |

Avoid double counting integration under resources, or business benefits under strategic alignment. Risk reduction measures potential benefit; controls measure implementation work. Decimal precision reflects arithmetic, not empirical certainty.

## Rationale and recommendation

**Investigate B first as a pilot candidate.** Recurring volume and a clear taxonomy support moderate potential impact with lower assumed preparation effort. Compare rules before choosing AI. The stable taxonomy and labeled history are key assumptions, not established facts.

**Keep A as the higher-impact strategic candidate.** Its commercial link and assumed workload suggest upside, but conversion and margin effects are unproven. Inconsistent sources and commercial review increase effort. If commercial value is verified and source preparation is manageable, A may take priority.

**Prepare C's content foundations first.** Approved, current manuals may improve quality and reduce search effort; uncertain versions raise both data preparation and control requirements. Confirm ownership and user demand.

This is a conditional recommendation. Matrix coordinates are (effort, impact): A (3.80, 4.20), B (2.15, 3.40), C (3.95, 3.05). No high/low thresholds have been validated. Urgency, capacity and evidence confidence also matter.

## Sensitivity

- If B's data and integration scores both rise from 2 to 4, effort rises to **3.15**; its advantage narrows.
- If A's revenue score falls from 5 to 3, impact falls to **3.70**; commercial upside needs validation.
- If C's data and controls scores fall from 5 to 2 after remediation, effort falls to **2.75**. Remediation itself still consumes resources and must be included in the full decision.

## Evidence before pilot approval

| Evidence | Purpose | Owner role to confirm |
| --- | --- | --- |
| Actual volume, task time and rework | Establish addressable work without claiming savings | Process owner |
| Conversion, margin and service baselines | Validate impact assumptions | Commercial / operations owner |
| Sample quality, taxonomy and permissions | Assess data readiness | Data / content owner |
| System dependencies and scoped design | Estimate integration work | Technology owner |
| Review burden and user needs | Assess adoption and realized benefit | Team lead |
| Error severity, controls and approval | Determine acceptable scope | Risk / security owner |

Approved data use, an accountable process owner and manageable critical errors are prerequisites. A high score cannot override an unresolved prerequisite.

## Proposed test for B — not executed

Define categories and error severity. Compare manual routing, rules and AI suggestions on identical synthetic requests, including ambiguous and out-of-scope cases. Separate category-development cases from evaluation cases. Record correctness, serious errors, abstention and human review effort. Set thresholds and resource limits before running the test.

Stop or redesign if categories cannot be agreed, serious errors cannot be controlled or simpler rules offer comparable performance with less effort. Synthetic results cannot establish real adoption, customer outcomes or ROI.

## Contribution and review record

- **Portfolio owner's explicit contribution:** two primary dimensions, impact and implementation effort, with subdimensions.
- **Assistant contribution:** synthetic scenario, weights, scores, calculations and conditional recommendation.
- **Publication:** authorized by the portfolio owner. Weights and scores remain illustrative, not independently validated.
- **Independent validation or real outcomes:** none.

The framework demonstrates prioritization reasoning. It is not a test of prompt reliability or evidence of a client engagement.

## En español

Caso ficticio de mantenimiento B2B. Se propone investigar primero clasificación de solicitudes por su impacto potencial moderado y menor esfuerzo supuesto. Cotizaciones tiene mayor impacto potencial y mayor esfuerzo. Conocimiento técnico requiere preparar sus fuentes. Tu contribución documentada es la elección de los dos ejes; pesos y calificaciones son supuestos ilustrativos, sin validación independiente.