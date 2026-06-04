---
name: "site-audit-agent"
description: "Ruleaza un audit serios pentru un site live sau local folosind un pipeline cu Squirrelscan, Dembrandt, Synthux/Ollama, design-review si frontend-design-audit. Produce artefacte tehnice, checklisturi, prompturi de remediere pentru Claude Code si un raport consolidat cu prioritati P0/P1/P2. Foloseste cand utilizatorul cere audit site, audit SEO/UX/accessibility/performance/security, analiza unui URL, verificare inainte de lansare sau comparatie dupa remedieri."
compatibility: codex-and-claude-code
agent_targets:
  - codex
  - claude-code
license: MIT
source: business-architect-ai/baai-skills-library
---

# Site Audit Agent

Foloseste acest skill pentru audituri serioase de site-uri, nu pentru o parere rapida. Pipeline-ul combina audit tehnic, design-system extraction, UX/accessibility review si prompt de remediere pentru autorul site-ului.

## Diferenta Codex vs Claude Code

- **Codex**: foloseste acest skill ca workflow agentic. Poate rula toolul local `tools/audit-site-agent`, poate citi artefactele, poate produce raportul consolidat si poate re-audita dupa deploy.
- **Claude Code**: foloseste acest skill ca plugin skill sau primeste promptul din `prompts/claude-code-remediation-prompt.md` impreuna cu raportul final pentru a remedia codul site-ului.

Nu presupune ca toate toolurile sunt disponibile. Verifica local si marcheaza ce lipseste.

## Tooluri

Pipeline-ul preferat:

1. **Squirrelscan** pentru SEO, accessibility, performance, security, links, crawlability.
2. **Dembrandt** pentru design tokens, typography, spacing, radii, buttons, inputs, links.
3. **Synthux + Ollama** pentru audit UX/accessibility in browser, manual.
4. **design-review** pentru polish vizual: layout, spacing, typography, hierarchy, responsive.
5. **frontend-design-audit** pentru audit UX si fixuri in cod, cand repo-ul site-ului este disponibil.
6. **Rams** optional pentru PR review automat pe GitHub.

## Instalare Tooluri Locale

Squirrelscan:

```bash
curl -fsSL https://squirrelscan.com/install | bash
squirrel self doctor
```

Dembrandt:

```bash
npm i -g dembrandt
```

Ollama pentru Synthux local:

```bash
brew install --cask ollama
ollama pull llama3.1
launchctl setenv OLLAMA_ORIGINS "*"
```

Synthux se instaleaza ca extensie Chrome de la `https://synthux.app/`, apoi se seteaza:

```text
Provider: Ollama
Model: llama3.1
```

## Rulare Audit

Din folderul acestui skill:

```bash
cd tools/audit-site-agent
npm run audit -- https://example.com --name example
```

Runnerul produce un folder:

```text
tools/audit-site-agent/runs/<timestamp>-<slug>/
```

Artefacte tipice:

- `01-squirrelscan.txt`
- `02-dembrandt.txt`
- `03-synthux-manual.md`
- `04-design-review-prompt.md`
- `05-frontend-design-audit-prompt.md`
- `06-rams-pr-review.md`
- `99-consolidation-prompt.md`
- `SUMMARY.md`

## Workflow De Audit

1. Ruleaza agentul local pe URL.
2. Citeste `01-squirrelscan.txt` si identifica scorul, erorile si warningurile.
3. Citeste `02-dembrandt.txt` si extrage design-system findings.
4. Cere utilizatorului rezultatele Synthux daca vrea audit UX in browser; acestea se pun ca `03-synthux-results.md`.
5. Daca exista repo-ul site-ului, foloseste `frontend-design-audit` pentru fixuri P0/P1.
6. Daca autorul lucreaza in Claude Code, da-i raportul final si promptul din `prompts/claude-code-remediation-prompt.md`.
7. Dupa deploy, re-ruleaza auditul si compara inainte/dupa.

## Raport Consolidat

Produce un raport cu:

- executive summary
- scoruri tooluri
- top 10 probleme
- SEO
- accessibility/WCAG
- performance/Core Web Vitals
- security headers/forms
- UX/conversion
- visual/design polish
- design-system consistency
- quick wins sub 1 ora
- backlog 1-2 saptamani
- verificare dupa remedieri

Prioritizeaza:

- **P0**: blocheaza utilizatorii, indexing, legal/compliance sau siguranta.
- **P1**: impact mare pe conversie, accesibilitate, incredere sau performanta.
- **P2**: imbunatatiri importante dar fara blocaj imediat.
- **P3**: polish.

## Checks UX/Frontend

Cand faci audit de UX sau ai codul site-ului, citeste doar daca este necesar:

- `references/frontend-design-heuristics.md`
- `references/frontend-design-patterns.md`

Verifica explicit:

- form labels si accessible names
- focus states si keyboard navigation
- aria-hidden cu elemente focusabile
- modals/dropdowns/tabs/accordions
- loading, empty, error si success states
- CTA clarity si hierarchy
- mobile tap targets si responsive layout
- contrast si text-muted prea slab

## Reguli

- Nu urca folderul `runs/` in git; poate contine date de client.
- Nu inventa rezultate daca un tool nu a rulat.
- Cand scorul este slab, spune direct ce categorie il trage in jos.
- Pentru URL live, raportul este report-only daca nu ai repo-ul site-ului.
- Pentru repo local, implementeaza intai P0/P1 si verifica dupa fiecare grup de fixuri.

