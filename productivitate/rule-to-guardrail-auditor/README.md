# Rule-to-Guardrail Auditor

Skill consultativ, compatibil cu Codex și Claude Code, care transformă un set aglomerat de instrucțiuni într-un audit acționabil.

## Când îl folosești

- agentul repetă aceeași greșeală;
- `AGENTS.md` sau `CLAUDE.md` a devenit lung ori contradictoriu;
- vrei să crești autonomia agentului fără să pierzi controlul;
- schimbi modelul și vrei să verifici dacă regulile vechi mai sunt utile;
- auditezi o soluție AI construită pentru un client.

## Ce produce

Fiecare instrucțiune primește o singură recomandare:

- `RULE` — rămâne regulă deoarece cere judecată;
- `CONTROL` — poate deveni verificare deterministă;
- `ELIMINATE` — este vagă, duplicată, depășită sau neacționabilă;
- `HUMAN_DECISION` — trebuie să rămână sub aprobarea omului.

Pentru controale, raportul definește triggerul, condiția, comportamentul la succes/eșec, testul pozitiv, testul negativ și fezabilitatea separată pe platforme.

## Ce nu face

V1 nu modifică regulile analizate, nu instalează hooks, nu execută comenzile de test furnizate, nu citește secrete și nu publică sau face deploy. Recomandă și validează structura raportului.

## Instalare din biblioteca BAAI

După clonarea repo-ului, copiază întregul folder.

### Codex

```bash
mkdir -p ~/.codex/skills/rule-to-guardrail-auditor
cp productivitate/rule-to-guardrail-auditor/skill.md ~/.codex/skills/rule-to-guardrail-auditor/SKILL.md
cp -R productivitate/rule-to-guardrail-auditor/references ~/.codex/skills/rule-to-guardrail-auditor/
cp -R productivitate/rule-to-guardrail-auditor/scripts ~/.codex/skills/rule-to-guardrail-auditor/
cp -R productivitate/rule-to-guardrail-auditor/examples ~/.codex/skills/rule-to-guardrail-auditor/
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/rule-to-guardrail-auditor
cp productivitate/rule-to-guardrail-auditor/skill.md ~/.claude/skills/rule-to-guardrail-auditor/SKILL.md
cp -R productivitate/rule-to-guardrail-auditor/references ~/.claude/skills/rule-to-guardrail-auditor/
cp -R productivitate/rule-to-guardrail-auditor/scripts ~/.claude/skills/rule-to-guardrail-auditor/
cp -R productivitate/rule-to-guardrail-auditor/examples ~/.claude/skills/rule-to-guardrail-auditor/
```

Repornește sesiunea agentului după instalare. Biblioteca păstrează convenția `skill.md`; la instalare, runtime-urile primesc numele standard `SKILL.md`.

## Utilizare

Într-o sesiune deschisă în proiectul auditat:

```text
Folosește Rule-to-Guardrail Auditor. Auditează AGENTS.md și CLAUDE.md.
Agentul uită să ruleze testele și încearcă uneori să citească .env.
Comanda de verificare este npm test. Platformele sunt Codex și Claude.
Nu modifica nimic. Returnează raportul în conversație.
```

Pentru artifacte reutilizabile:

```text
Salvează auditul ca Markdown și JSON și validează pachetul JSON.
Nu modifica și nu instala nimic.
```

## Validare manuală

Din folderul skillului:

```bash
python3 scripts/validate_audit.py /cale/absolută/audit.json
```

Exit `0` confirmă structura și coerența internă. Nu confirmă că recomandările sunt semantic perfecte sau că vreun control este instalat.

## Flux recomandat

```text
Audit → selecție umană → generare separată → testare → instalare aprobată
```

Pentru pilot, folosește-l pe un proiect real și notează: ce clasificări au fost utile, ce a fost neclar și ce control ai ales efectiv să implementezi.
