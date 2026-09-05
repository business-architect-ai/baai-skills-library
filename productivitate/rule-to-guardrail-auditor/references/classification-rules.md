# Classification rules

## Atomic unit

An atomic instruction expresses one required, forbidden, preferred, or approval-gated behavior. Split a compound instruction if its clauses have different owners or enforcement types.

Example:

```text
If tests pass, deploy to production.
```

becomes:

1. verify test success before release readiness — candidate `CONTROL`;
2. authorize production deployment — `HUMAN_DECISION`.

## Ordered decision procedure

Apply these tests in order.

### 1. Human authority

Classify `HUMAN_DECISION` when compliance involves explicit approval, external effects, destructive or difficult-to-reverse changes, sensitive access, material cost, deployment, publication, messaging, permission changes, legal/compliance judgment, or acceptance of substantial risk.

Mechanical detectability does not supply authority.

Required details:

- `decision_owner` or `unspecified`;
- `approval_moment`;
- `information_required`;
- `prohibited_before_approval`;
- `retained_risk`.

### 2. Mechanical observability

Classify `CONTROL` only when all three exist:

- an observable trigger;
- a deterministic pass/fail condition;
- a feasible enforcement point or check.

Required details:

- `trigger`, `condition`, `enforcement_point`;
- `allow_behavior`, `failure_behavior`;
- `positive_test`, `negative_test`;
- `limitations`;
- `control_status: proposed`.

Do not call a control active, installed, verified, or native without direct evidence.

### 3. Contextual judgment

Classify `RULE` when an instruction expresses a meaningful domain constraint, preference, principle, or tradeoff whose correct application requires context.

Required details:

- `retained_instruction`;
- `judgment_required`;
- `anti_pattern`;
- `review_question`.

When evidence is insufficient for a stronger disposition, retain provisionally as `RULE`, set confidence `low`, record an ambiguity, and ask the smallest resolving question. Do not eliminate or automate by guesswork.

### 4. Noise

Classify `ELIMINATE` for:

- `vague` — no operational meaning or observable criterion;
- `duplicate` — repeats an applicable instruction without adding scope;
- `obsolete` — evidence shows its trigger or environment no longer applies;
- `contradicted` — conflicts with a more authoritative applicable rule;
- `non_actionable` — cannot change behavior as written.

Required details:

- `reason` from the list above;
- `replacement`, including an empty-intent explanation when no replacement is needed;
- `related_instruction_ids`, populated for duplicate or contradicted records.

Never eliminate a safety, legal, compliance, or approval requirement merely because a newer model seems more capable.

## Calibration cases

| Instruction | Disposition | Reason |
|---|---|---|
| Run tests before declaring completion | `CONTROL` | Command result and completion event are observable |
| Do not read `.env` | `CONTROL` | Path access can be denied or detected without reading content |
| Represent money as integer minor units | `RULE` | Domain constraint requiring contextual application |
| Write clean code | `ELIMINATE` | No operational definition or acceptance criterion |
| Publish after completion | `HUMAN_DECISION` | Publication is an external effect requiring authority |

These calibrate the method rather than override context. Explain any context-supported deviation.

## Finding types

### Contradiction

Two applicable instructions require incompatible outcomes under the same condition. Name both IDs, the overlapping condition, the incompatible outcomes, and a resolution question.

### Not a contradiction

- A general rule plus a clearly scoped exception.
- Equivalent wording; that is duplication.
- An unclear term; that is ambiguity.
- A rule known to be inactive; that may be obsolete.

### Ambiguity

Name the instruction ID, unclear term, execution impact, and smallest resolving question.

## Confidence

- `high` — source, context, trigger, and boundary are explicit.
- `medium` — disposition is supported but an implementation or scope detail is missing.
- `low` — evidence is insufficient; retain provisionally and surface the ambiguity.
