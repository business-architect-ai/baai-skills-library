# Skill Radar

Radar pentru skilluri care merita evaluate, adaptate sau importate in BAAI Skills Library.

Regula de lucru: nu importam bulk. Alegem 5-10 skilluri pe runda, verificam licenta, citim continutul, adaptam la limba/standardul BAAI si setam corect `compatibility`.

## Surse Active

| Sursa | URL | Licenta | Potrivire BAAI | Observatii |
|---|---|---:|---:|---|
| Codex Plugin Marketplace | https://www.codex-marketplace.com/skills | variaza | High | Prima sursa pentru skilluri Codex-native. Verificam repo-ul sursa inainte de import. |
| PM Skills | https://github.com/phuryn/pm-skills | MIT | High | Mina buna pentru product, GTM, discovery, PRD, roadmap, market research. |
| GTM Agents | https://github.com/gtmagents/gtm-agents | Apache-2.0 | High | Mina buna pentru sales, marketing, RevOps, email, launch, copywriting. |
| Trail of Bits Skills | https://github.com/trailofbits/skills | CC-BY-SA-4.0 | Medium/High | Foarte bun pentru security/dev audit, dar licenta necesita atentie si atribuire/share-alike. |
| Netresearch Marketplace | https://github.com/netresearch/claude-code-marketplace | MIT | Medium | Bun pentru standard portabil multi-agent si skill tooling. |
| Anthropic Skills | https://github.com/anthropics/skills | variaza | Medium | Bun pentru structura si bune practici, mai putin pentru continut BAAI direct. |

## Candidati Runda 1

### Product / Strategie

| Candidat | Sursa | Categorie BAAI | Compatibilitate probabila | Recomandare |
|---|---|---|---|---|
| create-prd | phuryn/pm-skills | productivitate sau strategie | codex-and-claude-code | Import/adaptare. Template PRD in 8 sectiuni, util pentru fondatori si product work. |
| gtm-strategy | phuryn/pm-skills | marketing sau strategie | codex-and-claude-code | Import/adaptare. Complement bun pentru `biz-campaign` si `biz-offer`. |
| competitive-battlecard | phuryn/pm-skills | strategie | codex-and-claude-code | Evaluare. Poate completa `biz-competitor` cu output orientat pe vanzari. |
| opportunity-solution-tree | phuryn/pm-skills | strategie/productivitate | codex-and-claude-code | Evaluare. Bun pentru discovery si decizii de produs. |
| pre-mortem | phuryn/pm-skills | operatiuni/strategie | codex-and-claude-code | Evaluare. Bun pentru risc inainte de lansare/campanie/proiect. |

### Marketing / GTM / Revenue

| Candidat | Sursa | Categorie BAAI | Compatibilitate probabila | Recomandare |
|---|---|---|---|---|
| message-architecture | gtmagents/gtm-agents | marketing | codex-and-claude-code | Import/adaptare. Bun pentru ierarhie mesaj, hook bank, CTA matrix. |
| deliverability-ops | gtmagents/gtm-agents | marketing | codex-and-claude-code | Import/adaptare. Foarte util pentru email marketing operational. |
| launch-plays | gtmagents/gtm-agents | marketing | codex-and-claude-code | Evaluare. Poate completa `biz-campaign` cu playbook de lansare. |
| positioning | gtmagents/gtm-agents | marketing/strategie | codex-and-claude-code | Evaluare. Poate completa `biz-offer` si `biz-copy`. |
| account-health-framework | gtmagents/gtm-agents | operatiuni/strategie | codex-and-claude-code | Evaluare. Bun pentru customer success si account management. |

### Dev / Security / Quality

| Candidat | Sursa | Categorie BAAI | Compatibilitate probabila | Recomandare |
|---|---|---|---|---|
| ask-questions-if-underspecified | trailofbits/skills | productivitate/dev | codex-and-claude-code | Adaptare cu atribuire. Foarte bun ca meta-skill de clarificare. |
| modern-python | trailofbits/skills | dev | claude-code-only sau codex-and-claude-code dupa verificare | Evaluare. Depinde de comenzi/tooling. |
| insecure-defaults | trailofbits/skills | tehnic | claude-code-only sau codex-and-claude-code dupa verificare | Evaluare. Bun pentru audit config/securitate. |
| supply-chain-risk-auditor | trailofbits/skills | tehnic | claude-code-only | Evaluare. Probabil depinde de tooluri si verificari tehnice. |
| semgrep-rule-creator | trailofbits/skills | tehnic/dev | claude-code-only | Evaluare. Bun, dar tool-heavy. |

### Codex-Native

| Candidat | Sursa | Categorie BAAI | Compatibilitate probabila | Recomandare |
|---|---|---|---|---|
| project-skill-audit | Dimillian/Skills via Codex Marketplace | productivitate/dev | codex-only sau codex-and-claude-code | Evaluare. Foarte potrivit pentru auditarea bibliotecii noastre. |
| review-swarm | Dimillian/Skills via Codex Marketplace | tehnic | codex-only | Evaluare. Multi-agent review; probabil Codex-specific. |
| review-and-simplify-changes | Dimillian/Skills via Codex Marketplace | tehnic | codex-and-claude-code dupa adaptare | Evaluare. Bun pentru review schimbari locale. |
| planner | am-will/codex-skills via Codex Marketplace | productivitate | codex-and-claude-code dupa adaptare | Evaluare. Poate concura cu `/plan`, deci trebuie diferentiere. |
| frontend-responsive-ui | am-will/codex-skills via Codex Marketplace | design/dev | codex-and-claude-code | Evaluare. Bun companion pentru site-audit-agent si design-review. |

## Reguli De Import

1. Verifica licenta inainte de copiere/adaptare.
2. Nu copia skilluri cu instructiuni riscante, exfiltrare, bypass de siguranta sau comenzi destructive automate.
3. Nu importa skilluri care dubleaza unul existent fara diferentiere clara.
4. Pentru skilluri text-only, seteaza `compatibility: codex-and-claude-code`.
5. Pentru skilluri cu Playwright MCP, Chrome MCP, slash commands Claude, hooks, bash workflows sau `~/.claude/skill-memory`, seteaza `compatibility: claude-code-only`.
6. Pentru skilluri Codex plugin/marketplace reale, seteaza `codex-only` doar daca depind explicit de structura Codex.
7. Adauga sursa si licenta in frontmatter:

```yaml
source: https://github.com/org/repo
license: MIT
```

8. Fiecare import trebuie sa aiba `README.md` si `skill.md`.

## Backlog Runda 1

- [ ] Evaluare completa `create-prd`.
- [ ] Evaluare completa `gtm-strategy`.
- [ ] Evaluare completa `message-architecture`.
- [ ] Evaluare completa `deliverability-ops`.
- [ ] Evaluare completa `ask-questions-if-underspecified` cu atentie la CC-BY-SA.
- [ ] Decide daca `project-skill-audit` merita portat sau folosit direct ca inspiratie Codex-native.

## Note

Repo-uri clonate temporar pentru inspectie locala:

```text
/private/tmp/skill-radar/pm-skills
/private/tmp/skill-radar/gtm-agents
/private/tmp/skill-radar/netresearch-marketplace
/private/tmp/skill-radar/trailofbits-skills
```

Aceste clone nu fac parte din BAAI Skills Library.

