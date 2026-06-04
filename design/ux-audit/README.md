# /ux-audit — Audit UX complet al unei aplicații web

Parcurge o aplicație web ca un utilizator real, cu interacțiuni dovedite. Include: walkthrough pe toate paginile, verificare accesibilitate (axe-core), performanță (LCP/CLS/INP), stress tests, și un verdict final: Pass / Conditional Pass / Fail / Incomplete.

## Când îl folosești

- QA serios înainte de lansare sau prezentare importantă
- Vrei să găsești bug-uri de usability pe care review-ul static le ratează
- Ai nevoie de un raport cu findings clare, pași de reproducere și fix-uri

## Ce verifică

- Toate paginile și fluxurile aplicației (ca utilizator real, cu interacțiune)
- Hard gates automate: erori consolă, 5xx, layout collapse, accesibilitate
- Performanță: LCP < 4s, CLS < 0.25, INP < 500ms
- Stress scenarios: 11 scenarii de utilizare reală
- Visual polish sweep și component perfection checklist

## Diferența față de design-review

`/design-review` — "arată bine?" (rapid, vizual)
`/ux-audit` — "funcționează bine pentru utilizator?" (riguros, interacțiune reală)

## Instalare

Necesită Playwright MCP activ în sesiunea Claude Code.

```bash
mkdir -p ~/.claude/skills/ux-audit
cp skill.md ~/.claude/skills/ux-audit/SKILL.md
```

## Sursă

Adaptat din [jezweb/claude-skills](https://github.com/jezweb/claude-skills) — MIT License.
