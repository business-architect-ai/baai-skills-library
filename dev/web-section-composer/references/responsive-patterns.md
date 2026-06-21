# Responsive Patterns

Mobile este testul de adevăr pentru densitate. Dacă secțiunea devine lungă, confuză sau repetitivă pe mobil, compoziția nu este matură.

## Reguli generale

- Nu scala fonturile cu viewport width. Folosește dimensiuni stabile și breakpointuri.
- Nu lăsa două coloane să devină o coloană cu imagine decorativă uriașă înaintea textului important.
- Pe mobile, ordinea trebuie să urmeze înțelegerea: heading, explicație, acțiune, apoi media dacă media nu este esențială.
- Dacă media este produsul, poate veni înaintea textului, dar CTA-ul trebuie să rămână aproape.
- CTA-urile trebuie să fie ușor de atins și să nu se înghesuie.
- Grilele de carduri trebuie să aibă carduri de înălțime rezonabilă.

## Patternuri

### Two-column section

Desktop:
- text + media
- media + text dacă fluxul paginii are nevoie de variație

Mobile:
- text înaintea media dacă textul explică
- media înaintea textului dacă media este produsul/rezultatul
- evită alternanța mecanică care produce ordine ciudată

### Feature grid

Desktop:
- 3 coloane pentru 3-6 itemuri
- 2 coloane pentru itemuri cu text mai lung

Mobile:
- 1 coloană
- text scurt
- icon mic
- fără imagini decorative per card dacă împing conținutul prea jos

### Process

Desktop:
- timeline sau pași în carduri

Mobile:
- listă verticală numerotată
- pași scurți
- conectoare subtile, nu elemente decorative mari

### Pricing

Desktop:
- 2-4 planuri în coloane

Mobile:
- plan recomandat primul sau după planul de bază, în funcție de strategie
- diferențe clare
- CTA vizibil pe fiecare plan

### FAQ

Desktop:
- 1-2 coloane, dacă întrebările sunt scurte

Mobile:
- o coloană
- accordion doar dacă lista este lungă
- răspunsuri scurte

### Dashboard

Desktop:
- densitate mare, tabele, filtre, comparații

Mobile:
- prioritizează taskurile principale
- transformă tabelele complexe în liste, cards funcționale sau scroll orizontal explicit

## Greșeli frecvente

- Hero full-screen pe mobile cu H1 lung și imagine mare.
- Carduri egale vizual, dar cu conținut foarte diferit.
- CTA secundar la fel de puternic ca CTA principal.
- Secțiuni cu padding vertical identic indiferent de conținut.
- Imagini de 16:9 care devin prea mici pentru detalii importante pe mobil.
