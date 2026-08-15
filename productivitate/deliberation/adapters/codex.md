# Codex runtime adapter

This optional adapter maps Codex capabilities onto the canonical protocol. Read and
apply the package's `SKILL.md` and `references/` contracts first; this file does
not add a stage, loosen a contract, or authorize external dispatch.

## Capability mapping

When the active runtime exposes fresh workers or subagents and the user has
authorized their scope, give each worker the unchanged canonical worker packet.
Give a worker only its authorized context pack and its own output location. Do
not expose peer results until every accepted result is complete and sealed.

For every accepted result, record the executor class, model family when known,
session identifier when known, every initial or supplemental read, result path,
and sealed status in the canonical manifest. Claim L1 or L2 only when this
record proves the required blind, distinct-session execution; capability
availability or intended configuration is not evidence.

If fresh isolation is unavailable, dispatch is not authorized, or the evidence
cannot establish blind workers, use ordered passes in the active context. Finalize
and freeze each pass before the next stage, label the manifest `L0`, and disclose
that it is not independent consensus. Never describe this fallback as L1 or L2.

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

An installed command-line runtime can be an optional mechanism for a fresh
session only. Consult its local `--help` before use because names and flags vary
by version. For example, treat `<runtime-cli> --help` as discovery, not as a
required command or protocol step. Do not require a global installation, a
version-specific flag, or a permissions-bypass mode.
