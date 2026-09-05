# Claude adapter

Use this reference only after the platform-agnostic disposition is decided.

## Mapping protocol

For every `CONTROL`, write the generic requirement first:

```text
Event needed
Deterministic condition
Enforcement point
Allow behavior
Failure behavior
Positive and negative tests
```

Then inspect current authoritative Claude Code documentation when platform-specific feasibility is requested. Distinguish:

- natural-language instructions in `CLAUDE.md`;
- reusable skills;
- permissions and tool boundaries;
- documented hooks and their exact current events or schemas;
- project-owned scripts or linters;
- CI or repository checks.

## Feasibility labels

- `native` only when current documentation supports the required hook event and behavior;
- `scripted` when a deterministic project or CI script can check it;
- `advisory_only` when no reliable enforcement point exists;
- `unverified` when current evidence was not inspected.

Record the evidence used. Do not infer a Claude hook name or schema from memory or from Codex behavior.

## Authority boundary

Claude permissions or hook outcomes can support a boundary, but they do not create user authorization. Deployment, publication, destructive change, secret access, and other external effects remain `HUMAN_DECISION` unless separately authorized.

## V1 output

Describe the proposed mapping and its verification test. Do not write or install hooks, change permissions, alter `CLAUDE.md`, execute project tests, or claim activation.
