---
name: proiect-nou
compatibility: claude-code-only
license: MIT
description: "Pregătește un folder de proiect ca să nu depindă de conversațiile vechi și să nu existe doar pe un singur disc: CLAUDE.md cu regula de decizii, DECIZII.md (unde am rămas + decizii cu motiv), git cu .gitignore (propus pentru orice proiect, cu întrebare), regula cheilor (Keychain pe Mac, SecretStore pe Windows) și, la cerere, o copie privată pe GitHub. Merge pe folder gol sau pe proiect existent, fără să suprascrie nimic. Se declanșează cu /proiect-nou sau la formulări ca „pornesc un proiect nou”, „pregătește folderul ăsta”, „vreau ca proiectul să nu depindă de conversații”. Nu se folosește în folderul unui agent (are IDENTITY.md și SOUL.md)."
---

# Proiect nou: folderul care nu depinde de conversații

Conversațiile din Claude Code se șterg după `cleanupPeriodDays` (implicit 30 de zile), iar
un folder care stă doar pe discul tău se pierde odată cu discul. Skill-ul ăsta pune în
folderul curent ce face proiectul să-și țină singur firul: un `CLAUDE.md` care se încarcă
la fiecare sesiune, un `DECIZII.md` cu stadiul și deciziile, git pentru istoricul
versiunilor și, la cerere, o copie privată pe GitHub.

Pui întrebările una câte una, câte una pe mesaj, și aștepți răspunsul. Nu anunți lista
de pași dinainte.

## Pasul 0. Verifici unde ești

Rulezi (pe Windows, în PowerShell: `Get-Location; Get-ChildItem -Force`):

```
pwd; ls -A
```

- Dacă folderul are și `IDENTITY.md`, și `SOUL.md`, e folderul unui agent. Te oprești
  și spui că agenții au propria memorie (`MEMORY.md`) și că skill-ul nu se aplică aici.
- Dacă folderul e chiar folderul de acasă al utilizatorului (`~`), te oprești și ceri
  un folder dedicat proiectului.
- Notezi ce există deja: `CLAUDE.md`, `DECIZII.md`, `.git`, `.gitignore`. Nimic din ce
  există nu se suprascrie.

**Numele folderului.** Dacă numele folderului proiectului are spații sau diacritice
(ă, â, î, ș, ț), spui asta înainte de orice altceva: spațiile și diacriticele din căi
strică scripturi și comenzi, iar macOS poate scrie diacriticele în două forme diferite,
care nu se mai potrivesc între ele. Propui un nume scurt, cu litere mici și cratimă (de
exemplu `site cafenea` devine `site-cafenea`). Redenumirea se face acum sau niciodată:
mai târziu rupe legătura cu sesiunile și memoria din folder. Dacă omul acceptă, îi spui
să închidă sesiunea, să redenumească folderul din Finder (sau Explorer) și să pornească
din nou `/proiect-nou` în folderul redenumit. Dacă refuză, mergi mai departe.

**Chei.** Dacă vezi fișiere `.env` (în afară de `.env.example`), `*.key` sau `*.pem`,
nu le deschizi și nu le afișezi conținutul. Spui că există și că le tratezi la pasul 4.

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

## Pasul 3. Întrebarea 3: git

Dacă folderul are deja `.git`, sari peste întrebare.

Altfel: „Vrei istoric de versiuni (git) pentru proiect? Fiecare salvare e o fotografie a
fișierelor: vezi oricând ce s-a schimbat, te poți întoarce la o versiune veche și poți
avea o copie pe GitHub. Îl recomand pentru orice proiect, cod sau documente.”

Dacă proiectul are cod (aplicație, scripturi, site), spui că acolo git e practic
obligatoriu. Dacă omul refuză, nu insiști: scrii doar `CLAUDE.md` și `DECIZII.md`, iar
la pasul 4 sari peste git și peste regula de salvare.

Din fișiere și din primele răspunsuri știi deja ce fel de proiect e (cod, și ce limbaj,
sau documente). Întrebi separat doar dacă nu reiese, pentru că `.gitignore` depinde de asta.

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

