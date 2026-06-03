# BAAI Skills

Librărie de skilluri pentru Claude Code, construită pentru membrii comunității BAAI.

Fiecare skill e un fișier `.md` pe care îl copiezi în folderul `.claude/commands/` și devine disponibil instant ca comandă în Claude Code.

## Instalare rapidă

```bash
# Un singur skill
cp biz-copy/skill.md ~/.claude/commands/biz-copy.md

# Toate skillurile deodată
for d in */; do cp "$d/skill.md" ~/.claude/commands/"${d%/}.md"; done
```

## Catalog

### Business — strategie

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-review](biz-review/) | `/biz-review` | Diagnostic complet de business pe 6 dimensiuni |
| [biz-decision](biz-decision/) | `/biz-decision` | Framework structurat pentru decizii grele |
| [biz-competitor](biz-competitor/) | `/biz-competitor` | Analiză competitivă cu hartă și recomandări |
| [biz-pricing](biz-pricing/) | `/biz-pricing` | Review strategie de preț, benchmarking, recomandare |
| [biz-pitch](biz-pitch/) | `/biz-pitch` | Review și rescriere pitch sau prezentare |

### Business — marketing

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-campaign](biz-campaign/) | `/biz-campaign` | Planificare campanie cu KPIs și plan de contingență |
| [biz-copy](biz-copy/) | `/biz-copy` | Copywriting pe vocea brandului pentru orice canal |
| [biz-customer](biz-customer/) | `/biz-customer` | Construiește avatar client detaliat din date reale |
| [biz-funnel](biz-funnel/) | `/biz-funnel` | Diagnostic funnel, identifică scurgeri și fix-uri |
| [biz-offer](biz-offer/) | `/biz-offer` | Construiește sau revizuiește oferta comercială |

### Business — operațiuni

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-ops](biz-ops/) | `/biz-ops` | Audit procese, identifică bottleneck-uri și automatizări |
| [biz-meeting-prep](biz-meeting-prep/) | `/biz-meeting-prep` | Pregătire întâlnire cu agendă și worst case |
| [biz-meeting-notes](biz-meeting-notes/) | `/biz-meeting-notes` | Transformă note brute în acțiuni cu responsabili și deadlines |
| [biz-weekly](biz-weekly/) | `/biz-weekly` | Retrospectivă săptămânală cu wins, blocaje și priorități |
| [biz-day](biz-day/) | `/biz-day` | Ritual de dimineață: priorități, KPIs, follow-ups |

### Productivitate

| Skill | Comandă | Ce face |
|---|---|---|
| [thinkmap](thinkmap/) | `/thinkmap` | Cartografiază stilul de gândire pe 14 dimensiuni cognitive |
| [xlsx](xlsx/) | `/xlsx` | Analizează și procesează fișiere Excel sau CSV |
| [plan](plan/) | `/plan` | Planifică un feature nou înainte de a scrie cod |
| [ortografie-ro](ortografie-ro/) | `/ortografie-ro` | Corectează capitalizarea în texte românești |
| [savebook](savebook/) | `/savebook` | Salvează o carte sau resursă în lista de lectură |
| [imagine](imagine/) | `/imagine` | Generează o imagine dintr-un prompt |

### Tehnic

| Skill | Comandă | Ce face |
|---|---|---|
| [audit-saas](audit-saas/) | `/audit-saas` | Audit readiness SaaS pe 10 criterii: scalabilitate, debt, securitate |
| [commit](commit/) | `/commit` | Salvează modificările curent în git cu mesaj structurat |
| [push](push/) | `/push` | Trimite commit-urile locale pe GitHub |
| [review-pr](review-pr/) | `/review-pr` | Review complet PR cu agenți specializați în paralel |
| [code-review](code-review/) | `/code-review` | Code review pentru un pull request pe GitHub |
| [security-check](security-check/) | `/security-check` | Audit rapid de securitate: secrets expuse, vulnerabilități npm |

## Cum funcționează skillurile

Un skill e un fișier Markdown pe care Claude Code îl citește ca instrucțiuni atunci când scrii `/nume-skill`. Fișierul definește ce rol ia Claude, ce întrebări pune și ce format produce.

Cele mai multe skilluri includ un **Learning Engine** care salvează preferințele tale în `~/.claude/skill-memory/`. La a doua rulare, skillul știe deja contextul tău și nu mai întreabă de la zero.
