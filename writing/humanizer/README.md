# /humanizer — Elimină artefactele AI din text englezesc

Rescrie text englezesc ca să nu mai sune a AI. Acoperă 30 de pattern-uri documentate de Wikipedia (WikiProject AI Cleanup): vocabular AI suprafolosit, em dash-uri, structuri negative paralele, regula celor trei, voice colaborativ de chatbot, hedging excesiv, liste cu header-uri bold și altele.

Procesul are 4 etape: identificare pattern-uri, draft rewrite, audit intern și versiune finală.

## Când îl folosești

- Ai generat text în engleză și vrei să-l faci să sune uman
- Scrii conținut în engleză pentru blog, email, documentație sau social media
- Editezi conținut generat de AI înainte de publicare

## Instalare

Acest skill este de tip plugin:

```bash
mkdir -p ~/.claude/skills/humanizer
cp skill.md ~/.claude/skills/humanizer/SKILL.md
```

Activare în Claude Code: `/humanizer [text sau cale fișier]`
