# Skill Radar Round 1 Evaluation

Data: 2026-06-04

Scop: evaluarea primilor 6 candidati din `SKILL_RADAR.md`, fara import automat.

## Rezumat Decizie

| Candidat | Verdict | Prioritate | Motiv scurt |
|---|---|---:|---|
| `create-prd` | Import/adaptare | P1 | Umple un gol real: PRD complet. MIT, text-only, usor de adaptat. |
| `gtm-strategy` | Import/adaptare | P1 | Complement bun pentru `biz-campaign`; produce strategie GTM pe 90 zile. MIT, text-only. |
| `message-architecture` | Adaptare extinsa | P2 | Util, dar sursa e scheletica. Merita transformat in skill BAAI mai substantial. |
| `deliverability-ops` | Adaptare extinsa | P2 | Bun pentru email ops; completeaza `email-marketing-bible`, dar trebuie operationalizat. |
| `ask-questions-if-underspecified` | Nu importa acum | P3 | Workflow foarte bun, dar Trail of Bits e CC-BY-SA; mai bine inspiratie sau import separat cu atribuire/licenta atenta. |
| `project-skill-audit` | Import Codex-only / adaptare | P2 | Foarte bun pentru auditarea skillurilor, dar e Codex-specific prin `$CODEX_HOME`, sessions si memories. |

## Evaluari Detaliate

## 1. create-prd

**Sursa:** `phuryn/pm-skills`  
**Licenta:** MIT  
**Compatibilitate recomandata:** `codex-and-claude-code`  
**Categorie BAAI propusa:** `productivitate/create-prd` sau `strategie/create-prd`

### Ce face

Creeaza un Product Requirements Document cu template in 8 sectiuni:

1. Summary
2. Contacts
3. Background
4. Objective
5. Market segments
6. Value propositions
7. Solution
8. Release

### Comparatie cu BAAI existent

`productivitate/plan` este un mini-spec pentru feature inainte de cod. `create-prd` este mai strategic si mai complet, potrivit pentru documente de produs, stakeholder alignment si handoff catre dev/design.

Nu este duplicat.

### Ce trebuie adaptat

- Tradus/adaptat in romana BAAI.
- Eliminata instructiunea rigida "save as PRD-[product-name].md" sau facuta optionala.
- Adaugate intrebari initiale mai bune pentru context.
- Adaugat format final clar.
- Frontmatter:

```yaml
compatibility: codex-and-claude-code
source: https://github.com/phuryn/pm-skills
license: MIT
```

### Verdict

Import recomandat in prima runda.

## 2. gtm-strategy

**Sursa:** `phuryn/pm-skills`  
**Licenta:** MIT  
**Compatibilitate recomandata:** `codex-and-claude-code`  
**Categorie BAAI propusa:** `marketing/gtm-strategy` sau `strategie/gtm-strategy`

### Ce face

Creeaza strategie go-to-market pentru lansare:

- canale
- messaging
- KPI-uri
- timeline
- 90-day roadmap
- riscuri si mitigare

### Comparatie cu BAAI existent

`marketing/biz-campaign` planifica o campanie tactica. `gtm-strategy` este mai sus in funnel: lansare produs/piata, market selection, channel fit, message-market fit.

Nu este duplicat. Este companion bun pentru:

- `biz-campaign`
- `biz-offer`
- `biz-competitor`
- `biz-copy`

### Ce trebuie adaptat

- Sa ceara: produs, ICP, maturitatea ofertei, canal existent, constrangeri.
- Sa produca output in format BAAI: strategie, canale, mesaje, KPI, roadmap 30/60/90, riscuri.
- Sa evite planuri prea generice de tip "social + ads + SEO" fara prioritizare.

### Verdict

Import recomandat in prima runda.

## 3. message-architecture

**Sursa:** `gtmagents/gtm-agents`  
**Licenta:** Apache-2.0  
**Compatibilitate recomandata:** `codex-and-claude-code`  
**Categorie BAAI propusa:** `marketing/message-architecture`

### Ce face

Defineste arhitectura de mesaj:

- audience & insight
- promise
- proof
- hooks
- CTA matrix

### Comparatie cu BAAI existent

`biz-copy` scrie copy concret. `message-architecture` ar trebui sa fie pasul de sistem inainte de copy: casa mesajului, hook bank, CTA-uri pe funnel/persona.

Nu este duplicat, dar sursa este prea scurta ca import direct.

### Ce trebuie adaptat

- Extins in stil BAAI cu proces in 4-5 pasi.
- Output obligatoriu:
  - Message House
  - Hook Bank
  - Proof Bank
  - CTA Matrix
  - Banned Phrases
  - Channel Variants
