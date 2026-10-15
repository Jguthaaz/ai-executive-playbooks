# Blueprint — quotation responsiveness with commercial control
**Status: Work in Progress · Hypothetical design · No program executed**

[Blueprint home](README.md) · [Reusable template](template.md) · [Value measurement](../value-realization-playbook/exercise.md)

## 1. Strategic intent and decision
Fictional Northstar ServiceCo wants more responsive quotation service and sustainable commercial capacity. The proposed transformation covers one service line, from request intake to approved quotation. It excludes autonomous pricing, contract commitments and enterprise-wide rollout.

**Decision:** whether process standardization is sufficient, and whether later AI assistance earns a bounded pilot. The 90-day horizon is a planning scenario, not a delivery promise or authorization.

Desired outcomes: reliable intake, approved source content, clearer handoffs, lower end-to-end friction and measurable quality. Targets remain proposals until baseline evidence is available.

## 2. Current-state hypotheses
No diagnostic work has been conducted. Each row is an assumption to test.
| Step / assumed friction | Potential consequence | Evidence required |
| --- | --- | --- |
| Request arrives through inconsistent channels | Missing fields and repeated clarification | Intake samples and missing-field frequency |
| Specialist assembles scope from fragmented content | Rework and uncertain source currency | Content inventory and task observation |
| Price / scope approval ownership is unclear | Waiting and duplicated reviews | Handoff timestamps and decision-rights review |
| Drafts are revised without structured error records | Quality issues remain hard to diagnose | Severity-coded correction sample |
| Effort and waiting are not tracked separately | Capacity claims may target the wrong bottleneck | Active-time logs and elapsed-time distribution |

A drafting assistant cannot solve an approval queue or unclear commercial authority by itself.

## 3. Target operating workflow
| Step | Target design | Proposed accountable role | Control / evidence |
| --- | --- | --- | --- |
| 1. Structured intake | Required fields, scope and exception flags | Sales operations lead | Completeness checks; manual exception queue |
| 2. Source preparation | Curated catalog with versions and access rules | Content owner | Approved source inventory and change history |
| 3. Draft preparation | Standard template; optional AI only after gate approval | Quotation process owner | Traceable inputs, no generated pricing |
| 4. Commercial review | Explicit price, scope and delivery checks | Commercial approver | Approval record and exception escalation |
| 5. Issue and feedback | Human-approved quotation; structured corrections log | Sales lead | Approved version and correction severity |
| 6. Performance review | Compare quality, active work, waiting and adoption | Process owner | Dashboard specification and decision log |

Roles are placeholders. One person may cover several roles only if conflicts and review independence are addressed.

### Exception path
Incomplete intake returns for clarification. Missing or conflicting source content goes to the content owner. Unusual contractual or pricing conditions go to the commercial approver. AI outputs with unsupported content are rejected and logged. A manual template workflow remains available throughout any future pilot.

## 4. Capability gaps and interventions
| Capability | Assumed gap | Proposed intervention | Readiness evidence |
| --- | --- | --- | --- |
| Process and decision rights | Inconsistent handoffs | Define intake, review and escalation rules | Walkthrough accepted by users and approver |
| Data and knowledge | Fragmented source content | Assign owner, curate versions and access | Approved catalog for the scoped service line |
| Technology | Unverified access and logging | Design minimal integration and audit trail | Security/access review and end-to-end test plan |
| People and adoption | Review burden and trust unknown | Involve users, rehearse exceptions and train reviewers | Role-based rehearsal and documented feedback |
| Measurement | No comparable baseline | Capture active time, waiting, corrections and costs | Metric definitions and baseline quality review |
| Governance | Funding and stop rights unclear | Separate discovery, pilot and scale decisions | Named authorities and recorded gate decisions |

## 5. Proposed governance and accountability
- **Sponsor:** accountable for scope, resources, gate decisions and escalation.
- **Process owner:** accountable for the operating workflow and benefits realization.
- **Delivery lead:** responsible for coordinating dependencies, actions and progress.
- **Content owner:** accountable for approved source content and updates.
- **Commercial approver:** accountable for quotation approval within existing authority.
- **Technology and risk leads:** assess access, security, error containment and operating support.
- **Finance representative:** validates costs and distinguishes capacity from realized cash effects.
- **Representative users:** test practicality and report friction; participation does not imply sign-off authority.

