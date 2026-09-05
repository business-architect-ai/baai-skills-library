# Audit packet schema 1.0

The JSON packet is the canonical machine-readable audit. All objects are closed: keys not listed here are invalid. All required strings are non-empty.

## Top-level object

| Key | Type | Constraint |
|---|---|---|
| `schema_version` | string | exactly `1.0` |
| `audit_id` | string | `r2g-YYYYMMDD-lowercase-slug` |
| `created_at` | string | ISO-8601 timestamp with timezone |
| `mode` | string | exactly `consultative` |
| `target_platforms` | string array | non-empty, unique values from `generic`, `codex`, `claude` |
| `sources` | source array | IDs unique |
| `instructions` | instruction array | IDs unique |
| `contradictions` | contradiction array | IDs unique |
| `ambiguities` | ambiguity array | IDs unique |
| `coverage` | coverage object | counts recomputed from records |
| `attestation` | attestation object | every action flag is `false` |

## Source object

Exact keys:

| Key | Type | Constraint |
|---|---|---|
| `id` | string | unique within `sources` |
| `kind` | string | `file` or `pasted` |
| `locator` | string | path or pasted-input identifier |
| `status` | string | `processed`, `skipped`, `unreadable`, or `incomplete` |
| `note` | string | coverage or limitation note |

## Instruction object

Exact common keys:

| Key | Type | Constraint |
|---|---|---|
| `id` | string | unique within `instructions` |
| `source_id` | string | resolves to one source ID |
| `location` | string | line, section, or pasted-input location |
| `original` | string | minimum source wording needed for traceability |
| `normalized` | string | one atomic instruction |
| `disposition` | string | `RULE`, `CONTROL`, `ELIMINATE`, or `HUMAN_DECISION` |
| `confidence` | string | `low`, `medium`, or `high` |
| `rationale` | string | evidence-bound classification reason |
| `details` | object | exact shape selected by disposition |
| `platform_feasibility` | array | exactly one record per target platform |

### `RULE` details

Exact string keys:

- `retained_instruction`
- `judgment_required`
- `anti_pattern`
- `review_question`

### `CONTROL` details

Exact string keys:

- `trigger`
- `condition`
- `enforcement_point`
- `allow_behavior`
- `failure_behavior`
- `positive_test`
- `negative_test`
- `limitations`
- `control_status` — exactly `proposed`

### `ELIMINATE` details

Exact keys:

- `reason` — one of `vague`, `duplicate`, `obsolete`, `contradicted`, `non_actionable`;
- `replacement` — precise replacement or explanation that no replacement is needed;
- `related_instruction_ids` — string array; every ID resolves. Populate for `duplicate` and `contradicted`.

### `HUMAN_DECISION` details

Exact string keys:

- `decision_owner` — use `unspecified` when unknown;
- `approval_moment`;
- `information_required`;
- `prohibited_before_approval`;
- `retained_risk`.

## Platform feasibility object

Exact string keys:

| Key | Constraint |
|---|---|
| `platform` | one requested target platform |
| `feasibility` | `native`, `scripted`, `advisory_only`, or `unverified` |
| `mechanism` | proposed generic or verified platform mapping |
| `evidence` | evidence used or explicit statement that it was not checked |

The platform set must equal `target_platforms` with no duplicates. A platform note cannot change the core disposition.

## Contradiction object

Exact keys:

| Key | Type | Constraint |
|---|---|---|
| `id` | string | unique within contradictions |
| `instruction_ids` | string array | exactly two distinct, existing instruction IDs |
| `overlapping_condition` | string | conditions in which both apply |
| `incompatible_outcomes` | string | behaviors that cannot both occur |
| `resolution_question` | string | smallest question that selects authority or scope |

## Ambiguity object

Exact string keys:

- `id` — unique within ambiguities;
- `instruction_id` — resolves to one instruction;
- `unclear_term`;
- `impact`;
- `resolving_question`.

## Coverage object

Exact keys:

```json
{
  "sources_total": 1,
  "sources_processed": 1,
  "sources_skipped": 0,
  "sources_unreadable": 0,
  "sources_incomplete": 0,
  "instructions_total": 1,
  "dispositions": {
    "RULE": 1,
    "CONTROL": 0,
    "ELIMINATE": 0,
    "HUMAN_DECISION": 0
  }
}
```

Every value is a non-negative integer. Counts must exactly match the source and instruction records.

## Attestation object

Exact keys:

```json
{
  "modified_sources": false,
  "installed_controls": false,
  "executed_tests": false,
  "accessed_secrets": false,
  "published": false,
  "deployed": false,
  "sent_messages": false,
  "statement": "No audited source, control, hook, configuration, or permission was modified."
}
```

Any `true` flag invalidates a V1 packet.

## Complete valid packet

```json
{
  "schema_version": "1.0",
  "audit_id": "r2g-20260905-example",
  "created_at": "2026-09-05T10:00:00+03:00",
  "mode": "consultative",
  "target_platforms": ["generic"],
  "sources": [
    {
      "id": "S001",
      "kind": "pasted",
      "locator": "user-message-1",
      "status": "processed",
      "note": "One explicit instruction."
    }
  ],
  "instructions": [
    {
      "id": "R001",
      "source_id": "S001",
      "location": "line 1",
      "original": "Use integers for money.",
      "normalized": "Represent monetary values as integer minor units.",
      "disposition": "RULE",
      "confidence": "high",
      "rationale": "This domain constraint requires contextual application.",
      "details": {
        "retained_instruction": "Represent monetary values as integer minor units.",
        "judgment_required": "Identify monetary fields and currency boundaries.",
        "anti_pattern": "Persisting money as binary floating point.",
        "review_question": "Are persisted monetary values integer minor units?"
      },
      "platform_feasibility": [
        {
          "platform": "generic",
          "feasibility": "advisory_only",
          "mechanism": "Retain as a domain rule and review data contracts.",
          "evidence": "The rule does not depend on a platform event."
        }
      ]
    }
  ],
  "contradictions": [],
  "ambiguities": [],
  "coverage": {
    "sources_total": 1,
    "sources_processed": 1,
    "sources_skipped": 0,
    "sources_unreadable": 0,
    "sources_incomplete": 0,
    "instructions_total": 1,
    "dispositions": {
      "RULE": 1,
      "CONTROL": 0,
      "ELIMINATE": 0,
      "HUMAN_DECISION": 0
    }
  },
  "attestation": {
    "modified_sources": false,
    "installed_controls": false,
    "executed_tests": false,
    "accessed_secrets": false,
    "published": false,
    "deployed": false,
    "sent_messages": false,
    "statement": "No audited source, control, hook, configuration, or permission was modified."
  }
}
```

## Validation command

From the skill directory:

```bash
python3 scripts/validate_audit.py /absolute/path/to/audit.json
```

Exit codes: `0` valid, `1` contract violation, `2` usage/read/JSON error. Structural validity does not prove semantic correctness or control installation.
