# /web-section-composer — Compoziție secțiuni web

Compune, repară și auditează secțiuni de pagini web pentru claritate, ierarhie vizuală, densitate eficientă, responsive design, text scanabil și folosire corectă a imaginilor.

## Când îl folosești

- Construiești sau refaci secțiuni de landing page
- Vrei un hero mai clar și mai eficient ca spațiu
- Repari secțiuni de beneficii, features, proces, pricing, FAQ sau testimoniale
- Lucrezi la pagini SaaS, ecommerce, servicii, articole, documentație, portofolii sau dashboard-uri
- Auditezi o pagină ca să vezi ce e neclar, prea lung, prea decorativ sau greu de scanat pe mobil

## Ce face

- Decide jobul fiecărei secțiuni: orientare, explicare, convingere, dovadă, comparație sau acțiune
- Alege densitatea potrivită: compact, standard sau immersive
- Verifică dacă spațiul consumat este justificat de conținut
- Evită carduri inutile, hero-uri enorme fără conținut, CTA-uri multiple egale și carusele pentru informație critică
- Separă regulile pentru LP, SaaS, ecommerce, docs, articole, portofoliu și dashboard/app UI
- Include referințe pentru taxonomie de secțiuni, moduri de pagină, densitate, responsive, copy și audit
- Include script de audit HTML pentru semnale obiective

## Instalare

```bash
mkdir -p ~/.claude/skills/web-section-composer
cp skill.md ~/.claude/skills/web-section-composer/SKILL.md
cp -R references ~/.claude/skills/web-section-composer/
cp -R scripts ~/.claude/skills/web-section-composer/
cp -R agents ~/.claude/skills/web-section-composer/
chmod +x ~/.claude/skills/web-section-composer/scripts/audit-sections-html.mjs
```

## Audit automat

După instalare, poți verifica un fișier HTML static cu:

```bash
node ~/.claude/skills/web-section-composer/scripts/audit-sections-html.mjs path/to/page.html
```

Scriptul verifică semnale precum secțiuni fără heading, heading hierarchy ruptă, prea multe CTA-uri, CTA-uri generice, prea multe carduri, text lung în carduri, imagini fără `width`/`height`/`alt`, carusele, inline style excesiv și carduri puse în alte carduri.

## Recomandare

Folosește împreună cu `/imagini-web-lp` când pagina conține imagini sau video. `web-section-composer` decide compoziția secțiunii, iar `imagini-web-lp` verifică media.
