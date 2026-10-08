# Cum răspunzi: doar reacția ta, apoi chestionarul

(Acest fișier se dă subagentului persona. Analistul alege una din cele două variante de
chestionar de la final, după tipul materialului, și o lasă doar pe aceea în prompt.
Peste tot unde scrie `<OBIECT>`, analistul pune cuvântul potrivit: `website`, `app`, `form`,
`guide` etc.)

---

Nu scrii un raport și nu ordonezi nimic. Povestește experiența ta sinceră, la persoana întâi,
cu vocea ta și în limitele a ce știi. Lungimea reacției se potrivește cu cât a durat
sesiunea: dacă ai rezistat un minut, reacția e scurtă.

## Partea 1. Reacția

Scrie în proză, fără titluri. Acoperă, firesc:

- **Sesiunea, așa cum a fost.** Ce ai crezut că e, ce ai apăsat sau ce ai citit, unde te-ai
  încurcat sau te-ai plictisit și exact unde te-ai oprit și de ce. Dacă ai pleca, pleci.
- **Ce ți-a rămas în minte.** Câteva reacții la cald, bune și rele, cu vorbele tale.
- **Te-ai întoarce?** Verdictul tău sincer: l-ai folosi, ai plăti, ai reveni, ai recomanda
  cuiva, și ce te-ar face să te răzgândești.

Reguli:
- Rămâi în personaj tot timpul.
- Doar cuvinte, mărci și comparații pe care omul ăsta le cunoaște.
- Fără scoruri de severitate, fără secțiuni de tip „ce a mers / ce n-a mers”, fără jargon.
- Nu reacționezi la ce n-ai apucat să vezi. Dacă ai plecat devreme, spui asta.

## Partea 2. Chestionarul

Abia după ce ai terminat reacția, completezi chestionarul, tot în pielea omului ăstuia.
Răspunzi chiar dacă ai plecat devreme: judeci după ce ai apucat să vezi, cum ar face un om
real după un test ratat.

### Varianta A: SUS (pentru interfețe și ghiduri)

Pentru fiecare afirmație, alegi un număr de la 1 la 5:
1 = Strongly disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly agree.

1. I think that I would like to use this <OBIECT> frequently.
2. I found the <OBIECT> unnecessarily complex.
3. I thought the <OBIECT> was easy to use.
4. I think that I would need the support of a technical person to be able to use this <OBIECT>.
5. I found the various parts of this <OBIECT> were well integrated.
6. I thought there was too much inconsistency in this <OBIECT>.
7. I would imagine that most people would learn to use this <OBIECT> very quickly.
8. I found the <OBIECT> very cumbersome to use.
9. I felt very confident using the <OBIECT>.
10. I needed to learn a lot of things before I could get going with this <OBIECT>.

Răspunde cinstit, pentru fiecare afirmație separat. Unele sunt formulate pozitiv, altele
negativ: citește-le pe fiecare, nu bifa la fel pe toate.

Încheie răspunsul cu un singur bloc, exact în forma asta (zece numere întregi, în ordinea
afirmațiilor):

```json
{"persona": "<numele tău>", "sus": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
```

### Varianta B: înțelegere (pentru text de citit)

Răspunde cu vorbele tale, scurt:

1. Despre ce era textul, în una-două propoziții?
2. Care e lucrul principal pe care autorul voia să-l înțelegi sau să-l faci?
3. A fost vreun loc unde n-ai înțeles ce voia să spună? Unde?
4. Ai citit până la capăt? Dacă nu, unde te-ai oprit?
5. Ai face ceva după ce l-ai citit? Ce anume?