- Eventual legat de `biz-copy`.

### Verdict

Merita, dar ca adaptare extinsa, nu copiere directa.

## 4. deliverability-ops

**Sursa:** `gtmagents/gtm-agents`  
**Licenta:** Apache-2.0  
**Compatibilitate recomandata:** `codex-and-claude-code`  
**Categorie BAAI propusa:** `marketing/deliverability-ops`

### Ce face

Diagnostic pentru inbox placement si reputatie:

- engagement
- reputation
- SPF/DKIM/DMARC/BIMI/TLS/rDNS
- bounce/spam traps/list health
- warmup
- compliance checklist

### Comparatie cu BAAI existent

`email-marketing-bible` este o referinta mare, foarte buna, dar nu este un playbook operational scurt de diagnostic. `deliverability-ops` poate fi skill activ pentru "emailurile ajung in spam".

Nu este duplicat; este operationalizarea unei zone din email bible.

### Ce trebuie adaptat

- Checklist concret pentru user non-tehnic.
- Separare intre ce poate verifica agentul si ce trebuie verificat in ESP/DNS.
- Output:
  - Diagnostic
  - Probable causes
  - Fix plan 24h / 7 zile / 30 zile
  - DNS/auth checklist
  - Segmentare temporara pentru reputatie
- Avertisment legal: compliance nu este consultanta juridica.

### Verdict

Merita, dar ca adaptare extinsa.

## 5. ask-questions-if-underspecified

**Sursa:** `trailofbits/skills`  
**Licenta:** CC-BY-SA-4.0  
**Compatibilitate recomandata:** `codex-and-claude-code`, daca este importat  
**Categorie BAAI propusa:** `productivitate/ask-questions-if-underspecified` sau integrat in CONTRIBUTING

### Ce face

Meta-skill pentru clarificarea cerintelor inainte de implementare. Are reguli bune:

- decide daca cererea e sub-specificata
- pune 1-5 intrebari must-have
- nu actioneaza pana nu are raspunsuri
- ofera defaults si optiuni compacte

### Comparatie cu BAAI existent

Nu exista un meta-skill general de clarificare. `plan` face clarificare pentru feature-uri, dar nu pentru orice task.

### Risc

Licenta CC-BY-SA-4.0 Trail of Bits. Importul/copierea poate impune obligatii share-alike si atribuire. Pentru o biblioteca MIT/mixta, trebuie decizie explicita.

### Verdict

Nu importa acum. Foloseste ca inspiratie sau importa separat cu atribuire si nota de licenta clara.

## 6. project-skill-audit

**Sursa:** `Dimillian/Skills`  
**Licenta:** MIT  
**Compatibilitate recomandata:** `codex-only` daca se pastreaza forma actuala; `codex-and-claude-code` doar daca este rescris generic  
**Categorie BAAI propusa:** `tehnic/project-skill-audit` sau `productivitate/project-skill-audit`

### Ce face

Auditeaza un proiect pentru a recomanda skilluri noi sau update-uri pe baza:

- memorie Codex
- rollout summaries
- sesiuni
- skilluri locale existente
- conventii de repo

### Comparatie cu BAAI existent

Nu exista echivalent. Este foarte potrivit pentru administrarea bibliotecii BAAI si pentru proiecte cu istoric Codex.

### Risc / Limitare

Forma actuala este Codex-specific:

- `$CODEX_HOME`
- `~/.codex/memories`
- `~/.codex/sessions`
- `agents/openai.yaml`

Nu este potrivit ca `codex-and-claude-code` fara adaptare.

### Verdict

Import recomandat ca `codex-only` sau rescriere in doua moduri:

- `codex mode`: foloseste `$CODEX_HOME`
- `manual mode`: auditeaza doar repo-ul si skillurile locale, fara memories/sessions

## Recomandare Runda 1

Importam in urmatoarea ordine:

1. `create-prd` — cel mai curat import.
2. `gtm-strategy` — valoare mare, overlap mic.
3. `message-architecture` — adaptare BAAI, nu copiere directa.
4. `deliverability-ops` — adaptare BAAI, companion pentru `email-marketing-bible`.

Amanam:

- `ask-questions-if-underspecified` pana decidem politica CC-BY-SA.
- `project-skill-audit` pana decidem daca il vrem `codex-only` sau rescris generic.

## Actiune Propusa

Urmatorul pas: import/adaptare pentru primele doua skilluri MIT:

- `productivitate/create-prd`
- `marketing/gtm-strategy`

Dupa aceea, runda separata pentru:

- `marketing/message-architecture`
- `marketing/deliverability-ops`

