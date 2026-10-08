---
name: sus-panel
compatibility: claude-code-only
license: MIT
description: "Test de uzabilitate cu utilizatori simulați. Te întreabă cine se uită la material, construiește 3-5 persona diferite între ele (sau până la 10 în panel lărgit, opțional cu 2-3 repetări pe persona), le pune să parcurgă materialul ca niște oameni reali (fiecare ca subagent separat), apoi scoate un raport cu frecările găsite și, unde se potrivește, scorul SUS (System Usability Scale) calculat de un script. Merge pe site live, fișier local, text sau PDF și capturi de ecran. Se declanșează cu /sus-panel sau la formulări ca „testează asta cu utilizatori”, „ce ar zice un client care vede pagina”, „scor SUS”, „test de uzabilitate”, „fă un panel de utilizatori”."
---

# SUS panel: test de uzabilitate cu utilizatori simulați

Rulezi un mic test de uzabilitate: câțiva oameni simulați, fiecare cu alt profil, parcurg
un material și spun sincer unde s-au împiedicat. La final primești frecările ordonate după
gravitate și, pentru interfețe și ghiduri, scorul SUS.

Tot ce urmează e construit împotriva unui singur risc: **utilizatorul simulat care e, de fapt,
de partea autorului.** Unul care ghicește intenția, găsește drumul fericit și laudă. Oamenii
reali citesc pe sărite, înțeleg greșit butoanele și pleacă atunci când se enervează.

## Două straturi, ținute separat

- **Stratul persona** (subagent): trăiește sesiunea și scrie reacția brută, la persoana întâi,
  cu vorbele și cunoștințele omului respectiv. Completează chestionarul la final. Nu analizează.
- **Stratul analist** (tu, în sesiunea principală): transformi reacțiile în raport. Severitățile,
  termenii de UX și recomandările stau doar aici, niciodată în gura persona.

Un om care nu știe ce e un „CTA” nu scrie „CTA-ul nu e vizibil”. Scrie „n-am găsit unde să apăs”.

## Pasul 1. Ce testăm

Află, întrebând doar ce lipsește (o întrebare pe mesaj):

1. **Materialul și suprafața:**
   - `web`: URL live
   - `local`: fișier HTML sau aplicație de pe mașina asta
   - `text`: articol, ghid, document (Markdown, PDF, text lipit)
   - `capturi`: screenshot-uri sau machetă, nimic de apăsat
2. **Tipul materialului**, care decide chestionarul:
   - **interfață** (site, aplicație, formular, landing page) → SUS
   - **ghid de urmat** (tutorial, instrucțiuni pas cu pas) → SUS, cu „ghidul” în loc de „sistemul”
   - **text de citit** (articol, newsletter, pagină de opinie) → **fără SUS**, test de înțelegere
3. **Sarcina**, formulată ca obiectiv al omului, nu ca specificație de test.
   Bine: „programează-te la o consultație”. Rău: „testează fluxul de programare, inclusiv
   validarea câmpului de telefon”. Dacă nu există o sarcină anume: „uită-te și spune ce crezi”.
4. **Doar pentru text de citit:** ce ar trebui să rețină cititorul, în 1-3 propoziții. Persona
   nu află asta niciodată, îl folosești doar la analiză.
5. **Mărimea panelului.** Dacă omul nu a cerut altceva, mergi pe varianta standard și nu mai
   întrebi. Altfel, i le prezinți pe toate trei:
   - **standard** (implicit): 3-5 persona, câte o rulare fiecare. Găsește majoritatea
     problemelor la un cost rezonabil.
   - **panel lărgit**: 6-10 persona, câte o rulare fiecare. Acoperă mai multe tipuri de public,
     dar câștigul scade repede: persona simulate vin din același model și tind să se împiedice
     în aceleași locuri.
   - **repetări**: fiecare persona rulează de 2 sau 3 ori, independent. Arată dacă scorul unei
     persona e stabil sau e zgomot și care frecări apar la fiecare rulare. Se poate combina cu
     panelul lărgit.

### Costul, înainte de panel lărgit sau repetări

Înainte să pornești o variantă care nu e standard, spune-i omului câte rulări înseamnă
(persona × repetări) și o estimare grosieră de tokeni, apoi **așteaptă confirmarea**. Reper
măsurat: o persona pe un ghid de ~150 de rânduri a consumat ~90.000 de tokeni, iar pe o
aplicație web mare, explorată 30-40 de pași, 100.000-140.000 de tokeni și ~2 minute. Un site
cu mult conținut pe pagină costă mai mult. Spune că e o
estimare, nu o promisiune. Pe `web`, adaugă și timpul: rulările merg una după alta.

## Pasul 2. Persona

Caută întâi un folder `persone/` în proiectul curent. Dacă are persona potrivite publicului
materialului, arată-i omului tabelul din `persone/README.md` și întreabă-l pe care le folosim.

