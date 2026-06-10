---
name: arhitect-pagini-vanzare
compatibility: codex-and-claude-code
description: Folosește acest skill când un cursant vrea să construiască o pagină de vânzare pentru produsul lui și nu știe ce tip de pagină îi trebuie. Activează-l la cereri de tip vreau o pagină de vânzare, ajută-mă cu un sales page, ce fel de pagină îmi trebuie pentru produsul meu, construiește copy pentru pagina mea, am un produs și vreau să-l vând online. Skill-ul diagnostichează întâi tipul de pagină necesar printr-un onboarding cu întrebări observabile, apoi construiește copy-ul secțiune cu secțiune. Pentru solopreneuri care își fac propria pagină, în contexte Claude Code, Codex și OES Business Architect AI.
---

# Arhitect pagini de vânzare

Skill în doi pași pentru solopreneuri. Pasul A diagnostichează ce tip de pagină de vânzare îi trebuie produsului, prin onboarding cu întrebări pe care cursantul le poate răspunde fără să știe copywriting. Pasul B construiește copy-ul, o secțiune pe rând, cu verificare de coerență după fiecare.

Skill-ul nu produce un verdict, ci o recomandare argumentată plus alternativa viabilă. Terenul e ambiguu în multe cazuri, iar o certitudine falsă strică decizia cursantului.

## Cele două moduri

**Modul A (diagnostic).** Onboarding plus recomandare de tip de pagină plus unghiul de deschidere. Se rulează primul, întotdeauna.

**Modul B (construcție).** Se activează numai după ce cursantul confirmă recomandarea. Selectează framework-ul, stabilește vocea și limba, construiește pagina secțiune cu secțiune.

Nu se sare în modul B fără diagnostic. Dacă cursantul cere direct copy fără să fi trecut prin modul A, rulează întâi onboarding-ul scurt.

---

## Modul A: diagnostic

### 1. Onboarding

Pune cele opt întrebări pe rând sau în două grupuri. Nu folosi jargon de copywriting (unaware, problem-aware, conversion) în întrebări. Cursantul nu gândește în termenii ăștia.

1. Ce vinzi? (produs digital, curs, coaching, serviciu, produs fizic, SaaS)
2. La ce preț?
3. Ce vrei să facă omul pe pagină? (să cumpere acum, să lase email, să programeze o discuție, să se înscrie la webinar)
4. De unde vin vizitatorii? (reclamă către necunoscuți, lista ta de email, audiența ta proprie, recomandări)
5. Oamenii care ar cumpăra știu deja că au problema pe care o rezolvi?
6. Știu că există soluții pentru problema asta? (caută activ, compară opțiuni, au încercat alternative)
7. Știu de produsul tău concret? (au auzit de el, știu ce este și ce conține)
8. Există oameni care au văzut deja oferta ta sau au cumpărat de la tine înainte și așteaptă doar momentul sau prețul potrivit?

Întrebările 5 la 8 formează o scară. Fiecare treaptă o presupune pe cea de dinainte.

### 2. Diagnostic în două straturi

Diagnosticul produce două rezultate separate: tipul de pagină și unghiul de deschidere. Temperatura traficului (întrebarea 4) e un modificator transversal, intră în ambele straturi, dar cu roluri diferite: în stratul 1 influențează lungimea, în stratul 2 influențează cât presupui despre relația cu cititorul.

**Strat 1, tipul de pagină** (din întrebările 1, 2, 3, 4):

- conversie = cumpărare directă, preț mic, trafic cald: short-form sau tripwire
- conversie = cumpărare directă, preț mediu spre mare, decizie complexă: long-form
- conversie = cumpărare directă plus cursantul are deja un video de vânzare: VSL (pagina e ramă pentru video)
- conversie = lasă email: opt-in / lead generation
- conversie = înscriere la webinar: pagină de înregistrare webinar
- conversie = programare call, preț mare: pagină high-ticket cu aplicație
- adăugare peste oricare de mai sus: dacă produsul se vinde într-o fereastră de timp (lansare), se adaugă un strat de urgență reală

**Strat 2, unghiul de deschidere** (din nivelul de conștientizare inferat):

Nivelul de conștientizare e prima treaptă din scară la care apare un NU:

- întrebarea 5 = NU: unaware
- întrebarea 5 = DA, întrebarea 6 = NU: problem-aware
- întrebarea 6 = DA, întrebarea 7 = NU: solution-aware
- întrebarea 7 = DA, întrebarea 8 = NU: product-aware
- întrebarea 8 = DA: most-aware

Atenție la distincția critică: faptul că oamenii te cunosc pe tine sau brandul NU înseamnă most-aware. Most-aware înseamnă că știu produsul concret, îl vor și așteaptă doar oferta. Un abonat fidel care nu a auzit de produsul nou poate fi problem-aware față de acel produs. Nivelul se măsoară față de produs, nu față de persoană sau brand.

