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
cp strategie/battlecard-system/skill.md ~/.claude/commands/battlecard-system.md

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
| [biz-toolkit](strategie/biz-toolkit/) ★ | `/biz-toolkit` | Pachet complet: 15 module de consultanță (diagnostic, preț, ofertă, copy, avatar, competitori, funnel, campanie, decizie, procese, pitch, ședințe, retrospectivă, ritual) cu learning engine și context de afacere comun. Reunește comenzile individuale biz-* |
| [biz-review-portable](strategie/biz-review-portable/) | `/biz-review-portable` | Diagnostic business portabil pentru Codex + Claude Code, fără skill-memory |
| [battlecard-system](strategie/battlecard-system/) | `/battlecard-system` | Battlecard competitiv pentru sales: diferențiatori, talk track, obiecții și win/loss signals |
| [call-brief-framework](strategie/call-brief-framework/) | `/call-brief-framework` | Call brief pentru sales: obiectiv, stakeholderi, agenda, mesaje, întrebări și follow-up |
| [objection-handling](strategie/objection-handling/) | `/objection-handling` | Răspunsuri la obiecții de vânzări cu LACE, proof mapping și adaptare pe canal |
| [sales-playbook](strategie/sales-playbook/) | `/sales-playbook` | Playbook de vânzări cu ICP, proces, talk tracks, asseturi, rollout, coaching și KPI-uri |

## Marketing

| Skill | Comandă | Ce face |
|---|---|---|
| [biz-campaign-portable](marketing/biz-campaign-portable/) | `/biz-campaign-portable` | Plan campanie portabil pentru Codex + Claude Code, fără skill-memory |
| [biz-copy-portable](marketing/biz-copy-portable/) | `/biz-copy-portable` | Copywriting portabil pe canal și audiență, fără skill-memory |
| [biz-customer-portable](marketing/biz-customer-portable/) | `/biz-customer-portable` | Avatar client portabil cu limbaj, trigger, obiecții și canale |
| [gtm-strategy](marketing/gtm-strategy/) | `/gtm-strategy` | Strategie go-to-market cu ICP, poziționare, canale, KPI-uri și roadmap 30/60/90 |
| [message-architecture](marketing/message-architecture/) | `/message-architecture` | Arhitectură de mesaj cu public, promisiune, proof points, hook bank și CTA matrix |
| [deliverability-ops](marketing/deliverability-ops/) | `/deliverability-ops` | Diagnostic email deliverability: reputație, SPF/DKIM/DMARC, list health, warmup și compliance |
| [email-sequence](marketing/email-sequence/) ★ | `/email-sequence` | Secvențe de email: welcome, nurture, re-engagement, sales |
| [cold-email](marketing/cold-email/) ★ | `/cold-email` | Cold outreach B2B cu secvențe de follow-up și deliverability |
| [content-strategy](marketing/content-strategy/) ★ | `/content-strategy` | Strategie de conținut pe piloni, topic clusters, calendar |
| [social-content](marketing/social-content/) ★ | `/social-content` | Conținut social media pe orice platformă cu sistem de repurposing |
| [x-twitter-growth](marketing/x-twitter-growth/) ★ | `/x-twitter-growth` | Creștere X/Twitter: algoritm 2026, thread-uri, strategie reply |
| [email-marketing-bible](marketing/email-marketing-bible/) ★ | `/email-marketing-bible` | Referință completă email marketing: 908 surse, 19 industrii |

## Productivitate

