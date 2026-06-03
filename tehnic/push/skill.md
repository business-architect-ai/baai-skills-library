# /push - Trimite modificările pe GitHub

Trimite commit-urile locale pe GitHub (remote).

## Pași:

1. Rulează `git status` pentru a verifica:
   - Dacă există commit-uri locale care nu sunt pe remote
   - Dacă branch-ul curent are remote configurat
2. Dacă sunt modificări uncommitted, avertizează userul și întreabă dacă vrea să facă `/commit` întâi
3. Dacă totul e OK, execută `git push origin <branch>`
4. Confirmă că push-ul a fost făcut cu succes
5. Afișează link-ul către repo pe GitHub

## Reguli:
- NU face push fără confirmare explicită
- Dacă nu există remote, ajută userul să configureze unul
- Dacă branch-ul nu există pe remote, folosește `git push -u origin <branch>`

## Output la succes:
```
Push reușit pe GitHub!
Branch: main
Repo: https://github.com/<user>/<repo>
```
