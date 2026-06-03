# /security-check — Audit rapid de securitate

Verificare rapidă de securitate pe proiectul curent.

## Ce face

### 1. Verificări automate
- `npm audit` (dacă e proiect npm)
- Caută fișiere `.env` expuse
- Caută fișiere `.key`, `.pem` neprotejate
- Caută hardcoded secrets (`password`, `secret`, `api_key`) în cod

### 2. Verifică .gitignore
- `.env` e în .gitignore?
- `*.key`, `*.pem` sunt excluse?
- Foldere cu secrets sunt excluse?

### 3. Raport

```
🔒 SECURITY CHECK — [proiect]

VULNERABILITĂȚI NPM: [X critical, Y high]
FIȘIERE .ENV EXPUSE: [da/nu]
SECRETS ÎN COD: [fișierele găsite sau "Nimic găsit"]
.GITIGNORE: [OK / Probleme: ...]

ACȚIUNI NECESARE:
- [ ] [dacă există ceva de fixat]
```

## REGULI
- Nu afișa conținutul fișierelor cu secrets
- Dacă e totul OK, spune clar: "Proiect curat, nicio problemă găsită"
