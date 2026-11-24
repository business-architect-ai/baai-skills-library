# lean-powers: disciplina de verificare, fără procesul impus

Modelele care scriu cod au un obicei scump: spun „gata” fără să fi verificat. lean-powers păstrează din [superpowers](https://github.com/obra/superpowers) doar partea care corectează asta și renunță la procesul impus (brainstorming, planificare, execuție de planuri), pe care Claude Code îl are oricum nativ, prin plan mode, subagenți și workflow-uri.

## Ce reguli aduce

| Regula | Pe scurt |
|---|---|
| Verificare | nicio afirmație de succes fără o verificare rulată după ultima modificare |
| Depanare | nicio reparație înainte să poți arăta cauza; după trei reparații eșuate, te oprești |
| Testul întâi | testul scris și văzut picând, apoi codul |
| Review | observațiile de review se verifică pe cod înainte să fie implementate |

## Două variante

**1. Pluginul complet, pentru Claude Code (recomandat).** Pe lângă cele patru reguli, are o **poartă de verificare**: un hook care nu lasă tura să se încheie dacă s-a modificat cod și nu s-a rulat nicio verificare (teste, build, type-check, linter) după ultima modificare. O regulă scrisă poate fi ocolită, poarta nu.

Ai nevoie de Node.js (`node --version`; dacă lipsește, varianta LTS de pe [nodejs.org](https://nodejs.org)). Apoi, în Claude Code, pe rând:

```
/plugin marketplace add danutmitrut/lean-powers
```

```
/plugin install lean-powers@lean-powers
```

Repornești Claude Code. Codul, detaliile despre poartă și limitele cunoscute sunt în repo: [github.com/danutmitrut/lean-powers](https://github.com/danutmitrut/lean-powers).

**2. Skill-ul din acest folder, pentru Codex sau fără plugin.** Aceleași patru reguli, într-un singur fișier, fără poarta automată. Modelul le aplică singur, deci disciplina depinde de el.

Codex:

```bash
mkdir -p ~/.codex/skills/lean-powers
cp dev/lean-powers/skill.md ~/.codex/skills/lean-powers/SKILL.md
```

Claude Code, fără plugin:

```bash
mkdir -p ~/.claude/skills/lean-powers
cp dev/lean-powers/skill.md ~/.claude/skills/lean-powers/SKILL.md
```

Nu le instala pe amândouă în Claude Code: pluginul conține deja regulile.

## Când e util

- lucrezi cu un agent care scrie cod și vrei să nu mai primești „am terminat” fără dovadă;
- vrei disciplina din superpowers, dar fără ca fiecare sarcină mică să treacă prin brainstorming și plan;
- predai sau înveți lucrul cu agenți și vrei un standard simplu de „gata înseamnă verificat”.

Dacă folosești superpowers, dezactivează-l înainte, ca să nu lucreze amândouă în aceeași sesiune.

## Testat

Pe Opus 5.5, într-un banc A/B cu 27 de rulări: aceeași calitate ca superpowers, la costul variantei fără plugin (la una dintre sarcini, superpowers a fost de 2,8 ori mai lent și cu 47% mai scump). Sarcinile au fost ușoare pentru Opus, deci testul a măsurat mai ales costul, nu calitatea. Pe Sonnet și Haiku n-a fost încă măsurat.

## Licență

MIT. Regulile derivă din superpowers, Copyright (c) 2025 Jesse Vincent.