Dacă nu există sau nu se potrivesc, rulează onboardingul din `references/onboarding.md`:
întrebări una câte una despre cine se uită la material. Apoi propune atâtea persona câte cere
mărimea panelului (3-5 la standard și la repetări, 6-10 la panel lărgit), după
`references/persona-sablon.md`, diferite intenționat între ele, și **așteaptă aprobarea**
înainte să le scrii pe disc. Nu inventa date despre public. Ce nu știi, întrebi.

## Pasul 3. Briefingul curat

Briefingul e tot ce află persona. Scrie-l ca pentru un necunoscut intrat de pe stradă.

Include DOAR:
- încadrarea: *„Cineva te-a rugat să încerci ceva și să spui sincer ce crezi: ce e confuz,
  ce lipsește și dacă l-ai folosi cu adevărat.”*
- sarcina, cu vorbele omului (de la Pasul 1);
- unde se uită (URL, cale de fișier, textul sau capturile);
- o notă că poate fi neterminat, dacă e o machetă sau un prototip.

EXCLUDE mereu:
- ce vrea autorul să obțină, publicul țintă, poziționarea;
- drumul fericit, numele funcționalităților, termenii interni;
- pentru texte: mesajul pe care ar trebui să-l rețină cititorul;
- orice din conversația cu autorul.

Dacă simți nevoia să explici cum funcționează materialul, oprește-te. Exact explicația aia nu
o primește un om real.

## Pasul 4. Rularea persona

Fiecare persona e un **subagent separat** (Agent tool, tip general-purpose). Niciodată în
sesiunea principală: ar ști tot ce știi tu despre material.

Promptul subagentului, în ordinea asta:
1. **Identitatea:** conținutul complet al fișierului de persona, cu tot cu secțiunea
   „Ce știu și ce nu știu”. Plus: *„Ești omul ăsta pe toată durata sesiunii. Rămâi în
   personaj orice ar fi. Nu te descrie niciodată ca AI, tester sau model.”*
2. **Briefingul** de la Pasul 3.
3. **Regulile de fidelitate** de mai jos, cuvânt cu cuvânt.
4. **Instrucțiunile de suprafață** pentru suprafața aleasă.
5. **Formatul de răspuns:** conținutul din `references/reactie-persona.md`, cu varianta de
   chestionar potrivită tipului de material.

### Reguli de fidelitate (le dai subagentului cuvânt cu cuvânt)

- Reacționezi doar la ce ai efectiv în față. Nu ghicești ce „probabil” face un buton: apeși
  și vezi, sau eziți cum ai ezita în realitate.
- N-ai citit instrucțiuni, documentație sau ghiduri prin care nu ai fost obligat să treci.
  Citești pe sărite.
- Dacă ceva e confuz, rămâi confuz. Nu te prinzi mai repede decât te-ai prinde în realitate.
  Spune presupunerea greșită pe care ai face-o.
- **Plafonul de cunoaștere.** Folosești doar cuvinte, mărci și comparații pe care omul ăsta le
  știe (vezi „Ce știu și ce nu știu”). Ce e în afara lui descrii cu vorbele tale, fără să
  numești o tehnologie pe care n-ai cunoaște-o și fără să explici cum funcționează.
- **Autenticitate înaintea completitudinii.** Mergi doar cât de departe ar merge omul ăsta. Dacă
  te-ai plictisi sau te-ai enerva și ai pleca, pleci și te oprești acolo. Nu explorezi fiecare
  ecran ca să „termini testul”. Nu reacționezi la ce n-ai apucat să vezi.
- Ai toleranță mică la frecare. Dacă ai renunța, renunți și spui unde și de ce. Abandonul e un
  rezultat, nu un eșec.
- Nu ești îngăduitor cu autorul. Nu îndulcești problemele din politețe. Nu inventezi laude.
- **Nu ești analistul.** Nu ordonezi probleme, nu dai severități, nu scrii secțiuni de tip
  „ce a mers / ce n-a mers”. Spui doar ce ai trăit, cu vocea ta.
- Nu creezi conturi reale, nu introduci date personale sau de plată reale. Dacă fluxul ți le
  cere, asta e o frecare: reacționezi la ea și te oprești acolo.

### Instrucțiuni de suprafață

**web**: încarcă uneltele Playwright (ToolSearch, `playwright`). Pornește dintr-o sesiune
curată, fără login sau cookie-uri rămase de la o rulare anterioară, altfel persona sare peste
ecranele de intrare și reacția e falsă. Navighezi și apeși cum ar face persona. Pentru persona
pe telefon, redimensionează fereastra la 390×844 înainte de navigare și reacționezi ca pe
telefon: degetul mare, text mic, derulare.

**local**: un HTML local îl deschizi în browser, ca la `web`. Pentru o aplicație nativă
folosești uneltele de control al calculatorului, dacă sunt disponibile, altfel spui că nu poți.

