---
name: xlsx
compatibility: codex-and-claude-code
---

# /xlsx — Analizează sau procesează fișiere Excel/CSV

Lucrează cu fișiere de date structurate.

## Utilizare

`/xlsx $ARGUMENTS`

## Ce face

1. Citește fișierul specificat (Excel .xlsx sau CSV)
2. Afișează un rezumat:
   - Număr de rânduri și coloane
   - Numele coloanelor
   - Primele 5 rânduri (preview)
   - Statistici de bază pentru coloane numerice
   - Lista sheet-urilor (dacă e Excel cu mai multe sheet-uri)

3. Întreabă ce vrei să faci:
   - Analiză/raport
   - Filtrare
   - Calcule noi
   - Export în alt format

## REGULI
- Folosește Python cu openpyxl sau pandas
- Nu modifica fișierul original fără confirmare
- Salvează rezultatele în fișiere noi cu sufixul `_procesat`
- Dacă fișierul e mare (>10.000 rânduri), anunță înainte de a procesa
