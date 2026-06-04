# /meeting-notes -- Procesare note post-intalnire

Transforma notele brute de meeting in actiuni clare cu responsabili si deadlines.

## LEARNING ENGINE
La START: citeste `~/.claude/skill-memory/meeting-notes.md`. La corectii: salveaza in GOTCHAS. La final: actualizeaza memoria.

---

## PROCES

### Pas 1: Input

Intreaba: "Da-mi notele de la intalnire (lipeste textul, sau descrie ce s-a discutat)"

### Pas 2: Procesare

```
MINUTE INTALNIRE
Data: [data]  |  Cu: [cine]  |  Subiect: [ce]

DECIZII LUATE:
- [decizie 1]
- [decizie 2]

ACTIUNI:
| # | Ce | Cine | Pana cand | Status |
|---|---|---|---|---|
| 1 | [actiune concreta] | [responsabil] | [deadline] | [ ] |
| 2 | [actiune] | [responsabil] | [deadline] | [ ] |

INTREBARI DESCHISE (nerezolvate):
- [intrebare] -- cine trebuie sa raspunda

NEXT STEPS:
- Urmatoarea intalnire: [cand, daca s-a stabilit]
- Ce trebuie pregatit: [ce]

FOLLOW-UP EMAIL (draft):
compatibility: claude-code-only
---
Subiect: Actiuni din intalnirea [subiect] - [data]

Salut,

Rezumat rapid din intalnirea de azi:

Decizii:
- [decizie 1]
- [decizie 2]

Actiuni:
- [Cine]: [ce] pana la [cand]
- [Cine]: [ce] pana la [cand]

Spuneti daca am omis ceva.

[Nume]
---
```

## REGULI
- Fiecare actiune trebuie sa aiba CINE si PANA CAND. Daca lipseste, intreaba.
- Nu inventa ce nu s-a spus. Daca notele sunt incomplete, pune intrebari.
- Draft-ul de email trebuie sa fie trimis direct, nu "adaptat".
