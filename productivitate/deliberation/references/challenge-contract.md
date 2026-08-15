# Challenge contract

Challenge is one bounded, targeted round after valid perspective results are sealed.

## Materiality

A material item is a claim, assumption, or disagreement whose resolution can change the option, verdict priority, next action, or confidence band.

Only material items enter challenge. The purpose is to learn whether the recommendation changes, not to make every perspective agree.

## Inputs

For each targeted item, prepare:

1. `item_id` and type: claim, assumption, or disagreement;
2. the competing sealed positions, quoted or normalized without changing meaning;
3. source and provenance pointers;
4. why resolution is material;
5. one specific challenge question or evidence check;
6. permitted verification methods and authorized context boundary;
7. remaining work budget.

The challenger receives only the sealed results and evidence needed for that item. It does not reopen unrelated issues.

## Output recipe

For each item, return:

1. **Finding:** the narrow answer to the challenge question.
2. **Evidence status:** supported fact, inference, assumption, disputed claim, or requires external verification.
3. **Evidence and provenance:** consulted sources, supplemental reads, and unavailable checks.
4. **Resolution:** resolved, bounded by sensitivity, or unresolved.
5. **Decision effect:** whether the option, verdict priority, next action, or confidence band changes.
6. **Decision-changing condition:** the observable fact or threshold that would produce a different effect.

Preserve unresolved contradictions for fusion and final output.

## Stop conditions

Stop challenge when any one condition is true:

1. the recommendation is robust across plausible assumptions;
2. the remaining disagreement cannot be resolved with available evidence;
3. further work has low expected decision value;
4. the configured budget is reached.

When stopping for conditions 2–4, record what remains unresolved and how it affects confidence or next action.
