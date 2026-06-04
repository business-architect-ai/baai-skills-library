# Skill Quality Audit - Runda 6

Data: 2026-06-04

Scope:
- `productivitate/research-users`
- `productivitate/opportunity-solution-tree`
- `productivitate/pre-mortem`

## Verdict

Accept.

Cele trei skilluri completeaza zona de product discovery si product readiness: `research-users` sintetizeaza datele despre utilizatori, `opportunity-solution-tree` transforma insighturile in oportunitati/solutii/experimente, iar `pre-mortem` testeaza riscurile unui plan ales.

## Scor

| Skill | Claritate trigger | Structura | Compatibilitate | Output util | Siguranta | Diferentiere | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| `research-users` | 5 | 5 | 5 | 5 | 5 | 5 | Accept |
| `opportunity-solution-tree` | 5 | 5 | 5 | 5 | 5 | 5 | Accept |
| `pre-mortem` | 5 | 5 | 5 | 5 | 5 | 5 | Accept |

## Compatibility Check

Valoare actuala pentru toate cele trei skilluri: `codex-and-claude-code`

Valoare recomandata: `codex-and-claude-code`

Motiv:
- Sunt workflow-uri text-only.
- Nu folosesc `~/.claude/skill-memory/`.
- Nu folosesc MCP-uri, bash hooks, sub-agenti Claude sau structuri Codex-only.
- Nu au subfoldere `tools/`, `references/` sau `prompts/`.

## Suprapuneri

### `research-users` vs `biz-customer`, `message-architecture`

Recomandare: pastreaza separat.

`research-users` sintetizeaza date si produce personas/segmente/journey cu confidence levels. `biz-customer` este avatar client business/marketing, iar `message-architecture` transforma insighturile in sistem de mesaj.

### `opportunity-solution-tree` vs `plan`, `create-prd`

Recomandare: pastreaza separat.

`opportunity-solution-tree` este pentru discovery inainte de solutie. `plan` si `create-prd` sunt pentru specificarea unui feature/produs deja ales.

### `pre-mortem` vs `create-prd`, `plan`

Recomandare: pastreaza separat.

`pre-mortem` este stress-test pe un plan/PRD/lansare deja conturat. Nu scrie planul, ci identifica ce il poate deraia.

## Riscuri controlate

| Skill | Risc | Control introdus |
|---|---|---|
| `research-users` | Personas decorative sau concluzii inventate din date slabe. | Reguli explicite: confidence level, diferentiere evidence vs interpretare, ipoteze cand datele sunt subtiri. |
| `opportunity-solution-tree` | Transformarea feature-urilor in oportunitati false. | Reguli explicite: oportunitatile trebuie formulate ca nevoi/dureri client, nu solutii. |
| `pre-mortem` | Transformarea fiecarei griji in launch blocker. | Reguli explicite: Tigers/Paper Tigers/Elephants si clasificare launch-blocking/fast-follow/track. |

## Decizia recomandata

Skillurile pot fi publicate. Urmatorul pas recomandat este runda 7: standardizarea unor skilluri BAAI vechi in variante Codex-compatible, incepand cu skillurile text-only blocate de `~/.claude/skill-memory/`.
