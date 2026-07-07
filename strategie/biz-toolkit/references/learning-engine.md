# Learning engine, memorie persistentă per modul

Acest mecanism dă fiecărui modul din biz-toolkit o memorie care persistă între sesiuni. Scopul: modulul nu repetă greșeli corectate și nu re-întreabă ce a aflat deja.

`[MODUL]` de mai jos înseamnă rădăcina modulului curent (ex. `pricing`, `funnel`, `review`). Fișierul de memorie este întotdeauna `~/.claude/skill-memory/biz-[MODUL].md`.

---

## La START (înainte de orice altceva)

1. **Citește contextul afacerii** din `~/.claude/skill-memory/business-context.md` (comun tuturor modulelor).
   - Dacă fișierul nu există, creează-l copiind structura din `templates/business-context-template.md`.
   - Aplică faptele durabile de acolo (ce vinde, cine e clientul, stadiul, obiectivul) ca fundal al discuției. Nu re-întreba ce e deja completat; dacă un câmp relevant pentru modulul curent lipsește, întreabă-l o dată și salvează-l acolo, nu în memoria modulului.

2. **Citește memoria modulului** din `~/.claude/skill-memory/biz-[MODUL].md`.
   - Dacă fișierul nu există, creează-l copiind structura din `templates/memory-template.md`.
   - Dacă există, încarcă toate secțiunile și aplică-le în sesiunea curentă.

3. **Afișează gotchas active** (dacă sunt):
   ```
   Am învățat din sesiunile anterioare:
   - [gotcha 1]
   - [gotcha 2]
   Aplic automat. Spune-mi dacă ceva s-a schimbat.
   ```

---

## GOTCHA ENGINE (în timpul interacțiunii)

Monitorizează continuu semnalele de corecție.

**Semnale explicite** (acțiune imediată): „nu", „nu așa", „greșit", „schimbă", „fă altfel", „rescrie", „ți-am zis", „din nou", ori orice reformulare a output-ului tău.

**Semnale implicite** (înregistrează, cere confirmare): utilizatorul editează manual output-ul, ignoră o parte și folosește doar restul, sau repetă o instrucțiune.

La detectarea unei corecții:

1. **Recunoaște scurt**, fără scuze lungi: „Am prins. [ce am greșit] -> [ce trebuia]."
2. **Aplică imediat** în sesiunea curentă.
3. **Salvează în GOTCHAS**:
   ```
   - [DATA] | [comportament greșit] -> [comportament corect] | SURSĂ: corecție user
   ```
4. **Marchează recurența**: dacă un gotcha similar există deja, notează-l RECURENT (x3) și afișează-l la fiecare start.

Reguli gotcha:
- Un gotcha salvat = regulă permanentă. Nu-l ignora niciodată.
- Gotchas recurente (3+) devin reguli critice, afișate la fiecare start.
- Când un gotcha contrazice o instrucțiune nouă explicită, instrucțiunea nouă câștigă și gotcha-ul se actualizează.

---

## LEARNING LOOP (la finalul interacțiunii)

Rulează intern acest checklist:

```
1. Am primit corecții?        -> salvează în GOTCHAS
2. Am descoperit preferințe?  -> salvează în PREFERINȚE ÎNVĂȚATE
3. Ce a funcționat bine?      -> salvează în PATTERNS DE SUCCES
4. Ce nu a funcționat?        -> salvează în ANTI-PATTERNS
5. Context nou relevant?      -> salvează în CONTEXT ACUMULAT
6. Actualizează METRICI (sesiuni, streak, ultima corecție)
```

Apoi scrie fișierul `~/.claude/skill-memory/biz-[MODUL].md` cu secțiunile actualizate și `ultima_actualizare: [DATA]`.

---

## Reguli de aur

1. **Nu inventa gotchas.** Doar ce a corectat utilizatorul explicit.
2. **Nu presupune preferințe.** Doar ce a confirmat sau a acceptat fără obiecție de 3+ ori.
3. **Memoria bate presupunerile.** Dacă memoria spune X și instinctul spune Y, urmează memoria.
4. **Verifică înainte de aplicare.** Memoria poate fi depășită. Dacă ceva pare ciudat: „Știu că preferai [X]. E încă valabil?".
5. **Transparență.** La cererea „ce ai învățat?", dă raportul complet din memorie.
6. **Zero pierdere.** Nicio corecție și nicio preferință confirmată nu se uită.
7. **Fapte durabile în context comun.** Ce vinde utilizatorul, cine e clientul lui, stadiul și obiectivul afacerii merg în `business-context.md` (comun tuturor modulelor), nu în memoria modulului. În memoria modulului stau doar corecțiile și preferințele specifice acelui modul.
