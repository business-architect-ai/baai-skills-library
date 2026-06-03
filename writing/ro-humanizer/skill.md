---
name: ro-humanizer
version: 1.1.0
description: Elimină artefactele AI din text românesc. Self-contained, bazat pe date din 3.3M texte analizate (GPTZero), blader/humanizer v2.7.0 și cercetare NLP 2024-2025.
license: MIT
compatibility: claude-code
allowed-tools: Read
---

# ro-humanizer

Rescrie textul dat astfel încât să nu mai sune a AI. Nu adaugă voce personală - asta e treaba autorului. Elimină pattern-urile detectabile, forțează specificitatea, dezactivează mecanismele AI.

---

## BLOC 1: INVENTAR ARTEFACTE

### 1.1 Cuvinte-semnal lexicale

**Substantive (evită sau înlocuiește cu concret):**
potențial, impact, provocare, oportunitate, perspectivă, inovație, strategie, eficiență, angajament, soluție, transformare, dimensiune, context, abordare, ecosistem, paradigmă, sinergii, peisaj (în sens abstract), tapestry, blueprint, framework (în contexte nontehnice)

**Verbe AI (înlocuiește cu acțiune directă):**
a juca un rol (+ adjectiv), a valorifica, a facilita, a implementa (non-tehnic), a asigura (non-tehnic), a maximiza, a naviga (figurat), a debloca, a îmbrățișa (figurat), a livra (figurat), a genera (valoare/impact), a eleva, a stimula semnificativ

**Adjective-semnal:**
robust, comprehensiv, pivotal, inovativ, holistic, dinamic (figurat), proactiv, strategic (adjectiv pentru orice), granular, scalabil (non-tehnic), nuanțat, multifațetat, eficace, tangibil (când înlocuiește un cuvânt concret)

**Adverbe și fraze-calificator:**
"este esențial că", "în mod crucial", "mai mult decât atât", "în concluzie", "în final", "cu toate că" (la început de paragraf fără contraargument real), "nu în ultimul rând", "este important de menționat că", "este de remarcat că", "de asemenea", "în plus", "în mod semnificativ"

**GPTZero multiplicatori (din 3.3M texte analizate):**
- "joacă un rol semnificativ" = 182x mai frecvent în AI
- "nu numai... ci și" = 40x mai frecvent în AI
- "este esențial că" = 35x mai frecvent în AI
- em dash (—) = 10x mai frecvent în GPT-4o

---

### 1.2 Deschideri toxice

Aceste deschideri identifică AI cu precizie de peste 90% în studiile GPTZero:

- "În lumea de astăzi..." / "In today's world..."
- "În peisajul dinamic al..."
- "Trăim într-o epocă în care..."
- "Este bine cunoscut faptul că..."
- "De-a lungul anilor..."
- "Fie că ești [X] sau [Y]..." (falsă incluzivitate)
- "Hai să explorăm..."
- "Vă invit să..."
- "Imaginați-vă..."
- "Scenariul următor:" (urmat de poveste inventată)

**Înlocuire:** Intră direct. Prima propoziție trebuie să fie o afirmație sau un fapt, nu context.

---

### 1.3 Hedging excesiv

AI-ul se ferește de afirmații categorice. Rezultatul: text care nu spune nimic definitiv.

- "Ar putea fi argumentat că..."
- "Unii ar putea considera..."
- "Există dovezi care sugerează..."
- "În anumite contexte..."
- "Depinde de perspectivă..."
- "Poate că..." (la fiecare a 3-a propoziție)
- "S-ar putea să..." (fără motivare reală)

**Înlocuire:** Afirmă direct. Dacă nu poți afirma fără hedging, omite ideea sau recunoaște explicit incertitudinea ("nu știu" > "s-ar putea să").

---

### 1.4 Familia "nu X, ci Y"

Cea mai recognoscibilă familie AI. Introduce negație inutilă care nu adaugă informație.

| Robotic | Natural |
|---|---|
| "Succesul nu ține de talent, ci de disciplină." | "Succesul ține de disciplină." |
| "Problema nu este tehnologia, ci implementarea." | "Problema este implementarea." |
| "Nu este vorba despre instrument, ci despre utilizator." | "Utilizatorul face diferența." |
| "Nu funcționează pentru că e nou, ci pentru că e prost proiectat." | "Nu funcționează. E prost proiectat." |
| "Aceasta nu înseamnă că sistemul e defect, ci că trebuie ajustat." | "Sistemul trebuie ajustat." |

**Capcana reformulării cosmetice (lecția din v1.0):** A schimba doar vocabularul antitezei nu elimină artefactul. Structura logică „X negat, Y afirmat" este pattern-ul AI, nu cuvintele de legătură. Următoarele reformulări sunt tot artefacte:

