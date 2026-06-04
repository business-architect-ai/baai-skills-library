# Ghid de contribuție — BAAI Skills Library

Librăria este deschisă contribuțiilor din comunitatea Business Architect AI. Orice membru poate propune un skill nou, îmbunătăți unul existent sau adăuga suport pentru o platformă nouă.

---

## Structura unui skill

Fiecare skill trăiește într-un folder propriu, sub categoria potrivită:

```
[categorie]/[nume-skill]/
├── skill.md       ← instrucțiunile pe care agentul le urmează (obligatoriu)
└── README.md      ← descriere, use cases, instrucțiuni de instalare (obligatoriu)
```

Skillurile mai complexe (în special cele Codex) pot include subfoldere:

```
[categorie]/[nume-skill]/
├── skill.md
├── README.md
├── tools/         ← unelte sau scripturi apelate de skill
├── references/    ← fișiere de referință (reguli, exemple, date)
└── prompts/       ← prompturi auxiliare sau sub-skilluri
```

---

## Frontmatter obligatoriu în skill.md

Orice `skill.md` trebuie să înceapă cu un bloc YAML frontmatter:

```yaml
---
name: "nume-skill"
compatibility: codex-and-claude-code
description: "Descriere scurtă folosită de agent pentru a decide când să activeze skillul."
---
```

### Câmpul `compatibility`

| Valoare | Când se folosește |
|---|---|
| `codex-and-claude-code` | Skilluri pure text/instrucțiuni fără dependențe de platformă — **default pentru skilluri noi** |
| `claude-code-only` | Dependențe reale de Claude Code (vezi mai jos) |
| `codex-only` | Folosește structuri sau tooluri specifice Codex care nu există în Claude Code |

#### `claude-code-only` — când se aplică

Folosește această valoare **doar** dacă skillul depinde explicit de:
- Slash commands Claude Code (`/commit`, `/push`, comenzi din `~/.claude/commands/`)
- Chrome MCP sau Playwright MCP specific Claude Code
- Sub-agenți Claude sau workflow-uri multi-agent native
- Fișiere `~/.claude/skill-memory/` sau `~/.claude/skills/`
- Bash/git hooks integrate în sesiunea Claude

Exemple: `commit`, `push`, `review-pr`, `design-review`, `ux-audit`

#### `codex-and-claude-code` — default pentru text/instrucțiuni

Skillurile pure prompt/workflow funcționează în orice platformă care citește SKILL.md. Aceasta include toate skillurile de business, marketing, writing, strategie și productivitate care nu invocă unelte specifice de platformă.

Exemple: `biz-review`, `email-sequence`, `linkedin-post-writer`, `cold-email`

#### `codex-only`

Rezervat pentru skilluri care folosesc explicit structuri Codex (tools/, prompts/, references/) sau comportamente care nu există în Claude Code. Dacă skillul funcționează în ambele, folosește `codex-and-claude-code`.

#### Regulă pentru skilluri cu tooluri incluse

Dacă skillul are subfoldere `tools/`, `references/` sau `prompts/`, pune `compatibility` **doar după verificare** că workflow-ul funcționează pe platforma respectivă.

### Câmpuri opționale utile

```yaml
license: MIT
source: https://github.com/autor/repo (MIT License)   # dacă e importat/adaptat
agent_targets:                                          # pentru skilluri Codex
  - codex
  - claude-code
```

---

## Instalare per platformă

### Claude Code — command skill
```bash
cp [categorie]/[skill]/skill.md ~/.claude/commands/[skill].md
```

### Claude Code — plugin skill (★)
```bash
mkdir -p ~/.claude/skills/[skill]
cp [categorie]/[skill]/skill.md ~/.claude/skills/[skill]/SKILL.md
```

### Codex
```bash
mkdir -p ~/.codex/skills/[skill]
cp [categorie]/[skill]/skill.md ~/.codex/skills/[skill]/SKILL.md
# dacă are subfoldere:
cp -R [categorie]/[skill]/tools ~/.codex/skills/[skill]/
cp -R [categorie]/[skill]/references ~/.codex/skills/[skill]/
cp -R [categorie]/[skill]/prompts ~/.codex/skills/[skill]/
```

---

## Categorii existente

