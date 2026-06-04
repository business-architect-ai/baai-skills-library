# /skill-quality-audit - Audit de calitate pentru skilluri

Auditeaza un skill sau o librarie de skilluri pentru claritate, compatibilitate, frontmatter, structura, trigger rules, output, riscuri si suprapuneri.

## Cand il folosesti

- Vrei sa verifici un skill inainte de publicare.
- Vrei sa standardizezi o librarie de skilluri.
- Ai neclaritati despre `compatibility`.
- Vrei sa gasesti skilluri duplicate, prea vagi sau greu de instalat.

## Ce produce

- Verdict: accept / accept cu modificari / respinge temporar
- Scor pe criterii
- Probleme prioritizate
- Compatibility check
- Suprapuneri cu alte skilluri
- Fixuri recomandate
- Optional: frontmatter sau sectiuni imbunatatite

## Compatibilitate

```yaml
compatibility: codex-and-claude-code
```

## Instalare Claude Code

```bash
cp tehnic/skill-quality-audit/skill.md ~/.claude/commands/skill-quality-audit.md
```

## Instalare Codex

```bash
mkdir -p ~/.codex/skills/skill-quality-audit
cp tehnic/skill-quality-audit/skill.md ~/.codex/skills/skill-quality-audit/SKILL.md
```

## Sursa

Adaptat conceptual din [dimillian/skills](https://github.com/dimillian/skills) - MIT License.
