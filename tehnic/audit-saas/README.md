# /audit-saas — Audit SaaS readiness

Auditează un proiect SaaS pe 10 criterii grupate în 4 categorii: scalabilitate (N+1 queries, indexuri, in-memory storage), technical debt (funcții oversized, cod duplicat, error handling), dependențe (vulnerabilități, bundle size) și observabilitate (logging, error tracking). Produce un scor final și un verdict: READY / NEEDS WORK / NOT READY.

## Când îl folosești

- Înainte să lansezi un produs sau să-l deschizi publicului
- Vrei să știi dacă ține la 100+ utilizatori simultan
- Faci review tehnic al unui proiect construit cu AI

## Instalare

```bash
cp skill.md ~/.claude/commands/audit-saas.md
```

Activare în Claude Code: `/audit-saas` (din folderul proiectului)
