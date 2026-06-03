# /code-review — Code review pull request GitHub

Face review unui pull request de pe GitHub: verifică dacă e deschis și relevant, identifică fișierele modificate, lansează agenți paraleli pentru bugs, probleme de logică și conformitate cu regulile proiectului, validează fiecare problemă găsită și produce un raport cu issues de înaltă certitudine.

## Când îl folosești

- Ai un PR pe GitHub și vrei un review automat
- Vrei să prinzi bugs sau probleme înainte de merge
- Lucrezi cu cod generat de AI și vrei o verificare independentă

## Cerințe

- GitHub CLI (`gh`) instalat și autentificat
- Acces la repo-ul cu PR-ul

## Instalare

```bash
cp skill.md ~/.claude/commands/code-review.md
```

Activare în Claude Code: `/code-review` (cu `--comment` pentru a posta comentarii inline pe PR)
