# Scoring Rubric

Score each accepted candidate from 0 to 3 on every dimension. Cite the contract or evidence that justifies each score; do not infer missing details. Maximum: 15.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Reusability** | One-off or source-specific; no credible reuse | Repeats only in a narrow case | Reusable across similar tasks or sources | Reusable across domains, sources, or projects |
| **Operational clarity** | No executable rule, or required contract elements are missing | Intent is present, but steps, boundaries, or handoffs are materially ambiguous | Trigger and operation are usable with minor interpretation | Trigger, inputs, process, outputs, boundaries, and handoffs are explicit |
| **Verifiability** | No observable success check | Subjective check with no defined comparison or criterion | Defined check, rubric, or comparison with some judgment | Objective or repeatable validation with clear pass/fail evidence |
| **Durability/vendor independence** | Depends on transient news, pricing, benchmark, interface, or unavailable vendor feature | Strong vendor/version dependence; portability is costly | Some disclosed dependency, but the core pattern transfers | Stable capability independent of vendor, version, price, and interface |
| **Leverage** | No meaningful improvement over ad hoc work | Local or modest benefit | Repeated savings, quality, or risk reduction | Multiplies capability across many tasks or unlocks other assets |

## Eligibility and exclusion

- A build-shortlist candidate needs at least **10/15**.
- A candidate scoring **0 in operational clarity or verifiability is excluded** from accepted instruments, workflows, and evals and goes to `Rejected or incomplete signals`.
- Any item scoring **0 in reusability** is excluded from the build shortlist; retain it only as evidence or a rejected signal.
- A principle requires concrete enforcement. It may be retained below 10, but it cannot enter the build shortlist below 10 or with any zero in operational clarity or verifiability.
- The build shortlist contains **at most five** items and is ordered by expected value relative to build effort. Ties favor stronger evidence, then lower effort.

## Vendor dependence

Abstract the durable capability before scoring. A named product, model, release claim, price, benchmark, interface path, or temporary feature is evidence, not the candidate identity. Disclose unavoidable dependencies and lower durability accordingly. Vendor dependence is not automatic rejection when the user's requested task is vendor-specific, but public time-sensitive claims remain unverified unless separately verified.

## Deduplication tests

Before scoring the final set, compare every apparent pair:

1. Do they solve the same problem?
2. Do materially equivalent triggers invoke them?
3. Do they produce materially equivalent outputs?
4. Do they use materially equivalent validation?

**Merge** only when all four answers are yes. Keep one record, preserve every source, and note meaningful variants. If any answer is no, keep separate candidates.

**Compose** when distinct candidates are useful in an ordered sequence or handoff. Record the sequence, component roles, handoffs, combined output, and end-to-end validation under `Workflow compositions`. Common co-use is not evidence of duplication, and composition never replaces each component's own contract or score.
