# Output Contract

Use these seven report sections, exactly in this order. Render each section title as the exact unnumbered level-two heading shown below (for example, `## Build shortlist`); do not add numeric prefixes or use another heading level. Include every heading even when its content is `None`.

## Build shortlist

List at most five eligible candidates, ranked by expected value relative to build effort. Give each candidate's name, type, score, build effort, expected value, and a pointer to its complete record below. Do not place principles below the build threshold here.

## Instrument candidates

Record accepted invokable components whose inputs produce defined outputs.

## Operational principles

Record accepted rules that change behavior at a decision point, using the principle contract below.

## Workflow compositions

Record ordered cooperation among distinct instruments, principles, or evals. In addition to the complete workflow candidate contract below, state the sequence, handoffs, combined outcome, and end-to-end validation. Composition does not erase the component records.

## Evaluation gates

Record accepted rubrics, tests, validators, blind comparisons, and other quality gates separately from the work they assess.

## Rejected or incomplete signals

List rejected news, hype, volatile packaging, duplicates, and insufficiently operational ideas. For each, give the source evidence and rejection reason or missing contract element. Classify public time-sensitive vendor or reviewer claims as unverified unless separately verified.

## Sources processed

Inventory identifiers and paths when available. Mark each processed, skipped, unreadable, or incomplete; state language and coverage limits. For corpus batches, record revisions with the new evidence and reason.

## Complete candidate contract

Every instrument, workflow, and eval record must contain all fields:

- **NAME** — concise capability name.
- **TYPE** — exactly one of `instrument`, `workflow`, or `eval`.
- **PROBLEM SOLVED** — recurring operational problem.
- **TRIGGER** — observable condition for invocation.
- **INPUT** — required artifacts or information.
- **PROCESS** — bounded steps or decision logic.
- **OUTPUT** — produced artifact, state, or decision.
- **VALIDATION** — observable success check.
- **WHEN NOT TO USE** — scope boundary or contraindication.
- **VENDOR DEPENDENCIES** — `None` or explicit dependencies and portability limits.
- **SOURCE EVIDENCE** — minimal supporting passage or local file-and-line reference; preserve all independently supporting sources. Source-specific quantities remain evidence, not universal requirements unless independently supported.
- **CONFIDENCE** — `high`, `medium`, or `low`, with a short evidence-based reason.
- **BUILD EFFORT** — `low`, `medium`, or `high`, with a short reason.
- **SCORE** — dimension breakdown and total out of 15 from the scoring rubric.

An item missing TRIGGER, INPUT, PROCESS, OUTPUT, or VALIDATION is not an accepted instrument, workflow, or eval. Put it in section 6 and name the missing field.

## Principle contract

Every principle is recorded separately with:

- **RULE** — the operational directive.
- **WHEN IT APPLIES** — observable decision condition.
- **PREVENTED ANTI-PATTERN** — behavior the rule blocks.
- **ENFORCEMENT** — concrete mechanism or observable check.
- **EVIDENCE** — minimal passage or local file-and-line reference.
- **CONFIDENCE** — `high`, `medium`, or `low`, with reason.
- **SCORE** — the five-dimension breakdown and total.

A principle without concrete enforcement belongs in section 6. Principles may remain below the build threshold but never enter the shortlist unless eligible under the rubric.