| Antiteza originală | Reformulare cosmetică (tot artefact) | Eliminare reală |
|---|---|---|
| „Nu este vorba despre tehnologie, ci despre utilizare." | „Problema nu e tehnologia. Problema e utilizarea." | „Utilizarea face diferența." |
| „Transformarea nu e despre instrumente, ci despre mesaj." | „Transformarea nu e despre instrumente. E despre mesaj." | „Transformarea ține de mesaj." |
| „Nu este un lux, ci o necesitate." | „Nu e lux, e necesitate." | „E necesar." |

**Test rapid:** Dacă propoziția conține o negație urmată imediat de o afirmație care reformulează aceeași idee, e antiteză falsă, indiferent de cuvintele de legătură („ci", „dar", „în schimb", punct urmat de reluare cu „Problema e", „E despre", „Realitatea e"). Taie negația, păstrează doar afirmația.

---

### 1.5 Amplificare artificială

Creează impresia de profunzime prin duplicare semantică.

| Robotic | Natural |
|---|---|
| "Este nu doar eficient, ci și intuitiv." | "Este eficient și intuitiv." |
| "Aceasta nu numai optimizează, ci și reduce costurile." | "Optimizează și reduce costurile." |
| "Nu este un lux, ci o necesitate." | "Este necesar." |

---

### 1.6 Pseudo-explicație

Simulează analiza fără mecanism cauzal real.

- "Motivul este că sistemul este mai eficient." → "Sistemul este mai eficient."
- "Acest lucru se datorează faptului că algoritmul este optimizat." → "Algoritmul este optimizat."
- "Aceasta arată că utilizatorii preferă simplitatea." → "Utilizatorii preferă simplitatea."

---

### 1.7 Importanță artificială

Marchează importanța fără să o demonstreze.

- "Este important de menționat că viteza contează." → "Viteza contează."
- "Este esențial să înțelegem acest aspect." → "Trebuie să înțelegem asta."
- "Feedbackul joacă un rol important." → "Feedbackul corectează erorile." (specific!)

**Regula:** Dacă afirmația are nevoie de "este important că" ca să pară importantă, conținutul nu demonstrează singur asta. Fie specifici mai bine, fie tai.

---

### 1.8 Verbe-paravan (permisiune artificială)

Pun un strat de indirectivitate între subiect și acțiune.

| Paravan | Direct |
|---|---|
| "permite optimizarea procesului" | "optimizează procesul" |
| "ajută la îmbunătățirea performanței" | "îmbunătățește performanța" |
| "contribuie la creșterea eficienței" | "crește eficiența" |
| "facilitează înțelegerea" | "explică" |
| "asigură că" | verifică dacă există alternativă directă |

---

### 1.9 Cuvinte de umplutură structurală

Nu adaugă conținut, marchează doar structura formală. Taie fără înlocuire.

- "în esență" (promite distilare, nu o face)
- "în general" (calificare vagă)
- "în acest context" (redundant dacă contextul e clar)
- "per total" (anunță repetiție)
- "mai mult decât atât" (promite escaladă care nu vine)
- "în concluzie" / "in conclusion" (marchează concluzia în loc să o facă)
- "cu alte cuvinte" (dacă ai nevoie să explici ce ai zis, rescrie propoziția anterioară)

---

### 1.10 Atribuiri vagi (Weasel wording)

- "Studiile arată că..." (care studii?)
- "Experții consideră că..." (care experți?)
- "Industria raportează că..." (ce industrie?)
- "Cercetările indică..." (fără sursă)

**Înlocuire:** Citează specific sau elimină referința. "Un studiu MIT 2024 arată că..." > "studiile arată că..."

---

## BLOC 2: PROBLEME SPECIFICE LIMBII ROMÂNE

### 2.1 Calcuri lingvistice (false friends)

AI-ul gândește în engleză și traduce. Semnele rămân:

| AI (calchiat) | Corect românesc |
|---|---|
| "a naviga provocările" | "a face față provocărilor" |
| "a debloca potențialul" | "a valorifica potențialul" / mai specific |
| "a adresa o problemă" | "a aborda o problemă" |
| "a rula un test" | "a efectua un test" / "a face un test" |
| "a targeta" | "a viza" |
| "a procesa informația" | "a prelucra informația" |
| "experiență de utilizator" (oriunde) | "experiența utilizatorului" |
| "a livra rezultate" | "a obține rezultate" / "a produce rezultate" |
| "a îmbrățișa schimbarea" | taie sau reformulează |
| "în peisajul dinamic al" | taie complet |

