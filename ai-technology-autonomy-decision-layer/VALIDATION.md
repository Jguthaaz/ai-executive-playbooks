# Validation record
**Scope:** software/document checks, not model, client or business validation.

## Reproduce
From a complete repository checkout with Python 3 (standard library only):

```text
python ai-technology-autonomy-decision-layer/validate.py
python -m unittest discover -s simulator -p "test_*.py"
```

## Checks
- Synthetic default totals: template 4.10, fixed RAG copilot 3.75, bounded agent 2.35.
- Task-fit-priority totals: 3.50 / 4.10 / 3.10; reduced RAG fit: 3.50 / 3.10 / 3.10.
- Tie at 37.5% task-fit weight with equal remaining weights.
- Missing scores stay unknown; invalid weights/scores rejected.
- All mandatory gates must pass; fail/unknown blocks eligibility even with maximum scores.
- Relative file targets in new/updated Markdown exist; anchors and external URL availability are not covered.
- Four artifacts and MIT notice presence.
- Existing simulator regression suite, unchanged by this module.

## Review boundaries
Manual review: case preserves existing quotation scope, A1 human release and exclusions; tree distinguishes capability, RAG grounding, copilot interaction and agent orchestration. Default preference favors templates. Scorecard inputs are explicitly qualitative assumptions; totals are arithmetic rather than observed performance.

No implementation of a model, retrieval index, control enforcement, SaaS integration or agent was tested. Source permission filtering, hallucination/abstention, prompt injection resistance, security, cost estimates, task quality, timing and adoption remain unvalidated. No client validation or business result is claimed. Markdown is not a paginated one-page export.

## Executed November 9, 2026
- Module: 9 tests passed using Python 3, standard library only.
- Existing simulator: 4 regression tests passed, with its code and fixtures unchanged.
- Cost subtotal arithmetic checked: USD 2,400 / 9,800 / 20,800, excluding the listed unestimated costs.
- Validation was local against files retrieved from the pinned main baseline plus this change. No hosted CI run is claimed; the repository has no existing CI workflow in the inspected tree.
