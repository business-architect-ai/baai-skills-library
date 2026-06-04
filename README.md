# BAAI Skills Library

Colecție de skilluri pentru agenți AI — Claude Code, Codex și alte platforme compatibile. Construită de și pentru membrii comunității Business Architect AI.

Skilluri gata de instalat pentru strategie, marketing, operațiuni, dev, design și writing. Fiecare skill e un fișier `.md` pe care agentul îl citește ca instrucțiuni și îl urmează imediat.

Există două tipuri de skilluri pentru Claude Code:
- **Command skills** (cele mai multe): se copiază în `~/.claude/commands/`
- **Plugin skills** (marcate cu ★): se copiază în `~/.claude/skills/[nume]/SKILL.md`

Unele skilluri noi sunt marcate cu compatibilitate explicită:
- `compatibility: claude-code-only` — rulează doar în Claude Code
- `compatibility: codex-and-claude-code` — pot fi instalate și în Codex, și în Claude Code

## Instalare rapidă

### Claude Code

```bash
# Command skill (un singur skill, exemplu)
cp strategie/biz-review/skill.md ~/.claude/commands/biz-review.md

# Plugin skill (exemplu)
mkdir -p ~/.claude/skills/linkedin-post-writer
cp writing/linkedin-post-writer/skill.md ~/.claude/skills/linkedin-post-writer/SKILL.md

# Plugin skill compatibil Codex (exemplu)
mkdir -p ~/.codex/skills/site-audit-agent
cp tehnic/site-audit-agent/skill.md ~/.codex/skills/site-audit-agent/SKILL.md
cp -R tehnic/site-audit-agent/tools ~/.codex/skills/site-audit-agent/
cp -R tehnic/site-audit-agent/references ~/.codex/skills/site-audit-agent/
cp -R tehnic/site-audit-agent/prompts ~/.codex/skills/site-audit-agent/

# Toate command skillurile dintr-o categorie
for d in strategie/*/; do cp "$d/skill.md" ~/.claude/commands/"$(basename $d).md"; done

# Toate command skillurile
for d in */*/; do [ -f "$d/skill.md" ] && cp "$d/skill.md" ~/.claude/commands/"$(basename $d).md"; done
```

### Codex

```bash
# Un singur skill (exemplu)
mkdir -p ~/.codex/skills/linkedin-post-writer
cp writing/linkedin-post-writer/skill.md ~/.codex/skills/linkedin-post-writer/SKILL.md

# Toate skillurile compatibile Codex
for d in */*/; do
  [ -f "$d/skill.md" ] && mkdir -p ~/.codex/skills/"$(basename $d)" && cp "$d/skill.md" ~/.codex/skills/"$(basename $d)"/SKILL.md
done
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
| [email-sequence](marketing/email-sequence/) ★ | `/email-sequence` | Secvențe de email: welcome, nurture, re-engagement, sales |
| [cold-email](marketing/cold-email/) ★ | `/cold-email` | Cold outreach B2B cu secvențe de follow-up și deliverability |
| [content-strategy](marketing/content-strategy/) ★ | `/content-strategy` | Strategie de conținut pe piloni, topic clusters, calendar |
| [social-content](marketing/social-content/) ★ | `/social-content` | Conținut social media pe orice platformă cu sistem de repurposing |
| [x-twitter-growth](marketing/x-twitter-growth/) ★ | `/x-twitter-growth` | Creștere X/Twitter: algoritm 2026, thread-uri, strategie reply |
| [email-marketing-bible](marketing/email-marketing-bible/) ★ | `/email-marketing-bible` | Referință completă email marketing: 908 surse, 19 industrii |

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
| [book-end](productivitate/book-end/) | `/book-end` | Încheie o sesiune de lectură: idei, citate, acțiuni |
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
| [site-audit-agent](tehnic/site-audit-agent/) ★ | `/site-audit-agent` | Audit complet site: SEO, accessibility, performance, security, design tokens, prompt remediere Claude Code |

## Dev

| Skill | Comandă | Ce face |
|---|---|---|
| [tailwind](dev/tailwind/) | `/tailwind` | Stilizare cu Tailwind CSS v3/v4, responsive, teme custom |
| [animejs](dev/animejs/) | `/animejs` | Animații web cu Anime.js |
| [gsap](dev/gsap/) | `/gsap` | Animații performante cu GSAP și ScrollTrigger |
| [css-animations](dev/css-animations/) | `/css-animations` | Animații CSS cu keyframes și transitions |
| [waapi](dev/waapi/) | `/waapi` | Animații native cu Web Animations API |
| [lottie](dev/lottie/) | `/lottie` | Integrare și control animații Lottie (JSON din After Effects) |
| [three](dev/three/) | `/three` | Grafică 3D în browser cu Three.js |

## Design

| Skill | Comandă | Ce face |
|---|---|---|
| [huashu-design](design/huashu-design/) | `/huashu-design` | Prototipuri și slide-uri HTML hi-fi, animații, design exploration |
| [design-review](design/design-review/) ★ | `/design-review` | Review vizual: layout, tipografie, culori, consistență, responsive |
| [ux-audit](design/ux-audit/) ★ | `/ux-audit` | Audit UX complet cu interacțiune reală, axe-core, performanță, verdict |

## Writing

| Skill | Comandă | Ce face |
|---|---|---|
| [ro-humanizer](writing/ro-humanizer/) | `/ro-humanizer` | Elimină artefactele AI din text românesc în 4 etape |
| [humanizer](writing/humanizer/) | `/humanizer` | Elimină artefactele AI din text englezesc (30 de pattern-uri) |
| [copy-pagina-vanzare](writing/copy-pagina-vanzare/) | `/copy-pagina-vanzare` | Generează copy complet pentru pagina de vânzare prin 9 întrebări |
| [linkedin-post-writer](writing/linkedin-post-writer/) ★ | `/linkedin-post-writer` | Scrie postări LinkedIn cu cele 10 formule de hook 2026 |
| [linkedin-hook-extractor](writing/linkedin-hook-extractor/) ★ | `/linkedin-hook-extractor` | Demontează hookul oricărei postări virale și generează template |
| [linkedin-content-planner](writing/linkedin-content-planner/) ★ | `/linkedin-content-planner` | Plan de conținut LinkedIn pe 7 zile cu piloni, formule, ore |
| [linkedin-humanizer](writing/linkedin-humanizer/) ★ | `/linkedin-humanizer` | Elimină semnele AI din drafturi LinkedIn (3 tiere + modul audit) |

---

## Cum funcționează skillurile

Un skill e un fișier Markdown cu instrucțiuni pe care agentul le citește atunci când invoci comanda. Fișierul definește ce rol ia agentul, ce întrebări pune și ce format produce.

**Compatibilitate:**
- **Claude Code** — command skills (`/nume-skill`) și plugin skills (★)
- **Codex** — skillurile cu format SKILL.md funcționează direct în Codex Marketplace
- **Alte platforme** — orice agent care citește fișiere Markdown ca instrucțiuni

**Skillurile marcate cu ★** sunt de tip plugin pentru Claude Code:
```bash
mkdir -p ~/.claude/skills/[nume-skill]
cp [categorie]/[nume-skill]/skill.md ~/.claude/skills/[nume-skill]/SKILL.md
```

Cele mai multe skilluri includ un **Learning Engine** care salvează preferințele tale în `~/.claude/skill-memory/`. La a doua rulare, skillul știe deja contextul tău și nu mai întreabă de la zero.

---

*Skillurile marcate cu sursă externă sunt importate cu permisiunea autorilor (MIT License).*
