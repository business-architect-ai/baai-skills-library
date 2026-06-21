---
name: web-section-composer
description: Compune, repară și auditează secțiuni de pagini web pentru claritate, ierarhie vizuală, densitate eficientă, responsive design, text scanabil și folosire corectă a imaginilor. Folosește pentru landing pages, site-uri de prezentare, pagini de servicii, SaaS, ecommerce, articole, documentație, portofolii și dashboard-uri când construiești sau îmbunătățești hero, beneficii, features, proces, testimoniale, pricing, FAQ, galerie, articol, docs sau secțiuni de aplicație.
---

# Web Section Composer

Construiește secțiuni web după jobul lor, nu după un șablon decorativ. O secțiune bună are un singur scop clar, folosește spațiul proporțional cu importanța conținutului și rămâne ușor de scanat pe desktop și mobil.

## Principiul central

Înainte să construiești o secțiune, decide:

1. **Tipul paginii**: landing page, service, SaaS, ecommerce, articol, docs, portofoliu, dashboard.
2. **Jobul secțiunii**: orientare, explicare, convingere, comparație, dovadă, explorare, acțiune.
3. **Densitatea**: compact, standard sau immersive.
4. **Rolul imaginii**: primary, supporting, proof, decorative sau none.
5. **Acțiunea așteptată**: citește mai departe, compară, apasă CTA, contactează, cumpără, învață.

Nu crea secțiuni doar ca să umpli pagina. Dacă secțiunea nu adaugă claritate, încredere sau acțiune, comprim-o, combin-o sau elimin-o.

## Workflow obligatoriu

1. Identifică tipul paginii și audiența. Dacă lipsesc, inferă conservator din context.
2. Alege familia de secțiune potrivită pentru job. Pentru detalii, citește [section-taxonomy.md](references/section-taxonomy.md).
3. Alege modul de pagină. Pentru diferențe între LP, SaaS, ecommerce, docs, articole etc., citește [page-modes.md](references/page-modes.md).
4. Setează densitatea și spațierea. Pentru reguli precise, citește [density-and-spacing.md](references/density-and-spacing.md).
5. Scrie copy scanabil: heading clar, text scurt, CTA proporțional cu secțiunea. Pentru reguli, citește [copy-and-hierarchy.md](references/copy-and-hierarchy.md).
6. Construiește layout responsive, cu mobile ca test de economie a spațiului. Pentru patternuri, citește [responsive-patterns.md](references/responsive-patterns.md).
7. Aplică regulile de media web. Dacă există skillul `imagini-web-lp` / `media-web`, folosește-l pentru imagini și video.
8. Auditează secțiunea: claritate, densitate, ierarhie, mobile, media și accesibilitate. Pentru audit manual, citește [audit-checklist.md](references/audit-checklist.md). Pentru HTML static, rulează scriptul inclus.

## Reguli de compoziție

- O secțiune are un singur job principal. Nu combina educare, pricing, testimoniale și CTA major în aceeași secțiune decât dacă structura le separă clar.
- Cardurile sunt pentru elemente repetabile. Nu pune un singur text într-un card doar ca să pară design.
- Hero-ul nu trebuie să fie full-screen implicit. Folosește 100vh doar când experiența vizuală merită spațiul.
- Nu alterna text-stânga/imagine-dreapta mecanic. Alternanța trebuie să clarifice, nu să decoreze.
- Nu pune text lung peste imagini aglomerate. Dacă imaginea concurează cu textul, separă-le sau întunecă/curăță fundalul.
- Nu folosi carusel pentru informație critică. Caruselul ascunde conținut și cere efort inutil.
- Nu folosi spațiere mare ca înlocuitor pentru ierarhie. Aerul trebuie să organizeze, nu să mascheze conținut slab.
- Pe mobile, verifică lungimea reală a secțiunii. Dacă un beneficiu de 2 rânduri consumă un ecran întreg, densitatea e greșită.
- În dashboard/app, densitatea utilă bate storytelling-ul. În landing pages, claritatea și dovada bat ornamentul.
- Imaginea trebuie să aibă rol: arată produsul, explică mecanismul, dovedește rezultatul sau creează context. Dacă doar umple loc, elimin-o.

## Densitate rapidă

| Densitate | Când o folosești | Semne că e greșită |
|---|---|---|
| Compact | FAQ, trust strip, feature list, docs, dashboard | Pare înghesuit, nu se disting grupurile |
| Standard | Hero, beneficii, proces, testimoniale, service pages | Prea mult text pe carduri, spațiere inconsistentă |
| Immersive | Portofoliu, produs vizual, campanie, galerie, hero editorial | Ocupă mult spațiu fără informație sau emoție reală |

## Patternuri implicite

- **Hero**: H1 clar, subheadline util, CTA principal, dovadă scurtă, media relevantă. Evită sloganul vag.
- **Beneficii**: 3-6 elemente, titluri concrete, text de 1-2 rânduri. Dacă sunt multe, folosește grupare sau tabel.
- **Proces**: 3-5 pași, numerotați, fiecare cu rezultat clar. Timeline doar când ordinea contează.
- **Features**: arată ce face produsul, dar leagă fiecare feature de un beneficiu sau caz de utilizare.
- **Proof**: testimoniale, logo-uri, cifre, capturi reale. Dens și credibil, nu decorativ.
- **Pricing/comparison**: scanează vertical și orizontal, evidențiază diferențele reale, CTA clar.
- **FAQ**: întrebări reale, răspunsuri scurte, ordonate după obiecții.
- **Docs/article**: lizibilitate, cuprins, headinguri clare, exemple și callouts, fără hero-uri decorative mari.
- **Dashboard/app**: grile stabile, controale previzibile, informație densă, fără compoziție de landing page.

## Script de audit

Pentru HTML static:

```bash
node ~/.claude/skills/web-section-composer/scripts/audit-sections-html.mjs path/to/page.html
```

Scriptul verifică semnale obiective: secțiuni fără heading, heading hierarchy ruptă, prea multe CTA-uri, carduri cu texte lungi, imagini fără dimensiuni/alt, carusele, inline style excesiv, butoane generice și secțiuni probabil prea rarefiate.

Scriptul nu judecă gustul vizual. Folosește-l ca plasă de siguranță, apoi fă auditul manual din [audit-checklist.md](references/audit-checklist.md).

## Când citești referințele

- Creezi o pagină întreagă sau alegi ordinea secțiunilor: citește `page-modes.md` și `section-taxonomy.md`.
- Secțiunea pare prea lungă, prea goală sau prea încărcată: citește `density-and-spacing.md`.
- Textul e vag sau greu de scanat: citește `copy-and-hierarchy.md`.
- Lucrezi responsive/mobile: citește `responsive-patterns.md`.
- Faci review sau polish final: citește `audit-checklist.md`.
