# /proiect-nou: proiectul care nu depinde de conversații

Claude Code șterge conversațiile mai vechi de 30 de zile (setarea `cleanupPeriodDays`), iar un proiect care stă doar pe discul tău se pierde odată cu discul. Skill-ul pregătește folderul curent astfel încât o sesiune nouă să știe unde ai rămas și ce ai decis, chiar dacă discuțiile vechi nu mai există, și îți oferă o copie privată pe GitHub.

Pune în folder:

1. **`CLAUDE.md`** cu trei secțiuni: „Continuitate” (la fiecare sesiune se citește `DECIZII.md`, iar deciziile se scriu pe loc), „Chei” (cheile stau în Keychain pe Mac sau în SecretStore pe Windows, niciodată în fișierele proiectului) și „Salvare” (commit la final de etapă, plus push dacă ai copie pe GitHub).
2. **`DECIZII.md`** cu două secțiuni: „Unde am rămas” (maximum 10 rânduri, se rescrie) și „Decizii” (doar crește, câte o linie: „AAAA-LL-ZZ: decizia. Motiv: de ce.”).
3. **git**, propus pentru orice proiect (cod sau documente), doar dacă spui da, cu un `.gitignore` care exclude întotdeauna `.env`, cheile, `.DS_Store` și, după caz, dependențele, build-urile și datele brute.
4. **O copie privată pe GitHub**, la cerere: repo privat, creat și legat de folder, cu primul push verificat.

Nu suprascrie nimic. Pe un proiect existent adaugă doar ce lipsește și îți arată conținutul înainte să scrie.

Dacă numele folderului are spații sau diacritice, te avertizează la început și îți propune un nume scurt, cu cratimă: mai târziu, redenumirea rupe legătura cu sesiunile.

## Când îl folosești

- Pornești un proiect nou și vrei să nu depinzi de istoricul conversațiilor.
- Ai un proiect vechi în care deciziile stau doar în conversații.
- După ce ai pierdut conversații și vrei să nu se mai repete.

Nu se folosește în folderul unui agent (are `IDENTITY.md` și `SOUL.md`; agenții au memoria lor) și nici în folderul de acasă.

## Instalare Claude Code

**Mac:**

```bash
mkdir -p ~/.claude/skills/proiect-nou
cp productivitate/proiect-nou/skill.md ~/.claude/skills/proiect-nou/SKILL.md
```

**Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\proiect-nou"
Copy-Item productivitate\proiect-nou\skill.md "$HOME\.claude\skills\proiect-nou\SKILL.md"
```

Activare: deschizi Claude Code în folderul proiectului și scrii `/proiect-nou`.

## Cum verifici că a mers

Testul sesiunii goale: `/clear` (sau o sesiune nouă în același folder), apoi întrebi „Unde am rămas în proiectul ăsta și ce am decis?”. Răspunsul trebuie să vină din `DECIZII.md`.

## Ce face și ce nu face

- Pune întrebări una câte una: ce construiești, ce ai decis deja (cu motiv), dacă vrei git, dacă vrei copie pe GitHub.
- La un proiect în lucru, caută întâi singur deciziile în conversațiile existente ale folderului și în memoria automată a proiectului, apoi ți le dă spre confirmare. Nicio decizie găsită nu intră în fișier fără acordul tău.
- Nu inventează decizii și nici motive. Unde nu ai spus motivul, scrie „Motiv: nespecificat”.
- Nu face commit sau push fără confirmarea ta și nu creează repo-uri publice.
- Nu deschide și nu afișează fișiere cu chei. Dacă găsește un `.env`, se asigură că nu intră în git și îți propune mutarea cheilor în seif.
- Pentru GitHub folosește `gh` (GitHub CLI). Dacă nu e instalat, îți dă comanda pentru Mac sau Windows; autentificarea (`gh auth login`) o faci tu.

Face parte din seria „BAAI Claude Cases”, cazul 1 (Cleanup alert).