Proposed cadence: weekly delivery/dependency review; fortnightly sponsor decisions; gate reviews before any funding or scope expansion. Record evidence, disagreements, owners and revisit triggers. No actual roles have been assigned.

## 6. Illustrative 90-day roadmap
Phases sum to 90 calendar days. Work depends on access, available people and approvals; failure at a gate changes the schedule.
| Period | Work and outputs | Lead role | Exit decision / dependency |
| --- | --- | --- | --- |
| Days 1–15 | Validate problem, map active work and waiting, agree scope and baseline plan | Process owner | G1: sponsor confirms a material problem, owner, permitted inputs and evidence plan |
| Days 16–30 | Curate scoped catalog, define intake, template, approvals and exception handling | Operations / content owner | G2: process and sources are usable; otherwise remediate or stop |
| Days 31–45 | Rehearse template workflow on synthetic cases, train reviewers, define evaluation | Delivery / quality lead | G3: select process-only improvement, request a bounded AI test, or defer |
| Days 46–60 | If authorized, evaluate template vs AI on matched synthetic cases; document quality and review burden | Technology / quality lead | G4: risk, sponsor and process owner decide whether an approved real-data pilot is justified |
| Days 61–75 | Only after G4, run a scoped authorized pilot; otherwise continue process-only learning | Process owner | G5: assess evidence quality, adoption, full costs and operational support |
| Days 76–90 | Review benefits and controls, resolve ownership, document continue / redesign / stop decision | Sponsor / finance | G6: scale only with validated evidence and separate funding approval |

If AI is not justified at G3 or G4, use remaining time to evaluate the template, clarify approval queues and improve measurement. The plan does not require AI deployment to count as useful progress.

No fixed budget is implied. Estimate work packages, available capacity, support cost and contingency before each gate; reconcile scope differences with any investment-lab figures. Timeline alone does not establish resource feasibility.

## 7. Adoption and communications
| Audience | Need / concern | Proposed action | Feedback evidence |
| --- | --- | --- | --- |
| Quotation specialists | Added effort and loss of control | Co-design template, rehearse exceptions, preserve manual fallback | Observed task friction and correct workflow use |
| Commercial reviewers | Accountability and unreliable scope | Agree source checks, review rubric and authority | Review time and material corrections |
| Managers | Capacity use and customer response | Explain benefit hypotheses and redeployment choices | Documented reassignment, not assumed headcount savings |
| Content / technology owners | Maintenance burden | Define source update and incident routines | Support effort and unresolved incidents |
| Sponsor | Whether to continue investment | Concise evidence-and-decision brief at each gate | Recorded decision with rationale and dissent |

Communications are planned artifacts, not messages sent. Train on prohibited uses and escalation as well as normal operation.

## 8. Measurement and value ownership
Use the [Value Realization Playbook](../value-realization-playbook/exercise.md) for definitions and synthetic arithmetic. Track:
- Active preparation + review + correction time, against a template comparator.
- End-to-end turnaround separately from active time; inspect waiting.
- Material corrections and critical errors before and after review.
- Correct adoption among eligible tasks, not logins.
- Incremental setup, operating and support costs.
- Capacity actually reassigned and any independently verified spending changes.

The value playbook's base scenario does not justify scaling AI. This roadmap therefore includes a legitimate process-only path and stop decisions. No transformation benefit has been observed.

## 9. Risks, dependencies and stop conditions
| Risk | Response | Decision trigger |
| --- | --- | --- |
| Scope expands before foundations work | Keep one service line; require sponsor approval for changes | Freeze expansion while baseline or ownership is unresolved |
| Catalog lacks an accountable owner | Assign content governance before automation | Missing ownership blocks AI test |
| Improvement targets the wrong bottleneck | Measure waiting and active work separately | If approval waiting dominates, redesign approvals first |
| Review burden offsets drafting gains | Compare total active time with template-only workflow | No incremental benefit: redesign or stop AI |
| Critical errors escape review | Pause, investigate and reassess controls | Uncontained critical risk prevents continuation |
| Benefits are double counted | Finance review of attribution and overlap | Reject unsupported realized-value claims |
| Operating support is unfunded | Specify support owner, costs and incident process | No scale without sustainable operating ownership |

## 10. Limitations
This is a proposed operating design and sequence, not a completed diagnostic, implementation or validated methodology. No real users, systems, budgets or control effectiveness were assessed. Actual legal, security, labor, procurement and technology requirements must be established in context. Prepared with AI assistance; no employer or client information is included.
