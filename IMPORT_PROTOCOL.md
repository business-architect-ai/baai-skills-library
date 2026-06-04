# Import Protocol - BAAI Skills Library

Acest document descrie procesul oficial pentru adaugarea skillurilor noi in BAAI Skills Library.

Pipeline-ul standard este:

```text
radar -> evaluare -> import/adaptare -> skill-quality-audit -> commit -> pull --rebase -> push
```

Se aplica atat pentru Claude Code, cat si pentru Codex.

## 1. Radar

Scop: identificam candidati buni fara sa importam bulk.

Surse recomandate:

| Sursa | Licente tipice | Cand merita cautata |
|---|---|---|
| PM Skills | MIT | Product, PRD, discovery, roadmap, GTM |
| GTM Agents | Apache-2.0 | Marketing, sales, RevOps, email, enablement |
| Codex Marketplace | variaza | Skilluri Codex-native si structuri moderne |
| Anthropic Skills | variaza | Bune practici de structura si exemple oficiale |
| Trail of Bits Skills | CC-BY-SA-4.0 | Security/dev audit, doar cu atentie la licenta |
| Netresearch Marketplace | MIT | Structura multi-agent si marketplace tooling |

Reguli:
- Nu importa mai mult de 2-5 skilluri pe runda.
- Nu importa doar pentru ca exista. Candidatul trebuie sa completeze o nevoie clara in librarie.
- Noteaza candidatii in `SKILL_RADAR.md` sau intr-un raport de evaluare dedicat.

## 2. Evaluare

Inainte de import, verifica:

| Criteriu | Intrebare |
|---|---|
| Potrivire BAAI | Este util pentru fondatori, marketing, operatiuni, produs, dev sau design? |
| Diferentiere | Completeaza un skill existent sau il dubleaza? |
| Licenta | Este MIT, Apache-2.0, BSD sau alta licenta permisiva? |
| Risc | Poate produce recomandari periculoase, spam, exfiltrare, comenzi destructive sau claims false? |
| Portabilitate | Este text-only sau depinde de platforma/tooluri? |
| Mentenabilitate | Poate fi inteles si folosit fara repo-ul original? |

Pentru fiecare runda, creeaza sau actualizeaza un raport:

```text
SKILL_RADAR_ROUND_[N]_EVALUATION.md
```

Raportul trebuie sa spuna clar:
- candidati evaluati
- decizie: import / adaptare / amanare / respingere
- motiv
- categorie propusa
- compatibilitate probabila
- licenta

## 3. Import / Adaptare

Fiecare skill nou trebuie sa aiba structura:

```text
[categorie]/[nume-skill]/
├── skill.md
└── README.md
```

Pentru skilluri complexe, se pot adauga:

```text
tools/
references/
prompts/
```

Dar doar daca sunt necesare si explicate.

### Frontmatter obligatoriu

```yaml
---
name: "nume-skill"
description: "Descriere clara, orientata pe trigger: cand si de ce se foloseste skillul."
compatibility: codex-and-claude-code
license: MIT
source: https://github.com/org/repo (MIT License)
---
```

### Reguli de adaptare

- Rescrie skillul in stilul BAAI, nu copia mecanic.
- Pastreaza sursa si licenta.
- Elimina referinte personale, cai hardcodate sau dependente inutile.
- Adauga sectiune `Diferenta fata de skilluri apropiate` cand exista risc de suprapunere.
- Adauga reguli de siguranta pentru domenii cu risc: legal, security, finance, email/cold outreach, competitiv.
- Outputul trebuie sa fie concret: tabele, checklisturi, planuri, decizii, next actions.

## 4. Compatibility

Default:

```yaml
compatibility: codex-and-claude-code
```

Foloseste `claude-code-only` doar daca skillul depinde explicit de:
- `~/.claude/skill-memory/`
- slash commands Claude ca dependenta reala
- Playwright/Chrome MCP specific Claude Code
- sub-agenti Claude
- bash/git hooks integrate in Claude Code

Foloseste `codex-only` doar daca skillul depinde explicit de:
- structuri Codex-only
- tooluri Codex-only
- comportamente care nu exista in Claude Code

Un titlu de forma `/nume-skill` nu este motiv pentru `claude-code-only`; este doar conventia de invocare in Claude Code.

## 5. README principal

Dupa import, actualizeaza `README.md`:

- adauga skillul in categoria corecta
- foloseste link relativ catre folder
- pastreaza descrierea scurta si clara
- marcheaza cu `★` doar skillurile de tip plugin/skill folder pentru Claude Code, nu orice skill compatibil Codex

## 6. Skill Quality Audit

Dupa import si inainte de push, ruleaza auditul pe skillurile noi.

Foloseste `tehnic/skill-quality-audit/skill.md` ca protocol.

Auditul trebuie sa verifice:
- verdict: accept / accept cu modificari / respinge temporar
- scor pe criterii
- compatibility check
- suprapuneri cu skilluri existente
- riscuri si controale introduse
- decizia recomandata

Nu comite rapoarte de audit pe runde in repo by default. Pastreaza raportul doar daca Dan cere explicit arhivarea lui sau daca auditul contine o decizie de governance care trebuie pastrata. Daca auditul gaseste probleme mici, aplica fixurile in acelasi commit.

## 7. Git Protocol

Ambii agenti lucreaza pe `main`. Respecta secventa:

```bash
git pull
# editare/adaptare
git add .
git commit -m "feat: add [nume] skill"
git pull --rebase
git push origin main
```

Reguli:
- Nu forta push.
- Nu rescrie munca altui agent fara acordul lui Dan.
- Daca apar modificari staged de la alt agent, trateaza-le ca draft si cere clarificare daca afecteaza acelasi fisier.
- Daca remote-ul s-a schimbat, foloseste `git pull --rebase`.

## 8. Criterii De Respingere

Respinge sau amana skillul daca:

- licenta nu permite adaptare/distributie clara
- este prea dependent de platforma si nu vrem acel tip de skill
- dubleaza un skill existent fara diferentiere
- cere date private fara motiv
- incurajeaza spam, bypass, exfiltrare, scraping abuziv sau comenzi destructive
- produce claims legale/financiare/medicale fara disclaimere si verificari
- este prea vag pentru a produce output actionabil

## 9. Ordinea Recomandata Pentru Runde Viitoare

1. Sales enablement complementar: call prep, objection handling, sales playbook.
2. Product discovery: opportunity solution tree, pre-mortem, market research.
3. Versiuni Codex-compatible pentru skillurile BAAI vechi care sunt blocate de `~/.claude/skill-memory/`.
4. Dev/security doar dupa verificare stricta de tooluri si licenta.

## 10. Checklist Rapid

Inainte de push, confirma:

- [ ] `git pull` facut la inceput
- [ ] licenta verificata
- [ ] `skill.md` are frontmatter complet
- [ ] `README.md` exista
- [ ] `compatibility` este justificat
- [ ] README principal actualizat
- [ ] audit de calitate rulat; raport comis doar daca este necesar
- [ ] nu exista suprapunere neexplicata
- [ ] `git pull --rebase` inainte de push
- [ ] repo curat dupa push
