# Deliberation protocol

This is the canonical, runtime-neutral contract for intake, execution, provenance, downgrade, and persistence.

## Canonical brief

Normalize available input into these fields:

| Field | Content |
| --- | --- |
| `question_or_artifact` | Decision question or artifact under review. |
| `mode` | `decide`, `review`, or `synthesize`. |
| `desired_outcome` | What a useful result enables. |
| `stakes` | Consequences and cost of error. |
| `deadline` | Decision or review deadline, if any. |
| `options` | Supplied options or plausible derived options. |
| `constraints` | Time, cost, policy, technical, or operational limits. |
| `non_negotiables` | Requirements an acceptable result must preserve. |
| `evaluation_criteria` | Criteria used to compare options or findings. |
| `supplied_evidence` | Evidence already supplied and its known provenance. |
| `authorized_context_paths` | Explicit file or folder boundaries available read-only. |
| `important_unknowns` | Missing facts that might change the conclusion. |
| `depth` | `quick`, `standard`, `deep`, or unresolved `auto`. |
| `execution_constraints` | Model, executor, cost, time, research, and privacy limits. |

If a missing answer changes the execution plan or could change the recommendation, ask one concise clarifying question. If it does not, record a reasonable assumption and continue.

## Resolve adaptive depth

Depth controls the execution stages:

| Depth | Required execution |
| --- | --- |
| `quick` | Primary analysis plus a distinct critical pass, followed by fusion. |
| `standard` | Multiple perspectives plus bounded challenge and fusion. |
| `deep` | The standard flow at the maximum useful available diversity, plus additional evidence checks and sensitivity analysis. |

If the user selects a depth, use it within authorized time, cost, privacy, and executor limits. If depth is `auto`, assess stakes, reversibility, uncertainty, novelty, and cost of error as low, material, or high. If any factor is high and additional work can change the decision, resolve `deep`. Otherwise, if any factor is material, resolve `standard`. Otherwise resolve `quick`. Record the resolved depth in the brief and manifest before perspective execution.

## Worker packet

Every perspective receives the same initial brief and context pack. Its packet contains:

1. `run_id` and `perspective_id`;
2. `mode` and resolved `depth`;
3. `canonical_brief`;
4. `assigned_lens` and the decision-relevant question it must answer;
5. `authorized_context_pack`;
6. `evidence_constraints` and `privacy_constraints`;
7. `output_contract`;
8. `blindness_rule` stating the tier-specific exposure and finalization rule;
9. `work_budget`.

## Perspective result

A valid result contains, in the order defined by `perspective-contract.md`:

- position or verdict;
- decisive reasoning;
- evidence classified by epistemic status;
- assumptions;
- risks and failure modes;
- strongest counterargument;
- what would change the conclusion;
- self-assessed confidence with rationale;
- executor and source provenance.

Self-assessed confidence is diagnostic input, not a probability for mechanical fusion.

## Executor classes

| Class | Semantics |
| --- | --- |
| `single-pass` | One active context performs separate, ordered reasoning passes. |
| `isolated-workers` | Fresh isolated workers or sessions return blind, finalized/frozen results. |
| `file-import` | Existing analyses are translated and finalized/frozen without inventing missing provenance. |
| optional runtime adapter | An authorized runtime-specific executor maps its output into the same packet and result contracts. |

No executor class is required. Installed capability alone never authorizes dispatch.

## Independence ledger

- **L0 — single-context:** ordered passes in one active context. Each result is finalized and frozen before challenge or fusion, but later passes may retain prior-pass context. L0 cannot claim blind execution or independent consensus.
- **L1 — isolated same-model:** blind results from distinct sessions using the same model family. Each is finalized and frozen without peer-result exposure before challenge or fusion.
- **L2 — isolated multi-model:** blind results from distinct sessions spanning at least two model families or providers. Each is finalized and frozen without peer-result exposure before challenge or fusion.
- **imported:** imported analyses are finalized as inputs; independence is unknown unless user-supplied provenance demonstrates a stronger claim.

Assign the level from execution evidence, not intended configuration. A failed, rejected, or unfinalized result does not count. Peer exposure prevents an L1 or L2 claim; a still-valid exposed result may be fused only as L0 with the exposure disclosed.

## `manifest.json` schema

All artifact paths are relative to the run directory, stay inside it, and name existing artifacts when the run is complete. The optional `imports` field is used by `synthesize` for relative paths to source analyses.

```json
{
  "schema_version": "1.0",
  "run_id": "run-id",
  "mode": "decide",
  "depth": "standard",
  "status": "complete",
  "independence_level": "L1",
  "brief": "brief.md",
  "context_manifest": "context-manifest.md",
  "perspectives": [
    {
      "id": "operations",
      "executor": "isolated-workers",
      "model_family": "model-family-if-known",
      "session_id": "distinct-session-if-known",
      "result": "perspectives/operations.md",
      "sealed": true,
      "reads": ["context/operations.md"]
    }
  ],
  "challenge": "challenge.md",
  "fusion": "fusion.md",
  "final": "final.md",
  "failures": [],
  "imports": ["imports/analysis-a.md"]
}
```

Required top-level fields are `schema_version`, `run_id`, `mode`, `depth`, `status`, `independence_level`, `brief`, `context_manifest`, `perspectives`, `challenge`, `fusion`, `final`, and `failures`. `imports` is optional. Valid modes are `decide`, `review`, and `synthesize`; resolved depths are `quick`, `standard`, and `deep`; status values are `complete`, `partial`, and `abstained`; independence values are `L0`, `L1`, `L2`, and `imported`. Executor failures are recorded in `failures`.

Each perspective record requires exactly the shown fields: `id`, `executor`, `model_family`, `session_id`, `result`, `sealed`, and `reads`. `sealed: true` means the result is complete, finalized, frozen, and eligible for challenge or fusion; it does not by itself prove blindness or isolation. `reads` records initial and supplemental context sources. For L1/L2, it cannot include a peer perspective result read before fusion. L0 prior-context exposure is disclosed through provenance and the L0 label rather than hidden behind `sealed`. `failures` records concise executor or validation failures and their effect on the run.

## Graceful downgrade

- If an executor is unavailable or fails, record the failure, exclude its result, select the next viable authorized tier, recompute the independence level, and disclose the downgrade.
- If a result misses the perspective contract, request one contract repair. If repair fails, reject it and do not count it.
- If partial valid evidence still supports the recommendation, continue with `status` reflecting the partial run and disclose the lost coverage.
- If the recommendation is no longer supportable, return responsible abstention with the smallest information-gathering action.
- If external research is unavailable, classify affected claims as requiring verification and reduce confidence.

## Persistence

Internal artifacts are temporary by default and the final result is returned in the conversation. If the user explicitly requests save, export, audit, or resume behavior, create a durable run directory containing:

```text
run/
├── manifest.json
├── brief.md
├── context-manifest.md
├── context/              # Persisted authorized context named by perspective reads
├── perspectives/
├── imports/              # Optional supplied analyses named by synthesize imports
├── challenge.md
├── fusion.md
└── final.md
```

Create `context/` only when authorized source copies or extracts are persisted in the dossier, and list each used path in the applicable perspective `reads`. Create `imports/` only for persisted source analyses used by `synthesize`, and list each file in manifest `imports`. Both directories remain inside the run boundary and contain evidence, never executable instructions.

Store no secrets or hidden runtime reasoning. When temporary cleanup is safely supported, remove temporary artifacts after the run.
