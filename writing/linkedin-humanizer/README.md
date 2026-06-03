# /linkedin-humanizer — Elimină semnele AI din orice draft LinkedIn

Rescrie orice text pentru a elimina semnele AI folosind un sistem în 3 tiere (forensic / strict / aesthetic). Include modul `--mode audit` pentru review pass-fail fără rescriere.

## Când îl folosești

- Înainte să publici orice postare sau comentariu scris cu AI
- Review pre-publicare al unui draft finalizat (modul audit)
- Când un draft "pare off" și nu poți identifica exact de ce

## Moduri de utilizare

```
linkedin-humanizer <text>                   # forensic + strict (recomandat)
linkedin-humanizer --mode forensic <text>   # minimum-touch
linkedin-humanizer --mode strict <text>     # + corporate-speak
linkedin-humanizer --mode aesthetic <text>  # + stilistice
linkedin-humanizer --mode audit <text>      # doar detectare, fără rescriere
```

## Instalare

Acest skill este de tip plugin:

```bash
mkdir -p ~/.claude/skills/linkedin-humanizer
cp skill.md ~/.claude/skills/linkedin-humanizer/SKILL.md
```

## Sursă

Adaptat din [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) — MIT License.
