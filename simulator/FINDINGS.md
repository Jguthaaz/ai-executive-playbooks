# Scenario findings
**Evidence:** calculations executed on synthetic data, October 12, 2026. No measured business impact.

Balanced impact/effort: A 4.20/3.80; B 3.40/2.15; C 3.05/3.95; D 3.70/3.65; E 4.05/4.80; F 2.85/2.35.

A (quotations), B (triage) and D (demand forecasting) are on the eligible frontier in the balanced scenario. F is dominated by B. C and E have unresolved fictional prerequisites, so cannot participate in that frontier even if their scores improve.

Growth weights increase A's impact to 4.55 and reduce B's to 3.05. This illustrates how business priorities change the comparison; it does not prove quotation automation creates growth. Effort remains fixed across the four named scenarios; custom controls can change it.

The frontier may remain stable across several scenarios while score gaps change. Do not manufacture a priority change to make the demo more compelling. Use the exported CSV to inspect all results.

## Verification
Four Python tests passed: known score and normalization, invalid values/weights, exclusion of blocked candidates from domination, and consistency with published A/B scores. Browser checks cover scenario change, custom weights, filtering, reset and zero-total handling. These establish basic software behavior, not business validity.

## Next decision
Investigate the evidence behind A/B/D, clarify constraints and validate readiness. Do not interpret illustrative precision, low-confidence assumptions or frontier membership as approval for investment or deployment.
