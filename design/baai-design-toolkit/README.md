# /baai-design-toolkit — Unelte de design cu AI: shadcn/ui, 21st.dev, Open Design

Te ajută să alegi corect între cele trei unelte de design cu AI și să le folosești, cu router de decizie, comenzi de instalare verificate și reguli de securitate. Se leagă și de huashu-design nativ, ca să nu adaugi o unealtă când nu e nevoie.

## Când îl folosești

- Faci design web sau UI în Claude Code și ai nevoie de componente
- Vrei un design system, sau un prototip, landing, slide sau dashboard generat
- Nu știi care unealtă e potrivită: shadcn/ui, 21st.dev sau Open Design
- Întrebi „ce unealtă de design folosesc", „adaugă componente UI", „de unde iau un design system"

## Ce conține

- `skill.md`, routerul de decizie, tabelul de referință rapidă, regulile de securitate
- `references/shadcn.md`, articol despre shadcn/ui, cărămida
- `references/21st-dev.md`, articol despre 21st.dev, magazinul
- `references/open-design.md`, articol despre Open Design, fabrica

## Instalare

Skill-ul are și fișiere de referință, deci copiezi tot folderul:

```bash
mkdir -p ~/.claude/skills/baai-design-toolkit/references
cp skill.md ~/.claude/skills/baai-design-toolkit/SKILL.md
cp references/*.md ~/.claude/skills/baai-design-toolkit/references/
```

Activare în Claude Code: `/baai-design-toolkit`, sau declanșare naturală când ceri componente UI, un design system sau un prototip.
