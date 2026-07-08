# Open Design, fabrica

## Ideea în două fraze

Dacă shadcn e cărămida și 21st magazinul, Open Design e fabrica. E o aplicație desktop open-source care îți transformă agentul de cod într-un motor de design complet, nu o bibliotecă de componente. Îi dai un brief, iar el scoate artefacte întregi: prototipuri, landing pages, dashboards, slide-uri, imagini, chiar video HTML.

## Ce e, mai exact

E o aplicație desktop, open-source sub licența Apache-2.0, din repo-ul nexu-io/open-design. Se poziționează explicit ca alternativa open-source și local-first la Claude Design, adică rulează la tine pe mașină, cu cheia ta, nu pe o platformă a altcuiva.

Ideea centrală e „bring your own agent": nu vine cu un model propriu, se conectează la agentul pe care îl ai deja, Claude Code, Codex, Cursor, Gemini, peste 20 de CLI-uri. Agentul devine creierul, Open Design devine atelierul din jurul lui: îi dă direcție vizuală, un design system, un mod de lucru și un loc unde să scoată fișierele.

La final ai fișiere reale, nu doar o previzualizare. Export în HTML, PDF, PPTX și MP4, deci poți duce rezultatul mai departe fie ca sursă de cod, fie ca prezentare, fie ca video.

## Cele două concepte care contează

Ca să înțelegi Open Design, îți trebuie doi termeni ai lor.

design systems sunt fișiere DESIGN.md, un fel de carte de brand pe nouă secțiuni (paletă, tipografie, spacing, layout, componente, motion, voce, brand, anti-patterns). Marele avantaj e că sunt portabile: același DESIGN.md persistă între proiecte și între agenți, deci brandul tău te urmează, nu îl reconstruiești de fiecare dată. Vin în jur de 150 preinstalate (Linear, Stripe, Vercel, Notion, Anthropic și altele), iar unul propriu îl adaugi punând un DESIGN.md în design-systems/<brand>/.

skills sunt, ca structură, foarte apropiate de skill-urile din Claude Code: un folder cu un SKILL.md care descrie un workflow. Le pui în folder, restartezi daemon-ul, apar în picker. Vin peste 100 preinstalate conform README-ului lor (marketingul revendică mai multe, până spre 250, numărul crește în timp).

Dacă structura de skills îți sună cunoscut, e pentru că e aproape identică cu ce construiești tu în Claude Code. Ăsta e și motivul pentru care Open Design e „candidatul de upgrade de huashu": face aceeași idee, dar productizată ca aplicație.

## Cum îl pui la treabă

Varianta simplă și recomandată e aplicația desktop. Descarci installer-ul de pe open-design.ai (macOS pe Apple Silicon și Intel, Windows x64, Linux AppImage). La prima pornire, app-ul detectează singur agenții din PATH și încarcă cele aproximativ 150 de design systems și peste 100 de skills.

Ca să conectezi Claude Code prin MCP:

```bash
od mcp install claude
```

Dacă vrei să vezi ce ar face înainte să scrie ceva, rulezi un dry-run:

```bash
od mcp install claude --print
```

Suportă și alți agenți: codex, cursor, copilot, gemini, opencode, openclaw și alții. Dacă terminalul nu găsește comanda od după instalare, deschide o dată aplicația desktop, ca să pună CLI-ul pe PATH, și reîncearcă.

## Cheia de model

Aici e o subtilitate pe care merită s-o înțelegi. Când conectezi Claude Code cu `od mcp install claude`, Open Design folosește chiar agentul tău Claude Code, deci modelul și cheia pe care le ai deja acolo. Nu reintroduci nimic.

Doar dacă nu ai un agent CLI și vrei să lovești direct un provider intri pe proxy-ul BYOK al lor (/api/proxy/<provider>/stream), unde configurezi baseUrl, apiKey și model. Cheia stă local, nu o lipești în chat. Proxy-ul are și protecție SSRF, blochează implicit adresele interne.

## Câteva comenzi utile

```bash
od skill list --scenario marketing            # skill-uri pe scenariu
od search-files "primary button"              # cauți fișiere
od get-file design-systems/linear-app/DESIGN.md
od plugin run web-prototype --brief "landing page pentru ..."
```

Toate acceptă `--json`, dacă vrei să le legi în automatizări. Ca să vezi ce design systems ai la dispoziție, cel mai simplu e picker-ul din aplicație; din CLI folosești numele folderului (de exemplu linear-app) în comanda get-file.

## Fluxul de lucru, pe scurt

Ciclul lor arată așa: brief, alegi un skill, lockezi o direcție vizuală, alegi un design system, agentul scoate primul artefact, îl dai mai departe ca cod sau export, iar stilurile confirmate devin default pentru sesiunile următoare. Ultima parte, memoria, e ce face ca a doua oară să fie mai rapid decât prima.

## Când merită și când nu

Open Design e alegerea când vrei să generezi de la zero un artefact vizual complet, când vrei un design system consistent între proiecte, sau când vrei să rămâi local și cu cheia ta.

Nu e alegerea pentru o componentă punctuală, acolo folosești shadcn sau 21st. Și, sincer, nu neapărat nici când huashu-design nativ îți rezolvă deja cazul direct în Claude Code, fără să instalezi încă o aplicație. Fabrica merită pornită când chiar ai de fabricat ceva, nu pentru o singură piesă.

## De reținut

Open Design e cel mai aproape, dintre cele trei, de ce faci deja cu huashu: agentul devine motor de design. Diferența e ambalajul, o aplicație desktop cu bibliotecă de stiluri, skills și export multi-format. Pentru self-host mai există și variantă Docker (docker compose up -d, port 7456) sau din sursă, dacă vrei să te joci.

Site: https://open-design.ai. Repo: https://github.com/nexu-io/open-design.
