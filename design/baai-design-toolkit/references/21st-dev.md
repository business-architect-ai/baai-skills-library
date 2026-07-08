# 21st.dev, magazinul de componente

## Ideea în două fraze

Dacă shadcn îți dă cărămizile, 21st.dev e magazinul unde găsești cărămizi deja lucrate de alții. E un marketplace de componente și template-uri React, din aceeași familie shadcn/Tailwind, unde comunitatea publică piese gata făcute. Se autopromovează ca „npm pentru design engineers", iar mai nou ca „componente care combat AI slop", adică lucrate de oameni, nu generate prost pe bandă.

## Ce rezolvă

Problema pe care o rezolvă e timpul. În loc să construiești un hero, un pricing table sau un dashboard de la zero, cauți unul care arată bine și îl aduci în proiect în câteva secunde. E diferența dintre a turna singur fiecare cărămidă și a lua un perete gata făcut din magazin.

Peste catalogul de componente, 21st a pus și un strat de generare cu AI, care scoate mai multe variante ale aceleiași componente ca să compari și să alegi, în loc să te mulțumești cu prima formă.

## Cele două moduri de folosire

Există două căi, și e bine să le ții separate în cap.

Prima, componente gata făcute din catalog, pe care le aduci în proiect. A doua, prin Magic MCP, un server MCP care conectează agentul tău (Claude Code, Cursor) direct la 21st. Cu MCP-ul activ, ceri în limbaj natural, „generează un hero cu ... în trei variante" sau „caută un pricing table", iar agentul aduce codul și îl pune în proiect fără să ieși din conversație.

## Cum instalezi Magic MCP

Întâi îți iei un API key din consola 21st.dev Magic. Apoi ai două variante.

Varianta rapidă, o singură comandă, funcționează pentru IDE-urile pe care le suportă direct (cursor, windsurf, cline și altele):

```bash
npx @21st-dev/cli@latest install <client> --api-key <cheia-ta>
```

Varianta manuală, care merge oriunde, inclusiv în Claude Code, adaugi serverul în config-ul MCP al clientului:

```json
{
  "mcpServers": {
    "@21st-dev/magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic@latest", "API_KEY=\"cheia-ta\""]
    }
  }
}
```

După ce salvezi, restartezi clientul ca să încarce serverul.

Pentru Claude Code ține minte că one-linerul de mai sus e gândit pentru IDE-urile din listă, nu neapărat pentru Claude Code. La tine folosește config-ul manual, sau comanda `claude mcp` într-o sesiune interactivă. Și, ca la orice, nu lipești cheia în chat și nu modifici config-ul fără acordul cursantului.

## Componente fără MCP

Nu ești obligat să treci prin server ca să iei o componentă. Fiindcă piesele 21st sunt compatibile cu registry-ul shadcn, le poți trage direct cu CLI-ul shadcn:

```bash
npx shadcn@latest add "https://21st.dev/r/<autor>/<componenta>"
```

URL-ul îl iei de pe pagina componentei. Fluxul ăsta aduce codul public al componentei, fără cont și fără MCP, și presupune că proiectul a rulat deja shadcn init.

## Cât costă

Modelul e freemium și e cinstit despre limite:

- căutarea în catalog e gratis
- instalările de componente sunt 2 pe zi pe gratis, nelimitat pe Pro
- generarea cu AI e 30 de credite pe lună pe gratis, nelimitat pe Pro

Pentru un cursant care experimentează, planul gratis e suficient cât să înțeleagă unealta.

## Securitate

API key-ul e un secret, exact ca o parolă. Nu îl lipești în chat, nu îl comiți în git. Îl ții în config local sau în seiful sistemului.

## De reținut

21st.dev stă peste shadcn, nu îl înlocuiește. shadcn e vocabularul, 21st e biblioteca de fraze gata scrise în acel vocabular. Îl folosești când vrei viteză pe o piesă anume, nu când construiești un produs întreg de la zero.

Site: https://21st.dev. Repo CLI: https://github.com/21st-dev/cli.
