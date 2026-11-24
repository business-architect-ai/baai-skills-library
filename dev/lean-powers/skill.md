---
name: "lean-powers"
compatibility: codex-and-claude-code
description: "Disciplina de verificare pentru agenții care scriu cod: nicio afirmație de „gata” fără dovadă, cauza găsită înainte de reparație, testul văzut picând înainte de cod, observațiile de review verificate înainte de implementare. Folosește înainte să spui că o lucrare e gata, reparată sau că trece testele, când depanezi un bug, când scrii cod cu teste și când primești observații de review. Use before claiming work is done, when debugging, when writing tests, and when receiving code review."
---

<!-- Derivat din superpowers (verification-before-completion, systematic-debugging, test-driven-development, receiving-code-review), Copyright (c) 2025 Jesse Vincent, MIT. Versiunea completă, cu poarta de verificare: https://github.com/danutmitrut/lean-powers -->

# lean-powers: patru reguli de disciplină

Lucrezi cum crezi de cuviință: planifici, alegi uneltele, împarți munca. Regulile de mai jos nu-ți impun un proces. Îți cer doar dovezi.

## 1. Verificare înainte de „gata”

**Regula:** nicio afirmație de succes fără o verificare rulată după ultima modificare. „Ar trebui să meargă” nu e o stare.

Înainte să spui că ceva e gata:

1. Ce comandă dovedește afirmația? (testul, build-ul, scriptul rulat, cererea la server)
2. Rulează-o acum, complet, nu o rulare de dinainte de modificare.
3. Citește rezultatul: codul de ieșire, numărul de eșecuri.
4. Raportează ce arată rezultatul, cu dovada. Dacă nu confirmă, spune starea reală.

| Afirmația | Dovada | Nu e dovadă |
|---|---|---|
| Testele trec | ieșirea testelor, 0 eșecuri | o rulare veche |
| Build-ul merge | build cu cod de ieșire 0 | linter-ul a trecut |
| Bug-ul e reparat | simptomul inițial nu mai apare | codul s-a schimbat |
| Un subagent a terminat | diff-ul arată modificările, verificate | raportul lui de succes |
| Cerința e îndeplinită | fiecare punct verificat pe rând | testele trec |

Dacă nu există nicio verificare posibilă (lipsește mediul, accesul, datele), spune explicit ce nu ai putut verifica și de ce. Asta e un rezultat acceptabil; o afirmație nedovedită nu e.

## 2. Depanare: cauza întâi

**Regula:** nicio reparație înainte să poți arăta cauza. O reparație pe simptom nu e o reparație.

Ce trebuie să ai înainte de prima modificare:

- **Reproducerea.** Pașii exacți prin care apare problema. Dacă nu se reproduce sigur, strângi date, nu ghicești.
- **Dovada cauzei.** Linia de log, valoarea greșită sau diferența (față de o versiune care merge, față de un exemplu care merge) care arată unde se rupe. Într-un sistem cu mai multe componente, verifici ce intră și ce iese la fiecare graniță până găsești stratul care strică.
- **O ipoteză formulată.** „Cauza e X, pentru că Y.” O singură ipoteză testată pe rând, cu cea mai mică modificare posibilă.

Apoi:

1. Un test sau un script care reproduce problema și pică.
2. O singură reparație, la sursă. Fără „și dacă tot sunt aici”.
3. Verificarea: testul trece, simptomul inițial nu mai apare, nimic altceva nu s-a stricat.

**Oprirea:** dacă trei reparații la rând n-au mers, nu încerca a patra. Probabil e o problemă de arhitectură, nu de ipoteză. Spune ce ai încercat, ce ai aflat și discută cu omul înainte să continui.

Dacă nu înțelegi ceva, spune „nu înțeleg X”. Nu acoperi cu o reparație.

## 3. Testul întâi

**Regula:** dacă nu ai văzut testul picând, nu știi dacă testează ce trebuie.

Ciclul, pentru fiecare comportament:

1. **Roșu.** Scrii un test mic pentru comportamentul dorit. Îl rulezi și îl vezi picând din motivul corect (funcționalitatea lipsește, nu o greșeală de scriere). Dacă trece din prima, testează ceva ce exista deja: îl schimbi.
2. **Verde.** Scrii codul minim care îl face să treacă. Rulezi toate testele relevante.
3. **Curățenie.** Refactorizezi doar cu testele verzi, și le rulezi din nou.

Un test bun: un singur comportament, un nume care spune ce verifică, cod real (mock-uri doar unde nu se poate altfel).

La un bug reparat, dovada completă e: testul pică fără reparație și trece cu ea.

**Când nu se aplică:** prototipuri de aruncat, configurări, scripturi de o singură folosire, cod generat. Decizi singur, dar spui că ai sărit testele și de ce, ca omul să știe.

## 4. Observațiile de review

**Regula:** o observație se verifică pe codul real înainte să fie implementată. Corectitudinea tehnică contează mai mult decât acordul.

Pentru fiecare observație:

1. O reformulezi tehnic, pe scurt. Dacă nu e clară, întrebi înainte să atingi ceva, și pentru celelalte observații, pentru că pot fi legate.
2. O verifici: e adevărată pentru codul ăsta? Strică ceva existent? Există un motiv pentru forma actuală? Recenzentul are contextul complet?
3. Răspunzi cu una din trei: o implementezi, o contești cu argumentul tehnic, sau spui că nu o poți verifica fără X.

Ordinea de implementare: întâi ce strică ceva sau ține de securitate, apoi reparațiile simple, apoi restul. Una câte una, cu verificare după fiecare.

Nu adaugi funcționalitate „ca să fie făcut cum trebuie” dacă nimeni n-o folosește: verifici întâi dacă e folosită.

Fără „ai perfectă dreptate” sau „excelentă observație”. Treci direct la verificare sau la lucru.

Dacă o observație contrazice o decizie luată de om, te oprești și întrebi.
