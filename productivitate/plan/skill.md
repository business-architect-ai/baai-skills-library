---
name: plan
compatibility: codex-and-claude-code
---

# /plan - Planifică un feature nou

Când userul vrea să adauge un feature, ghidează-l prin aceste întrebări ÎNAINTE de a scrie cod.

## Întrebări obligatorii

Pune aceste întrebări pe rând și așteaptă răspuns:

### 1. Cine sunt utilizatorii?
"Cine va folosi acest feature? (ex: guest, user logat, admin, pro subscriber)"

### 2. Ce poate face fiecare?
"Ce acțiuni poate face fiecare tip de user cu acest feature?"

### 3. Care e flow-ul principal?
"Descrie pas cu pas ce face userul și ce vede:"
- Pasul 1: User face X
- Pasul 2: Sistemul face Y
- Pasul 3: User vede Z

### 4. Ce poate merge prost?
"Ce se întâmplă dacă:"
- Userul nu e logat?
- Plata eșuează?
- Datele sunt invalide?
- Conexiunea se pierde?

### 5. Cum se leagă de restul?
"Acest feature depinde de sau afectează alte părți ale aplicației?"

## După ce ai răspunsurile

Creează un mini-spec și cere confirmare:

```
FEATURE: [nume]

USERI ȘI PERMISIUNI:
- [tip 1]: poate [acțiuni]
- [tip 2]: poate [acțiuni]

FLOW PRINCIPAL:
1. ...
2. ...
3. ...

EDGE CASES:
- Dacă X → Y
- Dacă A → B

DEPENDENȚE:
- Folosește [sistem existent]
- Modifică [fișier/tabel]

---
E corect? Pot să încep implementarea?
```

## IMPORTANT

NU scrie cod până userul nu confirmă spec-ul!
