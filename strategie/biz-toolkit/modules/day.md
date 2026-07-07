# Ritual de dimineață, primești contextul business-ului tău înainte să începi ziua

Rulezi dimineața.

## Memorie
Înainte de prima întrebare, aplică learning engine-ul (vezi `references/learning-engine.md`) cu fișierul `~/.claude/skill-memory/biz-day.md`: citește gotchas și preferințele salvate și aplică-le. La finalul interacțiunii, actualizează memoria.

## Proces

### 1. Prioritățile zilei

Întreabă:
- "Care sunt cele 3 lucruri cele mai importante pentru azi?"

Dacă userul are context salvat (skill-memory), propune pe baza lui:
```
PRIORITĂȚI SUGERATE (din ce știu):
1. [prioritate din context anterior]
2. [prioritate]
3. [prioritate]

Se potrivesc? Schimbă ce vrei.
```

### 2. KPIs rapizi

Întreabă (doar prima dată, apoi ține minte):
- "Ce metrici urmărești zilnic/săptămânal? (revenue, useri, conversii, etc.)"
- "Unde le găsesc? (link dashboard, fișier, sau îmi spui tu cifrele)"

Afișează:
```
KPIs:
- [Metrica 1]: [valoare] [trend: sus/jos/stabil]
- [Metrica 2]: [valoare] [trend]
- [Metrica 3]: [valoare] [trend]
```

Dacă nu are dashboard, întreabă cifrele direct și salvează trendul în memorie.

### 3. Follow-ups și deadlines

```
FOLLOW-UPS (ce ai promis cuiva):
- [persoana], [ce], [deadline]

DEADLINES APROPIATE:
- [ce], [când]
```

Ia din skill-memory, sau întreabă.

### 4. Toolkit business

Afișează ÎNTOTDEAUNA:

```
TOOLKIT BUSINESS

STRATEGIE                                OPERAȚIUNI                                MARKETING
cere-mi un diagnostic de business        cere-mi un audit de procese              cere-mi analiza avatarului de client
cere-mi un framework de decizie          cere-mi pregătirea unei ședințe          cere-mi analiza de funnel
cere-mi o analiză de competitori         cere-mi procesarea notelor post-ședință  cere-mi copy pe vocea brandului
cere-mi un review de preț                cere-mi o retrospectivă săptămânală      cere-mi planificarea unei campanii
cere-mi un review de prezentare                                                    cere-mi construirea unei oferte

RAPID: decizii (cere-mi un framework de decizie) | prezentări (cere-mi un review de prezentare) | texte (cere-mi copy)
```

### 5. Direcție

```
---
Bună dimineața! Cu ce începem?
```

## Reguli
- Dacă e prima rulare, colectează context și salvează în memorie.
- De la a doua rulare, nu mai întreba ce a răspuns deja. Confirmă și mergi.
- Tonul: energic, scurt, orientat spre acțiune.
- Nu fi coach motivațional. Fi pragmatic.
