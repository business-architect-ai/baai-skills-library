# Decision packet contract

Use guarded finalization when the runtime can write JSON and execute the packaged
standard-library Python scripts. This path is runtime-neutral: the same packet and gates apply
to L0, L1, L2, and imported synthesis. If those local capabilities are unavailable, use the
output contract directly and disclose that finalization is best-effort rather than enforced.

## State machine

1. Fusion or the final L0 pass produces one UTF-8 `decision-packet.json`: a raw JSON object with no Markdown code fence,
   preamble, or trailing commentary.
2. Run `scripts/check_decision_packet.py PACKET`.
3. If invalid, give the same finalizer context only the original packet and the exact validator
   errors. Permit one packet-only repair; this does not authorize new reads, research, dispatch,
   or writes beyond the packet.
4. Validate the repaired packet once.
5. Render a valid packet with `scripts/render_decision_packet.py PACKET`.
6. After a second validation failure, use `render_decision_packet.py --safe-failure PACKET` and
   return its procedural failure. Never start another repair.

The validator exits `0` for valid, `1` for contract-invalid, and `2` for invocation or read
failure. The renderer exits `0` for valid output, `1` when normal rendering rejects an invalid
packet, `2` for invocation or write failure, and `3` after deliberately rendering a safe failure.

## Common object

Required top-level fields:

```text
schema_version, mode, outcome, answer, criteria, options, selected_option_id,
supported_facts, inferences, assumptions, disputed_claims, decision_basis,
information_gaps, next_action, risks, change_conditions, confidence,
material_dissent, coverage
```

`schema_version` is `1.0`. `mode` is `decide`, `review`, or `synthesize`. `outcome` is
`substantive` or `procedural`.

Use these exact shapes:

```text
criterion = {id, label, material, source_ids}
assessment = {criterion_id, status, evidence_ids, note}
option = {id, label, assessments}
supported fact = {id, claim, source}
inference = {id, claim, premise_ids}
assumption = {id, claim, sensitivity, verification}
disputed claim = {id, claim, source, decision_use}
decision basis = {id, claim, support_ids, criterion_ids, defeats_option_ids}
information gap = {id, claim, critical, verification}
verification = {action, completion_gate}
completion gate = {kind, value}
next action = {action, owner, completion_gate, gap_ids}
risk = {risk, safeguard}
change condition = {condition, effect}
material dissent = {claim, consequence}
```

All plural top-level epistemic and result fields are JSON lists, even when empty. In particular,
`material_dissent` is a list of `{claim, consequence}` objects; it is never one object.

Identifiers match `^[a-z][a-z0-9-]{0,63}$`. Gate `kind` is `threshold`, `test`, `artifact`, or
`state`; `value` names the observable threshold, result, artifact, or transition. Use `unknown`
as the owner only when no owner is known. Assessment `status` is `meets`, `fails`, or `unknown`.

`confidence` contains `evidence_quality`, `evidence_reason`, `independence`,
`independence_note`, and `residual_uncertainty`. `residual_uncertainty` is a list of strings,
even when there is only one uncertainty. Evidence quality is `strong`, `moderate`, `weak`, or
`insufficient`; independence is `L0`, `L1`, `L2`, or `imported`.

`coverage` contains lists named `consulted_sources`, `omitted_sources`, `limitations`, and
`failures`. Sources are labels or authorized relative paths. Never put secret contents, absolute
paths, home-relative paths, NUL bytes, or parent-directory traversal in the packet.

## Mode content

`review` also requires:

```text
review = {
  prioritized_findings: [{severity, finding, evidence_ids}],
  recommended_changes: [text],
  next_validation_step: {action, owner, completion_gate, gap_ids},
  strengths_to_preserve: [text]
}
```

Severity is `critical`, `important`, or `minor`.

`synthesize` also requires:

```text
synthesis = {
  implications: [text],
  irreducible_differences: [{difference, assumption_ids}],
  imported_analyses: [source label or authorized relative path]
}
```

## Eligibility gates

Every material criterion must be assessed exactly once for every option. `meets` and `fails`
assessments require supported facts or eligible inferences. An eligible inference has an acyclic
premise chain ending only in supported facts. Assumptions and disputed claims cannot become
inference premises or decisive support.

A substantive outcome requires an existing selected option, `meets` for all of its material
criteria, eligible decision-basis support, and eligible basis entries that defeat every material
alternative. If an alternative loses only because evidence is missing, it is not defeated.

A procedural outcome selects no option, and `decision_basis` must be an empty list. It requires
at least one critical information gap and a next action that references that gap and defines an
observable completion gate. Use procedural when decision-critical behavior, boundary, effort,
capacity, security, timing, or another material premise remains unverified.

The validator detects conservative lexical duplicates across epistemic classes; it does not
claim semantic duplicate detection. It enforces structure, traceable linkage, and eligibility,
but cannot prove a natural-language claim true or perfectly classify evaluative language. Source
verification and the output contract's epistemic audit remain required.

## Rendering boundary

The renderer validates the packet itself and ignores any caller-supplied validation claim. It
owns every level-two heading and flattens model-provided line breaks, so packet text cannot add a
preamble, heading, or code fence. It formats packet content but never invents evidence, rankings,
sources, or confidence.

Safe failure never uses the packet's answer or selected option. It emits the mode's exact heading
sequence, reports validation codes, labels evidence insufficient, requests human review or the
smallest missing check, and discloses that guarded finalization failed.
