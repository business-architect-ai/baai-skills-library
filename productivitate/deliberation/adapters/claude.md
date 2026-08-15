# Claude runtime adapter

This optional adapter maps runtime capabilities to the canonical deliberation
protocol. The canonical `SKILL.md` and `references/` remain the source of truth;
this adapter neither changes their semantics nor authorizes dispatch.

## Capability mapping

When authorized fresh Task workers or non-interactive sessions are available,
send each one unchanged canonical worker packet. Limit each worker to its
authorized context pack and its own result. Peer outputs remain unavailable
until accepted results are finalized and sealed.

Record executor class, model family when known, session identifier when known,
all reads, result path, and sealed status in the manifest. Use L1 or L2 only
when the resulting evidence demonstrates the required blind isolation, distinct
sessions, and (for L2) model-family diversity.

If the runtime cannot provide that evidence, if isolation is unavailable, or if
external execution is not authorized, perform ordered active-context passes.
Freeze each result before challenge or fusion, mark the manifest `L0`, and state
that no independent-consensus claim is being made. Do not upgrade the label from
an intended mechanism or an unverified session claim.

## Guarded finalization mapping

When local JSON writing and standard-library Python execution are available,
write `decision-packet.json` and run `check_decision_packet.py`. On failure,
return the exact errors to the same finalizer context for one packet-only repair.
Validate again. A second validation failure runs `render_decision_packet.py` in
safe failure mode; a valid packet runs its normal renderer.
A repair does not authorize new reads, research, dispatch, or implementation. If local execution
is unavailable, use the canonical Markdown contract and disclose best-effort
finalization.

## Non-core CLI illustration

Command-line execution is optional. Consult the locally installed runtime's
`--help` before choosing a fresh-session mechanism because supported commands
and flags vary. `<runtime-cli> --help` is illustrative discovery only; no named
agent, global installation path, fixed version-sensitive flag, or
permissions-bypass mode is required.
