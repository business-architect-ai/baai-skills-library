---
name: baai-design-toolkit
compatibility: claude-code-only
description: Use when the user does web or UI design in Claude Code and needs UI components, a design system, or wants to generate a prototype, landing page, slides or dashboard, or asks about shadcn/ui, 21st.dev or Open Design, or which AI design tool to pick. Triggers include "adauga componente UI", "de unde iau un design system", "vreau un prototip/landing/slide/dashboard", "ce unealta de design folosesc", shadcn, 21st, open design.
---

# BAAI Design Toolkit

Trei unelte de design pentru vibe coding, fiecare cu alt rol. Skill-ul te ajută să alegi corect și să dai pașii exacți, fără să confunzi cărămida cu fabrica.

## Principiul de bază

Nu sunt trei variante ale aceluiași lucru, sunt trei categorii diferite:

- **shadcn/ui** = cărămida. Componente pe care le deții în cod (React + Tailwind).
- **21st.dev** = magazinul. Catalog de componente plus generare AI, prin Magic MCP.
- **Open Design** = fabrica. Aplicație desktop care transformă agentul de cod în motor de design complet.

Peste toate, cursantul are deja **huashu-design** nativ în Claude Code. De multe ori ăla e cel mai simplu răspuns, nu adăuga o unealtă nouă dacă nu e nevoie.

## Router de decizie

| Ai nevoie de... | Folosește | De ce |
|---|---|---|
| O componentă punctuală (buton, formular, tabel, dialog) în React/Tailwind | shadcn/ui | O deții în cod, o modifici cum vrei |
| O componentă mai specială, gata stilizată, sau generare din prompt | 21st.dev (Magic MCP) | Catalog comunitar plus generare AI în variante |
| Un design system portabil între proiecte și agenți | Open Design (DESIGN.md) | Un fișier de brand care persistă între proiecte |
| Consistență de stil în cadrul unui proiect React deja pornit | token-urile shadcn | Variabile CSS în acel proiect (nu se plimbă singure între proiecte) |
| Un prototip / landing / slide / dashboard cu design system persistent sau export PPTX/PDF/MP4 | Open Design | Motor de design complet, bibliotecă de stiluri, export multi-format |
| Design hi-fi rapid, în flux, fără app separată | huashu-design (deja instalat) | Nativ în Claude Code, zero setup |

Regula scurtă: o piesă înseamnă shadcn sau 21st. Un sistem întreg sau o generare de la zero înseamnă Open Design sau huashu nativ.

**Când ezitați între huashu și Open Design** (ambele generează artefacte vizuale): începe cu huashu nativ, e deja acolo și n-are setup. Treci la Open Design doar dacă vrei un design system persistent, biblioteca lor de stiluri gata făcute, sau export în PPTX/PDF/MP4.

**Stack non-React** (HTML/CSS simplu, Vue, WordPress): shadcn și 21st sunt din lumea React/Tailwind, nu se aplică. Pentru o pagină sau un artefact întreg folosește huashu nativ sau Open Design; pentru o componentă izolată, scrii direct HTML/CSS.

## Referință rapidă

| Unealtă | Ce e | Instalare | Cost |
|---|---|---|---|
| shadcn/ui | Componente deținute în cod | `npx shadcn@latest init` | Gratis, open source |
| 21st.dev | Marketplace plus generare AI (Magic MCP) | Config MCP cu API key (one-liner pentru IDE-uri, config manual pentru Claude Code, vezi referința) | Freemium |
| Open Design | Agentul devine motor de design | Descarci de pe open-design.ai, apoi `od mcp install claude` | Gratis (plătești API-ul tău) |
| huashu-design | Skill nativ Claude Code, design hi-fi în HTML | Deja instalat, se declanșează cerând un prototip/slide/design | Gratis (parte din Claude Code) |

Pentru pașii detaliați pe fiecare, citește fișierul de referință:

- shadcn/ui: `references/shadcn.md`
- 21st.dev: `references/21st-dev.md`
- Open Design: `references/open-design.md`

## Reguli (guardrails)

- **Nu atinge config fără confirmare.** settings.json, config-ul MCP și .env se modifică doar cu acordul explicit al cursantului. Dă comenzile, oferă să le rulezi, dar întreabă înainte.
- **Cheie API înseamnă secret.** Cheile de la 21st.dev sau de la providerul de model nu se lipesc în chat și nu se comit. Le pui în config local sau în seif (Keychain pe Mac, SecretManagement pe Windows).
- **Free tiers reale.** 21st.dev: 2 instalări pe zi și 30 credite AI pe lună pe gratis, restul pe Pro. Open Design: gratis, dar plătești API-ul providerului tău. shadcn: complet gratis.
- **Nu instala o fabrică pentru o cărămidă.** Pentru un singur buton nu instalezi Open Design. Pentru un prototip întreg nu copiezi 40 de componente shadcn la mână.
- **21st e compatibil cu registry-ul shadcn.** Poți adăuga o componentă 21st și direct cu `npx shadcn@latest add "<url-21st>"`, fără să configurezi MCP.
- **Verifică versiunea.** Comenzile se schimbă. Dacă una nu merge, trimite la docs oficiale (linkurile sunt în fișierele de referință).

## Greșeli frecvente

- Le tratează ca fiind același lucru. Nu sunt: cărămidă vs magazin vs fabrică.
- Instalează Open Design ca să adauge o componentă. Overkill, folosește shadcn sau 21st.
- Scrie config MCP fără cheie sau fără confirmarea cursantului.
- Uită că huashu-design nativ acoperă deja multe cazuri de prototip sau slide, fără app în plus.
