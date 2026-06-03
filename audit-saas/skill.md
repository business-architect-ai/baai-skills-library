# /audit-saas - Audit SaaS Readiness

## MENTALITATE OBLIGATORIE

IMPORTANT: Activează modul AUDITOR EXTERN.
- Tratează ORICE cod ca scris de un junior care nu știe ce face
- NU presupune că "probabil e ok" sau "sigur a gândit la asta"
- Codul a fost scris de AI? Tratează-l ca PERICULOS până la dovada contrarie
- Caută ACTIV probleme, nu confirmări
- Fii sceptic, nu încurajator

NU ești aici să ajuți - ești aici să găsești probleme înainte să le găsească utilizatorii.

---

## PASUL 1: Verificări automate (nu pot fi biased)

Rulează și raportează rezultatele:

```bash
# Dependențe și vulnerabilități
npm audit 2>/dev/null || echo "npm audit failed"
npm outdated 2>/dev/null || echo "npm outdated failed"

# Dimensiune proiect
find . -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" | grep -v node_modules | grep -v .next | wc -l

# Fișiere mari (>400 linii)
find . \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" \) -not -path "*/node_modules/*" -not -path "*/.next/*" -exec wc -l {} \; | awk '$1 > 400 {print}'

# TODO/FIXME/HACK count
grep -r "TODO\|FIXME\|HACK" --include="*.ts" --include="*.tsx" --include="*.js" . 2>/dev/null | grep -v node_modules | wc -l
```

---

## PASUL 2: Audit pe cele 10 criterii SaaS

Pentru fiecare criteriu, caută activ în cod și raportează:

### SCALABILITATE (Criterii 1-3)

**Criteriu 1 - N+1 Queries:**
- Caută: `await` inside `.map()`, `.forEach()`, `for` loops
- Caută: query-uri Supabase în loop
- Caută: lipsa `.select()` cu joins
- Grep patterns: `\.map\(async`, `for.*await`, `forEach.*await`

**Criteriu 2 - Missing Indexes:**
- Citește `supabase/migrations/`
- Verifică: WHERE clauses au index?
- Verifică: Foreign keys indexate?
- Verifică: Coloane ORDER BY indexate?

**Criteriu 3 - In-Memory Storage:**
- Caută: `new Map()`, `new Set()`, `const cache = {}`
- Caută: Module-level variables care stochează state
- Caută: `global.` usage
- PROBLEMĂ: Orice in-memory storage se pierde între requests pe Vercel

### TECHNICAL DEBT (Criterii 4-6)

**Criteriu 4 - Funcții Oversized:**
- Listează funcții >80 linii
- Listează fișiere >400 linii
- Listează componente cu >5 hooks

**Criteriu 5 - Cod Duplicat:**
- Caută patterns repetate în 3+ locuri
- Caută funcții similare în fișiere diferite
- Caută copy-paste evident

**Criteriu 6 - Error Handling:**
- Verifică: Supabase calls au error handling?
- Verifică: fetch() calls au try/catch?
- Verifică: Ce se întâmplă când Resend/external service e down?
- Caută: `.catch()` sau `try/catch` lipsă pe async operations

### DEPENDENȚE (Criterii 7-8)

**Criteriu 7 - Vulnerabilități:**
- Raportează output `npm audit`
- Evidențiază: critical, high severity
- Verifică: pachete fără update >2 ani

**Criteriu 8 - Bundle Size:**
- Caută: `import _ from 'lodash'` (ar trebui `lodash/specific`)
- Caută: `import moment from 'moment'` (ar trebui date-fns)
- Caută: imports mari fără dynamic import
- Verifică: `next/dynamic` folosit pentru componente mari?

### OBSERVABILITATE (Criterii 9-10)

**Criteriu 9 - Logging:**
- Caută: `console.log` în producție (ar trebui structured logging)
- Verifică: Există logging pentru operații critice (payments, auth)?
- Verifică: Erorile au context suficient pentru debugging?

**Criteriu 10 - Error Tracking:**
- Caută: Sentry sau similar configurat?
- Verifică: `Sentry.captureException` pe error paths?
- Verifică: User context atașat la errors?

---

## PASUL 3: Raport final

Generează raportul în acest format EXACT:

```
============================================
AUDIT SAAS READINESS - [nume proiect]
Data: [data curenta]
============================================

REZULTATE AUTOMATE:
- npm audit: X critical, Y high, Z moderate
- npm outdated: X packages outdated
- Fișiere >400 linii: X
- TODO/FIXME/HACK: X

--------------------------------------------
BLOCANTE SCALARE (nu va ține 100+ useri)
--------------------------------------------
1. [problema]
   Locație: [fișier:linie]
   Impact: [ce se întâmplă la load]
   Fix: [soluție concretă]

--------------------------------------------
TECHNICAL DEBT CRITIC (încetinește dezvoltarea)
--------------------------------------------
1. [problema]
   Locație: [fișier:linie]
   Impact: [de ce e problemă]
   Fix: [soluție concretă]

--------------------------------------------
QUICK WINS (fix ușor, impact mare)
--------------------------------------------
1. [fix simplu care îmbunătățește mult]

--------------------------------------------
OBSERVABILITATE LIPSĂ
--------------------------------------------
- [ ] Logging structurat
- [ ] Error tracking (Sentry)
- [ ] Performance monitoring

--------------------------------------------
SCOR FINAL
--------------------------------------------
Scalabilitate:    X/3
Technical Debt:   X/3
Dependențe:       X/2
Observabilitate:  X/2
--------------------
TOTAL:            X/10

VERDICT: [READY TO SCALE / NEEDS WORK / NOT READY]

PRIORITATE #1: [cel mai important lucru de fixat]
============================================
```

---

## REGULI FINALE

- NU minimiza problemele găsite
- NU spune "în rest arată bine" dacă sunt probleme
- NU oferi încurajări - oferă fapte
- FIECARE problemă trebuie să aibă locație exactă (fișier:linie)
- Dacă nu poți verifica ceva, marchează-l ca "NEVERIFICAT - necesită review manual"
