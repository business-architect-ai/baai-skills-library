# Generic CLI adapter

This adapter is for an authorized command-line environment with no assumed
vendor, command name, installation location, or flag set. The canonical package
and its references define all deliberation semantics.

## Sealed export and import flow

1. Export one unchanged canonical worker packet for each assigned perspective.
2. Run each packet in an isolated context that cannot read peer packets, peer
   outputs, or later challenge and fusion materials.
3. Import only a result that is complete under the perspective contract; request
   one repair when allowed and reject a result that remains incomplete.
4. Record executor, model family, and session identifier as known values or
   explicit unknown values, together with every read and the imported result
   path.
5. Seal every accepted result before challenge or fusion, then assign L1 or L2
   only when the recorded evidence proves the relevant isolation conditions.

If the environment cannot isolate workers or preserve sufficient provenance,
use the canonical active-context process, record `L0`, and disclose the
downgrade. Imported analyses remain `imported` unless supplied provenance proves
otherwise. No command-line mechanism is required for the core package.

## Guarded finalization mapping

When local JSON writing and standard-library Python execution are available,
write `decision-packet.json` and run `check_decision_packet.py`. On failure,
return the exact errors to the same finalizer context for one packet-only repair.
Validate again. A second validation failure runs `render_decision_packet.py` in
safe failure mode; a valid packet runs its normal renderer.
A repair does not authorize new reads, research, dispatch, or implementation. If local execution
is unavailable, use the canonical Markdown contract and disclose best-effort
finalization.
