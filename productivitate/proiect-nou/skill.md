---
name: proiect-nou
compatibility: claude-code-only
license: MIT
description: "Pregătește un folder de proiect ca să nu depindă de conversațiile vechi: CLAUDE.md cu regula de decizii, DECIZII.md (unde am rămas + decizii cu motiv) și, dacă proiectul are cod, git. Merge pe folder gol sau pe proiect existent, fără să suprascrie nimic. Se declanșează cu /proiect-nou sau la formulări ca „pornesc un proiect nou”, „pregătește folderul ăsta”, „vreau ca proiectul să nu depindă de conversații”. Nu se folosește în folderul unui agent (are IDENTITY.md și SOUL.md)."
---

# Proiect nou: folderul care nu depinde de conversații

Conversațiile din Claude Code se șterg după `cleanupPeriodDays` (implicit 30 de zile).
Skill-ul ăsta pune în folderul curent cele trei lucruri care fac proiectul să-și țină
singur firul: un `CLAUDE.md` care se încarcă la fiecare sesiune, un `DECIZII.md` cu
stadiul și deciziile, și git, dacă e cod.

Pui întrebările una câte una, câte una pe mesaj, și aștepți răspunsul. Nu anunți lista
de pași dinainte.

## Pasul 0. Verifici unde ești

Rulezi:

```
pwd; ls -A
```

- Dacă folderul are și `IDENTITY.md`, și `SOUL.md`, e folderul unui agent. Te oprești
  și spui că agenții au propria memorie (`MEMORY.md`) și că skill-ul nu se aplică aici.
- Dacă folderul e chiar folderul de acasă al utilizatorului (`~`), te oprești și ceri
  un folder dedicat proiectului.
- Notezi ce există deja: `CLAUDE.md`, `DECIZII.md`, `.git`, `.gitignore`. Nimic din ce
  există nu se suprascrie.

## Pasul 1. Întrebarea 1: despre ce e proiectul

„Ce construiești aici, într-o frază sau două? Pentru cine e?”

Dacă folderul are deja fișiere, te uiți întâi prin ele și propui tu fraza, iar omul
doar confirmă sau corectează.

## Pasul 2. Cauți ce s-a decis deja, apoi întrebarea 2

Înainte să întrebi, cauți singur deciziile în ce a rămas de la sesiunile anterioare din
acest folder. Nu anunți căutarea ca pe un pas separat; spui doar, la final, ce ai găsit.

