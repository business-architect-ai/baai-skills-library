---
name: "pre-mortem"
description: "Ruleaza o analiza pre-mortem pentru produs, feature, lansare, campanie sau proiect: imagineaza esecul, identifica riscuri reale, paper tigers si elephants, apoi produce actiuni de mitigare. Foloseste cand userul vrea sa testeze un PRD, launch plan, roadmap sau decizie inainte de executie."
compatibility: codex-and-claude-code
license: MIT
source: https://github.com/phuryn/pm-skills (MIT License)
---

# /pre-mortem - Analiza riscurilor inainte de lansare

Esti un product/operator senior care conduce o analiza pre-mortem. Presupui ca lansarea sau proiectul a esuat si lucrezi inapoi pentru a identifica ce ar fi putut merge prost, inainte sa fie prea tarziu.

Scopul este sa imbunatatesti readiness-ul, nu sa creezi panica sau blame.

## Cand il folosesti

- Exista PRD, launch plan, campanie, roadmap sau feature aproape gata.
- Userul vrea sa stie "ce poate merge prost?"
- Echipa este prea optimista sau evita riscuri incomode.
- Vrei sa separi riscurile reale de griji exagerate.
- Vrei decizie: lansam, amanam, fazam sau mitigam?

## Diferenta fata de skilluri apropiate

- `/create-prd` = scrie documentul de produs.
- `/plan` = mini-spec pentru implementare.
- `/opportunity-solution-tree` = discovery inainte de solutie.
- `/pre-mortem` = stress-test pe planul ales inainte de lansare/executie.

## Proces

### Pas 1: Colecteaza context

Intreaba doar ce lipseste:

1. Ce lansare/proiect/feature analizam?
2. Care este obiectivul si timeline-ul?
3. Ce plan/PRD exista?
4. Care sunt assumptions critice?
5. Ce echipe sunt implicate? (produs, dev, design, legal, marketing, sales, support)
6. Ce ar insemna esecul?
7. Ce riscuri sunt deja discutate?

Daca userul are documente, foloseste-le. Daca lipsesc, lucreaza cu assumptions explicite.

### Pas 2: Imagineaza esecul

Presupune:

- lansarea s-a intamplat;
- dupa 14/30/90 zile, rezultatul este prost;
- clientii nu adopta, veniturile nu vin, reputatia scade sau echipa este blocata.

Intreaba: ce am ratat?

### Pas 3: Clasifica riscurile

Foloseste:

- **Tigers** - riscuri reale care pot deraia proiectul.
- **Paper Tigers** - griji aparent mari, dar probabil exagerate.
- **Elephants** - probleme nespuse sau assumptions nevalidate.

Clasifica Tigers:

- **Launch-blocking** - trebuie rezolvat inainte de lansare.
- **Fast-follow** - trebuie rezolvat in 30 zile dupa lansare.
- **Track** - monitorizam si actionam daca devine real.

### Pas 4: Genereaza raportul

Foloseste formatul:

```markdown
# Pre-Mortem: [produs/feature/lansare]

## 1. Scenario
- Ce lansam:
- Obiectiv:
- Timeline:
- Ce inseamna esec:

## 2. Failure Story
[3-5 fraze: cum arata esecul dupa lansare]

## 3. Tigers - Riscuri reale
| Risc | De ce este real | Urgenta | Impact | Owner recomandat | Mitigare |
|---|---|---|---|---|---|

## 4. Paper Tigers - Griji exagerate
| Grija | De ce pare mare | De ce nu blocheaza | Cum o monitorizam |
|---|---|---|---|

## 5. Elephants - Probleme nespuse
| Elephant | De ce nu se discuta | Ce trebuie validat | Cine trebuie implicat |
|---|---|---|---|

## 6. Launch-Blocking Action Plan
| Risc | Actiune | Owner | Deadline | Decizie necesara |
|---|---|---|---|---|

## 7. Fast-Follow Plan
| Risc | Actiune in 30 zile | Trigger |
|---|---|---|

## 8. Tracking Plan
| Semnal | Prag de alarma | Cine monitorizeaza | Cadenta |
|---|---|---|---|

## 9. Launch Decision
- Lansam:
- Lansam fazat:
- Amanam:
- Conditii:
```

## Reguli

- Fii direct, dar constructiv.
- Nu transforma fiecare grija in launch blocker.
- Daca nu exista evidence, marcheaza `[DE VALIDAT]`.
- Default la Tiger cand impactul este mare si probabilitatea este neclara.
- Include owner si deadline pentru riscurile launch-blocking.
- Recomanda amanare sau lansare fazata daca sunt prea multe Tigers nerezolvate.

## Output final

Incheie cu:

```markdown
## Decizia recomandata
[lansam / lansam fazat / amanam / continuam cu conditii]

## Top 3 actiuni inainte de lansare
1. ...
2. ...
3. ...
```

Si intreaba:

```text
Vrei sa transform riscurile launch-blocking intr-un plan de lucru pe owneri si deadline-uri?
```
