---
name: opinion
version: 2.0.0
description: A doua părere pe o decizie grea, cerută de la mai multe familii de modele independente (Claude, plus GPT prin Codex, Gemini sau un model local, după ce e disponibil), urmată de o fuziune arbitrată de un context care nu a opinat. Pentru decizii greu reversibile, luate singur. Se declanșează cu /opinion sau la formulări ca "vreau o a doua părere", "ce ar spune altcineva despre asta", "verifică-mi decizia asta".
compatibility: claude-code-only
---

# opinion

Aduce două păreri independente pe o decizie deja formulată, din familii de modele diferite, apoi le pune față în față. Nu decide în locul omului.

Ideea de la care pornește: două opinii care greșesc la fel îți dau senzația de confirmare. De aceea a doua voce trebuie să vină, pe cât posibil, din altă familie de modele decât prima.

## Când se folosește

Decizii greu reversibile, unde greșeala se plătește săptămâni: arhitectura unui sistem, ordinea dintre etape într-un flux, structura unui modul, alegerea între două direcții pe care se construiește mult.

Merge cel mai bine când ești deja sigur. Atunci testează o convingere în loc să umple un gol.

## Când nu se folosește

Decizii reversibile ieftin. Dacă poți încerca și da înapoi în zece minute, încearcă. Fiecare rulare înseamnă două sau trei apeluri de model puternic.

Când dilema nu e încă formulată. Formuleaz-o întâi, apoi vino cu întrebarea limpede.

Când răspunsul depinde de ceva ce știe doar omul și nu poate pune în briefing. Fără informația aia, ambele voci opinează pe presupuneri.

## Procedura

### Pasul 0: află unde ești și cu cine poți vorbi

Folderul acestui skill îl știi, ai citit `SKILL.md` din el. Rulează de acolo:

```
<CALE-SKILL>/tools/unde-sunt.sh
<CALE-SKILL>/tools/detecteaza.sh
```

Primul îți dă două valori pe care le folosești peste tot mai jos: `<CALE-SKILL>` și `<CALE-REZULTATE>`. Nu presupune niciodată calea, fiindcă același pachet se instalează și personal, în `~/.claude/skills/opinion`, și în folderul unui agent din flotă. Scriptul le rezolvă singur.

Al doilea îți spune cine e disponibil.

Întoarce o linie per familie, în forma `familie|stare|nume|greutate|citește-fișiere`. Reține care sunt `disponibil`.

Alege a doua voce în ordinea asta:

1. o familie de frontieră, alta decât Claude: `codex` sau `gemini`
2. dacă nu există niciuna, un model local: `ollama`
3. dacă nu există nici asta, un al doilea model Claude, printr-un subagent pe alt model decât primul

În cazurile 2 și 3 spune-i omului, la final, că diversitatea a fost mai mică decât ideal și că un consens între voci apropiate valorează mai puțin. Nu ascunde asta niciodată.

### Pasul 1: uită-te dacă s-a mai discutat

```
ls <CALE-REZULTATE>/ 2>/dev/null
```

Doar numele folderelor. Dacă vreunul pare pe aceeași temă, spune-o înainte să continui. Omul decide dacă se uită.

### Pasul 2: fă folderul

Slug din întrebare, cu cratime, maximum 40 de caractere. Dacă folderul există, adaugă `-2`, `-3`.

```
mkdir -p <CALE-REZULTATE>/$(date +%F)-slugul-tau
```

### Pasul 3: scrie briefingul

În `briefing.md`, din discuția curentă. Omul nu retastează nimic, asta e toată ideea.

O întrebare per rulare. Dacă discuția a produs mai multe dileme distincte, nu le împacheta împreună și nu alege tu care contează: enumeră-le scurt și lasă omul să spună pe care se dă dezbaterea. Un briefing cu două întrebări întoarce două opinii care răspund la jumătăți diferite, iar arbitrul nu are ce fuziona.

Șablonul:

```markdown
# [titlul deciziei]

## Întrebarea
[O singură întrebare, formulată ca alegere, nu ca temă de discuție.]

## Opțiunile pe care le vede
A. [...]
B. [...]

## Context și constrângeri
[Ce e adevărat despre situația lui și contează. Ce are deja construit, ce nu poate
schimba, cu ce timp și cu ce bani lucrează, cine folosește rezultatul.]

## Ce s-a încercat sau decis deja
[Ca să nu i se recomande ce a exclus deja, și de ce a exclus.]

## Ce nu e în discuție
[Limitele. Altfel primești păreri despre alte întrebări.]

## Folderul de context
[Cale absolută. Vocile care pot citi fișiere au voie să se uite acolo.]

## Ce fel de răspuns e util
[Ce ar trebui să conțină un răspuns ca să-l ajute efectiv.]
```

