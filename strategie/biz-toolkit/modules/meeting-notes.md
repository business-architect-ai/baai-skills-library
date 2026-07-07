# Note post-ședință, transformă notele brute de ședință în acțiuni clare, cu responsabili și termene

Transformă notele brute de meeting în acțiuni clare cu responsabili și deadlines.

## Memorie
Înainte de prima întrebare, aplică learning engine-ul (vezi `references/learning-engine.md`) cu fișierul `~/.claude/skill-memory/biz-meeting-notes.md`: citește gotchas și preferințele salvate și aplică-le. La finalul interacțiunii, actualizează memoria.

## Proces

### Pas 1: Input

Întreabă: "Dă-mi notele de la întâlnire (lipește textul, sau descrie ce s-a discutat)"

### Pas 2: Procesare

```
MINUTE ÎNTÂLNIRE
Data: [data]  |  Cu: [cine]  |  Subiect: [ce]

DECIZII LUATE:
- [decizie 1]
- [decizie 2]

ACȚIUNI:
| # | Ce | Cine | Până când | Status |
|---|---|---|---|---|
| 1 | [acțiune concretă] | [responsabil] | [deadline] | [ ] |
| 2 | [acțiune] | [responsabil] | [deadline] | [ ] |

ÎNTREBĂRI DESCHISE (nerezolvate):
- [întrebare], cine trebuie să răspundă

NEXT STEPS:
- Următoarea întâlnire: [când, dacă s-a stabilit]
- Ce trebuie pregătit: [ce]

FOLLOW-UP EMAIL (draft):
---
Subiect: Acțiuni din întâlnirea [subiect] - [data]

Salut,

Rezumat rapid din întâlnirea de azi:

Decizii:
- [decizie 1]
- [decizie 2]

Acțiuni:
- [Cine]: [ce] până la [când]
- [Cine]: [ce] până la [când]

Spuneți dacă am omis ceva.

[Nume]
---
```

## Reguli
- Fiecare acțiune trebuie să aibă CINE și PÂNĂ CÂND. Dacă lipsește, întreabă.
- Nu inventa ce nu s-a spus. Dacă notele sunt incomplete, pune întrebări.
- Draft-ul de email trebuie să fie trimis direct, nu "adaptat".
