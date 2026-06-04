# Audit Site Agent

Un runner local pentru audit serios de site-uri. Primește un URL, creează un folder de audit și coordonează tooluri precum Squirrelscan, Dembrandt, Synthux, `design-review`, `frontend-design-audit` și Rams.

Runnerul este intenționat fără dependențe npm. Detectează ce CLI-uri există local, rulează ce poate și produce artefacte pentru pașii manuali/agentici.

## Folosire rapidă

```bash
cd audit-site-agent
npm run audit -- https://example.com
```

Cu nume explicit:

```bash
npm run audit -- https://example.com --name example-homepage
```

Outputul apare în:

```text
runs/<timestamp>-<slug>/
```

## Ce produce

- `00-input.json`: URL, timp, configurare.
- `01-squirrelscan.*`: audit tehnic, dacă există CLI-ul.
- `02-dembrandt.*`: design-system extraction, dacă există CLI-ul.
- `03-synthux-manual.md`: checklist pentru extensia Synthux.
- `04-design-review-prompt.md`: prompt pentru skillul `jezweb/claude-skills design-review`.
- `05-frontend-design-audit-prompt.md`: prompt pentru skill/plugin `frontend-design-audit`.
- `06-rams-pr-review.md`: setup notes pentru Rams pe PR-uri.
- `99-consolidation-prompt.md`: prompt pentru raport consolidat.
- `SUMMARY.md`: indexul runului.

## Configurare comenzi

Implicit, runnerul caută comenzile de mai jos:

- `SQUIRRLSCAN_CMD` sau `squirrel audit`
- `DEMBRANDT_CMD` sau `dembrandt`

Poți suprascrie:

```bash
SQUIRRLSCAN_CMD="squirrel audit" npm run audit -- https://example.com
DEMBRANDT_CMD="npx dembrandt" npm run audit -- https://example.com
```

Important: `npx dembrandt` poate cere internet dacă pachetul nu e instalat local.

## Pipeline recomandat

1. Rulează agentul pe URL.
2. Deschide site-ul în browser și rulează Synthux pe paginile importante.
3. Pune rezultatele Synthux în folderul runului, de exemplu `03-synthux-results.md`.
4. Rulează promptul `99-consolidation-prompt.md` în Codex/Claude.
5. Dacă ai repo-ul site-ului, aplică fixurile P0/P1 cu `frontend-design-audit` și apoi verifică vizual cu `design-review`.
