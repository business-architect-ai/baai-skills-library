# /ro-humanizer — Elimină artefactele AI din text românesc

Rescrie textul dat ca să nu mai sune a AI. Nu adaugă voce personală, ci elimină pattern-urile detectabile: cuvinte-semnal, deschideri toxice, hedging excesiv, antiteze false, calcuri din engleză, topică nefirească. Bazat pe date din 3,3M texte analizate cu GPTZero și cercetare NLP 2024-2025.

Procesul are 4 etape: scanare, draft rewrite, audit intern ("ce mai sună a AI?") și versiune finală.

## Când îl folosești

- Ai generat un text cu Claude sau alt AI și vrei să-l faci să sune uman
- Scrii conținut în română pentru social media, email sau pagini web
- Vrei să înveți ce pattern-uri sunt specifice textului AI

## Instalare

Acest skill este de tip plugin. Instalare diferită față de skillurile de tip comandă:

```bash
mkdir -p ~/.claude/skills/ro-humanizer
cp skill.md ~/.claude/skills/ro-humanizer/SKILL.md
```

Activare în Claude Code: `/ro-humanizer [text sau cale fișier]`