**Unde cauți.** Conversațiile și memoria automată ale folderului stau în
`~/.claude/projects/<slug>/` (pe Windows `%USERPROFILE%\.claude\projects\<slug>\`).
`<slug>` e calea completă a folderului curent, cu fiecare caracter care nu e literă sau
cifră înlocuit cu `-` (de exemplu `/Users/ana/Proiecte/site cafenea` devine
`-Users-ana-Proiecte-site-cafenea`, iar `C:\Users\ana\site` devine `C--Users-ana-site`).
Dacă folderul cu numele ăsta nu există, cauți cu Grep, în `~/.claude/projects/*/*.jsonl`,
un fișier care conține `"cwd":"<calea curentă>"` (pe Windows, cu backslash-urile dublate).

Acolo citești:

1. `memory/` (dacă există): fișierele de memorie ale proiectului, de citit integral.
2. Fișierele `*.jsonl` (conversațiile), fără cel al sesiunii curente (cel mai recent
   modificat). Nu le citești întregi, pot avea zeci de MB. Folosești Grep pe liniile cu
   `"type":"user"` și te uiți doar la textul scris de om (nu la `tool_result`, nu la
   blocurile `<system-reminder>`), după semne de decizie: „am decis”, „alegem”, „mergem
   pe”, „rămâne”, „nu vreau”, „de acum”, „da” ca răspuns la o propunere, plus
   echivalentele în engleză. Unde un „da” confirmă ceva, citești mesajul asistentului de
   dinainte, ca să știi ce s-a confirmat.

**Ce iese.** O listă de decizii candidate, fiecare cu data conversației (din câmpul
`timestamp`) și cu motivul doar dacă apare în conversație. Fără motiv găsit, scrii
„Motiv: nespecificat”. O decizie schimbată ulterior în altă conversație apare o singură
dată, în forma ei finală.

**Dacă nu găsești nimic** (folder nou, fără conversații, sau conversații fără decizii),
spui asta într-o propoziție și treci la întrebare.

**Întrebarea 2**, în funcție de rezultat:

- cu candidați: „Din conversațiile anterioare am găsit deciziile de mai jos. Sunt
  corecte? Ce nu mai e valabil, ce lipsește, și unde știi motivul, spune-mi-l.” Urmează
  lista. Nicio decizie candidată nu intră în `DECIZII.md` fără confirmarea omului.
- fără candidați: „Ai deja decizii luate pentru proiect? De exemplu, cu ce unelte
  lucrezi, ce ai exclus, ce formă are rezultatul. Spune-mi și de ce, unde știi.”

Dacă spune că nu, treci mai departe. Nu inventezi decizii și nu completezi motive pe
care omul nu le-a spus: unde lipsește motivul, scrii „Motiv: nespecificat”.

Conversațiile mai vechi decât perioada de păstrare (`cleanupPeriodDays`, implicit 30 de
zile) au fost deja șterse. Ce s-a decis acolo poate fi recuperat doar din memoria omului.

## Pasul 3. Întrebarea 3: e cod?

Pui întrebarea doar dacă nu reiese din primele două răspunsuri sau din fișiere.
„Proiectul are cod (aplicație, scripturi, site) sau e doar documente?”

## Pasul 4. Scrii fișierele

Arăți întâi ce urmează să scrii (conținutul complet al fișierelor noi; la cele existente,
doar ce adaugi) și scrii după confirmare.

**`DECIZII.md`** (dacă nu există):

```
# Decizii: [numele proiectului]

## Unde am rămas

[AAAA-LL-ZZ: proiectul pornește. Ce e de făcut primul.]

## Decizii

- [câte un element de listă: „AAAA-LL-ZZ: decizia. Motiv: de ce.”, din răspunsul la întrebarea 2]
```

„Unde am rămas” are maximum 10 rânduri și se rescrie, nu se lungește. „Decizii” doar
crește, fiecare decizie pe un rând care începe cu `- ` (fără liniuță, rândurile se lipesc
într-un paragraf în previzualizare); o decizie schimbată primește o linie nouă care o înlocuiește pe cea veche,
cu motivul schimbării.

**`CLAUDE.md`** (dacă nu există, îl creezi; dacă există, adaugi doar secțiunea de mai jos,
la final, dacă nu e deja acolo):

```
# [Numele proiectului]

[Fraza de la întrebarea 1.]

## Continuitate

La începutul fiecărei sesiuni citești DECIZII.md.

Când luăm o decizie sau când te corectez, o scrii în DECIZII.md înainte să mergi mai
departe: un rând de listă, „- AAAA-LL-ZZ: decizia. Motiv: de ce.” Când se schimbă stadiul
proiectului, rescrii „Unde am rămas”.

Nu scrii acolo ce e deja în cod sau în istoricul git, nici detaliile unei singure sesiuni.
```

**git** (doar dacă e cod și nu există deja `.git`): `git init`, plus un `.gitignore`
potrivit limbajului, care exclude obligatoriu `.env`, `*.key` și `node_modules/` sau
echivalentul. Faci primul commit doar dacă omul confirmă.

## Pasul 5. Testul sesiunii goale

Îi spui omului ce să facă, el îl rulează:

1. `/clear` (sau o sesiune nouă în același folder).
2. Întreabă: „Unde am rămas în proiectul ăsta și ce am decis?”
3. Răspunsul trebuie să vină din DECIZII.md. Dacă lipsește ceva, se trece acolo.

## Ce nu faci

- Nu suprascrii fișiere existente.
- Nu pui `DECIZII.md` în `CLAUDE.md`: `CLAUDE.md` se încarcă la fiecare mesaj și trebuie
  să rămână scurt; `DECIZII.md` se citește prin regulă.
- Nu inventezi decizii, motive sau stadii.
- Nu rulezi skill-ul în folderul unui agent sau în folderul de acasă.
