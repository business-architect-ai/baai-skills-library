# BAAI Skills Library

Librărie de skilluri pentru Claude Code, construită pentru membrii comunității Business Architect AI.

Fiecare skill e un fișier `.md` pe care îl copiezi în folderul `.claude/commands/` și devine disponibil instant ca comandă în Claude Code.

## Instalare rapidă

```bash
# Un singur skill (exemplu)
cp strategie/biz-review/skill.md ~/.claude/commands/biz-review.md

# O categorie întreagă
for d in strategie/*/; do cp "$d/skill.md" ~/.claude/commands/"$(basename $d).md"; done

# Toate skillurile
for d in */*/; do [ -f "$d/skill.md" ] && cp "$d/skill.md" ~/.claude/commands/"$(basename $d).md"; done
```

---

## Strategie

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-review](strategie/biz-review/) | `/biz-review` | Diagnostic complet de business pe 6 dimensiuni |
| [biz-decision](strategie/biz-decision/) | `/biz-decision` | Framework structurat pentru decizii grele |
| [biz-competitor](strategie/biz-competitor/) | `/biz-competitor` | Analiză competitivă cu hartă și recomandări |
| [biz-pricing](strategie/biz-pricing/) | `/biz-pricing` | Review strategie de preț, benchmarking, recomandare |
| [biz-pitch](strategie/biz-pitch/) | `/biz-pitch` | Review și rescriere pitch sau prezentare |

## Marketing

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-campaign](marketing/biz-campaign/) | `/biz-campaign` | Planificare campanie cu KPIs și plan de contingență |
| [biz-copy](marketing/biz-copy/) | `/biz-copy` | Copywriting pe vocea brandului pentru orice canal |
| [biz-customer](marketing/biz-customer/) | `/biz-customer` | Construiește avatar client detaliat din date reale |
| [biz-funnel](marketing/biz-funnel/) | `/biz-funnel` | Diagnostic funnel, identifică scurgeri și fix-uri |
| [biz-offer](marketing/biz-offer/) | `/biz-offer` | Construiește sau revizuiește oferta comercială |

## Operațiuni

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-ops](operatiuni/biz-ops/) | `/biz-ops` | Audit procese, identifică bottleneck-uri și automatizări |
| [biz-meeting-prep](operatiuni/biz-meeting-prep/) | `/biz-meeting-prep` | Pregătire întâlnire cu agendă și worst case |
| [biz-meeting-notes](operatiuni/biz-meeting-notes/) | `/biz-meeting-notes` | Transformă note brute în acțiuni cu responsabili și deadlines |
| [biz-weekly](operatiuni/biz-weekly/) | `/biz-weekly` | Retrospectivă săptămânală cu wins, blocaje și priorități |
| [biz-day](operatiuni/biz-day/) | `/biz-day` | Ritual de dimineață: priorități, KPIs, follow-ups |

## Productivitate

| Skill | Comandă | Ce face |
|---|---|---|
| [thinkmap](productivitate/thinkmap/) | `/thinkmap` | Cartografiază stilul de gândire pe 14 dimensiuni cognitive |
| [xlsx](productivitate/xlsx/) | `/xlsx` | Analizează și procesează fișiere Excel sau CSV |
| [plan](productivitate/plan/) | `/plan` | Planifică un feature nou înainte de a scrie cod |
| [ortografie-ro](productivitate/ortografie-ro/) | `/ortografie-ro` | Corectează capitalizarea în texte românești |
| [savebook](productivitate/savebook/) | `/savebook` | Salvează o carte sau resursă în lista de lectură |
| [imagine](productivitate/imagine/) | `/imagine` | Generează o imagine dintr-un prompt |

## Tehnic

| Skill | Comandă | Ce face |
|---|---|---|
| [audit-saas](tehnic/audit-saas/) | `/audit-saas` | Audit readiness SaaS pe 10 criterii |
| [commit](tehnic/commit/) | `/commit` | Salvează modificările curent în git cu mesaj structurat |
| [push](tehnic/push/) | `/push` | Trimite commit-urile locale pe GitHub |
| [review-pr](tehnic/review-pr/) | `/review-pr` | Review complet PR cu agenți specializați în paralel |
| [code-review](tehnic/code-review/) | `/code-review` | Code review pentru un pull request pe GitHub |
| [security-check](tehnic/security-check/) | `/security-check` | Audit rapid de securitate: secrets expuse, vulnerabilități npm |

## Dev

> Skilluri pentru dezvoltare — în curând.

## Design

> Skilluri pentru design — în curând.

## Writing

> Skilluri pentru scriere și conținut — în curând.

---

## Cum funcționează skillurile

Un skill e un fișier Markdown pe care Claude Code îl citește ca instrucțiuni atunci când scrii `/nume-skill`. Fișierul definește ce rol ia Claude, ce întrebări pune și ce format produce.

Cele mai multe skilluri includ un **Learning Engine** care salvează preferințele tale în `~/.claude/skill-memory/`. La a doua rulare, skillul știe deja contextul tău și nu mai întreabă de la zero.