| Skill | Comandă | Ce face |
|---|---|---|
| [thinkmap](productivitate/thinkmap/) | `/thinkmap` | Cartografiază stilul de gândire pe 14 dimensiuni cognitive |
| [xlsx](productivitate/xlsx/) | `/xlsx` | Analizează și procesează fișiere Excel sau CSV |
| [plan](productivitate/plan/) | `/plan` | Planifică un feature nou înainte de a scrie cod |
| [create-prd](productivitate/create-prd/) | `/create-prd` | Creează PRD complet pentru produs, feature sau inițiativă |
| [research-users](productivitate/research-users/) | `/research-users` | Sintetizează research în personas, segmente comportamentale, journey map și recomandări |
| [opportunity-solution-tree](productivitate/opportunity-solution-tree/) | `/opportunity-solution-tree` | Product discovery tree: outcome, oportunități, soluții și experimente |
| [pre-mortem](productivitate/pre-mortem/) | `/pre-mortem` | Analiză de risc înainte de lansare: Tigers, Paper Tigers, Elephants și mitigări |
| [ortografie-ro](productivitate/ortografie-ro/) | `/ortografie-ro` | Corectează capitalizarea în texte românești |
| [savebook](productivitate/savebook/) | `/savebook` | Salvează o carte sau resursă în lista de lectură |
| [book-end](productivitate/book-end/) | `/book-end` | Încheie o sesiune de lectură: idei, citate, acțiuni |
| [imagine](productivitate/imagine/) | `/imagine` | Generează o imagine dintr-un prompt |
| [opinion](productivitate/opinion/) ★ | `/opinion` | A doua părere pe o decizie grea, de la două familii de modele diferite, plus sinteza contradicțiilor |
| [deliberation](productivitate/deliberation/) ★ | `/deliberation` | Recomandări, review și sinteză bazate pe dovezi, cu mod single-model sau multimodel, context din fișiere și validare deterministă |

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
| [skill-quality-audit](tehnic/skill-quality-audit/) | `/skill-quality-audit` | Audit de calitate pentru skilluri: compatibilitate, structură, trigger rules, riscuri și suprapuneri |
| [m2c1](tehnic/m2c1/) ★ | `/m2c1` | Orchestrare autonomă în 12 faze, de la idee dezordonată la aplicație construită, testată și publicată. Cere Playwright MCP |

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
| [imagini-web-lp](dev/imagini-web-lp/) ★ | `/imagini-web-lp` | Reguli imagini și video pentru landing pages: AVIF/WebP, lazy loading, Hero/LCP, video autoplay și audit HTML |
| [web-section-composer](dev/web-section-composer/) ★ | `/web-section-composer` | Compune și auditează secțiuni web după job, ierarhie vizuală, densitate, responsive și eficiență de spațiu |

## Design

| Skill | Comandă | Ce face |
|---|---|---|
| [huashu-design](design/huashu-design/) | `/huashu-design` | Prototipuri și slide-uri HTML hi-fi, animații, design exploration |
| [design-review](design/design-review/) ★ | `/design-review` | Review vizual: layout, tipografie, culori, consistență, responsive |
| [ux-audit](design/ux-audit/) ★ | `/ux-audit` | Audit UX complet cu interacțiune reală, axe-core, performanță, verdict |
| [baai-design-toolkit](design/baai-design-toolkit/) | `/baai-design-toolkit` | Alegi și folosești unelte de design cu AI (shadcn/ui, 21st.dev, Open Design), cu router de decizie și comenzi de instalare |

## Writing

| Skill | Comandă | Ce face |
|---|---|---|
| [ro-humanizer](writing/ro-humanizer/) | `/ro-humanizer` | Elimină artefactele AI din text românesc în 4 etape |
| [humanizer](writing/humanizer/) | `/humanizer` | Elimină artefactele AI din text englezesc (30 de pattern-uri) |
| [arhitect-pagini-vanzare](writing/arhitect-pagini-vanzare/) | `/arhitect-pagini-vanzare` | Diagnostichează tipul de pagină de vânzare și construiește copy secțiune cu secțiune |
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

Unele skilluri Claude Code vechi includ un **Learning Engine** care salvează preferințele tale în `~/.claude/skill-memory/`. Variantele marcate `portable` nu folosesc această memorie și sunt compatibile Codex + Claude Code.

---

*Skillurile marcate cu sursă externă sunt importate/adaptate din repo-uri cu licențe permisive, indicate în frontmatter și în README-ul fiecărui skill.*