Trei reguli la scris:

1. Neutru. Nu strecura varianta pe care o crezi tu bună, nici prin ordinea opțiunilor, nici prin cât spațiu dai fiecăreia. Dacă briefingul sugerează răspunsul, primești două ecouri și omul crede că are confirmare.
2. Constrângerile reale intră toate. Cele mai multe divergențe între modele vin din presupuneri diferite despre realitate, iar ce lipsește din briefing ele inventează.
3. Sub 300 de caractere nu pleacă. Completează-l.

### Pasul 4: oprire pentru confirmare

Arată-i briefingul omului înainte să plece. E singura oprire obligatorie din tot fluxul. Motivul: un briefing greșit strică toate opiniile deodată, iar asta nu se vede în rezultat, se vede peste două săptămâni.

### Pasul 5: vocile, în paralel

Lansează-le în același mesaj, ca să ruleze simultan.

**Vocea Claude**, subagent de tip `general-purpose`, cu context proaspăt:

```
Citește, în ordinea asta:
1. <CALE-SKILL>/prompts/format-opinie.md, care e contractul de format. Respectă-l exact.
2. <FOLDER>/briefing.md, care e decizia.

Ai voie să citești fișierele din <FOLDER-CONTEXT> ca să verifici ce se afirmă în briefing
și ca să găsești ce lipsește din el. Nu modifica nimic acolo.

Scrie răspunsul tău în <FOLDER>/opinie-claude.md. Acela e singurul fișier pe care ai voie
să-l scrii. La final adaugă o linie:
---
Sursa: Claude. Greutate: frontiera. Acces la fisiere: da.

Când ai terminat, întoarce o singură linie: "OK: opinie-claude.md scrisă".
Nu întoarce conținutul opiniei. Chiar nu, oricât de bună ți se pare.
```

Linia finală nu e figură de stil. Dacă subagentul întoarce opinia întreagă, intră în contextul sesiunii principale și dispare economia pentru care e construit fluxul așa.

**Vocea externă**, prin Bash, cu familia aleasă la pasul 0:

```
<CALE-SKILL>/tools/cere-parere.sh <FAMILIE> <FOLDER> <FOLDER-CONTEXT>
```

Motorul pune singur semnătura cu sursa și greutatea la finalul opiniei. Dacă nu există folder de context, dă calea folderului deciziei.

**Dă-i folderele reale, nu copii.** Vocea externă citește prin cale absolută de oriunde de pe disc, chiar dacă procesul rulează din folderul deciziei. Verificat pe Codex sub sandbox `read-only`: sandboxul interzice scrierea, nu citirea. Nu construi un folder cu fișiere copiate ca să ocolești o restricție care nu există.

Copiază fișiere într-un folder de context propriu doar când ai un motiv anume, de pildă că nu vrei să deschizi un repo cu secrete unui CLI extern. Atunci spune în briefing că e o selecție, nu repo-ul întreg. Motivul: ambele voci rămân închise în ce ai ales tu și nu mai pot găsi ce n-ai pus acolo, iar un acord între ele pe ceva citit din același folder curat nu e confirmare din două surse, e aceeași sursă citită de două ori. Arbitrul are dreptate să scadă din greutatea acordului, și o face.

### Pasul 6: judecătorul

Un al doilea subagent `general-purpose`, cu context proaspăt, care nu a dat nicio opinie:

```
Citește, în ordinea asta:
1. <CALE-SKILL>/prompts/prompt-fuziune.md, care e rolul tău
2. <FOLDER>/briefing.md
3. toate fișierele <FOLDER>/opinie-*.md

Scrie fuziunea în <FOLDER>/fuziune.md, apoi întoarce textul integral al fuziunii.
```

Aici da, vrei textul întors. Fuziunea e singurul lucru care are ce căuta în conversație.

### Pasul 7: raportul

Arată fuziunea și calea folderului. Dacă a doua voce a fost slabă sau din aceeași familie, spune-o aici, nu la sfârșit ca notă de subsol.

Nu adăuga propria ta părere peste fuziune în același mesaj: ai fost prezent la formularea întrebării, deci nu ești o voce independentă. Dacă ai ceva de spus, spune separat și spune că e a ta.

## Mod flotă

Se aplică atunci când skill-ul e instalat în folderul unui agent, adică în `<agent>/.claude/skills/opinion`, nu în casa unui om. `unde-sunt.sh` recunoaște singur situația și scrie rezultatele în `<agent>/opinions`.

