# Șablonul raportului

Construiești raportul din reacțiile persona. Două reguli:

1. **Ordonezi doar ce au trăit persona.** Nicio frecare inventată, niciun credit pentru părți
   la care n-au ajuns.
2. **Vocea rămâne în carantină.** Termenii de UX și severitățile stau în secțiunile de analiză.
   Citatele persona rămân neșlefuite, în secțiunea lor.

Severitate: **5** = blocaj (n-a putut sau n-a vrut să continue), **4** = majoră,
**3** = enervantă, **2** = minoră, **1** = cosmetică.

---

```markdown
# SUS panel: <ce s-a testat>
**Material:** <URL / fișier> · **Tip:** <interfață / ghid / text de citit> · **Suprafață:** <web / local / text / capturi> · **Data:** <AAAA-LL-ZZ>
**Sarcina dată:** <cu vorbele din briefing>
**Persona:** <nume 1>, <nume 2>, <nume 3> (detalii în `persone/`)

## Pe scurt
<3-4 propoziții: ce spune testul ăsta autorului. Cea mai importantă frecare, câte persona au
ajuns la capăt, scorul (dacă există) cu avertismentul lui.>

## Scor SUS
<Doar pentru interfețe și ghiduri. Copiază tabelul din ieșirea scriptului.>

| Persona | Scor | Notă |
|---|---|---|
| ... | ... | ... |
| **Media** | **...** | **...** |

Împrăștiere: <abaterea standard și intervalul, din script>.

> Scorul e orientativ. Persona sunt simulate de un model de limbaj, care tinde să dea scoruri
> mai mari decât oamenii reali, mai ales pentru un public puțin tehnic. Valoarea testului stă
> în frecările de mai jos, nu în cifră. Media de referință pentru SUS e 68.

## Înțelegere
<Doar pentru text de citit. Mesajul pe care voia autorul să-l transmită, apoi ce a reținut
fiecare persona. Unde se potrivește, unde deviază, unde s-au oprit din citit.>

## Frecări găsite de mai multe persona (încredere mai mare)
- **[S#]** <unde> : <ce s-a întâmplat, în termeni de analiză>. *(<persona care au atins-o>)*

## Frecări găsite de o singură persona
- **[S#]** <unde> : <ce s-a întâmplat>. *(<persona>, <de ce contează pentru profilul ei>)*

## Ce a mers
- <doar lucruri la care persona au reacționat efectiv>

## Recomandări
1. <cea mai importantă, legată de o frecare de mai sus>
2. ...
3. ...

## Cu vorbele lor
**<Persona 1>** (<cât de departe a ajuns>)
> „<citat>”
> „<citat>”
Verdict: <o linie, cu vocea ei>

**<Persona 2>** ...

## Pasul următor
Verifică frecările de severitate 4-5 cu 3-5 oameni reali din public, înainte să le consideri
confirmate.
```
