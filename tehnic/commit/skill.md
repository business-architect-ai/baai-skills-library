# /commit - Salvează modificările local

Fă commit la modificările curente (salvare locală în git).

## Pași:

1. Rulează `git status` pentru a vedea ce fișiere sunt modificate
2. Arată userul lista de fișiere modificate
3. Întreabă userul ce fișiere vrea să includă în commit (sau toate)
4. Cere userul un mesaj de commit (sau propune unul bazat pe modificări)
5. Execută:
   - `git add <fișierele selectate>`
   - `git commit -m "<mesaj>"`
6. Confirmă că commit-ul a fost făcut

## Reguli:
- Commit message în engleză
- Adaugă `Co-Authored-By: Claude <noreply@anthropic.com>` la final
- NU face push automat - userul trebuie să folosească `/push` separat
- Dacă nu sunt modificări, spune "Nu sunt modificări de salvat"

## Format commit message:
```
<tip>: <descriere scurtă>

Co-Authored-By: Claude <noreply@anthropic.com>
```

Tipuri: feat, fix, chore, refactor, docs, style, test