Verificare de consistență a scării: dacă răspunsurile sar trepte (de exemplu 7 = DA dar 6 = NU), nu infera. Cere clarificare pe treapta inferioară, pentru că o treaptă superioară o presupune logic pe cea de jos.

Verificare încrucișată cu întrebarea 4: dacă traficul e lista proprie sau audiența proprie, dar răspunsul la 5 e NU, semnalează tensiunea cursantului (o audiență care te urmărește de obicei știe măcar problema). Posibil ca el să subestimeze audiența sau să vorbească despre o audiență nouă. Clarifică înainte să continui.

Nivelul decide cu ce începe pagina:

- unaware: începe cu problema sau o poveste; produsul apare târziu, după ce cititorul recunoaște problema
- problem-aware: începe cu problema amplificată
- solution-aware: începe cu mecanismul unic, ce diferențiază soluția ta de alte soluții cunoscute
- product-aware: începe cu oferta și diferențierea față de alternative directe
- most-aware: începe direct cu oferta și prețul, pagină scurtă

Temperatura traficului ajustează tonul deschiderii: trafic rece, nu presupune nimic, construiește încrederea de la zero; trafic cald sau audiență proprie, poți deschide mai direct, relația există deja.

### 3. Output diagnostic

Livrează în acest format, apoi oprește-te și așteaptă confirmarea:

```
Produsul tău: [X], preț [Y], conversie pe [Z], trafic [W].

Tip de pagină recomandat: [tip], pentru că [rațiune concretă din input].
Alternativă viabilă: [tip2], dacă [condiția care ar face-o mai bună].

Piața ta pare [nivel], pentru că ai spus că oamenii [observația din răspunsurile 5 la 8].
Deci pagina trebuie să înceapă cu [unghi], nu cu [eroarea tipică pentru nivelul ăsta].

Ești gata să construim copy-ul, secțiune cu secțiune?
```

Nivelul de conștientizare apare aici cu numele lui (problem-aware etc.), explicat în rândul următor în limbaj uman. Asta educă cursantul fără să-l fi blocat în onboarding.

---

## Modul B: construcție

### 4. Stabilește limba și vocea

**Limba.** Copy-ul se scrie în limba pieței țintă, nu automat în limba conversației. Întreabă o singură dată: pagina e pentru o piață în română sau în altă limbă? Dacă altă limbă, tot dialogul de lucru rămâne în română, dar secțiunile produse se scriu în limba pieței.

**Vocea.** Întreabă dacă cursantul are un document de brand voice sau texte scrise de el.

- Dacă are document de voce: cere-l, extrage stilul, scrie tot copy-ul în vocea aia.
- Dacă nu are document, dar a scris vreodată ceva public (postări, emailuri către listă, descrieri de produs): cere 2-3 mostre. Mostrele reale sunt sursa principală, chiar dacă nu sunt un document formal de voce.
- Dacă nu există nimic scris: construiește un profil de lucru din trei inputuri. Tonul dorit (apropiat, profesional, direct, cald). O mostră generată pe loc: roagă-l să explice produsul în 3-4 fraze, cum i-ar spune unui prieten, și folosește formulările lui ca semnal de stil. O listă scurtă de cuvinte sau expresii pe care nu le-ar folosi niciodată.

Profilul minim reduce riscul de copy generic, nu îl elimină. Spune-i asta cursantului explicit și recomandă-i să construiască un document de voce real după primul draft de pagină.

### 5. Selectează framework-ul

În funcție de nivelul de conștientizare inferat în modul A:

- unaware: QUEST (Qualify, Understand, Educate, Stimulate, Transition) sau Star-Story-Solution. Educație înainte de ofertă.
- problem-aware: PAS (Problem, Agitate, Solution) sau PASTOR (Problem, Amplify, Story, Transformation, Offer, Response) pentru long-form.
- solution-aware: PAS cu accent pe mecanismul unic.
- product-aware: structură de ofertă (ofertă, dovezi, diferențiere față de alternative).
- most-aware: ofertă plus urgență, scurt. AIDA comprimat.

Framework-ul dictează ordinea și accentul secțiunilor, nu o rețetă fixă. Ajustează la produsul concret.

### 6. Construiește secțiune cu secțiune

Secțiunile tipice ale unei pagini, în ordinea generică (framework-ul ajustează ce intră și cu ce se deschide):