---

### 2.2 Topică nefirească (SVO rigid din engleză)

Româna are ordine liberă a cuvintelor. AI-ul forțează SVO (subiect-verb-obiect) din engleză.

- AI: "Acest lucru joacă un rol crucial în modelarea viitorului."
- Om: "Asta contează. Schimbă tot."

**Semne:** Lipsă inversiune naturală, absența emfazei prin dislocare, propoziții care niciodată nu încep cu verbul.

---

### 2.3 Register mismatch

AI-ul alege implicit formalul, care sună straniu pe social media sau în comunicare directă.

- "Dumneavoastră" în context informal → "tu"
- "a binevoi" → "a vrea"
- Vocabular birocratic în text personal

**Verificare:** Textul trebuie să sune ca registrul platformei/contextului, nu ca un comunicat de presă al Guvernului.

---

### 2.4 Pierderea idiomurilor românești

AI-ul înlocuiește expresiile idiomatice cu parafrazări plate.

| AI | Om |
|---|---|
| "a face o greșeală" | "a da cu bâta în baltă" (dacă se potrivește) |
| "a deveni frustrat" | "a-i sări muștarul" |
| "a absenta nemotivat" | "a trage chiulul" |

**Nota:** Nu forța idiomuri dacă nu se potrivesc. Dar dacă autorul le-ar fi folosit în mod natural, restaurează.

---

### 2.5 Title Case greșit

În română, titlurile au DOAR primul cuvânt cu majusculă (și substantivele proprii).

- Greșit (engleză): "Ghid Complet Pentru Scrierea Autentică"
- Corect (română): "Ghid complet pentru scrierea autentică"

---

### 2.6 Inflație retorică amplificată

Expresii care în engleză sunt moderat pompoase devin ridicole în română:

- "bogat patrimoniu cultural" (sună ca pliant turistic de primărie)
- "se ridică ca o mărturie a" (nimeni nu vorbește așa)
- "moment de cotitură" (acceptabil izolat, toxic în densitate)

---

## BLOC 3: CE SĂ NU ATINGI (FALSE POSITIVES)

**Nu tăia când:**
- Vocabularul academic e legitim în context academic (un articol de specialitate poate folosi "facilitate" corect)
- Propoziția formală aparține stilului deliberat al autorului, nu AI-ului
- Un singur "tapestry" sau un singur em dash nu e dovadă - densitatea e problema
- Autorul e un vorbitor de limbă nativă non-română - pattern-urile pot fi ale lui, nu ale AI-ului
- Gramatica perfectă poate veni din editare umană sau din Grammarly

**Regula densității:** Un artefact izolat nu e tell. Dacă același pattern apare de 3+ ori în 200 de cuvinte, e AI. Tratează densitatea, nu apariția izolată.

---

## BLOC 4: PROCESUL

Execuție în 4 etape. Nu le comprima, nu le omite.

**Etapa 1 - Scanare**
Citește textul o dată și identifică:
- Deschideri toxice
- Cuvinte-semnal de mare frecvență
- Pattern-uri structurale (uniformitate ritmică, sandwich, regula lui 3)
- Calcuri lingvistice (dacă textul e în română)
- Register mismatch

**Etapa 2 - Draft rewrite**
Rescrie cu aceste reguli:
- Înlocuiește, nu șterge pur și simplu
- Em dash → virgulă sau reformulează propoziția
- Deschideri toxice → intră direct în subiect
- Verbe-paravan → verb direct
- "nu X ci Y" → afirmația directă
- Variază lungimea propozițiilor (scurt-lung alternant)
- Forțează specificitate oriunde e posibil

**Etapa 3 - Audit intern**
Pune întrebarea: "Ce mai sună a AI?"
Răspunde cu 3-5 bullets scurte. Fii sincer. Dacă ceva a rămas robotic, notează-l.

**Etapa 4 - Final rewrite**
Adresează auditul. Versiunea finală integrează corecțiile din etapa 3.

---

## OUTPUT LIVRAT

1. **Draft** (cu notare schimbărilor majore)
2. **Audit intern** (bullets "ce mai era AI")
3. **Versiunea finală**
4. **Sumar schimbări** (categorii de artefacte eliminate, cifre dacă relevant)

---

## INVOCARE

```
/ro-humanizer [text sau cale fișier]
```

Dacă e cale de fișier: citește fișierul, procesează textul, afișează output-ul.

---

## LIMITĂ CLARĂ

ro-humanizer face textul să nu mai sune a AI. **Nu adaugă voce personală** - asta e treaba dm-humanizer sau dm-writing-voice. Rezultatul este un text neutru, uman, fără pattern-uri detectabile.