Trei reguli se schimbă, și niciuna nu e opțională.

**Confirmarea briefingului devine aprobare.** În flotă nu e nimeni la tastatură, deci oprirea de la pasul 4 nu poate fi o întrebare în conversație. Creează o aprobare prin skill-ul `approvals`, blochează sarcina și așteaptă decizia în inbox. Conținutul aprobării e briefingul întreg, ca omul să-l poată corecta înainte, nu după. Fără poarta asta, singura corecție umană din tot fluxul dispare, iar cele două opinii se formează pe o încadrare pe care nu a validat-o nimeni.

**Nu se invocă singur, niciodată.** Nu la heartbeat, nu din cron, nu fiindcă agentul a considerat că o decizie merită. Se pornește doar la cererea explicită a omului sau atunci când orchestratorul arbitrează o escaladare. Fiecare rulare înseamnă două sau trei apeluri de model puternic, iar un agent care se trezește noaptea și se consultă din proprie inițiativă costă bani fără ca cineva să afle.

**Briefingul îl scrie orchestratorul, nu agentul cu dilema.** Agentul care are problema e parte interesată: își descrie cazul cu propria încadrare, cu propriile presupuneri, și nu are cine să-l corecteze. La om, briefingul îl scrie asistentul și îl corectează omul. În flotă, rolul de corector îi revine orchestratorului. Specialiștii nu dețin skill-ul, îl cer, la fel cum evaluatorul escaladează prin orchestrator în loc să decidă singur.

Restul procedurii e identică. Vocile, judecătorul, contractul de format, degradarea, toate funcționează la fel.

## Degradare

Codurile de ieșire ale lui `cere-parere.sh`: `0` a mers, `1` familia nu e disponibilă, `2` a depășit timpul, `3` CLI-ul a ieșit cu eroare, `4` a răspuns dar fișierul e gol, `5` argumente sau briefing lipsă, `6` nu există adaptor cu numele cerut.

La `1` încearcă următoarea familie din ordinea de la pasul 0. La `2`, `3` sau `4` nu insista cu aceeași familie, treci mai departe și spune ce a eșuat. Motivul e în `<FOLDER>/.log-<familie>.txt`.

Dacă rămâne o singură voce, nu chema judecătorul, fiindcă nu are ce arbitra. Arată opinia rămasă și spune explicit, cu titlu vizibil, că e o singură voce și de ce a lipsit a doua.

Regula care le acoperă pe toate: o singură opinie prezentată ca două e mai rea decât nicio opinie, fiindcă dă încredere nemeritată. Degradarea se anunță întotdeauna, niciodată în tăcere.

## Familii și adaptoare

Fiecare familie e un fișier în `tools/adaptoare/`, de vreo cincisprezece linii, care declară cum se cheamă unealta și cum se verifică dacă există. Motorul face restul. O familie nouă înseamnă un fișier nou acolo, fără modificări în altă parte.

Starea la 2026-08-07: `codex` verificat, `ollama` verificat, `gemini` scris dar netestat, fiindcă unealta nu era instalată pe mașina pe care s-a construit skill-ul. Antetul din `adaptoare/gemini.sh` spune ce trebuie verificat la prima rulare.

## Depanare

**Codex iese cu 400 și mesajul „requires a newer version of Codex".** CLI-ul e mai vechi decât modelul din `~/.codex/config.toml`. Reparație: `npm install -g @openai/codex@latest` dacă e instalat prin npm, altfel prin managerul cu care l-ai pus. Soluție de moment: `OPINION_MODEL=<model-mai-vechi>`.

**Ollama spune indisponibil deși e instalat.** Adaptorul cere trei lucruri: comanda `ollama`, `python3` și serverul local care răspunde la `http://localhost:11434`. Verifică al treilea cu `curl -s http://localhost:11434/api/tags`.

**Opinia locală e ezitantă sau superficială.** Normal pentru modele mici. Semnătura o marchează cu greutate slabă, iar judecătorul o cântărește corespunzător. Alege alt model cu `OPINION_MODEL_LOCAL=...`.

**Rămâne un fișier `AGENTS.md` în folderul deciziei.** Unele unelte sau plugin-uri scriu context în directorul curent. E inofensiv acolo. Din acest motiv scripturile rulează din folderul deciziei, nu din folderele de lucru.

**Cronometrul.** Implicit 600 de secunde, se schimbă cu `OPINION_TIMEOUT`. Nu se folosește `timeout` din coreutils, fiindcă macOS nu îl are.
