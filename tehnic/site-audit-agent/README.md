# /site-audit-agent — Audit complet de site

Ruleaza un pipeline de audit pentru un site live sau local: SEO, accessibility, performance, security, links, design tokens, UX, visual polish si prompt de remediere pentru Claude Code.

## Compatibilitate

Acest skill este diferit fata de majoritatea skillurilor din biblioteca:

- **Codex**: compatibil ca plugin skill in `~/.codex/skills/site-audit-agent/SKILL.md`.
- **Claude Code**: compatibil ca plugin skill in `~/.claude/skills/site-audit-agent/SKILL.md`.
- Nu este un simplu command skill, pentru ca include tooluri, referinte si prompturi.

## Cand il folosesti

- Vrei audit serios pentru un site inainte de lansare.
- Vrei sa verifici SEO, accessibility, performance si security headers.
- Vrei sa dai autorului site-ului un raport remediabil in Claude Code.
- Vrei sa compari scorul inainte/dupa dupa deploy.
- Vrei o analiza mai serioasa decat un simplu design review vizual.

## Instalare pentru Codex

```bash
mkdir -p ~/.codex/skills/site-audit-agent
cp skill.md ~/.codex/skills/site-audit-agent/SKILL.md
cp -R tools ~/.codex/skills/site-audit-agent/
cp -R references ~/.codex/skills/site-audit-agent/
cp -R prompts ~/.codex/skills/site-audit-agent/
```

Restart Codex dupa instalare.

## Instalare pentru Claude Code

```bash
mkdir -p ~/.claude/skills/site-audit-agent
cp skill.md ~/.claude/skills/site-audit-agent/SKILL.md
cp -R tools ~/.claude/skills/site-audit-agent/
cp -R references ~/.claude/skills/site-audit-agent/
cp -R prompts ~/.claude/skills/site-audit-agent/
```

## Tooluri externe necesare

Squirrelscan:

```bash
curl -fsSL https://squirrelscan.com/install | bash
squirrel self doctor
```

Dembrandt:

```bash
npm i -g dembrandt
```

Ollama pentru Synthux local:

```bash
brew install --cask ollama
ollama pull llama3.1
launchctl setenv OLLAMA_ORIGINS "*"
```

Synthux: instaleaza extensia Chrome de la `https://synthux.app/` si alege `Provider: Ollama`, `Model: llama3.1`.

## Rulare

```bash
cd tools/audit-site-agent
npm run audit -- https://example.com --name example
```

Rezultatele apar in:

```text
tools/audit-site-agent/runs/
```

Folderul `runs/` este ignorat si nu trebuie urcat in repo.

## Output

Skillul produce:

- raport Squirrelscan
- extractie Dembrandt
- checklist Synthux
- prompt design-review
- prompt frontend-design-audit
- prompt Rams PR review
- prompt de consolidare
- raport final cu prioritati P0/P1/P2

## Sursa

Creat pentru Business Architect AI. Include un runner local construit pentru workflow Codex/Claude Code si referinte UX adaptate din `frontend-design-audit`.

