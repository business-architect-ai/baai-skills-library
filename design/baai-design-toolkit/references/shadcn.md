# shadcn/ui, cărămida pe care se construiește tot

## Ideea în două fraze

shadcn/ui e o colecție de componente React (butoane, formulare, dialoguri, meniuri, tabele) construite pe Radix UI, care se ocupă de accesibilitate și comportament, plus Tailwind CSS, care se ocupă de stilizare. Ce o face specială e cum ți-o dă: nu instalezi un pachet, copiezi codul direct în proiectul tău.

## De ce e altfel decât ce știai

Când folosești o librărie clasică gen Material UI sau Chakra, tragi un pachet npm închis. Componenta trăiește în node_modules, tu îi dai doar niște props și speri că se lasă stilizată cum vrei. Când vrei să schimbi ceva ce autorul n-a prevăzut, te lovești de un zid.

shadcn întoarce logica pe dos. Rulezi o comandă, iar codul componentei se copiază fizic în folderul tău, de obicei în components/ui/. Din secunda aia, componenta e a ta. O deschizi, o citești, o modifici linie cu linie. Nu mai există cutie neagră. Filozofia lor exactă e „open code", nu „closed library".

Compromisul e simplu de înțeles: câștigi control total, dar pierzi update-urile automate. Dacă autorul îmbunătățește un buton peste trei luni, la tine nu ajunge singur, pentru că butonul tău e deja copiat și eventual modificat. Pentru majoritatea proiectelor, controlul valorează mai mult decât update-ul automat.

## De ce contează pentru tine

shadcn a devenit standardul de facto în ecosistemul React, fundația peste care se construiește aproape tot ce apare nou în zona de componente, inclusiv 21st.dev din acest toolkit. Dacă înveți shadcn, înțelegi vocabularul comun al întregului ecosistem.

Recent au adăugat suport și pentru Base UI pe lângă Radix, deci nu ești legat rigid de o singură fundație. Radix nu e abandonat, fiecare componentă vine în ambele variante.

## Cum îl folosești

Package-ul se numește shadcn (nu shadcn-ui, ăla e numele vechi).

Prima dată, o singură dată pe proiect, îl inițializezi. Comanda asta îți setează Tailwind, variabilele de temă și structura de foldere:

```bash
npx shadcn@latest init
```

(dacă folosești alt package manager: `pnpm dlx shadcn@latest init` sau `bunx --bun shadcn@latest init`)

De aici încolo adaugi doar ce ai nevoie, componentă cu componentă:

```bash
npx shadcn@latest add button
npx shadcn@latest add dialog form table
```

Fiecare comandă copiază codul în components/ui/, de unde îl poți edita cum vrei.

## Componente din alte surse, inclusiv 21st.dev

CLI-ul nu e limitat la catalogul oficial. Acceptă un nume, un URL sau o cale locală. Asta înseamnă că poți trage o componentă publicată în orice registry compatibil, direct prin link:

```bash
npx shadcn@latest add "https://21st.dev/r/<autor>/<componenta>"
```

Așa aduci o componentă de pe 21st.dev fără să configurezi niciun server MCP. URL-ul îl copiezi de pe pagina componentei. Singura condiție e să fi rulat deja init în proiect, pentru că add are nevoie de fișierul components.json creat atunci.

## Când e alegerea potrivită

shadcn e răspunsul când ești deja într-un proiect React sau Next.js cu Tailwind și vrei componente pe care le controlezi complet. E și baza bună când vrei o structură consistentă de variabile CSS peste tot în proiect.

Nu e răspunsul dacă nu ești pe React/Tailwind, sau dacă vrei un prototip vizual generat de la zero. Pentru generare de la zero ai Open Design sau huashu-design, nu o bibliotecă de componente.

## De reținut

Cu shadcn iei cărămizile în mână. Le întreții tu, ăsta e costul. În schimb, nimic nu-ți mai e ascuns.

Docs oficiale: https://ui.shadcn.com. Referință CLI: https://ui.shadcn.com/docs/cli.