| Folder | Conținut |
|---|---|
| `strategie/` | Decizii de business, analiză competitivă, pitch |
| `marketing/` | Campanii, copywriting, email, social media |
| `operatiuni/` | Procese, întâlniri, planificare săptămânală |
| `productivitate/` | Instrumente generale, organizare, lectură |
| `tehnic/` | Audit, git, code review, securitate, site audit |
| `dev/` | Librării și framework-uri frontend |
| `design/` | Prototipuri, design review, UX audit |
| `writing/` | Copywriting, humanizare text, LinkedIn |

Dacă skillul tău nu se încadrează în nicio categorie existentă, propune una nouă în PR.

---

## Protocol de colaborare Claude + Codex

Această librărie este întreținută în paralel de Claude Code și Codex. Ambii agenți lucrează direct pe `main`. Regulile de mai jos previn conflicte și asigură că metadata rămâne consistentă.

### Reguli de bază (obligatorii pentru ambii agenți)

1. **`git pull` înainte de orice commit.** Fără excepții. Dacă există conflicte, rezolvă-le manual; nu forța push.
2. **Staging ≠ final.** Fișierele staged (dar necommise) sunt draft. Celălalt agent poate pusha între timp — dacă se întâmplă, faci `git reset HEAD .` și `git pull`, apoi reaplici modificările tale.
3. **Nu schimba `compatibility` la skilluri existente fără să citești conținutul skillului.** Regulile sunt în secțiunea de mai sus. Dacă e neclar, lasă valoarea actuală și notează în commit message că e neclar.
4. **`claude-code-only` nu este default.** Default-ul este `codex-and-claude-code` pentru orice skill text/instrucțiuni. Setezi `claude-code-only` doar când ai identificat explicit o dependență din lista din secțiunea anterioară.

### Ce poate face fiecare

| Acțiune | Claude Code | Codex |
|---|---|---|
| Adăugare skill nou | da | da |
| Modificare skill existent | da | da |
| Modificare README.md sau CONTRIBUTING.md | da | da |
| Standardizare compatibility metadata | da | da, respectând protocolul hibrid |
| Import din repo extern permisiv | da | da, cu `license:` și `source:` în frontmatter |

### Autoritate pe conflict

Dacă două versiuni ale aceluiași fișier sunt incompatibile, **Dan decide**. Niciunul dintre agenți nu suprascrie munca celuilalt fără confirmare explicită din partea lui Dan.

Referința de autoritate pentru `compatibility` este acest fișier (CONTRIBUTING.md). Nu există ierarhie între Claude și Codex, ambii aplică aceleași reguli.

### Format commit message

```
tip: descriere scurtă în română sau engleză

# exemple:
feat: adaugă skill linkedin-post-writer în writing/
fix: corectează compatibility pentru biz-* skills cu skill-memory
docs: actualizează protocolul de colaborare în CONTRIBUTING.md
```

Tipuri acceptate: `feat`, `fix`, `docs`, `refactor`, `chore`.

---

## Cum trimiți un skill nou

1. `git pull` la zi
2. Creează folderul `[categorie]/[nume-skill]/`
3. Adaugă `skill.md` cu frontmatter corect și `README.md`
4. Verifică: `compatibility` setat conform protocolului, `name` unic în librărie, README cu instrucțiuni de instalare
5. Commit și push direct pe main

### Dacă imporți dintr-un repo extern

- Verifică licența (acceptăm MIT, Apache-2.0, BSD și licențe permisive similare)
- Adaugă `license:` și `source: https://github.com/autor/repo (License)` în frontmatter
- Adaptează conținutul dacă e necesar (elimină referințe personale, căi hardcodate)

---

## Diferența dintre command skill și plugin skill

**Command skill** (Claude Code):
- Un singur fișier `.md` copiat în `~/.claude/commands/`
- Declanșat cu `/nume-skill` în Claude Code
- Potrivit pentru skilluri simple, fără dependențe de fișiere externe

**Plugin skill** (Claude Code ★ și Codex):
- Folder complet în `~/.claude/skills/[nume]/` sau `~/.codex/skills/[nume]/`
- Poate include referințe, unelte, sub-skilluri
- Potrivit pentru skilluri complexe cu mai multe fișiere de context