**`CLAUDE.md`** (dacă nu există, îl creezi; dacă există, adaugi doar secțiunile de mai jos
care lipsesc, la final). Secțiunea „Salvare” intră doar dacă proiectul are git.

```
# [Numele proiectului]

[Fraza de la întrebarea 1.]

## Continuitate

La începutul fiecărei sesiuni citești DECIZII.md.

Când luăm o decizie sau când te corectez, o scrii în DECIZII.md înainte să mergi mai
departe: un rând de listă, „- AAAA-LL-ZZ: decizia. Motiv: de ce.” Când se schimbă stadiul
proiectului, rescrii „Unde am rămas”.

Nu scrii acolo ce e deja în cod sau în istoricul git, nici detaliile unei singure sesiuni.

## Chei

Cheile API și parolele nu stau în fișierele proiectului. Pe Mac stau în Keychain, pe
Windows în SecretStore (PowerShell SecretManagement). În proiect poate exista cel mult un
`.env.example`, cu numele cheilor și fără valori. Nu afișezi niciodată valoarea unei chei.

## Salvare

La final de etapă, sau după o modificare care merge, faci commit cu un mesaj clar despre
ce s-a schimbat. Dacă proiectul are copie pe GitHub, faci și push. Pentru o etapă mare
lucrezi pe o ramură separată, pe care o unești apoi în `main`.
```

**git** (doar dacă omul a spus da la întrebarea 3 și nu există deja `.git`):
`git init -b main`, plus un `.gitignore` (dacă nu există; dacă există, adaugi doar ce
lipsește din lista obligatorie). Lista obligatorie, pentru orice proiect:

```
.env
.env.*
!.env.example
*.key
*.pem
.DS_Store
Thumbs.db
```

La ea adaugi ce se potrivește proiectului: dependențele și build-urile limbajului
(`node_modules/`, `.next/`, `dist/`, `build/`, `.venv/`, `__pycache__/` și echivalentele)
și folderele cu date brute sau fișiere mari pe care omul le numește (video, exporturi,
date ale clienților).

Dacă la pasul 0 ai găsit fișiere cu chei, verifici că `.gitignore` le exclude înainte de
orice commit, apoi îi spui omului că locul lor e în Keychain (Mac) sau SecretStore
(Windows) și te oferi să-l ajuți să le mute.

Faci primul commit doar dacă omul confirmă. Înainte de commit verifici, cu
`git status --short`, că nu intră niciun `.env`, `*.key` sau `*.pem`.

## Pasul 5. Întrebarea 4: copie pe GitHub

Doar dacă proiectul are git și primul commit e făcut.

„Vrei și o copie privată pe GitHub? Fără ea, proiectul există doar pe discul tău: dacă
discul se strică sau laptopul se pierde, pierzi tot. Repo-ul e privat, îl vezi doar tu.”

Dacă da:

1. Verifici uneltele cu `gh auth status`. Dacă `gh` lipsește, îi dai comanda de instalare
   (Mac: `brew install gh`; Windows: `winget install --id GitHub.cli`), apoi îi ceri să
   ruleze singur `gh auth login` și să revină. Autentificarea o face omul, nu tu.
2. Propui numele repo-ului (numele folderului) și îl creezi **privat**, ca pas separat:
   `gh repo create <nume> --private`. Nu creezi niciodată un repo public din skill-ul ăsta.
3. Legi folderul și trimiți: `git remote add origin <url>`, apoi `git push -u origin main`.
4. Verifici: `git status -sb` arată că ramura e la zi cu `origin/main`. Îi dai omului
   linkul repo-ului.

Dacă nu, mergi mai departe și notezi în „Unde am rămas” că proiectul nu are copie în
afara discului.

## Pasul 6. Testul sesiunii goale

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
- Nu deschizi și nu afișezi fișiere cu chei.
- Nu faci commit sau push fără confirmarea omului și nu creezi repo-uri publice.