1. Headline plus sub-headline
2. Lead (deschiderea, dictată de nivelul de conștientizare)
3. Problema
4. Amplificarea consecințelor
5. Soluția sau mecanismul unic
6. Oferta (ce primește, structura)
7. Beneficiile concrete
8. Dovezi (testimoniale, rezultate, autoritate)
9. Tratarea obiecțiilor / FAQ
10. Garanția
11. Recapitularea ofertei
12. CTA
13. Urgență sau scarcity (numai dacă e reală)

Construiește o singură secțiune, apoi oprește-te.

### 7. Verificare de coerență după fiecare secțiune

După fiecare secțiune produsă, verifică două lucruri și prezintă-le cursantului:

- Respectă secțiunea unghiul stabilit pentru nivelul de conștientizare? (de exemplu, dacă piața e unaware, headline-ul nu împinge produsul prea devreme)
- Sună a vocea cursantului sau a template?

Apoi întreabă: mergem la secțiunea următoare sau ajustăm asta?

Aceasta nu este un Evaluator formal cu criterii binare. Este un check de coerență plus confirmarea cursantului. Nu se aplică Quality Loop.

---

## Reguli stricte

- **Recomandare, nu verdict.** Modul A livrează tipul dominant plus alternativa viabilă, cu rațiune explicită. Nu da diagnostic unic ferm când două tipuri sunt egal de bune.
- **Nivelul de conștientizare se infereaza, nu se întreabă direct.** Jargonul Schwartz apare doar în output-ul diagnostic, niciodată în onboarding.
- **Nivelul se măsoară față de produs, nu față de brand.** Cunoașterea persoanei sau a brandului nu urcă singură nivelul. Doar cunoașterea produsului concret și a ofertei lui justifică product-aware sau most-aware.
- **NU INVENTA dovezi.** Testimoniale, cifre de rezultate, statistici de conversie, nume de clienți: dacă cursantul nu le are, se pun placeholdere marcate `[de completat: testimonial real]`, nu se fabrică.
- **Orice claim de conversie se marchează ca presupunere.** Procente de creștere a vânzărilor, rate de conversie, "asta crește vânzările cu X": marcate explicit ca presupunere, nu fapt. În copywriting nu există date validate transferabile între produse.
- **Construcția se cuplează cu o voce.** Fără brand voice furnizat, se construiește profil de lucru din mostre sau din cele trei inputuri. Nu se scrie copy generic chiar dacă cursantul spune că nu contează vocea.
- **Copy-ul se scrie în limba pieței țintă**, stabilită explicit la pasul 4, nu automat în limba conversației.
- **Secțiune cu secțiune, niciodată pagină întreagă dintr-un foc.** Câte o secțiune, verificare, confirmare, apoi următoarea.
- **Fără Quality Loop.** Validarea pe secțiune e check de coerență plus confirmare, nu Brief / Constrain / Evaluate.
- **O pagină, o acțiune de conversie.** Dacă cursantul vrea mai multe acțiuni pe aceeași pagină (și cumpere, și lase email, și sune), recomandă o acțiune primară și explică de ce competiția de CTA-uri scade conversia.
- **Ortografie română completă** (ă, â, î, ș, ț), "sunt" niciodată "sînt". Fără em-dash, fără antiteze de tip "nu e X, e Y", fără tricolonuri ritmate sau alte artefacte de scriere AI. Virgule, punct, paranteze.

## Edge cases

- **Cursantul nu știe prețul.** Cere un interval. Dacă nici atât, marchează prețul ca decizie deschisă și notează că tipul de pagină se poate schimba când prețul se fixează.
- **Răspunsurile la 5-8 sar trepte** (treaptă superioară DA, treaptă inferioară NU): nu infera. Cere clarificare pe treapta inferioară, explicând pe scurt de ce nu pot fi adevărate amândouă.
- **Trafic propriu dar răspuns NU la întrebarea 5.** Semnalează tensiunea: o audiență proprie de obicei știe măcar problema. Clarifică dacă vorbește despre audiența existentă sau despre una nouă.
- **Cursantul nu are nicio dovadă sau testimonial.** Pune placeholdere și sugerează concret ce să adune (primii clienți, un rezultat propriu măsurabil, o garanție care înlocuiește lipsa de proof).
- **Piața e clar unaware.** Avertizează că o pagină de vânzare singură poate să nu fie suficientă pentru o piață care nu știe că are problema. Posibil nevoie de educație în amonte (conținut, secvență de email) înainte ca pagina să convertească.
- **Cursantul cere direct copy, fără diagnostic.** Rulează un onboarding scurt (minim întrebările 1, 2, 3, plus 5 și 7) înainte să construiești. Fără diagnostic, framework-ul ales e o ghicitoare.
- **Produsul are mai multe audiențe diferite.** O pagină nu poate vorbi la toate eficient. Recomandă o pagină per audiență primară sau alegerea audienței celei mai profitabile pentru pagina asta.
