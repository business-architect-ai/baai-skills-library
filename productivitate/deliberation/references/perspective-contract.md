# Perspective contract

Each perspective answers a distinct, decision-relevant question from the same brief and initial context pack.

## Choose lenses

Choose lenses because they can change the option, verdict priority, next action, or confidence. Useful lenses may include domain feasibility, implementation, operations, user impact, risk, security, cost, opportunity cost, reversibility, evidence quality, or adversarial critique. State the question each lens must answer. A role label without a distinct decision question is not a perspective.

## Finalization and isolation

A perspective may read its worker packet and supplemental sources inside the authorized context boundary. Log supplemental reads in provenance and the context manifest.

Two states are distinct:

- **Finalized/frozen:** the result contract is complete, provenance and reads are logged, and content cannot change before challenge or fusion. Every accepted result at every tier requires this state; the manifest records it as `sealed: true`.
- **Blind/isolated:** the result was produced in a fresh isolated lane with no access to peer prompts, notes, or results before finalization. This stronger state is required for L1 and L2.

At L0, ordered passes share one active context and may retain prior-pass exposure. Finalize and freeze each pass before challenge or fusion, label the set L0 and non-independent, and do not claim blind execution. If an L1/L2 lane receives peer content before finalization, it cannot support L1/L2; it may be retained only as L0 when still valid and the exposure is disclosed.

## Positive result recipe

Return these sections in this order:

### POSITION OR VERDICT

State the recommended option or verdict in one clear sentence.

### DECISIVE REASONING

Give only the reasons that determine the position and explain why material alternatives lose.

### EVIDENCE

For every material decision-critical claim, use the applicable labeled class:

- **Supported fact:** claim plus source or observed artifact.
- **Inference:** conclusion plus supporting facts and reasoning link.
- **Assumption:** premise currently accepted without adequate evidence.
- **Disputed claim:** competing claims and the source of disagreement.
- **Requires external verification:** claim and the smallest verification needed.

If a class has no material entry, omit that class rather than inventing one.

### ASSUMPTIONS

List assumptions the position depends on and how sensitive the conclusion is to each.

### RISKS AND FAILURE MODES

Pair each material risk with impact, trigger, and available safeguard.

### STRONGEST COUNTERARGUMENT

Present the strongest evidence-based case against the position, then state whether it changes the conclusion and why.

### WHAT WOULD CHANGE THE CONCLUSION

Name observable evidence, thresholds, or conditions that would change the option, verdict, next action, or confidence band.

### SELF-ASSESSED CONFIDENCE

Use a qualitative band with a rationale based on evidence quality and residual uncertainty. This value is diagnostic and is never averaged during fusion.

### PROVENANCE

Record the perspective ID, executor class, model family and session identifier when known, initial and supplemental sources read, and any verification performed or unavailable. Do not infer missing provenance.

## Fusion-eligibility gate

A result is eligible for challenge or fusion only when all required sections are complete, provenance is attached, supplemental reads are logged, and the result is finalized and frozen as `sealed: true`. For L1/L2, eligibility for the claimed independence level additionally requires a distinct isolated session and no peer-result exposure before finalization. For L0, `sealed: true` records finalization only; prior-context exposure remains compatible with fusion but incompatible with an independence claim.
