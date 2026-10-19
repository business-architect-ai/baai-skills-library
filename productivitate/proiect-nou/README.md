# /proiect-nou: proiectul care nu depinde de conversații

Claude Code șterge conversațiile mai vechi de 30 de zile (setarea `cleanupPeriodDays`). Skill-ul pregătește folderul curent astfel încât o sesiune nouă să știe unde ai rămas și ce ai decis, chiar dacă discuțiile vechi nu mai există.

Pune în folder trei lucruri:

1. **`CLAUDE.md`** cu secțiunea „Continuitate”: la fiecare sesiune se citește `DECIZII.md`, iar deciziile se scriu pe loc.
2. **`DECIZII.md`** cu două secțiuni: „Unde am rămas” (maximum 10 rânduri, se rescrie) și „Decizii” (doar crește, câte o linie: „AAAA-LL-ZZ: decizia. Motiv: de ce.”).
3. **git**, doar dacă proiectul are cod, cu un `.gitignore` care exclude `.env`, `*.key` și `node_modules/`.

Nu suprascrie nimic. Pe un proiect existent adaugă doar ce lipsește și îți arată conținutul înainte să scrie.

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

- Pune întrebări una câte una: ce construiești, ce ai decis deja (cu motiv), dacă e cod.
- Nu inventează decizii și nici motive. Unde nu ai spus motivul, scrie „Motiv: nespecificat”.
- Nu face commit fără confirmarea ta.

Face parte din seria „BAAI Claude Cases”, cazul 1 (Cleanup alert).
