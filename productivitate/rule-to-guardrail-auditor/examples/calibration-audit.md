# Rule-to-Guardrail Audit

**Audit ID:** `r2g-20260905-calibration`
**Mode:** consultative
**Targets:** Codex, Claude

## Executive summary

Au fost analizate cinci instrucțiuni din două surse. Recomandarea este: două controale propuse, o regulă de domeniu păstrată, o formulare eliminată și o decizie menținută explicit la om. Niciun control nu este activ.

## Scope and coverage

- `S001` — `AGENTS.md` — processed.
- `S002` — `CLAUDE.md` — processed.
- 2/2 surse procesate; 5 instrucțiuni atomice; nicio sursă omisă sau inaccesibilă.
- Fișierele secrete și alte fișiere din proiect nu au făcut parte din scope.

## Instruction audit

| ID | Source | Instruction | Disposition | Confidence | Rationale |
|---|---|---|---|---|---|
| `R001` | `S001:10` | Rulează testele înainte de finalizare | `CONTROL` | high | Evenimentul de finalizare și exit code-ul sunt observabile |
| `R002` | `S002:4` | Nu citi `.env` | `CONTROL` | high | Accesul la cale poate fi blocat înainte de citirea conținutului |
| `R003` | `S001:16` | Folosește unități monetare minore întregi | `RULE` | high | Este o constrângere de domeniu aplicată contextual |
| `R004` | `S001:20` | Scrie cod curat | `ELIMINATE` | high | Nu are definiție operațională sau criteriu observabil |
| `R005` | `S002:12` | Publică după finalizare | `HUMAN_DECISION` | high | Publicarea produce un efect extern și cere autoritate |

## Recommended controls

### `R001` — poartă de testare înainte de finalizare

- Trigger: înainte ca agentul să declare sarcina finalizată.
- Condiție: comanda de test configurată iese cu status `0`.
- Enforcement point: poartă de finalizare sau script de verificare al proiectului.
- Allow: permite finalizarea după succes.
- Failure: blochează finalizarea și raportează comanda eșuată.
- Test pozitiv: exit `0` permite finalizarea.
- Test negativ: exit diferit de `0` o blochează.
- Limită: controlul acoperă numai testele incluse în comandă.
- Status: `proposed`.

### `R002` — protecția fișierelor secrete

- Trigger: înainte de citirea unei căi.
- Condiție: calea rezolvată nu aparține unei categorii interzise.
- Enforcement point: permisiune de filesystem, policy sau wrapper verificat.
- Allow: permite citirea `.env.example` când este în scope.
- Failure: blochează `.env` înainte ca textul să fie returnat.
- Test pozitiv: `.env.example` este permis.
- Test negativ: `.env` este blocat.
- Limită: numele fișierelor secrete diferă între proiecte.
- Status: `proposed`.

## Rules to retain

### `R003`

Păstrează: „Reprezintă valorile monetare în unități minore întregi.” Judecata necesară este identificarea câmpurilor monetare, valutelor și frontierelor de conversie. Întrebarea de review: toate valorile monetare persistate folosesc unități minore întregi?

## Human decisions

### `R005`

- Owner: proprietarul proiectului.
- Moment: după prezentarea dovezilor de validare și înainte de orice comandă sau API de publicare.
- Informații: țintă, vizibilitate, versiune, rezultat de validare și implicațiile revenirii.
- Interzis înainte de aprobare: publicare, deploy, release sau trimitere externă.
- Risc păstrat la om: expunerea accidentală a unui artifact neaprobat.

## Eliminations and rewrites

### `R004`

Elimină formularea vagă „Scrie cod curat”. Dacă intenția este reală, înlocuiește-o cu formatterul, linterul, limita de complexitate sau criteriile de review numite explicit.

## Contradictions and ambiguities

Nu au fost identificate contradicții directe sau ambiguități nerezolvate în fixture. Eliminarea `R004` este pentru vag, nu pentru contradicție.

## Platform implementation notes

- Codex: `R001` și `R002` rămân `unverified` până la verificarea mecanismelor curente de sandbox, aprobare, script sau lifecycle. Nu este revendicat un hook nativ.
- Claude: `R001` și `R002` rămân `unverified` până la verificarea documentației curente pentru permissions, hooks sau scripturi. Nu este inventat un nume de event.
- `R003`, `R004` și `R005` nu își schimbă dispoziția între platforme.

## Validation summary

Pachetul JSON pereche folosește schema `1.0`, aceleași ID-uri și statusul `proposed` pentru ambele controale. Validatorul determinist verifică structura și coerența internă; nu validează semantic judecata și nu activează controalele.

## Limitations and next step

Acesta este un caz de calibrare, nu un audit de producție. Următorul pas posibil este verificarea platform-specifică a fezabilității, urmată de o decizie umană separată privind generarea unui control. V1 nu generează și nu instalează nimic.

No audited source, control, hook, configuration, or permission was modified.
