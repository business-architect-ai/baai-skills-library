# /opinion - A doua părere pe o decizie grea

Cere două păreri independente pe o decizie deja formulată, de la modele din familii diferite, apoi le pune față în față și arată unde sunt de acord și unde se contrazic. Nu decide în locul tău.

Ideea de la care pornește: două modele din aceeași familie greșesc adesea la fel, iar atunci acordul lor îți dă o falsă siguranță. De aceea a doua voce vine, pe cât posibil, din altă familie.

## Când îl folosești

- Ai de luat o decizie greu de întors și o iei singur.
- Ești deja sigur pe un răspuns și vrei să vezi dacă rezistă. Aici lucrează cel mai bine.
- Decizia atinge alți oameni, deci greșeala ta se multiplică.
- Ai stat prea mult în interiorul problemei și nu mai vezi alternativa.

Nu îl folosi pentru decizii reversibile ieftin. Dacă poți încerca și da înapoi în zece minute, încearcă.

## Ce produce

- Un rezumat scris al deciziei, pe care îl confirmi înainte să plece
- Două păreri independente, în același format, fiecare cu presupunerile ei declarate
- O sinteză scrisă de o a treia inteligență care nu a dat nicio părere
- Un folder cu tot, ca istoric al deciziilor tale

Sinteza are patru părți: unde sunt de acord, unde se contrazic, ce a văzut una și n-a văzut cealaltă, și recomandarea finală. Partea cu contradicțiile e cea mai valoroasă, fiindcă acolo e riscul real al deciziei.

## Compatibilitate

```yaml
compatibility: claude-code-only
```

Folosește subagenți Claude și un workflow multi-agent, deci nu merge ca skill de Codex. Vocile externe se cheamă prin unelte de linie de comandă, dar orchestrarea e nativă Claude Code.

## Instalare Claude Code

Are subfoldere, deci se instalează ca skill complet, nu ca fișier de comandă:

```bash
mkdir -p ~/.claude/skills/opinion
cp -R productivitate/opinion/tools productivitate/opinion/prompts ~/.claude/skills/opinion/
cp productivitate/opinion/skill.md ~/.claude/skills/opinion/SKILL.md
chmod +x ~/.claude/skills/opinion/tools/*.sh
```

## Instalare într-un agent cortextOS

Aceleași fișiere, în folderul agentului. Skill-ul recunoaște singur unde e instalat și își scrie rezultatele în `<agent>/opinions`:

```bash
mkdir -p <agent>/.claude/skills/opinion
cp -R productivitate/opinion/tools productivitate/opinion/prompts <agent>/.claude/skills/opinion/
cp productivitate/opinion/skill.md <agent>/.claude/skills/opinion/SKILL.md
chmod +x <agent>/.claude/skills/opinion/tools/*.sh
```

În flotă se schimbă trei reguli, descrise în secțiunea „Mod flotă" din `skill.md`: confirmarea rezumatului trece prin skill-ul `approvals`, fiindcă nu e nimeni la tastatură; skill-ul nu se invocă niciodată singur din heartbeat sau cron; rezumatul îl scrie orchestratorul, nu agentul care are dilema, fiindcă acela e parte interesată în propriul caz.

Ține-l pe orchestrator. Specialiștii nu îl dețin, îl cer.

## Verifică instalarea

```bash
~/.claude/skills/opinion/tools/autotest.sh
```

Durează un minut, fiindcă la final cere o părere scurtă de probă ca să dovedească faptul că lanțul chiar funcționează, nu doar că fișierele sunt la locul lor.

Verdictul e în limbaj de om: „gata de folosit", „merge, cu rezerve" sau „nu e gata", cu ce anume trebuie reparat. Dacă nu îți dai seama ce să faci, textul e scris ca să poată fi trimis ca atare mai departe.

Doar fișierele, fără să cheme niciun model:

```bash
AUTOTEST_FARA_PROBA=1 ~/.claude/skills/opinion/tools/autotest.sh
```

## A doua voce

Funcționează fără nimic instalat în plus, dar atunci ambele păreri vin de la Claude, iar skill-ul îți spune de fiecare dată că diversitatea a fost mică. Ca să ai o a doua familie adevărată, îți trebuie una dintre:

| Unealtă | Ce cere | Calitatea părerii |
|---|---|---|
| Codex CLI | cont OpenAI | foarte bună, verificată |
| Ollama | nimic, rulează local | slabă, dar gratuită și privată, verificată |
| Gemini CLI | cont Google | adaptor scris, dar încă netestat de nimeni |

Skill-ul detectează singur ce ai și alege. O familie nouă înseamnă un fișier de cincisprezece linii în `tools/adaptoare/`, fără modificări în altă parte.

## Cum îl folosești

```
/opinion [întrebarea ta]
```

Regula care contează cel mai mult: pornește-l în sesiunea în care a apărut decizia, nu într-una nouă. Toată valoarea vine din faptul că agentul scrie rezumatul din discuția pe care tocmai ai avut-o. Într-o sesiune goală ajungi să-i rescrii tu tot contextul, adică exact munca pe care skill-ul ar trebui să o scutească.

Poți indica și un folder cu fișiere relevante:

```
/opinion dacă separ modulul de plăți de cel de facturare.
Contextul e în /Users/numele-tau/proiecte/aplicatia-mea
```

## Cum citești rezultatul

Nu începe cu recomandarea finală. Începe cu secțiunea unde se contrazic.

Apoi uită-te la presupunerile fiecărei păreri. Dacă una pleacă de la o presupunere falsă, se aruncă, nu se cântărește. E cel mai frecvent motiv pentru care două modele bune ajung la concluzii opuse.

Dacă apare secțiunea „consens suspect", tratează-o ca pe un avertisment. Înseamnă că ambele au răspuns la fel din aceleași motive, ceea ce se întâmplă des când rezumatul sugera răspunsul fără să vrei.

## Cât costă și cât durează

Două sau trei apeluri către modele puternice per rulare. Nu e o unealtă pentru orice bifurcație. Folosește-o pentru deciziile pe care le-ai regreta o lună.

Pe o decizie serioasă, cu un briefing de vreo nouă mii de caractere și un folder de context, măsurat pe o rulare reală: patru minute vocea externă, opt minute și jumătate vocea Claude, unsprezece minute arbitrul. De la confirmarea rezumatului până la sinteză, douăzeci și două de minute. Nu e o unealtă la care stai să te uiți. Pornește-o și întoarce-te.

## Depanare

Secțiunea de depanare din `skill.md` acoperă problemele cunoscute: unelte prea vechi, Ollama care nu răspunde, păreri superficiale de la modele mici, cronometrul. Rulează întâi autotestul, îți spune el în majoritatea cazurilor ce s-a stricat.
