# m2c1 - Framework de orchestrare autonomă a dezvoltării

Import din [grandamenium/m2c1](https://github.com/grandamenium/m2c1), licență MIT. Conținutul e păstrat în engleză, exact cum a fost scris de autor. README-ul ăsta e ce citești tu înainte să decizi dacă îl instalezi.

Ia o idee spusă dezordonat și o duce, în 12 faze, până la o aplicație construită, testată și publicată, cu cât mai puține intervenții umane. Nu e un skill de planificare, e un motor de execuție: după ce cele 12 faze de pregătire se termină, dai `/start` și orchestratorul ia sarcină cu sarcină, deschide câte un subagent pentru fiecare, testează și trece mai departe.

## Cele 12 faze, pe scurt

| Faza | Ce se întâmplă |
|---|---|
| 0 | creează structura de foldere a orchestrării |
| 1 | transformă ideea aruncată în PRD, sub 500 de rânduri |
| 2 | primul val de cercetare: câte un subagent paralel per domeniu atins |
| 3 | întrebările de clarificare, cu auto-audit pe 12 categorii înainte de a merge mai departe |
| 4 | al doilea val de cercetare, filtrat prin răspunsurile tale |
| 5 | instalarea uneltelor: MCP-uri, CLI-uri, conturi, chei API |
| 6 | verificarea fiecărei unelte cu o operație reală, nu cu o bifă |
| 7 | scrie câte un skill de proiect pentru fiecare unealtă, sursă de date și strategie de testare |
| 8 | îți cere să compactezi contextul, fiindcă toată starea e deja în fișiere |
| 9 | PHASES.md, planul general, cu sarcini, dependențe și criterii |
| 10 | sfărâmarea planului: fiecare sarcină devine un prompt de sine stătător pentru un agent de execuție |
| 11 | revizia de coerență între faze: contradicții, contracte de date care nu se potrivesc, goluri |
| 12 | PROGRESS.md, START.md și secțiunea de orchestrare din CLAUDE.md |

Cele două lucruri care îl deosebesc de un skill obișnuit de planificare sunt faza 3c și faza 7. Faza 3c e un auto-audit cu o întrebare de închidere: dacă un agent de execuție ar citi doar DISCOVERY.md, ar putea lua fiecare decizie de implementare fără să ghicească? Dacă răspunsul e nu, se întoarce și mai întreabă. Faza 7 obligă la câte un skill scris pentru fiecare unealtă și fiecare domeniu, ca agenții de execuție să nu inventeze forma unui API.

## Cerință obligatorie

**Playwright MCP.** Nu e opțional și framework-ul refuză să pornească fără el, fiindcă îl folosește în două locuri: la faza 5, ca să-ți creeze conturi și chei prin interfețele web ale serviciilor, și la testare, ca să treacă prin aplicație cum ar trece un om.

## Ce te costă

Ăsta e un framework greu, nu unul de buzunar. Numără subagenții înainte să-l pornești:

- două valuri de cercetare, cu câte un subagent per domeniu atins de proiect
- **câte un subagent de scris skill pentru fiecare unealtă, fiecare MCP, fiecare sursă de date, fiecare domeniu de cercetare, fiecare strategie de testare și fiecare bibliotecă netrivială.** Pe un proiect care atinge cinci servicii externe, aici sunt ușor douăzeci de subagenți
- câte un subagent de sfărâmare per fază
- subagenți de revizie a coerenței
- apoi, la execuție, câte un subagent per sarcină, plus un test de regresie la finalul fiecărei faze, plus o fază întreagă dedicată testării finale

Merită pe un proiect pe care chiar vrei să-l duci până la capăt fără să stai lângă el. Pe o aplicație mică sau pe o unealtă personală, pregătirea singură costă mai mult decât ai fi construit de mână.

## Ce trebuie să știi înainte să-l pornești

**Faza 5 îți cere credențiale.** Framework-ul îți cere parolele de la serviciile la care trebuie să intre, se autentifică în locul tău prin browser, generează chei API din panourile serviciilor și le scrie în `.env`-ul proiectului. E exact ce îl face autonom, dar înseamnă că treci chei și parole printr-un agent. Dacă lucrezi cu conturi de producție sau cu date de clienți, pregătește-ți întâi conturi separate de test.

**Faza 3a se uită prin spațiul tău de lucru.** Înainte să pună întrebări, framework-ul explorează directoarele tale, fișierele CLAUDE.md și documentația existentă, ca să înțeleagă contextul de business, proiectele și audiențele tale, și să pună întrebări mai bune. Pornește-l dintr-un folder de proiect, nu din rădăcina în care ții tot.

**Toate deciziile stau în DISCOVERY.md**, care e documentul de autoritate supremă. Dacă te răzgândești mai târziu, acolo se schimbă, nu în conversație.

## Compatibilitate

```yaml
compatibility: claude-code-only
```

Depinde de subagenți Claude și de un workflow multi-agent nativ, de Playwright MCP, de comanda `/start` și de structura `~/.claude/skills/`. Nu are echivalent în Codex.

## Instalare

Are subfoldere, deci se instalează ca skill complet, nu ca fișier de comandă:

```bash
mkdir -p ~/.claude/skills/m2c1
cp -R tehnic/m2c1/artifact-templates ~/.claude/skills/m2c1/
cp tehnic/m2c1/orchestration-workflow.md ~/.claude/skills/m2c1/
cp tehnic/m2c1/skill.md ~/.claude/skills/m2c1/SKILL.md
```

**Calea contează, nu o schimba.** Protocolul trimite subagenții la șabloane prin calea absolută `~/.claude/skills/m2c1/artifact-templates/...`, în trei locuri. Nu e o scăpare a autorului: un subagent pornește în directorul proiectului, nu în cel al skill-ului, deci o cale relativă ar căuta șabloanele în proiect și nu le-ar găsi. Instalat în altă parte, framework-ul pornește și cade abia la faza 2, când primul agent de cercetare nu găsește șablonul.

## Cum îl folosești

Deschizi o sesiune Claude Code în folderul proiectului și îți descrii ideea, dezordonat, cum îți vine. Skill-ul se recunoaște singur din descriere și pornește faza 1. Răspunzi la întrebările de la faza 3, treci prin instalarea uneltelor la faza 5, iar după faza 12 dai `/start` și începe execuția.

Între timp îți va cere o dată să compactezi contextul (faza 8). Nu pierzi nimic: toată starea e în fișiere, iar PROGRESS.md face ca orice sesiune nouă să continue de unde s-a oprit ultima.

## Cum se împacă cu restul librăriei

| Vrei | Folosește |
|---|---|
| o singură funcționalitate într-o aplicație existentă | `/plan` |
| documentul de produs, fără execuție | `/create-prd` |
| tot lanțul, de la idee la aplicație publicată, cu execuție autonomă | `m2c1` |

## Licența

MIT, declarată în README-ul repo-ului sursă. Repo-ul nu are fișier `LICENSE` separat, motiv pentru care GitHub nu afișează licența în interfață. Am păstrat `license:` și `source:` în frontmatter, conform CONTRIBUTING.md.