**text**: citești DOAR fișierul sau textul primit, ca pe o pagină tipărită. Nu deschizi alte
fișiere la care trimite, nu rulezi comenzi, nu modifici nimic. Dacă textul te trimite la alt
document, reacționezi ca un om care nu-l are în față. Citești cum ar citi omul ăsta: pe sărite
dacă e grăbit, de la cap la coadă doar dacă e genul. Te oprești acolo unde te-ai opri.

**capturi**: nu ai nimic de apăsat. Reacționezi la imagini și spui explicit unde ar trebui să
încerci pe viu ca să poți judeca.

### Paralel sau pe rând

- `text` și `capturi`: lansezi toți subagenții în același mesaj, în paralel.
- `web` și `local`: **pe rând**, unul după altul. Toți folosesc același browser și și-ar fura
  taburile între ei.

Nicio persona nu vede reacția alteia.

### Repetări

Fiecare rulare e un **subagent nou**, cu exact același prompt. Nu-i spui că e o repetare și nu
îi arăți ce a răspuns la rularea anterioară: tocmai independența rulărilor face repetarea
utilă. În blocul JSON, toate rulările aceleiași persona poartă **același nume**, ca scriptul să
le poată grupa. Pe `web`, fiecare rulare pornește tot dintr-o sesiune curată.

## Pasul 5. Scorul (doar pentru interfețe și ghiduri)

Din fiecare reacție extrage blocul JSON cu cele 10 răspunsuri SUS. Le pui într-un fișier,
o persona pe linie (vezi formatul din `tools/sus_scor.py`), și rulezi:

```bash
python3 <calea skillului>/tools/sus_scor.py raspunsuri.json
```

**Nu calcula scorul de mână.** Scriptul aplică formula, verifică răspunsurile și dă media,
împrăștierea și nota. La repetări, grupează rulările după numele persona, arată intervalul
dintre rulări și semnalează persona al căror scor variază cu mai mult de 15 puncte. Media
panelului se face pe persona, nu pe rulări, ca o persona rulată de trei ori să nu cântărească
triplu. Dacă scriptul refuză un set de răspunsuri, spune-i omului care și de ce,
nu „repara” tu valorile.

Dacă un subagent a abandonat înainte să poată judeca materialul, completează totuși
chestionarul (așa cum face și un om real după un test ratat). Răspunsurile lui intră în scor.

## Pasul 6. Raportul

Construiește-l după `references/raport-sablon.md`. Reguli ferme:

- **Ordonezi doar ce au trăit persona.** Nu inventezi frecări pe care nu le-au atins și nu dai
  credit unor părți la care n-au ajuns. Dacă au plecat devreme, raportul e scurt: asta e
  concluzia, nu un gol de umplut.
- **Vocea rămâne în carantină.** Citatele persona stau neșlefuite, în secțiunea lor.
- **Ce au găsit mai multe persona independent are încredere mai mare.** Separi asta clar de
  ce a găsit una singură. Numeri persona, nu rulări: aceeași frecare găsită de o persona în
  trei rulări înseamnă tot o singură persona.
- **La repetări, separi frecările stabile de cele întâmplătoare.** O frecare e stabilă pentru o
  persona dacă apare în majoritatea rulărilor ei (2 din 2, 2 din 3, 3 din 3). Una apărută
  într-o singură rulare din mai multe o marchezi ca întâmplătoare. Persona cu scor instabil
  (semnalate de script) le pomenești explicit și nu le iei scorul drept concluzie.
- **Scorul SUS vine cu avertismentul lui**, mereu: e orientativ, modelele tind să-l umfle,
  iar valoarea testului stă în frecări, nu în cifră.
- **Pentru text de citit**, compari ce a reținut fiecare persona cu mesajul de la Pasul 1.4.

Salvează raportul în proiect, în `teste-utilizatori/AAAA-LL-ZZ-<2-3-cuvinte>.md` (creezi
folderul dacă nu există), și spune-i omului calea. Rezumatul tău din chat: două-trei
propoziții, raportul e livrabilul.

## Reguli tari

- Intenția autorului nu intră niciodată în briefing.
- Persona rulează doar ca subagenți, niciodată în sesiunea principală.
- Persona nu scrie analiza. Analistul nu pune în gura persona cuvinte pe care ea nu le-ar ști.
- Scorul SUS îl calculează scriptul, nu modelul.
- Pe `web`, fiecare rulare pornește dintr-o sesiune curată, fără login sau cookie-uri moștenite.
- Nu scrii fișiere de persona fără aprobarea omului. Când adaugi sau schimbi o persona,
  actualizezi rândul ei din `persone/README.md`.
- Spui limitele: utilizatorii simulați sunt un filtru înainte de testul cu oameni reali, nu un
  înlocuitor al lui. Recomanzi mereu, la final, un test cu 3-5 oameni reali pe frecările găsite.
