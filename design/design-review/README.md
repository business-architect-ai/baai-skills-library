# /design-review — Review vizual al unui site sau aplicație web

Analizează calitatea vizuală a unui site sau aplicație: layout, tipografie, spațiere, culori, ierarhie, consistența componentelor, responsive. Produce un raport cu findings clasificate și Top 3 fix-uri de impact maxim.

## Când îl folosești

- Înainte să prezinți un site unui client sau investitor
- Când ceva "pare off" dar nu poți pune degetul exact
- Review rapid după ce ai construit o pagină nouă
- Vrei să știi dacă arată profesionist sau "ca un developer care a coduit singur"

## Ce verifică

- Layout și spațiere (grid, aliniere, breathing room)
- Tipografie (ierarhie, dimensiuni, line-height, lungime rând)
- Culori și contrast (WCAG AA, consistență semantică)
- Ierarhie vizuală (CTA principal, squint test, grupare)
- Consistența componentelor (butoane, carduri, inputuri, iconițe)
- Interaction design (hover, focus, active states, tranziții)
- Responsive (mobile nav, touch targets, tablet layout)

## Instalare

Necesită Playwright MCP activ în sesiunea Claude Code.

```bash
mkdir -p ~/.claude/skills/design-review
cp skill.md ~/.claude/skills/design-review/SKILL.md
```

## Sursă

Adaptat din [jezweb/claude-skills](https://github.com/jezweb/claude-skills) — MIT License.
