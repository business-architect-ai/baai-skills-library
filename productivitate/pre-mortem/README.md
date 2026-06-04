# /pre-mortem - Analiza riscurilor inainte de lansare

Ruleaza o analiza pre-mortem pentru produs, feature, lansare, campanie sau proiect: imagineaza esecul, identifica riscuri reale, paper tigers si elephants, apoi produce actiuni de mitigare.

## Cand il folosesti

- Ai PRD, launch plan, campanie sau feature aproape gata.
- Vrei sa stii ce poate merge prost.
- Echipa este prea optimista sau evita riscuri incomode.
- Vrei decizie: lansam, amanam, fazam sau mitigam.

## Ce produce

- Failure story
- Tigers / Paper Tigers / Elephants
- Launch-blocking action plan
- Fast-follow plan
- Tracking plan
- Launch decision

## Compatibilitate

```yaml
compatibility: codex-and-claude-code
```

## Instalare Claude Code

```bash
cp productivitate/pre-mortem/skill.md ~/.claude/commands/pre-mortem.md
```

## Instalare Codex

```bash
mkdir -p ~/.codex/skills/pre-mortem
cp productivitate/pre-mortem/skill.md ~/.codex/skills/pre-mortem/SKILL.md
```

## Sursa

Adaptat din [phuryn/pm-skills](https://github.com/phuryn/pm-skills) - MIT License.
