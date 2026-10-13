# Use Case: B2B Quotation Assistant
**Status:** hypothetical pilot design · AI-assisted · October 12, 2026.
**Execution:** not implemented or tested. No client, business outcome or personal delivery achievement is represented.

## Executive decision
Should a fictional maintenance-services company test AI-assisted quotation drafting, or first improve its templates and catalog?

This case develops option A from the [impact and effort prioritization](../experiments/01-ai-opportunity-prioritization.md). It demonstrates the transition from prioritization to a [pilot brief](../templates/pilot-brief.md), not a change to the earlier recommendation to investigate triage first.

## Business problem and value hypothesis
In the fictional scenario, commercial staff consult catalogs and prior proposals to prepare quotations. Sources have inconsistent formats. The earlier illustration assumes 200 quotations per month and 90 minutes of preparation each: 300 hours of task activity, not 300 hours of savings.

**Hypothesis:** assistance with grounded drafting could reduce preparation and rework while preserving commercial accuracy. Effects on conversion, revenue and margin are unknown and would need separate evidence.

## Workflow and scope
1. A commercial user enters a synthetic customer request.
2. The assistant identifies missing requirements.
3. It retrieves relevant sections from an approved, versioned service catalog.
4. It drafts scope, assumptions, exclusions and clarification questions with source references.
5. A commercial reviewer corrects and approves the draft.
6. Authorized staff complete pricing and contractual review in the existing workflow.

**Initial scope:** one service line, synthetic requests and approved fictional source documents.
**Excluded:** autonomous pricing, discounts, contractual commitments, customer messages, production integrations and actual customer data.

## Compare three approaches
| Approach | Expected advantage | Main limitation |
| --- | --- | --- |
| Current manual process | Familiar workflow and direct control | Baseline effort and rework must be measured |
| Improved template and curated catalog | Consistency with limited technical complexity | May require manual retrieval and adaptation |
| AI-assisted grounded draft | Flexible drafting and requirement clarification | Unsupported statements, review burden and source maintenance |

AI merits further investigation only if it offers a useful advantage over the improved-template approach.

## Illustrative input and expected behavior
**Synthetic request:** “Prepare a maintenance proposal for equipment family X at a customer site. Service frequency and coverage are unspecified.”

**Fictional approved catalog, version 1:**
- Service S1: preventive inspection for equipment family X.
- Service frequency: selected after a requirements review.
- Spare parts: excluded unless explicitly included in the approved quotation.
- No pricing or response-time commitments are supplied.

**Expected draft excerpt — manually constructed acceptance example, not model output:**
> Proposed scope: preventive inspection for equipment family X [Catalog v1, S1].
> Frequency: pending requirements review [Catalog v1, Frequency].
> Spare parts: excluded unless explicitly included in the approved quotation [Catalog v1, Exclusions].
> Please confirm equipment quantity, site conditions and desired coverage.
> Pricing and service-level commitments require authorized commercial review.

An acceptable assistant should not invent prices, frequency, equipment compatibility or response guarantees. Source references must support the associated statements. If the catalog does not cover the requested service, it should abstain and ask for review.

## Pilot design — proposed, not executed
**Roles to assign:** business sponsor, commercial process owner, catalog owner, evaluator and relevant technology/security reviewers. These are required roles, not actual appointments.

Prepare fictional catalog entries and synthetic requests covering complete, incomplete, contradictory and out-of-scope requirements. Add a request that asks for unauthorized discounts or guaranteed response times. Treat instructions inside source documents as untrusted content.

Use separate development and evaluation cases. Compare all three approaches on equivalent tasks, recording preparation and review effort separately. Have a commercial evaluator use a predefined rubric; do not let the assistant assess its own output as independent validation. A later real-data test requires approved access and a representative sample.

| Measure | Definition | Decision use |
| --- | --- | --- |
| Total task effort | Preparation + review + correction time | Compare effort with the improved-template baseline |
| Grounding | Whether each material claim is supported by an approved source | Detect invented scope or commitments |
| Requirements coverage | Relevant fields completed or explicitly flagged as missing | Assess completeness without encouraging guesses |
| Rework | Corrections needed, classified by severity | Understand reviewer burden |
| Appropriate abstention | Unsupported requests escalated rather than answered | Assess control behavior |
| Operating effort and cost | Tool usage, source maintenance and support | Evaluate economic plausibility |

**Thresholds and sample size:** not specified as facts. Agree them with the decision owner before testing, based on error severity and the intended next decision. A small synthetic exercise cannot establish productivity, adoption or ROI in production.

## Controls and stop criteria
- Version and approve source material; keep a traceable record of input, sources, output and human edits.
- Require human commercial approval; no automatic sending or commitment.
- Pause if the assistant produces unsupported pricing or contractual commitments, or if critical errors escape review.
- Redesign or stop if source quality cannot be maintained, permissions cannot be enforced or review effort erases the potential advantage.
- Prefer the improved-template approach if comparable quality is achieved with lower total effort and complexity.

## Conditional business case
Potential monthly capacity released =
eligible monthly volume × (baseline total minutes − assisted total minutes) × adoption rate ÷ 60.

All terms require measurement. Include review and correction in assisted time; account for unsuccessful cases. If calculating monetary value, distinguish capacity released from cash savings and subtract tool, maintenance, training and operating costs. Revenue gains require separate attribution; do not infer them from faster drafting.

## Exit decision
- **Stop:** critical errors are uncontrolled or simpler alternatives meet the need.
- **Revise:** promising drafting quality, but source preparation or reviewer burden remains unresolved.
- **Consider a limited pilot:** evidence supports the predefined criteria and owners approve the controls.
- **Consider scale later:** only after representative real-world evaluation, adoption evidence and an operational business case.

## Contribution and limitations
The assistant prepared this hypothetical use case to complement the portfolio owner's impact/effort framework. No observed results, model output, independent evaluation or prototype are claimed. The acceptance example is manually constructed.

## En español
Este caso muestra cómo convertir la oportunidad de cotizaciones B2B en una propuesta de piloto. Compara proceso manual, templates mejorados e IA; define métricas y conserva aprobación humana de precios y compromisos. Todos los datos y ejemplos son ficticios. El siguiente paso sería evaluar con casos sintéticos, no asumir ahorros o crecimiento.
