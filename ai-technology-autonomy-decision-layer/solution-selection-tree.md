# Solution Selection Tree
**v0.1 · original vendor-neutral decision guide**
[Canvas](technology-decision-canvas.md) · [Scorecard](architecture-trade-off-scorecard.md)

Use the numbered branches as the readable tree. Record the path and evidence IDs in the brief; uncertain answers lead to investigation, not a guessed product.

1. **Is the problem and baseline established (C1–C2)?**
   - No/unknown → investigate or defer. Include no change, process redesign, document cleanup and conventional search.
   - Yes → 2.
2. **Can a simpler process or deterministic rules meet the acceptance criteria (C3)?**
   - Yes → retain no-AI/process improvement or deterministic automation as preferred comparator.
   - No/unknown → 3; unknown means test both, not approve AI.
3. **Is the primary need a prediction/classification from structured historical data (C3–C4)?**
   - Yes → evaluate conventional ML against rules, with labeled-data quality, leakage, holdout, drift and operating-cost evidence. ML is not a default route for language drafting.
   - No → 4.
4. **Is language generation/synthesis needed (C3–C5)?**
   - No → revisit the problem and conventional analytics; do not force generative AI.
   - Yes → compare a bounded model call/workflow. If current proprietary facts must support claims, add retrieval/grounding (RAG) with permission filtering, source versions, citations and abstention; RAG does not guarantee correctness.
5. **Does a person initiate, inspect and release the work (C6)?**
   - Yes → use a copilot experience at A1; it can include RAG and deterministic steps.
   - No → a triggered deterministic workflow may suffice; a headless trigger alone does not require an agent.
6. **Must the system adaptively choose tools or plans beyond a known sequence (C6–C7)?**
   - No → retain fixed orchestration; document why an agent is unnecessary.
   - Yes → compare one bounded agent with fixed orchestration. Require evidence the flexibility improves the task enough to cover extra cost and failure modes. Set A2/A3 only through the autonomy contract and gates.
   - Multi-agent → only if separate tool/permission boundaries or measured task benefits justify coordination overhead. Role labels alone are insufficient.
7. **Do all mandatory gates pass (C4, C6–C10)?**
   - Fail/unknown → hold pilot approval; assign evidence/remediation and review date.
   - Pass → compare eligible configurations using the scorecard, challenge sensitivity, then request human decision.

## Architecture before product
For the selected pattern compare existing approved SaaS, configured low-code and custom implementation. Document identity/permission fit, required customization, operating skills, portability/export and exit cost. Do not equate one vendor product with RAG, copilot or agent.

## Boundary probes
- Stable approval routing → deterministic automation, even if triggered automatically.
- Demand forecast with usable labeled history → conventional ML candidate.
- Approved-catalog drafting with human release → RAG + A1 copilot + fixed workflow candidate.
- Variable incident diagnosis requiring tool choice → bounded agent candidate, subject to controls.
- Missing rights to source data → hold, even if every architectural score is 5.
