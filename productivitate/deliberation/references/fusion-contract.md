# Fusion contract

Fusion is an internal stage. It receives only valid finalized/frozen perspectives marked `sealed: true`, their provenance, the canonical brief, the context coverage manifest, and applicable bounded challenge results. It cannot use drafts or unfinalized results. L0 finalized passes remain eligible despite disclosed prior-context exposure, but are non-independent. L1/L2 inputs are eligible for those levels only when blind, isolated, and free of peer-result exposure before finalization.

## Fusion recipe

Follow this order:

1. Normalize claims and provenance.
2. Map genuine agreement without counting duplicated lineage twice.
3. Identify contradictions and underlying assumptions.
4. Preserve unique decision-relevant insights.
5. Detect suspicious consensus and shared blind spots.
6. Compare options against criteria and sensitivity cases.
7. Select the recommendation from evidence strength and robustness.
8. Preserve unresolved dissent and decision-changing conditions.

## Stage requirements

### Normalize

Separate supported facts, inferences, assumptions, disputed claims, and verification needs. Keep source lineage attached to each claim. Translate vocabulary without flattening meaningful differences.

### Compare

Treat convergence as information about agreement, never as proof. Shared sources, prompts, model lineage, or missing evidence can create suspicious consensus. Compare the recommendation under plausible changes to material assumptions and show why the winning option defeats material alternatives.

### Select

Choose from evidence strength, criteria fit, constraint compliance, reversibility, and robustness. Evidence quality and independence level remain separate dimensions. Self-assessed confidence remains qualitative diagnostic input.

### Preserve

Carry forward unique insights, unresolved material dissent, conditions that change the conclusion, missing evidence, executor failures, and coverage limits. If the evidence cannot support a substantive conclusion, select responsible abstention and its smallest information-gathering action.

## Rejected aggregations

Fusion does not use voting, majority selection, response length preference, or averaging self-reported confidence. No one of these is evidence that an option is correct.

## Fusion result

Return an internal record containing:

- selected recommendation, verdict, or combined conclusion;
- decisive evidence and reasoning;
- why material alternatives lost;
- evidence-quality assessment;
- recorded independence level and lineage caveats;
- material dissent and sensitivity cases;
- responsible next action;
- coverage, verification, and failure limitations.

The finalizer translates this record using `output-contract.md`; it does not expose hidden reasoning or raw perspective dumps by default.
