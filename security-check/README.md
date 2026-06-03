# /security-check — Audit rapid de securitate

Verifică proiectul curent pentru probleme de securitate comune: rulează `npm audit`, caută fișiere `.env` expuse, chei și certificate neprotejate, secrets hardcodate în cod și verifică `.gitignore`. Produce un raport clar cu acțiunile necesare.

## Când îl folosești

- Înainte să faci repo-ul public pe GitHub
- Înainte de un deploy în producție
- Periodic, ca verificare de rutină pe proiecte active

## Instalare

```bash
cp skill.md ~/.claude/commands/security-check.md
```

Activare în Claude Code: `/security-check` (din folderul proiectului)
