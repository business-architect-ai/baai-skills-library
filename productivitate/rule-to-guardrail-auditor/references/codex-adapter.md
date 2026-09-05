# Codex adapter

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

Then inspect current local Codex documentation or authoritative current OpenAI documentation when platform-specific feasibility is requested. Distinguish:

- natural-language project instructions;
- reusable skills;
- product sandbox and approval boundaries;
- project-owned scripts or linters;
- CI or repository checks;
- currently documented native lifecycle mechanisms, if verified.

## Feasibility labels

- `native` only when the current Codex environment documents the required event and behavior;
- `scripted` when a deterministic project or CI script can check it;
- `advisory_only` when no reliable enforcement point exists;
- `unverified` when current evidence was not inspected.

Record the evidence used. Do not infer a native hook from a similar feature in another runtime.

## Authority boundary

Codex sandboxing or an approval prompt can support a boundary, but it does not create user authorization. Deployment, publication, destructive change, secret access, and other external effects remain `HUMAN_DECISION` unless separately authorized.

## V1 output

Describe the proposed mapping and its verification test. Do not write or install configuration, change sandbox settings, alter `AGENTS.md`, execute project tests, or claim activation.
