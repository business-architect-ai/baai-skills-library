---
name: savebook
compatibility: codex-and-claude-code
---

# /savebook — Salvează o carte sau resursă

Salvează o carte, articol sau resursă pentru referință viitoare.

## Utilizare

`/savebook $ARGUMENTS`

## Ce face

1. Primește titlul cărții/articolului sau URL-ul
2. Caută informații despre resursă (autor, an, categorie)
3. Adaugă la fișierul `~/Documents/reading-list.md`
   - Dacă fișierul nu există, îl creează
   - Dacă userul specifică un alt path, folosește-l pe acela
4. Format intrare:

```markdown
## [Titlu] — [Autor]
**Adăugat:** [data]
**Categorie:** [AI / Business / Personal / Marketing / etc]
**De ce:** [1-2 rânduri despre ce aștepți de la ea]
**Status:** [ ] De citit
```

5. Confirmă că s-a salvat

## REGULI
- Dacă nu știi autorul, întreabă
- Categoriile existente: AI, Business, Personal Development, Marketing, Psihologie, Educație
- Nu adăuga duplicate — verifică dacă există deja
